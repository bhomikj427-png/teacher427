# 08 — First-order transients

<div class="sub">Class notes p.19–23, set 2 p.15–22 · MTE syllabus item 6 (step-wise, Laplace, test signals) · 4 board questions + 2 textbook · needs 01 (what can't jump), 06 (R_{Th} for the time constant)</div>

## Map

[[map:1 Timeline 0⁻, 0⁺, ∞ > 2 What each element becomes > 3 The one formula > 4 Time constant τ > 5 The switch that opens > 6 Laplace route > 7 Test signals δ, u, r|here=1]]

## The questions this file answers

- <span class="tag">Class p.19–20</span> V, a switch that closes at t = 0, R: find I at 0⁻, 0⁺, ∞.
- <span class="tag">Class p.21</span> V, switch, R, L in series; the switch closes at t = 0: find I_{R} and I_{L} at 0⁻, 0⁺, ∞.
- <span class="tag">Set 2 p.20–21</span> V, switch (closes at t = 0), R, C in series: find v_{C}, v_{R} and I at 0⁻, 0⁺, ∞.
- <span class="tag">Class p.22–23 · set 2 p.18–19</span> 10 V, switch (opens at t = 0), 1 kΩ, 1 mH: find I_{R} and I_{L} at 0⁻ and 0⁺.
- <span class="tag">textbook</span> The class RL circuit solved by Laplace; RC responses to δ(t), u(t), r(t).

---

## Build

### 1 · The timeline

:::q <span class="tag">Class p.19–20 · set 2 p.15–16</span>
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

:::q <span class="tag">Class p.21 · set 2 p.17</span>
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

:::q <span class="tag">Set 2 p.20–21</span>
V, a switch that closes at t = 0, R and C in series (C uncharged). Find v_{C}, v_{R} and I at 0⁻, 0⁺ and ∞.
:::

[[fig:rc_close||w=50]]

The mirror image of the inductor:

- **0⁻**: switch open, steady state: v_{C}(0⁻) = 0, v_{R}(0⁻) = 0, I = 0.
- **0⁺**: **v_{C}(0⁺) = v_{C}(0⁻) = 0**. The class writes it as the rule to remember: "v_{C}(0⁻) = v_{C}(0⁺), always". So the capacitor acts as a **short**, the whole V is across R: v_{R}(0⁺) = V, **I(0⁺) = V/R**. The current jumps; the capacitor voltage does not.
- **∞**: I = C·\frac{dv_{C}}{dt} = 0 because v_{C} is constant, so the capacitor is an **open** (set 2 p.21): **I(∞) = 0, v_{C}(∞) = V, v_{R}(∞) = 0**.

:::check Check 1
Same RC circuit, but C was charged to 4 V (+ at the top) before t = 0, with V = 10 V and R = 1 kΩ. Find I(0⁺) and I(∞).
:::

### 3 · The one formula for every first-order circuit

Every circuit with **one** L or **one** C (after reduction) moves from its 0⁺ value to its ∞ value **exponentially**:

$$x(t) = x(∞) + [x(0⁺) − x(∞)]·e^{−t/τ}$$

The class p.22 box: valid for **RL ✓ and RC ✓**, not for **RLC ✗ or LC ✗** (those are second order: they can oscillate).

[[fig:xt_plot|After one τ the change is 63.2 % complete; after 5τ, 99.3 %. The initial slope would reach x(∞) in exactly one τ.|w=80]]

So a first-order question is always **three numbers**: x(0⁺), x(∞), τ. Then write the formula.

### 4 · The time constant τ

$$τ = \frac{L}{R}  (RL)      τ = RC  (RC)$$

**R is the Thévenin resistance seen by the L or C** (06), with independent sources switched off. It is the plain R only when the L or C sees a single resistor.

Class p.21 circuit with the p.22 values (V = 10 V, R = 1 kΩ, L = 1 mH): x(0⁺) = 0, x(∞) = 10 mA, τ = \frac{1 mH}{1 kΩ} = **1 µs**:

$$i(t) = 10(1 − e^{−t/1 µs}) mA$$

[[fig:rl_rise_plot|Confirmed by simulating the circuit step by step: at t = 3 µs both give 9.50 mA.|w=78]]

:::check Check 2
An RC circuit: R = 2 kΩ, C = 5 µF. Find τ, and the time after which it is "settled" (99 %).
:::

### 5 · The switch that opens

:::q <span class="tag">Class p.22–23 · set 2 p.18–19</span>
10 V, a switch that opens at t = 0, 1 kΩ and 1 mH in series. Find I_{R} and I_{L} at 0⁻ and 0⁺.
:::

[[fig:rl_open||w=50]]

:::guess Guess first
At 0⁻ the loop is carrying current. At 0⁺ the switch is open. What must the inductor do, and where can its current go?
:::

- **0⁻**: switch closed, steady state, L = short: **I_{L}(0⁻) = 10 V / 1 kΩ = 10 mA** = I_{R}(0⁻).
- **0⁺**: the inductor current can't jump, so **I_{L}(0⁺) = 10 mA** ✓ (the professor's point).

