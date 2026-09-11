#!/usr/bin/env python3
"""
whiteboard_server.py — Teacher 2.0 Studio: the one-window interactive tutor surface
(design: ../whiteboard.md).

ONE app window (launched chrome/edge --app mode, no browser chrome) holding the whole
interaction: the lesson stream (teacher blocks: dialogue, math, maps, plots, images), a chat
input (learner types), a sketch pad (learner draws), and a camera/paste/drop intake (learner
photographs their notebook / pastes screenshots). Everything the learner produces lands as a
file + an event the engine long-polls for — so the engine and the learner hold a real
one-on-one loop *inside the window*.

Stdlib-only local server, 127.0.0.1:8471. Session state (blocks + learner events) is rewritten
to session.json on every change — an abrupt exit loses nothing; a same-day restart resumes.

HTTP surface:
  GET  /            the CANVAS studio (v3: one shared Excalidraw whiteboard — teacher content
                    lands ON the board; learner draws/types over it; Ask snapshots the board)
  GET  /classic     the v2 stream layout (fallback)
  GET  /canvas      saved canvas scene       POST /scene   autosave canvas {elements, files}
  GET  /events      SSE stream               GET /files/<f> serve session files
  GET  /status      session + last_event     GET /inbox?after=N&timeout=S  long-poll learner events
  POST /push        teacher block            POST /image   {url|path|b64, source, caption}
  POST /ask         {text, png(board snapshot), via} -> "ask" event (canvas mode's channel)
  POST /msg         learner chat text        POST /capture {png,label,via}
  POST /sketch      {png,label}              POST /session {subject,unit}   POST /export {}
"""
import argparse
import base64
import datetime
import json
import os
import queue
import shutil
import sys
import threading
import urllib.request

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render_lesson import _slugify, CDN  # same pinned CDN stack + slug rules as static lessons

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_PORT = 8471
FIGURE_TYPES = {"map", "process", "table", "plot", "structural", "timing", "image"}


# ----------------------------------------------------------------------------- the board (state)
class Board:
    """One studio session: subject+date, block log, learner-event inbox, SSE listeners."""

    def __init__(self, subject, unit=None, root=None):
        self.subject = subject
        self.unit = unit
        self.date = datetime.date.today().isoformat()
        self.root = root or REPO_ROOT
        seg = [_slugify(s) for s in str(subject).replace("\\", "/").split("/") if s.strip()]
        self.dir = os.path.join(self.root, "subjects", *seg, "whiteboard", self.date)
        os.makedirs(self.dir, exist_ok=True)
        self.path = os.path.join(self.dir, "session.json")
        self.lock = threading.Lock()
        self.event_cv = threading.Condition(self.lock)
        self.listeners = []          # queue.Queue per connected SSE client
        self.blocks = []             # [{"id":n,"fig":m|None,"block":{...},"orig":{...}}]
        self.fig = 0
        self.events = []             # learner inbox: [{"id":n,"kind":...,"time":...,...}]
        if os.path.exists(self.path):
            try:
                saved = json.load(open(self.path, encoding="utf-8"))
                self.blocks = saved.get("blocks", [])
                self.fig = saved.get("fig", 0)
                self.events = saved.get("events", [])
                self.unit = self.unit or saved.get("unit")
            except Exception:
                pass  # corrupt session file -> fresh in memory; next save rewrites it

    def _save(self):
        json.dump({"subject": self.subject, "unit": self.unit, "date": self.date,
                   "fig": self.fig, "blocks": self.blocks, "events": self.events},
                  open(self.path, "w", encoding="utf-8"), indent=1)

    def _broadcast(self, msg):
        for q in list(self.listeners):
            q.put(msg)

    # ---- teacher -> board ------------------------------------------------------------------
    def _process(self, block):
        """Server-side rendering for the two Python primitives (same path as render_lesson)."""
        t = block.get("type")
        if t in ("plot", "structural"):
            from make_figure import make_figure, NoStructuralRenderer
            fig = dict(block.get("figure", {}))
            if t == "plot" and not fig.get("kind"):
                fig["kind"] = "matplotlib"
            try:
                out = dict(block)
                out["svg"] = make_figure(fig)
                return out
            except NoStructuralRenderer as e:
                fb = block.get("fallback") or {"type": "prose", "md": "*[no figure]*"}
                out = self._process(dict(fb))
                out["note"] = (f"No structural renderer registered for subject '{e.subject}' — "
                               f"fell back ({fb.get('type')}).")
                out["caption"] = block.get("caption")
                return out
        return dict(block)

    def add_block(self, block):
        processed = self._process(block)
        with self.lock:
            bid = len(self.blocks) + 1
            fig = None
            if processed.get("type") in FIGURE_TYPES:
                self.fig += 1
                fig = self.fig
            entry = {"id": bid, "fig": fig, "block": processed, "orig": block}
            self.blocks.append(entry)
            self._save()
            self._broadcast({"kind": "block", **{k: entry[k] for k in ("id", "fig", "block")}})
        return bid, fig

    def add_image(self, source, caption=None, url=None, path=None, b64=None, filename=None):
        """Sourced OR generated image -> the board. `source` says where it came from — a citation
        for downloads, 'generated: <how>' for engine-made imagery (whiteboard.md §5)."""
        if not source or not str(source).strip():
            raise ValueError("image blocks need 'source' — a citation, or 'generated: <how>'")
        if url:
            name = filename or _slugify(os.path.basename(url.split("?")[0])) or "image"
            if "." not in name:
                name += ".png"
            fname = f"img-{name}"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (ece-studio)"})
            with urllib.request.urlopen(req, timeout=30) as r, \
                    open(os.path.join(self.dir, fname), "wb") as f:
                shutil.copyfileobj(r, f)
        elif path:
            fname = "img-" + os.path.basename(path)
            shutil.copyfile(path, os.path.join(self.dir, fname))
        elif b64:
            fname = f"img-{filename or 'image.png'}"
            with open(os.path.join(self.dir, fname), "wb") as f:
                f.write(base64.b64decode(b64))
        else:
            raise ValueError("add_image needs one of url / path / b64")
        return self.add_block({"type": "image", "file": fname, "source": source, "caption": caption})

    # ---- learner -> engine (the inbox) -------------------------------------------------------
    def _add_event(self, kind, **fields):
        with self.event_cv:
            eid = len(self.events) + 1
            ev = {"id": eid, "kind": kind,
                  "time": datetime.datetime.now().strftime("%H:%M:%S"), **fields}
            self.events.append(ev)
            self._save()
            self.event_cv.notify_all()
        return ev

    def learner_msg(self, text, via="typed"):
        self.add_block({"type": "learner", "md": text})       # shows in the stream
        return self._add_event("msg", text=text, via=via)     # via: typed | voice (ASR — read
        # voice text tolerantly: technical terms mis-transcribe, e.g. "assign" -> "a sign")

    def _save_png(self, png_b64, prefix, label=""):
        if "," in png_b64:
            png_b64 = png_b64.split(",", 1)[1]
        stamp = datetime.datetime.now().strftime("%H%M%S")
        slug = ("-" + _slugify(label)) if label else ""
        fname = f"{prefix}-{stamp}{slug}.png"
        with open(os.path.join(self.dir, fname), "wb") as f:
            f.write(base64.b64decode(png_b64))
        return fname

    def learner_sketch(self, png_b64, label=""):
        fname = self._save_png(png_b64, "sketch", label)
        self.add_block({"type": "image", "file": fname, "source": "learner sketch",
                        "caption": f"Your sketch{' — ' + label if label else ''}"})
        return self._add_event("sketch", file=fname, label=label,
                               path=os.path.join(self.dir, fname))

    def learner_capture(self, png_b64, label="", via="camera"):
        fname = self._save_png(png_b64, "capture", label)
        self.add_block({"type": "image", "file": fname, "source": f"learner capture ({via})",
                        "caption": f"Your {via}{' — ' + label if label else ''}"})
        return self._add_event("capture", file=fname, label=label, via=via,
                               path=os.path.join(self.dir, fname))

    def learner_ask(self, text="", png_b64="", via="typed"):
        """Canvas mode: the learner asks with the BOARD as context — text (may be empty) + a PNG
        snapshot of the whole annotated canvas. The engine Reads the PNG to see their ink."""
        path = None
        if png_b64:
            fname = self._save_png(png_b64, "board")
            path = os.path.join(self.dir, fname)
        if text:
            self.add_block({"type": "learner", "md": text})    # dialogue stays on the record
        return self._add_event("ask", text=text, path=path, via=via)

    # canvas scene persistence (elements + files), separate from the block log
    @property
    def canvas_path(self):
        return os.path.join(self.dir, "canvas.json")

    def save_scene(self, scene):
        with self.lock:
            json.dump(scene, open(self.canvas_path, "w", encoding="utf-8"))

    def load_scene(self):
        if os.path.exists(self.canvas_path):
            try:
                return json.load(open(self.canvas_path, encoding="utf-8"))
            except Exception:
                pass
        return {"elements": [], "files": {}}

    def wait_events(self, after, timeout):
        """Long-poll: learner events with id > after, waiting up to `timeout` seconds."""
        deadline = datetime.datetime.now().timestamp() + timeout
        with self.event_cv:
            while True:
                new = [e for e in self.events if e["id"] > after]
                if new:
                    return new
                remain = deadline - datetime.datetime.now().timestamp()
                if remain <= 0:
                    return []
                self.event_cv.wait(timeout=min(remain, 5))

    # ---- lifecycle ---------------------------------------------------------------------------
    def export_lesson(self):
        """Freeze the session into a normal dated static lesson (render_lesson.save_lesson)."""
        from render_lesson import save_lesson
        spec = {"title": f"Whiteboard session {self.date}", "subject": self.subject,
                "sections": [{"heading": None, "blocks": []}]}
        if self.unit:
            spec["unit"] = self.unit
        for e in self.blocks:
            b = dict(e["orig"])
            t = b.get("type")
            if t == "image":
                b["file"] = os.path.join(self.dir, b["file"])
            elif t in ("learner", "say"):                  # dialogue -> prose in the archive
                who = "You" if t == "learner" else "Teacher"
                b = {"type": "prose", "md": f"**{who}:** " + b.get("md", "")}
            spec["sections"][0]["blocks"].append(b)
        return save_lesson(spec, concept=f"whiteboard-{self.date}", open_browser=False,
                           root=self.root)


