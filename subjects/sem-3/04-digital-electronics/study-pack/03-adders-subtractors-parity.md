# 03 — Adders, Subtractors, Parity

---

## Map

```
   Half adder ---> Full adder ---> Ripple-carry adder ---> BCD adder
                        |                  |
                        |                  +--> Carry-look-ahead (speed fix)
                        |                  +--> Serial adder (one FA + shift regs)
                        v
                 Half / Full subtractor ---> 2's-complement adder-subtractor
                        |
                        v
                 Parity generator / checker   (XOR tree)
```

Everything on this page is built from one gate: **XOR**. Sum is XOR. Difference is XOR. Parity is
XOR. Learn the XOR identities and most of this file collapses.

```
  A (+) 0 = A          A (+) 1 = A'         A (+) A = 0         A (+) A' = 1
  XOR of n bits = 1  exactly when the number of 1s is ODD
```

---

## Attempt first

1. Write the sum and carry equations of a half adder.
2. A full adder has three inputs. Write `Sum` and `Cout` without looking.
3. Build a full adder from two half adders. What gate joins the two carries, and why that gate?
4. A 4-bit ripple-carry adder has full adders of 10 ns delay each. Worst-case delay to a valid sum?
5. `1011` is fed to a 4-bit **even** parity generator. What is the output bit?
6. Why can a plain 4-bit binary adder not add `0111 + 0110` correctly in BCD, and what fixes it?

---

## Method

### Half adder

Adds two bits. No carry input.

| A | B | Sum | Carry |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

```
  Sum   = A (+) B
  Carry = A · B
```

### Full adder

Adds two bits **plus a carry in** — the cell you actually chain.

| A | B | Cin | Sum | Cout |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

```
  Sum  = A (+) B (+) Cin                      = Sigma-m(1, 2, 4, 7)
  Cout = A·B + B·Cin + A·Cin                  = Sigma-m(3, 5, 6, 7)
       = A·B + Cin·(A (+) B)                  <- the two-half-adder form
```

**Memorise `Sum = Sigma-m(1,2,4,7)` and `Cout = Sigma-m(3,5,6,7)`.** The decoder question in file 05
and the MUX questions in file 04 both start from those two index sets.

### Full adder from two half adders

```
   A ---+
        | HA1 |--- S1 ------+
   B ---+     |--- C1 --+   | HA2 |--- Sum
                        |   |     |
   Cin ------------------+---+     |--- C2
                        |
              C1 --+    |
                   | OR |--------------- Cout
              C2 --+
```

- HA1: `S1 = A (+) B`, `C1 = A·B`
- HA2: `Sum = S1 (+) Cin`, `C2 = S1·Cin`
- `Cout = C1 + C2`

**An OR joins them, and an XOR would work equally well here** — C1 and C2 can never both be 1 at
once (if `A·B = 1` then `S1 = 0`, so `C2 = 0`). Examiners ask why; that mutual exclusion is the
answer.

### Ripple-carry adder

n full adders chained, carry out to carry in.

```
   A3 B3      A2 B2      A1 B1      A0 B0
    | |        | |        | |        | |
   [FA3]<--C3-[FA2]<--C2-[FA1]<--C1-[FA0]<-- Cin
    |          |          |          |
    S3         S2         S1         S0
   Cout
```

**Worst-case delay = n × (delay of one full adder).** The carry must physically propagate from
bit 0 to bit n-1. This is the adder's whole weakness and the reason carry-look-ahead exists.

### Carry-look-ahead

Compute the carries from the inputs directly instead of waiting for them.

```
  Generate:   G_i = A_i · B_i             this bit makes a carry by itself
  Propagate:  P_i = A_i (+) B_i           this bit passes an incoming carry along

  C_(i+1) = G_i + P_i · C_i
```

Expand it and every carry is a two-level function of the inputs:

```
  C1 = G0 + P0·C0
  C2 = G1 + P1·G0 + P1·P0·C0
  C3 = G2 + P2·G1 + P2·P1·G0 + P2·P1·P0·C0
```

**Delay becomes constant (two gate levels) instead of proportional to n** — paid for in fan-in and
gate count, which is why real designs use 4-bit look-ahead blocks chained together.

