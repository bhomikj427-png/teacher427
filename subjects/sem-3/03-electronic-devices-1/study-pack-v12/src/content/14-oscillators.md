# 14 — Oscillators

<div class="sub">Oscillator deck (phase-shift design example, Wien-bridge slides) · deck "crystal" (3 slides) · syllabus Unit 7 · needs 13 (the feedback loop)</div>

## Map

[[map:1 Barkhausen criterion > 2 RC phase-shift > 3 Wien bridge > 4 Hartley, Colpitts > 5 Crystal|here=1]]

13 subtracted the fed-back signal. Add it instead, with exactly the right size and timing, and the amplifier needs no input: it keeps itself going and makes a steady wave from the DC supply alone.

## The questions this file answers

- <span class="tag">Syllabus Unit 7</span> State the Barkhausen criterion.
- <span class="tag">Deck</span> Design a phase-shift oscillator for 800 Hz with 10 nF capacitors.
- <span class="tag">practice</span> Wien bridge: f_{0} and R_{2}. Colpitts and Hartley frequencies.
- <span class="tag">Deck "crystal"</span> Series and parallel resonance and the Q of a crystal.

---

## Build

### 1 · The Barkhausen criterion

:::q <span class="tag">Syllabus Unit 7</span>
State the Barkhausen criterion for sustained oscillations.
:::

:::guess Guess first
With positive feedback, A_{f} = A/(1 − βA). What value of βA makes the gain infinite?
:::

:::note Terms
**Oscillator:** produces a repeating output with no input signal; converts DC power into AC. **Positive feedback:** the returned signal is in phase with the input and adds to it.
:::

[[fig:osc_block|An oscillator is an amplifier whose feedback network closes the loop with 0° total phase.|w=60]]

When βA = 1 the denominator is zero: a finite output with zero input. A signal that goes once round the loop and arrives back with the same size and phase sustains itself.

**Answer.** Sustained sinusoidal oscillation occurs at the frequency where **|βA| = 1** and the **total loop phase shift is 0° or 360°**. If |βA| &lt; 1 the oscillation dies; if &gt; 1 it grows until the amplifier clips. Start-up: circuit noise contains every frequency; the frequency-selective network lets only one meet the phase condition. In practice |βA| is set slightly above 1, and the amplifier's non-linearity brings it back to 1.

| Type | Feedback network | Range | Examples |
|---|---|---|---|
| RC | resistors, capacitors | a few Hz to about 1 MHz (audio) | phase-shift, Wien bridge |
| LC | resonant tank | 100 kHz to 100 MHz (radio) | Hartley, Colpitts |
| Crystal | quartz crystal | 10 kHz to 30 MHz, very stable | clocks |
| Relaxation | RC timing + switch | — | square, triangle, sawtooth |

:::check Check 1
(a) What happens if the loop gain is 0.9? 1.5? (b) An inverting amplifier contributes 180°. What must the feedback network add?
:::

### 2 · The RC phase-shift oscillator

:::q <span class="tag">Deck design example</span>
Design a phase-shift oscillator for a frequency of 800 Hz. The capacitors are to be 10 nF.
:::

:::guess Guess first
One RC section shifts the phase by less than 90°. How many sections are needed for 180°?
:::

[[fig:phase_shift_osc|Op-amp RC phase-shift oscillator.|w=70]]

The inverting amplifier gives 180°; three identical RC sections give the other 180° at exactly one frequency:

$$f_{0} = 1/(2πRC√6)      β = 1/29 at f_{0}      so |A| ≥ 29, R_{f} = 29R$$

The third R is the op-amp's input resistor (the inverting input is a virtual ground). FET version: same f_{0}, g_{m}R_{L} ≥ 29. BJT version: f_{0} = 1/(2πRC√(6 + 4R_{C}/R)), h_{fe} ≥ 23 + 29(R/R_{C}) + 4(R_{C}/R). Tuning needs all three R or C changed together, so it suits fixed audio frequencies.

