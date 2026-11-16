# 03b — The diode under bias: current, resistance, capacitance

<div class="sub">Unit 1–2 deck, slides 75 and 79–100 · syllabus Unit 2 (diode equation, V–I characteristics, temperature dependence, static and dynamic resistance, equivalent circuits, transition and diffusion capacitance, reverse recovery) · needs 03a (barrier V_{bi} − V_{a}, depletion width W), 02b (minority carriers, lifetime τ, diffusion length L) · deck slides give definitions, not numbers: the openers are practice problems and Predict prompts</div>

## Map

[[map:1 The I–V curve > 2 Why exponential > 3 Diode equation > 4 Forward, reverse > 5 Where I_s comes from > 6 Temperature > 7 Static R_D > 8 Dynamic r_d > 9 Models > 10 C_T > 11 C_D > 12 Recovery|here=1]]

03a ended with a battery across the junction: forward bias **lowers** the barrier to V_{bi} − V_{a}, reverse bias **raises** it. This file turns that barrier height into a current, then asks how the diode behaves in a circuit: as a resistance (steps 7–9), as a capacitor (10–11), and when switched off (12). 04 and 05 use the results in circuits.

| Symbol | Meaning in this file | Typical value |
|---|---|---|
| V_{D} | voltage across the diode, anode minus cathode (same as 03a's V_{a}) | 0.6–0.7 V forward |
| I_{D} | current through the diode, anode to cathode | mA forward |
| I_{s} | reverse saturation current (step 3, step 5) | 1 pA in this file |
| V_{T} | thermal voltage kT/q (02b step 6) | 25.9 mV at 300 K |
| η | ideality factor (step 3) | 1 here unless told |

## The questions this file answers

- <span class="tag">practice · deck slides 79–83</span> A diode has I_{s} = 1 pA and η = 1 at 300 K. Find its current at V_{D} = 0.6 V. What does 60 mV more do?
- <span class="tag">practice · deck slides 80–81</span> I_{s} = 10 nA at 25 °C: find it at 55 °C.
- <span class="tag">practice · deck slides 84–86</span> Static and dynamic resistance at a given operating point.
- <span class="tag">practice · deck slides 87–89</span> A 5 V source, 1 kΩ and a Si diode: the current with each diode model.
- <span class="tag">practice · deck slides 91–98</span> Transition capacitance against reverse voltage; diffusion capacitance at a forward current; reverse recovery time.

---

## Build

### 1 · What the I–V curve looks like

:::guess Predict
A diode's voltage is swept from −5 V to +0.75 V and its current is plotted. Sketch the curve you expect from 03a step 12 (forward: small barrier; reverse: big barrier).
:::

:::note Terms
**I–V characteristic:** the graph of current against voltage for a device. **Knee (cut-in) voltage V_{γ}:** the forward voltage where the current becomes noticeable: about **0.7 V for Si**, 0.3 V for Ge, 1.2 V for GaAs.
:::

[[fig:iv_lin_log|What these graphs plot: for each diode voltage V_{D} (horizontal) the diode current I_{D} (vertical), for I_{s} = 1 pA. A point = "at this voltage this much current flows". ① On a linear scale, like deck slide 75. ② The same curve with the size of I_{D} on a log scale, where an exponential is a straight line.|w=96]]

- **Reverse** (V_{D} < 0): the current is so small that on a mA scale it looks like zero. The log plot shows it: a constant **1 pA** (deck slide 75: "the diode blocks conduction").
- **Forward:** almost nothing until about 0.5 V, then a near-vertical rise. Above about **0.8 V** a small Si diode overheats (deck slide 75).
- The log plot shows the forward side is a **straight line**: the current is an **exponential** of the voltage. Steps 2–3 explain why.

**Answer to the Predict.** Flat near zero on the reverse side, flat near zero up to about 0.5 V forward, then a steep wall. That one-way shape is **rectification**.

:::check Check 1
(a) What is the knee voltage of a Si diode? Of a Ge diode? (b) On which plot can you see the reverse current, and why? (c) What shape is the forward curve on a log scale, and what does that shape mean?
:::

### 2 · Why the current grows exponentially

Combine two things: 03a's barrier height, and 01b's Boltzmann count (the number of electrons above an energy falls by e for each kT higher).

:::guess Predict
Forward bias lowers the barrier by 0.06 V. That is a little over 2 kT. By roughly what factor does the number of electrons able to climb it change: 1.1, 2 or 10?
:::

:::note Terms
**Injection:** majority carriers climbing the barrier and arriving on the other side as minority carriers. **Barrier height:** the energy step q(V_{bi} − V_{a}) of 03a step 12.
:::

[[fig:barrier_bias|What these diagrams plot: electron energy E_{C} (vertical) against position (horizontal), p side left, n side right, for the running junction of 03a (V_{bi} = 0.775 V) at three biases. Blue: the n-side electrons, fewer at higher energy (01b step 6). Only those above the dotted line can reach the p side.|w=96]]

- Electrons on the n side have a spread of energies. The share above the barrier is **e^{−(barrier)/kT}** (Boltzmann, 01b step 6).
- The barrier is q(V_{bi} − V_{a}), so the share is e^{−(V_{bi} − V_{a})/V_{T}} = e^{−V_{bi}/V_{T}} × **e^{V_{a}/V_{T}}**. Every 25.9 mV of forward bias multiplies the crossing by e = 2.72.
- **Two currents cross the junction:**
  - **Diffusion** (majority carriers climbing the barrier): ∝ e^{V_{a}/V_{T}}. Changes hugely with V_{a}.
  - **Drift** (minority carriers sliding down it, step 5): a fixed small current, call it I_{s}. Does not depend on V_{a}.
- At V_{a} = 0 they cancel (03a step 6), so the diffusion current at V_{a} = 0 is also I_{s}. With bias it is I_{s}e^{V_{a}/V_{T}}. Net:

$$I_{D} = I_{s}e^{V_{D}/V_{T}} − I_{s}$$

**Answer to the Predict.** e^{0.06/0.0259} = e^{2.32} ≈ **10**. Lowering a barrier by a small voltage changes the crossing by a big factor.

:::check Check 2
(a) Forward bias of 0.1 V: by what factor does the diffusion current grow over its zero-bias value? (b) Why does the drift current not change with V_{a}? (c) At V_{a} = 0, what are the two currents and their sum?
:::

### 3 · The diode equation, term by term

:::q <span class="tag">practice · deck slides 79–83</span>
A diode has I_{s} = 1 pA and η = 1 at 300 K. Find its current at V_{D} = 0.6 V. What happens if V_{D} rises by 60 mV?
:::

:::guess Guess first
Microamps, milliamps or amps at 0.6 V?
:::

:::note Terms
**Reverse saturation current I_{s}:** the drift current of step 2; a property of the diode (step 5). nA or less for Si, μA for Ge (deck slide 79: "I_{s} is the reverse saturation current"). **Ideality factor η:** a number from 1 to 2 that stretches the exponential; 1 when all current is injection (step 2), up to 2 when much of it comes from recombination inside the depletion region. Deck slide 79: "assume η = 1 unless otherwise noted".
:::

[[fig:eqn_points|What this graph plots: for each V_{D} (horizontal, volts) the current I_{D} (vertical, mA) given by the diode equation with I_{s} = 1 pA. Solid: η = 1. Dashed: η = 2 with the same I_{s}. Dots: the values worked below.|w=72]]

Step 2's result, with the ideality factor (deck slides 79, 82):

$$I_{D} = I_{s}(e^{V_{D}/ηV_{T}} − 1)      V_{T} = \frac{kT}{q} = \frac{T}{11 600}$$

| Symbol | What it is | Unit | Typical value |
|---|---|---|---|
| I_{D} | diode current, anode → cathode | A | mA |
| I_{s} | reverse saturation current | A | 10^{−12} to 10^{−9} (Si) |
| V_{D} | anode − cathode voltage | V | 0.6–0.7 forward |
| η | ideality factor | none | 1 (2 if told) |
| V_{T} | thermal voltage; T in kelvin, k = 1.38 × 10^{−23} J/K | V | 25.9 mV at 300 K |

**Answer.** V_{D}/V_{T} = 0.6/0.0259 = 23.17; e^{23.17} = 1.15 × 10^{10}. I_{D} = 10^{−12} × 1.15 × 10^{10} = **11.5 mA** (the −1 is negligible). Another 60 mV multiplies it by e^{0.06/0.0259} = **10.1**: 0.66 V gives 116 mA.

With η = 2 the same diode carries only 0.107 μA at 0.6 V: η matters, so state the value you use.

:::note The deck's two rules for the ideality factor
Slide 79 says take η = 1 unless told. Slide 82 says "η = 1 for Ge and 2 for Si". Questions give η; when one does not, use η = 1 and write that down.
:::

:::check Check 3
(a) V_{T} at 100 °C? (b) Same diode (I_{s} = 1 pA, η = 1): current at 0.5 V? (c) What does η = 2 do to the curve?
:::

### 4 · The forward and reverse limits

:::guess Predict
At V_{D} = −0.1 V, is the "−1" in the bracket important or negligible? At +0.6 V?
:::

:::note Terms
**Decade:** a factor of 10 in current. **Saturation (reverse):** the current no longer changes with voltage.
:::

[[fig:decades|What these graphs plot: ① forward current (vertical, log scale) against V_{D}: a straight line, one decade per 59.6 mV; ② current divided by I_{s} (vertical) against V_{D} near zero and in reverse: it flattens at −1 (deck slide 83).|w=96]]

- **Forward, V_{D} ≫ V_{T}** (a few × 26 mV): e^{V_{D}/V_{T}} is huge, the −1 is lost (deck slide 83):

$$I_{D} ≈ I_{s}e^{V_{D}/ηV_{T}}$$

- Each **×10** in current needs **ηV_{T}ln10 = 59.6 mV** (η = 1) or 119 mV (η = 2). From 1 mA to 100 mA the voltage changes only 0.12 V; that is why one fixed drop (0.7 V) is a fair model (step 9).
- **Reverse, V_{D} ≲ −0.1 V:** e^{V_{D}/V_{T}} → 0, so (deck slide 83)

$$I_{D} ≈ −I_{s}$$

- In reverse the current is **flat**: more reverse voltage does not add current until breakdown (05).

**Answer to the Predict.** At −0.1 V: e^{−3.86} = 0.021, so I = −0.979 I_{s}: the −1 is the whole current. At +0.6 V: e^{23.2} = 1.15 × 10^{10}: the −1 is negligible.

:::check Check 4
(a) With I_{s} = 1 pA, what V_{D} gives 1 mA? 10 mA? (b) A diode at −10 V carries −2 nA. What current at −20 V (no breakdown)? (c) How many mV per decade if η = 2?
:::

### 5 · Where I_{s} comes from

:::guess Predict
I_{s} is built from minority carriers (step 2). Ge has n_{i} = 2.4 × 10^{13} cm^{−3}, Si 10^{10}. Which diode leaks more in reverse?
:::

:::note Terms
**Thermal generation:** heat breaking bonds to make electron–hole pairs (02b step 7). It is the only source of minority carriers in the dark.
:::

[[fig:is_origin|Reverse bias, drawn as in 03a step 6. A minority carrier made by heat near the depletion region is swept across by the field. The current is the rate at which heat makes them, not anything the battery controls.|w=82]]

- The minority counts are n_{i}^{2}/N_{A} (p side) and n_{i}^{2}/N_{D} (n side) (03a step 4). Each one that diffuses to the depletion edge is swept across.
- So **I_{s} ∝ n_{i}^{2}**: set by the material and the temperature, not by V_{D}. The full formula (stage-2 KB) is I_{s} = qAn_{i}^{2}[D_{p}/(L_{p}N_{D}) + D_{n}/(L_{n}N_{A})]; the exam needs only the proportionality.
- **Si vs Ge:** (2.4 × 10^{13}/10^{10})^{2} = 5.8 × 10^{6}: a Ge diode's ideal I_{s} is millions of times larger. Real Ge diodes leak μA, Si nA or less (deck slide 79).

**Answer to the Predict.** **Ge**, because its n_{i} is far larger and I_{s} ∝ n_{i}^{2}.

:::check Check 5
(a) Why does I_{s} not grow with reverse voltage? (b) Which doping term dominates I_{s} in a p⁺n diode, and why? (c) Why does I_{s} grow fast with temperature?
:::

### 6 · Temperature

:::q <span class="tag">practice · deck slides 80–81</span>
A Si diode has I_{s} = 10 nA at 25 °C. Find I_{s} at 55 °C. Its forward voltage at 25 °C is 0.70 V at 10 mA; estimate it at 75 °C at the same current.
:::

:::guess Guess first
Heat makes more carriers. Does the forward voltage at fixed current go up or down?
:::

[[fig:temp_iv|What this graph plots: forward current (vertical, mA) against V_{D} (horizontal, V) at 25 °C and 75 °C, drawn with the −2 mV/°C rule. At any fixed current the hot curve sits 0.1 V to the left.|w=72]]

- **I_{s} doubles every 10 °C** (deck slide 81):

$$I_{s2} = I_{s1} × 2^{(T_{2} − T_{1})/10}$$

- **Forward voltage at fixed current falls about 2 mV per °C** (Si). Heat lowers the cut-in voltage (deck slides 80–81).
- Ge diodes are **more** temperature-sensitive than Si or GaAs (deck slide 80).
- Both rules come from n_{i}(T) rising steeply (01a step 5) and I_{s} ∝ n_{i}^{2} (step 5).

**Answer.** 55 − 25 = 30 °C = three doublings: I_{s} = 10 × 2^{3} = **80 nA**. Forward: 0.70 − 0.002 × 50 = **0.60 V**.

:::check Check 6
(a) I_{s} = 1 pA at 25 °C: I_{s} at 125 °C? (b) A diode reads 0.65 V at 25 °C. Estimate at −15 °C, same current. (c) Why does a hot diode conduct at a lower voltage?
:::

### 7 · Static (DC) resistance

A diode is not a resistor: V/I changes along its curve. Two "resistances" are defined, one for DC and one for small changes (deck slide 84).

:::q <span class="tag">practice · deck slide 84</span>
A diode carries 2 mA at 0.7 V. Find its static resistance. Find it also at V_{D} = 0.6 V (I_{s} = 1 pA, so I_{D} = 11.5 mA) and at −5 V (I_{D} = −1 pA).
:::

:::guess Guess first
Is R_{D} larger near the knee or high up the curve? In reverse?
:::

:::note Terms
**Operating point (Q-point):** the DC voltage and current at which the diode sits in a circuit. **Static resistance R_{D} = V_{D}/I_{D}:** the slope of the line from the origin to the Q-point, inverted.
:::

[[fig:static_dynamic|What this graph plots: I_{D} (vertical, mA) against V_{D} (horizontal, V) for I_{s} = 1 pA, with the Q-point at 0.6 V. Dashed: the line from the origin, whose slope gives R_{D}. Red: the tangent at Q, whose slope gives r_{d} (step 8).|w=72]]

$$R_{D} = \frac{V_{D}}{I_{D}}$$

- **Near the knee and below:** little current for the voltage → **large** R_{D} (deck slide 84).
- **Higher up:** much current → small R_{D}.
- **Reverse:** almost no current → enormous R_{D}.

**Answer.** 0.7/0.002 = **350 Ω**. At 0.6 V: 0.6/0.0115 = **52 Ω**. At −5 V: 5/10^{−12} = **5 × 10^{12} Ω**.

:::check Check 7
(a) R_{D} at 0.65 V and 5 mA? (b) Why does R_{D} change along the curve? (c) Which is larger, R_{D} at 1 mA or at 10 mA, for the same diode?
:::

### 8 · Dynamic (AC) resistance r_{d}

In a circuit a small AC signal often rides on the DC (deck slide 85). The Q-point wobbles up and down the curve, so what matters is the **slope** there.

:::q <span class="tag">practice · deck slides 85–86</span>
Find the dynamic resistance at I_{D} = 2 mA (η = 1, V_{T} = 26 mV). Compare with R_{D} = 350 Ω from step 7.
:::

:::guess Guess first
Larger or smaller than R_{D}?
:::

:::note Terms
**Dynamic (AC) resistance r_{d} = ΔV_{D}/ΔI_{D}** for a small change: the inverse slope of the tangent at the Q-point (deck slide 86).
:::

Use the same figure as step 7: the red tangent.

**Derivation** (deck slide 86; each line follows from the one before):

1. Forward: I_{D} = I_{s}e^{V_{D}/ηV_{T}} (step 4).
2. Differentiate: dI_{D}/dV_{D} = I_{s}e^{V_{D}/ηV_{T}} × 1/(ηV_{T}) = **I_{D}/ηV_{T}**.
3. Invert:

$$r_{d} = \frac{ηV_{T}}{I_{D}} ≈ \frac{26 mV}{I_{D}}  (η = 1)$$

- Only I_{D} matters, not I_{s} or the exact curve. Double the current, halve r_{d}.
- For large swings use the **average** AC resistance r_{av} = ΔV/ΔI between the two end points (deck slide 85).

**Answer.** r_{d} = 26 mV / 2 mA = **13 Ω**, much smaller than R_{D} = 350 Ω: the curve is steep (small r_{d}) though its line from the origin is shallow (large R_{D}).

:::check Check 8
(a) r_{d} at 0.5 mA and at 5 mA? (b) r_{d} at 2 mA if η = 2? (c) Check: at 0.6 V the diode of step 7 carries 11.5 mA. Find r_{d} with V_{T} = 25.9 mV and compare with R_{D} = 52 Ω.
:::

### 9 · Equivalent circuits: three models

To solve a circuit by hand, the curve is replaced by straight lines (deck slides 87–89).

:::q <span class="tag">practice · deck slides 87–89</span>
A 5 V source drives a 1 kΩ resistor in series with a Si diode (forward). Find the current with (a) the ideal model, (b) the simplified 0.7 V model, (c) the piecewise-linear model with r_{av} = 10 Ω.
:::

:::guess Guess first
How much do the three answers differ: by half, or by a few per cent?
:::

:::note Terms
**Equivalent circuit:** simple parts (switch, battery, resistor) that behave like the device. **r_{av} (deck: R_{F}):** the resistance of the sloped straight line above V_{γ}.
:::

[[fig:diode_models|The three models as I–V graphs: current (vertical) against voltage (horizontal). Ideal: a closed switch forward, open reverse. Simplified: nothing until 0.7 V, then any current. Piecewise-linear: from 0.7 V a sloped line of slope 1/r_{av}.|w=92]]

[[fig:model_circuit|The question's circuit, and what replaces the diode in each model (forward direction).|w=92]]

| Model | Forward | Reverse | Use |
|---|---|---|---|
| ① Ideal (slide 89) | short (0 V) | open | quick first look, large voltages |
| ② Simplified (slide 88) | battery V_{γ} = 0.7 V | open | **default for exam circuits** |
| ③ Piecewise-linear (slide 87) | 0.7 V in series with r_{av} | open | when told r_{av} |

**Answer.** (a) I = 5/1000 = **5.0 mA**. (b) (5 − 0.7)/1000 = **4.30 mA**. (c) (5 − 0.7)/(1000 + 10) = **4.26 mA**; V_{D} = 0.7 + 4.26 mA × 10 Ω = 0.743 V.

The exact diode equation (I_{s} = 1 pA) gives 4.43 mA at 0.575 V. With 5 V available the models agree within 15 %; at low source voltages the 0.7 V matters much more.

:::check Check 9
(a) 12 V and 2.2 kΩ: current with the ideal and simplified models? (b) 2 V and 1 kΩ: by what percentage does the ideal model overestimate the simplified one? (c) When is the ideal model good enough?
:::

### 10 · Transition (depletion) capacitance C_{T}

A capacitor stores + charge on one plate and − on the other. 03a's depletion region already has that shape. Now change the voltage a little (deck slides 90–95).

:::q <span class="tag">practice · deck slides 91–95</span>
The running junction of 03a (N_{A} = 10^{17}, N_{D} = 10^{16}, W = 0.333 μm at 0 V) has area A = 100 μm × 100 μm. Find C_{T} at 0 V and at 5 V reverse.
:::

:::guess Guess first
More reverse voltage widens W. Does C_{T} go up or down?
:::

:::note Terms
**Capacitance C = dQ/dV:** extra charge stored per extra volt (deck slide 93). **Transition (depletion, space-charge, junction) capacitance C_{T}:** the capacitance from the ions of the depletion region; it dominates in reverse bias (deck slide 95). **Varactor:** a diode used as a voltage-controlled capacitor.
:::

[[fig:ct_plot|① The depletion region as a parallel-plate capacitor: the neutral regions are the plates, the carrier-free strip of width W is the insulator between them (deck slides 92, 95). ② What the graph plots: for each reverse voltage V_{R} (horizontal) the capacitance C_{T} (vertical, pF) of the running junction.|w=96]]

- Raise V_{R} by ΔV_{R}: W widens, more ions are bared on each edge, so the charge grows by ΔQ (deck slides 91–92). Majority carriers leave in about 0.6 ps (deck slide 92), so this happens instantly for any practical signal.
- The extra charge sits at the edges, a distance W apart, like a parallel-plate capacitor (deck slide 94):

$$C_{T} = \frac{εA}{W}$$

| Symbol | What it is | Unit |
|---|---|---|
| ε | permittivity of Si, 1.04 × 10^{−12} | F/cm |
| A | junction area | cm^{2} |
| W | depletion width at this bias (03a step 12) | cm |

- Since W ∝ √(V_{bi} + V_{R}): **C_{T} ∝ 1/√(V_{bi} + V_{R})**. More reverse voltage → smaller C_{T} (deck slide 95). That is the **varactor**.

**Answer.** A = (10^{−2} cm)^{2} = 10^{−4} cm^{2}. At 0 V: C_{T} = 1.04 × 10^{−12} × 10^{−4} / 3.33 × 10^{−5} = **3.12 pF**. At 5 V reverse W = 0.909 μm (03a step 12): C_{T} = **1.14 pF**, 0.37 times as much.

:::check Check 10
(a) A diode has 2 pF at 1 V reverse, V_{bi} = 0.7 V. Find C_{T} at 9.5 V reverse. (b) Why is C_{T} the one that matters in reverse bias? (c) Why does C_{T} fall as reverse voltage rises?
:::

### 11 · Diffusion (storage) capacitance C_{D}

In forward bias a second store of charge appears, outside the depletion region (deck slides 96–97).

:::q <span class="tag">practice · deck slide 96</span>
A Si diode conducts 1 mA forward. The minority-carrier lifetime is τ = 1 μs, η = 1. Find C_{D} and compare with C_{T} = 3.12 pF of step 10.
:::

:::guess Guess first
pF, nF or μF?
:::

:::note Terms
**Stored charge Q:** the extra minority carriers injected across the junction (step 2) and not yet recombined. **Lifetime τ:** the average time an extra minority carrier lives before recombining (02b step 10). **Diffusion (storage) capacitance C_{D}:** dQ/dV of that stored charge; it dominates in forward bias.
:::

[[fig:stored_charge|What this graph plots: the extra minority carriers (vertical, relative) against distance from the junction (horizontal, in diffusion lengths L). Injected carriers pile up at the edge and die away over L (02b step 12; deck slide 97). Shaded area = stored charge. Dashed: twice the current stores twice the charge.|w=74]]

**Building C_{D}** (each line follows from the one before):

1. Each injected carrier lives τ on average. A current I_{D} injects I_{D}/q carriers per second, so the store holds **Q = τI_{D}** (charge in, per second, × time each stays).
2. C_{D} = dQ/dV_{D} = τ × dI_{D}/dV_{D} = τ × I_{D}/(ηV_{T}) (step 8, line 2).

$$C_{D} = \frac{τI_{D}}{ηV_{T}}$$

| Symbol | What it is | Unit |
|---|---|---|
| τ | mean lifetime of the minority carriers | s |
| I_{D} | forward current | A |
| η, V_{T} | as in step 3 | —, V |

- C_{D} ∝ I_{D}: it is zero in reverse and grows with forward current.

**Answer.** Q = 1 μs × 1 mA = 1 nC. C_{D} = 10^{−6} × 10^{−3} / 0.0259 = **38.6 nF**, about **12 000 times** C_{T}. In forward bias C_{D} dominates; in reverse C_{T} does.

:::check Check 11
(a) τ = 20 ns, I_{D} = 10 mA, η = 1: C_{D}? (b) The current doubles: what happens to C_{D}? (c) Why is C_{D} negligible in reverse bias?
:::

### 12 · Reverse recovery: a diode cannot switch off at once

The stored charge of step 11 has to go somewhere when the diode is switched from forward to reverse (deck slides 97–100).

:::q <span class="tag">practice · deck slides 97–100</span>
A diode carries I_{F} = 10 mA (+10 V through 1 kΩ). At t = 0 the source flips to −5 V. With τ = 100 ns, how long does it conduct backwards? Use the charge-control result t_{s} = τln(1 + I_{F}/I_{R}).
:::

:::guess Guess first
At the instant the source flips, what is the diode current: zero, or something else?
:::

:::note Terms
**Storage time t_{s}:** the time the stored minority carriers keep the diode conducting backwards at a steady I_{R}. **Transition time t_{t}:** the time for the reverse current to then decay to the leakage level. **Reverse recovery time t_{rr} = t_{s} + t_{t}:** the total (deck slide 100).
:::

[[fig:recovery|What these graphs plot against time (horizontal, ns; the source flips at t = 0): top, the source voltage; bottom, the diode current (deck slide 97). For t_{s} the current is a steady −5 mA; then it decays over t_{t}.|w=80]]

- While stored charge remains, the junction stays forward-biased (about 0.7 V). The diode looks like a closed switch, so the current is set by the circuit: I_{R} = 5 V/1 kΩ = 5 mA, **backwards** (deck slide 99).
- When the store is empty, the junction can take the reverse voltage; the current decays to −I_{s} over t_{t}.
- t_{rr} ranges from a few ns to 1 μs in commercial diodes (deck slide 100). It sets the highest frequency a diode can rectify: a period must be much longer than t_{rr}.
- Faster recovery: shorter τ, or a bigger I_{R} to pull the charge out faster.

**Answer.** Not zero: it jumps to **−5 mA** and stays there. t_{s} = 100 ns × ln(1 + 10/5) = 100 × 1.10 = **110 ns**. With t_{t} = 30 ns (an assumed value: it depends on C_{T} and the circuit; the figure uses it), t_{rr} ≈ **140 ns**.

:::check Check 12
(a) Same diode, I_{R} raised to 10 mA: t_{s}? And 20 mA? (b) Why does the diode conduct backwards for a while? (c) Why does a short t_{rr} matter at high frequency?
:::

---

## Exam form

**Diode equation** (deck slides 79, 82–83). I_{D} = I_{s}(e^{V_{D}/ηV_{T}} − 1); V_{T} = kT/q = T/11 600 ≈ 26 mV; I_{s} reverse saturation current (minority carriers, ∝ n_{i}^{2}); η = 1 to 2 (1 unless told). Forward: I_{D} ≈ I_{s}e^{V_{D}/ηV_{T}}; reverse: I_{D} ≈ −I_{s}. Knee: Si 0.7 V, Ge 0.3 V, GaAs 1.2 V.

**Why exponential.** Barrier q(V_{bi} − V_{D}); Boltzmann share above it ∝ e^{V_{D}/V_{T}}; diffusion current I_{s}e^{V_{D}/V_{T}} minus fixed drift current I_{s}.

**Temperature** (deck slides 80–81). I_{s2} = I_{s1} × 2^{(T_{2} − T_{1})/10}; V_{D} falls about 2 mV/°C at fixed current; Ge more sensitive.

**Resistances** (deck slides 84–86). Static R_{D} = V_{D}/I_{D}. Dynamic: dI/dV = I_{D}/ηV_{T}, so **r_{d} = ηV_{T}/I_{D} ≈ 26 mV/I_{D}**. Average r_{av} = ΔV/ΔI for large swings.

**Equivalent circuits** (deck slides 87–89). Piecewise-linear: V_{γ} + r_{av}; simplified: V_{γ} only; ideal: switch. Reverse: open.

**Capacitances** (deck slides 91–97).

| | Transition C_{T} | Diffusion C_{D} |
|---|---|---|
| Bias | reverse | forward |
| Cause | bared ions at the depletion edges | stored injected minority carriers |
| Formula | εA/W | τI_{D}/ηV_{T} |
| Trend | falls as V_{R} rises (∝ 1/√(V_{bi} + V_{R})) | grows with I_{D} |
| Size | pF | nF |

**Reverse recovery** (deck slides 97–100). Stored charge keeps a reverse current I_{R} for t_{s}, then it decays over t_{t}; **t_{rr} = t_{s} + t_{t}**, ns to μs; limits switching frequency.

## Traps

- Using η = 2 without being told: state your choice.
- V_{T} = 26 **mV**: r_{d} = 26 mV/2 mA = 13 Ω, not 0.013 Ω.
- R_{D} (V/I, from the origin) is not r_{d} (the tangent slope).
- I_{s} doubles every **10 °C**, so 30 °C is ×8, not ×3.
- The forward voltage **falls** with temperature at fixed current.
- C_{T} is the reverse-bias capacitance; C_{D} the forward-bias one. Do not swap them.
- At switch-off the current does not drop to zero at once: it reverses for t_{s}.

## Self-test

1. I_{s} = 1 pA, η = 1, V_{T} = 25.9 mV: I_{D} at 0.65 V?
2. Same diode: what voltage gives 5 mA?
3. r_{d} at 1 mA (η = 1)?
4. I_{s} = 2 nA at 20 °C: I_{s} at 60 °C?
5. C_{T} = 10 pF at 0 V, V_{bi} = 0.75 V. C_{T} at 8.25 V reverse?
6. τ = 5 μs, I_{D} = 2 mA, η = 2: C_{D}?
7. 10 V, 470 Ω, Si diode with r_{av} = 5 Ω: current with the piecewise-linear model?
8. Explain in three lines why the forward current rises exponentially with V_{D}.

<!--ANSWERS-->

## Answers

**Check 1.** (a) **0.7 V** (Si), **0.3 V** (Ge). (b) The **log** plot: the reverse current is 10^{−12} A, invisible on a mA scale. (c) A **straight line**: the current is an exponential function of V_{D}.

**Check 2.** (a) e^{0.1/0.0259} = **47.5**. (b) It is set by how many minority carriers reach the edge, which heat sets, not the barrier: they slide down it whatever its height. (c) Diffusion I_{s} one way, drift I_{s} the other: sum **0**.

**Check 3.** (a) 373/11 600 = **32.2 mV**. (b) e^{0.5/0.0259} × 10^{−12} = **0.243 mA**. (c) It halves the exponent: the curve rises more slowly, needing twice the voltage for the same factor of current.

**Check 4.** (a) V = V_{T}ln(I/I_{s}): 0.0259 × ln(10^{9}) = **0.537 V**; 10 mA: **0.596 V** (one decade = 59.6 mV more). (b) **−2 nA**: the reverse current is flat. (c) **119 mV**.

**Check 5.** (a) It is set by the supply of minority carriers made by heat; every one that arrives is swept across already. (b) The **n-side** term n_{i}^{2}/N_{D}: the lightly doped side has far more minority carriers. (c) n_{i} rises steeply with T and I_{s} ∝ n_{i}^{2}.

**Check 6.** (a) 100 °C = 10 doublings: 2^{10} = 1024: **1.02 nA**. (b) 0.65 + 0.002 × 40 = **0.73 V**. (c) More carriers are made by heat, so a smaller barrier lowering gives the same current.

**Check 7.** (a) 0.65/0.005 = **130 Ω**. (b) The curve is not a straight line through the origin: V/I differs at each point. (c) **1 mA** (lower on the curve, less current per volt).

**Check 8.** (a) **52 Ω** and **5.2 Ω**. (b) 2 × 26/2 = **26 Ω**. (c) 0.0259/0.0115 = **2.25 Ω**, far below R_{D} = 52 Ω.

**Check 9.** (a) Ideal: 12/2200 = **5.45 mA**; simplified: 11.3/2200 = **5.14 mA**. (b) 2 mA vs 1.3 mA: **54 %** too high. (c) When the source voltage is much larger than 0.7 V.

**Check 10.** (a) C_{T} ∝ 1/√(V_{bi} + V_{R}): 2 × √(1.7/10.2) = **0.82 pF**. (b) In reverse there is no injected charge, so only the depletion charge changes with V. (c) W widens, so the "plates" are further apart.

**Check 11.** (a) 20 × 10^{−9} × 0.01 / 0.0259 = **7.72 nF**. (b) It **doubles** (C_{D} ∝ I_{D}). (c) In reverse almost nothing is injected, so nothing is stored.

**Check 12.** (a) 100 × ln 2 = **69 ns**; 100 × ln 1.5 = **41 ns**. (b) The stored minority carriers must leave or recombine before the junction can block; until then it stays forward-biased and the circuit pushes current backwards. (c) Each switching takes t_{rr}; if the period is not much longer, the diode conducts backwards for a large part of each cycle.

**Self-test.**

1. 10^{−12} × e^{25.10} = **79.6 mA**.
2. 0.0259 × ln(5 × 10^{9}) = **0.578 V**.
3. **26 Ω**.
4. Four doublings: **32 nA**.
5. 10 × √(0.75/9.0) = **2.89 pF**.
6. 5 × 10^{−6} × 2 × 10^{−3} / (2 × 0.0259) = **193 nF**.
7. 9.3/475 = **19.6 mA**.
8. The barrier is q(V_{bi} − V_{D}). The share of majority carriers able to climb it is e^{−(V_{bi} − V_{D})/V_{T}} (Boltzmann), so it grows as e^{V_{D}/V_{T}}. The opposing minority drift current is fixed at I_{s}, giving I_{s}(e^{V_{D}/V_{T}} − 1).

<!--/ANSWERS-->
