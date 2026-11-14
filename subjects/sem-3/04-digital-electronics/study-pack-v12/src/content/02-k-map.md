# 02 — The Karnaugh map

<div class="sub">Deck 02 (slides 4–69) · mid-term 2025 Q4 (4 marks) · practice set 1 Q1–Q2 · syllabus Unit 1 · needs 01 (minterms)</div>

## Map

[[map:1 Grouping 1s, don't-cares > 2 POS from the 0s > 3 Five variables|here=1]]

01 simplified by spotting terms that differ in one variable. A K-map lays the truth table out so those terms sit next to each other: grouping becomes a picture.

## The questions this file answers

- <span class="tag">MTE 2025 Q4 · 4 marks</span> Minimise F(a, b, c, d) = Σm(0, 4, 5, 7–9, 15) + Σd(1, 3, 6, 14); draw the circuit with basic gates.
- <span class="tag">Deck 02 slide 63</span> F(W, X, Y, Z) = Σm(0, 1, 2, 5, 8, 9, 10): minimal SOP and minimal POS. Which is minimal?
- <span class="tag">Deck 02 slides 58–61</span> A five-variable map.

---

## Build

### 1 · Grouping 1s, and don't-cares

:::q <span class="tag">MTE 2025 Q4 · 4 marks</span>
Minimize the following Boolean function using K-Map method to obtain a simplified expression. Also draw the logic circuit using basic gates. F(a, b, c, d) = Σm(0, 4, 5, 7–9, 15) + Σd(1, 3, 6, 14)
:::

:::guess Guess first
A don't-care can be read as 0 or 1. When would you choose 1?
:::

:::note Terms
**K-map:** the truth table as a grid ordered 00, 01, 11, 10, so neighbours differ in one variable. **Don't-care (X):** a combination that never occurs or whose output does not matter. **Prime implicant:** a group that cannot be made larger. **Essential:** a prime implicant that covers a 1 no other covers.
:::

[[fig:v1arg0|The mid-term map. Small numbers are minterm numbers.|w=45]]

Two neighbouring 1s differ in one variable x, so (rest)(x + x') = rest: the changing variable drops out. **Rules** (deck 02 slides 4–10):

1. Only 1s (and the X's you choose), never a 0.
2. Rectangles of 1, 2, 4, 8 … cells; no diagonals.
3. The map wraps: left edge touches right, top touches bottom.
4. Groups as large as possible, as few as possible; overlap allowed.
5. A group of 2^{k} cells removes k variables.

**Procedure:** fill 1s and Xs → essential prime implicants first → cover the rest with the fewest, largest groups → read each group: keep the variables that stay constant. Use an X only when it enlarges a group; an X never needs covering.

**Answer.** Cells 0, 1, 8, 9 (wrap; X at 1) → **b'c'**. Cells 6, 7, 14, 15 (Xs at 6, 14) → **bc**. Left: 4, 5 → cells 0, 1, 4, 5 → **a'c'**. X at 3 unused (read as 0).

$$F = b'c' + bc + a'c'$$

a'b (cells 4–7) covers 4, 5 equally well, so F = b'c' + bc + a'b is also minimal. Circuit: three 2-input ANDs into a 3-input OR:

[[fig:v1arg1|AND–OR circuit for the mid-term answer.|w=55]]

:::check Check 1
(a) <span class="tag">Deck 02 slide 69</span> Minimise Σm(0, 2, 6, 8, 12, 13, 15) + d(3, 4, 9). (b) <span class="tag">Deck 02 slide 27</span> Minimise F(a, b, c) = Σm(2, 3, 6, 7). The slide circles two pairs and marks it "Wrong!!": why? (c) How many literals does a group of 4 leave in a 4-variable map?
:::

### 2 · Product of sums from the 0s

:::q <span class="tag">Deck 02 slide 63 "PoS optimization from SoP"</span>
F(W, X, Y, Z) = Σm(0, 1, 2, 5, 8, 9, 10). Find the minimal SOP and the minimal POS. "Which one is the minimal one?"
:::

:::guess Guess first
To get a product of sums, which cells do you group?
:::

[[fig:v1arg2|Left: group the 1s (SOP). Right: group the 0s (POS).]]

**POS method.** Group the **0s** with the same rules. Each group gives a sum term read the opposite way: a variable that stays 0 is written plain, one that stays 1 complemented. AND the sums. (Grouping 0s gives F' as SOP; De Morgan turns it into F as POS.)

**Answer.** SOP: **X'Y' + X'Z' + W'Y'Z** (7 literals). POS: the 0s group as WX, YZ and XZ': **(W' + X')(Y' + Z')(X' + Z)** (6 literals). Both need three gates plus an output gate; the **POS is one literal cheaper**. Work out both when a question says "minimal".

:::check Check 2
<span class="tag">Deck 02 slide 64</span> F(W, X, Y, Z) = ΠM(0, 2, 3, 4, 5, 6). Find the minimal SOP.
:::

### 3 · Five variables

:::q <span class="tag">Deck 02 slides 58–61</span>
Minimise F(a, b, c, d, e) = Σm(5, 7, 13, 15, 21, 23, 29, 31).
:::

:::guess Guess first
The 1s in minterms 16–31 sit in the same places as those in 0–15. What does that tell you about a?
:::

[[fig:v1arg3|Two 4-variable maps: a = 0 (left) and a = 1 (right). Same position = neighbours.|w=70]]

Draw two 4-variable maps, one for a = 0 (0–15) and one for a = 1 (16–31). Cells in the same position on the two maps are neighbours, so a group that repeats in both loses a.

**Answer.** The same block of four (c = 1, e = 1) appears in both maps: **F = ce**.

:::check Check 3
<span class="tag">Set 1 Q1</span> Minimise F(v, w, x, y, z) = Σm(0, 2, 5, 8, 10, 13, 15, 17, 19, 21, 26, 28, 29, 30, 31) + Σd(7, 12, 14, 23, 24).
:::

---

## Exam form

**Method.** Draw the map with 00, 01, 11, 10 labels and minterm numbers; mark 1s and Xs; circle groups (each labelled with its term); write F; draw the circuit if asked.

**Rules.** The five group rules; X used only to enlarge; essential primes first.

**POS.** Group the 0s; read inverted; compare literal counts with the SOP.

## Traps

- Labelling the map 00, 01, 10, 11 (binary order): neighbours then differ in two bits.
- Forgetting wrap-around groups (corners, top–bottom).
- Covering an X that does not help.
- Reading a POS group the SOP way.
- Stopping at pairs when a quad exists.

## Self-test

1. Minimise F(a, b, c) = Σm(0, 1, 2, 3, 7).
2. Minimise F(A, B, C, D) = Σm(0, 1, 2, 5, 6, 7, 8, 9, 10, 14).
3. Minimise F(A, B, C, D) = Σm(1, 3, 7, 11, 15) + d(0, 2, 5).
4. Give the minimal POS of F(A, B, C) = Σm(0, 2, 3, 4, 5, 7).
5. When does a K-map have more than one minimal answer? Give an example from this file.

<!--ANSWERS-->

## Answers

**Check 1.** (a) **a'd' + c'd' + abd** (cells 0, 2, 4, 6 with X at 4; 0, 4, 8, 12; 13, 15). ac' in place of c'd' is equally minimal. (b) **F = b**: all four 1s form one quad. Two pairs give ab + a'b, which still simplifies, so the groups were not as large as possible. (c) **2**.

**Check 2.** The 1s are Σm(1, 7, 8–15): **F = W + XYZ + X'Y'Z**.

**Check 3.** **F = xz + wz' + v'x'z' + vw'z**. Groups: xz (5, 7, 13, 15, 21, 23, 29, 31), wz' (8, 10, 12, 14, 24, 26, 28, 30), v'x'z' (0, 2, 8, 10), vw'z (17, 19, 21, 23).

**Self-test.**

1. **a' + bc**.
2. **B'C' + CD' + A'BD**.
3. **CD + A'B'** (or CD + A'D, equally minimal).
4. Zeros at 1 and 6: **(A + B + C')(A' + B' + C)**.
5. When a 1 can be covered by two different groups of the same size: the mid-term map, where a'c' and a'b both cover cells 4 and 5.

<!--/ANSWERS-->
