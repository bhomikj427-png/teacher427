# 01 — Boolean Algebra and K-Maps

Notation in this pack: `A'` = NOT A · `+` = OR · `·` or juxtaposition = AND · `(+)` = XOR.

---

## Map

```
   Truth table  <---->  Sigma-m (SOP)  <---->  Pi-M (POS)
                              |
                              v
                        K-map plotting
                              |
                   +----------+----------+
                   v                     v
            group the 1s            group the 0s
             -> minimal SOP          -> minimal POS
                   |
                   v
            don't-cares: use each one ONLY if it grows a group
```

---

## Attempt first

1. Write `F = A'B' + A'` in its simplest form. How many gates does it need?
2. `F(a,b,c) = Sigma-m(1,3,5)`. Write the same function as a product of maxterms.
3. In a 4-variable K-map, are cells m0 and m8 adjacent? m0 and m10?
4. A K-map has a don't-care sitting alone in a corner with no adjacent 1. What do you do with it?
5. `F(a,b,c,d) = Sigma-m(0,4,5,7,8,9,15) + d(1,3,6,14)`. Minimize it.

---

## Method

### The laws you actually use

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

**Absorption and second absorption are the two that collapse exam expressions on sight.**
`A'B' + A'` is absorption: `A'` swallows `A'B'`, leaving `A'`.

### Σm and ΠM are the same function

For n variables, indices run 0 to 2^n - 1.

- **Minterm** m_i = the AND term that is 1 only at row i. Variable **complemented where the bit is 0**.
- **Maxterm** M_i = the OR term that is 0 only at row i. Variable **complemented where the bit is 1**.

Note the inversion — this is trap T5.

```
  Sigma-m(set S)  =  Pi-M(all indices NOT in S)
```

Example, 3 variables: `Sigma-m(1,3,5)` = `Pi-M(0,2,4,6,7)`.

For a=1,b=0,c=1 (index 5): m5 = `a b' c`, M5 = `a' + b + c'`.

### K-map layout

Columns and rows are in **Gray code order** (00, 01, 11, 10) so that neighbours differ in one bit.

4-variable map, rows = `ab`, columns = `cd`:

```
          cd=00   cd=01   cd=11   cd=10
  ab=00 |  m0  |  m1  |  m3  |  m2  |
  ab=01 |  m4  |  m5  |  m7  |  m6  |
  ab=11 | m12  | m13  | m15  | m14  |
  ab=10 |  m8  |  m9  | m11  | m10  |
```

**The map wraps.** Left edge touches right edge, top touches bottom. So m0-m2, m0-m8, and the four
corners m0/m2/m8/m10 are all valid groups. That is trap T4.

### Grouping rules

1. Groups are **powers of 2**: 1, 2, 4, 8, 16.
2. Groups are **rectangles** in the wrapped map — never diagonal, never L-shaped.
3. **Make every group as large as legally possible.** A group of 8 has 1 literal fewer than a group
   of 4 covering the same cells.
4. Groups may overlap. Overlap is free; an extra *term* is not.
5. Cover every 1 at least once. Stop the moment all 1s are covered.
6. Drop any group whose 1s are all covered by other groups — it is redundant. **Check this at the
   end**; it is the difference between a legal answer and a minimal one.

Group size to literal count, 4-variable map:

| Group size | Literals in the term |
|---|---|
| 1 | 4 |
| 2 | 3 |
| 4 | 2 |
| 8 | 1 |

### Don't-cares

A don't-care `d` (or `X`) is an input combination that cannot occur or whose output is never used.

**Rule: include a don't-care in a group only when doing so makes the group bigger. Never form a
group out of don't-cares alone.**

An unused don't-care is simply left as 0. It costs nothing. A don't-care treated as 0 *when it could
have enlarged a group* costs you the mark — trap T1.

### Minimal POS

Same map, group the **0s** instead of the 1s. That gives you `F'` in SOP form. Apply De Morgan to
get `F` in POS form. Don't-cares can be used here too.

### Five-variable maps

Two 4-variable maps side by side: one for `v = 0` (indices 0-15), one for `v = 1` (16-31).
Cells in the **same position** on both maps are adjacent — a group spanning both maps drops the `v`
literal entirely.

---

