# ECE2102 Digital Electronics — Progress Log

> Written **live** as sessions happen (log-first artifact pairing; never reconstructed at
> wrap-up). Session-resume block is overwritten each session-end; Session history is append-only.
> See `../../README.md`.

## Session resume
- Last session: — (no teaching session yet)
- Where we stopped: subject scaffolded 2026-07-05 (engine audit) — KB was already `stage-2✓`
  (TEACH-READY, queue 2026-06-27); curriculum/profile/log created so activation needs no
  mid-boot improvisation. **No teaching yet; learner level undiagnosed.**
- Next up: **Session 1** — diagnostic (K-map probe, memory-boundary probe, latch-race probe),
  then open U1 via the loop at the placed level (U0 number-systems prereq: verify by retrieval,
  teach only gaps).
- Due for review today: nothing yet (no items mastered).

## Mastery ledger
*(empty — nothing mastered to criterion yet)*

## Spaced-review / relearning queue
*(empty — fills as items are mastered)*

## Session history
- [2026-07-05] Scaffolded (engine audit; no teaching): curriculum derived from 00-map,
  profile + this log initialized. KB state unchanged (`stage-2✓` since 2026-06-27).
- [2026-09-11] Inbox triage (no teaching): **first exam material received.** 11 files routed from
  `../_inbox/_unsorted/` into `exam-pack/` — professor's 8-deck slide set (syllabus + K-map +
  adders + MUX/demux + decoder/encoder + comparator/parity + shifter/ALU + sequential/FFs), one
  partial merged deck (decks 1-5), the **MTE PYQ (25-Sep-2025, 30 marks / 90 min)**, and a
  10-question practice set (combinational). Triage-log: `../_inbox/TRIAGE-LOG.md`.
  **Code discrepancy logged:** slide deck header reads **ECE 2105**, MTE paper + KB read
  **ECE2102** — same syllabus text; treated as a stale code on a reused deck, marked `uncertain`.
  Next artifact: `knowledge-base/exam-map.md` rebuilt from this evidence (was an inferred stub).
- [2026-09-11] `knowledge-base/exam-map.md` **rebuilt from evidence** (was an inferred stub):
  MTE structure settled (30 marks/90 min; Sec A 3x2 "memory", Sec B 4x4 "concept", Sec C 1x8
  "analytical"); **MTE scope resolved to U1 + U2 + U3-through-counters** (U4/U5 absent, corroborated
  by the decks stopping at flip-flops); 11 verified question patterns P1-P11 cited to paper/practice
  items; per-unit weights re-rated; teaching order re-set to K-map+constrained-realization ->
  MUX/decoder -> FFs/waveforms/counter design. Next artifacts: KB CHANGELOG + research-queue row.
- [2026-09-11] Learner request: **exam-ready study files (.md) to self-study from**, MTE scope,
  built to the universal preferences (ASCII math, scannable, flow-map-first, feed-big). Building
  `study-pack/` (10 files: 00 start-here/flow map, 01 Boolean+K-map, 02 NAND/NOR realization,
  03 adders/subtractors/parity, 04 MUX/demux, 05 decoder/encoder/7-seg, 06 comparator/shifter/ALU,
  07 flip-flops+waveforms, 08 counter design, 09 drill set). **Tension named to learner and logged:**
  passive reading is not studying -> every file is question-first with answers separated to the
  bottom, so the mechanism (retrieval) survives the format. Content sequenced by the 2026-09-11
  exam-map scoring order; facts from the Stage-1/Stage-2 KB, framing from the prof decks + PYQ.
- [2026-09-11] `study-pack/` **built — 10 files, ~3,465 lines**, all MTE scope. Every file is
  question-first (Map -> Attempt -> Method -> Worked -> Traps -> Self-test -> Answers-at-bottom);
  ASCII math throughout (no LaTeX, verified by grep); small per-file maps, not one dense tree.
  All 8 MTE-2025 questions and all 10 practice-set questions solved and verified by substitution;
  7-segment equations checked digit-by-digit against the display table. **No teaching event —
  nothing taught, nothing assessed, mastery ledger and review queue unchanged.**
- [2026-09-11] **Where we stopped:** study-pack delivered; learner has not yet worked any drill.
  Next session: start-of-session recall, then a live diagnostic against Drill A Section B to place
  level before teaching (`curriculum.md` U1 entry), scoring order per `knowledge-base/exam-map.md` §5.
