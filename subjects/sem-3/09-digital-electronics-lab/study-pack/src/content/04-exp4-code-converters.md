# Exp 4 · Code converters: binary → Gray, BCD → Excess-3

<div class="sub">Manual pp. 11–12 · ICs 7486, 7432, 7408, 7404 · both converters checked over every valid input</div>

[[map:2 Adders/subtractors > 3 NAND/NOR design > 4 Code converters > 5 Comparator & parity|here=3]]

:::q <span class="tag">Manual Exp 4, aim</span>
Design and implement (A) a 4-bit binary to Gray code converter, (B) a BCD to Excess-3 converter. Viva form: "Why is Gray code used in position encoders, and why is Excess-3 self-complementing?"
:::

:::guess Guess first
How many bits change between consecutive Gray codes? What is 9's complement of 2 in Excess-3?
:::

## A · Binary → Gray

$$G_{3} = B_{3},   G_{2} = B_{3} ⊕ B_{2},   G_{1} = B_{2} ⊕ B_{1},   G_{0} = B_{1} ⊕ B_{0}$$

**Wiring** (manual's pins):

- B3 → output G3 directly.
- 7486 gate 1: B3 → 1, B2 → 2 → **3 = G2**.
- 7486 gate 2: B2 → 4, B1 → 5 → **6 = G1**.
- 7486 gate 3: B1 → 9, B0 → 10 → **8 = G0**.

| B | 0000 | 0001 | 0010 | 0011 | 0100 | 0101 | 0110 | 0111 | 1000 | 1001 | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| G | 0000 | 0001 | 0011 | 0010 | 0110 | 0111 | 0101 | 0100 | 1100 | 1101 | 1111 | 1110 | 1010 | 1011 | 1001 | 1000 |

**Gray → binary (exercise):** B3 = G3, B2 = B3 ⊕ G2, B1 = B2 ⊕ G1, B0 = B1 ⊕ G0. It is a chain: each XOR uses the *previous output*, not the previous input.

## B · BCD → Excess-3 (XS-3 = BCD + 3)

| BCD ABCD | 0000 | 0001 | 0010 | 0011 | 0100 | 0101 | 0110 | 0111 | 1000 | 1001 |
|---|---|---|---|---|---|---|---|---|---|---|
| XS-3 WXYZ | 0011 | 0100 | 0101 | 0110 | 0111 | 1000 | 1001 | 1010 | 1011 | 1100 |

The K-maps use 1010–1111 as don't-cares (they are not BCD). The manual's expressions, and a factored form that saves gates:

$$W = A + BC + BD = A + B(C + D)        X = B'C + B'D + BC'D' = B ⊕ (C + D)$$

$$Y = CD + C'D' = (C ⊕ D)'        Z = D'$$

**Wiring (factored form):**

| Gate | Wires |
|---|---|
| 7432 gate 1 | C → 1, D → 2 → 3 (C + D) |
| 7408 gate 1 | B → 1, 7432-3 → 2 → 3 (B(C + D)) |
| 7432 gate 2 | A → 4, 7408-3 → 5 → **6 = W** |
| 7486 gate 1 | B → 1, 7432-3 → 2 → **3 = X** |
| 7486 gate 2 | C → 4, D → 5 → 6; then 7404: 7486-6 → 1 → **2 = Y** |
| 7404 | D → 3 → **4 = Z** |

:::trap Trap: inputs above 1001
Set 1010–1111 and the outputs look like nonsense. Those inputs aren't BCD, and the design treated them as don't-cares. Test only 0000–1001.
:::

:::write Write in your record
**Result:** the binary-to-Gray converter (G3 = B3, Gi = Bi+1 ⊕ Bi) and the BCD-to-Excess-3 converter (W = A + BC + BD, X = B'C + B'D + BC'D', Y = CD + C'D', Z = D') were implemented and their truth tables verified.

**Theory for the record:** a code converter changes one binary code into another. In Gray code, successive values differ in one bit only. That avoids false intermediate readings in shaft encoders, and it gives the order of K-map labels. Binary → Gray: G_{n} = B_{n}, G_{i} = B_{i+1} ⊕ B_{i}. Excess-3 is BCD + 3. It is self-complementing: inverting all bits gives the 9's complement, which simplifies decimal subtraction. Each output bit is found from a K-map, with the six unused BCD codes as don't-cares.
:::

:::check Check 1
(a) Convert Gray 1011 to binary. (b) Show XS-3 is self-complementing using 2 and 7. (c) Why can X = B'C + B'D + BC'D' be written B ⊕ (C + D)?
:::

<!--ANSWERS-->

## Answers

**Opening question.** **One** bit changes between consecutive Gray codes, so a sensor caught mid-transition can be off by at most one step. 2 in XS-3 is 0101; inverting gives 1010 = XS-3 of 7 = 9 − 2. So the 9's complement is just the bitwise inverse.

**Check 1.** (a) B3 = 1, B2 = 1 ⊕ 0 = 1, B1 = 1 ⊕ 1 = 0, B0 = 0 ⊕ 1 = 1, giving **1101**. (b) XS-3(2) = 0101 and XS-3(7) = 1010: bitwise inverses, and 2 + 7 = 9. (c) B'C + B'D = B'(C + D), and BC'D' = B(C + D)'. B'P + BP' with P = C + D is exactly B ⊕ P.

<!--/ANSWERS-->
