# rendering.md — the Visual & Rendering subsystem (design doc / source of truth)

> The spec the two renderer tools implement (`tools/make_figure.py`, `tools/render_lesson.py`).
> Those tools cite this file by section (§2 two-surface rule, §3 the six primitives + fallback,
> §5 the registry). If the code and this doc disagree, treat the disagreement as a bug to
> reconcile — neither silently wins. Plumbing for *delivery*, not pedagogy: it changes **how** a
> lesson is shown, never **what** the five principles require.

## §1 Why this exists (the two pains it solves)

Two standing learner preferences (`learner-preferences.md` §3) cannot both be served by the
terminal alone:

- `[stated 2026-06-19]` **LaTeX / `$...$` math does not render in the learner's terminal** — it
  shows as raw symbols and reads as clutter.
- `[stated 2026-06-21]` **The learner demands a clean, scannable UI** — low tolerance for messy
  output; wants real diagrams, not paragraphs describing diagrams.

ASCII-only math and hand-drawn ASCII diagrams are the *terminal* fallback, and remain correct
there. But genuine rendered math, plots, and circuit schematics need a real rendering surface.
This subsystem adds that surface **without** moving the teaching dialogue out of the terminal.

It serves autonomy/relatedness (SDT, `research/05 Part B`) by honoring a stated delivery
preference. It is subject-agnostic by construction (§5) and **never** overrides a core principle:
the retrieval, the CHECK question, and its answer still happen in the terminal (§2).

## §2 The two-surface rule (load-bearing)

There are exactly two surfaces, and they never duplicate content:

- **Terminal = the control channel.** Stays plain ASCII. All dialogue, questioning, retrieval
  prompts, hints, and CHECK answers live here. This is where teaching *happens*. It must remain
  fully usable on its own — the lesson tab is an enhancement, never a prerequisite.
- **Browser tab = the lesson surface.** A single self-contained HTML file (`render_lesson.py`)
  holding the figures, rendered math, tables, and code that the terminal can only gesture at.

The handoff is by reference, not by repetition: the terminal says *"→ figure 2 in the lesson
tab"*, and figure 2 lives only in the tab. Figure-bearing blocks are auto-numbered `Figure N` so
the terminal can point at them unambiguously. A CHECK may *carry* a figure into the tab, but the
question-and-answer exchange itself still happens in the terminal (the tab hides the answer behind
a disclosure only as a self-study convenience).

**Consequence for the engine:** never paste a wall of TeX or an ASCII-art plot into the terminal
when a primitive exists. Build the lesson spec, render it, point at the figure number.

## §3 The six visual primitives (+ the fallback rule)

Every figure a lesson needs reduces to one of six primitives. Five are dependency-light client-side
JS (zero Python); two need real computation and are pre-rendered to inline SVG by `make_figure.py`
(primitive 4 fully; primitive 6 partly). Block `type` in the lesson spec is given in brackets.

| # | Primitive | Rendered by | Block type |
|---|-----------|-------------|------------|
| 1 | Math / derivation | MathJax (CDN) | `math` |
| 2 | Relationship graph / concept map | Mermaid (CDN) | `map` |
| 3 | Process / sequence / state | Mermaid (CDN) | `process` |
| 4 | Quantitative plot | matplotlib → SVG (Python) | `plot` |
| 5 | Tabular / comparison / truth grid | HTML + CSS | `table` |
| 6 | Domain structural diagram | registry → SVG (Python), or WaveDrom (CDN) | `structural` / `timing` |

Plus three support blocks: `code` (highlight.js, CDN), `prose` (minimal markdown — `**bold**`,
`` `code` ``, `- ` bullets), and `check` (a styled retrieval prompt with an optional disclosed
answer).

**The fallback rule (never block a lesson on a missing renderer).** Primitive 6 is the only
subject-specific slot (§5). If a `structural` block is requested for a subject with no registered
renderer, `make_figure.py` raises `NoStructuralRenderer`; `render_lesson.py` catches it and either
renders the block's `fallback` (typically a Mermaid `map`/`process` or a `plot`) plus a one-line
note, or emits a visible `[no figure]` placeholder. A lesson always renders.

## §4 The lesson spec (the declarative contract)

A lesson is data, not code. The teaching script computes any arrays (numpy/scipy) and assembles a
plain dict, then calls `render(spec, "out.html")`. Shape:

```
{
  "title":   str,
  "subject": str,                  # routes primitive-6 structural figures through the registry
  "intro":   str (optional markdown),
  "sections": [ {"heading": str, "blocks": [ <block>, ... ]}, ... ]
  # a flat top-level "blocks" list is also accepted (wrapped in one untitled section)
}
```

