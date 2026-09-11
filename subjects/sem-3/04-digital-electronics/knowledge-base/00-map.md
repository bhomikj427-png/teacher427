# ECE2102 Digital Electronics — 00 MAP (Stage 1, MUJ level)

> Big ideas, prerequisite graph, threshold concepts, scope, and the standing to-verify register.
> Built to `../../../../subject-research-protocol.md`. Scope = the official unit list in
> `../course-info.md` (syllabus text is `settled` — verbatim from the MUJ PDF). Tier-1 truth =
> A. Anand Kumar *Fundamentals of Digital Circuits* 2e + R.P. Jain *Modern Digital Electronics* 4e
> + Brown & Vranesic *Fundamentals of Digital Logic* 3e; logic-family numbers triangulated against
> manufacturer datasheets (TI/Fairchild 7400) (`sources.md`).

## The handful of big ideas (the expert's organizing schema)

1. **Two worlds of logic, and the line between them is *memory*.** A **combinational** circuit's
   output depends *only* on the present inputs — pure functions of the inputs, no history. A
   **sequential** circuit's output depends on inputs **and on stored state** — it remembers. The
   single deepest organizing split of the whole subject: *is there feedback that stores state, or
   not?* Adders, MUXes, decoders, ALUs = combinational. Latches, flip-flops, counters, registers,
   FSMs = sequential. Everything in the course is one or the other (or a partition of the two).
2. **Boolean algebra is the substrate; minimization is the craft.** Every combinational function is
   a Boolean expression; the *same* function has infinitely many circuit realizations. The engineer's
   job is to find a **minimal** one (fewest gates/literals) — by algebra, Karnaugh map, or
   Quine–McCluskey. SOP/POS canonical forms, minterms/maxterms, don't-cares, and K-map grouping are
   *the* recurring tool, reused in every combinational unit.
3. **NAND and NOR are functionally complete — the gate you build everything from.** {AND, OR, NOT}
   spans all logic, but a *single* gate type — NAND **or** NOR — alone is universal. This is *why*
   the 7400 NAND is the canonical building block and why logic families are characterized on their
   NAND/NOR gate. Universality + minimization is the bridge from algebra to silicon.
4. **A flip-flop is one bit of memory; clocking is how we tame feedback.** Cross-coupled gates
   (a latch) create bistable storage but are *level-sensitive* and race-prone. The master–slave /
   edge-triggered flip-flop makes storage update **once per clock edge** — turning unruly feedback
   into a disciplined, synchronous state element. **Synchronous design** (one clock, all FFs update
   together) is the entire discipline that makes large sequential systems analyzable.
5. **Any sequential machine is a finite-state machine: state register + next-state logic + output
   logic.** The FSM is the universal model — Moore (output = f(state)) vs Mealy (output =
   f(state,input)). Counters, shift registers, sequence detectors, controllers are *all* FSMs. Design
   = state diagram → state table → reduce → assign codes → derive FF excitation + output equations
   (combinational!). This is where combinational and sequential logic *fuse*.
6. **Timing is a first-class constraint, not an afterthought.** Real gates have **propagation
   delay**; real flip-flops have **setup/hold** windows. Maximum clock frequency, hazards/glitches,
   metastability, and clock skew all come from finite delay. The jump from "logically correct" to
   "works in hardware" *is* timing analysis — and it's what separates digital design from Boolean
   algebra on paper.
7. **Logic families are the physics tax on the abstraction.** The clean 0/1 abstraction is paid for
   by real transistors: TTL, ECL, CMOS each trade **speed vs power vs noise margin vs density**
   differently. Voltage thresholds (V_OH/V_OL/V_IH/V_IL), **noise margin**, **fan-out**, propagation
   delay, and power–delay product are the universal yardsticks. CMOS won (≈zero static power,
   scalable) — which is *why* it's the basis of all modern memory and PLDs.

## Prerequisite graph (load-bearing — triangulated, `settled`)

```
        Number systems + binary codes (BCD, gray, 2's-complement, ASCII)
                              │
              BOOLEAN ALGEBRA (axioms, theorems, De Morgan)
              + gates + functional completeness (NAND/NOR universal)
                              │
              MINIMIZATION (SOP/POS, minterms, K-map, Q–McCluskey, don't-cares)
                              │
        ┌──────────────────────┴───────────────────────┐
        ▼                                                ▼
  U1 COMBINATIONAL DESIGN                         (feeds everything below — the
  (adders, subtractors, serial/                    combinational "glue" inside every
   parallel/BCD adders)                            sequential block is built the same way)
        │
        ▼
  U2 MSI COMBINATIONAL BLOCKS
  (comparator, MUX/DEMUX, encoder/decoder,
   display driver, barrel shifter, ALU)
        │   [MUX/decoder also = function generators → loop back to minimization]
        ▼
  ─────────── the memory line: add feedback + a clock ───────────
        │
        ▼
  U3 SEQUENTIAL ELEMENTS
  (latch → FF: SR,D,JK,T,master-slave,edge-trig;
   counters ripple/synchronous; shift registers; timing)
        │
        ▼
  U4 STATE MACHINES
  (FSM Moore/Mealy; synchronous FSM design; state
   reduction; ASM charts; PRBS/pulse-train/clock gen; async)
        │
        ▼  [all of the above assume an ideal gate/FF — now pay the physics]
  U5 LOGIC FAMILIES & MEMORIES
  (TTL/ECL/CMOS: NM, t_pd, fan-out; tristate; interfacing;
   RAM/ROM; PLDs — PROM/PLA/PAL → implement the logic above)
```

