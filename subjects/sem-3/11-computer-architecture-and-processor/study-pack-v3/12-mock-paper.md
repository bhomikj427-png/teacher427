# 12 — Mock paper · 30 marks · 90 minutes

**Closed book. Timer on. Do not scroll past the line until time is up.**

This is a **diagnostic, not a lesson.** Do it only after you have worked the *Attempt* block of every
file. Its purpose is to tell you where you are still weak, not to teach you anything new.

---

## What this paper is, and what it is not

**Every question form here is one the professor has actually used** (Assignments 1 and 2) or one Mano
poses in the MTE chapters. **All numbers are new** — none is lifted from an assignment, so you cannot
pass by recall.

⚠ **The layout is assumed, not known.** ECE2108 has **no past paper at all** — neither MTE nor ETE.
The structure below (3 × 2 + 4 × 4 + 1 × 8) is taken from the sibling MUJ mid-term in Digital
Electronics. Treat the *questions* as evidence and the *shape* as a guess.

**U3 is included.** The v2 mock left it out because neither assignment tested it. That was a mistake
to copy forward: the hand-out puts the MTE divider after L19, and U3 is L12–L15. It is examinable, so
it is examined here — Section A3 and Section B4.

**Coverage:**

| Section | Marks | Units |
|---|---|---|
| A — three short answers | 3 × 2 = 6 | U1, U3 |
| B — four medium answers | 4 × 4 = 16 | U1, U2, U3 |
| C — one long answer | 1 × 8 = 8 | U4 |
| | **30** | |

---
---

# ECE2108 · Computer Architecture & Processor
## Mid-Term Examination (mock) · Max. marks 30 · 90 minutes
### All questions are compulsory. Missing data may be assumed suitably.

---

## Section A — 3 × 2 = 6 marks

**A1.** Define **microinstruction** and **microprogram**. *(2)*

**A2.** An 8-bit register holds `10110101`. Give its hexadecimal form, and its decimal value read as
a signed 2's-complement number. *(2)*

**A3.** Using Mano's mapping procedure, give the first microinstruction address for the operation
code `1001`. Show the working. *(2)*

---

## Section B — 4 × 4 = 16 marks

**B1.** Five 12-bit registers are to share a common bus built from multiplexers.
**(a)** How many multiplexers, of what size, and how many select lines? **(b)** State the two control
settings needed to perform `R3 ← R5`. *(4)*

**B2.** Two 8-bit registers hold R1 = `10110110` and R2 = `01101101`.
**(a)** Perform `R1 ← R1 + R2` and give the resulting values of the status bits C, S, Z and V.
**(b)** Starting again from R1 = `10110110`, give the B operand and the logic microoperation that
would change R1 to `10110000`. *(4)*

**B3.** In the Basic Computer, PC = `2C5`, AC = `4A1B`, E = 0, M[`2C5`] = `A3D0`, M[`3D0`] = `05F2`,
M[`5F2`] = `21C4`. Name the instruction that will be fetched and executed, and give the contents of
AC, E, PC, AR, DR and IR at the end of the instruction cycle. *(4)*

**B4.** A microinstruction has the fields F1 F2 F3 CD BR AD.
**(a)** Encode `AC ← 0, DR ← M[AR], PC ← AR` into the 9-bit microoperation field, or explain why it
cannot be done. **(b)** Give the CD and BR codes for *"call the subroutine INDRCT only if the
instruction is indirect."* *(4)*

---

## Section C — 1 × 8 = 8 marks

**C1.** A three-segment pipeline is used to compute `(Aᵢ − Bᵢ) × Cᵢ` for a stream of numbers.
The propagation times are: 25 ns for the operands to be read from memory into R1 and R2, 35 ns for
the signal to propagate through the subtractor, 5 ns for the transfer into R3, and 55 ns for the
signal to propagate through the multiplier.

**(a)** Specify the pipeline configuration and list the contents of all registers for i = 1 to 4. *(3)*
**(b)** What is the minimum clock cycle time that can be used? *(1)*
**(c)** A non-pipeline system performs the same operation with the interface registers removed. How
long does one task take? *(1)*
**(d)** Calculate the speedup for 20 tasks and for 200 tasks. *(2)*
**(e)** What is the maximum speedup achievable, and why is it not 3? *(1)*

---
---
---

# Answers and mark scheme

Mark yourself honestly. **A method with an arithmetic slip is worth more than a right number with no
working** — that is also how it is marked in the exam.

---

## Section A

**A1** *(2)* — one mark each, and the second definition must reference the first.

> A **microinstruction** is a control word stored in control memory — a string of bits specifying the
> control variables for one step. A **microprogram** is a **sequence of microinstructions**; the group
> implementing one machine instruction is called a **routine**.

