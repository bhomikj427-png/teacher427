# Feedback Amplifiers (Unit 6)

## slide 1

Feedback Amplifier
EDC

## slide 2

1.0 Classification of Amplifiers
Before proceeding with the concept of feedback it is useful to classify amplifiers into 4 basic categories based on their input & output signal relationships.
Voltage amplifier
Current  amplifier
Transconductance amplifier
Transresistance amplifier

## slide 3

1.1 Voltage amplifier

Circuit: Voltage amplifier equivalent circuit with signal source Vs in series with Rs connected across input resistance Ri (voltage Vi across Ri, condition Ri >> Rs); output has dependent voltage source Av * Vi in series with output resistance Ro connected across load resistance RL (output voltage Vo across RL, condition Ro << RL).

if Ri >> Rs
then Vi ≈ Vs
and if Ro << RL
then Vo ≈ Av * Vi ≈ Av * Vs
hence Av ≡ Vo / Vi
with RL = ∞
represent the open circuit voltage gain.

## slide 4

1.2 Current amplifier

Circuit: Current amplifier equivalent circuit with signal source Is in parallel with Rs connected across input resistance Ri (input current Ii into Ri, condition Ri << Rs); output has dependent current source Ai * Ii in parallel with output resistance Ro connected across load resistance RL (output current Io through RL, condition Ro >> RL).

if Ri << Rs
then Ii ≈ Is
and if Ro >> RL
then Io ≈ Ai * Ii ≈ Ai * Is
hence Ai ≡ Io / Ii
with RL = 0
represent the short circuit current gain.

## slide 5

1.3 Transconductance amplifier

Circuit: Transconductance amplifier equivalent circuit with signal source Vs in series with Rs connected across input resistance Ri (voltage Vi across Ri, condition Ri >> Rs); output has dependent current source Gm * Vi in parallel with output resistance Ro connected across load resistance RL (output current Io through RL, condition Ro >> RL).

if Ri >> Rs
then Vi ≈ Vs
and if Ro >> RL
then Io ≈ Gm * Vi ≈ Gm * Vs
hence Gm ≡ Io / Vi
with RL = 0
represent the short circuit mutual or
transfer conductance

## slide 6

1.4 Transresistance amplifier

Circuit: Transresistance amplifier equivalent circuit with signal source Is in parallel with Rs connected across input resistance Ri (input current Ii into Ri, condition Ri << Rs); output has dependent voltage source Rm * Ii in series with output resistance Ro connected across load resistance RL (output voltage Vo across RL, condition Ro << RL).

if Ri << Rs
then Ii ≈ Is
and if Ro << RL
then Vo ≈ Rm * Ii ≈ Rm * Is
hence Rm ≡ Vo / Ii
with RL = ∞
represent the open circuit mutual or
transfer resistance.

## slide 7

2.0 Feedback
Feedback is a technique where a proportion of the output of a system (amplifier) is fed back and recombined with input.
There are two types of feedback amplifier.
Positive feedback
Negative feedback
[Labels: input, output, A, β]

## slide 8

