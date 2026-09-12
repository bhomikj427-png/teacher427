# 10 — Pipelining: Speedup, the Arithmetic and Instruction Pipelines, Hazards

**U4, lectures L17–L19 · CO3.** L17 is practitioner-delivered and its stated Session Outcome is
*"Explain the role of Pipelining in **speedup**"* — which is why the **numerical** is the expected
form here. This is the highest-yield file in the pack after 05 and 06.

---

## Map

```
   PIPELINE = decompose a process into segments, one REGISTER per segment
        |
        |   the register is what makes it work: it isolates each segment
        |   so the next one's logic does not see the previous one changing
        v
   n tasks through k segments take (k + n − 1) clocks
        |
        v
   SPEEDUP  S = n·tₙ / ((k + n − 1)·tₚ)
        |
        +-- as n -> ∞:                   S -> tₙ / tₚ
        +-- if also tₙ = k·tₚ:           S -> k      <- the CEILING, never reached
        |
        +-- why never: unequal segments | register delay tᵣ | tₙ ≠ k·tₚ | HAZARDS
        |
        v
   TWO KINDS       arithmetic pipeline (FP add: compare, align, add, normalize)
                   instruction pipeline (FI - DA - FO - EX)
        |
        v
   HAZARDS   structural (resource)  -> duplicate the resource / Harvard
             data (dependency)      -> interlock | FORWARDING | compiler scheduling
             control (branch)       -> prefetch both | BTB | loop buffer | predict | delayed branch
```

---

## Attempt first

1. Why does every pipeline segment need a register in front of it?
2. Seven tasks through a 3-segment pipeline: how many clocks? Give the formula, then the number.
3. Write the speedup formula and derive the two limits.
4. A 4-stage pipeline with tₚ = 20 ns processes 100 tasks. Compute the speedup against a
   non-pipelined unit taking 80 ns per task.
5. Segment delays are 60, 70, 100, 80 ns with a 10 ns register delay. What is tₚ? What is tₙ?
6. Name the three hazard classes, and one cure for each.
7. `ADD R1, R2, R3` followed by `SUB R4, R1, R5`. Which hazard, and what does forwarding do about it?

---

## Method

### The core idea

**Definition:** *"a technique of decomposing a sequential process into suboperations, with each
subprocess being executed in a special dedicated segment that operates concurrently with all other
segments."*

**★ The mechanism that makes it work:** a **register is associated with every segment**. The registers
*"provide isolation between each segment so that each can operate on distinct data simultaneously."*
Without them, segment k+1's combinational logic would see segment k's output changing underneath it.

> **Each segment = an input register followed by a combinational circuit.**

The analogy is an industrial assembly line — and like an assembly line, the line's rate is set by its
**slowest** station.

### The canonical example — Aᵢ × Bᵢ + Cᵢ for i = 1…7, in three segments

```
   Segment 1:  R1 ← Aᵢ,  R2 ← Bᵢ                 load
   Segment 2:  R3 ← R1 × R2,  R4 ← Cᵢ            multiply and load
   Segment 3:  R5 ← R3 + R4                      add
```

Register contents, clock by clock — watch it **fill**, run **full**, then **drain**:

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

**7 tasks in a 3-segment pipeline take 9 clocks** — which is exactly **k + n − 1 = 3 + 7 − 1**.
The first result appears at clock **k** (that is the latency); one result per clock thereafter (that
is the throughput, 1/tₚ).

### Speedup — the numerical

For a **k-segment** pipeline with clock period **tₚ**, executing **n** tasks:

```
   the first task traverses all k segments:       k·tₚ
   the remaining n − 1 emerge one per clock:     (n − 1)·tₚ
   --------------------------------------------------------
   total pipelined time                     =    (k + n − 1)·tₚ

   a non-pipelined unit taking tₙ per task   =    n·tₙ
```

> ### **S = n·tₙ / ((k + n − 1)·tₚ)**

