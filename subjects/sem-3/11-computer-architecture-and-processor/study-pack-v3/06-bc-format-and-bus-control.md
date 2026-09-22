# 06 — Basic Computer: instruction format and bus control

**Assignment 2: Q1–Q4 · 40 of 150 marks · U2 (L9–L10) · needs 00, 03**

> **The question base changes here.** From this file on, **every Assignment 2 question is a Mano
> chapter-5 problem copied verbatim**, sub-parts sometimes dropped. So each step below carries both
> labels, and the dropped sub-parts are printed too — they are the obvious place an exam question
> comes from.

---

## Map

```
   [1] Instruction format ──► [2] Direct vs indirect
       I | opcode | address        the I bit
             │
             ▼
   [3] The registers ──────► [4] The common bus (S₂S₁S₀)
       AR PC DR AC IR TR          controls → transfer
             │                          │
             │                          ▼
             │                    [5] transfer → controls
             │                          (the reverse)
             ▼                          │
   [7] The instruction set ◄─────── [6] What needs two pulses
       25 instructions, hex
             │
             ▼
   [8] Completeness
```

---

## The questions this file answers

| # | Question | Marks | Mano |
|---|---|---|---|
| 1 | `[A2 Q1]` 256K words of 32 bits; instruction has indirect bit, opcode, register code for 64 registers, address. Bits in each part? Word format? Memory data/address inputs? | 10 | **5-1** |
| 2 | `[A2 Q2]` Given active control inputs on the common bus, specify the register transfer executed next. | 10 | **5-3** |
| 3 | `[A2 Q3]` Given register transfers, specify S₂S₁S₀, the LD, memory read/write, and adder operation. | 10 | **5-4** |
| 4 | `[A2 Q4]` For given 16-bit instructions: hex code, and what it performs. | 10 | **5-6** |

Unasked Mano follow-ups for this file: **5-2, 5-5, 5-7.**

---

## Build

### 1 · The instruction format

> **Q** `[A2 Q1 · 10 marks]` **= Mano 5-1**
> **A computer uses a memory unit with 256K words of 32 bits each. A binary instruction code is
> stored in one word of memory. The instruction has four parts: an indirect bit, an operation code,
> a register code part to specify one of 64 registers, and an address part.**
> **a. How many bits are in the operation code, the register code part, and the address part?**
> **b. Draw the instruction word format and indicate the number of bits in each part.**
> **c. How many bits are there in the data and address inputs of the memory?**
>
> *You did part (a) in file 00, step 4. Do it again from memory before reading — then get (b) and (c),
> which are the other six marks.*

Everything here is one fact from file 00: **n bits address 2ⁿ things**, run in both directions.

**(a)** 256K = 2⁸ × 2¹⁰ = **2¹⁸** → address part = **18 bits**.
64 registers = 2⁶ → register code = **6 bits**.
The instruction is one word = 32 bits, so: 1 + opcode + 6 + 18 = 32 → **opcode = 7 bits**.

**(b)**
```
 31   30                  24 23              18 17                        0
┌───┬──────────────────────┬──────────────────┬──────────────────────────┐
│ I │      opcode          │  register code   │        address           │
└───┴──────────────────────┴──────────────────┴──────────────────────────┘
  1           7                     6                     18
```

**(c)** The memory holds 32-bit words at 2¹⁸ addresses, so: **data input = 32 bits, address
input = 18 bits.** (The data input width is the *word* size, not the instruction's address field —
they are different numbers that happen to be in the same question.)

**Now the machine this course actually builds — Mano's Basic Computer:**

- memory **4096 × 16** → 4096 = 2¹² → **12 address bits**
- 16 − 12 − 1 (mode bit) = **3 bits of opcode**

```
 15    14  13  12   11                                  0
┌───┬──────────────┬────────────────────────────────────┐
│ I │    opcode    │              address               │
└───┴──────────────┴────────────────────────────────────┘
  1        3                       12
```

> ✓ **Check 1.** (a) Memory of 1M words of 16 bits: how many address bits? (b) If the BC had 8192
> words instead of 4096, how many opcode bits would remain? (c) Why is the memory's data input 32
> bits in A2 Q1 rather than 18?

---

### 2 · Direct and indirect addressing