**Answer.** R = 1/(2π × 800 × 10^{−8} × 2.449) = **8.12 kΩ**; use 8.2 kΩ. R_{f} = 29 × 8.2 k = **238 kΩ** (the deck's value). With 8.2 kΩ the frequency is 792 Hz.

:::check Check 2
(a) Why three sections, not two? (b) R = 10 kΩ, C = 0.01 μF: find f_{0} and R_{f}.
:::

### 3 · The Wien-bridge oscillator

:::q <span class="tag">practice · Wien-bridge slides</span>
A Wien-bridge oscillator uses R = 10 kΩ and C = 10 nF. Find f_{0}. If R_{1} = 10 kΩ, what should R_{2} be?
:::

:::guess Guess first
This amplifier is non-inverting. How much phase shift may the feedback network add?
:::

[[fig:wien_osc|Wien-bridge oscillator: series RC and parallel RC form the lead-lag network.|w=65]]

The **lead-lag network**: at low f the series C blocks; at high f the parallel C shorts. At one frequency the output is largest and **in phase**:

$$f_{0} = 1/(2πRC)      β = 1/3, 0°      1 + R_{2}/R_{1} = 3  ⟹  R_{2} = 2R_{1}$$

To start, R_{2}/R_{1} is made slightly more than 2. The two RC arms with R_{1}, R_{2} form a bridge. Clean sine, easy tuning (gang the two Cs): the standard audio oscillator.

| | RC phase-shift | Wien bridge |
|---|---|---|
| Amplifier | inverting (180°) | non-inverting (0°) |
| Network | three RC sections, 180° | lead-lag, 0° |
| f_{0} | 1/(2πRC√6) | 1/(2πRC) |
| β · gain needed | 1/29 · 29 | 1/3 · 3 |
| Tuning | awkward | easy |

**Answer.** f_{0} = 1/(2π × 10^{4} × 10^{−8}) = **1.59 kHz**. R_{2} = 2R_{1} = **20 kΩ** (slightly more, to start).

:::check Check 3
(a) To double the frequency, what do you do to C? (b) Why is the amplifier non-inverting here but inverting in the phase-shift oscillator?
:::

### 4 · LC oscillators: Hartley and Colpitts

:::q <span class="tag">practice</span>
A Colpitts oscillator has C_{1} = C_{2} = 200 pF and L = 1 mH. Find the frequency of oscillation.
:::

:::guess Guess first
The two capacitors are in series round the tank. Is their combined value more or less than 200 pF?
:::

:::note Terms
**Tank circuit:** L and C in a loop; energy swings between them at f_{0} = 1/(2π√(LC)).
:::

[[fig:lc_tanks|Hartley taps the inductor; Colpitts taps the capacitor.]]

A tank rings and dies away; the amplifier tops up the lost energy each cycle. The grounded tap puts the tank's two ends 180° apart, which with an inverting amplifier makes 360°.

| | Hartley | Colpitts |
|---|---|---|
| Tapped element | inductor: L_{1}, L_{2} | capacitor: C_{1}, C_{2} in series |
| Equivalent | L_{eq} = L_{1} + L_{2} (+ 2M if coupled) | C_{eq} = C_{1}C_{2}/(C_{1} + C_{2}) |
| f_{0} | 1/(2π√(L_{eq}C)) | 1/(2π√(LC_{eq})) |
| Notes | one variable C tunes it | better stability at high f |

Memory hook: **C**olpitts splits the **C**apacitor.

**Answer.** C_{eq} = 100 pF. f_{0} = 1/(2π√(10^{−3} × 10^{−10})) = **503 kHz**.

:::check Check 4
(a) Hartley: L_{1} = L_{2} = 1 mH (no coupling), C = 100 pF. Find f_{0}. (b) Why are LC oscillators not used at audio frequencies?
:::

### 5 · The crystal oscillator

:::q <span class="tag">Deck "crystal"</span>
A quartz crystal has L_{s} = 1 H, C_{s} = 0.01 pF, R_{s} = 1 kΩ and C_{p} = 10 pF. Find its series resonant frequency, how far above it the parallel resonance lies, and its Q.
:::

:::guess Guess first
An ordinary LC tank has a Q of about 100. Will the crystal's be similar?
:::

:::note Terms
**Piezoelectric effect:** squeezing quartz produces a voltage; the **inverse** effect: a voltage makes it change shape. **Q:** how sharply a resonator selects one frequency, Q = ω_{s}L/R.
:::

[[fig:crystal_fig|Crystal symbol and equivalent circuit: R_{s}–L_{s}–C_{s} in series, with C_{p} across.|w=60]]

An AC voltage makes the quartz vibrate; it vibrates strongly only at its mechanical frequency (set by cut and thickness), and the vibration produces a voltage back. Electrically: R_{s}, L_{s}, C_{s} (friction, mass, stiffness) in parallel with C_{p} (plates and holder).

$$f_{s} = 1/(2π√(L_{s}C_{s}))      f_{p} = f_{s}√(1 + C_{s}/C_{p})$$

At f_{s} the impedance is lowest (R_{s}); at f_{p}, just above, it is very large; between them the crystal is inductive. In an oscillator it replaces the tank or the inductor of a Colpitts circuit.

**Answer.** f_{s} = 1/(2π√(10^{−14})) = **1.592 MHz**. f_{p} = f_{s} × 1.0005, **795 Hz above**. Q = 2π × 1.592 × 10^{6} × 1/1000 = **10 000**, about 100 times an LC tank. So the frequency hardly moves with temperature, supply or ageing; it cannot be tuned over a range.

:::check Check 5
(a) Draw the equivalent circuit from memory and name each element. (b) Why is a crystal oscillator more stable than an LC oscillator?
:::

---

## Exam form

**Barkhausen.** |βA| = 1, loop phase 0°/360°; start-up from noise with |βA| slightly &gt; 1.

**Phase-shift.** Circuit; three sections, 180°; f_{0} = 1/(2πRC√6); β = 1/29, A ≥ 29.

**Wien bridge.** Circuit; lead-lag 0°; f_{0} = 1/(2πRC); β = 1/3, A = 3, R_{2} = 2R_{1}. Comparison table.

**LC.** Hartley and Colpitts circuits, L_{eq} / C_{eq}, f_{0}; comparison.

**Crystal.** Piezoelectric effect; equivalent circuit; f_{s}, f_{p}; Q 10^{4}–10^{6}; why stable.

## Traps

- Writing the Wien gain as 29 or the phase-shift gain as 3: swap check with β.
- Adding C_{1} + C_{2} for Colpitts: they are in series.
- Forgetting √6 in the phase-shift formula.
- Writing f_{0} = 1/(2πLC) without the square root.

## Self-test

1. State the Barkhausen criterion and explain how an oscillator starts.
2. Phase-shift oscillator, R = 5 kΩ, C = 0.01 μF. Find f_{0}.
3. Wien bridge, R = 1 kΩ, C = 0.1 μF. Find f_{0}.
4. Colpitts: C_{1} = 100 pF, C_{2} = 400 pF, L = 50 μH. Find f_{0}.
5. Hartley: L_{1} = 0.5 mH, L_{2} = 1 mH (no coupling), C = 200 pF. Find f_{0}.
6. Compare RC, LC and crystal oscillators in three points.

<!--ANSWERS-->

## Answers

**Check 1.** (a) 0.9: dies out. 1.5: grows until the amplifier saturates; clipped, distorted. (b) Another **180°**.

**Check 2.** (a) One section gives less than 90°, so two give less than 180°; three is the fewest that can reach 180°. (b) f_{0} = 1/(2π × 10^{4} × 10^{−8} × 2.449) = **650 Hz**; R_{f} = **290 kΩ**.

**Check 3.** (a) **Halve** both capacitors. (b) The Wien network adds 0°, so the amplifier must add 0°; the phase-shift network adds 180°, so the amplifier adds the other 180°.

**Check 4.** (a) L_{eq} = 2 mH: f_{0} = 1/(2π√(2 × 10^{−13})) = **356 kHz**. (b) Low f would need very large, heavy, costly L and C.

**Check 5.** (a) R_{s}, L_{s}, C_{s} in series (friction loss, vibrating mass, stiffness), all in parallel with C_{p} (plates and holder). (b) Its Q is far higher (10^{4}–10^{6}), so the resonance is very sharp and barely drifts.

**Self-test.**

1. See step 1.
2. **1.30 kHz**.
3. **1.59 kHz**.
4. C_{eq} = 80 pF: **2.52 MHz**.
5. L_{eq} = 1.5 mH: **291 kHz**.
6. Range (audio / radio / fixed up to tens of MHz); tuning (RC easy for Wien, LC with one variable C, crystal fixed); stability (crystal far best, Q 10^{4}–10^{6}).

<!--/ANSWERS-->
