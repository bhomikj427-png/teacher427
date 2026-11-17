## page 12

Q19. Draw the d.c. load line for the JFET amplifier shown in Fig. 11.

[Circuit: JFET amplifier with DC supply +V_DD = 20 V; drain resistor R_D = 500 Ω; output coupling capacitor C_C connected to drain; AC input coupling capacitor C_in connected to gate; gate resistor R_G connected in series with DC reverse-bias supply V_GG to ground; source connected directly to ground.]
Fig.11

Solution.

Max. V_DS = V_DD = 20V
This locates the point B (OB = 20V) of the d.c. load line.

Max. I_D = V_DD / R_D = 20V / 500Ω = 40 mA
This locates the point A (OA = 40 mA) of the d.c. load line.

Fig. 12 shows the d.c. load line AB.

[Graph: d.c. load line plotted on I_D vs V_DS axes; vertical axis I_D with point A at 40 mA; horizontal axis V_DS with point B at 20V; origin marked O; straight line AB connects point A (0, 40 mA) to point B (20V, 0).]
Fig.12

## page 13

Q20. The JFET in the amplifier of Fig. 13 has a transconductance gm = 1 mA/V. If the source resistance RS is very small as compared to RG, find the voltage gain of the amplifier.

[Circuit: JFET common-source amplifier with +V_DD = 20V; drain resistor R_D = 12 kΩ; drain coupled through capacitor C_c to load resistor R_L = 8 kΩ connected to ground with terminal OUTPUT across R_L; AC SIGNAL source connected in series with C_in to gate; gate resistor R_G = 1 MΩ from gate to ground; source connected to ground through source resistor R_S in parallel with bypass capacitor C_S.]
Fig.13

Solution.

Transconductance of JFET, gm = 1 mA/V
= 1000 μ mho = 1000 × 10^-6 mho

The total ac load (i.e. R_AC) in the drain circuit consists of the parallel combination of R_D and R_L i.e.
Total a.c. load, R_AC = R_D || R_L
= 12 kΩ || 8 kΩ = (12 × 8) / (12 + 8) = 4.8 kΩ

∴ Voltage gain, A_v = g_m × R_AC
= (1000 × 10^-6) × (4.8 × 10^3) = 4.8

Q21. The transconductance of a JFET used as a voltage amplifier is 3000 μmho and drain resistance is 10 kΩ. Calculate the voltage gain of the amplifier.

Solution.

Transconductance of JFET, g_m = 3000 μmho = 3000 × 10^-6 mho
Drain resistance, R_D = 10 kΩ = 10 × 10^3 Ω
∴ Voltage gain, A_v = g_m R_D = (3000 × 10^-6) (10 × 10^3) = 30

Q22. What is the r.m.s. output voltage of the unloaded amplifier in Fig. 14? The IDSS = 8 mA, VGS (off) = - 10V

## page 14

and ID = 1.9 mA.

[Circuit: JFET self-biased amplifier with V_DD = + 12 V; drain resistor R_D = 3.3 kΩ; output terminal v_out taken from drain; gate connected to AC input v_in = 100 mV (r.m.s.) through coupling capacitor C_1; gate resistor R_G = 10 MΩ to ground; source connected to ground through R_S = 2.7 kΩ bypassed by capacitor C_2 = 10 μF.]
Fig.14

Solution.

V_GS = - I_D R_S = - 1.9 mA × 2.7 × 10^3 Ω = - 5.13V
g_mo = (2 I_DSS) / |V_GS(off)| = (2 × 8 mA) / (10 V) = 1.6 × 10^-3 S
∴ g_m = g_mo [1 - V_GS / V_GS(off)] = 1.6 × 10^-3 [1 - (-5.13V / -10V)] = 779 × 10^-6 S
Voltage gain, A_v = g_m R_D = (779 × 10^-6) (3.3 × 10^3) = 2.57
∴ Output voltage, v_out = A_v v_in = 2.57 × 100 mV = 257 mV (r.m.s.)

Q23. If a 4.7 kΩ load resistor is a.c. coupled to the output of the amplifier in Fig. 15 , what is the resulting r.m.s. output voltage?

