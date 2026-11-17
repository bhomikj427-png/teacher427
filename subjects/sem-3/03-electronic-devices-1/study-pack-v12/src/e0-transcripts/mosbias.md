## slide 1

Mosfet biasing and digital circuit

## slide 2

MOSFETs as Switches

- MOSFET: Metal-Oxide-Semiconductor Field-Effect Transistor
  - n-channel MOSFET = nFET = NMOS
  - p-channel MOSFET = pFET = PMOS
  - Complementary MOS: CMOS

- Symbols

Circuit diagram:
- Circuit: Switch equivalent models of MOSFETs showing nFET symbol with gate V_G, drain V_D, source V_S equated (=) to an open switch labeled (V_D >= V_S), and pFET symbol with inverting bubble at gate V_G, drain V_D, source V_S equated (=) to a switch with bubble on contact arm labeled (V_S >= V_D).

## slide 3

MOSFETs as Switches

- Threshold voltage
  - nFET: V_Tn > 0
  - pFET: V_Tp < 0

- nFET
  - OFF: V_GSn <= V_Tn
  - ON: V_GSn > V_Tn

Circuit / graph:
- Circuit and logic translation graph: nFET Mn with Drain, Source connected to ground, Gate at V_A; logic translation axis for input V_A from 0 to V_DD shows range 0 to V_Tn corresponds to "A = 0: Mn OFF" and V_Tn to V_DD corresponds to "A = 1: Mn ON".

- pFET
  - OFF: V_SGp <= |V_Tp|
  - ON: V_SGp > |V_Tp|

Circuit / graph:
- Circuit and logic translation graph: pFET Mp with Source connected to V_DD, Drain at bottom, Gate at V_A with bubble; logic translation axis for input V_A from 0 to V_DD shows range 0 to V_DD - |V_Tp| corresponds to "A = 0: Mp ON" and V_DD - |V_Tp| to V_DD corresponds to "A = 1: Mp OFF".

## slide 4

Pass Characteristics

- nFET
  - Strong logic 0 transfer
  - Weak logic 1 transfer

- pFET
  - Strong logic 1 transfer
  - Weak logic 0 transfer

- CMOS
  - Use pFETs to pass logic 1.
  - Use nFETs to pass logic 0.

## slide 5

Basic Logic Gates in CMOS

- Principles
  - Construct the nFET network using only nFETs and the pFET network using only pFETs.
  - If the output is 1, the pFET network connects V_DD to the output and the nFET network disconnects V_SS and the output.
  - If the output is 0, the nFET network connects V_SS to the output and the pFET network disconnects V_DD and the output.

Circuit diagram:
- Circuit: Generalized CMOS gate block diagram with top supply V_DD connected to "pFET network" box, bottom ground (V_SS) connected to "nFET network" box, shared input bus "a, b, c, ... (inputs)", and common output terminal f (output).

## slide 6

Basic Logic Gates in CMOS

- Inverter

Circuit diagram:
- Circuit: CMOS inverter circuit with input x driving connected gates of top pFET (source to V_DD) and bottom nFET (source to ground), with output taken between drains as f = \bar{x}.

Stats:
# TRs: 2
nFET: 1
pFET: 1

Operation:
- Left circuit: input 0 applied to gate of pFET (ON, connected to V_DD) and nFET labeled "off", giving f = 1.
- Right circuit: input 1 applied to gate of nFET (ON, connected to ground) and pFET labeled "off", giving f = 0.

Equation:
f = \bar{x} · 1 + x · 0 = \bar{x}

## slide 7

Basic Logic Gates in CMOS

- Two-input NAND (NAND2)

Circuit diagram:
- Circuit: Two-input CMOS NAND gate circuit with two parallel pFETs between V_DD and output node f = \overline{a · b}, and two series nFETs between output node and ground, driven by inputs a and b.

Stats:
# TRs: 4
nFETs: 2
pFETs: 2

Operation:
- Left circuit: inputs a = 0, b = 0; both pFETs ON to V_DD, both nFETs labeled off; f = 1.
- Middle circuit: inputs a = 0, b = 1; left pFET ON, right pFET labeled off, top nFET labeled off, bottom nFET ON; f = 1.
- Right circuit: inputs a = 1, b = 1; both pFETs labeled off, both series nFETs ON to ground; f = 0.

Equation:
f = \bar{a} · \bar{b} · 1 + \bar{a} · b · 1 + a · \bar{b} · 1 + a · b · 0 = \bar{a} + \bar{b} = \overline{a · b}

