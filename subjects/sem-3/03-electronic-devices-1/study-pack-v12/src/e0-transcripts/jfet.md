# JFET (Junction Field Effect Transistor) - Unit 3 Slides Transcription

## slide 1

JFET
Junction Field Effect Transistor

## slide 2

Introduction (FET)
Field-effect transistor (FET) are important devices such as BJTs
Also used as amplifier and logic switches
Types of FET:
MOSFET (metal-oxide-semiconductor field-effect transistor)
Depletion-mode MOSFET
JFET (junction field-effect transistor)

- Graphic [s002-image5.png]: Subtle horizontal gradient background decorative element.

## slide 3

Types of Field Effect Transistors (The Classification)
JFET
MOSFET (IGFET)
n-Channel JFET
p-Channel JFET
n-Channel EMOSFET
p-Channel EMOSFET
Enhancement MOSFET
Depletion MOSFET
n-Channel DMOSFET
p-Channel DMOSFET
FET

Classification hierarchy:
- FET (Field Effect Transistor)
  - JFET
    - n-Channel JFET
    - p-Channel JFET
  - MOSFET (IGFET)
    - Enhancement MOSFET (EMOSFET)
      - n-Channel EMOSFET
      - p-Channel EMOSFET
    - Depletion MOSFET (DMOSFET)
      - n-Channel DMOSFET
      - p-Channel DMOSFET

## slide 4

BJT-Current-controlled device            FET –voltage controlled device

- Diagram (a) [s004-image6.jpeg]: Block diagram of BJT as a current-controlled device with input control current arrow IB entering base terminal on left, controlled current arrow IC entering top collector terminal, and emitter terminal exiting at bottom.
- Diagram (b) [s004-image7.jpeg]: Block diagram of FET as a voltage-controlled device with input control voltage VGS (+ at gate terminal on left, - at bottom source terminal), controlled drain current arrow ID entering top drain terminal, and source terminal exiting at bottom.

## slide 5

Junction FETs (JFETs)
JFETs consists of a piece of high-resistivity semiconductor material (usually Si) which constitutes a channel for the majority carrier flow.
Conducting semiconductor channel between two ohmic contacts – source & drain

- Circuit symbols [s005-image8.png]: Schematic symbols for JFET captioned "JFET (Junction gate)": N-channel JFET on left (labeled N, gate arrow pointing inwards toward the channel bar between drain and source) and P-channel JFET on right (labeled P, gate arrow pointing outwards away from the channel bar between drain and source).
- Diagram [s005-image9.png]: 3D rectangular bar representation of JFET showing elongated semiconductor channel with front terminal S (Source), rear terminal D (Drain), and side embedded regions joined to terminal G (Gate).
- Diagram [s005-image10.png]: 3D basic structure of n-channel JFET showing rectangular semiconductor block with red n-channel between terminal S (Source) and terminal D (Drain), embedded top and bottom blue p+ regions connected to terminal G (Gate), surrounded by yellow depletion regions.

## slide 6

Junction field-effect transistor (JFET)

- Diagram [s006-image11.jpeg]: Cross-sectional structure of n-channel JFET showing vertical n-channel slab with top Ohmic contact connected to Drain (D) and bottom Ohmic contact connected to Source (S), flanked symmetrically by two p-type regions with Ohmic contacts interconnected by external wire to Gate (G), and gray shaded depletion regions extending into the channel.

## slide 7

N-channel JFET..

- Diagram / Symbol [s007-image12.png]: Schematic circuit symbol (left) of n-channel JFET with Gate (inward-pointing arrow), Drain, and Source terminals; and physical planar structure (right) showing vertical n-type channel between top Drain contact and bottom Source contact, flanked by two green p-type gate regions connected to common Gate terminal.
- Circuit Symbol (a) [s007-image13.jpeg]: Circuit symbol of n-channel JFET with highlighted circle, showing terminal labels D (Drain), G (Gate), and S (Source), drain current arrow ID entering D, gate-to-source voltage VGS (+ at G, - at S), and drain-to-source voltage VDS (+ at D, - at S).

## slide 8

JFET for VGS = 0 V and 0<VDS<|Vp|
Channel becomes narrower as VDS is increased

