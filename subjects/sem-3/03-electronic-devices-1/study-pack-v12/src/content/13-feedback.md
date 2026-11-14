# 13 — Feedback amplifiers

<div class="sub">Feedback deck (51 slides: gain table slide 32, topologies slides 16–27 and 41–45, effects slides 28–40) · syllabus Unit 6 · needs 12 (amplifier gain, R_{i}, R_{o})</div>

## Map

[[map:1 A_{f} = A/(1 + βA) > 2 The four topologies > 3 The effects|here=1]]

You have met feedback twice without the name: the unbypassed source resistor (07 §6) and the emitter resistor (11 §3) both sent part of the output back to oppose the input. This file gives the general theory: one formula, four connections, and what each does.

## The questions this file answers

- <span class="tag">Deck slide 32</span> β = 0.01. Find A_{f} for A = 1000 and A = 10 000. What do you notice?
- <span class="tag">Deck slides 16–27</span> Identify the topology of a CE stage with an unbypassed R_{E}, and its effect on the impedances.
- <span class="tag">Deck slides 28–40</span> Effects of negative feedback on gain, bandwidth, distortion and impedance.

---

## Build

### 1 · The gain with feedback

:::q <span class="tag">Deck slide 32 "Stabilization of Gain"</span>
An amplifier has feedback factor β = 0.01. Find the gain with feedback when the open-loop gain is 1000, and again when it is 10 000. What do you notice?
:::

:::guess Guess first
The open-loop gain grows ten times. Does the gain with feedback grow ten times?
:::

