# 09 — Second-order circuits: series RLC

<div class="sub">MTE syllabus item 7 (under-, over-, critically damped, undamped) · not yet in the class notes: the question is a textbook problem · needs 08 (0⁻/0⁺/∞, Laplace)</div>

## Map

[[map:1 Why RLC is second order > 2 The characteristic equation > 3 α and ω₀ decide everything > 4 The four cases > 5 Using the initial conditions|here=1]]

## The question this file answers

- <span class="tag">textbook</span> 10 V is switched onto a series R, 1 H, 1 µF circuit at t = 0 (everything at rest). Find v_{C}(t) for R = 2.5 kΩ, 2 kΩ, 1.2 kΩ and 0. Classify each.

The class notes (set 2 p.18) already mark the boundary: the one first-order formula is "not for RLC and LC circuits". This file is what replaces it. Facts from the circuits knowledge base (Hayt; Van Valkenburg; Alexander & Sadiku ch. 8); every curve below was checked by simulating the circuit.

---

## Build

:::q <span class="tag">textbook</span>
Find v_{C}(t) after the switch closes, for R = 2.5 kΩ, 2 kΩ, 1.2 kΩ and 0.
:::

[[fig:rlc_series|L = 1 H, C = 1 µF, source 10 V, switch closes at t = 0. i(0⁻) = 0, v_{C}(0⁻) = 0.|w=58]]

:::guess Guess first
Make R very large, then zero. What does v_{C} do in each case? Can it ever go **above** 10 V?
:::

### 1 · Why it is second order

The circuit has **two** energy stores: the inductor (current) and the capacitor (voltage). Energy can pass back and forth between them, like a mass on a spring. The resistor is the friction.

KVL round the loop, with i = C\frac{dv_{C}}{dt}:

$$L C \frac{d^{2}v_{C}}{dt^{2}} + R C \frac{dv_{C}}{dt} + v_{C} = V$$

A second derivative: one time constant is no longer enough.

### 2 · The characteristic equation

By Laplace (08 §6), with everything at rest: I(s) = \frac{V/s}{R + sL + 1/sC}. Multiply top and bottom by s/L:

$$I(s) = \frac{V/L}{s^{2} + \frac{R}{L}s + \frac{1}{LC}}$$

The denominator set to zero is the **characteristic equation**. Its roots (the poles) decide the shape of the response:

$$s^{2} + 2αs + ω_{0}^{2} = 0     s = −α ± \sqrt{α^{2} − ω_{0}^{2}}$$

### 3 · Two numbers decide everything

| Symbol | Name | Series RLC | Here (L = 1 H, C = 1 µF) |
|---|---|---|---|
| **α** | damping coefficient (neper frequency) | \frac{R}{2L} | \frac{R}{2} per second |
| **ω_{0}** | undamped natural frequency | \frac{1}{\sqrt{LC}} | \frac{1}{\sqrt{10^{−6}}} = **1000 rad/s** |
| **ζ** | damping ratio | \frac{α}{ω_{0}} | |

Compare α with ω_{0}. The **critical resistance** is where α = ω_{0}: R_{c} = 2\sqrt{\frac{L}{C}} = 2\sqrt{10^{6}} = **2 kΩ**.

### 4 · The four cases

| R | α | Roots | Case | v_{C}(t) (V) |
|---|---|---|---|---|
| 2.5 kΩ | 1250 > ω_{0} | −500, −2000 (real, different) | **overdamped** | 10 − \frac{40}{3}e^{−500t} + \frac{10}{3}e^{−2000t} |
| 2 kΩ | 1000 = ω_{0} | −1000, twice (real, equal) | **critically damped** | 10 − 10(1 + 1000t)e^{−1000t} |
| 1.2 kΩ | 600 < ω_{0} | −600 ± j800 (complex) | **underdamped** | 10 − e^{−600t}(10 cos 800t + 7.5 sin 800t) |
| 0 | 0 | ± j1000 (imaginary) | **undamped** | 10(1 − cos 1000t) |

[[fig:rlc_plot|Each formula was checked against a time simulation of the circuit at t = 1, 2, 3.93 and 5 ms; they agree to 6 digits.|w=86]]

[[fig:splane|Where the roots sit. On the real axis: no oscillation. Off it: oscillation at the imaginary part. The further left, the faster the decay.|w=80]]

What each case looks like:

- **Overdamped** (α > ω_{0}, ζ > 1): two decaying exponentials; **slow**, no overshoot. The slow root (−500, i.e. τ = 2 ms) dominates.
- **Critically damped** (α = ω_{0}, ζ = 1): the form (A + Bt)e^{−αt}; the **fastest rise with no overshoot**.
- **Underdamped** (α < ω_{0}, ζ < 1): a decaying oscillation e^{−αt}cos(ω_{d}t + φ), at the **damped frequency ω_{d} = \sqrt{ω_{0}^{2} − α^{2}}** = \sqrt{1000^{2} − 600^{2}} = 800 rad/s. It **overshoots**: peak **10.95 V** at t = π/ω_{d} = **3.93 ms**.
- **Undamped** (R = 0, α = 0): the energy swings between L and C forever at ω_{0}; v_{C} goes up to **20 V**, twice the source.

