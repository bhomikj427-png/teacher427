# Unit 5 — BJTs (Bipolar Junction Transistors)

> Confidence: `settled`. Tier-1: Boylestad 10e ch.3–5; Sedra-Smith 7e ch.6; Neamen 4e ch.6,12.
> Mechanism-level, exam-ready. Builds on U2 (two coupled p-n junctions). Ends with the syllabus's
> BJT-vs-MOSFET comparison.

## Stage 1 (MUJ level)

### Construction & the core idea
- **Three doped regions, two junctions:** **npn** (n-emitter / p-base / n-collector) or **pnp**
  (mirror). **Emitter (E)** = heavily doped (injects carriers); **Base (B)** = very thin & lightly
  doped (the control region); **Collector (C)** = moderately doped, large area (collects).
- **"Bipolar"** = both electrons and holes participate (vs FETs = unipolar/majority-only).
- **The control mechanism (★, active region, npn):** forward-bias the **base-emitter** junction →
  the emitter floods electrons into the base. The base is so **thin** that almost all of them shoot
  across before recombining and are swept into the **reverse-biased base-collector** junction by its
  field. **A small base current controls a large collector current** → BJT is **current-controlled**
  (the deep contrast with voltage-controlled FETs).
- *Why the base must be thin & lightly doped:* to minimize recombination there, so nearly every
  injected carrier reaches the collector (high transport factor).

### Currents & the gain parameters
- KCL: **I_E = I_C + I_B**, with I_B ≪ I_C ≈ I_E.
- **α (common-base current gain)** = I_C/I_E ≈ 0.95–0.99 (close to 1; how much injected current
  reaches the collector).
- **β (common-emitter current gain, h_FE)** = I_C/I_B ≈ 50–300. *The headline amplification.*
- **Relations (load-bearing):** **β = α/(1−α)**, **α = β/(β+1)**, **I_E = (β+1)I_B**,
  **I_C = βI_B = αI_E.** (Small leakage I_CBO/I_CEO usually neglected at Stage 1.)
- Collector current is set by the BE voltage: **I_C = I_S·e^{V_BE/V_T}** (Ebers-Moll active form) —
  the BJT is *exponential* in V_BE (vs MOSFET square-law in V_OV). V_BE(on) ≈ 0.7 V (Si).

### Operating regions (set by the two junction biases)
| Region | B-E junction | B-C junction | Use |
|--------|-------------|-------------|-----|
| **Cutoff** | reverse | reverse | OFF switch (I_C≈0) |
| **Active** (forward-active) | **forward** | **reverse** | **amplifier** (I_C=βI_B) |
| **Saturation** | forward | forward | ON switch (V_CE≈0.2 V) |
| **Reverse-active** | reverse | forward | rarely used (poor β) |
- **Active:** I_C ≈ βI_B, ~independent of V_CE (slight slope = **Early effect**, base-width
  modulation; r_o = V_A/I_C, V_A = Early voltage). The amplifying region.
- **Saturation:** both junctions forward, V_CE ≈ V_CE(sat) ≈ 0.2 V, I_C < βI_B (collector can't
  supply more) → closed switch. **Cutoff:** I_B=0 → I_C≈0 → open switch.

### Characteristics
- **Input characteristic** (CE): I_B vs V_BE — looks like a forward diode (knee ≈ 0.7 V).
- **Output characteristic** (CE): I_C vs V_CE for stepped I_B — flat active-region lines (spaced by
  βΔI_B), rising slightly (Early effect, extrapolate to −V_A); steep saturation knee near V_CE≈0.2 V.

### Biasing (find the Q-point) — establish active-region operation
- **Fixed bias:** I_B=(V_CC−V_BE)/R_B, I_C=βI_B — simple but **β-sensitive / thermally unstable.**
- **Emitter (self) bias** with R_E: negative feedback stabilizes I_C against β and temperature.
- **Voltage-divider bias:** the standard stable design — R1/R2 set V_B, R_E sets I_E≈(V_B−V_BE)/R_E,
  making I_C ≈ V_E/R_E nearly **independent of β.** *Mechanism:* R_E feedback (if I_C rises, V_E
  rises, V_BE falls, I_C pulled back). Stability factor S = ∂I_C/∂I_CO.