## slide 8

Basic Logic Gates in CMOS

- Two-input NOR (NOR2)

Circuit diagram:
- Circuit: Two-input CMOS NOR gate circuit with two series pFETs (gates b and a) between V_DD and output node f = \overline{a + b}, and two parallel nFETs (gates a and b) between output node and ground.

Stats:
# TRs: 4
nFETs: 2
pFETs: 2

Operation:
- Left circuit: inputs a = 0, b = 0; both series pFETs ON to V_DD, both parallel nFETs labeled off; f = 1.
- Middle circuit: inputs b = 1, a = 0; top pFET off (gate 1), bottom pFET labeled off (gate 0), left nFET labeled off (gate 0), right nFET ON to ground (gate 1); f = 0.
- Right circuit: inputs b = 1, a = 1; both series pFETs labeled off, both parallel nFETs ON to ground; f = 0.

Equation:
f = \bar{a} · \bar{b} · 1 + \bar{a} · b · 0 + a · \bar{b} · 0 + a · b · 0 = \bar{a} · \bar{b} = \overline{a + b}

## slide 9

Complex Logic Gates in CMOS

- Example

f = \overline{a · (b + c)}

Circuit diagram:
- Circuit: Complex CMOS gate implementation of f = \overline{a · (b + c)} with pull-up network of pFET a in parallel with series pair of pFETs b and c connected to V_DD, and pull-down network of nFET a in series with parallel pair of nFETs b and c connected to ground, with output f.

Stats:
# TRs: 6
nFETs: 3
pFETs: 3

## slide 10

Gate Bias Circuit

The gate voltage in the gate bias circuit is fixed by an external voltage source. There is no voltage drop across the gate resistor in a MOSFET since the gate current is zero (I_G = 0). As a result, the applied bias voltage equals the gate voltage.

MOSFET Biasing

Circuit diagram:
- Circuit: Gate bias circuit with n-channel MOSFET having gate G connected via resistor R_G to DC voltage supply V_GG to ground with I_G = 0, drain D connected via resistor R_D to supply V_DD, and source S connected to ground, with drain-to-source voltage marked + V_DS -.

Given that the source is typically grounded:
V_G = V_GS

KVL application in the drain circuit:
V_DS = V_DD - I_D * R_D

In order to properly bias in the saturation region:
V_DS >= (V_GS - V_TN), V_GS >= V_TN

The MOSFET can be biased in the desired region by choosing the right gate voltage and drain resistance settings.

## slide 11

Drain-to-Gate Bias Circuit Configuration

A separate gate supply is not required thanks to the drain-to-gate bias circuit. Here, automatic biasing is achieved by connecting the gate to the drain via a resistor.

Circuit diagram:
- Circuit: Drain-to-gate feedback bias circuit with n-channel MOSFET having drain D connected via resistor R_D to V_DD, source S connected directly to ground, and gate G connected back to drain D through resistor R_G.

There is no voltage drop across the gate resistor since I_G = 0. Hence:
V_G = V_D

Therefore:
V_DS = V_GS

KVL application in the circuit:
V_DS = V_DD - I_D * R_D

DC Analysis
In this setup:
- Voltage across R_G = 0
- Gate current I_G = 0
- V_G = V_D
- V_GS = V_DS

The MOSFET functioning is naturally stabilized by this biasing technique, which usually maintains it in the saturation area.

## slide 12

Voltage Divider Bias Circuit

The gate voltage in this circuit is set using a voltage divider network (R_1 and R_2), which improves control and stability over earlier techniques.

Circuit diagram:
- Circuit: Voltage divider bias circuit with n-channel MOSFET where supply V_DD feeds divider resistors R_1 and R_2 to ground to set gate voltage V_G with I_G = 0, drain D connects to V_DD via resistor R_D with current I_DS, source S connects to ground via resistor R_S with voltage V_S, gate-to-source voltage is + V_GS -, and drain-to-source voltage is + V_DS -.

Given that I_G = 0, the gate voltage is determined by:
V_G = ( R_2 / (R_1 + R_2) ) V_DD

Source voltage:
V_S = I_D * R_S

Thus:
V_GS = V_G - V_S

KVL application in the drain circuit:
V_DS = V_DD - I_D(R_D + R_S)

In order to function properly in the saturation region:
V_DS >= (V_GS - V_TN), V_GS >= V_TN

This technique is frequently utilized in real-world circuits and offers good bias stability.

## slide 13

TO FIND V_DS
Apply KVL to output loop between D-S,