Topological teaching order = the official unit order: **U1 combinational → U2 MSI → U3 sequential
→ U4 FSM/ASM → U5 families+memory.** The two hardest, most load-bearing edges: (a) **minimization →
combinational design** (every block rests on K-map fluency), and (b) **combinational → sequential**
(the "add feedback + a clock = memory" jump, big idea 4). FSMs (U4) presuppose *both* flip-flops
(U3) **and** combinational minimization (U1) — next-state/output logic is combinational, so U4
cannot precede a solid U1+U3. U5 sits orthogonally underneath: it's the device-physics floor under
the whole stack, deliberately last so the logic is abstract until the abstraction is paid for.

> Cross-link: U5 (logic families, CMOS) and the existing **`../../../electronic-devices-1`** /
> **`../../../verilog`** subjects share substrate — MOSFET physics underlies CMOS; Verilog is the
> HDL modelling of exactly these combinational/sequential blocks. Re-use, don't re-derive.

## Threshold concepts (budget extra teaching here — where learners stall)

- **★ Combinational vs sequential — the *memory* boundary.** Novices treat all circuits alike. The
  threshold is grasping that **feedback storing state** is what makes output depend on history, and
  that this single property reorganizes the whole subject. Everything keys off this.
- **★ Functional completeness / NAND-NOR universality.** That one gate type builds *all* logic is
  non-obvious and is the conceptual hinge between "algebra of 0/1" and "a chip you can actually
  fabricate from one repeated cell." Students who memorize De Morgan but can't *use* it to convert
  AOI→NAND-only stall here.
- **★ The K-map as adjacency = Boolean adjacency.** The map *works* because physically adjacent
  cells differ in exactly one variable (gray-code ordering), so grouping = applying XY+XY'=X.
  Students who treat it as a magic grid (not as visual algebra) can't handle 5-var maps, don't-cares,
  or POS grouping.
- **★ Edge-triggering and the master–slave mechanism.** *Why* a plain latch races and *how*
  master–slave / edge-triggering fixes it (capture on one edge, hold otherwise) is the gateway to
  all reliable sequential design. The level-vs-edge distinction is where most FF confusion lives.
- **★ The FSM synthesis pipeline.** Seeing that "design a sequence detector" decomposes into a fixed
  procedure — state diagram → state table → state reduction → state assignment → excitation table →
  K-map the FF inputs + outputs — is *the* threshold of U4. It fuses everything prior; students who
  never see it as a pipeline flail.
- **★ Setup/hold and f_max — timing as the real constraint.** That a *logically correct* circuit can
  *fail in hardware* because of finite propagation delay (setup violation, hazard glitch,
  metastability) is the threshold from paper logic to engineering. f_max = 1/(t_pd,FF + t_comb +
  t_setup) is the load-bearing formula students must internalize.

## Scope (Stage 1 = the official units; cover all, don't exceed)

U1 Combinational logic design (Boolean algebra & K-map overview; half/full adders; subtractors;
serial & parallel adders; BCD adder) · U2 MSI devices (comparators; MUX; encoder; decoder; driver &
multiplexed display; barrel shifter; ALU) · U3 Sequential logic design (latch; FFs — SR, D, JK, T,
master-slave JK, edge-triggered; ripple & synchronous counters; shift registers; timing analysis) ·
U4 State machines (FSM; synchronous FSM design; state reduction; timing issues; ASM; synchronous
circuits — pulse-train gen, PRBS gen, clock generation; asynchronous circuits) · U5 Logic families &
semiconductor memories (TTL NAND — specs, noise margin, t_pd, fan-in/fan-out; tristate TTL; ECL;
CMOS families & interfacing; memory elements; PLDs; logic implementation with PLDs).
Per-unit notes: `01`–`05`. Number systems / codes are an assumed prereq (folded into U1's opening,
not a separate exam unit). Exact MUJ unit/MTE-ETE boundaries pending the handout + PYQs (`exam-map.md`).

## Open questions / to-verify register

