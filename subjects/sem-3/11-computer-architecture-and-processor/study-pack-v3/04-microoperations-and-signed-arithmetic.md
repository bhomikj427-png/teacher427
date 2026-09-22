# 04 — Microoperations and signed arithmetic

**Assignment 1: Q8, Q9, Q15, Q16, Q18, Q19 · 36 of 200 marks · U1 (L5–L7) · needs 00, 02, 03**

Six questions, all of them *doing* questions rather than *describing* questions. They are the easiest
marks in Assignment 1 to secure and the easiest to throw away on arithmetic slips.

> ⚠ **One of these questions is a trap, and it is worth knowing before you start.** A1 Q9 asks you to
> add +64 and +84 in 8-bit 2's complement. That **overflows**, and the expected answer is not a number
> — it is spotting the overflow. Step 3.

---

## Map

```
   [1] What a microoperation is ─── four categories ───┐
                                                       │
        ┌──────────────────┬───────────────────────────┤
        ▼                  ▼                           ▼
   [2] Signed numbers  [4] Arithmetic µops       [6] Logic µops
       3 systems           add, sub, inc, dec        AND OR XOR NOT
        │                  │                          │
        ▼                  ▼                          ▼
   [3] Overflow        [5] The adder-subtractor   [7] A1 Q18 trace
       the trap            one circuit, two jobs      (all three combined)
                                                       │
                                                       ▼
                                                  [8] Shift µops
                                                      logical / circular / arithmetic
```

---

## The questions this file answers

| # | Question | Marks | Mano |
|---|---|---|---|
| 1 | `[A1 Q15]` What is micro-operation? What are the different types of micro-operations? | 4 | — |
| 2 | `[A1 Q8]` How are +64 and −64 represented in signed-magnitude, 1's complement, and 2's complement? | 4 | ≈3-13 |
| 3 | `[A1 Q9]` Perform the addition of R1 = +64 and R2 = +84 using 2's complement. Registers are 8-bit. | 4 | ≈3-17 |
| 4 | `[A1 Q16]` Design a 4-bit adder-subtractor using four full-adders. Explain its working for (i) M=0, A=0111, B=0110 (ii) M=1, A=0101, B=1010. | 8 | **4-12** |
| 5 | `[A1 Q18]` Determine the results in R1–R4 after the given sequence of micro-operations. | 8 | **4-19** |
| 6 | `[A1 Q19]` Find the sequence of binary values in R after a logical shift-right, a circular shift right, a logical shift left, and a circular shift left, from R = 11111111. | 8 | **4-21** |

Mano's unasked follow-ups: **3-13 to 3-18, 4-13 to 4-18, 4-20.**

---

## Build

### 1 · What a microoperation is

> **Q** `[A1 Q15 · 4 marks]`
> **What is micro-operation? What are the different types of micro-operations?**
>
> *You have been using the word since file 00. Guess the definition and the count before reading on.*

**Definition to write:** a microoperation is an **elementary operation performed on data stored in
registers**, completed in **one clock pulse**.

Both halves matter. "Elementary" rules out anything needing intermediate storage; "one clock pulse" is
what makes it the *atom* of the machine — it is why `ADD 201` is not one microoperation (file 01,
step 3) and why file 03's illegal statements were illegal.

**Four categories** — this is the list he wants:

| Category | What it does | Example |
|---|---|---|
| **Register transfer** | move binary information between registers | `R2 ← R1` |
| **Arithmetic** | arithmetic on numeric data in registers | `R3 ← R1 + R2` |
| **Logic** | bit-manipulation on non-numeric data | `R3 ← R1 ∧ R2` |
| **Shift** | shift operations on data in registers | `R2 ← shr R2` |

Register transfer was file 03. The other three are this file, one step each.

> ✓ **Check 1.** (a) Give the two-part definition. (b) Which category does `AC ← AC ⊕ DR` belong to?
> (c) Why is "one clock pulse" part of the definition rather than an incidental detail?

---

### 2 · Signed numbers — three systems

