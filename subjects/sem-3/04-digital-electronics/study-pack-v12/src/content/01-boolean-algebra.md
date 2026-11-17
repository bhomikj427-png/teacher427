# 01 — Boolean algebra and canonical forms

<div class="sub">Deck 01 (slides 5–32) · syllabus Unit 1 (Boolean algebra, canonical forms) · 9 deck examples; the MTE tests this through Q1 and Q4 (files 02, 03) · needs nothing: this is the start</div>

## Map

[[map:1 AND OR NOT > 2 Truth table > 3 Gates > 4 Laws > 5 De Morgan > 6 Simplify > 7 Minterms > 8 Maxterms > 9 Σm ↔ ΠM > 10 Standard → canonical|here=1]]

Every digital circuit is built from wires that carry one of two values, 0 or 1. This file gives the language for saying what such a circuit does: the three basic operations, the truth table, the laws that let you rewrite an expression into a cheaper one, and the two **canonical forms** that write any function as a list of truth-table rows. File 02 does the same simplification with a picture (the K-map); file 03 builds the result from one gate type.

## Symbols

| Symbol | What it means in this file | Typical value |
|---|---|---|
| x, y, z (or A, B, C) | input variables: each one is a wire that is either 0 or 1 | 0 or 1 |
| F | the output: a value (0 or 1) fixed by the inputs on each row of the truth table | 0 or 1 |
| x' | NOT x: 1 when x is 0 | — |
| xy or x·y | x AND y: 1 only when both are 1 | — |
| x + y | x OR y: 1 when at least one is 1 (not arithmetic addition) | — |
| x ⊕ y, x ⊙ y | XOR (1 when x and y differ), XNOR (1 when they are equal) | — |
| n | number of input variables | 3 |
| j | row number: the inputs read as one binary number, first variable the most significant bit | 0 … 2^{n} − 1 |
| m_{j}, M_{j} | minterm and maxterm of row j (steps 7 and 8) | m_{5} = xy'z |
| Σm( ), ΠM( ) | lists of rows: "OR of these minterms", "AND of these maxterms" | Σm(2, 3, 5, 7) |

## Running example

**F(x, y, z) = x'yz + x'yz' + xz** (deck 01 slide 18). It is 1 on rows 2, 3, 5, 7 and 0 on rows 0, 1, 4, 6. Step 3 draws it, step 6 shrinks it to x'y + xz, steps 7–10 write it as Σm(2, 3, 5, 7) and ΠM(0, 1, 4, 6). Files 02 and 03 reuse it.

## The questions this file answers

- <span class="tag">Deck 01 slide 18</span> Simplify F = x'yz + x'yz' + xz.
- <span class="tag">Deck 01 slide 19</span> Prove x'y'z' + x'yz' + xyz' = x'z' + yz'.
- <span class="tag">Deck 01 slides 22–23</span> Write minterm m_{3} and maxterm M_{3} of (A, B, C).
- <span class="tag">Deck 01 slides 27–29</span> f_{1}(a, b, c) is 1 on rows 001, 010, 100, 110: write it as Σm and as ΠM.
- <span class="tag">Deck 01 slides 31–32</span> Convert a standard SOP and a standard POS to canonical form.

---

## Build

### 1 · Three basic operations: AND, OR, NOT

A lamp, a battery and two switches are enough to see all of digital logic.

:::guess Predict
Two switches A and B control one lamp. (i) They are wired one after the other (series). (ii) They are wired side by side (parallel). Write "switch closed" as 1 and "lamp on" as 1. For each wiring, on which of the four switch settings is the lamp on?
:::

:::note Terms
**Binary variable:** a quantity that takes exactly two values, written 0 and 1 (switch open/closed, voltage low/high). **Logic operation:** a rule that gives an output 0 or 1 for every combination of inputs.
:::

- **Series** → the lamp is on only if A **and** B are closed: **AND**, written AB or A·B.
- **Parallel** → the lamp is on if A **or** B (or both) is closed: **OR**, written A + B.
- A push-to-break button (closed when not pressed) gives the opposite of its input: **NOT**, written A'.

| A B | AB (series) | A + B (parallel) | A' |
|---|---|---|---|
| 0 0 | 0 | 0 | 1 |
| 0 1 | 0 | 1 | 1 |
| 1 0 | 0 | 1 | 0 |
| 1 1 | 1 | 1 | 0 |

