# ECE2107 Circuits & Systems — Progress Log

> Written **live** (log-first artifact pairing; never reconstructed at wrap-up). Session-resume block
> is overwritten each session-end; Session history is append-only. See `../README.md`.

## Session resume
- Last session: 2026-09-25 (no teaching; MTE study-pack build).
- Status: below `stage-1` as a subject (no KB of its own; facts anchored to `../06-circuits-and-network-theory/knowledge-base/`).
  Not teachable under the gate. The study pack is a learner-requested self-study artifact, not a lesson.
- Where we stopped: MTE study pack complete to the professor's syllabus: `study-pack/pdf/ECE2107-Circuits-and-Systems-study-pack.pdf` (73 pp.).
- Open questions for the professor: (1) Thévenin 2I: is the constant 2 Ω (set 2's 5.0025 V) or 2 kΩ (pack's 20/3 V)?
  (2) RL switch that opens: which path does the inductor current take after t = 0? (3) infinite ladder: do the values
  continue as primes? (4) class p.7 labels "4k/2k" vs working in Ω.
- Next up: learner works through the pack (Guess-first; mark clean/struggle/wrong); get the course hand-out + any PYQ.
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
- `[2026-09-25]` Learner request: MTE prep — extend the study pack to the professor's MTE syllabus. Inbox triage:
  `_inbox/_unsorted/33652e6a-….jpg` (handwritten MTE syllabus, dated 10/9/26) → `exam-pack/SYLLABUS-MTE-2026-09.jpg`;
  `WhatsApp Unknown 2026-09-25 at 4.26.41 AM.zip` (notes set 2, photos) → `exam-pack/NOTES-set2-2026-09/`.
  Plan: skim set 2 for new content + 2 conflicts only (superposition two-5 V case; Thévenin nodal route), add gap
  content (KVL/KCL, power sign convention, nodal/mesh, AC theorems, Laplace + test signals, 2nd-order RLC,
  lumped vs distributed), renumber to syllabus order, rebuild PDFs.
- `[2026-09-25]` Syllabus read (`exam-pack/SYLLABUS-MTE-2026-09.jpg`, dated 10/9/26): Part I = elements (R, L, C, IDS, DS);
  laws (VDR, CDR, power, energy, Ohm); KVL, KCL, source transformation; nodal + mesh/loop. Part II = superposition,
  Thévenin & Norton, MPT, each with DC and AC (and dependent / independent sources). Part III = first order
  (step-wise, Laplace, test signals u, r, δ); second order RLC (under-, over-, critically damped, undamped).
  Set 2 skimmed (22 photos, `exam-pack/NOTES-set2-2026-09/p01–p22`, send order): same lectures as set 1. **New in set 2:**
  lumped vs distributed parameters (p01); dependent-source device homework (VCVS = op-amp 741, CCCS = BC547,
  CCVS = "optical fibers", VCCS = MOSFET/lighting controls; p02–03); Z_L = Z_Th* (p14); RC switching with
  v_C(0⁻) = v_C(0⁺) (p20–21); standard test signals δ, u, r with ℒ pairs and examples (p22).
  **Conflicts:** (1) p09 two-5 V superposition: the teacher shorts the idle source, gets case 1 = case 2 = 0, I = 0 A,
  labelled LIMITATION; true I = 5 mA. (2) p11–12 Thévenin by nodal: V_Th = 5.0025 V. Solver shows this is exact for
  reading "2I" as **2 Ω × I** (V_Th 5.0025 V, R_Th 2999.5 Ω, I_L 1.2508 mA); the pack's 2 kΩ × I reading gives
  20/3 V, 8/3 kΩ, 20/11 mA. So it is a unit-convention mismatch, not an arithmetic error → question for the professor.
- `[2026-09-25]` New numbers verified by `study-pack/src/verify_mte.py` (nodal/mesh solves + ODE time simulation):
  KVL loop 12 V/2 k/4 k/4 V: i = 4/3 mA, powers 16 = 5.33 + 3.56 + 7.11 mW. Mesh 10 V/2 k/4 k/2 k/4 V: i1 = 2.2, i2 = 0.8 mA,
  node 5.6 V (nodal agrees). AC superposition 10 V DC + 10 cos 1000t, 1 kΩ + 1 H: i = 10 + 7.07 cos(1000t − 45°) mA (sim matches).
  AC Thévenin 10 V, 1 kΩ, 1 µF, ω = 1000: V_Th = 7.07∠−45° V, Z_Th = 500 − j500 Ω, I_N = 10 mA, P_max = 12.5 mW at
  Z_L = 500 + j500 Ω (sweep agrees). RC τ = 1 ms: step 1 − e^(−t/τ), ramp t − τ + τe^(−t/τ), impulse (1/τ)e^(−t/τ)
  (all sim-matched). Series RLC L = 1 H, C = 1 µF, 10 V step: R = 2.5 k over (−500, −2000), 2 k critical (−1000 double),
  1.2 k under (−600 ± j800, peak v_C 10.95 V at 3.93 ms), 0 undamped (10(1 − cos 1000t)); all sim-matched.
- `[2026-09-25]` Study pack restructured to the MTE syllabus order and rebuilt: `study-pack/pdf/` = 11 PDFs (00–10) +
  combined `ECE2107-Circuits-and-Systems-study-pack.pdf` (**73 pp.**, bookmarked). Files: 01 elements (+ lumped vs distributed,
  dependent-source devices) · 02 Ohm, dividers, power & energy (+ passive sign convention) · **03 KVL, KCL, source
  transformation (new)** · **04 nodal & mesh (new)** · 05 superposition (§5 rewritten to the set 2 version: 0 + 0 = 0 A vs
  true 5 mA; + §6 AC sources at different frequencies) · 06 Thévenin & Norton (nodal route; Note on 5.0025 V = 2 Ω reading,
  with a plot; + §6 AC Thévenin/Norton) · 07 MPT (+ worked conjugate match, 12.5 mW) · 08 first order (+ set 2 RC question,
  §6 Laplace route, §7 test signals δ, u, r) · **09 second-order RLC (new)** · 10 mock paper (20 numericals: 14 board + 6 textbook).
  16 new figures in `figures.py`. `build.py` fixes: `\sqrt{}` support; figure-token collision (FIGTOKEN1 matched inside
  FIGTOKEN10, misplacing figures in files with ≥ 10 figures). Every page of the combined PDF viewed; fixed during review:
  stale "0N —" titles after renumbering, form-feed chars from `\f` escapes, a markdown-eaten conjugate asterisk, label
  overlaps in the KVL/mesh figures, s-domain initial-condition source polarities (inductor + at bottom, capacitor + at top).