The Guess answer: large R → slow creep up to 10 V; R = 0 → endless oscillation between 0 and 20 V. So yes, v_{C} **can** exceed the source voltage, whenever the circuit is underdamped.

:::check Check 1
Series RLC with L = 10 mH, C = 1 µF. (a) Find ω_{0} and the critical R. (b) Classify R = 100 Ω and R = 500 Ω.
:::

### 5 · Using the initial conditions

The table's constants come from the two initial conditions (08: what can't jump):

- v_{C}(0⁺) = v_{C}(0⁻) = **0** (capacitor voltage cannot jump).
- i(0⁺) = i(0⁻) = **0** (inductor current cannot jump), and since i = C\frac{dv_{C}}{dt}, this gives \frac{dv_{C}}{dt}(0⁺) = **0**.
- Final value: at ∞ the capacitor is open, the inductor a short, so v_{C}(∞) = **10 V**.

**Overdamped, worked:** v_{C} = 10 + A_{1}e^{−500t} + A_{2}e^{−2000t}.

$$v_{C}(0) = 0: A_{1} + A_{2} = −10      \frac{dv_{C}}{dt}(0) = 0: −500A_{1} − 2000A_{2} = 0$$

The second gives A_{1} = −4A_{2}, so −3A_{2} = −10: **A_{2} = \frac{10}{3}, A_{1} = −\frac{40}{3}**, as in the table.

**Underdamped current**, the other quantity asked most often: i(t) = \frac{V}{ω_{d}L}e^{−αt}sin ω_{d}t = 12.5 e^{−600t} sin 800t mA (simulation at 1 ms: 4.92 mA ✓).

:::check Check 2
Why must the current in the undamped case be i(t) = 10 sin(1000t) mA? Check it with i = C·dv_{C}/dt.
:::

---

## Exam form

**Series RLC:** characteristic equation s^{2} + \frac{R}{L}s + \frac{1}{LC} = 0; α = \frac{R}{2L}, ω_{0} = \frac{1}{\sqrt{LC}}, ζ = α/ω_{0}, roots s = −α ± \sqrt{α^{2} − ω_{0}^{2}}.

| Condition | Case | Form of the natural response |
|---|---|---|
| α > ω_{0} (R > 2\sqrt{L/C}) | overdamped | A_{1}e^{s_{1}t} + A_{2}e^{s_{2}t} |
| α = ω_{0} (R = 2\sqrt{L/C}) | critically damped | (A_{1} + A_{2}t)e^{−αt} |
| α < ω_{0} | underdamped | e^{−αt}(A_{1}cos ω_{d}t + A_{2}sin ω_{d}t), ω_{d} = \sqrt{ω_{0}^{2} − α^{2}} |
| α = 0 (R = 0) | undamped | A_{1}cos ω_{0}t + A_{2}sin ω_{0}t |

Step response = final value + natural response. Constants from v_{C}(0⁺) and i_{L}(0⁺) (i.e. dv_{C}/dt(0⁺) = i_{L}(0⁺)/C).

**Parallel RLC** (for recognition): same ω_{0}, but α = \frac{1}{2RC}, so a **small** R gives heavy damping, the opposite of series.

## Traps

- Using x(t) = x(∞) + [x(0⁺) − x(∞)]e^{−t/τ} on an RLC circuit (set 2 p.18 warns against it).
- Writing α = R/L instead of R/2L.
- Oscillating at ω_{0} in the underdamped case: the oscillation is at ω_{d}, which is smaller.
- Forgetting the second initial condition (dv_{C}/dt(0⁺) from the inductor current).
- Parallel RLC: using the series α.

## Self-test

1. Write the characteristic equation of a series RLC and define α and ω_{0}.
2. L = 0.1 H, C = 10 µF. Find the critical resistance.
3. For R = 1.2 kΩ in the question, what is the period of the ringing?
4. Which case settles fastest without overshoot?
5. Why can an LC circuit (R = 0) never reach a steady state?

<!--ANSWERS-->
## Answers

**Check 1.** (a) ω_{0} = 1/\sqrt{10^{−2} × 10^{−6}} = **10 000 rad/s**; R_{c} = 2\sqrt{10^{−2}/10^{−6}} = **200 Ω**. (b) 100 Ω: underdamped (α = 5000 < 10 000). 500 Ω: overdamped (α = 25 000 > 10 000).

**Check 2.** i = C dv_{C}/dt = 10^{−6} × 10 × 1000 sin 1000t = 0.01 sin 1000t A = **10 sin(1000t) mA**. It starts at 0, as the inductor requires.

**Self-test.**

1. s^{2} + (R/L)s + 1/LC = 0; α = R/2L, ω_{0} = 1/\sqrt{LC}.
2. R_{c} = 2\sqrt{0.1/10^{−5}} = 2 × 100 = **200 Ω**.
3. T = 2π/ω_{d} = 2π/800 = **7.85 ms**.
4. **Critically damped**.
5. No resistor to turn the energy into heat: it keeps passing between L and C, so the roots sit on the jω axis and never decay.
<!--/ANSWERS-->
