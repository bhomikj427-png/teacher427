# 05 — The Arithmetic Logic Shift Unit (ALSU)

**Assignment 1: Q17 · 16 of 200 marks · U1 (L8) · needs 02, 03, 04**

★ **The professor's own deck ends on this question.** His last U1 slide reads *"Design a 4-bit ALU
that may perform the following operations. Explain its working in detail."* Treat it as the single
most likely U1 exam item.

> ⚠ **This file contains a correction that cost real marks elsewhere.** There are **two different
> function tables** in circulation for this circuit, both correct for their own wiring, and the
> professor examines **one** of them. Step 6 is about which. An earlier version of this pack had it
> wrong; the KB was corrected on 2026-09-15.

---

## Map

```
   [1] Arithmetic stage  ──┐
       FA + 4×1 MUX on Y   │
                           │      S₃S₂ picks the block
   [2] Logic stage  ───────┼────► [4] One ALSU stage ────► [5] Function table
       AND OR XOR NOT      │           (×n for n bits)          14 operations
                           │                                        │
   [3] Shifter  ───────────┘                                        ▼
       shr / shl                                          [6] ⚠ Which table?
                                                              the two orderings
```

---

## The question this file answers

`[A1 Q17 · 8 + 8 = 16 marks]` **Design a 4-bit arithmetic-logic-shift circuit. Explain the working of
the circuit for the following functions: i) Transfer A ii) Add with carry iii) XOR iv) Shift right A**

Note the split: **8 marks for the design, 8 for explaining those four named functions.** Most answers
draw the circuit and stop, and lose half the marks.

Mano's follow-ups: **4-15** (design an arithmetic circuit from a truth table), **4-16** (all 16 logic
functions), **4-17** (a four-function logic circuit), **4-22**.

---

## Build

### 1 · The arithmetic stage

> **Q** `[Mano 4-15 · not yet asked]`
> **Design an arithmetic circuit with one selection variable S and two n-bit data inputs A and B,
> generating: S=0,Cᵢₙ=0 → D = A + B · S=0,Cᵢₙ=1 → D = A + 1 · S=1,Cᵢₙ=0 → D = A − 1 ·
> S=1,Cᵢₙ=1 → D = A + B′ + 1. Draw the logic diagram for the first two stages.**
>
> *File 04 built an adder-subtractor with one XOR per bit and got two operations. Guess what you'd
> put in place of that XOR to get eight. Then read on.*

Replace the XOR with a **4-to-1 multiplexer** (file 02, step 3). One full adder per bit; the adder's
**X input is always Aᵢ**; its **Y input comes from the MUX**, which chooses among four things; and
**Cᵢₙ** is a third control.

```
         Bᵢ ──┬──────────────►│0 │
              └──►o──────────►│1 │  4×1
          0 ─────────────────►│2 │  MUX ──► Yᵢ ──┐
          1 ─────────────────►│3 │              │
                               ▲▲               ▼
                            S₁ S₀          ┌─────────┐
                                    Aᵢ ───►│ full    │──► Dᵢ
                                    Cᵢ ───►│ adder   │──► Cᵢ₊₁
                                           └─────────┘
```

Four MUX inputs × two values of Cᵢₙ = **8 combinations**, and because `A + 1111 = A − 1` in 2's
complement (file 04, step 4), you get increment, decrement, add, subtract and transfer out of one
adder. **No separate incrementer, no separate subtractor.**

> ✓ **Check 1.** (a) Why is the adder's X input hard-wired to A rather than multiplexed too?
> (b) How does feeding the MUX a constant 1 (all bits) produce a **decrement**?
> (c) How many distinct operations do 3 control bits give, and how many combinations?

---

### 2 · The logic stage

> **Q** `[Mano 4-17 · not yet asked]`
> **Design a digital circuit that performs the four logic operations exclusive-OR, exclusive-NOR, NOR
> and NAND. Use two selection variables. Show the logic diagram of one typical stage.**
>
> *Guess how many gates one stage needs. Then read on.*

