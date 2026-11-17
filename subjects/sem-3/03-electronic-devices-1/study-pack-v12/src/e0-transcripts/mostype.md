# MOSFET Types and Characteristics

## slide 1

MOSFET
Metal Oxide Semiconductor Field Effect Transistor

Circuit/component description: TO-220 package power MOSFET photograph with 3 pins and mounting tab labeled: pin 1 GATE (purple lead), pin 2 DRAIN (green lead, connected to metal tab), pin 3 SOURCE (magenta lead).

## slide 2

Introduction
MOSFETs are most common type of Field Effect Transistor
MOSFETs are used in switching or amplifying electronic signals
MOSFETs are voltage-controlled device
MOSFETs are three terminal device with Source (S), Drain (D) and Gate (G) terminals.
MOSFETs have very high switching speed
There are 2 classes of MOFETS : Enhancement and Depletion type
These 2 classes are further divided as N-channel and P-channel

## slide 3

A metal–oxide–semiconductor field-effect transistor (MOSFET, MOS-FET, or MOS FET) is a field-effect transistor where the voltage determines the conductivity of the device.
The ability to change conductivity with the amount of applied voltage can be used for amplifying or switching electronic signals.
MOSFETs are now even more common than BJTs (bipolar junction transistors) in digital and analog circuits.
MOSFETs
3

Diagram description: Cross-section schematic labeled "MOSFET Structure" showing a p-type substrate, two n regions with Source (S) and Drain (D) metal contacts, and a Gate (G) metal contact over a dielectric oxide layer.

## slide 4

n-channel
Enhancement Mode
(nMOSFET)
p-channel
Enhancement Mode
(pMOSFET)
n-channel
Depletion Mode
(nMOSFET)
p-channel
Depletion Mode
(pMOSFET)
FET
4

## slide 5

Types of MOSFET

Diagram description: Circuit symbols for four MOSFET types: Enhancement Mode N-Channel (broken line channel, substrate arrow pointing inward, terminals Drain (D), Source (S), Gate (G), Substrate tied with dashed line to Source), Enhancement Mode P-Channel (broken line channel, substrate arrow pointing outward, terminals D, S, G, Substrate tied with dashed line to Source), Depletion Mode N-Channel (continuous solid line channel, substrate arrow pointing inward, terminals D, S, G, Substrate tied with dashed line to Source), and Depletion Mode P-Channel (continuous solid line channel, substrate arrow pointing outward, terminals D, S, G, Substrate tied with dashed line to Source).

## slide 6

MOSFET : Structure
6
Typically L = 0.03 μm to 1 μm, W = 0.05 μm to 100 μm, and the thickness of the oxide layer (tox) is in the range of 1 to 10 nm.
perspective view;
Cross section.

Diagram description (perspective view, s006-image5.png): Perspective 3D view of an n-channel enhancement MOSFET on a p-type substrate (Body, B) showing Source region (n+) with terminal S, Drain region (n+) with terminal D, Gate terminal G over Metal layer, Oxide (SiO2) layer, channel width W, and channel length L.
Diagram description (cross section, s006-image6.png): Cross-section view of an n-channel enhancement MOSFET showing Source (S) and Drain (D) metal contacts over n+ wells separated by channel length L in a p-type substrate (Body, B), with Gate (G) over Metal layer and Oxide (SiO2) layer of thickness tox.

## slide 7

N-channel Enhancement MOSFET

Diagram description: Cross-section diagram of an N-channel Enhancement MOSFET showing a p substrate ("substrate", p), two n-doped wells ("n-doped region", n) with "No channel" between them, a "Silicon di Oxide Insulation" layer, "Metal contacts", Drain (D) terminal, Gate (G) terminal, Source (S) terminal, and "Source Substrate (SS)" terminal.

## slide 8

