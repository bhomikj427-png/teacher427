# Exps 9–10 · Flip-flops from NAND gates; 7474 and 7473; flip-flop conversion

<div class="sub">Manual pp. 4–8 (second numbering) · ICs 7400, 7410, 7474, 7473 · use the trainer's debounced pulser as the clock</div>

[[map:6–8 MUX, DEMUX, decoder > 9 Flip-flops (gates) > 10 Flip-flop ICs > 11–12 Counters & shift registers|here=2]]

:::q <span class="tag">Manual Exps 9–10</span>
Study SR, JK and T flip-flops built from NAND gates, the 7474 (positive-edge D, preset and clear) and the 7473 (negative-edge JK, clear), and conversions SR → D, D → SR. Viva form: "Your NAND JK flip-flop with J = K = 1 ends in a random state. Why, and how do the ICs avoid it?"
:::

:::guess Guess first
The gate JK is *level*-triggered: it reacts for as long as CLK = 1. What happens if Q flips while CLK is still 1?
:::

## Exp 9 · From gates

**Clocked SR (Fig 9.1), one 7400:**

- G1 = NAND(S, CLK): 1, 2 → 3.
- G2 = NAND(R, CLK): 4, 5 → 6.
- G3 = NAND(G1, Q'): 3 → 9, 11 → 10 → **8 = Q**.
- G4 = NAND(G2, Q): 6 → 12, 8 → 13 → **11 = Q'**.

| CLK | S R | Q_{n+1} |
|---|---|---|
| 0 | x x | Q_{n} (hold) |
| 1 | 0 0 | Q_{n} |
| 1 | 0 1 | 0 |
| 1 | 1 0 | 1 |
| 1 | 1 1 | **invalid** (Q = Q' = 1, then unpredictable when CLK falls) |

**JK (Fig 9.2):** feed Q' back into the J gate and Q into the K gate. That makes S = R = 1 impossible, and J = K = 1 toggles instead.

- 7410: J → 1, CLK → 2, Q' → 13 → 12; K → 3, CLK → 4, Q → 5 → 6.
- 7400 latch: 7410-12 → 1, Q' → 2 → **3 = Q**; 7410-6 → 4, Q → 5 → **6 = Q'**.

| CLK pulse | J K | Q_{n+1} |
|---|---|---|
| ↑ rising | 0 0 | Q_{n} |
| ↑ rising | 0 1 | 0 |
| ↑ rising | 1 0 | 1 |
| ↑ rising | 1 1 | Q_{n}' (toggle) |

:::trap Race-around
This JK is level-triggered. With J = K = 1, it toggles, the new Q feeds back, and it toggles again, as many times as fit inside one CLK-high time. The final state on the trainer is random. Edge-triggered ICs (7473, 7474) and master-slave designs act only at a clock **edge**, so each pulse gives exactly one toggle.
:::

**T flip-flop (Fig 9.3):** tie J = K = T. T = 0 holds; T = 1 toggles on every clock.

## Exp 10 · Flip-flop ICs

[[fig:pin7474|7474: two positive-edge D flip-flops with active-LOW preset and clear.|w=42]]

**7474 (FF 1):** CLR' 1, D 2, CLK 3, PR' 4, Q 5, Q' 6.

| PR' | CLR' | CLK | D | Q Q' |
|---|---|---|---|---|
| 0 | 1 | x | x | 1 0 (preset, ignores clock) |
| 1 | 0 | x | x | 0 1 (clear) |
| 0 | 0 | x | x | 1 1 (not allowed) |
| 1 | 1 | ↑ rising | 1 | 1 0 |
| 1 | 1 | ↑ rising | 0 | 0 1 |
| 1 | 1 | 0 | x | Q_{n} Q_{n}' |

[[fig:pin7473|7473: two negative-edge JK flip-flops with active-LOW clear. VCC = pin 4, GND = pin 11.|w=42]]

**7473 (FF 1):** CLK 1, CLR' 2, K 3, J 14, Q 12, Q' 13. **Table 10.2, filled:**

| CLR' | CLK | J K | Q_{n+1} | Q_{n+1}' |
|---|---|---|---|---|
| 0 | x | x x | 0 | 1 |
| 1 | ↓ falling | 0 0 | Q_{n} | Q_{n}' |
| 1 | ↓ falling | 1 0 | 1 | 0 |
| 1 | ↓ falling | 0 1 | 0 | 1 |
| 1 | ↓ falling | 1 1 | Q_{n}' | Q_{n} (toggle) |
| 1 | 1 (no edge) | x x | Q_{n} | Q_{n}' |

**Conversions:**

| Want | Using | Logic |
|---|---|---|
| D from SR (Fig 10.1) | S = D, R = D' | 7404 inverts D for R |
| SR from D (Fig 10.2) | D = S + R'Q | 7404 (R'), 7408 (R'·Q), 7432 (+S) into the 7474's D; Q fed back |
| JK from T (exercise) | T = JQ' + KQ | |
| T from D (exercise) | D = T ⊕ Q | one 7486 |
| SR from JK (exercise) | J = S, K = R | S = R = 1 must still be avoided |
| SR from NOR (exercise) | cross-coupled NORs | active-HIGH inputs; S = R = 1 forbidden |

:::write Write in your record
**Result:** the truth tables of the NAND-gate SR, JK and T flip-flops and of the 7474 (positive-edge D, PR'/CLR') and 7473 (negative-edge JK, CLR') were verified. SR → D (S = D, R = D') and D → SR (D = S + R'Q) conversions were verified.

**Theory for the record:** a flip-flop is a 1-bit memory element. The clocked SR flip-flop has an invalid state for S = R = 1. The JK removes it by feedback, giving toggle for J = K = 1. A level-triggered JK suffers race-around, which edge triggering or master-slave construction prevents. The D flip-flop copies D at the clock edge; the T flip-flop toggles when T = 1. Preset and clear are asynchronous, active-LOW inputs that override the clock. Conversion uses the excitation table of the available flip-flop to find its inputs in terms of the desired inputs and Q.
:::

:::check Check 1
(a) On the 7473, CLR' = 1, J = K = 1, Q = 0. Give Q after three clock pulses. (b) Why do you see no change on the 7474 while you hold the pulser down? (c) Derive D for a T flip-flop from the D excitation (D = Q_{n+1}).
:::

<!--ANSWERS-->

## Answers

**Opening question.** Race-around: with J = K = 1 and a long CLK-high, the gate JK toggles repeatedly through its own feedback, so the final state is random. ICs trigger on a clock **edge** (7474 ↑, 7473 ↓), so they change once per pulse.

**Check 1.** (a) It toggles each falling edge: 0 → 1 → 0 → **1**. (b) The 7474 acts only on the **rising** edge, which happens when you press. Holding the button is a steady level, so nothing more happens. (A 7473 acts on the release, the falling edge.) (c) Q_{n+1} = Q_{n} when T = 0 and Q_{n}' when T = 1, so **D = T ⊕ Q**.

<!--/ANSWERS-->
