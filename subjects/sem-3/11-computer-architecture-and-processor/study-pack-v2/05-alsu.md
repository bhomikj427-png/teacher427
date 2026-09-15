# 05 — The Arithmetic Logic Shift Unit (ALSU)

**Assignment 1: Q17 (8 + 8 = 16 marks) · U1 (L8) · the professor's own deck-closing question**

---

## ⚠ Two different tables — use the right one

The Unit-1 deck has **two** function tables that look alike:

| Deck page | Table | `S₁S₀Cᵢₙ` for **add with carry** |
|---|---|---|
| p. 25 | standalone **arithmetic circuit** (MUX inputs B, B′, 0, 1) | `0 0 1` |
| **p. 32** | **ALSU** (= Mano Table 4-8) | `S₃S₂S₁S₀Cᵢₙ = 0 0 0 1 1` |

**For the ALSU question, use p. 32**, and draw the arithmetic MUX wired **0 → 0, 1 → B, 2 → B′, 3 → 1**
so your circuit agrees with your table. v1 of this pack mixed the two; corrected 2026-09-15.

---

## Map

```
               ┌── arithmetic stage (FA + 4×1 MUX)  ── Dᵢ ──┐
   Aᵢ, Bᵢ ─────┤                                            │
               └── logic stage (4 gates + 4×1 MUX)  ── Eᵢ ──┼──► output 4×1 MUX ──► Fᵢ
   Aᵢ₊₁ ─────────────────────── (shift right) ──────────────┤     select S₃S₂
   Aᵢ₋₁ ─────────────────────── (shift left)  ──────────────┘
```

One stage, replicated 4 times. **S₃S₂ picks the block; S₁S₀ (+ Cᵢₙ) picks the operation inside it.**

---

## Attempt

Design a 4-bit arithmetic-logic-shift circuit. Explain its working for:
**(i)** transfer A **(ii)** add with carry **(iii)** XOR **(iv)** shift right A.

Draw first. Then write the select code for each of the four functions and what path the data takes.

---

## Learn

### One stage (bit i)

```
                         S₁ S₀ (common)
                           │  │
             ┌─────────────┴──┴──────────┐
     "0" ───►│ 0                         │
     Bᵢ ────►│ 1   4×1 MUX    Yᵢ         │
     Bᵢ′────►│ 2  ─────────►┌──────┐     │
     "1" ───►│ 3            │  FA  │──── Dᵢ ───────────────┐
             └──────────────│      │                       │
     Aᵢ ───────────────────►│ X    │                       │
     Cᵢ ───────────────────►│ Cin  │──► Cᵢ₊₁               │
                            └──────┘                       │
                                                           │    ┌─────────────┐
     Aᵢ ─┬─[AND]◄─ Bᵢ ──► 0 ┐                              ├──► │ 0           │
         ├─[OR ]◄─ Bᵢ ──► 1 │  4×1 MUX                     │    │             │
         ├─[XOR]◄─ Bᵢ ──► 2 ├─────────── Eᵢ ───────────────┼──► │ 1  4×1 MUX  │──► Fᵢ
         └─[NOT]──────► 3 ┘   (S₁ S₀)                      │    │             │
                                                           │    │             │
     Aᵢ₊₁ (shr) ───────────────────────────────────────────┼──► │ 2           │
     Aᵢ₋₁ (shl) ───────────────────────────────────────────┴──► │ 3           │
                                                                └──────┬──────┘
                                                                    S₃ S₂
```

### The 4-bit unit

Four stages side by side. **Common S₃S₂S₁S₀.** Carry C₀ = Cᵢₙ enters stage 0 and ripples C₁ → C₂ →
C₃ → C₄ = Cₒᵤₜ. End conditions for shifts: stage 3's shift-right input is serial input **Iᵣ**; stage
0's shift-left input is serial input **Iₗ**.

### Function table (deck p. 32 = Mano Table 4-8)

| S₃ | S₂ | S₁ | S₀ | Cᵢₙ | Operation | Function |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | F = A | **transfer A** |
| 0 | 0 | 0 | 0 | 1 | F = A + 1 | increment A |
| 0 | 0 | 0 | 1 | 0 | F = A + B | addition |
| 0 | 0 | 0 | 1 | 1 | F = A + B + 1 | **add with carry** |
| 0 | 0 | 1 | 0 | 0 | F = A + B′ | subtract with borrow |
| 0 | 0 | 1 | 0 | 1 | F = A + B′ + 1 | subtraction |
| 0 | 0 | 1 | 1 | 0 | F = A − 1 | decrement A |
| 0 | 0 | 1 | 1 | 1 | F = A | transfer A |
| 0 | 1 | 0 | 0 | × | F = A ∧ B | AND |
| 0 | 1 | 0 | 1 | × | F = A ∨ B | OR |
| 0 | 1 | 1 | 0 | × | F = A ⊕ B | **XOR** |
| 0 | 1 | 1 | 1 | × | F = A′ | complement A |
| 1 | 0 | × | × | × | F = shr A | **shift right A into F** |
| 1 | 1 | × | × | × | F = shl A | shift left A into F |

