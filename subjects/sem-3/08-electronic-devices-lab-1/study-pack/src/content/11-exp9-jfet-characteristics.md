# Exp 9 · JFET drain and transfer characteristics, and device parameters

<div class="sub">Manual pp. 26–28 · LTspice · CO1, CO2 · theory: ECE2101 unit 3 · the simulation reproduces the manual's printed table exactly · the professor flagged these four parameters as an 8-mark question (classmate's report, 2026-10-05)</div>

[[map:9 JFET curves > 10 CS amplifier > 11 Oscillator > 12 MOSFET inverter|here=1]]

**What you already have:** from Exp 1, a reverse-biased pn junction carries no current and has a depletion region with no free carriers. From Exp 5, families of output curves and slopes taken as parameters.

**Three terms first:**

- **FET (field-effect transistor):** current flows through a **channel**, and a **voltage** on the gate controls the channel's width. It is *voltage-controlled*. A BJT, by contrast, is controlled by base current.
- **JFET terminals:** **drain** (D, current in), **source** (S, current out), **gate** (G, controls).
- **Unipolar:** only one carrier type carries the current (electrons, in an n-channel JFET). A BJT uses both electrons and holes, which is why it is called *bipolar*.

:::q <span class="tag">Manual Exp 9, aim · professor's slide</span>
To plot the drain and transfer characteristics of a JFET in CS configuration and determine the device parameters. Viva / 8-mark form: "Define g_{m}, r_{d}, g_{d} and μ, find each from the curves, and show μ = g_{m} r_{d}."
:::

:::guess Guess first
Which of the four do you think is read from the *transfer* curve, and which from the *drain* curves?
:::

## How a JFET works

[[fig:jfet_structure|n-channel JFET: an n bar between two p gate regions. The gate–channel junctions are kept reverse-biased (V_{GS} ≤ 0).|w=45]]

1. **V_{GS} = 0:** the channel is fully open, and current flows from D to S.
2. **V_{GS} more negative:** the reverse-biased gate junctions' depletion regions widen into the channel, so the channel narrows and I_{D} falls.
3. **V_{GS} = V_{P}** (pinch-off voltage, ≈ −3 V here): the depletion regions meet and I_{D} ≈ 0. The JFET is off.
4. **Raising V_{DS}** at fixed V_{GS}: at first I_{D} rises like a resistor (**ohmic region**). Then the channel pinches off near the drain and I_{D} levels out (**saturation**, or pinch-off region). The amplifier operates here.
5. The gate junction is reverse-biased, so **gate current ≈ 0**: the input resistance is enormous (≫ MΩ). This is the JFET's big advantage.

**Shockley's equation** (the transfer curve, in saturation):

$$I_{D} = I_{DSS} (1 − \frac{V_{GS}}{V_{P}})^{2}$$

- I_{DSS} = drain current with the gate **S**horted to the **S**ource (V_{GS} = 0), in saturation.

## The four parameters (the professor's slide)