**The two limits — derive them, do not memorize them:**

- As **n → ∞**, the (k − 1) becomes negligible beside n, so **S → tₙ / tₚ**.
- If additionally **tₙ = k·tₚ** (the non-pipelined unit takes exactly as long as all k segments
  together), then **S → k**.

> **The theoretical maximum speedup of a k-segment pipeline is k.**

**Why real pipelines fall short of k — state these; they are the "explain" half of the question:**

1. **Segments take different times.** The clock must accommodate the **slowest** segment, so the
   faster ones idle.
2. **The interface registers cost time.** tₚ includes a register delay tᵣ that the non-pipelined
   circuit never pays.
3. **tₙ = k·tₚ is not true in general** — that assumption is what produced the ceiling.
4. **Hazards** stall the pipeline.

**Pipeline versus multiple functional units:** a k-stage pipeline achieves roughly what k identical
parallel units achieve, but with **one** copy of the hardware, processing data in sequence rather than
simultaneously. That is the economic argument for pipelining, and it is worth one line in any
"explain the role of pipelining" answer.

### The arithmetic pipeline — floating-point addition in four segments

Inputs X = A × 2ᵃ and Y = B × 2ᵇ (A, B mantissas; a, b exponents):

| Segment | Suboperation | Mechanism |
|---|---|---|
| 1 | **Compare the exponents** | subtract them; the **larger** becomes the result's exponent |
| 2 | **Align the mantissas** | shift the **smaller-exponent** mantissa **right** by the difference |
| 3 | **Add or subtract the mantissas** | |
| 4 | **Normalize the result** | on **overflow**: shift the mantissa right, increment the exponent. On **underflow**: count leading zeros, shift left that many, subtract from the exponent |

Built from a combinational comparator, shifter, adder-subtractor, incrementer and decrementer.

**The worked timing example — expect this exact shape.** t₁ = 60, t₂ = 70, t₃ = 100, t₄ = 80 ns, with
interface register delay tᵣ = 10 ns:

```
   pipelined clock:    tₚ = (slowest segment) + tᵣ = 100 + 10 = 110 ns
   non-pipelined:      tₙ = t₁ + t₂ + t₃ + t₄ + tᵣ = 60 + 70 + 100 + 80 + 10 = 320 ns
   speedup (large n):  S  = tₙ / tₚ = 320 / 110 = 2.9
```

**Not 4 — because the segments are unequal.** This example exists *precisely* to show why you do not
get k. Say that sentence in the answer.

### The instruction pipeline

Pipelining applied to the **instruction stream**: overlap fetch, decode and execute.

**The six general phases of an instruction cycle:**

```
   1. fetch the instruction from memory
   2. decode the instruction
   3. calculate the effective address
   4. fetch the operands from memory
   5. execute the operation
   6. store the result
```

Some instructions skip phases; EA calculation can fold into decoding; storing to a register happens
automatically in the execute phase.

**Mano's four-segment instruction pipeline** — obtained by two mergers (decode + EA calculation into
one; execute + store into one):

| Segment | Name | Job |
|---|---|---|
| 1 | **FI** | Fetch the Instruction from memory |
| 2 | **DA** | Decode the instruction **and** calculate the effective Address |
| 3 | **FO** | Fetch the Operand |
| 4 | **EX** | EXecute the operation |

Up to four instructions are in flight at once.

**On a branch:** *"the pending operations in the last two segments are completed and all information
stored in the instruction buffer is deleted."* An **interrupt** likewise empties the pipeline and
restarts from the new address.

**Why an instruction pipeline cannot run at full rate:** segments take different times · some segments
are **skipped** for some instructions · and **two segments may need memory at the same time**, forcing
one to wait.

### Hazards — know the cause, an example, and the cure for each

#### (a) Structural hazards — resource conflicts

**Cause:** *"hardware resources required by the instructions in simultaneous overlapped execution
cannot be met"* — some resource has not been duplicated enough.

