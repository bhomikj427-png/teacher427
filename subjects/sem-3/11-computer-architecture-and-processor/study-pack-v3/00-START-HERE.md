# Computer Architecture & Processor ECE2108 — Study Pack v3

**Every idea in this pack is introduced by a real question you cannot yet answer.**
The question comes first, you guess, then the answer teaches you the concept.
No invented questions — every one is quoted from the professor's assignments or from the textbook.

Status: **complete — 13 files, 00–12**, covering the whole MTE scope U1–U4.

---

## Where the questions come from

Two bases, in this order. The full list is `../question-bank.md`.

| | Base | Why it ranks there |
|---|---|---|
| **P1** | The professor's **Assignment 1** (20 Q) and **Assignment 2** (15 Q) | First-party — what he actually wrote and marked. |
| **P2** | **Mano's end-of-chapter problems** | He builds the assignments out of them. **All 15 of Assignment 2 are Mano problems, copied.** So Mano predicts what he hasn't asked yet. |

Every question below is tagged: `[A1 Q4 · 10 marks]` or `[Mano 3-1]`, and where an assignment question
*is* a Mano problem, both.

> **The finding that makes P2 worth your time.** A2 Q1–Q10 are Mano 5-1, 5-3, 5-4, 5-6, 5-8, 5-9,
> 5-12, 5-16, 5-20, 5-21. A2 Q11–Q15 are Mano 9-1, 9-3, 9-5, 9-10, 9-11. He often drops Mano's
> sub-parts — those dropped parts are the obvious place for an exam question to come from.
> Assignment 1 is Mano too, but **re-numbered** (his 4-19 with the registers renamed, his 4-12 with
> three rows deleted). So for U2 and U4, drill Mano's answers; for U1, drill Mano's *method*.

---

## How each file runs

```
## The questions this file answers   the real questions, listed up front
## Build        each step opens with one of them · guess · then the answer teaches it
## Exam form    the tables and definitions to reproduce in the exam
## Attempt      the full questions, now answerable, under exam conditions
## Traps
## Self-test
## Answers      at the bottom — Checks, Attempt, Self-test
```

**The one rule that makes this work:** when you hit a **Q**, write a guess on paper *before* reading on.
One line, however wrong. Guessing wrong and then being corrected sticks harder than reading a correct
answer you never tried. Reading the answer straight through feels faster and teaches you much less.

Mark every Check and Self-test item:

- **clean** → revisit in 3 days
- **with struggle** → revisit tomorrow
- **missed** → redo today, again tomorrow

---

## The path

```
  U1 │ [00] Ground zero        ◄ START   bits, hex, memory, register, clock, program
     │ [01] Foundations                 what a computer is, its parts, von Neumann,
     │                                  architecture vs organization, RISC/CISC
     │ [02] Digital building blocks     flip-flop, decoder, MUX, register circuits
     │ [03] RTL + common bus      *     how registers pass data — the gate to all of U2
     │ [04] Microoperations + signed arithmetic
     │ [05] ALSU                  *     the professor's own closing slide
  ───┼──────────────────────────────────────────────────────────────────
  U2 │ [06] BC: instruction format + bus control
     │ [07] Timing + execution traces   *
     │ [08] Control-gate derivation     *
  ───┼──────────────────────────────────────────────────────────────────
  U3 │ [09] Microprogrammed control     ⚠ no assignment covers U3
     │ [10] Program control + status bits
  ───┼──────────────────────────────────────────────────────────────────
  U4 │ [11] Pipelining numericals       needs only 03 — can be done early
  ───┼──────────────────────────────────────────────────────────────────
     │ [12] Mock paper                  30 marks, timed — a diagnostic, not a lesson
```

`*` = most marks per hour. **If time is short: 03, 07, 08, 05 first, then 11.**

⚠ **U3 (files 09 and 10) is your most exposed unit.** Neither assignment touches it, so there are no
worked examples from the professor at all — but the hand-out prints the Mid-Term divider after L19,
and U3 is L12–L15. Everything you practise there comes from Mano.

---

## The textbook