The "+" is **not** addition: 1 + 1 = 1 in Boolean algebra (deck 01 slide 8), because two closed parallel switches still give one lit lamp.

**Answer to the Predict.** Series: on only for A = B = 1 (one setting of four). Parallel: on for 01, 10, 11 (three settings).

:::check Check 1
(a) A = 1, B = 0: find AB, A + B, and B'. (b) What is (A')'? (c) In Boolean algebra, what is 1 + 1 + 0?
:::

### 2 · The truth table: 2^{n} rows

Step 1 listed every input setting for two inputs. A function of more inputs is described the same way, one row per setting.

:::q <span class="tag">Deck 01 slide 9, "Question & Answer" (our wording)</span>
How many rows does the truth table of a function of n variables have?
:::

:::guess Guess first
Count the rows for 1, 2 and 3 variables. What is the pattern?
:::

:::note Terms
**Truth table:** a list of every input combination with the output on each. It defines the function completely: two expressions with the same truth table are the same function. **Row number j:** the input bits read as one binary number (x the most significant bit): x y z = 1 0 1 is row 5.
:::

The running example on all 2^{3} = 8 rows:

| j | x y z | x'yz | x'yz' | xz | F |
|---|---|---|---|---|---|
| 0 | 0 0 0 | 0 | 0 | 0 | 0 |
| 1 | 0 0 1 | 0 | 0 | 0 | 0 |
| 2 | 0 1 0 | 0 | **1** | 0 | **1** |
| 3 | 0 1 1 | **1** | 0 | 0 | **1** |
| 4 | 1 0 0 | 0 | 0 | 0 | 0 |
| 5 | 1 0 1 | 0 | 0 | **1** | **1** |
| 6 | 1 1 0 | 0 | 0 | 0 | 0 |
| 7 | 1 1 1 | 0 | 0 | **1** | **1** |

Each variable doubles the count: it can be 0 or 1 for every row the others already make. So the rows are 2 × 2 × … × 2 = 2^{n}. Write them in counting order 000, 001, … so no row is missed.

**Answer.** **2^{n}** rows: 2 for one variable, 4 for two, 8 for three, 16 for four.

:::check Check 2
(a) How many rows for 5 variables? (b) Which row number is x = 1, y = 1, z = 0? (c) On which rows is xz equal to 1?
:::

### 3 · The seven gates, and a circuit from an expression

The table of step 2 needs hardware. Each operation has a **gate**: a circuit with one output for one logic operation.

:::guess Predict
NAND is "AND, then NOT". For inputs A = 1, B = 1, what does NAND give? And NOR ("OR, then NOT") for A = 0, B = 0?
:::

:::note Terms
**NAND, NOR:** AND and OR with the output inverted (the small circle, a "bubble", means NOT). **XOR (A ⊕ B):** 1 when the two inputs **differ**; A ⊕ B = A'B + AB'. **XNOR (A ⊙ B):** 1 when they are **equal**; A ⊙ B = A'B' + AB.
:::

[[fig:gates_row|The seven gate symbols (deck 01 slide 10). Under each: the expression it outputs for inputs A and B.]]

| A B | AND | OR | NAND | NOR | XOR | XNOR |
|---|---|---|---|---|---|---|
| 0 0 | 0 | 0 | 1 | 1 | 0 | 1 |
| 0 1 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 1 | 1 | 1 | 0 | 0 | 0 | 1 |

**From expression to circuit** (deck 01 slides 12–14): one AND gate per product term, one OR gate that collects them; a complemented input such as x' comes from a NOT gate (not drawn below; the label x' stands for it).

