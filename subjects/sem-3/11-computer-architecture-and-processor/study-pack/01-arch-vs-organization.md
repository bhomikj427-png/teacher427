# 01 — Architecture vs Organization, Functional Units, von Neumann/Harvard, RISC/CISC

**U1, lectures L1–L2 · CO1.** Four comparison tables and one mechanism each. The cheapest marks in
the paper — and the easiest to lose by reciting a table you cannot justify.

---

## Map

```
   ARCHITECTURE  (what the machine does — the ISA, a contract)
        |
        |  one architecture, many organizations
        v
   ORGANIZATION  (how it is delivered — buses, adders, control logic)
        |
        +--> functional units: input | memory | ALU | output | control
        |
        +--> memory arrangement:  von Neumann (one memory)  vs  Harvard (two)
        |                              |
        |                              +--> the von Neumann bottleneck
        |
        +--> ISA philosophy:      CISC (complex, variable)  vs  RISC (simple, fixed)
```

Everything in this course is a walk down that ladder: ISA on top (U1, U7, U8), microarchitecture in
the middle (U1–U3), performance engineering underneath (U4–U6).

---

## Attempt first

1. Two chips run the same program at different speeds. Same architecture or different? Same
   organization or different?
2. Name the five functional units of a computer. Which two together are called "the processor"?
3. Why does a von Neumann machine have a bottleneck that a Harvard machine does not?
4. Your laptop is almost certainly x86, which is CISC. If RISC is better, why?
5. CISC usually uses microprogrammed control and RISC usually uses hardwired control. Give the reason
   — not the fact.
6. Defining the internal organization of a computer means fixing three things. What three?

---

## Method

### 1. Architecture vs organization — the professor's table

| | Computer **Architecture** | Computer **Organization** |
|---|---|---|
| Question answered | **What** the computer does | **How** it does it |
| Deals with | functional behaviour | structural relationship |
| Design level | high-level design issues | low-level design issues |
| Also called | **instruction set architecture (ISA)** | **microarchitecture** |
| Comprises | instruction sets, registers, data types, addressing modes | circuit design, peripherals, adders, buses, control logic |
| Order of design | comes **first** | comes **after** architecture is decided |

**The mechanism behind the table.** The ISA is a **contract** between hardware and software: the set
of promises a programmer may rely on. Organization is any implementation that keeps those promises.
That is what lets Intel ship an 8086 and a Core i9 that run the same binaries — and it is why
architecture comes first: you cannot implement a contract you have not written.

⚠ **The deck contains one weak row:** *"Architecture indicates its hardware. Organization indicates
its performance."* That is muddled — architecture is the *abstraction*, not the hardware, and
performance belongs to the organization **and** the fabrication technology. **Reproduce the
professor's table if asked** (it is the examined framing); do not reason from that row.

### 2. The five functional units

| Unit | Job | The detail worth writing |
|---|---|---|
| **Input** | accepts program & data | a keypress is translated to its binary code and sent to memory or processor |
| **Memory** | stores programs & data | **primary** (fast, electronic-speed, holds what is executing) vs **secondary/auxiliary** (large, cheap, slow). Organized so one **word** is stored or retrieved per basic operation. **RAM** = any location reached in a *short and fixed* time after its address is given |
| **ALU** | arithmetic & logic | operands are first brought **into processor registers**, then operated on — which is *why* register transfers, not memory operations, are the atoms of this course |
| **Output** | sends results out | printer, display |
| **Control** | coordinates everything | issues read/write signals, senses states, and issues **timing signals** — "signals that determine *when* a given action is to take place" |

**Processor = ALU + control.** CPU = processor + its registers.

**The bridge sentence from Digital Electronics into this course:** defining the internal organization
of a computer means fixing **(1) the set of registers and their functions, (2) the set of allowable
microoperations, (3) the control signals that initiate sequences of them.** Combinational and
sequential circuits are the low-level building blocks; this course is what you build *with* them.

### 3. von Neumann vs Harvard

