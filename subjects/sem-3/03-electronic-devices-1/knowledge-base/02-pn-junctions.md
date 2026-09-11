# Unit 2 — PN Junctions & Diode Circuits

> Confidence: `settled` except where flagged. Tier-1: Boylestad 10e ch.1–2; Sedra-Smith 7e ch.3–4;
> Neamen 4e ch.7–9; Streetman 7e ch.5–6. Highest-weight unit (`exam-map.md`) and the load-bearing
> prerequisite for all transistors. Mechanism-level, exam-ready. Inherits the nᵢ caveat (`01`).

## Stage 1 (MUJ level)

### Junction formation & the depletion region ★ threshold
- Metallurgically join p-type and n-type. At the boundary, the huge concentration gradient makes
  **majority carriers diffuse across**: electrons (n→p), holes (p→n). They leave behind **immobile
  ionized dopant cores** — positive donor ions on the n-side, negative acceptor ions on the p-side.
- This exposed-ion region is the **depletion region** (space-charge region): swept free of mobile
  carriers, it holds a **built-in field E** pointing n→p. *Mechanism:* the field opposes further
  diffusion. **Equilibrium = diffusion exactly balanced by drift** for *each* carrier → net current
  zero, and the Fermi level E_F is **flat** across the junction.
- **Built-in potential V_bi** (a.k.a. V₀, contact potential):
  **V_bi = V_T · ln(N_A·N_D / nᵢ²)**. *Mechanism:* it's the band-bending needed to line up the two
  Fermi levels. Si typical ≈ 0.6–0.8 V. **You cannot measure V_bi with a voltmeter** — the probe
  contact potentials cancel it exactly (it does no net work around a loop). This is a ★ stumbling
  point.

### Bias
- **Forward bias** (V_D > 0, p to +): the applied voltage *opposes* the built-in field → barrier
  drops to (V_bi − V_D), depletion region **narrows**, the diffusion of majority carriers floods
  across → large current that rises **exponentially**. Carriers injected as excess minority carriers
  on each side, then recombine (diffusion current, U1).
- **Reverse bias** (V_D < 0): applied voltage *aids* the built-in field → barrier rises to
  (V_bi + |V_D|), depletion region **widens**, majority diffusion is choked off. Only a tiny
  **reverse saturation current I_S** flows — minority carriers swept across by the field (drift),
  set by thermal generation, ~independent of voltage.

### Junction electrostatics (Poisson) — depletion width & capacitance
- **Poisson's equation** in the depletion region: d²V/dx² = −ρ/ε_s. Using the **depletion
  approximation** (charge = fully ionized dopants, abrupt edges, mobile carriers neglected) and
  charge balance **N_A·x_p = N_D·x_n** (total + charge = total − charge):
- **Depletion width** (with V_R the reverse bias, V_R<0 for forward):
  **W = √[ (2ε_s/q)·(1/N_A + 1/N_D)·(V_bi − V_D) ]**.
  *Consequence:* the lighter-doped side holds **most** of the depletion width and most of the
  voltage (x_n/x_p = N_A/N_D). One-sided junction (p⁺n): W ≈ √[2ε_s(V_bi−V_D)/(qN_D)], all on the
  light side. ε_s(Si) = 11.7·ε₀ ≈ 1.04×10⁻¹² F/cm.
- **Junction (transition/depletion) capacitance C_j = ε_s·A/W** — a parallel-plate cap whose plate
  separation W *changes with reverse voltage*: **C_j = C_j0 / (1 − V_D/V_bi)^m**, m=½ abrupt, ⅓
  linearly-graded. *Mechanism:* reverse bias widens W → less capacitance. **This voltage-variable
  capacitance is exactly the varactor diode.** Dominates under reverse bias.
- **Diffusion (storage) capacitance C_d** dominates under **forward** bias: charge stored as excess
  minority carriers in the neutral regions, C_d = τ·I_D/V_T (τ = transit/lifetime). Sets switching
  speed (below).

### Continuity & the carrier flow that *makes* the current (syllabus: "Poisson & continuity equations")
- Poisson (above) fixes the **electrostatics** (field, depletion width). The **continuity equation**
  fixes the **carrier bookkeeping**: ∂n/∂t = (1/q)·∂J_n/∂x + (G − R) (and the hole analogue). It just
  says carriers in a slice change by what flows in/out **plus** what's generated minus what
  recombines.
- In a forward-biased diode's **neutral region**, steady state (∂/∂t=0), no field, low injection →
  it reduces to the **minority-carrier diffusion equation** D_p·d²Δp/dx² = Δp/τ_p, whose solution is
  the decaying excess-carrier profile **Δp(x) = Δp(0)·e^{−x/L_p}**, L_p=√(D_pτ_p) (U1). *Mechanism:*
  injected minority carriers diffuse in and recombine over a length L_p — and the **slope of that
  profile at the depletion edge is exactly the diffusion current**, which is what the Shockley
  equation below computes. So: **Poisson → the field/width; continuity → the current.** (Full
  derivation: `stage-2/02` §2.)

