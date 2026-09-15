# 02 — Digital Building Blocks, Drawn From Gates

**Assignment 1: Q7 (4 × 6 = 24 marks) · Digital Electronics prerequisite, used throughout U1–U2**

Every block here reappears later: the **decoder** makes T₀…T₁₅ and D₀…D₇, the **MUX** builds the
common bus and the ALSU, the **parallel-load register** is every BC register, the **shift register**
is AC's CIR/CIL.

---

## Map

```
   Combinational (no memory)            Sequential (memory, clocked)
   ─────────────────────────            ────────────────────────────
   3-to-8 decoder                       D flip-flop
   4-to-1 MUX                               │
   Quadruple 2-to-1 MUX                     ▼
        │                               4-bit register with parallel load
        └──── MUX per bit feeds ───────►     = D FFs + 2-to-1 MUX per bit
                                            │
                                            ▼
                                        4-bit bidirectional shift register
                                        with parallel load = D FFs + 4-to-1 MUX per bit
```

**The pattern for the two registers:** a flip-flop always loads *something* on every clock edge;
a MUX in front of it chooses **what** — its own old value (hold), a neighbour (shift), or new data
(load).

---

## Attempt

Explain the working of each, with a circuit drawn from basic gates. *(4 marks each)*

1. D flip-flop
2. 3-to-8 line decoder
3. 4-to-1 line multiplexer
4. Quadruple 2 × 1 multiplexer
5. 4-bit register with parallel load
6. 4-bit bidirectional shift register with parallel load

For each, include: **circuit · function/truth table · 2–3 lines of working.**

---

## Learn

### 1. D flip-flop

**Clocked D latch from NAND gates** (4 NANDs + 1 inverter):

```
   D ──────────┐                                 
               [NAND 1]── S' ──►[NAND 3]──► Q ──┐
   CLK ──┬─────┘                    ▲           │
         │                          └─── Q' ◄───┼──┐   cross-coupled
         │                          ┌─── Q  ◄───┘  │   SR latch
         │                          ▼              │
         └─────┐                 [NAND 4]──► Q' ───┘
   D ─[NOT]─D'─[NAND 2]── R' ──────►   
```

| Gate | Inputs | Output |
|---|---|---|
| NAND 1 | D, CLK | S′ = (D·CLK)′ |
| NAND 2 | D′, CLK | R′ = (D′·CLK)′ |
| NAND 3 | S′, Q′ | Q |
| NAND 4 | R′, Q | Q′ |

| CLK | D | Q(t+1) |
|---|---|---|
| 0 | × | Q(t) — hold |
| 1 | 0 | 0 — reset |
| 1 | 1 | 1 — set |

**Characteristic equation:** Q(t+1) = D.

**Working:** CLK = 0 forces both NAND 1 and NAND 2 to 1, so the latch holds. CLK = 1 passes D: D = 1
drives S′ = 0 → Q = 1; D = 0 drives R′ = 0 → Q = 0. The inverter makes S′ and R′ complementary, so the
forbidden SR state (both 0) cannot occur.

**Edge-triggered version:** two D latches in series (master–slave), clocked on opposite phases —
master follows D while CLK = 1, slave copies the master when CLK falls. Output changes only at a
clock edge. This is the flip-flop every register uses.

### 2. 3-to-8 line decoder

n inputs → 2ⁿ outputs; exactly one output is 1 — the minterm of the input.

```
   A ──┬──[NOT]── A'           D₀ = A'B'C'     D₄ = AB'C'
   B ──┼──[NOT]── B'           D₁ = A'B'C      D₅ = AB'C
   C ──┼──[NOT]── C'           D₂ = A'BC'      D₆ = ABC'
       │                       D₃ = A'BC       D₇ = ABC
       └── true and complemented lines run to 8 three-input AND gates
           (4-input if an enable E is added: Dᵢ = E · mᵢ)
```

| A | B | C | active output |
|---|---|---|---|
| 0 | 0 | 0 | D₀ |
| 0 | 0 | 1 | D₁ |
| 0 | 1 | 0 | D₂ |
| 0 | 1 | 1 | D₃ |
| 1 | 0 | 0 | D₄ |
| 1 | 0 | 1 | D₅ |
| 1 | 1 | 0 | D₆ |
| 1 | 1 | 1 | D₇ |

