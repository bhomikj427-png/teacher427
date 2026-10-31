# Exp 10 · JFET common-source amplifier: frequency response

<div class="sub">Manual pp. 29–30 · LTspice · CO4, CO5 · the JFET is the 2N5434 (the manual's "2N54349" is a typo)</div>

[[map:9 JFET curves > 10 CS amplifier > 11 Oscillator > 12 MOSFET inverter|here=2]]

**What you already have:** the BJT's CE amplifier (Exp 6), meaning bias, coupling and bypass capacitors, gain, and −3 dB points. The JFET's g_{m} (Exp 9).

**Two terms first:**

- **Common source (CS):** the FET's version of CE. Input at the gate, output at the drain, source common.
- **Self-bias:** the source resistor R_{s} lifts the source above the gate, which makes V_{GS} negative without a negative supply.

:::q <span class="tag">Manual Exp 10, aim</span>
To plot the frequency response of a common-source amplifier. Viva form: "Estimate the gain from g_{m} and the resistors, and say why the output is 180° out of phase."
:::

:::guess Guess first
CE gain was R_{C}/r_{e}. What do you think replaces 1/r_{e} for a FET?
:::

## The circuit and its bias

[[fig:exp10_circuit|Fig 10.1, redrawn: gate divider RA/RB, drain resistor R1, source resistor Rs bypassed by Cs, 10 kΩ load through C2.|w=88]]

| Part | Job |
|---|---|
| RA 6.8 MΩ, RB 1 MΩ | gate divider: V_{G} = 12 × 1/7.8 ≈ 1.54 V. Megohms are fine because the gate draws no current. |
| Rs 2.2 kΩ | self-bias: V_{GS} = V_{G} − I_{D}R_{s} is negative |
| Cs 100 µF | bypasses Rs for AC, giving full gain (as C_{E} did in Exp 6) |
| R1 3.3 kΩ | drain load: converts the I_{D} change into a voltage change |
| C1, C2 | coupling: block DC, pass the signal |

**Q-point (LTspice .op):** V_{G} = 1.54 V, V_{S} = 3.17 V, so **V_{GS} = −1.63 V**. I_{D} = 3.17/2.2k = **1.44 mA**, and V_{D} = 7.25 V. The drain sits well above the source, so the JFET is in saturation ✓.

**Gain by hand:** the small-signal model is a current source g_{m}v_{gs} into the drain.

$$A_{v} = −g_{m} (R_{1} ∥ R_{2}) = −g_{m} × (3.3 kΩ ∥ 10 kΩ) = −g_{m} × 2.48 kΩ$$

For the 2N5434 at this Q-point, g_{m} ≈ 9.7 mS (from its model: I_{DSS} ≈ 65 mA, V_{P} ≈ −1.9 V, using g_{m} = (2I_{DSS}/|V_{P}|)(1 − V_{GS}/V_{P})). So A_{v} ≈ −24. The **minus sign** is the 180° phase inversion: as v_{gs} goes up, I_{D} goes up, and the drain voltage V_{DD} − I_{D}R_{1} goes **down**.

## Do it

:::do Do it (LTspice)
1. Draw Fig 10.1 with J1 = **2N5434**, VDD = 12 V. Name the output node `out` (across R2).
2. Vin: `SINE(0 0.1 1k)` with AC amplitude `1`.
3. **Transient:** `.tran 10m`. Plot the input and V(out), and read both peak-to-peak values with cursors.
4. **Frequency response:** `.ac dec 10 100 100Meg`. Read the midband dB and find the two −3 dB frequencies.
5. Fill the table at 100 Hz, 1k, 5k, 10k, 50k, 100k, 500k, 1M, 5M, 10M, 100M.
:::

## What you should see

[[fig:exp10_tr|Transient: 0.2 V p-p in, ≈ 4.7 V p-p out, inverted.|w=82]]

[[fig:exp10_freq|AC: midband gain 24.3 (27.7 dB), f_{L} ≈ 32 Hz, f_{H} ≈ 4.5 MHz.|w=82]]

| f (Hz) | 100 | 1k | 5k | 10k | 50k | 100k | 500k | 1M | 5M | 10M | 100M |
|---|---|---|---|---|---|---|---|---|---|---|---|
| gain | 23.3 | 24.3 | 24.3 | 24.3 | 24.3 | 24.3 | 24.1 | 23.7 | 16.2 | 10.0 | 1.5 |
| dB | 27.3 | 27.7 | 27.7 | 27.7 | 27.7 | 27.7 | 27.6 | 27.5 | 24.2 | 20.0 | 3.4 |

## Calculation

- Transient gain = V_{O(pp)}/V_{in(pp)} = 4.73/0.2 = **23.6**.
- AC midband gain = **24.3**.
- BW = f_{H} − f_{L} = 4.48 MHz − 32 Hz ≈ **4.5 MHz**.

The low cut-off comes from Cs (with R_{s} ∥ 1/g_{m} ≈ 100 Ω) and from C2 (with R1 + R2). The high cut-off comes from the JFET's gate–drain and gate–source capacitances (35 pF each in its model), Miller-multiplied.

:::write Write in your record
**Result:** maximum gain ≈ **24.3 (27.7 dB)**; transient gain 4.73 V/0.2 V = 23.6; output 180° out of phase; f_{L} ≈ 32 Hz, f_{H} ≈ 4.5 MHz, bandwidth ≈ **4.5 MHz**.

**Theory for the record:** in a common-source amplifier the signal is applied to the gate and taken from the drain, with the source common (bypassed to AC ground). The gate divider and source resistor set a negative V_{GS} that biases the JFET in saturation. A gate-voltage change produces a drain-current change g_{m}v_{gs}, which develops an output voltage across the drain load: A_{v} = −g_{m}(R_{D} ∥ R_{L}). The output is inverted (180°). The input resistance is very high (set by the gate divider). The gain is lower than a BJT CE stage, but the input resistance and noise performance are better. Coupling/bypass capacitors set f_{L}; device capacitances set f_{H}.
:::

:::check Check 1
(a) Remove Cs. What happens to the gain, and why? (b) Why can the gate resistors be megohms here, when the BJT's bias resistors were kilohms? (c) Estimate the input resistance seen by the source.
:::

<!--ANSWERS-->

## Answers

**Opening question.** g_{m} replaces 1/r_{e}: A_{v} = −g_{m}(R_{D} ∥ R_{L}) ≈ −24. The output is inverted because a rising gate voltage raises I_{D}, which increases the drop across R1 and lowers the drain voltage.

**Check 1.** (a) The gain drops: R_{s} now gives negative feedback (as in Exp 8). A_{v} ≈ −g_{m}R_{D}'/(1 + g_{m}R_{s}) = −24/(1 + 9.7m × 2.2k) ≈ **−1.1**. (b) The JFET gate takes no current, so the divider is not loaded. A BJT's base current would make megohm resistors drop volts and wreck the bias. (c) R_{in} ≈ RA ∥ RB = 6.8 MΩ ∥ 1 MΩ ≈ **0.87 MΩ**.

<!--/ANSWERS-->
