# Unit 3 — JFETs (Junction Field-Effect Transistors)

> Confidence: `settled`. Tier-1: Boylestad 10e ch.6–7; Sedra-Smith 7e (FET ch.); Neamen 4e ch.12.
> Mechanism-level, exam-ready. Builds on U2 (reverse-biased junction → depletion control).

## Stage 1 (MUJ level)

### Construction & the core idea
- A **channel** of doped semiconductor (n-channel: n-type bar) between two ohmic contacts —
  **drain (D)** and **source (S)**. On the sides, a **gate (G)** region of the opposite type (p⁺)
  forms a **p-n junction** with the channel.
- **The control mechanism (★):** the gate junction is **always reverse-biased** (or zero). Its
  **depletion region** intrudes into the channel; making V_GS more negative (n-channel) widens the
  depletion region → **narrows the conducting channel** → raises channel resistance → reduces drain
  current. **A voltage (V_GS) controls a current (I_D) via depletion-width modulation** — no gate
  current flows (reverse-biased junction) → **very high input impedance.**
- This makes the JFET a **voltage-controlled, majority-carrier, normally-ON ("depletion-mode")**
  device: at V_GS = 0 the channel is wide open and conducts.
- **p-channel JFET:** mirror — p-type channel, n⁺ gate, all voltage polarities reversed.

### Characteristics & regions
Two control voltages: **V_GS** (gate-source, the input) and **V_DS** (drain-source). Increasing
V_DS at fixed V_GS:
- **Ohmic / triode region (small V_DS):** channel acts like a **voltage-controlled resistor**; I_D
  rises ~linearly with V_DS. (Used as a variable resistor / analog switch.)
- **Pinch-off & saturation region:** as V_DS rises, the depletion region near the **drain** widens
  (the reverse bias there is larger) until the channel "pinches off" at the drain. Beyond
  **pinch-off voltage**, I_D **saturates** — nearly flat vs V_DS (the active/amplifying region).
  *Mechanism:* once pinched, further V_DS drops across the pinched region; channel current is
  limited by what the source end injects. (It does **not** actually shut to zero — carriers are
  swept through the narrow pinched zone.)
- **Pinch-off voltage V_P** (a.k.a. V_GS(off)): the V_GS at which the channel is fully depleted and
  I_D → 0. For n-channel V_P is **negative**; |V_P| also equals the V_DS at which pinch-off first
  occurs when V_GS=0.
- **I_DSS:** the drain current at **V_GS = 0** in saturation — the maximum I_D. A datasheet anchor.
- Region test (saturation): **V_DS ≥ V_GS − V_P** i.e. V_DS ≥ |V_P| − |V_GS| (n-channel). Below
  that → triode.

### Shockley's equation (the JFET square law) — `settled`
- In **saturation**: **I_D = I_DSS·(1 − V_GS/V_P)²**, valid for V_P ≤ V_GS ≤ 0 (n-channel).
  *Mechanism:* depletion-width modulation gives the squared dependence. **Transfer characteristic
  is a parabola** from (V_P, 0) to (0, I_DSS).
- **Transconductance** g_m = dI_D/dV_GS = (−2I_DSS/V_P)(1 − V_GS/V_P) = g_m0·(1−V_GS/V_P), where
  **g_m0 = −2I_DSS/V_P** is g_m at V_GS=0 (maximum). g_m = 2√(I_DSS·I_D)/|V_P|. This is the
  small-signal gain element.
- **Channel-length modulation** (the slight upward slope in saturation): I_D = I_DSS(1−V_GS/V_P)²(1+λV_DS);
  output resistance r_d = 1/(λI_D). Often neglected in first-pass Stage 1.

### Biasing (find the Q-point)
- **Fixed bias:** a negative V_GG directly on the gate; V_GS = −V_GG; plug into Shockley for I_D.
- **Self-bias:** a source resistor R_S; V_GS = −I_D·R_S. Solve simultaneously with Shockley
  (quadratic, or graphically intersect the bias line V_GS=−I_D R_S with the transfer curve).
- **Voltage-divider bias:** gate held at V_G by a divider; V_GS = V_G − I_D R_S — most stable Q.
- The graphical **load-line on the transfer characteristic** (bias line ∩ parabola) is the canonical
  exam method.

### Small-signal model & applications
- Small-signal model: gate draws ~no current (open), drain = a current source **g_m·v_gs** in
  parallel with r_d. **Common-source voltage gain A_v ≈ −g_m(R_D ∥ r_d) ≈ −g_m R_D.**
- Configs (mirror BJT): **common-source** (high gain, inverting — the workhorse amplifier);
  **common-drain / source-follower** (gain ≈ 1, high Z_in, low Z_out — buffer);
  **common-gate** (low Z_in, non-inverting — high frequency).
- **Applications:** high-input-impedance amplifier / buffer (electrometer, scope front-ends),
  voltage-controlled resistor (triode region), analog switch/chopper, low-noise RF amplifier,
  constant-current source (gate tied to source → I_DSS).

### MOSFET vs JFET (preview of U4 — common compare question)
- Both FETs: voltage-controlled, majority-carrier, high Z_in. **JFET gate = reverse-biased p-n
  junction** (tiny leakage, modest Z_in ~10⁹ Ω); **MOSFET gate = oxide-insulated** (essentially
  zero DC current, Z_in ~10¹²–10¹⁵ Ω). JFET is **depletion-mode only** (normally on); MOSFET can be
  **enhancement** (normally off — the dominant type) or depletion. MOSFET scales/integrates →
  dominates VLSI; JFET prized for low noise & high Z_in discrete front-ends.

### Worked-problem patterns (what the exam asks)
1. Given I_DSS and V_P, find I_D for a stated V_GS (Shockley); or invert to find V_GS for a target I_D.
2. Self-bias / voltage-divider Q-point: solve V_GS=−I_D R_S with Shockley (quadratic or graphical).
3. g_m at a Q-point; common-source small-signal gain A_v ≈ −g_m R_D.
4. Identify region (triode vs saturation) from V_DS vs (V_GS−V_P).
5. Sketch transfer (parabola) and output (drain) characteristics; mark I_DSS, V_P, pinch-off locus.
6. JFET-as-VCR or constant-current-source reasoning.

### Key formulas (verified)
- I_D = I_DSS(1 − V_GS/V_P)² (saturation) · sat. condition V_DS ≥ V_GS − V_P
- g_m = (−2I_DSS/V_P)(1−V_GS/V_P) = 2√(I_DSS I_D)/|V_P| · g_m0 = −2I_DSS/V_P
- Self-bias V_GS = −I_D R_S · A_v ≈ −g_m(R_D∥r_d) · r_d = 1/(λI_D)

---
**Stage 2 (deep structure) — ✓ BUILT (2026-06-24):** lives separately in `stage-2/03-jfets.md`. *Adds:* derivation
of Shockley's square law from the gradual-channel approximation + depletion electrostatics; the full
(non-saturated) I_D(V_GS,V_DS) expression and the pinch-off boundary derivation; why I_D doesn't go
to zero past pinch-off (velocity-saturation / space-charge-limited view); channel-length modulation
& Early-like effect; temperature dependence (g_m vs I_DSS/V_P drift, the zero-tempco bias point);
noise (why JFETs are low-noise — no 1/f from oxide traps); MESFET/HEMT relatives; comparison of the
JFET square law with the MOSFET square law at the physics level.
