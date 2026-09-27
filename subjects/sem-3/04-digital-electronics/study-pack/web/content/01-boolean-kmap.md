@@ warm-up | Warm-up: try these cold | practice | Five questions before any teaching. Guess if you must.

Write an answer on paper for each, even a guess. A wrong attempt that you then correct sticks harder than a right answer you only read.

:::q Attempt first
1. Simplify `F = A'B' + A'`. How many gates does it need?
2. `F(a,b,c) = Σm(1,3,5)`. Write it as a product of maxterms.
3. In a 4-variable K-map, are m0 and m8 adjacent? m0 and m10?
4. A don't-care sits alone in a corner, no 1 next to it. What do you do with it?
5. Minimize `F(a,b,c,d) = Σm(0,4,5,7,8,9,15) + d(1,3,6,14)`.
:::

Keep your answers. The concepts on this map settle each one, and the worked MTE question (★) is question 5.

@@ laws | Two laws do most of the work | idea | Absorption and second absorption collapse exam expressions on sight.

[[fig:venn_absorption|**Absorption:** AB sits inside A, so adding it changes nothing. A + AB = A.|w=90]]

[[fig:venn_absorption2|**Second absorption:** the part of B outside A, added to A, fills out all of A and B. A + A'B = A + B.|w=90]]

[[fig:demorgan_gates|**De Morgan, drawn:** a NOR is an AND with both inputs inverted. (A + B)' = A'B'.|w=80]]

:::reveal All eight laws (reference table)
| Law | Form |
|---|---|
| Identity | `A + 0 = A` · `A · 1 = A` |
| Null | `A + 1 = 1` · `A · 0 = 0` |
| Idempotent | `A + A = A` · `A · A = A` |
| Complement | `A + A' = 1` · `A · A' = 0` |
| Absorption | `A + AB = A` · `A(A + B) = A` |
| Second absorption | `A + A'B = A + B` · `A(A' + B) = AB` |
| Consensus | `AB + A'C + BC = AB + A'C` |
| De Morgan | `(A + B)' = A'B'` · `(AB)' = A' + B'` |
:::

:::reveal Quick check: simplify A'B' + A'
Absorption. `A'` swallows `A'B'`, leaving **A'**: one NOT gate.
:::

@@ sm-pm | Σm and ΠM: one function, two lists | idea | Σm lists the rows where F = 1; ΠM lists the rows where F = 0.

[[fig:strip_sm_pm|Same truth table, read twice. Together the two lists name every row exactly once.|w=100]]

| | Minterm mᵢ | Maxterm Mᵢ |
|---|---|---|
| Gate | AND | OR |
| True/false at row i only | **1** only at row i | **0** only at row i |
| Complement a variable when its bit is | **0** | **1** |
| Row 5 (abc = 101) | `ab'c` | `a' + b + c'` |

:::trap T5 · ΠM read as Σm
`ΠM(0,3,5,6,7)` means F is **0** at those rows. Convert to `Σm(1,2,4)` first, then plot.
:::

:::reveal Quick check: Σm(1,3,5) as maxterms
**ΠM(0,2,4,6,7)**: every row not in the Σm list.
:::

@@ kmap-layout | The K-map: a folded truth table | idea | Gray-code order makes neighbours differ in one bit, and the edges wrap.

[[fig:kmap_layout|Rows and columns run 00, 01, 11, 10. m0 has four neighbours; two of them are across the edge.|w=70]]

**The map wraps.** Left edge touches right edge, top touches bottom. So the four corners m0, m2, m8, m10 are neighbours too.

:::reveal Quick check: are m0 and m8 adjacent? m0 and m10?
**m0–m8: yes** (top and bottom rows wrap). **m0–m10: no.** They differ in two bits (0000 vs 1010). They only join as part of the four-corner group.
:::

@@ group-size | Bigger group, fewer letters | method | Each doubling of a group deletes one variable.

[[fig:group_sizes|Each time a group doubles, the variable that changes inside it drops out.|w=100]]

On a 4-variable map: **1 cell → 4 letters, 2 → 3, 4 → 2, 8 → 1.**

@@ group-rules | What counts as a group | method | Power-of-2 rectangles on the wrapped map, as big as possible.

[[fig:legal_illegal|Top: illegal. Bottom: legal, including the ones that look wrong on paper.|w=100]]

1. Size is a **power of 2**, and the shape is a **rectangle** on the wrapped map.
2. Make every group **as large as it can legally be**.
3. Overlap is free; an extra term is not.
4. Cover every 1, then **delete any group whose 1s are all covered by others**.

@@ dont-cares | Don't-cares: jokers | method | Use an X only when it makes a group bigger. Otherwise it's 0.

[[fig:dontcare_effect|The same two 1s. Reading the X cells as 1 turns a pair into a quad and saves a letter.|w=80]]

Never make a group out of X cells alone. An X you don't need just stays 0 and costs nothing.

:::reveal Quick check: an X alone in a corner, no 1 beside it?
**Leave it as 0.** It can't grow any group, and a group made only of X cells adds a term for nothing.
:::

@@ pos | Minimal POS: group the 0s | method | Group the 0s to get F', then De Morgan each term.

[[fig:pos_example|F = Σm(0,1,2,3,7). The 0s group into F' = ab' + ac'.|w=60]]

$$F' = ab' + ac'   ⟹   F = (a' + b)(a' + c)$$

Don't-cares work here too, now as honorary 0s.

@@ five-var | Five variables: two maps | method | Same cell on both maps = adjacent. A group across both drops v.

[[fig:five_var_demo|m5, m7 on the v = 0 map and m21, m23 in the same cells on the v = 1 map form one group of 4. v changes inside it, so v drops: w'xz.|w=100]]

A group that stays on one map **keeps** v (v' on the left map, v on the right).

@@ q1 | MTE 2025 Q1 · 2 marks | exam | Absorption, then a NOR with its inputs tied.

:::q
Optimize `F = P'Q' + P'` and implement using 2-input NOR gates.
:::

**Minimize.** Absorption: `P'` swallows `P'Q'`, so **F = P'**.

**Realize.** Tie both inputs of a NOR together and it becomes an inverter:

[[fig:nor_inverter|NOR(P, P) = (P + P)' = P'. One gate.|w=55]]

@@ q4 | MTE 2025 Q4 · 4 marks | exam | Plot, find the essential groups, cover what's left, draw the circuit.

:::q
Minimize `F(a,b,c,d) = Σm(0,4,5,7,8,9,15) + d(1,3,6,14)` using a K-map. Draw the logic circuit using basic gates.
:::

**Try the grouping yourself first. Then press ▶ to add one group at a time.**

[[fig:q4_steps|Small numbers are minterm indices. Essential groups first: only b'c' covers m8 and m9, only bc covers m15. m4 and m5 are left, and a'b takes both.|w=70|steps=3]]

$$F = b'c' + bc + a'b$$

[[fig:q4_circuit|The circuit carries its own marks (trap T3). Bubbles on a gate input are the NOT gates.|w=70]]

:::check Check before moving on
m8 = 1000: b'c' = 1, so F = 1 ✓ (a minterm). m12 = 1100: every term is 0, so F = 0 ✓ (not a minterm).
:::

@@ traps | The five traps | trap | Where K-map marks are actually lost.

| # | Trap | Picture to remember |
|---|---|---|
| T1 | Don't-care read as 0 | The pair that should have been a quad |
| T2 | Group not maximal | Always ask "can this double?" |
| T3 | No circuit drawn | "Also draw the circuit" carries its own marks |
| T4 | Missed wrap-around | The four corners are one group |
| T5 | ΠM read as Σm | ΠM lists the **0** rows |

@@ self-test | Self-test | practice | Six questions. Paper first, then open each answer.

**1.** Simplify `F = AB + A'C + BC` and name the law.

:::reveal Answer 1
**Consensus.** `AB + A'C + BC = AB + A'C`. Wherever BC = 1, either A = 1 (so AB = 1) or A = 0 (so A'C = 1), so BC adds nothing.
:::

**2.** `F(a,b,c) = ΠM(0,3,5,6,7)`. Convert to Σm and minimize.

:::reveal Answer 2
ΠM(0,3,5,6,7) = **Σm(1,2,4)**.

[[fig:ans2|No two 1s touch. Each pair differs in two bits.|w=45]]

No grouping is possible: **F = a'b'c + a'bc' + ab'c'**.
:::

**3.** Minimize `F(w,x,y,z) = Σm(0,1,3,5,7,10,11) + d(2,6,13)`.

:::reveal Answer 3
[[fig:ans3|m0 is only in w'x', m5 only in w'z, m10 and m11 only in x'y, so all three are essential. w'y is a legal group, but all its 1s are already covered, so drop it.|w=60]]

**F = w'x' + w'z + x'y**
:::

**4.** Minimize `F(A,B,C,D) = Σm(0,2,8,10)`. How many letters?

:::reveal Answer 4
[[fig:ans4|The four corners, wrapping both ways.|w=55]]

**F = B'D'**, 2 letters.
:::

**5.** For the Q4 function, give the **other** minimal form and confirm it costs the same.

:::reveal Answer 5
[[fig:q4_alt|a'c' takes m4 and m5 instead of a'b.|w=60]]

**F = b'c' + bc + a'c'**: three terms, six letters, the same cost. Either earns full marks.
:::

**6.** Five variables: minimize `F(v,w,x,y,z) = Σm(0,2,5,8,10,13,15,17,19,21,26,28,29,30,31) + d(7,12,14,23,24)`.

:::reveal Answer 6
[[fig:ans6|xz and wz' span both maps, so they drop v. vw'z and v'x'z' live on one map, so they keep it.|w=100]]

All four groups are essential (m5, m26, m17/m19 and m0/m2 each sit in only one). wx is a legal group of 8, but its 1s are already covered, so **drop it**.

**F = xz + wz' + vw'z + v'x'z'**: four terms, ten letters.
:::
