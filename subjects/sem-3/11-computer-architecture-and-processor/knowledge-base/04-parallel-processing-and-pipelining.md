# U4 — Parallel Processing & Pipelining (Stage 1)

**Lectures L16–L19 · CO3 · MTE + ETE · deck: `../exam-pack/slides-unit3-…pdf` (36 pp)**
**⚠ L16 and L17 are marked `*` — delivered by an industry practitioner.**

Scope (deck's contents): Parallel Processing · Pipelining · Instruction Pipeline · Pipeline Hazards.

Truth authority: **Mano 3e ch. 9**. Verified against an independent institutional reproduction that
agrees with the deck on every formula and worked number.

> **This is the last MTE unit** — the hand-out prints the Mid Term Examination divider immediately
> after L19. Numerical speedup problems are the natural exam form here (F14 in `exam-map.md`).

---

## 1. Throughput — the quantity being bought — `settled`

**Throughput** = the amount of processing accomplished in a given interval of time.

| Kind | Measured as |
|---|---|
| **Instruction throughput** | instructions per second, or via **CPI** (cycles per instruction) |
| **Data / memory throughput** | GB/s or MB/s — how fast data moves between storage, memory, cache |

**The four techniques architects use to raise it** (the deck's own list), with what each actually
does:

| Technique | Mechanism |
|---|---|
| **Pipelining** | break instructions into steps so several overlap in execution |
| **Parallelism** | add execution units / cores to run different tasks concurrently |
| **Caching** | keep hot data in small ultra-fast memory near the CPU (→ U6) |
| **Vector processing** | one instruction operates on a whole dataset (**SIMD**) |

**★ The framing sentence to keep:** architects raise throughput **"often at the expense of slight
increases in individual task latency."** Throughput ≠ latency. A pipelined instruction takes *more*
total time than an unpipelined one (it now has register delays between stages) — but the machine
finishes far more of them per second. Students who conflate the two cannot answer "does pipelining
make a program faster?" correctly. (`misconceptions.md` M12.)

## 2. Parallel processing — `settled`

**Definition:** "execution of concurrent events in the computing process to achieve faster
computational speed."

**Levels of parallelism** (coarse → fine): job/program level · task/procedure level ·
inter-instruction level · intra-instruction level.

**Applications** (worth one line for a descriptive answer): numerical weather forecasting,
computational aerodynamics, finite-element analysis, remote sensing, genetic engineering,
computer-assisted tomography, defence research.

**Cost:** the amount of hardware increases with parallel processing, and with it the cost. Parallelism
is never free.

## 3. Flynn's classification — `settled`

M. J. Flynn classified computers by the **multiplicity of instruction streams and data streams**.

- **Instruction stream** = the sequence of instructions read from memory.
- **Data stream** = the operations performed on the data in the processor.

|  | **Single Data** | **Multiple Data** |
|---|---|---|
| **Single Instruction** | **SISD** | **SIMD** |
| **Multiple Instruction** | **MISD** | **MIMD** |

**SISD** — one control unit, one processor unit, one memory. The standard von Neumann machine;
instructions execute sequentially. Parallelism, if any, comes from **multiple functional units or
pipelining** inside it.
*Limitation:* the **von Neumann bottleneck** — maximum speed is limited by **memory bandwidth**, and
memory is shared by CPU and I/O.
*Ways to improve a SISD machine:* multiprogramming · spooling · multifunction processor · pipelining ·
instruction-level parallelism (**superscalar**, **superpipelining**, **VLIW**).

**SIMD** — many processing elements under one control unit. **Only one copy of the program exists**;
a single controller broadcasts one instruction at a time and all active PEs execute it on **different
data**. Shared memory must be multi-module to feed them all.
*Three types:* **array processors** (ILLIAC IV, Connection Machine, DAP, MPP) · **systolic arrays**
(regular VLSI grids of very simple processors — CMU Warp, Purdue CHiP) · **associative processors**
(content addressing — STARAN, PEPE).

**MISD** — **"there is no computer at present that can be classified as MISD."** It is of theoretical
interest only. (Say this plainly in an exam; do not invent an example.)

**MIMD** — multiple processing units executing multiple instructions on multiple data. Two families:

| | **Shared-memory multiprocessor** | **Message-passing multicomputer** |
|---|---|---|
| Memory | all processors have equally direct access to **one large address space** | **each processor has its own memory** |
| Communication | through shared memory | by **passing messages** |
| Examples | bus/cache-based (Sequent Balance, Encore Multimax); multistage-network (Ultracomputer, Butterfly, RP3, HEP); crossbar (C.mmp, Alliant FX/8) | tree (Teradata, DADO); mesh (Rediflow, J-Machine); hypercube (Cosmic Cube, iPSC, NCUBE, FPS T-series, Mark III) |
| Limitations | **memory access latency**; the **hot-spot problem** | **communication overhead**; hard to program |

**★ The point Flynn's table hides, and the deck states:** **pipelining does not fit Flynn's
classification.** Flynn distinguishes by the *number* of streams; a pipeline has one of each but
overlaps them in time. This is a genuine limitation of the taxonomy and a good short-answer question.

## 4. Pipelining — the core idea — `settled`

**Definition:** "a technique of decomposing a sequential process into suboperations, with each
subprocess being executed in a special dedicated segment that operates concurrently with all other
segments."

**The mechanism that makes it work:** a **register is associated with every segment**. The registers
"provide isolation between each segment so that each can operate on distinct data simultaneously."
Without the isolating registers, segment k+1's combinational logic would see segment k's output
changing underneath it. **Each segment = an input register followed by a combinational circuit.**
Analogy: an industrial assembly line.

**The canonical example — compute Aᵢ × Bᵢ + Cᵢ for i = 1…7 in three segments:**
```
Segment 1:  R1 ← Aᵢ,  R2 ← Bᵢ                 load
Segment 2:  R3 ← R1 × R2,  R4 ← Cᵢ            multiply and load
Segment 3:  R5 ← R3 + R4                      add
```

Contents of the registers, clock by clock — note how the pipeline **fills**, runs **full**, then
**drains**:

| Clock | R1 | R2 | R3 | R4 | R5 |
|---|---|---|---|---|---|
| 1 | A1 | B1 | — | — | — |
| 2 | A2 | B2 | A1×B1 | C1 | — |
| 3 | A3 | B3 | A2×B2 | C2 | A1×B1+C1 |
| 4 | A4 | B4 | A3×B3 | C3 | A2×B2+C2 |
| 5 | A5 | B5 | A4×B4 | C4 | A3×B3+C3 |
| 6 | A6 | B6 | A5×B5 | C5 | A4×B4+C4 |
| 7 | A7 | B7 | A6×B6 | C6 | A5×B5+C5 |
| 8 | — | — | A7×B7 | C7 | A6×B6+C6 |
| 9 | — | — | — | — | A7×B7+C7 |

**7 tasks in a 3-segment pipeline take 9 clocks** — which is exactly k + n − 1 = 3 + 7 − 1. The first
result appears at clock 3 (latency = k); one result per clock thereafter (throughput = 1/tₚ).

## 5. Speedup — `settled` (the numerical exam item)

For a **k-segment** pipeline with clock cycle **tₚ**, executing **n** tasks:

- The first task takes **k·tₚ** to traverse all segments.
- The remaining n − 1 tasks emerge one per clock: **(n − 1)·tₚ**.
- **Total pipelined time = (k + n − 1)·tₚ**

A non-pipelined unit doing the same work in **tₙ** per task takes **n·tₙ**.

> **S = n·tₙ / ((k + n − 1)·tₚ)**

**Two limits worth deriving, not memorizing:**

- As **n → ∞**: the (k − 1) becomes negligible, so **S → tₙ / tₚ**.
- If additionally **tₙ = k·tₚ** (the non-pipelined unit takes exactly as long as all k segments):
  **S → k**.

> **The theoretical maximum speedup of a k-segment pipeline is k.**

**Worked example (the deck's own — expect this form):** 4-stage pipeline, tₚ = 20 ns, 100 tasks.
- Non-pipelined: one task takes 4 × 20 = **80 ns**; 100 tasks = 100 × 80 = **8000 ns**.
- Pipelined: (k + n − 1)·tₚ = (4 + 99) × 20 = **2060 ns**.
- **S = 8000 / 2060 = 3.88** — close to but below the ceiling of 4, because the pipeline had to fill.

**Why real pipelines fall short of k** (state these; they are the "explain" half of the question):
1. **Segments take different times.** The clock must accommodate the *slowest* segment, so faster
   segments idle.
2. **The interface registers cost time.** tₚ includes a register delay tᵣ that the non-pipelined
   circuit never pays.
3. **It is not true that tₙ = k·tₚ** in general — the assumption behind S → k.
4. **Hazards** stall the pipeline (§8).

**Pipeline vs multiple functional units:** a k-stage pipeline achieves roughly what k identical
parallel units achieve — but with **one** copy of the hardware, processing data in sequence rather
than simultaneously. That is the economic argument for pipelining.

## 6. Arithmetic pipeline — `settled`

Used in high-speed computers for floating-point operations and fixed-point multiplication.

**Floating-point addition/subtraction in four segments** — inputs X = A × 2ᵃ and Y = B × 2ᵇ
(A, B mantissas; a, b exponents):

| Segment | Suboperation | Mechanism |
|---|---|---|
| 1 | **Compare the exponents** | subtract them; the **larger** becomes the result's exponent |
| 2 | **Align the mantissas** | shift the **smaller-exponent** mantissa **right** by the exponent difference |
| 3 | **Add or subtract the mantissas** | |
| 4 | **Normalize the result** | on **overflow**, shift mantissa right and increment exponent; on **underflow**, count leading zeros, shift left that many, and subtract from the exponent |

Implemented with combinational comparator, shifter, adder/subtractor, incrementer and decrementer.

**Worked timing example (`settled`):** t₁ = 60 ns, t₂ = 70 ns, t₃ = 100 ns, t₄ = 80 ns, interface
register delay tᵣ = 10 ns.
- **Pipelined clock:** set by the **slowest** segment plus the register: tₚ = t₃ + tᵣ = **110 ns**.
- **Non-pipelined:** tₙ = t₁ + t₂ + t₃ + t₄ + tᵣ = **320 ns**.
- **Speedup = 320 / 110 ≈ 2.9** — not 4, because the segments are unequal. **This example exists
  precisely to show why you don't get k.**

## 7. Instruction pipeline — `settled`

Pipelining applied to the **instruction stream** rather than the data stream: overlap fetch, decode
and execute.

**The six general phases of an instruction cycle:**
1. Fetch the instruction from memory
2. Decode the instruction
3. Calculate the effective address
4. Fetch the operands from memory
5. Execute the operation
6. Store the result

(Some instructions skip phases; EA calculation can fold into decoding; storing to a register happens
automatically in the execute phase.)

**Mano's four-segment instruction pipeline** — obtained by two mergers: decode + EA calculation into
one segment, and execute + store into one:

| Segment | Name | Job |
|---|---|---|
| 1 | **FI** | Fetch the instruction from memory |
| 2 | **DA** | Decode the instruction **and** calculate the effective address |
| 3 | **FO** | Fetch the operand |
| 4 | **EX** | Execute the operation |

Up to four instructions are in flight at once.

**On a branch:** "the pending operations in the last two segments are completed and all information
stored in the instruction buffer is deleted." An **interrupt** likewise empties the pipeline and
restarts from the new address.

**Why an instruction pipeline can't run at full rate:** segments take different times; some segments
are **skipped** for some instructions; and **two segments may need memory at the same time**, forcing
one to wait.

## 8. Pipeline hazards — `settled` (L19 — "differentiate the types")

Three classes. **Know the cause, an example, and the cure for each** — that is the shape of the
question.

### (a) Structural hazards — resource conflicts

**Cause:** "hardware resources required by the instructions in simultaneous overlapped execution
cannot be met" — some resource has not been duplicated enough.

**Canonical example:** with **one memory port**, an instruction fetch (FI) and an operand fetch (FO)
cannot both happen in the same clock. The later one **stalls**.

```
 i    FI  DA  FO  EX
 i+1      FI  DA  FO  EX
 i+2          stall stall FI  DA  FO  EX
```

**Cures:** duplicate the resource — a **two-port memory**, or **separate instruction and data
memories** (i.e. **Harvard**, closing the loop with U1 §3).

### (b) Data hazards — data-dependency conflicts

**Cause:** "an instruction scheduled to be executed in the pipeline requires the result of a previous
instruction, which is not yet available."

**Canonical example:**
```
ADD R1, R2, R3      ; R1 ← R2 + R3
SUB R4, R1, R5      ; needs R1 — but ADD hasn't written it back yet
```

**Cures:**

| Cure | Kind | Mechanism |
|---|---|---|
| **Hardware interlock** | HW | a circuit detects that an instruction's source is a pending destination, and **stalls** enough cycles. Preserves program order at the cost of time |
| **Forwarding (bypassing / short-circuiting)** | HW | a **data path routes the value directly from its producer (usually the ALU output) to its consumer**, bypassing the register file — so the value is used a stage *earlier* than a write-then-read would allow. Costs multiplexers + detection logic |
| **Instruction scheduling / delayed load** | SW | the **compiler** reorders instructions (or inserts NOPs) so the dependent instruction isn't adjacent |

**Forwarding, made concrete** (the deck's 3-stage I/A/E example): without bypassing, SUB must wait
for ADD's E stage to write R1. With bypassing, ADD's ALU result is routed straight into SUB's A stage
— **no stall**.

**Delayed load, worked** (`a = b + c; d = e − f;`):
```
   Unscheduled            Scheduled (compiler reordered)
   LW  Rb, b              LW  Rb, b
   LW  Rc, c              LW  Rc, c
   ADD Ra, Rb, Rc   ←     LW  Re, e        ← a useful instruction inserted
   SW  a,  Ra             ADD Ra, Rb, Rc      into the delay slot
   LW  Re, e              LW  Rf, f
   LW  Rf, f              SW  a,  Ra
   SUB Rd, Re, Rf         SUB Rd, Re, Rf
   SW  d,  Rd             SW  d,  Rd
```
The reordering fills what would have been stall cycles with independent work. **Note this is a
*compiler* fix to a *hardware* problem — the RISC philosophy in miniature (→ U8).**

### (c) Control hazards — branch difficulties

**Cause:** "branches and other instructions that change the PC make the fetch of the next instruction
to be delayed" — the branch target address is not known until the branch instruction completes, so
the pipeline does not know what to fetch next.

**Five cures** (the deck lists exactly these):

| Cure | Mechanism |
|---|---|
| **Prefetch target instruction** | fetch **both** streams (taken and not-taken), keep both until the branch resolves, then discard the wrong one |
| **Branch target buffer (BTB)** | an **associative memory** in the fetch segment holding previously executed branch addresses + their target instructions (and the next few after). On fetch, search the BTB; hit → fetch from there; miss → fetch normally and update the BTB |
| **Loop buffer** | a small very-high-speed register file holding an **entire loop**, so the loop executes without further memory accesses |
| **Branch prediction** | guess the outcome with additional logic and fetch speculatively; a correct guess eliminates the penalty |
| **Delayed branch** | the **compiler** rearranges code, inserting useful instructions after the branch that execute regardless ("delay slot"). Used in most RISC processors; NOPs if nothing useful exists |

**Pipeline interlock** (the general term): detect hazards, stall until cleared.

---

## Worked-problem patterns for this unit

1. **Numerical speedup** — given k, n, tₙ, tₚ compute S; compare with the ceiling k; explain the gap.
2. **Arithmetic-pipeline timing** — given per-segment delays and tᵣ, find tₚ, tₙ and S (the 110/320
   example).
3. **Space-time diagram** for a k-segment pipeline over n tasks; read off when the pipeline is full.
4. **Register-content table** for the Aᵢ×Bᵢ+Cᵢ pipeline.
5. **Flynn's classification** — the 2×2 table, one example per class, and "MISD has no real example."
6. **Given an instruction pair, name the hazard and give the cure.**
7. Explain forwarding with a before/after diagram.
8. Reorder code to remove a delayed-load stall.
9. Explain the four segments of a floating-point adder pipeline.
10. List and explain the five control-hazard techniques.

## Confidence summary

`settled`: throughput vs latency framing · the four throughput techniques · levels of parallelism ·
Flynn's four classes with characteristics and example systems · MISD has no extant realization ·
pipelining definition and the role of the isolating register · the k+n−1 timing and the register
table · **S = n·tₙ/((k+n−1)·tₚ)**, its limits tₙ/tₚ and k · the 4-stage/100-task/3.88 example · the
FP-adder four segments and the 110 ns / 320 ns / 2.9 example · FI-DA-FO-EX · all three hazard classes
with causes and cures · the delayed-load reordering.
*(Deck and an independent institutional reproduction agree on every formula and worked number.)*
`likely`: that MUJ asks the speedup numerically rather than descriptively — inferred from L17's
Session Outcome ("Explain the role of Pipelining in **speedup**") and the deck's worked example.
Not claimed: superscalar/VLIW internals beyond the names; vector-processor and array-processor detail
beyond Flynn (out of scope — `00-map.md`).

> **Stage 2 for this unit:** `stage-2/04-parallel-processing-and-pipelining.md` — Amdahl's law as the
> hard ceiling on all of this, why deeper pipelines stopped paying (the Pentium 4 lesson), RAW/WAR/WAW
> and why only RAW is a true dependence, branch-prediction accuracy and the 2-bit predictor,
> speculation and its security cost (Spectre/Meltdown), and where Flynn's taxonomy breaks down for
> GPUs (SIMT).
