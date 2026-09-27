# Boolean algebra & K-maps

<div class="sub">Chapter 1 of 9 · MTE weight: very high · feeds every other chapter</div>

[[map:Laws > Σm / ΠM > K-map layout > Grouping > Don't-cares > POS|here=0]]

:::q Attempt first — write something down before scrolling
1. Simplify `F = A'B' + A'`. How many gates does it need?
2. `F(a,b,c) = Σm(1,3,5)`. Write it as a product of maxterms.
3. In a 4-variable K-map, are m0 and m8 adjacent? m0 and m10?
4. A don't-care sits alone in a corner, no 1 next to it. What do you do with it?
5. Minimize `F(a,b,c,d) = Σm(0,4,5,7,8,9,15) + d(1,3,6,14)`.
:::

A wrong attempt that you then correct sticks harder than a right answer you only read.

## Two laws do most of the work

[[fig:venn_absorption|**Absorption:** AB sits inside A, so adding it changes nothing. A + AB = A.|w=90]]

[[fig:venn_absorption2|**Second absorption:** the part of B outside A, added to A, fills out all of A and B. A + A'B = A + B.|w=90]]

`A'B' + A'` is absorption on sight: `A'` swallows `A'B'`, leaving `A'`.

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

## Σm and ΠM: one function, two lists

[[fig:strip_sm_pm|Same truth table, read twice. Σm names the 1-rows; ΠM names the 0-rows. Together they list every row exactly once.|w=100]]

- **Minterm** mᵢ: AND term, 1 only at row i. Complement a variable where its **bit is 0**. m5 = `ab'c`.
- **Maxterm** Mᵢ: OR term, 0 only at row i. Complement a variable where its **bit is 1**. M5 = `a' + b + c'`.

:::trap T5 · ΠM read as Σm
`ΠM(0,3,5,6,7)` means F is **0** at those rows. Convert to `Σm(1,2,4)` first, then plot.
:::

## The K-map: a truth table folded so neighbours touch

[[fig:kmap_layout|Rows and columns run in Gray code (00, 01, 11, 10), so any two touching cells differ in one bit. m0 has four neighbours, and two of them are across the edge.|w=70]]

**The map wraps.** Left edge touches right edge; top touches bottom. So m0 and m8 **are** adjacent, and so are the four corners m0, m2, m8, m10.

## Bigger group, fewer letters

[[fig:group_sizes|Each time a group doubles, the variable that changes inside it drops out.|w=100]]

## What counts as a group

[[fig:legal_illegal|Top: illegal. Bottom: legal, including the ones that look wrong on paper.|w=100]]

1. Size is a **power of 2**, and the shape is a **rectangle** on the wrapped map.
2. Make every group **as large as it can legally be**.
3. Overlap is free; an extra term is not.
4. Cover every 1, then **delete any group whose 1s are all covered by others**.

## Don't-cares: use them only to grow a group

[[fig:dontcare_effect|The same two 1s. Reading the X cells as 1 turns a pair into a quad and saves a letter.|w=80]]

Never make a group out of X cells alone. An X you don't need just stays 0 and costs nothing.

## Minimal POS: group the 0s

[[fig:pos_example|F = Σm(0,1,2,3,7). Group the 0s to get F' = ab' + ac', then apply De Morgan to each term.|w=60]]

$$F = (a' + b)(a' + c)$$

## Five variables: two maps, stacked

The v = 0 map (m0–m15) sits beside the v = 1 map (m16–m31). **Cells in the same position on both maps are adjacent.** A group that spans both maps drops v. Self-test 6 below shows it drawn.

## Worked · MTE 2025 Q1 (2 marks)

:::q
Optimize `F = P'Q' + P'` and implement using 2-input NOR gates.
:::

Absorption: `P'` swallows `P'Q'`, so **F = P'**. A NOR with both inputs tied is an inverter:

[[fig:nor_inverter|NOR(P, P) = (P + P)' = P'. One gate.|w=55]]

## Worked · MTE 2025 Q4 (4 marks)

:::q
Minimize `F(a,b,c,d) = Σm(0,4,5,7,8,9,15) + d(1,3,6,14)` using a K-map. Draw the logic circuit using basic gates.
:::

**Step through the grouping.** Press ▶ to add one group at a time.

[[fig:q4_steps|Small numbers are minterm indices. Essential groups first: only b'c' covers m8 and m9, only bc covers m15. Then m4 and m5 are left, and a'b takes both.|w=70|steps=3]]

$$F = b'c' + bc + a'b$$

The circuit carries marks of its own (trap T3). Bubbles on a gate input are the NOT gates:

[[fig:q4_circuit|Three 2-input ANDs into a 3-input OR.|w=70]]

:::check Check before moving on
m8 = 1000: b'c' = 1, so F = 1 ✓ (a minterm). m12 = 1100: every term is 0, so F = 0 ✓ (not a minterm).
:::

## Traps

| # | Trap | Picture to remember |
|---|---|---|
| T1 | Don't-care read as 0 | The pair that should have been a quad |
| T2 | Group not maximal | Always ask "can this double?" |
| T3 | No circuit drawn | "Also draw the circuit" carries its own marks |
| T4 | Missed wrap-around | The four corners are one group |
| T5 | ΠM read as Σm | ΠM lists the **0** rows |

## Self-test

Try each one on paper first. Then open its answer.

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
