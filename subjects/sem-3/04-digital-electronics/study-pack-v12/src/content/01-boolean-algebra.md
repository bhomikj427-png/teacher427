# 01 — Boolean algebra and canonical forms

<div class="sub">Deck 01 (slides 9–31) · syllabus Unit 1 · mid-term Q1 rests on it · no prerequisite: this is the start</div>

## Map

[[map:1 Gates and laws > 2 Minterms, maxterms, Σm and ΠM|here=1]]

A digital signal has two values, 0 and 1. A **combinational** circuit's output depends only on its present inputs. This file gives the language for describing one; 02 shrinks it, 03 builds it from one gate type.

## The questions this file answers

- <span class="tag">Deck 01 slide 18</span> Simplify F = x'yz + x'yz' + xz.
- <span class="tag">Deck 01 slides 27–29</span> f_{1}(a, b, c) is 1 for rows 001, 010, 100, 110. Write it as Σm and as ΠM.

---

## Build

### 1 · Gates and the laws of Boolean algebra

:::q <span class="tag">Deck 01 slide 18 "Algebraic manipulation"</span>
Simplify F = x'yz + x'yz' + xz.
:::

:::guess Guess first
Which two terms differ in only one variable?
:::

:::note Terms
**Complement x':** 1 when x is 0. **Literal:** a variable or its complement (x and x' are two literals). **Gate:** a circuit for one logic operation.
:::

[[fig:gates_row|The seven gates and their truth tables.]]

AND (AB) is 1 only when both inputs are 1; OR (A + B) when at least one is; NOT inverts. NAND and NOR are AND and OR followed by NOT. **XOR** (A ⊕ B = A'B + AB') is 1 when the inputs differ; **XNOR** (A ⊙ B) when they are equal. n variables give 2^{n} truth-table rows.

| Law | OR form | AND form |
|---|---|---|
| Identity, null | X + 0 = X · X + 1 = 1 | X·1 = X · X·0 = 0 |
| Idempotent, complement | X + X = X · X + X' = 1 | X·X = X · X·X' = 0 |
| Involution | (X')' = X | |
| Distributive | X + YZ = (X + Y)(X + Z) | X(Y + Z) = XY + XZ |
| Absorption | X + XY = X · X + X'Y = X + Y | X(X + Y) = X |
| De Morgan | (X + Y)' = X'Y' | (XY)' = X' + Y' |
| Consensus | XY + X'Z + YZ = XY + X'Z | |

**Duality:** swap + with · and 0 with 1 in any law to get another true law. **De Morgan in words:** break the bar, change the sign.

**Answer.** The first two terms differ only in z: x'y(z + z') + xz = **x'y + xz**. Three 3-input ANDs became two 2-input ANDs.

:::check Check 1
(a) <span class="tag">Deck 01 slide 19</span> Prove x'y'z' + x'yz' + xyz' = x'z' + yz'. (b) Simplify A + A'B. (c) Complement A + B'C with no bar over more than one variable.
:::

### 2 · Minterms, maxterms and canonical forms

:::q <span class="tag">Deck 01 slides 27–29</span>
f_{1}(a, b, c) is 1 for the rows 001, 010, 100 and 110. Write it as a sum of minterms (Σm) and as a product of maxterms (ΠM).
:::

:::guess Guess first
Σm lists the rows where f = 1. Which rows does ΠM list?
:::

:::note Terms
**Minterm m_{j}:** an AND of all variables, 1 only on row j; complement a variable where the row has 0. **Maxterm M_{j}:** an OR of all variables, 0 only on row j; complement where the row has 1. M_{j} = m_{j}'.
:::

| j | a b c | m_{j} | M_{j} | f_{1} |
|---|---|---|---|---|
| 0 | 0 0 0 | a'b'c' | a + b + c | 0 |
| 1 | 0 0 1 | a'b'c | a + b + c' | 1 |
| 2 | 0 1 0 | a'bc' | a + b' + c | 1 |
| 3 | 0 1 1 | a'bc | a + b' + c' | 0 |
| 4 | 1 0 0 | ab'c' | a' + b + c | 1 |
| 5 | 1 0 1 | ab'c | a' + b + c' | 0 |
| 6 | 1 1 0 | abc' | a' + b' + c | 1 |
| 7 | 1 1 1 | abc | a' + b' + c' | 0 |

- **Canonical SOP:** OR of the minterms where F = 1. **Canonical POS:** AND of the maxterms where F = 0. Both are unique; convert by swapping Σ and Π and listing the missing rows.
- **Standard form** has shorter terms (a'b'c + bc' + ac'). To make it canonical, multiply each short term by (x + x') for each missing x: bc' = abc' + a'bc'.

**Answer.** f_{1} = **Σm(1, 2, 4, 6)** = a'b'c + a'bc' + ab'c' + abc'. The missing rows give f_{1} = **ΠM(0, 3, 5, 7)** = (a + b + c)(a + b' + c')(a' + b + c')(a' + b' + c').

:::note Slip in the slides
Deck 01 slide 31 expands the same function and its last line prints a'bc. It should be **a'bc'** (row 2); a'bc is row 3, where f_{1} = 0.
:::

:::check Check 2
(a) F(A, B, C) = Σm(0, 2, 5). Write it as ΠM. (b) Write m_{5} and M_{5} for (A, B, C). (c) Expand f = a'b'c + bc' + ac' into minterms.
:::

---

## Exam form

**Laws.** The table (both columns); duality; De Morgan; prove a law by truth table or by the other laws.

**Canonical forms.** Minterm/maxterm table; Σm ↔ ΠM by the missing rows; standard → canonical by (x + x').

## Traps

- Complementing a maxterm the minterm way: in M_{j}, a 1 in the row gives a complemented variable.
- De Morgan on a product inside a sum: (A + B'C)' = A'(B + C'), not A' + B + C'.
- Listing the same rows in Σm and ΠM.

## Self-test

1. Simplify AB + AB' + A'B.
2. Complement (A + B)C' using De Morgan.
3. F(A, B, C) = Σm(1, 3, 6, 7). Write it as ΠM.
4. Prove the consensus law XY + X'Z + YZ = XY + X'Z.
5. Write F(A, B, C) = A + B'C as Σm.
6. Write XOR and XNOR in SOP form.

<!--ANSWERS-->

## Answers

**Check 1.** (a) Repeat the middle term: x'y'z' + x'yz' + x'yz' + xyz' = x'z'(y' + y) + yz'(x' + x) = x'z' + yz'. (b) (A + A')(A + B) = **A + B**. (c) A'(B'C)' = **A'(B + C')**.

**Check 2.** (a) **ΠM(1, 3, 4, 6, 7)**. (b) m_{5} = **AB'C**; M_{5} = **A' + B + C'**. (c) a'b'c + abc' + a'bc' + ab'c' = **Σm(1, 2, 4, 6)**.

**Self-test.**

1. AB + AB' = A; A + A'B = **A + B**.
2. (A + B)' + C = **A'B' + C**.
3. **ΠM(0, 2, 4, 5)**.
4. YZ = YZ(X + X') = XYZ + X'YZ; XY + XYZ = XY and X'Z + X'YZ = X'Z, so the sum is XY + X'Z.
5. A covers 4–7; B'C covers 1 and 5: **Σm(1, 4, 5, 6, 7)**.
6. A ⊕ B = A'B + AB'; A ⊙ B = A'B' + AB.

<!--/ANSWERS-->
