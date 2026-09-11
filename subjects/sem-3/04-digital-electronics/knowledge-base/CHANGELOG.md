# ECE2102 Digital Electronics — CHANGELOG (correction audit trail)

> Per `../../../../subject-research-protocol.md` §10. One entry per correction:
> `[YYYY-MM-DD] <claim/topic> — <what changed> — <why> — <trigger> — <confidence: old → new>`.
> Never silently overwrite — every change is logged here.

- `[2026-09-11]` **exam-map.md REBUILT from real MUJ evidence** (replaces the 2026-06-27
  inferred stub). First exam material arrived and was triaged into `../exam-pack/`: professor's
  8-deck slide set, **MTE past paper 25-Sep-2025** (ECE2102, 30 marks/90 min), 10-question practice
  set. Changes: (1) **MTE structure now `settled`** — Sec A 3x2 "Memory Based", Sec B 4x4 "Concept
  Based", Sec C 1x8 "Analytical Based"; (2) **MTE/ETE split resolved `uncertain`→`likely`** — the
  old provisional guess "MTE ≈ U1–U2 (+start of U3)" was close but understated U3: the 2025 MTE
  reached **synchronous counter design** (8-mark Sec C); U4 and U5 wholly absent, independently
  corroborated by the decks stopping at flip-flops; (3) **11 question patterns P1–P11** extracted
  and cited per item — dominant framing is *constrained realization* (NOR/NAND-only, single 8:1 MUX,
  undersized 4:1 MUX, decoder+gate), not bare minimization; don't-cares in nearly every K-map item;
  (4) per-unit weights re-rated; teaching order re-sequenced by scoring value. **No truth claim
  changed** — slides/PYQ set scope and framing only (honesty rule). New open item: **course-code
  mismatch** (decks `ECE 2105` vs paper/KB `ECE2102`, identical syllabus text) and a **missing-deck
  gap** for counters/registers/FSM/logic-families/memories. — *trigger: inbox triage, learner
  supplied material* — confidence: exam-targeting `uncertain` → `likely` (MTE) / still `uncertain`
  (ETE, no paper).
- `[2026-06-27]` **Confirmation / completeness cross-check (vs NPTEL IIT-Kgp + MIT 6.004/6.111).**
  Audited the base against external syllabi. **MUJ verbatim scope confirmed fully covered.** Caught +
  fixed a real scoping gap and added depth: (1) **U4 "clock generation"** was under-interpreted as
  frequency-division → added clock-generation **hardware** (multivibrators, 555 f=1.44/((R₁+2R₂)C) &
  T=1.1RC, ring osc f=1/(2N·t_pd), crystal, Schmitt trigger; +M20/M21) — all verified this session;
  (2) `stage-2/05` **CMOS PUN/PDN dual-network gate construction** (Weste-Harris/MIT); (3) `stage-2/01`
  **error-control coding** parity→Hamming (2ʳ≥m+r+1, (7,4); verified) + **code converters** (Gray/
  excess-3) in U1 §4½ + Booth note. **Logged out-of-scope boundaries** (ADC/DAC→LIC, 8085→sep course,
  pipelining/Booth→COA, FPGA→verilog) so omissions are explicit, not silent. — *trigger: learner
  "confirmation check, cross-check MIT/IIT"* — confidence: added items `settled` (verified) / Booth
  `likely`; no prior claim demoted. Audit: `00-map` register + `sources.md`/`stage-2/sources.md`.
- `[2026-06-27]` **Stage 2 COMPLETE → stage-2✓ (TEACH-READY).** Built `stage-2/01`–`05` + `stage-2/
  sources.md` (depth-first, learner: "dig deep, important to ECE"). Added per unit: first-principles
  derivations, model limits / "where the UG textbook lies," cross-topic unification, frontier, harder
  problem classes. **Load-bearing deep formulas verified + triangulated against external/primary
  sources this session** (§1): CMOS switching threshold V_M=[r(V_DD−|V_Tp|)+V_Tn]/(1+r), r=√(k_p/k_n)
  (Tufts/Weste-Harris); metastability MTBF=e^{t_r/τ}/(T_W·f_c·f_d) (NXP AN219/Trilobyte); parallel-
  prefix adders Kogge-Stone O(log₂n)/Brent-Kung 2log₂n−2 (Wikipedia/Concordia); SRAM static noise
  margin = largest square in butterfly lobes, read<hold (SNM literature); m-sequence Golomb postulates
  R1–R3 (IIT-G/Golomb/Springer); 2's-complement subtraction from ℤ/2ⁿℤ. **Promoted M14 `uncertain→
  settled`** (state-assignment = NP-hard embedding, De Micheli). §0 surplus exit test PASSED on all 5
  units (expert/"why-not-what"/edge-case Qs answered from mechanism). — *trigger: depth-first build to
  teaching gate* — confidence: load-bearing items `settled`; short-circuit-%/DRAM-ΔV/essential-hazard-
  delay/74181-rows `likely`/`uncertain` (mechanisms settled, exact constants open); frontier `evolving`.
- `[2026-06-27]` **Stage 1 COMPLETE → stage-1✓.** Built all 5 unit files (U1 combinational, U2 MSI,
  U3 sequential, U4 FSM/ASM, U5 logic families+memories), each with mechanism-level notes, verified
  load-bearing forms, worked-problem patterns, and a passed exit test. Load-bearing specifics
  verified + triangulated against external sources *this session* (recall ≠ sourced, §1): full-
  subtractor borrow Bout=A′B+Bin(A⊕B)′; BCD-adder +6 correction Y=Cout+S₃S₂+S₃S₁; 4-bit comparator
  (A>B)/(A=B) equations with x_i=XNOR; JK characteristic eqn Q⁺=JQ′+K′Q + all four excitation tables;
  LFSR maximal length 2ⁿ−1 (primitive poly) + all-zeros lockout; **standard-TTL DC table → fan-out 10,
  NM=0.4 V (4 independent sources)**; PROM/PLA/PAL array structure. — *trigger: subject activation,
  depth-first build* — confidence: load-bearing items `settled`; per-series TTL/exam-targeting `uncertain`.
- `[2026-06-27]` **Knowledge base created — map pass.** Learner activated Digital Electronics for
  research/teaching. Built `00-map.md` (6 big ideas, prereq graph + threshold concepts triangulated
  `settled` vs Cambridge CST notes + standard texts), `sources.md`, `misconceptions.md` (M1–M19
  seed), `exam-map.md` (uncertain stub — no PYQ). Status stage-0 → stage-1 (in progress). No
  corrections yet (nothing prior to correct). — *trigger: subject activation* — confidence: n/a.
