# ECE2102 Digital Electronics — Learner Profile

> Current level, goals, known/observed misconceptions, and subject-specific preference overrides.
> Maintained by the engine via the self-update protocol (`../../../CLAUDE.md`).
> Scaffolded 2026-07-05 (engine audit — subject is `stage-2✓`/TEACH-READY); **level undiagnosed —
> first session opens with the diagnostic, per protocol.**

## Goal
- MUJ sem-3 core: score on MTE + ETE (Stage-1 set first, scoring-over-depth), then Stage-2 depth.
  Direct substrate for the verilog/RTL career track — every block here is what verilog models.

## Current level — **undiagnosed** (diagnose at first session, re-diagnose every answer)
- Prior signal available (verify, don't assume): verilog work shows half/full adder built in HDL
  and the 2026-07-03 flow map places combinational logic as current ground — so U1 material may be
  partly known **at the HDL level**; K-map fluency, MSI blocks, and sequential foundations are
  unknown. The verilog profile also flags **sequential-logic foundations as an open diagnostic** —
  this subject's U3 is where that gets settled.
- First-session probes: minimize a 4-var K-map with don't-cares (U1 threshold); combinational-vs-
  sequential boundary (U3 threshold); why a latch races / what edge-triggering fixes.
- **Cross-subject caution:** mastery here and in verilog are logged separately — an item mastered
  as HDL behavior is not automatically mastered as gate/K-map procedure, and vice versa.

## Known / suspected misconceptions to watch
*(from `knowledge-base/misconceptions.md` M1–M21 — confirm via retrieval, don't assume)*
- K-map as a magic grid rather than visual Boolean adjacency — blocks 5-var/POS/don't-cares.
- De Morgan memorized but unusable for AOI→NAND conversion (universality not operational).
- All circuits treated alike (no memory boundary) — the deepest split, probe early.
- Level-vs-edge confusion on flip-flops; "logically correct = works in hardware" (timing blindness).

## Preferences (overrides)
*(Subject-specific only; win over `../../../learner-preferences.md` inside this subject. None yet.
Note: the learner's verilog override — no gate-level reproduction drills — is verilog-scoped; in
THIS subject gate/truth-table derivation IS the exam skill. If tension appears, surface it and log
it here, don't silently import the override.)*

## Tensions to manage
- None yet.
