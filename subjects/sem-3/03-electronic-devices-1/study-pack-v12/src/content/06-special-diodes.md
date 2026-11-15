# 06 — Special diodes: LED, photodiode, tunnel diode

<div class="sub">Deck "LED, Tunnel, Photo" · beyond the syllabus text, taught on the slides · needs 03 (the junction) and 02b (recombination)</div>

## Map

[[map:1 LED > 2 Photodiode > 3 Tunnel diode|here=1]]

Three junctions built for one job each: turn current into light, turn light into current, and use a junction so thin that electrons pass straight through it.

## The questions this file answers

- <span class="tag">Deck</span> How does an LED work, and why isn't it made of silicon?
- <span class="tag">Deck</span> Why is a photodiode reverse biased? What is a PIN photodiode?
- <span class="tag">Deck</span> Draw the V–I characteristic of a tunnel diode and explain the negative-resistance region.

---

## Build

### 1 · The LED

:::guess Predict
In 02b, recombination in Si gave heat and in GaAs gave light. Which material would you make an LED from, and why?
:::

[[fig:special_symbols|Symbols: LED, photodiode, tunnel diode.|w=60]]

- **Forward biased.** Electrons and holes recombine at the junction; each recombination releases a **photon**.
- Needs a **direct-gap** material (GaAs, GaAsP, GaN), not Si.
- The colour is set by the gap: **λ(μm) = 1.24/E_{g}(eV)**.
- Forward drop 1.8–3.3 V. Always used with a **series resistor** to set the current.

**Answer.** GaAs or another direct-gap compound: Si's gap is indirect, so recombination goes through traps and gives heat, not light.

:::check Check 1
(a) A red LED material has E_{g} = 1.9 eV. Find λ. (b) Why does an LED need a series resistor?
:::

### 2 · The photodiode

:::guess Predict
Light falling on a junction creates electron–hole pairs. Under which bias will those extra carriers be the biggest fraction of the current?
:::

- **Reverse biased.** Light in the depletion region generates electron–hole pairs; the field sweeps them out as extra reverse current.
- Current ∝ light intensity. With no light only the small **dark current** flows.
- **PIN photodiode:** an undoped (intrinsic) layer between p and n widens the depletion region: more light absorbed, less capacitance, faster.

**Answer.** Reverse bias: the normal current is only the tiny I_{s}, so the light-generated current dominates and is proportional to the light.

:::check Check 2
What carries the photodiode's current, and why does a PIN structure respond faster?
:::

### 3 · The tunnel diode

:::q <span class="tag">Deck</span>
Draw the V–I characteristic of a tunnel diode and explain the negative-resistance region.
:::

:::guess Guess first
What would "negative resistance" have to mean on an I–V graph?
:::

[[fig:tunnel_iv|Tunnel diode: peak I_{p} at V_{p}, valley I_{v} at V_{v}, negative slope between.|w=60]]

Doping about 1000 times heavier than normal makes the depletion region only about 10 nm thick, so electrons **tunnel** straight through the barrier. Very fast; used in microwave oscillators and fast switches.

**Answer.** As forward voltage rises from zero, filled states on the n side line up with empty states on the p side and tunnel current rises to the **peak I_{p} at V_{p}**. Further voltage pulls those states out of line, so fewer electrons tunnel and the current falls to the **valley I_{v} at V_{v}**. Between them dI/dV is negative: **negative resistance**. Beyond the valley, ordinary diode current rises again.

:::check Check 3
Why does the tunnel diode's negative-resistance region make it useful in an oscillator (14)?
:::

---

## Exam form

| Device | Bias | Principle | Key facts |
|---|---|---|---|
| LED | forward | recombination releases photons | direct gap; λ = 1.24/E_{g}; 1.8–3.3 V; series R |
| Photodiode | reverse | light generates pairs in the depletion region | current ∝ light; dark current; PIN faster |
| Tunnel | small forward | tunnelling through a ~10 nm barrier | heavy doping; negative resistance; microwave |

Draw the tunnel characteristic with I_{p}, V_{p}, I_{v}, V_{v} marked.

## Traps

- Saying a photodiode is forward biased.
- Saying silicon LEDs are common: Si cannot emit efficiently.
- Forgetting the units in λ = 1.24/E_{g}: μm and eV.

## Self-test

1. A green LED has E_{g} = 2.3 eV. Find λ.
2. An LED drops 2 V at 20 mA from a 5 V supply. Find the series resistor.
3. What is dark current?
4. Give two applications of a tunnel diode.
5. Why is the tunnel diode's depletion region so thin?

<!--ANSWERS-->

## Answers

**Check 1.** (a) 1.24/1.9 = **0.653 μm** (653 nm, red). (b) Its I–V is steep (like any diode): without a resistor a small supply change gives a huge current.

**Check 2.** Light-generated electron–hole pairs swept out by the depletion field. The PIN's wide depletion region gives lower capacitance, so it responds faster (and absorbs more light).

**Check 3.** A negative resistance supplies energy to a tuned circuit, cancelling its loss resistance, so oscillation is sustained (the loop condition of 14).

**Self-test.**

1. 1.24/2.3 = **0.539 μm** (539 nm).
2. (5 − 2)/20 mA = **150 Ω**.
3. The small reverse current with no light: thermally generated minority carriers.
4. Microwave oscillators; very fast switches (also amplifiers in the negative-resistance region).
5. Doping about 1000 times normal: W ∝ √(1/N), so W shrinks to about 10 nm.

<!--/ANSWERS-->
