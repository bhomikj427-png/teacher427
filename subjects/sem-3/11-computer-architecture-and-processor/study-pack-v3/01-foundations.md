# 01 — Foundations

**Assignment 1: Q1–Q6, Q20 · 76 of 200 marks · U1 (L1–L2) · needs 00**

---

## Map

```
   [1] What a computer is
    │
   [2] Its five parts ─────────► [3] Where program and data live
    │                                 von Neumann vs Harvard
    ▼
   [4] Architecture vs organization ──► [5] How big the instruction list is
       + microoperation, RTL                RISC vs CISC
    │
   [6] How the hardware evolved     [7] How computers are classified
       5 generations                    3 axes
```

---

## Predict

1. Two laptops run the same app file. One is 10× faster. Is the app seeing a different "computer"?
2. One chef has one door to the storeroom for both recipe cards and ingredients. What slows the kitchen down?

---

## Build

### 1 · What a computer is

A **computer** takes digitized input, processes it by following a **list of instructions stored inside
it**, and produces output (Hamacher).

Two words carry the definition:

- **digital** — information held as bits (00, step 1)
- **stored** — the program sits in memory, like the 3 + 5 program in 00, step 9

A calculator that can only ever add has fixed wiring. A computer runs whatever program is loaded.

> **Check 1.** What makes a computer *general-purpose* rather than a fixed-function machine?

---

### 2 · The five functional units

Typing `3 + 5` and seeing `8` uses every part:

```
            ┌──────────── Processor ────────────┐
 Input ───► │   ALU  (arithmetic & logic)       │ ───► Output
 keyboard   │   Control (sequences every step)  │      screen
            └────────────────┬──────────────────┘
                             │  bus (shared wires)
                          Memory
                  holds program + data
```

| Unit | Job | In the 3 + 5 example |
|---|---|---|
| **Input** | turns outside data into bits | keys `3`, `5` → binary |
| **Memory** | stores program and data | M[200] = 3, M[201] = 5, program at 100 |
| **ALU** | arithmetic and logic on register values | AC + 5 → 8 |
| **Control** | tells each unit what to do and **when** (timing signals) | fetch, then load, then add, then store |
| **Output** | turns bits back into something readable | `8` on screen |

**Processor = ALU + Control.** The units are joined by a **bus** — one shared set of wires (file 03).

Memory has two levels:
**primary** — electronic, fast, holds the running program (RAM: any address reached in the same short time) ·
**secondary** — disks: large, cheap, slow, keeps data when power is off.

> **Check 2.** (a) Which unit decides *when* AC loads a new value? (b) Why is the processor two units, not one?

---

### 3 · Where program and data live: von Neumann vs Harvard

In 00's program, instructions (100–102) and data (200–202) sat in **one memory**, as the same kind of 16-bit word.
That is the **stored-program concept**, published by John von Neumann in 1945 (the EDVAC report).

**von Neumann architecture** = one memory for instructions and data, one path (bus) to the processor.

Consequence — the **von Neumann bottleneck**:
fetching an instruction and reading data both need the one path, so they take turns.
The processor can work faster than that path delivers words, and then it **waits**.
System speed is limited by the memory path, not by the processor.

**Harvard architecture** = two separate memories — one for instructions, one for data — each with its own path.
An instruction fetch and a data read can happen **at the same time**. The cost: twice the wiring, and a fixed split of memory.

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

> **Check 3.** (a) A chip reads its next instruction and a data byte in the same clock tick. Which architecture?
> (b) State the bottleneck in one sentence, with its cause.

---

### 4 · Architecture vs organization

A programmer writing for the Basic Computer needs to know only:

- **instruction set** — the list of instructions it understands (LDA, ADD, STA, …) and their bit format
- **registers** it can use — AC, PC
- **data types** — how bits are read: e.g. a 16-bit word as a signed integer
- **addressing modes** — how the address field finds the operand.
  *Direct*: `ADD 201` uses M[201]. *Indirect* (I = 1): M[201] holds the address of the operand.

That list is the **computer architecture**, also called the **instruction set architecture (ISA)**.
It is a **contract**: any machine that honours it runs the same programs.

