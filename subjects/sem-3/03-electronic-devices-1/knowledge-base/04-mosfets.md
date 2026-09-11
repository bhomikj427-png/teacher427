# Unit 4 — MOSFETs

> Confidence: `settled`. Tier-1: Sedra-Smith 7e ch.5 (the canonical MOSFET treatment) + Boylestad
> 10e ch.6–8; Neamen 4e ch.10–11; Razavi (Stage-2). Highest-weight transistor unit (`exam-map.md`);
> the syllabus aims here (switch + digital). Mechanism-level, exam-ready.

## Stage 1 (MUJ level)

### Structure & the MOS capacitor
- **MOSFET = Metal-Oxide-Semiconductor FET.** Four terminals: **Gate (G)** over a thin **oxide
  (SiO₂)** over the **body/substrate (B)**, with **source (S)** and **drain (D)** = two heavily-
  doped regions in the substrate. The gate is **insulated** — no DC gate current (Z_in enormous).
- **n-channel enhancement (NMOS):** p-type substrate, n⁺ source/drain. The S and D form back-to-back
  diodes with the body → **no conduction at V_GS=0** (normally off → "enhancement").
- **The MOS capacitor is the heart.** Gate + oxide + semiconductor = a capacitor. Raising V_G:
  - **Accumulation** (V_G<0 on p-sub): holes pile at the surface.
  - **Depletion** (small V_G>0): holes pushed away, exposing acceptor ions (a depletion region).
  - **Inversion** (V_G large enough): the surface **inverts** to n-type — electrons attracted from
    the substrate form a thin **n-channel** connecting source and drain. *★ This is the threshold
    idea:* a *voltage* on an insulated plate induces a conducting layer of the *opposite* type.

### Threshold voltage V_t
- **V_t (V_TN)** = the V_GS at which a conducting channel just forms (strong inversion). For NMOS
  V_t > 0; for PMOS V_t < 0. Set by oxide thickness, doping, gate material, oxide charge, and the
  **body effect** (V_t increases as source-to-body reverse bias V_SB grows):
  V_t = V_t0 + γ(√(2φ_F+V_SB) − √(2φ_F)). *Mechanism:* reverse body bias widens the depletion charge
  the gate must support before inverting.
- **Overdrive voltage V_OV = V_GS − V_t** (a.k.a. V_eff) — the single most useful MOSFET quantity;
  the channel exists only when V_OV > 0.

### Operating regions (NMOS; the region test is the #1 exam skill)
Let kₙ = kₙ′(W/L), kₙ′ = μ_n·C_ox (process transconductance parameter), C_ox = ε_ox/t_ox.
1. **Cutoff:** V_GS < V_t → no channel → **I_D = 0.**
2. **Triode / linear / ohmic** (V_GS>V_t **and** V_DS < V_OV):
   **I_D = kₙ′(W/L)[ (V_GS−V_t)V_DS − V_DS²/2 ]**. For *small* V_DS this ≈ kₙ′(W/L)V_OV·V_DS — a
   **voltage-controlled resistor** r_DS = 1/[kₙ′(W/L)V_OV]. *Mechanism:* channel continuous from S
   to D; conducts both ways.
3. **Saturation / active** (V_GS>V_t **and** V_DS ≥ V_OV): the channel **pinches off** at the drain;
   **I_D = ½·kₙ′(W/L)(V_GS−V_t)² · (1 + λV_DS)**. *Mechanism:* drain end of channel pinched; current
   set by V_OV, nearly independent of V_DS. **This is the amplifying region.** λ = channel-length-
   modulation parameter (the small saturation slope; r_o = 1/(λI_D) ≈ V_A/I_D, V_A=1/λ the Early-
   like voltage). Often drop the (1+λV_DS) for hand analysis.
- **Boundary** V_DS = V_OV = V_GS − V_t separates triode and saturation; at it both formulas agree.
- **PMOS:** all signs flipped (V_t<0, conducts when V_GS<V_t i.e. V_SG>|V_t|, currents reverse). In
  CMOS the PMOS sits in an n-well with source at V_DD.

