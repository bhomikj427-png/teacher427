# 01 — Foundations

**Assignment 1: Q1–Q6, Q20 · 76 of 200 marks · U1 (L1–L2) · needs 00**

This file is built on **six real questions**, and between them they *are* the whole 76-mark foundations
block of Assignment 1. Nothing here is invented and nothing here is optional.

> ⚠ **Where P2 is empty, and why the file says so.**
> Mano contributes **no questions to this file**. His book opens at digital logic and has no
> end-of-chapter problem on architecture-vs-organization, von Neumann vs Harvard, generations, or
> types of computers — he does not cover those topics at all. The professor got this material from
> elsewhere (Hamacher and his own slides). So for foundations, **P1 is the entire question base**, and
> that is a fact about the syllabus, not a gap in this pack. Mano's questions start at file 02 and
> take over from file 03 onward. Don't go looking for Mano problems here; there are none.

---

## The questions this file answers

| # | Question | Marks |
|---|---|---|
| 1 | `[A1 Q4]` List the various elements that constitute a computer? Explain the roles and responsibility of each element. | 10 |
| 2 | `[A1 Q6]` Describe the features of the Von Neumann architecture. Compare & contrast Von Neumann and Harvard architecture. | 10 |
| 3 | `[A1 Q2]` What distinguishes computer organization from computer architecture? | 4 |
| 3b | `[A1 Q1(ii)–(vi)]` Define: Computer Architecture · Computer Organization · Microarchitecture · Microoperations · Register Transfer Language | 10 |
| 4 | `[A1 Q20]` Write short note on: (i) RISC architecture (ii) CISC architecture | 20 |
| 5 | `[A1 Q3]` Briefly explain about the different generations of computers. Tabulate & highlight the significant technological contributions & human contributors of each generation. | 10 |
| 6 | `[A1 Q5]` In how many ways are computers divided? Distinguish between each type of computers. | 10 |

`[A1 Q1(i)]` — *Define: Digital Computer* — was answered in file 00, step 1. Six definitions, 12 marks,
and you already have one of them.

**Word limit, and it is enforced: 1 mark = 20 words.** 2 marks ≤ 40 words · 10 marks ≤ 200 words.

---

## Map

```
   [1] The five functional units ──────► [2] Where program and data live
    │                                        von Neumann vs Harvard
    ▼
   [3] Architecture vs organization ──► [4] How big the instruction list is
       + microarchitecture, RTL              RISC vs CISC
    │
   [5] How the hardware evolved        [6] How computers are classified
       5 generations                       3 axes
```

---

## Build

### 1 · The five functional units

> **Q** `[A1 Q4 · 10 marks]`
> **List the various elements that constitute a computer? Explain the roles and responsibility of
> each element.**
>
> *Guess first — how many parts, and what are they? Write your list on paper. Then read on.*

Almost everyone writes "CPU, RAM, hard disk, keyboard, monitor" — a list of *components you can buy*.
The examiner wants the five **functional units**, which is a different list, and the word
"responsibility" in the question is the hint: he wants a *job* attached to each.

Typing `3 + 5` and seeing `8` uses every one:

```
            ┌──────────── Processor ────────────┐
 Input ───► │   ALU  (arithmetic & logic)       │ ───► Output
 keyboard   │   Control (sequences every step)  │      screen
            └────────────────┬──────────────────┘
                             │  bus (shared wires)
                          Memory
                  holds program + data
```

| Unit | Job | In the 3 + 5 program from file 00 |
|---|---|---|
| **Input** | turns outside data into bits | keys `3`, `5` → binary |
| **Memory** | stores program **and** data | M[200] = 3, M[201] = 5, program at 100 |
| **ALU** | arithmetic and logic on register values | AC + 5 → 8 |
| **Control** | tells each unit what to do and **when** (the timing signals T₀, T₁, … from file 00 step 7) | fetch, then load, then add, then store |
| **Output** | turns bits back into something readable | `8` on screen |

**Processor = ALU + Control.** The units are joined by a **bus** — one shared set of wires (file 03).

