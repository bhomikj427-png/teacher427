# Exp 11 · RC phase-shift oscillator

<div class="sub">Manual pp. 31–33 · LTspice · CO4 · the manual's own observed frequency (13.76 kHz) and the simulation below (13.96 kHz) agree within 1.5 %</div>

[[map:9 JFET curves > 10 CS amplifier > 11 Oscillator > 12 MOSFET inverter|here=3]]

**What you already have:**

- From Exp 6, a CE stage inverts its signal (180°) and has gain.
- From Exp 8, negative feedback opposes the input.
- From C&S, in an RC circuit the voltage across R leads the input by an angle that depends on frequency.

**Two terms first:**

- **Oscillator:** a circuit that produces a steady AC output with **no** AC input. It is an amplifier whose output is fed back to its own input **in phase** (positive feedback).
- **Barkhausen criterion:** for steady oscillation, the loop gain must be |Aβ| = 1 (slightly more than 1 to start up), and the total phase shift around the loop must be **360°** (or 0°).

:::q <span class="tag">Manual Exp 11, aim</span>
To observe the frequency of oscillation of a phase-shift oscillator. Viva form: "Why three RC sections, and what is the frequency for R = 10 kΩ, C = 0.5 nF?"
:::

:::guess Guess first
The transistor gives 180°. How much must the RC network give, and how many degrees can one RC section give at most?
:::

## How it works

[[fig:rc_ladder|The feedback network: three CR sections, each adding phase lead. At one frequency the total is exactly 180°.|w=75]]

- The CE transistor inverts: **180°**. The RC network must add the other **180°** at the oscillation frequency, so the loop totals 360°.
- One RC section can give at most 90°, and only at f → 0, where the signal is gone. So **three** sections are used, about 60° each (in the manual's simple picture), to make 180° at a usable frequency.
- At exactly that frequency, the ladder's output is 1/29 of its input. So the **amplifier gain must be ≥ 29** for the loop gain to reach 1.

$$f = \frac{1}{2πRC\sqrt{2N}} = \frac{1}{2πRC\sqrt{6}}    (N = 3 sections)$$

For R = 10 kΩ, C = 0.5 nF:

$$f = \frac{1}{2π × 10^{4} × 0.5 × 10^{−9} × 2.449} = 13.0 kHz$$

For C = 1 nF: **6.50 kHz**.

[[fig:exp11_circuit|Fig 11.1, redrawn: a BC547B CE stage (10 V) with a three-section CR ladder from collector back to base.|w=92]]

:::do Do it (LTspice)
1. Draw Fig 11.1: Q1 = BC547B; R4 57k, R3 10k (bias); R1 6.8k (collector); R2 1.5k with C1 100n (emitter); ladder C2/C3/C4 = 0.5n, R5/R6 = 10k; V1 = 10 V. The third C goes back to the **base**.
2. Directive: `.tran 0 5m 2.5m` (simulate 5 ms, and plot only from 2.5 ms, after start-up). The circuit starts oscillating on its own. If the trace stays flat, add `startup` at the end of the directive to kick it.
3. Plot the collector voltage. Place cursor 1 on one peak and cursor 2 on a peak N cycles later. The readout gives the time difference and **Freq** (1/Δt). Divide the time difference by N for one period.
4. Change all three capacitors to `1n` and repeat.
:::

## What you should see

[[fig:exp11_wave|LTspice collector voltage (C = 0.5 nF): a steady oscillation of about 8.7 V p-p.|w=82]]

| S.No. | R | C | Observed f (LTspice) | Theoretical f | % error |
|---|---|---|---|---|---|
| 1 | 10 kΩ | 0.5 nF | 13.96 kHz | 13.00 kHz | 7.4 % |
| 2 | 10 kΩ | 1 nF | 8.40 kHz | 6.50 kHz | 29 % |

$$\% error = \frac{|f_{theory} − f_{observed}|}{f_{theory}} × 100 = \frac{|13.00 − 13.96|}{13.00} × 100 = 7.4 \%$$

**Why the error exists (and grows):** the formula assumes three **identical** sections and an ideal amplifier that doesn't load them. In the real circuit:

- the first C is driven through the 6.8 kΩ collector resistor, not from a zero-resistance source;
- the "third R" is not 10 kΩ but the base side: R3 ∥ R4 ∥ the transistor's input resistance, about 1–2 kΩ.

So the real network differs from the ideal one, and so does its 180° frequency. A % error of several percent is normal. LTspice shows the mismatch is worse at 1 nF.

:::write Write in your record
**Result:** the phase-shift oscillator produced **13.96 kHz** (C = 0.5 nF; theory 13.0 kHz, error 7.4 %) and **8.40 kHz** (C = 1 nF; theory 6.50 kHz). Increasing C (or R) lowers the frequency, as f ∝ 1/RC predicts.

**Theory for the record:** an oscillator is an amplifier with positive feedback that sustains an output without any input. The Barkhausen criterion requires a loop gain of at least 1 and a total loop phase shift of 360°. In the RC phase-shift oscillator, a CE transistor stage provides 180°, and a three-section RC ladder provides another 180° at f = 1/(2πRC√6). The ladder attenuates by 1/29 at that frequency, so the amplifier gain must be at least 29. Using more sections (e.g. four, 45° each) improves frequency stability. Varying R or C tunes the frequency. Used for audio-frequency sine generation.
:::

:::check Check 1
(a) Why can't two RC sections work? (b) The amplifier's gain is 20. What happens? (c) Calculate f for R = 4.7 kΩ, C = 1 nF.
:::

<!--ANSWERS-->

## Answers

**Opening question.** The network must add 180°. One section gives less than 90° (90° only at zero frequency), so at least three are needed: ≈ 60° each in the simple picture. f = 1/(2π × 10k × 0.5n × √6) = **13.0 kHz**.

**Check 1.** (a) Two sections reach 180° only at f → 0, where the signal is fully attenuated, so the loop can never meet the phase condition at a usable frequency. (b) Loop gain = 20/29 < 1: any oscillation dies out and the output stays flat. (c) f = 1/(2π × 4700 × 10⁻⁹ × 2.449) = **13.8 kHz**.

<!--/ANSWERS-->