> **Q** `[Mano 5-2 · not yet asked — a classic 4-marker]`
> **What is the difference between a direct and an indirect address instruction? How many references
> to memory are needed for each type of instruction to bring an operand into a processor register?**
>
> *You met an indirect instruction in file 00, Check 9 (the 932E case). Guess the memory-reference
> count for each before reading.*

The **I bit** (bit 15) decides:

| Mode | I | Mechanism | Effective address (EA) |
|---|---|---|---|
| **Direct** | 0 | the address field **is** the operand's address | EA = address field |
| **Indirect** | 1 | the address field points at a word that **holds** the address | EA = M[address field] |

*Worked:* `0 ADD 457` → the operand is in 457. `1 ADD 300` → go to 300, find (say) 1350 there, and
the operand is in **1350**.

**Memory references to bring the operand into a register:**

| | References | Which |
|---|---|---|
| **Direct** | **2** | 1 to fetch the instruction, 1 to fetch the operand |
| **Indirect** | **3** | 1 instruction, 1 to fetch the address, 1 to fetch the operand |

**Why indirect exists at all** — and this is the part that earns the explanation marks. It is *not*
about reach: 12 bits already names all 4096 words. It is about **computed addresses**. The pointer
word can be changed while the program runs, which is what makes arrays, pointers and parameter
passing possible on a machine with a single accumulator. The cost is one extra memory access, taken
at T₃.

> ✓ **Check 2.** (a) How many memory references for an indirect instruction, and what is each for?
> (b) Give the real reason indirection exists, given that 12 bits already reaches all of memory.
> (c) At which timing step does the extra access happen?

---

### 3 · The registers

> **Q** *(needed for steps 4 and 5 — no assignment question asks for the list alone, but every bus
> question assumes it)*
> **Name the Basic Computer's registers and say why some are 12 bits and others 16.**
>
> *Guess the rule that decides the width before reading on.*

| Register | Bits | Name | Function |
|---|---|---|---|
| **DR** | 16 | Data Register | holds the memory **operand** |
| **AR** | 12 | Address Register | holds the **address for memory** — always drives the memory's address pins |
| **AC** | 16 | Accumulator | the single general-purpose processor register |
| **IR** | 16 | Instruction Register | holds the instruction being executed |
| **PC** | 12 | Program Counter | holds the address of the **next** instruction |
| **TR** | 16 | Temporary Register | scratch |
| **INPR** | 8 | Input Register | one input character |
| **OUTR** | 8 | Output Register | one output character |

**The width rule:** registers that hold **addresses** are 12 bits (that is all an address needs);
registers that hold **words** are 16. INPR/OUTR are 8 because the BC's I/O is one character at a time.

Plus **SC** (4-bit sequence counter) and seven flip-flops: **I, S, E, R, IEN, FGI, FGO**.

**Why only one general-purpose register?** Because the BC is an **accumulator machine**: every
arithmetic instruction has one implicit operand (AC) and one memory operand, so the instruction needs
only *one* address field — which is exactly what buys the 3-bit opcode in step 1. Register count and
instruction format are not independent choices.

> ✓ **Check 3.** (a) Why are AR and PC 12 bits but DR and IR 16? (b) What would having four
> general-purpose registers cost in the instruction format? (c) Which register always drives the
> memory's address pins?

---

### 4 · The common bus — controls to transfer

> **Q** `[A2 Q2 · 10 marks]` **= Mano 5-3**
> **The following control inputs are active in the common bus system taught in the class. For each
> case, specify the register transfer that will be executed during the next clock transition.**
>
> | | S₂S₁S₀ | LD of register | Memory | Adder |
> |---|---|---|---|---|
> | a | 111 | IR | Read | — |
> | b | 110 | PC | — | — |
> | c | 100 | DR | Write | — |
> | d | 000 | AC | — | Add |
>
> *File 03 gave you the rule: select lines choose the source, LD chooses the destination. Try all
> four before reading on — (d) is the one that breaks the rule.*

Nine registers plus memory share **one 16-bit common bus**, selected by **S₂S₁S₀**:

| S₂S₁S₀ | Source on the bus |
|---|---|
| 000 | *(nothing)* |
| 001 | **AR** |
| 010 | **PC** |
| 011 | **DR** |
| 100 | **AC** |
| 101 | **IR** |
| 110 | **TR** |
| 111 | **Memory** |

