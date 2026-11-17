## slide 1

Common Emitter Connection

The common-emitter terminology is derived from the fact that the emitter is common to both the input and output sides of the configuration.

First Figure shows common emitter npn configuration and second figure shows common emitter pnp configuration.

- Circuit (i) [s001-image1.jpg]: Common emitter npn configuration showing npn transistor with input loop consisting of AC signal source labeled "SIGNAL" in series with DC battery V_BB (positive terminal to base, negative terminal to common emitter node) producing base current I_B directed into the base, emitter current I_E directed downward to common emitter node, and output loop with collector current I_C directed into collector through load resistor R_C (labeled with vertical double-headed dimension arrow "OUTPUT") in series with DC battery V_CC (positive terminal to R_C, negative terminal to common emitter node).
- Circuit (ii) [s001-image1.jpg]: Common emitter pnp configuration showing pnp transistor with input loop consisting of AC signal source labeled "SIGNAL" in series with DC battery V_BB (negative terminal to base, positive terminal to common emitter node) producing base current I_B directed out of the base, emitter current I_E directed upward into emitter from common emitter node, and output loop with collector current I_C directed out of collector through load resistor R_C (labeled with vertical double-headed dimension arrow "OUTPUT") in series with DC battery V_CC (negative terminal to R_C, positive terminal to common emitter node).

## slide 2

Common Emitter Connection

Base Current amplification factor (β) :

In common emitter connection input current is base current and output current is collector current.

The ratio of change in collector current to the change in base current is known as base current amplification factor, β.

β = ΔIC / ΔIB

Normally only 5% of emitter current flows to base, so amplification factor is greater than 20. Usually this range varies from 20 to 500.

Note: In raw slide text layout, the equation fraction was split across lines as `ΔIB` and `β = ΔIC`.

## slide 3

Relation Between β and α

Equations:
β = ΔIC / ΔIB
α = ΔIC / ΔIE
IE = IB + IC
ΔIE = ΔIB + ΔIC
ΔIB = ΔIE - ΔIC

β = ΔIC / (ΔIE - ΔIC)

β = (ΔIC / ΔIE) / ((ΔIE / ΔIE) - (ΔIC / ΔIE)) = α / (1 - α)

β = α / (1 - α)

## slide 4

Expression for Collector Current

Equations:
IC = α IE + ICBO
IE = IB + IC = IB + (α IE + ICBO)
IE (1 - α) = IB + ICBO
IE = IB / (1 - α) + ICBO / (1 - α)
IC ≃ [?] IE = *(β + 1) IB + (β + 1) ICBO

⚠ looks wrong: The slide heading is "Expression for Collector Current", but the algebraic derivation solves for emitter current IE = (β + 1) IB + (β + 1) ICBO and then equates IC ≃ IE, rather than solving directly for the exact common-emitter collector current IC = β IB + (β + 1) ICBO (or IC = β IB + ICEO). The derivation presented is identical to the common-collector current derivation seen on slide 11.

## slide 5

Characteristics of Common Emitter Configuration

Input Characteristics:
-> VBE vs IB characteristics is called input characteristics.
-> IB increases rapidly with VBE . It means input resistance is very small.
-> IE almost independent of VCE.
-> IB is of the range of micro amps.

⚠ looks wrong: Bullet point 3 states "IE almost independent of VCE" under input characteristics, whereas the input characteristic relates IB to VBE (or IB is relatively insensitive to VCE changes).

- Graph [s005-image6.jpg]: Input characteristics of common emitter configuration showing base current IB (μA) on the y-axis (calibrated from 0 to 100 μA in increments of 10 μA) versus base-emitter voltage VBE (V) on the x-axis (ticks at 0, 0.2, 0.4, 0.6, 0.8, 1.0 V), showing three exponential-like curves remaining near zero until knee voltage ~0.6 V and rising steeply thereafter, parameterized for VCE = 1 V (leftmost/steepest), VCE = 10 V (middle), and VCE = 20 V (rightmost).

