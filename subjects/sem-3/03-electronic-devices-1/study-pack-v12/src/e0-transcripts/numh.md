# Transcription: NUMERICALS-U5-h-parameter-book-pp131-145

## page 1

### Book page 131
Electronic Devices & Circuits | 131

Problem 3 : In a single stage amplifier the h-parameter
hic = 1.1 k , hrc ≈ 1 , hfc = - 51 , hoc = 25 µ A/V.
Calculate AI , Av , Avs , Ri & Ro for CC configuration with
Rs = RL = 10 k

Solution : AI = - hfc / (1 + hoc RL)
              = 51 / (1 + (25 × 10^-6 × 10 × 10^3)) = 40.8

Ri = hic + hrc AI RL = 409.1 k

Av = (AI RL) / Ri = (40.8 × 10^4) / (409.1 × 1000) = 0.997

Yo = hoc - (hfc hrc) / (hic + Rs)
   = 25 × 10^-6 + ((51)(1)) / (1100 + 10,000)
   = 4.62 × 10^-3 mho

Thus Ro = 1 / Yo = 216 Ω

Avs = (Av Ri) / (Ri + Rs) = (0.998 × 409.1) / (409.1 + 10) = 0.974.
⚠ looks wrong: Av was computed as 0.997 above, but 0.998 is substituted into the Avs formula.

Problem 4 : Draw the equivalent circuit for the CE and CC configurations subject to the restriction that RL = 0. Show that the input impedances of the two circuits are identical.

Solution :

Circuit description: CE hybrid model with input terminals B (+) and E (-), input voltage Vbe, input current Ib entering terminal B, input resistance Ri looking into B-E terminals; series resistor hie in the base branch, series controlled voltage source hre*Vce = 0; parallel branches between collector C and emitter E consisting of dependent current source hfe*Ib directed downwards, conductance hoe, and load resistor RL = 0 Ω in parallel across output terminals C and E.

---

## page 2

### Book page 132
132 | Electronic Devices & Circuits

Circuit description: CC hybrid model with input terminals B (+) and C (-), input voltage Vbc, input current Ib entering terminal B, input resistance Ri' looking into B-C terminals; series resistor hic in the base branch, series controlled voltage source hrc*Vec = 0; parallel branches between emitter E and collector C consisting of dependent current source hfc*Ib directed downwards, conductance hoc, and load resistor RL = 0 Ω connected across output terminals E and C.

Input resistance in CE
Ri = (Vbe / Ib) |_(Vce = 0)

By definition hie = (Vbe / Ib) |_(Vce = 0)

Hence Ri = hie
Similarly for CC configuration
Ri' = (Vbc / Ib) |_(Vec = 0) = hic
but we know that hie = hic
Hence Ri = Ri' .

Problem 5. : For any single-transistor amplifier prove that
Ri = hi / (1 - hr Av)

Solution : For single stage amplifier, input resistance
Ri = hi + hr AI RL
and Av = (AI RL) / Ri
∴ RL = (Av Ri) / AI
Substituting RL in the expression of Ri we get

### Book page 133
Electronic Devices & Circuits | 133

Ri = hi + hr AI ((Av Ri) / AI) = hi + hr Av Ri
∴ Ri = hi / (1 - hr Av)

Problem 6. : The circuit shown is an amplifier using a p-n-p transistor in parallel. The two transistors have identical characteristics. Find the expressions for the voltage gain and the input resistance of the amplifier, using the simplified hybrid model.

Circuit description: Two PNP transistors in parallel with their bases tied together to input Vi, collectors tied together to supply Vcc, and emitters tied together and connected to ground through load resistor Re with output voltage Vo taken across Re.

Solution : Drawing simplified hybrid model for both transistors.

Circuit description: Simplified hybrid model for the two parallel transistors showing base terminals B1 and B2 tied to input Vi with input current Ib splitting into ib1 and ib2; series resistor hie in each base-emitter arm meeting at common emitter node E; emitter resistor Re carrying current I to ground with output voltage Vo across Re; collectors C1 and C2 with dependent current sources hfe*ib1 and hfe*ib2 both feeding into emitter node E.

