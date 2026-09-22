# 11 — Parallel processing and pipelining

**Assignment 2: Q11–Q15 · 50 of 150 marks · U4 (L16–L19) · needs only 03**

The biggest single block in Assignment 2, and **all five questions are Mano chapter 9 verbatim**.
It also needs almost nothing from files 06–10, so you can do this file early if you want numerical
marks banked.

> ⚠ **Pipelining is on your mid-term.** Most universities put it after. The hand-out prints the Mid
> Term Examination divider immediately after **L19**, and pipelining is L16–L19. Do not assume the
> conventional ordering.
>
> L16 and L17 are marked `*` in the hand-out — delivered by an **industry practitioner**.

---

## Map

```
   [1] Throughput ≠ latency ──────► the thing pipelining actually buys
         │
         ├──► [2] Flynn's classification   SISD SIMD MISD MIMD
         │
         ▼
   [3] Pipelining — the isolating register
         │
         ├──► [4] k + n − 1  and the register table      (A2 Q11, Q12)
         │
         ├──► [5] Speedup S = n·tₙ / ((k+n−1)·tₚ)        (A2 Q13)
         │           └── why you never reach k
         │
         ├──► [6] Arithmetic pipeline — the FP adder
         │
         ▼
   [7] Instruction pipeline  FI DA FO EX                 (A2 Q15)
         │
         ▼
   [8] Hazards  structural · data · control              (A2 Q14)
```

---

## The questions this file answers

| # | Question | Marks | Mano |
|---|---|---|---|
| 1 | `[A2 Q11]` Perform (Aᵢ + Bᵢ)(Cᵢ + Dᵢ) on a stream. Specify a pipeline configuration and list all register contents for i = 1…6. | 10 | **9-1** |
| 2 | `[A2 Q12]` Clock cycles to process 200 tasks in a six-segment pipeline. | 10 | **9-3** |
| 3 | `[A2 Q13]` Three-segment (Aᵢ × Bᵢ) + Cᵢ with given propagation times: minimum clock, non-pipeline time, speedup for 10 and 100 tasks, maximum speedup. | 10 | **9-5** |
| 4 | `[A2 Q14]` Explain four possible **hardware** schemes to minimise degradation from instruction branching. | 10 | **9-10** |
| 5 | `[A2 Q15]` Four instructions in a four-segment pipeline — what happens in each segment during step 4? | 10 | **9-11** |

Unasked Mano follow-ups: **9-2, 9-4, 9-6, 9-7, 9-8, 9-9, 9-12 … 9-20.** 9-4 and 9-7 are the two most
likely exam numericals he has not yet used.

---

## Build

### 1 · Throughput is not latency

> **Q** *(the conceptual question behind every numerical here)*
> **Does pipelining make an individual instruction faster?**
>
> *Guess yes or no, and commit to it before reading. Most people guess wrong.*

**No.** A pipelined instruction takes *more* total time than an unpipelined one, because it now pays a
register delay between every stage. What pipelining buys is **throughput**, not latency.

| Quantity | Meaning |
|---|---|
| **Latency** | how long **one** task takes from start to finish |
| **Throughput** | how many tasks finish **per unit time** |

Architects raise throughput *"often at the expense of slight increases in individual task latency."*
Anyone who conflates the two cannot answer "does pipelining make a program faster?" correctly — the
honest answer is *it makes the machine finish far more instructions per second, while each individual
instruction takes slightly longer.*