[[fig:u1_run_before|The running example as written: F = x'yz + x'yz' + xz. Three AND gates (two with 3 inputs, one with 2) feed one 3-input OR.|w=60]]

**Answer to the Predict.** NAND(1, 1) = (1·1)' = **0**. NOR(0, 0) = (0 + 0)' = **1**.

:::check Check 3
(a) For A = B = 1 give NAND, NOR, XOR and XNOR. (b) How many AND-gate inputs does the circuit above use in total? (c) Show from the table that XNOR = (XOR)'.
:::

### 4 · The laws of Boolean algebra

The circuit in step 3 uses 8 AND inputs. The laws are the rules that rewrite an expression into a cheaper one without changing its truth table.

:::guess Predict
In ordinary algebra x + yz ≠ (x + y)(x + z). Try all eight rows with Boolean + and ·. Equal or not?
:::

:::note Terms
**Law (identity):** two expressions that agree on every row of the truth table. **Dual:** the expression obtained by swapping + with · and 0 with 1. The dual of a true law is also a true law.
:::

| Law | OR form | AND form (its dual) |
|---|---|---|
| Identity | X + 0 = X | X·1 = X |
| Null | X + 1 = 1 | X·0 = 0 |
| Idempotent | X + X = X | X·X = X |
| Complement | X + X' = 1 | X·X' = 0 |
| Involution | (X')' = X | |
| Commutative, associative | X + Y = Y + X; (X + Y) + Z = X + (Y + Z) | XY = YX; (XY)Z = X(YZ) |
| Distributive | X + YZ = (X + Y)(X + Z) | X(Y + Z) = XY + XZ |
| Absorption | X + XY = X; X + X'Y = X + Y | X(X + Y) = X |
| Consensus | XY + X'Z + YZ = XY + X'Z | |

Read two of them in switch language. **X + 1 = 1:** a closed switch in parallel with anything lights the lamp. **X + XY = X:** if X is closed the lamp is on; adding "X and Y" in parallel never adds a new way to light it.

Every law is proved by checking all rows (perfect induction), or derived from laws already proved.

**Answer to the Predict.** Equal. X = 1: both sides are 1. X = 0: the left is YZ, the right is (Y)(Z) = YZ. This second distributive law has no ordinary-algebra twin and is the one most often forgotten.

:::check Check 4
(a) Simplify X + X'Y using the distributive law. (b) Write the dual of X + 0 = X. (c) Simplify X(X + Y).
:::

### 5 · De Morgan's theorem

The laws in step 4 never put a bar over a whole sum or product. De Morgan's theorem removes such a bar, and file 03 rests on it.

:::q <span class="tag">Deck 01 slide 15 (our wording)</span>
Complement F = A + B'C so that no bar covers more than one variable.
:::

:::guess Guess first
Is (A + B)' the same as A' + B'? Try A = 1, B = 0.
:::

:::note Terms
**Complement of a function F':** the function that is 1 exactly on the rows where F is 0.
:::

$$(X + Y)' = X'·Y'          (X·Y)' = X' + Y'$$

Read in words: "neither X nor Y" is "not X and not Y"; "not both" is "at least one is not". Proof by all four rows:

| X Y | (X + Y)' | X'Y' | (XY)' | X' + Y' |
|---|---|---|---|---|
| 0 0 | 1 | 1 | 1 | 1 |
| 0 1 | 0 | 0 | 1 | 1 |
| 1 0 | 0 | 0 | 1 | 1 |
| 1 1 | 0 | 0 | 0 | 0 |

**Rule:** break the bar, change the sign (+ ↔ ·), and complement each piece. It holds for any number of variables: (X + Y + Z)' = X'Y'Z'.

**Answer.**

1. (A + B'C)' = A' · (B'C)'  — De Morgan on the sum
2. = A' · (B'' + C')  — De Morgan on the product B'C
3. = **A'(B + C')**  — involution, B'' = B

Answer to the Guess: no. A = 1, B = 0 gives (1 + 0)' = 0 but 1' + 0' = 1.

:::check Check 5
(a) Complement xyz. (b) Complement (A + B)C'. (c) Find F' for the running example's short form F = x'y + xz.
:::

### 6 · Algebraic simplification

With the laws and De Morgan in hand, the running example can be shrunk.

:::q <span class="tag">Deck 01 slide 18 "Algebraic manipulation"</span>
Simplify F = x'yz + x'yz' + xz.
:::

:::guess Guess first
Which two terms differ in only one variable?
:::

:::note Terms
**Literal:** one appearance of a variable, plain or complemented (x'yz has three literals). **Cost** of an SOP: the number of terms and literals; fewer means fewer and smaller gates.
:::

The key move: two terms that are identical except for one variable, plain in one and complemented in the other, merge and lose that variable:

$$P·z + P·z' = P(z + z') = P·1 = P$$

**Answer.**

1. F = x'yz + x'yz' + xz
2. = x'y(z + z') + xz  — distributive, factor out x'y
3. = x'y · 1 + xz  — complement, z + z' = 1
4. = **x'y + xz**  — identity

Cost: from 3 terms, 8 literals to 2 terms, 4 literals.

[[fig:u1_run_after|The same function after simplification: two 2-input ANDs and a 2-input OR (compare the circuit in step 3).|w=55]]