### Subtractors

**Half subtractor** (A - B):

```
  Difference = A (+) B
  Borrow     = A' · B
```

**Full subtractor** (A - B - Bin):

```
  Difference = A (+) B (+) Bin
  Bout       = A'·B + A'·Bin + B·Bin
             = A'·B + Bin·(A (+) B)'
```

**Note the difference from the adder:** `Sum` and `Difference` are the *same* expression; only the
carry/borrow term differs — `A·B` becomes `A'·B`, one complement.

### Adder-subtractor from one circuit

Use 2's complement. XOR each B bit with a mode line M, and feed M into Cin:

```
   M = 0  ->  B passes through unchanged, Cin = 0  ->  A + B
   M = 1  ->  B is inverted, Cin = 1               ->  A + B' + 1 = A - B
```

```
   B_i ---+
          | XOR |--- to FA_i
   M -----+
   M ------------------> Cin of FA0
```

One 4-bit adder plus four XOR gates does both operations. **Overflow** (signed) is flagged by
`C_n (+) C_(n-1)` — the carry into the sign bit differing from the carry out of it.

### BCD adder

BCD digits are 0000 to 1001 only. A 4-bit binary adder produces 0000 to 1111 plus a carry, so any
result above 9 is not a valid BCD digit.

**Correction: when the sum exceeds 9, add 0110 (decimal 6) and generate a decimal carry.**

Detect the invalid condition from the binary sum `S3 S2 S1 S0` and the binary carry `Cout`:

```
  Y = Cout + S3·S2 + S3·S1
```

- `Cout` catches sums of 16 and above.
- `S3·S2` catches 1100 to 1111 (12-15).
- `S3·S1` catches 1010 to 1011 (10-11).

Together they catch exactly 10 through 19.

```
   A3..A0   B3..B0
      |       |
   [ 4-bit binary adder ]---- Cout
      |  S3 S2 S1 S0
      |       |
      |   [ Y = Cout + S3S2 + S3S1 ]---- decimal carry out
      |       |
   [ 4-bit binary adder ]  <-- adds 0110 when Y = 1, 0000 when Y = 0
      |
   corrected BCD digit
```

**Worked instance:** `0111 + 0110` = 7 + 6.

```
  0111 + 0110 = 1101   (13, Cout = 0)
  Y = 0 + 1·1 + 1·0 = 1        -> correction needed
  1101 + 0110 = 1 0011
  Result: decimal carry 1, digit 0011  ->  "1 3"   correct
```

### Serial adder

One full adder plus shift registers. Bits are presented one pair per clock, LSB first; the carry is
stored in a D flip-flop and fed back.

**n bits take n clock cycles** — minimum hardware, maximum time. The opposite trade from
carry-look-ahead.

### Parity

**Even parity generator** outputs the bit that makes the *total* number of 1s even:

```
  P_even = A (+) B (+) C (+) D
```

It is 1 exactly when the data word has an **odd** number of 1s — that extra 1 is what makes the
total even. This inversion of wording is the whole trap.

**Odd parity generator** is the complement:

```
  P_odd = ( A (+) B (+) C (+) D )'          = XNOR at the final stage
```

**Checker:** XOR all data bits together with the received parity bit. For an even-parity system the
checker output is 0 when the word is clean and 1 when an error is present.

```
   A --+
       |XOR|--+
   B --+      |XOR|--+
   C --+      |      |XOR|--- P
       |XOR|--+      |
   D --+             |
```

Three XOR gates in a tree for 4 bits. Parity detects **any odd number of bit errors** and is blind
to any even number — two flipped bits pass as clean.

---

## Worked — MTE 2025 Q2 (2 marks)

> The four-bit binary sequence `1011` is applied to an even parity generator circuit. What will be
> the output?

Count the 1s in `1011`: **three**, which is odd.

```
  P = 1 (+) 0 (+) 1 (+) 1 = 1
```

**Output = 1.**

With that parity bit appended, the transmitted word `1011 1` contains four 1s — even, as required.

The fast check: **odd number of 1s in the data -> even-parity bit is 1.**

---

## Traps

