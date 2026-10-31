# Exp 5 · BJT input/output characteristics (CE) and h-parameters

<div class="sub">Manual pp. 17–19 · LTspice / Virtual Lab · CO1, CO2 · theory: ECE2101 unit 5 (BJTs)</div>

[[map:5 BJT curves > 6 CE amplifier > 7 Emitter follower > 8 Feedback|here=1]]

**What you already have:** a diode is one pn junction (Exp 1). It conducts forward above ≈ 0.7 V.

**Three terms first:**

- **BJT (bipolar junction transistor):** three layers, **n-p-n** for an NPN. The layers are the **emitter** (E, heavily doped), the **base** (B, very thin, lightly doped) and the **collector** (C). That makes two junctions: base–emitter (BE) and base–collector (BC).
- **Common emitter (CE):** the emitter is shared by the input (B–E) and the output (C–E).
- **h-parameters:** four numbers that describe how the transistor responds to small changes. Exp 6–8 amplifiers are built on them.

:::q <span class="tag">Manual Exp 5, aim</span>
To plot the input and output characteristics of an NPN transistor in CE configuration and determine h-parameters from the characteristics. Viva form: "Your output curves are flat lines spaced 5.5 mA apart for 20 µA steps of base current. What is h_{fe}, and what does a flat line tell you?"
:::

:::guess Guess first
Commit to a number for h_{fe}, and to a one-word meaning of "flat", before reading on.
:::

## The BJT in five lines

1. Forward-bias the BE junction (V_{BE} ≈ 0.6–0.7 V). The emitter injects electrons into the base.
2. The base is thin, so almost all of them cross it and are swept into the collector by the reverse-biased BC junction. A few recombine in the base: that is the base current.
3. So a **small base current controls a large collector current**: I_{C} = β I_{B}, with β ≈ 100–300 (≈ 290 for the BC547B).
4. KCL: **I_{E} = I_{B} + I_{C}**.
5. Which region the transistor is in depends on how the two junctions are biased:

| Region | BE junction | BC junction | Behaviour | Used as |
|---|---|---|---|---|
| **Active** | forward | reverse | I_{C} = βI_{B}, nearly independent of V_{CE} | amplifier (Exps 6–8, 11) |
| **Saturation** | forward | forward | V_{CE} ≈ 0.2 V, I_{C} < βI_{B} | closed switch |
| **Cut-off** | reverse | reverse | I_{C} ≈ 0 | open switch |

## The two families of curves

- **Input characteristic:** I_{B} against V_{BE}, at fixed V_{CE}. It is just the BE diode's forward curve.
- **Output characteristic:** I_{C} against V_{CE}, at fixed I_{B}. One curve per I_{B}.

**h-parameters** in CE form (small changes, written in lowercase):

$$v_{be} = h_{ie} i_{b} + h_{re} v_{ce}          i_{c} = h_{fe} i_{b} + h_{oe} v_{ce}$$

| Parameter | Name | Read from | Formula |
|---|---|---|---|
| h_{ie} (= h_{11}) | input resistance | input curve, V_{CE} fixed | ΔV_{BE}/ΔI_{B} |
| h_{re} (= h_{12}) | reverse voltage gain | input curves, I_{B} fixed | ΔV_{BE}/ΔV_{CE} |
| h_{fe} (= h_{21}) | forward current gain | output curves, V_{CE} fixed | ΔI_{C}/ΔI_{B} |
| h_{oe} (= h_{22}) | output admittance | one output curve, I_{B} fixed | ΔI_{C}/ΔV_{CE} |

The manual swaps the names for h_{21} and h_{22}, and writes "1/h_{oe} = ΔI_{C}/ΔV_{CE}". The table above is the correct version. ΔI/ΔV is a conductance, so h_{oe} is in siemens and 1/h_{oe} is the output resistance.

## The circuit, and one fix

[[fig:exp05_circuit|Fig 5.1 as printed: V_{be} through 2 kΩ to the base; V_{ce} through 62 kΩ to the collector.|w=70]]

:::trap Trap: the 62 kΩ makes the manual's table impossible
With 62 kΩ in the collector, I_{C} ≤ 10 V / 62 kΩ = **0.16 mA**. The transistor saturates as soon as I_{B} passes about 0.6 µA, so "V_{CE}" is no longer the 10 V you set, and the I_{B} = 20/40 µA curves of the observation table can never appear. That is why the manual's own output plot only reaches about 210 µA. The fix: **replace R2 with a wire** so V_{ce} sits directly on the collector, and drive the base with a **current source** for the output curves. The device and the directives stay the same.
:::

:::do Do it (LTspice)
**Input characteristics:**

1. Draw Fig 5.1 with R2 replaced by a wire. Q1: Pick New Transistor → **BC547B**. Label the base node `base`.
2. Directive: `.dc Vbe 0 1 0.001 Vce 0 5 5` (V_{CE} = 0 V and 5 V, as the observation table asks).
3. Run, click the base lead to plot **Ib(Q1)**, then right-click the x-axis and set it to **V(base)**.

**Output characteristics:**

