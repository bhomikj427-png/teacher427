# Unit 2 — Formula cheat sheet: the diode and its circuits

<div class="sub">One card per formula from v1.2 files 03a, 03b, 04, 05, 06 · each card: a question → the formula → every symbol defined → a figure → where it holds · answers at the end · every number recomputed in verify.py</div>

## Map

[[map:The junction (F21–F22) > The diode equation (F23–F24) > Resistance, capacitance (F25–F26) > DC circuits (F27–F28) > Rectifiers (F29–F31) > Wave shaping (F32–F35) > Zener, LED (F36–F37)]]

**Carried over from Unit 1.** V_{T} = kT/q ≈ 26 mV at 300 K. n_{i}, N_{A}, N_{D}: Unit 1 F1. **Diode model used in circuits (unless told "ideal"):** ON = a 0.7 V drop (Si; Ge 0.3 V); OFF = open circuit.

---

## Part 1 · The pn junction

### F21 · Built-in voltage: V_{bi} = V_{T} ln(N_{A}N_{D}/n_{i}^{2})

:::q <span class="tag">03a step 8</span>
N_{A} = 10^{17}, N_{D} = 10^{16} cm^{−3}, n_{i} = 10^{10} cm^{−3}, V_{T} = 25.9 mV. Find V_{bi}.
:::

$$V_{bi} = V_{T} ln\frac{N_{A}N_{D}}{n_{i}^{2}}$$

:::note Terms
**pn junction:** p-type and n-type Si in contact. **Depletion region:** the strip at the contact emptied of carriers; holes and electrons diffused across and recombined, leaving fixed ions (− on the p side, + on the n side). **V_{bi} (built-in voltage):** the voltage across that strip in equilibrium, where its field's drift cancels diffusion (Unit 1 F14). Si: 0.6–0.9 V. A voltmeter cannot read it.
:::

[[fig:junction|Fixed ions in the depletion region; built-in field from n to p.|w=72]]

### F22 · Depletion width: W ∝ √(V_{bi} − V_{a})

:::q <span class="tag">Deck slides 77–78</span>
(a) Abrupt Si junction, V_{bi} = 0.85 V. Find W_{1}/W_{0} for V_{a} = 0.6 V forward; repeat for 2 V reverse. (b) For F21's junction (V_{bi} = 0.775 V, ε = 1.04 × 10^{−12} F/cm) find W at zero bias and the fraction on the n side.
:::

$$W = √[\frac{2ε}{q}(\frac{1}{N_{A}} + \frac{1}{N_{D}})(V_{bi} − V_{a})]      N_{A}x_{p} = N_{D}x_{n}$$

:::note Terms
**W:** total depletion width = x_{p} (into the p side) + x_{n} (into the n side). **V_{a}:** applied voltage, **+ for forward** bias (p side positive), − for reverse. **Abrupt junction:** doping changes from p to n in one step. **N_{A}x_{p} = N_{D}x_{n}:** equal and opposite charge on both sides, so the region reaches further into the **lightly doped** side.
:::

- Forward bias → barrier V_{bi} − V_{a} lower → W narrower → current flows. Reverse → W wider → only tiny minority current.

---

## Part 2 · The diode equation

### F23 · Shockley equation: I_{D} = I_{s}(e^{V_{D}/ηV_{T}} − 1)

:::q <span class="tag">03b step 3</span>
I_{s} = 1 pA, η = 1, 300 K. Find I_{D} at 0.6 V. What does 60 mV more do?
:::

$$I_{D} = I_{s}(e^{V_{D}/ηV_{T}} − 1)      V_{T} = kT/q = T/11 600 ≈ 26 mV$$

:::note Terms
**I_{D}, V_{D}:** diode current and voltage (anode → cathode). **I_{s} (reverse saturation current):** the tiny current of minority carriers, nA in Si, μA in Ge; ∝ n_{i}^{2}. **η (ideality factor):** 1 to 2; take 1 unless told. **Knee voltage:** where current becomes large: Si 0.7 V, Ge 0.3 V, GaAs 1.2 V.
:::