**Canonical example:** with **one memory port**, an instruction fetch (FI) and an operand fetch (FO)
cannot both happen in the same clock. The later one **stalls**.

```
   i     FI   DA   FO   EX
   i+1        FI   DA   FO   EX
   i+2             --stall--   FI   DA   FO   EX
```

**Cures:** duplicate the resource — a **two-port memory**, or **separate instruction and data
memories**, which is to say **Harvard architecture**. (This closes the loop with file 01.)

#### (b) Data hazards — data-dependency conflicts

**Cause:** *"an instruction scheduled to be executed in the pipeline requires the result of a previous
instruction, which is not yet available."*

**Canonical example:**

```
   ADD R1, R2, R3      ; R1 ← R2 + R3
   SUB R4, R1, R5      ; needs R1 — but ADD has not written it back yet
```

**Cures:**

| Cure | Kind | Mechanism |
|---|---|---|
| **Hardware interlock** | HW | a circuit detects that an instruction's source is a pending destination and **stalls** enough cycles. Preserves program order, costs time |
| **Forwarding** (bypassing, short-circuiting) | HW | a **data path routes the value directly from its producer — usually the ALU output — to its consumer**, bypassing the register file, so the value is used a stage *earlier* than a write-then-read would allow. Costs multiplexers and detection logic |
| **Instruction scheduling / delayed load** | SW | the **compiler** reorders instructions (or inserts NOPs) so the dependent instruction is not adjacent |

**Delayed load, worked** — for `a = b + c; d = e − f;`:

```
   Unscheduled                 Scheduled (compiler reordered)
   LW  Rb, b                   LW  Rb, b
   LW  Rc, c                   LW  Rc, c
   ADD Ra, Rb, Rc   <--        LW  Re, e          <-- an independent instruction moved
   SW  a,  Ra                  ADD Ra, Rb, Rc         into what would have been a stall
   LW  Re, e                   LW  Rf, f
   LW  Rf, f                   SW  a,  Ra
   SUB Rd, Re, Rf              SUB Rd, Re, Rf
   SW  d,  Rd                  SW  d,  Rd
```

**Note what this is:** a **compiler** fix to a **hardware** problem — the RISC philosophy in
miniature.

#### (c) Control hazards — branch difficulties

**Cause:** *"branches and other instructions that change the PC make the fetch of the next instruction
to be delayed"* — the target address is not known until the branch resolves, so the pipeline does not
know what to fetch.

**The five cures:**

| Cure | Mechanism |
|---|---|
| **Prefetch target instruction** | fetch **both** streams (taken and not-taken), keep both until the branch resolves, then discard the wrong one |
| **Branch target buffer (BTB)** | an **associative memory** in the fetch segment holding previously executed branch addresses and their target instructions. On fetch, search the BTB: hit → fetch from there; miss → fetch normally and update the BTB |
| **Loop buffer** | a small very-high-speed register file holding an **entire loop**, so the loop runs without further memory accesses |
| **Branch prediction** | guess the outcome with additional logic and fetch speculatively; a correct guess eliminates the penalty |
| **Delayed branch** | the **compiler** rearranges code, putting useful instructions after the branch that execute regardless (the "delay slot"). Used in most RISC processors; NOPs if nothing useful exists |

**Pipeline interlock** is the general term for the hardware that detects hazards and stalls until they
clear.

---

## Worked — the speedup numerical (the deck's own example; form F14)

> **A non-pipelined unit takes 80 ns per task. A 4-stage pipeline with a 20 ns clock replaces it.
> Compute the time for 100 tasks both ways and the speedup. State the ceiling and explain the gap.**

**Step 1 — write the formula before substituting anything.**

```
   S = n·tₙ / ((k + n − 1)·tₚ)          k = 4,  n = 100,  tₙ = 80 ns,  tₚ = 20 ns
```

**Step 2 — non-pipelined time.**

```
   n·tₙ = 100 × 80 = 8000 ns
```

