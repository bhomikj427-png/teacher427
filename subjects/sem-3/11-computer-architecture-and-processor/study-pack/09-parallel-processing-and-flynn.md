# 09 — Parallel Processing and Flynn's Classification

**U4, lecture L16 · CO3 · ⚠ practitioner-delivered (marked `*` in the hand-out).** One lecture, so
expect **descriptive / short-answer** treatment rather than a derivation. Cheap marks if the tables
are clean — and one question (why pipelining does not fit Flynn) that most students cannot answer.

---

## Map

```
   THROUGHPUT = work finished per unit time         (NOT latency)
        |
        +-- raised by:  pipelining | parallelism | caching | vector processing
        |               ...often at the cost of slightly higher per-task latency
        v
   PARALLEL PROCESSING = concurrent events, for speed
        |
        +-- levels: job | task/procedure | inter-instruction | intra-instruction
        |
        v
   FLYNN: count the INSTRUCTION streams and the DATA streams
        |
        +-- SISD  one/one     the classic von Neumann machine
        +-- SIMD  one/many    array | systolic | associative processors
        +-- MISD  many/one    NO REAL MACHINE EXISTS
        +-- MIMD  many/many   shared-memory multiprocessor | message-passing multicomputer
        |
        v
   ...and pipelining fits NONE of the four boxes
```

---

## Attempt first

1. Define throughput. Now define latency. Which one does pipelining improve, and what happens to the
   other?
2. Name the four techniques architects use to raise throughput.
3. Give Flynn's 2×2 table and one real example system per class.
4. Which Flynn class has **no** real example, and what should you write when asked for one?
5. In a SIMD machine, how many copies of the program exist?
6. Name the two MIMD families and the single biggest limitation of each.
7. Why does pipelining not fit Flynn's classification?

---

## Method

### Throughput — the quantity being bought

**Throughput** = the amount of processing accomplished in a given interval of time.

| Kind | Measured as |
|---|---|
| **Instruction throughput** | instructions per second, or via **CPI** (cycles per instruction) |
| **Data / memory throughput** | GB/s or MB/s — how fast data moves between storage, memory and cache |

**The four techniques, with what each actually does:**

| Technique | Mechanism |
|---|---|
| **Pipelining** | break instructions into steps so several overlap in execution |
| **Parallelism** | add execution units or cores to run different tasks concurrently |
| **Caching** | keep hot data in small ultra-fast memory near the CPU |
| **Vector processing** | one instruction operates on a whole dataset (**SIMD**) |

**★ The framing sentence to keep, verbatim in spirit:** architects raise throughput *"often at the
expense of slight increases in individual task latency."*

> **Throughput ≠ latency.** A pipelined instruction takes *more* total time than an unpipelined one
> (it now pays a register delay between every stage) — but the machine finishes far more of them per
> second.

A student who conflates the two cannot answer "does pipelining make a program faster?" correctly.
(The honest answer: it makes the *machine* finish more work per second; any single instruction takes
slightly longer.)

### Parallel processing

**Definition:** *"execution of concurrent events in the computing process to achieve faster
computational speed."*

**Levels of parallelism**, coarse → fine:

```
   job / program level
        -> task / procedure level
             -> inter-instruction level
                  -> intra-instruction level
```

**Applications** (one line is enough for a descriptive answer): numerical weather forecasting,
computational aerodynamics, finite-element analysis, remote sensing, genetic engineering,
computer-assisted tomography, defence research.

**Cost:** the amount of hardware increases with parallel processing, and with it the cost.
**Parallelism is never free** — say this, because "more parallel is better" is the naive answer.

### Flynn's classification

M. J. Flynn classified computers by the **multiplicity of instruction streams and data streams**.

- **Instruction stream** = the sequence of instructions read from memory.
- **Data stream** = the operations performed on the data in the processor.

| | **Single Data** | **Multiple Data** |
|---|---|---|
| **Single Instruction** | **SISD** | **SIMD** |
| **Multiple Instruction** | **MISD** | **MIMD** |

**SISD** — one control unit, one processor unit, one memory. The standard von Neumann machine;
instructions execute sequentially. Any parallelism comes from **multiple functional units or
pipelining** *inside* it.

- *Limitation:* the **von Neumann bottleneck** — maximum speed limited by **memory bandwidth**, and
  memory is shared by CPU and I/O.
- *Ways to improve a SISD machine:* multiprogramming · spooling · multifunction processor ·
  pipelining · instruction-level parallelism (**superscalar**, **superpipelining**, **VLIW**).

**SIMD** — many processing elements under **one** control unit. **Only one copy of the program
exists**; the single controller broadcasts one instruction at a time and all active PEs execute it on
**different data**. Shared memory must be multi-module to feed them all.

