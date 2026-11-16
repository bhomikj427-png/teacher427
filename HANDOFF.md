# Handoff — read at session start, then reset

> Written by the session that ended; read and **reset** by the next one (`CLAUDE.md`, session start
> step 0c). Holds only what the next session needs to start. History lives in `progress-log.md`s and git.

## Task (from the learner, 2026-11-16)

Two jobs. **Design first: build nothing until the learner signs off.**

1. **Write study-pack-format v1.3.** Start from v1.2 plus what the learner approved in EDC 01a/01b
   (`subjects/sem-3/03-electronic-devices-1/study-pack-v12/src/content/01a-*.md`, `01b-*.md`: the new depth model):
   - one idea per step, never merged
   - every symbol explained in words: what it counts, what sets it
   - every graph states its axes and what one point means (already in v1.2 §5.4)
   - a long topic is split into a/b files, not compressed (replaces the 4–8 page rule)

   Also add the efficiency rules agreed 2026-11-15:
   - a per-subject brief, built once before any file: slides transcribed (equations and slips included), question bank,
     constants checked against the KB, gaps filled up front, figure list
   - a shared figure library and an automatic label-overlap check in `tools/`
   - `tools/study_pack_build.py`: building one file must not overwrite the combined PDF
   - one short fresh session per 1–3 files (`auto.py` where possible)

   Show the learner the v1.3 diff and the plan, then wait for sign-off.
2. **After sign-off:** plan the upgrade of the three v1.2 packs to v1.3:
   `01-statistics-and-probability` (18 files), `03-electronic-devices-1` (19), `04-digital-electronics` (21), all in
   `study-pack-v12/`. Order: each pack's START-HERE priority. EDC 01a/01b already meet v1.3, so don't redo them.
   Give the learner the order, the per-session batches, and the decisions they need to make.

## Read first

`study-pack-format.md` · EDC `01a`/`01b` content files above · `subjects/sem-3/03-electronic-devices-1/study-pack-v12/src/{build.py,figs_u1.py,verify_u1.py}`
· `tools/study_pack_build.py` · `auto.py` (memory: unattended runner).

## Speed: the learner wants this done properly *and* quickly

- v1.3 design: present it **in one turn**, as a compact diff and a plan, not a long essay. Then build.
- Rebuilds: one short fresh session per 1–3 files. Write the next batch into this file at the end of each session.

## What "depth" means in practice (from 01a/01b; write these into v1.3)

- **Open on a concrete anchor** before any formula: 01b's "seats × chance a seat is filled" (cinema analogy). Every later
  formula is read back in those words ("N_C = how many seats; the exponential = chance one is filled").
- **Every figure gets a "Reading the figure" line or a "What this graph plots:" caption**: each axis and what one point
  means. Then a small table reading the curve at 3–4 points with numbers (01b step 2).
- **Every Predict is answered explicitly** ("Answer to the Predict: …"). Every step opens with a one-line bridge saying
  why it is needed.
- **Define a symbol by what it counts and what sets it**, not by its name. "N_C: effective density of states" was the
  defect; the fix was "the seats that, all placed at E_C, would hold the same electrons".
- **Derivations: numbered lines, each one following from the line before**, with the approximation named at the line
  where it enters.
- **Professor slips get a note box** where they occur (01b: deck slides 36, 38).
- **Step count is set by the ideas.** 01b has 10 steps on what v1.2 had compressed into 1.

## Mechanics that cost time last session (avoid)

- Git Bash heredocs mangle `\n` inside inline Python. Write a `.py` file to the scratchpad and run it instead.
- `tools/study_pack_build.py build(only=…)` **rewrites the combined PDF with only those files**. Fix this first (tooling),
  or always run the full build.
- Slides: `python-pptx` is not installed. Read slide text with `zipfile` + a regex on `ppt/slides/slideN.xml`; images
  are in `ppt/media` (via `_rels`). Many equations exist **only as images**, so view them.
- Page review: render with `pymupdf` (`import pymupdf`) to low-dpi contact sheets, 4 pages per image. Zoom only on
  suspect figures. Every image stays in context and is re-sent on every turn, so keep it to one pass.
- Figure helpers (`study-pack/pdf/figs.py`): `_svg()` turns `X_y` into mathtext subscripts. `e^{x}` in a plain label
  prints literally, so wrap it in `$…$`. The `∝` glyph is missing from mathtext: write "grows as". Overlaps came
  from annotation text placed inside lattices/axes: put labels outside the drawing.
- KB gaps (constants the slides use but the KB lacks) were found mid-build. The per-subject brief must catch them first.
