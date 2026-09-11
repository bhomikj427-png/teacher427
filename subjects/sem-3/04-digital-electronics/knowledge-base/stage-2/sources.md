# ECE2102 Digital Electronics — Stage-2 sources (primary / graduate)

> Stage 2 climbs the tier ladder to primary (`../../../../subject-research-protocol.md` §2; two-stage-
> depth.md). These are the graduate/primary references for the deep-structure material. Stage-1's
> `../sources.md` stays clean (exam set). Load-bearing derivations verified vs external sources **this
> session** are tagged ✓VERIFIED below; canonical-but-recalled structural claims are cited to the
> standard reference and marked `settled (standard)` only where triangulated, else `likely`.

## Primary / foundational (Tier 1)
- **Weste & Harris — *CMOS VLSI Design* (4e).** Spine for U5 Stage 2: CMOS VTC, switching threshold,
  noise margin from the VTC, dynamic/short-circuit/leakage power, delay (RC/logical effort), SRAM/DRAM.
- **Rabaey, Chandrakasan & Nikolić — *Digital Integrated Circuits* (2e).** Co-spine for U5: power
  (CV²f derivation), SRAM static noise margin (butterfly), DRAM sense amps, scaling.
- **Razavi — *Design of Analog CMOS IC* / *Fundamentals of Microelectronics*.** TTL/ECL/CMOS
  transistor-level, current-steering (ECL), metastability dynamics.
- **Brown & Vranesic — *Fundamentals of Digital Logic with Verilog Design* (3e).** Prescribed #4;
  Stage-2 spine for U1–U4 rigor: Shannon expansion, FSM synthesis/minimization, hazards. → `../../../verilog`.
- **Wakerly — *Digital Design: Principles and Practices* (4e/5e).** Rigorous on hazards, async,
  metastability, PLD internals.
- **Unger — *Asynchronous Sequential Switching Circuits* (1969).** Primary for U4 async: fundamental
  mode, essential hazards, race-free assignment.
- **Golomb — *Shift Register Sequences* (rev. ed. 2017).** Primary for U4 LFSR/m-sequence algebra,
  the three randomness postulates. ✓VERIFIED (postulates) this session.
- **De Micheli — *Synthesis and Optimization of Digital Circuits* (1994).** Logic synthesis: 2-level
  (Q–McCluskey/ESPRESSO) + multilevel, state minimization/encoding complexity.
- **Hennessy & Patterson / Weste-Harris — parallel-prefix adders.** Kogge-Stone, Brent-Kung.
- **Mano & Ciletti — *Digital Design*.** Cross-reference for canonical derivations.

## Verified this session (✓ — external source reached, triangulated)
- **CMOS switching threshold** V_M = [r(V_DD−|V_Tp|)+V_Tn]/(1+r), r=√(k_p/k_n)=√(μ_pW_p/μ_nW_n);
  condition I_DSn=I_DSp with both in saturation. — Tufts COMP103 L05, Weste-Harris-derived notes,
  testbook worked problem. `settled`. <http://www.cs.tufts.edu/comp/103/notes/Lecture05(StaticInverterLayout).pdf>
- **Metastability MTBF** = e^(t_r/τ)/(T_W·f_c·f_d); τ = resolution time-constant (~20–50 ps modern
  CMOS), T_W = metastability window. — NXP AN219 "A Metastability Primer", Trilobyte (Golson, SNUG14),
  ecrionix CDC. `settled`. <https://www.nxp.com/docs/en/application-note/AN219.pdf>,
  <https://trilobyte.com/pdf/golson_snug14.pdf>
- **Parallel-prefix adders:** Kogge-Stone O(log₂n) depth (fastest, more area, lower fan-out);
  Brent-Kung depth = 2log₂n−2 (less area, ~half the wiring, higher depth); both built on the
  associative (g,p) prefix operator. — Wikipedia Kogge-Stone, Concordia COEN6501 notes (Vitoroulis
  2006), arXiv 2503.18070. `settled`. <https://en.wikipedia.org/wiki/Kogge%E2%80%93Stone_adder>
- **SRAM static noise margin:** butterfly curve (overlaid VTCs of the two cross-coupled inverters);
  SNM = side of the largest square fitting in the smaller lobe; read-SNM < hold-SNM (access
  transistors degrade the curve). — academia/ResearchGate SNM analyses, SBMicro 2019. `settled`.
- **m-sequence Golomb postulates:** R1 balance (#1−#0 = 1 over a period: 2^(n−1) ones, 2^(n−1)−1
  zeros), R2 run distribution (½ length-1, ¼ length-2, …), R3 two-level (ideal) autocorrelation
  (peak N=2ⁿ−1, off-peak −1). — IIT-G (Pinaki) Golomb notes, Springer "Golomb's Randomness
  Postulates", Mustansiriyah notes. `settled`. <https://www.iitg.ac.in/pinaki/Golomb.pdf>

## Added in the confirmation/cross-check pass (2026-06-27)
- **Hamming code SEC bound 2ʳ ≥ m+r+1; (7,4) code** — ✓VERIFIED/triangulated: angms.science ITC
  "Hamming (7,4)" notes, Hamming's original paper (arXiv 1401.5919 rewrite), worked examples. `settled`.
  Added to `stage-2/01` §C½ (flagged beyond-MUJ-scope enrichment).
- **CMOS PUN/PDN dual-network gate construction; NAND-preferred-over-NOR (series-PMOS slow)** — cited
  Weste-Harris / MIT 6.004 "gates from MOS". `settled (standard)`. Added to `stage-2/05` §A½.
- **Booth multiplication** — flagged adjacent (→ COA), mechanism noted in `stage-2/01`. `likely`.

## Open Stage-2 to-verify (→ `../00-map.md` register)
- DRAM charge-sharing sense-amp ΔV = V_signal·C_cell/(C_cell+C_bit) exact form — cite Rabaey before `settled`.
- Short-circuit power fraction (~10% of dynamic at balanced edges) — `likely`, source to Rabaey/Veendrick.
- Essential-hazard minimal-delay cure (Unger) — `likely`, confirm exact condition.
- Logical-effort delay model constants if used — cite Weste-Harris.