Vo = I Re = (ib1 + ib2 + hfe ib1 + hfe ib2) Re
∴ I Re = (ib/2 + ib/2 + hfe ib) Re

---

## page 3

### Book page 134
134 | Electronic Devices & Circuits

[ Since ib1 = ib2 = ib/2 for identical transistors ] .
∴ I Re = (1 + hfe) ib Re
Vi = ib1 hie + I Re [ Taking any one mesh ] .
Vi = (ib / 2) hie + (1 + hfe) ib Re = ib [ (hie / 2) + (1 + hfe) Re ] .

Hence input resistance
Ri = Vi / ib = (hie / 2) + (1 + hfe) Re

Voltage gain Av = Vo / Vi = ((1 + hfe) ib Re) / (ib [ (hie / 2) + (1 + hfe) Re ])
Av = (2 (1 + hfe) Re) / (hie + 2 (1 + hfe) Re) .

Problem 7. : For the circuit shown, find the voltage gain Vo / Vs and input impedance as a function of Rs , b , Re and RL . Assume that hoe (Re + RL) ≤ 0.1 .

Circuit description: NPN transistor amplifier circuit driven by voltage source Vs with series source resistance Rs connected to the base; collector connected to supply Vcc through resistor RL with output Vo taken between collector and ground; emitter connected to a tapped resistor consisting of upper section (1 - b)Re and lower section bRe to ground, with the lower terminal of source Vs connected to the tap between (1 - b)Re and bRe.

Solution : Since we assuming hoe (Re + RL) ≤ 0.1
The approximate h-parameter model can be used.
⚠ looks wrong: "Since we assuming" in the printed text is grammatically incomplete/incorrect for "Since we assume" or "Assuming".

### Book page 135
Electronic Devices & Circuits | 135

Circuit description: Small signal equivalent circuit of the amplifier with input source Vs in series with Rs connected to base terminal B, input resistance Ri looking into base; resistor hie between B and emitter terminal E; dependent current source hfe*Ib connected to collector C; load resistor RL connected between C and ground with output voltage Vo; resistor (1 - b)Re connected between E and the source return tap node; and resistor bRe connected from the tap node to ground.

Small signal equivalent circuit.

From the fig.
Voltage gain ,
Av = Vo / Vs = (- hfe Ib RL) / ([ Ib (Rs + hie) ] + [ hfe Ib (1 - b) Re + (1 - b) Re Ib ])
Av = (- hfe Ib RL) / (Ib [ (Rs + hie) + (1 + hfe) (1 - b) Re ])
Av = (- hfe RL) / ((Rs + hie) + (1 + hfe) (1 - b) Re)   ..... (1)

Input impedance
Ri = Vs / Ib = (Ib [ (Rs + hie) + (1 + hfe) (1 - b) Re ]) / Ib
   = Rs + hie + (1 + hfe) (1 - b) Re   .... (2)

Problem 8. : The cascade configuration shown is known as the tandem emitter follower. Find the input resistance Ri if hie = hre = hoe = 0 , and hfe is the same for each of the transistors Q1 to QN .

Circuit description: Tandem emitter follower consisting of N cascaded transistors Q1, Q2, ..., QN with collectors tied to common supply Vcc; input applied to base of Q1 with input resistance Ri; emitter of Q1 connected to base of Q2, and continuing to emitter of QN-1 connected to base of QN; emitter of QN connected to ground through load resistor Re.

---

## page 4

### Book page 136
136 | Electronic Devices & Circuits

Solution : For all the transistors shown in fig. hoe = 0 . So we can use approximate h-model for the configuration. ( hoe Re < 0.1) is satisfied.
Starting from the last transistor QN , the equivalent h-circuit will be as shown.

