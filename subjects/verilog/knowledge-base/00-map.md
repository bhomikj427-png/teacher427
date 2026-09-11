# Verilog — Knowledge Base Map (Layer 2)

> Built per `../../../subject-research-protocol.md`. Map pass (big ideas, prerequisite graph,
> threshold concepts, scope, source canon) **plus the full exhaustive deep pass** — at the
> learner's request (2026-06-15) the §8 "build the entire base upfront" option was taken, so
> per-unit deep notes `01`–`12` exist for the whole curriculum, not just the next unit. Confidence-
> marked throughout: `settled` / `contested` / `uncertain` / `suspect`. Sources tiered in `sources.md`.
>
> **Date built:** 2026-06-15. Verilog is a *moving-but-mature* field (the language is frozen at
> IEEE 1364-2005, merged into SystemVerilog IEEE 1800); tool/synthesis practice evolves, so
> synthesis-specific claims carry a recheck horizon (§10 of the protocol).
>
> **Stage status: `stage-2✓-equivalent` (provisional — stamped 2026-07-05, engine audit).** This
> base predates the two-stage vocabulary; its map + exhaustive deep pass (units 01–12, backlog
> cleared) is the same complete-base standard the gate requires. *Provisional because* no formal
> §0 surplus exit test (expert-level "why not what" probes answered from mechanism) is on record —
> run one and upgrade this line. **Exception inside the stamp:** the 3 job-framing scope-extension
> items in §6 (design-flow framing, processor capstone, FPGA toolflow) are `stage-0` — queued, not
> built — and are **not teachable** until researched to standard.

---

## 0. Scope & goal calibration

- **Learner goal:** professional RTL design (end state), currently *developing* (has written
  combinational Verilog — half adder, full adder). So the base is built **deep** (toward
  synthesis, timing, verification) but teaching climbs gradually. `[settled — stated by learner]`
- **Career re-frame (2026-06-29):** the goal is explicitly an **internship/job edge in VLSI/digital
  design**, and **Verilog is step #1 of a track** (next: SystemVerilog → Design-vs-Verification fork
  → UVM/scripting/flow — full plan in `../../_career-roadmap/roadmap.md`). This does not change the
  *truth* in this base; it changes *emphasis* — scoring-over-depth here means leading with the
  hire-able skills (a synthesizable end-to-end design + a small-processor capstone + RTL coding
  discipline + testbench literacy). `[settled — stated by learner]`
- **Syllabus anchor (2026-06-29):** scope/sequence anchored to **IIT Kharagpur NPTEL *Hardware
  Modeling using Verilog*** (Sengupta, 8-week layout) + **UC Berkeley EECS151** (FPGA/ASIC flow,
  industrial tools, RISC-V capstone); textbook truth-authority remains **Harris & Harris**. The
  existing units 01–12 already cover the anchors' scope; the *additions* the job framing surfaces
  (full design-flow framing, a synthesizable processor capstone, hands-on FPGA toolflow) are logged
  as **scope-extension items** in §6 — to be researched to `stage-2✓` *before* they are taught, so
  the teaching gate stays honest. `[settled]`
- **What "Verilog" is:** a **Hardware Description Language (HDL)** — a formal, human- and
  machine-readable notation for modeling digital electronic systems, used across design,
  simulation, synthesis, and verification. Standardized as **IEEE 1364** (1995 → 2001 → 2005);
  in 2009 merged into SystemVerilog, **IEEE 1800**. `[settled — IEEE SA; Wikipedia corroborates]`