2.1 Positive Feedback
Positive feedback is the process when the output is added to the input, amplified again, and this process continues.
Example. In a PA system, you get feedback when you put the microphone in front of a speaker and the sound gets uncontrollably loud (you have probably heard this unpleasant effect. ⚠ looks wrong: missing closing parenthesis
[Labels: input, output, A, β, +]

## slide 9

2.2 Negative Feedback
Negative feedback is when the output is subtracted from the input.
Example. Speed control. If the car starts to speed up above the desired set-point speed, negative feedback causes the throttle to close, thereby reducing speed; similarly, if the car slows, negative feedback acts to open the throttle.
The use of negative feedback reduces the gain. Part of the output signal is taken back to the input with a negative sign.
[Labels: input, output, A, β, -]

## slide 10

3.0  Feedback Concept
Basic structure of a single - loop feedback amplifier

Diagram: Single-loop feedback amplifier block diagram with Signal source feeding Comparator or mixer network (input Vi, Ii) -> Basic amplifier (forward transfer gain A, output V, I) -> Sampling network -> External load RL (output Io = IL, Vo), with Feedback network (reverse transmission β, output Vf, If) connected between sampling network and mixer network; mixer, basic amplifier, sampling network, and feedback network enclosed in dashed box labeled Feedback amplifier.

## slide 11

3.1  Feedback Network
This block is usually a passive two-port network.
contain resistors, capacitors, and inductors.
Usually it is simply a resistive network.

Diagram: Single-loop feedback amplifier block diagram (same diagram as slide 10, highlighting Feedback network block with reverse transmission β).

## slide 12

3.2  Sampling Network
The output voltage is sampled by connecting the feedback network in
shunt  across the output.
Type of connection is referred to as voltage or shunt or node sampling.

Diagram: Sampling networks: (a) Voltage, shunt, or node sampling (voltage sampler connects feedback network β in parallel/shunt across basic amplifier A output and load RL with Io, Vo); (b) Current, series, or loop sampling (current sampler connects feedback network β in series with load RL with Io, Vo).

## slide 13

3.2  Sampling Network
The output current is sampled by connecting the feedback network in
series  with the output
Type of connection is referred to as current or series or loop sampling.

Diagram: Sampling networks: (a) Voltage, shunt, or node sampling; (b) Current, series, or loop sampling (same diagram as slide 12).

## slide 14

3.3  Comparator or Mixer Network
voltage - applied feedback
identified as voltage or series or loop mixing.

Diagram: Mixer networks: (a) Voltage, series, or loop mixing (series mixer connects source Vs in series with Rs and feedback voltage Vf across input Vi of basic amplifier A); (b) Current, shunt, or node mixing (shunt mixer connects source Is in parallel with Rs and feedback current If across input Ii of basic amplifier A).

## slide 15

3.3  Comparator or Mixer Network
current - applied feedback
identified as current or shunt or node mixing.

Diagram: Mixer networks: (a) Voltage, series, or loop mixing; (b) Current, shunt, or node mixing (same diagram as slide 14).

## slide 16

4.0  Feedback Amplifier Topologies
VOLTAGE SERIES
CURRENT SHUNT
CURRENT SERIES
VOLTAGE SHUNT

Diagram: Four feedback amplifier topologies: (a) voltage-sampling series-mixing (source Vs in series with Vf, basic voltage amplifier Vi, output Vo across RL, shunt feedback β); (b) current-sampling shunt-mixing (source Is in parallel with If, basic current amplifier Ii, output Io through RL and series feedback β); (c) current-sampling series-mixing (source Vs in series with Vf, basic transconductance amplifier Vi, output Io through RL and series feedback β); (d) voltage-sampling shunt-mixing (source Is in parallel with If, basic transresistance amplifier Ii, output Vo across RL, shunt feedback β).

## slide 17

5.0  Feedback Connection Types
Voltage-series feedback
Voltage-shunt feedback
Current-series feedback
Current-shunt feedback
There are four basic ways of connecting the feedback signal:

## slide 18

Fig. 3-2: Feedback amplifier types: (a) voltage-series feedback; (b) voltage-shunt feedback; (c) current-series feedback; (d) current-shunt feedback.
Series refers to connecting the feedback signal in series with the input signal voltage.
Shunt refers to connecting the feedback signal in shunt (parallel) with an input current source.

Diagram: Fig. 3-2 feedback connection circuits: (a) voltage-series (source Vs, input Vi, basic amplifier A = Vo / Vi, feedback β = Vf / Vo, Vf = β*Vo, load RL across Vo); (b) voltage-shunt (source Is, input current Ii, basic amplifier A = Vo / Ii, feedback β = If / Vo, If = β*Vo, load RL across Vo); (c) current-series (source Vs, input Vi, basic amplifier A = Io / Vi, feedback β = Vf / Io, Vf = β*Io, load RL and feedback in series carrying Io = IL); (d) current-shunt (source Is, input current Ii, basic amplifier A = Io / Ii, feedback β = If / Io, If = β*Io, load RL and feedback in series carrying Io = IL).

## slide 19

Series feedback connections tend to increase the
input resistance, whereas shunt feedback
connections tend to decrease the input resistance.
Voltage feedback tends to decrease the output
impedance, whereas current feedback tends to
increase the output impedance.

## slide 20

TABLE 3-1: Summary of Gain, Feedback, and Gain with Feedback
from Figure 3-2

| Feedback Connection | Gain without feedback A | Feedback β | Gain with feedback Af |
|---|---|---|---|
| Voltage-Series | A = Vo / Vi | β = Vf / Vo | Af = Vo / Vs |
| Voltage-Shunt | A = Vo / Ii | β = If / Vo | Af = Vo / Is |
| Current-Series | A = Io / Vi | β = Vf / Io | Af = Io / Vs |
| Current-Shunt | A = Io / Ii | β = If / Io | Af = Io / Is |

## slide 21

Voltage-Series Feedback
Figure 3-2 (a) below shows the voltage-series feedback connection with a part of the output voltage fed back in series with the input signal.

Diagram: Figure 3-2 (a) voltage-series feedback connection with source Vs, input Vi, basic amplifier A = Vo / Vi, load RL across Vo, and feedback network β = Vf / Vo providing Vf = β*Vo in series with input loop.

If there is no feedback (Vf = 0), the voltage gain of the amplifier is
A = Vo / Vs = Vo / Vi

If a feedback signal Vf is connected with the input in series, the overall voltage gain is
Af = Vo / Vs = A / (1 + β*A)    (3-1)

## slide 22

Input Impedance with Feedback
Voltage-Series Feedback
Fig. 3-3: A more detailed voltage-series feedback connection

Diagram: Fig. 3-3 detailed voltage-series feedback connection showing source Vs, input terminals with Ri and Vi, series feedback -Vf+, arrow showing input resistance Rif; amplifier output model has dependent voltage source A*Vi in series with Ro connected to load RL (voltage Vo); feedback network β = Vf / Vo with input Vo and output Vf = β*Vo; arrow showing output resistance Rof looking back into output terminals before RL.

The input impedance can be determined as follows:
Zif = Vs / Ii = Zi * (1 + β*A)    (3-3)

## slide 23

Output Impedance with Feedback
Voltage-Series Feedback
The output impedance for the connections of Fig. 3-2 is dependent on whether voltage or current feedback is used.
For voltage feedback, the output impedance is decreased, whereas current feedback increases the output impedance.
Referring to Fig. 3-3, the output impedance can be determined by applying a voltage V, resulting in a current I. Then the output resistance with feedback is
Zof = V / I = Zo / (1 + β*A)    (3-5)

## slide 24

Voltage-Shunt Feedback

Diagram: Fig. 3-2 (b) voltage-shunt feedback connection with current source Is, input current Ii entering basic amplifier A = Vo / Ii, output voltage Vo across load RL, and feedback network β = If / Vo feeding feedback current If = β*Vo in shunt with Is.

The gain with feedback for the network of Fig. 3-2 (b) is
Af = A / (1 + β*A)    (3-2)

## slide 25

Voltage-Shunt Feedback
Fig. 3-4: A more detailed voltage-shunt feedback connection

Diagram: Fig. 3-4 detailed voltage-shunt feedback connection with input current source Is in parallel with input resistance Ri (current Ii into amplifier), amplifier output equivalent circuit having dependent voltage source A*Ii in series with Ro connected across load RL (output Vo); feedback network β = If / Vo connected in shunt across Vo and feeding feedback current If = β*Vo in shunt at input node.

The input impedance can be determined to be:
Zif = Zi / (1 + β*A)    (3-4)
Zof = Zo / (1 + β*A)

## slide 26

Current-Series Feedback
Fig. 3-5: A more detailed current-series feedback connection

Diagram: Fig. 3-5 detailed current-series feedback connection showing input source Vs in series loop with input impedance Zi (Vi, Ii) and feedback voltage Vf = β*Io; amplifier output has dependent current source Io = A*Vi in parallel with Zo, connected in series with load RL (Vo) and feedback network β = Vf / Io.

The output impedance is determined as
Zof = V / I
Zof = Zo * (1 + β*A)    (3-6)

## slide 27

A summary of the effect of feedback on input and output impedance is provided in Table 3-2:

TABLE 3-2:

| Feedback Connection | Zif | Zof |
|---|---|---|
| Voltage-Series | Zi * (1 + β*A) (increased) | Zo / (1 + β*A) (decreased) |
| Current-Series | Zi * (1 + β*A) (increased) | Zo * (1 + β*A) (increased) |
| Voltage-Shunt | Zi / (1 + β*A) (decreased) | Zo / (1 + β*A) (decreased) |
| Current-Shunt | Zi / (1 + β*A) (decreased) | Zo * (1 + β*A) (increased) |

## slide 28

6.0 Negative Feedback Gain
The gain with feedback (or closed-loop gain) Af as follows:
Xo = A * Xi
Xf = β * Xo
Xi = Xs - Xf
Af = Xo / Xs = A / (1 + β*A)
[Labels: Xo, Xi, Xf, Xs, A, β, -]

The quantity βA is called the loop gain, and the quantity (1+βA)
is called the amount of feedback.

## slide 29

6.0 Advantages of Negative Feedback
1. Stabilization of gain
make the gain less sensitive to changes in circuit components e.g. due to changes in temperature.
2. Reduce non-linear distortion
make the output proportional to the input, keeping the gain constant, independent of signal level.
3. Reduce the effect of noise
minimize the contribution to the output of unwanted signals generated in circuit components or extraneous interference.

## slide 30

6.0 Advantages of Negative Feedback
4. Extend the bandwidth of the amplifier
Reduce the gain and increase the bandwidth
5. Modification the input and output impedances
raise or lower the input and output impedances by selection of the appropriate feedback topology.

## slide 31

6.1 Stabilization of Gain
Stabilization of the gain of an amplifier against changes in the components (e.g., with temperature, frequency)
If you represent the gain without feedback (the open loop gain) by Ao, then the system gain with negative feedback is
Af = Vout / Vin = Ao / (1 + Ao * β) ≈ 1 / β
where β is the fraction of the output which feeds back as a negative voltage at the input. The extent of this stabilizing influence can be illustrated as follows:

## slide 32

6.1 Stabilization of Gain

Table: Gain stabilization for B = .01

for B = .01

| Ao | Af = Ao / (1 + Ao * B) |
|---|---|
| 1,000 | 90.9 |
| 5,000 | 98.3 |
| 10,000 | 99.0 |
| 20,000 | 99.5 |

## slide 33

6.2 Decreasing Distortion/noise with Feedback
The use of negative feedback can discriminate against sources of noise or distortion within an amplifier.

Diagram: Two-stage amplifier with feedback loop: input Vin connects to summer V', first amplifier stage Ao1 with distortion vd1 added at output summer, intermediate node V'', second amplifier stage Ao2 with distortion vd2 added at output summer to output Vout; feedback block -B from Vout back to input summer V'.

## slide 34

6.2 Decreasing Distortion/noise with Feedback
showing that distortion within the feedback loop is discriminated
against, with more reduction of distortion which arises near the
output.

Diagram: Two-stage amplifier distortion model: input Vin -> summer V' -> [Ao1] -> (+) summer with vd1 -> V'' -> [Ao2] -> (+) summer with vd2 -> Vout, with feedback -B from Vout to V'.
Annotations:
- Callout on vd1: "Early distortion is more serious."
- Callout on vd2: "Most power amp distortion occurs late, so feedback is effective for reduction."
- Callout on vd1 term: "This distortion reduced by factor 1 / Ao1"
- Callout on vd2 term: "This distortion reduced by factor 1 / (Ao1 * Ao2)"
Equation:
Vout = [Ao1 * Ao2 / (1 + Ao1 * Ao2 * B)] * Vin + [Ao2 / (1 + Ao1 * Ao2 * B)] * vd1 + [1 / (1 + Ao1 * Ao2 * B)] * vd2

## slide 35

6.3  Increasing the Bandwidth

Graph: Frequency response plot of gain A vs frequency ω (log scale): upper curve "without feedback" with midband gain AM and 3 dB cutoff frequencies ωL and ωH; lower curve "with feedback" with reduced midband gain AMf (reduced by factor ÷ D), lower cutoff ωLf shifted lower (÷ D) to ωL / D, and upper cutoff ωHf shifted higher (x D) to ωH * D.

Af = Ao / (1 + Ao * β)

## slide 36

6.4  Modification of input and output impedance
i) Input Resistance
The input resistance with negative feedback will be raised for series or voltage mixing.