*Common loss:* defining microinstruction as "a small instruction". It is a **control word**, and it
lives in **control memory**, not main memory.

**A2** *(2)*

- Hex: group in fours — `1011 0101` → **B5**.
- Signed: the MSB is 1, so it is negative. Invert → `0100 1010`, add 1 → `0100 1011` = 75.
  Therefore the value is **−75**.

*One mark for the hex, one for the signed value with the complement shown.*

**A3** *(2)*

Mano's mapping sends a 4-bit opcode `xxxx` to the 7-bit control-memory address `0xxxx00`:

```
   opcode 1001  →  0 1001 00  =  0100100₂  =  36
```

**Address 36.** *One mark for the `0xxxx00` form, one for the value.*
*Bonus-worthy line:* the two trailing zeros give each routine four words; the leading zero confines
all 16 routines to the first 64 words of the 128-word control memory.

---

## Section B

**B1** *(4)*

**(a)** *(2)* The sizing rule is **n multiplexers of k inputs**, one MUX per **bit position**:

- registers k = 5, width n = 12 → **12 multiplexers**, each **5-to-1**
- select lines = ⌈log₂ 5⌉ = **3** (shared by all twelve)

*Half marks for "5 multiplexers" — that is the standard error, counting registers instead of bits.*

**(b)** *(2)* **Select lines = the code for R5** (one of the eight codes a 3-bit field provides), and
**LD(R3) = 1**.

> Select lines choose the **source**; the LD input chooses the **destination**. Both are needed — a
> select code alone transfers nothing.

**B2** *(4)*

**(a)** *(2.5)*
```
   1011 0110     (B6 = 182 unsigned, −74 signed)
 + 0110 1101     (6D = 109)
 ──────────────
 1 0010 0011     = 23 hex, carry out 1
```
- **C = 1** (carry out of the MSB)
- **S = 0** (MSB of the result is 0)
- **Z = 0** (the result is not zero)
- carry **into** bit 7 = 1, carry **out** = 1 → **V = 1 ⊕ 1 = 0**

*Sanity check worth writing:* signed, −74 + 109 = +35 = `0010 0011` ✓, so V = 0 is right.
*Marks: 1 for the sum, 1.5 for the four bits with V justified by the two carries.*

**(b)** *(1.5)* Compare `10110110` with the target `10110000`: bits 2 and 1 change **1 → 0**, and
nothing changes 0 → 1. All changes in one direction downward → **mask (AND)**.

> **B = `11111001`**, microoperation **`R1 ← R1 ∧ B`**

*Common loss:* using OR, or putting 1s where bits must be cleared. In a mask, **0s clear**.

**B3** *(4)*

**Decode:** `A3D0` → `A` = `1010`, so **I = 1 (indirect)** and the opcode is `010` = **LDA**, address
field `3D0`.

**Indirect, so the address field is a pointer:** EA = M[`3D0`] = `05F2` → **EA = 5F2**.
The operand is M[`5F2`] = **`21C4`**.

**The cycle:**

| Step | Microoperation | Result |
|---|---|---|
| T₀ | `AR ← PC` | AR = 2C5 |
| T₁ | `IR ← M[AR]`, `PC ← PC + 1` | IR = A3D0, PC = **2C6** |
| T₂ | decode; `AR ← IR(0-11)`; `I ← IR(15)` | D₂ = 1, AR = 3D0, I = 1 |
| T₃ | `D′₇IT₃: AR ← M[AR]` | AR = **5F2** |
| T₄ | `D₂T₄: DR ← M[AR]` | DR = **21C4** |
| T₅ | `D₂T₅: AC ← DR`, `SC ← 0` | AC = **21C4** |

| | AC | E | PC | AR | DR | IR |
|---|---|---|---|---|---|---|
| | **21C4** | **0** | **2C6** | **5F2** | **21C4** | **A3D0** |

*Marks: 1 for identifying indirect LDA, 1 for EA = 5F2, 1 for AC, 1 for the other five registers.*
*Common losses:* taking `05F2` as the operand (it is the **address**); changing E (LDA does not touch
it); leaving PC at 2C5.

**B4** *(4)*

**(a)** *(2.5)* Look each symbol up in its field:

| Microoperation | Symbol | Field | Code |
|---|---|---|---|
| `AC ← 0` | CLRAC | **F1** | 010 |
| `DR ← M[AR]` | READ | **F2** | 100 |
| `PC ← AR` | ARTPC | **F3** | 110 |

All three are in **different fields**, so they can be decoded in parallel and **the encoding is
legal**:

> **`010 100 110`**

*The mark is as much for checking the fields differ as for the code.* State the rule: three
microoperations fit in one microinstruction **iff they come from three different fields**.