The same pattern as step 1 — **compute all candidates, select one**:

```
   Aᵢ ─┬──► AND ───►│0 │
   Bᵢ ─┤            │  │
       ├──► OR  ───►│1 │  4×1
       │            │  │  MUX ──► Eᵢ
       ├──► XOR ───►│2 │
       │            │  │
       └──► NOT A ─►│3 │
                     ▲▲
                  S₁ S₀
```

**Four gates and one 4-to-1 MUX per bit.** Sixteen logic functions of two variables exist, but only
these four are built — every other function can be composed from them, so building all sixteen would
be wasted silicon.

| S₁ | S₀ | Eᵢ |
|---|---|---|
| 0 | 0 | Aᵢ ∧ Bᵢ |
| 0 | 1 | Aᵢ ∨ Bᵢ |
| 1 | 0 | Aᵢ ⊕ Bᵢ |
| 1 | 1 | Aᵢ′ |

> ✓ **Check 2.** (a) Why build only 4 of the 16 possible two-variable functions?
> (b) Which of the four needs only one input? (c) How many gates for an 8-bit logic stage?

---

### 3 · The shifter

> **Q** `[part of A1 Q17 — "iv) Shift right A"]`
> **What hardware performs "shift right A" inside an ALU, and why does it need no gates at all?**
>
> *Guess before reading. The answer is genuinely almost nothing.*

A shift is **pure wiring**. To shift right, bit *i* of the output is taken from bit *i+1* of the
input — you simply connect the wires one position across. There is no gate, no adder, no delay.

```
   Aᵢ₊₁ ─────────────────────► shift-right input of stage i
   Aᵢ₋₁ ─────────────────────► shift-left  input of stage i
```

Which is why the shift operations sit as two **plain inputs** to the output MUX in step 4, alongside
the arithmetic and logic blocks. Everything else about shifting — what enters the vacated end,
logical vs circular vs arithmetic — was file 04, step 8, and is decided by what you wire to the end
stages, not by this circuit.

> ✓ **Check 3.** (a) Why is a shift faster than an addition? (b) Where does stage *n−1* get its
> shift-right input from?

---

### 4 · One ALSU stage

> **Q** `[A1 Q17, first half · 8 marks]`
> **Design a 4-bit arithmetic-logic-shift circuit.**
>
> *You now have three blocks. Guess how they are combined into one output — and how many select lines
> the whole thing needs. Then read on.*

One **4-to-1 MUX at the output**, choosing between the four blocks:

```
             ┌──────────────────────┐
   Aᵢ ──┬───→│  arithmetic circuit  │──→ Dᵢ ──┐
   Bᵢ ──┤    │  (FA + 4-to-1 MUX)   │         │      ┌─────────┐
        │    └──────────────────────┘         ├─────→│ 4-to-1  │
        │    ┌──────────────────────┐         │      │  MUX    │──→ Fᵢ
        └───→│    logic circuit     │──→ Eᵢ ──┤      │         │
             └──────────────────────┘         │      └─────────┘
   Aᵢ₊₁ ──────── shift right input ───────────┤          ▲
   Aᵢ₋₁ ──────── shift left  input ───────────┘          │
                                                    S₃ S₂ select
```

| Control | Chooses |
|---|---|
| **S₃ S₂** | which **block** reaches the output: 00 arithmetic · 01 logic · 10 shift right · 11 shift left |
| **S₁ S₀** | which **operation within** the arithmetic or logic block |
| **Cᵢₙ** | the arithmetic block's carry-in — a third arithmetic control |

**Total: 4 select lines + Cᵢₙ.** Replicate the stage 4 times for a 4-bit ALSU (n times for n bits),
with the carry rippling from stage to stage.

**Operation count — derive it, don't recite it:**

