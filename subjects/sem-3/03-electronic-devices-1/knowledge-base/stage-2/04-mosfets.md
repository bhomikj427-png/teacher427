# Unit 4 — MOSFETs — STAGE 2 (deep structure)

> On top of Stage-1 `../04-mosfets.md`. Primary: Sze 3e ch.6, Razavi *Microelectronics*, Sedra-Smith
> advanced, Taur & Ning *Modern VLSI Devices*. This is where the square law is shown to be a white lie.

## 1. MOS-capacitor electrostatics → threshold voltage, derived
- Surface potential φ_s vs gate voltage: accumulation → depletion → inversion. **Strong inversion
  defined at φ_s = 2φ_F**, where φ_F = V_T ln(N_A/nᵢ) (bulk Fermi offset). At that point surface
  electron density = bulk hole density.
- Gate voltage shares between oxide and semiconductor: V_GS = V_FB + 2φ_F + Q_dep/C_ox, giving
  **V_t0 = V_FB + 2φ_F + √(2ε_s q N_A·2φ_F)/C_ox**, with **flat-band V_FB = φ_ms − Q_ox/C_ox**
  (work-function difference + oxide charge). Every V_t-adjustment knob (doping, t_ox, gate material,
  implant) lives in this equation.
- **Body effect** falls straight out: extra reverse body bias V_SB increases the depletion charge →
  **V_t = V_t0 + γ(√(2φ_F+V_SB) − √(2φ_F))**, **γ = √(2ε_s q N_A)/C_ox** (the body-effect
  coefficient). Derived, not asserted (Stage-1 stated it).

## 2. Square law, derived (gradual-channel + charge-sheet)
- Inversion charge per area at point y: Q_n(y) = C_ox(V_GS − V_t − V(y)). Drain current (drift):
  I_D = μ_n W Q_n(y) dV/dy; integrate y: 0→L, V: 0→V_DS →
  **I_D = μ_nC_ox(W/L)[(V_GS−V_t)V_DS − V_DS²/2]** (triode). At V_DS=V_OV the bracket maximizes →
  **saturation I_D = ½μ_nC_ox(W/L)V_OV²** (Q_n→0 at drain = pinch-off). So Stage-1's two formulas are
  one integral evaluated to two limits.

## 3. Where the square law lies (the four big short-channel corrections) ★
1. **Velocity saturation.** Long-channel assumes v=μE. Short channels hit v_sat (Stage-2/U1 §6) →
   **I_D,sat ≈ W·v_sat·C_ox·(V_OV) — LINEAR in V_OV, not square**, and **L-independent**. g_m
   saturates at W·v_sat·C_ox. *This is the single most important deviation in modern devices.*
2. **Mobility degradation** from the vertical field (carriers pressed against the rough oxide
   interface): μ_eff = μ_0/(1+θ(V_GS−V_t)) → further sub-square behavior.
3. **Channel-length modulation / DIBL.** λ effect (r_o=1/λI_D=V_A/I_D); **DIBL**: the drain's field
   lowers the source barrier in short channels → V_t falls with V_DS, I_D rises — a short-channel
   leakage/gain killer.
4. **Subthreshold conduction.** Below V_t the device is **not off** — it conducts by **diffusion**
   (like a BJT): **I_D ∝ e^{V_GS/(nV_T)}**. **Subthreshold swing S = nV_T ln10 ≥ 60 mV/decade @300 K**
   (n=1+C_dep/C_ox ≥ 1). *(verified: ln10·kT/q = 2.303×25.85 mV = 59.5 mV — the famous "60 mV/dec
   limit.")* **★ This thermal floor is why supply voltage can't keep scaling** — leakage can't be
   shut off fast enough. Motivates FinFET/GAA (better electrostatic n→1) and the search for
   sub-thermal (tunnel-FET, negative-capacitance) switches.

## 4. C-V of the MOS capacitor
- C(V_G): high in accumulation (C_ox) → dips in depletion (C_ox in series with C_dep) → rises back at
  inversion (low-frequency) or stays low (high-frequency, minority carriers can't follow). C-V
  measurement extracts t_ox, V_FB, doping, oxide charge — the core MOS characterization (links ECE2130).

## 5. High-frequency model & f_T
- Gate capacitances C_gs, C_gd (Miller), C_gb. **Transit frequency f_T = g_m/(2π(C_gs+C_gd))**; for a
  long channel f_T ≈ 3μ V_OV/(4πL²) → **scales as 1/L²** (the speed driver of scaling); velocity-sat
  short channels → f_T ∝ v_sat/L (1/L). Sets the analog/RF bandwidth.

## 6. Scaling — Dennard, its end, and the device roadmap (frontier)
- **Dennard scaling (1974):** shrink all dimensions and voltages by κ → same field, ~κ² more density,
  ~κ faster, constant power density. Drove Moore's law for ~30 years.
- **Why it ended (~2005):** V_t can't scale (subthreshold 60 mV/dec floor → leakage explodes), so V_DD
  stopped dropping → power density wall → frequency plateaued, went multi-core.
- **Electrostatic fixes:** thin-body/SOI → **FinFET** (gate on 3 sides, ~2011, 22 nm) → **GAA /
  nanosheet** (gate all around, ~3 nm node) — all chasing better gate control (n→1, less DIBL/leakage).
  **High-κ + metal gate** (HfO₂, ~45 nm) replaced SiO₂/poly to cut gate-tunneling leakage while
  keeping C_ox. **Strain engineering** boosts μ. *Teach the roadmap as the answer to the 60 mV/dec
  and tunneling limits, not as trivia.*

## 7. Cross-topic unification
- **Subthreshold MOSFET = a BJT** (both diffusion, exponential) — the BJT is the *ideal* 60 mV/dec
  switch the MOSFET only approaches (Stage-2/U5). · **CMOS power** = dynamic CV²f + static (subthreshold
  + gate + junction leakage) — the leakage terms are the Stage-2 physics above. · MOS inversion layer
  is a **2-D electron gas** (DOS link, Stage-2/U1 §9) with quantum-confinement V_t shifts at thin t_ox.

## 8. Harder problem classes
- Derive V_t and γ from the MOS electrostatics. · Show square→linear I_D crossover under velocity
  saturation; find the critical L. · Compute subthreshold swing from C_dep/C_ox; explain the 60 mV/dec
  floor and why GAA helps. · f_T scaling long vs short channel. · DIBL effect on a current mirror.
  · "Why did Dennard scaling end and what replaced it?" (full electrostatic argument).

## Open / to-verify (Stage 2)
- `[opened 2026-06-24]` Process-specific numbers (E_c for v-sat onset, θ mobility-degradation
  coefficient, node-by-node t_ox) are technology fits — teach mechanisms and the 60 mV/dec floor
  (verified); don't pin process constants.