Circuit description: Small-signal equivalent h-parameter circuit for the last transistor QN with input voltage Vs, input current Ib entering base terminal B, series resistance hie = 0, emitter resistor Re connected to ground, dependent current source hfe*Ib directed into the emitter node from collector C, and input resistance RiN.

RiN = Vs / Ib = (Ib Re + hfe Ib · Re) / Ib = (1 + hfe) Re

Now taking last but one transistor QN - 1 , we can similarly prove that
RiN - 1 = (1 + hfe) [RiN] = (1 + hfe)^2 Re

Hence for N such transistors the value of input resistance
Ri = (1 + hfe)^N Re .

Problem 9. : A CE amplifier is driven by a voltage source of internal resistance Rs = 800 Ω . The load impedance is a resistance of 2 k Ω . The h-parameters are hie = 1.1 k , hfe = 50 , hoe = 25 µ ohms , hre = 2.5 × 10^-4 . Compute the current gain Ai , input resistance Ri , voltage gain Av , output resistance Ro and output terminal resistance Rot . Also calculate power gain Ap . Using (a) exact analysis (b) approximate analysis. Compute % error in Ai .
⚠ looks wrong: hoe unit is given as '25 µ ohms' instead of '25 µ mhos' (or µS).

Solution : (a) Exact analysis
(i) Current gain
Ai = - hfe / (1 + hoe RL) = - 50 / (1 + (25 × 10^-6 × 2000)) = - 47.6

(ii) Input resistance Ri = hie + hre Ai RL
= 1100 - (2.5 × 10^-4) × 47.6 × 2000

### Book page 137
Electronic Devices & Circuits | 137

= 1076.2 Ω = 1.0762 k Ω

(iii) Voltage gain Av = (Ai RL) / Ri = - 88.46

Overall voltage gain (i.e. including signal source ) Avs = (Av Ri) / (Ri + Rs)
= (- 88.46 × 1076.2) / (800 + 1076.2) = - 50.75

(iv) Output admittance Yo = hoe - (hre hfe) / (hie + Rs)
= 25 × 10^-6 - (2.5 × 10^-4 × 50) / (1100 + 800) = 18.42 µ ohms
⚠ looks wrong: Yo unit is printed as 'µ ohms' instead of 'µ mhos' (or µS).

∴ Ro = 1 / Yo = 54.28 k Ω

(v) Power gain Ap = Ai × Av = (- 47.6) (- 88.46) = 4210.6

(vi) Output terminal resistance Rot = Ro || RL = (54.28 × 2) / (54.28 + 2) = 1.92 k

(b) Approximate analysis.
Assume hre = hoe = 0

(i) Ai = - hfe / (1 + hoe RL) ≈ - hfe ≈ - 50
[ ∵ hoe since RL = 25 × 10^-6 × 2000 < 0.1 ]
⚠ looks wrong: text reads '[ ∵ hoe since RL = 25 × 10^-6 × 2000 < 0.1 ]', which is garbled typesetting for '[ ∵ since hoe * RL = 25 × 10^-6 × 2000 < 0.1 ]'.

(ii) Ri = hie + hre Ai RL ≈ hie ≈ 1100 Ω
[ ∵ Since hre Ai RL < 0.1 hie ]

(iii) Av = (Ai RL) / Ri ≈ (- hfe RL) / hie = - (50 × 2000) / 1100 ≈ - 90.91

Avs = (Av Ri) / (Rs + Ri) ≈ (Av × hie) / (Rs + hie) ≈ 52.62
⚠ looks wrong: Av is negative (-90.91), so Avs should be negative (-52.62); sign was dropped in the text.

(iv) Yo = 18.42 µ ohms ≈ 0 ohms
⚠ looks wrong: unit printed as 'ohms' instead of 'mhos'.

∴ Ro = 1 / Yo = 54.28 k (large value)

---

## page 5

### Book page 138
138 | Electronic Devices & Circuits

(v) Ap = Ai × Av = (- 50) (- 90.91) = 4545.5

(vi) Rot = Ro || RL ≈ 2.0 k (i.e. only RL neglecting Ro )

