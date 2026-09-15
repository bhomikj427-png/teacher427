# 03 — Arithmetic, Logic and Shift Microoperations, and the ALSU

**U1, lectures L5–L8 · CO1.** Six of the nineteen pre-MTE lectures are this material. The deck's
**closing slide is an exam question**: *"Design a 4-bit ALU that may perform the following
operations. Explain its working in detail."* Treat that as the single most likely U1 item.

---

## Map

```
   MICROOPERATION = one elementary operation on data held in registers
        |
        +-- register transfer   R2 <- R1                    (file 02)
        +-- ARITHMETIC          add, subtract, inc, dec, complement
        |       |
        |       +--> one adder-subtractor:  A + B(xor M) + M
        |       +--> the 4-bit arithmetic circuit: FA + 4-to-1 MUX per bit
        |
        +-- LOGIC               AND, OR, XOR, complement
        |       |
        |       +--> the three applications: selective set | selective complement | mask
        |       +--> insert = mask then OR
        |
        +-- SHIFT               logical | circular | arithmetic
                |
                +--> what differs is ONLY what enters the vacated end
                          |
                          v
                   ALSU = arithmetic + logic + shl + shr, all computed,
                          S3 S2 selects the block, S1 S0 (+ Cin) selects within it
```

---

## Attempt first

1. Name the four categories of microoperation.
2. One circuit does both addition and subtraction with a single mode line M. How?
3. In the 4-bit arithmetic circuit, what is fed to the Y input of each full adder, and what selects it?
4. `A = 1010`, `B = 1100`. Give `A ∨ B`, `A ⊕ B`, `A ∧ B`, and name the application each one is used
   for.
5. You need to place `1001` into the **high** nibble of `A = 1101 0110` without disturbing the low
   nibble. Two microoperations — which, in what order?
6. Shift `1011` right: (a) logically, (b) circularly, (c) arithmetically. Interpret all three as
   signed 4-bit numbers.
7. An ALSU has S₃S₂S₁S₀ and Cᵢₙ. How many distinct operations, and where does the number come from?

---

## Method

### The four categories

| Category | What it does |
|---|---|
| **Register transfer** | move binary information between registers |
| **Arithmetic** | arithmetic on numeric data in registers |
| **Logic** | bit-manipulation on non-numeric data |
| **Shift** | shift operations on data in registers |

### Arithmetic microoperations

