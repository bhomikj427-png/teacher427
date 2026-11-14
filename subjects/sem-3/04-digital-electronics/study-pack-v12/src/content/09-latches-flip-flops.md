# 09 — Latches and flip-flops

<div class="sub">Deck 08 (slides 6–40) · mid-term 2025 Q3 (2 marks) · practice set 2 Q1 · syllabus Unit 3 · needs 01 (NOR and NAND gates)</div>

## Map

[[map:1 Latches > 2 Flip-flops > 3 Excitation tables, conversion|here=1]]

Every circuit in 01–08 forgets its inputs the moment they change. A **sequential** circuit remembers: its output depends on the present inputs and on what came before. Memory comes from feeding a gate's output back to its input.

## The questions this file answers

- <span class="tag">Deck 08 slides 6–21</span> Draw a NOR SR latch, give its table, and explain why S = R = 1 is not allowed.
- <span class="tag">MTE 2025 Q3 · 2 marks</span> What excitation input should be applied to a T flip-flop to make its output toggle?
- <span class="tag">Set 2 Q1</span> Design a D flip-flop using SR, JK and T flip-flops and suitable gates.

---

## Build

### 1 · Latches

:::q <span class="tag">Deck 08 slides 6–21</span>
Draw an SR latch using NOR gates and give its output for every input combination. Why is S = R = 1 not allowed?
:::

:::guess Guess first
With S = R = 0 the circuit can sit with Q = 0 or Q = 1. What decides which?
:::

:::note Terms
**Latch:** a circuit with two stable states that stores one bit. **Set:** make Q = 1. **Reset:** make Q = 0. **Q':** the second output, normally the complement.
:::

[[fig:sr_latch|NOR SR latch.|w=50]]

| S R | Q | Action |
|---|---|---|
| 0 0 | unchanged | hold (memory) |
| 0 1 | 0 | reset |
| 1 0 | 1 | set |
| 1 1 | Q = Q' = 0 | not allowed |

**How it remembers.** S = 1 forces Q' = 0, so the upper gate sees two 0s and Q = 1. Return S to 0: Q = 1 is fed back and keeps Q' = 0. The loop holds the last value set.