## slide 6

Characteristics of Common Emitter Configuration

Output Characteristics:
VCE vs Ic characteristics is called output characteristics.
IC varies linearly with VCE ,only when VCE is very small.
As, VCE increases, IC becomes constant.

- Graph [s006-image7.jpg]: Output characteristics of common emitter configuration showing collector current IC (mA) on the y-axis (ticks 0 to 8 mA in steps of 1 mA) versus collector-emitter voltage VCE (V) on the x-axis (ticks 0, 5, 10, 15, 20 V), displaying curves for base current IB = 0 μA, 10 μA, 20 μA, 30 μA, 40 μA, 50 μA, 60 μA, 70 μA, 80 μA, and 90 μA, with regions marked: shaded "(Saturation region)" for VCE < VCEsat, "(Active region)" in the broad flat active region, shaded "(Cutoff region)" below the IB = 0 μA line, and an arrow indicating collector leakage offset ICEO ≃ β ICBO at the VCE axis.

## slide 7

Expression for Collector Current

Equations:
IC = α IE + ICBO
IE = IB + IC = IB + (α IE + ICBO)
IE (1 - α) = IB + ICBO
IE = IB / (1 - α) + ICBO / (1 - α)
IC ≃ [?] IE = *(β + 1) IB + (β + 1) ICBO

Side derivation for asterisk (*):
β = α / (1 - α)  ∴  β + 1 = α / (1 - α) + 1 = 1 / (1 - α)

⚠ looks wrong: Slide 7 repeats the derivation from slide 4 (which solves for IE and approximates IC ≃ IE) but additionally includes s007-image9.png showing the proof that β + 1 = 1 / (1 - α).

## slide 8

Common Collector Connection

- Circuit (i) [s008-image10.png]: Common collector npn configuration showing npn transistor with collector connected to common rail, input AC source labeled "SIGNAL" in series with DC battery (positive to base, negative to collector rail) connected to base, and emitter connected through load resistor labeled RC in series with DC battery (positive to RC, negative to collector rail), with vertical double-headed dimension arrow labeled "OUTPUT" across emitter and common rail. ⚠ looks wrong: load resistor in the emitter lead is labeled RC instead of RE.
- Circuit (ii) [s008-image10.png]: Common collector pnp configuration showing pnp transistor with collector connected to common rail, input AC source labeled "SIGNAL" in series with DC battery (negative to base, positive to collector rail) connected to base, and emitter connected through load resistor labeled RC in series with DC battery (negative to RC, positive to collector rail), with vertical double-headed dimension arrow labeled "OUTPUT" across emitter and common rail. ⚠ looks wrong: load resistor in the emitter lead is labeled RC instead of RE.

## slide 9

(i) Current amplification factor γ. In common collector circuit, input current is the base current IB and output current is the emitter current IE. Therefore, current amplification in this circuit arrangement can be defined as under :

The ratio of change in emitter current (ΔIE) to the change in base current (ΔIB) is known as current amplification factor in common collector (CC) arrangement i.e.

γ = ΔIE / ΔIB

This circuit provides about the same current gain as the common emitter circuit as ΔIE ≃ ΔIC.
However, its voltage gain is always less than 1.

Relation between γ and α

γ = ΔIE / ΔIB   ...(i)

α = ΔIC / ΔIE   ...(ii)

## slide 10

Now  IE = IB + IC
or  ΔIE = ΔIB + ΔIC
or  ΔIB = ΔIE - ΔIC

Substituting the value of ΔIB in exp. (i), we get,

γ = ΔIE / (ΔIE - ΔIC)

Dividing the numerator and denominator of R.H.S. by ΔIE, we get,

γ = (ΔIE / ΔIE) / ((ΔIE / ΔIE) - (ΔIC / ΔIE)) = 1 / (1 - α)    (∵ α = ΔIC / ΔIE)

∴  γ = 1 / (1 - α)

## slide 11

(ii) Expression for collector current

