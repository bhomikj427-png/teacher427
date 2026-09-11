# tools/ — engine automation

Small scripts the engine uses. Not pedagogy; plumbing for the content-sourcing path
(`subject-research-protocol.md` §2) and the lesson-delivery path (`../rendering.md`).

Install all deps once: `pip install -r ../requirements.txt`.

## fetch_transcripts.py — NPTEL/YouTube lecture transcript puller

The **verified automated content path**. NPTEL course/archive web pages don't fetch cleanly, so we
pull NPTEL's own YouTube lectures' captions and clean them into teachable plain text.

```
pip install yt-dlp        # one-time; pure Python, no ffmpeg needed for captions
python tools/fetch_transcripts.py "<playlist-or-video-url>" "subjects/<name>/knowledge-base/_transcripts/"
python tools/fetch_transcripts.py "ytsearch20:NPTEL signals and systems IIT" "out/"
```

Output: one numbered `<NN>-<title>.txt` per lecture + `_manifest.json`. Each file is headered with
its source URL and an AUTO-CAPTION warning.

**Caveat (load-bearing):** captions are ASR — reliable for narrative/structure/intuition, but they
mangle math, symbols, and numbers. Every formula/constant/definition read from a transcript must be
**triangulated against the canonical textbook** before it is taught as settled (§1, §5). Manual PDF
drop is the fallback only when no captioned lecture covers a unit.

## The Visual & Rendering subsystem — `make_figure.py` + `render_lesson.py`

The lesson-delivery path. Design + rationale: **`../rendering.md`** (the source of truth these two
implement). The model: the **terminal stays the plain-ASCII control channel** (all dialogue,
retrieval, CHECK answers), and a **browser tab is the lesson surface** holding the rendered math,
plots, tables, and circuit diagrams (the two-surface rule, `../rendering.md` §2). They never
duplicate content — the terminal references figures by number ("→ figure 2 in the lesson tab").

### render_lesson.py — assemble a self-contained HTML lesson

Takes a declarative **lesson spec** (`../rendering.md` §4) and emits ONE self-contained HTML file
(MathJax / Mermaid / WaveDrom / highlight.js pinned via CDN), then auto-opens it.

```
# normal path — a lesson script builds the spec in Python, then:
from render_lesson import render
render(spec, "out.html")                          # writes + opens the tab

# CLI (render a saved spec):
python tools/render_lesson.py <spec.json> <out.html> [--no-open]
```

**Saving lessons permanently (use this, not a temp path).** A rendered lesson is a durable artifact.
`save_lesson(spec)` routes it to the canonical, dated, per-subject home so it's never lost:

```
from render_lesson import save_lesson
save_lesson(spec)                 # -> subjects/<subject>/lessons/<YYYY-MM-DD>-<concept-slug>.html
                                  #    subject/concept/unit are read from the spec
```

- Derived from `spec["subject"]`, `spec["title"]`, and optional `spec["unit"]` (→ a `lessons/<unit>/`
  subfolder). Override with `save_lesson(spec, subject=..., concept=..., unit=...)`.
- **Dated** filename: re-rendering the same concept on a later day makes a new file; same day
  overwrites (same lesson, refined). `lesson_path(...)` returns the path without writing.
- `render(spec, outpath)` remains the low-level escape hatch for an exact path (used by the
  examples and for throwaway smoke tests in the scratch dir). Full rationale: `../rendering.md` §8.

### make_figure.py — Python figure renderer (primitives 4 + 6 → inline SVG)

A dispatcher over a renderer **registry** (`../rendering.md` §5). Handles the two primitives that
need real computation — `kind="matplotlib"` (quantitative plots) and `kind="structural"` (domain
schematics; ships an `"ece" → schemdraw` entry). The other primitives (math, concept maps, process
diagrams, tables, code, timing) are client-side CDN JS inside `render_lesson.py`, no Python.

```
from make_figure import make_figure, register_structural, NoStructuralRenderer
svg = make_figure({"kind": "matplotlib", "series": [...], "xlabel": "...", ...})

# CLI smoke test:
python tools/make_figure.py <spec.json> <out.svg>
```

A new subject adds its own structural renderer via `register_structural("<subject>", handler)` — no
edit to the dispatcher. A subject with no registered renderer falls back gracefully (§3); a lesson
is never blocked on a missing renderer.

**Deps:** `matplotlib`, `numpy`, `scipy` (plots); `schemdraw` (ECE schematics, imported lazily).
All pinned in `../requirements.txt`.

## Tutor Studio (Teacher 2.0) — `whiteboard_server.py` + `whiteboard.py`

The **shared-canvas interactive** teaching surface (design: `../whiteboard.md`; static lessons
above remain the permanent archive). Stdlib-only local server on `127.0.0.1:8471`, opened as a
dedicated **app window** (Edge/Chrome `--app`). Default page = **canvas mode**: one infinite
Excalidraw whiteboard where the teacher's content (dialogue, rendered math, concept maps, plots,
schematics, images) lands **as objects on the board** and the learner **draws/types directly
over it** with the full tool set; **Ask** (typed or 🎤 voice — `via:"voice"`, read tolerantly)
sends the text + a PNG snapshot of the whole annotated board, which the engine reads *visually*;
the **camera** button drops a notebook photo onto the canvas; paste/drop of images is native.
Scene autosaves to `canvas.json`. The v2 stream layout (chat bubbles + separate sketch pad) is
kept at `/classic` as fallback.

```
import sys; sys.path.insert(0, "tools"); import whiteboard as wb
wb.start("verilog", unit="07-fsm")       # boots server if needed + opens the app window
wb.say("From memory - what did we cover last time?")     # teacher chat bubble
last = 0
while teaching:
    events, last = wb.listen(after=last, timeout=540)    # BLOCKS until the learner acts
    # ev["kind"] == "msg"     -> ev["text"]         (they typed)
    # ev["kind"] == "sketch"  -> Read ev["path"]    (they drew - look at the PNG)
    # ev["kind"] == "capture" -> Read ev["path"]    (camera / paste / drop)
    wb.say(...) / wb.math(...) / wb.map_(...) / wb.plot(...)   # respond in the window
wb.export_lesson()                       # freeze the session into a dated lessons/ file
```

Other helpers: `prose/code/process/table/structural/check` and
`wb.image(url=... | path=... | b64=..., source=REQUIRED)` — images may be **generated**
(plots/schematics/SVG, `source="generated: <how>"`) or **downloaded** (citation), whichever fits
(learner rule; `../whiteboard.md` §5). Session record:
`subjects/<subject>/whiteboard/<date>/session.json` — written on every change; same-day restart
resumes. Terminal remains the fallback surface if the Studio isn't running.

### examples/ — worked lessons + acceptance tests

Two end-to-end lessons that double as the subsystem's acceptance tests (`../rendering.md`), proving
the primitive map is subject-agnostic, not ECE-bound:

```
python tools/examples/lesson_rc_lowpass.py    # Test A: ece — uses the structural registry (schemdraw)
python tools/examples/lesson_sorting.py       # Test B: python — universal path, registers NO primitive-6
```

Each writes a self-contained `.html` beside itself (add `--open` to open it). Test A exercises the
structural-registry path (concept map → schemdraw schematic → matplotlib Bode → MathJax → CHECK);
Test B exercises the universal path with **no** structural renderer (concept map → flowchart →
complexity plot → highlighted code → comparison table → CHECK). They are also the template for the
"normal path": a lesson script computes its arrays, builds the spec dict, and calls `render`.
