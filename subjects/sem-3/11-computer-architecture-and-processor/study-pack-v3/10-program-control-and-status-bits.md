# 10 — Program control and status bits

**U3 (L15) · MTE scope · needs 04, 07, 09**

The other half of U3, and it is **Mano chapter 8, not chapter 7**. Where file 09 branched between
*microinstructions*, this file branches between *machine instructions* — and the deciding evidence is
four flag bits.

> Same warning as file 09: **neither assignment touches U3**, and the unit is on the mid-term all the
> same. Every question below is a Mano chapter-8 problem.

> This file is also where file 04's overflow rule stops being arithmetic and becomes **hardware**.

---

## Map

```
   [1] Program control instructions ── they change PC
            │
            ▼
   [2] The four status bits  C · S · Z · V
            │
            ├──► [3] Why V = Cₙ ⊕ Cₙ₋₁
            │
            ├──► [4] Unsigned compare → C, Z
            │
            ├──► [5] Signed compare  → S ⊕ V, Z
            │
            ▼
   [6] Conditional branch instructions
            │
            ▼
   [7] Subroutine call: fixed word vs register vs STACK ──► recursion
            │
            ▼
   [8] Interrupts: external · internal · software
```

---

## The questions this file answers

| # | Question | Mano |
|---|---|---|
| 1 | Perform AND, OR and XOR with 10011100 and 10101010. | **8-20** |
| 2 | Given 1001101011001101: what operation clears the first eight bits? sets the last eight? complements the middle eight? | **8-21** |
| 3 | Represent ±83, ±68 in 8 bits; add, subtract, shift, and detect overflow. | **8-23** |
| 4 | R = 72 hex. Determine C, S, Z, V after five given instructions. | **8-25** |
| 5 | Show that unsigned relative magnitude follows from C and Z. | **8-26** |
| 6 | Show that signed relative magnitude follows from S, Z and V. | **8-27** |
| 7 | A = 01000001, B = 10000100: decimal values, sum, status bits, true branches. | **8-29** |
| 8 | The same pair compared as **unsigned** by subtraction. | **8-30** |
| 9 | The same pair compared as **signed**. | **8-31** |

Also live: **8-22** (eight shift instructions), **8-24**, **8-28** (the ten-output branch circuit).

---

## Build

### 1 · What a program control instruction is

> **Q** *(the definition every other question here rests on)*
> **What distinguishes a program control instruction from a data-transfer or arithmetic instruction?**
>
> *Guess in one sentence. It is about one register.*

**A program control instruction changes the value of PC**, and therefore changes *which instruction
runs next*. Everything else — loads, stores, arithmetic — leaves PC to its default increment.

