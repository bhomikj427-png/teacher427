# 04 — Adders and subtractors

<div class="sub">Deck 03 (slides 4–19) · deck 09 slides 25–26 (serial addition) · syllabus Unit 1 · mid-term Q6 used the full adder · needs 01 (XOR) and 02 (K-maps)</div>

## Map

[[map:1 Half and full adder > 2 Ripple, look-ahead, adder–subtractor > 3 Serial and BCD adders|here=1]]

The first real circuits built with 01–02: adding bits. One full adder per bit makes a word adder; the rest of the file is about making it faster, smaller or decimal.

## The questions this file answers

- <span class="tag">Deck 03 slides 4–12</span> Design a full adder: truth table, minimal sum and carry, and from two half adders.
- <span class="tag">Deck 03 slides 18–19</span> Add 1011 and 1110 in a 4-bit ripple adder; delay of an n-bit ripple adder.
- <span class="tag">Deck 09 slides 25–26</span> Trace a serial adder for A = 0100, B = 0111.

---

## Build

### 1 · Half adder, full adder, subtractors

:::q <span class="tag">Deck 03 slides 4–12</span>
Design a full adder. Give its truth table and the minimal expressions for sum and carry, and show how it is built from two half adders.
:::

:::guess Guess first
1 + 1 + 1 in binary: which bit is the sum and which the carry?
:::

[[fig:half_adder|Half adder: S = A ⊕ B, C = AB.|w=50]]

| A B C_{in} | C_{out} S | A B C_{in} | C_{out} S |
|---|---|---|---|
| 0 0 0 | 0 0 | 1 0 0 | 0 1 |
| 0 0 1 | 0 1 | 1 0 1 | 1 0 |
| 0 1 0 | 0 1 | 1 1 0 | 1 0 |
| 0 1 1 | 1 0 | 1 1 1 | 1 1 |

S is 1 for an odd number of 1s: Σm(1, 2, 4, 7). C_{out} is 1 for two or more: Σm(3, 5, 6, 7); its K-map gives three pairs.

$$S = A ⊕ B ⊕ C_{in}      C_{out} = AB + BC_{in} + AC_{in} = AB + C_{in}(A ⊕ B)$$

[[fig:full_adder_2ha|Full adder from two half adders and an OR gate.|w=70]]

| | Difference | Borrow out |
|---|---|---|
| Half subtractor (A − B) | A ⊕ B | A'B |
| Full subtractor | A ⊕ B ⊕ B_{in} | A'B + A'B_{in} + BB_{in} |

**Answer.** S = A ⊕ B ⊕ C_{in}, C_{out} = AB + BC_{in} + AC_{in}. The first half adder adds A and B; the second adds C_{in}. Only one of them can carry, so an OR gives C_{out}.

:::check Check 1
(a) S and C_{out} for A = 1, B = 0, C_{in} = 1? (b) What is the one difference between the full-adder carry and the full-subtractor borrow?
:::

### 2 · Ripple adder, carry look-ahead, adder–subtractor

:::q <span class="tag">Deck 03 slides 18–19</span>
Add A = 1011 and B = 1110 in a 4-bit ripple-carry adder, showing every carry. If each gate has delay T, what is the delay of an n-bit ripple-carry adder?
:::

:::guess Guess first
Which output bit is the last to become correct?
:::

[[fig:ripple_adder|4-bit ripple-carry adder.]]

The carry ripples from right to left, so the top bits settle last. **Carry look-ahead** removes the wait. Define G_{i} = A_{i}B_{i} (generate) and P_{i} = A_{i} ⊕ B_{i} (propagate); then C_{i+1} = G_{i} + P_{i}C_{i}. Substituting:

$$C_{2} = G_{1} + P_{1}G_{0} + P_{1}P_{0}C_{0}      C_{3} = G_{2} + P_{2}G_{1} + P_{2}P_{1}G_{0} + P_{2}P_{1}P_{0}C_{0}$$

Every carry is a two-level AND–OR, so all are ready together; S_{i} = P_{i} ⊕ C_{i}. The price: more, wider gates.

[[fig:cla_delay|Delay grows with n for ripple, stays flat for look-ahead.|w=60]]

**Adder–subtractor.** A − B = A + B' + 1. An XOR on each B input, controlled by M, with C_{0} = M: M = 0 adds, M = 1 subtracts. Unsigned: a final carry 1 means a positive result (discard it); 0 means negative, in 2's complement.

[[fig:adder_sub|4-bit adder–subtractor.]]

**Answer.** Bit 0: 1 + 0 → S_{0} = 1, C_{1} = 0. Bit 1: 1 + 1 → 0, C_{2} = 1. Bit 2: 0 + 1 + 1 → 0, C_{3} = 1. Bit 3: 1 + 1 + 1 → 1, C_{out} = 1. Result **1 1001 = 25** ✓. Delay (one T for the XOR, two levels per carry): **(2n + 1)T**, 9T for n = 4.

:::check Check 2
(a) For the same A, B with C_{0} = 0, find G, P and C_{1}–C_{4}. (b) Delay of an 8-bit ripple adder? (c) Do 0110 − 0011 the adder–subtractor's way and state the final carry.
:::

