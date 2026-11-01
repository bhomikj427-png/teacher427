# ECE2130 Electronic Devices Lab-I — progress log

## Session resume
- Last session: 2026-10-31. Lab pack built: `study-pack/pdf/ECE2130-ED-Lab-pack.pdf` (83 pp., 17 files: start-here,
  LTspice primer, Exp 0–12, extra two-stage + design problem, revision set). Nothing taught live yet; no misses reported.

## Where we stopped
- 2026-10-31: pack complete and visually reviewed. Next: learner works through the pack (guess-first, then reads) and
  reports misses only; DSA lab manual still awaited.

## Log
- `[2026-10-31]` Learner request: prepare for the ED, DSA and DE labs; "only from those files do we need to actually
  be able to perform those experiments"; learner is at zero in ED and DSA, comfortable in digital; deliverable = a PDF
  that "teaches everything we will be needing to get marks". Only the ED and DE lab manuals are uploaded so far; DSA lab
  manual not yet received. Manual filed as `exam-pack/MANUAL-ECE2130-ED-lab-2025-26.pdf`.
- `[2026-10-31]` Gate note: the theory of this lab is ECE2101 (`../03-electronic-devices-1`, **stage-2✓**); the manual is
  the defined source for scope (same standing exception as a marathon over a defined book). Facts checked against the
  03 knowledge base (Boylestad); every expected number comes from running the manual's own circuits in LTspice
  (models BC547B, 2N2222, 2N3819, 2N5434, FDR6580, BZX84C6V2L, 1N914, 1N4007 all ship with LTspice).
- `[2026-10-31]` Building `study-pack/` (src/content/*.md + figures.py + build.py, same pipeline as 13's study pack) →
  `study-pack/pdf/ECE2130-ED-Lab-pack.pdf`. Simulations in `study-pack/src/sim/`.
- `[2026-10-31]` LTspice runs (`src/sim/sims.py` → `out/results.json`): all 13 circuits simulated as printed. Matches with
  the manual's own data: Exp 2 line/load tables digit-for-digit; Exp 9 drain table identical; Exp 4 min −9.39 V (manual
  −9.38 V); Exp 11 13.96 kHz (manual 13.76 kHz); Exp 8 ≈ 42 dB / ≈ 4 dB (manual plots).
- `[2026-10-31]` Manual errors found and documented in the pack (00-START-HERE table): Exp 0 RMS uses V_pp/√2;
  Exp 1 lists 1N4007 for a zener experiment; Exp 5 h21/h22 names swapped, "1/hoe = ΔIc/ΔVce", "Ib = 20 A", and 62 kΩ
  collector resistor makes the IB = 20/40 µA table impossible (Ic ≤ 0.16 mA); Exp 6 500 mV input clips (sim +2.9/−8.8 V);
  Exp 7 "input impedance ~hundred ohms" (actually ≈ 3 kΩ / 600 kΩ into base) and 10 V supply clips a 0.5 V input
  (negative half at −0.32 V, sim); Exp 9 r_d arithmetic slip 3.3 kΩ → 33 kΩ (sim 38.5 kΩ); Exp 12 conflates V_TH and V_M.
- `[2026-10-31]` Design problem (manual p. 3) solved and verified in LTspice (`src/sim/design.py`): CE (R_E1 = 82 Ω
  unbypassed) + emitter follower, 9 V: gain 59.7, R_in 16.2 kΩ, R_out 39 Ω, 2.95 V p-p unclipped, 2.68 mA.
- `[2026-10-31]` Built `study-pack/pdf/ECE2130-ED-Lab-pack.pdf`, 83 pp. Every chapter: map → primed terms → manual aim as
  question → guess-first → theory → circuit → Do-it steps → simulated curves/tables → calculation → record block
  (result + 15-line theory) → traps → check, answers at the end. All 41 figures visually reviewed; label overlaps and one
  clipped label fixed. Revision set (24 questions, one per idea) = file 16.
- `[2026-11-02]` This pack is now pages 2-84 of the merged `../_lab-ete-pack/Sem3-Lab-ETE-pack.pdf` (ED + DE + DSA, 222 pp.); the pack itself is unchanged.
