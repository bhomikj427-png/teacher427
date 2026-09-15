# 04 — Microoperations, Signed Numbers, the Adder-Subtractor

**Assignment 1: Q8, Q9, Q15, Q16, Q18, Q19 · 36 of 200 marks · U1 (L6–L8)**

---

## Map

```
   Signed-number representation ──► 2's-complement addition + overflow
                                            │
                                            ▼
   Microoperation types ──────────► 4-bit adder-subtractor (one circuit, mode M)
   (transfer, arithmetic,                   │
    logic, shift)                           ▼
                                    Register traces: sequences of microops
                                            │
                                            ▼
                                    Shifts: logical, circular, arithmetic
```

---

## Attempt

1. Represent **+64** and **−64** in signed-magnitude, 1's complement and 2's complement (8 bits).
2. Add R1 = +64 and R2 = +84 in 8-bit 2's complement. Comment on the result.
3. What is a microoperation? What are the types?
4. Design a 4-bit adder-subtractor from four full adders. Explain its working for
   **(i)** M = 0, A = 0111, B = 0110 **(ii)** M = 1, A = 0101, B = 1010.
5. 8-bit registers: R1 = 11110010, R2 = 11111111, R3 = 10111001, R4 = 11101010. Give every register
   after, in order:
   **(i)** `R1 ← R1 + R2` **(ii)** `R3 ← R3 ∧ R4, R2 ← R2 + 1` **(iii)** `R1 ← R1 − R3`
6. Starting from R = 11111111, give the sequence of values after a logical shift right, a circular
   shift right, a logical shift left and a circular shift left.

---

## Learn

### Three signed representations (n bits, MSB = sign)

| | Positive | Negative | Range (8-bit) | Zeros |
|---|---|---|---|---|
| **Signed-magnitude** | 0 + magnitude | **1** + magnitude | −127 … +127 | two (+0, −0) |
| **1's complement** | same as SM | invert **every** bit of +x | −127 … +127 | two |
| **2's complement** | same as SM | invert every bit of +x, **add 1** | **−128 … +127** | one |

**Positive numbers are identical in all three.** Only negatives differ.

**Shortcut for 2's complement:** copy bits from the right up to and including the first 1, then invert
the rest.

### 2's-complement addition and overflow

Add all n bits including the sign; **discard the carry out** of the MSB.

**Overflow** happens only when two operands of the **same sign** give a result of the **other** sign.
Hardware test: **V = Cₙ ⊕ Cₙ₋₁** (carry into the sign bit XOR carry out of it).

### Microoperation types

| Type | Example | Hardware |
|---|---|---|
| Register transfer | `R2 ← R1` | wires + load |
| Arithmetic | `R3 ← R1 + R2`, `R1 ← R1 + 1` | adder, incrementer |
| Logic | `R1 ← R1 ∧ R2`, `R1 ← R1 ⊕ R2` | gates per bit |
| Shift | `R1 ← shl R1` | MUX per bit |

### Arithmetic microoperations

| RTL | Meaning |
|---|---|
| `R3 ← R1 + R2` | add |
| `R3 ← R1 + R2′ + 1` | subtract = R1 − R2 |
| `R2 ← R2′` | 1's complement |
| `R2 ← R2′ + 1` | 2's complement (negate) |
| `R1 ← R1 + 1` / `R1 ← R1 − 1` | increment / decrement |

### The 4-bit adder-subtractor

```
          B₃        B₂        B₁        B₀
          │         │         │         │
   M ─────┼────┬────┼────┬────┼────┬────┼────┐
          │    │    │    │    │    │    │    │
        [XOR]◄─┘  [XOR]◄─┘  [XOR]◄─┘  [XOR]◄─┘
          │         │         │         │
    A₃ ┌──┴──┐ A₂ ┌──┴──┐ A₁ ┌──┴──┐ A₀ ┌──┴──┐
    ──►│ FA  │───►│ FA  │───►│ FA  │───►│ FA  │◄── C₀ = M
       │  3  │ C₃ │  2  │ C₂ │  1  │ C₁ │  0  │
       └┬──┬─┘◄───┴┬────┘◄───┴┬────┘◄───┴┬────┘
        │  │       │          │          │
   C₄ ◄─┘  S₃      S₂         S₁         S₀        (carries ripple right → left)
```

