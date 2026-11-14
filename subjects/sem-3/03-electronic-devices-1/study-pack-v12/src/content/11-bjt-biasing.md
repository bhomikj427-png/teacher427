# 11 — BJT biasing and stability

<div class="sub">Decks L26–L27 (53 slides: fixed-bias example slide 15, emitter-bias example slide 27) · syllabus Unit 5 · needs 10 (α, β, the active region)</div>

## Map

[[map:1 Load line, fixed bias > 2 Why bias drifts > 3 Emitter bias, S > 4 Voltage-divider bias > 5 Compensation|here=1]]

10 showed that I_{C} = βI_{B} in the active region. An amplifier needs the transistor to sit at one fixed point in that region with no signal applied. This file chooses the resistors that put it there, and measures how well each circuit keeps it there.

## The questions this file answers

- <span class="tag">Deck L26 slide 15</span> Fixed bias: V_{CC} = 12 V, R_{B} = 240 kΩ, R_{C} = 2.2 kΩ, β = 50. Find I_{B}, I_{C}, V_{CE} and I_{C(sat)}.
- <span class="tag">Deck L27 slide 27</span> Emitter bias: V_{CC} = 20 V, R_{B} = 430 kΩ, R_{C} = 2 kΩ, R_{E} = 1 kΩ, β = 50. Find the Q-point and the stability factor S.
- <span class="tag">Deck</span> Define the stability factor and derive S for each bias circuit.
- <span class="tag">practice</span> Voltage-divider bias, exact and approximate.

---

## Build

### 1 · DC load line, Q-point and fixed bias

:::q <span class="tag">Deck L26 slide 15</span>
For the fixed-bias circuit (V_{CC} = 12 V, R_{B} = 240 kΩ, R_{C} = 2.2 kΩ, β = 50), find I_{B}, I_{C} and V_{CE} at the operating point, and the saturation current.
:::

:::guess Guess first
Which loop gives I_{B} directly?
:::

:::note Terms
**Operating (Q) point:** the DC values (V_{CE}, I_{C}) with no signal applied. **DC analysis:** every capacitor is an open circuit.
:::

[[fig:bjt_out_curves|Output curves with the DC load line. Q is where the line meets the curve for the actual I_{B}.|w=70]]

1. Base–emitter loop: V_{CC} = I_{B}R_{B} + V_{BE}, so **I_{B} = (V_{CC} − 0.7)/R_{B}**.
2. Active region: **I_{C} = βI_{B}**.
3. Collector–emitter loop: **V_{CE} = V_{CC} − I_{C}R_{C}**.

Step 3 is a straight line on the output curves, the **load line**. Ends: I_{C} = 0 gives V_{CE} = V_{CC} (cutoff); V_{CE} = 0 gives I_{C(sat)} = V_{CC}/R_{C}. For the largest undistorted swing, put Q near the middle. A larger I_{B} slides Q up toward saturation; a larger R_{C} flattens the line; a lower V_{CC} shifts it inward, parallel.

**Answer.** I_{B} = 11.3/240 k = **47.08 μA**. I_{C} = 50 × 47.08 μA = **2.35 mA**. V_{CE} = 12 − 2.35 × 2.2 = **6.82 V**. I_{C(sat)} = 12/2.2 k = **5.45 mA**. Q sits near the middle of the line.

:::check Check 1
Same circuit: (a) the transistor is replaced by one with β = 100. Find the new I_{C} and V_{CE}. What has happened? (b) Give the end points of the load line if R_{C} becomes 4 kΩ.
:::

### 2 · Why the Q-point drifts

:::guess Predict
Check 1(a) showed a new transistor can wreck the Q-point. Name three things that change I_{C} when the transistor only warms up.
:::

- **I_{CO}** (= I_{CBO}, the CB leakage) **doubles for every 10 °C** rise.
- **V_{BE}** falls about **2.5 mV per °C**.
- **β** rises with temperature, and varies widely between transistors of one type.

All three raise I_{C}. More I_{C} means more heat, which raises I_{C} again: **thermal runaway**, which can destroy the transistor.

The **stability factor** measures the leakage effect, with β and V_{BE} held constant. Smaller is better; the ideal is 1. Two more factors are defined the same way: S′ = ∂I_{C}/∂V_{BE}, S″ = ∂I_{C}/∂β.

$$S = ∂I_{C}/∂I_{CO}$$

**Derivation (general S).** Start from I_{C} = βI_{B} + (1 + β)I_{CO}. Differentiate with respect to I_{C}: 1 = β(dI_{B}/dI_{C}) + (1 + β)/S. Rearrange:

$$S = (1 + β)/(1 − β·dI_{B}/dI_{C})$$

**Answer.** I_{CO}, V_{BE} and β; all three move I_{C} up as temperature rises.

:::check Check 2
(a) Why is S = 1 + β for fixed bias? (b) What value of dI_{B}/dI_{C} would give the ideal S = 1? What sign must it have?
:::

