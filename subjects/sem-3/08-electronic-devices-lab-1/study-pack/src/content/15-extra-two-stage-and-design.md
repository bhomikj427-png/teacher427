# Extra · Two-stage RC-coupled amplifier, and the design problem

<div class="sub">Manual pp. 3 and 36–38 · LTspice · the design answer is verified spec-by-spec in LTspice (src/sim/design.py)</div>

[[map:6 CE amplifier > 7 Emitter follower > 8 Feedback > Extra: cascade + design|here=4]]

**What you already have:**

- From Exp 6, one CE stage: gain ≈ R_{C}/r_{e}, bandwidth f_{L} to f_{H}.
- From Exp 7, the emitter follower: low output resistance.
- From Exp 8, unbypassed R_{E} lowers gain and raises input resistance.

**Two terms first:**

- **Cascade:** stages in series, each one's output feeding the next one's input.
- **RC coupling:** the link between stages is a capacitor (it blocks one stage's DC from the next) plus the next stage's bias resistors.

## Part 1 · Two-stage RC-coupled amplifier

:::q <span class="tag">Manual, additional experiment</span>
To measure the gain and plot the frequency response of a two-stage RC-coupled amplifier and determine its 3 dB bandwidth. Viva form: "Two stages: does the gain add or multiply, and what happens to the bandwidth?"
:::

:::guess Guess first
Answer both halves before reading on.
:::

[[fig:expA_circuit|Fig E.2, redrawn: two copies of the Exp 6 stage. C3 couples Q1's collector to Q2's base; the load is R11 = 1 kΩ.|w=100]]

- **Gains multiply:** A_{total} = A_{1} × A_{2}. Decibels therefore **add**: dB_{total} = dB_{1} + dB_{2}.
- **Each A must be the gain *in place*.** Stage 1 is loaded by stage 2's input resistance. Stage 2 is driven by stage 1's output resistance (560 Ω) instead of the 2.2 kΩ generator resistance, so it gains more than stage 1 does.
- **Bandwidth shrinks.** At f_{L} and f_{H}, *each* stage is already down by some amount, and the losses multiply. So the cascade's −3 dB points move inward: f_{L} rises and f_{H} falls.

:::do Do it (LTspice)
1. Draw Fig E.1 (single stage, R5 = 1 kΩ load). Q1 = BC547B, V1 = 15 V, V2 with AC amplitude `0.5` (the manual says 5 V; either works for `.ac`, which is linear).
2. Directive: `.ac dec 10 100 1Meg` (or 500 Hz – 3 MHz as in the procedure). Run, then read the midband dB, f_{L} and f_{H}.
3. Copy the stage. Connect C3 from Q1's collector to Q2's base, and put the 1 kΩ load at the end. Run again.
4. Plot both V(b2) (the output of stage 1) and V(out), so you can fill both columns of the table.
:::

:::trap Trap: no transient at 0.5 V
With a gain of about 1600, a 0.5 V input asks for an 800 V output. Any `.tran` run at that level is pure clipping. Use millivolts for transient, or stick to `.ac`.
:::

[[fig:expA_freq|LTspice. One stage: 27.4 dB, f_{L} 310 Hz, f_{H} 833 kHz. Two stages: 64.0 dB, f_{L} 609 Hz, f_{H} 632 kHz.|w=86]]

| f (Hz) | 100 | 500 | 1k | 5k | 10k | 100k | 500k | 1M | 2M | 3M |
|---|---|---|---|---|---|---|---|---|---|---|
| one stage A_{v} | 7.2 | 19.9 | 22.4 | 23.4 | 23.4 | 23.3 | 20.1 | 15.0 | 9.0 | 6.3 |
| two stages A_{v} | 103 | 990 | 1379 | 1584 | 1591 | 1575 | 1252 | 839 | 435 | 264 |

| | Single stage | Two stage |
|---|---|---|
| midband gain | 23.4 (27.4 dB) | 1591 (64.0 dB) |
| f_{L} | 310 Hz | 609 Hz |
| f_{H} | 833 kHz | 632 kHz |
| bandwidth | ≈ 833 kHz | ≈ 632 kHz |

**Gains multiply, in place:** inside the cascade at 10 kHz, stage 1 gives 25.8 and stage 2 gives 61.8, so 25.8 × 61.8 = **1594** ≈ 1591 ✓. In dB: 28.2 + 35.8 = 64.0 dB ✓. The stage-alone figure (23.4) is not the in-place gain, so 23.4² ≠ 1591.

:::write Write in your record
**Result:** two-stage gain **64.0 dB** (1591) against **27.4 dB** for one stage; bandwidth falls from ≈ 833 kHz to ≈ **632 kHz** (f_{L} = 609 Hz, f_{H} = 632 kHz). Higher gain, narrower bandwidth.

**Theory for the record:** when amplifier stages are cascaded, the overall voltage gain is the product of the individual (loaded) stage gains, so gains in dB add. In RC coupling, the coupling capacitor passes the AC signal from one stage's collector to the next stage's base while blocking DC, so each stage keeps its own bias. It is cheap and gives a flat midband response. The overall bandwidth is narrower than a single stage's, because each stage's roll-off multiplies: the cascade's lower cut-off rises and its upper cut-off falls.
:::

## Part 2 · The design problem (manual p. 3)

:::q <span class="tag">Manual p. 3 · design experiment</span>
Design a small-signal voltage amplifier with: (1) voltage gain ≥ 50; (2) input resistance ≥ 15 kΩ; (3) output resistance < 100 Ω; (4) maximum unclipped output of 2 V p-p; (5) 9 V supply and low current drain.
:::

:::guess Guess first
Which single stage from Exps 6–8 meets *both* "gain ≥ 50" and "R_{out} < 100 Ω"? If none, what combination does?
:::

**The reasoning, one spec at a time:**

1. **Gain ≥ 50** calls for a CE stage. But a fully bypassed CE stage has a low R_{in} (≈ βr_{e}, about 1 kΩ in Exp 6).
2. **R_{in} ≥ 15 kΩ:** leave a small part of R_{E} **unbypassed** (R_{E1}). The base then sees β(r_{e} + R_{E1}), which is much larger, at the cost of some gain (Exp 8, partly). Use large bias resistors.
3. **R_{out} < 100 Ω:** a CE output is ≈ R_{C} (kilohms), so it fails. Add an **emitter follower** as stage 2 (Exp 7): R_{out} ≈ r_{e2} + R_{C}/β, which is tens of ohms.
4. **Low current drain:** run stage 1 at about 0.6 mA and stage 2 at about 2 mA.

[[fig:design_circuit|Verified design. Stage 1 is a CE with R_{E1} = 82 Ω unbypassed; stage 2 is an emitter follower direct-coupled from Q1's collector. Both BC547B.|w=95]]

**Hand design:**

- **Stage 1 bias:** V_{B1} = 9 × 33/(220 + 33) = 1.17 V, V_{E1} ≈ 0.5 V, I_{E1} = 0.5/(82 + 820) ≈ 0.55 mA, r_{e1} = 26/0.55 ≈ 47 Ω.
- **Stage 1 gain:** ≈ R_{C}/(r_{e1} + R_{E1}) = 8.2k/(47 + 82) ≈ **64**.
- **R_{in}:** = 220k ∥ 33k ∥ β(r_{e1} + R_{E1}) = 28.7k ∥ (290 × 129 Ω = 37k) ≈ **16 kΩ** ✓.
- **Stage 2:** V_{C1} ≈ 9 − 0.55m × 8.2k ≈ 4.4 V, so V_{E2} ≈ 3.7 V, I_{E2} = 3.7/1.8k ≈ 2 mA, r_{e2} = 13 Ω. R_{out} ≈ 13 + 8.2k/290 ≈ **41 Ω** ✓.
- **Swing:** V_{E2} = 3.7 V sits mid-supply, with room for ±1 V and more ✓.

**LTspice check of every spec** (`src/sim/design.py`):

| Spec | Required | Simulated | |
|---|---|---|---|
| voltage gain (1 kHz, 10 kΩ load) | ≥ 50 | **59.7** | ✓ |
| input resistance | ≥ 15 kΩ | **16.2 kΩ** | ✓ |
| output resistance | < 100 Ω | **39 Ω** | ✓ |
| unclipped output | 2 V p-p | **2.95 V p-p** clean (±1.43/−1.52 V at 25 mV in) | ✓ |
| supply / current | 9 V, low | 9 V, **2.68 mA** total | ✓ |
| bandwidth (bonus) | | 14 Hz to 4.4 MHz | |

:::check Check 1
(a) Two stages have midband gains of 20 dB and 26 dB in place. Give the overall gain as a ratio. (b) Why not reach "gain ≥ 50" with a fully bypassed emitter in the design? (c) In the design, which single resistor would you change to raise the gain, and what does it cost?
:::

<!--ANSWERS-->

## Answers

**Part 1 question.** Gains **multiply** (dB add). Bandwidth **shrinks**: f_{L} rises and f_{H} falls.

**Part 2 question.** No single stage meets both specs: CE has gain but high R_{out}, and CC has low R_{out} but gain < 1. So use **CE followed by CC**.

**Check 1.** (a) 46 dB = 10^{46/20} ≈ **200**. (b) The input resistance would drop to about βr_{e} ≈ 13 kΩ in parallel with the bias network (and lower at higher current), failing the 15 kΩ spec. The unbypassed R_{E1} is what lifts R_{in}. (c) Lower R_{E1} (or raise R_{C}). Lower R_{E1} raises the gain but lowers R_{in} (back towards the 15 kΩ limit) and adds distortion. Raising R_{C} raises the gain but lowers V_{C1}, which eats into the output swing.

<!--/ANSWERS-->