## Worked — MTE 2025 Q1 (2 marks)

> Optimize `F = P'Q' + P'` and implement using 2-input NOR gates.

**Minimize.** Absorption: `P'` absorbs `P'Q'`.

```
  F = P'Q' + P'
    = P'(Q' + 1)
    = P'(1)
    = P'
```

**Realize.** A 2-input NOR with both inputs tied together is an inverter:

```
  NOR(P, P) = (P + P)' = P'
```

```
        P ---+
             |>NOR>--- F = P'
        P ---+
```

**One 2-input NOR gate.** The whole question is: spot the absorption, then remember the
tied-input NOR inverter.

---

## Worked — MTE 2025 Q4 (4 marks)

> Minimize `F(a,b,c,d) = Sigma-m(0,4,5,7,8,9,15) + d(1,3,6,14)` using a K-map. Draw the logic
> circuit using basic gates.

**Plot.** 1 = minterm, X = don't-care, 0 = everything else.

```
          cd=00   cd=01   cd=11   cd=10
  ab=00 |   1  |   X  |   X  |   0  |
  ab=01 |   1  |   1  |   1  |   X  |
  ab=11 |   0  |   0  |   1  |   X  |
  ab=10 |   1  |   1  |   0  |   0  |
```

**Group.**

- `b'c'` — cells m0, m1(X), m8, m9. Column cd=00 and cd=01 in rows ab=00 and ab=10. Size 4.
- `bc` — cells m6(X), m7, m14(X), m15. Size 4.
- `a'b` — cells m4, m5, m7, m6(X). Size 4.
- `a'c'` — cells m0, m1(X), m4, m5. Size 4.

**Test for essential groups.**

- m15 is covered by `bc` alone -> **essential**.
- m8 and m9 are covered by `b'c'` alone -> **essential**.
- m0 falls inside `b'c'` already. m7 falls inside `bc` already.
- Left uncovered: **m4 and m5**. Either `a'b` or `a'c'` takes them, both 2 literals.

**Result.**

```
  F = b'c' + bc + a'b          (or equally minimal:  b'c' + bc + a'c')
```

Note `b'c' + bc` is XNOR(b, c) — worth recognising, but write it as two AND terms in the circuit
unless the question asks for XOR gates.

**Circuit** (basic gates, using the `a'b` form):

```
  b --+--[NOT]--b'--+
      |             +--[AND]--- b'c'  ---+
  c --+--[NOT]--c'--+                    |
      |                                  +--[OR]--- F
      +-------------+--[AND]--- bc   ----+
  b ----------------+                    |
  c ----------------+                    |
                                         |
  a --[NOT]--a'--+                       |
                 +--[AND]--- a'b --------+
  b -------------+
```

**Check your answer before moving on.** Substitute two or three of the original minterms and one
non-minterm. m8 = 1000: `b'c' = 1·1 = 1` -> F = 1, correct. m12 = 1100: `b'c' = 0`, `bc = 0`,
`a'b = 0·1 = 0` -> F = 0, and 12 was not a minterm, correct.

---

## Traps

**T1 — don't-care read as 0.** In the worked question, m6 and m14 are what let `bc` be a group of 4
instead of a lone pair. Read them as 0 and your answer grows two literals.

**T2 — non-maximal grouping.** Always ask "can this group double?" before writing the term. Check
wrap-around in both directions.

**T4 — missed wrap.** The four corners m0, m2, m8, m10 form a legal group of 4 (`b'd'` in the
ab/cd layout). It looks wrong on paper and is right.

**T5 — ΠM read as Σm.** `Pi-M(0,3,5,6,7)` over 3 variables means the function is **0** at 0,3,5,6,7
and **1** at 1,2,4. Convert to `Sigma-m(1,2,4)` first, then plot.

**T3 — no circuit drawn.** "Also draw the logic circuit" is worth marks on its own. A minimized
expression with no diagram loses them.

---

## Self-test

1. Simplify `F = AB + A'C + BC` and name the law.
2. `F(a,b,c) = Pi-M(0,3,5,6,7)`. Convert to Σm form and minimize.
3. Minimize `F(w,x,y,z) = Sigma-m(0,1,3,5,7,10,11) + d(2,6,13)`.
4. Minimize `F(A,B,C,D) = Sigma-m(0,2,8,10)`. How many literals?
5. `F(a,b,c,d) = Sigma-m(0,4,5,7,8,9,15) + d(1,3,6,14)` — give the **other** minimal form, the one
   not used in the worked solution above, and confirm it has the same cost.
