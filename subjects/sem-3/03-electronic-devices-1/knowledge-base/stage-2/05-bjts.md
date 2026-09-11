# Unit 5 — BJTs — STAGE 2 (deep structure)

> On top of Stage-1 `../05-bjts.md`. Primary: Sze 3e ch.5, Gray-Meyer 5e, Razavi, Streetman ch.7.
> Reuses the junction diffusion machinery (Stage-2/U2 §2) on a *thin* base.

## 1. Minority-carrier profile in the base → α, β derived
- Forward-active npn: BE junction injects electrons into the p-base; BC junction (reverse) collects.
- Solve the **minority-carrier diffusion equation in the base** with BCs n_p(0)=n_p0 e^{V_BE/V_T} (BE
  edge) and n_p(W_B)≈0 (BC reverse-biased sweeps it to ~0). For **W_B ≪ L_n** (thin base) the profile
  is **nearly linear** → dominated by **diffusion**, the short-diode limit of Stage-2/U2 §2.
- **Collector current** I_C = qA D_n·(dn/dx) = (qA D_n n_p0/W_B)·e^{V_BE/V_T} → **I_S = qA D_n nᵢ²/(N_B
  W_B)**. So I_C is exponential in V_BE and **∝ 1/(N_B W_B)** = inverse **base Gummel number** ∫N_B dx.
- **Base current** = recombination in base + hole back-injection into emitter. **β = I_C/I_B** factors:
  **β = γ·α_T** where **emitter injection efficiency γ ≈ 1/(1 + (D_p N_B W_B)/(D_n N_E L_E))** and
  **base transport factor α_T ≈ 1 − W_B²/(2L_n²)**. **★ This is why β wants thin base (W_B↓), lightly-
  doped base, heavily-doped emitter (N_E≫N_B)** — derived, not asserted (Stage-1 said "thin & lightly
  doped"; here's the formula behind M23).

## 2. Ebers-Moll & Gummel-Poon (all four regions, one model)
- **Ebers-Moll:** two coupled diodes + two current sources with reciprocity α_F I_F = α_R I_R. Gives
  I_C, I_E in *every* region (active, saturation, cutoff, reverse) from V_BE, V_BC — the unifying model
  the Stage-1 region table only tabulates. Saturation V_CE(sat) and the "I_C < βI_B" fact (M22) drop out.
- **Gummel-Poon** adds high-injection, base-width modulation, and series resistances — the SPICE model.
- **Gummel plot** (ln I_C, ln I_B vs V_BE): ideal region slope = 1/V_T; β = I_C/I_B read off; low-V_BE
  roll-off (recombination, η→2) and high-V_BE roll-off (high injection + R) visible — the diagnostic.

## 3. Early effect (base-width modulation), derived
- Raising V_CB widens the BC depletion region → **effective W_B shrinks** → I_C rises (since I_C ∝
  1/W_B). Extrapolated I_C–V_CE lines meet at **−V_A (Early voltage)**; **r_o = V_A/I_C**,
  V_A ≈ q N_B W_B/C_jc-ish (∝ base Gummel number). The BJT analogue of MOSFET channel-length
  modulation — unify them as "effective transit-region modulation."

## 4. High-current & breakdown limits (where simple β dies)
- **Kirk effect (base push-out):** at high I_C the mobile charge rivals the collector doping → the
  effective base widens into the collector → β and f_T **collapse** at high current. Upper bound on
  useful I_C.
- **Webster effect:** high-level injection in the base drops β at high current (before Kirk).
- **Breakdown:** **BV_CBO** (collector-base, avalanche) > **BV_CEO** (collector-emitter, open base)
  because avalanche-generated carriers get **β-multiplied**: BV_CEO ≈ BV_CBO/β^{1/n}. Sets the safe
  operating area (SOA), with thermal runaway (Stage-1) and second breakdown.

## 5. Charge-control & switching
- Stored base charge Q_B = I_C·τ_F (τ_F = forward transit time = W_B²/2D_n). Switching off requires
  removing Q_B (plus saturation excess charge if it was saturated) → **storage time**; this is why
  saturated BJT logic (TTL) is slow and why **Schottky-clamped** transistors (a Schottky from base to
  collector prevents deep saturation) switch faster. **f_T = 1/(2π τ_ec)**, τ_ec dominated by τ_F →
  **f_T ∝ D_n/W_B²** (thin base = fast), the BJT speed driver.

## 6. HBT and why SiGe (frontier)
- Emitter injection efficiency γ wants N_E ≫ N_B, but heavy N_E suffers **bandgap narrowing**
  (Stage-2/U1 §4) which *hurts* γ — a real ceiling on Si-BJT β. **Heterojunction BJT (HBT):** use a
  **wider-gap emitter** (or graded narrower-gap SiGe base) so the band offset boosts injection
  *independently* of doping → lets you dope the base heavily (low base resistance, high f_T) **and**
  keep high β. **SiGe HBTs** reach f_T/f_max in the hundreds of GHz — modern RF/mm-wave.

## 7. Cross-topic unification (the capstone)
- **BJT = the ideal 60 mV/dec switch** the MOSFET only approximates: both are diffusion/exponential
  (I_C=I_S e^{V_BE/V_T} ↔ subthreshold I_D∝e^{V_GS/nV_T}), but the BJT has n=1 exactly → it *is* the
  thermal-limit device (Stage-2/U4 §3). · **g_m=I_C/V_T (BJT) vs 2I_D/V_OV (MOS):** the BJT's higher
  g_m-per-current is the exponential paying off — the deep reason BJTs win for high-g_m analog/bandgap
  references, MOSFETs for high-Z_in/low-power/digital. · The BJT base reuses the **short-diode**
  solution (Stage-2/U2 §2) — one piece of physics, two devices. · **BiCMOS** combines both.

## 8. Harder problem classes
- Derive I_S, γ, α_T, β from the base profile + Gummel numbers (explain M23 quantitatively). ·
  Ebers-Moll in saturation → V_CE(sat). · Early voltage from base-width modulation; r_o. · BV_CEO vs
  BV_CBO with β-multiplication. · f_T from transit time; effect of Kirk effect. · "Why SiGe HBT?"
  (bandgap-narrowing vs heterojunction argument). · BJT-vs-MOSFET g_m/I and subthreshold-slope unification.

## Open / to-verify (Stage 2)
- `[opened 2026-06-24]` BV_CEO≈BV_CBO/β^{1/n} exponent n (3–6, avalanche-dependent) is empirical —
  teach the β-multiplication mechanism; flag the exponent `uncertain`.