**Hardware:** 3 NOT + 8 AND. **With enable:** E = 0 → all outputs 0; E = 1 → normal. A decoder with
enable is a 1-to-8 **demultiplexer** (E is the data input).
**Where it returns:** the BC's opcode decoder (IR(12–14) → D₀…D₇) is exactly this.

### 3. 4-to-1 line multiplexer

2ⁿ data inputs, n select lines, one output.

```
   S₁ ──┬─[NOT]─ S₁'
   S₀ ──┼─[NOT]─ S₀'
        │
   I₀ ─[AND: S₁' S₀' I₀]──┐
   I₁ ─[AND: S₁' S₀  I₁]──┤
   I₂ ─[AND: S₁  S₀' I₂]──┼──[4-input OR]── Y
   I₃ ─[AND: S₁  S₀  I₃]──┘
```

**Y = S₁′S₀′I₀ + S₁′S₀I₁ + S₁S₀′I₂ + S₁S₀I₃**

| S₁ | S₀ | Y |
|---|---|---|
| 0 | 0 | I₀ |
| 0 | 1 | I₁ |
| 1 | 0 | I₂ |
| 1 | 1 | I₃ |

**Hardware:** 2 NOT + 4 three-input AND + 1 four-input OR.
**Working:** the select lines form a 2-to-4 decoder inside the ANDs; only the AND whose select pattern
matches is enabled, and the OR passes its data bit.

### 4. Quadruple 2 × 1 multiplexer

Four 2-to-1 MUXes sharing **one select S** and **one enable E** — it chooses between two **4-bit
words** A = A₃A₂A₁A₀ and B = B₃B₂B₁B₀.

```
   S ──┬─[NOT]─ S'           for each bit i = 0…3:
   E ──┴─[NOT]─ E'
                             Aᵢ ─[AND: E' S' Aᵢ]──┐
                                                  ├─[OR]── Yᵢ
                             Bᵢ ─[AND: E' S  Bᵢ]──┘
```

**Yᵢ = E′(S′Aᵢ + SBᵢ)**

| E | S | Y |
|---|---|---|
| 1 | × | 0000 (disabled) |
| 0 | 0 | A |
| 0 | 1 | B |

**Hardware:** 2 NOT + 8 three-input AND + 4 OR.
**Working:** S is shared, so all four bits switch together — it selects a **word**, not a bit. This is
the "MUX per bit, common select" structure that the common bus scales up (file 03).

### 5. 4-bit register with parallel load

Four D flip-flops with a common clock. A **Load** line chooses, per bit, between new input Iᵢ and the
flip-flop's own output Aᵢ.

```
   Load ──┬─[NOT]─ Load'
          │
   for each bit i = 0…3:

        Iᵢ ─[AND: Load  · Iᵢ]──┐
                               ├─[OR]──► D ┌──────┐ Q ──┬──► Aᵢ
        ┌─[AND: Load' · Aᵢ]────┘           │ D FF │     │
        │                        Clock ───►│ >    │     │
        │                        Clear ───►│ CLR  │     │
        └──────────────────────────────────┴──────┘─────┘   (feedback)
```

**Dᵢ = Load·Iᵢ + Load′·Aᵢ**

| Clear | Load | Next state |
|---|---|---|
| 1 | × | 0000 |
| 0 | 0 | A (no change) |
| 0 | 1 | I₃I₂I₁I₀ loaded |

**Working:** the clock ticks continuously. Load = 0 routes each flip-flop's output back to its own
input, so every edge reloads the same value — the register **holds**. Load = 1 routes I into D, and
the next edge captures all four bits **simultaneously** (parallel). **This is why an RTL transfer
needs a load signal:** the clock alone changes nothing (file 03).

### 6. 4-bit bidirectional shift register with parallel load

Four D flip-flops; each is fed by a **4-to-1 MUX** with common selects S₁S₀.

Convention used here: A₃ is the leftmost (MSB); "shift right" moves bits toward A₀.