:::trap Read this before writing I_{R}(0⁺) = 0
Both sets of notes give I_{R}(0⁺) = 0 alongside I_{L}(0⁺) = 10 mA (set 2 p.19 draws the inductor as a 10 mA source). R and L are **in the same series loop**, so they must carry the **same** current. Both statements can't hold. With the switch open there is no path at all for the inductor's 10 mA. In an ideal circuit, di/dt → ∞ and the inductor voltage spikes. In a real one, the stored energy ½Li^{2} = ½ × 1 mH × (10 mA)^{2} = **50 nJ** arcs across the opening contacts.

**Ask the professor which path the current takes after t = 0.** Usually the full question has the switch move the R–L onto its own loop, or has a resistor across the switch.
:::

If the R–L loop is closed on itself after t = 0 (the usual version of this question):

[[fig:rl_discharge|Illustration, not the board circuit: the R–L loop with the source gone.|w=30]]

x(0⁺) = 10 mA, x(∞) = 0, τ = L/R = 1 µs:

$$i(t) = 10·e^{−t/1 µs} mA$$

[[fig:rl_decay_plot||w=78]]

### 6 · The Laplace route

:::q <span class="tag">textbook</span>
Solve the class p.21 circuit (10 V switched onto 1 kΩ and 1 mH at t = 0) by Laplace transform.
:::

:::guess Guess first
The answer is already known from step 4. What should the Laplace working give back, and at which step does the "1 − e" shape appear?
:::

The step-wise method needs the exponential shape to be known in advance. Laplace **derives** it: it turns d/dt into multiplication by s, so the circuit's differential equation becomes algebra.

**Pairs you need** (the 06-KB table; the full list is in step 7):

| f(t) | F(s) |
|---|---|
| δ(t) | 1 |
| u(t) (a DC source switched on at 0) | \frac{1}{s} |
| t·u(t) | \frac{1}{s^{2}} |
| e^{−at}u(t) | \frac{1}{s + a} |
| \frac{df}{dt} | sF(s) − f(0⁻) |

**Elements in the s-domain.** R → R. L → sL. C → \frac{1}{sC}. Energy stored at t = 0⁻ becomes a source in series:

[[fig:sdomain|Current enters the top terminal. The inductor's initial current appears as a voltage source L·i_{L}(0⁻); the capacitor's initial voltage as v_{C}(0⁻)/s.|w=80]]

**The class circuit.** i_{L}(0⁻) = 0, so no initial source. The 10 V switched on at t = 0 is 10·u(t) → \frac{10}{s}. KVL in s:

$$\frac{10}{s} = (R + sL)·I(s)  ⇒  I(s) = \frac{10}{s(1000 + 0.001s)} = \frac{10^{4}}{s(s + 10^{6})}$$

**Partial fractions:** \frac{10^{4}}{s(s + 10^{6})} = \frac{A}{s} + \frac{B}{s + 10^{6}}, with A = \frac{10^{4}}{10^{6}} = 0.01 and B = −0.01:

$$I(s) = \frac{0.01}{s} − \frac{0.01}{s + 10^{6}}  ⇒  i(t) = 0.01(1 − e^{−10^{6}t}) A = 10(1 − e^{−t/1 µs}) mA$$

