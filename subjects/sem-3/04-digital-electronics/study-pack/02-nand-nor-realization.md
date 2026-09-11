# 02 — NAND / NOR Realization (the house style)

The professor's questions almost never stop at a minimized expression. They say **"implement using
2-input NOR"**, **"realize using NAND gates only"**, **"using universal gate"**. This file is that
second half.

---

## Map

```
   minimal SOP  --(De Morgan twice)-->  all-NAND, 2 levels
        |
        |  complement route
        v
   minimal POS  --(De Morgan twice)-->  all-NOR, 2 levels

   plus:  inverter from a tied-input NAND or NOR
   plus:  fan-in limit -- "2-input only" forces a tree
```

---

## Attempt first

1. Build NOT, AND, and OR using only 2-input NAND gates. How many NANDs for each?
2. `F = AB + CD`. Draw it in NAND-only form. How many gates, how many levels?
3. Why is a **minimal SOP** the right starting point for NAND-only, but the wrong one for NOR-only?
4. You have `F = A + B + C + D` and only 2-input NOR gates. How many gates?
5. Realize `F = w'x' + w'z + x'y` with NAND gates only.

---

## Method

### Why NAND and NOR are "universal"

Each alone can build NOT, AND and OR, so it can build any Boolean function.

**From NAND:**

```
  NOT A      = NAND(A, A)
  AND(A,B)   = NAND( NAND(A,B), NAND(A,B) )        2 gates
  OR(A,B)    = NAND( NAND(A,A), NAND(B,B) )        3 gates
```

**From NOR:**

```
  NOT A      = NOR(A, A)
  OR(A,B)    = NOR( NOR(A,B), NOR(A,B) )           2 gates
  AND(A,B)   = NOR( NOR(A,A), NOR(B,B) )           3 gates
```

Note the symmetry: NAND is cheap at AND, expensive at OR. NOR is the reverse. **That is why SOP
pairs with NAND and POS pairs with NOR.**

### The two-level conversion — the only trick you need

**SOP to NAND.** Start from minimal SOP. Double-negate the whole expression and push one negation
in with De Morgan:

```
  F = AB + CD
    = ( (AB + CD)' )'                  double negation
    = ( (AB)' · (CD)' )'               De Morgan
    = NAND( NAND(A,B), NAND(C,D) )
```

**Every AND becomes a NAND. Every OR becomes a NAND. The structure does not change at all.**
Level 1 = one NAND per product term. Level 2 = one NAND collecting them.

```
   A ---+
        |NAND|---+
   B ---+        |
                 |NAND|--- F
   C ---+        |
        |NAND|---+
   D ---+
```

**POS to NOR.** Same move, mirrored:

```
  F = (A + B)(C + D)
    = ( ((A+B)(C+D))' )'
    = ( (A+B)' + (C+D)' )'
    = NOR( NOR(A,B), NOR(C,D) )
```

**Every OR becomes a NOR. Every AND becomes a NOR.**

### The rule of thumb

| Asked for | Start from | Then |
|---|---|---|
| NAND only | minimal **SOP** (group the 1s) | swap every gate for NAND |
| NOR only | minimal **POS** (group the 0s, De Morgan) | swap every gate for NOR |

Doing NAND-from-POS or NOR-from-SOP is possible but adds an inverter level. Get the starting form
right and the conversion is free.

### Complemented literals

A term like `w'x'` needs `w'` and `x'` first. Each costs one gate:

```
  w' = NAND(w, w)        or        w' = NOR(w, w)
```

Count these. A question asking "how many gates" expects the inverters included unless it says
complemented inputs are available.

### The 2-input constraint

"Using 2-input NOR gates" or "2-input NAND" limits **fan-in**. A 4-input function becomes a tree:

```
  A + B + C + D   with 2-input gates:

  OR(A,B) --+
            +-- OR( , ) --- F
  OR(C,D) --+
```

Each of those ORs is itself 3 NORs, so count carefully. Tree depth grows as log₂ of the number of
inputs — two levels of ORing for 4 inputs, three for 8.

### Bubble pushing (the fast way to read a diagram)

A bubble is an inversion. Two bubbles on the same wire cancel.

```
  AND with bubbled output   =  NAND
  OR  with bubbled inputs   =  NAND        (De Morgan, same gate)
  OR  with bubbled output   =  NOR
  AND with bubbled inputs   =  NOR
```

So a NAND drawn as "OR with inverted inputs" and a NAND drawn as "AND with inverted output" are the
**same gate**. When checking a given circuit, push bubbles along wires until they cancel in pairs —
what remains is the real function.

---

## Worked — MTE 2025 Q1 revisited

> `F = P'Q' + P'`, implement using 2-input NOR.

Minimized (file 01): `F = P'`.

Do **not** build an AND-OR structure and convert it — minimize first, and the structure vanishes:

```
  F = P' = NOR(P, P)
```

One gate. The marks here are for minimizing *before* realizing. A student who converts
`P'Q' + P'` gate-for-gate produces five or six NORs for a function that needs one.

---

## Worked — NAND realization of `F = w'x' + w'z + x'y`

(the self-test answer from file 01)

**Step 1 — inverters.** Need `w'` and `x'`.

```
  w' = NAND(w, w)
  x' = NAND(x, x)
```

**Step 2 — level 1, one NAND per product term.**

```
  N1 = NAND(w', x')
  N2 = NAND(w', z)
  N3 = NAND(x', y)
```

