# 02 — Digital building blocks

**Assignment 1: Q7 · 24 of 200 marks · U1 (prerequisite) · needs 00**

One question, 24 marks, six circuits at 4 marks each — the second-biggest item in Assignment 1.
It is Digital Electronics material, but he examines it **here**, and every later file is built out of
these six parts.

> **What "explain the working" means for 4 marks.** He asks for the circuit *and* the explanation.
> A drawing with no words scores badly; words with no drawing score worse. The pattern that scores:
> **what it does → the circuit → the truth/function table → one sentence of why the circuit produces
> that table.**

---

## Map

```
   [1] D flip-flop ────────────────────► stores ONE bit
    │                                     │
    │                                     ▼
   [2] Decoder ──────┐              [5] Register with parallel load
       1-of-2ⁿ       │                    │        (n flip-flops + a choice)
                     ├──► selection       │
   [3] Multiplexer ──┤    hardware        ▼
       n-to-1        │              [6] Bidirectional shift register
                     │                    with parallel load
   [4] Quad 2×1 MUX ─┘                    (the choice widened to four)
       one word, not one bit
```

Everything on this page is one of two ideas: **store a bit** (1) or **choose a source** (2, 3, 4).
5 and 6 are those two ideas combined.

---

## The questions this file answers

`[A1 Q7 · 4 × 6 = 24 marks]` **Explain the working of the following. Support your answer with circuits
formed with basic gates:** (i) D Flip-Flop (ii) 3-to-8 line Decoder (iii) 4-to-1-line multiplexer
(iv) Quadruple 2×1 multiplexer (v) 4-bit register with parallel load (vi) 4-bit Bidirectional Shift
Register with Parallel Load

Mano's chapter 2 supplies the follow-ups he hasn't asked yet: **2-6, 2-8, 2-9, 2-10, 2-12, 2-13,
2-15, 2-16**. Q7(iv) *is* Mano 2-9 and Q7(vi) *is* Mano 2-16.

---

## Build

### 1 · D flip-flop

> **Q** `[A1 Q7(i) · 4 marks]`
> **Explain the working of a D flip-flop. Support your answer with a circuit formed with basic gates.**
>
> *File 00 step 7 told you a register changes "only at a clock tick". Guess what physically enforces
> that. Then read on.*

A **flip-flop** is one bit of storage. The **D** (data) flip-flop is the simple one: **Q takes the
value of D at the clock edge, and holds it until the next edge.**

```
        ┌────────┐
  D ───►│D      Q│───► Q
        │        │
 CLK ──►│>     Q'│───► Q'
        └────────┘

  D ──┬──────────────► S ┐
      │                  ├─ SR latch ──► Q
      └──►o──────────► R ┘
         inverter
        (both gated by CLK)
```

Built from a **clocked SR latch plus one inverter**: D goes to S and D′ goes to R, so S and R can
never both be 1 — which is exactly the forbidden state of the SR latch. That inverter is the whole
trick, and saying so is the "why" sentence worth a mark.

| CLK | D | Q(next) |
|---|---|---|
| no edge | × | **Q (unchanged)** |
| ↑ edge | 0 | 0 |
| ↑ edge | 1 | 1 |

**Characteristic equation: Q(t+1) = D.**

Edge-triggered vs level-triggered matters: a *latch* is transparent the whole time the clock is high,
so its output can change several times in one clock period. A *flip-flop* samples once, at the edge.
Registers are built from flip-flops for exactly that reason — every register in this course changes
once per tick, together.

> ✓ **Check 1.** (a) Why can a D flip-flop never enter the SR latch's forbidden state?
> (b) A 16-bit register needs how many flip-flops? (c) What is the difference between a latch and a
> flip-flop, in one sentence?

---

### 2 · Decoder

> **Q** `[A1 Q7(ii) · 4 marks]`
> **Explain the working of a 3-to-8 line decoder, with a circuit formed with basic gates.**
>
> *A 12-bit address has to pick out exactly one of 4096 memory words (file 00, step 4). Guess what
> kind of circuit does that. Then read on.*

A **decoder** converts an n-bit binary code into **one active output out of 2ⁿ** — the output whose
number equals the input. It is how an address becomes a selection.

3 inputs → 8 outputs. Each output is one **minterm** of the three inputs:

