# 04 — Adders and subtractors

<div class="sub">Deck 03 (slides 1–28) · syllabus Unit 1 (half and full adders, subtractors, parallel adders, BCD adder) · no exam question yet; deck examples EX 3.4–3.23; MTE 2025 Q6 (file 06) builds this file's full adder from a decoder · needs 01 step 3 (XOR), 01 step 7 (minterms), 02 steps 2–4 (three-variable K-map), 03 step 7 (XOR from NAND)</div>

## Map

[[map:1 Half adder > 2 Full adder table > 3 Carry on a K-map > 4 Two half adders > 5 Ripple-carry adder > 6 Ripple delay > 7 Carry look-ahead > 8 NAND and NOR adders > 9 Half subtractor > 10 Full subtractor > 11 One cell, add or subtract > 12 Subtract by adding > 13 BCD adder|here=1]]

Files 01–03 ended with gates, minimised expressions and NAND-only circuits. This file uses them on the first real job a computer does: adding. Two bits give a half adder; a third bit (the carry from the column to the right) gives a full adder; a row of full adders adds whole numbers. The rest of the file makes that row faster (look-ahead), turns it round (subtraction) and makes it decimal (BCD). File 06 builds the same full adder from a decoder (MTE Q6), file 08 puts the adder inside an ALU, and file 16 step 12 builds a one-adder serial version.

## Symbols