**Derive the rows, don't memorize them:** the arithmetic stage computes D = A + Y + Cᵢₙ.

| S₁S₀ | Y | Cᵢₙ = 0 | Cᵢₙ = 1 |
|---|---|---|---|
| 00 | 0 | A | A + 1 |
| 01 | B | A + B | A + B + 1 |
| 10 | B′ | A + B′ | A + B′ + 1 = A − B |
| 11 | 1111 | A + 1111 = A − 1 | A + 1111 + 1 = A |

**Count:** 8 arithmetic + 4 logic + 1 + 1 = **14 operations** from 4 select lines + Cᵢₙ.

---

## Worked (A1 Q17 — full answer)

**(a) Design (8 marks):** one-stage diagram · statement that it is replicated 4 times with common
selects and rippling carry · end conditions Iᵣ, Iₗ · the function table.

**(b) Working of the four functions (8 marks),** with A = 1010, B = 0110, Iᵣ = 0 as illustration:

| Function | Code S₃S₂S₁S₀Cᵢₙ | Path | F |
|---|---|---|---|
| **(i) Transfer A** | 0 0 0 0 0 | S₃S₂ = 00 passes the arithmetic output. S₁S₀ = 00 makes every MUX output Yᵢ = 0; Cᵢₙ = 0. Each FA computes Aᵢ + 0 + carry 0 → **D = A** | **1010** |
| **(ii) Add with carry** | 0 0 0 1 1 | S₃S₂ = 00: arithmetic. S₁S₀ = 01 → Yᵢ = Bᵢ. Cᵢₙ = 1 enters stage 0 → **D = A + B + 1** | 1010 + 0110 + 1 = 1 0001 → **0001**, Cₒᵤₜ = 1 |
| **(iii) XOR** | 0 1 1 0 × | S₃S₂ = 01 passes the logic output. S₁S₀ = 10 selects the XOR gate in every stage → **F = A ⊕ B**. Cᵢₙ unused | **1100** |
| **(iv) Shift right A** | 1 0 × × × | S₃S₂ = 10 passes input 2 = Aᵢ₊₁ into Fᵢ: F₀ ← A₁, F₁ ← A₂, F₂ ← A₃, F₃ ← Iᵣ. S₁S₀, Cᵢₙ unused | **0101** |

**The explanation sentence that earns the working marks:**

> All three blocks compute their results simultaneously on every input. The output multiplexer,
> driven by S₃S₂, lets exactly one block's result reach F; S₁S₀ and Cᵢₙ choose the operation within
> the arithmetic or logic block. Unselected results are computed and discarded, so the delay is set by
> the slowest path — the ripple carry — regardless of the operation chosen.

---

## Traps

| Trap | Correction |
|---|---|
| Using deck p. 25's order (`001` = add with carry) | ALSU table: `00011`. And draw the MUX as 0, B, B′, 1 |
| Drawing MUX inputs B, B′, 0, 1 with the p. 32 table | Circuit and table then disagree — the examiner can see it |
| Shift right: F₃ ← A₂ | Right shift takes from the **higher** neighbour: Fᵢ ← Aᵢ₊₁, F₃ ← Iᵣ |
| "The ALSU decides, then computes" | It computes all, then selects |
| Showing only one stage | State the replication ×4, common selects, carry chain, and both end conditions |
| Leaving Cᵢₙ undefined for logic/shift rows | Write × — it is ignored there |

---

## Self-test

1. Give the code and F for **decrement A** with A = 0000. What is Cₒᵤₜ?
2. Code for **subtraction**; compute F for A = 0110, B = 1001 and interpret it.
3. Why does `0011 1` give transfer A? Show the addition for A = 0101.
4. Shift left A = 1001 with Iₗ = 1. Code and F.
5. A different ALSU uses only 3 select lines: S₂ picks arithmetic vs logic, no shifts, S₁S₀ + Cᵢₙ as
   above. How many operations?

---
---

## Answers

**Attempt.** See Worked.

**Self-test 1.** `0 0 1 1 0` → F = 0000 + 1111 = **1111** (−1 in 2's complement), Cₒᵤₜ = 0.

**Self-test 2.** `0 0 1 0 1` → F = 0110 + 0110 + 1 = **1101**, Cₒᵤₜ = 0 → A < B unsigned; 1101 = −3
signed = 6 − 9 ✓.

**Self-test 3.** Y = 1111 and Cᵢₙ = 1: 0101 + 1111 + 1 = 1 0101 → F = **0101** = A (carry out 1
discarded). Adding 1111 subtracts 1; the +1 restores it.

**Self-test 4.** `1 1 × × ×` → F₃ ← A₂ = 0, F₂ ← A₁ = 0, F₁ ← A₀ = 1, F₀ ← Iₗ = 1 → **0011**.

**Self-test 5.** 8 + 4 = **12**.