**Step 3 — pipelined time.** This is where marks are lost: it is **k + n − 1**, not k + n and not n.

```
   (k + n − 1)·tₚ = (4 + 100 − 1) × 20 = 103 × 20 = 2060 ns
```

**Step 4 — speedup.**

```
   S = 8000 / 2060 = 3.88
```

**Step 5 — the ceiling and the gap, which is the "explain" half.**

> The theoretical maximum for a 4-segment pipeline is **k = 4**. The measured 3.88 falls short because
> the pipeline must **fill**: the first result takes 4 clocks, so 103 clocks are needed for 100 tasks
> rather than 100. As n grows the gap closes — for n = 1000, S = (1000 × 80)/(1003 × 20) = **3.99** —
> but it never reaches 4.

**The follow-up to be ready for:** *"would a 12-stage pipeline be 12× faster?"*
**No.** Three reasons: segment delays would not divide evenly, so the clock is set by the slowest;
each of the 12 interface registers adds tᵣ to that clock; and more stages means a longer pipeline to
**flush** on every branch, so hazard penalties grow with depth. Beyond some depth the register
overhead and branch penalties dominate and speedup *falls*.

---

## Worked — the unequal-segment numerical (the deck's FP-adder example)

> **A floating-point adder pipeline has segment delays t₁ = 60 ns, t₂ = 70 ns, t₃ = 100 ns,
> t₄ = 80 ns, and an interface register delay tᵣ = 10 ns. Find the pipeline clock, the non-pipelined
> time, and the speedup for a large number of operations.**

**Step 1 — the pipeline clock is set by the SLOWEST segment, plus the register.** Not the average, not
the sum.

```
   tₚ = max(t₁, t₂, t₃, t₄) + tᵣ = 100 + 10 = 110 ns
```

**Step 2 — the non-pipelined time is the sum of all the work, plus one register delay.**

```
   tₙ = t₁ + t₂ + t₃ + t₄ + tᵣ = 60 + 70 + 100 + 80 + 10 = 320 ns
```

**Step 3 — speedup for large n.**

```
   S → tₙ / tₚ = 320 / 110 = 2.9
```

**Step 4 — the sentence the question is actually testing.**

> The ceiling for 4 segments is 4, but this pipeline reaches only **2.9**, because the segments are
> **unequal**: the 100 ns segment forces a 110 ns clock, so the 60 ns segment wastes 50 ns every
> cycle. **Balancing the segments — not adding more of them — is what would improve this design.**

If the four segments could be rebalanced to 77.5 ns each, tₚ would be 87.5 ns and S would rise to
about 3.7. That observation is worth stating: **pipeline design is segment balancing.**

---

## Worked — identify the hazard and give the cure (form F16)

> **For each pair, name the hazard class and give a cure:**
> **(a)** `LW R1, 0(R2)` then `ADD R3, R1, R4`
> **(b)** instruction i is in FO while instruction i+2 is in FI, and the machine has one memory port
> **(c)** `BEQ R1, R2, LABEL` followed by the next sequential instruction

**(a) Data hazard** (read-after-write). ADD needs R1, which LW has not yet written back.
*Cure:* **forwarding** routes the loaded value to ADD's input as soon as it is available — though for
a **load** specifically, forwarding alone may not be enough (the value only exists after the memory
stage), so this is the case that needs either a one-cycle **interlock stall** or a compiler
**delayed-load** reordering. Naming the load-use special case is the discriminating remark.

**(b) Structural hazard.** FO (operand fetch) and FI (instruction fetch) both want the single memory
port in the same clock; one must stall.
*Cure:* **duplicate the resource** — a two-port memory, or separate instruction and data memories
(Harvard), or separate I-cache and D-cache.

**(c) Control hazard.** The branch's outcome and target are unknown when the next fetch must happen.
*Cure:* any of the five — **prefetch both streams · branch target buffer · loop buffer · branch
prediction · delayed branch**. Name one and say what it does; a bare name earns less.

