# Transcription: Multistage Amplifier and Darlington Connection (Slides 1–13)

## slide 1

MULTISTAGE AMPLIFIER

• INTRODUCTION:
• Generally ,voltage gain or power gain obtained from a single stage amplifier is less. Therefore in order to achieve greater voltage and power gain ,we have to use more than one stage of amplification.

• A circuit containing more than one stage of amplification is called multistage amplifier.

## slide 2

MULTISTAGE AMPLIFIER

Cascaded Connection
Output of one stage is connected to the input of another stage.

Circuit / diagram: Block diagram of two cascaded amplifier blocks where input signal Vin 1 enters Amplifier 1 (Gain = AV1) and its output Vo 1 connects to the input of Amplifier 2 (Gain = AV2), producing overall output Vo 2.

Amplifier 1
Gain = AV1
Vin 1
Vo 1

Amplifier 2
Gain = AV2
Vo 2

Overall gain AV = VO2 / Vin 1 = Av1 * AV2

## slide 3

MULTISTAGE AMPLIFIER

Circuit / diagram: Block diagram of three cascaded amplifier stages where input AC voltage source Vi feeds stage 1 of gain Av1 producing output V1, which feeds stage 2 of gain Av2 producing output V2, which feeds stage 3 of gain Av3 producing output V3, continuing to stage n producing output Vn.

A_V = A_V1 x A_V2 x A_V3 .......... x A_Vn

Where,
A_V1 = V_1 / V_i
A_V2 = V_2 / V_1
A_V3 = V_3 / V_2

■ Over all the voltage gain of a multistage amplifier is equal to the product of the gain of the individual stages.

## slide 4

Multistage amplifiers may be divided into following categories.

a) Compound amplifiers: In these amplifiers each stage may be different from others (one may be CB and other may be CC amplifier stage) and also different type of coupling may be employed.

b) Cascaded amplifier: In cascaded amplifier, each stage as well as the types of inter-stage coupling used is identical.

## slide 5

Cascaded BJT Amplifier

Circuit: Two-stage RC-coupled common-emitter BJT amplifier circuit with input Vi, coupling capacitor C1, stage 1 voltage divider bias resistors R1 and R2 connected to VCC, transistor Q1, collector resistor RC1 connected to VCC, emitter resistor RE1 bypassed by Cs1, stage 1 collector output V1o coupled via capacitor C2 to stage 2 voltage divider bias resistors R3 and R4 connected to VCC, transistor Q2, collector resistor RC2 connected to VCC, emitter resistor RE2 bypassed by Cs2, and overall collector output V2o.

Gain AV1 = V_1o / V_1 = - (R_C1 || R_L1) / r_e1 [? V_i or V_1 in denominator]
Gain AV2 = V_2o / V_1o = - (R_C2 || R_L2) / r_e2

## slide 6

Circuit 1: Complete two-stage cascaded RC-coupled CE BJT amplifier schematic with input Vi, input coupling capacitor C1, transistor Q1 biased by resistors R1, R2, RC1, and RE1 with bypass capacitor Cs1, stage 1 collector output V1O coupled through C2 to transistor Q2 biased by R3, R4, RC2, and RE2 with bypass capacitor Cs2, and output V2O taken across load resistor RL.
Circuit 2: Small-signal AC equivalent circuit model with input Vi across R1 || R2 feeding base terminal b with base current Ib1 into input resistance ri1 to emitter e, collector current source beta1*Ib1 (Ic1) at collector c in parallel with RC1, R3, R4, and stage 2 input resistance ri2 carrying base current Ib2 to emitter e, with stage 2 collector current source beta2*Ib2 at collector c in parallel with RC2 and load RL developing output V2O.

A_v1 = - (R_C1 || R_3 || R_4 || (beta_2 * r_e2)) / r_e1
A_v2 = - R_C2 / r_e2
A_v2 = - (R_C2 || R_L) / r_e2
Overall gain, A_v = A_v1 * A_v2

## slide 7

Why do we measure gain in dB?

• It allows us to denote, both very small as well as very large quantities of linear scale.

• The human ear responds to the intensity of sound which is used by logarithmic scale.

Note : The overall voltage gain of a multistage amplifier in decibels is given by

G_V = G_1 + G_2 + G_3 +......+ G_N
20 log_10 A_V = 20 log_10 A_V1 + 20 log_10 A_V2 + 20 log_10 A_V3 +.........+ 20 log_10 A_n