The step-2 truth table confirms it: x'y is 1 on rows 2, 3 and xz on rows 5, 7, the same four rows as before.

:::check Check 6
(a) <span class="tag">Deck 01 slide 19</span> Prove x'y'z' + x'yz' + xyz' = x'z' + yz'. (Hint: a term may be used twice, since X + X = X.) (b) Simplify xy + xy'z.
:::

### 7 · Minterms and the canonical sum of products

Step 6 found a short form by insight. A **canonical form** is a fixed way to write any function straight from its truth table, with no insight needed.

:::q <span class="tag">Deck 01 slide 22 "Minterm"</span>
Write minterm m_{3} of the variables (A, B, C).
:::

:::guess Guess first
m_{3} must be 1 on row 3 (A B C = 0 1 1) and 0 on every other row. Which AND of A, B, C (some complemented) does that?
:::

:::note Terms
**Minterm m_{j}:** an AND of **all** n variables that is 1 on row j only. Each variable appears plain where row j has a 1 and complemented where it has a 0. **Canonical SOP (sum of minterms):** the OR of the minterms of the rows where F = 1, written Σm(…).
:::

| j | x y z | m_{j} | F |
|---|---|---|---|
| 0 | 0 0 0 | x'y'z' | 0 |
| 1 | 0 0 1 | x'y'z | 0 |
| 2 | 0 1 0 | x'yz' | 1 |
| 3 | 0 1 1 | x'yz | 1 |
| 4 | 1 0 0 | xy'z' | 0 |
| 5 | 1 0 1 | xy'z | 1 |
| 6 | 1 1 0 | xyz' | 0 |
| 7 | 1 1 1 | xyz | 1 |

The running example is 1 on rows 2, 3, 5, 7, so

$$F = x'yz' + x'yz + xy'z + xyz = Σm(2, 3, 5, 7)$$

Read it: "F is 1 on row 2, or row 3, or row 5, or row 7". The canonical SOP is **unique**: one function, one list (deck 01 slide 25). The short form x'y + xz is a **standard** SOP: not unique, cheaper.

**Answer.** Row 3 is A B C = 0 1 1: A complemented, B and C plain: **m_{3} = A'BC**.

:::check Check 7
(a) Write m_{5} for (A, B, C). (b) Write F(A, B, C) = AB + C' as Σm.
:::

### 8 · Maxterms and the canonical product of sums

Step 7 listed where F is 1. The other view lists where F is 0, and is built from ORs.

:::q <span class="tag">Deck 01 slide 23 "Maxterm"</span>
Write maxterm M_{3} of the variables (A, B, C).
:::

:::guess Guess first
M_{3} must be 0 on row 3 only. An OR is 0 only when every input is 0. So on row 3 (0 1 1), which of A, B, C must appear complemented?
:::

:::note Terms
**Maxterm M_{j}:** an OR of **all** n variables that is 0 on row j only. Each variable appears plain where row j has a **0** and complemented where it has a **1** (the opposite of a minterm). M_{j} = (m_{j})'. **Canonical POS (product of maxterms):** the AND of the maxterms of the rows where F = 0, written ΠM(…).
:::

| j | x y z | M_{j} | F |
|---|---|---|---|
| 0 | 0 0 0 | x + y + z | **0** |
| 1 | 0 0 1 | x + y + z' | **0** |
| 4 | 1 0 0 | x' + y + z | **0** |
| 6 | 1 1 0 | x' + y' + z | **0** |

(Only the four rows where F = 0 are shown.) The running example is

$$F = (x + y + z)(x + y + z')(x' + y + z)(x' + y' + z) = ΠM(0, 1, 4, 6)$$

Read it: "F is 0 on row 0, and on row 1, …": each maxterm forces a 0 on its own row, and the AND passes that 0 through; on every other row all four factors are 1.