- It is **not** a software programming language, despite C-like syntax. This is the master
  reframe (see Big Idea #1 / Threshold T1). `[settled — IEEE scope; Cummings; near-universal]`

---

## 1. The big ideas (the deep structure — what an expert reasons *from*)

Everything in the subject hangs off these. If a lesson can't be traced to one, it's drifting.

1. **Verilog describes hardware that exists and runs concurrently — it does not "execute" like a
   program.** Code maps to physical structure (gates, wires, registers) operating in parallel,
   continuously. Sequential, line-by-line behavior exists **only inside a procedural block**, and
   even there it's a modeling convenience, not a CPU running your lines. `[settled]`
2. **Concurrency is the default.** Every continuous assignment (`assign`), every gate primitive,
   every `always`/`initial` block runs **in parallel**, all the time. The simulator interleaves
   them via an event queue; real hardware just *is* all of them at once. `[settled]`
3. **Two consumers of the same code: the simulator vs. the synthesizer.** The simulator runs the
   *full* language (event-driven). The synthesizer maps only a **synthesizable subset** to real
   gates/flip-flops. Most beginner pain = confusing the two (e.g. `#delay`, `initial`, `x`/`z`
   behave differently or are ignored in synthesis). The synthesizable subset is a **discipline**.
   `[settled — IEEE; Doulos/Cummings on sim/synth mismatch]`
4. **The RTL model: state in registers, transformed by combinational logic, advanced by a clock.**
   Register-Transfer Level = "data flows register → (combinational cloud) → register, each clock
   edge." Almost everything synthesizable reduces to **combinational logic feeding flip-flops**.
   This is the mental model professional design runs on. `[settled — Doulos RTL; Harris & Harris]`
5. **Time is events; assignment scheduling is the mechanism.** Simulation advances through a
   **stratified event queue**. Blocking (`=`) updates immediately within a block; nonblocking
   (`<=`) evaluates all right-hand sides first, then updates all left-hand sides at end of the
   time step — which is exactly how a bank of flip-flops behaves on a clock edge. Getting this
   wrong causes races and sim/synth mismatch. `[settled — event-region terminology verified at deep
   pass via Accellera/IEEE 1364 §5 extract; see 06-blocking-nonblocking-scheduling.md]`
6. **One circuit, many description styles (abstraction levels).** Same hardware can be written
   **structural/gate-level** (instantiate gates, wire them), **dataflow** (`assign` + operators),
   or **behavioral** (`always` blocks, `if`/`case`). Experts pick the right level; the synthesizer
   collapses them all to gates. `[settled — multiple secondary sources; standard taxonomy]`

---

## 2. Prerequisite graph (the spine of `curriculum.md`)

`→` = "must precede." Triangulated for the load-bearing edges (protocol §8). The learner sits
around node **(C)** (built combinational adders); the big unclimbed thresholds are **(F)–(H)**.

```
(A) Digital-logic foundations  ──→ (B) Module & data-type basics ──→ (C) Combinational modeling
   binary, gates, boolean,          module/ports/instantiation,        structural (gates) +
   comb. vs seq., flip-flops,       wire vs reg, 4-state values         dataflow (assign, ops)
   clock — [PREREQ, mostly held]    (0/1/x/z), vectors/buses             [LEARNER IS HERE]
                                                                              │
        ┌─────────────────────────────────────────────────────────────────┘
        ▼
(D) Behavioral combinational ──→ (E) Behavioral sequential ──→ (F) ★Blocking vs nonblocking
   always @*, if/case,             always @(posedge clk),          + event scheduling
   blocking (=), latch-avoidance   flip-flops, reset, the          [THRESHOLD T2]
   [THRESHOLD T3: latches]         "reg ≠ register" trap
                                   [THRESHOLD T4]
        │
        ▼
(G) Finite state machines ──→ (H) RTL discipline & synthesis ──→ (I) Verification / testbenches
   state encoding, Moore/Mealy,    synthesizable subset, sim/        stimulus, self-checking,
   the 2-/3-block FSM idiom        synth mismatch [THRESHOLD T3]      $display/$monitor, waveforms
        │                                                                   │
        ▼                                                                   ▼
(J) Scaling: parameters, generate, hierarchy ──→ (K) Timing: setup/hold, clocking, CDC [PROF]
        │
        ▼
(L) SystemVerilog migration, assertions, UVM [PROFESSIONAL — far horizon]
```

**Note on (A):** the learner has *demonstrated* combinational logic (adders) but their grasp of
the foundations (esp. sequential/clocking, flip-flops) is **not yet diagnosed** — flagged for the
first teaching session. Adders are purely combinational, so building them proves nothing about (E).

---

## 3. Threshold concepts (budget extra teaching; learners predictably stall here)

These are the "once you get it, everything reorganizes" ideas — and the documented stall points.

- **T1 — It's hardware, concurrent, not a running program.** The master threshold. Everything in
  §1 #1–#2. Misreading Verilog as sequential software is the root of most downstream errors.
  `[settled — universal in the literature]`
- **T2 — Blocking (`=`) vs nonblocking (`<=`) and the event queue.** "One of the most
  misunderstood constructs in the language" even among experienced designers (Cummings). Owns the
  single most consequential coding decision a beginner makes. `[settled — Cummings SNUG]`
- **T3 — Synthesizable subset & sim/synth mismatch (incl. unintended latch inference).** Code that
  simulates fine but synthesizes to wrong/extra hardware (a latch from an incomplete `if`/`case`;
  `x` meaning "unknown" in sim but "don't-care" in synthesis). `[settled — Doulos; latch-inference
  sources; Cummings RTL-mismatch paper]`
- **T4 — `reg` is not a register; `wire` vs `reg` is about *assignment context*, not hardware.**
  `reg` only means "a variable assignable inside a procedural block"; it may synthesize to a wire,
  not a flip-flop. The keyword name actively misleads beginners. `[settled — corroborated; SV
  later renames toward `logic` partly for this reason]`
- **T5 — The RTL mindset.** Thinking natively in "registers + combinational clouds per clock
  cycle" rather than in statements. The reorganization that turns syntax knowledge into design
  ability. `[settled — Doulos RTL; standard practice]`

---

## 4. Known misconceptions

Maintained in `misconceptions.md` (sourced + confidence-marked per protocol §4). Summary pointers:
treating modules as functions that "return," reg=flip-flop, blocking in clocked logic, nonblocking
in combinational logic, incomplete sensitivity lists, forgetting that `assign` is continuous/always
live, expecting top-to-bottom execution across blocks.

---

## 5. Settled vs. contested vs. evolving

- **Settled & stable:** the core language (frozen at IEEE 1364-2005), the blocking/nonblocking
  guidelines, the RTL model, the abstraction taxonomy.
- **Evolving (recheck on re-entry):** synthesis-tool behavior and the *practical* synthesizable
  subset (vendor-specific: Vivado/Quartus/Yosys differ at the edges); the SystemVerilog-vs-Verilog
  question (industry has largely moved to SystemVerilog for new RTL — relevant to a *professional*
  goal, decide when we approach node L). `[uncertain — needs a dedicated check at the deep pass]`
- **Style-contested (teach as judgment, not law):** FSM 1- vs 2- vs 3-always-block style; reset
  strategy (sync vs async). Teach the tradeoffs, not one as "correct." `[contested — by design]`

---

## 6. Open questions / to-verify register  *(protocol §9/§10 format)*

> **Status: backlog cleared on the exhaustive deep pass (2026-06-15).** Per-unit deep notes
> `01`–`12` written for the whole curriculum. Resolved items recorded below + in `CHANGELOG.md`.

**Resolved**
- [resolved 2026-06-15] Event-region terminology/ordering (active / inactive / NBA / monitor) —
  sourced to the Accellera extract of IEEE 1364 §5 scheduling + chipverify corroboration; `uncertain
  → settled`. See `06-blocking-nonblocking-scheduling.md`.
- [resolved 2026-06-15] Verilog vs SystemVerilog strategic decision — researched (Pong Chu;
  industry commentary). Recommendation: Verilog fundamentals first (U1–U9) → migrate to SV at
  U10/U12; **needs learner sign-off before Phase IV**. See `12-systemverilog-migration.md`.
- [resolved 2026-06-15] 4-state `x`/`z` synthesis treatment (was M9 `uncertain`) — verified;
  `uncertain → settled`. See `02-modules-and-datatypes.md` §C.
- [resolved 2026-06-15] Cummings 8 guidelines — corroborated via the IEEE-1364-derived scheduling
  mechanism (not the paper alone); `settled`.

**Still open (genuinely cannot be closed without the noted action — not deferred busywork)**
- [open 2026-06-15] Learner's actual grasp of sequential-logic foundations (flip-flops, clocking)
  and whether they've crossed threshold T1 — **only resolvable by the learner**, via retrieval in
  session 1. Not a research gap.
- [open 2026-06-15] Minor: full *verbatim* IEEE 1364-2005 §5 text not read (PDF/paywall);
  terminology triangulated across two independent descriptions — sufficient to teach. Standing
  niceties only: obtain clean copies of the **Cummings paper body** and **IEEE §5** if ever paywall
  access appears. Does **not** block teaching.
- [open — recheck-on-re-entry] Industry SV-vs-Verilog default status and synthesis-tool specifics
  are in a *moving* field (§2 dating) — re-confirm on subject re-entry, not now.

**Scope-extension items (opened 2026-06-29 by the career re-frame — research to `stage-2✓` BEFORE teaching each)**
- [open 2026-06-29] **Full digital design flow framing** (spec → RTL → simulation → synthesis →
  place-and-route → STA → GDSII/bitstream; FPGA vs ASIC paths). Partly implicit in U10/U11; needs a
  consolidated, sourced unit because "knows the flow" is an interview staple. Anchor: NPTEL Week 1 +
  EECS151. → candidate **U0/U10+ extension**.
- [open 2026-06-29] **Synthesizable processor capstone** (a small CPU / RISC-V subset in Verilog —
  datapath + control FSM + memory, with a self-checking testbench). The single highest-leverage
  *portfolio* artifact for an internship. Anchor: NPTEL Week 8 (processor design) + EECS151 RISC-V.
  → candidate **U13 capstone**; depends on U1–U8.
- [open 2026-06-29] **Hands-on FPGA toolflow** (e.g. Vivado/Quartus or open Yosys+nextpnr; simulate
  with Icarus/Verilator; deploy to a board or sim). Turns paper-RTL into demonstrable work. Anchor:
  EECS151 FPGA lab. → cross-cutting, introduced alongside U8 verification.
- *These are intentionally NOT yet built. The existing units 01–12 remain `stage-2✓` for their
  scope and are teach-ready now; the extensions are queued, not blocking.*