Diagram: Input resistance circuits: (a) Voltage, series, or loop mixing with source vs, current is, voltage vi across Ri of amplifier A, output xo = A*vi to Load, feedback block β outputs vf = β*xo in series with vs, showing Rif looking in; (b) Current, shunt, or node mixing with current source is, voltage vs across Ri, current ii into Ri, output xo = A*ii to Load, feedback block β outputs if = β*xo in parallel with is, showing Rif looking in.

Zi = Vi / Ii
Vi = Vs - Vf
Zif = Vs / Ii = Zi * (1 + β*A)

## slide 37

6.4  Modification of input and output impedance
i) Input Resistance
The input resistance with negative feedback will be lowered for shunt or current mixing.

Diagram: Input resistance circuits: (a) Voltage, series, or loop mixing; (b) Current, shunt, or node mixing (same diagram as slide 36).

Zi = Vi / Ii
Ii = Is - If
Zif = Vi / Is = Zi / (1 + β*A)

## slide 38

6.4  Modification of input and output impedance
ii) Output Resistance
The output resistance with negative feedback will be lowered for shunt or voltage sampling.

Diagram: Output resistance test circuit: summer receives Xs (= 0) and feedback Xf = β*vt to produce Xi into basic amplifier (modeled as dependent source A*Xi in series with Ro); test voltage source vt applied at output terminals with current it entering; feedback block β connected across vt (load disconnected, I = 0) feeding Xf = β*vt back to summer.