> **Q** `[A1 Q8 · 4 marks]`
> **How are the +64 and −64 signed numbers represented in the signed-magnitude, 1's complement, and
> 2's complement number systems?**
>
> *Work out +64 in 8 bits first — you can do that from file 00. Then guess how the minus sign gets in.
> Then read on.*

+64 = 01000000 in 8 bits, and **a positive number looks the same in all three systems.** Only the
negatives differ, and each system differs only in *how it makes a negative*:

| System | Rule for the negative | −64 |
|---|---|---|
| **Signed-magnitude** | flip the **sign bit only**, leave the magnitude alone | **1**1000000 |
| **1's complement** | **invert every bit** of the positive | **10111111** |
| **2's complement** | invert every bit, **then add 1** | **11000000** |

Check the 2's complement: 01000000 → invert → 10111111 → +1 → **11000000**.

> **Notice something the question is quietly testing:** for −64 the signed-magnitude and 2's
> complement forms are *identical* (11000000). That is a coincidence of this number — 64 is a power of
> two, so its magnitude field is `1000000` and complementing-plus-one lands on the same pattern. It
> is **not** a general rule. Try −65 and they differ. Saying this out loud is worth a mark.

**Why 2's complement is the one machines use:** there is **only one zero** (00000000), whereas
signed-magnitude and 1's complement both have +0 and −0; and subtraction becomes addition, so one
adder does both jobs (step 5). Range for n bits: **−2ⁿ⁻¹ to +2ⁿ⁻¹ − 1** — for 8 bits, **−128 to +127**.
Hold that range; the next step is about what happens when you leave it.

> ✓ **Check 2.** (a) Represent −65 in all three systems and confirm they differ.
> (b) How many representations of zero does each system have?
> (c) `[Mano 3-13]` Give the 1's and 2's complements of 10101110 and of 00000000.

---

### 3 · Overflow — the trap in A1 Q9

> **Q** `[A1 Q9 · 4 marks]`
> **Perform the addition of two signed numbers R1 = +64 and R2 = +84 using 2's complement number
> systems. The size of each register is 8-bit.**
>
> *Add 64 + 84 in your head first. Then look at the range you just learnt in step 2. Then read on.*

64 + 84 = 148. The 8-bit signed range stops at **+127**. **The answer does not fit**, and that is the
entire point of the question. Writing "148" scores nothing — 148 cannot exist in this register.

Do it in binary:

```
   +64   0 1 0 0 0 0 0 0
   +84   0 1 0 1 0 1 0 0
       ─────────────────
         1 0 0 1 0 1 0 0
         ▲
         sign bit = 1 → the result reads as NEGATIVE
```

As a signed 8-bit value, `10010100` = **−108**. Two positive numbers added to give a negative one.
That is a **sign reversal**, and it is the symptom.

**The overflow test — two equivalent forms, know both:**

| Test | Here |
|---|---|
| **Carry into the sign bit ≠ carry out of the sign bit** | carry **into** bit 7 = 1, carry **out** = 0 → unequal → **overflow** |
| **V = C**ₙ **⊕ C**ₙ₋₁ | V = 0 ⊕ 1 = **1** |
| (informal) adding two numbers of the **same sign** gives a result of the **opposite** sign | + and + gave − → overflow |

**Model answer:** *"+64 = 01000000 and +84 = 01010100. Their sum is 10010100. The carry into the sign
position is 1 while the carry out is 0; they are unequal, so an **overflow** has occurred. The result
is invalid as an 8-bit signed number — the true sum 148 exceeds the 8-bit signed range −128 to +127,
and the stored pattern reads as −108. The V (overflow) flag would be set."*

⚠ **Overflow can only happen when the two operands have the same sign.** Adding a positive and a
negative can never overflow — the magnitude only shrinks.

> ✓ **Check 3.** (a) Why can +64 + (−84) never overflow? (b) `[Mano 3-16]` Perform (+42) + (−13) and
> (−42) − (−13) in 8-bit 2's complement. (c) What is the largest pair of positive 8-bit values that
> can be added without overflow?

---

### 4 · Arithmetic microoperations

