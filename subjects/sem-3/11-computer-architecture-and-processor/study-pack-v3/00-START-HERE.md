# Computer Architecture & Processor ECE2108 — Study Pack v3

v2 tells you what to write. v3 **teaches it first, from zero**, then shows what to write.
Every term is defined before it is used. Status: **00 and 01 built**; 02–10 follow once this shape is right.

---

## How each file runs

```
## Predict      2–3 guesses from common sense — no knowledge needed
## Build        one idea per step · concrete example · a Check after each step
## Exam form    the tables and definitions to reproduce in the exam
## Attempt      the professor's assignment questions
## Traps
## Self-test
## Answers      at the bottom — Checks, Attempt, Self-test
```

**Per step:** read it → cover it → answer the Check on paper → compare with Answers.
A wrong answer you then fix sticks better than a right answer you only read.

Mark every Check and Self-test item:

- **clean** → revisit in 3 days
- **with struggle** → revisit tomorrow
- **missed** → redo today, again tomorrow

---

## The path

```
   [00] Ground zero              ◄ YOU ARE HERE    bits, hex, memory, register, clock, program
    │
   [01] Foundations                                what a computer is, its parts,
    │                                              von Neumann/Harvard, architecture, RISC/CISC
   [02] Digital building blocks                    flip-flop, decoder, MUX, register circuits
    │
   [03] RTL + common bus          *                how registers pass data — the gate to everything after
    │
   [04] Microoperations + signed arithmetic
    │
   [05] ALSU                      *
    │
   [06] Basic Computer: instruction format + bus
    │
   [07] Timing + execution traces *
    │
   [08] Control-gate derivation   *
    │
   [09] Pipelining numericals                      needs only 03
    │
   [10] Mock paper
```

`*` = most marks per hour. Until a v3 file exists, use the same-numbered v2 file.

---

## The textbook

**"Mano" = M. Morris Mano, *Computer System Architecture*, 3rd ed., Pearson (2007).** Every "Ref: M. M.
Mano" on the slides means this book. Search the full title, not "Mano".

| Mano chapter | Unit |
|---|---|
| 4 — Register Transfer and Microoperations | U1 |
| 5 — Basic Computer Organization and Design | U2 |
| 7 — Microprogrammed Control · 8 — Central Processing Unit | U3 |
| 9 — Pipeline and Vector Processing | U4 |

12 of Assignment 2's 15 questions are copied from Mano's end-of-chapter problems.

---

# Ground zero

## Predict

1. A light switch is either on or off. How many different on/off patterns can **3** switches show?
2. A street has 4096 houses. Each house holds one sheet of paper with a number written on it.
   What two different numbers matter when you say "go to house 200 and read the sheet"?

---

## Build

### 1 · Bit

A **bit** is one value that is either **0 or 1**.
In hardware it is a switch: a voltage is low (0) or high (1).

Two values, because a circuit can tell "low" from "high" reliably even when voltages drift.
Telling ten voltage levels apart is far more error-prone.

**Digital** means information is held as values from a **limited set** — for computers, bits (Mano).

> **Check 1.** Why does a computer store 0/1 rather than the digits 0–9 directly?

---

### 2 · Binary numbers

Put bits side by side and each position has a weight, doubling right to left:

```
weight:   8   4   2   1
bits:     0   1   0   1      →  4 + 1 = 5
```

**n bits give 2ⁿ different patterns.** 3 bits → 8. 12 bits → 4096. 16 bits → 65,536.

> **Check 2.** (a) `1011` = ? in decimal. (b) How many patterns do 12 bits give?

---

### 3 · Hexadecimal (hex)

Long bit strings are unreadable, so group them **4 at a time**. 4 bits have 16 patterns → one hex digit.

```
0000 0   0100 4   1000 8   1100 C
0001 1   0101 5   1001 9   1101 D
0010 2   0110 6   1010 A   1110 E
0011 3   0111 7   1011 B   1111 F
```

`0010 0010 0000 0000` = `2200` in hex. Hex is only a shorthand — the hardware still holds 16 bits.

> **Check 3.** (a) `1010 0011` = ? in hex. (b) 3 hex digits = how many bits?

---

### 4 · Word

A **word** is the fixed-size group of bits the machine moves and stores as one unit.