**Computer organization** is the hardware that honours the contract — how the adder is built,
how registers connect to the bus, which memory chips, what control circuits. The programmer never sees it.

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

**Microarchitecture** = another name for organization.

**Microoperation** — one elementary step on register data, done in **one clock tick** (00, step 7).
`ADD 201` is not one step inside the machine. It runs as microoperations: read M[201] into a
data register DR, then add DR into AC.

**Register transfer language (RTL)** — the notation that writes microoperations exactly:

```
DR ← M[AR]         copy the memory word at address AR into DR   (AR = address register)
AC ← AC + DR       add DR into AC
P: R2 ← R1         copy R1 into R2, only when control signal P = 1
```

> **Check 4.** (a) A company makes its adder faster but keeps every instruction the same. Architecture or organization change?
> (b) A new instruction MUL is added. Which one changed? (c) Why can `ADD 201` not be one microoperation?

---

### 5 · How big the instruction list is: RISC vs CISC

Task: `M[202] ← M[200] × M[201]`. Two ways to design the instruction set (illustrative instructions, not a real ISA):

```
 CISC — one complex instruction          RISC — simple instructions only
   MULT 200, 201, 202                      LOAD  R1, 200
                                           LOAD  R2, 201
                                           MUL   R1, R2        (register-to-register)
                                           STORE R1, 202
```

**CISC** (complex instruction set computer) — many instructions, some doing load + compute + store in one.
Short programs. The hardware must handle instructions of different lengths and step counts.

**RISC** (reduced instruction set computer) — few, simple instructions, all the **same length**.
**Only LOAD and STORE touch memory** (*load/store*); arithmetic works on registers, so RISC gives many registers.
Programs are longer; the **compiler** does the work of splitting tasks up.

Why RISC wins speed: identical, simple instructions let the processor run them like an **assembly line** —
start the next instruction before the last one finishes (**pipelining**, U4). Uneven CISC instructions jam that line.

**Control unit** — the part that generates the step-by-step control signals:
**hardwired** = fixed logic gates, fast (usual in RISC) ·
**microprogrammed** = the steps stored as a small program in a ROM, easy to extend to many instructions (usual in CISC; U3).

Why CISC existed: memory was expensive and programs were hand-written, so dense instructions saved memory.
Memory got cheap and compilers got good → RISC.
Today's x86 is CISC to the programmer but internally splits each instruction into RISC-like steps.

Examples: **CISC** — Intel x86, VAX. **RISC** — ARM, RISC-V, MIPS.

> **Check 5.** (a) What does *load/store* mean? (b) Why does fixed instruction length help pipelining?
> (c) Which design puts the complexity in the compiler?

---

### 6 · Generations: the switching device

A processor is a huge number of switches (00, step 1). Each generation is defined by **what the switch is made of**.

| Gen | ≈ Period | The switch | What it changed | Landmarks | People |
|---|---|---|---|---|---|
| 1 | 1945–1956 | **vacuum tube** — glass bulb; big, hot, fails often | machine language; drum memory | ENIAC (1945, 18,000+ tubes); EDVAC report (1945); Manchester Baby ran the first stored program (1948); UNIVAC I (1951) | Eckert & Mauchly; von Neumann |
| 2 | 1956–1964 | **transistor** — solid, small, cool, reliable | core memory; assembly, FORTRAN (1957) | TX-0 (1956); IBM 7090 | Bardeen, Brattain, Shockley (transistor, 1947); Backus (FORTRAN) |
| 3 | 1964–1971 | **integrated circuit (IC)** — many transistors on one chip | operating systems, multiprogramming | IBM System/360 (1964) | Kilby (IC, 1958); Noyce (planar IC, 1959) |
| 4 | 1971–1980s | **LSI/VLSI** — a whole processor on one chip = **microprocessor** | personal computers | Intel 4004 (1971, ~2,300 transistors); Apple II (1977); IBM PC (1981) | Hoff, Mazor, Faggin, Shima (4004) |
| 5 | 1980s– | ULSI; massive parallelism; AI | — | Japan's Fifth Generation project (1982–1994) | — |