> **Q** `[A1 Q18(i) · part of 8 marks]` **= Mano 4-19**
> **R1 = 11110010 and R2 = 11111111. Determine the result of `R1 ← R1 + R2`.**
>
> *Add them. Then look at R2 again and guess why the professor chose that particular value.
> Then read on.*

He chose 11111111 because **in 2's complement, all-ones is −1**. So `R1 ← R1 + R2` here is
*decrement in disguise*, and the arithmetic confirms it: 11110010 = 242, 242 + 255 = 497, which in
8 bits is **11110001** (= 241) with a carry out that is discarded. 242 − 1 = 241. ✓

That identity — **adding all-1s subtracts 1** — is the reason the table below has no separate
decrementer.

**The arithmetic microoperations, and what each is built from:**

| RTL | Name | Hardware |
|---|---|---|
| `R3 ← R1 + R2` | add | binary adder — n full adders, ripple carry |
| `R3 ← R1 − R2` | subtract | the same adder, as `R1 + R2′ + 1` |
| `R2 ← R2′` | 1's complement | inverters |
| `R2 ← R2′ + 1` | 2's complement (negate) | inverters + increment |
| `R1 ← R1 + 1` | increment | binary incrementer (half-adders + constant 1) |
| `R1 ← R1 − 1` | decrement | add all-1s |

Multiply and divide are **not** microoperations — they are *sequences* of them (shift and add), which
is why they take many clock pulses.

> ✓ **Check 4.** (a) Why is there no separate subtractor circuit? (b) What is 11111111 as a signed
> 8-bit number? (c) `R2 ← R2 + 1` where R2 = 11111111 — what is the result, and what happened to the
> carry?

---

### 5 · The adder-subtractor — one circuit, two jobs

> **Q** `[A1 Q16 · 8 marks]` **= Mano 4-12**
> **Design a 4-bit adder-subtractor combinational circuit using four full-adder circuits. Explain its
> working using: (i) M = 0, A = 0111, B = 0110  (ii) M = 1, A = 0101, B = 1010.**
>
> *Step 4 said subtraction is A + B′ + 1. Guess what single extra gate per bit turns an adder into a
> subtractor. Then read on.*

**One XOR gate per bit**, and the mode line doubles as the input carry. That is the whole design, and
it is the cleanest example in the course of *control signals selecting behaviour from fixed hardware*.

```
        B₃      B₂      B₁      B₀
         │       │       │       │
   M ──┬─⊕──┬──┬─⊕──┬──┬─⊕──┬──┬─⊕──┐
       │    │  │    │  │    │  │    │
   A₃ ─┼───►FA │ A₂►FA │ A₁►FA │ A₀►FA ◄── C₀ = M
       │    │  │    │  │    │  │    │
       │   C₄  │   C₃  │   C₂  │   C₁
       │    │       │       │       │
      S₃ ◄─┘   S₂ ◄─┘  S₁ ◄─┘  S₀ ◄─┘
```

**Why it works:**

| M | XOR output | C₀ | Result |
|---|---|---|---|
| **0** | B ⊕ 0 = **B** (passes) | 0 | **A + B** |
| **1** | B ⊕ 1 = **B′** (inverts) | 1 | **A + B′ + 1 = A − B** |

M = 1 supplies *both* halves of the 2's complement at once: the XORs invert B, and feeding M into C₀
adds the 1. One line, one job each.

**Case (i): M = 0, A = 0111, B = 0110 → addition.**

```
     0 1 1 1     (A = 7)
   + 0 1 1 0     (B = 6)
   ───────────
     1 1 0 1     S = 1101,  C₄ = 0
```
S₃S₂S₁S₀ = **1101**, C₄ = **0**. Unsigned this is 7 + 6 = 13 ✓.
Read as *signed* 4-bit, 1101 = −3, and the carry into the sign (1) differs from the carry out (0), so
**V = 1**: 13 exceeds the 4-bit signed maximum of +7. Worth one line.

**Case (ii): M = 1, A = 0101, B = 1010 → subtraction.**

