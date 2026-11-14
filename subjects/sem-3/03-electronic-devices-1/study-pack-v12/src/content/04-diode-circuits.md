# 04 — Diode circuits and rectifiers

<div class="sub">Deck L08 (load line, DC diode circuits) · deck L09 (rectifiers) · syllabus Unit 2 · needs 03 (the diode curve and its 0.7 V model)</div>

## Map

[[map:1 Load line > 2 The three-step method > 3 Half-wave rectifier > 4 Full-wave rectifiers|here=1]]

03 built the diode and its simplified model: a 0.7 V drop when on, an open circuit when off. This file puts that model into circuits. Most of the unit's numerical marks are here.

## The questions this file answers

- <span class="tag">Deck L08 slide 4</span> E = 10 V, R = 0.5 kΩ, Si diode: find V_{DQ}, I_{DQ} and V_{R} from the characteristic.
- <span class="tag">Deck L08 slides 9–18</span> Series, parallel and two-source diode circuits.
- <span class="tag">Deck L09 slide 9</span> Sketch v_{o} of a half-wave rectifier and find its DC level, ideal and Si.
- <span class="tag">practice</span> Compare half-wave, centre-tapped and bridge rectifiers.

---

## Build

### 1 · The load line

:::q <span class="tag">Deck L08 slide 4</span>
For the given diode configuration and diode characteristics, determine V_{DQ}, I_{DQ} and V_{R}. (E = 10 V, R = 0.5 kΩ, silicon diode.)
:::

:::guess Guess first
Roughly how much of the 10 V lands on the resistor?
:::

<div class="two">

[[fig:ckt_load_line|The circuit.]]