BOARD = None
BOARD_LOCK = threading.Lock()


def set_board(subject, unit=None, root=None):
    global BOARD
    with BOARD_LOCK:
        BOARD = Board(subject, unit, root)
    return BOARD


# ----------------------------------------------------------------------------- HTTP handler
class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):
        pass

    def _json(self, obj, code=200):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _body(self):
        n = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(n).decode("utf-8")) if n else {}

    def _page(self, html_text):
        body = html_text.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        u = urlparse(self.path)
        if u.path == "/":
            self._page(PAGE_CANVAS)          # the shared-canvas Studio (v3, default)
        elif u.path == "/classic":
            self._page(PAGE)                 # the v2 stream layout, kept as fallback
        elif u.path == "/canvas":
            self._json(BOARD.load_scene())
        elif u.path == "/status":
            b = BOARD
            self._json({"ok": True, "subject": b.subject, "unit": b.unit, "date": b.date,
                        "dir": b.dir, "n_blocks": len(b.blocks),
                        "last_event": b.events[-1]["id"] if b.events else 0,
                        "events": b.events[-20:]})
        elif u.path == "/inbox":
            q = parse_qs(u.query)
            after = int(q.get("after", ["0"])[0])
            timeout = min(float(q.get("timeout", ["60"])[0]), 570)
            evs = BOARD.wait_events(after, timeout)
            self._json({"ok": True, "events": evs,
                        "last": evs[-1]["id"] if evs else after})
        elif u.path == "/events":
            self._sse()
        elif u.path.startswith("/vendor/"):
            name = os.path.basename(u.path[len("/vendor/"):])
            fp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vendor", name)
            if not os.path.isfile(fp):
                self._json({"ok": False, "error": "vendor file missing"}, 404)
                return
            data = open(fp, "rb").read()
            self.send_response(200)
            self.send_header("Content-Type", "application/javascript; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "max-age=86400")
            self.end_headers()
            self.wfile.write(data)
        elif u.path.startswith("/files/"):
            name = os.path.basename(u.path[len("/files/"):])
            fp = os.path.join(BOARD.dir, name)
            if not os.path.isfile(fp):
                self._json({"ok": False, "error": "not found"}, 404)
                return
            ext = os.path.splitext(fp)[1].lower()
            ctype = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
                     ".svg": "image/svg+xml", ".gif": "image/gif", ".webp": "image/webp",
                     ".json": "application/json"}.get(ext, "application/octet-stream")
            data = open(fp, "rb").read()
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        else:
            self._json({"ok": False, "error": "unknown path"}, 404)

    def _sse(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "keep-alive")
        self.end_headers()
        q = queue.Queue()
        b = BOARD
        with b.lock:                                   # atomic replay-then-subscribe
            replay = [{"kind": "block", **{k: e[k] for k in ("id", "fig", "block")}}
                      for e in b.blocks]
            b.listeners.append(q)
        try:
            self._send_event({"kind": "hello", "subject": b.subject, "unit": b.unit,
                              "date": b.date})
            for msg in replay:
                self._send_event(msg)
            while True:
                try:
                    self._send_event(q.get(timeout=15))
                except queue.Empty:
                    self.wfile.write(b": ping\n\n")
                    self.wfile.flush()
        except (BrokenPipeError, ConnectionError, OSError):
            pass
        finally:
            with b.lock:
                if q in b.listeners:
                    b.listeners.remove(q)

    def _send_event(self, msg):
        self.wfile.write(f"data: {json.dumps(msg)}\n\n".encode("utf-8"))
        self.wfile.flush()

    def do_POST(self):
        try:
            data = self._body()
            if self.path == "/push":
                bid, fig = BOARD.add_block(data)
                self._json({"ok": True, "id": bid, "fig": fig})
            elif self.path == "/msg":
                ev = BOARD.learner_msg(data["text"], data.get("via", "typed"))
                self._json({"ok": True, "event": ev["id"]})
            elif self.path == "/sketch":
                ev = BOARD.learner_sketch(data.get("png", ""), data.get("label", ""))
                self._json({"ok": True, "event": ev["id"], "path": ev["path"]})
            elif self.path == "/capture":
                ev = BOARD.learner_capture(data.get("png", ""), data.get("label", ""),
                                           data.get("via", "camera"))
                self._json({"ok": True, "event": ev["id"], "path": ev["path"]})
            elif self.path == "/ask":
                ev = BOARD.learner_ask(data.get("text", ""), data.get("png", ""),
                                       data.get("via", "typed"))
                self._json({"ok": True, "event": ev["id"], "path": ev.get("path")})
            elif self.path == "/scene":
                BOARD.save_scene(data)
                self._json({"ok": True})
            elif self.path == "/image":
                bid, fig = BOARD.add_image(source=data.get("source"), caption=data.get("caption"),
                                           url=data.get("url"), path=data.get("path"),
                                           b64=data.get("b64"), filename=data.get("filename"))
                self._json({"ok": True, "id": bid, "fig": fig})
            elif self.path == "/session":
                b = set_board(data["subject"], data.get("unit"))
                self._json({"ok": True, "subject": b.subject, "date": b.date, "dir": b.dir})
            elif self.path == "/export":
                self._json({"ok": True, "path": BOARD.export_lesson()})
            else:
                self._json({"ok": False, "error": "unknown path"}, 404)
        except Exception as e:
            self._json({"ok": False, "error": f"{type(e).__name__}: {e}"}, 400)