**The classification habit that makes these instant:**

```
   do two instructions want the same PIECE OF HARDWARE?   -> structural
   does one need a VALUE the other has not produced?      -> data
   does the machine not know WHICH INSTRUCTION comes next? -> control
```

---

## Traps

| # | Trap | The correction |
|---|---|---|
| T8 / M12a | "Speedup equals k" | k is the **ceiling** as n → ∞ *and* assuming tₙ = k·tₚ. The deck's own examples give **3.88** and **2.9** |
| T9 / M12 | "Pipelining makes each instruction faster" | It raises **throughput**; single-instruction latency typically **increases** (register delays) |
| — | Using k + n instead of **k + n − 1** | The first task takes k clocks; the other n − 1 take one each. Off by one = wrong answer |
| — | Setting tₚ from the **average** segment delay | The clock is set by the **slowest** segment, plus tᵣ |
| — | Forgetting tᵣ in tₙ | The deck's non-pipelined figure is t₁+t₂+t₃+t₄+**tᵣ** = 320, not 310 |
| — | "Deeper is always better" | Register overhead per stage and the branch-flush penalty both grow with depth |
| — | Naming a hazard without its cure (or vice versa) | The question form is **cause + example + cure**. All three |
| — | Saying forwarding removes every data stall | The **load-use** case still needs a stall or a reordering — the value does not exist until the memory stage |

---

## Self-test

1. Why does each segment need its own register? What would go wrong without them?
2. Ten tasks, 5-segment pipeline. How many clocks? Show the formula.
3. A 6-segment pipeline has tₚ = 15 ns; the non-pipelined unit takes 90 ns per task. Find the speedup
   for n = 50 and for n = 500. Comment on the trend.
4. Segment delays are 40, 90, 50, 60 ns with tᵣ = 5 ns. Find tₚ, tₙ and the large-n speedup. Then say
   what single change would most improve it and by how much.
5. Name the four segments of Mano's instruction pipeline and say which two phases were merged into
   each of two of them.
6. Give the four segments of a floating-point adder pipeline in order, with what each does.
7. Classify and cure: (a) two instructions both need the ALU in the same clock on a machine with one
   ALU; (b) `MUL R1, R2, R3` then `MUL R4, R1, R1`; (c) an indirect jump through a register.
8. Explain why the structural hazard of §(a) is the *same problem* as the von Neumann bottleneck from
   file 01.

---

## Answers

**1.** The register **isolates** each segment so that segment i+1's combinational logic sees a *stable*
input for the whole clock period. Without it, as soon as segment i began computing the next task, its
output would start changing and segment i+1 would be operating on a value that is still settling —
producing garbage. The registers are what allow all k segments to work on **distinct data
simultaneously**.

**2.** `k + n − 1 = 5 + 10 − 1 = **14 clocks**.`

**3.**
```
   n = 50:   S = (50 × 90) / ((6 + 50 − 1) × 15)  = 4500 / (55 × 15)  = 4500 / 825  = 5.45
   n = 500:  S = (500 × 90) / ((6 + 500 − 1) × 15) = 45000 / (505 × 15) = 45000 / 7575 = 5.94
```
**Trend:** speedup rises toward the ceiling **k = 6** as n grows, because the fixed fill cost of
(k − 1) clocks is amortized over more tasks. It approaches 6 but never reaches it. (Here tₙ = 90 = k·tₚ
exactly, which is why 6 is the right ceiling to quote.)

**4.**
```
   tₚ = max(40, 90, 50, 60) + tᵣ = 90 + 5 = 95 ns
   tₙ = 40 + 90 + 50 + 60 + 5 = 245 ns
   S  = 245 / 95 = 2.58        (ceiling for 4 segments = 4)
```
**The single best change is to split or rebalance the 90 ns segment**, because it alone sets the
clock. If the work were redistributed evenly, each segment would take 240/4 = 60 ns, so tₚ = 65 ns and
S = 245/65 = **3.77** — a ~46% improvement from balancing alone, with no extra hardware. Adding
segments without balancing them would not help.

