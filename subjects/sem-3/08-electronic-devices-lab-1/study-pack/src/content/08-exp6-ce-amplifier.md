# Exp 6 · CE amplifier: frequency response and bandwidth

<div class="sub">Manual pp. 20–21 · hands-on · CO4, CO5 · the same stage is reused in the extra experiment</div>

[[map:5 BJT curves > 6 CE amplifier > 7 Emitter follower > 8 Feedback|here=2]]

**What you already have:** from Exp 5, in the active region I_{C} = βI_{B}, and the BE junction needs ≈ 0.7 V. From C&S, a capacitor's reactance X_{C} = 1/(2πfC): huge at low f, tiny at high f.

**Three terms first:**

- **Biasing:** DC voltages that park the transistor in the active region at a chosen **Q-point** (quiescent point = the DC operating point with no signal).
- **Small-signal gain A_{v}:** v_{o}/v_{in} for a small sine riding on the Q-point. In decibels: 20 log₁₀ A_{v}.
- **Bandwidth:** the frequency range over which the gain stays within 3 dB (a factor of 0.707) of its maximum.

:::q <span class="tag">Manual Exp 6, aim</span>
To plot the frequency response of a CE amplifier and determine its bandwidth. Viva form: "Why does the gain fall at **both** low and high frequencies, and what sets each cut-off?"
:::

:::guess Guess first
Name one part responsible for each end before reading on.
:::

## The circuit, part by part

[[fig:exp06_circuit|Fig 6.1, redrawn: voltage-divider bias, emitter resistor with bypass capacitor, coupling capacitors in and out.|w=82]]

