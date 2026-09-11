# Unit 1 — Semiconductor Physics — STAGE 2 (deep structure)

> Built **on top of** Stage-1 `../01-semiconductor-physics.md` (do not edit that exam file). Primary
> sources climb to Sze & Ng 3e, Streetman 7e, Neamen 4e, Pierret. Load-bearing specifics
> triangulated/verified this session (`sources.md` here). Confidence as marked.

## 1. Density of states & where nᵢ really comes from (derivation)
- Free-electron-in-a-box → **DOS** g(E) ∝ √(E−E_C) near the band edge (3-D parabolic band).
  Multiply by Fermi-Dirac f(E) and integrate → carrier densities.
- **Effective density of states** (parabolic-band, Boltzmann tail):
  **N_C = 2(2πm_n*kT/h²)^{3/2}**, **N_V = 2(2πm_p*kT/h²)^{3/2}** — both ∝ T^{3/2}.
- Then **n = N_C e^{−(E_C−E_F)/kT}**, **p = N_V e^{−(E_F−E_V)/kT}**, and the product
  **np = N_C N_V e^{−E_g/kT} = nᵢ²** — *independent of E_F* (mass-action proved; this is why doping
  can't change the product at equilibrium). So **nᵢ = √(N_C N_V)·e^{−E_g/2kT}**.
- **Si @300 K (verified 2026-06-24):** N_C ≈ 2.8×10¹⁹ cm⁻³; N_V ≈ 1.0–1.8×10¹⁹ (source-dependent —
  *(eesemi/HTElabs/Green 1990; ResearchGate)*). **★ This spread in N_V (via the hole effective mass,
  itself a warped/degenerate-band average) is the deep reason nᵢ is textbook-dependent** (Stage-1
  `contested` flag): nᵢ = √(N_C N_V)e^{−E_g/2kT} inherits the m* uncertainty *and* is exponentially
  sensitive to E_g. So the 1.0 vs 1.5×10¹⁰ disagreement isn't sloppiness — it's m* + E_g convention.
- **Intrinsic level E_i** sits not exactly mid-gap: E_i = (E_C+E_V)/2 + (kT/2)ln(N_V/N_C) — offset
  by the DOS asymmetry (small for Si, ~ a few meV below midgap).

## 2. Fermi-Dirac → Boltzmann: the non-degenerate assumption (and when it lies)
- Stage-1's n = N_C e^{−(E_C−E_F)/kT} is the **Boltzmann approximation** to Fermi-Dirac, valid only
  when E_F is ≳ 3kT below E_C (**non-degenerate**). The exact result needs the **Fermi-Dirac
  integral** F_{1/2}(η).
- **Breaks (degenerate) when:** heavy doping (N_D ≳ 10¹⁹), E_F enters the band. Then n ≠ N_D simply,
  Boltzmann over-counts, and you need F_{1/2}. **Where the UG textbook lies:** "n = N_D, fully
  ionized, Boltzmann" silently assumes non-degenerate, room-T, complete ionization — all three fail
  in real devices (source/drain, emitters).

## 3. Incomplete ionization & carrier freeze-out
- Stage-1 assumes **full ionization**. At **low T** dopants don't fully ionize (E_F rises above the
  donor level): **freeze-out**, n < N_D, conductivity collapses — the carriers "freeze" onto the
  dopant atoms. The donor occupancy uses a degeneracy-factor (g=2) Fermi function. Three regimes vs
  T: **freeze-out → extrinsic (n≈N_D, flat) → intrinsic (n≈nᵢ, rises)** — the classic n(T) curve.
- High-T intrinsic onset is why power devices and the intrinsic-region of any device fail hot
  (leakage ∝ nᵢ² runs away).

## 4. Heavy doping: bandgap narrowing & nᵢ,eff
- At high doping, impurity bands + many-body effects **shrink E_g** (bandgap narrowing, ΔE_g grows
  ~with ln N). Effective **nᵢ,eff² = nᵢ² e^{ΔE_g/kT}** rises. *Consequence:* heavily-doped BJT
  emitters have degraded injection efficiency (a Stage-2/U5 link — limits β); a white lie the simple
  α/β story hides.