6. Five-variable: minimize `F(v,w,x,y,z) = Sigma-m(0,2,5,8,10,13,15,17,19,21,26,28,29,30,31) +
   d(7,12,14,23,24)`.

---
---
---

## Answers

**1.** Consensus law. `AB + A'C + BC = AB + A'C`. The `BC` term is implied by the other two: wherever
BC = 1, either A = 1 (so AB = 1) or A = 0 (so A'C = 1).

**2.** `Pi-M(0,3,5,6,7)` = `Sigma-m(1,2,4)`.

```
          bc=00   bc=01   bc=11   bc=10
   a=0  |   0  |   1  |   0  |   1  |
   a=1  |   1  |   0  |   0  |   0  |
```

No two 1s are adjacent — m1(001), m2(010), m4(100) each differ from the others in two bits.
No grouping is possible.

```
  F = a'b'c + a'bc' + ab'c'
```

**3.** Plot with rows `wx`, columns `yz`:

```
          yz=00   yz=01   yz=11   yz=10
  wx=00 |   1  |   1  |   1  |   X  |
  wx=01 |   0  |   1  |   1  |   X  |
  wx=11 |   0  |   X  |   0  |   0  |
  wx=10 |   0  |   0  |   1  |   1  |
```

Groups: `w'x'` (m0, m1, m3, m2X) · `w'z` (m1, m3, m5, m7) · `x'y` (m2X, m3, m10, m11).

- m0 -> only `w'x'` — essential.
- m5 -> only `w'z` — essential.
- m10, m11 -> only `x'y` — essential.

```
  F = w'x' + w'z + x'y
```

(`w'y`, covering m2X/m3/m6X/m7, is a legal group but every one of its 1s is already covered — drop it.)

**4.** m0 = 0000, m2 = 0010, m8 = 1000, m10 = 1010. Common: `B = 0`, `D = 0`.

```
  F = B'D'        2 literals
```

This is the four-corners group — it wraps both ways.

**5.** `F = b'c' + bc + a'c'`.

Cost check: three terms, two literals each, six literals — identical to `b'c' + bc + a'b`.
Both are minimal; either earns full marks. `a'c'` covers m0, m1(X), m4, m5; `a'b` covers m4, m5,
m7, m6(X). The uncovered cells after the two essential groups were m4 and m5, and both candidates
contain them.

**6.** Split into `v = 0` (m0-m15) and `v = 1` (m16-m31).

```
  v = 0                             v = 1
          yz=00  01   11   10               yz=00  01   11   10
  wx=00 |  1  |  0  |  0  |  1  |   wx=00 |  0  |  1  |  1  |  0  |
  wx=01 |  0  |  1  |  X  |  0  |   wx=01 |  0  |  1  |  X  |  0  |
  wx=11 |  X  |  1  |  1  |  X  |   wx=11 |  1  |  1  |  1  |  1  |
  wx=10 |  1  |  0  |  0  |  1  |   wx=10 |  X  |  0  |  0  |  1  |
```

Groups spanning both maps drop `v`:

- `x z` — m5, m7X, m13, m15, m21, m23X, m29, m31. Size 8.
- `w z'` — m8, m10, m12X, m14X, m24X, m26, m28, m30. Size 8.

Groups on one map only keep `v`:

- `v' x' z'` — m0, m2, m8, m10. Size 4.
- `v w' z` — m17, m19, m21, m23X. Size 4.

Essential check: m0 and m2 sit only in `v'x'z'`. m17 and m19 sit only in `vw'z`. m26 sits only in
`wz'`. m5 sits only in `xz`. All four essential.

`w x` (m12X, m13, m14X, m15, m28, m29, m30, m31) is also a legal group of 8, but every one of its
1s is already covered — **drop it**. That redundancy check is the whole difficulty of this question.

```
  F = x z  +  w z'  +  v w' z  +  v' x' z'
```

Four terms, ten literals. File `02` realizes this one in NAND gates.