N-channel Enhancement MOSFET
It has P-type semiconductor material as body/substrate
Two N-type wells are diffused on the body/substrate
Two PN junctions are formed creating 2 depletion regions
A metal contact is created at the bottom and a terminal is taken out known as body/ substrate terminal
Same metal contacts are created on the top of N-type making source and drain terminals
There is a layer of Silicon Dioxide in between the 2 N-type well which act as a dielectric
A metal contact is created on the top of SiO2 layer and a terminal is taken out called Gate
Generally Source and body terminal are internally connected and is grounded

## slide 9

Operation with Zero Gate Voltage:
With zero voltage applied to the gate, two back-to-back diodes exist in series between drain and source.
n+ drain region and the p-type substrate,
p-type substrate and the n+ source region.
These back-to-back diodes prevent current conduction from drain to source when a voltage VDS is applied.
The path between drain and source has a very high resistance (of the order of 1012 Ω). [Note: 1012 Ω = 10^12 Ω]
MOSFET : Operation
9

## slide 10

Channel for Current Flow:
Source & Drain are grounded and applied a positive voltage to the gate (VGS).
VGS  repells the free holes from the region of the substrate under the gate (the channel region).
These holes are pushed downward into the substrate, leaving behind a carrier-depletion region.
Positive VGS attracts electrons from the n+ source and drain regions into the channel region
MOSFET : Operation
10
When a sufficient number of electrons accumulate near the surface of the substrate under the gate, an n region is in effect created, connecting the source and drain regions,

Diagram description: Cross-section diagram of an NMOS transistor with grounded Source (S), Drain (D), and Body (B), positive DC voltage source vGS applied to Gate electrode (G) (+ at G, - at ground), showing Oxide (SiO2), induced n-type channel of length L, and carrier-depletion region outlined by a dashed boundary in the p-type substrate.

## slide 11

Channel for Current Flow:
If a voltage is applied between drain and source, current flows through this induced n region.
The induced n region thus forms a channel for current flow from drain to source
This is called an n-channel MOSFET or an NMOS transistor.
The channel is created by inverting the substrate surface from p type to n type. Hence the induced channel is also called an inversion layer.
MOSFET : Operation
11
Note: An n-channel MOSFET is formed in a p-type substrate
The excess of VGS over Vt is termed the effective voltage or  the overdrive voltage and is the quantity that determines the charge in the channel.
Here, VGS −Vt ≡ VOV

Diagram description: Cross-section diagram of an NMOS transistor (identical to slide 10) showing grounded Source (S), Drain (D), Body (B), positive voltage vGS applied to Gate (G), Oxide (SiO2), induced n-type channel of length L, and depletion region in p-type substrate.

## slide 12

Gate and Channel region of the MOSFET form a parallel-plate capacitor, with the oxide layer acting as the capacitor dielectric.
Positive gate voltage causes positive charge to accumulate on the top plate of the capacitor (the gate electrode).
Negative charge on the bottom plate is formed by the electrons in the induced channel.
This field controls the amount of charge in the channel hence it determines the channel conductivity when a voltage VDS is applied.
This is the origin of the name “field-effect transistor” (FET).
MOSFET
12

## slide 13

N-channel Enhancement MOSFET
Apply VGS between gate and source terminal keeping gate at high potential
Electrons will push towards the gate terminal and accumulate there
On increasing VGS electron hole pairs are formed pushing holes below and accumulating more electrons near Gate
When VGS reaches a threshold voltage, an n type channel is formed

Diagram description: Cross-section schematic labeled "Vgs < Vthreshold" showing a DC voltage source connected between Gate (+) and Source (-), Source connected to Body, p-type substrate with two n+ wells (Source, Drain), and gate dielectric, illustrating carrier accumulation and channel formation under applied Vgs.

## slide 14

N-channel Enhancement MOSFET
Now on applying VDS keeping drain at high potential, drain current will flow
On increasing the value of VDS, drain current will increase
VDS at which channel is pinched-off and drain current stop rising is called pinch-off voltage or saturation voltage
At pinch of voltage drain current is called saturation current
Now to increase saturation current further increase VGS