The same answer as step 4. The "1 − e" comes from the two partial fractions: 1/s gives the final value, 1/(s + 1/τ) gives the decaying part. The pole at s = −10^{6} = −\frac{1}{τ} **is** the time constant.

**With stored energy.** The step 5 decay (R–L loop, i_{L}(0⁻) = 10 mA, no source): KVL with the initial-current source, 0 = (R + sL)I(s) − L·i_{L}(0⁻), so

$$I(s) = \frac{i_{L}(0⁻)}{s + R/L} ⇒ i(t) = 10e^{−t/1 µs} mA$$

**Quick checks without inverting** (final- and initial-value theorems): i(∞) = lim_{s→0} sI(s) = \frac{10^{4}}{10^{6}} = 10 mA ✓; i(0⁺) = lim_{s→∞} sI(s) = 0 ✓. The final-value theorem only holds if the response settles (no poles on the jω axis or to the right).

:::check Check 3
Write I(s) for 10 V switched onto R = 2 kΩ and C = 1 µF in series (C uncharged), and invert it.
:::

### 7 · Standard test signals: δ(t), u(t), r(t)

:::guess Predict
A step is the integral of an impulse. If you know how a circuit responds to an impulse, how could you get its step response without solving again?
:::

The class list (set 2 p.22), with its everyday examples:

[[fig:test_signals|The three test signals and their Laplace transforms.|w=90]]

| Signal | Definition | ℒ | Class example | Tests… |
|---|---|---|---|---|
| **unit impulse δ(t)** | zero except at t = 0; area ∫ δ(t) dt = 1 | 1 | a kitchen lighter's spark, a bike's spark plug | the response to a sudden kick |
| **unit step u(t)** | 0 for t < 0, 1 for t > 0 | \frac{1}{s} | a switch closing | the response to a sudden constant input |
| **unit ramp r(t)** | t·u(t) | \frac{1}{s^{2}} | pressing an accelerator | tracking a steadily rising input: the "toughest" test signal (class) |

They are linked: δ(t) = \frac{du}{dt} and u(t) = \frac{dr}{dt}. So in a linear circuit **the step response is the integral of the impulse response**, and the ramp response is the integral of the step response. The Predict answer: integrate.

:::q <span class="tag">textbook</span>
RC circuit: R = 1 kΩ, C = 1 µF (τ = RC = 1 ms), initially uncharged, output v_{C}. Find v_{C}(t) for a unit impulse, a unit step and a unit ramp at the input.
:::

Voltage divider in s: V_{C}(s) = V_{in}(s)·\frac{1/sC}{R + 1/sC} = V_{in}(s)·\frac{1}{1 + sτ}.

| Input | V_{C}(s) | Partial fractions | v_{C}(t) |
|---|---|---|---|
| δ(t) | \frac{1}{1 + sτ} | \frac{1/τ}{s + 1/τ} | **\frac{1}{τ}e^{−t/τ}** |
| u(t) | \frac{1}{s(1 + sτ)} | \frac{1}{s} − \frac{1}{s + 1/τ} | **1 − e^{−t/τ}** |
| r(t) | \frac{1}{s^{2}(1 + sτ)} | \frac{1}{s^{2}} − \frac{τ}{s} + \frac{τ}{s + 1/τ} | **t − τ + τe^{−t/τ}** |

[[fig:rc_test_plot|All three checked by simulating the circuit: at t = 1 ms and 3 ms the simulated and formula values agree.|w=92]]

Read the ramp result: after the transient dies, v_{C} = t − τ. The output follows the input with a **constant lag of τ = 1 ms** that never goes away. That permanent error is why the ramp is called the toughest test.

:::check Check 4
Differentiate the step response 1 − e^{−t/τ}. Which response do you get?
:::

---

## Exam form