**"Mano" = M. Morris Mano, *Computer System Architecture*, 3rd ed., Pearson.** Every "Ref: M. M. Mano"
on the slides means this book. Search the full title, not "Mano".

| Mano chapter | Unit |
|---|---|
| 4 — Register Transfer and Microoperations | U1 |
| 5 — Basic Computer Organization and Design | U2 |
| 7 — Microprogrammed Control · 8 — Central Processing Unit | U3 |
| 9 — Pipeline and Vector Processing | U4 |

---
---

# Ground zero

Nine ideas. Each is the thing you need in order to read one real exam question.

## The questions this file answers

By the end you can start every one of these. You cannot start any of them now.

1. `[A1 Q1(i) · 2]` Define: **Digital Computer**.
2. `[Mano 3-1]` Convert the following binary numbers to decimal: 101110; 1110101; 110110100.
3. `[Mano 3-5]` Convert the hexadecimal number F3A7C2 to binary and octal.
4. `[A2 Q1 = Mano 5-1 · 10]` A computer uses a memory unit with 256K words of 32 bits each… how many bits are there in the address part?
5. `[A1 Q10(iii) · part of 4]` Categorise as register or memory transfer and explain: `R1 ← M[AR]`.
6. `[A1 Q18 · 8]` The initial values of the 8-bit registers R1, R2, R3, R4 are… determine the results after the following micro-operations.
7. `[A2 Q5 = Mano 5-8 · 10]` With the help of a timing diagram explain the working of the microoperation `C₇T₃: SC ← 0`.
8. `[A2 Q4 = Mano 5-6 · 10]` For the 16-bit instruction `1011 0001 0010 0100`: give the hexadecimal code and explain what it performs.
9. `[A2 Q7 = Mano 5-12 · 10]` The content of PC is 3AF. The content of memory at address 3AF is 932E. What is the instruction that will be fetched and executed next?

---

## Build

### 1 · Bit

> **Q** `[A1 Q1(i) · 2 marks]`
> **Define: Digital Computer.**
>
> *Guess first — one line, on paper. Then read on.*

Most people write "a machine that computes". That earns 0 of 2, because it leaves out the word the
examiner is testing: **digital**.

**Digital** means information is held as values from a **limited set** of discrete values.
For a computer that set has exactly two members, and one such value is a **bit**: **0 or 1**.

In hardware a bit is a switch: a voltage is low (0) or high (1).
Two values, because a circuit can tell "low" from "high" reliably even when voltages drift.
Telling ten voltage levels apart is far more error-prone.

So Mano's definition, which is the one to write:

> A digital computer is a **digital system** that performs various **computational tasks**; *digital*
> means the information is represented by variables taking a **limited number of discrete values**.
> It executes a **stored program** automatically.

Three scoring words: *digital* · *discrete values* · *stored program*. (The third one is file 01.)

> ✓ **Check 1.** Why does a computer store 0/1 rather than the digits 0–9 directly?

---

### 2 · Binary numbers

> **Q** `[Mano 3-1]`
> **Convert the following binary numbers to decimal: 101110; 1110101; 110110100.**
>
> *Try the first one. Then read on.*

Put bits side by side and each position has a weight, doubling right to left:

```
weight:   8   4   2   1
bits:     0   1   0   1      →  4 + 1 = 5
```

So `101110` = 32 + 8 + 4 + 2 = **46**. Add the weights wherever there is a 1. That is the whole method.

**n bits give 2ⁿ different patterns.** 3 bits → 8. 12 bits → 4096. 16 bits → 65,536. 
That counting fact is what question 4 in the list above is really about — hold onto it.

> ✓ **Check 2.** (a) `1011` = ? in decimal. (b) How many patterns do 12 bits give?
> (c) Finish Mano 3-1: `1110101` and `110110100`.

---

### 3 · Hexadecimal (hex)

> **Q** `[Mano 3-5]`
> **Convert the hexadecimal number F3A7C2 to binary and octal.**
>
> *You need to know what F means first. Guess what base "hexadecimal" is, then read on.*