| S₃S₂ | Block | Operations |
|---|---|---|
| 00 | arithmetic | S₁S₀ (4) × Cᵢₙ (2) = **8** |
| 01 | logic | S₁S₀ = **4** |
| 10 | shift right | **1** |
| 11 | shift left | **1** |
| | | **14 total** |

★ **The sentence that earns the "explain in detail" marks:** the ALSU computes *every* candidate
result **in parallel, every cycle**, and the select lines merely decide which one is allowed out.
Hardware does not decide-then-compute; it computes everything and discards. That is the deep reason
control is nothing but *selection* — and it is the idea the whole control unit in file 08 is built on.

> ✓ **Check 4.** (a) How many select lines in total, and what does each group do?
> (b) Derive the 14. (c) Why does the arithmetic block get three control bits where the logic block
> gets two?

---

### 5 · The function table

> **Q** `[A1 Q17, second half · 8 marks]`
> **Explain the working of the circuit for the following functions: i) Transfer A ii) Add with carry
> iii) XOR iv) Shift right A.**
>
> *For each one, you must give the control values that select it. Try to work out "Transfer A" from
> step 4 before reading on.*

**This is the professor's table** (his deck, p. 32 — identical to Mano's Table 4-8):

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
| 1 | 0 | × | × | × | F = shr A | **shift right A** |
| 1 | 1 | × | × | × | F = shl A | shift left A |

**The four he asks for, explained the way the marks want:**

| Function | S₃S₂S₁S₀ Cᵢₙ | What the hardware does |
|---|---|---|
| **i) Transfer A** | `00000` | S₃S₂ = 00 selects the arithmetic block; S₁S₀ = 00 makes the MUX feed **0** into Y; Cᵢₙ = 0 → the full adder computes A + 0 + 0 = **A**. The output MUX passes it. |
| **ii) Add with carry** | `00011` | Same block; S₁S₀ = 01 feeds **B** into Y; Cᵢₙ = 1 → A + B + 1. |
| **iii) XOR** | `0110×` | S₃S₂ = 01 selects the **logic** block; S₁S₀ = 10 selects its XOR gates, so Fᵢ = Aᵢ ⊕ Bᵢ bit by bit. Cᵢₙ is irrelevant — the logic block has no carry. |
| **iv) Shift right A** | `10×××` | S₃S₂ = 10 selects the **shift-right input**, which is simply Aᵢ₊₁ wired across. No arithmetic or logic circuit is involved; S₁S₀ and Cᵢₙ are don't-cares. |

**Notice rows 1 and 8 both say "transfer A".** Three control bits give 8 combinations but only 7
distinct arithmetic operations, so one is duplicated (`A + 1111 + 1 = A`). Examiners ask why two rows
agree — now you can say.

> ✓ **Check 5.** (a) Give the control values for **subtraction**. (b) Why is Cᵢₙ a don't-care for
> every logic operation? (c) Why do two rows both give "transfer A"?

---

### 6 · ⚠ Which table — the trap

> **Q** *(no assignment or Mano question — this is a trap the marks live in)*
> **Your notes contain two different tables for this circuit, and they disagree about what `S₁S₀ = 00`
> does. Which one does the professor examine, and how can both be correct?**
>
> *Look back at step 1's MUX and at step 5's table. Guess where the disagreement comes from.*

Both tables are **correct for their own wiring of the arithmetic block's 4-to-1 MUX.** That is the
whole resolution.

| | Standalone arithmetic circuit | **The ALSU (his table)** |
|---|---|---|
| MUX input 0 | B | **0** |
| MUX input 1 | B′ | **B** |
| MUX input 2 | 0 | **B′** |
| MUX input 3 | 1 | **1** |
| So `S₁S₀ = 00` gives | A + B (**add**) | A + 0 (**transfer A**) |
| So "add with carry" is at | `S₁S₀Cᵢₙ = 001` | **`S₃S₂S₁S₀Cᵢₙ = 00011`** |