Rules that get examined:
- **AR and PC are 12-bit**, so when they drive the 16-bit bus the **high 4 bits are 0s**.
- **OUTR is 8-bit** and takes the **low 8 bits** of the bus.
- Five registers have **LD, INR and CLR** (AR, PC, DR, AC, TR); **IR and OUTR have LD only**.
- ★ **AC's input does not come from the bus.** It comes from the **adder-and-logic circuit**, whose
  inputs are AC, DR and INPR. This is U1's ALSU instantiated for this machine (file 05).

Now the four cases:

| | Reasoning | Transfer |
|---|---|---|
| **a** | 111 puts **memory** on the bus, read asserted; IR loads | **IR ← M[AR]** |
| **b** | 110 puts **TR** on the bus; PC loads | **PC ← TR** |
| **c** | 100 puts **AC** on the bus; DR loads **and** memory write is asserted, and a write takes whatever is on the bus | **DR ← AC, M[AR] ← AC** |
| **d** | 000 means **nothing is on the bus** — yet AC loads. AC's input is the adder circuit, and "Add" selects addition of DR | **AC ← AC + DR** |

Case (d) is the whole point of the question. If you answered "nothing happens", re-read the AC rule
above — it is the one register that can be loaded with the bus idle.

> ✓ **Check 4.** (a) What is on the bus when S₂S₁S₀ = 011? (b) Why can AC be loaded while the bus
> carries nothing? (c) In case (c), why do *two* things happen from one set of controls?

---

### 5 · The common bus — transfer to controls

> **Q** `[A2 Q3 · 10 marks]` **= Mano 5-4**
> **The following register transfers are to be executed in the system of Fig. 5-4. For each, specify:
> (1) the binary value applied to S₂, S₁, S₀; (2) the register whose LD must be active (if any);
> (3) a memory read or write (if needed); (4) the operation in the adder and logic circuit (if any).**
> **a. `AR ← PC`  b. `IR ← M[AR]`  c. `M[AR] ← TR`  d. `AC ← DR, DR ← AC` (simultaneously)**
>
> *This is step 4 run backwards. Do (a)–(c) quickly; spend your guess on (d) — and recall file 03,
> step 3.*

| | S₂S₁S₀ | LD | Memory | Adder |
|---|---|---|---|---|
| **a. AR ← PC** | **010** (PC) | **AR** | — | — |
| **b. IR ← M[AR]** | **111** (memory) | **IR** | **read** | — |
| **c. M[AR] ← TR** | **110** (TR) | none | **write** | — |
| **d. AC ← DR, DR ← AC** | **100** (AC) | **DR** *and* **AC** | — | **transfer DR** |

**(c) has no LD at all** — the destination is memory, and memory's "load" is the write signal. That
catches people.

**(d) is the simultaneous exchange from file 03, step 3 — and here you can see the hardware that makes
it work.** DR is loaded **from the bus**, which carries AC. AC is loaded **from the adder-and-logic
circuit**, which is fed DR directly. Two different paths, so both registers can be written on the
same clock edge, each receiving the other's old value. No temporary register. This is *why* the BC
puts the adder circuit on AC's input rather than taking AC from the bus.

> ✓ **Check 5.** (a) Why does (c) need no LD? (b) Trace the two separate paths in (d).
> (c) Give the controls for `TR ← AC`.

---

### 6 · What cannot be done in one pulse

> **Q** `[Mano 5-5 · not yet asked]`
> **Explain why each of the following microoperations cannot be executed during a single clock pulse
> in the system shown in Fig. 5-4. Specify a sequence of microoperations that will perform the
> operation.**
> **a. `IR ← M[PC]`  b. `AC ← AC + TR`  c. `DR ← DR + AC` (AC does not change)**
>
> *Each one is blocked by a different limitation. Guess at least one before reading.*

| | Why it is impossible | The legal sequence |
|---|---|---|
| **a** | Memory is addressed **only by AR**. PC cannot drive the memory address pins. | `AR ← PC` then `IR ← M[AR]` |
| **b** | The adder-and-logic circuit's second input is **DR** (and INPR) — **not TR**. TR cannot reach the adder. | `DR ← TR` then `AC ← AC + DR` |
| **c** | The adder's output goes **only to AC**. There is no path from the adder to DR. | `AC ← AC + DR` then... but AC must not change — so first save it: `TR ← AC`, then `AC ← AC + DR`, then `DR ← AC`, then `AC ← TR` |

