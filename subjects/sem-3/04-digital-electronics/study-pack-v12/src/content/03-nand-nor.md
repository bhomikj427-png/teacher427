# 03 — NAND-only and NOR-only circuits

<div class="sub">Deck 01 (slides 33–47) · syllabus Unit 1 (universal gates, NAND/NOR implementation) · 3 real questions: MTE 2025 Q1 (2 marks), practice set 1 Q2, practice set 1 Q1 (circuit part) · needs 01 step 5 (De Morgan), 02 steps 7–9 (minimal SOP and POS)</div>

## Map

[[map:1 NAND is universal > 2 NOR is universal > 3 SOP → NAND–NAND > 4 Multi-level NAND > 5 POS → NOR–NOR > 6 Map → NAND only > 7 XOR from 4 NANDs|here=1]]

File 02 ended with minimal expressions such as F = b'c' + bc + a'c', drawn with AND, OR and NOT gates. A chip is cheaper and simpler when every gate is the same kind. This file shows that NAND alone, or NOR alone, can build any circuit, and gives the recipe for turning a minimal SOP into NAND gates and a minimal POS into NOR gates. Later files (05 MUX, 06 decoder) use the same gates as building blocks.

## Symbols

| Symbol | What it means in this file | Typical value |
|---|---|---|
| (XY)' | NAND of X and Y: 0 only when both are 1 | — |
| (X + Y)' | NOR of X and Y: 1 only when both are 0 | — |
| bubble | the small circle on a gate pin: a NOT at that point | — |
| level | how many gates a signal passes through from input to output | 2 for SOP/POS |
| AND-level / OR-level | in a multi-level circuit, a gate that does an AND (or an OR) of the expression | — |
| gate count | number of gates in the circuit; inverters for complemented inputs counted separately | 3–6 |

## Running example

**File 02's MTE Q4 answer, F = b'c' + bc + a'c'** (SOP) and its POS F = (b + c')(a' + b' + c) (file 02 Check 8b). Step 3's Check builds the SOP from NAND gates; step 6's Check builds both and compares gate counts.

## The questions this file answers

