# 05 — Clippers, clampers, Zener, Schottky

<div class="sub">Deck L10 (clippers slides 3–7, clampers slide 13) · syllabus Unit 2 · needs 04 (the three-step method)</div>

## Map

[[map:1 Series clipper > 2 Parallel clipper > 3 Clamper > 4 Voltage multipliers > 5 Breakdown, Zener regulator > 6 Schottky diode|here=1]]

04 used the diode to pass one half of a wave. Here a battery shifts the level at which it switches (clippers), a capacitor shifts the whole wave (clampers), and breakdown, which 03b treated as a limit, becomes useful (Zener).

## The questions this file answers

- <span class="tag">Deck L10 slide 3</span> Output of a series clipper: 5 V battery, ideal diode, R; 20 V peak sine.
- <span class="tag">Deck L10 slide 6</span> Parallel clipper with a 4 V battery; triangular input of 16 V peak.
- <span class="tag">Deck L10 slide 13</span> Clamper: square wave +10/−20 V, C = 0.1 μF, R = 100 kΩ, 5 V battery. Find v_{o}.
- <span class="tag">practice</span> Zener regulator: V_{i} = 16 V, R = 1 kΩ, V_{Z} = 10 V, R_{L} = 1.2 kΩ and 3 kΩ.

---

## Build

### 1 · The series clipper

:::q <span class="tag">Deck L10 slide 3</span>
Determine the output waveform. (Series clipper: a 5 V battery, then an ideal diode, then R. Input: 20 V peak sine.)
:::

:::guess Guess first
Sketch v_{o} for one cycle.
:::

:::note Terms
**Clipper (limiter):** removes part of a waveform and passes the rest unchanged. **Transition voltage:** the input value at which the diode changes state.
:::

[[fig:clip_series|Series clipper and its output.|w=70]]

The diode is in series with the output, so there is output only while it conducts. The battery shifts the switching level.

1. **Transition voltage.** Put the ideal diode at the edge (i_{d} = 0, v_{d} = 0) and write KVL: v_{i} + 5 = 0, so it switches at **v_{i} = −5 V**.
2. **ON** (v_{i} &gt; −5 V): v_{o} = v_{i} + 5.
3. **OFF** (v_{i} &lt; −5 V): no current, v_{o} = 0.

**Answer.** The output is the input lifted by 5 V while v_{i} &gt; −5 V, and zero otherwise. Peak **25 V**.

:::check Check 1
Reverse the battery. Find the new transition voltage and the peak of v_{o}.
:::

### 2 · The parallel clipper

:::q <span class="tag">Deck L10 slide 6</span>
Triangular input of 16 V peak; ideal diode with its anode on a 4 V battery, across the output. Find v_{o}. Repeat with a silicon diode (slide 7).
:::

:::guess Guess first
While the diode is off, what does the output do?
:::

[[fig:clip_parallel|Parallel clipper and its output.|w=70]]

The diode is across the output. **OFF:** the output follows the input. **ON:** it pins the output to the battery level. Two branches facing opposite ways clip both peaks, which squares up a sine.

**Answer.** The diode conducts whenever v_{i} &lt; 4 V and holds **v_{o} = 4 V**; above 4 V it is off and **v_{o} = v_{i}**. With Si, the pinned level is 4 − 0.7 = **3.3 V**.

:::check Check 2
(a) Turn the diode around (cathode on the battery). Describe v_{o}. (b) In which clipper type does the output follow the input while the diode is off?
:::

### 3 · The clamper

:::q <span class="tag">Deck L10 slide 13</span>
Determine v_{o}. (Square-wave input +10 V and −20 V, f = 1000 Hz. C = 0.1 μF, R = 100 kΩ, ideal diode in series with a 5 V battery.)
:::

:::guess Guess first
The input swings 30 V in total. What total swing will the output have?
:::

:::note Terms
**Clamper:** C, a diode and R that shift a whole waveform up or down without changing its shape. **Time constant τ = RC:** a capacitor needs about 5τ to charge or discharge.
:::

[[fig:clamper|Clamper, deck L10 slide 13.|w=60]]