B′ = 0101, C₀ = 1:
```
     0 1 0 1     (A)
   + 0 1 0 1     (B′)
   +       1     (C₀ = M)
   ───────────
     1 0 1 1     S = 1011,  C₄ = 0
```
S₃S₂S₁S₀ = **1011**, C₄ = **0**.
Unsigned: 5 − 10, and **C₄ = 0 signals a borrow** — in a subtractor, *no carry out means the result
went negative*. 1011 is the 4-bit 2's complement of −5. ✓
Signed: B = 1010 reads as −6, so this is 5 − (−6) = +11, which overflows 4 bits — V = C₄ ⊕ C₃ = 0 ⊕ 1 = 1.
**Say which interpretation you are using;** the bit pattern is the same either way.

> ✓ **Check 5.** (a) What does C₄ = 0 mean after a subtraction? (b) How many XOR gates in an 8-bit
> adder-subtractor? (c) `[Mano 4-12(c)]` Do M = 1, A = 1100, B = 1000. (d) `[Mano 4-13]` How would you
> build a 4-bit **decrementer** from four full-adders?

---

### 6 · Logic microoperations — mask, set, complement, insert

> **Q** `[Mano 4-18 · not yet asked, and a standard exam item]`
> **Register A holds the 8-bit binary 11011001. Determine the B operand and the logic microoperation
> to be performed in order to change the value in A to: (a) 01101101  (b) 11111101**
>
> *Guess which of AND, OR, XOR you would use for each, before working out B. Then read on.*

Logic microoperations work **bit by bit on non-numeric data** — they are for manipulating individual
bits, not for arithmetic. Sixteen two-variable logic functions exist; four are built: **AND (∧),
OR (∨), XOR (⊕), complement (′)**. Everything else is made from those.

The three named applications are what get examined:

| Application | Operation | Mechanism | Worked |
|---|---|---|---|
| **Selective set** | `A ← A ∨ B` | 1s in B **force** those A bits to 1; 0s in B leave A alone | A=1010, B=1100 → **1110** |
| **Selective complement** | `A ← A ⊕ B` | 1s in B **toggle** those A bits | A=1010, B=1100 → **0110** |
| **Mask / selective clear** | `A ← A ∧ B` | **0s in B clear** those A bits; 1s let them through | A=1010, B=1100 → **1000** |
| **Clear (test equality)** | `A ← A ⊕ B` with A = B | gives all zeros — XOR is 0 exactly when the bits match | — |

**Insert = mask, then OR** — two steps, and he can ask for either half:
to put `1001` into the high nibble of A = `11010110`:
1. mask: A ∧ `00001111` = `00000110` (clears the target field)
2. insert: ∨ `10010000` = **`10010110`**

Now the question. Compare A with the target, bit by bit:

**(a) 11011001 → 01101101.** Bits change in both directions (some 1→0, some 0→1). Only **XOR** can do
both, so it is selective complement. B = A ⊕ target:
```
  A       1 1 0 1 1 0 0 1
  target  0 1 1 0 1 1 0 1
  XOR     1 0 1 1 0 1 0 0   →  B = 10110100,  operation: A ← A ⊕ B
```

**(b) 11011001 → 11111101.** Every change is 0→1 and nothing goes 1→0. That is **selective set** —
use OR, with 1s only where a bit must be forced up:
```
  A       1 1 0 1 1 0 0 1
  target  1 1 1 1 1 1 0 1
  differ      ↑     ↑        →  B = 00100100,  operation: A ← A ∨ B
```

**The method, generalised:** *all changes 0→1* → OR. *All changes 1→0* → AND (with 0s at those
positions). *Changes in both directions* → XOR with the difference pattern.

> ✓ **Check 6.** (a) Which operation would you use if every change were 1→0, and what is B?
> (b) Mask the low nibble of 11010110 to zero — give B and the result.
> (c) `[Mano 4-18]` Insert `1010` into the **low** nibble of `11011001` in two steps.

---

### 7 · The full trace — A1 Q18

> **Q** `[A1 Q18 · 8 marks]` **= Mano 4-19**
> **The initial values of the 8-bit registers R1, R2, R3, R4 are R1 = 11110010, R2 = 11111111,
> R3 = 10111001, R4 = 11101010. Determine the results in each register once the following sequence
> of micro-operations has been performed:**
> **i) `R1 ← R1 + R2`  ii) `R3 ← R3 ∧ R4, R2 ← R2 + 1`  iii) `R1 ← R1 − R3`**
>
> *You can now do every line. Do it on paper before reading — this is the one question in the file
> that is pure execution.*

