# Unit 2 — PN Junctions & Diodes — STAGE 2 (deep structure)

> On top of Stage-1 `../02-pn-junctions.md`. Primary: Sze 3e ch.2, Streetman 7e ch.5–6, Neamen ch.7–9.
> The single most important derivation in the course (the diode equation) lives here.

## 1. Junction electrostatics, derived (depletion approximation)
- **Depletion approximation:** assume the SCR is fully depleted of mobile carriers (ρ = qN_D on n-
  side, −qN_A on p-side) with abrupt edges; neutral regions field-free. Then Poisson d²φ/dx² = −ρ/ε_s
  integrates twice. Field is **triangular** (peak E_max at the junction = qN_D x_n/ε_s = qN_A x_p/ε_s),
  potential is **parabolic**.
- Charge balance **N_A x_p = N_D x_n** (overall neutrality) → most of W and most of the voltage drop
  on the **lightly doped** side. Total **V_bi = ½ E_max·W**, giving Stage-1's W(V) formula.
- **Where it lies:** real edges aren't abrupt (there's a Debye-length ~√(ε_skT/q²N) tail); mobile-
  carrier "spill" makes the true transition smooth. The depletion approx is excellent for W and C_j,
  poorer near the edges and at low bias.
- **Linearly graded junction:** ρ = qax → W ∝ (V_bi−V)^{1/3}, C_j ∝ (…)^{−1/3} (the m=⅓ in Stage-1).
- **C-V profiling:** 1/C_j² is linear in V_R with slope ∝ 1/N → measuring C(V) extracts the doping
  profile. A real lab/characterization technique (links ECE2130).

## 2. The Shockley diode equation, fully derived (the centerpiece) ★
1. **Law of the junction** (from quasi-Fermi splitting, Stage-2/U1 §9): under bias V, minority
   density at the depletion edge is raised by e^{V/V_T}: **p_n(x_n) = p_n0 e^{V/V_T}**,
   n_p(−x_p) = n_p0 e^{V/V_T}. (Low-injection, quasi-equilibrium across the thin SCR.)
2. **Solve the minority-carrier diffusion equation** in each neutral region: D_p p_n'' = (p_n−p_n0)/τ_p
   → Δp_n(x) = p_n0(e^{V/V_T}−1) e^{−(x−x_n)/L_p} (long-diode BC: decays over L_p=√(D_pτ_p)).
3. **Diffusion current at the edge** J_p = −qD_p dΔp/dx |_{x_n} = (qD_p p_n0/L_p)(e^{V/V_T}−1); same
   for electrons. Sum (current continuous across the SCR if no recombination there):
   **J = J_S(e^{V/V_T}−1)**, with **J_S = qD_p p_n0/L_p + qD_n n_p0/L_n = q nᵢ²(D_p/(L_p N_D) +
   D_n/(L_n N_A))** — proving I_S ∝ nᵢ² (hence the steep T-dependence) and showing the **lightly-doped
   side dominates injection.**
- **Short (narrow) diode:** if the neutral region ≪ L, the profile is **linear**, L is replaced by
  the **physical width W_B** → J_S = qD p_n0/W_B. This *is* the BJT base transport (Stage-2/U5).

## 3. Departures from ideal (the η-factor and the real I-V) — where the UG model lies
- **Recombination in the SCR (Sah-Noyce-Shockley):** mid-gap traps give an extra current
  J_rec ∝ nᵢ·e^{V/2V_T} (the **η=2** term), dominant at **low forward bias** in Si. So real Si log-I
  vs V has slope ~2 at low V, →1 at moderate V.
- **High-level injection:** when Δp ≳ majority density, slope returns toward 2 and I rolls off.
- **Series resistance R_s:** at high current V = ηV_T ln(I/I_S) + I·R_s — the curve bends over.
- Together: the real Si diode has **four regions** on a log-I–V plot (recombination η≈2 → ideal η≈1 →
  high-injection → series-R). Knowing which regime you're in is the Stage-2 skill.
- **Reverse current** isn't flat at −I_S either: **generation in the SCR** adds J_gen = qnᵢW/τ_g
  (∝ nᵢ, grows with W ∝ √V_R) — usually ≫ the ideal I_S in Si. So Si reverse leakage is generation-,
  not diffusion-, limited and rises with reverse voltage.

## 4. Breakdown physics, quantitatively
- **Avalanche:** multiplication M = 1/(1−∫α dx), α = ionization coefficient ∝ e^{−b/E}. Diverges →
  breakdown. V_BR scales with the lighter doping: **V_BR ∝ N^{−3/4}** (lower doping → higher V_BR),
  positive tempco (phonon scattering shortens the ionizing mean free path). Critical field E_crit ≈
  3×10⁵ V/cm in Si (rises slowly with N).
- **Zener (tunneling):** band-to-band tunneling probability ∝ e^{−(const·E_g^{3/2})/E}; needs
  E ≳ 10⁶ V/cm → only in heavily-doped, narrow junctions. Negative tempco (E_g shrinks with T →
  easier tunneling). The ~5–6 V crossover gives the near-zero-tempco reference diode.
- **Punch-through** (the SCR reaches the other contact) is a third reverse-limit in narrow bases.

## 5. Metal–semiconductor junctions (Schottky), properly
- Barrier **φ_B = φ_m − χ** (ideal Schottky-Mott; χ = electron affinity). Real barriers are pinned by
  **interface states** (Bardeen) → weak φ_m dependence. Depletion only on the semiconductor side.
- Current is **thermionic emission** over the barrier: J = A*T² e^{−φ_B/kT}(e^{V/V_T}−1) — same V-shape
  as a p-n diode but **majority-carrier**, so **no minority storage → fast; lower turn-on** (φ_B set,
  ~0.2–0.45 V). **Image-force lowering** Δφ reduces φ_B slightly with field.
- **Ohmic contact:** make the semiconductor so heavily doped (n⁺) that the barrier is thin enough to
  **tunnel** through → low, linear resistance. *Same metal-semiconductor junction, opposite design
  goal* — a key Stage-2 distinction the UG course glosses.

## 6. Switching transient — charge-control model
- Stored minority charge Q = I_F·τ. On reverse switching, current reverses to ~I_R while the stored
  charge is removed: **storage time t_s = τ ln[(I_F+I_R)/I_R]**, then a transition time as C_j
  recharges. **t_rr = t_s + t_t.** This is the quantitative basis for "Schottky switches faster"
  (no stored minority Q → t_s≈0).

## 7. Cross-topic unification
- The diode is **one junction**; the **BJT is two** sharing a thin base (Stage-2/U5 reuses §2 with W_B
  for L). The **JFET/MOSFET** reuse §1 electrostatics (depletion-width control). The **varactor**
  is C_j(V); the **solar cell/photodiode** is the same J(V) shifted by a photo-generated I_L
  (J = J_S(e^{V/V_T}−1) − I_L). One equation, many devices — the expert's compression.

## 8. Harder problem classes
- Derive J_S for a short vs long diode; show the BJT base-transport limit. · Identify the η from a
  log-I–V slope and name the dominant mechanism. · Reverse leakage: separate diffusion (∝nᵢ²,
  T-doubling ~5 °C) from generation (∝nᵢ, ∝√V_R). · V_BR(N) scaling; pick avalanche vs Zener from
  doping. · Schottky vs p-n turn-on & recovery. · Photodiode/solar-cell I-V & fill factor.

## Open / to-verify (Stage 2)
- `[opened 2026-06-24]` Si E_crit and α(E) ionization coefficients are field/temperature fits with
  spread across sources — teach as ~3×10⁵ V/cm order-of-magnitude, not a pinned constant.
