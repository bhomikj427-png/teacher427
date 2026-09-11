# 06 — Comparator, Barrel Shifter, ALU

Medium weight. These are deck-supported and did not appear on the 2025 MTE, but they sit squarely
in the MSI-devices unit and the question forms are short. Work this file after 01-05.

---

## Map

```
   MAGNITUDE COMPARATOR: A vs B -> three outputs (A<B, A=B, A>B)
        |
        +--> 1-bit -> 2-bit -> 4-bit (the cascading pattern is the point)

   SHIFTER: move bits sideways
        |
        +--> logical (fill 0)  ·  arithmetic (keep sign)  ·  circular (wrap)
        +--> barrel shifter = MUX stages, shifts any amount in one pass

   ALU: arithmetic + logic in one block, a select word picks the operation
```

---

## Attempt first

1. Write the three outputs of a 1-bit magnitude comparator.
2. What single gate tells you two bits are equal?
3. For a 4-bit comparator, `A = 0101` and `B = 0100`. Which output is high, and which bit position
   decided it?
4. `110110` logically shifted right by 1. Then the same word arithmetically shifted right by 1.
   Do they differ, and why?
5. An 8-bit barrel shifter shifts by 0 to 7 places. How many MUX stages, and how many select lines?

---

## Method

### 1-bit magnitude comparator

| A | B | L (A<B) | E (A=B) | G (A>B) |
|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 | 0 |

```
  L = A'·B
  E = A ⊕ B  complemented  =  XNOR(A, B)  =  A·B + A'·B'
  G = A·B'
```

**Exactly one of the three is high at any time**, and `L + E + G = 1` always.

### The equality building block

`XNOR` is the equality detector. For an n-bit comparison define

```
  x_i = XNOR(A_i, B_i)     = 1 when bit i of A and B match
```

Then

```
  (A = B) = x_(n-1) · ... · x_1 · x_0        all bits match
```

### 4-bit magnitude comparator

Equality is the easy one:

```
  (A = B) = x3 · x2 · x1 · x0
```

Greater-than works **from the MSB down**: A is greater if its MSB wins, or the MSBs match and the
next bit wins, and so on.

```
  (A > B) = A3·B3'
          + x3·A2·B2'
          + x3·x2·A1·B1'
          + x3·x2·x1·A0·B0'
```

```
  (A < B) = A3'·B3
          + x3·A2'·B2
          + x3·x2·A1'·B1
          + x3·x2·x1·A0'·B0
```

**Read the structure, do not memorise the letters:** each term says "all higher bits equal, and at
this bit A beats B." The third output can always be found as
`(A < B) = ( (A > B) + (A = B) )'` — one NOR instead of a second four-term network.

### Shift operations

For a word `110110`:

| Shift type | Right by 1 | What fills the vacated bit |
|---|---|---|
| **Logical** | `011011` | always `0` |
| **Arithmetic** | `111011` | a copy of the **sign bit** (MSB) |
| **Circular** (rotate) | `011011` | the bit that fell off the other end |

Left shifts:

| Shift type | Left by 1 | Fill |
|---|---|---|
| Logical | `101100` | `0` |
| Arithmetic | `101100` | `0` (same as logical on the left) |
| Circular | `101101` | the bit shifted out of the MSB |

**Why arithmetic shift exists:** for a 2's-complement number, right-shifting by 1 divides by 2. If
you shift a 0 into the sign position, a negative number becomes positive — arithmetic shift
replicates the sign bit to keep the value correct.

### Barrel shifter

A combinational shifter that shifts by **any amount in one operation**, no clock, no repeated
single-bit shifts.

Built as **log₂(n) stages of 2:1 MUXes**, each stage shifting by a power of two:

```
  8-bit barrel shifter, shift amount S2 S1 S0

  stage 1:  shift by 4 if S2 = 1     (8 MUXes)
  stage 2:  shift by 2 if S1 = 1     (8 MUXes)
  stage 3:  shift by 1 if S0 = 1     (8 MUXes)
```

Any shift 0-7 is the sum of those powers: shift 5 = 4 + 1, so stages 1 and 3 act and stage 2 passes
through.

**For an n-bit barrel shifter: log₂(n) stages, log₂(n) select lines, n·log₂(n) MUXes.**

### ALU

One block performing several arithmetic and logic operations, chosen by a select word. A typical
small ALU:

| S1 | S0 | Operation |
|---|---|---|
| 0 | 0 | `A + B` |
| 0 | 1 | `A - B` |
| 1 | 0 | `A AND B` |
| 1 | 1 | `A OR B` |

Structure: an **arithmetic unit** (adder-subtractor from file 03), a **logic unit** (gate array),
and an output MUX selecting between them.

```
   A, B --+--> [ arithmetic unit ] --+
          |                          +--> [ MUX ] --- result
          +--> [ logic unit ]      --+
                                        |
                                   select lines
```

The classic MSI part is the **74181**, a 4-bit ALU with 4 function-select lines plus a mode line
(M = 0 arithmetic, M = 1 logic) giving 16 functions in each mode.

---

## Worked — 2-bit magnitude comparator