:::note Terms
**Open-loop gain A:** the amplifier alone. **Feedback factor β:** the fraction of the output returned to the input (not the transistor's β). **Closed-loop gain A_{f}:** the whole circuit with feedback.
:::

[[fig:fb_block|Feedback block diagram: V_{f} = βV_{o} is subtracted from V_{s}.|w=65]]

In **negative** feedback the returned signal is subtracted; in **positive** feedback it adds (14). The amplifier sees V_{i} = V_{s} − βV_{o}:

$$V_{o} = A(V_{s} − βV_{o})  ⟹  A_{f} = V_{o}/V_{s} = A/(1 + βA)$$

| Name | Expression | Meaning |
|---|---|---|
| Loop gain | βA | gain once round the loop |
| Amount of feedback (desensitivity) D | 1 + βA | gain falls by this factor; everything else improves by it |
| Feedback in dB | 20 log(1 + βA) | |

**The key result.** If βA ≫ 1, A_{f} ≈ 1/β: the gain depends only on the feedback network, made of stable resistors. The four basic amplifiers: **voltage** (V in, V out; wants high R_{i}, low R_{o}), **current** (I in, I out; low R_{i}, high R_{o}), **transconductance** (V in, I out; high R_{i}, high R_{o}), **transresistance** (I in, V out; low R_{i}, low R_{o}).

**Answer.** A = 1000: A_{f} = 1000/11 = **90.9**. A = 10 000: 10 000/101 = **99.0**. A changed by 900%, A_{f} by only 9%, and both are close to 1/β = 100. Feedback trades gain for stability.

:::note Slip in the slide
Slide 32 prints 98.3 for A = 5000. The formula gives 5000/51 = 98.0. The other entries (90.9, 99.0, 99.5) are correct.
:::

:::check Check 1
(a) Derive A_{f} = A/(1 + βA) from the block diagram, from memory. (b) A = 20 000, β = 0.01. Find A_{f}. (c) What is A_{f} when βA ≫ 1, and why is that useful?
:::

### 2 · The four topologies

:::q <span class="tag">practice · deck slides 16–27, 41–45</span>
A CE amplifier has an unbypassed emitter resistor R_{E}. Identify the feedback topology and say what it does to the input and output resistance.
:::

:::guess Guess first
Is the voltage across R_{E} proportional to the output voltage or to the output current?
:::

:::note Terms
**Sampling:** how the feedback senses the output: its voltage (across the load) or its current (in series with it). **Mixing:** how it is combined at the input: a voltage in series, or a current in shunt.
:::

[[fig:fb_topologies|The four topologies: sampled quantity – mixing.]]

| | Voltage-series | Voltage-shunt | Current-series | Current-shunt |
|---|---|---|---|---|
| Samples · mixes | V_{o} · series V | V_{o} · shunt I | I_{o} · series V | I_{o} · shunt I |
| Improves a | voltage amp | transresistance amp | transconductance amp | current amp |
| β | V_{f}/V_{o} | I_{f}/V_{o} (S) | V_{f}/I_{o} (Ω) | I_{f}/I_{o} |
| Z_{if} | Z_{i}(1 + βA) ↑ | Z_{i}/(1 + βA) ↓ | Z_{i}(1 + βA) ↑ | Z_{i}/(1 + βA) ↓ |
| Z_{of} | Z_{o}/(1 + βA) ↓ | Z_{o}/(1 + βA) ↓ | Z_{o}(1 + βA) ↑ | Z_{o}(1 + βA) ↑ |
| Example | emitter/source follower | collector-to-base resistor | CE with unbypassed R_{E} | two stages, 2nd emitter → 1st base |

**Two rules cover the table** (slide 40): a **series** connection at a port **raises** its resistance by (1 + βA); a **shunt** connection **lowers** it. At the output, voltage sampling is a shunt connection (Z_{o} falls) and current sampling is series (Z_{o} rises).

**Answer.** V_{f} = I_{o}R_{E} is proportional to the output current and sits in series with the input (v_{be} = v_{s} − v_{f}): **current-series**, β = −R_{E}. Both **Z_{i} and Z_{o} rise** by (1 + βA). With heavy feedback the gain becomes about −R_{C}/R_{E}.

:::check Check 2
(a) Which topology gives high Z_{in} and low Z_{out}? (b) Which lowers both? (c) In an emitter follower, what fraction of the output is fed back, and which topology is it?
:::

### 3 · What negative feedback does

:::q <span class="tag">practice · deck slides 28–40</span>
A = 1000, f_{H} = 20 kHz, Z_{i} = 2 kΩ, Z_{o} = 20 kΩ, 10% distortion. Voltage-series feedback with β = 0.1 is applied. Find A_{f}, the new f_{H}, Z_{if}, Z_{of} and the distortion.
:::

:::guess Guess first
One number, 1 + βA, appears in every answer. What is it here?
:::

[[fig:fb_bw|Feedback lowers the gain and widens the bandwidth; gain × bandwidth stays constant.|w=65]]

| Effect | Formula | Why |
|---|---|---|
| Gain reduced | A_{f} = A/(1 + βA) | the price |
| Gain stabilised | dA_{f}/A_{f} = (dA/A)/(1 + βA) | a change in A shrinks by (1 + βA) |
| Bandwidth widened | f_{Hf} = f_{H}(1 + βA), f_{Lf} = f_{L}/(1 + βA) | where A falls, feedback falls with it |
| Distortion, noise reduced | D_{f} = D/(1 + βA) | inside-loop distortion is fed back inverted |
| Impedances modified | × or ÷ (1 + βA) | per step 2 |

**Disadvantages.** Lower gain, so more stages; and if phase shifts add to 180° at some frequency, the feedback turns positive and the amplifier can oscillate (14 does it on purpose).

**Answer.** 1 + βA = **101**. A_{f} = **9.90**. f_{Hf} = **2.02 MHz**. Z_{if} = 2 k × 101 = **202 kΩ**, Z_{of} = 20 k/101 = **198 Ω**. Distortion **0.099%**. Check: gain × bandwidth = 20 MHz before and after.

:::check Check 3
Same amplifier: (a) A drops by 10% as it warms. By what percentage does A_{f} change? (b) f_{L} = 100 Hz. Find f_{Lf}. (c) List four advantages and one disadvantage of negative feedback.
:::

---

## Exam form

**Concept.** Block diagram; derive A_{f} = A/(1 + βA); loop gain, desensitivity; A_{f} ≈ 1/β.

**Topologies.** The 4-column table with Z_{if}, Z_{of} and an example; the two rules (series raises, shunt lowers).

**Effects.** Table: gain, stability (derive dA_{f}/A_{f} by differentiating A_{f}), bandwidth, distortion, impedances; disadvantages.

## Traps

- Confusing the feedback β with the transistor's β.
- Applying "Z_{o} falls" to current sampling: current sampling raises Z_{o}.
- Forgetting that the lower cutoff divides by (1 + βA) while the upper multiplies.
- Writing 98.3 from slide 32.

## Self-test

1. Derive dA_{f}/A_{f} = (dA/A)/(1 + βA).
2. A = 500, β = 0.02. Find A_{f}.
3. An amplifier with A = 2000 must have A_{f} = 50. Find β.
4. A resistor from collector to base of a CE stage: which topology, and what happens to Z_{i}?
5. A = 200, f_{H} = 50 kHz, β = 0.05. Find the new f_{H}.
6. Why can too much negative feedback make an amplifier oscillate?

<!--ANSWERS-->

## Answers

**Check 1.** (a) V_{i} = V_{s} − βV_{o}; V_{o} = A(V_{s} − βV_{o}); V_{o}(1 + βA) = AV_{s}. (b) 20 000/201 = **99.5**. (c) ≈ 1/β: the gain depends only on stable resistors, not on the transistor.

**Check 2.** (a) Voltage-series. (b) Voltage-shunt. (c) All of it: V_{f} = V_{o}, β = 1; voltage-series.

**Check 3.** (a) About 10%/101 ≈ **0.1%** (exactly: A = 900 gives 9.89, a fall of 0.11%). (b) 100/101 = **0.99 Hz**. (c) Stable gain, wider bandwidth, less distortion and noise, impedances raised or lowered as needed. Against: reduced gain (and possible instability).

**Self-test.**

1. A_{f} = A/(1 + βA); dA_{f}/dA = 1/(1 + βA)^{2}; divide by A_{f}: dA_{f}/A_{f} = (dA/A)/(1 + βA).
2. 1 + βA = 11: A_{f} = **45.5**.
3. 1 + βA = 2000/50 = 40, so β = 39/2000 = **0.0195**.
4. **Voltage-shunt**: Z_{i} **falls** by (1 + βA).
5. 1 + βA = 11: f_{Hf} = **550 kHz**.
6. At high frequency the amplifier's own phase shift can reach 180°; the subtracted signal then adds, and if the loop gain is ≥ 1 there, the circuit sustains its own output.

<!--/ANSWERS-->