| Type | Examples |
|---|---|
| Branch / jump | BR, JMP — unconditional transfer |
| Conditional branch | BZ, BNZ, BC, BP, BM, BV — transfer if a flag says so |
| Skip | skip the next instruction if a condition holds (U2's SPA, SNA, SZA, SZE) |
| Call / return | subroutine entry and exit (step 7) |
| Compare / test | set the flags **without keeping the result** |

★ **Compare and test are the ones people misread.** A *compare* performs a subtraction and a *test*
performs an AND, but **neither stores the result** — the whole purpose is the side effect on the
status bits, which a following conditional branch then reads. That two-instruction pattern —
*compare, then branch* — is how every high-level `if` becomes machine code.

> ✓ **Check 1.** (a) Which register do all these instructions have in common? (b) What does a compare
> instruction do with its result? (c) Why must compare come immediately before the branch?

---

### 2 · The four status bits

> **Q** `[Mano 8-25]`
> **An 8-bit computer has a register R. Determine the values of status bits C, S, Z and V after each
> of the following instructions. The initial value of R in each case is hexadecimal 72. The numbers
> below are also hexadecimal.**
> **a. Add immediate operand C6 to R.  b. Add immediate 1E.  c. Subtract immediate 9A.
> d. AND immediate 8D.  e. Exclusive-OR R with R.**
>
> *This is the standard drill and a near-certain exam item. Do (a) before reading — all four bits.*

A **status register** holds bits set by the ALU's last operation:

| Bit | Name | Set when |
|---|---|---|
| **C** | carry | there is a carry out of the MSB |
| **S** | sign | the MSB of the result is 1 |
| **Z** | zero | every result bit is 0 |
| **V** | overflow | **Cₙ ⊕ Cₙ₋₁** — carry *into* the sign position differs from carry *out* of it |

```
        ┌──────────────────────┐
  A ───►│                      │──► result
  B ───►│        ALU           │
        └───┬──────┬──────┬────┘
            │      │      │
           Cₙ     Cₙ₋₁   result bits
            │      │      ├──► MSB ──────────► S
            ├──────⊕──────────────────────────► V
            └────────────────────────────────► C
                          └── 8-input NOR ───► Z
```

**Z is an n-input NOR across the whole result** — the same "check for zero" circuit you met in
file 08. It is not a wire.

**Now the five parts.** R = 72 = `0111 0010`.

**(a) Add C6** (`1100 0110`):
```
   0111 0010     (72)
 + 1100 0110     (C6)
 ──────────────
 1 0011 1000     = 38, carry out 1
```
Carry into bit 7 = 1, carry out = 1. **C = 1 · S = 0 · Z = 0 · V = 1 ⊕ 1 = 0.**
*(Sanity: signed, 114 + (−58) = 56 = 0x38 — fits, so no overflow, as V says.)*

**(b) Add 1E** (`0001 1110`):
```
   0111 0010     (72)
 + 0001 1110     (1E)
 ──────────────
   1001 0000     = 90, no carry out
```
Carry into bit 7 = 1, carry out = 0. **C = 0 · S = 1 · Z = 0 · V = 1 ⊕ 0 = 1.**
*(114 + 30 = 144 > 127 — signed overflow, exactly A1 Q9's situation from file 04.)*

**(c) Subtract 9A** — done as R + 9A′ + 1 = 72 + 66:
```
   0111 0010     (72)
 + 0110 0110     (9A' + 1 = 66)
 ──────────────
   1101 1000     = D8, no carry out
```
Carry into bit 7 = 1, carry out = 0. **C = 0 · S = 1 · Z = 0 · V = 1.**
*(As signed, 9A = −102, so this is 114 − (−102) = 216 > 127 — overflow. As unsigned, C = 0 after a
subtraction means a **borrow**: 114 < 154.)*

**(d) AND 8D** (`1000 1101`): `0111 0010 ∧ 1000 1101` = `0000 0000`.
Logic operations produce no carry and no signed overflow, so both are **cleared**.
**C = 0 · S = 0 · Z = 1 · V = 0.**

**(e) XOR R with R** = `0000 0000` — anything XOR itself is zero (file 04, step 6).
**C = 0 · S = 0 · Z = 1 · V = 0.**

> ✓ **Check 2.** (a) Which two bits do logic operations always clear? (b) How is Z generated in
> hardware? (c) `[Mano 8-20]` Perform AND, OR and XOR with 10011100 and 10101010.

---

### 3 · Why V is that XOR

> **Q** `[Mano 8-23]`
> **Represent +83, −83, +68, −68 in binary using eight bits. a. Perform (−83) + (+68) and interpret
> the result. b. Perform (−68) − (+83) and indicate if there is an overflow. c. Shift binary −68 once
> to the right and give the value in decimal. d. Shift binary −83 once to the left and indicate if
> there is an overflow.**
>
> *You have the mechanics from file 04. Guess which of (a) and (b) overflows before computing.*

**The representations** (file 04, step 2):

| | Binary |
|---|---|
| +83 | `0101 0011` |
| −83 | `1010 1101` |
| +68 | `0100 0100` |
| −68 | `1011 1100` |

**(a) (−83) + (+68)** = `1010 1101 + 0100 0100` = `1111 0001` = **−15** ✓ (and −83 + 68 = −15).
Opposite signs, so overflow is impossible — the magnitudes partly cancel.

**(b) (−68) − (+83)** = (−68) + (−83) = `1011 1100 + 1010 1101`:
```
   1011 1100
 + 1010 1101
 ──────────────
 1 0110 1001     = 69 hex, carry out 1
```
Carry into bit 7 = **0**, carry out = **1** → **V = 1, overflow.** And you can see it without the
rule: two negatives added gave a **positive** result (`0110 1001` = +105). The true answer −151 is
below the 8-bit floor of −128.

**★ Why V is Cₙ ⊕ Cₙ₋₁, mechanically.** The sign bit is just another bit position to the adder. If the
carry *into* it differs from the carry *out* of it, then the magnitude bits have **carried into and
corrupted the sign** — the result's sign no longer means what it should. When the two carries agree,
nothing has leaked across the boundary and the sign is trustworthy.

**C is for unsigned overflow; V is for signed.** Confusing them is the most common error in this
topic, and steps 4 and 5 are the two halves of that distinction.

**(c) −68 shifted right** — arithmetically, so the sign is replicated: `1011 1100` → `1101 1110` =
**−34** ✓ (−68 ÷ 2).

**(d) −83 shifted left** — test before shifting: R₇ ⊕ R₆ = 1 ⊕ 0 = **1 → overflow.** (−83 × 2 = −166,
below −128.) The shifted pattern `0101 1010` reads as +90, a sign reversal.

> ✓ **Check 3.** (a) Why can two numbers of opposite sign never overflow on addition? (b) State the
> two carries that define V. (c) Which flag reports unsigned overflow?

---

### 4 · Comparing unsigned numbers

> **Q** `[Mano 8-26]` **and** `[Mano 8-30]`
> **Two unsigned numbers A and B are compared by subtracting A − B. The carry bit is treated as a
> borrow, so C = 1 if A < B. Show that the relative magnitude of A and B follows from C and Z.**
> **Then: A = 01000001, B = 10000100. Evaluate A − B, determine C (borrow) and Z, and list the
> conditional branch instructions that will be true.**
>
> *Guess which two flags could possibly carry ordering information. Then read on.*

**The relation table** — this is what the question wants shown:

| Relation | Condition |
|---|---|
| A > B | C = 0 **and** Z = 0 |
| A ≥ B | C = 0 |
| A < B | C = 1 |
| A ≤ B | C = 1 **or** Z = 1 |
| A = B | Z = 1 |
| A ≠ B | Z = 0 |

**Why it works:** the subtraction A − B is performed as A + B′ + 1. If A ≥ B the result is
non-negative and the adder produces a **carry out**; if A < B it does not. Machines that treat C as a
**borrow** invert that carry, so **borrow = 1 exactly when A < B**. Z then separates "greater" from
"greater or equal".

**Now the numbers.** A = `01000001` = 65, B = `10000100` = 132.
```
   0100 0001     (A)
 + 0111 1100     (B' + 1)
 ──────────────
   1011 1101     = BD, no carry out
```
The raw carry out is **0**, so under the borrow convention **C (borrow) = 1** — and indeed
65 < 132 ✓. Z = **0** (the result `1011 1101` is non-zero).

**Branches that are true:** those testing **A < B** (C = 1) and **A ≤ B** (C = 1 or Z = 1) and
**A ≠ B** (Z = 0). In flag terms: **BC** (branch on carry/borrow) and **BNZ**.

⚠ **Say which convention you are using.** The adder's carry out is 0; the *borrow* is 1. They are
complements, and the question hands you the convention in its own wording.

> ✓ **Check 4.** (a) Why does C = 1 mean A < B under the borrow convention? (b) Which flag alone
> distinguishes = from ≠? (c) What is the raw carry out in the worked example?

---

### 5 · Comparing signed numbers

> **Q** `[Mano 8-27]` **and** `[Mano 8-31]`
> **Two signed numbers in 2's complement are compared by subtracting A − B. Show that the relative
> magnitude follows from S, Z and V. Then: A = 01000001, B = 10000100 — evaluate the difference and
> list the true branch conditions.**
>
> *Same two numbers as step 4. Guess whether the answer to "which is bigger" changes. Then read on.*

**It changes completely**, and that is the whole lesson. As **unsigned** these are 65 and 132, so
A < B. As **signed** they are **+65** and **−124**, so **A > B**. Same bits, opposite ordering.

**The relation table:**

| Relation | Condition |
|---|---|
| A > B | (S ⊕ V) = 0 **and** Z = 0 |
| A ≥ B | (S ⊕ V) = 0 |
| A < B | (S ⊕ V) = 1 |
| A ≤ B | (S ⊕ V) = 1 **or** Z = 1 |
| A = B | Z = 1 |
| A ≠ B | Z = 0 |

**★ Why S ⊕ V and not just S.** Your instinct says "if A − B is negative then A < B", i.e. read S. That
is right *only when the subtraction did not overflow*. If it **did** overflow, the sign bit is
corrupted (step 3) and reads backwards — so V = 1 must **flip** the interpretation. XOR is exactly
"flip S when V is set". This worked example is built to show it:

```
   0100 0001     (A = +65)
 + 0111 1100     (−B = +124, since B = −124)
 ──────────────
   1011 1101     = BD
```
Carry into bit 7 = 1, carry out = 0 → **V = 1**. S = **1** (the result looks negative). Z = **0**.

Naïvely reading S = 1 would say A < B — **wrong**, because +65 > −124. But
**S ⊕ V = 1 ⊕ 1 = 0 → A > B** ✓. The true difference is 65 − (−124) = **+189**, which overflows 8-bit
signed and is why the sign bit lied.

**True branch conditions:** A > B and A ≥ B and A ≠ B — i.e. the branches testing (S ⊕ V) = 0 with
Z = 0.

**`[Mano 8-29]`, the same pair *added* rather than subtracted:** A + B = `01000001 + 10000100` =
`11000101`. Unsigned that is 65 + 132 = 197; signed it is 65 + (−124) = **−59**. Carry into bit 7 = 0,
carry out = 0 → **V = 0**; C = 0, S = 1, Z = 0. No overflow either way, because the signs differ.

> ✓ **Check 5.** (a) Why is S alone insufficient for signed comparison? (b) What does V = 1 do to the
> interpretation of S? (c) The same bit patterns gave A < B unsigned and A > B signed — how?

---

### 6 · Conditional branch instructions

> **Q** `[Mano 8-28]`
> **Design a digital circuit with four inputs C, S, Z, V and 10 outputs, one for each of the branch
> conditions in Problems 8-26 and 8-27. Draw the logic diagram using two OR gates, one XOR gate and
> five inverters.**
>
> *You have both tables. Guess why only one XOR gate is needed for ten outputs.*

The ten conditions are the six unsigned rows plus the six signed rows, with **A = B** and **A ≠ B**
shared between them (both are just Z and Z′) — 6 + 6 − 2 = **10**.

| Output | Expression |
|---|---|
| A > B (unsigned) | C′Z′ |
| A ≥ B (unsigned) | C′ |
| A < B (unsigned) | C |
| A ≤ B (unsigned) | C + Z |
| A > B (signed) | (S ⊕ V)′ Z′ |
| A ≥ B (signed) | (S ⊕ V)′ |
| A < B (signed) | S ⊕ V |
| A ≤ B (signed) | (S ⊕ V) + Z |
| A = B | Z |
| A ≠ B | Z′ |

**Why one XOR suffices:** S ⊕ V is computed **once** and fanned out to all four signed outputs;
everything else is an inversion or a two-input OR. Two ORs (`C + Z` and `(S⊕V) + Z`), five inverters
(C′, Z′, (S⊕V)′, and the two used inside the AND-like terms), one XOR. **Sharing the common
subexpression is the minimisation**, exactly as in file 08.

The corresponding instructions in a real ISA: **BZ / BNZ** (Z), **BC / BNC** (C), **BP** (S = 0),
**BM** (S = 1), **BV** (V = 1). High-level `if (a > b)` becomes *compare, then branch on the right
combination* — and **which** combination depends on whether the variables are signed.

> ✓ **Check 6.** (a) Why 10 outputs rather than 12? (b) Which subexpression is shared, and how many
> outputs use it? (c) `[Mano 8-21]` For the 16-bit value 1001101011001101, what operation clears the
> first eight bits? sets the last eight? complements the middle eight?

---

### 7 · Subroutine call and return

> **Q** *(the compare/contrast that ties U2 and U3 together)*
> **A CALL must save a return address and jump. Name the three historical places to save it, and say
> which permits recursion.**
>
> *You met one of them as BSA in file 07. Guess why it cannot recurse.*

| Where the return address goes | Consequence |
|---|---|
| **a fixed memory location** (U2's **BSA**) | simple; **not reentrant, no recursion** |
| **a processor register** | fast; only one level deep unless saved |
| **a stack** | **reentrant and recursive** — the modern answer |

**Mechanism.** With a stack:

```
 CALL:  SP ← SP − 1;  M[SP] ← PC;  PC ← EA
 RET :  PC ← M[SP];   SP ← SP + 1
```

Because each call pushes a **new frame**, a subroutine may call itself, or be called from an
interrupt while already running. U2's BSA overwrites **the single saved word at EA**, so a second (or
recursive) call destroys the first return address and the program can never get back.

★ **You have now seen this same limitation three times, at three levels**, which is why it is worth
naming: U2's BSA stores one return address at a fixed word; U3's microprogram sequencer has a
**single SBR**, so a microsubroutine cannot call another (file 09, step 8); and real machines solved
it at both levels with a **stack**. Same problem, same fix, different scale.

> ✓ **Check 7.** (a) Write the stack CALL and RET in RTL. (b) Why exactly does BSA break under
> recursion? (c) What is the microprogram-level analogue of BSA's limitation?

---

### 8 · Interrupts

> **Q** *(the machine-level view of file 07, step 9)*
> **Name the three classes of interrupt and say what distinguishes an interrupt from a subroutine
> call.**
>
> *Guess the distinguishing word. It is one word.*

**Asynchronous.** A subroutine call is *in* the program — the programmer wrote it, and it happens at a
point they chose. An interrupt is initiated by **something other than the running program**, at a
point the program never chose.

| Class | Source | Examples |
|---|---|---|
| **External** | outside the CPU | I/O device ready, timer, power failure |
| **Internal (trap)** | the instruction being executed | overflow, divide by zero, invalid opcode, stack overflow |
| **Software** | a deliberate instruction | supervisor call / system call — a program *asking* for a service |

**What must be saved: the program state** — PC, the status bits, and (depending on the machine) the
registers. Saving the status bits matters more than students expect: an interrupt that ran an ADD
would otherwise destroy the C/S/Z/V the interrupted program was about to branch on.

Internal interrupts are **synchronous** in the sense that re-running the same program with the same
data reproduces them; external ones are not.

> ✓ **Check 8.** (a) What single word distinguishes an interrupt from a subroutine call?
> (b) Why must the status bits be saved and not just PC? (c) Which class is a divide-by-zero?

---

## Exam form

### The four status bits

```
 C  carry out of the MSB                  → UNSIGNED overflow
 S  MSB of the result                     → sign
 Z  all result bits zero (n-input NOR)    → equality
 V  Cₙ ⊕ Cₙ₋₁                             → SIGNED overflow
```

Logic operations (AND, OR, XOR, NOT) **clear C and V**.

### The two comparison tables

| Relation | Unsigned | Signed |
|---|---|---|
| A > B | C′Z′ | (S⊕V)′Z′ |
| A ≥ B | C′ | (S⊕V)′ |
| A < B | C | S⊕V |
| A ≤ B | C + Z | (S⊕V) + Z |
| A = B | Z | Z |
| A ≠ B | Z′ | Z′ |

**Unsigned uses C. Signed uses S ⊕ V.** If you remember one sentence from this file, that is it.

### How to answer a status-bit question

1. Write both operands in binary, 8 bits.
2. If subtracting, convert to `A + B′ + 1`.
3. Add **column by column, recording the carry into and out of bit 7**.
4. C = carry out · S = bit 7 of the result · Z = is it all zeros · **V = the two carries XOR-ed**.
5. Interpret twice — once unsigned, once signed — and say which you mean.

---

## Attempt

1. `[Mano 8-25]` all five parts, four flags each — the highest-yield drill here.
2. `[Mano 8-23]` all four parts including both shifts.
3. `[Mano 8-29]`, `[8-30]`, `[8-31]` — the same bit pair three ways. Doing all three together is what
   makes the signed/unsigned split stick.
4. `[Mano 8-26]`, `[8-27]` — derive both tables rather than reciting them.
5. `[Mano 8-20]`, `[8-21]` — the logic-operation drills (they are file 04, step 6 again).
6. `[Mano 8-28]` the ten-output circuit.
7. `[Mano 8-22]` the eight shift instructions applied to 01111011 with carry = 1.

---

## Traps

| Trap | Correction |
|---|---|
| Using C for signed comparison | C is **unsigned**. Signed uses **S ⊕ V** |
| Reading S alone after a subtraction | If V = 1 the sign bit is corrupted and reads backwards |
| Forgetting that logic operations clear C and V | AND, OR, XOR, NOT always do |
| Treating the carry out as the borrow | They are **complements**. State the convention you are using |
| Computing V from the result alone | V needs the **two carries**, not just the output bits |
| Thinking BSA is just an old CALL | It cannot recurse — the single saved word is overwritten |
| Saving only PC on an interrupt | The **status bits** must be saved too, or the interrupted branch breaks |
| Treating Z as a wire | It is an n-input NOR across the whole result |

---

## Self-test

1. Define all four status bits, and say which reports unsigned and which signed overflow.
2. R = 5A, add A6. Give C, S, Z, V.
3. A and B are compared as unsigned by A − B; C (borrow) = 0 and Z = 0. Which relation holds?
4. The same flags, but the numbers are signed and V = 1, S = 0. Which relation holds?
5. Why can a stack-based CALL recurse when BSA cannot?
6. Which class of interrupt is an invalid opcode?
7. What is the one-sentence rule for choosing between C and S ⊕ V?

---
---

## Answers

**Check 1.** (a) **PC**. (b) It **discards** it — only the status bits are kept. (c) Because any
instruction in between could overwrite the flags with its own result.

**Check 2.** (a) **C and V**. (b) An **n-input NOR** across every bit of the result. (c)
AND = `1000 1000`, OR = `1011 1110`, XOR = `0011 0110`.

**Check 3.** (a) The magnitudes partly cancel, so the result is no larger than the bigger operand and
must fit. (b) The carry **into** the sign position and the carry **out** of it: V = Cₙ ⊕ Cₙ₋₁.
(c) **C**.

**Check 4.** (a) A − B is computed as A + B′ + 1, which produces a carry out exactly when A ≥ B; the
borrow convention inverts that carry, so borrow = 1 exactly when A < B. (b) **Z**. (c) **0** — which
is why the borrow is 1.

**Check 5.** (a) Because a subtraction that overflows corrupts the sign bit, so S reports the opposite
of the truth. (b) It **flips** it — which is precisely what XOR-ing S with V does. (c) `10000100` is
132 read as unsigned and −124 read as 2's complement; the bits are identical, the interpretation is
not, and the flags are chosen to match the interpretation.

**Check 6.** (a) Because **A = B** and **A ≠ B** are the same in both tables (just Z and Z′), so
6 + 6 − 2 = 10. (b) **S ⊕ V**, used by the four signed outputs. (c) Clear the first eight:
**AND with `0000 0000 1111 1111`**. Set the last eight: **OR with `0000 0000 1111 1111`**. Complement
the middle eight: **XOR with `0000 1111 1111 0000`**.

**Check 7.** (a) `CALL: SP ← SP − 1; M[SP] ← PC; PC ← EA` · `RET: PC ← M[SP]; SP ← SP + 1`.
(b) Because BSA writes the return address into **one fixed word (EA)**; a second call writes over the
first, so the first return address is lost. (c) The microprogram sequencer's **single SBR** — a
microsubroutine cannot call another one.

**Check 8.** (a) **Asynchronous.** (b) Because the interrupt service routine will run ALU operations
of its own and overwrite C, S, Z and V — the interrupted program may have been about to branch on
them. (c) **Internal** (a trap).

**Self-test 1.** C = carry out of the MSB (**unsigned** overflow) · S = MSB of the result (sign) ·
Z = result is all zeros · V = Cₙ ⊕ Cₙ₋₁ (**signed** overflow).

**Self-test 2.** 5A = `0101 1010`, A6 = `1010 0110`.
```
   0101 1010
 + 1010 0110
 ──────────────
 1 0000 0000     = 00, carry out 1
```
Carry into bit 7 = 1, carry out = 1. **C = 1 · S = 0 · Z = 1 · V = 0.** (90 + 166 = 256 → wraps to 0.)

**Self-test 3.** C = 0 and Z = 0 → **A > B**.

**Self-test 4.** S ⊕ V = 0 ⊕ 1 = 1, and Z = 0 → **A < B**. (Note S = 0 alone would have said A > B —
V flips it.)

**Self-test 5.** Because each call **pushes a new frame** onto the stack, so an inner call cannot
overwrite an outer call's return address; BSA has only one saved word per subroutine.

**Self-test 6.** **Internal** — a trap.

**Self-test 7.** Use **C** when the operands are unsigned and **S ⊕ V** when they are signed —
identical bits, different ordering.

---

## What to do next

U3 is complete, and so is everything except U4. File 11 is **pipelining**: five of Assignment 2's
questions, all of them Mano chapter 9, and the unit the professor unusually puts *before* the
mid-term. It needs only file 03 — you can go there directly if you want a change of gear.
