# Exp 8 · Effect of negative feedback (removing the emitter bypass capacitor)

<div class="sub">Manual pp. 24–25 · LTspice · CO4, CO5 · the manual's two plots (≈ 42 dB and ≈ 4 dB) match the simulation below</div>

[[map:5 BJT curves > 6 CE amplifier > 7 Emitter follower > 8 Feedback|here=4]]

**What you already have:** from Exp 6, C_{E} bypasses R_{E}, and gain ≈ R_{C}/r_{e}. From Exp 7, a resistor in the emitter makes the output "follow" and pulls the gain down.

**Two terms first:**

- **Feedback:** feeding part of the output back to the input.
  - **Negative** feedback opposes the input. It lowers the gain but steadies everything else.
  - **Positive** feedback adds to the input. It leads to oscillation (Exp 11).
- **Current-series feedback:** the feedback voltage is produced by the output **current** (I_{E} ≈ I_{C} through R_{E}) and subtracted in **series** with the input (V_{BE} = v_{in} − I_{E}R_{E}).

:::q <span class="tag">Manual Exp 8, aim</span>
To observe the effect of negative feedback (emitter bypass capacitor) on the frequency response of an amplifier. Viva form: "Removing one capacitor cuts the gain from 122 to 1.7. Why would anyone want that?"
:::

:::guess Guess first
Name one thing that gets **better** when the gain drops.
:::

## The idea

[[fig:exp08_circuit|Fig 8.1, redrawn: a CE stage (2N2222) with load. C1 (red) is the bypass capacitor. Removing it is the whole experiment.|w=88]]

- **C1 in:** R4 is shorted for AC, so there is no feedback. A_{v} ≈ (R_{C} ∥ R_{L})/r_{e}, which is large.
- **C1 out:** the signal current through R4 (2.2 kΩ) makes a voltage that rises with the input, so the BE voltage the transistor actually sees shrinks. That is negative feedback. A_{v} ≈ (R_{C} ∥ R_{L})/(r_{e} + R_{E}) = 4.27k/2.2k ≈ 1.9 at the base.

**What negative feedback buys, at the cost of gain:**

| Property | Effect |
|---|---|
| gain | falls, but becomes **set by resistors** (R_{C}/R_{E}), not by β or temperature, so it is **stable** |
| bandwidth | **increases** (gain is traded for bandwidth) |
| distortion and noise | decrease |
| input resistance | increases (series feedback) |

## Do it

:::do Do it (LTspice)
1. Draw Fig 8.1. Q1 = **2N2222**. V2: AC amplitude `1`. Supply V1 = 15 V. Label the output `vo` (across R5, 47 kΩ).
2. Directive: `.ac dec 10 1 1Meg` (manual: 1 Hz – 1 MHz). Run. Plot V(vo): the solid line is the dB gain.
3. Read the peak dB with a cursor. Move the cursor to the frequencies where the gain is 3 dB lower: those are f_{L} and f_{H}.
4. **Delete C1** (or set it to `1p`). Run again and repeat.
5. Fill the table at 100 Hz, 500, 1k, 5k, 10k, 50k, 100k, 500k, 1M for both cases.
:::

## What you should see

[[fig:exp08_freq|LTspice. Blue: with C1, 41.7 dB peak, f_{L} 116 Hz, f_{H} 135 kHz. Red: without C1, 4.5 dB, f_{L} 9.5 Hz, f_{H} 4.1 MHz.|w=86]]

| f (Hz) | 100 | 500 | 1k | 5k | 10k | 50k | 100k | 500k | 1M |
|---|---|---|---|---|---|---|---|---|---|
| A_{v} with C1 | 79.8 | 119.1 | 121.4 | 122.1 | 121.9 | 114.5 | 98.0 | 31.7 | 16.3 |
| A_{vf} without C1 | 1.67 | 1.68 | 1.68 | 1.68 | 1.68 | 1.68 | 1.68 | 1.67 | 1.63 |

| | Without feedback (C1 in) | With feedback (C1 out) |
|---|---|---|
| maximum gain | 122 (41.7 dB) | 1.68 (4.5 dB) |
| f_{L} | 116 Hz | 9.5 Hz |
| f_{H} | 135 kHz | 4.1 MHz |
| bandwidth | ≈ **135 kHz** | ≈ **4.1 MHz** |

**Hand check** (Q-point: V_{B} = 3.56 V, V_{E} = 2.90 V, so I_{E} = 1.32 mA and r_{e} = 19.7 Ω):

- R_{in} with feedback = 68k ∥ 22k ∥ β × 2.2k ≈ 16 kΩ. The source divider is 16/(16 + 2.2) = 0.88.
- A_{vf} ≈ 0.88 × 4.27k/2.22k = **1.70** (LTspice: 1.68) ✓.

:::write Write in your record
**Result:** bandwidth ≈ **135 kHz** without feedback (gain 41.7 dB). With negative feedback (C_{E} removed), the gain falls to 4.5 dB and the bandwidth rises to ≈ **4.1 MHz**: the higher cut-off is far above 1 MHz, as the manual expects.

**Theory for the record:** removing the emitter bypass capacitor leaves R_{E} unbypassed. The AC emitter current develops a voltage across R_{E} that subtracts from the input in series: current-series negative feedback. The voltage gain falls from ≈ R_{C}/r_{e} to ≈ R_{C}/(r_{e} + R_{E}), but becomes stable (independent of β and temperature). The bandwidth increases, distortion and noise fall, and the input resistance rises. Negative feedback trades gain for bandwidth and stability.
:::

:::check Check 1
(a) Gain × bandwidth without feedback, and with feedback. Is the product the same? (b) Why is the 2N2222's own β almost irrelevant to the gain once C1 is out? (c) Which part of the response barely changed between the two cases at 100 kHz–1 MHz, and why?
:::

<!--ANSWERS-->

## Answers

**Opening question.** Negative feedback makes the gain **stable and predictable** (set by resistors, not β), **widens the bandwidth** (135 kHz → 4.1 MHz), and reduces distortion and noise. You add gain back with more stages; stability is hard to add later.

**Check 1.** (a) 122 × 135 kHz ≈ 16.5 MHz; 1.68 × 4.1 MHz ≈ 6.9 MHz. **Not the same**: "gain × bandwidth = constant" holds for a single dominant pole, not exactly for this circuit, but the direction (gain down, bandwidth up) holds. (b) A_{vf} ≈ (R_{C} ∥ R_{L})/(r_{e} + R_{E}), and R_{E} ≫ r_{e}, so β drops out. (c) The without-C1 curve is flat across it, while the with-C1 curve is already falling. With feedback, f_{H} moved out to MHz.

<!--/ANSWERS-->