**Use the ALSU table (step 5) whenever the question says ALU / ALSU / arithmetic-logic-shift** — that
is the professor's slide and Mano's Table 4-8. Use the other ordering only if a question explicitly
gives you the standalone arithmetic circuit of the earlier section with its own wiring.

**How to be safe either way:** in the exam, **draw the MUX with its input wiring labelled** (0, B, B′,
1) before you give the table. Then your table is justified by your own diagram and cannot be marked
wrong against a different convention.

> ✓ **Check 6.** (a) Under the ALSU wiring, what does `S₁S₀ = 11` with Cᵢₙ = 0 give, and why?
> (b) What single thing should you always draw to make your table defensible?
> (c) Both tables are correct — correct *relative to what*?

---

## Exam form

### The answer skeleton for A1 Q17 (16 marks)

```
1. Block diagram of one stage       arithmetic | logic | shr | shl → 4×1 output MUX
2. The arithmetic stage in detail   FA + 4×1 MUX on Y, WITH THE WIRING LABELLED (0, B, B', 1)
3. The logic stage                  AND OR XOR NOT → 4×1 MUX
4. The shifts                       plain wiring, A(i+1) and A(i-1)
5. Control summary                  S3S2 picks block; S1S0 picks operation; Cin third arithmetic control
6. Operation count                  8 + 4 + 1 + 1 = 14, derived
7. The four named functions         control values + one sentence of mechanism each
8. The closing sentence             all results computed in parallel; select lines choose which escapes
```

### Counting rules

| Quantity | Value |
|---|---|
| Select lines | **4** (S₃S₂S₁S₀) **+ Cᵢₙ** |
| Operations | **14** = 8 arithmetic + 4 logic + 2 shift |
| Per bit-stage | 1 full adder, 1 arithmetic MUX, 4 logic gates, 1 logic MUX, 1 output MUX |
| For 4 bits | four such stages, carry rippling between them |

⚠ 14 is the count **for this design**. A differently drawn ALSU gives a different count — **derive it
from your own diagram**, never recite it.

---

## Attempt

1. `[A1 Q17 · 16]` in full, following the eight-point skeleton. Time yourself: it should take about
   20 minutes, which is what 16 marks buys.
2. `[Mano 4-15]` the four-operation arithmetic circuit from its truth table — this forces you to
   *derive* MUX wiring rather than recall it, which is the skill step 6 is protecting.
3. `[Mano 4-17]` the XOR / XNOR / NOR / NAND logic circuit with two selection variables.
4. `[Mano 4-16]` all 16 logic functions — harder, and good preparation for being asked "why only four?"

---

## Traps

| Trap | Correction |
|---|---|
| Using the standalone arithmetic-circuit ordering for the ALSU | Different MUX wiring. For ALSU questions use the step 5 table |
| Drawing the circuit and stopping | Half the 16 marks is *explaining the four named functions* with their control values |
| Reciting "14 operations" | Derive it: 8 + 4 + 1 + 1, from your own diagram |
| Forgetting Cᵢₙ when counting select lines | 4 select lines **plus** Cᵢₙ |
| Treating Cᵢₙ as relevant to logic operations | The logic block has no carry — Cᵢₙ is a don't-care there |
| "Two rows can't both be transfer A" | They can: 8 combinations, 7 distinct operations |
| Drawing a shifter with gates | A shift is wiring. No gates |
| Not labelling the arithmetic MUX inputs | Label them. It is what makes your table defensible |

---

## Self-test

1. How many select lines does the ALSU need, and what does each group control?
2. Give the control values for: transfer A, add with carry, XOR, shift right A.
3. Derive the operation count from first principles.
4. Under the professor's wiring, what is at `S₃S₂S₁S₀Cᵢₙ = 00101`?
5. Why is a shift operation free in hardware terms compared with an addition?
6. State the one-sentence reason control in a computer is nothing but selection.
7. Two published tables for this circuit disagree. Explain how both can be right.

---
---

## Answers