### Square law & transconductance
- Saturation **I_D ∝ V_OV²** (square law). **g_m = ∂I_D/∂V_GS = kₙ′(W/L)V_OV = √(2kₙ′(W/L)·I_D) =
  2I_D/V_OV.** *(verified standard, Sedra-Smith.)* Note g_m rises with √I_D (vs BJT's linear g_m=I_C/V_T).
- **Output resistance** r_o = 1/(λI_D) = V_A/I_D. Intrinsic gain g_m·r_o.

### Small-signal model & amplifier configurations
- Small-signal: gate open (no g current), drain = current source **g_m·v_gs** ∥ r_o; add g_mb·v_bs
  for body effect when source ≠ body.
- **Common-source (CS):** A_v = −g_m(R_D ∥ r_o). High gain, inverting — the workhorse. With source
  degeneration R_S: A_v ≈ −g_m R_D/(1+g_m R_S) (more linear, lower gain).
- **Common-gate (CG):** non-inverting, low Z_in (≈1/g_m), good high-frequency / current buffer.
- **Common-drain (CD, source follower):** A_v ≈ g_m R_S/(1+g_m R_S) ≈ 1, high Z_in, low Z_out —
  **voltage buffer.**
- (Mirrors the JFET/BJT config trio: CS↔CE, CG↔CB, CD↔CC.)

### MOSFET as a switch ★ (syllabus emphasis)
- **Gate drives the switch.** NMOS: V_GS=0 → **cutoff → open switch** (I_D=0). V_GS≫V_t with small
  V_DS → **deep triode → closed switch**, on-resistance **R_on = 1/[kₙ′(W/L)(V_GS−V_t)]** (small).
  *Mechanism:* operate in triode (not saturation) to be a good closed switch — low V_DS, low drop.
- **Why MOSFETs are *the* switch:** insulated gate → ~zero static drive current; bidirectional in
  triode; scalable; pairs into CMOS for ~zero static power. NMOS passes a strong 0 but a weak 1
  (threshold drop); PMOS passes a strong 1 but weak 0 → use **both** (transmission gate / CMOS).

### MOSFET-based digital circuits (the syllabus endpoint)
- **CMOS inverter:** PMOS (source→V_DD) on top, NMOS (source→GND) on bottom, gates tied = input,
  drains tied = output. **In=0:** PMOS on, NMOS off → out=V_DD (strong 1). **In=1:** NMOS on, PMOS
  off → out=0 (strong 0). *Key virtue:* one transistor is always off → **~zero static power**; power
  is drawn only during switching (CV²f dynamic power). This is *the* reason CMOS won.
- **VTC (voltage transfer characteristic):** sharp transition near V_DD/2; high noise margins.
  Switching threshold set by relative PMOS/NMOS strengths (size PMOS wider — holes slower — to
  balance).
- **CMOS logic gates:** NAND/NOR via **pull-down network (NMOS, in series for AND-ing) + complementary
  pull-up network (PMOS, in parallel)** — series-NMOS/parallel-PMOS = NAND; parallel-NMOS/series-
  PMOS = NOR. (Detail is Digital Electronics' job; ED introduces the principle.)
- Older families for contrast: **NMOS logic** (resistive/depletion load) burns static power and has
  asymmetric drive — why CMOS replaced it.

### Worked-problem patterns (what the exam asks)
1. **Region ID:** given V_GS, V_DS, V_t → cutoff / triode / saturation (test V_OV>0 and V_DS vs V_OV).
2. **I_D numerical** in the identified region (triode or square-law saturation); include (1+λV_DS) if asked.
3. **Bias the MOSFET:** find Q-point with a given bias network (often assume saturation, solve, verify).
4. **g_m, r_o** at a Q-point; **CS gain** A_v=−g_m(R_D∥r_o); follower/CG as needed.
5. **R_on** as a switch; voltage drop across an on-MOSFET in triode.
6. **CMOS inverter:** outputs for in=0/1; identify each transistor's region; sketch VTC; static power=0.
7. PMOS analogues with flipped signs.

### Key formulas (verified)
- Triode: I_D = kₙ′(W/L)[V_OV·V_DS − V_DS²/2] · sat: I_D = ½kₙ′(W/L)V_OV²(1+λV_DS) · V_OV=V_GS−V_t
- kₙ′ = μ_n C_ox, C_ox = ε_ox/t_ox · region boundary V_DS = V_OV
- g_m = kₙ′(W/L)V_OV = 2I_D/V_OV = √(2kₙ′(W/L)I_D) · r_o = 1/(λI_D) = V_A/I_D
- R_on = 1/[kₙ′(W/L)V_OV] · body effect V_t = V_t0 + γ(√(2φ_F+V_SB) − √(2φ_F))
- CS: A_v = −g_m(R_D∥r_o)

---
**Stage 2 (deep structure) — ✓ BUILT (2026-06-24):** lives separately in `stage-2/04-mosfets.md`. *Adds:* MOS-cap
electrostatics & surface-potential derivation of V_t (2φ_F condition, γ from depletion charge);
gradual-channel derivation of the triode + saturation I_D; channel-length modulation & DIBL; the
**short-channel effects** the square law hides (velocity saturation → I_D ∝ V_OV not V_OV²,
mobility degradation, hot carriers, subthreshold conduction I_D ∝ e^{V_GS/nV_T} and the 60 mV/dec
limit, leakage); C-V curve of the MOS capacitor; high-frequency model (C_gs/C_gd, f_T); CMOS scaling
(Dennard) and why it ended → FinFET/GAA; the EKV/BSIM modeling viewpoint; charge-sharing & narrow-
width effects.