### The diode equation (Shockley) — I-V characteristic
- **I_D = I_S (e^{V_D/(η V_T)} − 1)** *(load-bearing, `settled`)*. η (or n) = **ideality factor**,
  1 (ideal, diffusion-dominated) to 2 (recombination in depletion region dominates, low current);
  Si discrete diodes often modeled η≈1–2. V_T ≈ 26 mV @300 K.
- **I_S (reverse saturation current)** = qA·(D_p·p_n0/L_p + D_n·n_p0/L_n), with p_n0=nᵢ²/N_D etc.
  *Mechanism:* set by minority-carrier injection/recombination; **∝ nᵢ²**. Tiny (~10⁻¹²–10⁻¹⁵ A),
  strongly temperature-dependent (inherits nᵢ caveat). **Temperature rule (verified 2026-06-24):**
  the *measured* reverse current of a Si diode **≈ doubles every ~10 °C** (Boylestad; the real Si
  leakage is **generation**-dominated, ∝ nᵢ). The **ideal diffusion** I_S alone (∝ nᵢ²) would double
  ~every 5 °C — so quote **~10 °C** for a real diode, ~5 °C only for the pure nᵢ² term. *(prior draft
  said "~5 °C" unqualified — corrected; see CHANGELOG.)*
- **Three regions of the curve:** (1) reverse: I ≈ −I_S, ~flat; (2) forward below cut-in: small;
  (3) forward above **cut-in/knee voltage** V_γ (Si ≈ 0.7 V, Ge ≈ 0.3 V): steep exponential.
- **Temperature:** at fixed current, V_D **drops ≈ −2 mV/°C** (Si). I_S rises with T. The two
  combine so forward V falls and reverse leakage grows with heat.
- **Dynamic (AC) resistance** at a Q-point: r_d = ηV_T/I_D (≈ 26 mV/I_D for η=1). **Static**
  resistance R = V_D/I_D. r_d is the small-signal model element (below).

### Diode models (large-signal, in increasing fidelity)
1. **Ideal:** short when forward (V=0), open when reverse. (First-pass circuit analysis.)
2. **Constant-voltage-drop (CVD):** forward = battery V_γ (0.7 V Si) then short; reverse = open.
   *(Most common exam model.)*
3. **Piecewise-linear:** forward = V_γ in series with r_av (the slope). reverse = open (or +leakage).
4. **Small-signal:** at a Q-point, r_d = ηV_T/I_DQ in parallel with C (C_d forward, C_j reverse).
- **Solving diode circuits:** assume a state → solve the linear circuit → check consistency (is a
  "forward" diode actually carrying I>0? is a "reverse" one really at V<V_γ?). **Load-line** method:
  intersect the diode curve with the circuit's Thevenin load line. Iterative method when using the
  exponential exactly.

### Breakdown — avalanche vs Zener (a classic compare question)
- Under large reverse bias, current suddenly shoots up at **V_BR** (the breakdown voltage). Not
  destructive *if current is limited*; the diode survives and the voltage stays ≈ V_BR.
- **Avalanche breakdown** (impact ionization): the strong field accelerates carriers enough to
  knock out new e-h pairs → chain multiplication. Dominates in **lightly-doped, wide** junctions →
  **higher V_BR (≳ ~6 V)**. **Positive temperature coefficient** (V_BR rises with T — more lattice
  scattering shortens mean free path, needs more voltage).
- **Zener breakdown** (band-to-band tunneling): in **heavily-doped, narrow** junctions the
  depletion region is so thin the field rips bonding electrons straight across the gap by quantum
  tunneling → **lower V_BR (≲ ~5 V)**. **Negative temperature coefficient.**
- ~5–6 V devices mix both (near-zero tempco — used as references). *Naming caution:* commercial
  "Zener diodes" use *either* mechanism; the name is generic for "breakdown reference diode."

### Special diodes
- **Zener diode:** designed to operate *in* reverse breakdown at a sharp, stable V_Z → **voltage
  reference / regulator.** (Circuit below.)
- **Schottky diode:** **metal–semiconductor** junction (not p-n). Conduction is by **majority
  carriers only** → (1) **no minority-charge storage → very fast switching**; (2) **low forward
  drop ≈ 0.2–0.45 V.** Used in high-speed rectifiers, clamps, RF. *Mechanism:* barrier is the
  metal-semiconductor work-function difference (Schottky barrier φ_B).
- (Varactor = the voltage-variable C_j above; LED = direct-gap radiative recombination; photodiode
  = reverse-biased, light generates carriers.)