**"Even parity generator" does not mean "output 1 when the input is even."** It means the output
makes the *total* even. Count the data 1s: odd count -> output 1.

**Full subtractor borrow is `A'B + ...`, not `AB + ...`.** One complement separates it from the
adder's carry. Derive it rather than recalling it if you are unsure.

**BCD correction is `+0110`, and it is triggered by `Y = Cout + S3S2 + S3S1`.** Writing "add 6 when
sum > 9" is true but unmarked — the question wants the detection logic.

**Ripple delay is n × FA delay, not n × gate delay.** Read what the question gives you.

---

## Self-test

1. Write the full-adder `Cout` in both forms and show they are equal.
2. Design a full subtractor. Give both equations.
3. A 4-bit ripple-carry adder uses full adders with 12 ns propagation delay. What is the worst-case
   time to a stable `Cout`? What if it used carry-look-ahead with 2 gate levels of 5 ns each?
4. Add `1001 + 1000` in BCD. Show the correction and the final output.
5. Draw a 4-bit **odd** parity generator.
6. In a full adder built from two half adders, can `C1` and `C2` both be 1? Prove your answer.
7. An adder-subtractor is set to `M = 1` with `A = 0110`, `B = 0011`. Trace the result.

---
---
---

## Answers

**1.**

```
  Form 1:  Cout = A·B + B·Cin + A·Cin
  Form 2:  Cout = A·B + Cin·(A (+) B)
```

Expand form 2: `A (+) B = A'B + AB'`, so

```
  Cin·(A (+) B) = A'·B·Cin + A·B'·Cin
  Cout = A·B + A'·B·Cin + A·B'·Cin
```

Compare with form 1. Where `A·B = 1`, both give 1. Where `A·B = 0`, form 1 reduces to
`Cin·(A + B)` with A and B not both 1, which is exactly `Cin·(A (+) B)`. Equal on all 8 rows.

**2.** Full subtractor, A - B - Bin:

```
  Difference = A (+) B (+) Bin
  Bout       = A'·B + A'·Bin + B·Bin      =  A'·B + Bin·(A (+) B)'
```

Verify the 1s: Bout = 1 for `(A,B,Bin)` = 001, 010, 011, 111. Check 001: `A'B = 0`,
`Bin·(A(+)B)' = 1 · (0(+)0)' = 1 · 1 = 1`. Correct.

**3.** Ripple: `4 × 12 = 48 ns`.
Carry-look-ahead: 2 levels × 5 ns = **10 ns**, independent of the word length (before the extra
fan-in cost is counted).

**4.** `1001 + 1000` = 9 + 8 = 17.

```
  1001 + 1000 = 1 0001        binary sum 0001, Cout = 1
  Y = Cout + S3S2 + S3S1 = 1 + 0 + 0 = 1      -> correct
  0001 + 0110 = 0111
  Result: decimal carry 1, digit 0111   ->  "1 7"    correct
```

Note this case is caught by `Cout` alone — the `S3S2` and `S3S1` terms are for sums of 10 to 15,
which produce no binary carry.

**5.** Same XOR tree as even parity, with the last stage inverted:

```
   A --+
       |XOR|--+
   B --+      |XNOR|--- P_odd
   C --+      |
       |XOR|--+
   D --+
```

Equivalently, three XORs followed by a NOT. `P_odd = (A (+) B (+) C (+) D)'`.

**6.** No. `C1 = A·B` and `C2 = S1·Cin` where `S1 = A (+) B`.

If `C1 = 1` then `A = B = 1`, so `S1 = 1 (+) 1 = 0`, so `C2 = 0`.
If `C2 = 1` then `S1 = 1`, so A and B differ, so `A·B = 0`, so `C1 = 0`.

They are mutually exclusive, which is why OR and XOR both work as the final carry gate.

**7.** `M = 1` inverts B and sets `Cin = 1`.

```
  B  = 0011  ->  B' = 1100
  A + B' + Cin = 0110 + 1100 + 1 = 1 0011
```

Discard the carry out: result `0011` = 3. And `6 - 3 = 3`. Correct.
The carry out of 1 in a subtraction signals **no borrow** — the result is non-negative.