```
 A₂ ──┬──────────────┬──────── …
      └─►o─┐         │
 A₁ ──┬────┼───┐     │        D₀ = A₂'A₁'A₀'   ┌───┐
      └─►o─┼─┐ │     │        D₁ = A₂'A₁'A₀    │AND│──► Dᵢ
 A₀ ──┬────┼─┼─┼─┐   │        …                └───┘
      └─►o─┘ │ │ │   │        D₇ = A₂ A₁ A₀      (one 3-input AND
                                                   per output)
```

**Circuit: 3 inverters + eight 3-input AND gates.** Each AND gate is wired to the true or complemented
form of each input so that it fires for exactly one combination.

| A₂ A₁ A₀ | Active output |
|---|---|
| 0 0 0 | D₀ |
| 0 0 1 | D₁ |
| 0 1 0 | D₂ |
| … | … |
| 1 1 1 | D₇ |

Exactly one output is 1 at any time; the other seven are 0.

**Enable input.** Add a 4th input E to every AND gate: E = 0 forces **all** outputs to 0, E = 1 lets the
decoder work normally. The enable is what lets you build big decoders out of small ones — which is
Mano's follow-up question.

> ✓ **Check 2.** (a) A 12-bit memory address feeds a decoder. How many outputs?
> (b) `[Mano 2-6]` Build a 5-to-32-line decoder from four 3-to-8 decoders with enable and one 2-to-4
> decoder. Which input bits go where? (c) How many outputs of a decoder are 1 at once?

---

### 3 · Multiplexer

> **Q** `[A1 Q7(iii) · 4 marks]`
> **Explain the working of a 4-to-1-line multiplexer, with a circuit formed with basic gates.**
>
> *A decoder turns a code into one selected line. Guess what circuit does the reverse — many lines
> in, one line out. Then read on.*

A **multiplexer (MUX)** selects **one of several data inputs** and routes it to a single output. The
select lines carry the number of the chosen input. It is a hardware switch with no moving parts.

4 data inputs need **2 select lines** (2² = 4).

```
  I₀ ──►┐
        │ AND ──┐      S₁'S₀'
  I₁ ──►┤ AND ──┤      S₁'S₀     ┌────┐
        │       ├─────►│ OR │────► Y
  I₂ ──►┤ AND ──┤      S₁ S₀'    └────┘
        │       │
  I₃ ──►┘ AND ──┘      S₁ S₀

        S₁ S₀ (+ their complements from 2 inverters)
```

**Circuit: 2 inverters + four 3-input AND gates + one 4-input OR gate.** Each AND gate is enabled by
one select combination, so exactly one AND passes its data input and the rest deliver 0; the OR gate
collects the survivor.

| S₁ | S₀ | Y |
|---|---|---|
| 0 | 0 | I₀ |
| 0 | 1 | I₁ |
| 1 | 0 | I₂ |
| 1 | 1 | I₃ |

**The mechanism one sentence deeper, because it recurs everywhere in this course:** a MUX does not
"fetch" the selected input. All four inputs are present at all times; the select lines merely decide
which one is *allowed through*. Hardware computes everything and discards — you will meet that idea
again as the whole basis of the ALSU (file 05) and of control (file 08).

Notice a MUX contains a decoder: the select lines are decoded to enable one AND gate.

> ✓ **Check 3.** (a) How many select lines does a 16-to-1 MUX need?
> (b) `[Mano 2-8]` Build a 16-to-1 MUX from two 8-to-1 MUXes and one 2-to-1 MUX.
> (c) What is inside a MUX that you have already met in step 2?

---

### 4 · Quadruple 2×1 multiplexer

> **Q** `[A1 Q7(iv) · 4 marks]` **= Mano 2-9**
> **Explain the working of a quadruple 2×1 multiplexer, with a circuit formed with basic gates.**
>
> *Steps 3 and 4 look like the same question. Guess what is actually different about this one.
> Then read on.*

They are not the same question, and the difference is the mark.

- A 4-to-1 MUX chooses **one bit from four sources**.
- A **quadruple 2-to-1 MUX** chooses **one 4-bit word from two sources.**

"Quadruple" counts the *multiplexers*, not the inputs: it is **four 2-to-1 MUXes in one package,
sharing one select line and one enable.**

```
   A₃ ─┐            B₃ ─┐
       │ 2×1 MUX ──────────► Y₃
   A₂ ─┐            B₂ ─┐
       │ 2×1 MUX ──────────► Y₂        all four share
   A₁ ─┐            B₁ ─┐                S  (select)
       │ 2×1 MUX ──────────► Y₁          E  (enable)
   A₀ ─┐            B₀ ─┐
       │ 2×1 MUX ──────────► Y₀
```