### 3 · Serial adder and BCD adder

:::q <span class="tag">Deck 09 slides 25–26 "serial addition"</span>
A serial adder holds A = 0100 and B = 0111 in two shift registers. Trace the four clock pulses and give the final contents of register A.
:::

:::guess Guess first
A serial adder has only one full adder. Where does it keep the carry between bits?
:::

[[fig:serial_adder|Serial adder: one full adder, a carry flip-flop, two shift registers.|w=70]]

One full adder is reused for every bit: each clock presents the two lowest bits, shifts the sum into the top of A, and stores the carry in a flip-flop. 1 adder + 1 flip-flop for any length, but n clocks.

| Clock | A, B, carry | S | New carry | Register A |
|---|---|---|---|---|
| start | | | 0 | 0100 |
| 1 | 0 + 1 + 0 | 1 | 0 | 1010 |
| 2 | 0 + 1 + 0 | 1 | 0 | 1101 |
| 3 | 1 + 1 + 0 | 0 | 1 | 0110 |
| 4 | 0 + 0 + 1 | 1 | 0 | 1011 |

**BCD adder.** Add two BCD digits in binary. If the result exceeds 9, add 6 (0110): a 4-bit adder rolls over at 16, a decimal digit at 10. Correction when K (first carry) = 1 or the sum is 10–15: **Y = K + Z_{3}Z_{2} + Z_{3}Z_{1}**. Example 8 + 7 = 1111, Y = 1, + 0110 → 1 0101: "15" ✓.

[[fig:bcd_adder|BCD adder: binary adder, correction logic Y, second adder adding 0110.|w=60]]

**Answer.** After four clocks register A holds **1011** (4 + 7 = 11) and the carry flip-flop holds 0.

:::check Check 3
(a) Add the BCD digits 6 and 5: first sum, Y, corrected sum. (b) 9 + 9 the same way. (c) Full adders and clock pulses for an 8-bit serial adder?
:::

---

## Exam form

**Full adder.** Truth table; K-maps; S and C_{out}; two-half-adder circuit. Subtractor table.

**Parallel adders.** Ripple circuit and delay (2n + 1)T; G, P, C_{i+1} = G_{i} + P_{i}C_{i} expanded to C_{3}; adder–subtractor with M.

**Serial and BCD.** Serial trace table; BCD rule Y = K + Z_{3}Z_{2} + Z_{3}Z_{1}, add 0110.

## Traps

- Writing S = A ⊕ B for a full adder (forgetting C_{in}).
- Forgetting C_{0} = 1 in subtraction (that is the +1 of 2's complement).
- Adding 6 to a BCD sum of exactly 9 or less.
- Missing the K term: 9 + 9 = 1 0010 looks valid but needs correcting.

## Self-test

1. Draw a full adder from two half adders and explain why one OR suffices.
2. Write C_{4} for a 4-bit look-ahead adder in G and P.
3. Add 0111 and 0101 in a ripple adder, showing carries.
4. Do 0011 − 0110 with the adder–subtractor and interpret the final carry.
5. Add the BCD digits 4 and 8.
6. Compare a serial and a parallel adder in two points.

<!--ANSWERS-->

## Answers

**Check 1.** (a) **S = 0, C_{out} = 1**. (b) A is replaced by A' in the borrow.

**Check 2.** (a) G = 1010, P = 0101 (bits 3…0). C_{1} = 0, C_{2} = 1, C_{3} = 1, C_{4} = 1: the ripple carries. (b) **17T**. (c) B' = 1100; 0110 + 1100 + 1 = 1 0011: carry **1**, positive, **0011** = 3.

**Check 3.** (a) 1011 (11): Z_{3}Z_{1} = 1, Y = 1; + 0110 = 1 0001 → "11". (b) 1 0010: K = 1, Y = 1; 0010 + 0110 = 1000, carry 1 → "18". (c) **1** full adder (and a flip-flop), **8** clocks.

**Self-test.**

1. Figure in step 1. The two half-adder carries can never both be 1 (if A = B = 1 the first sum is 0), so OR = sum.
2. C_{4} = G_{3} + P_{3}G_{2} + P_{3}P_{2}G_{1} + P_{3}P_{2}P_{1}G_{0} + P_{3}P_{2}P_{1}P_{0}C_{0}.
3. Bit 0: 1 + 1 → 0, c 1. Bit 1: 1 + 0 + 1 → 0, c 1. Bit 2: 1 + 1 + 1 → 1, c 1. Bit 3: 0 + 0 + 1 → 1, c 0. **1100** (7 + 5 = 12).
4. B' = 1001; 0011 + 1001 + 1 = 1101, carry **0**: negative; 2's complement of 1101 is 0011, so the result is **−3**.
5. 0100 + 1000 = 1100 (12): Z_{3}Z_{2} = 1, Y = 1; + 0110 = 1 0010 → "12".
6. Serial: 1 full adder, n clocks (small, slow). Parallel: n full adders, one step (large, fast).

<!--/ANSWERS-->