- Diagram [s008-image14.jpeg]: Biasing diagram of n-channel JFET for VGS = 0 V (gate terminal G connected directly to source terminal S at ground) and 0 < VDS < |Vp| supplied by variable DC source VDD (+ to drain D, - to ground/source S), showing electron flow (e) moving upward from source to drain, drain current arrow ID entering D and source current arrow IS leaving S, with gray depletion regions becoming progressively wider toward the drain end, making the conductive channel narrower at the top.

## slide 9

Pinch-off (VGS = 0 V, VDS = VP).

- Diagram [s009-image15.jpeg]: Biasing diagram of n-channel JFET at pinch-off condition with VGS = 0 V (gate G connected to grounded source S) and VDS = VP (+ at D, - at S), showing gray depletion regions from both p-regions extending inward and almost touching near the drain end, labeled "Pinch-off", leaving a narrow constriction for saturation current.

## slide 10

Application of a negative voltage to the gate of a JFET.

- Diagram [s010-image16.jpeg]: Biasing diagram of n-channel JFET with reverse-biased gate: DC source of 1 V connected between gate G and grounded source S giving VGS = -1 V (- at G, + at S, gate current IG = 0 A) and drain bias VDS > 0 V (+ at D, - at S), resulting in wider depletion regions along the entire channel and channel narrowing occurring at a lower VDS, with drain current ID entering D and source current IS leaving S.

## slide 11

Operation of a  JFET
P
P
+
-
DC Voltage Source
+
-
+
-
N
N
Gate
Drain
Source

- Diagram [slide 11 vector diagram]: Structural diagram illustrating the operation of an n-channel JFET, showing central n-channel bar (N, N) with Drain terminal at top and Source terminal at bottom connected across a DC Voltage Source (+ to drain, - to source), flanked by two p-type gate regions (P, P) connected to Gate terminal with reverse-bias polarity indications (+ / -).

## slide 12

Operation of JFET at Various Gate Bias Potentials
Figure: The nonconductive depletion region becomes broader with increased reverse bias.
(Note: The two gate regions of each FET are connected to each other.)

- Diagram [s012-image17.jpeg]: Three-panel diagram showing the n-channel JFET channel at various gate bias potentials:
  - (a) Bias is zero and depletion layer is thin; low-resistance channel exists between the drain and the source (gate G connected directly to source S, channel between D and S).
  - (b) Moderate gate-to-channel reverse bias results in narrower channel, with DC voltage source connected between G and S such that 0 > vGS > Vto.
  - (c) Bias greater than pinch-off voltage; no conductive path from drain to source, with larger reverse bias battery connected between G and S such that vGS < Vto, causing hatched depletion layers to touch in the center and pinch off the channel.

## slide 13

SYMBOLS
n-channel JFET
Gate
Drain
Source
n-channel JFET
Offset-gate symbol
Gate
Drain
Source
p-channel JFET
Gate
Drain
Source

- Schematic Symbols [slide 13 vector diagram]: Three circuit symbols for JFET: standard n-channel JFET symbol (Gate with centered inward arrow, Drain at top, Source at bottom), offset-gate n-channel JFET symbol (Gate with inward arrow positioned closer to Source terminal), and p-channel JFET symbol (Gate with outward-pointing arrow, Drain at top, Source at bottom).

## slide 14

Junction FETs
JFET is a high-input resistance device, while the BJT is comparatively low.
If the channel is doped with a donor impurity, n-type material is formed and the channel current will consist of electrons.
If the channel is doped with an acceptor impurity, p-type material will be formed and the channel current will consist of holes.
N-channel devices have greater conductivity than p-channel types, since electrons have higher mobility than do holes; thus n-channel JFETs are approximately twice as efficient conductors compared to their p-channel counterparts.

- Diagram [s014-image10.png]: 3D "Basic structure" diagram of n-channel JFET showing rectangular semiconductor block with red n-channel between terminal S (Source) and terminal D (Drain), embedded top and bottom blue p+ regions connected to terminal G (Gate), surrounded by yellow depletion regions.

## slide 15

N-channel JFET
N channel JFET:
Major structure is  n-type material (channel) between embedded p-type material to form 2 p-n junction.
In the normal operation of an n-channel device, the Drain (D) is positive with respect to the Source (S). Current flows into the Drain (D), through the channel, and out of the Source (S)
Because the resistance of the channel depends on the gate-to-source voltage (VGS), the drain current (ID) is controlled by that voltage