Circuit description: 3D circuit schematic of an n-channel MOSFET with DC voltage source VDD connected via load resistor and an in-line ammeter labeled "CURRENT" to Drain, voltage source VG connected to Gate, Source connected to negative supply line, with an inset graph of Drain Current (mA, 0-25) vs Drain Voltage (V, 0-6) showing a downward-sloping "Load Line" from (0 V, 15 mA) to (5 V, 0 mA).

## slide 15

N-channel Enhancement MOSFET V-I Characteristics

Graph description: Output characteristics plot of drain current iD (A) versus drain-to-source voltage vDS (V) for family of gate voltages vGS = 10 V, 9 V, 8 V, 7 V, 6 V, 5 V, and 4 V, separated by a dashed boundary line into "on/linear/constant resistance region" and "saturation/active/constant current region", with an "off-region" labeled near the horizontal axis below vGS = 4 V.

## slide 16

N-channel Depletion MOSFET

Diagram description: Cross-section diagram of N-channel Depletion MOSFET showing p-type substrate ("substrate", P), two n-doped regions ("n-doped region", n) connected by an existing n-channel along the "Silicon di Oxide insulation", Metal contacts, Drain (D), Gate (G), Source (S), and Source Substrate (SS).

## slide 17

N-channel Depletion MOSFET
N-type Channel is already present
Thickness of channel increases on applying VGS keeping gate at higher potential
Now on applying VDS keeping drain at hight potential, drain current will flow
On increasing the value of VDS, drain current will increase
On increasing VDS further the N-channel towards drain will become narrow thus decreasing drain current
VDS at which channel is pinched-off and drain current stop rising is called pinch-off voltage or saturation voltage
At pinch of voltage drain current is called saturation current
Now to increase saturation current further increase VGS

Diagram description: Cross-section schematic of N-channel Depletion MOSFET showing terminals Source (S), Gate (G), Drain (D), top yellow oxide layer, two square n-doped wells, and an existing channel beneath Gate showing carrier distribution across the channel in the substrate.

## slide 18

N-channel Depletion MOSFET V-I Characteristics

Graph description: Output characteristics plot of ID (mA) versus drain voltage (horizontal axis labeled 0, 2, 4, 6, 8, 10, 12, (+ve)) divided by a dashed curve into "Ohmic" and "Saturation" regions with IDSS indicated at VGS = 0V; curves labeled from top to bottom as VGS = +0.5V, VGS = 0V, VGS = +0.5V ⚠ looks wrong: positive sign below 0V, should be -0.5V, VGS = +1.0V ⚠ looks wrong: positive sign below 0V, should be -1.0V, and VGS = 2.0V ⚠ looks wrong: positive value below 0V, should be -2.0V, with a vertical double-headed arrow labeled +VGS to -VGS around VGS = 0.

## slide 19

D-MOSFET Transfer Characteristic
Fig. 19.49
Note that the transconductance curve for the D-MOSFET is very similar to the curve for a JFET. Because of this similarity, the JFET and the D-MOSFET have the same transconductance equation viz.

I_D = I_DSS (1 - V_GS / V_GS(off))^2

Graph description: Transfer characteristic curve plotting drain current ID (mA) on the vertical axis versus gate-to-source voltage VGS on the horizontal axis (negative -VGS to left, 0 V origin, positive VGS to right), showing vertical axis intercept at IDSS, horizontal axis intercept at VGS(off), labeled "Depletion (ID < IDSS)" for VGS < 0 and "Enhancement (ID > IDSS)" for VGS > 0.

## slide 20

These are important parameters of a D-MOSFET and a brief discussion on them is desirable.

(i) D-MOSFET Transconductance (g_m). The value of g_m is found for a D-MOSFET in the same way that it is for the JFET i.e.

g_m = g_mo (1 - V_GS / V_GS(off))

(ii) D-MOSFET Input Impedance. The gate impedance of a D-MOSFET is extremely high. For example, a typical D-MOSFET may have a maximum gate current of 10 pA when V_GS = 35V.

.: Input impedance = (35 V) / (10 pA) = (35 V) / (10 * 10^-12 A) = 3.5 * 10^12 \Omega

With an input impedance in this range, D-MOSFET would present virtually no load to a source circuit.

