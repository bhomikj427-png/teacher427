# 08 — The MOSFET

<div class="sub">MOSFET deck slides 4–18 · "MOSFET biasing" deck slides 10–16 · numericals sheet Q20–Q31 · syllabus Unit 4 · needs 07 (Shockley, biasing, g_{m})</div>

## Map

[[map:1 Structure, types > 2 Regions, equations > 3 Biasing > 4 CS, CD, CG amplifiers|here=1]]

The JFET (07) controls its channel with a reverse-biased junction. The MOSFET replaces that junction with a metal plate on a thin layer of glass. The idea is the same (a gate voltage sets the channel current), the equations are almost the same, and it is the transistor inside every digital chip (09).

## The questions this file answers

- <span class="tag">Sheet Q30</span> I_{D(on)} = 500 mA at V_{GS} = 10 V and V_{GS(th)} = 1 V. Find I_{D} at V_{GS} = 5 V.
- <span class="tag">Sheet Q26</span> A D-MOSFET has I_{DSS} = 10 mA and V_{GS(off)} = −8 V. n- or p-channel? I_{D} at V_{GS} = −3 V and +3 V?
- <span class="tag">Sheet Q28</span> D-MOSFET, gate at 0 V, V_{DD} = 18 V, R_{D} = 620 Ω. Find V_{DS}.
- <span class="tag">practice</span> Divider and drain-feedback bias of an E-MOSFET; g_{m} and the gain of CS, CD and CG stages.

---

## Build

### 1 · Structure and the two types

:::guess Predict
With V_{GS} = 0, an enhancement MOSFET carries no drain current but a depletion MOSFET does. What would have to exist between source and drain for current to flow?
:::

:::note Terms
**Oxide:** a very thin insulating layer of SiO_{2} under the gate. **Substrate (body):** the p-type silicon the device is built in, normally tied to the source. **n⁺:** heavily doped n-type.
:::

[[fig:mos_struct|n-channel enhancement MOSFET. Gate, oxide and substrate form a capacitor.|w=60]]

- Two n⁺ regions (source, drain) sit in a p substrate. With V_{GS} = 0 the path is n–p–n: two diodes back to back, so **no current**.
- A positive gate pushes holes away from the surface and attracts electrons. At the **threshold voltage V_{T}** (also V_{GS(th)}) the electrons form an n-type **inversion layer**: the channel.
- More gate voltage, more electrons, more current: the gate **enhances** the channel.

| | Enhancement (E-MOSFET) | Depletion (D-MOSFET) |
|---|---|---|
| Channel at V_{GS} = 0 | none: **normally off** | built in: **normally on** |
| n-channel control | V_{GS} &gt; V_{T} (positive) turns it on | negative V_{GS} depletes, positive enhances |
| Saturation equation | I_{D} = K(V_{GS} − V_{T})^{2} | Shockley: I_{D} = I_{DSS}(1 − V_{GS}/V_{GS(off)})^{2}, valid for positive V_{GS} too |
| Symbol | broken channel line | solid channel line |

[[fig:mos_symbols|MOSFET symbols.|w=60]]

The gate is insulated, so I_{G} ≈ 0 and the input resistance is even higher than a JFET's (10^{10}–10^{15} Ω). The thin oxide is destroyed by static charge, so MOSFETs need careful handling. A p-channel device reverses every voltage (V_{T} negative).

**Answer.** Current needs a continuous channel of one type. An E-MOSFET has none at V_{GS} = 0, only two back-to-back junctions, so it stays off until V_{GS} &gt; V_{T} induces one. A D-MOSFET is made with the channel in place, so I_{D} = I_{DSS} flows at V_{GS} = 0.

:::check Check 1
(a) What does each letter of MOS stand for, and what does each layer do? (b) What is the inversion layer? (c) Why is the gate current of a MOSFET essentially zero?
:::

### 2 · Regions and the current equations

:::q <span class="tag">Sheet Q30</span>
The data sheet for an E-MOSFET gives I_{D(on)} = 500 mA at V_{GS} = 10 V and V_{GS(th)} = 1 V. Determine the drain current for V_{GS} = 5 V.
:::

:::guess Guess first
V_{GS} is halved. Is the current halved?
:::

