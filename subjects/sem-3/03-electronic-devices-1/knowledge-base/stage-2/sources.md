# ECE2101 — STAGE 2 sources (primary / graduate)

> Stage-2 sources climb to **primary/graduate** (protocol §2 tier-1 for depth). Triangulate any
> load-bearing specific across ≥2 independent tier-1 sources. Kept separate from the Stage-1
> `../sources.md` so the exam set stays clean.

## Tier 1 — Primary / graduate texts
- **Sze & Ng, *Physics of Semiconductor Devices*, 3e (Wiley 2006).** The depth anchor: junction
  electrostatics, Shockley derivation, breakdown (impact ionization/tunneling), Schottky/thermionic
  emission, MOS physics. `settled`.
- **Taur & Ning, *Fundamentals of Modern VLSI Devices*, 2e.** MOSFET scaling, short-channel effects,
  subthreshold, DIBL, FinFET. `settled`.
- **Razavi, *Design of Analog CMOS ICs* / *Microelectronics*.** Small-signal depth, g_m/I_D, f_T.
- **Gray, Hurst, Lewis & Meyer, *Analysis & Design of Analog ICs*, 5e (2015).** BJT/MOS device models
  for IC design, Ebers-Moll/Gummel-Poon, mismatch.
- **Streetman & Banerjee 7e; Neamen 4e.** Bridge texts — derivations at UG-honors→grad level.
- **Pierret, *Semiconductor Device Fundamentals*.** Clean derivations (continuity, diffusion eqn).

## Tier 1 — Graduate courseware
- **MIT OCW 6.012 / 6.720 (Integrated Microelectronic Devices).** Derivations + problem sets.
- **NPTEL advanced semiconductor-device courses** — ingest via `tools/fetch_transcripts.py`
  (ASR caveat: verify every formula/constant vs text). *Not yet pulled.*

## Verified THIS SESSION (2026-06-24)
- **Si effective density of states:** N_C ≈ 2.8×10¹⁹ cm⁻³; **N_V ≈ 1.0–1.8×10¹⁹** (source-dependent
  via m_p*). Sources: eesemi.com Si/Ge/GaAs-at-300K table; HTElabs Si constants; Green 1990
  (ResearchGate). → grounds the Stage-2/U1 §1 explanation of *why nᵢ is textbook-dependent* (the
  Stage-1 `contested` flag): m* + E_g convention, not error.
- **Subthreshold-swing thermal limit:** S = ln10·kT/q = 2.303×25.85 mV = **59.5 mV/decade @300 K**
  (the "60 mV/dec" floor) — verified by computation from the verified V_T; standard (Taur-Ning, Sze).
  Grounds Stage-2/U4 §3 and the BJT-unification (Stage-2/U5 §7).

## Confidence notes
- Derivations (Shockley diode, MOS V_t/γ, square law, base profile→β, Early effect, subthreshold
  swing) are `settled` graduate-canonical.
- Process/empirical constants (E_crit≈3×10⁵ V/cm, ionization coefficients, ZTC offset, BV_CEO
  exponent, θ mobility-degradation, N_V exact) are fits with literature spread → flagged `uncertain`
  in the unit files; mechanisms taught, numbers not pinned (protocol §4/§9).

## Used to source the previously-`uncertain` misconceptions (M6, M13, M19, M24)
- M6 (σ vs T regime-dependence), M13 (I_S(T) ∝ nᵢ², not constant), M19 (V_t body/T dependence), M24
  (β spread with I_C/T/part) — all now grounded in the Stage-2 mechanisms above + Sze/Neamen/Taur-Ning;
  promoted toward `settled` in `../misconceptions.md` (see CHANGELOG 2026-06-24 Stage-2 entry).
