# 08 — Shifts, barrel shifter, ALU

<div class="sub">Deck 07 (slides 1–10) · syllabus Unit 2 (shifter, ALU) · no exam question yet; deck examples EX 7.2–7.4 (shifts of 110110), EX 7.9–7.10 (arithmetic circuit) · needs 04 steps 5 and 12 (ripple adder, A − B = A + B' + 1), 05 steps 1–2 (2:1 and 4:1 MUX)</div>

## Map

[[map:1 Logical shift > 2 Circular shift > 3 Arithmetic shift > 4 Barrel shifter > 5 Logic unit > 6 Arithmetic circuit > 7 Choosing the operation > 8 The ALU|here=1]]

File 04 ended with one ripple adder that adds or subtracts, depending on what reaches its B inputs. This file builds the two blocks every processor's datapath is made of: a **shifter**, which moves the bits of a word sideways, and an **arithmetic logic unit (ALU)**, which is 04's adder plus file 05's multiplexers choosing what it computes. Shift registers (file 11) do the same shifts one place per clock; here they happen at once, with no clock.

## Symbols

| Symbol | What it means in this file | Typical value |
|---|---|---|
| n | the number of bits in the word | 6 (deck 07), 4, 8 |
| serial input | the bit that enters the empty end of the word during a shift; the three shift types differ only in this bit | 0, the bit that fell out, or the sign bit |
| sign bit | the leftmost bit of a 2's-complement number: 1 means negative | — |
| s (S_{1}S_{0}) | shift amount of the barrel shifter, as a binary number | 0–3 for 4 bits |
| D_{3} … D_{0}, Y_{3} … Y_{0} | barrel shifter: data in, data out | — |
| S_{1}S_{0} | logic unit select: which of NOT, AND, OR, XOR reaches the output | 00–11 |
| S, C_{in} | arithmetic circuit selects: S and the adder's carry in; together they pick +B, +1, −1, −B | 0 or 1 |
| X_{i}, Y_{i} | the two inputs of full adder i in the arithmetic circuit (X_{i} = A_{i}; Y_{i} from the MUX) | — |
| M | mode: 0 arithmetic, 1 logic (step 8) | 0 or 1 |
| F | ALU output word | — |

## Running example

**Shifts: the 6-bit word 110110** (deck 07 EX 7.2–7.4; as a 2's-complement number, −10). **Arithmetic and ALU: A = 0110 (6), B = 0011 (3).** Steps 1–3 shift 110110 every way the deck does; steps 5–8 put A and B through every operation.

## The questions this file answers

- <span class="tag">Deck 07 slide 2 (EX 7.2)</span> Logical shift of 110110 left by 2 and right by 1.
- <span class="tag">Deck 07 slide 3 (EX 7.3)</span> Circular shift of 110110 left by 2 and right by 1.
- <span class="tag">Deck 07 slide 4 (EX 7.4)</span> Arithmetic shift of 110110 right by 1 and left by 2.
- <span class="tag">Deck 07 slides 9–10 (EX 7.9, 7.10)</span> Design an arithmetic circuit with inputs A and B that generates addition, subtraction, increment and decrement; draw the first two stages.

---

## Build

### 1 · Logical shift: fill with 0

Write 0350 and move every digit one place left: 3500, ten times bigger. A binary shift does the same with ×2, and the only question is what goes into the empty place.

:::q <span class="tag">Deck 07 slides 1–2 (EX 7.2)</span>
Shift 110110 logically (i) left by 2 places, (ii) right by 1 place.
:::

:::guess Guess first
Shifting left by 2 empties two places on the right. What goes into them?
:::

:::note Terms
**Shift:** every bit moves the same number of places left or right; bits pushed past the end are lost. **Serial input:** the bit that enters the emptied place (slide 1: the three kinds of shift differ only in this). **Logical shift:** the serial input is always 0.
:::

[[fig:shift_types|The three shifts on one register (deck 07 slides 2–4). Logical: 0 enters. Circular: the bit leaving one end enters the other. Arithmetic right: the sign bit is copied into itself.|w=75]]

Left by 2, one line per place (slide 2):

1. 110110 → drop the two leftmost bits 1, 1 → 0110 _ _.
2. Fill the two right places with 0 → **011000**.

Right by 1: drop the rightmost 0 → _ 11011 → fill with 0 → **011011**.

For an unsigned number, each place left is × 2 and each place right is ÷ 2 (rounded down), as long as no 1 is pushed out: 0011 (3) shifted left 1 is 0110 (6). In 110110 two 1s fall off the left, so the result is not 54 × 4.

**Answer to the Guess.** **0s**: 110110 → **011000**; right by 1 → **011011**.

:::check Check 1
(a) Logical shift right by 2 of 10110100. (b) 00001101 (13) logically shifted left by 1: the result, and its decimal value.
:::

### 2 · Circular shift: nothing is lost

Step 1 threw away the bits pushed out. A circular shift (also called rotate) feeds them back into the other end.

:::q <span class="tag">Deck 07 slide 3 (EX 7.3)</span>
Circular-shift 110110 (i) left by 2, (ii) right by 1.
:::

:::guess Guess first
Left by 2: the two bits leaving on the left are 1 and 1. Where do they reappear?
:::

:::note Terms
**Circular shift (rotate):** the serial input is the bit shifted out of the other end of the register (slide 3), so the word turns like a ring.
:::

1. Left by 2: 110110 → the leading 11 leaves → 0110 _ _ → 11 enters on the right → **011011**.
2. Right by 1: the trailing 0 leaves → _ 11011 → 0 enters on the left → **011011**.

Both answers are 011011. That is a property of this word, not of rotation: 110110 is 110 written twice, so turning it by 1 to the right lands on the same word as turning it by 2 to the left. A 6-bit rotate by 6 places always gives the word back.

**Answer to the Guess.** On the **right**, in the same order: **011011**.

:::check Check 2
(a) Rotate 1001 left by 1. (b) Rotate 1011 right by 1, then left by 1. What do you get back?
:::

### 3 · Arithmetic shift: keep the sign

A logical right shift halves an unsigned number. For a negative 2's-complement number it fails: 110110 (−10) logically shifted right gives 011011 (+27). The arithmetic shift fixes the sign.

:::q <span class="tag">Deck 07 slide 4 (EX 7.4)</span>
Arithmetic-shift 110110 (i) right by 1, (ii) left by 2.
:::

:::guess Guess first
110110 is negative (sign bit 1). After a right shift, what must the new leftmost bit be for the result to stay negative?
:::

:::note Terms
**Sign bit:** the leftmost bit of a 2's-complement number; 1 = negative. **Arithmetic shift:** right, the serial input is a copy of the sign bit; left, it is 0, as in a logical shift (slide 4).
:::

1. Right by 1: _ 11011, and the sign bit 1 is copied into the empty place → **111011**.
2. Check by value: 110110 = −32 + 16 + 4 + 2 = −10; 111011 = −32 + 16 + 8 + 2 + 1 = −5. **÷ 2, sign kept**.
3. Left by 2: the same as logical → **011000** = +24.

−10 × 4 = −40 does not fit in 6 bits (the range is −32 to +31), so the left shift **overflows**: the sign bit changed from 1 to 0, which is how an arithmetic left shift shows overflow.

**Answer to the Guess.** **1**, a copy of the old sign bit: 110110 → **111011** (−5).

:::check Check 3
(a) Arithmetic shift right of 1001 (4-bit). What numbers are 1001 and the result? (b) Arithmetic shift right of 0110: result and value.
:::

### 4 · The barrel shifter: any shift in one step

Steps 1–3 moved bits one place at a time, as a shift register (file 11) does, one place per clock. A shift by 3 would take three clocks.

:::q <span class="tag">Predict</span>
Build a 4-bit circuit with no clock that rotates D_{3}D_{2}D_{1}D_{0} left by any amount s = 0, 1, 2 or 3 in one step. What does each output bit need?
:::

:::guess Guess first
Output Y_{0} gets a different input bit for each of the four shift amounts. Which block from file 05 picks one of four inputs with a 2-bit code?
:::

:::note Terms
**Barrel shifter:** a combinational circuit that shifts or rotates a word by any amount in one step; the amount is a binary number on its select lines (slide 3 names it with the circular shift).
:::

Rotate left by s: output bit i takes input bit (i − s), counted round the ring.

| S_{1}S_{0} (s) | Y_{3} | Y_{2} | Y_{1} | Y_{0} |
|---|---|---|---|---|
| 00 (0) | D_{3} | D_{2} | D_{1} | D_{0} |
| 01 (1) | D_{2} | D_{1} | D_{0} | D_{3} |
| 10 (2) | D_{1} | D_{0} | D_{3} | D_{2} |
| 11 (3) | D_{0} | D_{3} | D_{2} | D_{1} |

Each **column** is one 4:1 MUX: the column lists its data inputs I_{0}…I_{3} in order, and S_{1}S_{0} drives all four MUXes together.

[[fig:barrel4|4-bit rotate-left barrel shifter: four 4:1 MUXes, one per output bit, sharing the selects S_{1}S_{0}. Each MUX's inputs I_{0}–I_{3} are the four data bits in the order of its column in the table.|w=80]]

An n-bit barrel shifter needs n MUXes of n:1. A different shift type only changes the wiring: a logical shift wires 0 where the rotate wires a wrapped-round bit.

**Answer to the Predict.** One **4:1 MUX per output bit** (four in all), selects on s. Y_{0}'s MUX has inputs D_{0}, D_{3}, D_{2}, D_{1}.

:::check Check 4
(a) D_{3}D_{2}D_{1}D_{0} = 1011, S_{1}S_{0} = 10. Give Y_{3}Y_{2}Y_{1}Y_{0}. (b) How many MUXes, and of what size, does an 8-bit barrel shifter need?
:::

### 5 · The logic unit: a MUX picks the operation

Step 4 used a MUX to pick one of four bits. Slide 8 uses one to pick one of four **operations**: every gate computes at once, and the select lines decide which answer is passed on.

:::q <span class="tag">Deck 07 slide 8</span>
Design a 1-bit logic unit that gives A', AB, A + B or A ⊕ B, chosen by S_{1}S_{0}.
:::

:::guess Guess first
A = 0, B = 1. Which of the four operations give 1?
:::

:::note Terms
**Logic unit (LU):** computes a bitwise logic operation; bit i of the output depends only on bit i of A and B. **Function select S_{1}S_{0}:** the MUX select lines; their code names the operation.
:::

[[fig:lu41|1-bit logic unit (deck 07 slide 8): NOT, AND, OR and XOR gates all fed by A and B, into inputs I_{0}–I_{3} of a 4:1 MUX; S_{1}S_{0} choose; output Y.|w=62]]

| S_{1}S_{0} | Output | Operation |
|---|---|---|
| 00 | A' | complement |
| 01 | AB | AND |
| 10 | A + B | OR |
| 11 | A ⊕ B | XOR |

For a 4-bit word, four copies, one per bit, share S_{1}S_{0}. Running example A = 0110, B = 0011: NOT A = 1001, AND = 0010, OR = 0111, XOR = 0101.

:::note Slip in the slides
Slide 8 is titled "1-bit ALU design", but the circuit has no adder: it is a 1-bit **logic** unit. The arithmetic half is slides 9–10 (step 6); step 8 joins them into an ALU.
:::

**Answer to the Guess.** A' = 1, AB = 0, A + B = 1, A ⊕ B = 1: **NOT, OR and XOR** give 1.

:::check Check 5
A = 1010, B = 1100 (4 copies of the unit). Give the output for S_{1}S_{0} = 01 and for 11.
:::

### 6 · The arithmetic circuit: change what the adder adds

File 04 step 12 subtracted by feeding B' into the adder with carry in 1. Slides 9–10 generalise this: one ripple adder, and a MUX per bit choosing what goes into its second input.

:::q <span class="tag">Deck 07 slides 9–10 (EX 7.9, 7.10)</span>
Design an arithmetic circuit with inputs A and B that generates A + B, A + 1, A − 1 and A − B. Draw the logic diagram for the first two stages.
:::

:::guess Guess first
An adder computes A + Y + C_{in}. Which word Y, with which C_{in}, gives A − 1?
:::

:::note Terms
**X_{i}, Y_{i}:** the two inputs of full adder i; X_{i} = A_{i}, Y_{i} comes from a 4:1 MUX. **S, C_{in}:** the MUX selects (S_{1} = S, S_{0} = C_{in}); the same C_{in} is the adder's carry into bit 0.
:::

Four things can go into Y: B, all 0s, all 1s, or B'. With C_{in}, each gives one operation (slide 10's table):

| S | C_{in} | Y | F = A + Y + C_{in} | Operation |
|---|---|---|---|---|
| 0 | 0 | B | A + B | add |
| 0 | 1 | 0000 | A + 1 | increment |
| 1 | 0 | 1111 | A + 1111 = A − 1 | decrement |
| 1 | 1 | B' | A + B' + 1 = A − B | subtract |

Why 1111 decrements: 1111 is −1 in 4-bit 2's complement, so adding it subtracts 1 (the carry out is discarded).

[[fig:arith2|First two stages of the arithmetic circuit (deck 07 slide 10). In each stage a 4:1 MUX, selects S and C_{in}, chooses Y_{i} from B_{i}, 0, 1, B_{i}'; full adder i adds X_{i} = A_{i} and Y_{i}; C_{0} = C_{in}, C_{1} passes from stage 0 to stage 1.|w=82]]

Running example, A = 0110, B = 0011:

| S C_{in} | A + Y + C_{in} | F | Check |
|---|---|---|---|
| 00 | 0110 + 0011 + 0 | 1001 | 6 + 3 = 9 |
| 01 | 0110 + 0000 + 1 | 0111 | 6 + 1 = 7 |
| 10 | 0110 + 1111 + 0 = 1 0101 | 0101 | 6 − 1 = 5 |
| 11 | 0110 + 1100 + 1 = 1 0011 | 0011 | 6 − 3 = 3 |

**Answer to the Guess.** **Y = 1111** (all 1s, = −1) with **C_{in} = 0**.

:::check Check 6
(a) A = 1010, B = 0111, S C_{in} = 11. Give Y and F. (b) A = 0000, S C_{in} = 10. Give F and say what it means.
:::

### 7 · Why these four codes

Step 6's table looks arbitrary. It follows from asking, for each of the four Y words, which carry in gives a useful result.

:::q <span class="tag">Predict</span>
Swap C_{in} in every row of step 6's table. Which four operations do you get, and why did the slide not use them?
:::

:::guess Guess first
Y = B with C_{in} = 1 gives A + B + 1. Is that one of the four operations asked for?
:::

| Y | C_{in} = 0 | C_{in} = 1 |
|---|---|---|
| B | **A + B** | A + B + 1 |
| 0000 | A (transfer) | **A + 1** |
| 1111 | **A − 1** | A (transfer) |
| B' | A − B − 1 | **A − B** |

Each Y gives two results, one per C_{in}. The slide keeps the one that is a named operation (bold) and drops the other; that is why C_{in} doubles as a select line. With a 4:1 MUX on S and C_{in}, each of the four codes picks both Y and C_{in} in one go.

**Answer to the Predict.** A + B + 1, A (twice: transfer) and A − B − 1. None of them is among the four required operations.

:::check Check 7
Which (Y, C_{in}) pairs pass A through unchanged, and why does each one work?
:::

### 8 · The ALU: arithmetic and logic behind one more MUX

Steps 5 and 6 each give four operations from two selects. Slide 5's ALU is both units side by side, with one more choice: arithmetic or logic.

:::q <span class="tag">Deck 07 slides 5–7</span>
Join step 5's logic unit and step 6's arithmetic circuit into one ALU. How many select lines does it need, and what does each code do?
:::

:::guess Guess first
Each unit already takes a 2-bit code. How many more select lines choose between the two units?
:::

:::note Terms
**ALU:** computes one arithmetic or logic operation on two words, chosen by select lines; the arithmetic unit, the logic unit and the control that chooses are its parts (slide 5). **Mode M:** 0 passes the arithmetic result, 1 the logic result, through a 2:1 MUX per bit.
:::

[[fig:alu_block|One bit of the ALU: the arithmetic stage (MUX + full adder, step 6) and the logic unit (step 5) share the two code lines; a 2:1 MUX on M passes one result to F_{i}. The carry runs only through the arithmetic stages.|w=78]]

The two code lines are shared: for M = 0 they are S, C_{in}; for M = 1 they are S_{1}S_{0}.

| M | code | F | | M | code | F |
|---|---|---|---|---|---|---|
| 0 | 00 | A + B | | 1 | 00 | A' |
| 0 | 01 | A + 1 | | 1 | 01 | A AND B |
| 0 | 10 | A − 1 | | 1 | 10 | A OR B |
| 0 | 11 | A − B | | 1 | 11 | A XOR B |

Three select lines, 2^{3} = 8 operations. Slide 7 lists further ALU jobs (multiplication by repeated addition, shifts and rotations): in practice they are added the same way, as another input to the output MUX, for example a barrel shifter from step 4.

**Answer to the Guess.** **One** (M): three select lines, eight operations.

:::check Check 8
A = 0110, B = 0011. Give F for (a) M = 1, code 10, and (b) M = 0, code 01. (c) Which two codes give the same F for this A and B?
:::

---

## Exam form

**Shifts** (EX 7.2–7.4, word 110110):

| Shift | Serial input | Left 2 | Right 1 |
|---|---|---|---|
| Logical | 0 | 011000 | 011011 |
| Circular | the bit leaving the other end | 011011 | 011011 |
| Arithmetic | right: copy of the sign bit; left: 0 | 011000 | 111011 |

Logical left/right = × 2 / ÷ 2 unsigned; arithmetic right = ÷ 2 keeping the sign; arithmetic left overflows if the sign bit changes.

**Barrel shifter.** Table of Y against S_{1}S_{0}; one n:1 MUX per output bit, each column of the table = one MUX's inputs.

**Arithmetic circuit (EX 7.9–7.10).**

1. Per bit: a 4:1 MUX with selects S, C_{in} and inputs B_{i}, 0, 1, B_{i}'; its output Y_{i} into full adder i with X_{i} = A_{i}.
2. C_{0} = C_{in}, carries ripple.
3. Table: 00 A + B · 01 A + 1 · 10 A − 1 · 11 A − B.
4. Draw stages 0 and 1.

**Logic unit and ALU.** 4:1 MUX on NOT, AND, OR, XOR (S_{1}S_{0}); ALU = both units + a 2:1 MUX per bit on M; 8-row function table.

## Traps

- Arithmetic **left** shift copying the sign bit: it fills with 0.
- Arithmetic right shift filling with 0: that is the logical shift and turns a negative number positive.
- Reading a circular shift as logical: the leaving bits come back, nothing is lost.
- Decrement with C_{in} = 1: A + 1111 + 1 gives A back.
- Calling slide 8's circuit an ALU: it has no adder (logic unit only).
- Giving a barrel shifter a clock: it is combinational, one step for any amount.

## Self-test

1. Logical shift right by 2 of 10110100.
2. Rotate left by 1 of 1001.
3. Arithmetic shift right by 1 of 0110. Give the result in decimal.
4. Arithmetic circuit: A = 0101, S C_{in} = 01. F?
5. Arithmetic circuit: A = 0101, B = 0010, S C_{in} = 00. F?
6. Why does Y = 1111 with C_{in} = 0 decrement A? One line.
7. In the 4-bit rotate-left barrel shifter, list the inputs I_{0}–I_{3} of the MUX for Y_{2}.
8. The 6-bit word 011000 is arithmetically shifted right by 3. Result and decimal values before and after?

<!--ANSWERS-->

## Answers

**Check 1.** (a) **00101101**. (b) **00011010** = 26 (13 × 2).

**Check 2.** (a) **0011**. (b) 1011 → right 1 → **1101** → left 1 → **1011**: the original word.

**Check 3.** (a) 1001 = −8 + 1 = **−7**; result **1100** = −8 + 4 = **−4** (÷ 2 rounded down, towards −∞). (b) **0011** = 3 (6 ÷ 2).

**Check 4.** (a) Rotate left by 2: Y_{3} = D_{1} = 1, Y_{2} = D_{0} = 1, Y_{1} = D_{3} = 1, Y_{0} = D_{2} = 0: **1110**. (b) **Eight 8:1 MUXes**.

**Check 5.** 01 (AND): **1000**. 11 (XOR): **0110**.

**Check 6.** (a) Y = B' = **1000**; 1010 + 1000 + 1 = 1 0011: **F = 0011** (10 − 7 = 3). (b) 0000 + 1111 + 0 = **1111**: −1 in 2's complement (or 15 if read unsigned: 0 − 1 wraps round).

**Check 7.** **Y = 0000, C_{in} = 0** (A + 0 + 0) and **Y = 1111, C_{in} = 1** (A − 1 + 1).

**Check 8.** (a) A OR B = **0111**. (b) A + 1 = **0111**. (c) **These two**: M = 1 code 10 (OR) and M = 0 code 01 (increment) both give 0111.

**Self-test.**

1. **00101101**.
2. **0011**.
3. **0011** = 3 (6 ÷ 2).
4. A + 1 = **0110**.
5. A + B = **0111** (5 + 2).
6. 1111 is −1 in 2's complement, so A + 1111 = A − 1 (the carry out is discarded).
7. Y_{2} column of the table: **D_{2}, D_{1}, D_{0}, D_{3}**.
8. **000011**; 011000 = 24, 000011 = 3 (24 ÷ 8). The sign bit is 0, so 0s enter.

<!--/ANSWERS-->
