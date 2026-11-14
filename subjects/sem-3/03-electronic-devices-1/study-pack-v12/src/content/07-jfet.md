# 07 — The JFET

<div class="sub">JFET deck slides 5–44 · numericals sheet Q1–Q19 · syllabus Unit 3 · "8 marks" relayed for the parameters (§3) · needs 03 (the reverse-biased pn junction and its depletion region)</div>

## Map

[[map:1 What a JFET is > 2 Shockley's equation > 3 g_{m}, r_{d}, μ > 4 Self-bias > 5 Voltage-divider bias > 6 Amplifiers|here=1]]

A diode (03) has two terminals and no control. A transistor adds a third terminal that controls the current between the other two. The JFET is the simplest one: a reverse-biased pn junction squeezes a channel of doped silicon.

## The questions this file answers

- <span class="tag">Deck slides 30–31 · 8 marks</span> Define the characteristic parameters of a JFET and derive the relation among them.
- <span class="tag">Sheet Q2</span> I_{DSS} = 32 mA, V_{GS(off)} = −8 V, V_{GS} = −4.5 V. Find the drain current.
- <span class="tag">Sheet Q17</span> Determine I_{D} and V_{GS} for the JFET with voltage-divider bias in Fig. 9, given V_{D} = 7 V.
- <span class="tag">practice</span> Self-bias Q-point; gain of a common-source amplifier.

---

## Build

### 1 · What a JFET is

:::guess Predict
The gate of a JFET is a pn junction that is always kept reverse biased. How much current flows into the gate?
:::

:::note Terms
**Channel:** the strip of n-type silicon the current flows through. **Source, drain:** its two ends; carriers enter at the source and leave at the drain. **Gate:** the p regions on both sides of the channel, joined together.
:::

[[fig:jfet_struct|n-channel JFET. The gate–channel junctions are reverse biased, so each has a depletion region (03).|w=70]]

- Making V_{GS} **more negative** widens the depletion regions, which **narrows the channel**, so the drain current I_{D} falls.
- At V_{GS} = **V_{GS(off)}** the depletion regions meet and I_{D} = 0 (cutoff).
- With V_{GS} = 0, raising V_{DS} pinches the channel at the drain end. Above the **pinch-off voltage V_{P}** the current stops rising and stays at **I_{DSS}**, the largest current the JFET carries. Numerically V_{P} = |V_{GS(off)}|.

**Answer.** Only a leakage current of nanoamps (I_{G} ≈ 0), because the gate junction is reverse biased. So the input resistance is very high (10^{8}–10^{12} Ω), and the drain current is controlled by a **voltage**, not a current. One type of carrier does the work, so the JFET is **unipolar**.

:::check Check 1
(a) What two things does making V_{GS} more negative do inside the device? (b) Define I_{DSS} and V_{GS(off)}. (c) Why is the depletion region wider at the drain end than at the source end?
:::

### 2 · Shockley's equation

Step 1 says I_{D} falls as V_{GS} goes negative. The next question is by how much.

:::q <span class="tag">Sheet Q2</span>
A JFET has I_{DSS} = 32 mA, V_{GS(off)} = −8 V and V_{GS} = −4.5 V. Find the value of drain current.
:::

:::guess Guess first
V_{GS} is a little over halfway to cutoff. Is I_{D} more or less than half of I_{DSS}?
:::

[[fig:jfet_curves|Left: transfer curve (I_{D} against V_{GS}). Right: drain curves, one per V_{GS}.]]

In saturation the transfer curve is a parabola:

$$I_{D} = I_{DSS}(1 − V_{GS}/V_{GS(off)})^{2}$$

Quick sketch points: V_{GS} = 0 gives I_{DSS}; V_{GS} = V_{GS(off)}/2 gives I_{DSS}/4; V_{GS} = V_{GS(off)} gives 0. Both voltages are negative for an n-channel JFET, so the ratio is positive.

| Region | Condition | Behaviour |
|---|---|---|
| Ohmic | V_{DS} &lt; V_{GS} − V_{GS(off)} | a resistor whose value V_{GS} sets |
| **Saturation** | V_{DS} ≥ V_{GS} − V_{GS(off)} | I_{D} fixed by V_{GS} alone; amplifiers work here |
| Cutoff | V_{GS} ≤ V_{GS(off)} | I_{D} = 0 |

**Answer.** I_{D} = 32 × (1 − (−4.5)/(−8))^{2} = 32 × 0.4375^{2} = **6.12 mA**, under a fifth of I_{DSS}: the square makes the current fall fast.

:::check Check 2
(a) <span class="tag">Sheet Q5</span> V_{GS} = −2 V, V_{GS(off)} = −6 V, I_{DSS} = 3 mA. Find I_{D}. (b) <span class="tag">Sheet Q3</span> I_{D} = 5 mA, I_{DSS} = 10 mA, V_{GS(off)} = −6 V. Find V_{GS} and V_{P}.
:::

### 3 · The parameters g_{m}, r_{d}, μ

I_{D} depends on two voltages, V_{GS} and V_{DS}. Each slope of that dependence is a parameter, and this is the item flagged at 8 marks.

:::q <span class="tag">Deck slides 30–31 · 8 marks</span>
Define the characteristic parameters of a JFET and derive the relation among them.
:::

:::guess Guess first
How many independent slopes can you take of a quantity that depends on two variables?
:::

| Parameter | Definition | Held constant | Meaning, unit |
|---|---|---|---|
| **Transconductance g_{m}** | ΔI_{D}/ΔV_{GS} | V_{DS} | how strongly the gate controls I_{D}; S (mS, μS) |
| **Drain resistance r_{d}** | ΔV_{DS}/ΔI_{D} | V_{GS} | AC resistance of the channel in saturation; kΩ–MΩ |
| **Drain conductance g_{d}** | ΔI_{D}/ΔV_{DS} = 1/r_{d} | V_{GS} | slope of a drain curve; S |
| **Amplification factor μ** | −ΔV_{DS}/ΔV_{GS} | I_{D} | volts of V_{DS} that undo 1 V of V_{GS}; no unit |

**Answer (derivation).** For small changes, ΔI_{D} = (∂I_{D}/∂V_{GS})ΔV_{GS} + (∂I_{D}/∂V_{DS})ΔV_{DS} = g_{m}ΔV_{GS} + ΔV_{DS}/r_{d}. Hold I_{D} constant (ΔI_{D} = 0): g_{m}ΔV_{GS} = −ΔV_{DS}/r_{d}, so −ΔV_{DS}/ΔV_{GS} = g_{m}r_{d}. The left side is μ by definition:

$$μ = g_{m} × r_{d}$$

**g_{m} from Shockley.** Differentiating step 2's equation:

$$g_{m} = g_{m0}(1 − V_{GS}/V_{GS(off)})    g_{m0} = 2I_{DSS}/|V_{GS(off)}|$$

Example: I_{DSS} = 8 mA, V_{GS(off)} = −4 V gives g_{m0} = 4 mS; at V_{GS} = −2 V, g_{m} = 2 mS. With r_{d} = 50 kΩ, μ = 2 mS × 50 kΩ = 100.

:::check Check 3
(a) <span class="tag">Sheet Q7</span> When V_{GS} changes from −3.1 V to −3 V, I_{D} changes from 1 mA to 1.3 mA. Find g_{m}. (b) <span class="tag">Sheet Q8</span> g_{m0} = 4000 μS and V_{GS(off)} = −8 V. Find g_{m} at V_{GS} = −3 V.
:::

### 4 · Self-bias

To use a JFET, it must sit at a fixed point (I_{D}, V_{DS}) in saturation. Choosing the resistors that put it there is **biasing**.

:::q <span class="tag">practice</span>
A self-biased JFET has I_{DSS} = 8 mA, V_{GS(off)} = −4 V, R_{S} = 1 kΩ, R_{D} = 3.3 kΩ and V_{DD} = 20 V. Find I_{D}, V_{GS} and V_{DS}.
:::

:::guess Guess first
The gate is tied to ground through R_{G}. How can V_{GS} be negative with no negative supply?
:::

[[fig:jfet_self_bias|Self-bias: the gate returns to ground through R_{G}; the source sits above ground by I_{D}R_{S}.|w=45]]

Two facts make every JFET bias problem short: **I_{G} = 0**, so there is no drop across R_{G} and V_{G} = 0; and **I_{S} = I_{D}**. The source sits at I_{D}R_{S} above ground, so **V_{GS} = −I_{D}R_{S}**. If I_{D} rises, V_{GS} becomes more negative and pulls it back: the circuit corrects itself.

**Answer.** Put V_{GS} = −I_{D} (mA, kΩ) into Shockley: I_{D} = 8(1 − I_{D}/4)^{2}, which gives I_{D}^{2} − 10I_{D} + 16 = 0, so I_{D} = 2 mA or 8 mA. **Reject 8 mA**: it needs V_{GS} = −8 V, beyond cutoff. So **I_{D} = 2 mA, V_{GS} = −2 V**, and V_{DS} = 20 − 2(3.3 + 1) = **11.4 V**. Saturation check: 11.4 ≥ V_{GS} − V_{GS(off)} = 2 V ✓.

:::check Check 4
(a) Why does self-bias always give two roots, and how do you pick the right one? (b) <span class="tag">Sheet Q19</span> V_{DD} = 20 V, R_{D} = 500 Ω, no R_{S}. Give the two end points of the d.c. load line.
:::

### 5 · Voltage-divider bias

Self-bias depends strongly on the device's I_{DSS}, which varies from part to part. A divider fixes the gate voltage instead.

:::q <span class="tag">Sheet Q17</span>
Determine I_{D} and V_{GS} for the JFET with voltage-divider bias in Fig. 9, given that V_{D} = 7 V. (Fig. 9: V_{DD} = 12 V, R_{D} = 3.3 kΩ, R_{S} = 1.8 kΩ, R_{1} = 6.8 MΩ, R_{2} = 1 MΩ.)
:::

:::guess Guess first
V_{D} is given. Which single resistor lets you find I_{D} straight away?
:::

[[fig:jfet_divider|Voltage-divider bias.|w=45]]

$$V_{G} = V_{DD}R_{2}/(R_{1} + R_{2})    V_{GS} = V_{G} − I_{D}R_{S}    V_{DS} = V_{DD} − I_{D}(R_{D} + R_{S})$$

V_{GS} must still come out negative. The drain-loop equation is the same for every bias circuit.

**Answer.** I_{D} = (V_{DD} − V_{D})/R_{D} = (12 − 7)/3.3 k = **1.52 mA**. V_{S} = 1.52 mA × 1.8 kΩ = 2.73 V. V_{G} = 12 × 1/(6.8 + 1) = 1.54 V. V_{GS} = 1.54 − 2.73 = **−1.19 V** (the sheet rounds to −1.2 V).

:::check Check 5
<span class="tag">Sheet Q18</span> An n-channel JFET with I_{DSS} = 10 mA and V_{GS(off)} = −5 V is biased by a divider with V_{DD} = 30 V, R_{1} = 1 MΩ, R_{2} = 500 kΩ, to I_{D} = 2.5 mA and V_{DS} = 8 V. Find R_{S}.
:::

### 6 · JFET amplifiers

A biased JFET turns a small change in v_{gs} into a change in i_{d} of g_{m}v_{gs} (step 3). A drain resistor turns that current into an output voltage.

:::q <span class="tag">practice</span>
A common-source amplifier has g_{m} = 2 mS, r_{d} = 50 kΩ and R_{D} = 2.2 kΩ, with R_{S} fully bypassed. Find the voltage gain.
:::

:::guess Guess first
Will the output be in phase with the input, or inverted?
:::

[[fig:fet_cs_amp|Common-source amplifier. C_{1}, C_{2} pass the signal and block DC; C_{S} shorts R_{S} for the signal.|w=55]]

[[fig:fet_small_signal|Small-signal model: a current source g_{m}v_{gs} in parallel with r_{d}; the gate is an open circuit.|w=55]]

| | Common source | Common drain (source follower) | Common gate |
|---|---|---|---|
| In · out | gate · drain | gate · source | source · drain |
| A_{v} | −g_{m}(r_{d} ∥ R_{D}); unbypassed: −g_{m}R_{D}/(1 + g_{m}R_{S}) | g_{m}R_{S}/(1 + g_{m}R_{S}), just under 1 | +g_{m}R_{D} |
| Phase | inverted | in phase | in phase |
| Z_{in} | R_{G}, very high | R_{G}, very high | R_{S} ∥ 1/g_{m}, low |
| Z_{out} | ≈ R_{D} | R_{S} ∥ 1/g_{m}, low | ≈ R_{D} |
| Used as | voltage amplifier | buffer | high-frequency stage |

**Answer.** r_{d} ∥ R_{D} = (50 × 2.2)/52.2 = 2.107 kΩ, so A_{v} = −2 mS × 2.107 kΩ = **−4.21**. Inverted: a rise in v_{gs} raises i_{d}, which drops more voltage across R_{D}, so the drain falls.

:::check Check 6
(a) A source follower has g_{m} = 2 mS, R_{S} = 1 kΩ. Find A_{v} and Z_{out}. (b) What happens to the CS gain if C_{S} is removed, and why? (c) Which configuration goes between a 1 MΩ sensor and a 1 kΩ load?
:::

---

## Exam form

**Operation.** n-channel bar, two p-gate regions; gate reverse biased, so I_{G} ≈ 0 and Z_{in} is very high. More negative V_{GS} → wider depletion → narrower channel → less I_{D}. Cutoff at V_{GS(off)}; pinch-off at V_{P} = |V_{GS(off)}|, where I_{D} levels at I_{DSS}. Unipolar, voltage-controlled.

**Shockley.** I_{D} = I_{DSS}(1 − V_{GS}/V_{GS(off)})^{2}; saturation if V_{DS} ≥ V_{GS} − V_{GS(off)}.

**Parameters (8 marks).** Table of g_{m}, r_{d}, g_{d}, μ with what is held constant → ΔI_{D} = g_{m}ΔV_{GS} + ΔV_{DS}/r_{d} → set ΔI_{D} = 0 → μ = g_{m}r_{d}. Add g_{m} = g_{m0}(1 − V_{GS}/V_{GS(off)}), g_{m0} = 2I_{DSS}/|V_{GS(off)}|.

**Bias procedure.** 1. Gate loop: V_{GS} = −I_{D}R_{S} (self) or V_{G} − I_{D}R_{S} (divider). 2. Put it into Shockley, solve the quadratic. 3. Reject the root beyond cutoff. 4. V_{DS} = V_{DD} − I_{D}(R_{D} + R_{S}). 5. Check saturation.

**Amplifiers.** CS: −g_{m}(r_{d} ∥ R_{D}), inverted. CD: g_{m}R_{S}/(1 + g_{m}R_{S}), Z_{out} = R_{S} ∥ 1/g_{m}. CG: +g_{m}R_{D}, Z_{in} low.

**Applications.** Low-noise high-Z_{in} first stage, buffer, voltage-variable resistor (ohmic region), analog switch, constant-current source.

## Traps

- Dropping the minus signs: for n-channel, V_{GS} and V_{GS(off)} are both negative, and their ratio is positive.
- Keeping the root beyond cutoff after solving the self-bias quadratic.
- Skipping the saturation check at the end.
- Putting a voltage drop across R_{G}: I_{G} = 0.
- Using −g_{m}R_{D} when R_{S} is unbypassed: the gain falls to −g_{m}R_{D}/(1 + g_{m}R_{S}).
- Writing V_{P} with a sign: V_{P} is the magnitude of V_{GS(off)}.

## Self-test

1. Why is a JFET called voltage-controlled and unipolar?
2. <span class="tag">Sheet Q4</span> V_{GS(off)} = −4 V, I_{DSS} = 12 mA, R_{D} = 560 Ω, gate tied to source. Find the minimum V_{DD} for the constant-current region.
3. <span class="tag">Sheet Q6</span> A reverse gate voltage of 15 V gives a gate current of 10^{−3} μA. Find the resistance between gate and source.
4. Write μ = g_{m}r_{d} starting from ΔI_{D} = 0, from memory.
5. Find g_{m0} for I_{DSS} = 8 mA, V_{GS(off)} = −4 V, and g_{m} at V_{GS} = −1 V.
6. List three applications of the JFET.

<!--ANSWERS-->

## Answers

**Check 1.** (a) Widens the gate depletion regions, so the channel narrows; channel resistance rises and I_{D} falls. (b) I_{DSS}: the drain current in saturation with V_{GS} = 0, the maximum. V_{GS(off)}: the V_{GS} at which I_{D} becomes zero. (c) The channel voltage rises from source to drain, so the gate junction is more reverse biased near the drain.

**Check 2.** (a) I_{D} = 3(1 − 2/6)^{2} = 3 × 0.444 = **1.33 mA**. (b) 5 = 10(1 + V_{GS}/6)^{2}, so 1 + V_{GS}/6 = √0.5 = 0.707 and **V_{GS} = −1.76 V**; **V_{P} = 6 V**.

**Check 3.** (a) g_{m} = 0.3 mA/0.1 V = **3 mS** (3000 μS). (b) g_{m} = 4000 × (1 − 3/8) = **2500 μS**.

**Check 4.** (a) Shockley is a square, so the gate-loop line crosses the parabola twice. The root with |V_{GS}| larger than |V_{GS(off)}| is beyond cutoff, where the equation does not apply: reject it. (b) I_{D} = 0 gives V_{DS} = V_{DD} = **20 V**; V_{DS} = 0 gives I_{D} = 20/0.5 k = **40 mA**.

**Check 5.** Shockley: 2.5 = 10(1 + V_{GS}/5)^{2}, so V_{GS} = −2.5 V. V_{G} = 30 × 500/1500 = 10 V. V_{S} = V_{G} − V_{GS} = 12.5 V. R_{S} = 12.5 V/2.5 mA = **5 kΩ**.

**Check 6.** (a) A_{v} = 2/(1 + 2) = **0.667**; Z_{out} = 1 kΩ ∥ 500 Ω = **333 Ω**. (b) It falls to −g_{m}R_{D}/(1 + g_{m}R_{S}): the signal current now flows through R_{S}, and the voltage there subtracts from v_{gs} (negative feedback, 13). (c) **Common drain**: very high Z_{in}, low Z_{out}.

**Self-test.**

1. I_{D} is set by the gate voltage through the depletion width, with no gate current. One carrier type (electrons in n-channel) carries the current.
2. Constant current needs V_{DS} ≥ V_{P} = 4 V with I_{D} = I_{DSS} = 12 mA. V_{DD} = 4 + 12 mA × 560 Ω = **10.72 V**.
3. R = 15 V/10^{−9} A = **1.5 × 10^{10} Ω** (15 000 MΩ).
4. See step 3's derivation.
5. g_{m0} = 2 × 8/4 = **4 mS**; g_{m} = 4 × (1 − 1/4) = **3 mS**.
6. Any three: low-noise high-input-impedance amplifier, buffer, voltage-variable resistor, analog switch or chopper, constant-current source.

<!--/ANSWERS-->