Compare `A = A1 A0` with `B = B1 B0`.

```
  x1 = XNOR(A1, B1)
  x0 = XNOR(A0, B0)

  (A = B) = x1 · x0
  (A > B) = A1·B1' + x1·A0·B0'
  (A < B) = A1'·B1 + x1·A0'·B0
```

**Test `A = 10`, `B = 01`:**

```
  x1 = XNOR(1,0) = 0
  (A > B) = 1·1 + 0·(...) = 1
```

A > B, decided at the MSB — the `x1` factor switches off the lower-bit terms entirely. That
gating is the mechanism to describe in an exam answer.

---

## Traps

**Equality is XNOR, not XOR.** XOR is the *inequality* detector. Writing `x_i = A_i ⊕ B_i` inverts
the whole comparator.

**Higher bits gate lower bits.** Every lower-order term in a magnitude comparator carries the
`x` factors for all bits above it. Dropping them makes `A = 0111` compare as greater than
`B = 1000`.

**Arithmetic left shift equals logical left shift.** The sign-replication rule applies on the
**right** shift only. A question asking for both on the left is testing whether you know they
coincide.

**Barrel shifter stages are powers of two, not one each.** `log₂(n)` stages, not `n`.

---

## Self-test

1. Design a 1-bit comparator using only NAND gates.
2. Write the `(A > B)` equation for a 4-bit comparator and verify it for `A = 0110`, `B = 0101`.
3. `10110100` is an 8-bit 2's-complement number. Give its value, then its value after an arithmetic
   right shift by 1 and after a logical right shift by 1.
4. `110110` — apply: logical shift left 2, logical shift right 1, circular shift right 2.
5. How many 2:1 MUXes in a 16-bit barrel shifter? How many select lines?
6. Show how the third comparator output can be derived from the other two.

---
---
---

## Answers

**1.** `L = A'·B`, `G = A·B'`, `E = (L + G)'`.

```
  A'   = NAND(A, A)
  B'   = NAND(B, B)
  n1   = NAND(A', B)          = (A'B)'
  L    = NAND(n1, n1)         = A'B
  n2   = NAND(A, B')          = (AB')'
  G    = NAND(n2, n2)         = AB'
  E    = NAND(n1, n2)         = ( (A'B)' · (AB')' )' ... 
```

Careful with the last one: `NAND(n1, n2) = (n1·n2)'`. With `n1 = (A'B)'` and `n2 = (AB')'`,

```
  n1 · n2 = (A'B)'·(AB')' = (A'B + AB')' = (A ⊕ B)'
  E = ( (A ⊕ B)' )' = A ⊕ B          -- that is XOR, not XNOR
```

So `NAND(n1, n2)` gives XOR. Invert once more:

```
  E = NAND( NAND(n1,n2), NAND(n1,n2) )
```

**8 NAND gates** total. The near-miss above is the exact error to avoid — always expand the
De Morgan rather than assuming the bubble count.

**2.**

```
  (A > B) = A3·B3' + x3·A2·B2' + x3·x2·A1·B1' + x3·x2·x1·A0·B0'
```

For `A = 0110`, `B = 0101`:

```
  x3 = XNOR(0,0) = 1      x2 = XNOR(1,1) = 1      x1 = XNOR(1,0) = 0

  term 1: A3·B3'          = 0·1 = 0
  term 2: x3·A2·B2'       = 1·1·0 = 0
  term 3: x3·x2·A1·B1'    = 1·1·1·1 = 1
  term 4: x3·x2·x1·A0·B0' = 1·1·0·... = 0

  (A > B) = 1
```

Correct: 6 > 5, decided at bit 1.

**3.** `10110100`. MSB is 1, so it is negative.

```
  2's complement value: invert -> 01001011, add 1 -> 01001100 = 76,  so value = -76
```

**Arithmetic right shift by 1:** replicate the sign bit.

```
  10110100 -> 11011010
  Value: invert -> 00100101, +1 -> 00100110 = 38,  so value = -38
```

And `-76 / 2 = -38`. The arithmetic shift preserved the division.

**Logical right shift by 1:** fill with 0.

```
  10110100 -> 01011010  = +90
```

The value jumped from -76 to +90 — the sign was destroyed. This is exactly why arithmetic shift
exists.

**4.** `110110`:

```
  logical shift left 2    ->  011000
  logical shift right 1   ->  011011
  circular shift right 2  ->  101101
```

Check the rotate: the two LSBs `10` come off the right and reappear at the left of the remaining
`1101`, giving `10` + `1101` = `101101`.

**5.** 16-bit barrel shifter: `log₂(16) = 4` stages, each with 16 MUXes.

```
  4 × 16 = 64 two-input MUXes,  4 select lines  (shift amounts 0 to 15)
```

**6.** The three outputs are mutually exclusive and exhaustive — exactly one is high. So any one is
the NOR of the other two:

```
  (A < B) = ( (A > B) + (A = B) )'
```

One NOR gate replaces a four-term AND-OR network. Exam answers that build all three from scratch
are correct but wasteful; note the relation and you save half the drawing.