**The lesson that generalises:** a microoperation is possible only if a **physical path** exists for
it. "One clock pulse" is not about time, it is about wiring. This is why file 03's illegal statements
were illegal and why the BSA instruction takes two steps (file 07).

> ✓ **Check 6.** (a) Which single register can address memory? (b) Which registers feed the adder?
> (c) Where does the adder's output go?

---

### 7 · The instruction set

> **Q** `[A2 Q4 · 10 marks]` **= Mano 5-6**
> **Consider the instruction formats of the basic computer and respective list of instructions. For
> each of the following 16-bit instructions: (i) determine the equivalent four-digit hexadecimal code
> and (ii) explain in your own words what the instruction is going to perform.**
> **a) `1011 0001 0010 0100`  b) `0111 0000 0010 0000`**
> ⚠ **He dropped Mano's part (a): `0001 0000 0010 0100`. Do that one too.**
>
> *Convert all three to hex first (file 00, step 3). Then guess what makes (b) different in kind from
> the other two.*

**Three instruction formats**, distinguished by opcode 111 and the I bit:

| Format | Opcode | I | Count |
|---|---|---|---|
| **Memory-reference (MRI)** | 000–110 | either | 7 |
| **Register-reference (RRI)** | **111** | **0** | 12 |
| **Input–output (IO)** | **111** | **1** | 6 |

**7 + 12 + 6 = 25 instructions.**

| Symbol | I=0 | I=1 | Operation |
|---|---|---|---|
| AND | 0xxx | 8xxx | AC ← AC ∧ M[EA] |
| ADD | 1xxx | 9xxx | AC ← AC + M[EA], E ← carry |
| LDA | 2xxx | Axxx | AC ← M[EA] |
| STA | 3xxx | Bxxx | M[EA] ← AC |
| BUN | 4xxx | Cxxx | PC ← EA |
| BSA | 5xxx | Dxxx | M[EA] ← PC, PC ← EA + 1 |
| ISZ | 6xxx | Exxx | M[EA] ← M[EA] + 1, skip if zero |

| RRI | Hex | | | IO | Hex | |
|---|---|---|---|---|---|---|
| CLA | 7800 | clear AC | | INP | F800 | input char to AC |
| CLE | 7400 | clear E | | OUT | F400 | output char from AC |
| CMA | 7200 | complement AC | | SKI | F200 | skip on input flag |
| CME | 7100 | complement E | | SKO | F100 | skip on output flag |
| CIR | 7080 | circulate right AC & E | | ION | F080 | interrupt on |
| CIL | 7040 | circulate left AC & E | | IOF | F040 | interrupt off |
| INC | 7020 | increment AC | | | | |
| SPA | 7010 | skip if AC positive | | | | |
| SNA | 7008 | skip if AC negative | | | | |
| SZA | 7004 | skip if AC zero | | | | |
| SZE | 7002 | skip if E zero | | | | |
| HLT | 7001 | halt | | | | |

★ **The hex pattern is not decoration — do not memorise it, derive it.** RRI codes are `7` followed by
a **one-hot** 12-bit field: 7800 = bit 11, 7400 = bit 10, 7200 = bit 9, … 7001 = bit 0. IO codes are
`F` followed by one-hot bits 11 down to 6. The hardware tests `IR(i) = Bᵢ` **directly, with no
decoder**, which is *why* the codes must be one-hot. Anyone who memorises the hex without seeing this
cannot reconstruct it under pressure; anyone who sees it never needs to.

**Now the three instructions:**

| Binary | Hex | I | Opcode | Field | What it does |
|---|---|---|---|---|---|
| `1011 0001 0010 0100` | **B124** | **1** | 011 = **STA** | addr 124 | **Indirect STA.** EA = M[124]; then **M[EA] ← AC** — store AC at the address *found in* location 124 |
| `0111 0000 0010 0000` | **7020** | 0 | 111 → **RRI** | 0x020 = bit 5 | **INC** — **AC ← AC + 1**. No memory is touched |
| `0001 0000 0010 0100` | **1024** | 0 | 001 = **ADD** | addr 024 | **Direct ADD** — **AC ← AC + M[024]**, with the carry out going to E |

