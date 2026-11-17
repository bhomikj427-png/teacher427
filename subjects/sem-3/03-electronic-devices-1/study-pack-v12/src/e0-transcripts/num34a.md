# Solved Numericals: JFET, D-MOSFET, E-MOSFET (Pages 1–11)

Source folder: `NUMERICALS-U3-U4-jfet-dmosfet-emosfet-solved`

## page 1

Q2. A JFET has the following parameters: IDSS = 32 mA ▪
; VGS (off) = – 8V ; VGS = – 4.5 V. Find the value of drain ▪

[Note: Page 1 contains only the opening lines of Q2 at the bottom; Q1 is absent from the sheet.]

## page 2

current.

Solution :

ID = IDSS [1 - VGS / VGS (off)]^2
   = 32 [1 - (-4.5) / -8]^2 mA
   = 6.12 mA

Q3. A JFET has a drain current of 5 mA. If IDSS = 10 mA and VGS (off) = – 6 V, find the value of (i) VGS and (ii) VP.

Solution.

ID = IDSS [1 - VGS / VGS (off)]^2
or
5 = 10 [1 + VGS / 6]^2
or
1 + VGS / 6 = sqrt(5/10) = 0.707
(i) .'.
VGS = - 1.76 V
(ii) and
VP = - VGS (off) = 6 V

Q4. For the JFET in Fig. 2, VGS (off) = – 4V and IDSS = 12 mA. Determine the minimum value of VDD required to put the device in the constant-current region of operation.

[Circuit diagram: Fig. 2 — n-channel JFET with Gate connected to ground (0 V), Source connected to ground (0 V), and Drain connected through resistor RD = 560 Ω to the positive terminal of DC supply VDD whose negative terminal is connected to ground.]

## page 3

Fig.2

Solution. Since VGS (off) = - 4V, VP = 4V. The minimum value of VDS for the JFET to be in constant-current region is
VDS = VP = 4V
In the constant current region with VGS = 0V,
ID = IDSS = 12 mA
Applying Kirchhoff's voltage law around the drain circuit, we have,
VDD = VDS + VRD = VDS + ID RD
    = 4V + (12 mA) (560Ω) = 4V + 6.72V = 10.72V
This is the value of VDD to make VDS = VP and put the device in the constant-current region.

Q5. Determine the value of drain current for the circuit shown in Fig. 3.

[Circuit diagram: Fig. 3 — n-channel JFET with parameters VGS (off) = - 6 V, IDSS = 3 mA; Drain connected through an unlabeled resistor to supply terminal + VDD; Source connected to ground; Gate connected to DC source labeled VGS = 2 V with positive terminal grounded.]

Fig.3

Solution. It is clear from Fig. 3 that VGS = - 2V. The drain current for the circuit is given by;

ID = IDSS (1 - VGS / VGS (off))^2
   = 3 mA (1 - -2V / -6V)^2
   = (3 mA) (0.444) = 1.33 mA

Q6. When a reverse gate voltage of 15 V is applied to a JFET, the gate current is 10-3 μA. Find the resistance between gate and source.

Solution.

[UI navigation: 4/23]

## page 4

VGS = 15 V ; IG = 10^-3 μA = 10^-9 A

.'. Gate to source resistance = VGS / IG = 15 V / 10^-9 A = 15 × 10^9 Ω = 15,000 MΩ

Q7. When VGS of JFET changes from –3.1 V to –3 V, the drain current changes from 1 mA to 1.3 mA. What is the value of transconductance?

Solution.
ΔVGS = 3.1 - 3 = 0.1 V    ... magnitude
ΔID = 1.3 - 1 = 0.3 mA
.'. Transconductance, gfs = ΔID / ΔVGS = 0.3 mA / 0.1 V = 3 mA/V = 3000 μ mho

Q8. A JFET has a value of gmo = 4000 μS. Determine the value of gm at VGS = – 3V. Given that VGS (off) = – 8V.

Solution.
gm = gmo (1 - VGS / VGS (off))
   = 4000 μS (1 - -3V / -8V)
   = 4000 μS (0.625) = 2500 μS

Q9. The datasheet of a JFET gives the following information: IDSS = 3 mA, VGS (off) = – 6V and gm(max) = 5000 μS. Determine the transconductance for VGS = – 4V and find drain current ID at this point.

Solution. At VGS = 0, the value of gm is maximum i.e. gmo.
.'. gmo = 5000 μS

Now
gm = gmo (1 - VGS / VGS (off))
   = 5000 μS (1 - -4V / -6V)
   = 5000 μS (1/3) = 1667 μS

Also
ID = IDSS (1 - VGS / VGS (off))^2
   = 3 mA (1 - -4 / -6)^2 = 333 μA

[UI navigation: 5/23]

