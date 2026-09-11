# ECE2101 Electronic Devices-I — CHANGELOG (correction audit trail)

> Per `subject-research-protocol.md` §10. Append-only. Records what changed, why, and the source.
> Confidence can move both ways; corrections are logged here, never silently overwritten.

## 2026-06-24 — Stage 1 built (learner-activated, depth-first)
- **Created** `00-map.md` (big ideas, prereq graph, threshold concepts, scope, register),
  `exam-map.md` (provisional `uncertain` stub — no PYQ), units `01`–`05`, `misconceptions.md`,
  `sources.md`, this file. Status `stage-0` → `stage-1` → **`stage-1✓`** (see exit test below).
- **Verified this session (load-bearing exact constants, protocol §1):**
  - Silicon **nᵢ** is **textbook-dependent** — logged as `contested`, resolved-as-teach-the-spread
    (1.0–1.5×10¹⁰ cm⁻³): Boylestad/older 1.5×10¹⁰, refined ≈1.0×10¹⁰ (Sproul/Green), best measured
    ≈9.65×10⁹ (Altermatt). Sources: PVEducation, OSTI 5748038, Springer *Silicon* 2023. This caveat
    is propagated into `01` (intrinsic), `02` (V_bi, I_S∝nᵢ²), and the `00-map` register.
  - Silicon **E_g ≈ 1.12 eV @300 K** (1.17 @0 K), **V_T=kT/q ≈ 25.85 mV @300 K** — `settled`
    (ResearchGate Band-Gap-in-Si; bandgap-reference PTAT search).
- **Scope decision:** Stage-1 truth anchored on Boylestad 10e + Sedra-Smith 7e; physics depth
  (Neamen/Streetman/Sze) deferred to Stage 2. Logged to `sources.md`.

### Stage-1 exit test (representative textbook problems — no PYQ in hand, so exam-targeting UNCONFIRMED)
Confirmed the base answers each from mechanism, method shown, citing a prescribed text:
1. **U1** — n-type Si, N_D=10¹⁶: n≈10¹⁶, p=nᵢ²/N_D; σ=qN_Dμ_n; sheet R = ρ/t. ✓ (`01`)
2. **U2** — V_bi from doping (V_T ln(N_A N_D/nᵢ²)); depletion width scaling with V_R; diode I from
   Shockley + CVD model; rectifier V_dc/PIV/ripple; Zener regulator R_S range. ✓ (`02`)
3. **U3** — JFET I_D from Shockley square law given I_DSS,V_P; self-bias Q-point; g_m. ✓ (`03`)
4. **U4** — MOSFET region ID (V_OV>0, V_DS vs V_OV) → I_D (triode/sat); CS gain −g_m(R_D∥r_o);
   CMOS inverter outputs + static power = 0. ✓ (`04`)
5. **U5** — α/β conversions; region ID from junction biases; divider-bias Q-point (β-independent);
   CE gain; BJT-vs-MOSFET table. ✓ (`05`)
**Result:** all units pass from mechanism → **`stage-1✓`**. Caveat: exam-targeting unconfirmed
until PYQs/PPTs are dropped into `exam-pack/` (then rebuild `exam-map.md`, re-weight depth).

## 2026-06-24 — Stage 2 built (learner-activated, depth-first) → `stage-2✓`
- **Created** `stage-2/01`–`05` (mirrored deep-structure unit files) + `stage-2/sources.md`. Status
  `stage-1✓` → `stage-2` → **`stage-2✓`** (§0 surplus test below). The five Stage-1 unit-file
  pointers flipped "PENDING" → "✓ BUILT".
- **Deep structure added:** DOS/effective-mass derivation of N_C,N_V,nᵢ + why nᵢ is convention-
  dependent; Fermi-Dirac→Boltzmann validity, freeze-out, bandgap narrowing; Einstein from detailed
  balance; μ(T,N,E) regimes + velocity saturation; continuity/diffusion-eqn engine; **full Shockley-
  diode derivation** (law of the junction → diffusion eqn → J_S∝nᵢ²), η=2 recombination, generation-
  limited reverse leakage, breakdown quantitatively, Schottky thermionic emission vs ohmic contact,
  reverse-recovery charge control; **MOS V_t/γ derivation, square-law derivation, and the four short-
  channel corrections** (velocity sat → linear I_D, mobility degradation, DIBL, **subthreshold
  60 mV/dec floor**); CMOS scaling (Dennard → end → FinFET/GAA/high-κ); JFET GCA derivation, ZTC,
  1/f-noise, MESFET/HEMT; **BJT base-profile derivation of α/β** (γ·α_T, Gummel number), Ebers-Moll/
  Gummel-Poon, Early effect, Kirk/Webster, BV_CEO vs BV_CBO, charge-control switching, SiGe HBT.
- **Cross-topic unification (the §0 generative structure):** quasi-Fermi levels unify all biased
  devices; one junction → diode, two → BJT, depletion-control → JFET/MOSFET; **subthreshold MOSFET =
  BJT** (BJT is the ideal 60 mV/dec device); g_m=I_C/V_T vs 2I_D/V_OV explains the analog/digital split.
- **Verified this session (protocol §1):** Si N_C≈2.8×10¹⁹, N_V≈1.0–1.8×10¹⁹ (m*-convention spread —
  *grounds* the Stage-1 nᵢ `contested` flag; eesemi/HTElabs/Green 1990); subthreshold floor
  S=ln10·kT/q=59.5 mV/dec @300 K (computed from verified V_T; Taur-Ning/Sze). Logged in `stage-2/sources.md`.
