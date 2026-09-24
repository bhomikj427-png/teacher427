# 06 — First-order transients

<div class="sub">Class notes p.19–23 · 3 board questions · needs 01 (what can't jump), 04 (R_{Th} for the time constant)</div>

## Map

[[map:1 The timeline: 0⁻, 0⁺, ∞ > 2 What each element becomes > 3 The one formula > 4 Time constant τ > 5 The switch that opens|here=1]]

## The questions this file answers

- <span class="tag">Class p.19–20</span> V, a switch that closes at t = 0, R: find I at 0⁻, 0⁺, ∞.
- <span class="tag">Class p.21</span> V, switch, R, L in series; the switch closes at t = 0: find I_{R} and I_{L} at 0⁻, 0⁺, ∞.
- <span class="tag">Class p.22–23</span> 10 V, switch (opens at t = 0), 1 kΩ, 1 mH: find I_{R} and I_{L} at 0⁻ and 0⁺.

---

## Build

### 1 · The timeline

:::q <span class="tag">Class p.19–20</span>
V, a switch that closes at t = 0, and R. Find I(0⁻), I(0⁺) and I(∞).
:::

[[fig:r_sw||w=35]]

:::guess Guess first
Is there any "transient" at all in this circuit, i.e. any gradual change?
:::

[[fig:timeline|Before the switch: the old steady state. From 0⁺ to about 5τ: the transient. After that: the new steady state.|w=85]]

- **t = 0⁻**: the instant **just before** the switch operates. Old steady state.
- **t = 0⁺**: the instant **just after**.
- **t = ∞**: long after (in practice about 5τ): new steady state.

For the resistor-only circuit: **I(0⁻) = 0** (switch open), **I(0⁺) = V/R**, **I(∞) = V/R**. The current jumps straight to its final value, because a resistor has no memory (class p.20: "a resistor allows sudden change").

So the Guess answer: **no transient**. A transient needs an element that stores energy, an L or a C.

### 2 · What each element becomes at 0⁺ and at ∞

:::q <span class="tag">Class p.21</span>
V, switch, R and L in series; the switch closes at t = 0. Find I_{R} and I_{L} at 0⁻, 0⁺ and ∞.
:::

[[fig:rl_close||w=50]]

:::guess Guess first
The switch has just closed. The source is pushing. Why can't the current be V/R at t = 0⁺?
:::

Two rules do all the work (from 01, step 5):

| Element | At 0⁺: it keeps its 0⁻ value | At ∞ (DC steady state) |
|---|---|---|
| **Inductor** | a **current source** of value i_{L}(0⁻); an **open circuit** if that value is 0 | **short circuit** |
| **Capacitor** | a **voltage source** of value v_{C}(0⁻); a **short circuit** if that value is 0 | **open circuit** |
| **Resistor** | no memory: whatever the rest of the circuit forces | same |

[[fig:rl_snaps|The three snapshots of the class p.21 circuit.|w=98]]

- **0⁻**: switch open, so I_{R}(0⁻) = I_{L}(0⁻) = **0**.
- **0⁺**: i_{L} can't jump, so I_{L}(0⁺) = 0 and the inductor acts as an **open**. In series, I_{R}(0⁺) = **0**.
- **∞**: the inductor is a **short**, so I(∞) = **V/R**.

The current must travel from 0 to V/R. How it travels is step 3.

:::check Check 1
Same circuit with a capacitor instead of the inductor (uncharged at 0⁻). Find I at 0⁺ and at ∞.
:::

### 3 · The one formula for every first-order circuit

Every circuit with **one** L or **one** C (after reduction) moves from its 0⁺ value to its ∞ value **exponentially**:

$$x(t) = x(∞) + [x(0⁺) − x(∞)]·e^{−t/τ}$$

The class p.22 box: valid for **RL ✓ and RC ✓**, not for **RLC ✗ or LC ✗** (those are second order: they can oscillate).

[[fig:xt_plot|After one τ the change is 63.2 % complete; after 5τ, 99.3 %. The initial slope would reach x(∞) in exactly one τ.|w=80]]

So a first-order question is always **three numbers**: x(0⁺), x(∞), τ. Then write the formula.

### 4 · The time constant τ

$$τ = \frac{L}{R}  (RL)      τ = RC  (RC)$$

**R is the Thévenin resistance seen by the L or C** (04), with independent sources switched off. It is the plain R only when the L or C sees a single resistor.

Class p.21 circuit with the p.22 values (V = 10 V, R = 1 kΩ, L = 1 mH): x(0⁺) = 0, x(∞) = 10 mA, τ = \frac{1 mH}{1 kΩ} = **1 µs**:

$$i(t) = 10(1 − e^{−t/1 µs}) mA$$

[[fig:rl_rise_plot|Confirmed by simulating the circuit step by step: at t = 3 µs both give 9.50 mA.|w=78]]

:::check Check 2
An RC circuit: R = 2 kΩ, C = 5 µF. Find τ, and the time after which it is "settled" (99 %).
:::

### 5 · The switch that opens

:::q <span class="tag">Class p.22–23</span>
10 V, a switch that opens at t = 0, 1 kΩ and 1 mH in series. Find I_{R} and I_{L} at 0⁻ and 0⁺.
:::

[[fig:rl_open||w=50]]

:::guess Guess first
At 0⁻ the loop is carrying current. At 0⁺ the switch is open. What must the inductor do, and where can its current go?
:::

- **0⁻**: switch closed, steady state, L = short: **I_{L}(0⁻) = 10 V / 1 kΩ = 10 mA** = I_{R}(0⁻).
- **0⁺**: the inductor current can't jump, so **I_{L}(0⁺) = 10 mA** ✓ (the professor's point).

