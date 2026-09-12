# 08 — Program Control: Status Bits, Conditional Branches, Subroutines

**U3, lecture L15 · CO2.** This is Mano ch. 8 §8-7, not ch. 7 — the *machine-instruction*-level
counterpart of the microinstruction branching in file 07. Short file, cheap marks, and one derivation
(**V = Cₙ ⊕ Cₙ₋₁**) that recurs in the 8086 unit later in the year.

---

## Map

```
   PROGRAM CONTROL = instructions that change PC
        |
        +-- branch | jump | skip | call | return | compare | test
        |
        v
   they test STATUS BITS set by the last ALU operation
        |
        +-- C  carry     -> carry out of the MSB        -> UNSIGNED overflow
        +-- S  sign      -> MSB of the result
        +-- Z  zero      -> all result bits are 0
        +-- V  overflow  -> Cₙ ⊕ Cₙ₋₁                     -> SIGNED overflow
        |
        v
   SUBROUTINE CALL must (i) save the return address (ii) jump
        |
        +-- fixed memory location (BSA)   -> no recursion, not reentrant
        +-- a processor register          -> one level deep
        +-- A STACK                       -> reentrant and recursive  <- the modern answer
        |
        v
   INTERRUPT = the same save-and-jump, but ASYNCHRONOUS
```

---

## Attempt first

1. Name the four status bits and say what sets each.
2. `0x7F + 0x01` in 8 bits: which flags are set? Now `0xFF + 0x01`: which flags are set?
3. Derive the overflow condition `V = Cₙ ⊕ Cₙ₋₁` — do not just state it.
4. To compare two **unsigned** numbers you test one flag; for **signed** numbers you need a
   combination. Which, and why?
5. The Basic Computer's BSA saves the return address in a fixed memory word. Write a two-line program
   sketch that breaks because of this.
6. Give the stack-based CALL and RET as register transfers.
7. Name three ways an interrupt differs from a subroutine call.

---

## Method

### Program control instructions

Instructions that **change the value of PC**, and so alter the sequence of execution:
**branch · jump · skip · call · return · compare · test.**

Everything else in a program runs straight through; these are the only instructions that make control
flow a *graph* rather than a line.

### The status bits

A status register holds bits set by the ALU's last operation. Defined for an n-bit result, with Cₙ
the carry **out of** the sign position and Cₙ₋₁ the carry **into** it:

| Bit | Name | Set when |
|---|---|---|
| **C** | carry | there is a carry-out of the MSB |
| **S** | sign | the MSB of the result is 1 |
| **Z** | zero | all result bits are 0 |
| **V** | overflow | **Cₙ ⊕ Cₙ₋₁** — the carry into the sign position differs from the carry out of it |

**★ Why V is that XOR — the derivation, which is the examinable part.**

Signed overflow means *the true result did not fit*. In 2's complement, the sign bit is a normal bit
position that happens to carry the sign's weight. So:

- If the carry **into** the sign position equals the carry **out** of it, the sign bit came out
  consistent with the magnitude bits below it — the result is correct.
- If they **differ**, the magnitude bits have carried into the sign position and corrupted it (or the
  sign has carried out and been lost). The sign of the answer is then wrong.

`Cₙ ⊕ Cₙ₋₁` is exactly "these two differ". Hence V.

**★ C and V are independent — this is the trap.** Two 8-bit examples make the point, and they are
worth memorizing *as a pair*:

```
   0x7F + 0x01  =  0111 1111 + 0000 0001  =  1000 0000
        signed:   +127 + 1 = +128, which does not fit in [-128, +127]   -> V = 1
        unsigned:  127 + 1 =  128, which fits fine in [0, 255]          -> C = 0
        also S = 1 (MSB set), Z = 0

   0xFF + 0x01  =  1111 1111 + 0000 0001  = 1 0000 0000
        unsigned:  255 + 1 = 256, does not fit in [0, 255]              -> C = 1
        signed:     -1 + 1 = 0, entirely correct                        -> V = 0
        also S = 0, Z = 1
```

> **C is for unsigned overflow. V is for signed overflow. The hardware computes both, every time, and
> the *programmer* decides which one is meaningful by choosing which branch instruction to use.**