[[fig:diode_iv|Forward knee near 0.7 V, flat −I_{s} in reverse, breakdown far left.|w=58]]

- Forward: I_{D} ≈ I_{s}e^{V_{D}/ηV_{T}}; **every 60 mV multiplies the current by 10**. Reverse: I_{D} ≈ −I_{s}.

### F24 · Temperature: I_{s} doubles every 10 °C

:::q <span class="tag">03b step 6</span>
I_{s} = 10 nA at 25 °C. Find I_{s} at 55 °C.
:::

$$I_{s2} = I_{s1} × 2^{(T_{2} − T_{1})/10}      at fixed I_{D}: V_{D} falls ≈ 2 mV/°C$$

:::note Terms
I_{s} ∝ n_{i}^{2}, and n_{i} rises steeply with T (Unit 1 F2). T in °C; only the difference matters.
:::

---

## Part 3 · Resistance and capacitance

### F25 · Static and dynamic resistance: r_{d} = ηV_{T}/I_{D}

:::q <span class="tag">03b steps 7–8</span>
A diode carries 2 mA at 0.7 V (η = 1). Find its static and dynamic resistance.
:::

$$R_{D} = \frac{V_{D}}{I_{D}}      r_{d} = \frac{ηV_{T}}{I_{D}} ≈ \frac{26 mV}{I_{D}}      r_{av} = \frac{ΔV_{D}}{ΔI_{D}}$$

:::note Terms
**R_{D} (static, DC):** voltage ÷ current at the operating point. **r_{d} (dynamic, AC):** 1/slope of the curve there; what a small AC signal sees. **r_{av}:** the same for a large swing between two points. mV ÷ mA = Ω.
:::

[[fig:diode_models|Ideal, simplified (0.7 V) and piecewise-linear (0.7 V + r_{av}) models.|w=70]]

### F26 · Capacitances: C_{T} = εA/W, C_{D} = τI_{D}/ηV_{T}

:::q <span class="tag">03b steps 10–11</span>
(a) V_{bi} = 0.85 V. By what factor does C_{T} change from 0 V to 5 V reverse? (b) τ = 1 μs, I_{D} = 1 mA, η = 1, V_{T} = 26 mV. Find C_{D}.
:::

$$C_{T} = \frac{εA}{W}   (reverse)      C_{D} = \frac{τI_{D}}{ηV_{T}}   (forward)      t_{rr} = t_{s} + t_{t}$$

:::note Terms
**C_{T} (transition):** the depletion region acts as a capacitor dielectric of thickness W; more reverse V → wider W → smaller C_{T} (a **varactor** uses this). **C_{D} (diffusion):** minority charge stored while forward biased; much larger. **A:** junction area. **τ:** minority lifetime (Unit 1 F17). **t_{rr} (reverse recovery time):** storage time t_{s} (stored charge pulled out) + transition time t_{t} (current dies away).
:::

---

## Part 4 · Diode DC circuits

### F27 · Load line: I_{D} = (E − V_{D})/R

:::q <span class="tag">Deck L08 slide 4</span>
E = 10 V, R = 0.5 kΩ, Si diode. Find the load line's ends, then V_{DQ}, I_{DQ}, V_{R} from the curve.
:::

$$E = V_{D} + I_{D}R   ⇒   I_{D} = \frac{E − V_{D}}{R}      ends: (0, E/R) and (E, 0)$$

:::note Terms
**Load line:** every (V_{D}, I_{D}) pair the resistor and source allow (KVL). **Q-point (quiescent):** where the load line crosses the diode curve; the circuit's actual operating point.
:::

<div class="two">

[[fig:ckt_load_line|The circuit.]]

[[fig:load_line|Load line on the diode curve.]]

</div>

### F28 · Three-step method: I = (ΣE − ΣV_{D})/ΣR

:::q <span class="tag">Deck L08 slide 14</span>
E_{1} = 10 V, Si diode, R_{1} = 4.7 kΩ, R_{2} = 2.2 kΩ, E_{2} = 5 V, as drawn. Find I, V_{1}, V_{2}, V_{o}.
:::