# ----------------------------------------------------------------------------- the studio page
PAGE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Tutor Studio</title>
<link rel="stylesheet" href="__HLJS_CSS__">
<style>
:root{--bg:#15171c;--panel:#1d2027;--ink:#e6e8ee;--dim:#9aa3b2;--line:#2c313b;--accent:#6aa9ff;
 --accent-soft:#22304a;--check:#1e2a1e;--check-line:#3c5a3c;--max:52rem;--me:#243447;}
*{box-sizing:border-box} html{font-size:17px}
body{margin:0;background:var(--bg);color:var(--ink);line-height:1.6;
 font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;}
main{max-width:var(--max);margin:0 auto;padding:1.6rem 1.4rem 9rem;}
.head{display:flex;align-items:baseline;gap:.8rem;border-bottom:1px solid var(--line);
 padding-bottom:.7rem;margin-bottom:1.2rem;}
.badge{font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);
 background:var(--accent-soft);padding:.2rem .6rem;border-radius:.4rem;white-space:nowrap;}
.head h1{font-size:1.15rem;margin:0;font-weight:600}
.head .surface-note{color:var(--dim);font-size:.78rem;margin-left:auto;}
p{margin:.6rem 0} ul{margin:.5rem 0;padding-left:1.3rem} li{margin:.22rem 0}
code{font-family:Consolas,Menlo,monospace;font-size:.9em;background:#0e1014;
 border:1px solid var(--line);border-radius:.3rem;padding:.05rem .35rem;}
pre.code{background:#0e1014;border:1px solid var(--line);border-radius:.6rem;
 padding:1rem 1.1rem;overflow:auto;margin:1rem 0;}
pre.code code{background:none;border:none;padding:0;font-size:.86rem;line-height:1.55;}
.math{overflow-x:auto} div.math{margin:1.1rem 0}
figure.fig{margin:1.2rem 0;padding:0}
.fig .card{background:#fff;border:1px solid var(--line);border-radius:.6rem;padding:1rem;
 text-align:center;overflow:auto;}
.fig .card svg,.fig .card img{max-width:100%;height:auto;}
figcaption{color:var(--dim);font-size:.85rem;margin-top:.45rem;text-align:center;}
.srcline{color:var(--dim);font-size:.75rem;text-align:center;margin-top:.1rem;font-style:italic;}
table.grid{border-collapse:collapse;width:100%;background:var(--panel);font-size:.92rem;}
table.grid th,table.grid td{border:1px solid var(--line);padding:.5rem .75rem;text-align:left;}
table.grid th{background:#222633} table.grid tr.hi td{background:var(--accent-soft)}
.note{color:var(--dim);font-size:.85rem;font-style:italic;}
.check{background:var(--check);border:1px solid var(--check-line);border-left:4px solid #5fa85f;
 border-radius:.6rem;padding:1rem 1.2rem;margin:1.4rem 0;}
.check-tag{font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:#8fce8f;margin-bottom:.4rem;}
.answer{margin-top:.8rem}.answer summary{cursor:pointer;color:var(--accent);font-size:.85rem}
.answer>div{margin-top:.6rem;padding-top:.6rem;border-top:1px dashed var(--check-line);}
/* chat bubbles */
.say{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--accent);
 border-radius:.7rem;padding:.7rem 1rem;margin:.9rem 15% .9rem 0;}
.learner{background:var(--me);border:1px solid #33475f;border-right:3px solid #7fb8ff;
 border-radius:.7rem;padding:.7rem 1rem;margin:.9rem 0 .9rem 15%;}
.who{font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;color:var(--dim);margin-bottom:.2rem;}
#typing{display:none;color:var(--dim);font-size:.85rem;margin:.6rem 0 .6rem 0;}
#typing.on{display:block}
/* input dock */
#dock{position:fixed;left:0;right:0;bottom:0;background:var(--panel);z-index:20;
 border-top:1px solid var(--line);padding:.6rem .8rem;}
#dock-inner{max-width:var(--max);margin:0 auto;display:flex;gap:.5rem;align-items:center;}
#msg{flex:1;background:#0e1014;color:var(--ink);border:1px solid var(--line);border-radius:.6rem;
 padding:.55rem .8rem;font-size:.95rem;font-family:inherit;}
.dockbtn{background:#0e1014;color:var(--ink);border:1px solid var(--line);border-radius:.6rem;
 padding:.5rem .8rem;font-size:.9rem;cursor:pointer;white-space:nowrap;}