Let Xs = 0
replaced load with test voltage
Xi = -Xf = -β * vt
it = (vt - A * Xi) / Ro = (vt + β * A * vt) / Ro = vt * (1 + β * A) / Ro
Zof = vt / it = Ro / (1 + β * A)

## slide 39

6.4  Modification of input and output impedance
ii) Output Resistance
The output resistance with negative feedback will be raised for series or current sampling.
The output resistance with feedback for current
or series sampling to be:
Zof = Ro * (1 + β * A)

## slide 40

6.4  Modification of input and output impedance
Summary
For a series connection at input or output, the resistance is increased by (1+A) and
For a shunt connection at input or output, the resistance is lowered by (1+A).

## slide 41

7.0  Practical Feedback Circuits
Voltage-Series Feedback
Fig. 3-7: FET amplifier with voltage-series feedback.

Diagram: Fig. 3-7 JFET common-source amplifier with voltage-series feedback: drain connected to VDD via RD and ac-coupled via CD to output resistor divider R1 and R2 to ground; load Ro connected in parallel with (R1 + R2), output voltage Vo across Ro; feedback voltage Vf across R2 is connected in series loop with source Vs and gate-source voltage Vi; FET source terminal connected to ground.

The feedback voltage Vf is connected in series with the source signal Vs, their difference being the input signal Vi.
Without feedback the amplifier gain is
A = Vo / Vi = -gm * RL    (3-7)
where,
gm = transconductance
factor