We know  IC = α IE + ICBO   ([clipped: equation number])
Also  IE = IB + IC = IB + (α IE + ICBO)
∴  IE (1 - α) = IB + ICBO
or  IE = IB / (1 - α) + ICBO / (1 - α)
or  IC ≃ IE = *(β + 1) IB + (β + 1) ICBO

⚠ looks wrong: The heading reads "(ii) Expression for collector current", but in common collector the output current is emitter current IE, and the derivation solves for IE = (β + 1) IB + (β + 1) ICBO before writing IC ≃ IE.

## slide 12

- Graph [s012-image15.png]: Input characteristics of common collector configuration showing base current IB (μA) on the y-axis (ticks at 0, 20, 40, 60, 80, 100 μA with dashed horizontal guideline at 100 μA) versus collector-base voltage VBC (V) on the x-axis (ticks at 0, 1, 2, 3, 4, 5 V), showing steep downward-sloping curves for VEC = 2V (reaching 0 at VBC ≃ 1.5 V) and VEC = 4V (reaching 0 at VBC ≃ 3.5 V).
- Graph [s012-image16.png]: Output characteristics of common collector configuration showing emitter current IE (mA) on the y-axis (ticks 0, 1, 2, 3, 4, 5, 6 mA) versus emitter-collector voltage VEC (V) on the x-axis (ticks 0, 1, 2, 3, 4, 5, 6 V), showing a family of curves for base current IB = 0 μA (flat at ~0.5 mA), IB = 20 μA (flat at ~1.4 mA), IB = 40 μA (flat at ~2.3 mA), IB = 60 μA (flat at ~3.3 mA), IB = 80 μA (flat at ~4.25 mA), and IB = 100 μA (flat at ~5.0 mA), each rising sharply from 0 to ~1 V and flattening out across the active operating region.

## slide 13

Comparison of Transistor Connection

| S. No. | Characteristic | Common base | Common emitter | Common collector |
| --- | --- | --- | --- | --- |
| 1. | Input resistance | Low (about 100 Ω) | Low (about 750 Ω) | Very high (about 750 kΩ) |
| 2. | Output resistance | Very high (about 450 kΩ) | High (about 45 kΩ) | Low (about 50 Ω) |
| 3. | Voltage gain | about 150 | about 500 | less than 1 |
| 4. | Applications | For high frequency applications | For audio frequency applications | For impedance matching |
| 5. | Current gain | No (less than 1) | High (β) | Appreciable |

## slide 14

Transistor Load line analysis

In transistor circuit analysis it is necessary to determine collector current for various VCE voltage.

One method is we can determine the collector current at any desired VCE voltage, from the output characteristics.

More conveniently we can use load line analysis to determine operating point.

## slide 15

Transistor Load line analysis

Consider common emitter npn transistor ckt shown in figure.
There is no input signal.
Apply KVL in the output ckt-

- Circuit [s015-image18.jpg]: DC circuit diagram for load line analysis showing npn transistor in common emitter connection with input terminals labeled "NO SIGNAL" connected in series with battery V_BB (positive to base) producing base current I_B into base, emitter current I_E directed downward to common rail, collector current I_C flowing into collector through load resistor R_C from DC supply battery V_CC (positive to R_C, negative to common rail), and collector-to-emitter voltage labeled V_CE across collector and emitter terminals.

Equations:
VCE = VCC - IC RC

(i) When the collector current IC = 0, then collector-emitter voltage is maximum and is equal to VCC i.e.
Max. VCE = VCC - IC RC
= VCC    (∵ IC = 0)

When collector-emitter voltage VCE = 0,
VCE = VCC - IC RC
0 = VCC - IC RC
Max. IC = VCC / RC

## slide 16

Transistor Load line analysis