[[fig:mos_curves|E-MOSFET transfer and drain curves.]]

| Region | Test (n-channel) | Drain current | Acts as |
|---|---|---|---|
| Cutoff | V_{GS} ≤ V_{T} | I_{D} = 0 | open switch |
| Triode (ohmic) | V_{GS} &gt; V_{T}, V_{DS} &lt; V_{GS} − V_{T} | K[2(V_{GS} − V_{T})V_{DS} − V_{DS}^{2}] | resistor set by V_{GS} |
| **Saturation** | V_{GS} &gt; V_{T}, V_{DS} ≥ V_{GS} − V_{T} | **K(V_{GS} − V_{T})^{2}** | current source; amplifier |

- The region test is the **first step of every MOSFET problem**. V_{GS} − V_{T} is the **overdrive**.
- K comes from one data-sheet point: **K = I_{D(on)}/(V_{GS(on)} − V_{T})^{2}**. In device terms K = ½μ_{n}C_{ox}(W/L). Sedra & Smith write k_{n} = 2K, so their equation reads ½k_{n}(V_{GS} − V_{T})^{2}: same physics.
- Channel-length modulation tilts the saturation curves: I_{D} = K(V_{GS} − V_{T})^{2}(1 + λV_{DS}), giving r_{o} = 1/(λI_{D}).

**Answer.** K = 500/(10 − 1)^{2} = 500/81 = 6.17 mA/V^{2}. At 5 V: I_{D} = 6.17 × (5 − 1)^{2} = **98.8 mA** (the sheet prints 98.7). Halving V_{GS} cut the current by five, because the law squares the overdrive.

:::check Check 2
(a) <span class="tag">Sheet Q26</span> A D-MOSFET has I_{DSS} = 10 mA and V_{GS(off)} = −8 V. (i) n- or p-channel? (ii) I_{D} at V_{GS} = −3 V? (iii) I_{D} at V_{GS} = +3 V? (b) An nMOS has K = 1 mA/V^{2}, V_{T} = 1 V, V_{GS} = 3 V. Name the region and find I_{D} for V_{DS} = 1 V and for V_{DS} = 4 V.
:::

### 3 · Biasing

:::q <span class="tag">practice · biasing deck slides 10–16</span>
In circuit (a), the E-MOSFET has K = 0.5 mA/V^{2} and V_{T} = 2 V (V_{DD} = 20 V, R_{1} = 7 MΩ, R_{2} = 3 MΩ, R_{D} = 3 kΩ, R_{S} = 1 kΩ). Find I_{D}, V_{GS} and V_{DS}, and confirm the region.
:::

:::guess Guess first
What is the gate voltage? (I_{G} = 0, so nothing flows out of the divider.)
:::

[[fig:mos_bias_three|(a) voltage divider, (b) drain-to-gate feedback, (c) self-bias (depletion type only).]]

| Circuit | Gate–source loop | Notes |
|---|---|---|
| Fixed bias | V_{GS} = V_{GG} | Q-point moves if K or V_{T} change |
| Voltage divider (a) | V_{G} = V_{DD}R_{2}/(R_{1} + R_{2}); V_{GS} = V_{G} − I_{D}R_{S} | the usual choice |
| Drain feedback (b) | no drop in R_{G}: V_{GS} = V_{DS} = V_{DD} − I_{D}R_{D} | always in saturation, since V_{DS} = V_{GS} &gt; V_{GS} − V_{T} |
| Self-bias (c) | V_{GS} = −I_{D}R_{S} | depletion type only: negative V_{GS} never turns on an E-MOSFET |

Procedure, the same as 07: write V_{GS} in terms of I_{D} → put it into I_{D} = K(V_{GS} − V_{T})^{2} → keep the root with V_{GS} &gt; V_{T} → V_{DS} = V_{DD} − I_{D}(R_{D} + R_{S}) → check V_{DS} ≥ V_{GS} − V_{T}. The DC load line V_{DS} = V_{DD} − I_{D}R_{D} ends at (0, V_{DD}/R_{D}) and (V_{DD}, 0).