| Type | What it is | Examples |
|---|---|---|
| **Array processors** | a grid of PEs under one controller | ILLIAC IV, Connection Machine, DAP, MPP |
| **Systolic arrays** | regular VLSI grids of very simple processors, data pumped through | CMU Warp, Purdue CHiP |
| **Associative processors** | content addressing rather than address addressing | STARAN, PEPE |

**MISD** — many instruction streams, one data stream.

> **"There is no computer at present that can be classified as MISD."** It is of theoretical interest
> only.

Write exactly that. **Do not invent an example** — this is a question designed to see whether you
will.

**MIMD** — multiple processing units executing multiple instructions on multiple data. Two families:

| | **Shared-memory multiprocessor** | **Message-passing multicomputer** |
|---|---|---|
| Memory | all processors have equally direct access to **one large address space** | **each processor has its own memory** |
| Communication | through shared memory | by **passing messages** |
| Examples | bus/cache-based (Sequent Balance, Encore Multimax); multistage-network (Ultracomputer, Butterfly, RP3, HEP); crossbar (C.mmp, Alliant FX/8) | tree (Teradata, DADO); mesh (Rediflow, J-Machine); hypercube (Cosmic Cube, iPSC, NCUBE, FPS T-series, Mark III) |
| Limitations | **memory access latency**; the **hot-spot problem** | **communication overhead**; hard to program |

### ★ The limitation of Flynn's taxonomy

**Pipelining does not fit Flynn's classification.** Flynn distinguishes by the *number* of streams; a
pipeline has **one of each** — one instruction stream, one data stream — but **overlaps them in
time**. Concurrency in time is invisible to a taxonomy that counts streams.

This is a genuine limitation of the scheme and an excellent short-answer question, because it shows
whether you understand *what Flynn is measuring* rather than having memorized four boxes.

---

## Worked — classify a set of machines (inferred form F17; classes and examples from the deck)

> **Classify each of the following under Flynn's scheme and justify in one line: (a) a single-core
> desktop CPU with a 5-stage pipeline, (b) a GPU running one shader program over a million pixels,
> (c) a 64-node cluster with one program per node and an interconnect for messages, (d) a fault-
> tolerant avionics box where three processors run different algorithms on the same sensor reading.**

**The method — always answer two questions in this order:**

```
   1. How many INSTRUCTION streams are being fetched and decoded at once?
   2. How many DATA streams are being operated on at once?
```

**(a) SISD.** One instruction stream, one data stream. **The pipeline does not change the
classification** — that is the point of the taxonomy's limitation. The pipeline overlaps the *stages*
of consecutive instructions; there is still exactly one stream of each.

**(b) SIMD.** One program, broadcast to many processing elements, each operating on different data
(different pixels). A GPU is the modern mass-market SIMD machine.

⚠ **State the caveat if you have room:** GPU vendors call this model **SIMT** (single instruction,
multiple *threads*) because each element has its own program counter and can diverge on a branch.
Flynn's 1966 scheme predates it and does not have a box for it — the honest answer is "SIMD in
Flynn's terms, SIMT in the manufacturer's."

**(c) MIMD, message-passing multicomputer.** Multiple instruction streams (one per node), multiple
data streams, **no shared address space** — nodes communicate by passing messages. Limitation to
state: communication overhead, and the difficulty of programming it.

**(d) This is the classic MISD candidate, and the honest answer is that it is not a real MISD
machine.** Three instruction streams over one data stream is the *definition*, and fault-tolerant
redundant systems are the usual example people reach for — but the standard position is that **no
extant computer is classified MISD**, because the three processors are independent machines fed the
same input rather than one machine with multiple instruction streams over a shared data stream.
**Saying this, with the reason, is a better answer than either inventing an example or writing
nothing.**

---

## Worked — throughput versus latency (inferred form; the framing is the deck's)

> **A 4-stage pipeline is added to a processor. Each stage takes 20 ns and the interface registers
> add 2 ns per stage. Before pipelining, one instruction took 80 ns end-to-end. Discuss the effect on
> throughput and on latency.**

**Latency — the time for one instruction:**

```
   before:  80 ns
   after:   4 stages x (20 + 2) = 88 ns
```

**Latency got WORSE by 8 ns** — the register delays are pure overhead that the unpipelined circuit
never paid.

**Throughput — instructions finished per second, once the pipeline is full:**

```
   before:  one every 80 ns   ->  12.5 million/s
   after:   one every 22 ns   ->  45.5 million/s
```

**Throughput improved 3.6×.**

**The sentence that carries the mark:**

> Pipelining did not make any instruction faster — it made each one slightly slower. It made the
> machine **finish more of them per second**, by having four instructions in flight at once. The
> gain is in throughput and it is **paid for in latency**, which is exactly the trade architects
> accept.