- **Promoted misconceptions** M6, M13, M19, M24 `uncertain`→`settled` (now grounded in the Stage-2
  derivations above).

### Stage-2 exit test (§0 surplus — expert / "why-not-what" / edge-case, answered from mechanism + primary sources)
1. *Why do textbooks disagree on Si nᵢ?* → m_p* (N_V) convention + exponential E_g sensitivity, not
   error (`stage-2/01` §1). ✓
2. *Derive the diode I_S and show it equals the BJT collector saturation current in the thin-base
   limit.* → short-diode J_S=qD p_n0/W (`stage-2/02` §2 = `stage-2/05` §1). ✓
3. *Why can't CMOS supply voltage keep scaling?* → 60 mV/dec subthreshold floor → leakage can't be
   shut off → V_t/V_DD wall → Dennard ended (`stage-2/04` §3,§6). ✓
4. *Is the MOSFET square law right?* → No: velocity saturation makes I_D∝V_OV (linear) in short
   channels; four named corrections (`stage-2/04` §3). ✓
5. *Why does β fall at high I_C, and why SiGe?* → Webster/Kirk roll-off; HBT band offset beats the
   doping-vs-bandgap-narrowing ceiling (`stage-2/05` §4,§6). ✓
6. *In what sense is a BJT a "better" MOSFET and vice versa?* → exponential n=1 (high g_m, ideal
   switch) vs insulated gate (high Z_in, low-power, scalable) (`stage-2/05` §7). ✓
**Result: §0 surplus test passed → `stage-2✓`. Subject is now TEACH-READY** (gate met), subject to
the open items below (none block teaching; exam-targeting still wants PYQs to weight depth).

## 2026-06-24 — Verification pass (the "do the real work" pass) + gap patch
> Triggered by a completeness challenge. Goal: stop labeling recall as `settled` — actually verify
> load-bearing claims vs external sources this session (protocol §1), fix gaps, correct errors.

- **Correction (real error caught):** Unit `02` + misconception M12 said the diode **reverse current
  doubles every ~5 °C**. Verified figure: a *real* Si diode's reverse current **≈ doubles every
  ~10 °C** (generation-dominated, ∝nᵢ); only the *ideal* diffusion I_S (∝nᵢ²) doubles ~5 °C. Both
  files corrected to quote ~10 °C with the nᵢ-vs-nᵢ² distinction. (Sources: Wikipedia *Saturation
  current*; Brainly/Fiveable; consistent with `stage-2/02` §3 generation-vs-diffusion leakage.)
- **Gap patched:** added the **continuity equation** to Stage-1 unit `02` (syllabus names "Poisson &
  continuity equations"; it was previously only in `00-map`/`stage-2`). Now: Poisson→field/width,
  continuity→current, leading into Shockley.
- **Verified vs external sources this session (now legitimately `settled`):** Si μ_n/μ_p, v_sat, ε_r;
  V_T=25.85 mV; E_g, N_C, N_V; V_D tempco −2 mV/°C; reverse-current 10 °C rule; Zener/avalanche
  ranges + TC signs; cut-in voltages; V_bi & depletion-width formulas; Shockley form; MOSFET
  triode/sat/g_m/body-effect forms. **Verified by derivation:** BJT α/β/g_m/r_π identities, JFET &
  MOSFET g_m, rectifier averages. Full list with sources → `sources.md` "Verification pass".
- **Honest confidence re-marking:** the above are `settled` *because checked*, not because recalled.
  **Stage-2 empirical/frontier specifics that were NOT externally verified** (E_crit, V_BR∝N^{−3/4},
  ZTC offset, BV_CEO exponent, FinFET node years, θ, exact N_V) **remain `uncertain`** — mechanisms
  taught, numbers not pinned (already flagged in `stage-2/` files; restated in `sources.md`).

### Honest status after this pass
- **Stage 1: load-bearing claims verified → genuinely `stage-1✓`.** Syllabus coverage now complete
  (continuity added). The exam-ready set is trustworthy.
- **Stage 2: derivations + unifications are mechanism-sound (verifiable); several frontier/empirical
  specifics remain `uncertain` and are flagged as such.** The deep structure is real; not every
  Stage-2 number is source-pinned. This is an *honest* `stage-2✓`: `settled` where earned, `uncertain`
  where not — not a blanket `settled`. Remaining to fully close Stage 2: source-verify the flagged
  specifics and work the "harder problem classes" with solutions (currently listed, not solved).

## Open items carried forward (see `00-map.md` register)
- Exact MUJ unit/MTE-ETE boundaries (`uncertain`) — needs official handout + PYQs (re-scope only).
- Silicon nᵢ exact value (`contested`) — teach the spread; recheck for newer best bound on re-entry.
- Process/empirical constants (E_crit, ionization coeffs, ZTC offset, BV_CEO exponent, N_V exact)
  (`uncertain`) — mechanisms taught, numbers not pinned (`stage-2/sources.md`).
- ~~Misconceptions M6, M13, M19, M24~~ — promoted to `settled` 2026-06-24 (Stage-2 grounded).
- **Next:** TEACH-READY (`stage-2✓`). On teaching activation: run the teaching loop, lead with
  exam-relevant material (scoring-over-depth). Re-verify stale/`contested` claims on re-entry. Rebuild
  `exam-map.md` + re-weight depth when PYQs/PPTs land in `exam-pack/`.