[[fig:load_line|Load line on the diode's curve.]]

</div>

The diode and resistor carry the same current, and KVL gives E = V_{D} + I_{D}R. Rearranged, **I_{D} = (E − V_{D})/R** is a straight line on the diode's own axes. Its ends: V_{D} = 0 gives I_{D} = E/R; I_{D} = 0 gives V_{D} = E. The circuit must sit on the line and on the diode curve at once: the crossing is the **Q-point**.

**Answer.** Ends 20 mA and 10 V. The crossing reads **V_{DQ} ≈ 0.78 V, I_{DQ} ≈ 18.5 mA**. **V_{R}** = 18.5 mA × 0.5 kΩ = **9.25 V** (check: E − V_{DQ} = 9.22 V).

:::note Slip in the slide
Slide 5 writes V_{R} = (18.5 mA)(1 K) = 18.5 V. R is 0.5 kΩ, and 18.5 V cannot come out of a 10 V source. Use 9.25 V.
:::

:::check Check 1
If R is doubled to 1 kΩ, where do the line's ends move, and does I_{DQ} rise or fall?
:::

### 2 · Without the graph: the three-step method

:::q <span class="tag">Deck L08 slide 14</span>
Determine I, V_{1}, V_{2} and V_{o}. (E_{1} = 10 V, Si diode, R_{1} = 4.7 kΩ, R_{2} = 2.2 kΩ, E_{2} = 5 V, as drawn.)
:::

:::guess Guess first
Is the diode on? Which way do the two sources push?
:::

[[fig:ckt_two_source|Deck L08 slide 14.|w=60]]

1. **Decide the state.** Remove the diode. If the voltage across the gap pushes current along the arrow and exceeds 0.7 V (Si), it is **ON**; otherwise **OFF**.
2. **Substitute.** ON → a 0.7 V drop (0.3 V Ge, 0 ideal). OFF → open circuit, I = 0.
3. **Solve** with KVL and Ohm's law.

Combinations: diodes in series add their drops (Si + red LED = 0.7 + 1.8 V); a reversed diode anywhere in a series path opens it. Diodes in parallel share one 0.7 V drop, and identical ones split the current equally.

**Answer.** The sources total 15 V along the arrow: ON. I = (10 + 5 − 0.7)/(4.7 k + 2.2 k) = **2.07 mA**. V_{1} = **9.74 V**, V_{2} = **4.56 V**, V_{o} = V_{2} − E_{2} = **−0.44 V**.

:::check Check 2
All deck L08. (a) Slide 9: E = 8 V, Si diode and R = 2.2 kΩ in series. Find V_{D}, V_{R}, I_{D}; then reverse the diode. (b) Slide 12: +12 V feeds a Si diode, a red LED (1.8 V), then 680 Ω to ground. Find V_{o} (across R) and I_{D}. (c) Slide 15: 10 V feeds 0.33 kΩ, then two Si diodes in parallel to ground. Find V_{o}, I_{1} and each diode's current. (d) Slide 18: 20 V feeds Si diode D_{1}; then R_{1} = 3.3 kΩ in parallel with Si diode D_{2}; then R_{2} = 5.6 kΩ back to the source. Find I_{1}, I_{2}, I_{D2}.
:::

### 3 · The half-wave rectifier

:::q <span class="tag">Deck L09 slide 9</span>
Sketch the output v_{o} and determine its DC level. Repeat if the ideal diode is replaced by a silicon diode. (Input: 20 V peak sine; the diode points toward the source; R = 2 kΩ across the output.)
:::

:::guess Guess first
Which half-cycle reaches the output, and with what sign?
:::

:::note Terms
**Rectifier:** turns AC into one-direction (pulsating DC) voltage. **V_{m}:** peak of the input sine; V_{rms} = V_{m}/√2. **V_{dc}:** the average of the output over one period, what a DC meter reads. **PIV:** the largest reverse voltage the diode must survive while blocking.
:::

<div class="two">

[[fig:ckt_hw|Half-wave rectifier.]]

[[fig:rect_waves|Input and half-wave / full-wave outputs.]]

</div>

One diode conducts on one half-cycle and blocks the other. Averaging one half-sine over a full period:

$$V_{dc} = V_{m}/π = 0.318V_{m}      Si: 0.318(V_{m} − 0.7)      PIV = V_{m}$$

**Answer.** The diode points toward the source, so it conducts only when v_{i} is negative: the output is the **negative half-cycles**. Ideal: V_{dc} = −0.318 × 20 = **−6.36 V**. Si: −0.318 × 19.3 = **−6.14 V**. PIV = 20 V.

:::check Check 3
Derive the ripple factor 1.21 from V_{rms} = V_{m}/2 and V_{dc} = V_{m}/π, using r = √[(V_{rms}/V_{dc})^{2} − 1].
:::

### 4 · Full-wave rectifiers

:::q <span class="tag">practice</span>
A bridge rectifier with Si diodes is fed 12 V rms. Find V_{m}, V_{dc} and the PIV per diode.
:::

:::guess Guess first
Two diodes conduct at a time in a bridge. How does that change the 0.7 V correction?
:::

<div class="two">

[[fig:bridge_fig|Bridge: D_{1}, D_{3} on the positive half; D_{2}, D_{4} on the negative.]]

[[fig:ckt_ct|Centre-tapped: each half-secondary feeds R through its own diode.]]

</div>

Both half-cycles push current through R in the same direction, so V_{dc} doubles. In the centre-tapped circuit V_{m} is the peak from the tap to one end, and the off diode sees both halves: PIV = 2V_{m}.

| | Half-wave | Centre-tapped | Bridge |
|---|---|---|---|
| Diodes | 1 | 2 | 4 |
| V_{dc} (ideal) | 0.318V_{m} | 0.636V_{m} | 0.636V_{m} |
| V_{dc} (Si) | 0.318(V_{m} − 0.7) | 0.636(V_{m} − 0.7) | 0.636(V_{m} − 1.4) |
| V_{rms} of output | V_{m}/2 | V_{m}/√2 | V_{m}/√2 |
| PIV per diode | V_{m} | 2V_{m} | V_{m} |
| Ripple factor | 1.21 | 0.482 | 0.482 |
| Max efficiency | 40.6% | 81.2% | 81.2% |
| Ripple frequency | f | 2f | 2f |

Efficiency η = (V_{dc}/V_{rms})^{2} for ideal diodes. A capacitor across R (a filter) holds the voltage up between peaks and cuts the ripple.

**Answer.** V_{m} = 12√2 = **17.0 V**. V_{dc} = 0.636 × (17.0 − 1.4) = **9.92 V**. PIV ≈ **17 V**.

:::check Check 4
Why is a bridge usually preferred over the centre-tapped circuit? Two reasons.
:::

---

## Exam form

**Load line.** KVL: E = V_{D} + I_{D}R; ends (0, E/R) and (E, 0); Q-point at the crossing; V_{R} = I_{DQ}R.

**Three-step method.** State → substitute (0.7 V / open) → KVL. Series drops add; parallel diodes share one drop.

**Rectifiers.** Draw each circuit with its waveforms. The comparison table (V_{dc}, V_{rms}, PIV, r, η, ripple f). Derive r = 1.21 and 0.482 and η = 40.6% and 81.2%.

## Traps

- Reading V_{R} with the wrong R (the slide-5 slip).
- Assuming a diode is on without the state test.
- Subtracting only 0.7 V for a bridge: two diodes conduct, so 1.4 V.
- PIV of the centre-tapped circuit is 2V_{m}, not V_{m}.
- Using V_{rms} of the input (V_{m}/√2) for a half-wave output (V_{m}/2).

## Self-test

1. State the three-step method for a diode circuit.
2. E = 12 V, Si diode, R = 1 kΩ in series. Find I_{D} and V_{R}.
3. A half-wave rectifier with a Si diode has V_{m} = 10 V. Find V_{dc} and PIV.
4. A centre-tapped rectifier has 15 V peak from the tap to each end, ideal diodes. Find V_{dc} and PIV.
5. Derive the full-wave ripple factor.
6. Why is the ripple frequency of a full-wave rectifier 2f?

<!--ANSWERS-->

## Answers

**Check 1.** E/R falls to 10 mA; the V_{D} end stays at 10 V. The line is flatter, so **I_{DQ} falls** (to about 9.3 mA).

**Check 2.** (a) Forward: V_{D} = 0.7 V, V_{R} = **7.3 V**, I_{D} = **3.32 mA**. Reversed: I_{D} = 0, V_{R} = 0, V_{D} = **8 V**. (b) V_{o} = 12 − 0.7 − 1.8 = **9.5 V**; I_{D} = **13.97 mA**. (c) V_{o} = **0.7 V**; I_{1} = 9.3/0.33 k = **28.18 mA**; **14.09 mA** each. (d) I_{1} = 0.7/3.3 k = **0.212 mA**; I_{2} = (20 − 1.4)/5.6 k = **3.32 mA**; I_{D2} = **3.11 mA**.

**Check 3.** V_{rms}/V_{dc} = (V_{m}/2)/(V_{m}/π) = π/2 = 1.571; r = √(1.571^{2} − 1) = **1.21**.

**Check 4.** No centre-tapped transformer is needed, and each diode needs only half the PIV (V_{m}, not 2V_{m}).

**Self-test.**

1. See step 2.
2. I_{D} = 11.3/1 k = **11.3 mA**; V_{R} = **11.3 V**.
3. V_{dc} = 0.318 × 9.3 = **2.96 V**; PIV = **10 V**.
4. V_{dc} = 0.636 × 15 = **9.54 V**; PIV = **30 V**.
5. V_{rms}/V_{dc} = (V_{m}/√2)/(2V_{m}/π) = π/(2√2) = 1.111; r = √(1.234 − 1) = **0.482**.
6. Both half-cycles give an output pulse, so the output repeats twice per input period.

<!--/ANSWERS-->
