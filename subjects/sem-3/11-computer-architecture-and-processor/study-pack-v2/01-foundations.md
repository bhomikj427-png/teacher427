# 01 — Foundations: Definitions, Generations, Types, von Neumann/Harvard, RISC/CISC

**Assignment 1: Q1, Q2, Q3, Q4, Q5, Q6, Q20 · 76 of 200 marks · U1 (L1–L2)**

Word limit in A1: **1 mark = 20 words.** A 2-mark definition is ≤ 40 words; a 10-mark note ≤ 200.

---

## Map

```
   What a computer is  ──►  How it evolved  ──►  How it is built
   (definitions)            (5 generations)      (5 functional units)
                                                        │
                        ┌───────────────────────────────┤
                        ▼                               ▼
              How memory is shared             How instructions are designed
              (von Neumann vs Harvard)         (RISC vs CISC)
```

---

## Attempt

Write these on paper first. Respect the word limits.

1. Define, ≤ 40 words each: **(i)** digital computer **(ii)** computer architecture **(iii)** computer
   organization **(iv)** microarchitecture **(v)** microoperation **(vi)** register transfer language.
2. What distinguishes computer organization from computer architecture? *(4 marks)*
3. Tabulate the generations of computers with the technology, landmark machines and people of each.
   *(10 marks)*
4. List the elements that constitute a computer; explain the role of each. *(10 marks)*
5. In how many ways are computers divided? Distinguish the types. *(10 marks)*
6. Describe the features of the von Neumann architecture. Compare it with Harvard. *(10 marks)*
7. Short notes: **(i)** RISC architecture **(ii)** CISC architecture. *(10 + 10 marks)*

---

## Learn

### Definitions

| Term | Definition (exam form) |
|---|---|
| **Digital computer** | A digital system that performs various computational tasks; *digital* means information is represented by variables taking a limited number of discrete values (Mano). It executes a stored program automatically. |
| **Computer architecture** | The attributes visible to the programmer — instruction set, data types, registers, addressing modes. **What** the computer does. Also called instruction set architecture (ISA). |
| **Computer organization** | The operational units and their interconnections that realize the architecture — datapath, control signals, buses, memory technology. **How** it does it. |
| **Microarchitecture** | Another name for computer organization: the specific implementation of a given ISA. One ISA can have many microarchitectures (8086 and Core i9 run the same x86 binaries). |
| **Microoperation** | An elementary operation performed on data stored in registers, completed in one clock pulse — e.g. shift, load, clear, increment. |
| **Register transfer language (RTL)** | A symbolic notation that describes the microoperations among registers and the control conditions under which they happen, e.g. `P: R2 ← R1`. |

### Architecture vs organization

| | Architecture | Organization |
|---|---|---|
| Question | **what** | **how** |
| Deals with | functional behaviour | structural relationship |
| Design level | high-level | low-level |
| Other name | instruction set architecture | microarchitecture |
| Contents | instruction set, registers, data types, addressing modes | circuits, adders, buses, control logic, peripherals |
| Order | decided **first** | decided **after** |
| Visible to programmer? | yes | no |

**The one sentence that earns the marks:** architecture is a *contract* with the software; organization
is any hardware that keeps it. That is why one architecture (IBM System/360, 1964) could span a 50:1
range of machines.

⚠ The deck's table has a row "Architecture indicates its hardware, organization indicates its
performance." Reproduce it if you must; do not reason from it — architecture is the abstraction, not
the hardware.

### Generations of computers

Date boundaries differ between textbooks by a few years — write "approximately".

| Gen | ≈ Period | Technology | Landmarks | People |
|---|---|---|---|---|
| **1st** | 1945–1956 | **vacuum tubes**; machine language; drum/delay-line memory | ENIAC (1945, 18,000+ tubes); EDVAC report (1945) = stored-program concept; Manchester Baby ran the first stored program (1948); UNIVAC I (1951) | J. P. Eckert, J. Mauchly; John von Neumann |
| **2nd** | 1956–1964 | **transistors**; magnetic-core memory; assembly, first high-level languages | TX-0 (1956); IBM 7090; FORTRAN (1957) | Bardeen, Brattain, Shockley (transistor, 1947); John Backus (FORTRAN) |
| **3rd** | 1964–1971 | **integrated circuits** (SSI/MSI); operating systems, multiprogramming | IBM System/360 (1964); RCA Spectra 70 (1966) | Jack Kilby (IC, 1958); Robert Noyce (planar IC, 1959) |
| **4th** | 1971–1980s | **LSI/VLSI**; the **microprocessor**; personal computers | Intel 4004 (1971, ~2,300 transistors); Altair 8800 (1975); Apple II (1977); IBM PC (1981) | Ted Hoff, Stanley Mazor, Federico Faggin, Masatoshi Shima (4004) |
| **5th** | 1980s– | ULSI, massive parallelism, AI | Japan's Fifth Generation Computer Systems project (1982–1994) | — |

**Pattern to state in the answer:** each generation is defined by its **switching device**; each step
cut size, power and cost and raised speed and reliability.

### Functional units (Hamacher's five)

| Unit | Role |
|---|---|
| **Input** | accepts program and data; converts them to binary (keyboard, mouse) |
| **Memory** | stores program and data. **Primary** — fast, electronic, holds running programs; RAM reaches any word in short, fixed time. **Secondary** — large, cheap, slow (disks, optical) |
| **ALU** | arithmetic and logic; operands are first brought **into processor registers** |
| **Output** | sends results out (display, printer) |
| **Control** | coordinates all units: issues read/write and **timing signals** (which decide *when* each action happens) |