- Graph [s016-image23.jpg]: DC load line plot showing collector current IC (mA) on the y-axis versus collector-emitter voltage VCE (VOLTS) on the x-axis with origin O, showing straight load line connecting point A (IC = VCC / RC on y-axis) and point B (VCE = VCC on x-axis), with operating point Q located on the line projecting to point C on the y-axis (IC) and point D on the x-axis (VCE).
- Graph [s016-image24.jpg]: DC load line and Q-point plot showing collector current IC on the y-axis versus collector-emitter voltage VCE on the x-axis with origin O, with straight load line connecting point A on the y-axis to point B on the x-axis intersecting an active-region transistor output curve for base current IB = 5μA at operating point Q, which projects to point D on the y-axis (IC) and point C on the x-axis (VCE).

## slide 17

Operating Point

The zero signal values of IC and VCE are known as the operating point.

It is called operating point because variation of IC takes place about this point.

It is also called quiescent point or Q-point.

- Graph [s017-image24.jpg]: DC load line and Q-point plot showing collector current IC on the y-axis versus collector-emitter voltage VCE on the x-axis with origin O, with straight load line connecting point A on the y-axis to point B on the x-axis intersecting an active-region transistor output curve for base current IB = 5μA at operating point Q, which projects to point D on the y-axis (IC) and point C on the x-axis (VCE).

---

## Done Report

- **File written**: `C:/Users/bhomi/AppData/Local/Temp/claude/6e81c002d1e3bfcd/bd6f37ef-47e2-42fc-83d1-906fe62e205d/scratchpad/edc-e0/out/ce.md`
- **Sections**: 17 slide sections (`## slide 1` through `## slide 17`)
- **Counts**:
  - Total slides transcribed: 17
  - Total image occurrences transcribed/described: 26 (from 25 distinct image files: `s001-image1.jpg` through `s017-image25.jpg`, with `s016-image24.jpg` / `s017-image24.jpg` appearing on both slide 16 and slide 17)
  - Circuit diagrams described: 5 circuits (Slide 1: CE npn and pnp; Slide 8: CC npn and pnp; Slide 15: CE npn DC bias circuit)
  - Graphs described: 6 graphs (Slide 5: CE input characteristics; Slide 6: CE output characteristics; Slide 12: CC input characteristics; Slide 12: CC output characteristics; Slide 16: DC load line intercepts; Slide 16 & 17: Q-point on load line with IB = 5μA curve)
  - Tables: 1 table (Slide 13: Comparison of Transistor Connection)
  - Worked examples / numerical questions: None present in slides 1–17
- **Unreadable items**: None (`[unreadable]` count: 0)
- **Clipped items**: 1 item on slide 11 (`[clipped: equation number]` at right cropped border of `s011-image14.png`)
- **Uncertain readings**:
  - Slide 4 & Slide 7: `IC ≃ [?] IE` where symbol in image is rendered with visual artifacts resembling a semicolon or broken tilde-equals.
- **Flagged issues (`⚠ looks wrong`)**:
  - Slide 4: `⚠ looks wrong: The slide heading is "Expression for Collector Current", but the algebraic derivation solves for emitter current IE = (β + 1) IB + (β + 1) ICBO and then equates IC ≃ IE, rather than solving directly for the exact common-emitter collector current IC = β IB + (β + 1) ICBO (or IC = β IB + ICEO). The derivation presented is identical to the common-collector current derivation seen on slide 11.`
  - Slide 5: `⚠ looks wrong: Bullet point 3 states "IE almost independent of VCE" under input characteristics, whereas the input characteristic relates IB to VBE (or IB is relatively insensitive to VCE changes).`
  - Slide 7: `⚠ looks wrong: Slide 7 repeats the derivation from slide 4 (which solves for IE and approximates IC ≃ IE) but additionally includes s007-image9.png showing the proof that β + 1 = 1 / (1 - α).`
  - Slide 8: `⚠ looks wrong: In both common collector circuit diagrams (i) and (ii), the load resistor in the emitter lead is labeled RC instead of RE.`
  - Slide 11: `⚠ looks wrong: The heading reads "(ii) Expression for collector current", but in common collector the output current is emitter current IE, and the derivation solves for IE = (β + 1) IB + (β + 1) ICBO before writing IC ≃ IE.`