| E | S | Y (all four bits) |
|---|---|---|
| 1 | × | **all 0** (disabled) |
| 0 | 0 | A |
| 0 | 1 | B |

*(E is active-low in the standard part, IC 74157 — state whichever convention you draw.)*

Each 2-to-1 MUX is: `Y = S′·A + S·B` — one inverter, two AND gates, one OR gate. Four of those.

**Why this part exists at all:** registers are words, not bits, so real selection hardware is always
*k* MUXes wide. This is the shape of every datapath choice in the rest of the pack — and it is exactly
the sizing rule in file 03: **to bus k registers of n bits you need n multiplexers of k inputs each.**

> ✓ **Check 4.** (a) In one sentence, the difference between a 4-to-1 MUX and a quadruple 2-to-1 MUX.
> (b) How many MUXes and of what size to choose between four 8-bit registers?
> (c) Why is the select line shared across all four MUXes rather than separate?

---

### 5 · 4-bit register with parallel load

> **Q** `[A1 Q7(v) · 4 marks]`
> **Explain the working of a 4-bit register with parallel load, with a circuit formed with basic gates.**
>
> *Four D flip-flops side by side already store four bits. Guess what "with parallel load" adds, and
> why it is needed at all. Then read on.*

Four D flip-flops on a common clock store a 4-bit word — but they would capture their D inputs at
**every** tick. A register must hold its value for many ticks and change only when told. That is what
**parallel load** means: a control input **LD** that decides whether this tick changes anything.

There are two ways to build it, and the difference is a standard exam trap.

**The wrong way — gate the clock** `[this is Mano 2-10]`:
```
  LD ──┐
       ├─ AND ──► clock input of every flip-flop
 CLK ──┘
```
It "works", but the AND gate delays the clock, so this register's flip-flops now tick slightly later
than every other register's. In a machine where many registers must capture on the *same* edge
(file 00, step 7) that skew breaks the design. **Never gate the clock.**

**The right way — gate the data** `[Mano's Fig. 2-7]`: give every flip-flop a **2-to-1 MUX** on its D
input, selected by LD:

```
            ┌─────────┐
  I₃ ──────►│ 2×1 MUX │──► D ┌────┐
        ┌──►│  (LD)   │      │ FF │──┬──► A₃
        │   └─────────┘   ┌─►│>   │  │
        └─────────────────┘  └────┘  │
              feedback ◄─────────────┘        … same for A₂, A₁, A₀
                                        CLK common to all four
```

| LD | What each flip-flop captures at the next tick |
|---|---|
| 0 | its **own output** — the value is rewritten unchanged, so the register appears to hold |
| 1 | the corresponding **input Iᵢ** — the word is loaded |

**The clock never stops; the register still ticks every cycle.** When LD = 0 it simply loads itself.
Say that sentence in the exam — it is the answer to "explain the working".

> ✓ **Check 5.** (a) Why is gating the clock bad practice? (b) With LD = 0, what does each flip-flop
> load? (c) `[Mano 2-12]` How would you add a **synchronous clear** to this register?

---

### 6 · 4-bit bidirectional shift register with parallel load

> **Q** `[A1 Q7(vi) · 4 marks]` **= Mano 2-16**
> **Explain the working of a 4-bit bidirectional shift register with parallel load, with a circuit
> formed with basic gates.**
>
> *Step 5's register had two choices (hold / load) and one select line. This one has four choices.
> Guess what they are before reading on.*

Four choices → a **4-to-1 MUX** on each flip-flop's D input (step 3), and **two** select lines S₁S₀.
Same idea as step 5, widened.

Each stage *i* takes its four MUX inputs from:

| MUX input | Source | Gives |
|---|---|---|
| 0 | **A**ᵢ — its own output | hold |
| 1 | **A**ᵢ₊₁ — the neighbour on its **left** | shift **right** |
| 2 | **A**ᵢ₋₁ — the neighbour on its **right** | shift **left** |
| 3 | **I**ᵢ — the external input | parallel load |

