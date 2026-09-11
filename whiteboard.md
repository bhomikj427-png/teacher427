# whiteboard.md — Teacher 2.0 Studio: the one-window interactive tutor surface (design doc)

> The v2 teaching surface, learner-directed. Extends `rendering.md` — static dated lessons
> (`render_lesson.py`) remain the permanent archive; the Studio is the **live, interactive**
> surface. Implemented by `tools/whiteboard_server.py` (server + page) + `tools/whiteboard.py`
> (engine client). If code and this doc disagree, reconcile — neither silently wins.
> Delivery, not pedagogy: nothing here overrides a core principle (retrieval, mastery gating,
> feedback rules all apply *inside* the window exactly as they did in the terminal).
>
> History: scaffolded 2026-07-05 as a one-way board + sketch pad; **upgraded same day to the
> one-window Studio at the learner's direction** ("interactive window… I draw or type whatever
> and u type back with explanation and diagrams, correcting where I went wrong; camera for my
> notebook; a proper tool"). That direction supersedes the v1 split below.

## §0 v3 — CANVAS mode (the default page; learner-directed 2026-07-05)

The learner's third redirect: *"what u generate itself should be the whiteboard — I draw over
your explanations and ask questions directly."* So the stream/drawer split is gone from the
default page; the surface is now **one shared infinite whiteboard**:

- **Tool research (2026-07-05):** requirements = engine-drivable programmatic canvas + learner
  ink over engine content + snapshot readback. Verdict: **Excalidraw** (MIT, no license keys
  ever, esm.sh no-build embed, `updateScene`/`addFiles`/`exportToBlob`/`convertToExcalidrawElements`,
  native image paste/drop). Runner-up tldraw (nicer SDK, but license-key regime — dev-mode-only
  free). Off-the-shelf apps (OneNote/Miro/tldraw.com) rejected: none let the local engine with
  the subject KBs drive the board and read back ink — that link is the whole product.