**The four techniques for raising throughput** (the deck's own list):

| Technique | Mechanism |
|---|---|
| **Pipelining** | break the work into steps so several overlap |
| **Parallelism** | add execution units or cores |
| **Caching** | keep hot data in small ultra-fast memory near the CPU |
| **Vector processing** | one instruction operates on a whole dataset (SIMD) |

> ✓ **Check 1.** (a) Define throughput and latency in one line each. (b) Why does a pipelined
> instruction take longer than an unpipelined one? (c) Name the four throughput techniques.

---

### 2 · Flynn's classification

> **Q** *(a standard descriptive item; the deck devotes slides to it)*
> **Classify computers by Flynn's scheme. Give one real example per class.**
>
> *Guess how many of the four classes have real machines. The answer is not four.*

Flynn classified by the **multiplicity of instruction streams and data streams**.

|  | **Single Data** | **Multiple Data** |
|---|---|---|
| **Single Instruction** | **SISD** | **SIMD** |
| **Multiple Instruction** | **MISD** | **MIMD** |

**SISD** — one control unit, one processor, one memory. The standard von Neumann machine. Parallelism,
if any, comes from **multiple functional units or pipelining** inside it. Its limitation is the
**von Neumann bottleneck** (file 01, step 2): speed is capped by memory bandwidth.

**SIMD** — many processing elements under **one** control unit. **Only one copy of the program
exists**; the controller broadcasts one instruction and all active PEs execute it on **different
data**. Three types: array processors (**ILLIAC IV**, Connection Machine), systolic arrays (CMU Warp),
associative processors (STARAN).

**MISD** — ⚠ **"there is no computer at present that can be classified as MISD."** It is of
theoretical interest only. **Say that plainly; do not invent an example.**

**MIMD** — multiple units executing multiple instructions on multiple data. Two families:

| | **Shared-memory multiprocessor** | **Message-passing multicomputer** |
|---|---|---|
| Memory | one large shared address space | each processor has **its own** |
| Communication | through shared memory | by **passing messages** |
| Examples | Sequent Balance, Encore Multimax, C.mmp | hypercube (Cosmic Cube, iPSC, NCUBE), mesh, tree |
| Limitation | memory-access latency; the **hot-spot** problem | communication overhead; hard to program |

★ **The limitation the table hides, and a good short-answer question: pipelining does not fit Flynn's
classification at all.** Flynn counts *streams*; a pipeline has one of each and overlaps them **in
time**. The taxonomy has no axis for that.

> ✓ **Check 2.** (a) Which class has no real machine? (b) In a SIMD machine, how many copies of the
> program exist? (c) Why does pipelining escape Flynn's scheme?

---

### 3 · What makes a pipeline work

> **Q** *(the definition, and the one component everyone leaves out of the diagram)*
> **Define pipelining. What component makes it possible, and what goes wrong without it?**
>
> *Guess what sits between two stages of an assembly line in hardware.*

**Definition:** *a technique of decomposing a sequential process into suboperations, with each
subprocess executed in a dedicated segment that operates concurrently with all other segments.*

★ **A register is associated with every segment.** The registers *"provide isolation between each
segment so that each can operate on distinct data simultaneously."* **Each segment = an input
register followed by a combinational circuit.**

**Without the isolating registers**, segment k+1's combinational logic would see segment k's output
changing underneath it as the next task flowed in — the stages would smear together and nothing would
be reliable. The register is what freezes each stage's input for a whole clock period.

That register is also why tₚ is never quite tₙ/k: **it costs time the unpipelined circuit never pays**
(step 5).

> ✓ **Check 3.** (a) What is between two segments? (b) What goes wrong without it? (c) What is a
> segment made of?

---

### 4 · The k + n − 1 rule — A2 Q11 and Q12

> **Q** `[A2 Q12 · 10 marks]` **= Mano 9-3**
> **Determine the number of clock cycles that it takes to process 200 tasks in a six-segment pipeline.**
>
> **and** `[A2 Q11 · 10 marks]` **= Mano 9-1**
> **In certain scientific computations it is necessary to perform the arithmetic operation
> (Aᵢ + Bᵢ)(Cᵢ + Dᵢ) with a stream of numbers. Specify a pipeline configuration to carry out this
> task. List the contents of all registers in the pipeline for i = 1 through 6.**
>
> *Q12 is one line if you know the rule. Derive the rule from Q11's table rather than memorising it.*

**The canonical example first** — Aᵢ × Bᵢ + Cᵢ in three segments:

```
Segment 1:  R1 ← Aᵢ,  R2 ← Bᵢ              load
Segment 2:  R3 ← R1 × R2,  R4 ← Cᵢ         multiply, and load C
Segment 3:  R5 ← R3 + R4                   add
```

Watch the pipeline **fill**, run **full**, then **drain** — 7 tasks, 3 segments:

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

**9 clocks for 7 tasks in 3 segments** — and 9 = 3 + 7 − 1.

> **Total time = (k + n − 1) clock cycles.** The first task takes **k** clocks to traverse all
> segments (that is the **latency**); the remaining n − 1 emerge **one per clock** (that is the
> **throughput**).

**A2 Q12 is therefore one line:** k = 6, n = 200 → **6 + 200 − 1 = 205 clock cycles.**

**A2 Q11** needs a configuration you design yourself. `(Aᵢ + Bᵢ)(Cᵢ + Dᵢ)` has two independent
additions that can run **side by side**, then one multiplication:

```
Segment 1:  R1 ← Aᵢ,  R2 ← Bᵢ,  R3 ← Cᵢ,  R4 ← Dᵢ         load four operands
Segment 2:  R5 ← R1 + R2,       R6 ← R3 + R4              two adders, in parallel
Segment 3:  R7 ← R5 × R6                                  multiply
```

k = 3, n = 6 → **3 + 6 − 1 = 8 clocks.**

| Clock | R1 | R2 | R3 | R4 | R5 | R6 | R7 |
|---|---|---|---|---|---|---|---|
| 1 | A1 | B1 | C1 | D1 | — | — | — |
| 2 | A2 | B2 | C2 | D2 | A1+B1 | C1+D1 | — |
| 3 | A3 | B3 | C3 | D3 | A2+B2 | C2+D2 | (A1+B1)(C1+D1) |
| 4 | A4 | B4 | C4 | D4 | A3+B3 | C3+D3 | (A2+B2)(C2+D2) |
| 5 | A5 | B5 | C5 | D5 | A4+B4 | C4+D4 | (A3+B3)(C3+D3) |
| 6 | A6 | B6 | C6 | D6 | A5+B5 | C5+D5 | (A4+B4)(C4+D4) |
| 7 | — | — | — | — | A6+B6 | C6+D6 | (A5+B5)(C5+D5) |
| 8 | — | — | — | — | — | — | (A6+B6)(C6+D6) |

**Two adders in segment 2, not one.** The two sums are independent, so doing them sequentially would
need a fourth segment and cost a clock of latency for nothing.

> ✓ **Check 4.** (a) State the total-time rule and say what each part represents. (b) `[Mano 9-2]`
> Draw a space-time diagram for a six-segment pipeline processing eight tasks — how many clocks?
> (c) When is the pipeline in Q11 completely full?

---

### 5 · Speedup — A2 Q13

> **Q** `[A2 Q13 · 10 marks]` **= Mano 9-5**
> **A three-segment pipeline performs (Aᵢ × Bᵢ) + Cᵢ. R1–R5 receive new data every clock. Propagation
> times: 40 ns for the operands to be read from memory into R1 and R2, 45 ns for the signal to
> propagate through the multiplier, 5 ns for the transfer into R3, and 15 ns to add the two numbers
> into R5.**
> **a. What is the minimum clock cycle time that can be used?**
> **b. A non-pipeline system can perform the same operation by removing R3 and R4. How long will it
> take to multiply and add the operands without using the pipeline?**
> **c. Calculate the speedup of the pipeline for 10 tasks and again for 100 tasks.**
> **d. What is the maximum speedup that can be achieved?**
>
> *Part (a) is the one that decides the rest. Guess which of the four given times sets the clock.*

**The formula, derived rather than recited:**

- pipelined time for n tasks = **(k + n − 1)·tₚ**
- non-pipelined time = **n·tₙ**

> **S = n·tₙ / ((k + n − 1)·tₚ)**

**(a) The clock is set by the *slowest segment*, not by the total.** Sort the given times into their
segments:

| Segment | Work | Time |
|---|---|---|
| 1 | read operands into R1, R2 | 40 ns |
| 2 | multiplier (45) **+ transfer into R3** (5) | **50 ns** |
| 3 | add into R5 | 15 ns |

**Minimum clock cycle tₚ = 50 ns.** Segments 1 and 3 finish early and then idle — that idling is
exactly why real speedup falls short of k.

**(b) Non-pipelined**, with R3 and R4 removed, the whole thing is one combinational path:
40 + 45 + 15 = **tₙ = 100 ns**. (The 5 ns is the transfer *into R3*, and R3 is gone.)

**(c)**
```
 n = 10 :  S = (10 × 100) / ((3 + 10 − 1) × 50)  = 1000 / (12 × 50)  = 1000/600  = 1.67
 n = 100:  S = (100 × 100) / ((3 + 100 − 1) × 50) = 10000/(102 × 50) = 10000/5100 = 1.96
```

**(d) Maximum speedup** — let n → ∞ and the (k − 1) becomes negligible:
**S → tₙ / tₚ = 100 / 50 = 2.**

Notice 1.67 → 1.96 → 2: **the more tasks, the closer to the ceiling**, because the fill cost
(k − 1 clocks) is amortised over more work.

★ **Why you never reach k** — state these; they are the "explain" half of the marks:

1. **Segments take different times.** The clock accommodates the **slowest**, so faster segments idle.
   Here 40 and 15 both wait for 50.
2. **The interface registers cost time** that the non-pipelined circuit never pays.
3. **tₙ = k·tₚ is generally false** — and S → k depends on it. Here tₙ = 100 but k·tₚ = 150.
4. **Hazards stall the pipeline** (step 8).

⚠ **Two delay conventions, and questions use both.** In this problem the register transfer time
(5 ns) is given **inside** a segment. In others (Mano 9-7, the FP adder) a register delay **tᵣ** is
stated separately and must be **added to the slowest segment**: tₚ = t_max + tᵣ. Read which convention
the question is using before computing — it changes the answer.

> ✓ **Check 5.** (a) Which segment sets the clock, and why that one? (b) Why does S rise from 1.67 to
> 1.96? (c) `[Mano 9-4]` A non-pipeline system takes 50 ns per task; a six-segment pipeline has a
> 10 ns clock. Speedup for 100 tasks, and the maximum?
> (d) `[Mano 9-7]` Four segments t₁ = 50, t₂ = 30, t₃ = 95, t₄ = 45 ns, tᵣ = 5 ns. How long for 100
> pairs — and how would you roughly halve it?

---

### 6 · The arithmetic pipeline

> **Q** *(the descriptive counterpart of step 5; the deck's own example)*
> **Explain the four segments of a floating-point adder pipeline.**
>
> *Two floating-point numbers cannot be added until one thing is true of them. Guess what.*

Their **exponents must match**. That single requirement generates the whole pipeline.

Inputs X = A × 2ᵃ and Y = B × 2ᵇ (A, B mantissas; a, b exponents):

| Segment | Suboperation | Mechanism |
|---|---|---|
| 1 | **Compare the exponents** | subtract them; the **larger** becomes the result's exponent |
| 2 | **Align the mantissas** | shift the **smaller-exponent** mantissa **right** by the difference |
| 3 | **Add or subtract the mantissas** | |
| 4 | **Normalize the result** | on overflow, shift the mantissa right and increment the exponent; on underflow, count leading zeros, shift left that many, subtract from the exponent |

Built from a comparator, a shifter, an adder/subtractor, an incrementer and a decrementer.

**The worked timing example — and it exists precisely to show why you don't get k:**
t₁ = 60, t₂ = 70, t₃ = 100, t₄ = 80 ns, with interface-register delay tᵣ = 10 ns.

```
 pipelined clock  tₚ = slowest segment + tᵣ = 100 + 10 = 110 ns
 non-pipelined    tₙ = 60 + 70 + 100 + 80 + 10          = 320 ns
 speedup          S  = 320 / 110                        ≈ 2.9      (not 4)
```

The segments are unequal: 60, 70 and 80 ns of work all wait on the 100 ns one.

> ✓ **Check 6.** (a) Why must exponents be compared first? (b) Which mantissa gets shifted, and in
> which direction? (c) Why is the speedup 2.9 rather than 4?

---

### 7 · The instruction pipeline — A2 Q15

> **Q** `[A2 Q15 · 10 marks]` **= Mano 9-11**
> **Consider the four instructions in the following program. Suppose the first instruction starts from
> step 1 in the four-segment pipeline. Specify what operations are performed in the four segments
> during step 4.**
> ```
> Load    R1 ← M[312]
> ADD     R2 ← R2 + M[313]
> INC     R3 ← R3 + 1
> STORE   M[314] ← R3
> ```
>
> *Draw the diagonal table before reading. The answer falls straight out of it.*

The **six general phases** of an instruction cycle are: fetch instruction · decode · calculate
effective address · fetch operands · execute · store result.

**Mano's four-segment pipeline** merges two pairs — decode with EA calculation, and execute with
store:

| Segment | Name | Job |
|---|---|---|
| 1 | **FI** | Fetch the Instruction from memory |
| 2 | **DA** | Decode the instruction **and** calculate the effective Address |
| 3 | **FO** | Fetch the Operand |
| 4 | **EX** | Execute the operation |

Up to four instructions are in flight at once. Now lay the four instructions on the diagonal:

| Instruction | 1 | 2 | 3 | **4** | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| 1 Load | FI | DA | FO | **EX** | | | |
| 2 ADD | | FI | DA | **FO** | EX | | |
| 3 INC | | | FI | **DA** | FO | EX | |
| 4 STORE | | | | **FI** | DA | FO | EX |

**The answer — during step 4:**

| Instruction | Segment | What it is doing |
|---|---|---|
| **Load R1 ← M[312]** | **EX** | executes — places the operand fetched from 312 into R1 |
| **ADD R2 ← R2 + M[313]** | **FO** | fetches the operand from memory location 313 |
| **INC R3 ← R3 + 1** | **DA** | decodes the instruction and calculates its effective address |
| **STORE M[314] ← R3** | **FI** | fetches the instruction from memory |

⚠ **Notice a structural hazard lurking here** and say so — it is free credit. At step 4, instruction 2
needs memory for its operand (**FO**) while instruction 4 needs memory for its instruction (**FI**).
With a single memory port those cannot both happen, and one must stall. That is step 8(a), and it is
the reason real machines split instruction and data memory.

**On a branch**, *"the pending operations in the last two segments are completed and all information
stored in the instruction buffer is deleted."* An interrupt empties the pipeline the same way.

> ✓ **Check 7.** (a) What do FI, DA, FO, EX stand for? (b) Which two of the six general phases are
> merged into DA? (c) At step 5, what is each instruction doing?

---

### 8 · Hazards — A2 Q14

> **Q** `[A2 Q14 · 10 marks]` **= Mano 9-10**
> **Explain four possible hardware schemes that can be used in an instruction pipeline in order to
> minimise the performance degradation caused by instruction branching.**
>
> *There are five well-known techniques. The question asks for four. Guess which one it excludes and
> why — the word "hardware" is doing the work.*

**Three classes of hazard.** Know the **cause, an example and the cure** for each — that is the shape
of the question.

#### (a) Structural hazards — resource conflicts

**Cause:** the hardware resources needed by overlapping instructions cannot all be met — something has
not been duplicated enough.

**Canonical example:** with **one memory port**, an instruction fetch (FI) and an operand fetch (FO)
cannot happen in the same clock — exactly what step 7 spotted at step 4.

```
 i      FI  DA  FO  EX
 i+1        FI  DA  FO  EX
 i+2            --  --  FI  DA  FO  EX      ← stalled two clocks
```

**Cures:** duplicate the resource — a **two-port memory**, or **separate instruction and data
memories**, which is **Harvard architecture** (file 01, step 2) arriving for a concrete reason.

#### (b) Data hazards — data-dependency conflicts

**Cause:** an instruction needs the result of a previous instruction that has not been written back yet.

```
ADD R1, R2, R3      ; R1 ← R2 + R3
SUB R4, R1, R5      ; needs R1 — but ADD hasn't written it back
```

**Cures:**

| Cure | Kind | Mechanism |
|---|---|---|
| **Hardware interlock** | HW | detects that a source is a pending destination and **stalls** until it is ready. Preserves order, costs time |
| **Forwarding (bypassing)** | HW | routes the value **straight from the ALU output to the next instruction's input**, bypassing the register file, so it is used a stage earlier than write-then-read allows. Costs multiplexers and detection logic |
| **Instruction scheduling / delayed load** | **SW** | the **compiler** reorders instructions (or inserts NOPs) so the dependent instruction is not adjacent |

**Delayed load, worked** — `a = b + c; d = e − f;`

```
   Unscheduled                 Scheduled (compiler reordered)
   LW  Rb, b                   LW  Rb, b
   LW  Rc, c                   LW  Rc, c
   ADD Ra, Rb, Rc   ← stalls   LW  Re, e      ← independent work moved into the gap
   SW  a,  Ra                  ADD Ra, Rb, Rc
   LW  Re, e                   LW  Rf, f
   LW  Rf, f                   SW  a,  Ra
   SUB Rd, Re, Rf              SUB Rd, Re, Rf
   SW  d,  Rd                  SW  d,  Rd
```

★ **Note what that is: a *compiler* fix to a *hardware* problem — the RISC philosophy in miniature**
(file 01, step 4).

#### (c) Control hazards — branch difficulties

**Cause:** the branch target is not known until the branch completes, so the pipeline does not know
what to fetch next.

**Five techniques, and only four of them are hardware** — which is the question's real test:

| Technique | Kind | Mechanism |
|---|---|---|
| **Prefetch target instruction** | **HW** | fetch **both** streams (taken and not-taken), keep both until the branch resolves, discard the wrong one |
| **Branch target buffer (BTB)** | **HW** | an **associative memory** in the fetch segment holding previously executed branch addresses with their targets (and the next few instructions). Hit → fetch from there; miss → fetch normally and update |
| **Loop buffer** | **HW** | a small very-high-speed register file holding an **entire loop**, so the loop runs with no further memory accesses |
| **Branch prediction** | **HW** | guess the outcome with additional logic and fetch speculatively; a correct guess removes the penalty |
| **Delayed branch** | **SW** | the **compiler** puts useful instructions after the branch in the "delay slot"; they execute regardless. Used in most RISC processors, NOPs if nothing useful exists |

**The four to give:** prefetch target instruction · branch target buffer · loop buffer · branch
prediction. **Delayed branch is the compiler's technique**, so it does not answer a question that says
*hardware* — mention it in one line as the software fifth and you have shown you know the difference.

**Pipeline interlock** is the general term for detecting a hazard and stalling until it clears.

> ✓ **Check 8.** (a) Name the three hazard classes with one-line causes. (b) Which branch technique is
> software, and why does that matter for A2 Q14? (c) What is forwarding, and what does it cost?
> (d) `[Mano 9-12 … 9-15]` Give an example program causing a data conflict; one using delayed load;
> one causing a branch penalty; one using delayed branch.

---

## Exam form

### The formulas — derive, then use

```
 total pipelined time  = (k + n − 1) · tₚ          k segments, n tasks
 non-pipelined time    = n · tₙ

 speedup   S = n·tₙ / ((k + n − 1)·tₚ)

 limits:   n → ∞           S → tₙ / tₚ
           and tₙ = k·tₚ   S → k          (the theoretical ceiling)
```

**Clock cycle:** tₚ = the **slowest segment**, plus tᵣ **if the question states a separate register
delay**. Check the convention.

### The tables to be able to draw

1. The **register-contents table** for a given expression (A2 Q11's shape).
2. The **diagonal segment table** for an instruction pipeline (A2 Q15's shape).
3. Flynn's **2 × 2**.
4. The **three hazard classes** — cause, example, cure.

### One-liners that earn marks

- Throughput ≠ latency; pipelining raises the first and slightly worsens the second.
- The first result appears after **k** clocks; one per clock thereafter.
- **MISD has no real implementation.**
- **Pipelining does not fit Flynn's classification.**
- Real speedup < k because segments are unequal, registers cost time, and hazards stall.
- Separate instruction and data memory = **Harvard**, and it cures the structural hazard.

---

## Attempt

1. `[A2 Q12 · 10]` — one line, get it exactly right.
2. `[A2 Q11 · 10]` — configuration **and** the full 8-row register table.
3. `[A2 Q13 · 10]` — all four parts. Show which segment sets the clock.
4. `[A2 Q15 · 10]` — draw the diagonal table, then read off step 4. Mention the structural hazard.
5. `[A2 Q14 · 10]` — four **hardware** schemes, plus one line on delayed branch being software.
6. `[Mano 9-4]` and `[Mano 9-7]` — the two most likely unasked numericals.
7. `[Mano 9-2]` the space-time diagram; `[Mano 9-12–9-15]` the four hazard examples.

---

## Traps

| Trap | Correction |
|---|---|
| "Pipelining makes each instruction faster" | It raises **throughput**; per-instruction latency slightly **increases** |
| Clock = total of all segment times | Clock = the **slowest** segment (+ tᵣ if stated separately) |
| Total time = n · tₚ | It is **(k + n − 1)·tₚ** — the pipeline must fill |
| Assuming S = k | k is a **ceiling** approached only as n → ∞ **and** tₙ = k·tₚ |
| Inventing an MISD example | There is none. Say so |
| Listing delayed branch as a hardware scheme | It is a **compiler** technique |
| One adder in A2 Q11's segment 2 | The two additions are independent — run them in parallel |
| Ignoring which delay convention the question uses | tᵣ inside the segment times, or added separately? It changes tₚ |
| Forgetting to mention the structural hazard in A2 Q15 | FI and FO both want memory at step 4 — free marks |

---

## Self-test

1. How many clocks for 50 tasks in a 4-segment pipeline?
2. Segment times 30, 80, 45, 60 ns with tᵣ = 10 ns. Give tₚ, tₙ and the maximum speedup.
3. Why is the speedup for 10 tasks lower than for 100?
4. Which Flynn class has no real machine, and which does not fit the scheme at all?
5. Name the hazard: `LW R1, 0(R2)` followed immediately by `ADD R3, R1, R4`. Give two cures, one
   hardware and one software.
6. In a four-segment pipeline, what is instruction 3 doing at step 5?
7. State the two conditions under which speedup equals k.

---
---

## Answers

**Check 1.** (a) **Throughput** = tasks finished per unit time; **latency** = time for one task start
to finish. (b) It now passes through an isolating register between every pair of segments, and each
register costs time. (c) Pipelining, parallelism, caching, vector processing.

**Check 2.** (a) **MISD**. (b) **One** — the single control unit broadcasts it to all processing
elements. (c) Flynn counts the **number of streams**; a pipeline has one of each and overlaps them in
**time**, an axis the taxonomy does not have.

**Check 3.** (a) An **interface register**. (b) Segment k+1's combinational logic would see segment k's
output changing as the next task flowed through — the stages would smear together. (c) An input
register followed by a combinational circuit.

**Check 4.** (a) **(k + n − 1)·tₚ**: **k** is the latency of the first task through all segments,
**n − 1** is one further result per clock. (b) 6 + 8 − 1 = **13 clocks**. (c) From clock 3 (when R7
first produces a result) to clock 6 — four clocks in which every segment holds live data.

**Check 5.** (a) **Segment 2**, at 50 ns (45 ns multiplier + 5 ns transfer into R3) — the clock must be
long enough for the slowest segment to finish. (b) Because the fill cost of (k − 1) = 2 extra clocks is
amortised over 100 tasks instead of 10. (c) S = (100 × 50)/((6 + 100 − 1) × 10) = 5000/1050 = **4.76**;
maximum = tₙ/tₚ = 50/10 = **5**. (d) tₚ = 95 + 5 = 100 ns, so (4 + 100 − 1) × 100 = **10,300 ns**. To
halve it, **split the 95 ns segment into two** of about 47.5 ns each: k becomes 5 and tₚ becomes
50 + 5 = 55 ns, giving (5 + 100 − 1) × 55 = **5,720 ns** ≈ half.

**Check 6.** (a) Two floating-point numbers can only be added once their exponents match, so the
difference must be known first. (b) The mantissa with the **smaller exponent**, shifted **right** by
the exponent difference. (c) The segments are unequal — 60, 70 and 80 ns of work all wait on the
100 ns segment, and tᵣ adds to every clock.

**Check 7.** (a) Fetch Instruction · Decode and calculate Address · Fetch Operand · Execute.
(b) **Decode** and **calculate effective address**. (c) Instruction 1 is finished; instruction 2 is in
**EX**, instruction 3 in **FO**, instruction 4 in **DA**.

**Check 8.** (a) **Structural** — two instructions need the same resource. **Data** — an instruction
needs a result not yet written back. **Control** — the branch target is unknown until the branch
resolves. (b) **Delayed branch** is software; the question says *hardware schemes*, so it is not one
of the four. (c) Routing a value directly from the ALU output to the next instruction's input,
bypassing the register file; it costs multiplexers and hazard-detection logic. (d) *Data conflict:*
`ADD R1,R2,R3` then `SUB R4,R1,R5`. *Delayed load:* move an independent `LW` between them.
*Branch penalty:* a conditional branch immediately followed by the instruction that would be
squashed. *Delayed branch:* put an instruction that must execute either way into the slot after the
branch.

**Self-test 1.** 4 + 50 − 1 = **53**.

**Self-test 2.** tₚ = slowest + tᵣ = 80 + 10 = **90 ns**; tₙ = 30 + 80 + 45 + 60 + 10 = **225 ns**;
maximum speedup = 225/90 = **2.5**.

**Self-test 3.** Because the (k − 1) clocks spent filling the pipeline are a larger fraction of a short
run than of a long one.

**Self-test 4.** **MISD** has no real machine; **pipelining** does not fit the scheme at all.

**Self-test 5.** A **data hazard** (specifically a load-use dependency). Hardware: **forwarding**, or a
hardware interlock that stalls. Software: **compiler scheduling / delayed load** — move an
independent instruction between them.

**Self-test 6.** Instruction 3 enters at step 3, so at step 5 it is in its third segment: **FO**.

**Self-test 7.** **n → ∞** (the fill cost becomes negligible) **and tₙ = k·tₚ** (the unpipelined unit
takes exactly as long as all k segments together).

---

## What to do next

Every unit is now covered. File 12 is the **mock paper** — 30 marks, MTE format, closed book, timed.
Do it only after you have worked the Attempt block of every file; it is a diagnostic, not a lesson.