| MUX input | Selected when S₁S₀ = | Source for flip-flop Aᵢ | Operation |
|---|---|---|---|
| 0 | 00 | Aᵢ (own output) | **no change** |
| 1 | 01 | Aᵢ₊₁ (left neighbour); A₃ takes serial input for right shift | **shift right** |
| 2 | 10 | Aᵢ₋₁ (right neighbour); A₀ takes serial input for left shift | **shift left** |
| 3 | 11 | Iᵢ (parallel input) | **parallel load** |

```
         serial-in (right shift)                         serial-in (left shift)
                │                                                 │
   ┌────────────┼───────────┬────────────┬────────────┐           │
   │  A₃ stage  │  A₂ stage │  A₁ stage  │  A₀ stage  │           │
   │  4×1 MUX   │  4×1 MUX  │  4×1 MUX   │  4×1 MUX   │◄──────────┘
   │  0: A₃     │  0: A₂    │  0: A₁     │  0: A₀     │
   │  1: SIR    │  1: A₃    │  1: A₂     │  1: A₁     │
   │  2: A₂     │  2: A₁    │  2: A₀     │  2: SIL    │
   │  3: I₃     │  3: I₂    │  3: I₁     │  3: I₀     │
   │     │      │    │      │    │       │    │       │
   │   D FF     │  D FF     │  D FF      │  D FF      │ ◄── common clock
   └─────┼──────┴────┼──────┴────┼───────┴────┼───────┘     common S₁ S₀
         A₃          A₂          A₁           A₀
```

**Working:** all four MUXes share S₁S₀, so the whole register performs one operation per clock edge.
00 recirculates (hold); 01 and 10 take each bit from a neighbour (shift); 11 takes the external inputs
(load). This is the 74194 universal shift register; its mode table is the same.

---

## Worked

**Trace the shift register:** A = 1011, serial-in for right shift = 0, serial-in for left shift = 1,
I = 0110. Apply S₁S₀ = 01, 10, 11, 00 on successive edges.

```
   start        1011
   01 shr       0101      A₃←SIR=0, A₂←A₃=1, A₁←A₂=0, A₀←A₁=1
   10 shl       1011      A₃←A₂=1, A₂←A₁=0, A₁←A₀=1, A₀←SIL=1
   11 load      0110
   00 hold      0110
```

---

## Traps

| Trap | Correction |
|---|---|
| Drawing the parallel-load register without the feedback path | Without Load′·Aᵢ, Load = 0 loads 0s — it would **clear**, not hold |
| "A flip-flop only changes when you tell it" | It samples D on **every** edge. Hold is achieved by feeding Q back |
| Quad 2×1 MUX drawn with four separate selects | One common S — it switches a whole word |
| Decoder: "outputs = binary count" | One output is high: the **minterm** of the input |
| Shift direction without stating the convention | Say which end is the MSB; textbooks draw it both ways |

---

## Self-test

1. How many AND gates does a 4-to-16 decoder with enable need, and how many inputs does each have?
2. Write Yᵢ for a quadruple 2×1 MUX whose enable is **active-high**.
3. In the parallel-load register, what is loaded on the next edge if Load = 1 and I = 1001 but Clear = 1?
4. Shift register A = 0110, SIR = 1, SIL = 0. Give A after S₁S₀ = 01, then 01, then 10.
5. Which of the six blocks is the BC's T₀…T₁₅ generator built from, and with what input?

---
---

## Answers

**Attempt 1–6.** See each Learn subsection: circuit + table + working paragraph is the full 4-mark
answer.

**Self-test 1.** 16 AND gates, each 5-input (4 variables + E). Plus 4 inverters.

**Self-test 2.** Yᵢ = E(S′Aᵢ + SBᵢ).

**Self-test 3.** 0000 — Clear dominates.

**Self-test 4.**
```
   start   0110
   01      1011     A₃←1, A₂←0, A₁←1, A₀←1
   01      1101     A₃←1, A₂←1, A₁←0, A₀←1
   10      1010     A₃←1, A₂←0, A₁←1, A₀←0
```

**Self-test 5.** A 4-to-16 decoder, driven by the 4-bit sequence counter SC.