- **Teacher content = canvas objects.** `say`/`prose`/`check`/`code`/`table` → text elements;
  `math` (MathJax tex-svg) / `map`/`process` (Mermaid) / `plot`/`structural` (matplotlib/
  schemdraw SVG) / `image` → image elements. Placed down a column (y-cursor), tagged
  `customData.blockId` so a reload never re-places them. Light board (#fdfdf8) — figures are
  black-on-white.
- **The learner draws/types/erases ANYWHERE with the full Excalidraw tool set** — over, around,
  on top of teacher content. Circling a node and writing "why?" next to it *is* the question.
- **Ask = board snapshot.** The dock's Ask (typed or 🎤 voice) POSTs `/ask`: the text + a PNG
  export of the entire annotated canvas → inbox event `ask` → the engine Reads the PNG and sees
  exactly what was circled/written and where; it answers by adding objects to the board.
- **Camera** drops the notebook photo ON the canvas (position it, annotate it, Ask). Paste/drop
  of images is Excalidraw-native.
- **Scene autosave**: elements+files → `canvas.json` (debounced, every change survives); the
  block log (`session.json`) still records the dialogue/content sequence for export and the
  progress-log record.
- The v2 stream layout survives at **`/classic`** as the fallback surface.

## §1 The Studio model (v2 — now the /classic fallback; §0 supersedes as default)

**One app window carries the whole session** (launched via Edge/Chrome `--app` mode — a dedicated
window, no tabs/URL bar; the browser engine is the rendering runtime, same architecture as
Electron/VS Code — that's what makes math/diagram rendering first-class, not a shortcut):

- **Teacher → learner:** chat bubbles (`say`), prose, rendered math, concept maps, plots,
  schematics, tables, code, CHECK cards, images — pushed live (SSE), appearing instantly.
- **Learner → teacher (four channels, all producing events the engine reads):**
  1. **Type** — the chat bar; 2. **Draw** — the sketch pad; 3. **Camera** — photograph the
  notebook page (`getUserMedia`; localhost is a secure context); 4. **Paste / drag-drop** — any
  screenshot or image file. Channels 2–4 save PNGs **the engine reads visually**.
- **The terminal remains the engine's runtime and the fallback surface** (Studio down → teach in
  the terminal per `rendering.md`/ASCII rules; nothing is ever blocked on the Studio).

**The interactive loop:** the engine long-polls `GET /inbox` (blocking; `wb.listen()`), so a
session is: push → wait for the learner's message/sketch/photo → read it (visually if an image) →
respond in-window with explanation + diagrams + corrections → repeat. One-on-one, in one window.

## §1b What it adds over the static lesson surface

| | Static lesson (`rendering.md`) | Studio (this) |
|---|---|---|
| Update mid-session | re-render + reload file | **live push** (SSE) |
| Direction | one-way | **full duplex** — typed chat + sketches + camera/paste/drop, all read by the engine |
| Dialogue | terminal | **in-window** (chat bubbles; terminal = fallback) |
| Images | computed only | **generated or downloaded, situationally** (§5) |
| Persistence | one dated HTML | `session.json` (blocks + learner events) per subject/day; exportable to a static lesson |

## §2 Architecture (deliberately boring)

- **`tools/whiteboard_server.py`** — Python **stdlib-only** local server (`http.server` +
  threads + Server-Sent Events), bound to `127.0.0.1:8471`. No new dependencies, no cloud, no
  build step. Serves one self-contained page (same pinned CDN stack as `render_lesson.py`:
  MathJax / Mermaid-neutral / highlight.js).
- **`tools/whiteboard.py`** — the engine-side client. `start(subject)` boots the server (detached)
  and opens the tab; `push(block)` / helpers append blocks; `latest_sketch()` returns the newest
  learner sketch path for the engine to Read; `export_lesson()` freezes the session into a normal
  dated lesson under `lessons/`.
- **Blocks are the same spec language as `rendering.md` §3/§4** (prose, math, code, map, process,
  table, plot, structural, timing, check) **plus `image` and `sketch`**. `plot`/`structural` are
  rendered server-side through `make_figure` (same registry, same fallback rule) and pushed as
  inline SVG. One spec language everywhere → any whiteboard session can be re-rendered as a
  static lesson and vice versa.

## §3 Session persistence (live-logging discipline applies to the board too)

```
subjects/<subject>/whiteboard/<YYYY-MM-DD>/     (flat, one folder per session-day)
├── session.json                # ordered block log — rewritten on every push (no end-of-session
│                               #   reconstruction; an abrupt exit loses nothing)
├── sketch-HHMMSS[-label].png   # learner drawings, saved on the learner's click
└── img-<name>.<ext>            # downloaded/copied sourced images served to the page
```

Same-day restart **resumes** the existing session (the page replays `session.json`). The board is
an artifact of the session, so the **log-first rule holds**: a teaching session records to
`progress-log.md` what the board was used for, as it happens.

## §3b Subject integration (the Studio is a surface, NOT a separate system)

A Studio session **is** a normal teaching session — every engine rule fires exactly as if it ran
in the terminal:

- **Keyed to the subject:** `wb.start(subject)` files everything under
  `subjects/<subject>/whiteboard/<date>/`; the teaching gate (`stage-2✓`), the curriculum, and
  the learner profile of *that subject* govern what gets taught in the window.
- **Session start:** integrity check + learner-recalls-first + due-review sweep run before new
  content — in the window (`say` + CHECK blocks) instead of the terminal.
- **Live logging (log-first):** a mastery CHECK passed in the window → mastery-ledger entry +
  spaced-review queue entry with next-due date, *then* continue; "Where we stopped" is updated as
  each step completes. `session.json` records the *surface* trace automatically, but it does
  **not replace** `progress-log.md` — the progress log stays the single resume record, written
  live as always.
- **Learner artifacts = evidence:** a saved sketch/photo that demonstrates mastery is cited in
  the ledger by filename (e.g. "mastered FSM state diagram — evidence: sketch-1432-fsm.png").
- **Preferences flow in:** universal + subject overrides load at session start and shape the
  window's delivery (feed-big pacing, no-scaffolding language, flow-map-first — all unchanged).
- **Wrap-up:** identical ritual; `wb.export_lesson()` additionally freezes the visual record
  into the subject's `lessons/` archive.

## §4 The learner input channels ("better draw myself" + voice)

**Mic (Web Speech API):** the 🎤 button dictates into the chat box — words appear live, the
learner edits any mis-heard term, then sends. Messages carry `via: "voice"` so the engine reads
them tolerantly (ASR mangles technical terms — "assign" → "a sign"; same caveat class as NPTEL
captions). Recognition runs through the browser's speech service (Edge/Chrome); no install.

## §4b The learner sketch pad ("better draw myself")

A canvas drawer built into the page (pen / highlighter / eraser, colours, width, undo, clear).
**Save** posts the drawing to the server → PNG lands in the session folder → the engine reads it
*visually* and responds in the terminal. Uses, in loop terms:
- **TEACH-BACK / CHECK:** "draw the FSM for this spec, save it" → engine inspects the actual
  diagram, targets feedback at the error (task/process feedback, after a retrieval attempt).
- **GUIDE:** learner sketches a partial attempt; engine hints minimally at the drawn state.
- Sketches are **retrieval evidence** — they may be cited in the mastery ledger like any other
  demonstration.

## §5 Images — GENERATE or DOWNLOAD, whichever fits (learner rule, 2026-07-05)

The learner's rule supersedes the old blanket no-generation line: the teacher may **generate or
download images situationally**. The honesty mechanics that survive:

- **Generated (preferred for anything quantitative or structural):** matplotlib plots, schemdraw
  schematics, Mermaid maps, hand-built SVG — the engine controls every line, so the figure is
  faithful by construction. `source: "generated: <how>"`.
- **Downloaded (for what can't be computed):** photos, device cross-sections, die shots, real
  scope traces — from authoritative origins; `source` = the citation. Content claims in the image
  are tiered per `subject-research-protocol.md` §2 like any claim.
- **Diffusion/AI-generated imagery:** allowed *in principle* under the learner's rule, but (a) no
  image-gen API is wired in this environment, and (b) if one is added, its output is a *claim
  generator* — every technical detail in such an image must be verified before it is taught, same
  as any unsourced content. Programmatic generation stays the default because it needs no such
  audit.
- The server still **rejects any image without a `source`** — provenance is always stated.

## §6 HTTP surface (for the engine; all localhost)

```
GET  /            the studio page (chat + stream + sketch pad + camera)
GET  /events      SSE stream — replays session.json, then live blocks
GET  /status      {subject, date, dir, n_blocks, last_event, events:[recent]}
GET  /inbox?after=N&timeout=S   LONG-POLL learner events (msg/sketch/capture) — the engine's ear
POST /push        one teacher block (spec JSON) → {ok, id, fig}
POST /image       {url|path|b64, source, caption} → saves + pushes an image block
POST /msg         {text} — learner chat (page); shows in stream + lands in the inbox
POST /sketch      {png: dataURL, label} — learner drawing (page) → PNG + inbox event
POST /capture     {png, label, via: camera|paste|drop} — learner photo/screenshot → PNG + inbox event
POST /session     {subject, unit?} → switch/open a session
POST /export      freeze session → static dated lesson via save_lesson → {path}  (POST with {} body)
GET  /files/<f>   serve a file from the session folder (flat, no traversal)
```

## §7 Open items (design tail — revisit after first real use)

- WaveDrom timing blocks on the live board render via a try/catch shim (static lessons remain the
  reference for timing-heavy lessons) — promote once exercised.
- Excalidraw as an optional richer sketch layer (shapes/arrows/text) — the sketch-pad API is
  already just "PNG in, path out," so it can be swapped in without touching the engine side.
- Contract integration (CLAUDE.md rendering section pointing here as default surface) — after
  learner sign-off.