Worked example details:
- Given values:
  - Maximum gate current = 10 pA
  - V_GS = 35 V
- Step:
  - Input impedance = (35 V) / (10 pA) = (35 V) / (10 * 10^-12 A)
- Final answer:
  - Input impedance = 3.5 * 10^12 \Omega

## slide 21

Important equations region wise

| Operation Mode | Type | Condition | Equation |
| :--- | :--- | :--- | :--- |
| Cut-Off | NMOS | V_GS < V_TH | I_D = 0 |
| Cut-Off | PMOS | \|V_GS\| < \|V_TH\| | I_D = 0 |
| Linear | NMOS | V_GS >= V_TH<br>V_DS <= V_GS - V_TH | I_D = K_n (2(V_GS - V_TH) V_DS - V_DS^2) |
| Linear | PMOS | \|V_GS\| >= \|V_TH\|<br>\|V_DS\| <= \|V_GS\| - \|V_TH\| | I_D = K_p (2(V_GS - V_TH) V_DS - V_DS^2) ⚠ looks wrong: written as (V_GS - V_TH) V_DS without absolute values / PMOS polarities |
| Saturation | NMOS | V_GS >= V_TH<br>V_DS >= V_GS - V_TH | I_D = K_n (V_GS - V_TH)^2 (1 - \lambda V_DS) |
| Saturation | PMOS | \|V_GS\| >= \|V_TH\|<br>\|V_DS\| >= \|V_GS\| - \|V_TH\| | I_D = K_p (V_GS - V_TH)^2 (1 - \lambda V_DS) ⚠ looks wrong: written with (V_GS - V_TH)^2 (1 - \lambda V_DS) without PMOS polarities |

## slide 22

P-channel Enhancement MOSFET

Diagram description: Cross-section schematic of a P-channel Enhancement MOSFET showing an n-type substrate grounded at the bottom, two p+ wells with Source (S) contact grounded and Drain (D) contact, and Gate (G) contact above a gate insulator/metal layer over the channel region.

## slide 23

P-channel Enhancement MOSFET
It has N-type semiconductor material as body/substrate
Two P-type wells are diffused on the body/substrate
Two PN junctions are formed creating 2 depletion regions
A metal contact is created at the bottom and a terminal is taken out known as body/ substrate terminal
Same metal contacts are created on the top of P-type making source and drain terminals
There is a layer of Silicon Dioxide in between the 2 P-type well which act as a dielectric
A metal contact is created on the top of SiO2 layer and a terminal is taken out called Gate
Generally Source and body terminal are internally connected and is grounded

## slide 24

P-channel Enhancement MOSFET
Apply VGS between gate and source terminal keeping gate at low potential
Holes will push towards the gate terminal and accumulate there
When VGS reaches a threshold voltage, an p type channel is formed
Now on applying VDS keeping drain at low potential, drain current will flow
On increasing the value of VDS, drain current will increase
VDS at which channel is pinched-off and drain current stop rising is called pinch-off voltage or saturation voltage
At pinch of voltage drain current is called saturation current
Now to increase saturation current further make VGS more negetive

Diagram description: Cross-section diagram of P-channel Enhancement MOSFET channel formation showing N-TYPE SUBSTRATE, two P+ regions, INDUCED P-CHANNEL with positive hole charges (+), SiO2 Layer, Aluminium Metalization contacts, SOURCE (S) terminal, DRAIN (D) terminal, and GATE (G) (-) terminal with negative charges on gate and oxide interface.

## slide 25

P-channel Enhancement MOSFET V-I Characteristics

Graph description: Drain characteristics plot of drain current ID versus drain-to-source voltage VDS for P-channel Enhancement MOSFET with curves for VGS = -7V, VGS = -6V, VGS = -5V, VGS = -4V, VGS = -3V, cutoff at horizontal axis marked VGS = VT = -2V, and a parabolic boundary labeled "Locus of VDS (sat)".

## slide 26

The K constant in a MOSFET represents the process transconductance parameter, which defines how strongly the MOSFET can conduct for a given gate voltage.