**Procedure for any first-order switching question.**
1. **t = 0⁻**: old circuit, DC steady state (L = short, C = open). Find i_{L}(0⁻) or v_{C}(0⁻).
2. **t = 0⁺**: new circuit. L → current source i_{L}(0⁻); C → voltage source v_{C}(0⁻). Find the asked quantity.
3. **t = ∞**: new circuit, DC steady state (L = short, C = open).
4. **τ** = L/R_{Th} or R_{Th}C, with R_{Th} seen by the L or C.
5. x(t) = x(∞) + [x(0⁺) − x(∞)]e^{−t/τ}.

**Laplace route.** (1) Find i_{L}(0⁻), v_{C}(0⁻). (2) Transform: sources → F(s), R → R, L → sL (+ source L i_{L}(0⁻)), C → 1/sC (+ source v_{C}(0⁻)/s). (3) KVL/KCL in s, solve for the unknown. (4) Partial fractions, inverse transform.

**Test signals.** δ(t) ↔ 1, u(t) ↔ 1/s, r(t) = t·u(t) ↔ 1/s^{2}; δ = du/dt, u = dr/dt. RC (τ = RC): impulse (1/τ)e^{−t/τ}, step 1 − e^{−t/τ}, ramp t − τ + τe^{−t/τ}.

**Facts to state.** Inductor current and capacitor voltage cannot change instantaneously (v_{C}(0⁻) = v_{C}(0⁺), i_{L}(0⁻) = i_{L}(0⁺)). Settling ≈ 5τ (99.3 %). 63.2 % of the change happens in one τ.

## Traps

- Using the ∞ circuit at 0⁺ (treating L as a short immediately).
- Calling i_{L}(0⁺) = 0 when the inductor was carrying current at 0⁻: it keeps its 0⁻ value, whatever it was.
- τ = L/R with the wrong R: it must be the Thévenin resistance the L sees.
- Using the first-order formula on an RLC circuit.
- Laplace: forgetting the initial-condition source, or writing a DC source as V instead of V/s.
- Using the final-value theorem on a response that oscillates forever.

## Self-test

1. What does a capacitor look like at 0⁺ if it was uncharged? And at ∞?
2. Why is τ = L/R and not LR? Check with units: H/Ω = ?
3. RL circuit, i(0⁺) = 2 A, i(∞) = 0, τ = 5 ms. Write i(t). What is i at 10 ms?
4. After how many time constants is a transient 99 % done?
5. Why is there no transient in a purely resistive circuit?
6. Give the Laplace transform of δ(t), u(t), r(t), and one everyday example of each.
7. Find I(s) and i(t) for an RL circuit (R = 1 kΩ, L = 1 H) with i(0⁻) = 5 mA and no source.

<!--ANSWERS-->
## Answers

**Check 1.** v_{C}(0⁺) = 4 V, so the resistor sees 10 − 4 = 6 V: I(0⁺) = **6 mA**. At ∞ the C is open: I(∞) = **0** (v_{C}(∞) = 10 V).

**Check 2.** τ = 2 kΩ × 5 µF = **10 ms**; settled after about 5τ = **50 ms**.

**Check 3.** I(s) = \frac{10/s}{2000 + 1/(10^{−6}s)} = \frac{0.005}{s + 500} ⇒ i(t) = **5e^{−500t} mA** (τ = 2 ms; I(0⁺) = 10 V/2 kΩ ✓).

**Check 4.** \frac{1}{τ}e^{−t/τ}: the **impulse response**, as δ = du/dt predicts.

**Self-test.**

1. A **short** at 0⁺; an **open** at ∞.
2. H/Ω = (V·s/A)/(V/A) = **s**: L/R is a time. (LR has units Ω²·s, not a time.)
3. i(t) = **2e^{−t/5 ms} A**; at 10 ms, i = 2e^{−2} = **0.27 A**.
4. About **5τ** (99.3 %); 4.6τ gives exactly 99 %.
5. A resistor stores no energy, so nothing needs time to build up or run down: every quantity jumps straight to its final value.
6. **1, 1/s, 1/s^{2}**. Lighter spark (impulse), switch (step), accelerator (ramp).
7. I(s) = \frac{L i(0⁻)}{R + sL} = \frac{0.005}{s + 1000} ⇒ i(t) = **5e^{−1000t} mA** (τ = 1 ms).
<!--/ANSWERS-->