**5.** **FI** (fetch instruction) · **DA** (decode **and** calculate the effective address) ·
**FO** (fetch operand) · **EX** (execute).
The mergers: **decode + effective-address calculation** were merged into DA, and **execute + store
result** were merged into EX.

**6.** (1) **Compare the exponents** — subtract them; the larger becomes the result's exponent.
(2) **Align the mantissas** — shift the mantissa with the smaller exponent right by the difference.
(3) **Add or subtract the mantissas.**
(4) **Normalize** — on overflow shift right and increment the exponent; on underflow count leading
zeros, shift left that many, and subtract from the exponent.

**7.**
(a) **Structural hazard** — one ALU, two claimants. *Cure:* duplicate the resource (a second ALU or a
separate address-calculation adder), or stall one instruction.
(b) **Data hazard** — the second MUL needs R1, which the first has not written back; R1 appears as
**both** source operands, so the dependency cannot be avoided by operand choice. *Cure:* forwarding
from the multiplier's output, or an interlock stall, or compiler scheduling of independent work
between them.
(c) **Control hazard** — the target of an indirect jump is not known until the register is read, so
the fetch stage cannot know what to fetch. *Cure:* branch prediction with a target buffer (a BTB can
cache the last target for that jump), or a delayed-branch slot, or simply stall.

**8.** Both are **one shared resource serving two simultaneous demands**. The von Neumann bottleneck
is a single memory-and-bus carrying both the instruction stream and the data stream, so the CPU cannot
fetch an instruction and an operand at once. The structural hazard is that *same* single memory port
being wanted by the FI segment and the FO segment in the same clock. **Same cause, same cure:**
duplicate the path — which is Harvard architecture at the system level and split I-/D-caches or a
two-port memory at the pipeline level. The thread runs all the way back to the common bus in file 02:
sharing one path in time saves wires and costs simultaneity.

---

## Appendix — the CPI formulation (a *different* way this topic gets asked)

⚠ **This appendix is not Mano and not the method above.** Everything before this line uses Mano's
S = n·tₙ/((k+n−1)·tₚ) and his FI-DA-FO-EX segments. What follows works the same topic in **CPI and
clock-rate** terms on a MIPS 5-stage pipeline. Do not mix the two formulas.

**Why it is here at all** — one specific, checkable reason: the hand-out marks **L16 and L17 with
`*`, meaning they are delivered by an industry practitioner**, not by the course instructor
(`../knowledge-base/exam-map.md` §1). Industry pipelining is taught in CPI and IPC, not in Mano's
segment counts. So there is a real chance your pipelining lectures use this framing. That is a
`likely`, **not** a `settled` — nobody has told us what the practitioner actually taught.

**Provenance:** both problems come from an IIT Guwahati NPTEL tutorial (*Introduction to Advanced
Computer Architecture*, Prof. John Jose, Tutorial 2). The transcript was fetched and read; **the
arithmetic below was re-derived independently and matches.** See `../video-lectures.md` §5.

### The CPI model in three lines

```
   execution time per instruction  =  CPI × clock period

   effective CPI (pipelined)  =  base CPI (= 1)  +  Σ (stall cycles per instruction)

   stall contribution of a cause  =  (fraction of instructions of that type)
                                   × (fraction of those that stall)
                                   × (cycles lost per stall)
```

**The trap:** that middle factor. "5% of memory instructions miss" is **not** 5% of all
instructions — it is 5% of the 30% that are memory instructions.

### A1 — Speedup with a slower pipelined clock

> An unpipelined design runs at **1.5 GHz** and takes **5 cycles** per instruction. Pipelining it
> into 5 stages adds interface-register overhead, so the pipelined version runs at only **1 GHz**.
> In a given program: **30%** of instructions are memory instructions, of which **5%** miss and cost
> **50** stall cycles · **20%** are branches, of which **30%** cost **2** stall cycles · **10%** are
> load-ALU pairs costing **1** stall cycle. Find the speedup.

