# ECE2101 — Misconceptions & predictable errors

> Feeds the engine's productive-failure & feedback moves (`teaching-manual.md`). Each is a *claim*
> (protocol §4): device-physics errors that are documented/structural are `settled`; ones marked
> `uncertain` are plausible-but-not-yet-sourced to education literature and must not be asserted as
> "the common error" on recall. Many are the negative image of the U1–U5 threshold concepts
> (`00-map.md`).

## Semiconductor physics (U1)
- **M1 `settled` — "current is only drift (carriers pushed by the field)."** Misses **diffusion**
  current (gradient-driven, no field). Diffusion *dominates the forward diode*. The single biggest
  U1 gap. Anchor: J = drift + diffusion, both carriers.
- **M2 `settled` — "a hole is a real positive particle."** A hole is the *absence* of a bonding
  electron; it moves because neighboring electrons hop. Useful as a +q quasi-particle, not a thing.
- **M3 `settled` — "doping adds charge / makes the material charged."** Doped semiconductor stays
  **electrically neutral** (dopant ion charge balances the carrier it donates). Doping changes
  *carrier population*, not net charge.
- **M4 `settled` — "n·p = nᵢ² only for intrinsic material."** It holds at **equilibrium for any
  doping.** Students apply n=p (intrinsic) to doped material. (Equilibrium-only: fails under bias —
  then quasi-Fermi levels split.)
- **M5 `settled` — "majority carriers determine everything."** Device behavior (diode, BJT) is
  often governed by **minority** carriers (injection, lifetime, diffusion length). Easy to ignore.
- **M6 `settled` — "raising temperature always raises conductivity in semiconductors."** True for
  *intrinsic/lightly doped* (carriers ↑ wins); in *heavily doped* extrinsic material, mobility ↓
  with T can make σ fall over a range. Sign depends on regime. *(Promoted 2026-06-24: grounded in
  the μ(T,N) regimes — phonon μ∝T^{−3/2} vs the carrier-population rise — `stage-2/01` §6; Neamen/Sze.)*

## PN junction & diodes (U2)
- **M7 `settled` — "you can measure V_bi with a voltmeter."** No — contact potentials at the probes
  cancel it exactly; V_bi does no net work around a loop. The ★ junction threshold error.
- **M8 `settled` — "a forward diode is just a 0.7 V battery (it generates voltage)."** 0.7 V is a
  *drop* across a conducting diode, not a source; with no external drive it produces nothing.
- **M9 `settled` — "the depletion region is where the carriers are."** Opposite — it's *depleted*
  of mobile carriers (only fixed ionized dopant cores remain); conduction happens in the neutral
  regions / channel.
- **M10 `settled` — "Zener and avalanche breakdown are the same thing."** Different mechanisms
  (tunneling vs impact ionization), opposite temperature coefficients, different doping/V_BR ranges.
  "Zener diode" is a generic *name* for breakdown-reference diodes regardless of mechanism.
- **M11 `settled` — "breakdown destroys the diode."** Not if current is limited — breakdown is
  reversible and is the *operating* mode of a Zener regulator. Destruction is from excess *power*.
- **M12 `settled` — "diode reverse current is exactly zero."** A small reverse current flows,
  strongly temperature-dependent (**≈ doubles every ~10 °C** in Si — measured/generation-dominated;
  ∝nᵢ² ideal I_S would be ~5 °C — verified 2026-06-24). Plus breakdown at large reverse V.
- **M13 `settled` — "the diode equation's I_S is a fixed constant."** It depends on geometry,
  doping, and *strongly* on temperature; treating it as constant across T gives wrong numbers.
  *(Promoted 2026-06-24: I_S = qnᵢ²(D_p/L_pN_D + D_n/L_nN_A) derived in `stage-2/02` §2 → ∝ nᵢ², the
  exponential T-dependence is structural, not incidental.)*

## JFET / MOSFET (U3, U4)
- **M14 `settled` — "at pinch-off the channel closes and I_D drops to zero."** No — past pinch-off
  I_D **saturates** (stays roughly constant); the pinched region is where carriers are swept across,
  not where current stops. The ★ FET threshold confusion.
- **M15 `settled` — "gate current flows in a FET."** ~Zero DC gate current (reverse-biased junction
  in JFET; insulating oxide in MOSFET) — that's the whole point (high Z_in). (Tiny leakage only.)
- **M16 `settled` — "use the saturation square-law everywhere."** Must **first test the region**
  (cutoff vs triode vs saturation). Using the saturation formula in triode (or vice versa) is the
  #1 MOSFET numerical error.
- **M17 `settled` — "enhancement and depletion MOSFETs are the same / JFET = MOSFET."** JFET is
  depletion-mode only (normally on); enhancement MOSFET is normally off. JFET gate = junction;
  MOSFET gate = oxide-insulated.
- **M18 `settled` — "a good MOSFET switch operates in saturation."** A *closed* switch operates in
  **triode** (low V_DS, low drop); saturation is the *amplifying* region. (Confusingly, BJT
  "saturation" *is* the on-switch — opposite naming, see M21.)
- **M19 `settled` — "MOSFET threshold V_t is a fixed device constant."** It shifts with the
  **body effect** (source-body bias) and with temperature; ignoring V_SB gives wrong V_t. *(Promoted
  2026-06-24: V_t = V_t0 + γ(√(2φ_F+V_SB) − √(2φ_F)) derived from MOS electrostatics in `stage-2/04`
  §1; Taur-Ning/Sze.)*

## BJT (U5)
- **M20 `settled` — "the BJT is voltage-controlled like a FET."** It's **current-controlled**
  (I_C=βI_B), drawing real base current; this is the defining BJT/FET split.
- **M21 `settled` — confusing BJT 'saturation' with FET/JFET 'saturation'.** **BJT saturation = ON
  switch** (both junctions forward, V_CE≈0.2 V). **FET saturation = active/amplifying** region.
  Same word, opposite role — a guaranteed cross-unit trap.
- **M22 `settled` — "I_C = βI_B always."** Only in the **active** region. In saturation the
  collector can't supply βI_B, so I_C < βI_B. Region first, then the relation.
- **M23 `settled` — "a thicker/heavily-doped base gives more gain."** Opposite — β is high
  *because* the base is **thin and lightly doped** (less recombination, high transport factor).
- **M24 `settled` — "β is a fixed number for a transistor type."** β varies widely part-to-part,
  with I_C, and with temperature; robust designs (divider+R_E bias) are made **β-independent** on
  purpose. *(Promoted 2026-06-24: β=γ·α_T with γ,α_T from doping/base-width + the Webster/Kirk
  high-current roll-off, `stage-2/05` §1,§4; Gray-Meyer/Sze.)*

## Cross-cutting
- **M25 `settled` — conflating large-signal (DC Q-point) with small-signal (AC gain).** Two analyses
  of the same circuit; e.g. computing g_m at zero bias, or applying small-signal models without
  first finding the Q-point. The ★ analog threshold (`00-map.md`).