**Check 1.** (a) A is needed in every single operation (even "transfer A" and the shifts are about A),
so there is nothing to select. (b) All-1s is −1 in 2's complement, so A + 1111 = A − 1 (file 04,
step 4). (c) 3 bits → 8 combinations, but only **7 distinct** operations — one is a duplicate.

**Check 2.** (a) The other twelve can be composed from AND, OR, XOR and NOT, so building them would be
silicon spent for nothing. (b) **Complement (A′)** — B is unused. (c) 8 × 4 = **32 gates**, plus eight
4-to-1 MUXes.

**Check 3.** (a) It is only wiring — no gate delay, no carry to propagate, so it completes in
negligible time, whereas an addition must wait for the carry to ripple across all stages. (b) From
outside the ALSU — the serial input, and *what* is wired there is what makes the shift logical,
circular or arithmetic (file 04, step 8).

**Check 4.** (a) **Four**: S₃S₂ selects the block, S₁S₀ selects the operation inside the arithmetic or
logic block — plus **Cᵢₙ** as a third arithmetic control. (b) arithmetic 4 × 2 = 8, logic 4, shift
right 1, shift left 1 → **14**. (c) Because its adder has a carry input, and Cᵢₙ genuinely changes the
result (A + B vs A + B + 1); the logic gates have no carry, so a third bit would change nothing.

**Check 5.** (a) **`00101`** — S₃S₂ = 00 (arithmetic), S₁S₀ = 10 (MUX feeds B′), Cᵢₙ = 1 → A + B′ + 1 =
A − B. (b) The logic block is built from plain gates with no carry path, so no carry input exists to
connect. (c) Three control bits give 8 combinations but there are only 7 distinct arithmetic
operations; `S₁S₀ = 11, Cᵢₙ = 1` computes A + 1111 + 1 = A, duplicating `S₁S₀ = 00, Cᵢₙ = 0`.

**Check 6.** (a) MUX input 3 is the constant **1** (all bits), so A + 1111 + 0 = **A − 1**, decrement.
(b) **The arithmetic MUX with its four inputs labelled** (0, B, B′, 1). (c) Correct **relative to the
wiring of the arithmetic block's 4-to-1 MUX** — change the wiring and the table's row order changes
with it.

**Self-test 1.** Four — **S₃S₂** selects the block (arithmetic / logic / shr / shl), **S₁S₀** selects
the operation within the block — plus **Cᵢₙ** as a third arithmetic control.

**Self-test 2.** Transfer A `00000` · add with carry `00011` · XOR `0110×` · shift right A `10×××`.

**Self-test 3.** S₃S₂ = 00 gives S₁S₀ (4) × Cᵢₙ (2) = 8 arithmetic; S₃S₂ = 01 gives S₁S₀ = 4 logic;
S₃S₂ = 10 and 11 give one shift each. 8 + 4 + 1 + 1 = **14**.

**Self-test 4.** S₃S₂ = 00 arithmetic, S₁S₀ = 10 → Y = B′, Cᵢₙ = 1 → **F = A + B′ + 1 = A − B**,
subtraction.

**Self-test 5.** A shift is a wiring offset — no gates, no carry propagation — whereas an addition
must wait for the carry to ripple through every stage.

**Self-test 6.** The ALSU computes every candidate result in parallel every cycle, and the select
lines merely decide which one is allowed out — so "control" is selection, not computation.

**Self-test 7.** They describe the same structure with **different wiring of the arithmetic block's
4-to-1 MUX** (0,B,B′,1 versus B,B′,0,1). Each table is correct for its own wiring; the professor's
ALSU slide and Mano Table 4-8 use the first, so label your MUX and the ambiguity disappears.

---

## What to do next

U1 is finished. Files 06–08 build the **Basic Computer** out of everything so far — and the question
base changes character: from here on, **Assignment 2 is Mano chapter 5 copied verbatim**, so every
question in files 06, 07 and 08 is both an assignment item and a textbook problem.
