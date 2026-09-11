# ECE2101 Electronic Devices-I — Curriculum (derived from knowledge-base/00-map.md)

> Ordered objectives, **prerequisites first** (cognitive-load order). Strictly downstream of the
> map's prerequisite graph. Base is **`stage-2✓`** — Stage-1 files are the exam set; `stage-2/`
> holds depth to open after exam mastery (scoring-over-depth governs teaching order). Mastery-
> gated: a unit opens only when the prior is *demonstrated*. ★ marks threshold units (extra time
> + productive-failure setups). Teaching order = official unit order = topological order.

## U1 — Semiconductor Physics Fundamentals ★ (drift-vs-diffusion threshold)
- Energy bands, intrinsic Si; doping → n/p extrinsic, carrier concentrations (n·p = nᵢ²).
- **Drift** (mobility, resistivity) and **diffusion** (D, Einstein D/μ = V_T) — both coexist (★).
- nᵢ is textbook-dependent (`contested`: ≈1.0–1.5×10¹⁰ cm⁻³) — teach the spread, use the exam
  textbook's value in problems.
- Outcome: computes carrier concentrations and conductivity from doping; explains *why* diffusion
  current exists without a field and when each mechanism dominates.

## U2 — PN Junctions + Diode Circuits ★★ (the load-bearing unit — everything sits on it)
- Junction electrostatics: depletion region, built-in potential Vbi (★ — exists at equilibrium,
  unmeasurable by voltmeter), depletion width, junction capacitance.
- Shockley diode equation from continuity; forward/reverse behavior; temperature effects
  (reverse current doubles ~10 °C — corrected claim, see CHANGELOG).
- Breakdown (avalanche vs Zener), Schottky, switching/charge storage.
- Diode circuits: rectifiers, clippers, clampers, Zener regulator (the exam's worked-problem core).
- Outcome: derives/uses the diode equation with correct mechanism; solves rectifier/regulator
  problems; explains Vbi without hand-waving.

## U3 — JFETs
- Reverse-biased gate pinches the channel; pinch-off, I_DSS, Shockley's square law.
- Bias configurations + Q-point; transfer characteristic.
- Outcome: finds a JFET Q-point graphically and algebraically; states the control mechanism
  (field narrows channel — no gate current).

## U4 — MOSFETs ★ (inversion threshold; the protagonist)
- MOS capacitor → **inversion** (★ — insulated gate induces an opposite-type channel at V_t).
- Triode vs saturation; square-law I-V; E-MOSFET vs D-MOSFET.
- MOSFET as switch; CMOS and the bridge to digital logic (cross-link: 04-digital-electronics U5).
- Outcome: identifies operating region from voltages and computes I_D; explains inversion with
  the capacitor-that-becomes-a-resistor model.

## U5 — BJTs + Comparison ★ (controlled-source threshold)
- Two junctions; base current controls collector current (α, β); cutoff/active/saturation.
- Bias circuits + Q-point stability; **the transistor as a controlled source** (★).
- Large-signal → small-signal split (★): Q-point first, then linearize (gm, rπ, ro).
- BJT vs MOSFET: current- vs voltage-controlled — the deepest split (big idea 3).
- Outcome: solves bias problems to a Q-point; explains why the collector acts as a current source
  in active region; picks BJT-vs-FET trade-offs from mechanism.

## Teaching notes carried from the map
- **U1→U2 is the hardest, most load-bearing edge** — junction electrostatics rests entirely on
  drift/diffusion + doping. Do not open U2 until U1's threshold is demonstrated.
- Confidence flags survive into teaching: nᵢ `contested` (teach the spread); exact MUJ unit/MTE-ETE
  boundaries `uncertain` (no PYQ yet — re-confirm scope when exam-pack fills); Stage-2
  frontier/empirical specifics stay flagged `uncertain` (E_crit, ZTC, BV_CEO exp, FinFET years).
- Stage-2 depth (`knowledge-base/stage-2/01–05`) opens per unit only after that unit's exam-level
  mastery — never interleaved into first-pass teaching.
