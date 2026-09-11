# ECE2101 — exam-map (marks-aiming map) — PROVISIONAL STUB

> **Status: `uncertain` — no PYQ/PPT ingested yet** (`../exam-pack/` is empty as of 2026-06-24).
> Per `two-stage-depth.md`, Stage 1 is meant to be *PYQ/PPT-driven*; until material is dropped in,
> weightage below is **inferred** from standard ECE-UG course emphasis + the prescribed textbooks,
> **not** from MUJ evidence. Every weighting here is a hypothesis to be replaced, not a finding.
> Honesty split (`exam-resources.md`): a PYQ/PPT is tier-1 for *what is asked*; never for *what is
> true*. Rebuild this file the moment papers arrive.

## Inferred topic weightage (HYPOTHESIS — replace with PYQ evidence)

| Unit | Topic | Inferred weight | Likely question types | Conf |
|------|-------|-----------------|------------------------|------|
| U1 | Semiconductor physics (bands, doping, drift/diffusion, resistivity, sheet R) | Med | Numerical: nᵢ/n/p, conductivity, resistivity, sheet R; short-answer mechanism; Einstein relation | `uncertain` |
| U2 | PN junction physics (depletion, Vbi, I-V, breakdown, Zener, Schottky) | **High** | Derive/state Shockley eqn; Vbi & depletion-width numericals; junction capacitance; compare avalanche vs Zener | `uncertain` |
| U2 | Diode circuits (rectifiers, clippers, clampers, Zener regulator) | **High** | Design/analyze: ripple, PIV, regulator with load line; sketch output waveform of clipper/clamper | `uncertain` |
| U3 | JFET (construction, characteristics, Shockley eqn, applications) | Med | Shockley eqn numericals (ID from VGS); pinch-off/VP; transfer vs output curves; biasing | `uncertain` |
| U4 | MOSFET (regions, square-law, small-signal, CS/CG/CD, switch, digital) | **High** | ID in triode/sat numericals; small-signal gm/gain of CS amp; MOSFET-as-switch & inverter (VTC) | `uncertain` |
| U5 | BJT (construction, characteristics, comparison with MOSFET) | Med | Characteristics & regions; α/β relations; compare BJT vs MOSFET (table); biasing basics | `uncertain` |

## Recurring numerical patterns to drill (textbook-derived, pending PYQ confirmation)

1. Given doping → carrier conc (n·p=nᵢ²), conductivity σ=q(nμn+pμp), resistivity, sheet resistance.
2. PN junction: built-in potential Vbi=V_T·ln(N_A N_D/nᵢ²); depletion width; junction capacitance.
3. Diode I-V: I=I_S(e^{V/ηV_T}−1); find I or V; load-line / iterative / piecewise-linear solution.
4. Rectifier: V_dc, ripple factor, PIV, ripple with filter capacitor (V_r ≈ I/(fC)).
5. Zener regulator: choose R_S, find I_Z range across line/load variation; power dissipation.
6. JFET: Shockley ID=I_DSS(1−VGS/VP)²; self-bias / fixed-bias Q-point; gm.
7. MOSFET: triode vs saturation test (VDS vs VGS−Vt); ID square-law; gm=√(2kₙ′(W/L)ID); CS gain ≈ −gm(ro∥RD).
8. BJT: IC=βIB, IE=(β+1)IB, α=β/(β+1); region identification from terminal voltages.

## MTE vs ETE split

`uncertain` — unknown without the official handout/PYQs. Typical MUJ pattern (assumption only):
MTE ≈ U1–U2 (semiconductor physics + junction/diode), ETE ≈ full syllabus weighted to U2/U4. **Do
not rely on this** — flag to learner; confirm from papers.

## To replace this stub

Drop MTE+ETE papers and course PPTs into `../exam-pack/` (or via `../../_inbox/`). Then: count
topic frequency, extract real question types + marks, read instructor emphasis off the PPTs, and
rewrite the weightage table from evidence. Promote confidences from `uncertain` accordingly.