**Answer.** V_{G} = 20 × 3/10 = 6 V, so V_{GS} = 6 − I_{D} (mA, kΩ). I_{D} = 0.5(4 − I_{D})^{2} gives I_{D}^{2} − 10I_{D} + 16 = 0: I_{D} = 2 or 8 mA. 8 mA makes V_{GS} = −2 V, below V_{T}: reject. **I_{D} = 2 mA, V_{GS} = 4 V, V_{DS} = 20 − 2(3 + 1) = 12 V**. 12 ≥ 4 − 2 = 2 V: saturation ✓.

:::check Check 3
(a) Solve circuit (b) with the same MOSFET (V_{DD} = 12 V, R_{D} = 4 kΩ). (b) <span class="tag">Sheet Q28</span> A D-MOSFET with V_{GS(off)} = −8 V and I_{DSS} = 12 mA has its gate at 0 V, V_{DD} = +18 V, R_{D} = 620 Ω. Find V_{DS}. (c) Why does self-bias fail for an enhancement MOSFET?
:::

### 4 · Small signal: CS, CD and CG amplifiers

:::q <span class="tag">practice · syllabus Unit 4</span>
The MOSFET of step 3 is biased at V_{GS} = 4 V, I_{D} = 2 mA. Find g_{m}, and the gain of a common-source stage with R_{D} = 3 kΩ. Neglect r_{o}.
:::

:::guess Guess first
Will the formula for gain look like the JFET's (07 §6)? What changes?
:::