Long bit strings are unreadable, so group them **4 at a time**. 4 bits have 16 patterns → one hex digit.

```
0000 0   0100 4   1000 8   1100 C
0001 1   0101 5   1001 9   1101 D
0010 2   0110 6   1010 A   1110 E
0011 3   0111 7   1011 B   1111 F
```

Hex → binary is pure table lookup, one digit at a time:
`F3A7C2` → `1111 0011 1010 0111 1100 0010`.
Octal is the same trick with groups of **3** bits, re-grouped from the right: `74723702`.

`0010 0010 0000 0000` = `2200` in hex. Hex is only a shorthand — the hardware still holds 16 bits.

> ✓ **Check 3.** (a) `1010 0011` = ? in hex. (b) 3 hex digits = how many bits?
> (c) Why is hex used for 16-bit words rather than octal?

---

### 4 · Word, memory, address

> **Q** `[A2 Q1 = Mano 5-1 · 10 marks]`
> **A computer uses a memory unit with 256K words of 32 bits each. A binary instruction code is
> stored in one word of memory. The instruction has four parts: an indirect bit, an operation code,
> a register code part to specify one of 64 registers, and an address part.**
> **a. How many bits are there in the operation code, the register code part, and the address part?**
>
> *This is a 10-mark question and the professor copied it from Mano unchanged. Guess how you'd even
> start. Then read on.*

You cannot start it yet because three words are undefined. Here they are.

**Word** — the fixed-size group of bits the machine moves and stores as one unit.
"32 bits each" means one word is 32 bits wide. The machine this course builds (Mano's **Basic
Computer**, U2) has a **16-bit word** = 4 hex digits.

**Memory** — a long numbered row of words.

```
 address │ content
─────────┼─────────
   200   │  0003
   201   │  0005
   202   │  0000
```

**Address** — a word's number in that row. **Address ≠ content.** Address 200 *holds* the value 3.

Now the question cracks open, using only step 2's counting fact:

- 256K words = 2⁸ × 2¹⁰ = **2¹⁸ words** → an address needs **18 bits**.
- 64 registers = 2⁶ → the register code needs **6 bits**.
- The instruction is one word = 32 bits, split into four parts:
  1 (indirect) + opcode + 6 (register) + 18 (address) = 32 → **opcode = 7 bits**.

Basic Computer memory: **4096 words**. 4096 = 2¹², so an address is **12 bits** = 3 hex digits (`000`–`FFF`).

> ✓ **Check 4.** (a) How many hex digits does one Basic Computer word take?
> (b) From the table, what is at address 201? (c) Finish Mano 5-1 part (c): how many bits are in the
> data and address inputs of the memory?

---

### 5 · The M[ ] notation

> **Q** `[A1 Q10(iii) · part of 4 marks]`
> **Categorise as a register or a memory transfer statement, and explain the operation being
> performed: `R1 ← M[AR]`.**
>
> *Guess what the square brackets mean. Then read on.*

**M[X]** = "the word stored in memory at address X". So `M[200]` is `0003` in the table above.

`R1 ← M[AR]` reads: take the address currently sitting in register **AR**, go to that address in
memory, read the word there, put it in **R1**. Because memory is touched, it is a **memory transfer**
— that is the answer to the "categorise" half.

The arrow `←` always means *copy into*. The thing on the right is unchanged.

> ✓ **Check 5.** (a) If AR holds 201, what does `R1 ← M[AR]` put in R1?
> (b) Is `A ← B` a register or a memory transfer? (c) What does `M[AR] ← R2` do?

---

### 6 · Register

> **Q** `[A1 Q18 · 8 marks]`
> **The initial values of the 8-bit registers R1, R2, R3, and R4 are: R1 = 11110010, R2 = 11111111,
> R3 = 10111001, R4 = 11101010. Determine the results in each register after: (i) `R1 ← R1 + R2`
> (ii) `R3 ← R3 ∧ R4, R2 ← R2 + 1` (iii) `R1 ← R1 − R3`.**
>
> *You can already do the binary. Guess what a "register" is from how it's used here. Then read on.*