| Symbol | What it means in this file | Typical value |
|---|---|---|
| A, B (A_{i}, B_{i}) | the two bits being added (bit i of the two numbers; i = 0 is the rightmost) | 0 or 1 |
| S (S_{i}) | sum bit: the bit written in the answer's column | 0 or 1 |
| C, C_{out} (C_{i+1}) | carry out: the 1 passed to the next column to the left, worth 2 in this column | 0 or 1 |
| C_{in} (C_{i}) | carry in: the carry arriving from the column to the right; C_{0} is the carry into bit 0 | 0 or 1 |
| G_{i}, P_{i} | generate A_{i}B_{i}, propagate A_{i} ⊕ B_{i} (step 7) | 0 or 1 |
| T | one gate delay: the time one gate takes to respond (deck 03's unit) | ns |
| D | difference bit of a subtractor | 0 or 1 |
| b_{out}, b_{in} | borrow out (this column took 2 from the next column left), borrow in (the column to the right took one from this one) | 0 or 1 |
| E, M | mode controls: E = 0 add, 1 subtract in the controlled cell (step 11); M the same for the 2's-complement adder–subtractor (step 12) | 0 or 1 |
| K, Z, Y | BCD adder: carry and sum of the first binary adder, and the "add 6" signal (step 13) | — |

## Running example

**Deck 03 slide 18: A = 1011 (eleven), B = 1110 (fourteen).** Step 5 adds them in a ripple adder (25 = 1 1001), step 7 finds their generate and propagate bits, step 12 subtracts them (11 − 14 = −3). Single-column steps use rows of the same numbers.

## The questions this file answers

- <span class="tag">Deck 03 slides 4–8 (EX 3.4, 3.8)</span> Add two single bits: truth table, sum and carry, half-adder circuit.
- <span class="tag">Deck 03 slides 9–13 (EX 3.13)</span> Full adder: truth table, minimal S and C_{out}, built from two half adders.
- <span class="tag">Deck 03 slides 15–20 (EX 3.15–3.18)</span> Add 1011 and 1110 in a 4-bit adder; delay of an n-bit ripple-carry adder; carry look-ahead.
- <span class="tag">Deck 03 slides 21–28 (EX 3.23)</span> NAND/NOR adders; half and full subtractor; one circuit that adds or subtracts.

---

## Build

### 1 · Adding two bits: the half adder

Add 7 + 5 by hand: 7 + 5 = 12, so you write 2 and carry 1 to the next column. Binary is the same with only two digits, and the carry comes sooner.

:::q <span class="tag">Deck 03 slides 4–8 (EX 3.4, 3.8)</span>
Add two single binary digits A and B. Give the truth table with outputs Sum and Carry, their Boolean expressions, and the circuit.
:::

:::guess Guess first
1 + 1 in binary is "10". Which digit of "10" is written in the column, and which one is carried?
:::

:::note Terms
**Sum S:** the bit written in this column (worth 1). **Carry C:** the bit passed to the next column (worth 2). **Half adder:** a circuit that adds exactly two bits, with no carry coming in.
:::

| A | B | A + B | C | S |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 2 = "10" | 1 | 0 |

Read the columns: S is 1 when **exactly one** input is 1, which is XOR (file 01 step 3). C is 1 only when **both** are 1, which is AND.

$$S = A ⊕ B      C = A·B$$

[[fig:half_adder|Half adder (deck 03 slide 7): one XOR for the sum, one AND for the carry, both fed by A and B.|w=50]]

**Answer to the Guess.** The **0** is written (S = 0) and the **1** is carried (C = 1): 1 + 1 = 2 = one 2 and no 1.

:::check Check 1
(a) A = 1, B = 0: give C and S. (b) Why is a half adder enough for bit 0 of a sum but not for bit 1?
:::

### 2 · Three bits in a column: the full adder table

Step 1's Check (b) found the problem: every column except the rightmost may also receive a carry. A column therefore adds three bits.

:::q <span class="tag">Deck 03 slides 9, 13 (EX 3.13)</span>
A full adder adds A, B and the carry in C_{in}. Write its truth table.
:::

:::guess Guess first
1 + 1 + 1 = ? Write it as a 2-bit binary number and read off C_{out} and S.
:::

:::note Terms
**Full adder:** adds three bits (A, B and the carry in C_{in}) and outputs a sum S and a carry out C_{out}. **Carry in C_{in}:** the carry arriving from the column to the right.
:::

| Row | A B C_{in} | count of 1s | C_{out} S |
|---|---|---|---|
| 0 | 0 0 0 | 0 | 0 0 |
| 1 | 0 0 1 | 1 | 0 1 |
| 2 | 0 1 0 | 1 | 0 1 |
| 3 | 0 1 1 | 2 | 1 0 |
| 4 | 1 0 0 | 1 | 0 1 |
| 5 | 1 0 1 | 2 | 1 0 |
| 6 | 1 1 0 | 2 | 1 0 |
| 7 | 1 1 1 | 3 | 1 1 |

The output pair C_{out}S is just the count of 1s written in binary (0 = 00, 1 = 01, 2 = 10, 3 = 11). So:

1. S = 1 when the count is odd (1 or 3): rows **Σm(1, 2, 4, 7)**.
2. C_{out} = 1 when the count is 2 or more: rows **Σm(3, 5, 6, 7)**. "Two or more of three" is called the **majority** function.

An odd count of 1s is what a chain of XORs detects, so **S = A ⊕ B ⊕ C_{in}** (deck 03 slide 11).

**Answer to the Guess.** 1 + 1 + 1 = 3 = **11**: C_{out} = 1, S = 1 (row 7).

:::check Check 2
(a) Row A = 1, B = 0, C_{in} = 1 (row 5): give C_{out} and S. (b) Bit 2 of the running example adds A_{2} = 0, B_{2} = 1 and a carry in of 1. Give C_{out} and S.
:::

### 3 · The carry on a K-map

Step 2 gave C_{out} as four minterms. Four 3-literal terms cost four AND gates; a K-map (file 02 steps 2–4) shrinks it.

:::q <span class="tag">Deck 03 slide 10</span>
Minimise the carry out C_{out} = Σm(3, 5, 6, 7) of the full adder.
:::

:::guess Guess first
Cell 7 (A = B = C_{in} = 1) is next to how many other 1-cells on the map?
:::

[[fig:fa_kmaps|What this graph plots: two 3-variable K-maps, A down the side and B C_{in} across in Gray order 00, 01, 11, 10. One cell = one row of step 2's table; a loop = one product term. Left, S: the 1s sit on a checkerboard, no two side by side, so no loop forms. Right, C_{out}: three pairs, each sharing cell 7.|w=80]]

Cell 7 touches cells 3, 5 and 6, and each of those is a 1. Each pair drops the one variable that changes inside it (file 02 step 3):

| Pair | Variable that changes | Term |
|---|---|---|
| 6, 7 | C_{in} | AB |
| 3, 7 | A | BC_{in} |
| 5, 7 | B | AC_{in} |

$$C_{out} = AB + BC_{in} + AC_{in}$$

Read it back: "carry when **any two** inputs are 1". S cannot be shortened on a map: on a checkerboard every 1 is alone, so S stays as the 3-input XOR of step 2.

**Answer to the Guess.** **Three** (cells 3, 5, 6), which is why three pairs overlap at cell 7.

:::check Check 3
(a) How many 2-input gates does C_{out} = AB + BC_{in} + AC_{in} need (count the 3-input OR as one gate)? (b) Use the expression to find C_{out} for A = 0, B = 1, C_{in} = 1.
:::

### 4 · A full adder from two half adders

Step 3 built C_{out} from scratch. Deck 03 slides 11–12 reuse step 1's half adder instead: add A and B first, then add the carry in.

:::q <span class="tag">Deck 03 slides 11–12</span>
Build a full adder from two half adders and one OR gate, and show that it gives the same S and C_{out}.
:::

:::guess Guess first
Can both half adders produce a carry of 1 for the same inputs? Try A = B = C_{in} = 1.
:::

[[fig:full_adder_2ha|Full adder from two half adders (deck 03 slides 11–12). Half adder 1 adds A and B; half adder 2 adds its sum to C_{in}; the OR gate joins the two carries.|w=70]]

Name the inner signals and follow them, one line each:

1. Half adder 1: s_{1} = A ⊕ B, c_{1} = AB.
2. Half adder 2: S = s_{1} ⊕ C_{in} = A ⊕ B ⊕ C_{in} (step 2's sum).
3. Half adder 2's carry: c_{2} = s_{1}C_{in} = (A ⊕ B)C_{in}.
4. C_{out} = c_{1} + c_{2} = **AB + (A ⊕ B)C_{in}**.
5. Expand A ⊕ B = AB' + A'B: C_{out} = AB + AB'C_{in} + A'BC_{in}, which is 1 on rows 6, 7 (AB), 5 and 3: the same Σm(3, 5, 6, 7) as step 3.

Why an OR and not an adder for the two carries: c_{1} = 1 needs A = B = 1, which makes s_{1} = 0 and so c_{2} = 0. The two carries are never 1 together, so OR gives their sum.

**Answer to the Guess.** **No.** For 1, 1, 1: s_{1} = 0, c_{1} = 1, c_{2} = 0 · 1 = 0. C_{out} = 1, S = 0 ⊕ 1 = 1 (row 7 of step 2 ✓).

:::check Check 4
For A = 0, B = 1, C_{in} = 1 give s_{1}, c_{1}, c_{2}, S and C_{out}.
:::

### 5 · Adding words: the ripple-carry adder

One full adder adds one column. A 4-bit number has four columns, so four full adders are chained, each one's carry out feeding the next one's carry in.

:::q <span class="tag">Deck 03 slides 15–18 (EX 3.15–3.18)</span>
Add A = 1011 (eleven) and B = 1110 (fourteen) in a 4-bit adder made of four full adders. Show every carry.
:::

:::guess Guess first
11 + 14 = 25 does not fit in 4 bits (largest 1111 = 15). Where does the fifth bit of the answer come out?
:::

:::note Terms
**Ripple-carry adder (parallel adder):** n full adders in a row; stage i adds A_{i}, B_{i} and C_{i}, and its C_{i+1} is the next stage's carry in. C_{0} = 0 for plain addition. The sum of two n-bit numbers needs n + 1 bits (slide 14): the last carry C_{n} is the extra bit.
:::

[[fig:ripple_adder|4-bit ripple-carry adder (deck 03 slide 17): bit 0 on the right, C_{0} = 0 into it, each carry passed left, C_{out} = C_{4} the fifth bit of the sum.]]

Work right to left, one full adder (step 2's table) per column:

| Stage i | A_{i} | B_{i} | C_{i} | count | C_{i+1} | S_{i} |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 | 2 | 1 | 0 |
| 2 | 0 | 1 | 1 | 2 | 1 | 0 |
| 3 | 1 | 1 | 1 | 3 | 1 | 1 |

Result C_{4}S_{3}S_{2}S_{1}S_{0} = 1 1001 = 16 + 8 + 1 = 25 ✓. File 16 step 12 does the same sum with one full adder used four times (the serial adder).

**Answer to the Guess.** As the last carry, **C_{4} = 1**: the answer is **1 1001** (25).

:::check Check 5
Deck 03 slide 15: add A = 0101 (5) and B = 0111 (7). Give C_{1}–C_{4} and S_{3}…S_{0}.
:::

### 6 · How long the ripple takes

Step 5 worked the stages right to left, and the hardware has to do the same: stage 3 cannot finish until stage 2's carry arrives.

:::q <span class="tag">Deck 03 slide 19</span>
Assume every gate has delay T. How long does a 4-bit ripple-carry adder take, and what is the delay of an n-bit one?
:::

:::guess Guess first
In a full adder built from two half adders (step 4), how many gates does a carry pass through on its way from C_{in} to C_{out}?
:::

:::note Terms
**Gate delay T:** the time from a gate's input changing to its output changing. **Carry path:** the gates a carry passes through from C_{i} to C_{i+1}; in step 4's circuit, half adder 2's AND and then the OR, so **2T per stage**.
:::

Time every signal from the moment A, B and C_{0} are applied (t = 0), counting gates on the slowest path (slide 19's counting):

1. Stage 0: s_{1} = A_{0} ⊕ B_{0} is ready at 1T (one XOR; this is slide 19's "1 delay from the first half adder").
2. C_{1} = A_{0}B_{0} + s_{1}C_{0}: the AND waits for s_{1} (2T), the OR adds one (**3T**).
3. Every later stage already has its own A_{i} ⊕ B_{i} (ready at 1T); it only waits for the carry: AND + OR = 2T more. C_{2} at 5T, C_{3} at 7T, **C_{4} at 9T**.
4. In general C_{n} is ready at 1T + 2T × n = **(2n + 1)T**. The last sum bit S_{n−1} = s_{1} ⊕ C_{n−1} is ready at 2nT, one T earlier, so C_{n} is the last output.

| n | 1 | 4 | 8 | 16 |
|---|---|---|---|---|
| delay (2n + 1)T | 3T | 9T | 17T | 33T |

The delay grows in proportion to n: doubling the word length almost doubles the time. The IIT Kharagpur virtual lab and LSU EE 3755 notes count the same 2 gate levels per stage, 2n for the carry chain; texts differ only in what they add for the first and last gates.

**Answer to the Guess.** **Two** (an AND and an OR), so each stage adds 2T; the 4-bit adder takes **9T** (slide 19: "8T to compute the last carry, + 1 = 9T").

:::check Check 6
(a) Delay of a 32-bit ripple-carry adder? (b) At what time is C_{2} ready in a 4-bit adder?
:::

### 7 · Carry look-ahead

Step 6's delay comes from each stage waiting for the one before. Slide 20's fix: compute every carry straight from the inputs and C_{0}, so no stage waits.

:::q <span class="tag">Deck 03 slide 20</span>
How does a carry look-ahead adder remove the ripple delay? Write C_{1} to C_{4} in terms of the inputs and C_{0}.
:::

:::guess Guess first
Stage i receives a carry in of 1. For which A_{i}, B_{i} does that carry pass through to C_{i+1}? For which does stage i make a carry on its own?
:::

:::note Terms
**Generate G_{i} = A_{i}B_{i}:** 1 when stage i makes a carry on its own, whatever comes in. **Propagate P_{i} = A_{i} ⊕ B_{i}:** 1 when stage i passes an incoming carry on (exactly one input is 1). Both depend only on A_{i} and B_{i}, so all are ready at 1T.
:::

Slide 20's two principles in one line (step 4's line 4 with G and P):

$$C_{i+1} = G_{i} + P_{i}C_{i}$$

"A carry leaves stage i if the stage makes one, **or** passes one on." Substitute each carry into the next:

1. C_{1} = G_{0} + P_{0}C_{0}
2. C_{2} = G_{1} + P_{1}C_{1} = G_{1} + P_{1}G_{0} + P_{1}P_{0}C_{0}
3. C_{3} = G_{2} + P_{2}G_{1} + P_{2}P_{1}G_{0} + P_{2}P_{1}P_{0}C_{0}
4. C_{4} = G_{3} + P_{3}G_{2} + P_{3}P_{2}G_{1} + P_{3}P_{2}P_{1}G_{0} + P_{3}P_{2}P_{1}P_{0}C_{0}

Each carry is now one level of AND gates and one OR, fed by G, P and C_{0}: ready at 1T + 2T = 3T whatever n is ("independent of n", slide 20). Then S_{i} = P_{i} ⊕ C_{i} at 4T. The price is gate size: C_{4} needs a 5-input AND and a 5-input OR, and C_{n} needs (n + 1)-input gates, so large adders build look-ahead in 4-bit blocks.

[[fig:cla_delay2|What this graph plots: the time until every output of an n-bit adder is settled (in gate delays T, up the side) against the word length n (across). One point = one adder size. Ripple carry rises as (2n + 1)T; carry look-ahead stays at 4T.|w=62]]

| n | 2 | 4 | 8 | 16 |
|---|---|---|---|---|
| ripple (2n + 1)T | 5T | 9T | 17T | 33T |
| look-ahead | 4T | 4T | 4T | 4T |

**Running example.** A = 1011, B = 1110: G = A AND B = **1010**, P = A ⊕ B = **0101** (bits 3…0), C_{0} = 0. C_{1} = G_{0} = 0; C_{2} = G_{1} = 1; C_{3} = G_{2} + P_{2}G_{1} = 0 + 1 = 1; C_{4} = G_{3} = 1. The same carries as step 5, found without waiting.

**Answer to the Guess.** It passes the carry when **exactly one** of A_{i}, B_{i} is 1 (P_{i} = 1); it makes a carry on its own when **both** are 1 (G_{i} = 1).

:::check Check 7
(a) For A = 0101, B = 0111, C_{0} = 0, give G, P and C_{1}–C_{4} from the look-ahead equations. (b) How many inputs does the largest AND gate in C_{3} have?
:::

### 8 · Adders from NAND or NOR gates only

File 03 showed NAND alone can build anything, and step 7 of that file built XOR from four NANDs. Slides 21–22 use that to build the adders.

:::q <span class="tag">Deck 03 slides 21–22</span>
Draw a half adder using NAND logic only, and state how a full adder is built from NAND gates.
:::

:::guess Guess first
File 03's 4-NAND XOR already has (AB)' at the output of its first gate. How many more NAND gates does the carry AB need?
:::

[[fig:ha_nand|Half adder from five NAND gates (deck 03 slide 21). Gates 1–4 are file 03's XOR; gate 5, with both inputs joined, inverts gate 1's (AB)' to give C = AB.|w=70]]

| Circuit | Gates | How |
|---|---|---|
| Half adder, NAND (slide 21) | 5 | gates 1–4 give S = A ⊕ B; gate 5 inverts (AB)' to C = AB |
| Half adder, NOR (slide 21) | 5 | NOR 1, 2 give A', B'; NOR 3 gives (A + B)'; NOR 4: (A' + B')' = AB = C; NOR 5: (AB + (A + B)')' = A ⊕ B = S |
| Full adder, NAND (slide 22) | 9 | two 4-NAND XORs give A ⊕ B, then S; their first gates give (AB)' and ((A ⊕ B)C_{in})'; gate 9 NANDs these two |

Gate 9 reads, by De Morgan (file 01 step 5): ((AB)' · ((A ⊕ B)C_{in})')' = AB + (A ⊕ B)C_{in}, which is step 4's C_{out}. The two half adders' AND and the OR of step 4 have collapsed into one NAND.

**Answer to the Guess.** **One**: a NAND with both inputs joined is a NOT, and NOT (AB)' = AB. Total 4 + 1 = 5.

:::check Check 8
In the 9-NAND full adder, take A = 1, B = 1, C_{in} = 0. What are (AB)', ((A ⊕ B)C_{in})' and C_{out}?
:::

### 9 · Subtracting two bits: the half subtractor

Adding carried a 1 to the left. Subtracting does the reverse: when the top bit is too small, the column **borrows** from the left.

:::q <span class="tag">Deck 03 slide 23 (EX 3.23)</span>
Design a half subtractor for A − B: truth table, difference D, borrow b_{out}, and the circuit.
:::

:::guess Guess first
0 − 1 in one binary column: borrow 1 from the left (worth 2 here). What is written in the column?
:::

:::note Terms
**Difference D:** the bit written in this column. **Borrow out b_{out}:** 1 when this column had to take 2 from the next column to the left (because A < B here). **Half subtractor:** subtracts one bit from another, with no borrow coming in.
:::

| A | B | A − B | b_{out} | D |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 2 − 1 = 1, after borrowing | 1 | 1 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 0 |

D is the same column as the half adder's S: **D = A ⊕ B**. A borrow happens only on row 01 (A = 0, B = 1): **b_{out} = A'B**.

[[fig:half_sub|Half subtractor (deck 03 slide 23): an XOR gives D; A passes through an inverter into an AND with B to give the borrow b_{out} = A'B.|w=55]]

The only change from the half adder is the inverter on A: the carry AB becomes the borrow A'B.

**Answer to the Guess.** **1** (2 − 1 = 1), with borrow 1 (slide 23: 0 − 1 = 1, borrow 1).

:::check Check 9
(a) A = 1, B = 1: D and b_{out}? (b) Which single row of the table has b_{out} = 1, and why only that one?
:::

### 10 · The full subtractor

Like the adder, every column except the rightmost may have lent a borrow to the column on its right, so a column subtracts **two** things from A.

:::q <span class="tag">Deck 03 slides 24–26</span>
Design a full subtractor for A − B − b_{in}: truth table, minimal D and b_{out}, and a circuit from two half subtractors.
:::

:::guess Guess first
0 − 1 − 1 = ? (Borrow 2 from the left.) Give D and b_{out}.
:::

:::note Terms
**Borrow in b_{in}:** 1 when the column to the right borrowed from this one, so 1 more must be taken off A here. **Full subtractor:** computes A − B − b_{in}, giving D and b_{out}.
:::

| Row | A B b_{in} | A − B − b_{in} | b_{out} D |
|---|---|---|---|
| 0 | 0 0 0 | 0 | 0 0 |
| 1 | 0 0 1 | −1 = 2 − 1 | 1 1 |
| 2 | 0 1 0 | −1 = 2 − 1 | 1 1 |
| 3 | 0 1 1 | −2 = 2 − 2 | 1 0 |
| 4 | 1 0 0 | 1 | 0 1 |
| 5 | 1 0 1 | 0 | 0 0 |
| 6 | 1 1 0 | 0 | 0 0 |
| 7 | 1 1 1 | −1 = 2 − 1 | 1 1 |

1. D = 1 on rows 1, 2, 4, 7, the same rows as the adder's S (slide 24's checkerboard map): **D = A ⊕ B ⊕ b_{in}**.
2. b_{out} = Σm(1, 2, 3, 7). On a K-map cell 3 pairs with 1 (A'b_{in}), 2 (A'B) and 7 (Bb_{in}): **b_{out} = A'B + A'b_{in} + Bb_{in}** (slide 26).
3. Compare with C_{out} = AB + AC_{in} + BC_{in}: the same shape with A replaced by A' in the two terms that contain A.

[[fig:full_sub_2hs|Full subtractor from two half subtractors and an OR gate (deck 03 slide 26). Half subtractor 1 gives A ⊕ B and A'B; half subtractor 2 subtracts b_{in} from A ⊕ B, giving D and (A ⊕ B)'b_{in}; the OR joins the borrows.|w=72]]

From the circuit: b_{out} = A'B + (A ⊕ B)'b_{in}. Both forms are 1 on rows 1, 2, 3, 7, so they are the same function.

**Answer to the Guess.** −2 = (2 borrowed) − 2 = 0: **D = 0, b_{out} = 1** (row 3).

:::check Check 10
(a) Row A = 1, B = 1, b_{in} = 1: D and b_{out}? (b) Evaluate both b_{out} forms for A = 0, B = 0, b_{in} = 1.
:::

### 11 · One cell that adds or subtracts

Steps 4 and 10 built the full adder and full subtractor from the same parts; the only difference is an inverter on A (and on A ⊕ B) in front of the two ANDs. Slides 27–28 make that inverter switchable.

:::q <span class="tag">Deck 03 slides 27–28</span>
Design one circuit that works as a full adder when E = 0 and as a full subtractor when E = 1.
:::

:::guess Guess first
An XOR gate with one input tied to a control E: what does it output when E = 0, and when E = 1?
:::

:::note Terms
**Controlled inverter:** an XOR with one input on a control line; X ⊕ 0 = X (passes), X ⊕ 1 = X' (inverts). **E:** the mode line; E = 0 add, E = 1 subtract.
:::

[[fig:addsub_cell|Full adder/subtractor cell (deck 03 slide 28): two half adder/subtractor stages. In each, an XOR with E (controlled inverter) feeds the AND, so E = 0 gives the adder's AND and E = 1 the subtractor's.|w=78]]

1. Stage 1: XOR(A_{i}, B_{i}) = A_{i} ⊕ B_{i}, and AND((A_{i} ⊕ E), B_{i}).
2. Stage 2: D_{i} = (A_{i} ⊕ B_{i}) ⊕ C_{i}, and AND(((A_{i} ⊕ B_{i}) ⊕ E), C_{i}).
3. C_{i+1} = OR of the two ANDs.

| E | Stage 1 AND | Stage 2 AND | C_{i+1} | Circuit |
|---|---|---|---|---|
| 0 | A_{i}B_{i} | (A_{i} ⊕ B_{i})C_{i} | carry (step 4) | full adder |
| 1 | A_{i}'B_{i} | (A_{i} ⊕ B_{i})'C_{i} | borrow (step 10) | full subtractor |

The sum and the difference are the same XOR, so they need no switching.

**Answer to the Guess.** E = 0: the other input **unchanged**; E = 1: its **complement**.

:::check Check 11
E = 1, A_{i} = 1, B_{i} = 0, C_{i} = 1. Give D_{i} and C_{i+1}, and check them as 1 − 0 − 1.
:::

### 12 · Subtracting by adding: the 2's-complement adder–subtractor

Step 11 needs a special cell. Most hardware subtracts with the ordinary ripple adder of step 5, using 2's complement: A − B = A + (2's complement of B) = A + B' + 1.

:::q <span class="tag">Predict</span>
With the running example, compute 1011 − 1110 (11 − 14) as 1011 + B' + 1 in a 4-bit adder. What is the final carry, and what does the 4-bit result mean?
:::

:::guess Guess first
11 − 14 is negative. Will the 4-bit adder produce a carry out of 1 or 0?
:::

:::note Terms
**B' (1's complement):** every bit of B inverted. **2's complement of B:** B' + 1; adding it subtracts B. **M:** mode line; M = 0 add, M = 1 subtract.
:::

[[fig:adder_sub|4-bit adder–subtractor: an XOR on every B input, controlled by M, and C_{0} = M. M = 0 passes B and adds 0; M = 1 inverts B and adds 1.]]

Each XOR gives B_{i} ⊕ M (B_{i} when M = 0, B_{i}' when M = 1, the controlled inverter of step 11), and the same M enters as C_{0}, which supplies the "+ 1".

Reading the result for unsigned numbers (n bits):

| Final carry C_{n} | Meaning | Result bits |
|---|---|---|
| 1 | A ≥ B | the difference A − B (discard the carry) |
| 0 | A < B | negative: the 2's complement of B − A |

Running example, M = 1:

1. B = 1110, B' = 0001.
2. 1011 + 0001 + 1 = 1101, carry out C_{4} = **0**.
3. Carry 0: negative. 2's complement of 1101 = 0010 + 1 = 0011 = 3. Result **−3** (11 − 14 ✓).

**Answer to the Predict.** C_{4} = **0** and the 4 bits are **1101**, the 2's complement of 3: the answer is −3.

:::check Check 12
(a) Do 1110 − 1011 (14 − 11) the same way: B', the sum, the final carry, the result. (b) Do 0110 − 0011.
:::

### 13 · The BCD adder

Step 5 adds binary numbers. Calculators and clocks store each decimal digit in its own 4 bits (BCD: 0000–1001 for 0–9). A binary adder on two BCD digits can produce 1010–1111, which are not BCD digits.

:::q <span class="tag">Predict</span>
Add the BCD digits 8 and 7 in a 4-bit binary adder. The result 1111 is not a BCD digit. What must be added to turn it into "1" carried and "5" in the units?
:::

:::guess Guess first
A 4-bit adder wraps round at 16; a decimal digit wraps round at 10. How many codes does the decimal digit skip?
:::

:::note Terms
**BCD digit:** a decimal digit 0–9 written as 4-bit binary. **K:** the carry out of the first (binary) adder. **Z_{3}Z_{2}Z_{1}Z_{0}:** its 4-bit sum. **Y:** 1 when the binary sum is above 9, so 0110 must be added; Y is also the decimal carry to the next digit.
:::

[[fig:bcd_adder|BCD adder: the first 4-bit adder forms the binary sum K Z; the logic Y = K + Z_{3}Z_{2} + Z_{3}Z_{1} detects a sum above 9; a second 4-bit adder adds 0110 when Y = 1 and 0000 when Y = 0.|w=60]]

When to correct (the sum of two digits plus a carry is 0–19):

| Binary sum | Detected by | Why |
|---|---|---|
| 16–19 | K = 1 | the first adder already wrapped |
| 12–15 | Z_{3}Z_{2} = 1 | 1100–1111 |
| 10–11 | Z_{3}Z_{1} = 1 | 1010, 1011 |

$$Y = K + Z_{3}Z_{2} + Z_{3}Z_{1}$$

Adding 6 = 0110 skips the six unused codes 1010–1111, so the 4 bits wrap at 10 instead of 16. The correction's carry is not used; Y itself is the carry into the next decimal digit.

**Answer to the Predict.** 8 + 7 = 1111, K = 0, Z_{3}Z_{2} = 1 so Y = 1. 1111 + 0110 = 1 0101: units **0101 = 5**, decimal carry **Y = 1**: "15" ✓. **Six** codes are skipped, so add **0110**.

:::check Check 13
(a) 6 + 5: binary sum, Y, corrected digit, decimal carry. (b) 9 + 9 the same way. (c) 4 + 5: is a correction needed?
:::

---

## Exam form

**Half adder.** Truth table · S = A ⊕ B, C = AB · XOR + AND circuit.

**Full adder.**

1. Truth table of A, B, C_{in} → S = Σm(1, 2, 4, 7), C_{out} = Σm(3, 5, 6, 7).
2. K-maps: S does not reduce (checkerboard) → S = A ⊕ B ⊕ C_{in}; C_{out} = AB + BC_{in} + AC_{in}.
3. From two half adders: s_{1} = A ⊕ B, c_{1} = AB; S = s_{1} ⊕ C_{in}, c_{2} = s_{1}C_{in}; C_{out} = c_{1} + c_{2} = AB + (A ⊕ B)C_{in}; one OR, because c_{1} and c_{2} are never both 1.

**Ripple-carry adder.** n full adders, carry right to left, C_{0} = 0; stage table as in step 5. Delay: 2T per stage on the carry path + 1T for the first XOR = **(2n + 1)T** (9T for 4 bits).

**Carry look-ahead.** G_{i} = A_{i}B_{i}, P_{i} = A_{i} ⊕ B_{i}, C_{i+1} = G_{i} + P_{i}C_{i}; expand C_{1}…C_{4} (step 7); all carries at 3T, sums at 4T, independent of n; cost: wide gates.

**NAND/NOR.** Half adder 5 NAND (or 5 NOR); full adder 9 NAND, last gate ((AB)'((A ⊕ B)C_{in})')'.

**Subtractors.** Half: D = A ⊕ B, b_{out} = A'B. Full: D = A ⊕ B ⊕ b_{in}, b_{out} = A'B + A'b_{in} + Bb_{in} = A'B + (A ⊕ B)'b_{in}; two half subtractors + OR. Controlled cell: XOR with E before each AND (E = 0 add, 1 subtract).

**2's-complement adder–subtractor.** XOR on each B with M, C_{0} = M; A − B = A + B' + 1; carry 1 → positive result, carry 0 → negative, take the 2's complement.

**BCD adder.** Binary add → Y = K + Z_{3}Z_{2} + Z_{3}Z_{1} → add 0110 if Y = 1; Y is the decimal carry.

## Traps

- S = A ⊕ B for a full adder: the carry in is missing (S = A ⊕ B ⊕ C_{in}).
- Joining the two half-adder carries with XOR or a third half adder: one OR is enough, because they are never both 1.
- Ripple delay as 2nT or nT when the question uses slide 19's counting: the first XOR adds 1T, (2n + 1)T.
- Writing the borrow as AB' (A complemented on the wrong side): the borrow needs A = 0, B = 1, so A'B.
- Subtracting with the adder but leaving C_{0} = 0: that gives A + B' = A − B − 1.
- Reading carry 0 after A + B' + 1 as "positive": carry 0 means A < B.
- BCD: correcting a sum of 9 or less, or missing the K term (9 + 9 = 1 0010 has Z = 0010, which looks valid).

## Self-test

1. Draw a full adder from two half adders and explain in one line why one OR gate suffices.
2. Write C_{4} of a 4-bit look-ahead adder in G, P and C_{0}.
3. Add 0111 and 0101 in a ripple-carry adder, showing C_{1}–C_{4}.
4. Do 0011 − 0110 with the 2's-complement adder–subtractor and interpret the final carry.
5. Add the BCD digits 4 and 8.
6. Full subtractor: give D and b_{out} for A = 0, B = 0, b_{in} = 1, and say what the borrow means.
7. Delay of a 6-bit ripple-carry adder, gate delay T, counted as in slide 19?
8. How many NOR gates does slide 21's half adder use, and which gate gives the carry?

<!--ANSWERS-->

## Answers

**Check 1.** (a) **C = 0, S = 1**. (b) Bit 0 has nothing on its right, so only two bits; from bit 1 on, a carry may arrive and a column adds **three** bits.

**Check 2.** (a) Count 2: **C_{out} = 1, S = 0**. (b) 0 + 1 + 1 = 2: **C_{out} = 1, S = 0** (step 5's stage 2).

**Check 3.** (a) **Four**: three 2-input ANDs and one 3-input OR (two 2-input ORs if only 2-input gates exist). (b) AB = 0, BC_{in} = 1, AC_{in} = 0: **C_{out} = 1**.

**Check 4.** s_{1} = **1**, c_{1} = **0**, c_{2} = 1 · 1 = **1**, S = 1 ⊕ 1 = **0**, C_{out} = **1** (row 3 ✓).

**Check 5.** Stage 0: 1 + 1 + 0 = 2 → S_{0} = 0, C_{1} = **1**. Stage 1: 0 + 1 + 1 = 2 → S_{1} = 0, C_{2} = **1**. Stage 2: 1 + 1 + 1 = 3 → S_{2} = 1, C_{3} = **1**. Stage 3: 0 + 0 + 1 = 1 → S_{3} = 1, C_{4} = **0**. Sum **1100** = 12 ✓.

**Check 6.** (a) (2 × 32 + 1)T = **65T**. (b) C_{1} at 3T, C_{2} at **5T**.

**Check 7.** (a) G = **0101**, P = **0010** (bits 3…0). C_{1} = G_{0} = **1**; C_{2} = G_{1} + P_{1}G_{0} = 0 + 1 · 1 = **1**; C_{3} = G_{2} + P_{2}G_{1} + P_{2}P_{1}G_{0} = **1**; C_{4} = G_{3} + P_{3}(…) = **0**. Same as Check 5. (b) **Four** inputs (P_{2}P_{1}P_{0}C_{0}).

**Check 8.** (AB)' = **0**; A ⊕ B = 0, so ((A ⊕ B)C_{in})' = **1**; C_{out} = (0 · 1)' = **1** (1 + 1 + 0 = 2 ✓).

**Check 9.** (a) **D = 0, b_{out} = 0**. (b) Row **A = 0, B = 1**: the only row where the bit taken away is larger than the bit there.

**Check 10.** (a) 1 − 1 − 1 = −1 = 2 − 1: **D = 1, b_{out} = 1**. (b) A'B + A'b_{in} + Bb_{in} = 0 + 1 + 0 = **1**; A'B + (A ⊕ B)'b_{in} = 0 + 1 · 1 = **1**. Both 1 (row 1 ✓).

**Check 11.** A_{i} ⊕ B_{i} = 1; D_{i} = 1 ⊕ 1 = **0**. Stage 1 AND: (1 ⊕ 1) · 0 = 0. Stage 2 AND: (1 ⊕ 1) · 1 = 0. **C_{i+1} = 0**. 1 − 0 − 1 = 0, no borrow ✓.

**Check 12.** (a) B = 1011, B' = 0100; 1110 + 0100 + 1 = 1 0011: carry **1**, positive, result **0011** = 3 ✓. (b) B' = 1100; 0110 + 1100 + 1 = 1 0011: carry **1**, result **0011** = 3 ✓.

**Check 13.** (a) 0110 + 0101 = 1011 (11), K = 0, Z_{3}Z_{1} = 1 → **Y = 1**; 1011 + 0110 = 1 0001: digit **0001**, decimal carry 1: "11". (b) 1001 + 1001 = 1 0010: **K = 1**, Y = 1; 0010 + 0110 = **1000**, decimal carry 1: "18". (c) 0100 + 0101 = 1001 (9): K = 0, Z_{3}Z_{2} = 0, Z_{3}Z_{1} = 0 → **Y = 0**, no correction.

**Self-test.**

1. Step 4's figure. c_{1} = 1 needs A = B = 1, which makes A ⊕ B = 0 and c_{2} = 0, so the two carries are never both 1 and OR = sum.
2. C_{4} = G_{3} + P_{3}G_{2} + P_{3}P_{2}G_{1} + P_{3}P_{2}P_{1}G_{0} + P_{3}P_{2}P_{1}P_{0}C_{0}.
3. Stage 0: 1 + 1 → S_{0} = 0, C_{1} = **1**. Stage 1: 1 + 0 + 1 → 0, C_{2} = **1**. Stage 2: 1 + 1 + 1 → 1, C_{3} = **1**. Stage 3: 0 + 0 + 1 → 1, C_{4} = **0**. **1100** (7 + 5 = 12).
4. B' = 1001; 0011 + 1001 + 1 = 1101, carry **0**: negative; 2's complement of 1101 is 0011, so the result is **−3**.
5. 0100 + 1000 = 1100 (12): Z_{3}Z_{2} = 1, Y = 1; 1100 + 0110 = 1 0010: digit **0010**, decimal carry 1: "12".
6. 0 − 0 − 1 = −1 = 2 − 1: **D = 1, b_{out} = 1**. The column had to borrow 2 from the next column to the left.
7. (2 × 6 + 1)T = **13T**.
8. **Five** NOR gates; NOR 4 gives the carry: (A' + B')' = **AB**.

<!--/ANSWERS-->