% error = ((Exact - approximate) / Exact value) × 100 %
% error in Ai = (- 47.6 - (- 50)) / 47.6 × 100 % = 5.04 %
⚠ looks wrong: denominator has positive 47.6 while numerator uses signed values (-47.6 - (-50)).

Problem 10. : For the transistor amplifier shown in fig. hie = 1.5 k , hfe = 100 , hre = 3 × 10^-4 , hoe = 25 µ mhos = 1 / (40k) . Calculate Ai , Ri , Av , Yo .

Circuit description: Single-stage BJT common-emitter amplifier with DC power supply +Vcc = 20V, voltage divider bias resistors R1 = 50k and R2 = 5k, collector load resistor Rc = 5k, AC-coupled load resistor RL = 10k, AC input voltage source Vs with series source resistance Rs = 1k connected to base terminal B, and emitter terminal E connected directly to ground.

Solution : The ac equivalent circuit is as follows.

Circuit description: AC equivalent circuit of the amplifier showing input source Vs with series resistor Rs = 1k, total base bias resistance Rb in parallel to ground, input resistance Ri looking into source/bias network, transistor base terminal B, input resistance Ri' looking into base, input voltage Vbe, base current Ib, emitter terminal E connected to ground, collector terminal C, collector current I, equivalent AC load resistance RL' = 3.3k connected from collector to ground, and output voltage Vce.

### Book page 139
Electronic Devices & Circuits | 139

RB = R1 || R2 = (R1 R2) / (R1 + R2) = 4.5 k
RL' = RL || Rc = (RL Rc) / (RL + Rc) = 3.3 k