The only thing that can go wrong is bookkeeping: **each line uses the values produced by the line
before it.** Track all four registers on every line, even the unchanged ones.

**Line (i)** `R1 ← R1 + R2` — step 4 already did this: 11110010 + 11111111 = **11110001** (carry out
discarded). R1 = 11110001.

**Line (ii)** — two microoperations, one clock pulse, different destinations, so both are legal
(file 03, step 8).
```
 R3 ← R3 ∧ R4     1 0 1 1 1 0 0 1
                  1 1 1 0 1 0 1 0   AND
                  ───────────────
                  1 0 1 0 1 0 0 0    R3 = 10101000

 R2 ← R2 + 1      11111111 + 1 = 00000000    R2 = 00000000  (carry out discarded)
```

**Line (iii)** `R1 ← R1 − R3` = 11110001 − 10101000, done as R1 + R3′ + 1:
```
  R3′ + 1  =  01010111 + 1  =  01011000
      1 1 1 1 0 0 0 1
    + 0 1 0 1 1 0 0 0
    ─────────────────
    1 0 1 0 0 1 0 0 1        R1 = 01001001,  carry out 1 discarded
```
Check in decimal: 241 − 168 = 73 = 01001001 ✓

**Answer table — present it exactly like this:**

| After | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| start | 11110010 | 11111111 | 10111001 | 11101010 |
| (i) | **11110001** | 11111111 | 10111001 | 11101010 |
| (ii) | 11110001 | **00000000** | **10101000** | 11101010 |
| (iii) | **01001001** | 00000000 | 10101000 | 11101010 |

R4 is never a destination, so it never changes. Say so — it shows you understood rather than copied.

> ✓ **Check 7.** (a) Why is line (ii) legal as a single clock pulse? (b) What happened to the carry
> out in lines (i) and (iii)? (c) Would the answer change if line (ii)'s two microoperations were
> swapped in order?

---

### 8 · Shift microoperations

> **Q** `[A1 Q19 · 8 marks]` **= Mano 4-21**
> **Find the sequence of binary values in register R following a logical shift-right, a circular
> shift right, a logical shift left, and a circular shift left, starting from R = 11111111.**
>
> *File 02, step 6 built the hardware and left one thing undecided: what enters the vacated end.
> Guess how many different answers there are to that. Then read on.*

There are three, and **that single choice is the entire difference between the three shift types.**
The hardware is identical.

| Type | RTL | What enters the vacated position | Used for |
|---|---|---|---|
| **Logical** | `shl`, `shr` | **0** | unsigned data, bit manipulation |
| **Circular (rotate)** | `cil`, `cir` | **the bit that fell out the other end** | rotating — no information lost |
| **Arithmetic** | `ashl`, `ashr` | `ashr`: **a copy of the sign bit**; `ashl`: 0 | signed × 2 and ÷ 2 |

**Why arithmetic shift is different:** in 2's complement, shifting right divides by 2 and left
multiplies by 2 — but *only if the sign survives*. Shifting a 0 into the MSB of a negative number
would make it positive. So `ashr` **replicates the sign bit** (sign extension). `ashl` shifts 0 in at
the right and **overflows if the sign changes**, tested by **V = Rₙ₋₁ ⊕ Rₙ₋₂** *before* the shift.

Now the question. It says *"the sequence"*, so each shift is applied to the **result of the previous
one** — not four independent shifts from 11111111. Getting that wrong is the commonest error here.

| Step | Operation | R before | R after | What entered |
|---|---|---|---|---|
| start | — | — | 11111111 | — |
| 1 | logical shift **right** | 11111111 | **01111111** | 0 at the MSB |
| 2 | circular shift **right** | 01111111 | **10111111** | the 1 that fell off the LSB end |
| 3 | logical shift **left** | 10111111 | **01111110** | 0 at the LSB |
| 4 | circular shift **left** | 01111110 | **11111100** | the 0 that fell off the MSB end |