**(b)** *(1.5)* "Only if the instruction is indirect" is the condition **I** = DR(15) → **CD = 01**.
"Call the subroutine" → **BR = 01 (CALL)**.

> `NOP   I   CALL   INDRCT`  →  **CD = 01, BR = 01**

*Worth a line:* CALL also loads **SBR ← CAR + 1**, which is how the RET finds its way back.

---

## Section C

**C1** *(8)*

**(a)** *(3)* Two operands must be subtracted before the multiply, and Cᵢ must be held until then:

```
Segment 1:  R1 ← Aᵢ,  R2 ← Bᵢ
Segment 2:  R3 ← R1 − R2,   R4 ← Cᵢ
Segment 3:  R5 ← R3 × R4
```

k = 3, n = 4 → 3 + 4 − 1 = **6 clocks**.

| Clock | R1 | R2 | R3 | R4 | R5 |
|---|---|---|---|---|---|
| 1 | A1 | B1 | — | — | — |
| 2 | A2 | B2 | A1−B1 | C1 | — |
| 3 | A3 | B3 | A2−B2 | C2 | (A1−B1)×C1 |
| 4 | A4 | B4 | A3−B3 | C3 | (A2−B2)×C2 |
| 5 | — | — | A4−B4 | C4 | (A3−B3)×C3 |
| 6 | — | — | — | — | (A4−B4)×C4 |

*Marks: 1 for the configuration, 2 for a correct table showing fill and drain.*

**(b)** *(1)* The clock is set by the **slowest segment**:

| Segment | Time |
|---|---|
| 1 — read operands | 25 ns |
| 2 — subtract (35) + transfer into R3 (5) | 40 ns |
| 3 — multiply | **55 ns** |

> **tₚ = 55 ns**

**(c)** *(1)* With the interface registers removed the whole path is combinational:
25 + 35 + 55 = **tₙ = 115 ns**. (The 5 ns is the transfer *into R3*, and R3 is gone.)

**(d)** *(2)*
```
 n = 20 :  S = (20 × 115)  / ((3 + 20 − 1)  × 55) = 2300 / 1210  = 1.90
 n = 200:  S = (200 × 115) / ((3 + 200 − 1) × 55) = 23000 / 11110 = 2.07
```

**(e)** *(1)* Maximum speedup = tₙ / tₚ = 115 / 55 = **2.09**.

> It is not 3 because the segments are **unequal**: the 25 ns and 40 ns segments both sit idle waiting
> for the 55 ns multiplier, and the interface registers add time the non-pipelined path never pays.
> The ceiling k = 3 is reached only if every segment takes exactly tₙ/k.

*Full marks require the reason, not just the number.*

---
---

## After the paper — what your score means

| Score | Read it as |
|---|---|
| 24–30 | Solid. Move to spaced revision: redo the Self-test items you marked *with struggle* on the 3-day schedule |
| 18–23 | The method is there, the execution is not. Re-do every question you lost marks on **the same day**, then again tomorrow |
| 12–17 | One or two units are hollow. Find which from the table below and re-work that file's Build steps, not its Answers |
| < 12 | Do not re-sit this paper yet. Go back to the files whose Checks you cannot do from memory |

**Diagnose by question, not by total:**

| Lost marks on | The weak file is |
|---|---|
| A1, A3, B4 | **09** — microprogrammed control |
| A2, B2 | **04** — microoperations and signed arithmetic |
| B1 | **03** — RTL and the common bus |
| B3 | **06** and **07** — instruction format and traces |
| B2's status bits | **10** — program control and status bits |
| C1 | **11** — pipelining |

**Then re-test, don't re-read.** A question you got wrong and then fixed is worth more than a page you
re-read until it felt familiar. Familiarity is not recall.

---

## Where the rest of the practice is

This paper is 30 marks. The real bank is much larger:

| Source | Items |
|---|---|
| `../question-bank.md` P1 | 35 — the professor's own assignment questions |
| `../question-bank.md` P2 | 141 — Mano's end-of-chapter problems, chs. 2–9 |

The highest-value unattempted items, by unit:

- **U1** — Mano 4-13, 4-15, 4-16, 4-18, 4-20
- **U2** — Mano **5-10, 5-11** (the direct-MRI and ISZ-indirect traces — the twins of A2 Q7), 5-2, 5-5, 5-7, 5-22
- **U3** — Mano **7-4, 7-7, 7-11, 7-12, 7-21** and **8-25** *(U3 has no assignment coverage at all, so
  everything here is unattempted — it is the most exposed unit you have)*
- **U4** — Mano **9-4, 9-7** (the two unasked numericals), 9-2, 9-12–9-15
