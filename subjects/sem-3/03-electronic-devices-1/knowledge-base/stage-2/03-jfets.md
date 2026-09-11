# Unit 3 — JFETs — STAGE 2 (deep structure)

> On top of Stage-1 `../03-jfets.md`. Primary: Sze 3e, Neamen ch.12, Streetman ch.6.

## 1. Shockley's square law, derived (gradual-channel approximation)
- **GCA assumption:** the channel potential varies slowly along x, so at each x the *transverse*
  electrostatics are 1-D (the depletion-width formula applies locally with the local channel-to-gate
  reverse bias). Valid when channel length ≫ depletion width — fails in short channels.
- Local channel half-opening b(x) = a[1 − √((V_bi + V(x) − V_GS)/V_P0)] where a = metallurgical
  half-width and V_P0 = qN_D a²/(2ε_s) is the **pinch-off parameter** (full depletion of the channel).
- Drift current I_D = q N_D μ_n (channel area) dV/dx; integrate x from source (V=0) to drain (V=V_DS)
  → the full **Shockley I_D(V_GS, V_DS)** with a (…)^{3/2} form. Near saturation it **collapses to the
  square law I_D = I_DSS(1−V_GS/V_P)²** — so the square law is the *saturated* limit of a messier
  cubic-root expression, not exact everywhere.
- **Pinch-off** occurs where the channel opening → 0 at the drain: V_DS,sat = V_GS − V_P. Define
  **I_DSS = I_DSS(geometry, N_D, μ)** and **V_P** from V_P0 − V_bi.

## 2. Why I_D doesn't fall to zero past pinch-off
- The channel doesn't physically close — it reaches a minimum opening; the GCA breaks there
  (transverse field comparable to longitudinal). Carriers are **injected into a high-field pinched
  region and swept across** at saturation velocity. Current is set at the source end and is ~constant
  → saturation. Same physics as MOSFET pinch-off (Stage-2/U4).

## 3. Channel-length modulation & output resistance
- Beyond saturation, the pinch-off point moves slightly toward the source as V_DS rises → effective
  L shrinks → I_D creeps up: I_D = I_DSS(1−V_GS/V_P)²(1+λV_DS), r_d = 1/(λI_D). The JFET analogue of
  the BJT **Early effect**; both are "effective-length/width modulation."

## 4. Temperature behavior & the zero-tempco bias point
- Two competing T-effects: **μ ↓ with T** (I_D falls) vs **|V_P| ↓ / V_bi ↓ with T** (I_D rises). They
  cancel at a specific drain current — the **zero-temperature-coefficient (ZTC) point** (≈ where
  V_GS ≈ V_P + 0.63 V for Si JFETs). Designers bias there for thermal stability. *(value is a
  textbook approximation — `uncertain`, teach the existence of ZTC, not the exact offset.)*

## 5. Noise — why JFETs are low-noise
- No oxide → **no carrier trapping/detrapping at an oxide interface → very low 1/f (flicker) noise**
  vs MOSFETs. Thermal channel noise ≈ that of a resistor. This is why JFET front-ends dominate
  low-noise instrumentation, electrometers, and audio/precision input stages despite MOSFET
  ubiquity.

## 6. Relatives & unification
- **MESFET:** replace the p-n gate with a **Schottky** gate (Stage-2/U2 §5) on GaAs → high-speed
  microwave FETs. **HEMT/MODFET:** 2-D electron gas at a heterojunction → ultra-high mobility & f_T
  (mm-wave, RF). The JFET's "deplete a channel from the side" idea scales up to the entire
  III-V RF transistor family.
- **JFET vs MOSFET square law:** both ∝ V_OV² in saturation, but the JFET modulates a **doped bulk
  channel via junction depletion**, the MOSFET modulates an **induced inversion layer via oxide
  field**. Same algebra, different charge-control physics — a clarifying expert parallel.

## 7. Harder problem classes
- Derive V_P0 = qN_Da²/2ε_s from depletion of the channel; get I_DSS from geometry. · Full
  (non-saturated) I_D vs the square-law limit. · ZTC bias derivation (set dI_D/dT=0). · 1/f-noise
  argument for choosing a JFET over a MOSFET in a given front-end. · MESFET/HEMT qualitative
  scaling.

## Open / to-verify (Stage 2)
- `[opened 2026-06-24]` Exact ZTC offset (~0.63 V above V_P) is a Si-JFET textbook figure — teach
  the *mechanism*; flag the number `uncertain` pending a primary-source check.
