# Unit 1 — Semiconductor Physics Fundamentals

> Confidence: `settled` except where flagged. Tier-1: Boylestad 10e ch.1; Neamen 4e ch.1–5;
> Streetman 7e ch.1–4; Sedra-Smith 7e ch.3. Exact constants verified vs PVEducation / OSTI /
> Springer 2026-06-24 (see `00-map.md` register + `sources.md`). Mechanism-level, exam-ready.
>
> **★ nᵢ caveat (carries through the whole unit):** silicon's intrinsic carrier concentration at
> 300 K is **textbook-dependent** — Boylestad/older: 1.5×10¹⁰ cm⁻³; refined: ≈1.0×10¹⁰; best
> measured ≈9.65×10⁹. Use the value *your exam's textbook* uses; every nᵢ²-based number inherits
> this. (`contested`, `00-map.md`.)

## Stage 1 (MUJ level)

### Energy bands (intrinsic Si)
- Isolated atoms have discrete energy levels; bring 10²³ atoms together and levels split into quasi-
  continuous **bands**. The two that matter: the **valence band** (E_V, highest filled at 0 K) and
  the **conduction band** (E_C, lowest empty). The gap between them is the **bandgap E_g = E_C−E_V**.
  *Mechanism:* only electrons in the conduction band (or holes left in the valence band) are mobile;
  the gap is the energy "toll" to free a bonding electron.
- **Silicon E_g ≈ 1.12 eV at 300 K** (often rounded 1.1 eV; 1.17 eV at 0 K). *(verified 2026-06-24:
  ResearchGate "Band Gap Energy in Silicon"; standard.)* Ge ≈ 0.66 eV, GaAs ≈ 1.42 eV. Insulators
  have large E_g (~5 eV+, diamond); conductors have overlapping bands (no gap). **Semiconductor =
  small enough gap that thermal energy frees a useful number of carriers.**
- E_g **decreases with temperature** (Varshni relation; bonds weaken as the lattice expands/vibrates).

### Intrinsic semiconductor
- Pure Si, covalently bonded (4 valence electrons, diamond lattice). Thermal energy breaks bonds →
  an electron-hole **pair**. A **hole** is the absence of a bonding electron — it behaves as a mobile
  +q charge because a neighboring electron hops to fill it, moving the vacancy along.
- **Intrinsic carrier concentration nᵢ:** n = p = nᵢ. nᵢ = √(N_C N_V)·e^{−E_g/2kT}; the controlling
  factor is the **exp(−E_g/2kT)** — strongly temperature-dependent, roughly doubling every ~few K
  near room temp. *Mechanism:* generation rate (thermal) balances recombination rate at equilibrium.
- **Si nᵢ(300 K) ≈ 1.0–1.5×10¹⁰ cm⁻³** (see caveat). Tiny vs Si atom density ≈ 5×10²² cm⁻³ — only
  ~1 in 10¹² atoms is ionized intrinsically. This is *why* doping dominates.

### Extrinsic semiconductor (doping)
- Add **donor** impurities (group V: P, As, Sb — 5 valence e⁻): the 5th electron is loosely bound,
  ionizes at room temp → **n-type**, electrons are **majority**, holes **minority**. Donor conc N_D.
- Add **acceptor** impurities (group III: B, Al, Ga — 3 valence e⁻): accepts a bonding electron,
  creating a hole → **p-type**, holes majority, electrons minority. Acceptor conc N_A.
- **Mass-action law (load-bearing, `settled`):** **n·p = nᵢ²** *at thermal equilibrium, always*
  (intrinsic or doped). *Mechanism:* generation depends only on T (sets nᵢ²); raising one carrier by
  doping forces the other down to keep the product fixed (more electrons → faster recombination of
  holes).
- **Approximations (full ionization, room temp):**
  - n-type: n ≈ N_D, p ≈ nᵢ²/N_D (since N_D ≫ nᵢ).
  - p-type: p ≈ N_A, n ≈ nᵢ²/N_A.
  - Exact (charge neutrality): n − p = N_D − N_A, combined with n·p = nᵢ² → solve the quadratic when
    doping isn't ≫ nᵢ or when both dopants present (net = |N_D−N_A|).
- **Fermi level E_F:** the energy at which occupation probability = ½ (Fermi-Dirac). Intrinsic: E_F
  ≈ mid-gap (E_i). n-type: E_F moves **up** toward E_C; p-type: **down** toward E_V. *Mechanism:* E_F
  encodes carrier population: n = nᵢ·e^{(E_F−E_i)/kT}, p = nᵢ·e^{(E_i−E_F)/kT}. **A flat E_F across a
  system = equilibrium** (this becomes the key junction tool in U2).

### Carrier transport 1 — Drift (field-driven)
- Apply field E → carriers accelerate but scatter (lattice vibrations + ionized impurities),
  reaching an average **drift velocity** v_d = μE. **μ = mobility** (cm²/V·s). For Si ≈ μ_n 1350,
  μ_p 480 (lightly doped, 300 K) — **electrons are ~3× more mobile than holes** (lighter effective
  mass), a fact that recurs (NMOS faster than PMOS, npn preferred).