### 3 · Emitter bias and its stability factor

:::q <span class="tag">Deck L27 slide 27</span>
For the emitter-stabilised circuit (V_{CC} = 20 V, R_{B} = 430 kΩ, R_{C} = 2 kΩ, R_{E} = 1 kΩ, β = 50), find I_{B}, I_{C} and V_{CE}. Then find S and compare with fixed bias.
:::

:::guess Guess first
What could a resistor in the emitter do about a rise in I_{C}?
:::

[[fig:bjt_bias_three|(a) fixed bias, (b) emitter bias, (c) voltage-divider bias.]]

**How R_{E} stabilises.** If I_{C} rises, the drop across R_{E} rises, which raises the emitter voltage and leaves less to drive the base. I_{B} falls and pulls I_{C} back: negative feedback (13).

Base loop: V_{CC} = I_{B}R_{B} + 0.7 + (β + 1)I_{B}R_{E}, so

$$I_{B} = (V_{CC} − V_{BE})/(R_{B} + (β + 1)R_{E})$$

With R_{E} present: V_{CE} = V_{CC} − I_{C}R_{C} − I_{E}R_{E} ≈ V_{CC} − I_{C}(R_{C} + R_{E}), and I_{C(sat)} = V_{CC}/(R_{C} + R_{E}).

| Circuit | dI_{B}/dI_{C} | S |
|---|---|---|
| Fixed bias | 0 | 1 + β (worst) |
| Emitter bias | −R_{E}/(R_{B} + R_{E}) | (1 + β)(1 + R_{B}/R_{E})/(1 + β + R_{B}/R_{E}) |
| Voltage divider | −R_{E}/(R_{Th} + R_{E}) | same, with R_{B} → R_{Th} (best: R_{Th} is small) |
| Collector-to-base feedback | −R_{C}/(R_{B} + R_{C}) | (1 + β)/(1 + βR_{C}/(R_{B} + R_{C})) |

**Answer.** I_{B} = 19.3/(430 k + 51 k) = **40.1 μA**. I_{C} = 50 × 40.1 = **2.01 mA**; I_{E} = 2.05 mA. V_{CE} = 20 − 2.01 × 2 − 2.05 × 1 = **13.94 V** (13.97 V with I_{E} ≈ I_{C}). R_{B}/R_{E} = 430, so S = 51 × 431/(51 + 430) = **45.7**, against 51 for fixed bias: R_{E} helps only a little, because R_{B} is far larger than R_{E}.

:::check Check 3
In circuit (b), R_{B} is replaced by a divider with R_{Th} = 10 kΩ (β = 50, R_{E} = 1 kΩ). Find the new S.
:::

### 4 · Voltage-divider bias

:::q <span class="tag">practice · circuit (c)</span>
V_{CC} = 22 V, R_{1} = 39 kΩ, R_{2} = 3.9 kΩ, R_{C} = 10 kΩ, R_{E} = 1.5 kΩ, β = 100. Find I_{C}, V_{CE} and S, exactly and approximately.
:::

:::guess Guess first
If the divider current is much bigger than I_{B}, does β matter at all?
:::

**Exact.** Replace R_{1}, R_{2} and V_{CC} by their Thévenin equivalent seen from the base: E_{Th} = V_{CC}R_{2}/(R_{1} + R_{2}), R_{Th} = R_{1} ∥ R_{2}. Then I_{B} = (E_{Th} − 0.7)/(R_{Th} + (β + 1)R_{E}).

**Approximate** (valid when **βR_{E} ≥ 10R_{2}**): ignore I_{B}. V_{B} = E_{Th}, V_{E} = V_{B} − 0.7, I_{C} ≈ I_{E} = V_{E}/R_{E}. β does not appear: the circuit is **β-independent**.

**Answer.** E_{Th} = 22 × 3.9/42.9 = 2.0 V, R_{Th} = 3.55 kΩ. Exact: I_{B} = 1.3/(3.55 k + 151.5 k) = 8.38 μA, **I_{C} = 0.84 mA**, V_{CE} = 22 − 0.838 × 10 − 0.846 × 1.5 = **12.35 V**, S = 101 × 3.36/103.36 = **3.29**. Approximate: 150 k ≥ 39 k ✓; V_{E} = 1.3 V, I_{C} ≈ 1.3/1.5 k = **0.87 mA**.

:::check Check 4
(a) Why is S so much smaller here than for emitter bias? (b) With β = 200 instead, which answer, exact or approximate, changes?
:::

### 5 · Bias compensation

:::guess Predict
Feedback through R_{E} costs gain (13). Is there a way to cancel drift without feedback?
:::

Compensation uses a temperature-sensitive part to cancel the drift directly.