$$1. state test   2. ON → 0.7 V, OFF → open   3. KVL: I = \frac{ΣE − ΣV_{D}}{ΣR}$$

:::note Terms
**State test:** remove the diode; if the voltage across the gap pushes along the arrow by more than 0.7 V, it is ON. **Series diodes:** drops add. **Parallel diodes:** share one 0.7 V drop; identical ones split the current.
:::

[[fig:ckt_two_source|Deck L08 slide 14.|w=55]]

---

## Part 5 · Rectifiers

### F29 · Half-wave: V_{dc} = V_{m}/π

:::q <span class="tag">Deck L09 slide 9</span>
20 V peak sine, diode pointing toward the source, R = 2 kΩ. Sketch v_{o}; find V_{dc} ideal and Si; PIV.
:::

$$V_{dc} = \frac{V_{m}}{π} = 0.318V_{m}      Si: 0.318(V_{m} − 0.7)      V_{rms} = \frac{V_{m}}{2}      PIV = V_{m}$$

:::note Terms
**Rectifier:** turns AC into one-direction voltage. **V_{m}:** peak input; V_{m} = √2 × (rms input). **V_{dc}:** the average output, what a DC meter reads. **V_{rms}:** the heating value of the output. **PIV (peak inverse voltage):** the largest reverse voltage the diode must block.
:::

<div class="two">

[[fig:ckt_hw|Half-wave rectifier.]]

[[fig:rect_waves|Input; half-wave and full-wave outputs.]]

</div>

### F30 · Full-wave: V_{dc} = 2V_{m}/π

:::q <span class="tag">04 step 4</span>
A bridge rectifier with Si diodes is fed 12 V rms. Find V_{m}, V_{dc}, PIV per diode.
:::

$$V_{dc} = \frac{2V_{m}}{π} = 0.636V_{m}      bridge Si: 0.636(V_{m} − 1.4)      PIV: bridge V_{m}, centre-tapped 2V_{m}$$

:::note Terms
**Bridge:** 4 diodes, two conduct each half (so two drops, 1.4 V). **Centre-tapped:** 2 diodes, transformer with a middle tap; V_{m} is tap-to-end; the OFF diode sees 2V_{m}. Output V_{rms} = V_{m}/√2.
:::

<div class="two">

[[fig:bridge_fig|Bridge.]]

[[fig:ckt_ct|Centre-tapped.]]

</div>

### F31 · Ripple factor and efficiency

:::q <span class="tag">04 Check 3, Self-test 5</span>
Derive r = 1.21 (half-wave) and 0.482 (full-wave), and η = 40.6 % and 81.2 %.
:::

$$r = √[(\frac{V_{rms}}{V_{dc}})^{2} − 1]      η = (\frac{V_{dc}}{V_{rms}})^{2}   (ideal diodes)$$

:::note Terms
**Ripple factor r:** the AC left on the output ÷ its DC; smaller = smoother. **Efficiency η:** DC power to the load ÷ total power delivered. **Ripple frequency:** f for half-wave, 2f for full-wave (two pulses per cycle).
:::

| | Half-wave | Centre-tapped | Bridge |
|---|---|---|---|
| V_{dc} | 0.318V_{m} | 0.636V_{m} | 0.636V_{m} |
| V_{rms} | V_{m}/2 | V_{m}/√2 | V_{m}/√2 |
| PIV | V_{m} | 2V_{m} | V_{m} |
| r | 1.21 | 0.482 | 0.482 |
| η max | 40.6 % | 81.2 % | 81.2 % |

---

## Part 6 · Wave shaping

### F32 · Series clipper: transition at KVL with i_{d} = 0, v_{d} = 0

:::q <span class="tag">Deck L10 slide 3</span>
5 V battery, ideal diode, R in series; 20 V peak sine. Find the transition voltage and v_{o}.
:::

$$transition: KVL with v_{d} = 0, i_{d} = 0      ON: v_{o} = v_{i} + V_{B}      OFF: v_{o} = 0$$

:::note Terms
**Clipper:** cuts off part of a wave, passes the rest. **Transition voltage:** the v_{i} at which the diode switches. **V_{B}:** the battery, signed as it adds around the loop. **Series:** output only while the diode is ON.
:::