**Answer.** Row 3 is 0 1 1: A plain, B and C complemented: **M_{3} = A + B' + C'**. Check: De Morgan on m_{3}: (A'BC)' = A + B' + C', so M_{3} = m_{3}'.

:::check Check 8
(a) Write M_{5} for (A, B, C). (b) On which single row is (a + b' + c) equal to 0?
:::

### 9 · Converting between Σm and ΠM

Steps 7 and 8 wrote the same function twice. The two lists are linked by one rule.

:::q <span class="tag">Deck 01 slides 27–29</span>
f_{1}(a, b, c) is 1 for the rows 001, 010, 100 and 110. Write it as a sum of minterms and as a product of maxterms.
:::

:::guess Guess first
Σm lists the rows where f = 1. Which rows does ΠM list?
:::

Every row is either a 1-row or a 0-row. So:

- **Σm → ΠM:** list the row numbers **missing** from the Σm list, and swap Σm for ΠM.
- **F → F':** F' = Σm(the missing rows): the complement uses the other list with the same symbol.

Running example: rows 0–7, Σm(2, 3, 5, 7) → missing 0, 1, 4, 6 → ΠM(0, 1, 4, 6), which is what step 8 built.

**Answer.**

1. Rows 001, 010, 100, 110 are rows 1, 2, 4, 6.
2. f_{1} = **Σm(1, 2, 4, 6)** = a'b'c + a'bc' + ab'c' + abc'.
3. The missing rows are 0, 3, 5, 7: f_{1} = **ΠM(0, 3, 5, 7)** = (a + b + c)(a + b' + c')(a' + b + c')(a' + b' + c').

:::check Check 9
(a) F(A, B, C) = Σm(0, 2, 5). Write it as ΠM. (b) Write F' for the same F as Σm.
:::

### 10 · From a standard form to a canonical form

Simplification (step 6) goes from canonical to short. Exams also ask the reverse: expand a short form until every term holds every variable.

:::q <span class="tag">Deck 01 slides 31–32</span>
Convert f_{1} = a'b'c + bc' + ac' to canonical SOP; convert a standard POS to canonical POS.
:::

:::guess Guess first
bc' lacks a. How can you put a into it without changing its value?
:::

:::note Terms
**Standard SOP / POS:** a sum of products (product of sums) whose terms need not contain every variable. Not unique (deck 01 slide 30).
:::

**SOP:** AND each short term with (x + x') = 1 for each missing variable x, then distribute.

1. bc' = bc'(a + a') = abc' + a'bc'  — rows 6 and 2
2. ac' = ac'(b + b') = abc' + ab'c'  — rows 6 and 4
3. f_{1} = a'b'c + abc' + a'bc' + ab'c' (abc' once, X + X = X) = **Σm(1, 2, 4, 6)**

**POS:** OR each short sum with x·x' = 0 for each missing x, then use X + YZ = (X + Y)(X + Z). Running example's short POS (x + y)(x' + z):

1. x + y = x + y + zz' = (x + y + z)(x + y + z')  — rows 0 and 1
2. x' + z = x' + z + yy' = (x' + y + z)(x' + y' + z)  — rows 4 and 6
3. F = **ΠM(0, 1, 4, 6)**, as in step 8.

**Shortcut:** a term with k missing variables covers 2^{k} rows; list them by filling the missing bits every way.

:::note Slip in the slides
Deck 01 slide 31 ends the expansion of f_{1} with the term a'bc. It should be **a'bc'** (row 2); a'bc is row 3, where f_{1} = 0. The pack uses a'bc'.
:::

**Answer.** f_{1} = a'b'c + a'bc' + ab'c' + abc' = Σm(1, 2, 4, 6) (step 9's function); the POS example gives ΠM(0, 1, 4, 6).

:::check Check 10
(a) Expand F(A, B, C) = A + B'C into Σm. (b) Expand (a + b')(b + c) into ΠM.
:::

---

## Exam form

**Laws.** Reproduce the table of step 4 (both columns) and state duality. Prove a law either by the full truth table or line by line from earlier laws, naming the law on each line.

**De Morgan.** (X + Y)' = X'Y', (XY)' = X' + Y'; to complement an expression, break each bar from the outside in and change the sign; show each line.

**Algebraic simplification.**

1. Find two terms identical except for one variable (plain in one, complemented in the other).
2. Factor: P(x + x') = P. Repeat; reuse a term if needed (X + X = X).
3. Finish with absorption (X + XY = X, X + X'Y = X + Y).

**Canonical forms.**

1. Write the truth table, rows 0 to 2^{n} − 1.
2. Σm: rows where F = 1; minterm = AND, variable complemented where the row has 0.
3. ΠM: rows where F = 0; maxterm = OR, variable complemented where the row has 1.
4. Σm ↔ ΠM: the missing rows. Standard → canonical: AND with (x + x') (SOP) or OR with xx' (POS).

## Traps

- Reading + as addition: 1 + 1 = 1, not 2 (or 10).
- Writing a maxterm the minterm way: in M_{j}, a 1 in the row gives a **complemented** variable.
- De Morgan on a product inside a sum: (A + B'C)' = A'(B + C'), not A' + B + C'.
- Listing the same rows in Σm and ΠM: they are complementary lists.
- Forgetting the second distributive law X + YZ = (X + Y)(X + Z).
- Expanding a short term and then counting the shared minterm twice (abc' in step 10).

## Self-test

1. Simplify AB + AB' + A'B.
2. Complement (A + B)C' with no bar over more than one variable.
3. F(A, B, C) = Σm(1, 3, 6, 7). Write it as ΠM.
4. Prove the consensus law XY + X'Z + YZ = XY + X'Z.
5. Write F(A, B, C) = A + B'C as Σm (done in Check 10a; now write it as ΠM).
6. Write XOR and XNOR of A, B in SOP form.
7. A function of 4 variables: how many truth-table rows? Write m_{9} and M_{9} for (A, B, C, D).

<!--ANSWERS-->

## Answers

**Check 1.** (a) AB = **0**, A + B = **1**, B' = **1**. (b) (A')' = **A** (involution). (c) **1**.

**Check 2.** (a) 2^{5} = **32**. (b) 110 = **row 6**. (c) xz = 1 needs x = 1 and z = 1: rows **5 and 7**.

**Check 3.** (a) NAND **0**, NOR **0**, XOR **0**, XNOR **1**. (b) 3 + 3 + 2 = **8** inputs. (c) In every row of the gate table the XNOR column is the XOR column inverted (0 1 1 0 against 1 0 0 1).

**Check 4.** (a) X + X'Y = (X + X')(X + Y) = 1·(X + Y) = **X + Y**. (b) **X·1 = X**. (c) X(X + Y) = XX + XY = X + XY = **X**.

**Check 5.** (a) (xyz)' = **x' + y' + z'**. (b) ((A + B)C')' = (A + B)' + C'' = **A'B' + C**. (c) F' = (x'y)'(xz)' = (x + y')(x' + z'); multiplying out, x·x' = 0, so F' = xz' + x'y' + y'z' and by consensus (y'z' is the consensus of xz' and x'y') **F' = xz' + x'y'**. Check on rows: 1 on 0, 1, 4, 6, the 0-rows of F.

**Check 6.** (a) Use x'yz' twice (X + X = X): x'y'z' + x'yz' + x'yz' + xyz' = x'z'(y' + y) + yz'(x' + x) = **x'z' + yz'**. (b) xy + xy'z = x(y + y'z) = x(y + z) = **xy + xz** (absorption X + X'Y = X + Y).

**Check 7.** (a) Row 5 = 1 0 1: **m_{5} = AB'C**. (b) AB is 1 on rows 6, 7; C' on rows 0, 2, 4, 6: F = **Σm(0, 2, 4, 6, 7)**.

**Check 8.** (a) Row 5 = 1 0 1: **M_{5} = A' + B + C'**. (b) All three literals 0: a = 0, b = 1, c = 0: **row 2** (010).

**Check 9.** (a) Missing rows: **ΠM(1, 3, 4, 6, 7)**. (b) **F' = Σm(1, 3, 4, 6, 7)**.

**Check 10.** (a) A covers rows 4–7 (A = 1, B and C anything); B'C covers rows 1 and 5 (B = 0, C = 1, A anything): **Σm(1, 4, 5, 6, 7)**. (b) a + b' is 0 when a = 0, b = 1: rows 2, 3. b + c is 0 when b = 0, c = 0: rows 0, 4. **ΠM(0, 2, 3, 4)**.

**Self-test.**

1. AB + AB' = A(B + B') = A; then A + A'B = **A + B**.
2. ((A + B)C')' = (A + B)' + C = **A'B' + C**.
3. Missing rows of 0–7: **ΠM(0, 2, 4, 5)**.
4. YZ = YZ(X + X') = XYZ + X'YZ. Then XY + XYZ = XY and X'Z + X'YZ = X'Z (absorption), so XY + X'Z + YZ = **XY + X'Z**.
5. Σm(1, 4, 5, 6, 7) leaves rows 0, 2, 3: **ΠM(0, 2, 3)**.
6. **A ⊕ B = A'B + AB'**; **A ⊙ B = A'B' + AB**.
7. **16** rows. Row 9 = 1001: **m_{9} = AB'C'D**, **M_{9} = A' + B + C + D'**.

<!--/ANSWERS-->
