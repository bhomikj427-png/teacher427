# Exp 3 · Diode clipper circuits

<div class="sub">Manual pp. 13–14 · hands-on · CO3</div>

[[map:0 Instruments > 1 Zener curve > 2 Regulator > 3 Clipper > 4 Clamper|here=4]]

**What you already have:** a silicon diode conducts once its anode is about 0.7 V above its cathode (Exp 1, forward region). Below that it is an open circuit.

**Three terms first:**

- **Clipper:** a circuit that cuts off the part of a waveform above (or below) a set level.
- **Clipping level:** the voltage at which the cut happens.
- **Cut-in voltage V_{γ}:** the forward voltage at which a diode starts to conduct (≈ 0.7 V for silicon).

:::q <span class="tag">Manual Exp 3, aim</span>
To implement a diode clipper circuit and observe its output waveform. Viva form: "A 10 V-peak sine feeds Fig 3.1(a). At what level is it clipped, and which half is affected?"
:::

:::guess Guess first
Look at the circuit below and commit to a number and a half (top or bottom) before reading on.
:::

## How it works

[[fig:exp03a_circuit|Fig 3.1(a): diode anode at V_{o}, cathode at the + of a 2 V battery.|w=58]]

Treat the diode as a switch, and ask when its anode is more than 0.7 V above its cathode.

- The cathode sits at **+2 V** (the battery).
- The diode conducts when V_{o} > 2 + 0.7 = **2.7 V**. Then V_{o} is held at 2.7 V, and the rest of V_{in} drops across the 1 kΩ.
- When V_{in} < 2.7 V the diode is off: no current flows, so there is no drop across the 1 kΩ, and **V_{o} = V_{in}**.

Result: the **top** of the sine is cut flat at +2.7 V, and the bottom passes untouched.

[[fig:exp03b_circuit|Fig 3.2(a): diode and battery both reversed.|w=58]]

Here the diode's anode is at −2 V. It conducts when V_{o} < −2.7 V, so the **bottom** is clipped at −2.7 V.

[[fig:exp03_wave|LTspice with a 1N4007: clipping at ±2.66 V (this diode drops 0.66 V at the clipping current).|w=95]]

**Transfer characteristic** (V_{o} plotted against V_{i}, manual Fig 3.3): a 45° line (V_{o} = V_{i}) that turns flat at +2.7 V for (a), or at −2.7 V for (b).

:::do Do it (hands-on)
1. Generator: sine, **10 V peak** (20 V p-p on the DSO), 1 kHz. Check it on the DSO **before** connecting the circuit.
2. Breadboard: generator → 1 kΩ → output node. From the output node, connect the diode with its **anode at the output** (band/cathode away from the output), then its cathode to the **+** of the 2 V supply. Supply − goes to the generator's ground.
3. DSO CH1 on V_{in} and CH2 on V_{o}, both grounds at circuit ground. Coupling **DC** (AC coupling shifts the trace and hides the true level).
4. Read the clipping level: divisions × VOLTS/DIV.
5. Swap the diode **and** the supply polarity to build Fig 3.2(a). Repeat.
6. Optional: DSO **X-Y mode** (CH1 = x, CH2 = y) draws the transfer characteristic directly.
:::

:::write Write in your record
**Result:** clipping level ≈ **+2.7 V** for Fig 3.1(a) (positive clipper) and **−2.7 V** for Fig 3.2(a) (negative clipper). Measured with the 1N4007: about ±2.66 V.

**Theory for the record:** a clipper removes the part of a signal beyond a chosen level without disturbing the rest. A diode in series with a DC reference V_{R}, placed across the output, conducts when the output exceeds V_{R} + V_{γ}, holding the output at that level. Otherwise the diode is off and V_{o} = V_{i}. Reversing the diode and the reference clips the opposite half. The series resistor limits the current and drops the excess voltage. Clippers are used for wave shaping and to protect inputs from overvoltage.
:::

:::trap Trap: the DSO on AC coupling
AC coupling removes the DC average, so the flat top no longer reads +2.7 V. Use DC coupling for any clipping-level or clamping measurement.
:::

:::check Check 1
(a) Change the battery in Fig 3.1(a) to 5 V. New clipping level? (b) Remove the battery (short it) in Fig 3.1(a). New clipping level? (c) Why must the series 1 kΩ be there at all?
:::

<!--ANSWERS-->

## Answers

**Opening question.** At about +2.7 V (2 V battery + 0.7 V diode). The **positive** half is clipped.

**Check 1.** (a) 5 + 0.7 = **+5.7 V**. (b) **+0.7 V**: a plain diode clipper. (c) While the diode conducts, the output is pinned. The difference V_{in} − 2.7 V must drop somewhere, and the resistor takes it. Without it, the generator would drive a large current straight into the diode and battery.

<!--/ANSWERS-->
