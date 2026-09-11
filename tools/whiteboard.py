#!/usr/bin/env python3
"""
whiteboard.py — engine-side client for the Teacher 2.0 Studio (../whiteboard.md).

THE INTERACTIVE LOOP (how the engine holds a one-on-one session inside the window):

    import sys; sys.path.insert(0, "tools")
    import whiteboard as wb

    wb.start("verilog", unit="07-fsm")     # boots server if needed + opens the APP WINDOW
    wb.say("Before anything - from memory: what did we cover last time?")
    last = 0
    while session_running:
        events, last = wb.listen(after=last, timeout=540)   # blocks until the learner acts
        for ev in events:
            if ev["kind"] == "ask":      # CANVAS mode (default page): ev["text"] + ev["path"] =
                ...                      #   a PNG snapshot of the whole annotated board — Read it
                                         #   visually; their ink/typing sits ON your content.
            if ev["kind"] == "msg":      ...ev["text"]...      # v2 stream: they typed
            if ev["kind"] == "sketch":   ...Read ev["path"]...  # v2: sketch pad PNG
            if ev["kind"] == "capture":  ...Read ev["path"]...  # v2: camera / paste / drop
        wb.say(...) / wb.math(...) / wb.map_(...) / wb.plot(...)   # respond ON the board

Learner input channels: typed chat, the sketch pad, the camera (photograph their notebook),
Ctrl+V paste, drag-drop. All produce an event + (for images) a PNG path the engine Reads visually.

Images the teacher ships: GENERATE (matplotlib/schemdraw/SVG - preferred for anything
quantitative or structural, it's always faithful) or DOWNLOAD (photos/cross-sections; cite the
source) - whichever fits, per the learner's rule. `source` describes provenance either way.
"""
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import webbrowser

TOOLS = os.path.dirname(os.path.abspath(__file__))
PORT = 8471
BASE = f"http://127.0.0.1:{PORT}"

_BROWSERS = (  # app-mode shells, tried in order: a dedicated window, no tabs/URL bar
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
)


# ----------------------------------------------------------------------------- transport
def _req(path, payload=None, timeout=120):
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    r = urllib.request.Request(BASE + path, data=data,
                               headers={"Content-Type": "application/json"} if data else {})
    with urllib.request.urlopen(r, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def status():
    """Server status dict (incl. last_event + recent events), or None if not running."""
    try:
        return _req("/status")
    except (urllib.error.URLError, ConnectionError, OSError):
        return None


def open_window():
    """Open the studio as a dedicated app window (falls back to the default browser)."""
    for exe in _BROWSERS:
        if os.path.exists(exe):
            subprocess.Popen([exe, f"--app={BASE}/"])
            return "app-window"
    webbrowser.open(BASE + "/")
    return "browser-tab"


def start(subject, unit=None, open_browser=True, timeout=15):
    """Ensure the server runs on this subject's session; open the app window."""
    st = status()
    if st is None:
        flags = 0x08 if os.name == "nt" else 0            # DETACHED_PROCESS on Windows
        subprocess.Popen([sys.executable, os.path.join(TOOLS, "whiteboard_server.py"),
                          "--subject", subject] + (["--unit", unit] if unit else []),
                         creationflags=flags, close_fds=True,
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        t0 = time.time()
        while status() is None:
            if time.time() - t0 > timeout:
                raise RuntimeError("studio server did not come up — run "
                                   "tools/whiteboard_server.py manually to see the error")
            time.sleep(0.3)
    elif st.get("subject") != subject:
        _req("/session", {"subject": subject, "unit": unit})
    if open_browser:
        open_window()
    return status()


# ----------------------------------------------------------------------------- the inbox (learner -> engine)
def listen(after=0, timeout=540):
    """Long-poll the learner inbox. Blocks until something arrives (or timeout);
    returns (events, last_id). Call in a loop with the returned last_id."""
    q = urllib.parse.urlencode({"after": after, "timeout": timeout})
    r = _req(f"/inbox?{q}", timeout=timeout + 30)
    return r["events"], r["last"]


def last_event_id():
    st = status()
    return st["last_event"] if st else 0


# ----------------------------------------------------------------------------- teacher -> window
def push(block):
    return _req("/push", block)


def say(md):
    """A teacher chat bubble — the dialogue channel inside the window."""
    return push({"type": "say", "md": md})


def prose(md):
    return push({"type": "prose", "md": md})


def math(tex, display=True):
    return push({"type": "math", "tex": tex, "display": display})


def code(code_text, lang="", caption=None):
    return push({"type": "code", "code": code_text, "lang": lang, "caption": caption})


def map_(mermaid, caption=None):
    return push({"type": "map", "mermaid": mermaid, "caption": caption})


def process(mermaid, caption=None):
    return push({"type": "process", "mermaid": mermaid, "caption": caption})


def table(headers, rows, caption=None, highlight_row=None):
    return push({"type": "table", "headers": headers, "rows": rows,
                 "caption": caption, "highlight_row": highlight_row})


def plot(figure, caption=None):
    """figure = the make_figure matplotlib spec (kind filled in server-side). GENERATED imagery."""
    return push({"type": "plot", "figure": figure, "caption": caption})


def structural(figure, caption=None, fallback=None):
    return push({"type": "structural", "figure": figure, "caption": caption, "fallback": fallback})


def check(q, answer=None):
    return push({"type": "check", "q": q, "answer": answer})


def image(url=None, path=None, b64=None, source=None, caption=None, filename=None):
    """Ship an image: DOWNLOADED (source = citation) or GENERATED elsewhere and saved
    (source = 'generated: <how>'). `source` states provenance either way — required."""
    return _req("/image", {"url": url, "path": path, "b64": b64,
                           "source": source, "caption": caption, "filename": filename})


# ----------------------------------------------------------------------------- lifecycle
def export_lesson():
    """Freeze the session into a normal dated static lesson; returns the saved path."""
    return _req("/export", {})["path"]     # empty body so urllib issues a POST, not a GET


if __name__ == "__main__":
    print(json.dumps(status(), indent=1) if status() else "studio server not running")