- **Thermal runaway:** I_C heats junction → V_BE drops / I_CO rises → I_C rises → more heat. R_E and
  good biasing prevent it.

### Small-signal model & amplifier configurations
- **Transconductance g_m = I_C/V_T** (linear in I_C — note the contrast with MOSFET √I_D).
- **Input resistance r_π = β/g_m = βV_T/I_C**; output r_o = V_A/I_C.
- **Hybrid-π / re model:** r_e = V_T/I_E ≈ 1/g_m; r_π = (β+1)r_e.
- **Configs:**
  - **Common-emitter (CE):** A_v = −g_m(R_C∥r_o), high gain, inverting, moderate Z_in (the
    workhorse, ↔ CS).
  - **Common-base (CB):** non-inverting, low Z_in, ~unity current gain, high-frequency (↔ CG).
  - **Common-collector (CC, emitter follower):** A_v≈1, high Z_in, low Z_out — buffer (↔ CD).

### BJT vs MOSFET (the syllabus's closing comparison — high-value)
| Aspect | BJT | MOSFET |
|--------|-----|--------|
| Control | **current** (I_B) | **voltage** (V_GS) |
| Carriers | bipolar (e⁻ + holes) | unipolar (majority only) |
| Input impedance | moderate (r_π, base current) | **very high** (insulated gate, ~0 DC) |
| I-control law | **exponential** I_C=I_S e^{V_BE/V_T} | **square-law** I_D∝V_OV² (long channel) |
| g_m at given current | **higher** (g_m=I_C/V_T) | lower (g_m=2I_D/V_OV) |
| Switch ON drop | V_CE(sat)≈0.2 V (offset) | R_on·I (resistive, →0 at low I) |
| Static power (logic) | high | **~zero (CMOS)** |
| Integration/scaling | poorer | **excellent → VLSI** |
| Speed | fast (esp. RF); charge storage in saturation slows switching | fast; gate-cap limited |
| Temperature | V_BE −2 mV/°C; thermal-runaway risk | mobility ↓ with T → self-limiting (positive R tempco) |
| Noise / matching | better matching, lower offset | better Z_in, low-power |
- **One-liner:** BJT = high g_m, exponential, current-driven, great analog/RF; MOSFET = high-Z_in,
  scalable, low-power, *the* digital/VLSI device. Modern ICs mix them (BiCMOS).

### Worked-problem patterns (what the exam asks)
1. α↔β conversions; find I_C, I_B, I_E given any one + β (or α).
2. Region identification from terminal voltages (check both junction biases) → cutoff/active/sat.
3. DC bias / Q-point: fixed, emitter, voltage-divider — find I_C, V_CE; comment on β-stability.
4. Small-signal: g_m, r_π, r_e at a Q-point; CE gain A_v=−g_m(R_C∥r_o); follower/CB.
5. BJT as a switch: base resistor to ensure saturation (force I_B > I_C(sat)/β); V_out levels.
6. BJT-vs-MOSFET comparison (table/short-answer).

### Key formulas (verified)
- I_E=I_C+I_B · α=I_C/I_E · β=I_C/I_B · β=α/(1−α) · α=β/(β+1) · I_E=(β+1)I_B
- I_C=I_S e^{V_BE/V_T} · g_m=I_C/V_T · r_π=βV_T/I_C · r_e=V_T/I_E · r_o=V_A/I_C
- Divider bias: I_E≈(V_B−V_BE)/R_E · CE: A_v=−g_m(R_C∥r_o) · V_CE(sat)≈0.2 V, V_BE(on)≈0.7 V

---
**Stage 2 (deep structure) — ✓ BUILT (2026-06-24):** lives separately in `stage-2/05-bjts.md`. *Adds:* full
Ebers-Moll & Gummel-Poon models (all four regions from two coupled diodes); derivation of α/β from
emitter injection efficiency × base transport factor; the minority-carrier profile in the base &
why β depends on base width/doping; Early effect derived (base-width modulation, V_A); high-current
roll-off (Kirk effect) & Webster effect; base-charge / charge-control model and the storage time in
switching; breakdown (BV_CEO vs BV_CBO, the β multiplication); heterojunction BJT (HBT) and why SiGe;
the deep g_m=I_C/V_T vs MOSFET subthreshold-slope unification (a BJT is the ideal "60 mV/dec"
device); current mirrors & matching at the physics level.