- <span class="tag">MTE 2025 Q1 · 2 marks</span> Optimized the following expression and implement using 2-input NOR gate. F = P'Q' + P'
- <span class="tag">Practice set 1 Q2</span> Minimize the following expression using K-Map and realize using NAND gates only. F(w, x, y, z) = Σm(0, 1, 3, 5, 7, 10, 11) + d(2, 6, 13)
- <span class="tag">Practice set 1 Q1 (second half)</span> … implement the circuit using universal gate (the function minimised in file 02 step 9).
- <span class="tag">Deck 01 slides 41, 42, 45</span> NAND–NAND for X'Y'Z' + XYZ'; multi-level NAND for (AB' + A'B)E(C + D'); NOR–NOR for (X' + Y)(X + Y')Z'.

---

## Build

### 1 · NAND alone is enough

File 01 step 3 defined NAND as "AND, then NOT". The claim of this step is stronger: NAND gates alone can make NOT, AND and OR, and so any circuit at all.

:::guess Predict
A 2-input NAND has both its inputs tied to the same wire X. What is its output? (Try X = 0 and X = 1.)
:::

:::note Terms
**Universal gate:** a gate type from which NOT, AND and OR can all be built; since every function has an SOP (file 01 step 7), that means every function. **Tied inputs:** both inputs of a gate connected to one wire, so they always carry the same value.
:::

[[fig:universal_nand|NOT, AND and OR built from NAND gates only (deck 01 slide 35). Left: inputs tied. Middle: a NAND followed by a NAND used as an inverter. Right: each input inverted first, then a NAND.]]

| Build | Circuit | Why (one line each) |
|---|---|---|
| NOT | NAND(X, X) | (X·X)' = X' (idempotent: X·X = X) |
| AND | NAND, then NOT | ((XY)')' = XY (involution) |
| OR | NAND(X', Y') | (X'·Y')' = X'' + Y'' = X + Y (De Morgan) |

The OR line is the key fact for the rest of the file: **a NAND is an OR gate with a bubble on each input.**

**Answer to the Predict.** X = 0 → (0·0)' = 1; X = 1 → (1·1)' = 0: the output is **X'**, so a tied NAND is an inverter.

:::check Check 1
(a) How many NAND gates does an OR of two variables take (inverters included)? (b) Build a 3-input AND from 2-input NANDs only: how many gates?
:::

### 2 · NOR alone is enough

NOR is the dual of NAND (swap AND and OR, file 01 step 4), so the same three builds work with the roles swapped.

:::q <span class="tag">MTE 2025 Q1 · 2 marks</span>
Optimized the following expression and implement using 2-input NOR gate. F = P'Q' + P'
:::

:::guess Guess first
Before drawing anything: can the answer still depend on Q?
:::

[[fig:u1_universal_nor|NOT, OR and AND built from NOR gates only (deck 01 slide 43). Left: inputs tied. Middle: a NOR then a NOR inverter. Right: each input inverted first, then a NOR.]]

| Build | Circuit | Why |
|---|---|---|
| NOT | NOR(X, X) | (X + X)' = X' |
| OR | NOR, then NOT | ((X + Y)')' = X + Y |
| AND | NOR(X', Y') | (X' + Y')' = X''·Y'' = XY (De Morgan) |

So **a NOR is an AND gate with a bubble on each input.**

**Answer.**

1. F = P'Q' + P' = P'(Q' + 1)  — factor out P'
2. = P'·1 = **P'**  — null law, Q' + 1 = 1 (or absorption X + XY = X directly)
3. Q drops out. One 2-input NOR with both inputs tied to P gives (P + P)' = P':

[[fig:nor_inverter|MTE Q1: the whole circuit is one 2-input NOR used as an inverter.|w=40]]

Five gates (two inverters, an AND, an OR) shrink to **one** gate because the expression was simplified first.

:::check Check 2
(a) Build a 2-input AND from NOR gates only. How many gates? (b) Implement F = P' + Q' with 2-input NOR gates only.
:::

### 3 · From a minimal SOP to NAND–NAND

Steps 1–2 build single gates. A whole AND–OR circuit converts in one move.

:::q <span class="tag">Deck 01 slides 40–41</span>
Implement F = X'Y'Z' + XYZ' with NAND gates only.
:::

:::guess Guess first
Take the AND–OR circuit. Replace every gate, the ANDs and the OR, by a NAND. Does the output change?
:::

:::note Terms
**Two-level circuit:** first-level gates make the product terms, one second-level gate combines them. **Bubble pushing:** adding a pair of bubbles (two NOTs) on one wire, which leaves the signal unchanged, then moving each bubble into a gate.
:::

**Why the swap works**, in three lines (F = P + Q with P, Q the product terms):

1. F = P + Q = ((P + Q)')'  — involution
2. = (P'·Q')'  — De Morgan
3. = NAND(NAND(…P…), NAND(…Q…))  — P' is the NAND of P's literals

In pictures: put two bubbles on each wire between the levels. One bubble turns each AND into a NAND; the other moves onto the OR's inputs, and an OR with input bubbles is a NAND (step 1).

[[fig:u1_nand_141|F = X'Y'Z' + XYZ' with NAND gates only: two 3-input NANDs (one per product term) into a 2-input NAND. Same layout as the AND–OR circuit.|w=60]]

**Recipe:** minimal SOP → draw AND–OR → change every gate to NAND. Nothing else moves.

**Answer.** NAND1(X', Y', Z') and NAND2(X, Y, Z') feed NAND3: F = ((X'Y'Z')'·(XYZ')')' = X'Y'Z' + XYZ'. Three NAND gates (plus NAND inverters for X', Y', Z' if only X, Y, Z are available).

:::note Slip in the slides
Deck 01 slide 41 labels the output of both circuits **Z**, the name of an input. The pack calls the output **F**.
:::

:::check Check 3
(a) Implement the running example F = b'c' + bc + a'c' with NAND gates only. How many gates (complemented inputs given)? (b) Implement file 01's running example x'y + xz with NAND gates only.
:::

### 4 · Multi-level NAND circuits, and lone literals

Not every expression is a flat SOP. When AND and OR levels alternate more than twice, the same bubble idea still works, level by level.

:::q <span class="tag">Deck 01 slides 39, 42</span>
Implement F = (AB' + A'B)·E·(C + D') with NAND gates only.
:::

:::guess Guess first
The variable E goes straight into the last AND. When that AND becomes a NAND, does E need an inverter?
:::

:::note Terms
**AND-level gate:** a gate that ANDs its inputs in the expression → becomes a plain NAND. **OR-level gate:** a gate that ORs its inputs → becomes a NAND whose inputs must arrive **complemented** (an OR with input bubbles).
:::

**Rule** (deck 01 slide 39):

1. Draw the AND/OR circuit straight from the expression.
2. Every AND → NAND. Every OR → NAND with inverted inputs.
3. A wire from a NAND into an OR-level gate already carries the bubble it needs.
4. A **lone literal** (straight from an input) into an **OR-level** gate must be complemented; into an AND-level gate it goes in plain.
5. If the output gate is AND-level, its NAND gives F': add one NAND inverter.

**Answer**, gate by gate:

| Gate | Inputs | Output | Role |
|---|---|---|---|
| N1 | A, B' | (AB')' | AND-level |
| N2 | A', B | (A'B)' | AND-level |
| N3 | N1, N2 | ((AB')'(A'B)')' = AB' + A'B | OR-level: inputs already complemented |
| N4 | C', D | (C'D)' = C + D' | OR-level: lone literals C, D' enter complemented |
| N5 | N3, E, N4 | ((AB' + A'B)·E·(C + D'))' = F' | AND-level: E enters plain |
| N6 | N5, N5 | F | inverter, because the last level is an AND |

**6 NAND gates** (with A', B', C' available; three more NAND inverters otherwise). Answer to the Guess: **no**, E enters plain, because the last gate is AND-level.

:::check Check 4
(a) Implement F = A + BC with NAND gates only. Which input is complemented, and why? (b) Implement F = (A + B)(C + D) with NAND gates only. How many gates?
:::

### 5 · From a minimal POS to NOR–NOR

The NOR version is the dual of step 3: start from a product of sums, not a sum of products.

:::q <span class="tag">Deck 01 slides 44–45</span>
Implement F = (X' + Y)(X + Y')Z' with NOR gates only.
:::

:::guess Guess first
Z' is a lone literal entering the output AND. When that AND becomes a NOR (an AND with input bubbles), which signal must the wire carry: Z or Z'?
:::

**Why the swap works** (F = S·T with S, T the sum terms):

1. F = S·T = ((S·T)')'  — involution
2. = (S' + T')'  — De Morgan
3. = NOR(NOR(…S…), NOR(…T…))  — S' is the NOR of S's literals

**Recipe:** minimal POS → draw OR–AND → change every gate to NOR; a lone literal into the output gate enters complemented.

[[fig:u1_nor_145|F = (X' + Y)(X + Y')Z' with NOR gates only: NOR(X', Y) and NOR(X, Y') feed the output NOR; the lone literal enters as Z.|w=60]]

**Answer.** NOR1(X', Y) = (X' + Y)', NOR2(X, Y') = (X + Y')', and the lone literal Z' enters complemented, as **Z** = (Z')'. Output: NOR3((X' + Y)', (X + Y')', Z) = (X' + Y)(X + Y')Z' (De Morgan). **3 NOR gates.**

Do not start a NOR–NOR circuit from an SOP: swapping AND–OR for NOR–NOR gives a different function.

:::check Check 5
(a) How many 2-input NOR gates realise F = (A + B)(C + D)? (b) Realise F = (A + B)C with NOR gates only.
:::

### 6 · Map to NAND-only, in one go

Steps 3–5 started from a given expression. Exam questions start from Σm and ask for both the map and the gates.

:::q <span class="tag">Practice set 1 Q2</span>
Minimize the following expression using K-Map and realize using NAND gates only. F(w, x, y, z) = Σm(0, 1, 3, 5, 7, 10, 11) + d(2, 6, 13)
:::

:::guess Guess first
For a NAND-only answer, do you need the minimal SOP or the minimal POS?
:::

[[fig:u1_km4_ps1q2|What this map plots: practice set 1 Q2. Rows w x, columns y z; X = don't-care. Three quads: w'x' (row 00, using X at 2), w'z (cells 1, 3, 5, 7), x'y (cells 2, 3, 10, 11).|w=44]]

**Answer.**

1. Quad 0, 1, 2, 3 (X at 2): w = 0, x = 0 → **w'x'**.
2. Quad 1, 3, 5, 7: w = 0, z = 1 → **w'z**.
3. Quad 2, 3, 10, 11 (X at 2): x = 0, y = 1 → **x'y**. X at 6 and 13 unused.
4. F = **w'x' + w'z + x'y** (3 terms, 6 literals).
5. NAND–NAND (step 3): three 2-input NANDs (w', x' · w', z · x', y) into one 3-input NAND.

[[fig:u1_nand_ps1q2|Practice set 1 Q2 with NAND gates only. 4 gates; w' and x' from two more NAND inverters if only w, x are available.|w=60]]

The same recipe finishes **practice set 1 Q1** ("implement using universal gate"): its minimal SOP from file 02 step 9, F = xz + wz' + v'x'z' + vw'z, becomes four NANDs into one 4-input NAND.

[[fig:u1_nand_ps1q1|Practice set 1 Q1 with NAND gates only: one NAND per term of the minimal SOP, into a 4-input NAND.|w=62]]

Answer to the Guess: the **SOP** (NAND–NAND); the POS would go to NOR–NOR.

:::check Check 6
The running example has minimal SOP b'c' + bc + a'c' and minimal POS (b + c')(a' + b' + c) (file 02 Check 8b). (a) Count the gates for a NAND-only and for a NOR-only version (complemented inputs given). (b) Which would you build?
:::

### 7 · XOR from four NAND gates

XOR (file 01 step 3) is not a two-level AND–OR gate, but NAND still builds it, with fewer gates than the SOP recipe would use.

:::q <span class="tag">Deck 01 slides 46–47</span>
Build XOR, F = A ⊕ B = A'B + AB', from NAND gates. How many are needed?
:::

:::guess Guess first
The SOP A'B + AB' through the step-3 recipe needs two NANDs for the terms, one for the output, plus two inverters: 5 gates. Can a gate be shared?
:::

[[fig:xor_nand|XOR from four NAND gates (deck 01 slide 47). The first gate's output (AB)' feeds both middle gates.|w=60]]

1. N1 = (AB)'
2. N2 = (A·N1)' = (A(AB)')' ; since A(AB)' = A(A' + B') = AB', N2 = (AB')'
3. N3 = (B·N1)' = (A'B)' by the same steps
4. F = (N2·N3)' = AB' + A'B = **A ⊕ B**  — step 3's NAND–NAND output

The shared gate N1 replaces both inverters: A(A' + B') = AB' supplies the complement B' "for free".

**Answer.** **4 NAND gates.**

:::check Check 7
(a) Check the four-NAND circuit on the row A = 1, B = 1: give N1, N2, N3, F. (b) XNOR = (A ⊕ B)': how many NAND gates?
:::

---

## Exam form

**Universality** (draw all three and write the line under each):

| | from NAND | from NOR |
|---|---|---|
| NOT | inputs tied: (XX)' = X' | inputs tied: (X + X)' = X' |
| AND | NAND + NAND inverter | NOR(X', Y') = XY |
| OR | NAND(X', Y') = X + Y | NOR + NOR inverter |

**Two-level conversion.**

1. Simplify first (map or algebra).
2. NAND only: minimal **SOP** → AND–OR → every gate NAND.
3. NOR only: minimal **POS** → OR–AND → every gate NOR.
4. A lone literal into the output gate enters **complemented**.
5. Prove the output with De Morgan in one line.

**Multi-level NAND:** AND-level → NAND; OR-level → NAND with complemented inputs; lone literals into OR-level gates complemented; an AND-level output needs a final NAND inverter.

## Traps

- Building NOR–NOR from an SOP (or NAND–NAND from a POS): it gives the wrong function.
- Forgetting to complement a lone literal at the output gate (step 3–5 rule).
- Not simplifying first: MTE Q1's F = P' needs one gate, not five.
- Counting "2-input NOR" answers with 3-input gates when the question fixes 2 inputs.
- In multi-level circuits, forgetting the final inverter when the last level is an AND.

## Self-test

1. Prove that NOR is universal.
2. Realise F = AB + CD with NAND gates only. How many gates?
3. Realise F = (A + B)C with NOR gates only. How many gates?
4. Simplify F = A'B + A'B' + AB' and implement it with one gate.
5. Realise file 01's x'y + xz with NOR gates only. (Hint: use its POS, file 01 step 10.)
6. Why does replacing every gate of an AND–OR circuit with NAND leave the function unchanged? Answer in two lines.

<!--ANSWERS-->

## Answers

**Check 1.** (a) **3**: two tied NANDs make X' and Y', a third NAND gives (X'Y')' = X + Y. (b) NAND(A, B) → inverter → AB; NAND(AB, C) → inverter → ABC: **4 gates**.

**Check 2.** (a) Two tied NORs make A' and B'; a third NOR gives (A' + B')' = AB: **3 gates**. (b) P' + Q' = (PQ)'. AND from NORs: NOR(P', Q') = PQ needs P', Q' (two tied NORs) and one NOR: 3 gates for PQ, then one tied NOR to invert: **4 gates**, F = (PQ)'.

**Check 3.** (a) NAND(b', c'), NAND(b, c), NAND(a', c') into a 3-input NAND: **4 gates**; F = ((b'c')'(bc)'(a'c')')' = b'c' + bc + a'c'. (b) NAND(x', y) and NAND(x, z) into a 2-input NAND: **3 gates** (plus a tied NAND for x').

**Check 4.** (a) A is a lone literal into the OR-level output gate, so it enters as **A'**: F = (A'·(BC)')' = A + BC. Gates: NAND(B, C), tied NAND for A', output NAND: **3**. (b) Both sums are OR-level: NAND(A', B') = A + B and NAND(C', D') = C + D; the AND-level output NAND gives F', then an inverter: **4 gates** (plus inverters for A', B', C', D' if not given).

**Check 5.** (a) **Three**: NOR(A, B), NOR(C, D), and a NOR of those two: ((A + B)' + (C + D)')' = (A + B)(C + D). (b) NOR(A, B) = (A + B)'; lone literal C enters complemented: C' = NOR(C, C); output NOR((A + B)', C') = (A + B)C: **3 gates**.

**Check 6.** (a) NAND: three 2-input NANDs + one 3-input NAND = **4 gates**. NOR: NOR(b, c') and NOR(a', b', c) + one 2-input output NOR = **3 gates**. (b) The **NOR** version: one gate fewer and 7 gate inputs (2 + 3 + 2) against 9 (2 + 2 + 2 + 3).

**Check 7.** (a) N1 = (1·1)' = **0**; N2 = (1·0)' = **1**; N3 = (1·0)' = **1**; F = (1·1)' = **0** = 1 ⊕ 1. ✓ (b) Add a NAND inverter: **5 gates**.

**Self-test.**

1. NOT: NOR with tied inputs, (X + X)' = X'. OR: NOR then a NOR inverter. AND: NOR(X', Y') = XY. NOT, AND, OR build every SOP, so NOR builds every function.
2. NAND(A, B), NAND(C, D), NAND of those two: **3 gates**.
3. NOR(A, B), NOR(C, C) = C', output NOR: **3 gates** (Check 5b).
4. A'B + A'B' = A'; A' + AB' = A' + B' = (AB)': **one NAND** of A and B.
5. POS (x + y)(x' + z): NOR(x, y), NOR(x', z), output NOR: **3 gates** (plus a tied NOR for x'); output ((x + y)' + (x' + z)')' = (x + y)(x' + z) = x'y + xz.
6. ((P)'(Q)')' = P + Q by De Morgan: the NAND output gate is an OR whose inputs arrive complemented, and the first-level NANDs supply exactly those complements P', Q'.

<!--/ANSWERS-->