- **Diode compensation:** a forward-biased diode of the same material in the base circuit. Its drop falls with temperature exactly as V_{BE} does, so the two cancel.
- **Thermistor** (resistance falls as temperature rises) in the lower divider arm: as it heats, the base voltage drops and holds I_{C} down.
- **Sensistor** (resistance rises with temperature) in the upper arm or in the emitter does the same.

**Answer.** Yes: a part whose value drifts the opposite way to the transistor cancels the change without feedback.

:::check Check 5
Where would you put a thermistor in a divider-bias circuit, and why there?
:::

---

## Exam form

**Fixed bias.** I_{B} = (V_{CC} − 0.7)/R_{B}; I_{C} = βI_{B}; V_{CE} = V_{CC} − I_{C}R_{C}; load line ends (V_{CC}, 0), (0, V_{CC}/R_{C}).

**Stability.** Causes: I_{CO} ×2 per 10 °C, V_{BE} −2.5 mV/°C, β rises; thermal runaway. S = ∂I_{C}/∂I_{CO}; derive S = (1 + β)/(1 − β dI_{B}/dI_{C}) from I_{C} = βI_{B} + (1 + β)I_{CO}. Table of S for the four circuits.

**Emitter bias.** I_{B} = (V_{CC} − V_{BE})/(R_{B} + (β + 1)R_{E}); explain the feedback in one line.

**Divider bias.** Thévenin: E_{Th}, R_{Th}; exact I_{B}; approximate when βR_{E} ≥ 10R_{2}: V_{E} = V_{B} − 0.7, I_{C} = V_{E}/R_{E}.

**Compensation.** Diode, thermistor, sensistor: where and why.

## Traps

- Using V_{CE} = V_{CC} − I_{C}R_{C} when R_{E} is present: subtract the R_{E} drop too.
- Forgetting (β + 1) in front of R_{E} in the base loop.
- Using the approximate divider method without checking βR_{E} ≥ 10R_{2}.
- Calling a smaller S "worse": smaller is better, 1 is ideal.
- Writing I_{C(sat)} = V_{CC}/R_{C} when R_{E} is present: it is V_{CC}/(R_{C} + R_{E}).

## Self-test

1. Explain thermal runaway in three lines.
2. Fixed bias: V_{CC} = 10 V, R_{B} = 200 kΩ, R_{C} = 2 kΩ, β = 80. Find I_{C}, V_{CE} and I_{C(sat)}.
3. Divider bias, approximate: V_{CC} = 12 V, R_{1} = 40 kΩ, R_{2} = 10 kΩ, R_{C} = 3 kΩ, R_{E} = 1 kΩ, β = 100. Check the condition, then find I_{C} and V_{CE}.
4. Emitter bias with β = 100 and R_{B}/R_{E} = 50. Find S.
5. Derive the general expression for S, from memory.
6. How does a diode in the base circuit compensate for V_{BE} drift?

<!--ANSWERS-->

## Answers

**Check 1.** (a) I_{B} is unchanged at 47.08 μA, so I_{C} = **4.71 mA** and V_{CE} = 12 − 4.71 × 2.2 = **1.64 V**. Q has moved most of the way to saturation only because β changed: fixed bias is not stable. (b) (12 V, 0) and (0, **3 mA**).

**Check 2.** (a) I_{B} = (V_{CC} − V_{BE})/R_{B} does not depend on I_{C}, so dI_{B}/dI_{C} = 0 and S = 1 + β. (b) dI_{B}/dI_{C} = −1: every rise in I_{C} must cut I_{B} by the same amount. It must be negative (feedback).

**Check 3.** R_{Th}/R_{E} = 10: S = 51 × 11/(51 + 10) = **9.2**.

**Check 4.** (a) R_{Th}/R_{E} = 2.36 is small; S approaches 1 + R_{Th}/R_{E} when β is large. (b) Only the exact one, slightly; the approximate answer has no β in it.

**Check 5.** In the lower arm (R_{2}): as temperature rises its resistance falls, V_{B} falls, and I_{C} is held down.

**Self-test.**

1. Heat raises I_{CO} and β and lowers V_{BE}; all raise I_{C}; more I_{C} dissipates more power and heats the junction further; the loop runs away until the device fails.
2. I_{B} = 9.3/200 k = 46.5 μA, **I_{C} = 3.72 mA**, **V_{CE} = 2.56 V**, **I_{C(sat)} = 5 mA**.
3. βR_{E} = 100 kΩ ≥ 10R_{2} = 100 kΩ ✓ (just). V_{B} = 12 × 10/50 = 2.4 V, V_{E} = 1.7 V, **I_{C} ≈ 1.7 mA**, **V_{CE} ≈ 12 − 1.7 × 4 = 5.2 V**.
4. S = 101 × 51/(101 + 50) = **34.1**.
5. See step 2.
6. The diode carries a forward current and its drop falls about 2.5 mV/°C, exactly as V_{BE} does; placed in the base loop, the two changes cancel and I_{C} stays put.

<!--/ANSWERS-->