| Parameter | Definition | Held constant | Read from |
|---|---|---|---|
| transconductance g_{m} | ΔI_{D}/ΔV_{GS} | V_{DS} | two drain curves at one V_{DS} (or the transfer curve's slope) |
| drain resistance r_{d} | ΔV_{DS}/ΔI_{D} | V_{GS} | one drain curve, in saturation |
| drain conductance g_{d} | ΔI_{D}/ΔV_{DS} = 1/r_{d} | V_{GS} | same |
| amplification factor μ | −ΔV_{DS}/ΔV_{GS} | I_{D} | **μ = g_{m} × r_{d}** |

**Why μ = g_{m}r_{d}:** μ asks how much V_{DS} change balances a V_{GS} change at constant I_{D}. Write it as a chain of ratios: (ΔV_{DS}/ΔI_{D}) × (ΔI_{D}/ΔV_{GS}) = r_{d} × g_{m}. The minus sign records that a more negative V_{GS} must be balanced by a larger V_{DS}.

## Do it

[[fig:exp09_circuit|Fig 9.2, redrawn: V_{gs} on the gate, V_{ds} on the drain, source grounded.|w=60]]

:::do Do it (LTspice)
1. Draw the circuit with J1: Pick New JFET → **2N3819** (an n-channel JFET, `njf`). Name the sources `Vgs` and `Vds`.
2. **Drain characteristics:** `.dc Vds 0 16 0.1 Vgs 0 -3 -1`. This gives four curves, for V_{GS} = 0, −1, −2, −3 V. Plot **Id(J1)**.
3. **Transfer characteristic:** set Vds = 8 V, then `.dc Vgs -5 0 0.01`. Plot Id(J1) against V_{gs}.
4. Read I_{DSS} (cursor at V_{GS} = 0) and V_{P} (where I_{D} reaches ≈ 0).
:::

## What you should see

[[fig:exp09_out|Drain characteristics: ohmic rise, pinch-off, then flat saturation. Each curve flattens at V_{DS} ≈ V_{GS} − V_{P}.|w=86]]

| V_{DS} (V) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| I_{D} (mA), V_{GS} = 0 | 0 | 6.45 | 10.37 | 11.72 | **11.75** | 11.77 | **11.80** | **11.83** | 11.85 |
| I_{D} (mA), V_{GS} = −1 | 0 | 3.89 | 5.21 | 5.22 | **5.24** | 5.25 | 5.26 | 5.27 | 5.28 |
| I_{D} (mA), V_{GS} = −2 | 0 | 1.30 | 1.31 | 1.31 | 1.31 | 1.32 | 1.32 | 1.32 | 1.32 |
| I_{D} (mA), V_{GS} = −3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

These are the manual's printed numbers (it lists them in amps: 0.01185 A = 11.85 mA).

[[fig:exp09_tr|Transfer characteristic at V_{DS} = 8 V, with Shockley's equation (dots) laid on top: a near-perfect match.|w=75]]

## Calculations

- **I_{DSS} = 11.85 mA** (V_{GS} = 0, V_{DS} = 8 V).
- **V_{P} ≈ −3 V** (I_{D} reaches 0 at V_{GS} = −3 V).

$$g_{m} = \frac{ΔI_{D}}{ΔV_{GS}} = \frac{11.75 − 5.24 mA}{0 − (−1) V} = 6.51 mA/V (= 6.51 mS)    at V_{DS} = 4 V$$

$$r_{d} = \frac{ΔV_{DS}}{ΔI_{D}} = \frac{8 − 3 V}{11.852 − 11.722 mA} = \frac{5 V}{0.130 mA} = 38.5 kΩ    at V_{GS} = 0$$

$$g_{d} = \frac{1}{r_{d}} = 26 µS          μ = g_{m} r_{d} = 6.51 mS × 38.5 kΩ ≈ 250$$

**Cross-check with Shockley:**

- The slope at V_{GS} = 0 is g_{m0} = 2I_{DSS}/|V_{P}| = 2 × 11.85/3 = 7.9 mS.
- The 0 → −1 V chord equals the slope at the midpoint, V_{GS} = −0.5 V: g_{m} = g_{m0}(1 − 0.5/3) = 6.6 mS ✓ (6.51 measured).

:::trap Trap: the manual's r_{d} line
It writes (7 − 6)/(0.1183 − 0.1180) = 3.3 kΩ. The currents are 0.01183 A and 0.01180 A, so the difference is 0.03 mA, and r_{d} = 1 V / 0.03 mA = **33 kΩ**. Also, a 1 V span with 4-digit data is coarse: use a wide V_{DS} span (3 → 8 V) inside saturation, which gives 38.5 kΩ.
:::

:::write Write in your record
**Result:** I_{DSS} = **11.85 mA**, V_{P} = **−3 V**, g_{m} = **6.51 mS** (V_{DS} = 4 V), r_{d} = **38.5 kΩ** (V_{GS} = 0); also g_{d} = 26 µS and μ = g_{m}r_{d} ≈ 250.

**Theory for the record:** an n-channel JFET is an n-type channel between two p-type gate regions. With the gate–source junction reverse-biased, the depletion regions narrow the channel as V_{GS} becomes more negative, so the gate voltage controls the drain current. Gate current is negligible, giving very high input resistance. As V_{DS} increases, I_{D} first rises linearly (ohmic region), then the channel pinches off and I_{D} saturates. At V_{GS} = V_{P} the channel is cut off. In saturation, I_{D} = I_{DSS}(1 − V_{GS}/V_{P})² (Shockley). Parameters: g_{m} = ΔI_{D}/ΔV_{GS} at constant V_{DS}; r_{d} = ΔV_{DS}/ΔI_{D} at constant V_{GS}; μ = g_{m}r_{d}.
:::

:::check Check 1
(a) Use Shockley to predict I_{D} at V_{GS} = −2 V, and compare with the table. (b) Why is a JFET's gate never forward-biased in normal use? (c) BJT vs JFET: give two differences an examiner would accept.
:::

<!--ANSWERS-->

## Answers

**Opening question.** g_{m} from the **transfer** curve (or two drain curves at one V_{DS}); r_{d} and g_{d} from **one drain curve** in saturation; μ from g_{m} × r_{d}.

**Check 1.** (a) 11.85 × (1 − 2/3)² = 11.85/9 = **1.32 mA**; the table gives 1.31–1.32 ✓. (b) Forward bias would make the gate junction conduct. The gate would draw current, the high input resistance would be lost, and the device could be damaged. (c) Any two: a JFET is voltage-controlled, a BJT current-controlled; a JFET is unipolar, a BJT bipolar; a JFET has very high input resistance, a BJT moderate (h_{ie} ≈ kΩ); a JFET is less noisy and more thermally stable; a BJT has higher gain (g_{m}).

<!--/ANSWERS-->