On one half-cycle the diode conducts and charges C quickly. On the other it is off, and C can discharge only through the large R. If 5τ ≫ half-period, C holds its voltage like a battery in series with the input.

1. Start with the half-cycle that turns the diode **ON**: v_{i} = −20 V. The output is pinned to the battery: v_{o} = 5 V.
2. KVL in that state: −20 + V_{C} − 5 = 0, so **V_{C} = 25 V**.
3. Other half, diode OFF: v_{o} = v_{i} + V_{C} = 10 + 25 = 35 V.
4. Check the swing: 35 − 5 = 30 V ✓.

**Answer.** v_{o} is a square wave between **5 V and 35 V**. τ = 100 kΩ × 0.1 μF = 10 ms, 5τ = 50 ms: 100 times the half-period of 0.5 ms ✓.

:::check Check 3
(a) Remove the 5 V battery (diode straight to ground). Find the two output levels. (b) What goes wrong if R is made 100 Ω?
:::

### 4 · Voltage multipliers

:::guess Predict
A clamper shifts a wave up by V_{m}. If a peak detector then follows it, what DC voltage does it hold?
:::

[[fig:doubler|Half-wave voltage doubler.|w=60]]

**Half-wave doubler.** Positive half: D_{1} conducts and charges C_{1} to V_{m}. Negative half: the source and C_{1} add in series, D_{2} conducts, and C_{2} charges to **2V_{m}**. Each diode must stand PIV = 2V_{m}. More sections give a tripler (3V_{m}) and a quadrupler (4V_{m}), for high-voltage, low-current loads.

**Answer.** 2V_{m}: the clamper output peaks at 2V_{m}, and the peak detector holds it.

:::check Check 4
What DC voltage does a quadrupler give from a 10 V peak input, ideally?
:::

### 5 · Breakdown and the Zener regulator

:::q <span class="tag">practice</span>
In the regulator, V_{i} = 16 V, R = 1 kΩ, V_{Z} = 10 V. Find V_{L}, I_{L}, I_{Z} and P_{Z} for (a) R_{L} = 1.2 kΩ and (b) R_{L} = 3 kΩ.
:::

:::guess Guess first
In which case is the Zener actually regulating?
:::

<div class="two">

[[fig:zener_iv|Zener curve: nearly vertical at V_{Z}.]]

[[fig:zener_reg|Zener regulator.]]

</div>

Breakdown is the sharp rise of reverse current at one reverse voltage. It does not destroy the diode if the current is limited.

| | Zener breakdown | Avalanche breakdown |
|---|---|---|
| Doping | heavy both sides | light |
| Depletion region | very thin, huge field | wide |
| Mechanism | field pulls electrons out of bonds (tunnelling) | fast carriers knock out more (multiplication) |
| Voltage | below about 5 V | above about 6 V |
| Temperature coefficient | negative (V falls) | positive (V rises) |

A **Zener diode** is built to work in breakdown; its voltage stays at V_{Z} over a wide current range, so it is a voltage reference.

1. **Test the state.** Remove the Zener: V = V_{i}R_{L}/(R + R_{L}). If V ≥ V_{Z} it is ON; if not, OFF (open).
2. **If ON:** V_{L} = V_{Z}; I_{R} = (V_{i} − V_{Z})/R; I_{L} = V_{Z}/R_{L}; I_{Z} = I_{R} − I_{L}; P_{Z} = V_{Z}I_{Z} &lt; P_{ZM}.

**Answer.** (a) V = 16 × 1.2/2.2 = 8.73 V &lt; 10 V: **OFF**, V_{L} = **8.73 V**, I_{Z} = 0, P_{Z} = 0. No regulation. (b) V = 12 V ≥ 10: **ON**. V_{L} = **10 V**, I_{R} = 6 mA, I_{L} = **3.33 mA**, I_{Z} = **2.67 mA**, P_{Z} = **26.7 mW**. Smallest load that keeps it on: R_{L,min} = RV_{Z}/(V_{i} − V_{Z}) = 1.67 kΩ.

:::check Check 5
(a) A 4.7 V Zener and a 12 V Zener heat up. Whose voltage falls, and why? (b) V_{i} rises to 20 V with R_{L} = 3 kΩ. Find I_{Z}.
:::