Each `<block>` is one of the types in §3. Figure-bearing blocks may carry a `caption` and are
auto-numbered `Figure N`. Per-block fields are documented in the tool docstrings (the authoritative
field reference); this doc fixes the *model*, the docstrings fix the *fields*.

## §5 The renderer registry (subject-agnostic extensibility)

The dispatcher (`make_figure.make_figure`) routes by figure **kind** — never by subject. Subject
only matters inside primitive 6, which is an **extensible registry**, not a fixed switch:

```
register_structural("<subject>", handler)   # handler(spec) -> inline SVG string
```

Adding a domain's structural renderer touches that one call, never the dispatcher. We ship one
entry: `"ece" -> schemdraw` (circuits, op-amps, gates), with schemdraw imported lazily inside the
handler so a subject that never draws a schematic carries no dependency on it. A new subject that
needs structural diagrams registers its own handler; until it does, the §3 fallback covers it.

## §6 Determinism

A given spec renders byte-stable across runs: fixed font (`DejaVu Sans`, ships with matplotlib),
font size, figure size, dpi, and a fixed Okabe-Ito colour cycle (never matplotlib's default, which
shifts between versions). CDN dependencies are major/minor pinned. No network calls at lesson time
except the pinned CDN `<script>`/`<link>` tags.

## §7 How the engine uses it (in the teaching loop)

The subsystem is invoked during **PRESENT / MODEL / CHECK** when a concept needs real math, a plot,
or a structural diagram that the terminal can't show cleanly:

1. Build the spec in the lesson script (compute arrays first; keep handlers pure — data in, not
   code).
2. `from render_lesson import render; render(spec, "<scratch>/lesson.html")` — writes and opens the
   tab.
3. In the terminal, continue the dialogue in ASCII and reference figures by number.

The terminal still owns the loop. The tab is where the math and figures *land*; it is never where
the retrieval happens.

## §8 Persistence & layout (where rendered lessons live — permanent)

A rendered lesson is a **durable artifact**, not a temp file. It is saved to a fixed, dated,
per-subject home so it persists across sessions and sits beside the subject it belongs to — never
in a scratch/temp directory.

**Canonical path:**
```
subjects/<subject>/lessons/[<unit-slug>/]<YYYY-MM-DD>-<concept-slug>.html
```
- **Per subject** — lessons live next to that subject's `knowledge-base/` and `progress-log.md`.
- **Dated + slugged** — re-rendering the same concept on a later day writes a *new* file; an
  earlier day's copy is never clobbered. (Same concept, same day → same filename, intentionally
  overwritten — it's the same lesson refined.)
- **Optional unit subfolder** — if the spec carries `"unit"`, lessons group under
  `lessons/<unit-slug>/` for arrangement; otherwise they sit flat in `lessons/`.

**How to save (the engine path):** call `save_lesson(spec)` (`render_lesson.py`) — it derives
subject/concept/unit from the spec and routes to the canonical path. `render(spec, outpath)` is the
low-level escape hatch that writes to an exact path; teaching sessions use `save_lesson`.

**Source of truth.** The HTML is *generated*; the lesson **script** (which builds the spec) is the
reproducible source. Both persist: the script under the subject (or `tools/examples/` for the
subsystem's own demos), the HTML under `lessons/`. A lost HTML is always re-renderable from its
script.

**Two exceptions that do NOT go under a subject's `lessons/`:**
- `tools/examples/*.html` — the subsystem's own acceptance-test demos; regenerable, kept beside
  their scripts.
- Throwaway smoke tests — use the scratch dir explicitly; never a subject's `lessons/`.

The research gate still applies: a real lesson (hence a file under `lessons/`) only exists for a
subject at `stage-2✓` (§ none-below-gate, `CLAUDE.md`).

## §9 Files & dependencies (v2 note)

**Teacher 2.0 extension:** a **live two-way whiteboard** now exists on top of this subsystem —
same block/spec language, same primitives, plus live push (SSE), a learner sketch pad (saved
sketches are PNGs the engine reads visually), and a sourced-`image` block (citation required; the
no-image-gen rule of §5 unchanged). Design: **`whiteboard.md`**; code:
`tools/whiteboard_server.py` + `tools/whiteboard.py`. Static dated lessons (this file) remain the
permanent archive; a whiteboard session can be exported into one. Original §9 content follows.

### Files & dependencies

- `tools/make_figure.py` — Python figure renderer (primitives 4 + 6); the registry lives here.
- `tools/render_lesson.py` — assembles the self-contained HTML lesson surface; imports `make_figure`.
- `requirements.txt` — pinned deps. Primitive 4: `matplotlib`, `numpy`, `scipy`. Primitive-6 ECE
  entry: `schemdraw` (lazy). Client-side primitives (1,2,3,5,code,timing) need no Python deps.
- `tools/README.md` — operational usage for both tools.