```
 serial-in (right shift)
        │
        ▼
     ┌─────┐   ┌─────┐   ┌─────┐   ┌─────┐
     │ A₃  │◄─►│ A₂  │◄─►│ A₁  │◄─►│ A₀  │
     └─────┘   └─────┘   └─────┘   └─────┘        ▲
        ▲         ▲         ▲         ▲           │
      4×1 MUX   4×1 MUX   4×1 MUX   4×1 MUX   serial-in
        ▲                                     (left shift)
     S₁ S₀  common to all four
```

**Mode table** — the thing to reproduce:

| S₁ | S₀ | Operation |
|---|---|---|
| 0 | 0 | no change (hold) |
| 0 | 1 | shift **right** (towards the LSB) |
| 1 | 0 | shift **left** (towards the MSB) |
| 1 | 1 | **parallel load** |

*(This is the ordering of the standard part, IC 74194.)*

**Serial inputs.** A shift vacates one end, and something must enter it: for a right shift the serial
input enters at **A₃** (the MSB end); for a left shift at **A₀**. *What* enters is not decided here —
it is decided by what you wire to that pin, and that single choice is what separates logical, circular
and arithmetic shifts in file 04. Note this now; file 04 spends a whole step on it.

> ✓ **Check 6.** (a) Why does this register need a 4-to-1 MUX per stage where step 5 needed 2-to-1?
> (b) Which stage receives the serial input during a right shift?
> (c) `[Mano 2-13]` A 4-bit register holds 1101 and is shifted right six times with serial input
> 101101 (first bit in first). Give the contents after each shift.
> (d) `[Mano 2-15]` A ring counter is this register with the serial output fed back to the serial
> input. Starting from 1000, list the states after each shift.

---

## Exam form

**Answer skeleton for every part of Q7 — 4 marks, ~80 words + a drawing:**

```
1. What it does            one sentence
2. The circuit             drawn from basic gates, labelled
3. The table               truth table / function table / mode table
4. Why                     one sentence linking circuit to table
```

| Part | Circuit is | Table to give | The "why" sentence |
|---|---|---|---|
| (i) D flip-flop | clocked SR latch + 1 inverter | Q(t+1) = D | the inverter makes S and R always opposite, so the forbidden state cannot occur |
| (ii) 3-to-8 decoder | 3 inverters + eight 3-input ANDs (+ enable) | input code → one active output | each AND gate realises one minterm |
| (iii) 4-to-1 MUX | 2 inverters + four 3-input ANDs + one 4-input OR | S₁S₀ → Y = Iᵢ | the select lines enable exactly one AND; the OR collects it |
| (iv) Quadruple 2×1 MUX | four 2-to-1 MUXes, shared S and E | E,S → Y = A or B | it selects a 4-bit **word**, not a bit |
| (v) Register with parallel load | 4 D FFs + a 2-to-1 MUX per D input | LD = 0 hold, LD = 1 load | LD = 0 feeds each output back to its own input, so the tick rewrites the same value |
| (vi) Bidirectional shift register | 4 D FFs + a 4-to-1 MUX per D input | S₁S₀: 00 hold, 01 right, 10 left, 11 load | each MUX chooses between self, left neighbour, right neighbour and external input |

**Counting rules worth memorising** (they generate half the marks in this unit and the next):

- n-to-2ⁿ decoder → **2ⁿ AND gates of n inputs, n inverters**
- k-to-1 MUX → **⌈log₂ k⌉ select lines**
- to select among **k sources, n bits wide** → **n MUXes, each k-to-1**

---

## Attempt

`[A1 Q7]` in full, on paper, 80 words and one drawing per part, in this order (easiest first):
(i) D flip-flop → (ii) decoder → (iii) 4-to-1 MUX → (iv) quadruple 2×1 MUX → (v) register with
parallel load → (vi) bidirectional shift register.

Then, from Mano: **2-6** (5-to-32 decoder), **2-8** (16-to-1 MUX), **2-13** (six right shifts),
**2-15** (ring counter).

---

## Traps

| Trap | Correction |
|---|---|
| Quadruple 2×1 MUX = 4-to-1 MUX | One picks a **word** from two sources; the other picks a **bit** from four |
| Building parallel load by ANDing LD with the clock | Clock skew. Gate the **data** with a MUX, not the clock |
| "With LD = 0 the register is not clocked" | It *is* clocked, every cycle — it loads its own output |
| Drawing a shift register with no serial input | A shift always vacates one end; the serial input must be drawn |
| Confusing shift-right direction | Shift **right** = towards the LSB; the serial input enters at the **MSB** end |
| Circuit with no explanation (or vice versa) | He asks for both. Half the circuit + the table + one "why" sentence beats a perfect drawing alone |
| A latch called a flip-flop | A latch is transparent while the clock is high; a flip-flop samples once at the edge |