:::trap Read this before writing I_{R}(0⁺) = 0
The notes give I_{R}(0⁺) = 0 alongside I_{L}(0⁺) = 10 mA. R and L are **in the same series loop**, so they must carry the **same** current. Both statements can't hold. With the switch open there is no path at all for the inductor's 10 mA. In an ideal circuit, di/dt → ∞ and the inductor voltage spikes. In a real one, the stored energy ½Li^{2} = ½ × 1 mH × (10 mA)^{2} = **50 nJ** arcs across the opening contacts.

**Ask the professor which path the current takes after t = 0.** Usually the full question has the switch move the R–L onto its own loop, or has a resistor across the switch.
:::

If the R–L loop is closed on itself after t = 0 (the usual version of this question):

[[fig:rl_discharge|Illustration, not the board circuit: the R–L loop with the source gone.|w=30]]

x(0⁺) = 10 mA, x(∞) = 0, τ = L/R = 1 µs:

$$i(t) = 10·e^{−t/1 µs} mA$$

[[fig:rl_decay_plot||w=78]]

---

## Exam form

**Procedure for any first-order switching question.**
1. **t = 0⁻**: old circuit, DC steady state (L = short, C = open). Find i_{L}(0⁻) or v_{C}(0⁻).
2. **t = 0⁺**: new circuit. L → current source i_{L}(0⁻); C → voltage source v_{C}(0⁻). Find the asked quantity.
3. **t = ∞**: new circuit, DC steady state (L = short, C = open).
4. **τ** = L/R_{Th} or R_{Th}C, with R_{Th} seen by the L or C.
5. x(t) = x(∞) + [x(0⁺) − x(∞)]e^{−t/τ}.

**Facts to state.** Inductor current and capacitor voltage cannot change instantaneously. Settling ≈ 5τ (99.3 %). 63.2 % of the change happens in one τ.

## Traps

- Using the ∞ circuit at 0⁺ (treating L as a short immediately).
- Calling i_{L}(0⁺) = 0 when the inductor was carrying current at 0⁻: it keeps its 0⁻ value, whatever it was.
- τ = L/R with the wrong R: it must be the Thévenin resistance the L sees.
- Using the first-order formula on an RLC circuit.

## Self-test

1. What does a capacitor look like at 0⁺ if it was uncharged? And at ∞?
2. Why is τ = L/R and not LR? Check with units: H/Ω = ?
3. RL circuit, i(0⁺) = 2 A, i(∞) = 0, τ = 5 ms. Write i(t). What is i at 10 ms?
4. After how many time constants is a transient 99 % done?
5. Why is there no transient in a purely resistive circuit?

<!--ANSWERS-->
## Answers

**Check 1.** Uncharged C = short at 0⁺, so I(0⁺) = **V/R**. At ∞ the C is open, so I(∞) = **0**. (The mirror image of the inductor.)

**Check 2.** τ = 2 kΩ × 5 µF = **10 ms**; settled after about 5τ = **50 ms**.

**Self-test.**

1. A **short** at 0⁺; an **open** at ∞.
2. H/Ω = (V·s/A)/(V/A) = **s**: L/R is a time. (LR has units Ω²·s, not a time.)
3. i(t) = **2e^{−t/5 ms} A**; at 10 ms, i = 2e^{−2} = **0.27 A**.
4. About **5τ** (99.3 %); 4.6τ gives exactly 99 %.
5. A resistor stores no energy, so nothing needs time to build up or run down: every quantity jumps straight to its final value.
<!--/ANSWERS-->