(i) AiT ( Current gain of transistor )
= Ic / Ib = - hfe / (1 + hoe RL') = - 100 / (1 + (3.3 / 40)) = - 92.4

The overall current gain Ai = Ic / I = (Ic / Ib) · (Ib / I) = AiT × (Ib / I)
but Ib / I = RB / (RB + Ri')
Ri' = hie + hre AI RL' = 1.4 k
∴ Ib / I = 4.5 / (4.5 + 1.4) = 0.76
hence Ai = AiT × (Ib / I) = (- 92.4) (0.76) = - 70.2

(ii) Ri = RB || Ri' = (4.5 × 1.4) / (4.5 + 1.4) = 1.0 k

(iii) AvT = Vce / Vbe = (Ai RL') / Ri' = ((- 70.2) 3.3) / 1.4 = - 165.4

The overall voltage gain
Avs = Vce / Vs = (Vce / Vbe) · (Vbe / Vs) = AvT · (Vbe / Vs)
but Vbe / Vs = Ri / (Rs + Ri) = 1 / (1 + 1) = 0.5
∴ Av = Vce / Vs = (Vce / Vbe) · (Vbe / Vs) = (> 165.4) (0.5) =-82.7
⚠ looks wrong: typed as '(> 165.4)' instead of '(- 165.4)'.

(iv) Yo = hoe - (hre hfe) / (hie + Rs')
where Rs' = (Rs RB) / (Rs + RB) = 818.18 Ω
= 1.2 × 10^-5 mho = 12 µ mho

---

## page 6

### Book page 140
140 | Electronic Devices & Circuits

Problem 11. : An emitter follower with RL = 4k uses a single transistor having hie = 1.1 k , hre = 2.5 × 10^-4 , hfe = 50 , hoe = 25 µ ohms = 1 / 40 k . Estimate Ai , Ri , Av .
If the circuit is modified by using two transistors in Darlington connection, Estimate Ai , Ri & Av .
⚠ looks wrong: hoe unit is given as '25 µ ohms' instead of '25 µ mhos' (or µS).

Solution : (i) For single transistor
Ai = (1 + hfe) / (1 + hoe RL) = 46
Ri = hie + Ai RL = 185.1 k
Av = 1 - (hie / Ri) = 1 - (1.1 / 185.1) = 0.9941 .

(ii) For Darlington connection.
Ai = (1 + hfe)^2 / (1 + hoe hfe RL) = (1 + 50)^2 / (1 + (1 / 40) × 50 × 4) = 433.5
Ri1 = hie + Ai RL = 17.34 Mz
⚠ looks wrong: unit printed as 'Mz' instead of 'MΩ'.
Av1 = 1 - (hie / Ri1) = 0.9999 , Av2 = 1 - (hie / Ri2) = 0.9941
∴ Av = Av1 × Av2 = 0.9998 .

Problem 12. : For the bootstrap circuit shown, calculate Ai = Io / I1 , Ri and Av . The transistor parameters are hie = 2K , hfe = 100 , 1/hoe = 40K , and hre = 2.5 × 10^-4 .

Circuit description: Bootstrap emitter follower circuit supplied by Vcc, with base bias resistors of 4k and 4k in series, collector resistor of 3k, emitter resistor of 2k connected to ground, feedback bootstrap capacitor C connected between emitter and the junction of the two 4k base resistors, transistor Q with base, collector, and emitter, input current I1, output current Io, input voltage Vi, output voltage Vo, and input resistance Ri.

### Book page 141
Electronic Devices & Circuits | 141

Solution : The capacitor C will effectively provides short circuit for a.c. Hence the effective emitter resistance is
Re' = 2k || 4k || 4k = 1k
Since hoe (Rc + Re') = (1 / 40) (3 + 1) = 0.1
We can use approximate model.

Current gain Ai = Io / Ii = (Io / Ib) (Ib / Ii) = Ai' · (Ib / I1)
Io / Ib = Ai' ≈ - hfe (approximately)
≈ - 100

Ri' = Vi / Ib = hie + (1 + hfe) Re' = 103 k

The voltage gain Av' = 1 - (hie / Ri') = 1 - (2 / 103) = 0.9806

Transferring 10 k resistance to base and collector circuit respectively By Miller's theorem.
R1 = 10k / (1 - Av) = 10k / (1 - 0.9806) = 515 k
R2 = 10k / (1 - (1 / Av')) = - 500 k (This may be ignored)

The input resistance Ri = Ri' || R1 = 103 || 515 = 85.6 k
and Ai = Ai' · (Ib / I1) = - 100 (R1 / (R1 + Ri')) = - 83.2
and Av = - (RL / Ri') × Ai' = - (3 × 100) / 103 = - 2.91

Problem 13. : The transistor amplifier shown uses a transistor whose h parameters are given. Find Ai = Io / Ii , Av , Avs , Ro and Ri

Solution : Given that hie = 1.1K , hre = 2.5 × 10^-4
hfe = 50 , hoe = 25 µ A/V = 1 / (40K)

---

## page 7

### Book page 142
142 | Electronic Devices & Circuits

Let Ai' = Io / Ib = - hfe / (1 + hoe RL)
= - 50 / (1 + (5 / 40)) = - 44.5
and Ri' = hie + hre (Ai') RL
= 1.1K + 2.5 × 10^-4 (- 44.5) (5K) = 1.04 K

R12 = equivalent resistance of R1 and R2
= R1 || R2 = (R1 R2) / (R1 + R2) = 9.1 K

Circuit description (left): Practical CE transistor amplifier circuit with DC power supply Vcc, collector load resistor 5k, base potential divider resistors R1 = 100k and R2 = 10K, input AC source of internal resistance 10k connected to the base, grounded emitter, and output taken from collector.

Circuit description (right): AC equivalent circuit showing AC input source Vs with internal resistance Rs = 10k, input current Ii entering the node, parallel equivalent base bias resistance R12, base current Ib entering the base terminal of the transistor, emitter connected to ground, collector connected to load RL, input resistance Ri looking into the divider node, and input resistance Ri' looking into the base terminal.

Overall gain Ai = Io / Ii = (Io / Ib) · (Ib / Ii)
= Ai' · (R12 / (R12 + Ri')) = (- 44.5) · (9.1K / ((9.1 + 1.05) K))
Ai = - 39.9
Ri = R12 || Ri' = 9.1 K || 1.05 K = 941 Ω
Av = (Ai RL) / Ri = ((- 39.8) (5K)) / (0.941 K) = - 212
Overall voltage gain Avs = (Av Ri) / (Ri + Rs)
= (- 212 × (0.941)) / (0.941 + 10) = - 18.2

### Book page 143
Electronic Devices & Circuits | 143

Output admittance Yo = hoe - (hre · hfe) / (hie + (Rs || R12)) = 22.9 × 10^-6 mho
∴ Ro = 1 / Yo = 1 / (22.9 × 10^-6) = 43.7 K ohm

Problem 14. : For the amplifier shown, use standard h parameters. Compute Ai = Io / I1 , Av , Avs and Ri .

Solution : Replacing transistor by its equivalent low frequency model.

Circuit description (top): Transistor amplifier circuit with negative DC supply -Vcc, collector resistor RL = 5k, base bias divider resistors R1 = 100k and R2 = 10k, emitter resistor Re = 1k, AC source Vs with series resistance Rs = 10k coupled through capacitor to base, input current I1, output current Io, input resistance Ri, and output voltage Vo taken from collector to ground.

Circuit description (bottom): Low-frequency small-signal equivalent circuit of the amplifier showing input voltage source Vs with series resistor Rs, input current I1, parallel base resistance R12, base current Ib flowing into series base resistance hie, controlled voltage generator hre*Vce, emitter resistor Re = 1k carrying emitter current Ie to ground, dependent current source hfe*Ib in parallel with conductance hoe, output load resistor RL carrying output current Io, output voltage Vo, and voltage V1 defined from base terminal to ground.

R12 = R1 || R2 = (R1 R2) / (R1 + R2) = 9.1 K .
Load current - Io = hfe Ib + hoe Vce
- Io = 50 Ib + 25 × 10^-6 Vce   ..... (1)
but Vce = Vo - Ie Re = Vo - (Ib - Io) Re
Vce = Vo - 1000 (Ib - Io)   ..... (2)

---

## page 8

### Book page 144
144 | Electronic Devices & Circuits

Vo = Io RL = 5000 Io   ..... (3)
Substituting the value of Vo and Vce from equation (2) and (3) into (1).
- Io = 50 Ib + 25 × 10^-6 (5000 Io - 1000 Ib + 1000 Io)
- Io = 49.75 Ib + 0.15 Io or Io = - 43.3 Ib   ..... (4)

Again, V1 = hie Ib + hre Vce + (Ib - Io) Re
but from (2) (3) and (4)
Vce = 5000 (- 43.3 Ib) - 1000 (Ib + 43.3 Ib) = - 26.1 × 10^4 Ib   ..... (5)
∴ V1 = 1000 Ib + 2.5 × 10^-4 (- 26.1 × 10^4 Ib) + 44.3 × 1000 Ib
V1 = 45.3 × 10^3 Ib   ..... (6)
Ri' = V1 / Ib = 45.3 × 10^3 Ω
∴ Ai = Io / Ii = (Io / Ib) · (Ib / Ii)

From (4) Io / Ib = - 43.3
∴ Ai = - 43.3 (R12 / (R12 + Ri')) = - 43.3 (9.1 K / (91 K + 45.3 K))
⚠ looks wrong: the denominator in the original text substitutes '91 K' instead of '9.1 K' (even though R12 was given as 9.1 K).
= - 7.25
Ri = Ri' || R12 = 9.1 K || 45.3 K = 7.6 K
Av = (Ai RL) / Ri = - 4.77 .
Avs = Av · (Ri / (Ri + Rs)) = - 2.05

Problem 15. : Calculate Ri = Vs / Ii , Av and Ai = - Io / Ii for the circuit shown below. Use the h - parameter values as .
hic = 1.1 × 10^3 Ω , hrc = 1 , hfc = - 51 , hoc = 25 × 10^-6 A/V

### Book page 145
Electronic Devices & Circuits | 145

Circuit description: Darlington pair emitter follower amplifier comprising two cascaded transistors Q1 and Q2; common collector connection tied to positive DC supply Vcc; DC bias source VBB connected in series with AC input voltage source Vs to the base of Q1 with input current Ii entering the base; emitter of Q1 connected to base of Q2 carrying intermediate emitter current I with node voltage V1; emitter of Q2 connected to 1k emitter resistor to ground, carrying output current Io, with output voltage Vo taken across the 1k resistor.

Solution : Ai2 = - hfc / (1 + hoc RL) = - (- 51) / (1 + 25 × 10^-6 × 10^3)
= 51 / 1.025 = 49.75
Ri2 = hic + hrc Ai RL = 1.1 + 1 × 49.75 × 1 = 50.75 K
Av2 = Ai2 × (RL / Ri2) = 49.75 × (1 / 50.75) = 0.9803
Ai1 = - hfc / (1 + hoc RL) = - (- 51) / (1 + 25 × 10^-6 × 50.75 × 10^3)
= 51 / 2.268 = 22.48
Ri1 = 1.1 + 1 × 22.48 × 50.75 = 114.3 K
Av1 = Ai1 × (RL1 / Ri1) = 22.48 × (50.75 / 1142.3) = 0.999
⚠ looks wrong: denominator printed as '1142.3' instead of '114.3' or '114.3 K' (formula gives 22.48 * 50.75 / 1143 = 0.998).
∴ Av = Av1 Av2 = 0.999 × 0.9803 = 0.9793
Ai = Ai1 Ai2 = 22.48 × 49.75 = 1118

Problem 16. : For the circuit shown with transistor parameter as hie = 1100 Ω , hre = 2.5 × 10^-4 , hfe = 50 , hoe = 25 µ A / V. Calculate voltage gain.

---

## Done report (rule 8)
- Files written: `C:/Users/bhomi/AppData/Local/Temp/claude/6e81c002d1e3bfcd/bd6f37ef-47e2-42fc-83d1-906fe62e205d/scratchpad/edc-e0/out/numh.md`
- Sections transcribed: 8 page sections (`## page 1` through `## page 8`), covering 15 book pages (Book pp. 131–145) from `NUMERICALS-U5-h-parameter-book-pp131-145-p001.png` to `p008.png`.
- Counts:
  - Total problems transcribed: 14 problems (Problem 3 through Problem 16).
  - Total circuits described: 12 circuit / equivalent circuit models.
  - Total equations / calculation steps transcribed: ~65 equation blocks.
- What could not be read: None; all pages were fully legible.
- Every `[?]`: None.
- Errata / typesetting anomalies noted in source:
  - p. 131 (Problem 3): Av calculated as 0.997, but substituted as 0.998 in Avs formula.
  - p. 134 (Problem 7): "Since we assuming" grammatical error in source text.
  - p. 136 (Problem 9): hoe unit given as "25 µ ohms" instead of "25 µ mhos" (or µS).
  - p. 137 (Problem 9): Yo unit given as "18.42 µ ohms" instead of "µ mhos".
  - p. 137 (Problem 9): Approximate analysis reads "[ ∵ hoe since RL = 25 × 10^-6 × 2000 < 0.1 ]" (garbled typesetting for hoe * RL).
  - p. 137 (Problem 9): Avs sign dropped in approximate analysis (printed 52.62 instead of -52.62).
  - p. 138 (Problem 9): % error in Ai formula mixes signed values in numerator with positive value in denominator.
  - p. 139 (Problem 10): Typo `(> 165.4)` instead of `(- 165.4)`.
  - p. 140 (Problem 11): hoe unit given as "25 µ ohms" instead of "25 µ mhos".
  - p. 140 (Problem 11): Ri1 unit printed as "17.34 Mz" instead of "MΩ".
  - p. 144 (Problem 14): In Ai formula denominator, "91 K" substituted instead of "9.1 K".
  - p. 145 (Problem 15): In Av1 denominator, "1142.3" printed instead of "114.3".