## slide 42

Whereas RL is combination of resistors:
RL = RD || Ro || (R1 + R2) ≅ (Ro * RD) / (Ro + RD)
The feedback network provides a feedback factor of
β = Vf / Vo = -R2 / (R1 + R2)
Using the values of A and β, we find the gain with negative feedback to be
Af = A / (1 + β*A) = -gm * RL / [1 + (R2 * RL * gm) / (R1 + R2)]
If βA >> 1, we have
Af ≅ -1 / β = -(R1 + R2) / R2    (3-7) ⚠ looks wrong: slide reuses equation number (3-7) from slide 41

## slide 43

Current-Series Feedback
Fig. 3-8: (a) a single transistor amplifier circuit and (b) ac equivalent circuit without feedback

Diagram: Fig. 3-8: (a) single transistor amplifier circuit: NPN BJT with base resistor RB to +VCC, collector resistor RC to +VCC, unbypassed emitter resistor RE to ground; input source Vs ac-coupled via C1 to base (voltage Vi across base-emitter), output Vo at collector, feedback voltage Vf across RE resulting from emitter current Io; (b) ac equivalent circuit without feedback: input source Vs in parallel with RB and transistor input resistance hie (base current Ib into hie); collector has dependent current source hfe * Ib in parallel with RC, output current Io through RC, output voltage Vo across RC.

The feedback voltage VE is resulted in by the current through resistor RE.

## slide 44

Without Feedback
Referring to the Fig. 3-8 and summarized in Table 3-1, we have
A = Io / Vi = (-Ib * hfe) / (Ib * hie + Ib * RE) = -hfe / (hie + RE)    (3-8) ⚠ looks wrong: textbook equation (3-8) defines open-loop gain A as -hfe / (hie + RE) including RE in input loop, though slide title states "Without Feedback"
The input and output impedances are, respectively,
β = Vf / Io = -Io * RE / Io = -RE    (3-9) ⚠ looks wrong: slide lists feedback factor β equation right after "input and output impedances are, respectively"
Zi = RB || (hie + RE) ≅ hie + RE    (3-10)
Zo = RC    (3-11)

## slide 45

With Feedback
The input and output impedances are calculated as specified in Table 3-2,
Af = Io / Vs = A / (1 + β*A) = (-hfe / hie) / [1 + (-RE) * (-hfe / (hie + RE))] ≅ -hfe / (hie + hfe * RE)    (3-12)
Zif = Zi * (1 + β*A) ≅ hie * [1 + (hfe * RE) / hie] = hie + hfe * RE    (3-13)
Zof = Zo * (1 + β*A) = RC * [1 + (hfe * RE) / hie]    (3-14)