| | **von Neumann** | **Harvard** |
|---|---|---|
| Memory | **one** memory holds instructions and data | **separate** instruction and data memories |
| Buses | one shared address+data path | two independent sets of address and data buses |
| Consequence | instruction fetch and data access **contend** for the one bus | both proceed **simultaneously** |
| Cost | simpler, cheaper, flexible (memory splits any way) | more pins, more silicon, fixed split |
| Where used | general-purpose machines (U2's Basic Computer is von Neumann) | DSPs, microcontrollers, and the **L1 cache level** of most modern CPUs |

**The von Neumann bottleneck.** Because one bus carries both streams, the system's maximum speed is
limited by **memory bandwidth**, not processor speed — the CPU outruns its memory and waits. This is
not a separate fact to memorize: it is the same trade as the common bus (share one path in time to
save wires, pay in contention), and it is *why* the structural hazard exists in U4 — one memory port,
two pipeline segments wanting it.

**The stored-program concept** (the reason von Neumann matters): instructions live in the same memory
as data, in the same binary form. A program can therefore be loaded, relocated, and even modified
like data — which is what makes a general-purpose computer general.

**Modified Harvard** — worth one line: most real CPUs are von Neumann in main memory but Harvard at
the cache level (split L1-instruction and L1-data caches), getting the bandwidth without committing
to a fixed memory split.

### 4. RISC vs CISC

| | **CISC** | **RISC** |
|---|---|---|
| Instruction count / complexity | many, complex, multi-step | few, simple, one job each |
| Instruction length | **variable** (8086: 1–6 bytes) | **fixed** (RISC-V: 32 bits) |
| Memory operands | most instructions may touch memory | **load/store only** — arithmetic is register-to-register |
| Registers | few, special-purpose | many, general-purpose (RISC-V: 32) |
| Addressing modes | many (8086: ~12) | few |
| Control unit | usually **microprogrammed** | usually **hardwired** |
| Cycles per instruction | variable, often many | ~1, pipelined |
| Complexity lives in | the **hardware** | the **compiler** |

**Why the pendulum swung.** CISC made sense when memory was scarce and expensive and people wrote
assembly: a dense, powerful instruction saved precious bytes, and microprogramming made a rich
instruction set cheap to build. When memory got cheap and compilers got good, the calculus inverted —
what matters now is how fast you can **pipeline**, and you can only pipeline cleanly if instructions
are uniform in length, take uniform time, and touch memory in one predictable place.

That is also the answer to "why hardwired for RISC": a small, uniform instruction set makes the D·T
equations simple enough to wire directly, and the control memory access that microprogramming needs
would sit in the critical path of a machine whose whole selling point is one instruction per cycle.

---

## Worked — "Distinguish computer architecture from organization" (inferred form F1; the deck gives this table verbatim)

A 4-mark answer has three parts. Most answers have one.

**(i) The definitions, in one line each.**
Architecture = the attributes visible to a programmer — instruction set, registers, data types,
addressing modes. Organization = the operational units and their interconnections that realize the
architecture — buses, adders, control logic, timing.

**(ii) The table.** Four to six rows from §1 above. Rows, not prose — it reads as a comparison and
marks faster.

**(iii) The discriminating example — this is the part that separates a 4 from a 2.**

> The Intel 8086 and the Core i9 share an architecture: a binary compiled for one runs on the other,
> because both keep the same contract (same instructions, same register names, same addressing
> modes). Their organizations are unrecognizably different — the i9 has caches, pipelines,
> out-of-order execution and multiple cores, none of which the 8086 had. **One architecture, many
> organizations.**

The exam's test of whether you understand the split is exactly the question in Attempt 1: two chips,
same program, different speeds → **same architecture, different organization**. Speed is not part of
the contract.

---

## Worked — "Compare von Neumann and Harvard" (inferred form F2)

**(i) Structure.**

```
   von Neumann                         Harvard

   +---------+                         +---------+   +---------+
   | MEMORY  |  instructions + data    | INSTR   |   |  DATA   |
   | (one)   |                         | MEMORY  |   | MEMORY  |
   +----+----+                         +----+----+   +----+----+
        |  one bus                          | bus 1       | bus 2
   +----+----+                         +----+-------------+----+
   |   CPU   |                         |          CPU          |
   +---------+                         +-----------------------+
```

**(ii) The consequence, stated as a mechanism.** In the von Neumann machine the CPU cannot fetch an
instruction and read an operand in the same cycle — the one bus serializes them. In the Harvard
machine it can, because there are two independent paths.

**(iii) The honest closing line.** Harvard is better for bandwidth and for safety (data cannot be
fetched as instructions); von Neumann is better for flexibility (memory can be divided between code
and data any way a program needs). **Modern machines cheat by being both** — von Neumann in main
memory, Harvard at L1 cache.

---

## Traps

| # | Trap | The correction |
|---|---|---|
| M1 | "Architecture is the hardware; organization is the performance" — the deck's own weak row | Architecture is the **abstraction/contract**; performance belongs to the organization and the technology |
| M3 | "CISC is obsolete; RISC won" | x86 is CISC and dominates desktops and servers. Modern x86 **decodes CISC instructions into RISC-like micro-operations** internally: CISC architecture, RISC-ish organization. What RISC won is the *argument*, not the market |
| M4 | "A bus is just a wire" / "buses make things faster" | A bus is a **shared, time-multiplexed path** adopted to avoid O(n²) interconnect. It trades **simultaneity** away to save wires. It makes a system buildable, not faster |
| — | Listing four functional units and forgetting **control** | Control is the one that issues **timing** signals; without it the other four never start |
| — | Saying Harvard is "just better" | It is better for bandwidth and safety, worse for flexibility. Say the trade, not a verdict |

---

## Self-test

1. Give four rows of the architecture-vs-organization table, then name one thing that is arguably
   *both* and say why.
2. "RAM" is defined by a property, not by a technology. What property?
3. Why must operands be brought into processor registers before the ALU acts on them? What does that
   fact set up for the rest of the course?
4. A DSP chip fetches an instruction and two operands in the same clock cycle. What memory
   architecture does it use, and what did it give up to do that?
5. State the von Neumann bottleneck in one sentence, then name the U4 phenomenon that is the same
   problem in a different place.
6. Fill in the missing cells: CISC instruction length is ___ ; RISC arithmetic instructions may touch
   memory: ___ ; complexity in RISC lives in the ___ .
7. Why does a rich, complex instruction set push a designer toward microprogrammed control?
8. Your phone's CPU is ARM (RISC), your laptop is x86 (CISC), and both run comparable software at
   comparable speeds. What does that tell you about the RISC/CISC distinction as a *predictor of
   performance*?

---

## Answers

**1.** Any four rows from §1 (what vs how · functional behaviour vs structural relationship · ISA vs
microarchitecture · instruction sets/registers/addressing modes vs adders/buses/control logic · high
vs low level · designed first vs designed after).
*Arguably both:* **cache size** — classified as organization, but architecturally observable through
timing (which is how side-channel attacks like Spectre work), so anything a program can measure has
leaked into the contract. **Pipeline depth** is another: MIPS made it architectural by exposing a
branch delay slot.

**2.** Any location can be reached in a **short and fixed time** once its address is given — access
time is independent of *which* address. (Contrast a disk or a tape, where position matters.)

**3.** Because the ALU has no path to memory; it reads its inputs from registers and writes its
output to a register. That is why the atomic unit of this course is the **register transfer** (a
microoperation), not "an operation on a memory location" — and it is why RTL, not pseudocode, is the
notation of U1–U3.

**4.** **Harvard** (separate instruction and data memories with independent buses). It gave up
flexibility — the code/data split is fixed in hardware — and paid in pins and silicon area.

**5.** Because instructions and data share one memory and one bus, system speed is capped by
**memory bandwidth** rather than processor speed, so the CPU stalls waiting for memory.
The U4 counterpart is the **structural hazard**: with a single memory port, an instruction fetch (FI)
and an operand fetch (FO) collide in the same clock and one must stall. Same cause, later chapter.

**6.** variable (1–6 bytes on the 8086) · **no** — RISC is load/store only, arithmetic is
register-to-register · the **compiler**.

**7.** Because hardwired control hard-codes each instruction's D·T equations in gates. With many
complex, irregular instructions that logic becomes a tangle of special cases, and any ISA change
forces a re-derivation and a rewiring. Microprogramming turns the problem into a **lookup**: each
instruction gets a routine in control memory, so adding an instruction means writing more firmware,
not redesigning silicon. The cost is a control-memory read per microinstruction.

**8.** That it is an **ISA-level** distinction, not a performance prediction. Performance is decided
by organization and process technology — pipelining, caches, issue width, fabrication node. The
useful modern question is not "RISC or CISC?" but "**fixed-length and load-store, or not?**", because
that is what determines how cleanly the thing can be pipelined.