> ✓ **Check 7.** (a) Convert 7400 to binary and name the instruction from the one-hot bit.
> (b) What is `C1F0`? (c) Why must the RRI codes be one-hot?

---

### 8 · Is the instruction set complete?

> **Q** `[Mano 5-7 · not yet asked]`
> **What are the two instructions needed in the basic computer in order to set the E flip-flop to 1?**
>
> *There is no "set E" instruction. Guess how you'd do it with what exists.*

There is no SET-E, but there is **CLE** (clear E to 0) and **CME** (complement E). So:

```
CLE      E ← 0
CME      E ← E' = 1
```

Two instructions. That trick — *build what you need from what exists* — is the idea behind the
standard exam question **"is the BC's instruction set complete?"**

A set is complete if it can compute anything computable. The BC qualifies because it has all four
necessary categories:

| Category | BC instructions |
|---|---|
| Arithmetic / logic / shift | ADD, CMA, INC, CIR, CIL, AND, CLA |
| Data transfer | LDA, STA |
| Control / branching | BUN, BSA, ISZ |
| Input–output | INP, OUT |

*Why these suffice:* AND + CMA give NAND, which is functionally complete for logic; ADD + CMA + INC
give subtraction by 2's complement, hence multiplication and division by repetition; BUN + ISZ give
conditional branching, hence loops. Everything else is convenience, not necessity.

> ✓ **Check 8.** (a) How do you set E to 1? (b) Name the four categories a complete set needs.
> (c) The BC has no SUBTRACT instruction. How do you subtract?

---

## Exam form

### The three formats

```
 MRI   I ≠ 111 opcode    →  7 instructions, I selects direct/indirect
 RRI   opcode 111, I = 0 →  12 instructions, IR(0-11) one-hot
 IO    opcode 111, I = 1 →  6 instructions,  IR(0-11) one-hot
                                                        25 total
```

### The bus table

Memorise `000 none · 001 AR · 010 PC · 011 DR · 100 AC · 101 IR · 110 TR · 111 Memory`.
Mnemonic: it is the order they appear in Mano's Fig. 5-4, top to bottom.

### Answering bus questions in either direction

| Given | Find |
|---|---|
| S₂S₁S₀ + LD + memory + adder | look up the source, name the destination → the transfer |
| a transfer | source → S₂S₁S₀ · destination → its LD (or memory write) · adder only if AC is the destination |

**Three facts that catch people:** memory-as-destination has **no LD** (it has write) · **AC** is
loaded from the **adder**, not the bus · **AR and PC** drive only the low 12 bits.

### Sizing

n bits ↔ 2ⁿ locations, in both directions. Instruction word = mode + opcode + (register code) + address.

---

## Attempt

1. `[A2 Q1 · 10]` all three parts, with the format drawn and labelled.
2. `[A2 Q2 · 10]` all four cases. Make sure (d) says `AC ← AC + DR`.
3. `[A2 Q3 · 10]` all four transfers as a four-column table.
4. `[A2 Q4 · 10]` **all three** instructions — his two plus Mano's dropped one.
5. `[Mano 5-2]` direct vs indirect with the memory-reference counts.
6. `[Mano 5-5]` the three impossible microoperations and their legal sequences.
7. `[Mano 5-7]` setting E.

---

## Traps

| Trap | Correction |
|---|---|
| S₂S₁S₀ = 000 means "nothing happens" | It means nothing is **on the bus**. AC can still be loaded from the adder |
| Giving an LD for `M[AR] ← TR` | Memory's destination control is **write**, not LD |
| Memory data input = the address-field width | Data input = **word** width; address input = ⌈log₂ words⌉ |
| Memorising the 7xxx hex codes | They are **one-hot**. Derive them |
| Reading `B124` as a direct STA | First hex digit B = 1011 → **I = 1**, indirect |
| Treating 7020 as a memory-reference instruction | Opcode 111 with I = 0 → register-reference; no memory access |
| "Indirect addressing extends the address range" | 12 bits already reaches all 4096 words. It exists for **computed addresses** |
| Forgetting AR and PC are 12-bit on a 16-bit bus | Their high 4 bits appear as 0s |

---

## Self-test