Memory has two levels:
**primary** — electronic, fast, holds the running program (RAM: any address reached in the same short time) ·
**secondary** — disks: large, cheap, slow, keeps data when power is off.

> ✓ **Check 1.** (a) Which unit decides *when* AC loads a new value?
> (b) Why is the processor counted as two units, not one?
> (c) The question says "roles and responsibility" — what does that tell you the answer must contain
> besides the list?

---

### 2 · Where program and data live: von Neumann vs Harvard

> **Q** `[A1 Q6 · 10 marks]`
> **Describe the features of the Von Neumann architecture. Compare & contrast Von Neumann and
> Harvard architecture.**
>
> *One chef has one door to the storeroom, for both recipe cards and ingredients. Guess what slows
> the kitchen down. Then read on.*

In file 00's program, instructions (100–102) and data (200–202) sat in **one memory**, as the same kind
of 16-bit word, and nothing marked which was which. That is the **stored-program concept**, published
by John von Neumann in 1945 (the EDVAC report).

**von Neumann architecture** = one memory for instructions and data, one path (bus) to the processor.

Consequence — the **von Neumann bottleneck**:
fetching an instruction and reading data both need the one path, so they take turns.
The processor can work faster than that path delivers words, and then it **waits**.
System speed is limited by the memory path, not by the processor. *(That is the chef's one door.)*

**Harvard architecture** = two separate memories — one for instructions, one for data — each with its
own path. An instruction fetch and a data read happen **at the same time**. The cost: twice the wiring,
and a fixed split of memory you cannot re-balance.

```
 von Neumann                          Harvard
 ┌─────────┐   one bus  ┌────────┐    ┌─────────┐       ┌───────────┐
 │Processor│◄──────────►│ Memory │    │         │◄─────►│Instruction│
 └─────────┘            │ instr. │    │Processor│       │  memory   │
                        │ + data │    │         │◄─────►│Data memory│
                        └────────┘    └─────────┘       └───────────┘
```

Where each is used: von Neumann — general-purpose computers (the Basic Computer is one).
Harvard — DSPs, microcontrollers, and the split instruction/data **cache** inside modern CPUs.

**The word "features" in the question is scored separately from the comparison.** Features of von
Neumann: stored program · one memory, same binary form for instructions and data · one bus ·
sequential fetch–execute driven by the PC · the five functional units. Then the table.

> ✓ **Check 2.** (a) A chip reads its next instruction and a data byte in the same clock tick.
> Which architecture? (b) State the bottleneck in one sentence, with its cause.
> (c) Is Harvard obsolete?

---

### 3 · Architecture vs organization

> **Q** `[A1 Q2 · 4 marks]`
> **What distinguishes computer organization from computer architecture?**
>
> **and** `[A1 Q1(ii)–(vi) · 2 marks each]`
> **Define: Computer Architecture · Computer Organization · Microarchitecture · Microoperations ·
> Register Transfer Language**
>
> *Guess the difference in one line before reading. Most first guesses are "architecture is hardware,
> organization is software" — if that was yours, note it down, because it is the trap this question
> is built to catch.*

It is **not** hardware vs software. Both are hardware. The split is *visible to the programmer* vs
*not visible*.

A programmer writing for the Basic Computer needs to know only:

- **instruction set** — the list of instructions it understands (LDA, ADD, STA, …) and their bit format
- **registers** it can use — AC, PC
- **data types** — how bits are read: e.g. a 16-bit word as a signed integer
- **addressing modes** — how the address field finds the operand.
  *Direct*: `ADD 201` uses M[201]. *Indirect* (I = 1): M[201] holds the address of the operand — this is
  the `932E` case you met in file 00, Check 9.

That list is the **computer architecture**, also called the **instruction set architecture (ISA)**.
It is a **contract**: any machine that honours it runs the same programs.

**Computer organization** is the hardware that honours the contract — how the adder is built, how
registers connect to the bus, which memory chips, what control circuits. The programmer never sees it.

Same contract, different hardware:

| | Machine X | Machine Y |
|---|---|---|
| Runs `2200 1201 3202`? | yes, M[202] = 8 | yes, M[202] = 8 |
| Adder | slow ripple adder | fast adder |
| Speed | 1× | 10× |
| Difference is in | — | **organization** |

Real case: Intel's 8086 (1978) and a Core i9 run the same x86 programs. IBM System/360 (1964) sold one
architecture across machines differing 50:1 in performance.

Architecture is decided **first** — hardware cannot implement a contract not yet written.

That settles Q2 and two of the definitions. The other three:

**Microarchitecture** = another name for organization: the specific hardware implementation of a given ISA.

**Microoperation** — one elementary operation on register data, done in **one clock tick**
(file 00, step 7). `ADD 201` is *not* one step inside the machine. It runs as microoperations: read
M[201] into a data register DR, then add DR into AC. This is the same fact as file 00 Check 6(b).

**Register transfer language (RTL)** — the notation that writes microoperations exactly:

```
DR ← M[AR]         copy the memory word at address AR into DR
AC ← AC + DR       add DR into AC
P: R2 ← R1         copy R1 into R2, only when control signal P = 1
```

You have been reading RTL since file 00 step 5. **A definition of RTL without an example scores badly** —
always include one.

> ✓ **Check 3.** (a) A company makes its adder faster but keeps every instruction identical.
> Architecture or organization change? (b) A new instruction MUL is added. Which one changed?
> (c) Why can `ADD 201` not be a single microoperation?
> (d) Write, in RTL: copy R1 into R3 only when control signal T = 1.

---

### 4 · How big the instruction list is: RISC vs CISC

> **Q** `[A1 Q20 · 10 + 10 = 20 marks]`
> **Write short note on the following: (i) RISC architecture (ii) CISC architecture.**
>
> *20 marks — the single biggest item in Assignment 1. Guess what R and C stand for, then read on.*

Task: `M[202] ← M[200] × M[201]`. Two ways to design the instruction set (illustrative instructions, not
a real ISA):

```
 CISC — one complex instruction          RISC — simple instructions only
   MULT 200, 201, 202                      LOAD  R1, 200
                                           LOAD  R2, 201
                                           MUL   R1, R2        (register-to-register)
                                           STORE R1, 202
```

**CISC** (complex instruction set computer) — many instructions, some doing load + compute + store in
one. Short programs. The hardware must handle instructions of different lengths and step counts.

**RISC** (reduced instruction set computer) — few, simple instructions, all the **same length**.
**Only LOAD and STORE touch memory** (*load/store*); arithmetic works on registers, so RISC gives many
registers. Programs are longer; the **compiler** does the work of splitting tasks up.

Why RISC wins speed: identical, simple instructions let the processor run them like an **assembly line**
— start the next instruction before the last one finishes (**pipelining**, U4). Uneven CISC instructions
jam that line.

**Control unit** — the part that generates the step-by-step control signals:
**hardwired** = fixed logic gates, fast (usual in RISC) ·
**microprogrammed** = the steps stored as a small program in a ROM, easy to extend to many instructions
(usual in CISC; U3).

Why CISC existed: memory was expensive and programs were hand-written, so dense instructions saved
memory. Memory got cheap and compilers got good → RISC.
Today's x86 is CISC to the programmer but internally splits each instruction into RISC-like steps.

Examples: **CISC** — Intel x86, VAX. **RISC** — ARM, RISC-V, MIPS.

**A "short note" at 10 marks is ≤ 200 words and wants five things:** definition · features · why it
exists · its cost · examples. Not a paragraph of opinion.

> ✓ **Check 4.** (a) What does *load/store* mean? (b) Why does fixed instruction length help pipelining?
> (c) Which design puts the complexity in the compiler? (d) Is RISC always faster?

---

### 5 · Generations: the switching device

> **Q** `[A1 Q3 · 10 marks]`
> **Briefly explain about the different generations of computers. Tabulate & highlight the significant
> technological contributions & human contributors of each generation.**
>
> *Guess what changes from one generation to the next — the single thing that defines the boundary.
> Then read on.*

A processor is a huge number of switches (file 00, step 1). Each generation is defined by **what the
switch is made of**. Note the two words the question puts in bold-able positions: *tabulate* (he wants a
table, not prose) and *contributors* (he wants names — most answers drop these and lose marks).

| Gen | ≈ Period | The switch | What it changed | Landmarks | People |
|---|---|---|---|---|---|
| 1 | 1945–1956 | **vacuum tube** — glass bulb; big, hot, fails often | machine language; drum memory | ENIAC (1945, 18,000+ tubes); EDVAC report (1945); Manchester Baby ran the first stored program (1948); UNIVAC I (1951) | Eckert & Mauchly; von Neumann |
| 2 | 1956–1964 | **transistor** — solid, small, cool, reliable | core memory; assembly, FORTRAN (1957) | TX-0 (1956); IBM 7090 | Bardeen, Brattain, Shockley (transistor, 1947); Backus (FORTRAN) |
| 3 | 1964–1971 | **integrated circuit (IC)** — many transistors on one chip | operating systems, multiprogramming | IBM System/360 (1964) | Kilby (IC, 1958); Noyce (planar IC, 1959) |
| 4 | 1971–1980s | **LSI/VLSI** — a whole processor on one chip = **microprocessor** | personal computers | Intel 4004 (1971, ~2,300 transistors); Apple II (1977); IBM PC (1981) | Hoff, Mazor, Faggin, Shima (4004) |
| 5 | 1980s– | ULSI; massive parallelism; AI | — | Japan's Fifth Generation project (1982–1994) | — |

Each step: smaller, cheaper, less power, faster, more reliable — that is the one-line "briefly explain".

Year boundaries differ between textbooks by a few years — write **"approximately"**.
ENIAC was **not** a stored-program computer: it was reprogrammed by rewiring plugboards.

> ✓ **Check 5.** (a) What single thing defines a generation? (b) What did the 4th generation put on
> one chip? (c) Two words in the question tell you the *format* of the answer. Which?

---

### 6 · Types of computers

> **Q** `[A1 Q5 · 10 marks]`
> **In how many ways are computers divided? Distinguish between each type of computers.**
>
> *"In how many ways" is a strange phrasing. Guess what he is asking for before reading on.*

He is asking for the number of **axes of classification**, not the number of computers. There is no
single official count, which is why the answer must *open by naming the axes* and then split each one.

| Axis | Classes |
|---|---|
| **Size / capability** | personal (desktop) · notebook · workstation (engineering graphics) · mainframe / enterprise (business data) · server (databases, many users) · supercomputer (weather, aircraft simulation) |
| **Data representation** | analog (continuous values) · digital (discrete values) · hybrid (both) |
| **Purpose** | general-purpose (any program) · special-purpose / embedded (one fixed task — washing machine, car ECU) |

Open with: *"Computers are classified on three bases — size and capability, data representation, and
purpose."* Then one distinguishing line per class.

Note how axis 2 reaches back to file 00 step 1: *digital* is one value of one axis, not a synonym for
*computer*.

> ✓ **Check 6.** Classify a smartphone on all three axes.

---

## Exam form

### Definitions (≤ 40 words each) — `[A1 Q1]`

| Term | Write |
|---|---|
| **Digital computer** | A digital system that performs various computational tasks; *digital* means information is represented by variables taking a limited number of discrete values. It executes a stored program automatically. (Mano) |
| **Computer architecture** | The attributes visible to the programmer — instruction set, data types, registers, addressing modes. It describes **what** the computer does. Also called instruction set architecture (ISA). |
| **Computer organization** | The operational units and interconnections that realize the architecture — datapath, control signals, buses, memory technology. It describes **how** the computer does it. |
| **Microarchitecture** | Another name for computer organization: the specific hardware implementation of a given ISA. One ISA can have many microarchitectures. |
| **Microoperation** | An elementary operation performed on data stored in registers, completed in one clock pulse — e.g. load, clear, shift, increment. |
| **Register transfer language** | A symbolic notation describing the microoperations among registers and the control conditions under which they occur, e.g. `P: R2 ← R1`. |

### Architecture vs organization — `[A1 Q2]`

| | Architecture | Organization |
|---|---|---|
| Question | what | how |
| Deals with | functional behaviour | structural relationship |
| Design level | high-level | low-level |
| Other name | instruction set architecture | microarchitecture |
| Contents | instruction set, registers, data types, addressing modes | circuits, adders, buses, control logic, peripherals |
| Order | decided first | decided after |
| Visible to programmer | yes | no |

⚠ The professor's deck has the row "Architecture indicates its hardware, organization indicates its
performance." Reproduce it if asked. It is imprecise: architecture is the abstraction, not the hardware.

### von Neumann vs Harvard — `[A1 Q6]`

| | von Neumann | Harvard |
|---|---|---|
| Memory | one, shared by instructions and data | separate instruction and data memories |
| Buses | one set | two independent sets |
| Fetch and data access | take turns → **von Neumann bottleneck** | simultaneous |
| Cost / flexibility | cheaper, flexible memory split | more hardware, fixed split |
| Used in | general-purpose computers | DSPs, microcontrollers, CPU caches |

### RISC vs CISC — `[A1 Q20]`

| | CISC | RISC |
|---|---|---|
| Instructions | many, complex | few, simple |
| Length | variable (8086: 1–6 bytes) | fixed (RISC-V: 32 bits) |
| Memory access | most instructions | load/store only |
| Addressing modes | many | few |
| Registers | few | many (RISC-V: 32) |
| Control | usually microprogrammed | usually hardwired |
| Pipelining | hard | easy |
| Complexity lives in | hardware | compiler |
| Examples | x86, VAX | ARM, RISC-V, MIPS |

### Functional units, generations, types — `[A1 Q4, Q3, Q5]`

Use the tables in Build steps 1, 5 and 6 as they stand.

---

## Attempt

The six questions, in full, on paper, **within the word limits and without looking back**.
This is the assignment block — treat it as the mock.

1. `[A1 Q1 · 12]` Define: (i) digital computer (ii) computer architecture (iii) computer organization
   (iv) microarchitecture (v) microoperation (vi) register transfer language. *(2 marks each)*
2. `[A1 Q2 · 4]` What distinguishes computer organization from computer architecture?
3. `[A1 Q3 · 10]` Briefly explain the generations of computers. Tabulate technology, landmark machines
   and people.
4. `[A1 Q4 · 10]` List the elements that constitute a computer and explain the role and responsibility
   of each.
5. `[A1 Q5 · 10]` In how many ways are computers divided? Distinguish the types.
6. `[A1 Q6 · 10]` Describe the features of the von Neumann architecture. Compare & contrast with Harvard.
7. `[A1 Q20 · 20]` Short notes: (i) RISC architecture (ii) CISC architecture.

---

## Traps

| Trap | Correction |
|---|---|
| Architecture = hardware, organization = software | Both concern hardware. Architecture is the programmer-visible contract; organization is its implementation |
| Answering Q4 with "CPU, RAM, hard disk, monitor" | He asks for the five **functional units** with their **jobs** — a different list |
| Answering Q1 definitions with no example for RTL | An RTL definition without `P: R2 ← R1` loses marks |
| Exact generation years as fact | They vary by author. Write "approximately" |
| ENIAC as the first stored-program computer | ENIAC used plugboards. Stored-program idea: EDVAC report (1945); first run: Manchester Baby (1948) |
| Q3 written as prose | He says **tabulate**, and he says **contributors**. No table, no names → marks gone |
| Harvard is obsolete | It is in DSPs, microcontrollers and every CPU's split cache |
| RISC is always faster | Speed depends on the implementation; RISC makes a fast one easier to build |
| Ignoring the word limit | 1 mark = 20 words is printed on the paper. Over-writing is penalised |

---

## Self-test

1. One ISA, two machines 10× apart in speed. Architecture or organization difference? Why?
2. Which generation introduced the stored-program concept, and why was it not ENIAC?
3. Name the unit that holds the program while it runs, and the unit that decides the order of steps.
4. Give two RISC features that exist *because* of pipelining.
5. A RISC program for a task has more instructions than the CISC one. Why can it still run faster?
6. Write RTL: copy register R1 into R3 only when control signal T = 1.
7. Your file-00 fact: instructions and data are stored identically. Which architecture is that, and what
   does it cost you?

---
---

## Answers

**Check 1.** (a) **Control** — it issues the timing signals. (b) They do different jobs: the ALU computes,
Control sequences and times every unit. (c) Not just the list — a stated **job** for each of the five,
which is where the 10 marks actually sit.

**Check 2.** (a) **Harvard** — separate paths allow both at once. (b) Instruction fetch and data access
share one memory path, so they take turns and the processor waits on memory. (c) No — DSPs,
microcontrollers, and the split instruction/data cache in every modern CPU.

**Check 3.** (a) **Organization** — the programmer-visible contract is unchanged. (b) **Architecture** —
the instruction set changed. (c) It needs several register-level steps across clock ticks: read M[201]
into DR, then add DR to AC. (d) `T: R3 ← R1`

**Check 4.** (a) Only load and store instructions access memory; all arithmetic is between registers.
(b) Every instruction is fetched and decoded in the same time, so instructions move through the
assembly-line stages in lockstep. (c) **RISC**. (d) No — RISC makes a fast implementation *easier to
build*; the speed comes from the implementation, not the acronym.

**Check 5.** (a) The **switching device** (tube → transistor → IC → LSI/VLSI). (b) The whole
**processor** — the microprocessor (Intel 4004, 1971). (c) **"Tabulate"** and **"contributors"**.

**Check 6.** Size: personal / portable · data: digital · purpose: general-purpose (it contains embedded
special-purpose processors too).

**Attempt 1.** Definitions table, *Exam form*. The RTL definition must include an example.

**Attempt 2.** *(4 marks, ≤ 80 words)*
> Computer architecture is the set of attributes visible to the programmer — instruction set, data
> types, registers and addressing modes; it describes *what* the computer does and is decided first.
> Computer organization is how those attributes are realized in hardware — control signals, datapath,
> buses, memory technology; it describes *how*, is invisible to the programmer, and follows the
> architecture. Many organizations can implement one architecture.

**Attempt 3.** Generations table (step 5) + one line: each generation is defined by its switching
device; each step cut size, power and cost and raised speed and reliability. **Table, with names.**

**Attempt 4.** Functional-units table (step 1, drop the example column) + the block diagram.
State Processor = ALU + Control. Give each unit an explicit responsibility.

**Attempt 5.** Three axes (step 6). Open by naming the three bases, then one distinguishing line per class.

**Attempt 6.** von Neumann features: stored program (instructions and data in one memory, same binary
form) · one bus · sequential fetch–execute driven by the PC · five functional units. Then the comparison
table + the bottleneck mechanism stated causally.

**Attempt 7.** Each note, ≤ 200 words: (1) definition (2) five features from the table (3) why it exists
(4) its cost (5) examples. RISC skeleton: reduced set of simple fixed-length instructions · load/store,
fixed format, few addressing modes, many registers, hardwired control · easy pipelining · longer
programs, compiler carries complexity · ARM, RISC-V, MIPS.

**Self-test 1.** Organization — the ISA, hence the programmer-visible attributes, is identical.

**Self-test 2.** 1st generation (EDVAC report 1945; Manchester Baby 1948). ENIAC was programmed by
plugboards — its program was not in memory.

**Self-test 3.** Memory (primary); Control.

**Self-test 4.** Fixed instruction length · load/store only (memory touched at one predictable point).

**Self-test 5.** Simple, uniform instructions pipeline well, so many run overlapped; total time drops
despite the higher count.

**Self-test 6.** `T: R3 ← R1`

**Self-test 7.** **von Neumann** — one memory, one form, one bus. The cost is the **von Neumann
bottleneck**: instruction fetch and data access share the single path, so they take turns and the
processor waits on memory.

---

## What to do next

1. Mark every Check and Self-test item with **clean / with struggle / missed** and schedule accordingly.
2. Do the **Attempt** block under exam conditions — it is 76 marks of real assignment.
3. File 02 is next, and the question base changes: **Mano starts supplying questions there**
   (2-9, 2-12, 2-13, 2-15, 2-16 map straight onto `[A1 Q7]`'s six circuits, 24 marks).