[Circuit: JFET amplifier identical to Fig. 14; V_DD = + 12 V; drain resistor R_D = 3.3 kΩ; output terminal v_out; gate connected to AC input v_in = 100 mV (r.m.s.) via C_1 and gate resistor R_G = 10 MΩ to ground; source connected to ground through R_S = 2.7 kΩ bypassed by capacitor C_2 = 10 μF.]

## page 15

Solution.

The value of gm remains the same. However, the value of total a.c. drain resistance RAC changes due to the connection of load RL (= 4.7 kΩ).

Total a.c. drain resistance, RAC = RD || RL
= (R_D R_L) / (R_D + R_L) = ((3.3 kΩ) (4.7 kΩ)) / (3.3 kΩ + 4.7 kΩ) = 1.94 kΩ
∴ Voltage gain, A_v = g_m R_AC = (779 × 10^-6) (1.94 × 10^3) = 1.51
Output voltage, v_out = A_v v_in = 1.51 × 100 mV = 151 mV (r.m.s.)

Q24. In a JFET amplifier, the source resistance RS is unbypassed. Find the voltage gain of the amplifier. Given gm = 4 mS; RD = 1.5 kΩ and RS = 560Ω.

Solution.
Voltage gain, A_v = (g_m R_D) / (1 + g_m R_S)
Here g_m = 4mS = 4 × 10^-3 S ; R_D = 1.5 kΩ = 1.5 × 10^3 Ω ; R_S = 560Ω

∴ A_v = ((4 × 10^-3) (1.5 × 10^3)) / (1 + (4 × 10^-3) (560)) = 6 / (1 + 2.24) = 1.85

If R_S is bypassed by a capacitor, then,
A_v = g_m R_D = (4 × 10^-3) (1.5 × 10^3) = 6

Thus with unbypassed RS, the gain = 1.85 whereas with RS bypassed by a capacitor, the gain is 6. Therefore, voltage gain is reduced when RS is unbypassed.

Q25. For the JFET amplifier circuit shown in Fig. 16, calculate the voltage gain with (i) RS bypassed by a capacitor (ii) RS unbypassed.

https://electronicspost.com/solved-problems-on-field-effect-transistors/ 16/23

## page 16

[Circuit: JFET amplifier with DC supply V_DD = + 9 V; drain resistor R_D = 1.5 kΩ; output v_out coupled via capacitor C_2 from drain; AC input v_in coupled via capacitor C_1 to gate; gate resistor R_G to ground; source resistor R_S = 750 Ω in parallel with bypass capacitor C_S to ground; JFET Data: I_DSS = 10 mA, V_GS(off) = - 3.5V.]
Fig.16

Solution. From the d.c. bias analysis, we get, *I_D = 2.3 mA and V_GS = - 1.8V.
The value of g_m is given by;
g_m = (2 I_DSS / |V_GS(off)|) (1 - V_GS / V_GS(off))
= ((2 × 10) / 3.5) (1 - (-1.8 / -3.5)) = (5.7 mS) (0.486) = 2.77 mS

(i) The voltage gain with R_S bypassed is
A_v = g_m R_D = (2.77 mS) (1.5 kΩ) = 4.155

(ii) The voltage gain with R_S unbypassed is
A_v = (g_m R_D) / (1 + g_m R_S) = 4.155 / (1 + (2.77 mS) (0.75 kΩ)) = 1.35

## page 17

Q26. For a certain D-MOSFET, IDSS = 10 mA and VGS (off) = - 8V.
(i) Is this an n-channel or a p-channel ?
(ii) Calculate ID at VGS = - 3V.
(iii) Calculate ID at VGS = + 3V.

Solution.
(i) The device has a negative V_GS (off). Therefore, it is n-channel D-MOSFET.

(ii) I_D = I_DSS (1 - V_GS / V_GS(off))^2
= 10 mA (1 - (-3 / -8))^2 = 3.91 mA

(iii) I_D = I_DSS (1 - V_GS / V_GS(off))^2
= 10 mA (1 - (+ 3V / - 8V))^2 = 18.9 mA