## slide 16

Introduction.. (Advantages of FET)
High input impedance (M)                                (Linear AC amplifier system)
Temperature stable than BJT
Smaller than BJT
Can be fabricated with fewer processing
BJT is bipolar – conduction both hole and electron
FET is unipolar – uses only one type of current carrier
Less noise compare to BJT
Usually use as logic switch

## slide 17

P-channel JFET..

- Diagram / Symbol [s017-image18.png]: Schematic circuit symbol (left) of p-channel JFET with Gate (outward-pointing arrow), Drain, and Source terminals; and physical planar structure (right) showing vertical green p-type channel between top Drain contact and bottom Source contact, flanked by two light-purple n-type gate regions connected to common Gate terminal.
- Circuit Symbol (b) [s017-image19.jpeg]: Circuit symbol of p-channel JFET with highlighted circle, showing terminal labels D (Drain), G (Gate), and S (Source), drain current arrow ID directed upwards out of D, gate-to-source voltage VGS (+ at G, - at S), and drain-to-source voltage VDS (+ at D, - at S).

## slide 18

p-Channel JFET

- Diagram [s018-image20.jpeg]: Biasing diagram of p-channel JFET showing holes (+) moving upward from source to drain, biased by DC source VGG (+ to gate G, - to source S giving VGS = +VGG, gate current IG = 0 A) and DC source VDD (+ to drain D, - to grounded source S giving VDS with + at D, - at S); drain current arrow ID directed upward out of D and source current arrow IS directed upward into S, with gray depletion regions wider near the drain end.

## slide 19

JFET Characteristic Curve
To start, suppose VGS=0
Then, when VDS is increased, ID increases. Therefore, ID is proportional to VDS for small values of VDS
For larger value of VDS, as VDS increases, the depletion layer become wider, causing the resistance of channel increases.
After the pinch-off voltage (Vp) is reached, the ID becomes nearly constant (called as ID maximum, IDSS-Drain to Source current with Gate Shorted)

## slide 20

JFET Characteristic Curve
ID versus VDS for VGS = 0 V.

- Graph [s020-image21.jpeg]: Graph of drain current ID versus drain-to-source voltage VDS for VGS = 0 V starting at origin 0, showing an initial linear region labeled "n-channel resistance", a curved knee labeled "Increasing resistance due to narrowing channel", a vertical dashed line at pinch-off voltage VP, and a flat horizontal region labeled "Saturation level" at constant maximum current IDSS.

## slide 21

JFET Characteristic Curve
n-Channel JFET characteristics curve with IDSS = 8 mA and VP = -4 V.

- Graph [s021-image22.jpeg]: Drain characteristic family of curves for n-channel JFET with IDSS = 8 mA and VP = -4 V, plotting ID (mA, 0 to 8) versus VDS (V, 0 to 25); curves plotted for VGS = 0 V (saturating at IDSS = 8 mA), VGS = -1 V (saturating at ~4.5 mA), VGS = -2 V (saturating at 2 mA), VGS = -3 V (saturating at ~0.5 mA), and VGS = -4 V = VP (cutoff at 0 mA); dashed parabolic curve indicates "Locus of pinch-off values", dividing the "Ohmic Region" on the left from the "Saturation Region" on the right, with VP (for VGS = 0 V) marked at 4 V on the horizontal axis.

## slide 22

p-Channel JFET characteristics with IDSS = 6 mA and VP = +6 V.

- Graph [s022-image23.jpeg]: Drain characteristic family of curves for p-channel JFET with IDSS = 6 mA and VP = +6 V, plotting ID (mA, 0 to 7) versus negative VDS (V, 0 to -25); curves plotted for VGS = 0 V (saturating at ~6 mA), VGS = +1 V (~4.5 mA), VGS = +2 V (~2.8 mA), VGS = +3 V (~1.3 mA), VGS = +4 V (~0.6 mA), and VGS = +5 V (~0.1 mA), showing a gray shaded oval labeled "Breakdown region" where drain current rises sharply between VDS = -19 V and -25 V.

## slide 23

Characteristics for n-channel JFET