**The follow-up you should expect:** *"then why does my program run faster?"* Because a program is
thousands of instructions, and what a program's runtime depends on is throughput, not the latency of
any single instruction. The exception matters though — a program that is one long chain of dependent
instructions gets no overlap, and for it the pipeline is a **net loss**.

---

## Traps

| # | Trap | The correction |
|---|---|---|
| M12 | "Pipelining makes each instruction faster" | It raises **throughput** and typically **increases** single-instruction latency (the interface registers) |
| T10 | Inventing an MISD example | "There is no computer at present that can be classified as MISD." State it plainly |
| — | "SIMD machines run many copies of the program" | **One** copy. One control unit broadcasts one instruction; the PEs differ only in their data |
| — | Confusing the two MIMD families | Shared-memory = one address space, limited by **memory latency** and **hot spots**. Message-passing = private memories, limited by **communication overhead** |
| — | Classifying a pipelined CPU as something other than SISD | A pipeline has one instruction stream and one data stream. Flynn counts streams, not overlap |
| — | "More parallelism is always better" | Hardware cost — and therefore price and power — grows with it. Parallelism is never free |
| — | Listing Flynn's classes without examples | The examples are half the marks in a descriptive question |

---

## Self-test

1. Define instruction throughput two different ways (one rate, one ratio).
2. Give the four techniques for raising throughput and say which of them **also** reduces latency for
   a single access. Justify.
3. Draw Flynn's 2×2 and fill in all four names, with one example machine each where one exists.
4. A machine has one control unit broadcasting to 1024 processing elements. How many programs are in
   memory, and what must be true of the memory system?
5. Name the three types of SIMD machine and give one example of each.
6. State the von Neumann bottleneck and list four ways a SISD machine can be improved despite it.
7. Why is pipelining not classifiable under Flynn? Answer in terms of what Flynn measures.
8. A vendor claims their 64-core chip is "64× faster". Give two independent reasons to doubt it,
   one from this file and one from the next.

---

## Answers

**1.** As a **rate**: instructions completed per second (e.g. MIPS, or instructions/clock × clock
frequency). As a **ratio**: via **CPI** — cycles per instruction — where throughput is inversely
proportional to CPI for a fixed clock. Both describe *work finished per unit time*, which is the
definition.

**2.** Pipelining · parallelism · caching · vector processing.
**Caching** is the one that also reduces **latency**: a hit returns the data in a few cycles instead
of the tens or hundreds a main-memory access costs, so the individual access genuinely finishes
sooner. Pipelining and parallelism raise throughput while leaving single-task latency unchanged or
slightly worse; vector processing raises throughput by amortizing one instruction over many data
elements.

**3.**

| | Single Data | Multiple Data |
|---|---|---|
| **Single Instruction** | **SISD** — a conventional uniprocessor (any classic von Neumann machine) | **SIMD** — ILLIAC IV, Connection Machine, DAP, MPP |
| **Multiple Instruction** | **MISD** — **no extant example** | **MIMD** — Sequent Balance, Encore Multimax, Cosmic Cube, NCUBE, C.mmp |

**4.** **One** program. A SIMD machine holds a single copy of the program, executed by one control
unit which broadcasts each instruction to all active PEs. The memory system must be **multi-module**
(banked), so that 1024 elements can be supplied with their different operands concurrently — a single
memory port would serialize them and destroy the parallelism.

**5.** **Array processors** (ILLIAC IV, Connection Machine, DAP, MPP) · **systolic arrays** (CMU Warp,
Purdue CHiP) · **associative processors** (STARAN, PEPE).

**6.** *The bottleneck:* because instructions and data share one memory and one bus, the system's
maximum speed is limited by **memory bandwidth** rather than processor speed, and the memory is
shared with I/O as well.
*Four improvements:* multiprogramming · spooling · a multifunction processor · pipelining · or
instruction-level parallelism (superscalar, superpipelining, VLIW) — any four.

**7.** Because Flynn classifies by **how many instruction streams and data streams exist**, and a
pipelined machine has exactly **one of each**. Its concurrency is in **time** — overlapping different
*phases* of consecutive instructions — not in the multiplicity of streams. A taxonomy that counts
streams is blind to overlap, so pipelining falls outside all four boxes. (The same blindness is why
GPUs need the extra term SIMT.)

**8.** *From this file:* throughput is not latency and **parallelism is not free** — 64 cores raise
the work finished per second only for workloads that actually decompose into 64 independent pieces;
a serial program sees roughly one core's performance, and the hardware cost/power went up regardless.
*From file 10:* the same ceiling argument as pipeline speedup — the achievable gain is bounded by the
fraction of the work that can be parallelized (and by memory bandwidth, hot spots and communication
overhead), so the measured speedup is always below the nominal factor, exactly as a k-stage pipeline
never reaches k.