## page 5

Q10. A JFET in Fig. 4 has values of VGS (off) = – 8V and IDSS = 16 mA. Determine the values of VGS, ID and VDS for the circuit.

[Circuit diagram: Fig. 4 — n-channel JFET fixed-bias circuit: Gate connected via resistor RG = 1 MΩ to supply -5 V and through an input coupling capacitor to an input terminal; Drain connected via resistor RD = 2.2 kΩ to supply +10 V and through an output coupling capacitor to an output terminal; Source connected directly to ground.]

Fig. 4

Solution.

Since there is no gate current, there will be no voltage drop across RG.

.'. VGS = VGG = - 5V

Now
ID = IDSS (1 - VGS / VGS (off))^2
   = 16 mA (1 - -5 / -8)^2
   = 16 mA (0.1406) = 2.25 mA

Also
VDS = VDD - ID RD
    = 10 V - 2.25 mA × 2.2 kΩ = 5.05 V

Note that operating point for the circuit is 5.05V, 2.25 mA

Q11. Find VDS and VGS in Fig. 5, given that ID = 5 mA.

## page 6

[Circuit diagram: Fig. 5 — n-channel JFET self-bias circuit: Drain connected via resistor RD = 1 kΩ to supply VDD = + 15 V; Source connected via resistor RS = 470 Ω to ground; Gate connected via resistor RG to ground, with gate voltage labeled VG = 0 V.]

Fig. 5

Solution.
VS = ID RS = (5 mA) (470 Ω) = 2.35 V
and
VD = VDD - ID RD
   = 15V - (5 mA) × (1 kΩ) = 10V
.'.
VDS = VD - VS = 10V - 2.35 V = 7.65V

Since there is no gate current, there will be no voltage drop across RG and VG = 0.
Now
VGS = VG - VS = 0 - 2.35V = - 2.35 V

Q12. The transfer characteristic of a JFET reveals that when VGS = – 5V, ID = 6.25 mA. Determine the value of RS required.

Solution.
RS = |VGS| / |ID| = 5V / 6.25 mA = 800 Ω

Q13. Determine the value of RS required to self-bias a p-channel JFET with IDSS = 25 mA, VGS (off) = 15 V and VGS = 5V.

Solution.

## page 7

ID = IDSS (1 - VGS / VGS (off))^2 = 25 mA (1 - 5V / 15V)^2 = 25mA (1 - 0.333)^2 = 11.1 mA
.'. RS = |VGS| / |ID| = 5V / 11.1 mA = 450 Ω

Q14. Select resistor values in Fig. 6 to set up an approximate midpoint bias. The JFET parameters are : IDSS = 15 mA and VGS (off) = – 8V. The voltage VD should be 6V (one-half of VDD).

[Circuit diagram: Fig. 6 — n-channel JFET self-bias circuit: Drain connected through resistor RD to supply VDD = + 12 V; Source connected through resistor RS to ground; Gate connected through resistor RG to ground.]

Fig.6

Solution. For midpoint bias, we have,
ID ~= IDSS / 2 = 15 mA / 2 = 7.5 mA
and
VGS ~= VGS (off) / 3.4 = -8 / 3.4 = - 2.35 V
.'.
RS = |VGS| / |ID| = 2.35V / 7.5 mA = 313Ω
Now
VD = VDD - ID RD
.'.
RD = (VDD - VD) / ID = (12V - 6V) / 7.5 mA = 800Ω

## page 8

Q15. In a self-bias n-channel JFET, the operating point is to be set at ID = 1.5 mA and VDS = 10 V. The JFET parameters are IDSS = 5 mA and VGS (off) = – 2 V. Find the values of RS and RD. Given that VDD = 20 V.

Solution. Fig. 7 shows the circuit arrangement.

[Circuit diagram: Fig. 7 — n-channel JFET self-bias circuit: Drain connected via resistor RD with current ID pointing down to supply + VDD = 20 V; Drain-to-Source voltage indicated as VDS; Source connected to parallel combination of source resistor RS (with current ID) and bypass capacitor CS to ground, with voltage VS indicated across RS; Gate connected via resistor RG to ground with an input terminal on the left.]

Fig.7

## page 9

ID = IDSS (1 - VGS / VGS (off))^2
or
1.5 = 5 (1 + VGS / 2)^2
or
1 + VGS / 2 = sqrt(1.5 / 5) = 0.55
or
VGS = - 0.9 V
Now
VGS = VG - VS
or
VS = VG - VGS
   = 0 - (-0.9) = 0.9 V
.'.
RS = VS / ID = 0.9 V / 1.5 mA = 0.6 k Ω