I_D = K (V_GS - V_GS(th))^2

The constant K depends on the particular E-MOSFET and its value is determined from the following equation :

K = I_D(on) / (V_GS(on) - V_GS(th))^2

K = (1/2) \mu C_ox (W / L)

where:

| Symbol | Meaning |
| :--- | :--- |
| \mu | Mobility of charge carriers (electrons in NMOS, holes in PMOS) |
| C_ox | Oxide capacitance per unit area |
| W | Channel width |
| L | Channel length |

## slide 27

P-channel Depletion MOSFET

Diagram description: Cross-section diagram of P-channel Depletion MOSFET showing N-type Substrate, two p regions connected by a "Diffused Channel", "Dielecric layer" ⚠ looks wrong: typo for Dielectric layer, "Metallization Layer" for Gate (G), and terminals Source (S) and Drain (D) contacting p regions through the dielectric.

## slide 28

P-channel Depletion MOSFET
P-type Channel is already present
Apply VDS keeping drain at low potential, drain current will flow
On increasing the value of VDS, drain current will increase
On increasing VDS further the P-channel towards drain will become narrow thus decreasing drain current
VDS at which channel is pinched-off and drain current stop rising is called pinch-off voltage or saturation voltage
At pinch of voltage drain current is called saturation current
Now to increase saturation current further increase VGS ⚠ looks wrong: for P-channel depletion MOSFET, more negative VGS increases drain current; increasing VGS (making it more positive) depletes the channel

Diagram description: Cross-section schematic of P-channel Depletion MOSFET with Vgs = 0V applied from DC source between Gate and Source/Body, n-type substrate, Body contact at bottom connected to Source, two p+ regions (Source, Drain), and a pre-existing "Implanted p-channel" in red beneath gate dielectric.

## slide 29

P-channel Depletion MOSFET V-I Characteristics

Graph description: Output characteristics plot of ID(mA) versus drain voltage (horizontal axis labeled 0, 2, 4, 6, 8, 12, +ve) divided by a dashed red curve into "Ohmic" and "Saturation" regions, with IDSS marked at VGS = 0V, curves labeled from top to bottom as VGS = +0.5V, VGS = 0V, VGS = -0.5V, VGS = -0.1V ⚠ looks wrong: curve is placed below -0.5V and above -0.2V, out of sequence and with positive/negative polarities inverted for PMOS, and VGS = -0.2V, with vertical arrows on the right spanning +VGS to -VGS from VGS = 0 v.

---

## Done report

- Files written: `C:/Users/bhomi/AppData/Local/Temp/claude/6e81c002d1e3bfcd/bd6f37ef-47e2-42fc-83d1-906fe62e205d/scratchpad/edc-e0/out/mostype.md`
- Sections transcribed: slides 1 through 29 (29 slide sections)
- Counts:
  - Total slides transcribed: 29
  - Tables transcribed: 2 (slide 21: region-wise equations table; slide 26: K constant parameter definition table)
  - Worked examples / calculations: 1 (slide 20: input impedance calculation)
  - Diagrams / circuits / graphs described: 19
- What could not be read: None (all slides, images, and formulas were legible)
- Every `[?]`: None (no ambiguous text or symbols requiring `[?]`)
- Noted discrepancies / errors flagged (`⚠ looks wrong: <why>`):
  - Slide 18: Curves below VGS = 0V labeled with positive voltages (+0.5V, +1.0V, 2.0V) instead of negative depletion voltages (-0.5V, -1.0V, -2.0V).
  - Slide 21: PMOS Linear and Saturation equations written as $(V_{GS} - V_{TH})$ without PMOS polarities / absolute values.
  - Slide 27: Typo "Dielecric layer" in diagram for dielectric layer.
  - Slide 28: Text states "Now to increase saturation current further increase VGS" for P-channel depletion MOSFET (increasing VGS makes it more positive, which depletes a p-channel rather than increasing current).
  - Slide 29: Curve labels for PMOS depletion characteristics are placed out of numerical sequence (-0.1V placed below -0.5V, and -0.2V below -0.1V).