#send{background:var(--accent);color:#0e1014;font-weight:700;border:none;}
#btn-mic.rec{outline:2px solid #e05555;color:#e05555;animation:pulse 1.2s infinite;}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(224,85,85,.5)}50%{box-shadow:0 0 0 6px rgba(224,85,85,0)}}
/* drawer + camera share the overlay */
#overlay{position:fixed;left:0;right:0;bottom:3.6rem;height:60vh;background:var(--panel);z-index:19;
 border-top:2px solid var(--accent);display:none;flex-direction:column;}
#overlay.open{display:flex}
#toolbar{display:flex;gap:.5rem;align-items:center;padding:.5rem .8rem;
 border-bottom:1px solid var(--line);flex-wrap:wrap;}
#toolbar button,#toolbar input[type=text]{background:#0e1014;color:var(--ink);
 border:1px solid var(--line);border-radius:.4rem;padding:.32rem .7rem;font-size:.85rem;cursor:pointer;}
#toolbar button.active{outline:2px solid var(--accent)}
.swatch{width:1.5rem;height:1.5rem;border-radius:50%;border:2px solid var(--line);cursor:pointer;padding:0;}
.swatch.active{outline:2px solid var(--accent)}
#toolbar input[type=text]{cursor:text;flex:1;min-width:7rem}
.gobtn{background:var(--accent) !important;color:#0e1014 !important;font-weight:700;}
#pad-wrap{flex:1;position:relative;background:#fff;display:none;}
#pad{position:absolute;inset:0;touch-action:none;cursor:crosshair;}
#cam-wrap{flex:1;position:relative;background:#000;display:none;align-items:center;justify-content:center;}
#cam{max-width:100%;max-height:100%;}
#ovl-msg{color:#8fce8f;font-size:.8rem;}
#drop-hint{position:fixed;inset:0;background:rgba(34,48,74,.85);z-index:40;display:none;
 align-items:center;justify-content:center;font-size:1.3rem;color:var(--accent);}
</style>
</head>
<body>
<main>
  <header class="head">
    <span class="badge" id="subject">studio</span>
    <h1>Tutor Studio</h1>
    <span class="surface-note">type · draw · snap — the teacher answers right here</span>
  </header>
  <div id="stream"></div>
  <div id="typing">teacher is looking at it…</div>
</main>

<div id="overlay">
  <div id="toolbar">
    <span id="mode-tools" style="display:contents">
      <button data-tool="pen" class="active">Pen</button>
      <button data-tool="hl">Highlight</button>
      <button data-tool="eraser">Eraser</button>
      <button class="swatch active" data-c="#111111" style="background:#111"></button>
      <button class="swatch" data-c="#0072B2" style="background:#0072B2"></button>
      <button class="swatch" data-c="#D55E00" style="background:#D55E00"></button>
      <button class="swatch" data-c="#009E73" style="background:#009E73"></button>
      <button data-act="undo">Undo</button>
      <button data-act="clear">Clear</button>
    </span>
    <input type="text" id="label" placeholder="label (optional)">
    <button id="ovl-go" class="gobtn">Send &rarr; teacher</button>
    <span id="ovl-msg"></span>
    <button data-act="close">&times;</button>
  </div>
  <div id="pad-wrap"><canvas id="pad"></canvas></div>
  <div id="cam-wrap"><video id="cam" autoplay playsinline></video></div>
</div>

<div id="dock"><div id="dock-inner">
  <input id="msg" placeholder="ask / answer here — Enter to send   (Ctrl+V pastes a screenshot)">
  <button id="btn-mic" class="dockbtn" title="speak — words land in the box, edit then Send">&#127908;</button>
  <button id="send" class="dockbtn">Send</button>
  <button id="btn-draw" class="dockbtn">&#9998; Draw</button>
  <button id="btn-cam" class="dockbtn">&#128247; Camera</button>
</div></div>
<div id="drop-hint">drop the image — it goes straight to the teacher</div>

<script>
 window.MathJax={tex:{inlineMath:[['\\(','\\)']],displayMath:[['\\[','\\]']]},svg:{fontCache:'global'}};
</script>
<script async src="__MATHJAX__"></script>
<script src="__MERMAID__"></script>
<script src="__HLJS_JS__"></script>
<script>
mermaid.initialize({startOnLoad:false, theme:'neutral', securityLevel:'loose'});
const stream=document.getElementById('stream'), typing=document.getElementById('typing');
const seen=new Set();

function esc(s){const d=document.createElement('div');d.textContent=s==null?'':String(s);return d.innerHTML;}
function inline(s){return esc(s).replace(/\*\*(.+?)\*\*/g,'<strong>$1</strong>')
                               .replace(/`(.+?)`/g,'<code>$1</code>');}
function md(s){return (s||'').trim().split(/\n\s*\n/).map(ch=>{
  const ls=ch.split('\n').filter(l=>l.trim());
  if(ls.length&&ls.every(l=>l.trim().startsWith('- ')))
    return '<ul>'+ls.map(l=>'<li>'+inline(l.trim().slice(2))+'</li>').join('')+'</ul>';
  return '<p>'+ls.map(inline).join('<br>')+'</p>';}).join('');}
function figure(inner,fig,cap,src){
  return '<figure class="fig">'+inner+
    '<figcaption>Figure '+fig+(cap?' — '+inline(cap):'')+'</figcaption>'+
    (src?'<div class="srcline">'+inline(src)+'</div>':'')+'</figure>';}