Applying Kirchhoff's voltage law to the drain circuit, we have,
VDD = ID RD + VDS + ID RS
or
20 = 1.5 mA × RD + 10 + 0.9
.'.
RD = (20 - 10 - 0.9) V / 1.5 mA = 6 k Ω

Q16. In the JFET circuit shown in Fig. 8, find (i) VDS and (ii) VGS.

[Circuit diagram: Fig. 8 — n-channel JFET circuit: Drain terminal D connected through resistor RD = 5 kΩ with drain current ID = 2.5 mA to supply + VDD = 30 V; Source terminal S connected through parallel combination of resistor RS = 200 Ω and bypass capacitor CS to ground; Gate connected directly to ground (0 V).]

Fig.8

Solution.
(i) VDS = VDD - ID (RD + RS) = 30 - 2.5 mA (5 + 0.2) = 30 - 13 = 17 V
(ii) VGS = - ID RS = - (2.5 × 10^-3) × 200 = - 0.5 V

## page 10

Q17. Determine ID and VGS for the JFET with voltage-divider bias in Fig. 9, given that VD = 7V.

[Circuit diagram: Fig. 9 — n-channel JFET voltage-divider bias circuit: Voltage divider on left consisting of R1 = 6.8 MΩ connected from VDD = + 12 V to Gate, and R2 = 1 MΩ connected from Gate to ground; Drain connected via resistor RD = 3.3 kΩ to VDD = + 12 V; Source connected via resistor RS = 1.8 kΩ to ground.]

Fig.9

Solution.

ID = (VDD - VD) / RD = (12V - 7V) / 3.3 kΩ
   = 5V / 3.3 kΩ = 1.52 mA

VS = ID RS = (1.52 mA) (1.8 kΩ) = 2.74V

VG = (VDD / (R1 + R2)) × R2 = (12V / 7.8 MΩ) × 1 MΩ = 1.54V

.'. VGS = VG - VS = 1.54 V - 2.74 V = - 1.2V

Q18. In an n-channel JFET biased by potential divider method, it is desired to set the operating point at ID = 2.5 mA and VDS = 8V. If VDD = 30 V, R1 = 1 MΩ and R2 = 500 kΩ, find the value of RS. The parameters of JFET are IDSS = 10 mA and VGS (off) = – 5 V.

## page 11

Solution. Fig. 10 shows the conditions of the problem.

[Circuit diagram: Fig. 10 — n-channel JFET voltage-divider bias circuit: Voltage divider with R1 = 1 MΩ from + VDD = 30 V to Gate, and R2 = 500 kΩ from Gate to ground with voltage across R2 labeled V2; Drain connected via resistor RD with current ID = 2.5 mA to + 30 V; Drain-to-Source voltage labeled VDS = 8V; Gate-to-Source voltage labeled VGS; Source connected to parallel combination of resistor RS and bypass capacitor CS to ground.]

Fig.10

ID = IDSS (1 - VGS / VGS (off))^2
or
2.5 = 10 (1 + VGS / 5)^2
or
1 + VGS / 5 = sqrt(2.5 / 10) = 0.5
or
VGS = - 2.5 V

Now,
V2 = (VDD / (R1 + R2)) × R2
   = (30 / (1000 + 500)) × 500
   = 10 V

Now
V2 = VGS + ID RS
or
10 V = - 2.5 V + 2.5 mA × RS
.'.
RS = (10 V + 2.5 V) / 2.5 mA = 12.5 V / 2.5 mA
   = 5 kΩ

---

## Done Report

- **File written**: `C:/Users/bhomi/AppData/Local/Temp/claude/6e81c002d1e3bfcd/bd6f37ef-47e2-42fc-83d1-906fe62e205d/scratchpad/edc-e0/out/num34a.md`
- **Sections transcribed**: Pages 1 through 11 (`## page 1` to `## page 11`)
- **Counts**:
  - Questions covered: 17 questions/solutions transcribed (Q2 through Q18; Q1 absent from source document)
  - Circuit diagrams described: 9 circuits (Fig. 2 on page 2/3, Fig. 3 on page 3, Fig. 4 on page 5, Fig. 5 on page 6, Fig. 6 on page 7, Fig. 7 on page 8, Fig. 8 on page 9, Fig. 9 on page 10, Fig. 10 on page 11)
  - Tables: 0 (source document contains no data tables in pages 1–11)
- **Unreadable items**: None
- **Every `[?]`**: None (all equations, symbols, values, and circuit component labels were clear and legible)
- **Noted anomalies**:
  - Page 1 starts directly at Q2; Q1 is absent from the sheet.
  - Page 3, Q6: Question statement text prints "10-3 μA" where "10^-3 μA" is meant (transcribed faithfully as "10-3 μA"; solution on page 4 writes "10^-3 μA").
  - Page 3, Fig. 3: Drain resistor has no label or component value indicated on the schematic.