Answer: **01111111 → 10111111 → 01111110 → 11111100.**

⚠ `ashr` of an odd negative number rounds **toward −∞**, not toward zero: −5 `ashr` 1 = −3, not −2.

> ✓ **Check 8.** (a) What is the only difference between the three shift types?
> (b) `[Mano 4-20]` An 8-bit register holds 10011100. Give the result of an arithmetic shift right.
> Then, from the same start, an arithmetic shift left — and say whether it overflows.
> (c) Why would `shr` be wrong for dividing a negative number by 2?

---

## Exam form

### Definitions

| Term | Write |
|---|---|
| **Microoperation** | An elementary operation performed on data stored in registers, completed in one clock pulse — e.g. load, clear, shift, increment. |
| **Overflow** | A result that cannot be represented in the available number of bits; detected when the carry into the sign position differs from the carry out of it (V = Cₙ ⊕ Cₙ₋₁). |

### The four categories `[A1 Q15]`

Register transfer · arithmetic · logic · shift. One example each.

### 2's complement facts

- negate = invert all bits, add 1
- range for n bits = **−2ⁿ⁻¹ … +2ⁿ⁻¹ − 1** (8 bits: −128 … +127)
- all-1s = **−1**; adding all-1s = decrement
- one zero only
- **overflow only when both operands have the same sign**

### The three applications of logic microoperations

| Goal | Operation | How to find B |
|---|---|---|
| Force bits to 1 (selective set) | `A ∨ B` | 1s where a bit must go up |
| Force bits to 0 (mask / clear) | `A ∧ B` | **0s** where a bit must go down, 1s elsewhere |
| Toggle bits (selective complement) | `A ⊕ B` | 1s where A and the target differ |
| Insert a field | mask **then** OR | two steps — say both |

### The three shift types

Distinguished only by what enters: **0** (logical) · **the bit shifted out** (circular) · **the sign
bit** (arithmetic right).

---

## Attempt

On paper, in this order (they get harder):

1. `[A1 Q15 · 4]` definition + four categories with examples.
2. `[A1 Q8 · 4]` +64 and −64 in all three systems — and note where two of them coincide.
3. `[A1 Q9 · 4]` the addition. **Your answer must contain the word "overflow".**
4. `[A1 Q19 · 8]` the shift sequence — sequential, not independent.
5. `[A1 Q18 · 8]` the trace, presented as a four-column table.
6. `[A1 Q16 · 8]` the adder-subtractor circuit + both cases worked.

Then from Mano: **3-13, 3-16, 3-17** (complements and overflow), **4-13** (decrementer), **4-18**
(mask/set), **4-20** (arithmetic shift overflow).

---

## Traps

| Trap | Correction |
|---|---|
| Answering A1 Q9 with "148" | It overflows. The answer is the detection, not the number |
| Thinking +64 + (−84) might overflow | Opposite signs can never overflow |
| Taking A1 Q19's four shifts as independent | It says "the sequence" — each acts on the previous result |
| `shr` used on signed data | Use `ashr`, which replicates the sign bit |
| Forgetting that C₄ = 0 after subtraction means borrow | In a subtractor, no carry out = the result went negative |
| Giving only the changed registers in A1 Q18 | Show all four on every line, including unchanged R4 |
| Mask with 1s where you want bits cleared | Backwards — **0s** clear, 1s pass |
| Multiply treated as a microoperation | It is a sequence of shifts and adds, many clock pulses |
| Ignoring the discarded carry out | In fixed-width registers the carry out is dropped; say so |

---

## Self-test

1. Define a microoperation in one sentence containing both required parts.
2. −1 in 8-bit 2's complement is what pattern, and what does adding it do?
3. Two 8-bit values are added; the carry into bit 7 is 0 and the carry out is 1. Overflow?
4. A = 10110011. You need 10110000. Which operation, and what is B?
5. R = 10011100. Apply `cir` once, then `ashr` once. Give both results.
6. Why does one adder circuit suffice for both addition and subtraction?
7. What is the 8-bit signed range, and which A1 question is designed to break it?

---
---