Each Bᵢ passes through XOR with M; M is also the carry into FA₀.

| M | XOR output | C₀ | Result |
|---|---|---|---|
| 0 | Bᵢ ⊕ 0 = **Bᵢ** | 0 | **A + B** |
| 1 | Bᵢ ⊕ 1 = **Bᵢ′** | 1 | A + B′ + 1 = **A − B** |

**Reading the result:**
- Unsigned: after subtraction, **C₄ = 1 means A ≥ B**, C₄ = 0 means A < B (result is the 2's complement
  of B − A).
- Signed: **V = C₄ ⊕ C₃** flags overflow.

### Shift microoperations

| Type | RTL | What enters the vacated bit |
|---|---|---|
| Logical | `shl`, `shr` | **0** |
| Circular | `cil`, `cir` | the bit shifted out the other end |
| Arithmetic | `ashl`, `ashr` | `ashr`: copy of the sign bit; `ashl`: 0 (overflow if sign changes) |

---

## Worked (A1 — full answers)

**Q8.** 8-bit.

| | +64 | −64 |
|---|---|---|
| Signed-magnitude | 0100 0000 | **1**100 0000 |
| 1's complement | 0100 0000 | 1011 1111 |
| 2's complement | 0100 0000 | 1100 0000 |

(−64 in 2's complement: invert 0100 0000 → 1011 1111, add 1 → 1100 0000. SM and 2's complement happen
to coincide for −64 because 64 is a power of two with only one 1 bit, bit 6.)

**Q9.**
```
      C₈ C₇
       0  1          ← carries out of and into the sign bit
   R1 = +64    0100 0000
   R2 = +84  + 0101 0100
             ───────────
               1001 0100
```
The result reads as **−108**, but +64 + +84 = **+148**, which exceeds the 8-bit maximum of +127.
Two positives gave a negative → **overflow**. V = C₈ ⊕ C₇ = 0 ⊕ 1 = **1**. The register cannot hold
the answer; a 9th bit would be needed (0 1001 0100 = 148).

**Q15.** A microoperation is an elementary operation performed on data stored in registers, executed
in one clock pulse. Four types: register transfer, arithmetic, logic, shift (table above, one example
each).

**Q16.** Circuit and M-table above. The two cases:

```
 (i)  M = 0 → add            (ii) M = 1 → subtract
      A      0111                 A          0101
      B      0110                 B′         0101   (1010 inverted by the XORs)
    + C₀        0               + C₀            1
      ─────────                   ─────────────
      C₄=0  1101                  C₄=0  1011
```

| Case | Unsigned reading | Signed reading |
|---|---|---|
| (i) | 7 + 6 = **13** ✓ (C₄ = 0, no unsigned overflow) | +7 + +6 → 1101 = −3: **overflow**, V = C₄ ⊕ C₃ = 0 ⊕ 1 = 1 |
| (ii) | 5 − 10: C₄ = 0 → A < B; 1011 is the 2's complement of 0101, i.e. **−5** ✓ | 1010 = −6, so +5 − (−6) = +11 > +7: **overflow**, V = 0 ⊕ 1 = 1 |

Mano's own solution reads both cases unsigned (13 and −5). State the unsigned reading as the answer;
add the signed overflow line for completeness.

**Q18.** Sequential — each step uses the results of the previous one.

```
 (i)  R1 ← R1 + R2        1111 0010
                        + 1111 1111
                        ───────────
                        1 1111 0001   carry discarded → R1 = 1111 0001
                                      (adding all 1s = subtracting 1)

 (ii) R3 ← R3 ∧ R4        1011 1001
                        ∧ 1110 1010
                        ───────────
                          1010 1000   → R3 = 1010 1000
      R2 ← R2 + 1         1111 1111 + 1 = 1 0000 0000 → R2 = 0000 0000
      (comma: both happen on the same edge)

 (iii) R1 ← R1 − R3       1111 0001            = R1 + R3′ + 1
                        + 0101 0111   (R3′)
                        +         1
                        ───────────
                        1 0100 1001   carry discarded → R1 = 0100 1001
                        check: 241 − 168 = 73 = 0100 1001 ✓
```

| | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| start | 1111 0010 | 1111 1111 | 1011 1001 | 1110 1010 |
| after (i) | **1111 0001** | 1111 1111 | 1011 1001 | 1110 1010 |
| after (ii) | 1111 0001 | **0000 0000** | **1010 1000** | 1110 1010 |
| after (iii) | **0100 1001** | 0000 0000 | 1010 1000 | 1110 1010 |

**Q19.** "Sequence" = each shift applies to the previous result.

```
   start            1111 1111
   shr  (0 in)      0111 1111
   cir  (LSB→MSB)   1011 1111
   shl  (0 in)      0111 1110
   cil  (MSB→LSB)   1111 1100
```

If the examiner intended each shift applied to the **original** 1111 1111: shr 0111 1111, cir
1111 1111, shl 1111 1110, cil 1111 1111. Write the sequential answer and state the assumption in one
line ("missing data may be assumed suitably").

---

## Traps

| Trap | Correction |
|---|---|
| Writing −64 in 1's complement as 1100 0000 | That is 2's complement. 1's = invert only: 1011 1111 |
| Calling the carry-out an overflow | Carry-out is **unsigned** overflow. Signed overflow is V = Cₙ ⊕ Cₙ₋₁ |
| Adder-subtractor without M into C₀ | Then M = 1 gives A + B′ = A − B − 1 |
| Q18 step (ii) done in sequence | The comma means **same edge**; here the two don't interact, but in `A ← B, B ← A` order matters |
| Q18 step (iii) with the original R1 | Use R1 **after** step (i) |
| `cir` shifting in 0 | Circular shift re-inserts the bit that fell out |

---

## Self-test

1. Represent −1 in all three 8-bit forms.
2. Add −100 and −50 in 8-bit 2's complement. Overflow? Show V.
3. Adder-subtractor with M = 1, A = 1100, B = 0011. Give S, C₄, and both readings.
4. R = 1001 1100. Give `ashr R` and `ashl R`. Does `ashl` overflow?
5. R1 = 0000 1111, R2 = 1010 1010. After `R1 ← R1 ⊕ R2, R2 ← R2′`, then `R1 ← R1 ∨ R2`, give both.

---
---

## Answers

**Attempt 1–6.** See Worked.

**Self-test 1.** SM 1000 0001 · 1's 1111 1110 · 2's 1111 1111.

**Self-test 2.**
```
   −100 = 1001 1100
   −50  = 1100 1110
          ─────────
        1 0110 1010   → 0110 1010 = +106
```
Two negatives gave a positive → **overflow**. Carry into sign bit C₇ = 0, carry out C₈ = 1, V = 1.
(True result −150 < −128.)

**Self-test 3.** A + B′ + 1 = 1100 + 1100 + 1 = 1 1001 → S = 1001, C₄ = 1.
Unsigned: 12 − 3 = 9 ✓ (C₄ = 1 → A ≥ B). Signed: −4 − (+3) = −7 = 1001 ✓, V = C₄ ⊕ C₃ = 1 ⊕ 1 = 0.

**Self-test 4.** `ashr`: 1100 1110 (sign 1 copied). `ashl`: 0011 1000 — **overflow**: the sign changed
from 1 to 0 (test before shifting: R₇ ⊕ R₆ = 1 ⊕ 0 = 1).

**Self-test 5.**
```
   step 1:  R1 ← 0000 1111 ⊕ 1010 1010 = 1010 0101
            R2 ← (1010 1010)′          = 0101 0101
   step 2:  R1 ← 1010 0101 ∨ 0101 0101 = 1111 0101
```
R1 = 1111 0101, R2 = 0101 0101.
