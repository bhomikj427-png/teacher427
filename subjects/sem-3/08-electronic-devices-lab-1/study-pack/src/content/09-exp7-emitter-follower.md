# Exp 7 · Emitter follower (common collector): verify its gain

<div class="sub">Manual pp. 22–23 · hands-on (with LTspice steps in the manual's procedure) · CO4, CO5</div>

[[map:5 BJT curves > 6 CE amplifier > 7 Emitter follower > 8 Feedback|here=3]]

**What you already have:** from Exp 6, r_{e} = 26 mV/I_{E}, and voltage-divider bias. From Exp 5, V_{E} = V_{B} − 0.7 V in the active region.

**Two terms first:**

- **Common collector (CC):** the collector sits at the supply, which is AC ground. Input at the base, output at the **emitter**.
- **Buffer:** a stage with gain ≈ 1, high input resistance and low output resistance. It copies a voltage without loading the source.

:::q <span class="tag">Manual Exp 7, aim</span>
Verify the gain of an emitter follower circuit. Viva form: "The gain is less than 1. Why would anyone build an amplifier that doesn't amplify voltage?"
:::

:::guess Guess first
Hint: think about **current** and about **resistance seen from each side**.
:::

## How it works

[[fig:exp07_circuit|Fig 7.1, redrawn: 33 kΩ / 3.3 kΩ divider, 2 kΩ emitter resistor, output taken from the emitter through 10 µF.|w=70]]

The emitter is always one diode-drop below the base: V_{E} = V_{B} − 0.7. So when the base moves up by 0.5 V, the emitter moves up by (almost) 0.5 V. The emitter **follows** the base. That is the whole idea.

**Q-point (LTspice .op):** V_{B} = 1.36 V, V_{E} = 0.75 V, I_{E} = 0.75/2k = **0.376 mA**.

$$r_{e} = \frac{26 mV}{0.376 mA} = 69 Ω          A_{v} = \frac{R_{E}}{R_{E} + r_{e}} = \frac{2000}{2069} = 0.967$$

| Property | Value here | Why |
|---|---|---|
| voltage gain | ≈ 0.97, **no inversion** | the emitter follows the base; the output is in phase |
| input resistance | ≈ 3 kΩ (bias resistors), ≈ 600 kΩ into the base alone | the base sees R_{E} multiplied by β: β(r_{e} + R_{E}) = 290 × 2.07 kΩ |
| output resistance | ≈ 70 Ω (≈ r_{e}) | looking back into the emitter |
| current gain | large (≈ β) | the base current is tiny; the emitter current is β + 1 times bigger |

So the answer to the viva question: it is a **current amplifier and impedance converter**. A weak, high-resistance source can drive a heavy, low-resistance load through it without its voltage sagging. That is why the extra design problem uses it as the output stage.

:::trap Trap: the manual's theory paragraph
It says the input impedance is "of the order of hundred ohms" and the output "of the order of ten ohms". The output part is right in spirit (tens of ohms). The input impedance is **high**: kilohms to hundreds of kilohms. High input, low output is the whole point.
:::

:::do Do it
**Hands-on:**

1. Build Fig 7.1. Use the **15 V** shown in the figure. The parts list says 10 V; see the trap below.
2. Check the Q-point with no signal: V_{B} ≈ 1.36 V, V_{E} ≈ 0.75 V.
3. Generator: sine, 0.5 V peak, 1 kHz, into C2. DSO CH1 on the input, CH2 on V_{out}. The two traces should overlap, in phase.
4. Step the frequency through 200 Hz, 500, 1k, 10k, 100k, 1 MHz and record V_{o}. Gain = V_{o}/V_{i}.

**LTspice (manual's procedure):**

1. V2 with `SINE(0 0.5 1k)` and AC amplitude `0.5`. Q1 = BC547B.
2. Run `.tran 10m` and compare V(out) with the input.
3. Then run `.ac dec 10 200 1Meg`. Comment out the line you are not using (right-click the directive and choose **Comment**), or the `;` prefix in the manual's figure does the same thing.
:::

## What you should see

[[fig:exp07_tr|LTspice: output (solid) sits on the input (dashed), in phase, 0.96 V p-p for 1.0 V p-p in.|w=82]]

[[fig:exp07_freq|Gain ≈ 0.97 across the whole 200 Hz – 1 MHz sweep. Neither −3 dB point is inside the sweep: f_{L} ≈ 5 Hz, f_{H} far above 1 MHz.|w=82]]

| f (Hz) | 200 | 500 | 1k | 10k | 100k | 1M |
|---|---|---|---|---|---|---|
| A_{v} | 0.965 | 0.966 | 0.966 | 0.966 | 0.966 | 0.966 |
| dB | −0.31 | −0.30 | −0.30 | −0.30 | −0.30 | −0.30 |

:::trap Trap: a 10 V supply clips the output
With 10 V, V_{E} drops to about 0.35 V. A 0.5 V-peak input then pulls the emitter below 0 V and the transistor cuts off: LTspice shows the negative half flattened at −0.32 V. With 10 V, either use 0.2 V peak (clean) or the figure's 15 V.
:::

:::write Write in your record
**Result:** maximum gain of the emitter follower ≈ **0.97** (−0.3 dB), output in phase with input; flat from 200 Hz to 1 MHz, so the bandwidth exceeds the measured range (simulation: f_{L} ≈ 5 Hz).

**Theory for the record:** in the common-collector (emitter follower) circuit, the input is applied to the base and the output taken from the emitter, while the collector is at AC ground. Because V_{E} = V_{B} − V_{BE}, the emitter follows the base: voltage gain is slightly below 1 (R_{E}/(R_{E} + r_{e})) with no phase inversion. The input resistance is high (≈ βR_{E}) and the output resistance low (≈ r_{e}), so the stage is used as a buffer for impedance matching from a high-impedance source to a low-impedance load. It has a high current gain and power gain, and a wide bandwidth.
:::

:::check Check 1
(a) Why is A_{v} always a little less than 1, never exactly 1? (b) Change R_{E} to 1 kΩ (same bias). Estimate the new I_{E}, r_{e} and A_{v}. (c) Which stage, CE or CC, would you put directly in front of an 8 Ω speaker, and why?
:::

<!--ANSWERS-->

## Answers

**Opening question.** It amplifies **current** (≈ β) and therefore power. It also converts a high source resistance into a low output resistance (a buffer), so a weak source can drive a heavy load.

**Check 1.** (a) The output is taken across R_{E}, which is in series with r_{e}: A_{v} = R_{E}/(R_{E} + r_{e}). r_{e} is never zero. (b) I_{E} = 0.75/1k = 0.75 mA, r_{e} = 26/0.75 = 35 Ω, A_{v} = 1000/1035 = **0.966**: still about the same. (c) **CC (emitter follower).** Its output resistance is tiny, so the 8 Ω load does not collapse the voltage. A CE stage's output resistance (≈ R_{C}) would drop most of the signal internally.

<!--/ANSWERS-->
