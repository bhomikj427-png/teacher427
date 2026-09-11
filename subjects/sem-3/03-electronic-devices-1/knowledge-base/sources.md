# ECE2101 Electronic Devices-I — sources (tiered, dated, confidence-marked)

> Per `subject-research-protocol.md` §2/§5. Tier-1 = prescribed textbooks (truth) + official
> syllabus (scope). Stage-1 content is anchored on Boylestad + Sedra-Smith (the standard ECE-UG
> pair); Neamen/Streetman/Sze carry the physics depth (Stage-2 primary). Web sources below were
> used to **verify load-bearing exact constants this session** (recall ≠ sourced, protocol §1).

## Tier 1 — Prescribed textbooks (content truth)
- **Boylestad & Nashelsky, *Electronic Devices and Circuit Theory*, 10e (2009).** Primary Stage-1
  anchor for diode/JFET/BJT characteristics, models, biasing, diode circuits. `settled`.
- **Sedra & Smith, *Microelectronic Circuits*, 7e (2014).** Primary for MOSFET (ch.5) & BJT (ch.6)
  square-law/exponential models, small-signal, regions. `settled`.
- **Neamen, *Semiconductor Physics and Devices*, 4e (2012).** Semiconductor physics, junction
  electrostatics, device derivations (bridges Stage-1↔2). `settled`.
- **Streetman & Banerjee, *Solid State Electronic Devices*, 7e (2014).** Bands, carriers, junction
  physics (Stage-2 leaning). `settled`.
- **Sze & Ng, *Physics of Semiconductor Devices*, 3e (2006).** → Stage-2 primary (deep physics).
- **Gray, Hurst, Lewis & Meyer, *Analysis & Design of Analog ICs*, 5e (2015).** → Stage-2 (analog IC).

## Tier 2 — Official scope (not truth)
- **MUJ B.Tech ECE Syllabus 2023-onwards (PDF).** Defines the official ECE2101 unit list & textbooks
  (verbatim in `../course-info.md`). Scope `settled`; exam-unit boundaries `uncertain` (no handout).
  URL in `course-info.md` (pulled 2026-06-16).

## Tier 3 — Triangulation / standard course material (confirm, not final word)
- **NPTEL** (Semiconductor Devices / Electronic Devices courses) — for triangulation; ingest
  lectures via `tools/fetch_transcripts.py` (ASR caveat: verify formulas vs textbook). *Not yet pulled.*
- **MIT OCW 6.012 Microelectronic Devices and Circuits** — triangulation for device models.

## Web sources used THIS SESSION to verify exact constants (2026-06-24)
- **PVEducation — Intrinsic Carrier Concentration** <https://www.pveducation.org/pvcdrom/pn-junctions/intrinsic-carrier-concentration>
  — Si nᵢ value & temperature dependence. Used for the nᵢ discrepancy (`00-map.md` register, `01`).
- **OSTI biblio 5748038 — "Improved value for the silicon intrinsic carrier concentration
  275–375 K"** <https://www.osti.gov/biblio/5748038> — confirms refined nᵢ ≈ 1.0×10¹⁰ (Sproul/Green)
  vs older 1.45–1.5×10¹⁰.
- **Springer, *Silicon* (2023), "Recalculation of Intrinsic Carrier Concentration in Si at 300 K"**
  <https://link.springer.com/article/10.1007/s12633-023-02674-2> — modern best value ≈9.65×10⁹
  (Altermatt). → conclusion: **teach nᵢ as textbook-dependent 1.0–1.5×10¹⁰**, don't pin.
- **ResearchGate, "Band Gap Energy in Silicon"** <https://www.researchgate.net/publication/241884255_Band_Gap_Energy_in_Silicon>
  — Si E_g ≈ 1.12 eV @300 K (1.17 eV @0 K, Varshni T-dependence). `settled`.
- Thermal voltage V_T=kT/q ≈ 25.85 mV @300 K — confirmed via the bandgap-reference search
  (PTAT slope ~+0.086 mV/°C); standard. `settled`.

## Verification pass — load-bearing claims checked vs external sources (2026-06-24)
> Per protocol §1 ("recall ≠ sourced"). Each item below was confirmed against ≥1 external source
> *this session* (most against ≥2); algebraic identities are marked "by derivation" (the derivation
> is the verification — they are not empirical). This is what earns the `settled` marks; anything not
> here that is a specific number/edge-case stays `uncertain`.

**Empirical specifics — externally verified (≥2 independent where noted):**
- Si **μ_n ≈ 1350**, **μ_p ≈ 480 cm²/V·s**, **v_sat ≈ 10⁷ cm/s**, **ε_r = 11.7** @300 K — Wikipedia
  *Electron mobility*; eesemi/HTElabs Si-300K tables. `settled`.