Each step: smaller, cheaper, less power, faster, more reliable.
Year boundaries differ between textbooks by a few years — write "approximately".

ENIAC was **not** a stored-program computer: it was reprogrammed by rewiring plugboards.

> **Check 6.** (a) What single thing defines a generation? (b) What did the 4th generation put on one chip?

---

### 7 · Types of computers

No single official count. Three standard axes:

| Axis | Classes |
|---|---|
| **Size / capability** | personal (desktop) · notebook · workstation (engineering graphics) · mainframe / enterprise (business data) · server (databases, many users) · supercomputer (weather, aircraft simulation) |
| **Data representation** | analog (continuous values) · digital (discrete values) · hybrid (both) |
| **Purpose** | general-purpose (any program) · special-purpose / embedded (one fixed task — washing machine, car ECU) |

> **Check 7.** Classify a smartphone on all three axes.

---

## Exam form

**Word limit in A1: 1 mark = 20 words.** 2 marks ≤ 40 words · 10 marks ≤ 200 words.

### Definitions (≤ 40 words each)

| Term | Write |
|---|---|
| **Digital computer** | A digital system that performs various computational tasks; *digital* means information is represented by variables taking a limited number of discrete values. It executes a stored program automatically. (Mano) |
| **Computer architecture** | The attributes visible to the programmer — instruction set, data types, registers, addressing modes. It describes **what** the computer does. Also called instruction set architecture (ISA). |
| **Computer organization** | The operational units and interconnections that realize the architecture — datapath, control signals, buses, memory technology. It describes **how** the computer does it. |
| **Microarchitecture** | Another name for computer organization: the specific hardware implementation of a given ISA. One ISA can have many microarchitectures. |
| **Microoperation** | An elementary operation performed on data stored in registers, completed in one clock pulse — e.g. load, clear, shift, increment. |
| **Register transfer language** | A symbolic notation describing the microoperations among registers and the control conditions under which they occur, e.g. `P: R2 ← R1`. |

### Architecture vs organization

| | Architecture | Organization |
|---|---|---|
| Question | what | how |
| Deals with | functional behaviour | structural relationship |
| Design level | high-level | low-level |
| Other name | instruction set architecture | microarchitecture |
| Contents | instruction set, registers, data types, addressing modes | circuits, adders, buses, control logic, peripherals |
| Order | decided first | decided after |
| Visible to programmer | yes | no |

⚠ The professor's deck has the row "Architecture indicates its hardware, organization indicates its performance."
Reproduce it if asked. It is imprecise: architecture is the abstraction, not the hardware.

### von Neumann vs Harvard

| | von Neumann | Harvard |
|---|---|---|
| Memory | one, shared by instructions and data | separate instruction and data memories |
| Buses | one set | two independent sets |
| Fetch and data access | take turns → **von Neumann bottleneck** | simultaneous |
| Cost / flexibility | cheaper, flexible memory split | more hardware, fixed split |
| Used in | general-purpose computers | DSPs, microcontrollers, CPU caches |

### RISC vs CISC

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

### Functional units, generations, types

Use the tables in Build steps 2, 6, 7 as they stand.

---

## Attempt

On paper, within the word limits.

1. Define: (i) digital computer (ii) computer architecture (iii) computer organization (iv) microarchitecture
   (v) microoperation (vi) register transfer language. *(2 marks each)*
2. Distinguish computer organization from computer architecture. *(4 marks)*
3. Tabulate the generations of computers with technology, landmark machines and people. *(10 marks)*
4. List the elements that constitute a computer and explain the role of each. *(10 marks)*
5. In how many ways are computers divided? Distinguish the types. *(10 marks)*
6. Describe the features of the von Neumann architecture. Compare it with Harvard. *(10 marks)*
7. Short notes: (i) RISC architecture (ii) CISC architecture. *(10 + 10 marks)*

---

## Traps