[[fig:clip_series|Series clipper and output.|w=66]]

### F33 · Parallel clipper: output pinned while ON

:::q <span class="tag">Deck L10 slides 6–7</span>
16 V peak triangle; diode across the output, anode on a 4 V battery. Find v_{o}, ideal and Si.
:::

$$OFF: v_{o} = v_{i}      ON: v_{o} = V_{B} (ideal),  V_{B} − 0.7 (Si, this direction)$$

:::note Terms
**Parallel:** diode across the output; output **follows** the input while the diode is OFF, and is pinned to the battery level while ON.
:::

[[fig:clip_parallel|Parallel clipper and output.|w=66]]

### F34 · Clamper: v_{o} = v_{i} + V_{C}

:::q <span class="tag">Deck L10 slide 13</span>
Square wave +10/−20 V, 1 kHz; C = 0.1 μF, R = 100 kΩ, ideal diode with a 5 V battery. Find v_{o}.
:::

$$ON half: KVL gives V_{C}      OFF half: v_{o} = v_{i} + V_{C}      need 5RC ≫ T/2      output swing = input swing$$

:::note Terms
**Clamper:** shifts a whole wave up or down without changing its shape. **V_{C}:** the voltage C charges to in the ON half; it then acts as a battery. **τ = RC:** time constant; C needs ≈ 5τ to discharge. **T/2:** half the period.
:::

[[fig:clamper|Clamper, deck L10 slide 13.|w=55]]

### F35 · Voltage multiplier: V_{out} = nV_{m}

:::q <span class="tag">05 Check 4</span>
Ideal DC output of a quadrupler fed 10 V peak?
:::

$$doubler 2V_{m}, tripler 3V_{m}, quadrupler 4V_{m}      PIV per diode = 2V_{m}$$

:::note Terms
**Doubler:** a clamper (shifts the wave up by V_{m}) followed by a peak detector (holds the top, 2V_{m}). For high voltage, low current loads.
:::

[[fig:doubler|Half-wave doubler.|w=55]]

---

## Part 7 · Zener and LED

### F36 · Zener regulator

:::q <span class="tag">05 step 5</span>
V_{i} = 16 V, R = 1 kΩ, V_{Z} = 10 V. Find V_{L}, I_{L}, I_{Z}, P_{Z} for (a) R_{L} = 1.2 kΩ, (b) R_{L} = 3 kΩ. Smallest R_{L} that keeps regulation?
:::

$$test: V = \frac{V_{i}R_{L}}{R + R_{L}} ≥ V_{Z}?      ON: I_{R} = \frac{V_{i} − V_{Z}}{R},  I_{L} = \frac{V_{Z}}{R_{L}},  I_{Z} = I_{R} − I_{L},  P_{Z} = V_{Z}I_{Z}      R_{L,min} = \frac{RV_{Z}}{V_{i} − V_{Z}}$$

:::note Terms
**Breakdown:** a sharp rise of reverse current at one reverse voltage; safe if current is limited. **V_{Z}:** the Zener's breakdown voltage; it holds this voltage over a wide current range. **R:** series resistor that drops the extra voltage. **R_{L}:** load. **P_{ZM}:** maximum allowed power; need P_{Z} &lt; P_{ZM}. **Zener vs avalanche:** below ≈ 5 V, heavy doping, negative temperature coefficient; above ≈ 6 V, light doping, positive.
:::

<div class="two">

[[fig:zener_iv|Zener curve: vertical at V_{Z}.]]

[[fig:zener_reg|Zener regulator.]]

</div>

### F37 · LED colour: λ = 1.24/E_{g}

:::q <span class="tag">06 Check 1, Self-test 2</span>
(a) A red LED material has E_{g} = 1.9 eV. Find λ. (b) A 2 V LED should carry 20 mA from 5 V. Series R?
:::

$$λ(μm) = \frac{1.24}{E_{g}(eV)}      R = \frac{V_{S} − V_{LED}}{I_{LED}}$$