### 6 · The Schottky diode

:::guess Predict
04's rectifiers are limited at high frequency by the stored charge of 03b (reverse recovery, step 12). What junction would store no minority charge?
:::

A **Schottky diode** is a metal–n-type silicon junction. Only majority carriers (electrons) take part, so there is no stored minority charge and almost no reverse recovery time: it switches very fast. Forward drop 0.2–0.4 V. The price: larger reverse leakage, lower breakdown voltage. Used in high-frequency rectifiers and fast logic.

**Answer.** A metal–semiconductor junction, where only majority carriers flow.

:::check Check 6
Give two advantages and two disadvantages of a Schottky diode against a pn diode.
:::

---

## Exam form

**Clippers.** Transition voltage by KVL at the edge (i_{d} = 0, v_{d} = 0); ON and OFF expressions; sketch input and output aligned. Series: output only while ON. Parallel: output follows input while OFF.

**Clampers.** Start with the ON half → V_{C} by KVL → other half v_{o} = v_{i} + V_{C} → check swing → check 5τ ≫ T/2.

**Multipliers.** Doubler operation, 2V_{m}, PIV 2V_{m}.

**Zener.** Zener vs avalanche table; regulator procedure; R_{L,min}; P_{Z}.

**Schottky.** Metal–n junction, majority carriers only, fast, 0.3 V drop.

## Traps

- Not checking the Zener is ON before writing V_{L} = V_{Z}.
- Clamper: starting with the half-cycle where the diode is OFF.
- Forgetting that the clamper output swing equals the input swing.
- Mixing up which clipper follows the input when the diode is off.
- Saying Zener breakdown has a positive temperature coefficient.

## Self-test

1. Compare Zener and avalanche breakdown in four points.
2. Zener regulator: V_{i} = 20 V, R = 500 Ω, V_{Z} = 8 V, R_{L} = 1 kΩ. Find V_{L}, I_{L}, I_{Z} and P_{Z}.
3. For Q2, find R_{L,min}.
4. A ±10 V square wave drives a clamper whose diode (to ground, no battery) conducts on the negative half. Find the output levels.
5. A voltage tripler is fed a 15 V peak sine. Ideal DC output?
6. Why must a clamper's RC be large compared with the period?

<!--ANSWERS-->

## Answers

**Check 1.** KVL at the edge: v_{i} − 5 = 0, transition at **+5 V**. ON for v_{i} &gt; 5 V with v_{o} = v_{i} − 5; peak **15 V**.

**Check 2.** (a) It conducts when v_{i} &gt; 4 V and pins v_{o} = 4 V; below 4 V, v_{o} = v_{i}. The top is clipped at 4 V. (b) The parallel clipper.

**Check 3.** (a) ON at −20 V pins v_{o} = 0, V_{C} = 20 V; other half 10 + 20 = 30 V. Levels **0 V and 30 V**. (b) τ = 10 μs ≪ 0.5 ms: C discharges within each half-cycle, so the level droops and the shape distorts.

**Check 4.** **40 V**.

**Check 5.** (a) The **4.7 V** one: below about 5 V the mechanism is Zener breakdown, negative coefficient. The 12 V one is avalanche; its voltage rises. (b) I_{R} = 10 mA, I_{L} = 3.33 mA, **I_{Z} = 6.67 mA**.

**Check 6.** For: very fast switching (no stored charge), low forward drop. Against: higher reverse leakage, lower breakdown voltage.

**Self-test.**

1. See step 5's table.
2. Test: 20 × 1/1.5 = 13.3 V ≥ 8: ON. **V_{L} = 8 V**, I_{R} = 12/0.5 k = 24 mA, **I_{L} = 8 mA**, **I_{Z} = 16 mA**, **P_{Z} = 128 mW**.
3. R_{L,min} = 500 × 8/12 = **333 Ω**.
4. Negative half: v_{o} = 0, V_{C} = 10 V. Positive half: 10 + 10 = 20 V. Levels **0 and 20 V**.
5. 3 × 15 = **45 V**.
6. C must hold its charge through the OFF half-cycle; if 5τ is not much longer than T/2, it discharges through R and the output droops.

<!--/ANSWERS-->