- `[opened 2026-06-27]` **Exact MUJ unit boundaries + MTE/ETE split** — `course-info.md` syllabus
  text is verbatim/`settled`, but the partition into examined units and what falls in MTE vs ETE is
  unknown without the official handout/PYQs. *Resolve by:* dropping papers into `../exam-pack/` and
  rebuilding `exam-map.md`. Until then exam-targeting is `uncertain`, research is syllabus-driven.
- `[opened 2026-06-27]` **No PYQ/PPT ingested** — `exam-map.md` is a provisional stub; topic
  weightage is inferred from standard course emphasis + the textbook, not from MUJ evidence.
- `[opened 2026-06-27]` **Which prescribed textbook MUJ examines from.** course-info lists 4. A.
  Anand Kumar + R.P. Jain are the standard Indian-UG anchors (problem style matches MUJ); Brown &
  Vranesic is the rigorous structural/FSM reference and the Verilog bridge. Treating Anand Kumar +
  Jain as tier-1 for Stage 1, Brown & Vranesic + Wakerly (Stage 2) for derivation rigor. Confirm via
  handout. Gothmann (text #3) not yet sourced.
- `[RESOLVED 2026-06-27]` **Logic-family numeric specifics** — standard-TTL DC table (V_OH 2.4 /
  V_OL 0.4 / V_IH 2.0 / V_IL 0.8; I_OH 400µA / I_OL 16mA / I_IH 40µA / I_IL 1.6mA → **fan-out 10,
  NM_H=NM_L=0.4 V**) **verified + triangulated** (4 independent sources; see `sources.md`/U5) →
  `settled`. *Remaining `uncertain`:* per-series numbers (74LS/HC/etc.) and exact ECL swing — read
  the specific datasheet; teach standard-TTL table as the anchor + the series caveat.
- `[opened 2026-06-27]` **Paired lab ECE2131** (`../../09-digital-electronics-lab`) — FF/counter/MUX
  experiments will re-scope emphasis once its KB/experiment list exists.
- `[RESOLVED 2026-06-27, Stage 2]` **State-assignment cost (was M14)** — resolved: assignment is an
  NP-hard embedding/cost+hazard problem (one-hot vs binary vs adjacent), sourced to De Micheli §9 /
  Brown & Vranesic. See `stage-2/04` §B. Misconception M14 promoted `uncertain → settled`.
- `[opened 2026-06-27, Stage 2 to-verify]` **A few deep specifics single-/standard-sourced** (kept
  `likely`/`uncertain`, mechanism solid): short-circuit power ≈10% of dynamic (→ Rabaey/Veendrick);
  DRAM charge-sharing ΔV = V_sig·C_cell/(C_cell+C_bit) exact form (→ Rabaey); essential-hazard minimal-
  delay cure exact condition (→ Unger); 74181 exact function-table rows (→ datasheet). *Resolve by:*
  reaching the named primary. Mechanisms are `settled`; only the precise constants/rows are open.
- `[2026-06-27 — CONFIRMATION/CROSS-CHECK PASS vs NPTEL(IIT-Kgp) + MIT 6.004/6.111]` Audited coverage.
  **All MUJ verbatim syllabus items confirmed covered.** Cross-check surfaced + RESOLVED:
  - **Filled (in MUJ scope):** "clock generation" was under-read as frequency-division → added the
    **clock-generation hardware** (astable/monostable/bistable multivibrators, 555 f=1.44/((R₁+2R₂)C)
    & T=1.1RC, ring osc f=1/(2N·t_pd), crystal osc, Schmitt trigger) to U4 §5; misconceptions M20/M21.
  - **Filled (Stage-2 depth):** CMOS pull-up/pull-down dual-network gate construction (`stage-2/05`
    §A½); error-control coding parity→Hamming SEC/SEC-DED, 2ʳ≥m+r+1, (7,4) (`stage-2/01` §C½, flagged
    beyond-MUJ); code converters (Gray/excess-3) made explicit in U1 §4½.
  - **DELIBERATELY OUT OF SCOPE (logged, not gaps — live in other subjects):** **ADC/DAC data
    converters** → `../../07-linear-integrated-circuits`; **8085/microprocessor** → separate course;
    **pipelining/computer arithmetic incl. Booth multiplier** → COA (Booth mechanism noted in
    `stage-2/01` as adjacent); **FPGA/HDL design flow** → `../../../verilog`. The base states its
    boundaries rather than silently omitting.
- `[opened 2026-06-27, evolving]` **Frontier claims are dated & `evolving`** (Dennard-scaling end ~2005,
  FinFET→GAA, emerging memory MRAM/ReRAM/PCM/FeFET) — recheck horizon on subject re-entry (§10 staleness
  trigger); teach as live frontier, not closed fact. Shared substrate with `../../../electronic-devices-1`
  stage-2.