function render(m){
  if(seen.has(m.id))return; seen.add(m.id);
  const b=m.block, el=document.createElement('div');
  let h='';
  if(b.note) h+='<p class="note">'+inline(b.note)+'</p>';
  switch(b.type){
    case 'prose': h+=md(b.md); typing.classList.remove('on'); break;
    case 'say': h+='<div class="say"><div class="who">teacher</div>'+md(b.md)+'</div>';
                typing.classList.remove('on'); break;
    case 'learner': h+='<div class="learner"><div class="who">you</div>'+md(b.md)+'</div>';
                typing.classList.add('on'); break;
    case 'math': h+= b.display===false ? '<span class="math">\\('+b.tex+'\\)</span>'
                                       : '<div class="math">\\['+b.tex+'\\]</div>';
                typing.classList.remove('on'); break;
    case 'code': h+='<pre class="code"><code class="language-'+esc(b.lang||'')+'">'+esc(b.code)+'</code></pre>';
                typing.classList.remove('on'); break;
    case 'map': case 'process':
      h+=figure('<div class="card"><pre class="mermaid">'+esc(b.mermaid)+'</pre></div>',m.fig,b.caption);
      typing.classList.remove('on'); break;
    case 'table': {
      let t='<table class="grid"><thead><tr>'+(b.headers||[]).map(x=>'<th>'+inline(String(x))+'</th>').join('')+'</tr></thead><tbody>';
      (b.rows||[]).forEach((r,i)=>{t+='<tr'+(b.highlight_row===i?' class="hi"':'')+'>'+r.map(c=>'<td>'+inline(String(c))+'</td>').join('')+'</tr>';});
      h+=figure('<div class="card" style="padding:0">'+t+'</tbody></table></div>',m.fig,b.caption);
      typing.classList.remove('on'); break;}
    case 'plot': case 'structural':
      h+=figure('<div class="card">'+(b.svg||'<span style="color:#b00">[no figure]</span>')+'</div>',m.fig,b.caption);
      typing.classList.remove('on'); break;
    case 'image': {
      const mine=(b.source||'').startsWith('learner');
      h+=figure('<div class="card"><img src="/files/'+encodeURIComponent(b.file)+'"></div>',
                m.fig,b.caption, mine?null:('source: '+b.source));
      if(!mine) typing.classList.remove('on');
      break;}
    case 'timing':
      h+=figure('<div class="card"><pre class="code" style="text-align:left">'+esc(JSON.stringify(b.wavedrom,null,1))+'</pre></div>',
                m.fig,(b.caption||'')+' (timing spec)'); break;
    case 'check':
      h+='<div class="check"><div class="check-tag">CHECK — retrieve before revealing</div>'+
         '<div>'+md(b.q)+'</div>'+
         (b.answer?'<details class="answer"><summary>show answer</summary><div>'+md(b.answer)+'</div></details>':'')+'</div>';
      typing.classList.remove('on'); break;
    default: h+='<p class="note">[unknown block '+esc(b.type)+']</p>';
  }
  el.innerHTML=h; stream.appendChild(el);
  el.querySelectorAll('pre.mermaid').forEach(n=>mermaid.run({nodes:[n]}));
  el.querySelectorAll('pre.code code').forEach(n=>{if(window.hljs)hljs.highlightElement(n);});
  if(window.MathJax&&MathJax.typesetPromise)MathJax.typesetPromise([el]);
  window.scrollTo({top:document.body.scrollHeight,behavior:'smooth'});
}

const es=new EventSource('/events');
es.onmessage=e=>{const m=JSON.parse(e.data);
  if(m.kind==='hello'){document.getElementById('subject').textContent=
     m.subject+(m.unit?' · '+m.unit:'')+' · '+m.date;return;}
  if(m.kind==='block')render(m);};

/* ---------- chat ---------- */
const msg=document.getElementById('msg');
let usedVoice=false;
async function post(p,body){const r=await fetch(p,{method:'POST',
  headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});return r.json();}
async function sendMsg(){const t=msg.value.trim(); if(!t)return; msg.value='';
  const via=usedVoice?'voice':'typed'; usedVoice=false;
  if(rec&&listening)rec.stop();
  await post('/msg',{text:t,via});}
document.getElementById('send').onclick=sendMsg;
msg.addEventListener('keydown',e=>{if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();sendMsg();}});

/* ---------- mic (Web Speech API; words land in the box — edit, then Send) ---------- */
const btnMic=document.getElementById('btn-mic');
const SR=window.SpeechRecognition||window.webkitSpeechRecognition;
let rec=null, listening=false;
btnMic.onclick=()=>{
  if(!SR){msg.placeholder='speech recognition not available in this browser';return;}
  if(listening){rec.stop();return;}
  rec=new SR(); rec.lang='en-IN'; rec.interimResults=true; rec.continuous=true;
  const base=msg.value?msg.value+' ':'';
  rec.onresult=e=>{let fin='',interim='';
    for(let i=0;i<e.results.length;i++){const r=e.results[i];
      if(r.isFinal){fin+=r[0].transcript;usedVoice=true;} else interim+=r[0].transcript;}
    msg.value=(base+fin+interim).replace(/\s+/g,' ').trimStart();};
  rec.onend=()=>{listening=false;btnMic.classList.remove('rec');};
  rec.onerror=ev=>{listening=false;btnMic.classList.remove('rec');
    if(ev.error!=='aborted'&&ev.error!=='no-speech')msg.placeholder='mic error: '+ev.error;};
  rec.start(); listening=true; btnMic.classList.add('rec'); msg.focus();};

/* ---------- overlay: draw + camera ---------- */
const overlay=document.getElementById('overlay'), padWrap=document.getElementById('pad-wrap'),
      camWrap=document.getElementById('cam-wrap'), pad=document.getElementById('pad'),
      ctx=pad.getContext('2d'), video=document.getElementById('cam'),
      modeTools=document.getElementById('mode-tools');
let mode=null, tool='pen', color='#111111', drawing=false, undo=[], camStream=null;

function openOverlay(m){mode=m; overlay.classList.add('open');
  padWrap.style.display=m==='draw'?'block':'none';
  camWrap.style.display=m==='cam'?'flex':'none';
  modeTools.style.display=m==='draw'?'contents':'none';
  document.getElementById('ovl-go').textContent=m==='draw'?'Send → teacher':'Snap → teacher';
  if(m==='draw')resize();
  if(m==='cam')startCam();}
function closeOverlay(){overlay.classList.remove('open');
  if(camStream){camStream.getTracks().forEach(t=>t.stop());camStream=null;}}
document.getElementById('btn-draw').onclick=()=>openOverlay('draw');
document.getElementById('btn-cam').onclick=()=>openOverlay('cam');

async function startCam(){
  try{camStream=await navigator.mediaDevices.getUserMedia(
        {video:{facingMode:'environment',width:{ideal:1920}}});
      video.srcObject=camStream;}
  catch(e){document.getElementById('ovl-msg').textContent='camera error: '+e.message;}}

function resize(){
  const r=padWrap.getBoundingClientRect(), keep=pad.width?pad.toDataURL():null;
  pad.width=r.width*devicePixelRatio; pad.height=r.height*devicePixelRatio;
  pad.style.width=r.width+'px'; pad.style.height=r.height+'px';
  ctx.setTransform(devicePixelRatio,0,0,devicePixelRatio,0,0);
  ctx.fillStyle='#fff'; ctx.fillRect(0,0,r.width,r.height);
  if(keep){const im=new Image();im.onload=()=>ctx.drawImage(im,0,0,r.width,r.height);im.src=keep;}
  ctx.lineCap='round';ctx.lineJoin='round';}
function snap(){undo.push(pad.toDataURL());if(undo.length>25)undo.shift();}
function pos(e){const r=pad.getBoundingClientRect();return[e.clientX-r.left,e.clientY-r.top];}
pad.addEventListener('pointerdown',e=>{drawing=true;snap();pad.setPointerCapture(e.pointerId);
  const[x,y]=pos(e);ctx.beginPath();ctx.moveTo(x,y);e.preventDefault();});