A **register** is a tiny storage place for one word, **inside the processor**.
It is built from **flip-flops** — one flip-flop stores one bit (Digital Electronics), so a 16-bit
register = 16 flip-flops.

| | Register | Memory word |
|---|---|---|
| Where | inside the processor | outside, in the memory chip |
| How many | a handful | thousands |
| Speed | fastest | slower |
| Reached by | its name | an address |

Registers are named by their job. Three to know now:

- **AC** (accumulator) — holds the number currently being worked on.
- **PC** (program counter) — holds the **address** of the next instruction.
- **AR** (address register) — holds the address memory is currently being told to use.

The processor calculates only on values in registers. A value in memory is first copied into a register
— which is exactly why `R1 ← M[AR]` exists.

> ✓ **Check 6.** (a) Give two differences between a register and a memory word.
> (b) In A1 Q18 above, why can the machine do `R1 ← R1 + R2` in one step but not `R1 ← R1 + M[200]`?

---

### 7 · Clock

> **Q** `[A2 Q5 = Mano 5-8 · 10 marks]`
> **With the help of a timing diagram explain the working of the microoperation `C₇T₃: SC ← 0`.**
>
> *Guess what the subscript 3 in T₃ might count. Then read on.*

The **clock** is a signal that ticks 0 → 1 → 0 at a steady rate.
A register changes its stored value **only at a clock tick** (the clock edge). Between ticks it holds still.

So a computer works in **discrete steps**: one tick = one smallest step. Those steps get numbered —
**T₀, T₁, T₂, T₃, …** — and that is what the subscript counts: *which tick we are on.*

A **microoperation** is one elementary operation on register data, done in one tick.
The notation in the question reads:

```
 C₇ T₃ :  SC ← 0
 └┬┘ └┬┘   └──┬──┘
  │   │       └─ the microoperation: clear SC to 0
  │   └───────── only during timing step 3
  └───────────── only if control signal C₇ is 1
```

Everything left of the colon is a **condition**. Everything right of it happens, in one tick, when the
condition holds. You will meet SC (the sequence counter, the thing that produces T₀, T₁, T₂ …) in file 07
— this question is answerable in full there, not here. What you need now is: **subscripts on T are
clock steps, and the colon means "only when".**

> ✓ **Check 7.** (a) AC holds 5. The adder's output already reads 8. When does AC actually hold 8?
> (b) In `xT₂: R1 ← R2`, under what two conditions does the copy happen?

---

### 8 · Instruction

> **Q** `[A2 Q4 = Mano 5-6 · 10 marks]`
> **For the 16-bit instruction `1011 0001 0010 0100`: (i) determine the equivalent four-digit
> hexadecimal code, and (ii) explain in your own words what the instruction is going to perform.**
>
> *Part (i) you can already do — do it now. Part (ii) you cannot. Then read on.*

Part (i) is step 3: `1011 0001 0010 0100` → **B124**.

Part (ii) needs one more idea: **some words in memory are not numbers, they are commands.**

An **instruction** is a word the processor reads as a command.
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

`B124` has first digit B = `1011`, so bit 15 = **1**: this is an *indirect* instruction, opcode 011,
address 124. Indirect means M[124] does not hold the operand — it holds the **address of** the operand.
The full answer needs the instruction table from file 06; the shape of the answer is available now.

> ✓ **Check 8.** (a) What does `3205` do? (b) Write the word for "load AC from address 1A0".
> (c) Do the professor's other instruction, `0111 0000 0010 0000`, as far as you can.

---

### 9 · A program running

> **Q** `[A2 Q7 = Mano 5-12 · 10 marks]`
> **The content of PC in the basic computer is 3AF. The content of AC is 7EC3. The content of memory
> at address 3AF is 932E. The content of memory at address 32E is 09AC. The content of memory at
> address 9AC is 8B9F. What is the instruction that will be fetched and executed next?**
>
> *This is the question that ties the whole file together. Guess: which of those four numbers is
> the instruction, and how did you decide? Then read on.*

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