| Part | Job |
|---|---|
| 25 kΩ + 8.2 kΩ (R1, R2) | voltage divider: fixes V_{B} ≈ 15 × 8.2/33.2 ≈ 3.6–3.7 V |
| 560 Ω emitter (R_{E}) | sets I_{E} = V_{E}/R_{E}. It also stabilises the bias: if I_{C} rises with temperature, V_{E} rises, which reduces V_{BE}. |
| 47 µF across R_{E} (C_{E}, **bypass**) | shorts R_{E} for AC, so the signal sees the emitter grounded. This gives full gain. |
| 10 µF input (C_{in}, **coupling**) | passes the signal, blocks DC (so the generator doesn't upset the bias) |
| 10 µF output (C_{C}) | passes the amplified signal, blocks the 12 V collector DC from the CRO |
| 560 Ω collector (R_{C}) | turns the collector current change into a voltage change |

**Q-point (LTspice .op):** V_{B} = 3.60 V, V_{E} = 2.92 V, I_{C} = 5.2 mA, V_{C} = 12.09 V, so V_{CE} = 9.2 V. The transistor is safely active.

**Gain by hand:**

- r_{e} = 26 mV / I_{E} = 26/5.2 = **5 Ω**. This is the BE junction's small-signal resistance.
- Base to collector: A_{v} = −R_{C}/r_{e} = −560/5 = −112.
- The 2.2 kΩ source resistor and the amplifier's input resistance (R_{in} = 25k ∥ 8.2k ∥ βr_{e} ≈ 1.2 kΩ) form a divider. Only 1.2/(1.2 + 2.2) = 0.35 of v_{s} reaches the base.
- Overall: v_{o}/v_{s} ≈ 0.35 × 112 ≈ **39**. LTspice gives **36**.
- The minus sign means the output is **inverted** (180° phase shift).

## Why the gain falls at both ends

[[fig:bandwidth_concept|The general shape. Low end: capacitor reactances grow. High end: the transistor's internal junction capacitances short the signal.|w=80]]

- **Low f:** X_{C} = 1/(2πfC) grows. The coupling capacitors start to block the signal, and above all **C_{E} stops bypassing R_{E}**, which brings in negative feedback (see Exp 8). The lower cut-off is set mostly by C_{E}: f_{L} ≈ 1/(2π C_{E} R_{e}'), where R_{e}' ≈ r_{e} + (source ∥ bias)/β ≈ 10.6 Ω. That gives 1/(2π × 47 µF × 10.6 Ω) ≈ **320 Hz**.
- **High f:** tiny capacitances inside the transistor (between its junctions) and in the wiring start to short the signal. The base–collector capacitance is multiplied by the gain (the *Miller effect*), so it dominates.
- **Middle (midband):** all external capacitors act as shorts and the internal ones as opens, so the gain is flat.

:::do Do it (hands-on)
1. Build Fig 6.1 on the breadboard with supply **+15 V**. 25 kΩ is not a standard value: use 22 kΩ + 3.3 kΩ in series. Check the electrolytic capacitors' polarity: + towards the higher DC voltage (base side for C_{in}, collector side for C_{C}, emitter side for C_{E}).
2. **Check the Q-point first** with the DMM, no signal applied: V_{B} ≈ 3.6 V, V_{E} ≈ 2.9 V, V_{C} ≈ 12 V. If V_{C} ≈ 15 V the transistor is off; if V_{C} ≈ V_{E} it is saturated. Fix this before going on.
3. Generator: sine, 1 kHz. Set the amplitude **small: about 20 mV peak** (use the generator's −20 dB/attenuator button, or a 1 kΩ:100 Ω divider). Look at V_{o} on the DSO. It must be a clean sine, not flattened.
4. Keep V_{s} constant. Step the frequency through **100 Hz, 500, 800, 1k, 5k, 10k, 50k, 100k, 500k, 800k, 1 MHz** and read V_{o(pp)} at each.
5. Calculate A_{v} = V_{o}/V_{s} and 20 log A_{v}. Plot dB (y) against frequency on **semi-log** paper (log x-axis).
6. Draw a line 3 dB below the maximum. Where it cuts the curve gives f_{L} and f_{H}. BW = f_{H} − f_{L}.
:::

:::trap Trap: the manual's 500 mV input
At 500 mV the output would need to swing about ±18 V, but the collector can only move between ≈ 3 V and 15 V. The output is clipped flat (below), so the "gain" you read is meaningless. Even the 100 mV in Fig 6.1 distorts (+2.5 / −3.4 V). Use about 20 mV.
:::

[[fig:exp06_clip|LTspice: the same amplifier with 20 mV in (clean, gain ≈ 34) and 500 mV in (clipped).|w=92]]

## What you should see

[[fig:exp06_freq|LTspice, Fig 6.1 with the CRO as a 1 MΩ load. Midband gain 36 (31.1 dB), f_{L} ≈ 306 Hz, f_{H} ≈ 687 kHz.|w=82]]

| f (Hz) | 100 | 500 | 800 | 1k | 5k | 10k | 50k | 100k | 500k | 800k | 1M |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A_{v} = V_{o}/V_{s} | 11.2 | 30.8 | 33.7 | 34.5 | 36.0 | 36.1 | 36.0 | 35.7 | 29.2 | 23.5 | 20.4 |
| gain (dB) | 21.0 | 29.8 | 30.6 | 30.8 | 31.1 | 31.1 | 31.1 | 31.1 | 29.3 | 27.4 | 26.2 |

**On the bench,** f_{L} should land close to 300 Hz, because it is set by the capacitors you placed. f_{H} depends on breadboard wiring, probe and generator capacitance, so expect anything from a few hundred kHz upward. The simulation is the ideal-wiring value.

## Calculation

$$BW = f_{H} − f_{L} = 687 kHz − 0.306 kHz ≈ 687 kHz$$

When f_{H} ≫ f_{L}, the bandwidth is essentially f_{H}.

:::write Write in your record
**Result:** maximum gain ≈ **36 (31.1 dB)**; f_{L} ≈ **306 Hz**, f_{H} ≈ **687 kHz**; bandwidth ≈ **687 kHz** (simulation; use your measured values).

**Theory for the record:** in a CE amplifier the input is applied at the base and the output taken at the collector, with the emitter common (grounded for AC by the bypass capacitor). Voltage-divider bias with an emitter resistor sets a stable Q-point in the active region. A small base signal produces a β-times-larger collector current change, which develops a large, phase-inverted voltage across R_{C}. Gain ≈ R_{C}/r_{e}. The frequency response is flat in midband, falls at low frequencies because of the coupling and bypass capacitors, and falls at high frequencies because of junction and stray capacitances. Bandwidth = f_{H} − f_{L}, measured at the −3 dB (0.707 A_{max}) points, also called the half-power points.
:::

:::check Check 1
(a) Why is the −3 dB point called the "half-power" point? (b) You remove C_{E}. Does the gain go up or down, and roughly to what? (c) V_{C} reads 15 V with no signal. What is wrong?
:::

<!--ANSWERS-->

## Answers

**Opening question.** Low end: the **coupling and bypass capacitors**' reactance becomes large; C_{E} matters most (f_{L} ≈ 1/(2πC_{E}R_{e}')). High end: the **transistor's internal junction capacitances** (Miller-multiplied C_{bc}) plus stray capacitance.

**Check 1.** (a) Power ∝ V². At 0.707 of the voltage, the power is 0.707² = 0.5 of maximum, and 20 log 0.707 = −3 dB. (b) **Down.** R_{E} returns to the AC path, so A_{v} ≈ −R_{C}/(r_{e} + R_{E}) = −560/565 ≈ −1. The overall gain is about 1 or less (this is Exp 8's effect). (c) No collector current: the transistor is cut off. Look for an open base connection, a missing emitter return, a wrong pin order (check the BC547's pinout: C-B-E with the flat face towards you) or a dead transistor.

<!--/ANSWERS-->