That last sentence is the whole idea: the ALU does not know whether your bits are signed.

### Conditional branch instructions

| Instruction | Branches when |
|---|---|
| **BZ** | Z = 1 (result was zero) |
| **BNZ** | Z = 0 |
| **BC** | C = 1 |
| **BNC** | C = 0 |
| **BP** | S = 0 (result positive) |
| **BM** | S = 1 (result minus) |
| **BV** | V = 1 (overflow) |

**Comparison is subtraction that throws away the difference and keeps the flags.**

- For **unsigned** comparison, the relevant bit is **C** (the borrow out of the subtraction).
- For **signed** comparison, you need **S together with V**: the true sign of A − B is `S ⊕ V`,
  because V = 1 means the computed sign is inverted from the true one.

### Subroutine call and return

A CALL must do two things: **(i) save the return address, (ii) jump to the subroutine.** The only
design question is *where the return address goes*, and history offers three answers:

| Where the return address goes | Consequence |
|---|---|
| a **fixed memory location** (BSA — U2's way) | simple; **not reentrant, no recursion** |
| a **processor register** | fast; only **one level deep** unless the program saves it |
| **a stack** | **reentrant and recursive** — the modern answer |

**The stack mechanism, as register transfers:**

```
   CALL:   SP ← SP − 1
           M[SP] ← PC
           PC ← EA

   RET:    PC ← M[SP]
           SP ← SP + 1
```

**Why a stack permits recursion and BSA does not.** Each call **pushes a new frame**, so every
activation of the subroutine has its *own* return-address slot. BSA writes to a single fixed word at
EA, so a second call — recursive or merely nested through the same subroutine — **overwrites the
first return address**, and the first call can never return. That is the clean compare/contrast
answer, and it is why real machines abandoned BSA.

### Program interrupt

The machine-level view of the interrupt hardware in file 05. Three kinds:

| Kind | Source | Examples |
|---|---|---|
| **External** | a device outside the CPU | I/O device ready, timer, power fail |
| **Internal (trap)** | the executing instruction itself | overflow, divide by zero, invalid opcode, stack overflow |
| **Software** | a deliberate instruction | supervisor call / system call |

The CPU must save the **program state**: PC, the status bits, and — depending on the machine — the
registers.

**The one difference that matters:** an interrupt is **asynchronous** — initiated by something other
than the running program, at a moment the program did not choose. A subroutine call is written into
the program by the programmer. Everything else about the two (save the return address, jump, restore)
is the same mechanism, which is exactly why U2's interrupt cycle is *literally* a hardware BSA.

---

## Worked — flags for a given operation (inferred form; definitions from Mano ch. 8)

> **An 8-bit ALU computes `A − B` with A = 0x50 and B = 0x70. Give C, S, Z and V, then say what a
> signed comparison and an unsigned comparison would each conclude.**

**Step 1 — do the subtraction as the hardware does it: A + B′ + 1.**

```
   A        = 0101 0000   (0x50 = +80)
   B        = 0111 0000   (0x70 = +112)
   B'       = 1000 1111
   A + B' + 1:
              0101 0000
            + 1000 1111
            + 0000 0001
            -----------
              1110 0000    result = 0xE0
```

**Step 2 — read the carries.** Adding column by column, no carry ever leaves the MSB:
**Cₙ = 0**. The carry into the sign position is also **Cₙ₋₁ = 0** (bit 6 produces no carry: 1 + 0 + 0).

**Step 3 — the flags.**

| Flag | Value | Why |
|---|---|---|
| **C** | **0** | no carry out. In subtraction, C = 0 means a **borrow occurred** — A < B as unsigned |
| **S** | **1** | result MSB = 1 |
| **Z** | **0** | result is not zero |
| **V** | **Cₙ ⊕ Cₙ₋₁ = 0 ⊕ 0 = 0** | no signed overflow |

**Step 4 — the two conclusions.**

- **Unsigned:** C = 0 (borrow) → **A < B**. Check: 80 < 112. ✓
- **Signed:** the true sign is `S ⊕ V = 1 ⊕ 0 = 1` → negative → **A < B**. Check: +80 < +112. ✓

**Here both agree** — because both operands were small positives. The point of the question is the
*method*: read C for unsigned, read `S ⊕ V` for signed, and never assume they agree.
`0x50 − 0xF0` is the case where they disagree: unsigned says 80 < 240, signed says +80 > −16.

---

## Worked — why BSA cannot recurse (inferred form; the contrast is Mano's)

> **A subroutine `FACT` computes a factorial by calling itself. Explain precisely what goes wrong on
> the Basic Computer, and what a stack changes.**

**The BSA layout.** `BSA FACT` stores the return address in **M[FACT]** and jumps to **FACT + 1**.

```
   main:   BSA FACT       ; M[FACT] <- return address in main, say 100
   ...
   FACT:   ---            ; the return-address slot
   FACT+1: ...            ; body
           BSA FACT       ; RECURSIVE CALL -- overwrites M[FACT] with, say, FACT+5
   ...
           BUN FACT (I=1) ; return: PC <- M[FACT]
```

**What goes wrong, stated exactly:** the recursive `BSA FACT` writes the *inner* return address into
**the same word M[FACT]** that already held the *outer* one. The outer return address is destroyed.
When the innermost call returns, it jumps correctly; when the next one tries to return, M[FACT] still
holds the inner address, so control jumps back into the middle of the subroutine — an **infinite
loop**.

**Why the same failure hits non-recursive code too:** any two activations of the subroutine that are
live at once break it. A subroutine that BSA can safely call is one that is never re-entered before
it returns — which is the definition of **not reentrant**. Interrupts make this concrete: if an
interrupt service routine calls a subroutine that the interrupted program was already inside, the
same overwrite occurs.

**What a stack changes.** `SP ← SP − 1; M[SP] ← PC; PC ← EA` puts each return address at a **different
address**, because SP moves. Depth is limited only by memory. Returns pop in exactly the reverse order
of the calls — which is what "last in, first out" means and why the structure fits the problem.

---

## Traps

| # | Trap | The correction |
|---|---|---|
| M11 | "Carry and overflow are the same thing" | **C = unsigned** overflow; **V = signed** overflow. `0x7F + 0x01` sets V and not C; `0xFF + 0x01` sets C and not V |
| — | Stating `V = Cₙ ⊕ Cₙ₋₁` without the reason | The mark is in "the carry into the sign differs from the carry out, so the sign bit has been corrupted" |
| — | Using C to compare signed numbers | Signed comparison needs `S ⊕ V`. C is the unsigned answer |
| — | "The ALU knows whether the numbers are signed" | It does not. It computes **both** C and V every time; the *branch instruction you choose* decides which interpretation you meant |
| — | Saying BSA "doesn't support recursion" and stopping | The mark is the mechanism: the **fixed** return-address word is overwritten by the second call |
| — | Treating an interrupt as just a subroutine call | It is **asynchronous**, it must save the **status bits** as well as PC, and the hardware — not the program — initiates it |
| — | Forgetting the three interrupt kinds | External · internal (trap) · software (supervisor call) |

---

## Self-test

1. An 8-bit addition produces `1000 0000` with Cₙ = 1 and Cₙ₋₁ = 1. Give C, S, Z, V, and say whether
   a signed program should worry.
2. Compute `0x50 − 0xF0` in 8 bits. Give all four flags, then state the unsigned and the signed
   conclusion and explain why they differ.
3. Why is the zero flag Z usually computed as the NOR of all result bits rather than by a comparison?
4. Write, as register transfers, a CALL and a RET that use a stack that **grows upward** (SP
   increments on push). State one reason a real machine might prefer a downward-growing stack.
5. Give three properties a subroutine-linkage mechanism must have to support recursion, and say which
   of the three storage choices provides all three.
6. A trap and an external interrupt both vector the CPU to a service routine. Give two ways they
   differ.
7. On the Basic Computer, the interrupt cycle stores the return address in M[0] and clears IEN. What
   goes wrong if IEN were *not* cleared? Relate your answer to the BSA recursion problem.
8. Explain why "compare" instructions exist at all, given that a subtract instruction sets exactly the
   same flags.

---

## Answers

**1.** **C = Cₙ = 1 · S = 1 · Z = 0 · V = Cₙ ⊕ Cₙ₋₁ = 1 ⊕ 1 = 0.**

A **signed** program should not worry — V = 0 means the signed result is correct. A concrete case with
these exact carries is `0xC0 + 0xC0`: −64 + (−64) = −128 = `1000 0000`, which is representable in 8-bit
2's complement.

An **unsigned** program should worry — C = 1 means the true sum exceeded 255 (192 + 192 = 384).

*Same bits, same flags, opposite verdicts.* Contrast `0x80 + 0x80`, where Cₙ = 1 but Cₙ₋₁ = 0, giving
V = 1: −128 + (−128) = −256 is **not** representable.

**2.**
```
   A  = 0101 0000  (0x50 = 80 unsigned, +80 signed)
   B  = 1111 0000  (0xF0 = 240 unsigned, -16 signed)
   B' = 0000 1111
   A + B' + 1 = 0101 0000 + 0000 1111 + 1 = 0110 0000  (0x60)
```
Carries: the addition produces no carry out of the MSB → **Cₙ = 0**; the carry into the sign position
is also **0**.
**C = 0 · S = 0 · Z = 0 · V = 0 ⊕ 0 = 0.**
**Unsigned conclusion:** C = 0 → borrow → **A < B** (80 < 240). ✓
**Signed conclusion:** true sign = `S ⊕ V` = 0 → result positive → **A > B** (+80 > −16). ✓
They differ because the **same bit pattern** `0xF0` means 240 to one interpretation and −16 to the
other. Nothing in the hardware distinguishes them; only the branch instruction the programmer chooses
does.

**3.** Because Z must be 1 exactly when **every** result bit is 0, and a NOR of all n bits is precisely
that function — one gate level, no comparison, no extra operand. Building it as "compare the result
with zero" would require a second n-bit comparison after every ALU operation, doubling the work to
compute something the result bits already express.

**4.** Upward-growing stack:
```
   CALL:   M[SP] ← PC,  SP ← SP + 1,  PC ← EA
   RET:    SP ← SP − 1,  PC ← M[SP]
```
**Why downward is common:** placing the stack at the top of memory and the program/heap at the bottom
lets the two grow **toward** each other, so neither needs a fixed size limit — the memory between them
is shared until they collide. With both growing upward from low addresses you must fix a boundary in
advance.

**5.** (i) Each activation must have its **own** storage for the return address; (ii) storage must be
allocated and released in **last-in-first-out** order, matching call/return nesting; (iii) the depth
must not be fixed by the hardware to one.
**A stack provides all three.** A fixed memory location fails (i). A single processor register fails
(i) and (iii) — it holds one return address, so the first nested call destroys the outer one unless
the program manually saves it (which is to say, unless the program builds a stack in software).

**6.** Any two of: a **trap is synchronous** — caused by the instruction currently executing (overflow,
divide-by-zero, invalid opcode) and therefore reproducible; an **external interrupt is asynchronous** —
caused by a device, at an arbitrary moment. A trap usually cannot be masked (you cannot ignore a
divide-by-zero and continue meaningfully); external interrupts are **maskable** via IEN. A trap is
normally an error or a service request from the program itself; an external interrupt is a
notification from outside.

**7.** If IEN stayed set, a second interrupt could be recognized **while the first service routine is
running**. The interrupt cycle would then write the new return address into **M[0]**, overwriting the
first one — and the original program could never be resumed. **This is precisely the BSA recursion
failure**: a single fixed return-address word, re-entered before it was consumed. Clearing IEN is the
cheap fix (forbid re-entry); the general fix, as with subroutines, is a **stack**.

**8.** Because a subtract **writes its difference into a register**, destroying whatever was there,
whereas a comparison is wanted precisely when you need the *flags* and want to **keep both operands
intact** — typically to test the same value repeatedly against several bounds. `CMP` performs the
subtraction internally and discards the result, keeping only the status bits. It is the same ALU
operation with the write-back suppressed.
