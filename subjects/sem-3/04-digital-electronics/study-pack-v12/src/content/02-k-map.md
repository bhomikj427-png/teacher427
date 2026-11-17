# 02 — The Karnaugh map

<div class="sub">Deck 02 (slides 2–70) · syllabus Unit 1 (K-map minimisation, don't-cares) · 3 real questions: MTE 2025 Q4 (4 marks), practice set 1 Q1 and Q4 · needs 01 step 2 (row numbers), step 6 (P z + P z' = P), steps 7–8 (minterms, maxterms)</div>

## Map

[[map:1 Neighbours merge > 2 Gray order > 3 Read a group > 4 Largest groups > 5 Prime implicants > 6 Four variables > 7 Don't-cares > 8 POS from 0s > 9 Five variables > 10 Words → map|here=1]]

File 01 shrank x'yz + x'yz' + xz to x'y + xz by spotting two terms that differ in one variable. With 4 or 5 variables such pairs are hard to spot. The **Karnaugh map (K-map)** redraws the truth table so that every such pair sits side by side: simplifying becomes drawing rectangles. File 03 builds the result from NAND or NOR gates only.

## Symbols

| Symbol | What it means in this file | Typical value |
|---|---|---|
| a, b, c, d (or A…D, W…Z, v…z) | input variables; the first one is the most significant bit of the row number | 0 or 1 |
| cell | one square of the map = one truth-table row; the small grey number in it is the row number j | 0 … 15 |
| 1 / 0 / X in a cell | F on that row is 1, is 0, or "don't care" (step 7) | — |
| group | a rectangle of cells drawn round 1s (or 0s), with 2^{k} cells | 2, 4, 8 cells |
| k | how many variables a group removes: a group of 2^{k} cells drops k variables | 1, 2, 3 |
| Σd( ) or d( ) | list of don't-care rows | d(1, 3, 6, 14) |
| PI, EPI | prime implicant, essential prime implicant (step 5) | — |
| cost | (terms, literals) of the answer; fewer is cheaper | (3, 6) |

## Running example

**MTE 2025 Q4:** F(a, b, c, d) = Σm(0, 4, 5, 7, 8, 9, 15) + Σd(1, 3, 6, 14). Steps 1–5 work on 2- and 3-variable maps (with file 01's F(x, y, z) = Σm(2, 3, 5, 7)); step 6 maps the seven 1s alone (cost 4 terms, 12 literals), step 7 adds the don't-cares (3 terms, 6 literals), step 8 tries the 0s, file 03 builds it from NAND gates.

## The questions this file answers

- <span class="tag">MTE 2025 Q4 · 4 marks</span> Minimize the following Boolean function using K-Map method to obtain a simplified expression. Also draw the logic circuit using basic gates. F(a, b, c, d) = Σm(0, 4, 5, 7–9, 15) + Σd(1, 3, 6, 14)
- <span class="tag">Practice set 1 Q1</span> Minimize the following Boolean function using K-Map method and implement the circuit using universal gate. F(v, w, x, y, z) = Σm(0, 2, 5, 8, 10, 13, 15, 17, 19, 21, 26, 28, 29, 30, 31) + Σd(7, 12, 14, 23, 24)
- <span class="tag">Practice set 1 Q4</span> Design a combinational circuit having 4 inputs that will produce an output '1' when two consecutive input bits are 1 and produce '0' for other cases.
- <span class="tag">Deck 02 slide 63</span> F(W, X, Y, Z) = Σm(0, 1, 2, 5, 8, 9, 10): minimal SOP and minimal POS; which is minimal?

---

## Build

### 1 · Neighbouring rows merge: the two-variable map

File 01 step 6 merged x'yz with x'yz' because they differ only in z. A K-map places such rows next to each other.

:::q <span class="tag">Deck 02 slides 15–16, Example 1</span>
Simplify Z = AB' + AB with a two-variable K-map.
:::

:::guess Guess first
AB' and AB differ in one variable. Which one drops out?
:::

:::note Terms
**K-map:** the truth table drawn as a grid, one **cell** per row. The row label gives the first variable(s), the column label the rest. **Adjacent cells:** cells that share a side; their rows differ in exactly one variable.
:::

[[fig:u1_km2|What this map plots: a 2 × 2 grid. Row label A, column label B; each cell is one truth-table row (grey number = row number), filled with F on that row. The ring is one group: the two 1s of row A = 1.|w=32]]

- AB' is row 2 (A B = 1 0); AB is row 3 (1 1). Both cells lie in the row A = 1, side by side.
- Inside the ring A stays 1 and B takes both values. From file 01: AB' + AB = A(B' + B) = A. **The variable that changes inside a group drops out; the one that stays is kept.**

**Answer.** Z = **A**.

:::check Check 1
(a) <span class="tag">Deck 02 slide 14</span> Plot the 2-input OR gate (1 on rows 1, 2, 3) on a two-variable map and read it with two groups. (b) Which cell is adjacent to both cell 1 and cell 2?
:::

### 2 · Three variables: why the columns go 00, 01, 11, 10

Two variables give a 2 × 2 grid, where every pair of side-by-side cells differs in one bit. Three variables need 8 cells, and the order of the columns starts to matter.

:::guess Predict
Label the four columns for y z in counting order 00, 01, 10, 11. Which two neighbouring columns differ in **two** bits? What order fixes it?
:::

:::note Terms
**Gray order:** a sequence of codes in which each code differs from the next in exactly one bit: 00, 01, 11, 10. **Wrap-around:** the last column (10) and the first (00) also differ in one bit, so they count as adjacent, as if the map were rolled into a tube.
:::

[[fig:u1_km3_idx|What this map plots: the empty 3-variable map. Row = x, columns = y z in Gray order. Each grey number is the row number j of the truth table that the cell holds. Columns 3 and 4 are not in counting order.|w=40]]

- Counting order 00, 01, 10, 11 puts 01 next to 10: two bits change, so those cells would not merge. Gray order 00, 01, 11, 10 makes every step one bit.
- So the cells are **not** in counting order: the third column holds rows 3 and 7, the fourth rows 2 and 6. Plot by row number, not by position.
- Each cell has 3 neighbours (one per variable): cell 0 (000) touches 1 (001), 2 (010) across the wrap, and 4 (100).

**Answer to the Predict.** 01 → 10 changes two bits. Gray order **00, 01, 11, 10** fixes it, and 10 → 00 (wrap) is also one bit.

:::check Check 2
(a) List the three neighbours of cell 5 in a 3-variable map. (b) Plot file 01's running example F(x, y, z) = Σm(2, 3, 5, 7): which positions hold the 1s?
:::

### 3 · Reading a group: 2^{k} cells remove k variables

The map is now plotted. Each ring drawn round 1s becomes one product term.

:::guess Predict
File 01's F = Σm(2, 3, 5, 7) gives two rings of two cells each. Read each ring by the variables that stay fixed inside it. Do you get file 01's answer?
:::

:::note Terms
**Group (implicant):** a rectangle of 2^{k} cells, all 1 (or don't-care). It stands for one product term, true on exactly those cells.
:::

[[fig:u1_km3_run|What this map plots: F(x, y, z) = Σm(2, 3, 5, 7). Each 1 is a row where F = 1. Each ring is one group, labelled with the product term it stands for.|w=40]]

**Reading rule:** for each variable, look at its value over the whole group.

| Variable over the group | In the term |
|---|---|
| always 1 | plain (x) |
| always 0 | complemented (x') |
| both 0 and 1 | left out |

- Ring 1, cells 2 and 3 (x y z = 010, 011): x = 0, y = 1, z changes → **x'y**.
- Ring 2, cells 5 and 7 (101, 111): x = 1, z = 1, y changes → **xz**.
- A group of 2^{k} cells has k variables changing: 2 cells → 1 dropped, 4 cells → 2 dropped, 8 → 3.

**Answer to the Predict.** F = **x'y + xz**: the same answer as file 01 step 6, with no algebra.

:::check Check 3
(a) In a 3-variable map, how many literals does a group of 4 leave? A group of 8? (b) Read the group of cells 0, 4 (x y z = 000, 100).
:::

### 4 · Groups as large as possible

Step 3 read groups given to you. Choosing the groups is the skill, and the main rule is: make each one as big as the rules allow.

:::q <span class="tag">Deck 02 slides 27, 33–34</span>
F(a, b, c) = Σm(2, 3, 6, 7). The slide circles two pairs and marks it "Wrong!!". Why, and what is the minimal F?
:::

:::guess Guess first
The two pairs give a'b and ab. Can a'b + ab be simplified further?
:::

<div class="two">

[[fig:u1_km3_wrong|Two pairs (slide 33, "Wrong!!"): a'b + ab, 2 terms, 4 literals.]]

[[fig:u1_km3_right|One quad (slide 34): b, 1 term, 1 literal.]]

</div>

What these maps plot: row = a, columns = b c (Gray order); the four 1s fill the two middle columns, where b = 1.

**The rules** (deck 02 slides 4–10, summary slide 10):

1. A group holds only 1s (or don't-cares); never a 0.
2. Rectangles only: no diagonals.
3. The number of cells is a power of 2: 1, 2, 4, 8, 16. A group of 3 or 5 is not allowed.
4. Groups as **large** as possible; overlap is allowed.
5. Every 1 in at least one group; as **few** groups as possible.
6. Edges wrap: left touches right (and, on a 4-row map, top touches bottom).

Special cases (slides 36–38): all 8 cells 1 → F = 1; no 1s → F = 0; a checkerboard (no two 1s adjacent) has no groups larger than 1 cell: it is a ⊕ b ⊕ c, which needs XOR gates, not a smaller SOP.

**Answer.** The two pairs break rule 4: they sit side by side and form one quad. Inside it a and c both change and b = 1: **F = b**. Algebra agrees: a'b + ab = b.

:::note Slip in the slides
Deck 02 slide 28 plots minterms 2, 3, 6, 7 correctly but prints the function underneath as Σm(2, 4, 5, 7). The pack uses Σm(2, 3, 6, 7) from slide 27.
:::

:::check Check 4
(a) Why is a group of 3 cells never allowed? (b) A 3-variable map has 1s in every cell of the row a = 0. What is F?
:::

### 5 · Prime implicants and essential prime implicants

"As large as possible" and "as few as possible" can pull in different directions when groups overlap. The deck's five-step procedure settles it.

:::q <span class="tag">Deck 02 slides 39–44</span>
Simplify F(a, b, c) = Σm(2, 3, 4, 5, 6).
:::

:::guess Guess first
Cell 6 can join cell 2 or cell 4. Does the choice change the cost?
:::

:::note Terms
**Prime implicant (PI):** a group that cannot be made any larger. **Essential prime implicant (EPI):** a PI that is the **only** PI covering some 1; it must be in the answer. **Cover:** a set of groups that together include every 1.
:::

[[fig:u1_km3_pi|What this map plots: F(a, b, c) = Σm(2, 3, 4, 5, 6) with all four prime implicants ringed. Row = a, columns = b c.|w=42]]

**The procedure** (deck 02 slides 28–32):

1. Plot the 1s.
2. Ring **all** prime implicants.
3. Mark the essential ones: find each 1 covered by only one ring.
4. Cover the 1s that are left with the fewest, largest remaining PIs.
5. Read the map: OR the terms.

**Answer.**

1. PIs: a'b (cells 2, 3), ab' (4, 5), bc' (2, 6), ac' (4, 6).
2. Cell 3 lies only in a'b → a'b is essential. Cell 5 lies only in ab' → ab' is essential.
3. Left uncovered: cell 6. Either bc' or ac' covers it, each with 2 literals.
4. F = **a'b + ab' + bc'** (the slide's answer) or, equally minimal, **a'b + ab' + ac'**: 3 terms, 6 literals either way.

Answer to the Guess: no; both choices cost the same, so this function has **two** minimal answers.

:::check Check 5
<span class="tag">Deck 02 slides 27–32</span> Simplify F(a, b, c) = Σm(2, 3, 4, 5). Which PIs are essential?
:::

### 6 · Four variables: corners and edges

Four variables give a 4 × 4 map: rows a b, columns c d, both in Gray order. Wrap-around now works in both directions.

:::guess Predict
In the 4-variable map, are cells 0 and 8 neighbours? Are the four corner cells 0, 2, 8, 10 one group?
:::

[[fig:u1_km4_idx|What this map plots: the empty 4-variable map. Rows = a b, columns = c d, both in Gray order 00, 01, 11, 10. Each grey number is the truth-table row the cell holds.|w=44]]

- Each cell has 4 neighbours (one per variable). Top row touches bottom row (ab = 00 and 10 differ only in a), left column touches right.
- The four corners (0, 2, 8, 10) are mutually adjacent through both wraps: one quad, b'd'.

Now the running example's seven 1s alone (don't-cares ignored for now, read as 0):

[[fig:u1_km4_nodc|What this map plots: the 1s of MTE Q4, F = Σm(0, 4, 5, 7, 8, 9, 15), with no don't-cares. Each ring is one group of two cells, labelled with its term.|w=44]]

1. Cell 7 (0111) and cell 15 (1111): pair, a changes → **bcd** (essential: no other group reaches 15).
2. Cell 9 (1001) pairs only with cell 8 → **ab'c'** (essential).
3. Cell 5: pair with 4 → **a'bc'**.
4. Cell 0: pair with 8 across the top–bottom wrap → **b'c'd'**.

F = b'c'd' + a'bc' + bcd + ab'c': **4 terms, 12 literals** (two other covers tie: a'c'd' for cells 0, 4, or a'bd for cells 5, 7).

**Answer to the Predict.** Yes: 0 (0000) and 8 (1000) differ only in a. Yes: the corners form one quad, b'd'.

:::check Check 6
<span class="tag">Deck 02 slides 51–53</span> Minimise F(a, b, c, d) = Σm(0, 2, 3, 6, 8, 12, 13, 15).
:::

### 7 · Don't-care conditions

Step 6 left the running example at 12 literals because it read the four X cells as 0. The question allows them to be either.

:::q <span class="tag">MTE 2025 Q4 · 4 marks</span>
Minimize the following Boolean function using K-Map method to obtain a simplified expression. Also draw the logic circuit using basic gates. F(a, b, c, d) = Σm(0, 4, 5, 7–9, 15) + Σd(1, 3, 6, 14)
:::

:::guess Guess first
A don't-care can be read as 0 or as 1. When would you read it as 1?
:::

:::note Terms
**Don't-care (X):** an input row that never occurs, or whose output does not matter (deck 02 slides 66–67). Written Σd( ). "7–9" in the question means rows 7, 8, 9.
:::

[[fig:u1_km4_dc|What this map plots: MTE Q4 with its four don't-cares (X at 1, 3, 6, 14). Each ring is a group of four; X cells inside a ring are read as 1, the X at 3 lies in no ring and is read as 0.|w=44]]

**Rule:** read an X as 1 only when it makes a group **larger**; an X never needs to be covered on its own.

**Answer.**

1. Cells 0, 1, 8, 9 (X at 1; top–bottom wrap): b and c are 0, a and d change → **b'c'**.
2. Cells 6, 7, 14, 15 (X at 6, 14): b = 1, c = 1 → **bc**.
3. Left: cells 4, 5. Quad 0, 1, 4, 5 (X at 1): a = 0, c = 0 → **a'c'**.
4. X at 3 is in no group: read as 0.

$$F = b'c' + bc + a'c'$$

**3 terms, 6 literals**, against 4 terms, 12 literals without the don't-cares (step 6). The quad 4, 5, 6, 7 (a'b) covers cells 4, 5 equally well, so **F = b'c' + bc + a'b** is also minimal; either earns the marks.

The question also asks for the circuit with basic gates: one AND per term, one OR:

[[fig:u1_mte4_andor|MTE Q4 with basic gates: three 2-input ANDs into a 3-input OR. b', c', a' come from NOT gates on the inputs.|w=55]]

:::check Check 7
<span class="tag">Deck 02 slides 69–70</span> Minimise F(a, b, c, d) = Σm(0, 2, 6, 8, 12, 13, 15) + d(3, 4, 9). Which don't-cares do you use?
:::

### 8 · Product of sums: group the 0s

Every answer so far is a sum of products. Grouping the **0s** instead gives a product of sums, which is sometimes cheaper (and is what NOR circuits in file 03 need).

:::q <span class="tag">Deck 02 slide 63 "PoS optimization from SoP"</span>
F(W, X, Y, Z) = Σm(0, 1, 2, 5, 8, 9, 10). Find the minimal SOP and the minimal POS. "Which one is the minimal one?"
:::

:::guess Guess first
A group of 0s is read the opposite way to a group of 1s. If W = 1 and X = 1 throughout a group of 0s, which sum term is it?
:::

<div class="two">

[[fig:u1_km4_sop63|Grouping the 1s (SOP): X'Y' + X'Z' + W'Y'Z.]]

[[fig:u1_km4_pos|Grouping the 0s (POS): (W' + X')(Y' + Z')(X' + Z).]]

</div>

What these maps plot: rows W X, columns Y Z; the same seven 1s; left the groups of 1s, right the groups of 0s.

**Why it works:** the 0s of F are the 1s of F'. Grouping them gives F' as an SOP; De Morgan (file 01 step 5) turns F = (F')' into a product of sums, with every literal flipped.

**Reading a 0-group:** a variable that stays 0 is written **plain**, one that stays 1 **complemented**; OR them. (This is the maxterm rule of file 01 step 8.)

**Answer.**

1. SOP from the 1s: **X'Y' + X'Z' + W'Y'Z**: 3 terms, 7 literals.
2. 0-groups: cells 12–15 (W = 1, X = 1) → (W' + X'); cells 3, 7, 11, 15 (Y = 1, Z = 1) → (Y' + Z'); cells 4, 6, 12, 14 (X = 1, Z = 0) → (X' + Z).
3. POS: **(W' + X')(Y' + Z')(X' + Z)**: 3 terms, 6 literals.
4. The **POS** is minimal here: one literal fewer, and three 2-input gates in place of two 2-input and one 3-input gate.

:::check Check 8
(a) <span class="tag">Deck 02 slide 64</span> F(W, X, Y, Z) = ΠM(0, 2, 3, 4, 5, 6). Find the minimal SOP. (b) Find the minimal POS of the running example (MTE Q4, don't-cares allowed). Is it cheaper than b'c' + bc + a'c'?
:::

### 9 · Five variables: two maps side by side

A fifth variable doubles the cells to 32. The deck handles it with two 4-variable maps.

:::q <span class="tag">Practice set 1 Q1</span>
Minimize the following Boolean function using K-Map method and implement the circuit using universal gate. F(v, w, x, y, z) = Σm(0, 2, 5, 8, 10, 13, 15, 17, 19, 21, 26, 28, 29, 30, 31) + Σd(7, 12, 14, 23, 24)
:::

:::guess Guess first
Rows 0–15 have v = 0 and rows 16–31 have v = 1. If the same block of 1s appears in the same place on both halves, what happens to v?
:::

:::note Terms
**Five-variable map:** two 4-variable maps, one for v = 0 (rows 0–15) and one for v = 1 (rows 16–31). Cells in the **same position** on the two maps are adjacent (they differ only in v).
:::

The deck's warm-up (slides 58–61), F(a, b, c, d, e) = Σm(5, 7, 13, 15, 21, 23, 29, 31):

[[fig:u1_km5_ce|What this map plots: left the a = 0 half, right the a = 1 half; rows b c, columns d e. The same quad (c = 1, e = 1) sits in both halves, so it is one group of 8 and a drops out: F = ce.|w=80]]

**Answer** (the minimising part; the universal-gate circuit is file 03 step 6).

[[fig:u1_km5_ps1q1|What this map plots: practice set 1 Q1. Left v = 0, right v = 1; rows w x, columns y z; X = don't-care. Rings: xz and wz' span both halves (8 cells each), v'x'z' is in the left half only, vw'z in the right half only.|w=86]]

1. **xz** (x = 1, z = 1 in both halves): 5, 7, 13, 15, 21, 23, 29, 31, using X at 7 and 23.
2. **wz'** (w = 1, z = 0 in both halves): 8, 10, 12, 14, 24, 26, 28, 30, using X at 12, 14, 24.
3. Left half, cells 0, 2, 8, 10 (the four positions with x = 0, z = 0): **v'x'z'** (v = 0 only).
4. Right half, cells 17, 19, 21, 23 (w = 0, z = 1): **vw'z**.

$$F = xz + wz' + v'x'z' + vw'z$$

4 terms, 10 literals; every 1 is covered and no smaller cover exists (checked by the Quine–McCluskey method in the pack's verify script).

:::check Check 9
<span class="tag">Deck 02 slide 62</span> Simplify f(V, W, X, Y, Z) = Σm(0, 1, 4, 5, 6, 11, 12, 14, 16, 20, 22, 28, 30, 31).
:::

### 10 · From words to a map

The practice set also gives problems in words. The map is the same; the first job is the truth table.

:::q <span class="tag">Practice set 1 Q4</span>
Design a combinational circuit having 4 inputs that will produce an output '1' when two consecutive input bits are 1 and produce '0' for other cases.
:::

:::guess Guess first
Name the inputs A B C D in order. Which pairs of inputs are "consecutive"? Is 0111 a 1-row?
:::

**Reading the words.** The consecutive pairs are (A, B), (B, C), (C, D). F = 1 when **at least one** of those pairs is 1 1. So 0111 (two such pairs) and 1111 also give 1. (Reading "exactly two 1s, side by side" would drop 0111, 1110, 1111, 1011, 1101; the pack takes the plain reading "two consecutive bits are 1".)

| Rows with F = 1 | A B C D |
|---|---|
| 3 | 0 0 1 1 |
| 6, 7 | 0 1 1 0, 0 1 1 1 |
| 11 | 1 0 1 1 |
| 12, 13, 14, 15 | 1 1 0 0, 1 1 0 1, 1 1 1 0, 1 1 1 1 |

[[fig:u1_km4_ps1q4|What this map plots: F(A, B, C, D) = Σm(3, 6, 7, 11, 12, 13, 14, 15). Rows A B, columns C D. Three quads: AB (row 11), BC, CD (column 11).|w=44]]

**Answer.**

1. Cells 12–15 (A = 1, B = 1) → **AB**.
2. Cells 6, 7, 14, 15 (B = 1, C = 1) → **BC**.
3. Cells 3, 7, 11, 15 (C = 1, D = 1) → **CD**.

$$F = AB + BC + CD$$

Each term is exactly one "consecutive pair": the map confirms the words.

[[fig:u1_ps1q4_andor|The circuit: three 2-input ANDs, one per adjacent pair, into a 3-input OR.|w=55]]

:::check Check 10
Change the circuit so it gives 1 when **three** consecutive input bits are 1. Write F without a map, then check one row.
:::

---

## Exam form

**K-map minimisation (SOP)**, as MTE Q4 expects:

1. Draw the map with Gray-order labels (00, 01, 11, 10) on both sides and the variable names in the corner; write the row numbers in the cells.
2. Enter 1s and Xs (blank = 0).
3. Ring all prime implicants; mark the essential ones; cover the rest with the fewest, largest groups. Use an X only if it enlarges a group.
4. Label each ring with its term (keep the variables that do not change).
5. Write F as the OR of the terms; state "also minimal: …" if another cover ties.
6. Draw the circuit if asked: one AND per term, one OR (basic gates); NAND/NOR versions in file 03.

**POS:** ring the 0s (and Xs), read each ring with the variables flipped, AND the sums.

**Five variables:** two 4-variable maps (first variable 0 and 1); same position = adjacent.

**Rules:** 2^{k} cells; rectangles; wrap-around; largest groups; fewest groups; overlap allowed.

## Traps

- Labelling the map 00, 01, 10, 11 (counting order): neighbours then differ in two bits.
- Plotting by position instead of row number: in Gray order, column 3 holds rows 3, 7, 11, 15.
- Forgetting wrap-around groups (corners, top–bottom).
- Stopping at two pairs when they form a quad (deck 02 slide 33).
- Covering an X that does not enlarge any group.
- Reading a 0-group the SOP way: in a POS, a variable that stays 1 is written complemented.
- In a 5-variable map, grouping a cell with a cell in a different position on the other half.

## Self-test

1. Minimise F(a, b, c) = Σm(0, 1, 2, 3, 7).
2. Minimise F(A, B, C, D) = Σm(0, 1, 2, 5, 6, 7, 8, 9, 10, 14).
3. Minimise F(A, B, C, D) = Σm(1, 3, 7, 11, 15) + d(0, 2, 5).
4. Give the minimal POS of F(A, B, C) = Σm(0, 2, 3, 4, 5, 7).
5. When does a K-map have more than one minimal answer? Give an example from this file.
6. Why must the map's labels be in Gray order? Name the three cells adjacent to cell 6 in a 3-variable map.

<!--ANSWERS-->

## Answers

**Check 1.** (a) Rows 1, 2, 3 are A'B, AB', AB. Ring row A = 1 (cells 2, 3) → A; ring column B = 1 (cells 1, 3) → B: **F = A + B**. (b) **Cell 3** (and cell 0): cell 3 = 11 differs from 01 and 10 in one bit each.

**Check 2.** (a) Cell 5 = 101: change one bit at a time → **4 (100), 7 (111), 1 (001)**. (b) Row x = 0: the two right-hand columns (yz = 11 holds 3, yz = 10 holds 2). Row x = 1: the two middle columns (yz = 01 holds 5, yz = 11 holds 7).

**Check 3.** (a) Group of 4 drops 2 of 3 variables: **1 literal**. Group of 8: **0 literals** (F = 1). (b) Cells 000 and 100: x changes, y = 0, z = 0 → **y'z'**.

**Check 4.** (a) A group must be a product term, and a term with k variables dropped is true on exactly 2^{k} rows: 3 is not a power of 2. (b) **F = a'**.

**Check 5.** PIs: a'b (cells 2, 3) and ab' (cells 4, 5); no other group exists (cells 3 and 4 are not adjacent). Both are essential: **F = a'b + ab'** (= a ⊕ b).

**Check 6.** No quad fits, so every PI is a pair. Essential: **a'b'c** (the only group for 3), **a'cd'** (the only group for 6), **abd** (the only group for 15). Left: 0, 8, 12, which need two more pairs, for example a'b'd' (0, 2) and ac'd' (8, 12): **F = a'b'd' + a'b'c + a'cd' + ac'd' + abd** (5 terms, 15 literals). Two other covers tie: b'c'd' + ac'd', or b'c'd' + abc', for the cells 0, 8, 12.

**Check 7.** Use X at 4 (quad 0, 2, 4, 6 → a'd'; quad 0, 4, 8, 12 → c'd') and X at 9 is not needed; 13, 15 → abd. **F = a'd' + c'd' + abd**; ac' (8, 9, 12, 13 with X at 9) in place of c'd' is equally minimal. X at 3 unused.

**Check 8.** (a) The 1s are rows 1, 7, 8–15: **F = W + XYZ + X'Y'Z** (W covers 8–15; 7 pairs with 15; 1 pairs with 9). (b) 0s at 2, 10, 11, 12, 13 (Xs free). Rings: 2, 3, 10, 11 (X at 3) → (b + c'); 12, 13 → (a' + b' + c). **F = (b + c')(a' + b' + c)**: 2 terms, 5 literals, against 6 for the SOP: **yes, one literal cheaper**.

**Check 9.** **f = XZ' + V'W'Y' + W'Y'Z' + V'WX'YZ + VWXY** (5 terms, 17 literals). XZ' spans both halves (8 cells); none of cell 11's five neighbours (3, 9, 10, 15, 27) is a 1, so 11 stays a single cell, V'WX'YZ; 31 pairs with 30 to give VWXY.

**Check 10.** Three consecutive bits: (A, B, C) or (B, C, D): **F = ABC + BCD**. Row 0111: BCD = 1, so F = 1; row 1101: neither, F = 0.

**Self-test.**

1. **F = a' + bc** (row a = 0 is a quad; cell 7 pairs with 3).
2. **F = B'C' + CD' + A'BD**.
3. **F = CD + A'B'** (X at 0, 2 used), or equally **CD + A'D** (X at 5 used).
4. 0s at rows 1 and 6, no neighbours: **(A + B + C')(A' + B' + C)**.
5. When a 1 can be covered by two different groups of the same size and cost: MTE Q4 (a'c' or a'b), or step 5 (bc' or ac').
6. So that every pair of adjacent cells (including across the wrap) differs in one variable, which is what lets P x + P x' = P drop it. Cell 6 = 110: neighbours **7, 4, 2**.

<!--/ANSWERS-->