V_DD = I_D * R_D + V_DS + I_D * R_S

Rearrange the above equation to get V_DS

V_DS = V_DD - I_D * R_D - I_D * R_S

V_DSQ = V_DS = V_DD - I_D (R_D + R_S)

Circuit diagram:
- Circuit: Voltage divider bias circuit with n-channel MOSFET showing supply V, divider resistors R_1 and R_2 to ground setting gate voltage V_G, drain resistor R_D carrying current I_D, source resistor R_S to ground, voltages + V_GS - and + V_DS -, and a red vertical downward arrow on the right marking KVL loop traversal across D-S.

## slide 14

TO FIND V_GS
Using voltage divider rule gate voltage can be writter as ⚠ looks wrong: "writter" in original slide, should be "written"

V_G = (R_1 / (R_1 + R_2)) * V_DS ⚠ looks wrong: original slide gives formula with R_1 instead of R_2 and V_DS instead of V_DD (or V)

Apply KVL to the input circuit,

V_G = V_GS + I_S * R_S

V_G = V_GS + I_D * R_S (∵ I_D = I_S)

V_GS Q = V_GS = V_G - I_D * R_S

TO FIND I_D
The drain current ID is given by

I_DQ = I_D = K_n(V_GS - V_TN)^2

Circuit diagram:
- Circuit: Voltage divider bias circuit with n-channel MOSFET showing supply V, divider resistors R_1 and R_2 to ground, drain resistor R_D with current I_D, source resistor R_S to ground, voltages + V_GS - and + V_DS -, and a red right-angle path with arrow entering gate and traveling down through R_S to ground marking input KVL loop.

## slide 15

Self-Bias Circuit Configuration

The source resistor in the self-bias circuit is used to bias the gate, which is coupled to ground via a resistor.

Circuit diagram:
- Circuit: Self-bias circuit with n-channel MOSFET having gate G connected to ground via resistor R_G at voltage V_G, drain D connected to V_DD via resistor R_D, source S connected to ground via resistor R_S, with gate-to-source voltage marked + V_GS -.

Given that I_G = 0:

V_G = 0

KVL application from gate to source:

V_GS = - I_D * R_S

DC Analysis

From the relationship mentioned above:

I_D = - V_GS / R_S

This demonstrates that in this configuration, V_GS is negative.

- Negative V_GS for an enhancement MOSFET indicates no channel creation and the device stays off.

- Therefore, self-bias is inappropriate for MOSFET enhancement.

- The channel for the Depletion MOSFET is already present, thus the device can function correctly.

## slide 16

DC LOAD LINE AND Q POINT

V_DS = V_DD - I_D * R_D ---- (1)

To find point A
Sub V_DS = 0 in (1)
V_DD = I_D * R_D
I_D = V_DD / R_D
Pt. A = (0, V_DD / R_D)

To find point B
Sub I_D = 0 in (1)
V_DS = V_DD
Pt. B = (V_DD, 0)

Graph diagram:
- Graph: DC load line and Q-point plot on MOSFET drain characteristics (I_D vs V_DS). The horizontal axis is V_DS and vertical axis is I_D; family of parametric curves for increasing V_GS shows linear and saturation regions. A downward-sloping linear DC load line connects Pt. A = (0, V_DD / R_D) on the vertical axis to Pt. B = (V_DD, 0) on the horizontal axis; its intersection with a V_GS curve defines operating point Q at coordinates (V_DSQ, I_DQ).

---

## Done report
- **Files written**: `C:/Users/bhomi/AppData/Local/Temp/claude/6e81c002d1e3bfcd/bd6f37ef-47e2-42fc-83d1-906fe62e205d/scratchpad/edc-e0/out/mosbias.md`
- **Sections transcribed**: Slides 1 through 16 (16 sections titled `## slide 1` to `## slide 16`).
- **Counts**:
  - Total slides transcribed: 16
  - Circuit and graph descriptions: 15 diagrams/graphs across 12 slides.
  - Worked derivation steps and formulas: transcribed across slides 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16.
- **Unreadable items**: None (`0` unreadable).
- **Uncertain readings `[?]`**: None (`0` occurrences of `[?]`).
- **Anomalies flagged (`⚠ looks wrong`)**:
  - Slide 14: Typo in original slide text: `"writter"` instead of `"written"`.
  - Slide 14: Formula error in original slide: `V_G = \frac{R_1}{R_1 + R_2} V_{DS}` (uses resistor `R_1` instead of `R_2`, and `V_{DS}` instead of `V_{DD}` or `V`).