- Graph [s023-image24.png]: Plot titled 'Characteristic curves for a typical N-channel JFET' showing drain-source current Ids (mA, 0 to 40) versus drain-source voltage Vds (Volts, 0 to 20); green shaded area (0 to ~2.5 V) indicates ohmic/triode region and cream shaded area (2.5 to 20 V) indicates saturation region; curves shown for gate-source voltage Vgs = 0 V (saturating at ~34.5 mA), -1 V (~17 mA), -2 V (~6 mA), and -3 V (~1 mA); header defines Ids = drain-source current, Vds = drain-source voltage, Vgs = gate-source voltage.

## slide 24

JFET Characteristic Curve..
For negative values of VGS, the gate-to-channel junction is reverse biased even with VDS=0
Thus, the initial channel resistance is higher (in which the initial slope of the curves is smaller for values of VGS closer to the pinch-off voltage (VP)
The resistance value is under the control of VGS
If VGS is less than pinch-off voltage, the resistance becomes an open-circuit ;therefore the device is in cutoff (VGS=VGS(off) )
The region where ID constant – The saturation/pinch-off region
The region where ID depends on VDS is called the linear/triode/ohmic region

## slide 25

Characteristics for p-channel JFET
P
+
+
+

- Graph [s025-image24.png]: Duplicate image of 'Characteristic curves for a typical N-channel JFET' (identical to s023-image24.png) plotting Ids (mA, 0 to 40) versus Vds (Volts, 0 to 20) with green ohmic region and cream saturation region, curves for Vgs = 0 V, -1 V, -2 V, -3 V.
⚠ looks wrong: Slide title is 'Characteristics for p-channel JFET', but the embedded image (s025-image24.png) is identical to slide 23 (s023-image24.png), which displays curves for an N-channel JFET (labeled 'Characteristic curves for a typical N-channel JFET', with positive Vds and negative Vgs = 0 V to -3 V). Slide text also contains isolated stray text 'P', '+', '+', '+'.

## slide 26

Operation of n-channel JFET
JFET is biased with two voltage sources:
VDD
VGG
VDD generate voltage bias between Drain (D) and Source (S) – VDS
VDD causes drain current, ID flows from Drain (D) to Source (S)
VGG generate voltage bias between Gate (G) and Source (S) with negative polarity source is connected to the Gate Junction (G) – reverse-biases the gate; therefore gate current, IG = 0.
VGG is to produce depletion region in N channel so that it can control the amount of drain current, ID that flows through the channel

## slide 27

Transfer Characteristics
JFET Transfer Characteristic Curve
JFET Characteristic Curve

- Graph [s027-image25.jpeg]: Dual-quadrant graph illustrating the derivation of the JFET transfer characteristic curve (left) from drain characteristics (right): right quadrant plots drain characteristics ID (mA, 0 to 10) vs VDS (V, 0 to 25) for VGS = 0 V (IDSS = 8 mA), -1 V (4.5 mA), -2 V (2 mA), -3 V (~0.5 mA), -4 V (0 mA) with horizontal dashed projection lines and an arrow pointing left; left quadrant plots transfer characteristics ID (mA, 0 to 10) vs VGS (V, -4 to 0) connecting points (-4 V, 0 mA labeled "ID = 0 mA, VGS = VP"), (-3 V, ~0.5 mA), (-2 V, 2 mA), (-1 V, 4.5 mA), and (0 V, 8 mA labeled IDSS) along a parabolic curve.

## slide 28

Transfer Characteristics..
In JFET, the relationship between VGS (input voltage) and ID (output current) is used to define the transfer characteristics. It is called as Shockley’s Equation:
The relationship is more complicated (and not linear)
As a result, FET’s are often referred to a square law devices
VP=VGS (OFF)

Shockley's Equation [s028-image26.png]:
ID = IDSS * (1 - VGS / VP)^2

## slide 29

Transfer Characteristics…
Defined by Shockley’s equation:
Relationship between ID and VGS.
Obtaining transfer characteristic curve axis point from  Shockley:
When VGS = 0 V, ID = IDSS
When VGS = VGS(off) or Vp, ID = 0 mA

Equations [s029-image27.png]:
ID = IDSS * (1 - VGS / VGS(off))^2
VP = VGS(off)

## slide 30

CHARACTERISTICS PARAMETERS OF JFET

1. Mutual conductance or transconductance, gm [s030-image90.png]
gm = (∂ID / ∂VGS)_VDS = ΔID / ΔVGS, with VDS constant [s030-image100.png]

2. Drain resistance, rd [s030-image11.png]
rd = (∂VDS / ∂ID)_VGS = ΔVDS / ΔID, with VGS constant [s030-image120.png]

3. Drain conductance, gd [s030-image13.png]
gd = (∂ID / ∂VDS)_VGS = ΔID / ΔVDS, with VGS constant [s030-image14.png]

4. Amplification factor, μ [s030-image15.png]
μ = -(∂VDS / ∂VGS)_ID = -ΔVDS / ΔVGS, with ID constant [s030-image16.png]

## slide 31

Relationship among FET parameters or Relation between μ, rd & gm [s031-image17.png]

ID = f(VDS, VGS) [s031-image180.png]

Using Taylor’s theorem by considering fractional change in VDS, VGS & ID [s031-image190.png]:

ΔID = (∂ID / ∂VDS)_VGS * ΔVDS + (∂ID / ∂VGS)_VDS * ΔVGS [s031-image20.png]

ΔID / ΔVGS = (∂ID / ∂VDS)_VGS * (ΔVDS / ΔVGS) + (∂ID / ∂VGS)_VDS [s031-image21.png]

If ID is constant, [s031-image22.png]
ΔID / ΔVGS = 0 [s031-image23.png]

0 = (∂ID / ∂VDS)_VGS * (ΔVDS / ΔVGS) + (∂ID / ∂VGS)_VDS [s031-image240.png]

gm = (∂ID / ∂VGS)_VDS [s031-image250.png]
rd = (∂VDS / ∂ID)_VGS [s031-image26.png]
μ = -(∂VDS / ∂VGS)_ID [s031-image27.png]

0 = (1 / rd) * (-μ) + gm [s031-image28.png]

μ / rd = gm [s031-image29.png]

μ = rd * gm [s031-image30.png]

## slide 32

Show that gm = (2 / |VP|) * sqrt(IDS * IDSS) [s032-image31.png]

Decreasing the gate voltage VGS from zero till ID is reduced to zero [s032-image33.png]
Characteristic is parabolic

- Graph [s032-image32.png]: Transfer characteristic curve showing parabolic variation of drain current ID (mA, 0 to 15) versus negative gate-to-source voltage -VGS (V, 0 to -6); curve starts at VGS(OFF) = -6 V where ID = 0 mA and increases to IDSS (~12 mA) at VGS = 0 V; at Vp / 2 = -2 V, a triangle indicates incremental values δVGS and δID with tangent slope line.
⚠ looks wrong: On graph s032-image32.png, the label Vp / 2 is marked at -2 V while VGS(OFF) is marked at -6 V (if pinch-off Vp = -6 V, half pinch-off Vp / 2 would be -3 V, not -2 V).

Shockley gives the equation of drain characteristics as:
IDS = IDSS * (1 - VGS / VP)^2 [s032-image36.png]

IDS / IDSS = (1 - VGS / VP)^2 [s032-image34.png]

Equation of Parabola is given as
y = x^2 [s032-image35.png]

This resembles equation of parabola

## slide 33

IDS = IDSS * (1 - VGS / VP)^2 [s033-image37.png]

Differentiating above equation with respect to VGS, [s033-image38.png]

∂IDS / ∂VGS = [s033-image39.png] IDSS * [s033-image40.png] 2 * (1 - VGS / VP) [s033-image41.png] * (-1 / VP) [s033-image42.png]

∵ gm = (∂IDS / ∂VGS)_VDS [s033-image43.png]
= - (2 * IDSS / VP) * (1 - VGS / VP) [s033-image44.png]

gm = - (2 * IDSS / VP) * (1 - VGS / VP) [s033-image45.png]

IDS / IDSS = (1 - VGS / VP)^2 [s033-image46.png]

sqrt(IDS / IDSS) = (1 - VGS / VP) [s033-image47.png]

∴ gm = - (2 * IDSS / VP) * sqrt(IDS / IDSS) [s033-image48.png]

∴ gm = (2 / -VP) * sqrt(IDSS^2 * IDS / IDSS) [s033-image50.png]

= (2 / -VP) * sqrt(IDSS * IDS) [s033-image49.png]

gm = (2 / |VP|) * sqrt(IDS * IDSS) [s033-image51.png]

## slide 34

gm = - (2 * IDSS / VP) * (1 - VGS / VP) [s034-image52.png]

Let gm = gm0 when VGS = 0 [s034-image57.png]

gm0 = - (2 * IDSS / VP) * (1 - 0 / VP) [s034-image58.png]

gm0 = - (2 * IDSS / VP) [s034-image59.png]

gm = gm0 * (1 - VGS / VP) [s034-image60.png]

IDS / IDSS = (1 - VGS / VP)^2 [s034-image53.png]

sqrt(IDS / IDSS) = (1 - VGS / VP) [s034-image54.png]

∴ gm = - (2 * IDSS / VP) * sqrt(IDS / IDSS) [s034-image55.png]

= (2 / -VP) * sqrt(IDSS * IDS) [s034-image56.png]

gm = gm0 * sqrt(IDS / IDSS) [s034-image61.png]

∴ gm = (2 / -VP) * sqrt(IDSS^2 * IDS / IDSS) [s034-image62.png]

gm = (2 / |VP|) * sqrt(IDS * IDSS) [s034-image63.png]

## slide 35

COMMON SOURCE (CS) AMPLIFIER

- Circuit (a) [s035-image33.png]: Common source JFET amplifier circuit with AC input voltage Vi (+ top, - bottom) across gate resistor RG to gate G; n-channel JFET with drain D connected to supply VDD through drain resistor RD, source S connected to ground through source self-bias resistor RS in parallel with bypass capacitor Cs; output voltage Vo taken between drain D (+) and ground (-).
- Circuit (b) [s035-image33.png]: Small-signal equivalent circuit of common source amplifier using voltage-source model: input voltage Vi across RG to gate G establishing gate-to-source voltage Vgs (+ at G, - at S); output loop has dependent voltage source μ*Vgs (- top, + bottom at source S) in series with internal drain resistance rd up to drain D, external drain resistor RD connected from D to S (ground) carrying current id, with output voltage Vo across RD (+ at D, - at S).

## slide 36

Voltage Gain  Source resistor (Rs) is used to set the Q-point but is bypassed by CS for mid-frequency operation. From the small signal equivalent circuit, the output voltage, [s036-image34.png]

Vo = (-RD / (RD + rd)) * μ * Vgs [s036-image35.png]

where Vgs = Vi, the input voltage.
Hence, the voltage gain,

Av = Vo / Vi = -μ * RD / (RD + rd) [s036-image35.png]

Input Impedance  From Fig. 5.14(b), Input Impedance is

Zi = RG [s036-image35.png]

For voltage divider bias as in CE Amplifiers of BJT

RG = R1 || R2 [s036-image35.png]

## slide 37

Output Impedance  Output Impedance is the impedance measured at the output terminals with the input voltage Vi = 0
From Fig. 5.14(b) when Vi = 0, Vgs = 0 and hence
μ * Vgs = 0
Then the equivalent circuit for calculating Output Impedance is given in Fig. 5.14(c).
Output impedance  Zo = rd || RD
Normally rd will be far greater than RD [Typical values are rd = 35 kΩ and RD = 5 kΩ]
Hence Zo ≈ RD [s037-image36.png]

- Circuit [Fig. 5.14(c) in s037-image36.png]: Equivalent circuit for calculation of output impedance of CS amplifier, showing parallel combination of internal drain resistance rd and drain resistor RD connected across the output terminals, looking in with arrow Zo.

## slide 38

COMMON DRAIN (CD) AMPLIFIER
Zi = RG
Output Impedance Zo
It is given by

- Circuit [Fig3.12 in s038-image37.jpeg]: Circuit of Common Drain amplifier (source follower): input signal Vi applied via coupling capacitor C1 to gate G, with gate resistor RG to ground (gate voltage VG to ground; input impedance Zi looking into gate); n-channel JFET with drain D connected directly to VDD; source S connected through source resistor RS to ground (source voltage VS to ground) and via coupling capacitor C2 to output terminal Vo (output impedance Zo looking into source); gate-to-source voltage VGS from G to S.
- Circuit [Fig3.13 in s038-image38.jpeg]: Simplified small model of Common Drain amplifier: input voltage Vi across gate resistor RG to open-circuit gate G (+); common line connected to drain D (grounded); dependent current source gm*Vgs directed upwards from D to source terminal S (current ID arrow right); parallel branches between S and D contain internal drain resistance rd (with impedance Z'o looking left) and source resistor RS; output voltage Vo taken across RS (output impedance Zo looking in from output).

Derivation [s038-image39.jpeg]:
Zo = Z'o || RS
where Z'o = (Vo / Id)|_(Vi = 0)

Applying KVL to the outer loop we can have,
Vi + Vgs - Vo = 0
As Vi = 0,
Vgs = Vo
Looking at Fig. we can write that,
gm * Vgs = Id
But Vgs = Vo, so
gm * Vo = Id
Z'o = Vo / Id = 1 / gm
∴ Zo = (1 / gm) || RS

⚠ looks wrong: In KVL equation 'Vi + Vgs - Vo = 0', setting Vi = 0 gives 'Vgs = Vo' without accounting for the negative sign/polarity inversion between gate-source and source-drain (Vgs = Vg - Vs = 0 - Vo = -Vo in Fig 3.13).

## slide 39

Derivation of CD Amplifier Voltage Gain [s039-image40.jpeg]:

Av = Vo / Vi

Looking at Fig. we can write that,
Vo = - Id * (rd || RS)
and Id = gm * Vgs
∴ Vo = - gm * Vgs * (rd || RS)

But
Vi = - Vgs + Vo
= - Vgs + [ - gm * Vgs * (rd || RS) ]

⚠ looks wrong: Slide derivation is cut off/incomplete; it ends at Vi = - Vgs + [ - gm * Vgs * (rd || RS) ] without completing the voltage gain expression Av = Vo / Vi (which simplifies to Av = gm * (rd || RS) / (1 + gm * (rd || RS))).

## slide 40

COMMON GATE (CG) AMPLIFIER

- Circuit (a) [s040-image41.png]: Common Gate (CG) JFET amplifier circuit: input Vi (+ top, - bottom) applied through coupling capacitor CC across source resistor RS to source S; gate G biased with voltage divider R1 (connected to VDD) and R2 (connected to ground); drain D connected to VDD through drain resistor RD and through coupling capacitor CC to output Vo (+ top, - bottom).
- Circuit (b) [s040-image41.png]: Small-signal equivalent circuit of common gate amplifier: input Vi across source resistor RS to source terminal S (+ top, - bottom at gate G, voltage labeled Vsg); dependent current source gm*Vgs directed left from drain D to source S, with internal drain resistance rd connected in parallel between S and D; drain D connects to ground (G) through external drain resistor RD carrying current id, with output voltage Vo (+ top at D, - bottom at G).

## slide 41

Derivation of CG Amplifier Voltage Gain [s041-image64.png]:

Voltage Gain  From the small signal equivalent circuit by applying KCL, ir = id - gm * Vgs. Applying KVL around the outer loop gives
Vo = (id - gm * Vgs) * rd + Vsg

But Vsg = - Vgs = Vi and id = -Vo / RD

Thus,
Vo = ((-Vo / RD) + gm * Vi) * rd + Vi

Hence, the voltage gain,
AV = Vo / Vi = (gm * rd + 1) * RD / (RD + rd)

## slide 42

Input Impedance  Figure 5.18(b) is modified for calculation of Input Impedance as shown in Fig. 5.18(c). [s042-image65.png]

- Circuit [Fig. 5.18(c) in s042-image65.png]: Modified Equivalent Circuit for Input Impedance calculation: input voltage Vi (+ top, - bottom) across source resistor RS, looking into input impedance Zi (and Z'i looking past RS); source current I1 enters source S; parallel branch between S and D has internal drain resistance rd (carrying current Ird directed right) and dependent current source gm*Vgs directed left; drain terminal D connects to external drain resistor RD carrying current IRD downward with output voltage Vo (+ top, - bottom); common return rail connected to gate terminal G.

## slide 43

Current through rd is [s043-image66.png]
Ird = - Ir = I1 + gm * Vgs
I1 = Ird - gm * Vgs
where
Ird = (Vi - Vo) / rd
= (Vi - IRD * RD) / rd
Hence
I1 = (Vi - IRD * RD) / rd - gm * Vgs
From Fig. 5.18(c),
Vi = - Vgs
I1 = (Vi - IRD * RD) / rd + gm * Vi
= (Vi / rd) - (IRD * RD / rd) + gm * Vi
I1 + (IRD * RD / rd) = (Vi / rd) + gm * Vi

From Fig. 5.18(c), [s043-image67.png]
I1 = IRD
Therefore
I1 * [(rd + RD) / rd] = Vi * [(1 / rd) + gm]
Vi / I1 = (rd + RD) / (1 + gm * rd) = Z'
From Fig. 5.18(c),
Zi = RS [?] Z'i
= RS [?] (rd + RD) / (1 + gm * rd)
In practice, rd >> RD and gm * rd >> 1.
Therefore,
Zi = RS [?] rd / (gm * rd)
= RS [?] 1 / gm

⚠ looks wrong: In s043-image67.png, the parallel operator symbol (||) failed to render and appears as blank whitespace between RS and Z'i (and in subsequent steps: 'Zi = RS   Z\'i', '= RS   (rd + RD)/(1 + gm * rd)', 'Zi = RS   rd/(gm * rd)', '= RS   1/gm').

## slide 44

From Fig. 5.18(c) when Vi = 0, Vsg = 0, the resultant equivalent circuit is shown in Fig. 5.18(d). [s044-image68.png]
Zo = rd || RD
as rd >> RD
Zo ≈ RD

- Circuit [Fig. 5.18(d) in s044-image68.png]: Equivalent Circuit for Output Impedance of CG amplifier: loop showing internal drain resistance rd in parallel with drain resistor RD across output terminals looking in with arrow Zo.

---

## Done Report

- **File written**: `C:/Users/bhomi/AppData/Local/Temp/claude/6e81c002d1e3bfcd/bd6f37ef-47e2-42fc-83d1-906fe62e205d/scratchpad/edc-e0/out/jfet.md`
- **Sections**: 44 slide sections (`## slide 1` through `## slide 44`)
- **Counts**:
  - Total slides transcribed: 44
  - Total circuit/graph images described: 33 (31 image files plus 2 native PowerPoint vector shape diagrams on slides 11 and 13)
- **Unreadable items**: None (`[unreadable]` count: 0)
- **Uncertain readings**: `[?]` count: 4 (all on slide 43 where the parallel operator symbol failed to render as text/glyph and appears as whitespace in the equation image)
- **Flagged issues**: 5 items
  1. Slide 25: `⚠ looks wrong: Slide title is 'Characteristics for p-channel JFET', but the embedded image (s025-image24.png) is identical to slide 23 (s023-image24.png), which displays curves for an N-channel JFET (labeled 'Characteristic curves for a typical N-channel JFET', with positive Vds and negative Vgs = 0 V to -3 V). Slide text also contains isolated stray text 'P', '+', '+', '+'.`
  2. Slide 32: `⚠ looks wrong: On graph s032-image32.png, the label Vp / 2 is marked at -2 V while VGS(OFF) is marked at -6 V (if pinch-off Vp = -6 V, half pinch-off Vp / 2 would be -3 V, not -2 V).`
  3. Slide 38: `⚠ looks wrong: In KVL equation 'Vi + Vgs - Vo = 0', setting Vi = 0 gives 'Vgs = Vo' without accounting for the negative sign/polarity inversion between gate-source and source-drain (Vgs = Vg - Vs = 0 - Vo = -Vo in Fig 3.13).`
  4. Slide 39: `⚠ looks wrong: Slide derivation is cut off/incomplete; it ends at Vi = - Vgs + [ - gm * Vgs * (rd || RS) ] without completing the voltage gain expression Av = Vo / Vi (which simplifies to Av = gm * (rd || RS) / (1 + gm * (rd || RS))).`
  5. Slide 43: `⚠ looks wrong: In s043-image67.png, the parallel operator symbol (||) failed to render and appears as blank whitespace between RS and Z'i (and in subsequent steps: 'Zi = RS   Z\'i', '= RS   (rd + RD)/(1 + gm * rd)', 'Zi = RS   rd/(gm * rd)', '= RS   1/gm').`