- **V_T = kT/q ≈ 25.85 mV @300 K** (25.852 mV) — Wikipedia *Shockley diode equation*. `settled`.
- Si **E_g ≈ 1.12 eV**, **N_C≈2.8×10¹⁹**, **N_V≈1.0–1.8×10¹⁹** — (see above + `stage-2/sources.md`).
- **Diode forward V tempco ≈ −2 mV/°C** (−2.2 at RT) — Testbook; JEEE article. `settled`.
- **Reverse current ≈ doubles every ~10 °C** in Si (measured/generation-limited, ∝nᵢ); the ideal
  diffusion I_S (∝nᵢ²) alone ≈ 5 °C — Brainly/Fiveable refs; Wikipedia *Saturation current*. **This
  corrected a draft error ("~5 °C" unqualified).** `settled`. (See CHANGELOG.)
- **Breakdown:** Zener (tunneling) dominant ≲5–6 V with **negative** TC; avalanche dominant ≳6 V with
  **positive** TC; min-TC reference 4.7–5.6 V — ScienceDirect *Zener Breakdown*; Toshiba FAQ; Kynix.
  `settled`. (Confirms `02` breakdown section + M10.)
- **Cut-in voltages:** Si ≈ 0.6–0.7 V, Ge ≈ 0.3–0.35 V — electronics-tutorials.ws; Kasap *pn Junction
  Devices*. Schottky ≈ 0.2–0.45 V (lower; less precisely pinned — `settled` as a range). `settled`.

**Formula forms — externally verified:**
- **V_bi = (kT/q) ln(N_A N_D/nᵢ²)** and **W = √[2ε(N_A+N_D)V_bi/(q N_A N_D)]** (≡ my 1/N_A+1/N_D
  form) — TU-Graz PSD problem set; BYU pn-junction calculator; Kasap. `settled`.
- **Shockley I = I_S(e^{V/nV_T}−1)**, reverse → −I_S — Wikipedia. `settled`.
- **MOSFET** triode I_D=μC_ox(W/L)[V_ov V_DS−V_DS²/2]; sat I_D=½μC_ox(W/L)V_ov²(1+λV_DS);
  **g_m=2I_D/V_ov**; body effect V_t=V_t0+γ[√(V_SB+2φ_B)−√(2φ_B)] — Wikipedia *MOSFET*. `settled`.

**Identities verified BY DERIVATION (non-empirical — derivation = verification):**
- BJT: I_E=I_C+I_B; β=α/(1−α); α=β/(β+1); I_E=(β+1)I_B; **g_m=dI_C/dV_BE=I_C/V_T**; r_π=β/g_m.
- JFET: g_m=dI_D/dV_GS of I_DSS(1−V_GS/V_P)² = (−2I_DSS/V_P)(1−V_GS/V_P) = 2√(I_DSS I_D)/|V_P|.
- MOSFET: g_m=μC_ox(W/L)V_ov=√(2μC_ox(W/L)I_D) (from I_D=½μC_ox(W/L)V_ov²).
- Rectifier averages: HW V_dc=(1/2π)∫₀^π V_m sinθ dθ=V_m/π; FW=2V_m/π. ✓

**NOT verified this session → remain `uncertain` (mechanisms taught, numbers not pinned):**
- Stage-2 empirical/frontier specifics: E_crit≈3×10⁵ V/cm, ionization coefficients, **V_BR∝N^{−3/4}**,
  JFET ZTC offset (~0.63 V), **BV_CEO≈BV_CBO/β^{1/n}** exponent, FinFET/GAA node years, θ
  mobility-degradation, exact N_V. Flagged in the `stage-2/` files + `stage-2/sources.md`.

## Exam material (PYQs / PPTs)
- **None ingested** as of 2026-06-24 (`../exam-pack/` empty). `exam-map.md` is a provisional,
  inferred stub flagged `uncertain`. Drop MTE/ETE papers + PPTs into `../exam-pack/` (or `../../_inbox/`)
  to make Stage-1 exam-targeted. See `../../research-engine/exam-resources.md`.

## Confidence summary
- `settled`: all standard device equations & mechanisms (Shockley diode, square-law MOSFET, JFET
  Shockley eqn, BJT α/β & exponential, junction electrostatics, drift/diffusion, Einstein relation).
- `contested`: silicon nᵢ exact value (textbook-dependent — teach the spread).
- `uncertain`: exact MUJ unit/MTE-ETE boundaries; topic weightage (no PYQ); a few misconceptions
  (M6, M13, M19, M24) not yet sourced to education literature.