:::note Terms
**LED:** forward-biased junction where electron–hole recombination gives off light; needs a **direct gap** (GaAs family, not Si, Unit 1 F16). **λ:** wavelength in μm. **E_{g}:** gap in eV; bigger gap → bluer light. **V_{LED}:** 1.8–3.3 V. The series R limits current, because the I–V is steep.
:::

[[fig:special_symbols|Symbols: LED, photodiode, tunnel diode.|w=55]]

<!--ANSWERS-->

## Answers

**F21.** 0.0259 × ln(10^{33}/10^{20}) = 0.0259 × 29.93 = **0.775 V**.

**F22.** (a) √(0.25/0.85) = **0.54** (narrower); √(2.85/0.85) = **1.83** (wider). (b) W = √(2 × 1.04 × 10^{−12}/1.6 × 10^{−19} × 1.1 × 10^{−16} × 0.775) = **0.333 μm**; x_{n}/W = (1/N_{D})/(1/N_{A} + 1/N_{D}) = **91 %** on the lightly doped n side.

**F23.** 10^{−12} × e^{23.2} ≈ **11.5 mA** (≈ 12 mA). +60 mV: × e^{2.32} ≈ **× 10**, so ≈ 115 mA.

**F24.** Three doublings: **80 nA**.

**F25.** R_{D} = 0.7/2 mA = **350 Ω**. r_{d} = 26/2 = **13 Ω**.

**F26.** (a) W × √(5.85/0.85) = × 2.62, so C_{T} **× 0.38**. (b) C_{D} = 10^{−6} × 10^{−3}/0.026 = **38.5 nF**.

**F27.** Ends **20 mA** and **10 V**. Crossing: **V_{DQ} ≈ 0.78 V, I_{DQ} ≈ 18.5 mA**. **V_{R} = 9.25 V** (slide 5 prints 18.5 V: wrong R).

**F28.** Sources add along the arrow (15 V): ON. I = (15 − 0.7)/6.9 k = **2.07 mA**; V_{1} = **9.74 V**; V_{2} = **4.56 V**; V_{o} = V_{2} − E_{2} = **−0.44 V**.

**F29.** Conducts on the **negative** half: output = negative half-cycles. Ideal **−6.36 V**; Si **−6.14 V**; PIV **20 V**.

**F30.** V_{m} = 12√2 = **17.0 V**; V_{dc} = 0.636 × 15.6 = **9.92 V**; PIV ≈ **17 V**.

**F31.** HW: V_{rms}/V_{dc} = (V_{m}/2)/(V_{m}/π) = π/2; r = √(2.467 − 1) = **1.21**; η = (2/π)^{2} = **40.6 %**. FW: (V_{m}/√2)/(2V_{m}/π) = π/(2√2) = 1.111; r = √(1.234 − 1) = **0.482**; η = (2√2/π)^{2} = **81.1 %** (books: 81.2 %).

**F32.** v_{i} + 5 = 0: transition **−5 V**. Above it v_{o} = v_{i} + 5 (peak **25 V**); below it v_{o} = 0.

**F33.** Below 4 V the diode is ON: **v_{o} = 4 V** (Si **3.3 V**). Above 4 V: **v_{o} = v_{i}**.

**F34.** ON half (−20 V): v_{o} = 5 V, −20 + V_{C} − 5 = 0 → **V_{C} = 25 V**. OFF half: 10 + 25 = **35 V**. Output square **5 V to 35 V** (swing 30 ✓). 5τ = 50 ms = 100 × T/2 ✓.

**F35.** **40 V**.

**F36.** (a) V = 16 × 1.2/2.2 = 8.73 V &lt; 10: **OFF**; V_{L} = **8.73 V**, I_{Z} = 0. (b) V = 12 V ≥ 10: ON. **V_{L} = 10 V**, I_{R} = 6 mA, **I_{L} = 3.33 mA**, **I_{Z} = 2.67 mA**, **P_{Z} = 26.7 mW**. R_{L,min} = 1 k × 10/6 = **1.67 kΩ**.

**F37.** (a) 1.24/1.9 = **0.653 μm** (653 nm, red). (b) (5 − 2)/20 mA = **150 Ω**.

<!--/ANSWERS-->
