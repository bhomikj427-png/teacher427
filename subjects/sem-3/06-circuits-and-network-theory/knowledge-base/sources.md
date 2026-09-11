# ECE2120 Circuits & Network Theory — Sources (Stage 1)

> Every source tiered (`subject-research-protocol.md §2`), dated, with confidence. Stage-2 primary/
> graduate sources are tracked separately in `stage-2/sources.md`. **The researcher is a model:**
> content recalled from training is `uncertain` until checked against an external source this session
> (§1). Load-bearing exact claims verified 2026-06-22 are noted against the relevant tier-1 source.

## Tier 1 — Primary / foundational (the prescribed textbooks = ground truth for content)

- **Van Valkenburg, *Network Analysis* (3e), PHI.** *The* anchor for **network functions (U4)** and
  **synthesis (U5)** — driving-point/transfer functions, poles/zeros, Hurwitz, positive-real
  functions, Foster & Cauer realization. The official primary text for the synthesis half.
- **Sudhakar & Shyammohan, *Circuits and Networks* (5e), TMH, 2017.** Anchor for **theorems (U1)**,
  **transients (U2)**, **two-ports (U3)** — Indian-curriculum aligned, matches MUJ scope.
- **Hayt, Kemmerly & Durbin, *Engineering Circuit Analysis* (8e), McGraw-Hill, 2012.** Anchor for
  theorems, first/second-order transients, Laplace circuit analysis; clean mechanism statements.
- **Ashfaq Husain, *Networks and Systems* (2e), Khanna** and **Salivahanan & Pravin Kumar, *Circuit
  Theory*, Vikas.** Secondary prescribed texts; triangulation for the same content.

*(All five are listed as official prescribed texts in `../course-info.md`. They are the truth ground;
the web sources below were used this session to **verify exact load-bearing claims** against, since
the researcher's own recall is not a source — §1.)*

## Web sources used THIS SESSION to verify load-bearing exact claims (2026-06-22)

- **Positive-real function** — Wikipedia "Positive-real function"; Electrical4U "Network Synthesis |
  Hurwitz Polynomial | Positive Real Functions"; LBRCE NT-II Unit-V notes. *Verified:* PR conditions
  (Re Z(s)≥0 for Re s≥0; no RHP poles/zeros; jω-axis poles simple with real positive residues; N and
  D Hurwitz; degree difference ≤ 1). Triangulated, `settled`.
- **RC / RL driving-point properties** — eeeguide "RC Driving Point Impedance function | Properties"
  and "RL Driving Point Impedance | Properties"; testbook RC pole-zero-pattern items. *Verified:*
  neg-real-axis simple alternating poles/zeros; RC nearest-origin = pole / farthest = zero, no zero at
  origin, Z_RC(0)>Z_RC(∞), residues positive; RL nearest-origin = zero, no pole at origin,
  Z_RL(0)<Z_RL(∞), positive slope. Triangulated, `settled`.
- **Foster's reactance theorem (LC)** — Wikipedia "Foster's reactance theorem" (cites Foster 1924,
  *Bell System Technical Journal*). *Verified:* jω-axis simple alternating poles/zeros; Foster I =
  series-connected parallel-LC tanks, Foster II = parallel series-LC. `settled`.
- **Cauer forms** — Sanfoundry "Cauer Methods in Network Synthesis"; testbook Cauer items. *Verified:*
  Cauer I = continued fraction about ∞ → series-L/shunt-C ladder (low-pass); Cauer II = about origin →
  series-C/shunt-L ladder (high-pass). `settled`.
- **Maximum power transfer (AC)** — Wikipedia "Maximum power transfer theorem"; LibreTexts 12.5;
  GeeksforGeeks. *Verified:* Z_L = Z_th* conjugate match; efficiency 50 % at the match; constrained
  optima (|Z_L|=|Z_th|, or R_L=√(R_th²+X_th²)). `settled`.
- **Two-port reciprocity/symmetry** — RF-Wireless-World "Two-Port Network Parameters"; Wikipedia
  "Two-port network"; testbook symmetry item. *Verified:* reciprocity Z₁₂=Z₂₁, Y₁₂=Y₂₁, h₁₂=−h₂₁,
  AD−BC=1; symmetry Z₁₁=Z₂₂, A=D. `settled`.

## Tier 3 — Derivative (orientation / leads only)
- eeeguide, testbook, Sanfoundry, Electrical4U: Indian-exam study sites. Used **only** to triangulate
  exact statements that also appear in the tier-1 texts — never as the sole authority for a fact.
  (Cross-checked against Van Valkenburg's known treatment; consistent.)

## Confidence summary
- U1 theorems, U2 transients: `settled` (canonical, triangulated text + web).
- U3 two-ports (conversions, reciprocity/symmetry, interconnection): `settled`; image-parameter filter
  detail `settled` at exam depth.
- U4 network functions (poles/zeros, Hurwitz, PR): `settled` (verified this session).
- U5 synthesis (LC/RC/RL properties, Foster/Cauer): `settled` (verified this session).
- Misconceptions M8, M10: `uncertain` (see `misconceptions.md` to-verify).
- Exam weighting / MUJ unit boundaries: `uncertain` (no PYQ/PPT/handout — `00-map.md` register).