| Trap | Correction |
|---|---|
| Architecture = hardware, organization = software | Both concern hardware. Architecture is the programmer-visible contract; organization is its implementation |
| Exact generation years as fact | They vary by author. Write "approximately" |
| ENIAC as the first stored-program computer | ENIAC used plugboards. Stored-program idea: EDVAC report (1945); first run: Manchester Baby (1948) |
| Harvard is obsolete | It is in DSPs, microcontrollers and every CPU's split cache |
| RISC is always faster | Speed depends on the implementation; RISC makes a fast one easier to build |
| Address and content mixed up | M[200] is the content *at* address 200 |

---

## Self-test

1. One ISA, two machines 10× apart in speed. Architecture or organization difference? Why?
2. Which generation introduced the stored-program concept, and why was it not ENIAC?
3. Name the unit that holds the program while it runs, and the unit that decides the order of steps.
4. Give two RISC features that exist *because* of pipelining.
5. A RISC program for a task has more instructions than the CISC one. Why can it still run faster?
6. Write RTL: copy register R1 into R3 only when control signal T = 1.

---
---

## Answers

**Predict 1.** No — the app sees the same instruction set; the speed gap is in the hardware (step 4).
**Predict 2.** Cards and ingredients take turns through one door — the von Neumann bottleneck (step 3).

**Check 1.** Its program is stored in memory, so loading a different program makes it do a different job.

**Check 2.** (a) **Control** — it issues the timing signals. (b) They do different jobs: the ALU computes,
Control sequences and times every unit.

**Check 3.** (a) **Harvard** — separate paths allow both at once. (b) Instruction fetch and data access share
one memory path, so they take turns and the processor waits on memory.

**Check 4.** (a) **Organization** — the programmer-visible contract is unchanged. (b) **Architecture** — the
instruction set changed. (c) It needs several register-level steps across clock ticks: read M[201] into DR,
then add DR to AC.

**Check 5.** (a) Only load and store instructions access memory; all arithmetic is between registers.
(b) Every instruction is fetched and decoded in the same time, so instructions move through the
assembly-line stages in lockstep. (c) **RISC**.

**Check 6.** (a) The **switching device** (tube → transistor → IC → LSI/VLSI). (b) The whole **processor** — the microprocessor (Intel 4004, 1971).

**Check 7.** Size: personal / portable · data: digital · purpose: general-purpose (it contains embedded special-purpose processors too).

**Attempt 1.** Definitions table, Exam form. The RTL definition must include an example.

**Attempt 2.** (4 marks, ≤ 80 words)
> Computer architecture is the set of attributes visible to the programmer — instruction set, data types,
> registers and addressing modes; it describes *what* the computer does and is decided first. Computer
> organization is how those attributes are realized in hardware — control signals, datapath, buses, memory
> technology; it describes *how*, is invisible to the programmer, and follows the architecture. Many
> organizations can implement one architecture.

**Attempt 3.** Generations table (step 6) + one line: each generation is defined by its switching device;
each step cut size, power and cost and raised speed and reliability.

**Attempt 4.** Functional-units table (step 2, drop the example column) + the block diagram. State Processor = ALU + Control.

**Attempt 5.** Three axes (step 7). Open with: *"Computers are classified on three bases — size and
capability, data representation, and purpose."* One distinguishing line per class.

**Attempt 6.** von Neumann features: stored program (instructions and data in one memory, same binary form) ·
one bus · sequential fetch–execute driven by the PC · five functional units. Then the comparison table + the bottleneck mechanism.

**Attempt 7.** Each note, ≤ 200 words: (1) definition (2) five features from the table (3) why it exists
(4) its cost (5) examples.
RISC skeleton: reduced set of simple fixed-length instructions · load/store, fixed format, few addressing
modes, many registers, hardwired control · easy pipelining · longer programs, compiler carries complexity ·
ARM, RISC-V, MIPS.

**Self-test 1.** Organization — the ISA, hence the programmer-visible attributes, is identical.

**Self-test 2.** 1st generation (EDVAC report 1945; Manchester Baby 1948). ENIAC was programmed by plugboards — its program was not in memory.

**Self-test 3.** Memory (primary); Control.

**Self-test 4.** Fixed instruction length · load/store only (memory touched at one predictable point).

**Self-test 5.** Simple, uniform instructions pipeline well, so many run overlapped; total time drops despite the higher count.

**Self-test 6.** `T: R3 ← R1`