**Step 3 — level 2, collect.**

```
  F = NAND(N1, N2, N3)
```

**Total: 6 NAND gates** (2 inverters + 3 product + 1 collector), assuming a 3-input NAND is allowed.

If restricted to **2-input** NANDs, the collector becomes a tree, and here the bubble bookkeeping
matters: `NAND(N1,N2)` is not a partial OR. Convert properly —

```
  OR(a, b) with NANDs = NAND( NAND(a,a), NAND(b,b) )
```

so build `F = (N1' + N2' + N3')` as an OR tree of the inverted N's. Simplest correct route with
2-input gates: form `T = OR(N1', N2')` and then `F = OR(T, N3')`, each OR being 3 NANDs — or note
that `N1' = w'x'` directly, and just re-derive. **When a question restricts fan-in, state your gate
count and show the tree; do not hand-wave a 3-input gate.**

---

## Worked — NAND realization of the 5-variable result

`F = xz + wz' + vw'z + v'x'z'` (file 01, self-test 6)

**Inverters needed:** `v'`, `w'`, `x'`, `z'` -> 4 NANDs.

**Level 1 — one NAND per term:**

```
  N1 = NAND(x, z)
  N2 = NAND(w, z')
  N3 = NAND(v, w', z)          3-input
  N4 = NAND(v', x', z')        3-input
```

**Level 2:**

```
  F = NAND(N1, N2, N3, N4)     4-input
```

**Total: 9 NAND gates**, using gates up to 4 inputs. State the fan-in you assumed — examiners accept
it when it is stated and penalise it when it is silently exceeded.

---

## Traps

**Minimize before converting.** The conversion is mechanical; the minimization is where the marks
are. Converting an unminimized expression is the single most common way to get a bloated, wrong-cost
answer.

**Count the inverters.** `F = w'x' + w'z + x'y` looks like 4 gates and is 6.

**Wrong starting form.** NOR-only from an SOP expression works but costs an extra inversion level.
If the question says NOR, minimize by grouping the **0s**.

**"2-input" is a real constraint.** Silently drawing a 4-input NAND when the question said 2-input
loses marks even though the logic is right.

**Do not stop at the expression.** These questions say *implement* / *realize*. Draw the gates.

---

## Self-test

1. Convert `F = AB + A'C` to NAND-only. Count the gates.
2. Convert `F = (A + B)(A' + C)` to NOR-only. Count the gates.
3. Minimize `F(w,x,y,z) = Σm(0,1,3,5,7,10,11) + d(2,6,13)` and realize using NAND only.
4. How many 2-input NOR gates to build `F = ABCD`?
5. Minimize `F(v,w,x,y,z) = Σm(0,2,5,8,10,13,15,17,19,21,26,28,29,30,31) + d(7,12,14,23,24)`
   and implement using a universal gate.
6. A gate is drawn as an **OR symbol with both inputs bubbled**. Which standard gate is it?
   And if its output feeds *both* inputs of a second identical gate, what is the overall function?

---
---
---

## Answers

**1.** `F = AB + A'C`.

```
  A'  = NAND(A, A)                         1
  N1  = NAND(A, B)                         2
  N2  = NAND(A', C)                        3
  F   = NAND(N1, N2)                       4
```

**4 NAND gates.**

**2.** `F = (A + B)(A' + C)`. Already POS, so NOR is the natural target.

```
  A'  = NOR(A, A)                          1
  N1  = NOR(A, B)                          2
  N2  = NOR(A', C)                         3
  F   = NOR(N1, N2)                        4
```

**4 NOR gates.**

**3.** Minimal SOP from file 01: `F = w'x' + w'z + x'y`.

```
  w' = NAND(w, w)
  x' = NAND(x, x)
  N1 = NAND(w', x')
  N2 = NAND(w', z)
  N3 = NAND(x', y)
  F  = NAND(N1, N2, N3)
```

**6 NAND gates.**

**4.** `F = ABCD` with 2-input NOR.

`AND(A,B) = NOR( NOR(A,A), NOR(B,B) )` = 3 gates. So:

```
  AND(A,B)          3 gates
  AND(C,D)          3 gates
  AND of those two  3 gates
```

**9 NOR gates.** NOR is expensive at AND — this is the asymmetry in action.

**5.** From file 01: `F = xz + wz' + vw'z + v'x'z'`.

NAND realization, 9 gates:

```
  v' = NAND(v,v)   w' = NAND(w,w)   x' = NAND(x,x)   z' = NAND(z,z)

  N1 = NAND(x, z)
  N2 = NAND(w, z')
  N3 = NAND(v, w', z)
  N4 = NAND(v', x', z')

  F  = NAND(N1, N2, N3, N4)
```

State the assumed fan-in (up to 4 inputs). If restricted to 2-input gates, expand each multi-input
NAND into a tree and recount.

**6.** An OR symbol with both inputs bubbled is `A' + B'`, which by De Morgan is `(AB)'` —
a **NAND**. The two drawings are the same gate; which one an engineer uses is a readability choice,
not a different device.

Feeding that output into both inputs of a second NAND:

```
  NAND( NAND(A,B), NAND(A,B) )  =  ( (AB)' )'  =  AB
```

The second gate acts as an inverter, so the pair is an **AND**. That is the bubble-cancelling rule:
two inversions on one path cancel. Count inversions along each path — even cancels, odd leaves one
NOT.