## slide 8

The purpose of coupling device is
1) To transfer AC output of the first stage to the input of the next stage.
2) To isolate the DC conditions of one stage from the next.

Types of coupling amplifiers:
1. RC coupling amplifier.
2. Direct coupling amplifier.
3. Transformer coupling amplifier.

## slide 9

Two stage R-C coupled transistor amplifier:

Circuit 1: Two-stage RC-coupled NPN transistor amplifier schematic with AC input source Vs (input sine waveform vi, AC), input coupling capacitor CB, stage 1 voltage divider resistors R1 and R2, transistor Q1, collector resistor RC to Vcc, emitter resistor RE with bypass capacitor CE1, collector output Vo1 (amplified, 180° inverted waveform) coupled via interstage capacitor CC1 to stage 2 voltage divider R1 and R2, transistor Q2, collector resistor RC to Vcc, emitter resistor RE with bypass capacitor CE2, collector output VCE coupled via capacitor CC2 across load resistor RL, producing amplified in-phase output waveform.

Advantages of RC coupling:
➤ It is inexpensive.
➤ It has good frequency response.
➤ It has low distortion.
➤ Overall gain is high.

Disadvantages of RC coupling:
• The gain is reduced because of loading effect.
• It cannot amplify very low frequency signal.
• Power loss due to large number of resistors.

Applications:
✓ Used as a voltage amplifiers such as radio and TV receivers.

Two stage direct coupled amplifier:

Circuit 2: Two-stage direct-coupled NPN transistor amplifier schematic with AC input source vi connected directly to base of first transistor biased by R1 and R2 to +VCC, collector resistor RC to +VCC, emitter resistor RE to ground, collector of first transistor connected directly to base of second transistor with collector resistor RC to +VCC and emitter resistor RE to ground, and output vo taken across collector of second transistor to ground, showing input, intermediate inverted, and final in-phase amplified waveforms.

This amplifier is also called as DC amplifier and is used to amplify very low frequencies including Direct current or zero frequency.

Working:
• The output of first stage is directly connected to the base of the next transistor.
• Moreover ,there is no input and output coupling capacitors.
• Required DC conditions of the first stage are obtained from R1 and R2 [along with Vcc].
• The DC voltage of first stage provides the required DC bias for the second stage.
• The signal to be amplified is applied directly to the input of the first stage. Due to transistor action, it appears in the amplified form across the collector resistor of transistor T1. This voltage then drives the base of the second transistor T [? T or T2]

Advantages:
• 1. The circuit arrangement is very simple.
• 2. The circuit cost is less.
• 3. It can amplify very low frequencies [even zero frequency].

Disadvantages:
• 1. It cannot amplify high frequency signals.
• 2. It has poor temperature stability.

Applications:
▪ Used in electrocardiogram, computers instrumentation amplifiers.
▪ Regulator circuits.

## slide 10

Frequency response of RC coupled amplifier

The curve drawn between voltage gain and the signal frequency of an amplifier is known as frequency response.

Graph 1: Frequency response curve of an RC coupled amplifier showing voltage Gain versus Frequency with peak midband gain AM, 3 dB down gain AM / sqrt(2) at lower cutoff frequency fL and upper cutoff frequency fU, bandwidth BW = fU - fL, and three designated regions: Low frequency region, Mid frequency region, and High frequency region.
Fig Frequency response curve

Frequency response of direct coupled amplifier

Graph 2: Frequency response curve of a direct-coupled amplifier showing Voltage gain versus Frequency starting flat from 0 (DC) at Av max up to corner frequency f2 where gain drops to Avmax / sqrt(2), and falling off at higher frequencies.

## slide 11

MILLER'S EFFECT

❖ History
✓ The Miller effect was named afterJohn Milton Miller .
✓ When Miller published his work in 1920,he was working onvacuum tube triodes , however the same theory applies to more modern devices such as BJT and FET.

❖ Definition
✓ The miller effect is the increase in effective capacitance at the input of an amplifier due to the voltage gain,causing bandwidth reduction and phase shift.

❖ Explanation
✓ Inelectronics, the Miller effect accounts for an increase in the equivalent input capacitance of aninverting voltageamplifier due to amplification of capacitance between the input and output terminals. Although
✓ Miller effect normally refers to capacitance, any impedance connected between the input and another node exhibiting high gain can modify the amplifier inputimpedance via the Miller effect.This increase in input capacitance is given by

