# ECE2107 Circuits & Systems — Progress Log

> Written **live** (log-first artifact pairing; never reconstructed at wrap-up). Session-resume block
> is overwritten each session-end; Session history is append-only. See `../README.md`.

## Session resume
- Last session: 2026-09-25 (no teaching).
- Status: **folder created by inbox triage only — no knowledge base, below `stage-1`.** Not teachable
  (teaching gate: `stage-2✓`). Content overlaps heavily with `../06-circuits-and-network-theory/`
  (ECE2120, `stage-1✓`), which was built for the old scheme; whether 06's KB is re-used for ECE2107
  is part of the batch re-map the learner still has to confirm (`../research-engine/research-queue.md`).
- Where we stopped: learner's handwritten class notes transcribed + verified (see below). No teaching.
- Next up: learner reviews the re-checked summary (slips, not method errors) in `exam-pack/NOTES-class-notes-transcribed.md`;
  get the ECE2107 course hand-out (syllabus, textbook, MTE boundary) into the inbox.
- Due for review today: nothing.

## Mastery ledger
*(empty)*

## Spaced-review / relearning queue
*(empty)*

## Session history
- `[2026-09-25]` Inbox triage: `Adobe Scan 12 Sept 2026.pdf` (23-page scan of the learner's own
  handwritten notes, titled "Circuits & Systems") → `exam-pack/NOTES-handwritten-2026-09.pdf`.
  Folder `13-circuits-and-systems/` created for it (same precedent as 11 and 12). Pages rendered with
  PyMuPDF (installed this session; the machine has no poppler) and read visually.
- `[2026-09-25]` Transcribed → `exam-pack/NOTES-class-notes-transcribed.md`. Every formula and every
  worked answer re-derived; cross-checked against `../06-circuits-and-network-theory/knowledge-base/01-network-theorems.md`
  + `02-transient-analysis.md` (textbook-sourced), Alexander & Sadiku ch. 1 (active/passive definition), and
  7809 datasheet summaries. Found **5 errors in the notes** (inductor law written with C; superposition
  answer mixes mA and A; MPT source power 0.5 mW → 5 mW; RL question at t=0⁺ has I_R ≠ I_L in a series
  loop; "active element needs no external energy" contradicts "amplifier is active") and **3 gaps**
  (superposition doesn't apply to power; dependent sources are never switched off; P_max = V_th²/4R_th).
  Lab pages: 20 Vpp into a bridge gives ~8.6 V peak, which is below a 7809's ~11 V minimum input.
- `[2026-09-25]` Re-check at the learner's request ("teacher's notes shouldn't have big mistakes").
  Re-read every flagged passage at 260 dpi and simulated every circuit with a nodal solver
  (`verify.py`, scratchpad). **Revised verdicts:** p.7 superposition: with 4 Ω/2 Ω the full-circuit solve
  gives **exactly 3 A**, the notes' answer, so the method and answer are right and only the "k" labels clash
  (was E3 "wrong", now a unit-label slip). p.16 "0 5 mW": no decimal point is visible, so it may read 5 mW
  (was E4 "wrong", now ❓). p.9: both sources + on top; "remove, don't short" gives 5+5 = 10 mA vs the true
  5 mA, which is most likely the teacher's **demonstration of limitation 3**, not an error. p.3 C-for-L =
  pen slip (the side box has ψ = Li). p.22–23 RL: kept as a question to clarify, not a teacher error.
  All numeric answers in the notes and all my additions confirmed by simulation: p.5 5.33/2.67/4 A;
  p.11 I_L = 20/11 mA (V_oc 6.67 V, I_sc 2.5 mA, R_Th 2.67 kΩ); MPT sweep peak at R_L = 10 kΩ, 2.5 mW;
  RL step Euler sim matches (V/R)(1−e^(−t/τ)), τ = 1 µs; 5τ = 99.3 %; ladder 2.3177 kΩ.
- `[2026-09-25]` Learner request: "make my study pack … convert the files into clean pdfs with diagrams".
  Building `study-pack/` (v3 question-first shape: Q → guess → taught answer → Check; Exam form,
  Attempt, Traps, Self-test, Answers). Output = one PDF per file + one combined PDF, built by
  `study-pack/src/build.py`: schemdraw circuits, matplotlib plots, HTML → Chrome headless → PDF.
  **Gate note:** ECE2107 has no KB of its own (below `stage-1`). Facts are anchored to
  `../06-circuits-and-network-theory/knowledge-base/` (textbook-sourced, `stage-1✓`, same topics) plus the
  simulation-verified notes. Question base: P1 = the professor's board questions in the learner's notes
  (12 items); P2 (textbook problems) = empty, stated as such. This is the first build of the parked
  pictorial-pack design (`../../../_PARKED-visual-study-packs.md`, option C: PDF). It stays local to
  this subject; no engine files (CLAUDE.md, rendering.md, tools/) are edited.
- `[2026-09-25]` Study pack built: `study-pack/pdf/` = 8 PDFs (00–07) + `ECE2107-Circuits-and-Systems-study-pack.pdf`
  (45 pp., bookmarked). 32 figures (schemdraw circuits for every board question and every solution sub-circuit;
  matplotlib plots: AC division, ladder convergence, MPT power/efficiency sweep, first-order curves,
  continuity). Every page visually reviewed. Fixes made during review: CCVS polarity drawn upside down in
  the first render; mixed text+math labels lost text in schemdraw (all math labels now pure math); nested
  fractions not rendering. Source of truth = `study-pack/src/` (`build.py`, `figures.py`, `content/*.md`);
  rebuild with `python build.py`.