The machine this course builds (Mano's **Basic Computer**, U2) has a **16-bit word** = 4 hex digits.
Everything it holds — numbers and instructions — is a 16-bit word.

> **Check 4.** How many hex digits does one Basic Computer word take?

---

### 5 · Memory and address

**Memory** is a long numbered row of words. A word's number is its **address**.

```
 address │ content
─────────┼─────────
   200   │  0003
   201   │  0005
   202   │  0000
```

**Address ≠ content.** Address 200 *holds* the value 3.
Notation: **M[200]** = "the word stored at address 200" = `0003`.

Basic Computer memory: **4096 words**. Since 4096 = 2¹², an address needs **12 bits** = 3 hex digits (`000`–`FFF`).

> **Check 5.** (a) From the table, M[201] = ? (b) Which address holds `0003`? (c) Why is an address 12 bits?

---

### 6 · Register

A **register** is a tiny storage place for one word, **inside the processor**.
It is built from **flip-flops** — one flip-flop stores one bit (Digital Electronics), so a 16-bit register = 16 flip-flops.

| | Register | Memory word |
|---|---|---|
| Where | inside the processor | outside, in the memory chip |
| How many | a handful | thousands |
| Speed | fastest | slower |
| Reached by | its name | an address |

Registers are named by their job. Two to know now:

- **AC** (accumulator) — holds the number currently being worked on.
- **PC** (program counter) — holds the **address** of the next instruction.

The processor calculates only on values in registers. A value in memory is first copied into a register.

> **Check 6.** Give two differences between a register and a memory word.

---

### 7 · Clock

The **clock** is a signal that ticks 0 → 1 → 0 at a steady rate.
A register changes its stored value **only at a clock tick** (the clock edge). Between ticks it holds still.

So a computer works in discrete steps: one tick = one smallest step.

> **Check 7.** AC holds 5. The adder's output already reads 8. When does AC hold 8?

---

### 8 · Instruction and program

An **instruction** is a word that the processor reads as a command.
A **program** is a list of instructions stored in memory.

Basic Computer instruction (16 bits):

```
 bit 15 │ bits 14–12 │ bits 11–0
   I    │   opcode   │  address
  mode  │ what to do │ which memory word to do it to
```

With I = 0 the **first hex digit is the opcode** and the **last three are the address**:

| Word | Opcode | Name | Meaning |
|---|---|---|---|
| `2200` | 2 | LDA 200 | load: AC ← M[200] |
| `1201` | 1 | ADD 201 | add: AC ← AC + M[201] |
| `3202` | 3 | STA 202 | store: M[202] ← AC |

> **Check 8.** (a) What does `3205` do? (b) Write the word for "load AC from address 1A0".

---

### 9 · A program running

The whole machine, holding one program that computes 3 + 5:

```
 address │ content │
─────────┼─────────┤
   100   │  2200   │  LDA 200     ┐
   101   │  1201   │  ADD 201     │ instructions
   102   │  3202   │  STA 202     ┘
   ...   │         │
   200   │  0003   │              ┐
   201   │  0005   │              │ data
   202   │  0000   │              ┘
```

The processor repeats one loop: **fetch** the word at address PC → PC moves to the next address → **execute** it.

| Step | PC before | Fetched | Executes | AC after | M[202] after |
|---|---|---|---|---|---|
| 1 | 100 | `2200` | AC ← M[200] | 0003 | 0000 |
| 2 | 101 | `1201` | AC ← AC + M[201] | 0008 | 0000 |
| 3 | 102 | `3202` | M[202] ← AC | 0008 | 0008 |

Instructions and data sit **in the same memory, in the same 16-bit form**. File 01 starts from that fact.

> **Check 9.** (a) Why does PC start at 100 and not 200? (b) If M[201] were `0007`, what would M[202] end as?

---
---

## Answers

**Predict 1.** 8 (2 × 2 × 2). **Predict 2.** The address (200) and the content (the number on the sheet).

**Check 1.** Two voltage levels can be told apart reliably despite noise and drift; ten levels cannot.

**Check 2.** (a) 8 + 2 + 1 = **11**. (b) 2¹² = **4096**.

**Check 3.** (a) `1010` = A, `0011` = 3 → **A3**. (b) **12 bits**.

**Check 4.** **4** (16 ÷ 4).

**Check 5.** (a) **0005**. (b) **200**. (c) 4096 words = 2¹² addresses, so 12 bits name every one.

**Check 6.** Any two: a register is inside the processor, memory is outside · a few registers vs thousands
of words · registers are faster · a register is reached by name, a memory word by address.

**Check 7.** At the **next clock tick**.

**Check 8.** (a) STA 205: **M[205] ← AC** — copy AC into address 205. (b) Opcode 2, address 1A0 → **`21A0`**.

**Check 9.** (a) PC holds the address of the next **instruction**; the instructions start at 100, the data at 200
is never meant to be executed. (b) 3 + 7 → **`000A`** (10 in hex).