| Latch | What it adds |
|---|---|
| NAND SR | active-low inputs: S' = 0 sets, R' = 0 resets, 11 holds, 00 forbidden (Q = Q' = 1) |
| Gated SR | an enable EN: changes only while EN = 1 |
| D latch | S = D, R = D': no forbidden case. EN = 1: Q follows D (transparent); EN = 0: holds |

**Answer.** S = R = 1 forces both outputs to 0, so they are no longer complements. If S and R then return to 0 together, both gates race to 1 and the final state depends on which is faster: unpredictable.

:::check Check 1
(a) A NAND latch has S' = 0, R' = 1. Q? (b) A D latch has EN = 1 throughout while D goes 0 → 1 → 0 → 1. How many times does Q change? (c) What must a circuit have to store a bit?
:::

### 2 · Flip-flops

:::q <span class="tag">MTE 2025 Q3 · 2 marks</span>
What excitation input should be applied to a T-FF to make output toggle?
:::

:::guess Guess first
A latch is open for as long as its enable is 1. What could go wrong if a latch's output fed, through logic, back into its own input?
:::

:::note Terms
**Clock (CLK):** a square wave telling every memory element when to update. **Edge:** rising (0 → 1) or falling (1 → 0). **Flip-flop:** a 1-bit memory that updates only at a clock edge. **Toggle:** change to the opposite value.
:::

[[fig:latch_vs_ff|Same D, same clock: the latch follows D (glitch included) while EN = 1; the flip-flop samples only at ↑.|w=75]]

In a synchronous system every flip-flop changes at the same instant, so signals are steady when read: hence flip-flops, not latches.

[[fig:ff_symbols|SR, JK, D and T flip-flop symbols.|w=75]]

| J K | Q⁺ (JK) | D | Q⁺ (D) | T | Q⁺ (T) |
|---|---|---|---|---|---|
| 0 0 | Q (hold) | 0 | 0 | 0 | Q (hold) |
| 0 1 | 0 (reset) | 1 | 1 | 1 | Q' (toggle) |
| 1 0 | 1 (set) | | | | |
| 1 1 | Q' (toggle) | | | | |

Characteristic equations: Q⁺ = JQ' + K'Q · Q⁺ = D · Q⁺ = T ⊕ Q. JK is SR with the forbidden 11 used for toggle; T is JK with J = K = T; D is JK with J = D, K = D'.

**Race-around.** In a level-triggered JK with J = K = 1, Q toggles, feeds back, and toggles again while CLK stays 1: the final value is unknown. Cures: **master–slave** (master open while CLK = 1, slave copies while CLK = 0) or **edge triggering**. **PRESET/CLEAR** act at once, without the clock, usually active-low.

[[fig:ms_jk|Master–slave JK flip-flop.|w=70]]

**Answer.** **T = 1**: Q⁺ = T ⊕ Q, so with T = 1 the output complements at every active edge.

:::check Check 2
(a) JK with J = K = 1 and Q = 0: Q after three edges? (b) T = 1 clocked at 1 kHz: frequency at Q? (c) CLEAR (active-low) goes to 0 between edges. When does Q change?
:::

### 3 · Excitation tables and conversion

:::q <span class="tag">Set 2 Q1</span>
Design a D flip-flop, using SR, JK & T flip-flop and suitable logic gates.
:::

:::guess Guess first
A D flip-flop must go to Q⁺ = D. For a T flip-flop, when exactly must it toggle?
:::

The **excitation table** reads the characteristic table backwards: to move Q → Q⁺, what must the inputs be? It drives every design from here on (13, 15).

| Q → Q⁺ | S R | J K | D | T |
|---|---|---|---|---|
| 0 → 0 | 0 X | 0 X | 0 | 0 |
| 0 → 1 | 1 0 | 1 X | 1 | 1 |
| 1 → 0 | 0 1 | X 1 | 0 | 1 |
| 1 → 1 | X 0 | X 0 | 1 | 0 |

The Xs are why JK usually gives the simplest logic. **Conversion:** (1) characteristic table of the wanted flip-flop; (2) beside each row, the excitation of the one you have; (3) K-map each input.

| D Q | Q⁺ | S R | J K | T |
|---|---|---|---|---|
| 0 0 | 0 | 0 X | 0 X | 0 |
| 0 1 | 0 | 0 1 | X 1 | 1 |
| 1 0 | 1 | 1 0 | 1 X | 1 |
| 1 1 | 1 | X 0 | X 0 | 0 |

**Answer.** From SR: **S = D, R = D'**. From JK: **J = D, K = D'**. From T: **T = D ⊕ Q** (one XOR fed by D and the flip-flop's own Q).

| Have → want | Logic | Have → want | Logic |
|---|---|---|---|
| SR → JK | S = JQ', R = KQ | D → JK | D = JQ' + K'Q |
| D → SR | D = S + R'Q | D → T | D = T ⊕ Q |
| JK → T | J = K = T | T → JK | T = JQ' + KQ |

:::check Check 3
(a) Give the JK excitation for 1 → 0 and explain the X. (b) Derive SR → JK from the tables.
:::

---

## Exam form

**Latch.** NOR SR circuit and table, how feedback stores, why 11 is forbidden; NAND version; D latch.

**Flip-flop.** Latch vs flip-flop; four characteristic tables and equations; race-around and its two cures; PRESET/CLEAR.

**Excitation and conversion.** The excitation table; the three-step conversion procedure with K-maps; the conversion table.

## Traps

- NAND latch inputs are active-low: 00 is the forbidden case, not 11.
- Using the characteristic table where the excitation table is needed.
- In T = D ⊕ Q, Q is the flip-flop's own output.
- Saying edge triggering "slows" the flip-flop: it only fixes when it samples.

## Self-test

1. A NOR SR latch gets S = 1, R = 0, then S = 0, R = 0. Q?
2. JK with J = 1, K = 0 and Q = 0: Q⁺?
3. Convert a T flip-flop into a JK flip-flop.
4. Write the characteristic equation of the JK flip-flop and check it against its table.
5. Why does a master–slave JK not race around?

<!--ANSWERS-->

## Answers

**Check 1.** (a) **Q = 1** (S' = 0 sets). (b) **Three times**: transparent. (c) **Feedback**: an output fed back to an input.

**Check 2.** (a) 0 → 1 → 0 → 1: **Q = 1**. (b) **500 Hz**. (c) **At once**, without waiting for an edge.

**Check 3.** (a) **J K = X 1**: K = 1 is needed; J = 0 is a reset and J = 1 a toggle, both reach 0. (b) Rows J K Q → Q⁺ → S R: 000 → 0, 0X; 001 → 1, X0; 010 → 0, 0X; 011 → 0, 01; 100 → 1, 10; 101 → 1, X0; 110 → 1, 10; 111 → 0, 01. K-maps: **S = JQ', R = KQ**.

**Self-test.**

1. **Q = 1** (set, then hold).
2. **Q⁺ = 1** (set).
3. **T = JQ' + KQ**.
4. Q⁺ = JQ' + K'Q: JK = 00 → Q; 01 → 0; 10 → Q' + Q = 1; 11 → Q'. ✓
5. Master and slave are never open together: the slave changes only after the master has closed, so the new Q cannot reach the inputs while they are being sampled.

<!--/ANSWERS-->