**Step 1 — the two clock periods.**

```
   unpipelined:  1 / 1.5 GHz = 0.667 ns
   pipelined:    1 / 1 GHz   = 1.0 ns          <- slower, on purpose: that is the register overhead
```

**Step 2 — unpipelined time per instruction.**

```
   CPI × clock = 5 × 0.667 = 3.33 ns
```

**Step 3 — effective CPI of the pipelined version.** Base 1, then one term per stall cause:

| Cause | fraction × fraction × cycles | contribution |
|---|---|---|
| memory miss | 0.30 × 0.05 × 50 | **0.75** |
| branch | 0.20 × 0.30 × 2 | **0.12** |
| load-ALU | 0.10 × 1 | **0.10** |
| | base | 1.00 |
| | **effective CPI** | **1.97** |

**Step 4 — pipelined time and speedup.**

```
   pipelined:  1.97 × 1.0 ns = 1.97 ns
   speedup  =  3.33 / 1.97   =  1.69
```

**The sentence that carries the mark.** A 5-stage pipeline gave **1.69×**, not 5×, for two separate
reasons — and naming both is the answer:
1. the clock got **slower** (1.5 GHz → 1 GHz) because of interface-register overhead, and
2. stalls pushed CPI from 1 to **1.97**, nearly doubling it, with the memory misses alone (0.75)
   costing more than branches and load-use combined.

Note this is the same story as the Mano ceiling — *you never reach k* — told with different numbers.

### A2 — Stalls in a dependency chain, with and without forwarding

> A program has **2000 instructions**: Load, Add, Load, Add, … Every Add depends on the Load
> immediately before it, and every Load depends on the Add immediately before it. On a 5-stage
> pipeline, find the actual CPI **without** operand forwarding and **with** it.

**Without forwarding.** A dependent instruction cannot decode until the producer has written back,
so **ID of instruction n must follow WB of instruction n−1** — that is **3 stall cycles** each.

```
   instruction 1 reaches WB at cycle 5
   every later instruction follows 4 cycles behind the last (1 + 3 stalls)

   total = 5 + 1999 × 4 = 5 + 7996 = 8001 cycles
   CPI   = 8001 / 2000 = 4.0
```

**With forwarding.** Now the asymmetry appears, and it is the whole point of the question:

- **Add after Load → still 1 stall.** Forwarding cannot beat the clock here: the loaded value does
  not exist until the end of MEM, so it can only reach the *next* instruction's EX. This is the
  **load-use** case from the Traps table above.
- **Load after Add → no stall.** The Add's result is available at the ALU output and forwards
  cleanly.

So **every second instruction stalls once**, not every instruction three times.

```
   loads complete at 5, 8, 11, 14, …        adds complete at 7, 10, 13, 16, …
   the last instruction is the 1000th Add:  7 + 999 × 3 = 3004 cycles
   CPI = 3004 / 2000 = 1.502
```

**Sanity check worth doing in the exam:** 2000 instructions, 1000 of them stalling once, ≈ 3000
cycles, CPI ≈ 1.5. If your exact answer is far from that, you mis-counted the pattern.

**What this problem is really testing** — and the reason it earns its place here even though the
notation is not Mano's: **forwarding does not remove all data stalls.** The load-use hazard survives
it. An answer that says "forwarding fixes data hazards" full stop is the one this question is built
to catch, in exactly the way trap "forwarding removes every data stall" above says.

### What was deliberately left out

The same tutorial's third numerical is a **2-bit correlating branch predictor** (state transitions
over 16 outcomes). Branch prediction is named in `study-pack/10` as one of the five control-hazard
cures, and that is all the MTE needs — predictor *state machines* are Stage-2 depth
(`../knowledge-base/stage-2/04-…`). **Out of scope; skip it.**

---