[[fig:mos_ss_table|The small-signal model is the JFET's: g_{m}v_{gs} in parallel with r_{o}, gate open.|w=70]]

Differentiating I_{D} = K(V_{GS} − V_{T})^{2}:

$$g_{m} = 2K(V_{GS} − V_{T}) = 2\sqrt{K I_{D}} = 2I_{D}/(V_{GS} − V_{T})$$

| | Common source | Common drain (follower) | Common gate |
|---|---|---|---|
| In · out | gate · drain | gate · source | source · drain |
| A_{v} | −g_{m}(R_{D} ∥ r_{o}); unbypassed R_{S}: −g_{m}R_{D}/(1 + g_{m}R_{S}) | g_{m}R_{S}/(1 + g_{m}R_{S}) ≈ 1 | +g_{m}R_{D} |
| Phase | 180° | 0° | 0° |
| R_{in} | very high | very high | 1/g_{m}, low |
| R_{out} | R_{D} ∥ r_{o} | R_{S} ∥ 1/g_{m}, low | R_{D} |
| Role | voltage gain | buffer | current buffer, wide band |

"Common" names the terminal at AC ground, shared by input and output.

**Answer.** g_{m} = 2 × 0.5 × (4 − 2) = **2 mS** (check: 2√(0.5 × 2) = 2 mS). A_{v} = −2 mS × 3 kΩ = **−6**.

:::check Check 4
With g_{m} = 2 mS: (a) the input resistance of a common-gate stage; (b) the gain of a source follower with R_{S} = 1 kΩ; (c) the bias current rises from 2 mA to 8 mA: the new g_{m}?
:::

---

## Exam form

**Structure and operation.** Sketch: p substrate, n⁺ source and drain, oxide, gate. V_{GS} = 0: back-to-back junctions, no current. V_{GS} &gt; V_{T}: inversion layer forms the channel. E-type normally off; D-type normally on (channel built in). Insulated gate: I_{G} ≈ 0.

**Equations.** Cutoff V_{GS} ≤ V_{T}. Triode: K[2(V_{GS} − V_{T})V_{DS} − V_{DS}^{2}]. Saturation (V_{DS} ≥ V_{GS} − V_{T}): K(V_{GS} − V_{T})^{2}. K = I_{D(on)}/(V_{GS(on)} − V_{T})^{2}. D-MOSFET: Shockley.

**Bias procedure.** Gate loop → substitute → reject root with V_{GS} &lt; V_{T} → V_{DS} → region check.

**Small signal.** g_{m} = 2K(V_{GS} − V_{T}) = 2√(KI_{D}). CS −g_{m}R_{D}; CD g_{m}R_{S}/(1 + g_{m}R_{S}); CG +g_{m}R_{D}, R_{in} = 1/g_{m}.

## Traps

- Skipping the region test, then using the saturation equation in triode.
- Using self-bias with an enhancement device: V_{GS} would be negative, and it never turns on.
- Keeping the quadratic root with V_{GS} &lt; V_{T}.
- Mixing K and k_{n} = 2K between books: check which form the question uses.
- For a D-MOSFET with positive V_{GS}, I_{D} &gt; I_{DSS}: that is correct, not an error.
- g_{m} grows with √I_{D}, not with I_{D}.

## Self-test

1. Draw an n-channel E-MOSFET and explain how the channel forms.
2. An E-MOSFET has K = 0.25 mA/V^{2}, V_{T} = 2 V. Find I_{D} at V_{GS} = 6 V in saturation, and g_{m} there.
3. <span class="tag">Sheet Q26</span> For the D-MOSFET of Check 2(a), find V_{GS} for I_{D} = 2.5 mA.
4. State the condition for saturation and explain physically why I_{D} stops depending on V_{DS}.
5. A CS stage has g_{m} = 4 mS, R_{D} = 2 kΩ and an unbypassed R_{S} = 0.5 kΩ. Find A_{v}.
6. Compare E-MOSFET and D-MOSFET in four points.

<!--ANSWERS-->

## Answers

**Check 1.** (a) Metal: the gate electrode. Oxide: the SiO_{2} insulator. Semiconductor: the silicon where the channel forms. (b) A thin layer of electrons at the surface of the p substrate, attracted by a positive gate; it is n-type, so it joins source to drain. (c) The oxide is an insulator: only a capacitor-charging current flows, none in steady state.

**Check 2.** (a) (i) **n-channel**: V_{GS(off)} is negative. (ii) 10(1 − 3/8)^{2} = **3.91 mA**. (iii) 10(1 + 3/8)^{2} = **18.9 mA**, above I_{DSS} because positive V_{GS} enhances. (b) Overdrive 2 V. V_{DS} = 1 V &lt; 2 V: **triode**, I_{D} = 1 × [2(2)(1) − 1] = **3 mA**. V_{DS} = 4 V ≥ 2 V: **saturation**, I_{D} = 1 × 2^{2} = **4 mA**.

**Check 3.** (a) V_{GS} = V_{DS} = 12 − 4I_{D}. I_{D} = 0.5(10 − 4I_{D})^{2} gives 8I_{D}^{2} − 41I_{D} + 50 = 0: I_{D} = 2 or 3.125 mA. The second gives V_{GS} = −0.5 V: reject. **I_{D} = 2 mA, V_{GS} = V_{DS} = 4 V**. (b) V_{GS} = 0, so I_{D} = I_{DSS} = 12 mA; V_{DS} = 18 − 12 × 0.62 = **10.56 V** (sheet: 10.6 V). (c) V_{GS} = −I_{D}R_{S} is negative; an n-channel E-MOSFET needs V_{GS} &gt; V_{T} &gt; 0.

**Check 4.** (a) R_{in} = 1/g_{m} = **500 Ω**. (b) A_{v} = 2/(1 + 2) = **0.667**. (c) g_{m} = 2√(0.5 × 8) = **4 mS**: four times the current, twice the g_{m}.

**Self-test.**

1. See step 1: positive gate repels holes, attracts electrons; at V_{T} an n-type inversion layer joins source and drain.
2. I_{D} = 0.25 × 4^{2} = **4 mA**; g_{m} = 2 × 0.25 × 4 = **2 mS**.
3. 2.5 = 10(1 + V_{GS}/8)^{2}: 1 + V_{GS}/8 = 0.5, so **V_{GS} = −4 V**.
4. V_{DS} ≥ V_{GS} − V_{T}. The channel pinches off at the drain end; extra V_{DS} drops across the short pinched region, so the channel voltage and current stay fixed.
5. A_{v} = −4 × 2/(1 + 4 × 0.5) = −8/3 = **−2.67**.
6. Channel built-in or induced; normally on or off; V_{GS} polarity range (both signs vs above V_{T} only); equation (Shockley vs K(V_{GS} − V_{T})^{2}); symbol (solid vs broken line); self-bias possible only for D-type.

<!--/ANSWERS-->
