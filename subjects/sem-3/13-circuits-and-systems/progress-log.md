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
- Next up: learner reviews the ⚠ corrections in `exam-pack/NOTES-class-notes-transcribed.md`;
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
