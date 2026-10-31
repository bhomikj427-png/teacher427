# Exp 13 · FSM: overlapping sequence detector (1010, and 101), and an asynchronous circuit

<div class="sub">Manual pp. 15–18 (second numbering) · ICs 7473, 7404, 7408, 7411, 7432, 7486 (and 7474 for the 101 version) · both detectors checked on 300 random input streams each</div>

[[map:11 Counters > 12 Shift registers > 13 FSM > 14 TTL|here=3]]

:::q <span class="tag">Manual Exp 13, aim</span>
Design a sequence detector that detects an overlapping sequence 1010 from an input sequence. (The list of experiments says **101**, so both are given.) Viva form: "Mealy or Moore? And what does *overlapping* change in the state diagram?"
:::

:::guess Guess first
After 1010 is detected, which earlier state does the machine return to, and why not the start?
:::

## 1010 detector (the manual's design)

[[fig:fsm1010|Mealy state diagram. Each state remembers the longest useful suffix seen. After 1010, the last "10" is already the start of the next 1010, so the machine goes to C, not A.|w=88]]

**State encoding** (manual): A = 00, B = 01, C = 11, D = 10 (bits = flip-flop A, flip-flop B). With 7473 JK flip-flops, the K-maps give:

$$J_{A} = BX'    K_{A} = BX' + B'X = B ⊕ X    J_{B} = X + A    K_{B} = A    Z = AB'X'$$

| Signal | Wiring (7473: FF A = J 14, K 3, Q 12, Q' 13, CLK 1, CLR' 2; FF B = J 7, K 10, Q 9, Q' 8, CLK 5, CLR' 6) |
|---|---|
| X' | 7404: X → 1 → 2 |
| J_{A} | 7408: QB (9) → 1, X' → 2 → 3 → 7473-14 |
| K_{A} | 7486: QB → 1, X → 2 → 3 → 7473-3 |
| J_{B} | 7432: X → 1, QA (12) → 2 → 3 → 7473-7 |
| K_{B} | QA (12) → 7473-10 |
| **Z** | 7411: QA → 1, QB' (8) → 2, X' → 13 → **12 = Z** |
| clock, clear | pins 1, 5 ← pulser; pins 2, 6 ← clear; VCC 4, GND 11 |

**Running it:**

1. Clear to A.
2. For each bit: set X, **read Z first** (Mealy: Z depends on the present X), then pulse the clock.
3. Input 1, 0, 1, 0, 1, 0 gives Z = 0, 0, 0, **1**, 0, **1**. The second detection uses the overlap.

## 101 detector (the version in the experiment list)

States: S0 = nothing (00), S1 = seen "1" (01), S2 = seen "10" (10). With D flip-flops (7474), the logic shrinks to:

$$D_{1} = Q_{0}X'    D_{0} = X    Z = Q_{1}X$$

(JK form: J_{1} = Q_{0}X', K_{1} = 1, J_{0} = X, K_{0} = X'.)

**Wiring:**

- 7474: FF1 holds Q1 (D 2, Q 5), FF2 holds Q0 (D 12, Q 9).
- X → 7474-12. 7408: Q0 (9) → 1, X' (7404) → 2 → 3 → 7474-2.
- Z: 7408: Q1 (5) → 4, X → 5 → **6**. CLK pins 3, 11; CLR' pins 1, 13 to clear; PR' 4, 10 HIGH.

Input 1, 0, 1, 0, 1 gives Z = 0, 0, **1**, 0, **1** (overlap: the final 1 of one "101" starts the next).

## (ii) Fundamental-mode asynchronous circuit

Spec: Z follows X while Y = 1; Z holds while Y = 0. The manual reduces the six-state flow table to two states, giving

$$F^{+} = XY + FY'    Z = F$$

That is a gated D latch, with Y as the enable.

**Wiring:**

- 7408: X → 1, Y → 2 → 3 (XY).
- 7404: Y → 1 → 2 (Y').
- 7408: F → 4, Y' → 5 → 6 (FY').
- 7432: 7408-3 → 1, 7408-6 → 2 → **3 = F**, which is fed back to 7408-4. Z = F.

:::trap Trap: the latch can drop out
With X = F = 1 and Y switching 1 → 0, the XY term turns off a moment before FY' turns on (the inverter delay). F can glitch to 0 and the latch loses its 1: a static-1 hazard. The cure is the consensus term **XF**: F⁺ = XY + FY' + XF. It is the same function (checked), and hazard-free.
:::

:::write Write in your record
**Result:** the overlapping 1010 Mealy detector (J_{A} = BX', K_{A} = B ⊕ X, J_{B} = X + A, K_{B} = A, Z = AB'X') produced Z = 1 at the 4th and 6th bits of 101010. The 101 detector (D_{1} = Q_{0}X', D_{0} = X, Z = Q_{1}X) produced Z = 1 at the 3rd and 5th bits of 10101. The asynchronous circuit F⁺ = XY + FY' transferred X to Z when Y = 1 and held it when Y = 0.

**Theory for the record:** a finite state machine has a finite set of states held in flip-flops. The next state depends on the present state and the inputs. In a Mealy machine the output depends on the state and the input; in a Moore machine on the state only. Design steps: state diagram → state table → state assignment → flip-flop excitation table → K-map minimisation → circuit. An overlapping detector returns, after a match, to the state for the longest suffix of the sequence that is also its prefix. A fundamental-mode asynchronous circuit has no clock: one input changes at a time and the circuit settles, and hazards must be removed with consensus terms.
:::

:::check Check 1
(a) Make the 1010 detector non-overlapping: where does the "0/1" arrow from D go? (b) Why must you read Z before pulsing the clock in a Mealy machine? (c) Moore version of 101: how many states?
:::

<!--ANSWERS-->

## Answers

**Opening question.** **Mealy** (Z = AB'X' uses the input X). After 1010 the machine goes to **C** ("10" seen), not A, because the trailing "10" can begin the next 1010. That is what *overlapping* means.

**Check 1.** (a) To **A** (start), so a match has to begin from scratch. (b) Z is a function of the present input. After the clock edge the state has moved on, and Z refers to the next bit. (c) **4**: S0, "1", "10", "101". The detection state is an extra state whose output is 1.

<!--/ANSWERS-->