---

## Self-test

1. How many AND gates, and of how many inputs, in a 4-to-16 decoder?
2. You must choose between **eight** 16-bit registers. How many MUXes, and of what size?
3. Why does the register in step 5 need feedback wires that the plain 4-flip-flop register did not?
4. A bidirectional shift register holds 1011 with S₁S₀ = 01 and serial input 0. What does it hold
   after one tick?
5. Which of the six circuits in Q7 contains a decoder inside it, and why?
6. Name the one design rule about clocks that step 5 exists to teach.

---
---

## Answers

**Check 1.** (a) D is fed to S and D′ to R, so S and R are always opposite — S = R = 1 is unreachable.
(b) **16**. (c) A latch is transparent for as long as the clock level is active and can change output
repeatedly within one clock period; a flip-flop samples its input once, at the clock edge.

**Check 2.** (a) 2¹² = **4096**. (b) The **two high-order bits** (A₄A₃) drive the 2-to-4 decoder, whose
four outputs are the **enables** of the four 3-to-8 decoders; the **three low-order bits** (A₂A₁A₀) go
to all four 3-to-8 decoders in parallel. Exactly one 3-to-8 block is enabled, and it activates one of
its eight outputs → one of 32. (c) Exactly **one**.

**Check 3.** (a) **4** (2⁴ = 16). (b) Split the 16 inputs 8 + 8 into the two 8-to-1 MUXes, driven by the
three low select bits S₂S₁S₀; feed their two outputs into the 2-to-1 MUX driven by the top bit S₃.
(c) A **decoder** — the select lines are decoded to enable exactly one AND gate.

**Check 4.** (a) A 4-to-1 MUX selects one **bit** out of four sources; a quadruple 2-to-1 MUX selects
one **4-bit word** out of two sources. (b) **8 MUXes** (one per bit), each **4-to-1** (one input per
register). (c) Because all four bits must come from the *same* source — a per-bit select would mix
halves of two different words, which is never what you want.

**Check 5.** (a) The gate delays the clock for this register only, so it captures later than every
other register; in a synchronous machine all registers must capture on the same edge. (b) Its **own
output**, fed back through the MUX — so the stored value is unchanged. (c) Add a third input to the
MUX (making it a 3-to-1) wired to constant 0, or AND each flip-flop's D input with CLR′ — either way
the clear takes effect **at the clock edge**, which is what makes it *synchronous*.

**Check 6.** (a) Four choices need two select lines and a 4-input selector; step 5 had only two
choices. (b) **A₃**, the MSB end. (c) Start 1101; each shift drops A₀ and takes one serial bit into A₃, using
101101 in order:

| Shift | Serial in | Register | Bit out |
|---|---|---|---|
| — | — | 1101 | — |
| 1 | 1 | **1110** | 1 |
| 2 | 0 | **0111** | 0 |
| 3 | 1 | **1011** | 1 |
| 4 | 1 | **1101** | 1 |
| 5 | 0 | **0110** | 1 |
| 6 | 1 | **1011** | 0 |

(d) 1000 → 0100 → 0010 → 0001 → 1000 — it cycles with period 4,
one 1 circulating. That is why it is called a ring counter.

**Self-test 1.** **16 AND gates, 4 inputs each** (plus 4 inverters).

**Self-test 2.** **16 MUXes** (one per bit), each **8-to-1** (3 select lines).

**Self-test 3.** Without feedback, LD = 0 would leave the D inputs undefined or capture whatever is on
the input lines. The feedback path gives the flip-flop something correct to reload — itself.

**Self-test 4.** S₁S₀ = 01 is shift right; serial input 0 enters at the MSB. 1011 → **0101**.

**Self-test 5.** The **multiplexers** (iii, iv, and the MUXes inside v and vi) — the select lines are
decoded internally to enable exactly one AND gate.

**Self-test 6.** **Never gate the clock.** Control *what a flip-flop loads*, never *whether it ticks*.

---

## What to do next

File 03 is where these parts get used: the MUXes of steps 3 and 4 become the **common bus**, and the
registers of steps 5 and 6 become AC, PC, AR and DR. It is the highest-value file in the pack — every
file after it depends on it.