1. 2M words of 64 bits. Memory address input width? Data input width?
2. S₂S₁S₀ = 101 with LD(AC) active and the adder set to transfer — what is the transfer?
3. Give the controls for `PC ← AR`.
4. What is `E7FF`?
5. Why can `AC ← AC + TR` not happen in one clock pulse?
6. How many memory references does an indirect ADD make in total, and what is each one for?
7. Why must register-reference instruction codes be one-hot rather than binary-encoded?

---
---

## Answers

**Check 1.** (a) 1M = 2²⁰ → **20 bits**. (b) 8192 = 2¹³ → 13 address bits, so 16 − 13 − 1 = **2 bits**
of opcode (only 4 memory-reference opcodes — which is why Mano stopped at 4096). (c) The data input
carries a whole **word**, and words here are 32 bits; 18 is how many wires the *address* input needs.

**Check 2.** (a) **Three** — fetch the instruction, fetch the effective address from the pointer word,
fetch the operand. (b) For **computed addresses**: the pointer can be modified at run time, enabling
arrays, pointers and parameter passing on a one-accumulator machine. (c) **T₃**, via `D′₇IT₃: AR ← M[AR]`.

**Check 3.** (a) AR and PC hold **addresses**, which need only 12 bits here; DR and IR hold **words**,
which are 16 bits. (b) A register field in every instruction — fewer bits left for the opcode and the
address, exactly the trade in step 1's A2 Q1 machine. (c) **AR**.

**Check 4.** (a) **DR**. (b) Because AC's input comes from the **adder-and-logic circuit** (fed by AC,
DR and INPR), not from the bus. (c) The bus carries AC, DR's LD captures it, **and** the memory write
signal stores whatever is on the bus — so one bus value lands in two places.

**Check 5.** (a) Its destination is memory, whose write control replaces LD. (b) DR ← bus ← AC; and
AC ← adder-and-logic ← DR. Two physically separate paths, so both can be written on the same edge.
(c) S₂S₁S₀ = **100** (AC on the bus), **LD(TR)**, no memory, no adder.

**Check 6.** (a) **AR**. (b) **AC, DR and INPR**. (c) Only to **AC**.

**Check 7.** (a) 7400 = `0111 0100 0000 0000` → opcode 111, I = 0, one-hot bit **10** → **CLE**, clear E.
(b) C1F0: C = 1100 → I = 1, opcode 100 = **BUN**, indirect, address 1F0 → `PC ← M[1F0]`.
(c) Because the hardware wires `IR(i)` straight to the control gates as Bᵢ — there is no decoder for
that field, so exactly one bit must identify the instruction.

**Check 8.** (a) **CLE then CME**. (b) Arithmetic/logic/shift · data transfer · control/branching ·
input–output. (c) `CMA` then `INC` gives the 2's complement of AC, then `ADD` — i.e. A − B = A + B′ + 1.

**Self-test 1.** 2M = 2²¹ → address input **21 bits**; data input **64 bits**.

**Self-test 2.** 101 puts **IR** on the bus, but AC is loaded from the **adder**, not the bus — with the
adder set to transfer, its data input is DR, so the transfer is **AC ← DR**. (Putting IR on the bus
is irrelevant to AC; this is the trap in the question.)

**Self-test 3.** S₂S₁S₀ = **001** (AR on the bus), **LD(PC)**, no memory, no adder.

**Self-test 4.** E7FF: E = 1110 → I = **1**, opcode 110 = **ISZ**, indirect, address 7FF →
EA = M[7FF]; increment M[EA]; skip the next instruction if the result is zero.

**Self-test 5.** The adder-and-logic circuit's second data input is **DR** (and INPR) — TR has no path
to the adder. TR must first be copied to DR.

**Self-test 6.** **Three**: the instruction fetch (T₁), the effective-address fetch (T₃), the operand
fetch (T₄).

**Self-test 7.** The 12-bit field is applied **directly** to the control gates as B₀…B₁₁ with no
decoder, so each instruction must be identified by its own single bit.

---

## What to do next

File 07 puts the machine in motion: the timing signals T₀…T₁₅, the fetch–decode–execute cycle, and
the full register traces that A2 Q5–Q8 ask for. It is where the pack's opening question from file 00
(PC = 3AF) finally gets answered in full.