pad.addEventListener('pointermove',e=>{if(!drawing)return;const[x,y]=pos(e);
  ctx.globalAlpha=tool==='hl'?0.35:1;
  ctx.strokeStyle=tool==='eraser'?'#ffffff':color;
  ctx.lineWidth=tool==='eraser'?26:(tool==='hl'?14:2.4);
  ctx.lineTo(x,y);ctx.stroke();e.preventDefault();});
['pointerup','pointercancel'].forEach(ev=>pad.addEventListener(ev,()=>{drawing=false;ctx.globalAlpha=1;}));

document.getElementById('toolbar').addEventListener('click',e=>{
  const b=e.target.closest('button'); if(!b)return;
  if(b.dataset.tool){tool=b.dataset.tool;
    document.querySelectorAll('#toolbar [data-tool]').forEach(x=>x.classList.toggle('active',x===b));}
  if(b.dataset.c){color=b.dataset.c;
    document.querySelectorAll('.swatch').forEach(x=>x.classList.toggle('active',x===b));}
  if(b.dataset.act==='undo'&&undo.length){const im=new Image();
    im.onload=()=>{const r=pad.getBoundingClientRect();ctx.fillStyle='#fff';
      ctx.fillRect(0,0,r.width,r.height);ctx.drawImage(im,0,0,r.width,r.height);};im.src=undo.pop();}
  if(b.dataset.act==='clear'){snap();const r=pad.getBoundingClientRect();ctx.fillStyle='#fff';
    ctx.fillRect(0,0,r.width,r.height);}
  if(b.dataset.act==='close')closeOverlay();});

document.getElementById('ovl-go').onclick=async()=>{
  const label=document.getElementById('label').value, m=document.getElementById('ovl-msg');
  m.textContent='sending…';
  let j;
  if(mode==='draw'){j=await post('/sketch',{png:pad.toDataURL('image/png'),label});}
  else{const c=document.createElement('canvas');
       c.width=video.videoWidth;c.height=video.videoHeight;
       c.getContext('2d').drawImage(video,0,0);
       j=await post('/capture',{png:c.toDataURL('image/png'),label,via:'camera'});}
  m.textContent=j.ok?'sent — teacher can see it':'error: '+j.error;
  setTimeout(()=>m.textContent='',3500);
  if(j.ok&&mode==='cam')closeOverlay();};

/* ---------- paste + drag-drop ---------- */
document.addEventListener('paste',async e=>{
  for(const it of e.clipboardData.items){
    if(it.type.startsWith('image/')){
      const f=it.getAsFile(), fr=new FileReader();
      fr.onload=()=>post('/capture',{png:fr.result,label:'pasted',via:'paste'});
      fr.readAsDataURL(f); e.preventDefault(); return;}}});
const hint=document.getElementById('drop-hint');
document.addEventListener('dragover',e=>{e.preventDefault();hint.style.display='flex';});
document.addEventListener('dragleave',e=>{if(!e.relatedTarget)hint.style.display='none';});
document.addEventListener('drop',e=>{e.preventDefault();hint.style.display='none';
  const f=[...e.dataTransfer.files].find(f=>f.type.startsWith('image/'));
  if(!f)return; const fr=new FileReader();
  fr.onload=()=>post('/capture',{png:fr.result,label:f.name,via:'drop'});
  fr.readAsDataURL(f);});