| RTL | Name | Built from |
|---|---|---|
| `R3 ← R1 + R2` | add | binary adder (n full adders, ripple carry) |
| `R3 ← R1 − R2` | subtract | via `R1 + R2′ + 1` (2's complement) |
| `R2 ← R2′` | 1's complement | inverters |
| `R2 ← R2′ + 1` | 2's complement (negate) | complement + increment |
| `R1 ← R1 + 1` | increment | binary incrementer (half-adders + a constant 1) |
| `R1 ← R1 − 1` | decrement | add all 1s (= −1 in 2's complement) |

**★ The adder-subtractor mechanism — one circuit, one mode line.** Pass each B input through an XOR
with a mode line M, and feed **M into C₀** as well:

```
         M = 0                              M = 1
   B ⊕ 0 = B,  C₀ = 0                  B ⊕ 1 = B′,  C₀ = 1
   => D = A + B                       => D = A + B' + 1 = A - B
```

*One* adder does both. This is the cleanest example in the course of "control signals select
behaviour from fixed hardware."

**The 4-bit arithmetic circuit — the deck's own construction.** One full adder per bit. X is always
A. **Y is driven by a 4-to-1 MUX** selecting B, B′, 0 or 1 under S₁S₀. Cᵢₙ is the third control.

| S₁ | S₀ | Cᵢₙ | Y | Output D | Microoperation |
|---|---|---|---|---|---|
| 0 | 0 | 0 | B | D = A + B | add |
| 0 | 0 | 1 | B | D = A + B + 1 | add with carry |
| 0 | 1 | 0 | B′ | D = A + B′ | subtract with borrow |
| 0 | 1 | 1 | B′ | D = A + B′ + 1 | **subtract** |
| 1 | 0 | 0 | 0 | D = A | transfer A |
| 1 | 0 | 1 | 0 | D = A + 1 | increment A |
| 1 | 1 | 0 | 1 | D = A − 1 | decrement A |
| 1 | 1 | 1 | 1 | D = A | transfer A |

**Two things examiners ask about this table.**

- *Why is `A + 1111` the same as `A − 1`?* Because in 2's complement all-1s **is** −1. That is the
  identity behind the last two rows.
- *Why do rows 5 and 8 agree?* Three control bits give 8 combinations but the circuit has only **7
  distinct operations** — row 8 is `A + 1111 + 1 = A + 10000 = A` with the carry-out discarded. The
  redundancy is real, not a misprint.

### Logic microoperations

Bit-wise operations on **non-numeric** data — used "to change bit values, delete a group of bits, or
insert new bit values."

Sixteen logic functions of two variables exist; **four are implemented**: **AND (∧), OR (∨),
XOR (⊕), complement (′)**. Everything else is built from those.

**The three named applications — this is what gets examined.**

| Application | Operation | Rule | A = 1010, B = 1100 |
|---|---|---|---|
| **Selective set** | `A ← A ∨ B` | 1s in B **force** those A bits to 1 | → **1110** |
| **Selective complement** | `A ← A ⊕ B` | 1s in B **toggle** those A bits | → **0110** |
| **Mask (selective clear)** | `A ← A ∧ B` | **0s in B clear** those A bits; 1s pass through | → **1000** |

**Insert = mask, then OR** — a two-step recipe, always in that order:

```
   A       = 1101 0110       put 1001 into the high nibble
   mask:   A ∧ 0000 1111 = 0000 0110      (clear the target field)
   insert: ∨ 1001 0000     = 1001 0110    (OR in the new value)
```

**Clear** is `A ⊕ B` with A = B → all zeros. Which is also the **equality test**: XOR gives 0 exactly
when the two operands are equal.

### Shift microoperations

Three kinds. **What distinguishes them is entirely what enters at the vacated serial input.**

| Type | RTL | Serial input | Use |
|---|---|---|---|
| **Logical** | `shl`, `shr` | **0** | unsigned data, bit manipulation |
| **Circular (rotate)** | `cil`, `cir` | **the bit shifted out the other end** | nothing is lost |
| **Arithmetic** | `ashl`, `ashr` | `ashr`: **the sign bit is replicated**; `ashl`: 0 enters | signed ×2 / ÷2 |

**Why arithmetic shift is different.** In 2's complement, shifting right divides by 2 and shifting
left multiplies by 2 — **but only if the sign is preserved**. So `ashr` copies the sign bit into the
MSB (sign extension); shifting in a 0 instead would turn a negative number into a large positive one.

For an n-bit register with sign bit Rₙ₋₁:

- **`ashr`**: Rₙ₋₁ is **unchanged** and also copied into Rₙ₋₂; everything else shifts right.
- **`ashl`**: 0 enters at the right. **Overflow** occurs if the sign changes — i.e. if
  **Rₙ₋₁ ⊕ Rₙ₋₂ = 1 before the shift**, because the bit about to move into the sign position differs
  from the sign.

> **`ashl` overflow test:  V = Rₙ₋₁ ⊕ Rₙ₋₂  (evaluated before the shift)**

⚠ `ashr` of an odd negative number rounds **toward −∞**, not toward zero: −5 `ashr` 1 = **−3**, while
integer division −5/2 = −2.

**Hardware:** a combinational shifter is a MUX per bit position (select = direction / no-shift) — the
barrel shifter you already met in Digital Electronics.

### The Arithmetic Logic Shift Unit

**Structure — one stage, replicated n times:**

```
             +----------------------+
   Ai --+--->|  arithmetic circuit  |--> Di --+
   Bi --+    |  (FA + 4-to-1 MUX)   |         |      +---------+
        |    +----------------------+         +----->| 4-to-1  |
        |    +----------------------+         |      |  MUX    |--> Fi
        +--->|    logic circuit     |--> Ei --+      | S1 S0   |
             +----------------------+         |      +---------+
   Ai+1 --------- shift right input ----------+           ^
   Ai-1 --------- shift left  input ----------+           |
                                                     S3 S2 select
```

- **S₃, S₂** select **which block** reaches the output: arithmetic · logic · shift-right · shift-left.
- **S₁, S₀** (plus **Cᵢₙ**) select **which operation inside** the chosen block.
- Total control: **4 select lines + Cᵢₙ**.

**The operation count, derived rather than recited:**

| S₃S₂ | Block | Operations |
|---|---|---|
| 00 | arithmetic | **8** (the S₁S₀ + Cᵢₙ table above) |
| 01 | logic | **4** (AND, OR, XOR, complement) |
| 10 | shift right | **1** |
| 11 | shift left | **1** |
| | | **14 total** |

⚠ **14 is Mano's standard 4-select-line design, not a universal constant.** A differently drawn ALSU
gives a different count — **derive it from the table you drew**, and say which design you assumed.

**★ The mechanism to say out loud in the answer:** the ALSU computes **all** candidate results in
parallel, every cycle; the select lines merely choose which one is allowed out. Hardware does not
"decide, then compute" — it computes everything and discards. That is why the ALSU's delay is the
same regardless of which operation is selected, and it is the deep reason control is just *selection*
(the idea U2's control unit is built on).

---

## Worked — the deck's own question: design a 4-bit ALSU and explain its working (form F4)

> **Design a 4-bit arithmetic logic shift unit and explain its working in detail.**

This is an 8-mark-shaped answer. Five parts, in this order.

**(1) State the specification.** A 4-bit ALSU performing 14 operations under four select lines
S₃S₂S₁S₀ and a carry input Cᵢₙ, operating on two 4-bit operands A and B.

**(2) Draw one stage** (the figure above) and then say the load-bearing sentence: *"this stage is
replicated four times, once per bit; all four stages share the same select lines, and the carry
ripples from stage i to stage i+1."*

**(3) Give the arithmetic block.** One full adder per bit; X = Aᵢ; Y = the output of a 4-to-1 MUX
selecting 0, Bᵢ, Bᵢ′ or 1 under S₁S₀ (ALSU wiring — see the correction below); Cᵢₙ into stage 0.

**(4) Give the logic block.** Four gates per bit — AND, OR, XOR, NOT of Aᵢ — selected by S₁S₀:

| S₁ | S₀ | Output Eᵢ | Operation |
|---|---|---|---|
| 0 | 0 | Aᵢ ∧ Bᵢ | AND |
| 0 | 1 | Aᵢ ∨ Bᵢ | OR |
| 1 | 0 | Aᵢ ⊕ Bᵢ | XOR |
| 1 | 1 | Aᵢ′ | complement A |

**(5) Give the output MUX and the full function table.** The 4-to-1 output MUX takes Dᵢ (arithmetic),
Eᵢ (logic), Aᵢ₊₁ (shift right) and Aᵢ₋₁ (shift left), selected by S₃S₂:

> ⚠ **Corrected 2026-09-15.** This table previously reused the arithmetic-circuit ordering. The
> professor's ALSU slide (deck 1 p. 32) and Mano Table 4-8 use the ordering below, which corresponds to
> the arithmetic MUX wired **0 → 0, 1 → B, 2 → B′, 3 → 1**. Draw the MUX that way in this answer.
> Worked in full in `../study-pack-v2/05-alsu.md`.

| S₃ | S₂ | S₁ | S₀ | Cᵢₙ | Operation | Function |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | F = A | transfer A |
| 0 | 0 | 0 | 0 | 1 | F = A + 1 | increment A |
| 0 | 0 | 0 | 1 | 0 | F = A + B | addition |
| 0 | 0 | 0 | 1 | 1 | F = A + B + 1 | add with carry |
| 0 | 0 | 1 | 0 | 0 | F = A + B′ | subtract with borrow |
| 0 | 0 | 1 | 0 | 1 | F = A + B′ + 1 | subtraction |
| 0 | 0 | 1 | 1 | 0 | F = A − 1 | decrement A |
| 0 | 0 | 1 | 1 | 1 | F = A | transfer A |
| 0 | 1 | 0 | 0 | × | F = A ∧ B | AND |
| 0 | 1 | 0 | 1 | × | F = A ∨ B | OR |
| 0 | 1 | 1 | 0 | × | F = A ⊕ B | XOR |
| 0 | 1 | 1 | 1 | × | F = A′ | complement A |
| 1 | 0 | × | × | × | F = shr A | shift right |
| 1 | 1 | × | × | × | F = shl A | shift left |

**(6) The "explain its working" paragraph** — the part most answers omit and most marks hide in:

> All four blocks receive A and B and produce their results **simultaneously and continuously**.
> S₃S₂ drives the output multiplexer, which admits exactly one of those results to F; S₁S₀ and Cᵢₙ
> choose the operation within the arithmetic or logic block. Nothing is "decided" before computing —
> the unselected blocks compute too, and their outputs are discarded. Consequently the propagation
> delay is set by the slowest block (the ripple-carry adder, whose delay grows with word length),
> not by which operation was requested.

---

## Worked — logic microoperations on given patterns (inferred form; mechanism from the deck)

> **`A = 1011 0101`. (a) Set the high nibble to all 1s without changing the low nibble. (b) Toggle
> bits 3 and 0 only. (c) Clear the high nibble. (d) Replace the low nibble with 1110.**

Pick the operation from the *effect you want*, not by trial:

| Want | Operation | Because |
|---|---|---|
| force bits to 1 | **OR** with 1s there | 1 ∨ x = 1 |
| toggle bits | **XOR** with 1s there | 1 ⊕ x = x′ |
| clear bits | **AND** with 0s there | 0 ∧ x = 0 |
| leave bits alone | OR/XOR with **0**, or AND with **1** | identity elements |

```
(a)  A ∨ 1111 0000  =  1011 0101 ∨ 1111 0000  =  1111 0101
(b)  A ⊕ 0000 1001  =  1011 0101 ⊕ 0000 1001  =  1011 1100
(c)  A ∧ 0000 1111  =  1011 0101 ∧ 0000 1111  =  0000 0101
(d)  two steps:  mask   A ∧ 1111 0000 = 1011 0000
                 insert   ∨ 0000 1110 = 1011 1110
```

**(d) is the one that costs marks** — a single OR would give `1011 1111`, because OR can only set
bits, never clear the ones already there. **Insert is always mask-then-OR.**

---

## Traps

| # | Trap | The correction |
|---|---|---|
| M5 | "Arithmetic right shift is the same as dividing by 2, always" | For negative odd numbers `ashr` rounds toward **−∞**: −5 `ashr` 1 = −3, not −2 |
| T12 | Using `shr` where `ashr` is meant | `shr` shifts in **0**, which turns a negative number into a large positive one. `ashr` replicates the **sign** |
| M6 | "The ALSU decides which operation to do, then does it" | It computes **all** of them every cycle and selects. That is why its delay is constant across operations |
| — | Quoting "14 operations" as a universal fact | 14 belongs to *this* design (4 select lines, 8 + 4 + 1 + 1). Derive it from your own table |
| — | Doing an insert with OR alone | OR cannot clear. **Mask first** (AND), then OR |
| — | Treating rows 5 and 8 of the arithmetic table as an error | 8 combinations, 7 distinct operations. `A + 1111 + 1 = A` |
| — | Forgetting Cᵢₙ is a **third** control input, not part of S₁S₀ | The arithmetic block has 8 rows precisely because of it |

---

## Self-test

1. Build a subtractor from an adder. Give the two things the mode line M must do.
2. In the 4-bit arithmetic circuit, what does S₁S₀ = 10 with Cᵢₙ = 1 compute, and how does the MUX
   make it happen?
3. `A = 1100 1010`, `B = 0110 0110`. Compute `A ∧ B`, `A ∨ B`, `A ⊕ B`.
4. Insert `0111` into the **low** nibble of `A = 1010 1010`. Show both microoperations.
5. Register `R = 1001` (4-bit, 2's complement). Apply `shr`, `cir`, and `ashr`. Give all three
   results and their signed decimal values.
6. `R = 0110`. Does `ashl R` overflow? Apply the test, then verify by computing the decimal values.
7. An ALSU is built with **3** select lines plus Cᵢₙ, where S₂ selects arithmetic-vs-logic and there
   is no shift block. How many operations? Show the arithmetic.
8. Why does the ALSU's propagation delay not depend on which operation you select — and what *does*
   set it?

---

## Answers

**1.** M must (a) invert every B input, via an XOR of Bᵢ with M, and (b) supply the +1, by being fed
into C₀. Then M = 0 gives A + B and M = 1 gives A + B′ + 1 = A − B.

**2.** S₁S₀ = 10 selects **Y = 0** at every MUX, so the adder computes A + 0 + Cᵢₙ. With Cᵢₙ = 1 that
is **D = A + 1**, the **increment**. The MUX makes it happen by feeding a constant 0 to every full
adder's Y input, which turns the adder into a pass-through for A and lets the carry-in do the work.

**3.**
```
   A     = 1100 1010
   B     = 0110 0110
   A ∧ B = 0100 0010
   A ∨ B = 1110 1110
   A ⊕ B = 1010 1100
```

**4.**
```
   mask:    1010 1010 ∧ 1111 0000 = 1010 0000
   insert:  1010 0000 ∨ 0000 0111 = 1010 0111
```

**5.** R = 1001 = **−7** signed.

| Operation | Result | Signed value | Comment |
|---|---|---|---|
| `shr R` | **0100** | +4 | a 0 entered at the MSB — the sign is destroyed |
| `cir R` | **1100** | −4 | the bit shifted out at the right re-entered at the left |
| `ashr R` | **1100** | −4 | the sign bit was replicated; −7/2 rounds toward −∞ → −4 |

Note `cir` and `ashr` agree here by coincidence (the LSB happened to equal the sign bit); they are not
the same operation.

**6.** R = 0110. Test **before** the shift: R₃ ⊕ R₂ = 0 ⊕ 1 = **1** → **overflow**.
Verify: 0110 = +6; `ashl` gives 1100 = **−4**, not +12. The sign flipped, exactly as the test
predicted. (+12 is unrepresentable in 4-bit 2's complement, whose range is −8…+7.)

**7.** S₂ = 0 selects arithmetic: S₁S₀ + Cᵢₙ = 3 bits = **8** operations. S₂ = 1 selects logic:
S₁S₀ = **4** operations (Cᵢₙ is a don't-care there). No shift block. **8 + 4 = 12 operations.**
The point of the question is that the count is *derived* from how many bits reach each block — never
memorized.

**8.** Because every block computes continuously from the same inputs and the output multiplexer only
*selects*; there is no sequencing and nothing is skipped. The delay is therefore the **worst-case
path through the slowest block plus the output MUX** — in practice the **ripple-carry adder**, whose
carry must propagate through all n stages, so t_add ≈ n · t_carry. That is why widening the machine
(4 → 16 → 64 bits) directly threatens the clock period, and why real designs replace ripple carry
with carry-lookahead.
