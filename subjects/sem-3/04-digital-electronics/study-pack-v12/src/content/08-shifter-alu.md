# 08 — Shifts, barrel shifter, ALU

<div class="sub">Deck 07 (shifts slides 2–4, ALU slides 9–10) · syllabus Unit 2 · needs 04 (parallel adder, 2's complement) and 05 (MUX)</div>

## Map

[[map:1 Logical, circular, arithmetic shifts > 2 Barrel shifter > 3 Arithmetic logic unit|here=1]]

Two blocks of every processor's datapath, built from parts you already have: a barrel shifter is a row of 05's MUXes; an ALU is 04's adder with a MUX choosing what goes into its B input.

## The questions this file answers

- <span class="tag">Deck 07 slides 2–4</span> For 110110: logical shift left by 2, circular shift left by 2, arithmetic shift right by 1.
- <span class="tag">Deck 07 slides 9–10</span> Design an arithmetic circuit for add, subtract, increment and decrement.

---

## Build

### 1 · Shifts

:::q <span class="tag">Deck 07 slides 2–4</span>
For the word 110110 give (i) logical shift left by 2, (ii) circular shift left by 2, (iii) arithmetic shift right by 1.
:::

:::guess Guess first
110110 is negative in 2's complement. After a right shift, what must the new leftmost bit be to keep it negative?
:::

[[fig:shift_types|Logical, circular and arithmetic shifts.|w=75]]

| Shift | Empty places filled with | Meaning |
|---|---|---|
| Logical | 0 | left = × 2, right = ÷ 2 (unsigned) |
| Circular (rotate) | the bits that fell off the other end | nothing lost |
| Arithmetic | right: a copy of the sign bit; left: 0 | ÷ 2 keeping the sign (2's complement) |

**Answer.** (i) **011000**. (ii) **011011**: the 11 that leaves the left comes back on the right. (iii) **111011**: the sign bit is copied.

:::check Check 1
(a) Arithmetic shift right of 1001. What numbers are these in 2's complement? (b) Circular shift right by 1 of 110110.
:::

### 2 · The barrel shifter

:::guess Predict
A shift register (11) moves one place per clock. How could a circuit shift by 3 places in one step, with no clock?
:::

A **barrel shifter** is combinational: each output bit has a MUX, and the shift amount drives every select. 4-bit rotate-left:

| S_{1}S_{0} | Y_{3} Y_{2} Y_{1} Y_{0} |
|---|---|
| 00 | D_{3} D_{2} D_{1} D_{0} |
| 01 | D_{2} D_{1} D_{0} D_{3} |
| 10 | D_{1} D_{0} D_{3} D_{2} |
| 11 | D_{0} D_{3} D_{2} D_{1} |

[[fig:v1arg7|The MUX for Y_{0}.|w=40]]

**Answer.** One n:1 MUX per output bit (n MUXes), or log_{2}n rows of 2:1 MUXes shifting by 1, 2, 4, ….

:::check Check 2
How many 8:1 MUXes does an 8-bit barrel shifter need?
:::

### 3 · The arithmetic logic unit

:::q <span class="tag">Deck 07 slides 9–10</span>
Design an arithmetic circuit with inputs A and B that generates addition, subtraction, increment and decrement.
:::

:::guess Guess first
An adder computes A + (something) + carry-in. What "something" and carry-in give A − 1?
:::

Keep one parallel adder (04) and change its B input, Y. Two selects choose Y; C_{in} is a third control:

$$Y_{i} = B_{i}S_{0} + B_{i}'S_{1}      F = A + Y + C_{in}$$

| S_{1} S_{0} | Y | C_{in} = 0 | C_{in} = 1 |
|---|---|---|---|
| 0 0 | all 0s | A (transfer) | **A + 1 (increment)** |
| 0 1 | B | **A + B (add)** | A + B + 1 |
| 1 0 | B' | A + B' | **A − B (subtract)** |
| 1 1 | all 1s | **A − 1 (decrement)** | A (transfer) |

All 1s is −1 in 2's complement, so adding it decrements. Each stage: a full adder plus two ANDs and an OR for Y_{i}.

[[fig:alu_fig|One ALU stage: Y_{i} logic into a full adder.|w=60]]

A full ALU adds a logic unit (AND, OR, XOR, NOT) and a MUX per bit choosing arithmetic or logic; it outputs flags: **carry, zero, sign, overflow**.

**Answer.** The table: add (01, C_{in} 0), subtract (10, 1), increment (00, 1), decrement (11, 0).

:::check Check 3
(a) A = 0110, B = 0011, S_{1}S_{0} = 10, C_{in} = 1. Find F. (b) A = 0110, S_{1}S_{0} = 11, C_{in} = 0. Find F.
:::

---

## Exam form

**Shifts.** The three types with an example each.

**Barrel shifter.** Table and MUX per bit.

**ALU.** Y_{i} = B_{i}S_{0} + B_{i}'S_{1}; the 8-entry function table; stage diagram; flags.

## Traps

- Arithmetic left shift copying the sign: it fills with 0.
- Decrement with C_{in} = 1: that gives A again.
- Reading the circular shift as logical.

## Self-test

1. Logical shift right by 2 of 10110100.
2. Rotate left by 1 of 1001.
3. Arithmetic shift right by 1 of 0110. What is it in decimal?
4. ALU: A = 0101, S_{1}S_{0} = 00, C_{in} = 1. F?
5. ALU: A = 0101, B = 0010, S_{1}S_{0} = 01, C_{in} = 0. F?
6. Why is all 1s the right Y for decrement?

<!--ANSWERS-->

## Answers

**Check 1.** (a) **1100**: 1001 = −7, 1100 = −4 (÷ 2, rounded down). (b) **011011**.

**Check 2.** **Eight**.

**Check 3.** (a) Y = 1100; 0110 + 1100 + 1 = 1 0011: **F = 0011** (6 − 3). (b) Y = 1111; 0110 + 1111 = 1 0101: **F = 0101** (6 − 1).

**Self-test.**

1. **00101101**.
2. **0011**.
3. **0011** = 3 (6 ÷ 2).
4. **0110** (increment).
5. **0111** (5 + 2).
6. All 1s is −1 in 2's complement, so A + 1111 = A − 1 (carry discarded).

<!--/ANSWERS-->
