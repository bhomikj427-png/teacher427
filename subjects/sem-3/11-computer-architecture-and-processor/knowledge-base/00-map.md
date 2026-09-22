# ECE2108 Computer Architecture & Processor — 00 MAP (Stage 1, MUJ level)

> Big ideas, the learning-flow map, prerequisite graph, threshold concepts, scope, and the standing
> to-verify register. Built to `../../../../subject-research-protocol.md`.
>
> **Scope is unusually well-evidenced for this batch:** it comes from the professor's own
> **course hand-out** (36-lecture plan, `../exam-pack/HANDOUT-ECE2108-course-handout.pdf`) plus
> three of his unit decks — not from an inferred syllabus. Unit boundaries are `settled`.
>
> **Truth authority is split three ways** (see `sources.md`):
> units 1–6 → **Mano, *Computer System Architecture* 3e**; unit 7 → **Bhurchandi & Ray, *Advanced
> Microprocessors and Peripheral Devices* 3e**; unit 8 → **Patterson & Hennessy, *COD RISC-V
> Edition*** + the **official ratified RISC-V spec**.

---

## The handful of big ideas (the expert's organizing schema)

1. **Architecture is the contract; organization is the implementation.** *Architecture* = what the
   machine does as seen by a programmer — the **instruction set**, registers, data types,
   addressing modes (the deck: "Architecture describes what the computer does… also called
   instruction set architecture"). *Organization* = how that contract is met — buses, adders,
   control logic, timing (the deck: "frequently called micro architecture"). One architecture admits
   many organizations. **The whole course is one walk down this ladder** — ISA at the top (units 1,
   7, 8), microarchitecture in the middle (units 1–3), performance engineering underneath (units
   4–6).
2. **Everything a computer does decomposes into timed register transfers.** A machine instruction is
   *not* an atom: it is a **sequence of microoperations** — elementary operations on data held in
   registers — clocked out one time-step at a time. **RTL** (register transfer language) is the
   notation; `R2 ← R1` plus a control function `P:` is the whole vocabulary. This is the generative
   idea behind units 1–3: if you can write the RTL, you can build the hardware, because each RTL
   statement *is* a wiring instruction (which register drives the bus, which load line is asserted,
   at which clock edge).
3. **A bus exists because full interconnection costs O(n²).** Connecting n registers pairwise needs
   **n(n−1)** lines (the deck states this explicitly). One shared, time-multiplexed path plus a
   select code collapses that to O(n) — the Basic Computer's 16-bit common bus with select lines
   S₂S₁S₀ picking one of 7 registers or memory. **Trading parallelism for wire count by sharing in
   time** is the recurring hardware economy of the course, and it reappears as the von Neumann
   bottleneck (unit 4) and as the single-ported-memory structural hazard (unit 4).
4. **The control unit is a sequencer that turns an opcode into a timed pattern of control signals.**
   Every control signal is a **sum of D·T products** — D from the decoded opcode, T from the
   sequence counter. Two ways to build it, and the contrast is the deepest either/or in the course:
   **hardwired** (combinational logic + sequence counter — fast, cheap, rigid, hard to change) vs
   **microprogrammed** (a control memory holding microinstructions, a CAR, and a sequencer —
   slower, but the instruction set becomes *programmable firmware*). RISC machines mostly went back
   to hardwired; that is not an accident (unit 3 ↔ unit 8).
5. **Concurrency buys throughput, and usually costs latency.** Pipelining, parallel functional
   units, caching and vector processing all raise **work per unit time**; they do not make any one
   instruction finish sooner (the deck: architects increase throughput "often at the expense of
   slight increases in individual task latency"). A k-stage pipeline's speedup is **bounded above by
   k** — and hazards (structural, data, control) are precisely the mechanisms that stop you reaching
   it.
6. **The memory hierarchy is a bet on locality, and it only pays because programs are repetitive.**
   Fast memory is small and expensive; large memory is slow. The hierarchy wins **only** because of
   **locality of reference** — temporal (a recently used item will be used again soon) and spatial
   (its neighbours will be used soon). Cache mapping, replacement policy, associative memory and
   virtual memory are all answers to two questions: *where may this block live?* and *how do I find
   it without a linear search?*
7. **I/O is a synchronization problem before it is a data problem.** CPU and peripherals differ in
   speed, signal type, data format and autonomy. Everything in unit 5 is a rung on one ladder of
   **increasing device autonomy / decreasing CPU involvement**: strobe → handshake → polled flags →
   interrupts → DMA → I/O processor. Each rung buys CPU time by moving intelligence outward.
8. **A real instruction set embodies a philosophy, and the course ends by putting two side by
   side.** **CISC (8086):** variable-length instructions (1–6 bytes), memory operands, few
   special-purpose registers, segmented address space, microcoded. **RISC (RISC-V):** fixed 32-bit
   instructions, load/store-only memory access, 32 general registers, no condition codes, designed
   for a pipeline. Units 7 and 8 are the same question asked twice — *what should an instruction
   be?*

---

## Learning-FLOW map — the ordered path (start here)

Sequence + dependencies + where you are. Follow it left to right; the MTE line is printed in the
professor's own lecture plan.

```
  ① FOUNDATIONS            ② THE MACHINE              ③ THE CONTROLLER
  arch vs org,       →     Mano's Basic         →     hardwired vs
  functional units,        Computer: registers,       microprogrammed,
  von Neumann/Harvard,     instruction set,           control memory,
  RISC vs CISC             instruction cycle          program control
  (L1–L2)                  (L9–L11)                   (L12–L15)
        │                        ▲
        ▼                        │
  ①b RTL & MICROOPS ─────────────┘
  register transfer, bus & memory
  transfers, arithmetic / logic /
  shift microops, ALSU
  (L3–L8)
        │
        ▼
  ④ CONCURRENCY  ═════ ⟨ MID-TERM EXAM ends here — handout prints the divider after L19 ⟩
  parallel processing, Flynn,
  pipelining, instruction pipeline,
  pipeline hazards
  (L16–L19)
        │
        ▼
  ⑤ I/O ORGANIZATION  →  ⑥ MEMORY ORGANIZATION  →  ⑦ THE 8086  →  ⑧ RISC-V
  peripherals, async        hierarchy, main/aux,        architecture,   the open ISA,
  transfer, modes of        associative memory,         addressing      RV32I, formats,
  transfer, DMA             cache, virtual memory       modes, ALP      features
  (L20–L22)                 (L23–L26)                   (L27–L34)       (L35–L36)
```

**You are here: nothing taught yet.** Teaching has not begun for this subject — the live position is
`../progress-log.md` (created on teaching activation), never this file.

**Why this order and not the syllabus paragraph's order:** the hand-out's lecture plan already *is*
the dependency order. It differs from the one-paragraph syllabus text in §F (which lists "Control
unit design, Microprogrammed Control" before "Parallel Processing" but reads as a topic dump, not a
sequence). Follow the **lecture plan**; it is the instructor's real sequencing and it matches the
prerequisite graph below.

### Sub-map ①/①b — Foundations + RTL (unit 01)

```
arch vs organization ──┬─→ functional units (input, memory, ALU, output, control)
                       ├─→ von Neumann (one memory, one bus → the bottleneck)
                       │      └─→ Harvard (split instruction/data memory + bus)
                       └─→ RISC vs CISC (the ISA-philosophy axis; reopened in U7/U8)
                                │
RTL: R2←R1, control function P: ─┴─→ bus & memory transfers (S₂S₁S₀ select, DR←M, M←DR)
                                     └─→ microoperations: arithmetic · logic · shift
                                           └─→ Arithmetic Logic Shift Unit (one stage, MUX-selected)
```

### Sub-map ② — The Basic Computer (unit 02)

```
instruction codes (I | opcode | address) ─→ 8 BC registers (AR PC DR AC IR TR INPR OUTR)
      │                                          └─→ common bus (7 sources + memory)
      ▼
25 instructions = 7 memory-reference + 12 register-reference + 6 input-output
      │
      ▼
timing & control (3×8 opcode decoder, 4-bit SC → 4×16 decoder = T₀…T₁₅)
      │
      ▼
instruction cycle: fetch → decode → (indirect) → execute ─→ interrupt cycle (R flip-flop)
      │
      ▼
DESIGN: scan every RTL statement that changes a register → its LD/INR/CLR equation
        (control of registers, flags, bus) → design of accumulator logic
```

### Sub-map ③ — The controller (unit 03)

```
hardwired control ←─── the same job ───→ microprogrammed control
(comb. logic + SC)                        (control memory + CAR + sequencer)
                                               │
                          address sequencing ──┼─→ incrementer (in-line)
                                               ├─→ conditional branch (CD field + status bits)
                                               ├─→ mapping (opcode → routine address)
                                               └─→ subroutine call / return (SBR)
                                                      │
                                    microinstruction format: F1 F2 F3 CD BR AD
                                                      │
                          program control: status bits, conditional branch, subroutines, stack
```

### Sub-map ④ — Concurrency (unit 04)

```
throughput vs latency ─→ Flynn: SISD | SIMD | MISD | MIMD
                              │          └─ array / systolic / associative processors
                              │      MIMD ─→ shared-memory multiprocessor
                              │              | message-passing multicomputer
                              ▼
pipelining: decompose + a register per segment ─→ speedup S = n·tₙ / ((k+n−1)·tₚ) → max k
      ├─→ arithmetic pipeline (FP add: compare exponents → align → add → normalize)
      └─→ instruction pipeline (FI · DA · FO · EX)
                 └─→ HAZARDS: structural | data | control → cures (interlock, forwarding,
                     delayed load, prefetch, BTB, loop buffer, prediction, delayed branch)
```

Distant areas ⑤–⑧ get their sub-maps when we reach them (learner rule: near-term areas only).

---

## Prerequisite graph (load-bearing — `settled` from the hand-out's lecture plan)

```
   Digital Electronics (ECE2105 / ECE2102) — ASSUMED PREREQ, NOT RE-TAUGHT
   registers · decoders · MUX · flip-flops · adders · tri-state buffers · counters
                          │
                          ▼
   U1a  architecture vs organization · functional units · von Neumann/Harvard · RISC/CISC
                          │
                          ▼
   U1b  REGISTER TRANSFER LANGUAGE  ← the notation everything after is written in
         bus & memory transfers → arithmetic → logic → shift microops → ALSU
                          │
                          ▼
   U2   BASIC COMPUTER: instruction codes → registers + bus → instruction set →
        timing & control → instruction cycle → MRI → I/O & interrupt →
        complete description → design of BC → design of accumulator logic
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
   U3  CONTROL UNIT DESIGN          U4  PARALLEL PROCESSING & PIPELINING
       hardwired vs microprogrammed      (needs only the instruction-cycle
       control memory · sequencing        phases from U2, not the BC design)
       program control
                          │        ══════ MTE BOUNDARY (after L19) ══════
                          ▼
   U5  INPUT-OUTPUT ORGANIZATION   ← extends U2's I/O + interrupt to real peripherals
       peripherals · async transfer · modes of transfer · DMA · IOP
                          │
                          ▼
   U6  MEMORY ORGANIZATION         ← extends U2's flat 4096×16 to a hierarchy
       hierarchy · main/auxiliary · associative memory · cache · virtual memory
                          │
                          ▼
   U7  8086 MICROPROCESSOR         ← a REAL CISC ISA; the first machine that isn't a toy
       architecture (BIU/EU) · segmentation · addressing modes · instruction set ·
       assembler directives · assembly language programming
                          │
                          ▼
   U8  RISC-V                      ← the deliberate contrast to U7
       the open ISA · RV32I · registers · instruction formats · features
```

**The three load-bearing edges** (get these wrong and everything downstream mis-sequences):

- **(a) RTL → everything.** U2 and U3 are *written in* RTL. A learner who reads `AR ← PC` as
  pseudocode rather than as "put PC on the bus (S₂S₁S₀=010) and assert LD(AR) during T₀" cannot do
  the design steps at all. RTL fluency is the gate.
- **(b) U2 → U3.** Microprogrammed control is only meaningful once you have seen a control unit
  *hardwired* for a specific machine; Mano builds the BC's hardwired controller in ch. 5 and only
  then re-implements control as firmware in ch. 7. Reversing this teaches the abstraction before the
  thing it abstracts.
- **(c) U6 presupposes U2's flat memory model.** Cache and virtual memory are *deviations* from
  "memory is one array you address directly" — you need the naive model first for the deviation to
  mean anything.

**U4 is deliberately out of the U2→U3 chain:** pipelining needs only the *phases* of the instruction
cycle, not the BC's design. That is why the professor can (and does) hand L16/L17 to an industry
practitioner and still place it before the MTE.

> Cross-links — reuse, don't re-derive: **`../../04-digital-electronics`** (registers, decoders, MUX,
> flip-flops, adders, ALU, tri-state — U1's arithmetic/logic/shift circuits and the ALSU are
> *literally* that subject's unit-02 content, and its deck 7 "Shifter_ALU" overlaps this course's
> L7–L8); **`../../../verilog`** (RTL as a *language* — the same register-transfer abstraction, and
> the natural place these datapaths get built); **`../../03-electronic-devices-1`** (the RAM/ROM and
> SRAM/DRAM substrate under U6).

---

## Threshold concepts (budget extra teaching here — where learners predictably stall)

- **★ RTL statements are hardware, not code.** The single biggest stall in this course. `R2 ← R1` is
  not an assignment executed by something; it is a *clock edge* at which a bus source is selected and
  a load line is high. Until this flips, every "design" question (design of BC, control of AC) looks
  like magic. **Diagnostic:** ask what two things must be true for `DR ← M[AR]` to happen — answer:
  S₂S₁S₀ = 111 (memory drives the bus) **and** LD(DR) = 1.
- **★ Control signals are sums of D·T products.** The derivation move — "scan *all* register-transfer
  statements that change register X, then OR their conditions to get LD(X)" — is the whole method of
  "Design of Basic Computer". Worked in U2: LD(AR) = R′T₀ + R′T₂ + D′₇IT₃, CLR(AR) = RT₀,
  INR(AR) = D₅T₄. A learner who can recite the instruction set but cannot perform this scan has
  memorized U2 and understood none of it.
- **★ The sequence counter is what makes a sequence.** That one opcode produces a *series* of actions
  because SC increments (T₀, T₁, T₂, …) and is **cleared** to end the instruction (`D₃T₄: SC ← 0`) is
  the mechanism of instruction execution. Most "how does the computer know what to do next"
  confusion resolves here.
- **★ Mano uses TWO different machines, and students fuse them.** The **Basic Computer** (ch. 5) is
  4096×16 with a **3-bit opcode** and 12-bit address. The **microprogram example** (ch. 7) is a
  *different, smaller* machine: 2048×16, a **4-bit opcode**, 11-bit address, 128×20 control memory.
  Fusing them produces nonsense (e.g. "mapping a 3-bit opcode to 0xxxx00"). **Flag this explicitly
  before U3** — see `misconceptions.md` M7, the highest-yield correction in the subject.
- **★ Pipeline speedup is bounded by k, and the bound is never reached.** The formula
  S = n·tₙ/((k+n−1)·tₚ) is easy; the threshold is *why* the ceiling is k (you can at best overlap k
  things) and why real pipelines fall short (unequal segment delays, the interface-register delay
  tᵣ, and hazards). A learner who only memorizes the formula cannot answer "would a 12-stage
  pipeline be 12× faster?" — the exam's favourite trap.
- **★ Segmented addressing: physical address = segment × 16 + offset.** The 8086 threshold, with two
  sub-shocks: (i) the segment register is *shifted left one hex digit*, not merely added — so
  segments begin every 16 bytes ("paragraphs"); (ii) **segments overlap** — many different
  seg:offset pairs name the *same* physical byte. Until this is concrete, no addressing-mode
  question is safe.
- **★ A cache tag is the part of the address you threw away.** Cache mapping is a function from
  address → slot. The index picks the slot; the **tag is exactly the bits the index discarded**, and
  it must be stored so you can tell *which* of the many blocks mapping to this slot is present.
  Learners who see tag/index as arbitrary field names cannot derive a bit-split for an unseen
  configuration — which is the only cache question worth asking.

---

## Scope (Stage 1 = the official hand-out; cover all of it, don't exceed)

Eight units, derived from the hand-out's 36-lecture plan (lecture numbers in brackets):

| # | Unit file | Lectures | CO | Exam |
|---|---|---|---|---|
| 01 | `01-architecture-fundamentals-and-rtl.md` | L1–L8 | CO1 | MTE + ETE |
| 02 | `02-basic-computer-organization-and-design.md` | L9–L11 (+ deck 2) | CO2 | MTE + ETE |
| 03 | `03-control-unit-and-microprogrammed-control.md` | L12–L15 | CO2 | MTE + ETE |
| 04 | `04-parallel-processing-and-pipelining.md` | L16–L19 | CO3 | **MTE + ETE** |
| 05 | `05-input-output-organization.md` | L20–L22 | CO3 | ETE only |
| 06 | `06-memory-organization.md` | L23–L26 | CO3 | ETE only |
| 07 | `07-8086-microprocessor.md` | L27–L34 | CO4, CO5 | ETE only |
| 08 | `08-risc-v.md` | L35–L36 | CO5 | ETE only |

**Assumed prerequisite, not in scope:** combinational and sequential digital logic (that is ECE2105 /
`../../04-digital-electronics`).

**Explicitly NOT in scope** — stated so the base declares its boundaries rather than silently
omitting: floating-point arithmetic *algorithms*, Booth multiplication and division hardware (Mano
ch. 10 — **not** in the hand-out), vector/array-processor detail beyond Flynn's classes,
multiprocessor cache coherence, the 8087/8259/8255 peripheral ICs, and RISC-V privileged
architecture or extensions beyond RV32I.

---

## Open questions / to-verify register

- `[opened 2026-09-12]` **Which scheme revision the learner is enrolled under — RESOLVED for this
  course, open for the batch.** ECE2108 is **absent** from the *2023-onwards* ECE curriculum PDF that
  seeded this batch (verified by text extraction: 67 course codes, no ECE2108) but **present in the
  MUJ *2025-2026 onwards* ECE scheme**, Third Semester, 3 credits. That scheme's Sem-3 is
  MASXXXX Probability & Statistics · Principles of Management/Engineering Economics · **ECE2104 Data
  Structures & Algorithms** · **ECE2105 Digital Electronics** · **ECE2106 Electronics Devices &
  Circuits** · **ECE2107 Circuits & Systems** · **ECE2108 Computer Architecture & Processor** + labs
  ECE2132 / ECE2133 / ECE2134 (24 credits). This explains **both** halves of the learner's report — a
  subject they have that the registry lacks, and registry subjects they don't have. *Resolve the
  batch-level reconciliation by:* learner confirming their registration list; then the sem-3 registry
  is re-mapped. **Not acted on unilaterally** — restructuring the batch touches subjects with built
  knowledge bases. Logged in `../../research-engine/research-queue.md`.
- `[opened 2026-09-12]` **Session year on the hand-out is internally inconsistent** — header
  "July-Dec 2027", filename "Jan 2027", deck footers machine-stamped **8/6/2026**. Taking Jul–Dec
  **2026** as the live session (`likely`). Does not affect content; affects only the exam calendar.
  *Resolve by:* learner confirming, or an MTE date-sheet.
- `[opened 2026-09-12]` **No PYQ for this subject — neither MTE nor ETE.** Exam *structure* is
  `settled` from the hand-out's marks table (MTE 30 / CWS 30 / ETE 40) and the MTE *scope boundary*
  is `settled` from the printed lecture-plan divider. But **question forms, per-topic weightage and
  the mark-per-question breakdown are `uncertain`** — inferred from the CO/Bloom levels and from the
  sibling ECE2102 Digital Electronics MTE pattern (3×2 / 4×4 / 1×8), which is a *different course and
  examiner*. `exam-map.md` marks exactly which rows are evidence and which are inference.
- `[opened 2026-09-12]` **Internal contradiction in the hand-out's lecture plan.** Lectures 29–32
  (8086 addressing modes 2, assembler, arithmetic/logic programming, loops & subroutines) are printed
  **after** the "Mid Term Examination" divider, yet their *Mode of assessing CO* column lists
  "Assignment, **MTE**, ETE". Positional divider vs boilerplate column. Taking the **divider** as
  authoritative (`likely`): 8086 is ETE material, consistent with CO4/CO5 being the last COs.
  *Resolve by:* asking the instructor, or one real MTE paper.
- `[opened 2026-09-12]` **No deck for L12–L15** (microprogrammed control, control memory, control
  unit design, program control) **or for any ETE unit** (I/O org, memory org, 8086, RISC-V). Those
  units are built **textbook + institutional/NPTEL-primary**, per protocol §2 ("when no instructor
  material exists for a unit, skip straight to the prescribed textbook + NPTEL"). Their *emphasis* is
  therefore less certain than U1/U2/U4's. Later decks probably exist — **ask the learner.**
- `[CLOSED 2026-09-23]` ~~**Could not obtain a clean full copy of Mano 3e this session.**~~ The one
  full-text copy located is served chunked and **truncates** — 8 download attempts gave 2.0–7.3 MB,
  never a complete file; an xref rebuild recovered 1262 of ~4759 objects, with the page tree lost
  inside object streams. **Consequence and mitigation:** Mano's chapters were verified against
  **multiple independent institutional reproductions that agree with each other and with the
  professor's decks** (triangulation table in `sources.md`). That is authoritative-secondary, not
  primary. Load-bearing numbers so verified are `settled`; anything resting on a single reproduction
  stays `likely`. ~~*Resolve by:* the learner supplying a Mano PDF, or a library copy.~~
  **RESOLVED `[2026-09-23]` — the book was obtained** from archive.org item
  `computer-system-architecture-morris-mano-third-edition` (OCR full text, complete; `sources.md`).
  Mano-derived claims may now be verified against the primary text directly. The end-of-chapter
  problems are transcribed into `../question-bank.md`. OCR damages subscripts and figure values, so
  the text is primary for *prose and problem statements* and still wants a figure check for *numbers*.
- `[opened 2026-09-12]` **8086 addressing-mode COUNT is convention-dependent — and CO4 is the
  highest-target CO (85%, L3).** Institutional sources give **12 modes in 5 groups** (register,
  immediate, direct, register indirect, based, indexed, based-index, string, direct I/O port,
  indirect I/O port, relative, implied); other textbooks compress to 7 or 8 by folding in the
  I/O-port and relative/implied modes. The *mechanisms* are `settled`; the *taxonomy* is a naming
  convention. **Teach the 12-in-5-groups scheme and say the count varies** — never assert "there are
  exactly N addressing modes" as fact. Same caveat for instruction-set grouping (7 vs 8 groups).
- `[opened 2026-09-12]` **8086 per-instruction clock counts and the full opcode map not verified.**
  Mnemonics and operation are `settled`; clock counts were not checked this session (one datum was:
  AAM = 83 clocks, single-sourced, `likely`). *Resolve by:* the Intel 8086 Family User's Manual.
- `[opened 2026-09-12, evolving]` **RISC-V is a live, versioned standard.** Verified against the
  **ratified** unprivileged ISA (v20240411 / v20260120 reference library). The extension set and
  ratification status move; recheck on subject re-entry (protocol §10 staleness trigger). Teach RV32I
  as stable — the spec itself commits to keeping the base constant — and the extension ecosystem as
  evolving.
- `[opened 2026-09-12]` **One source error already caught and quarantined** — an institutional 8086
  document states "SF is used with unsigned numbers". That is **wrong** (the sign flag copies the MSB
  and is meaningful under *signed* interpretation; the same document's own flag table says "Set equal
  to high-order bit of result"). Corrected in `07-8086-microprocessor.md`, logged in `CHANGELOG.md`,
  and kept as `misconceptions.md` M16 — evidence that these sources must be read against themselves.
- `[opened 2026-09-12]` **CWS (30 marks) composition is unspecified.** The hand-out says
  "(Quiz + Assignments) / (Research + Presentation)" with no weights or counts, so 30% of the grade
  is unplannable. *Resolve by:* learner reporting what the instructor actually set.