1. Replace V_{be} and R1 with a **current source** `Ib` (arrow pointing **into** the base).
2. Directive: `.dc Vce 0 12 0.05 Ib 0 60u 20u` (I_{B} = 0, 20, 40, 60 µA).
3. Plot **Ic(Q1)** against V_{ce}.

**h_{re}:** set Ib = `20u`, run `.op` at V_{ce} = 2 V and at 10 V, and read V(base) both times.
:::

## What you should see

[[fig:exp05_in_plot|Input characteristic: a diode curve. Raising V_{CE} shifts it right (at V_{CE} = 0 the BC junction is also forward and adds base current).|w=78]]

[[fig:exp05_out_plot|Output characteristics: saturation hugging the left edge, the active region (nearly flat), and cut-off at I_{B} = 0.|w=88]]

| V_{CE} (V) | 0.5 | 1 | 2 | 4 | 6 | 8 | 10 | 12 |
|---|---|---|---|---|---|---|---|---|
| I_{C} (mA), I_{B} = 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| I_{C} (mA), I_{B} = 20 µA | 5.46 | 5.50 | 5.59 | **5.77** | 5.95 | 6.13 | **6.30** | 6.48 |
| I_{C} (mA), I_{B} = 40 µA | 10.53 | 10.61 | 10.78 | 11.13 | 11.47 | 11.81 | 12.16 | 12.50 |
| I_{C} (mA), I_{B} = 60 µA | 15.27 | 15.40 | 15.65 | 16.15 | 16.65 | 17.14 | 17.64 | 18.14 |

Input, V_{CE} = 5 V: V_{BE} = 0.60 V → 0.81 µA; 0.62 → 1.73; 0.64 → 3.68; 0.66 → 7.73; 0.68 → 15.9; 0.70 → 31.6 µA. At V_{CE} = 0 V: 0.50 V → 1.07 µA; 0.55 → 6.55; 0.60 → 41.2 µA.

## Calculations (from the curves above)

$$h_{ie} = \frac{ΔV_{BE}}{ΔI_{B}} = \frac{0.6984 − 0.6670}{30 − 10 µA} = \frac{31.4 mV}{20 µA} = 1.57 kΩ    (V_{CE} = 5 V)$$

$$h_{fe} = \frac{ΔI_{C}}{ΔI_{B}} = \frac{11.30 − 5.86 mA}{40 − 20 µA} = \frac{5.44 mA}{20 µA} = 272    (V_{CE} = 5 V)$$

$$h_{oe} = \frac{ΔI_{C}}{ΔV_{CE}} = \frac{6.30 − 5.77 mA}{10 − 4 V} = \frac{0.533 mA}{6 V} = 89 µS    (I_{B} = 20 µA; 1/h_{oe} = 11.2 kΩ)$$

$$h_{re} = \frac{ΔV_{BE}}{ΔV_{CE}} = \frac{0.68671 − 0.68638}{10 − 2} = \frac{0.33 mV}{8 V} = 4.2 × 10^{−5}    (I_{B} = 20 µA)$$

**Sense check:** h_{re} is tiny (the output barely affects the input), and h_{oe} is small (the flat lines tilt only slightly). That is why simple amplifier analysis often drops both.

:::write Write in your record
**Result (BC547B, CE):** h_{ie} ≈ **1.57 kΩ**, h_{re} ≈ **4.2 × 10⁻⁵**, h_{oe} ≈ **89 µS**, h_{fe} ≈ **272**. State the operating point used: V_{CE} = 5 V, I_{B} ≈ 20 µA.

**Theory for the record:** a BJT has emitter, base and collector regions forming two junctions. For amplification the BE junction is forward-biased and the BC junction reverse-biased (active region): carriers injected from the emitter cross the thin base and reach the collector, so I_{C} = βI_{B} and I_{E} = I_{B} + I_{C}. In CE configuration, the input characteristic (I_{B} vs V_{BE} at constant V_{CE}) resembles a forward diode curve. The output characteristics (I_{C} vs V_{CE} at constant I_{B}) show saturation, active and cut-off regions. The h-parameters h_{ie}, h_{re}, h_{fe}, h_{oe} are the slopes of these curves at the operating point and form the small-signal model.
:::

:::check Check 1
(a) Using the table, find h_{fe} at V_{CE} = 10 V between I_{B} = 40 and 60 µA. (b) Why is the output curve for I_{B} = 0 flat at zero? (c) Which region is the transistor in at V_{CE} = 0.1 V and I_{B} = 40 µA, and how can you tell?
:::

<!--ANSWERS-->

## Answers

**Opening question.** h_{fe} = 5.5 mA / 20 µA ≈ **275**. "Flat" means **I_{C} does not depend on V_{CE}**: the transistor acts as a current source controlled by I_{B}. That is the active region, and the slight tilt is h_{oe}.

**Check 1.** (a) (17.64 − 12.16) mA / 20 µA = 5.48 mA / 20 µA = **274**. (b) With no base current, the BE junction isn't injecting carriers, so the transistor is cut off and only a leakage current (nA) flows. (c) **Saturation.** V_{CE} is below about 0.2–0.3 V, the steep left-hand part of the curve, where I_{C} is less than βI_{B} and depends strongly on V_{CE}.

<!--/ANSWERS-->