</script>
</body>
</html>
"""
PAGE = (PAGE.replace("__HLJS_CSS__", CDN["hljs_css"]).replace("__HLJS_JS__", CDN["hljs_js"])
            .replace("__MATHJAX__", CDN["mathjax"]).replace("__MERMAID__", CDN["mermaid"]))


# ----------------------------------------------------------------------- the CANVAS page (v3)
# ONE shared infinite whiteboard (Excalidraw UMD, MIT, VENDORED in tools/vendor/ — the researched
# choice; esm.sh module-graph loading proved unreliable in testing): teacher
# content lands as objects ON the canvas; the learner draws/types over it with the full tool set;
# "Ask" snapshots the annotated board to a PNG the engine reads visually. Light board on purpose —
# math/plots/schematics are black-on-white. The v2 stream page survives at /classic as fallback.
EXCALIDRAW_VER = "0.17.6"   # vendored UMD build in tools/vendor/ (see whiteboard.md)
PAGE_CANVAS = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Tutor Studio — Canvas</title>
<style>
:root{--panel:#1d2027;--ink:#e6e8ee;--line:#2c313b;--accent:#6aa9ff;}
html,body{margin:0;height:100%;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;}
#app{position:fixed;inset:0 0 3.4rem 0;}
#dock{position:fixed;left:0;right:0;bottom:0;height:3.4rem;background:var(--panel);z-index:50;
 border-top:1px solid var(--line);display:flex;align-items:center;gap:.5rem;padding:0 .8rem;}
#subject{font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);
 background:#22304a;padding:.2rem .55rem;border-radius:.4rem;white-space:nowrap;}
#msg{flex:1;background:#0e1014;color:var(--ink);border:1px solid var(--line);border-radius:.6rem;
 padding:.5rem .8rem;font-size:.95rem;font-family:inherit;}
.dockbtn{background:#0e1014;color:var(--ink);border:1px solid var(--line);border-radius:.6rem;
 padding:.45rem .8rem;font-size:.9rem;cursor:pointer;white-space:nowrap;}
#ask{background:var(--accent);color:#0e1014;font-weight:700;border:none;}
#btn-mic.rec{outline:2px solid #e05555;color:#e05555;animation:pulse 1.2s infinite;}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(224,85,85,.5)}50%{box-shadow:0 0 0 6px rgba(224,85,85,0)}}
#toast{position:fixed;bottom:4.2rem;right:1rem;z-index:60;background:#22304a;color:var(--accent);
 padding:.45rem .9rem;border-radius:.5rem;font-size:.82rem;opacity:0;transition:opacity .3s;}
#cam-modal{position:fixed;inset:0;background:rgba(0,0,0,.85);z-index:70;display:none;
 align-items:center;justify-content:center;flex-direction:column;gap:.8rem;}
#cam-modal.open{display:flex}
#cam{max-width:90vw;max-height:70vh;border-radius:.5rem;}
#boot{position:fixed;inset:0;display:flex;align-items:center;justify-content:center;
 color:#9aa3b2;background:#fdfdf8;z-index:5;font-size:.95rem;}
</style>
<script>
  // fonts/locales still come from the CDN; the three engine bundles are VENDORED locally
  // (tools/vendor/, served at /vendor/) so the canvas always boots even if the CDN is slow.
  window.EXCALIDRAW_ASSET_PATH = "https://unpkg.com/@excalidraw/excalidraw@__XVER__/dist/";
  window.MathJax={tex:{inlineMath:[['\\(','\\)']]},svg:{fontCache:'none'},
                  startup:{typeset:false}};
</script>
<script src="/vendor/react.production.min.js"></script>
<script src="/vendor/react-dom.production.min.js"></script>
<script src="/vendor/excalidraw.production.min.js"></script>
<script>
  // surface module/boot failures where the learner (and headless tests) can see them
  window.process = window.process || { env: { NODE_ENV: "production" } };
  window.addEventListener('error', e => { const b = document.getElementById('boot');
    if (b) b.textContent = 'boot error: ' + (e.message || e.type) +
      (e.filename ? '  [' + e.filename.split('/').slice(-1)[0] + ':' + e.lineno + ']' : ''); });
  window.addEventListener('unhandledrejection', e => { const b = document.getElementById('boot');
    if (b) b.textContent = 'boot error (promise): ' + (e.reason && e.reason.message || e.reason); });
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg.js"></script>
<script src="__MERMAID__"></script>
</head>
<body>
<div id="boot">loading the canvas…</div>
<div id="app"></div>
<div id="toast"></div>
<div id="cam-modal">
  <video id="cam" autoplay playsinline></video>
  <div><button class="dockbtn" id="cam-snap">Snap → board</button>
       <button class="dockbtn" id="cam-close">&times; close</button></div>
</div>
<div id="dock">
  <span id="subject">canvas</span>
  <input id="msg" placeholder="ask here (or just draw/type ON the board and hit Ask — I get a snapshot of everything)">
  <button id="btn-mic" class="dockbtn" title="speak">&#127908;</button>
  <button id="ask" class="dockbtn">Ask</button>
  <button id="btn-cam" class="dockbtn" title="photograph your notebook">&#128247;</button>
  <a class="dockbtn" href="/classic" title="old stream layout" style="text-decoration:none">v2</a>
</div>

<script type="module">
/* Dynamic imports with progressive boot status: a stall names its stage instead of hanging on a
   blank "loading". If nothing mounts in 45 s, the /classic fallback is offered. */
const boot=document.getElementById('boot');
const bootSay=(t)=>{if(document.getElementById('boot'))boot.textContent=t;};
setTimeout(()=>{if(document.getElementById('boot'))boot.innerHTML=
  boot.textContent+' — taking long? <a href="/classic">open the classic layout</a> '+
  '(first load fetches the canvas engine once; it is cached after)';},45000);

bootSay('starting the canvas…');
const ExcalidrawLib=window.ExcalidrawLib, React=window.React;
const createRoot=window.ReactDOM.createRoot;
if(!ExcalidrawLib||!React){bootSay('boot error: vendored canvas engine missing — '+
  'check tools/vendor/ (see tools/README.md)');throw new Error('vendor bundles missing');}
bootSay('restoring your board…');

mermaid.initialize({startOnLoad:false, theme:'neutral', securityLevel:'loose'});
const toast=(t)=>{const el=document.getElementById('toast');el.textContent=t;el.style.opacity=1;
                  setTimeout(()=>el.style.opacity=0,2500);};
let api=null;

/* ---------- boot: restore scene, mount, then subscribe ---------- */
const saved=await (await fetch('/canvas')).json();
const placed=new Set((saved.elements||[]).map(e=>e.customData&&e.customData.blockId).filter(Boolean));

bootSay('mounting…');
createRoot(document.getElementById('app')).render(
  React.createElement(ExcalidrawLib.Excalidraw,{
    excalidrawAPI:(a)=>{api=a; const b=document.getElementById('boot'); if(b)b.remove();
                        subscribe();},
    initialData:{elements:saved.elements||[], files:saved.files||{},
                 appState:{viewBackgroundColor:'#fdfdf8', currentItemStrokeColor:'#1e1e1e',
                           currentItemFontFamily:1}},
    theme:'light',
  }));

/* ---------- scene autosave (debounced; the canvas is part of the session record) ---------- */
let saveTimer=null, dirty=false;
setInterval(()=>{if(!api||!dirty)return; dirty=false;
  fetch('/scene',{method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify({elements:api.getSceneElements(),files:api.getFiles()})});},2500);
document.addEventListener('pointerup',()=>{dirty=true;});
document.addEventListener('keyup',()=>{dirty=true;});

/* ---------- layout: teacher content flows down a column ---------- */
const COL_X=90, COL_W=720, GAP=36;
function yCursor(){
  let y=60;
  for(const e of (api?api.getSceneElements():[]))
    if(e.y+ (e.height||0) > y) y=e.y+(e.height||0);
  return y+GAP;}

function addElements(skeletons){
  const conv=ExcalidrawLib.convertToExcalidrawElements(skeletons);
  api.updateScene({elements:[...api.getSceneElements(),...conv]});
  api.scrollToContent(conv,{animate:true,fitToViewport:false});
  dirty=true; return conv;}

function wrap(s,n=86){const out=[];
  for(const raw of String(s).split('\n')){let line='';
    for(const w of raw.split(' ')){
      if((line+' '+w).trim().length>n){out.push(line.trim());line=w;}else line+=' '+w;}
    out.push(line.trim());}
  return out.join('\n');}
const plain=(md)=>String(md).replace(/\*\*(.+?)\*\*/g,'$1').replace(/`(.+?)`/g,'$1');

function addText(md,{color='#1e1e1e',size=17,family=2,prefix=''}={},blockId=null){
  addElements([{type:'text',x:COL_X,y:yCursor(),text:wrap(prefix+plain(md)),
    fontSize:size,fontFamily:family,strokeColor:color,
    customData:blockId?{blockId}:undefined}]);}

async function addSvg(svg,caption,blockId){
  const dataURL='data:image/svg+xml;base64,'+btoa(unescape(encodeURIComponent(svg)));
  await addDataURL(dataURL,'image/svg+xml',caption,blockId);}

function addDataURL(dataURL,mime,caption,blockId){return new Promise(res=>{
  const im=new Image();
  im.onload=()=>{let w=im.naturalWidth||COL_W,h=im.naturalHeight||300;
    if(w>COL_W){h=h*COL_W/w;w=COL_W;}
    const fileId=String(Math.random()).slice(2)+Date.now();
    api.addFiles([{id:fileId,dataURL,mimeType:mime,created:Date.now()}]);
    const y=yCursor();
    const sk=[{type:'image',x:COL_X,y,width:w,height:h,fileId,
               customData:blockId?{blockId}:undefined}];
    if(caption)sk.push({type:'text',x:COL_X,y:y+h+8,text:wrap('· '+plain(caption),100),
                        fontSize:13,fontFamily:2,strokeColor:'#7a7a72'});
    addElements(sk);res();};
  im.onerror=()=>{addText('[figure failed to load]',{color:'#b00000'},blockId);res();};
  im.src=dataURL;});}

/* ---------- placing teacher blocks onto the canvas ---------- */
let mseq=0;
async function place(m){
  if(placed.has('b'+m.id))return; placed.add('b'+m.id);
  const b=m.block, id='b'+m.id;
  try{
    switch(b.type){
      case 'say':    addText(b.md,{color:'#1b4f9c',size:18},id); break;
      case 'prose':  addText(b.md,{},id); break;
      case 'learner':addText(b.md,{color:'#5c5c54',size:15,prefix:'you: '},id); break;
      case 'check':  addText('CHECK — answer before moving on:\n'+plain(b.q),
                             {color:'#1e7a1e',size:17},id); break;
      case 'code':   addText(b.code,{family:3,size:14},id); break;
      case 'math': {
        const node=MathJax.tex2svg(b.tex,{display:true}).querySelector('svg');
        node.setAttribute('width',(parseFloat(node.getAttribute('width'))||20)*10+'px');
        node.removeAttribute('height');
        await addSvg(node.outerHTML,b.caption,id); break;}
      case 'map': case 'process': {
        const {svg}=await mermaid.render('mm'+(++mseq),b.mermaid);
        await addSvg(svg,b.caption,id); break;}
      case 'plot': case 'structural':
        if(b.svg)await addSvg(b.svg,b.caption,id);
        else addText('[no figure]',{color:'#b00000'},id);
        break;
      case 'image': {
        const blob=await (await fetch('/files/'+encodeURIComponent(b.file))).blob();
        const dataURL=await new Promise(r=>{const fr=new FileReader();
          fr.onload=()=>r(fr.result);fr.readAsDataURL(blob);});
        await addDataURL(dataURL,blob.type||'image/png',
          (b.caption||'')+((b.source&&!b.source.startsWith('learner'))?'   ['+b.source+']':''),id);
        break;}
      case 'table': {
        const rows=[(b.headers||[]).join(' | '),
                    (b.headers||[]).map(()=>'---').join(' | '),
                    ...(b.rows||[]).map(r=>r.join(' | '))];
        addText(rows.join('\n'),{family:3,size:14},id);
        if(b.caption)addText('· '+b.caption,{color:'#7a7a72',size:13},null);
        break;}
      default: addText('['+b.type+' block — open /classic to view]',{color:'#7a7a72',size:13},id);
    }
  }catch(err){addText('[render error: '+err.message+']',{color:'#b00000'},id);}
}

/* place strictly in order — SSE events queue through a promise chain */
let chain=Promise.resolve();
function subscribe(){
  const es=new EventSource('/events');
  es.onmessage=e=>{const m=JSON.parse(e.data);
    if(m.kind==='hello'){document.getElementById('subject').textContent=
      m.subject+(m.unit?' · '+m.unit:'')+' · '+m.date; return;}
    if(m.kind==='block')chain=chain.then(()=>place(m));};}

/* ---------- Ask: text + a PNG snapshot of the whole annotated board ---------- */
const msg=document.getElementById('msg');
let usedVoice=false;
async function ask(){
  const text=msg.value.trim(); msg.value='';
  toast('sending the board…');
  let png='';
  try{
    const blob=await ExcalidrawLib.exportToBlob({
      elements:api.getSceneElements(),files:api.getFiles(),mimeType:'image/png',
      appState:{exportBackground:true,viewBackgroundColor:'#fdfdf8'},maxWidthOrHeight:2200});
    png=await new Promise(r=>{const fr=new FileReader();fr.onload=()=>r(fr.result);
                              fr.readAsDataURL(blob);});
  }catch(err){/* snapshot failed -> still send the text */}
  const via=usedVoice?'voice':'typed'; usedVoice=false;
  const j=await (await fetch('/ask',{method:'POST',
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({text,png,via})})).json();
  toast(j.ok?'sent — teacher is looking at the board':'error: '+j.error);}
document.getElementById('ask').onclick=ask;
msg.addEventListener('keydown',e=>{if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();ask();}});

/* ---------- mic (Web Speech; words land in the box) ---------- */
const btnMic=document.getElementById('btn-mic');
const SR=window.SpeechRecognition||window.webkitSpeechRecognition;
let rec=null,listening=false;
btnMic.onclick=()=>{
  if(!SR){toast('speech recognition not available');return;}
  if(listening){rec.stop();return;}
  rec=new SR();rec.lang='en-IN';rec.interimResults=true;rec.continuous=true;
  const base=msg.value?msg.value+' ':'';
  rec.onresult=e=>{let fin='',interim='';
    for(let i=0;i<e.results.length;i++){const r=e.results[i];
      if(r.isFinal){fin+=r[0].transcript;usedVoice=true;}else interim+=r[0].transcript;}
    msg.value=(base+fin+interim).replace(/\s+/g,' ').trimStart();};
  rec.onend=()=>{listening=false;btnMic.classList.remove('rec');};
  rec.onerror=ev=>{listening=false;btnMic.classList.remove('rec');
    if(ev.error!=='aborted'&&ev.error!=='no-speech')toast('mic error: '+ev.error);};
  rec.start();listening=true;btnMic.classList.add('rec');msg.focus();};

/* ---------- camera: photo of the notebook -> an object ON the board ---------- */
const camModal=document.getElementById('cam-modal'),video=document.getElementById('cam');
let camStream=null;
document.getElementById('btn-cam').onclick=async()=>{
  camModal.classList.add('open');
  try{camStream=await navigator.mediaDevices.getUserMedia(
        {video:{facingMode:'environment',width:{ideal:1920}}});
      video.srcObject=camStream;}
  catch(e){toast('camera error: '+e.message);camModal.classList.remove('open');}};
document.getElementById('cam-close').onclick=()=>{camModal.classList.remove('open');
  if(camStream){camStream.getTracks().forEach(t=>t.stop());camStream=null;}};
document.getElementById('cam-snap').onclick=async()=>{
  const c=document.createElement('canvas');c.width=video.videoWidth;c.height=video.videoHeight;
  c.getContext('2d').drawImage(video,0,0);
  await addDataURL(c.toDataURL('image/png'),'image/png','your notebook photo',null);
  document.getElementById('cam-close').click();
  toast('photo is on the board — position it, annotate, then Ask');};
</script>
</body>
</html>
"""
PAGE_CANVAS = (PAGE_CANVAS.replace("__XVER__", EXCALIDRAW_VER)
                          .replace("__MERMAID__", CDN["mermaid"]))


# ----------------------------------------------------------------------------- entry point
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--subject", required=True)
    ap.add_argument("--unit", default=None)
    ap.add_argument("--port", type=int, default=DEFAULT_PORT)
    ap.add_argument("--root", default=None)
    args = ap.parse_args()
    set_board(args.subject, args.unit, args.root)
    srv = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    srv.daemon_threads = True
    print(f"[studio] {args.subject} -> http://127.0.0.1:{args.port}  (session: {BOARD.dir})")
    srv.serve_forever()


if __name__ == "__main__":
    main()