Q27. A D-MOSFET has parameters of VGS (off) = - 6V and IDSS = 1 mA. How will you plot the transconductance curve for the device?

Solution.

When VGS = 0 V, ID = IDSS = 1 mA and when VGS = VGS (off), ID = 0A. This locates two points viz IDSS and VGS (off) on the transconductance curve. We can locate more points of the curve by changing VGS values.

## page 18

When V_GS = - 3V ; I_D = 1 mA (1 - (-3V / -6V))^2 = 0.25 mA
When V_GS = - 1V ; I_D = 1 mA (1 - (-1V / -6V))^2 = 0.694 mA
When V_GS = + 1V ; I_D = 1 mA (1 - (+1V / -6V))^2 = 1.36 mA
When V_GS = + 3V ; I_D = 1 mA (1 - (+3V / -6V))^2 = 2.25 mA

Thus we have a number of VGS - ID readings so that transconductance curve for the device can be readily plotted.

Q28. Determine the drain-to-source voltage (VDS) in the circuit shown in Fig. 17 if VDD = +18V and RD = 620Ω. The MOSFET data sheet gives VGS (off) = - 8V and IDSS = 12 mA.

[Circuit: D-MOSFET circuit with zero bias; drain resistor R_D = 620 Ω connected to DC supply +V_DD = +18V; drain current indicated as I_DSS; gate connected to ground through R_G, V_G = 0V; source connected to ground; gate-to-source voltage marked V_GS = 0.]
Fig.17

Solution. Since I_D = I_DSS = 12 mA, the V_DS is given by;
V_DS = V_DD - I_DSS R_D
= 18V - (12 mA) (0.62 kΩ) = 10.6V

## page 19

Q29. The D-MOSFET used in the amplifier of Fig. 18 has an IDSS = 12 mA and gm = 3.2 mS. Determine (i) d.c. drain-to-source voltage VDS and (ii) a.c. output voltage. Given vin = 500 mV.

[Circuit: D-MOSFET amplifier circuit with zero bias; drain connected through R_D = 620 Ω to +V_DD = + 15 V; coupling capacitor C_2 from drain to output terminal v_out with load resistor R_L = 8.2 kΩ connected to ground; AC input v_in coupled through C_1 to gate; gate resistor R_G = 10 MΩ to ground; source connected directly to ground.]
Fig.18

Solution.
(i) Since the amplifier is zero biased, I_D = I_DSS = 12 mA.
∴ V_DS = V_DD - I_DSS R_D
= 15V - (12 mA) (0.62 kΩ) = 7.56V

(ii) Total a.c. drain resistance R_AC of the circuit is
R_AC = R_D || R_L = 620Ω || 8.2 kΩ = 576Ω
∴ v_out = A_v × v_in = (g_m R_AC) (v_in)
= (3.2 × 10^-3 S × 576 Ω) (500 mV) = 922 mV

Q30. The data sheet for an E-MOSFET gives ID(on) = 500 mA at VGS = 10V and VGS (th) = 1V. Determine the drain current for VGS = 5V.

Solution. Here V_GS(on) = 10 V.
I_D = K (V_GS - V_GS(th))^2 ... (i)
Here K = I_D(on) / (V_GS(on) - V_GS(th))^2 = 500 mA / (10V - 1V)^2 = 6.17 mA/V^2
Putting the various values in eq. (i), we have,
I_D = 6.17 (5V - 1V)^2 = 98.7 mA

## page 20

Q31. The data sheet for an E-MOSFET gives ID (on) = 3 mA at VGS = 10V and VGS (th)= 3V. Determine the resulting value of K for the device. How will you plot the transconductance curve for this MOSFET ?