## slide 46

The voltage gain A with feedback is
Avf = Vo / Vs = (-Io * RC) / Vs = (Io / Vs) * RC = Af * RC ≅ (-hfe * RC) / (hie + hfe * RE)    (3-15)

## slide 47

Voltage-Shunt Feedback
Fig. 3-9: Voltage-shunt negative feedback amplifier: (a) constant-gain circuit; (b) equivalent circuit.

Diagram: Fig. 3-9: (a) constant-gain circuit: inverting op-amp configuration with non-inverting terminal (+) grounded, input voltage V1 connected via resistor R1 to inverting terminal (-), feedback resistor Ro connected from output Vo to inverting terminal; (b) equivalent circuit: Norton input current source Is = V1 / R1 in parallel with inverting input (input current Ii into op-amp, open-loop voltage gain ∞, non-inverting terminal grounded), feedback resistor Ro connected from output Vo back to inverting input carrying feedback current If; output voltage Vo.

Referring to Fig. 3-9 and Table 3-1 and the op-amp ideal characteristics Ii = 0, Vi = 0, and voltage gain of infinity, for a constant-gain we have:
A = Vo / Ii = ∞    (3-16)
β = If / Vo = -1 / Ro    (3-17)

## slide 48

The gain with feedback is then
Af = Vo / Is = Vo / Ii = A / (1 + β*A) = -1 / β = -Ro    (3-18)
The more usual gain is the voltage gain with feedback,
Avf = (Vo / Is) * (Is / V1) = (-Ro) * (1 / R1) = -Ro / R1    (3-19)

## slide 49

Fig. 3-10: Voltage-shunt feedback amplifier using an FET: (a) circuit; (b) equivalent circuit.

Diagram: Fig. 3-10: (a) circuit: JFET common-source amplifier with source resistor bypassed by capacitor to ground, drain connected via RD to +VCC, output Vo taken at drain; feedback resistor RF connected between drain and gate; input source Vs in series with RS connected to gate; (b) equivalent circuit: Norton input current source Is in parallel with RS (input current Ii into gate); feedback resistor RF connected from output Vo back to gate carrying feedback current If; small-signal JFET model with drain resistor RD in parallel with output Vo (source grounded).

## slide 50

With no feedback, Vf = 0,
A = Vo / Ii ≅ -gm * RD * RS    (3-20)
The feedback is,
β = If / Vo = -1 / RF    (3-21)
With feedback, the gain of the circuit is,
Af = Vo / Is = A / (1 + β*A) = (-gm * RD * RS) / [1 + (-1 / RF) * (-gm * RD * RS)]    (3-22)

## slide 51

Or,
Af = (-gm * RD * RS * RF) / (RF + gm * RD * RS)    (3-23)
The voltage gain of the circuit with feedback is then
Avf = (Vo / Is) * (Is / Vs) = [(-gm * RD * RS * RF) / (RF + gm * RD * RS)] * (1 / RS)
Avf = (-gm * RD * RF) / (RF + gm * RD * RS)    (3-24)

---

## Done report (Rule 8)
- **Files written:** `C:/Users/bhomi/AppData/Local/Temp/claude/6e81c002d1e3bfcd/bd6f37ef-47e2-42fc-83d1-906fe62e205d/scratchpad/edc-e0/out/fb.md`
- **Sections written:** `## slide 1` through `## slide 51` (51 slide sections in total)
- **Counts:**
  - 51 slides transcribed
  - 148 images processed (118 MathType equations, 24 PNG diagrams, 6 JPEG diagrams)
  - 3 markdown tables (Slide 20 Table 3-1, Slide 27 Table 3-2, Slide 32 Gain stabilization table)
  - 0 worked examples or numerical problem sets present in this slide deck
- **What could not be read:** None (every slide text, diagram, and equation was fully read and transcribed)
- **Every `[?]`:** None
- **Anomalies / `⚠ looks wrong`:**
  - Slide 8: Missing closing parenthesis in text `(you have probably heard this unpleasant effect.`
  - Slide 42: Reuses equation number `(3-7)` which was already assigned to `A = Vo / Vi = -gm * RL` on slide 41.
  - Slide 44: Equation (3-8) defines open-loop gain A as `-hfe / (hie + RE)` with RE included in the denominator, even though the slide heading is "Without Feedback". In addition, equation (3-9) for feedback factor β is listed under the line "The input and output impedances are, respectively," before equations (3-10) and (3-11).