### Switching behavior & charge storage
- A forward-conducting diode has stored minority charge (C_d). Switch it suddenly to reverse and it
  **keeps conducting backward** until that charge is removed/recombines — the **reverse recovery
  time t_rr** (storage time + transition time). *Why it matters:* limits switching frequency; this
  is the headline reason **Schottky diodes (no stored minority charge) switch faster.**

### Diode circuits (high exam weight)
**(a) Rectifiers.**
- **Half-wave:** passes one half-cycle. V_dc = V_m/π; ripple high; PIV across diode = V_m.
- **Full-wave (center-tap or bridge):** both half-cycles. V_dc = 2V_m/π. **Bridge:** 4 diodes, PIV =
  V_m (per diode); center-tap PIV = 2V_m. Subtract diode drops for real V_m (−0.7 per conducting
  diode; bridge has 2 in the path → −1.4 V).
- **Capacitor filter:** smooths to near V_m with **ripple** V_r ≈ I_L/(f·C) (half-wave) or
  I_L/(2f·C) (full-wave) ≈ V_m/(fRC). Ripple factor r = V_r(rms)/V_dc. *Trade-off:* bigger C → less
  ripple but larger surge current.

**(b) Clippers (limiters):** diode + (optional bias) clips part of the waveform. Series or shunt;
the bias level + diode drop sets the clip threshold; orientation sets which part is removed. *Solve
by:* for each input region, decide each diode's state, replace with its model, find V_out.

**(c) Clampers (DC restorers):** capacitor + diode (+ optional bias) **shifts the DC level** of a
waveform without changing its shape (peak-to-peak preserved). The cap charges (through the diode on
one half-cycle) to a value that offsets the signal; clamps the peak to ≈ the bias (±V_γ). *Solve
by:* find the steady-state cap voltage on the diode-conducting half-cycle, then V_out = V_in ± V_cap.

**(d) Zener voltage regulator:** Zener in reverse across the load, series resistor R_S from the
(higher) source. R_S drops the excess; the Zener pins V_out = V_Z across line and load changes.
- Design: keep I_Z between I_Z(min) (to stay in breakdown) and I_Z(max)=P_Z(max)/V_Z (to not burn
  out) across the *worst-case* line/load. KCL: I_R = I_Z + I_L, I_R = (V_in−V_Z)/R_S.
- Worst case for I_Z: **max** at high V_in + no load; **min** at low V_in + max load. Size R_S so
  both are satisfied.

### Worked-problem patterns (what the exam asks)
1. V_bi numerical from doping; depletion width W and how it scales with V_R and doping; which side
   holds the width/voltage; C_j vs reverse voltage.
2. Diode current from Shockley (or find V given I); η and I_S effects; r_d at a Q-point; temperature
   shift of V_D (−2 mV/°C) and of I_S.
3. Diode-circuit solve with CVD/piecewise model: assume state → solve → verify. Load-line.
4. Rectifier: V_dc, PIV, ripple with filter C, ripple factor; half vs full vs bridge comparison.
5. Sketch clipper/clamper output for a given input + bias (state-by-state).
6. Zener regulator design: find R_S range, I_Z(min/max), power, behavior under line/load swing.
7. Compare avalanche vs Zener (mechanism, doping, V_BR range, tempco); why Schottky is fast/low-drop.

### Key formulas (verified)
- V_bi = V_T ln(N_A N_D/nᵢ²) · W = √[(2ε_s/q)(1/N_A+1/N_D)(V_bi−V_D)] · N_A x_p = N_D x_n
- C_j = ε_s A/W = C_j0/(1−V_D/V_bi)^m · C_d = τ I_D/V_T
- I_D = I_S(e^{V_D/ηV_T} − 1) · I_S ∝ nᵢ² · r_d = ηV_T/I_D · ΔV_D/ΔT ≈ −2 mV/°C (Si)
- Half-wave V_dc=V_m/π; full-wave V_dc=2V_m/π · V_r ≈ I_L/(fC) or I_L/(2fC) · bridge PIV=V_m
- Zener: I_R=(V_in−V_Z)/R_S = I_Z+I_L · I_Z(max)=P_Z(max)/V_Z

---
**Stage 2 (deep structure) — ✓ BUILT (2026-06-24):** lives separately in
`stage-2/02-pn-junctions.md`. *Adds:*
full derivation of the Shockley equation from the minority-carrier diffusion equation + boundary
conditions (law of the junction p_n=p_n0 e^{V/V_T}); the depletion approximation derived and its
breakdown; quasi-Fermi levels under bias; the full ideal-diode current with generation-
recombination (Sah-Noyce-Shockley, the η=2 term); high-level injection; series resistance & the
roll-off; junction breakdown field physics (impact-ionization coefficients, tunneling probability);
heterojunctions; metal-semiconductor (Schottky) barrier derivation incl. image-force lowering &
the difference from an ohmic contact; transient reverse-recovery charge-control model.