- **Drift current density:** J_drift = q(n μ_n + p μ_p)E = σE (microscopic Ohm's law).
- **Conductivity σ = q(n μ_n + p μ_p)**; **resistivity ρ = 1/σ**. For extrinsic material one term
  dominates: n-type σ ≈ qN_Dμ_n; p-type σ ≈ qN_Aμ_p.
- μ **decreases** with temperature (more lattice scattering) and with heavy doping (more impurity
  scattering). At high field, v_d **saturates** (~10⁷ cm/s in Si) — μ is no longer constant
  (matters in short-channel MOSFETs, U4/Stage-2).

### Carrier transport 2 — Diffusion (gradient-driven) ★ threshold
- A concentration *gradient* drives net carrier flow from high to low density (random thermal motion
  + imbalance), **with no field needed.** This is the carrier transport novices forget.
- **Diffusion current density:** J_n,diff = +q D_n (dn/dx); J_p,diff = −q D_p (dp/dx). (Signs: the
  electron *charge* is −q, so electron *current* ends up +qD_n·dn/dx; holes carry +q so the minus
  sign from "high→low" stays.) **D = diffusion coefficient** (cm²/s).
- **Einstein relation (load-bearing, `settled`):** **D/μ = kT/q = V_T**. *Mechanism:* drift and
  diffusion are the same scattering physics seen two ways; in equilibrium they must cancel, which
  forces this ratio. **V_T = kT/q ≈ 25.85 mV ≈ 26 mV at 300 K** *(verified 2026-06-24)*. So
  D_n ≈ 0.026·1350 ≈ 35 cm²/s, D_p ≈ 0.026·480 ≈ 12.5 cm²/s.
- **Total current = drift + diffusion**, for each carrier. The forward diode current is *diffusion*-
  dominated; resistor current is *drift*. Keeping both in mind is the whole game (U2 uses both).

### Resistivity & sheet resistance (the IC-fabrication numerical)
- **Resistance of a bar:** R = ρL/A = ρL/(W·t).
- **Sheet resistance R_s = ρ/t** (units Ω, spoken "ohms per square"). *Mechanism / why useful:* for a
  thin doped layer of fixed depth t, R = R_s·(L/W) — resistance depends only on the **number of
  squares L/W**, not absolute size. This is how IC resistors are specified. For a non-uniform doped
  layer, R_s = 1/(q ∫ μ(x)·N(x) dx) over the layer depth.

### Generation & recombination (sets up minority-carrier lifetime)
- **Generation:** create an e-h pair (thermal, optical). **Recombination:** an electron drops into a
  hole, releasing energy (heat in Si — *indirect* gap; light in GaAs — *direct* gap, hence LEDs).
- At equilibrium G = R and n·p = nᵢ². Disturb it (inject carriers, as in forward bias) and excess
  minority carriers decay with **minority-carrier lifetime τ**: Δp(t)=Δp₀e^{−t/τ}. Tied to the
  **diffusion length L = √(Dτ)** — how far minority carriers diffuse before recombining. **L and τ
  are the bridge to the diode current** (U2): they set how steep the injected-carrier gradient is.

### Worked-problem patterns (what the exam asks)
1. **Carrier conc:** given N_D (or N_A), find majority/minority conc via n≈N_D, p=nᵢ²/N_D. (Watch
   the nᵢ value used — see caveat.)
2. **Compensated material:** both dopants → net = |N_D−N_A|, then mass-action for the minority; if
   net is comparable to nᵢ, solve the quadratic n−p=N_D−N_A with np=nᵢ².
3. **Conductivity/resistivity:** σ=q(nμ_n+pμ_p); intrinsic vs extrinsic; effect of T on σ (carriers
   ↑ dominates intrinsic; mobility ↓ dominates heavily-doped extrinsic).
4. **Sheet resistance:** R = R_s·(L/W); count squares; R_s=ρ/t.
5. **Einstein relation:** get D from μ (or vice versa) at a stated T; recompute V_T off 300 K.
6. **Drift velocity / current:** v_d=μE; J=σE; resistance of a doped bar.

### Key formulas (verified)
- n·p = nᵢ² (equilibrium) · n≈N_D, p≈N_A (full ionization) · charge neutrality n+N_A⁻ = p+N_D⁺
- σ = q(nμ_n+pμ_p), ρ=1/σ · R=ρL/A · R_s=ρ/t, R=R_s(L/W)
- J_drift=σE · J_n,diff=qD_n dn/dx · D/μ=kT/q=V_T (≈25.85 mV @300 K)
- n=nᵢe^{(E_F−E_i)/kT}, p=nᵢe^{(E_i−E_F)/kT} · nᵢ=√(N_C N_V)e^{−E_g/2kT} · L=√(Dτ)

---
**Stage 2 (deep structure) — ✓ BUILT (2026-06-24):** lives separately in
`stage-2/01-semiconductor-physics.md` — kept out of this exam file on purpose. *Adds:* density-of-states & effective mass derivation of N_C/N_V and nᵢ; Fermi-Dirac → Boltzmann
approximation and its validity (non-degenerate limit); incomplete ionization & freeze-out at low T;
degenerate doping + bandgap narrowing (why heavily-doped nᵢ_eff rises); derivation of the Einstein
relation from detailed balance; scattering mechanisms & the μ(T,N) Caughey-Thomas model; velocity
saturation physics; direct vs indirect gap (E-k diagrams) and its device consequences.