## Answers

**Check 1.** (a) An elementary operation on data stored in registers, completed in **one clock pulse**.
(b) **Logic**. (c) Because it defines the *atom* of the machine — anything that cannot finish in one
pulse must be broken into several microoperations across several timing steps, which is why
instructions take multiple ticks.

**Check 2.** (a) +65 = 01000001. Signed-magnitude −65 = **11000001**; 1's complement = **10111110**;
2's complement = **10111111**. All three differ. (b) Signed-magnitude **two** (00000000, 10000000);
1's complement **two** (00000000, 11111111); 2's complement **one**. (c) 10101110: 1's = **01010001**,
2's = **01010010**. 00000000: 1's = **11111111**, 2's = **00000000** (the +1 carries out and is dropped
— the reason 2's complement has a single zero).

**Check 3.** (a) The magnitudes partly cancel, so the result is smaller than the larger operand and
must fit. (b) (+42) + (−13): 00101010 + 11110011 = **00011101** = +29 ✓, carry out discarded, no
overflow. (−42) − (−13) = (−42) + (+13): 11010110 + 00001101 = **11100011** = −29 ✓.
(c) +127 and… nothing — 127 + 1 already overflows. The largest safe pair sums to 127, e.g. 64 + 63.

**Check 4.** (a) Because `A − B = A + B′ + 1` — the same adder does it with B inverted and a carry-in
of 1. (b) **−1**. (c) **00000000**, with a carry out of 1 that is discarded — the register wraps.

**Check 5.** (a) A **borrow**: the subtraction went negative (for the unsigned reading). (b) **8**.
(c) M = 1, A = 1100, B = 1000 → B′ = 0111, C₀ = 1: 1100 + 0111 + 1 = **0100**, C₄ = **1**. (12 − 8 = 4,
and C₄ = 1 means no borrow ✓.) (d) Feed every B input a constant **1** (i.e. B = 1111) with C₀ = 0, so
the circuit computes A + 1111 = A − 1.

**Check 6.** (a) **AND**, with B carrying **0s** at the positions to clear and 1s everywhere else.
(b) B = **11110000** → 11010110 ∧ 11110000 = **11010000**. (c) mask: 11011001 ∧ 11110000 =
**11010000**; then OR: 11010000 ∨ 00001010 = **11011010**.

**Check 7.** (a) The two microoperations have **different destination registers** (R3 and R2).
(b) Discarded — the registers are 8 bits wide and there is nowhere to put a 9th bit. (c) No — they are
simultaneous and independent; neither reads the other's destination.

**Check 8.** (a) **What enters the vacated bit position** — 0, the bit shifted out, or the sign bit.
(b) `ashr` of 10011100: the sign bit 1 is preserved and copied → **11001110**. `ashl` of 10011100: 0
enters at the right → **00111000**; check V = R₇ ⊕ R₆ before the shift = 1 ⊕ 0 = **1 → overflow** (the
sign flipped from negative to positive). (c) It shifts a 0 into the sign position, turning a negative
number positive — the result would be badly wrong, not merely rounded.

**Self-test 1.** An elementary operation performed on data stored in registers, completed in one clock
pulse.

**Self-test 2.** **11111111**; adding it **decrements** (it is −1).

**Self-test 3.** Carry in ≠ carry out → **yes, overflow** (V = 0 ⊕ 1 = 1).

**Self-test 4.** All changes are 1→0 → **AND (mask)**, B = **11111100**.

**Self-test 5.** `cir` of 10011100: the LSB 0 wraps to the MSB → **01001110**. Then `ashr` of 01001110:
the sign bit 0 is replicated → **00100111**.

**Self-test 6.** Because subtraction is `A + B′ + 1`, and one XOR per bit plus a carry-in of 1
converts the adder into a subtractor under a single mode line.

**Self-test 7.** **−128 to +127**; **A1 Q9** (+64 + 84 = 148).

---

## What to do next

File 05 puts steps 4, 6 and 8 into one circuit — the **arithmetic logic shift unit**. That is A1 Q17,
16 marks, and the professor's own deck ends on it as an exam question. It is the highest-value single
item in U1.