The processor repeats one loop: **fetch** the word at the address in PC → PC moves on → **execute** it.

| Step | PC before | Fetched | Executes | AC after | M[202] after |
|---|---|---|---|---|---|
| 1 | 100 | `2200` | AC ← M[200] | 0003 | 0000 |
| 2 | 101 | `1201` | AC ← AC + M[201] | 0008 | 0000 |
| 3 | 102 | `3202` | M[202] ← AC | 0008 | 0008 |

Now the exam question answers itself. **PC holds the address of the next instruction**, PC = 3AF, so
the instruction fetched is **M[3AF] = 932E** — the other three numbers are the trail it will follow, and
7EC3 is just what AC happened to contain. That is the *whole* of part (a), and the reason it is worth
marks is that most people pick the wrong number.

Instructions and data sit **in the same memory, in the same 16-bit form**, and nothing marks which is
which except where PC points. File 01 starts from exactly that fact.

> ✓ **Check 9.** (a) Why does PC start at 100 and not 200 in the program above?
> (b) If M[201] were `0007`, what would M[202] end as?
> (c) In the exam question, `932E` has first digit 9 = `1001`, so bit 15 = 1. What does that tell you
> about where the operand really is — and which of 09AC / 8B9F becomes relevant?

---
---

## Answers

**Check 1.** Two voltage levels can be told apart reliably despite noise and drift; ten levels cannot.
This is what *digital* — a limited number of discrete values — buys you.

**Check 2.** (a) 8 + 2 + 1 = **11**. (b) 2¹² = **4096**.
(c) `1110101` = 64+32+16+4+1 = **117**; `110110100` = 256+128+32+16+4 = **436**.

**Check 3.** (a) `1010` = A, `0011` = 3 → **A3**. (b) **12 bits**.
(c) 16 divides by 4 exactly (4 hex digits per word) but not by 3 — octal would straddle word boundaries.

**Check 4.** (a) **4** (16 ÷ 4). (b) **0005** — the *content*; 201 is the address.
(c) Data input = one word = **32 bits**; address input = **18 bits**. (This is Mano 5-1(c) in full.)

**Check 5.** (a) `0005`. (b) **Register transfer** — no memory is touched.
(c) Writes the contents of R2 into memory at the address held in AR — a memory (write) transfer.

**Check 6.** (a) Any two: register is inside the processor, memory is outside · a few registers vs
thousands of words · registers are faster · a register is reached by name, a memory word by address.
(b) Both R1 and R2 are already inside the processor, so the adder can reach them in one tick. M[200]
is outside — it must first be copied into a register (`DR ← M[200]`), which costs its own tick.

**Check 7.** (a) At the **next clock tick**. (b) Control signal x = 1 **and** the machine is in timing
step T₂ — both, simultaneously.

**Check 8.** (a) STA 205: **M[205] ← AC** — copy AC into address 205. (b) Opcode 2, address 1A0 → **`21A0`**.
(c) `0111 0000 0010 0000` → **7020**. First digit 7 = `0111`, so bit 15 = 0 (direct) and the opcode is
111 — opcode 7 is the *register-reference* group, where the address field is not an address at all but a
code for which register operation to do. File 06 finishes it.

**Check 9.** (a) PC holds the address of the next **instruction**; instructions start at 100, and the
data at 200 is never meant to be executed. (b) 3 + 7 → **`000A`** (10 in hex).
(c) Bit 15 = 1 means **indirect**: the address field 32E does not hold the operand, it holds the
*address of* the operand. So the machine goes to M[32E] = 09AC, and **09AC is the real operand address**;
the operand itself is M[9AC] = **8B9F**. That is why the question gives you three chained memory values.

---

## What to do next

1. Mark each Check. Anything missed → redo it today and again tomorrow.
2. **Go to file 01.** It opens with `[A1 Q1]` in full — all six definitions, 12 marks — and the rest
   of the 76-mark Assignment 1 foundations block.
3. Do **not** try A2 Q7 in full yet. It needs files 06 and 07. You have just done part (a), which is
   the part most people get wrong.