C_M = C(1 - A_v)

where
A_v is the gain of the amplifier and C is the feedback capacitance.

[unreadable: top line cut off at image boundary]
I_i = (V_i - V_o) / Z = V_i(1 - A_v) / Z

✓ As this current flows through the impedance Z , this equation shows that because of the gain of the amplifier a huge current flows in Z ; in effect Z behaves as though it were much smaller than it is. The input impedance of the circuit is

Z_in = V_i / I_i = (V_i * Z) / (V_i(1 - A_v)) = Z / (1 - A_v)

✓ If Z represents a capacitor, then

Z = 1 / (j * omega * C)

and the resulting input impedance is

Z_in = 1 / (j * omega * C(1 - A_v)) = 1 / (j * omega * C_M)

Where

C_M = C(1 - A_v).

✓ Thus the effective or Miller capacitance C_M is the physical C multiplied by the factor (1 - A_v).

## slide 12

Darlington Connection

Overall beta = beta_1 * beta_2

Two transistors are connected in such a way that emitter current of one is fed to the base of another, so that the overall current gain is the product of their individual current gains. It is also known as superbeta transistor

Circuit: Darlington pair configuration consisting of two NPN transistors Q1 and Q2, with base current IB1 entering the base of Q1, collectors of Q1 and Q2 connected together, emitter of Q1 carrying current IE1 connected directly to the base of Q2, and emitter of Q2 carrying total output current IE2.

I_E1 = (1 + beta_1) * I_B1
I_E2 = (1 + beta_2) * I_B2
I_E2 = (1 + beta_2) * (1 + beta_1) * I_B1
I_E2 ~= beta_2 * beta_1 * I_B1

## slide 13

DC bias of Darlington Circuit

Circuit: DC bias circuit for Darlington pair (effective beta_D) with base resistor RB connected from DC supply VCC to the base terminal carrying IB, collectors tied directly to VCC carrying IC, emitter connected through resistor RE to ground carrying IE, with base-to-emitter DC voltage drop VBE.

I_B = (V_CC - V_BE) / (R_B + beta_D * R_E)
I_E = (1 + beta_D) * I_B ~= beta_D * I_B
V_B = V_E + V_BE
V_E = I_E * R_E

---

## Done Report

- **File written**: `C:/Users/bhomi/AppData/Local/Temp/claude/6e81c002d1e3bfcd/bd6f37ef-47e2-42fc-83d1-906fe62e205d/scratchpad/edc-e0/out/multi.md`
- **Sections**: 13 slide sections (`## slide 1` through `## slide 13`)
- **Counts**:
  - Total slides transcribed: 13 (slides 1 to 13)
  - Circuit schematics and block diagrams described: 7
    - Slide 2: Two-stage cascaded amplifier block diagram
    - Slide 3: Multi-stage (3+ stage) cascaded block diagram
    - Slide 5: Two-stage RC-coupled common-emitter BJT amplifier circuit
    - Slide 6: Two circuits (complete 2-stage RC-coupled BJT schematic and small-signal AC equivalent model)
    - Slide 9: Two circuits (two-stage RC-coupled BJT amplifier and two-stage direct-coupled BJT amplifier)
    - Slide 12: Darlington pair two-transistor connection
    - Slide 13: Darlington pair DC bias configuration circuit
  - Graphs described: 2
    - Slide 10: Frequency response curve of RC-coupled amplifier
    - Slide 10: Frequency response curve of direct-coupled amplifier
  - Equations transcribed: 23 equations across slides 2, 3, 5, 6, 7, 11, 12, 13
  - Worked examples / numerical questions: 0 (none present in this deck)
  - Tables: 0 (none present in this deck)
- **What could not be read ([unreadable])**:
  - Slide 11: Top line of `s011-image20.png` (`[unreadable: top line cut off at image boundary]`), where descenders/tops of letters were clipped directly above `I_i = (V_i - V_o) / Z = V_i(1 - A_v) / Z`.
- **Uncertain readings ([?])**:
  - Slide 5: `[? V_i or V_1 in denominator]` — in `Gain AV1 = V_1o / V_1`, the denominator is drawn as $V_1$ representing input voltage $V_i$.
  - Slide 9: `[? T or T2]` — in the last bullet of Working, text ends as "base of the second transistor T" without digit 2.