## 5. Einstein relation, derived from detailed balance
- At equilibrium total current of each carrier = 0 everywhere: qμ_n n E + qD_n dn/dx = 0. Use the
  built-in field E = (1/q)dE_i/dx (from band bending) and n = nᵢ e^{(E_F−E_i)/kT} with E_F flat
  (equilibrium) → **D_n/μ_n = kT/q.** *This is not an approximation* — it's forced by equilibrium +
  Boltzmann statistics. (Degenerate version: D/μ = (kT/q)·F_{1/2}/F_{−1/2}, the generalized Einstein
  relation — another non-degenerate-limit white lie.)

## 6. Mobility: the real μ(T, N, E)
- Stage-1 "μ ≈ const" hides three regimes. **Matthiessen's rule** combines scattering: 1/μ = 1/μ_lattice
  + 1/μ_impurity + …
  - **Lattice (phonon) scattering:** μ ∝ T^{−3/2} (dominates lightly doped / high T).
  - **Ionized-impurity scattering:** μ ∝ T^{+3/2}/N (Conwell-Weisskopf/Brooks-Herring; dominates
    heavy doping / low T) — so μ *falls* with doping.
  - Empirical **Caughey-Thomas:** μ(N) = μ_min + (μ_max−μ_min)/(1+(N/N_ref)^α).
- **Velocity saturation:** at high field v_d → v_sat ≈ 10⁷ cm/s (Si); v = μE/(1+E/E_c). *Mechanism:*
  optical-phonon emission caps energy gain. **This kills the MOSFET square law in short channels**
  (Stage-2/U4): I_D becomes ∝ V_OV (linear), not V_OV².

## 7. Continuity & the ambipolar transport equation (the engine for every device)
- **Continuity equation:** ∂n/∂t = (1/q)∂J_n/∂x + (G−R). Substituting drift+diffusion gives the
  full transport PDE. The **minority-carrier diffusion equation** (low injection, quasi-neutral,
  no field) ∂Δp/∂t = D_p ∂²Δp/∂x² − Δp/τ_p is the workhorse that yields the **diode current**
  (Stage-2/U2) and the **BJT base profile** (Stage-2/U5). **L = √(Dτ)** falls out as its decay length.
- **SRH recombination:** R = (np−nᵢ²)/[τ_p(n+n₁)+τ_n(p+p₁)] — trap-assisted, the real lifetime
  mechanism in Si (indirect gap → band-to-band is weak). Adds **Auger** (∝n³, heavy injection) and
  **surface recombination** (S·Δn) for the full picture.

## 8. Direct vs indirect gap (E-k) and device consequences
- Si/Ge **indirect** (conduction min not over valence max in k-space): radiative recombination needs
  a phonon → slow, weak → **Si is a poor light emitter** but fine for absorption/electronics. GaAs
  **direct** → efficient LEDs/lasers, higher μ. This single band-structure fact explains the
  optoelectronics material split.

## 9. Cross-topic unification
- E_F flat = equilibrium; **quasi-Fermi levels (F_n, F_p) split under bias** → the unifying language
  for *every* biased device (np = nᵢ² e^{(F_n−F_p)/kT}; the junction "law" p_n=p_n0 e^{V/V_T} is
  just F_n−F_p = qV). Carry this into U2–U5.
- DOS ∝ √E (3-D) → constant (2-D, quantum wells/MOS inversion layer) → the 2-D DOS underlies modern
  device electrostatics (Stage-2/U4 quantum-confinement V_t shift).

## 10. Harder problem classes
- Compute nᵢ from N_C,N_V,E_g and reconcile with a textbook's quoted value (explain the m*/E_g
  source of the discrepancy). · n(T) across freeze-out/extrinsic/intrinsic. · Generalized Einstein
  in the degenerate limit. · Steady-state Δp(x) from the diffusion equation with a given injection BC.
  · "Why is Si used for ICs but GaAs for lasers?" (E-k argument).

## Open / to-verify (Stage 2)
- `[opened 2026-06-24]` Exact Si N_V value (1.04 vs 1.83×10¹⁹) — m_p* convention; not pinned, teach
  as convention-dependent (ties to the nᵢ `contested` flag). *(verified spread, not a single number.)*