Processor = ALU + control. The units are connected by a **bus** (file 03).

### Types of computers

There is no single official count. Three axes are standard; name them and give each class.

| Axis | Classes |
|---|---|
| **Size / capability** (Hamacher) | personal/desktop · notebook · workstation (graphics, engineering) · enterprise system/mainframe (business data processing) · server (large databases, many requests) · supercomputer (weather forecasting, aircraft simulation) |
| **Data representation** | analog (continuous) · digital (discrete) · hybrid |
| **Purpose** | general-purpose (any program) · special-purpose/embedded (one task) |

Opening line for "in how many ways": *"Computers are classified on three bases — size and capability,
data representation, and purpose."*

### von Neumann vs Harvard

**von Neumann features:** stored-program concept (instructions and data in the **same** memory, same
binary form) · one address/data path to the CPU · sequential fetch–decode–execute controlled by a
program counter · five functional units.

| | von Neumann | Harvard |
|---|---|---|
| Memory | one, shared by instructions and data | separate instruction and data memories |
| Buses | one set | two independent sets |
| Fetch vs data access | **contend** for one bus → the **von Neumann bottleneck** | simultaneous |
| Cost / flexibility | cheaper, flexible split | more hardware, fixed split |
| Used in | general-purpose computers | DSPs, microcontrollers, CPU L1 caches |

**Bottleneck mechanism:** the CPU can outrun the single memory path and then waits; system speed is
limited by memory bandwidth, not processor speed.

### RISC and CISC

| | CISC | RISC |
|---|---|---|
| Instructions | many, complex, multi-step | few, simple |
| Length | variable (8086: 1–6 bytes) | fixed (RISC-V: 32 bits) |
| Memory access | most instructions | **load/store only** |
| Addressing modes | many | few |
| Registers | few | many (RISC-V: 32) |
| Control | usually microprogrammed | usually hardwired |
| Pipelining | hard | easy — uniform instructions |
| Complexity lives in | hardware | compiler |
| Examples | Intel x86, VAX | RISC-V, ARM, MIPS |

**Why each exists:** CISC suited costly memory and hand-written assembly (dense code). RISC suits cheap
memory and good compilers, where pipelining speed matters most. Modern x86 is CISC in its ISA but
decodes into RISC-like micro-operations internally.

---

## Worked

**Q2 (4 marks, ≤ 80 words):**

> Computer architecture is the set of attributes visible to the programmer — the instruction set, data
> types, registers and addressing modes; it describes *what* the computer does and is decided first.
> Computer organization is how those attributes are realized in hardware — control signals, datapath,
> buses, memory technology; it describes *how*, is invisible to the programmer, and follows the
> architecture. Many organizations can implement one architecture.

(68 words.)

**Q20(i) RISC, 10 marks — the skeleton for ≤ 200 words:**

1. Definition — reduced instruction set: a small set of simple, fixed-length instructions.
2. Five features — load/store, fixed format, few addressing modes, many registers, hardwired control.
3. Why — uniform instructions make pipelining easy; one-cycle execution.
4. Cost — more instructions per program; the compiler carries the complexity.
5. Examples — RISC-V, ARM, MIPS.

---

## Traps

| Trap | Correction |
|---|---|
| "Architecture = hardware, organization = software" | Both are hardware-related. Architecture is the programmer-visible **abstraction**; organization is the implementation |
| Exact generation years as fact | They vary by author. Write "approximately" |
| ENIAC as the first stored-program computer | ENIAC was plugboard-programmed. The stored-program idea is von Neumann's 1945 EDVAC report; Manchester Baby ran first (1948) |
| Harvard = "old" | Harvard is alive in DSPs, microcontrollers and every CPU's split L1 cache |
| "RISC is faster than CISC" | Performance depends on the implementation; RISC makes a fast implementation *easier* |

---

## Self-test

1. One ISA, two machines 10× apart in speed. Is the difference architecture or organization? Why?
2. Which generation introduced the stored-program concept, and why was it not ENIAC's?
3. A microcontroller fetches its next instruction and reads a data byte in the same clock cycle.
   Which architecture must it have?
4. Give two RISC features that exist *because* of pipelining.
5. Place a smartphone in each of the three classification axes.

---
---

## Answers

**Attempt 1.** See the definitions table. Each must fit 40 words; the RTL one must include an example.

**Attempt 2.** See Worked.

**Attempt 3.** The generations table. For 10 marks: table + one line on the pattern (switching device,
falling size/cost, rising speed/reliability).

**Attempt 4.** The functional-units table + a one-line block diagram: Input → Memory ⇄ Processor
(ALU + Control) → Output, with control lines to every unit.

**Attempt 5.** The three axes table + one distinguishing line per class.

**Attempt 6.** The von Neumann features list + comparison table + the bottleneck mechanism.

**Attempt 7.** Use the RISC/CISC table split into two notes, each with definition, 5 features, why,
examples.

**Self-test 1.** Organization. The ISA is identical, so the programmer-visible attributes are the same;
the speed difference comes from implementation (pipelining, caches, technology).

**Self-test 2.** 1st generation (1945 EDVAC report; 1948 Manchester Baby). ENIAC was programmed by
plugboards and switches — its program was not held in memory.

**Self-test 3.** Harvard — separate instruction and data paths let both accesses happen at once.

**Self-test 4.** Fixed-length instructions (every fetch/decode takes the same time) and load/store only
(memory is touched in one predictable stage).

**Self-test 5.** Size: personal/portable. Data: digital. Purpose: general-purpose (it contains many
special-purpose embedded processors too).