Solution. The value of K can be determined from the following equation :
K = I_D(on) / (V_GS(on) - V_GS(th))^2
Here I_D(on) = 3 mA ; V_GS(on) = 10V ; V_GS(th) = 3V
∴ K = 3 mA / (10V - 3V)^2 = 3 mA / (7V)^2 = 0.061 × 10^-3 A/V^2
Now I_D = K (V_GS - V_GS(th))^2
In order to plot the transconductance curve for the device, we shall determine a few points for the curve by changing the value of V_GS and noting the corresponding values of I_D.
For V_GS = 5V : I_D = 0.061 × 10^-3 (5V - 3V)^2 = 0.244 mA
For V_GS = 8V : I_D = 0.061 × 10^-3 (8V - 3V)^2 = 1.525 mA
For V_GS = 10V : I_D = 0.061 × 10^-3 (10V - 3V)^2 = 3 mA
For V_GS = 12V : I_D = 0.061 × 10^-3 (12V - 3V)^2 = 4.94 mA
Thus we can plot the transconductance curve for the E-MOSFET from these V_GS/I_D points.

Q31. Determine VGS and VDS for the EMOSFET circuit in Fig. 19. The data sheet for this particular MOSFET gives ID (on) = 500 mA at VGS = 10V and VGS (th) = 1V.
⚠ looks wrong: question number duplicated as Q31 (expected Q32)

[Circuit: E-MOSFET voltage-divider bias circuit; DC supply +V_DD = 24 V connected to voltage divider R_1 = 100 kΩ and R_2 = 15 kΩ to ground; gate connected between R_1 and R_2; drain resistor R_D = 470 Ω connected to +V_DD; source connected directly to ground.]
Fig.19

Solution. Referring to the circuit shown in Fig. 19, we have,

## page 21

V_GS = (V_DD / (R_1 + R_2)) × R_2
= 24V / ((100 + 15) kΩ) × 15 kΩ = 3.13V

The value of K can be determined from the following equation :
K = I_D(on) / (V_GS(on) - V_GS(th))^2
= 500 mA / (10V - 1V)^2 = 6.17 mA/V^2 [∵ [?] V_GS(on) = 10V]
∴ I_D = K (V_GS - V_GS(th))^2 = 6.17 mA/V^2 (3.13V - 1 V)^2 = 28 mA
∴ V_DS = V_DD - I_D R_D = 24V - (28 mA) (470Ω) = 10.8V

Q32. Determine the values of ID and VDS for the circuit shown in Fig. 20. The data sheet for this particular MOSFET gives ID (on) = 10 mA when VGS = VDS.
⚠ looks wrong: question number Q32 follows duplicated Q31

[Circuit: E-MOSFET drain-feedback bias circuit; drain connected to + 20 V supply through R_D = 1 kΩ; gate connected to drain through feedback resistor R_G = 5 MΩ; input terminal connected through a coupling capacitor to gate; output terminal connected through a coupling capacitor from drain; source connected directly to ground; label I_D(on) = 10 mA at drain-source.]
Fig.20

Solution. Since in the drain-feedback circuit V_GS = V_DS,
∴ I_D = I_D(on) = 10 mA
The value of V_DS (and thus V_GS) is given by :
V_DS = V_DD - I_D R_D
= 20V - (10 mA) (1 kΩ) = 20V - 10V = 10V

---

## Done report

- **Files written**:
  - `C:/Users/bhomi/AppData/Local/Temp/claude/6e81c002d1e3bfcd/bd6f37ef-47e2-42fc-83d1-906fe62e205d/scratchpad/edc-e0/out/num34b.md`
- **Sections**:
  - `## page 12`
  - `## page 13`
  - `## page 14`
  - `## page 15`
  - `## page 16`
  - `## page 17`
  - `## page 18`
  - `## page 19`
  - `## page 20`
  - `## page 21`
- **Counts**:
  - 10 pages transcribed (pages 12 to 21)
  - 14 question entries (Q19, Q20, Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28, Q29, Q30, Q31 [first], Q31 [second duplicate], Q32)
  - 10 circuit / graph diagram descriptions (Fig. 11, Fig. 12, Fig. 13, Fig. 14, Fig. 15, Fig. 16, Fig. 17, Fig. 18, Fig. 19, Fig. 20)
- **What could not read**: None (all text and equations clearly legible)
- **Every `[?]`**:
  - Page 21: `[∵ [?] V_GS(on) = 10V]` (leading symbol inside bracket is typeset as `∵` or `[:.` / `Q`)
