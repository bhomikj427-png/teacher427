# 16 · Revision set: one question per idea, for the night before

<div class="sub">Answer from memory on paper, then check the answers page. Any miss points back to its chapter, shown in brackets.</div>

## Draw from memory

1. The zener regulator (Exp 2) with values, the clamper (Exp 4), and the CE amplifier (Exp 6) with every part labelled. Then say each part's job in one line.

## Diodes

2. A DSO shows 6 divisions peak-to-peak at 0.5 V/div on a sine. Give V_{rms}. *(Exp 0)*
3. Zener: define dynamic resistance, and say why "dynamic". *(Exp 1)*
4. A 6.2 V zener: which breakdown mechanism, and why is its temperature drift small? *(Exp 1)*
5. In the zener regulator, V_{in} goes up by 3 V. Which part takes almost all of it? *(Exp 2)*
6. Write the formulas for % line regulation and % load regulation. *(Exp 2)*
7. A positive clipper uses a 3 V battery. Clipping level? *(Exp 3)*
8. Clipper vs clamper: what happens to V_{pp} in each? *(Exps 3–4)*
9. What condition on RC makes a clamper work at 1 kHz? *(Exp 4)*

## BJT

10. Bias of the two junctions in active, saturation and cut-off. *(Exp 5)*
11. Name the four h-parameters, and say from which curve, with what held constant, each is read. *(Exp 5)*
12. In Exp 6, which capacitor mostly sets f_{L}, and why does the gain fall at high f? *(Exp 6)*
13. Define bandwidth and the −3 dB point. *(Exp 6)*
14. Why is the CE output 180° out of phase? *(Exp 6)*
15. Emitter follower: gain, phase, input and output resistance (high/low). *(Exp 7)*
16. Removing C_{E}: name the type of feedback, and two things that improve. *(Exp 8)*

## FET, oscillator, MOSFET

17. Define g_{m}, r_{d}, μ and show μ = g_{m}r_{d}. *(Exp 9)*
18. Write Shockley's equation, and define I_{DSS} and V_{P}. *(Exp 9)*
19. CS amplifier gain formula, and why the gate divider can use megohms. *(Exp 10)*
20. Barkhausen criterion, and the frequency formula of the RC phase-shift oscillator. *(Exp 11)*
21. Why must the amplifier's gain be at least 29 in the phase-shift oscillator? *(Exp 11)*
22. Resistive-load inverter: the MOSFET's state and the output for each input. Define V_{M}. *(Exp 12)*
23. Two cascaded stages: what happens to the gain and to the bandwidth? *(Extra)*
24. In LTspice, how do you enter 1 MΩ, and which analysis gives a frequency response? *(01)*

<!--ANSWERS-->

## Answers

1. See each chapter's redrawn figure and part table.
2. V_{pp} = 3 V, so V_{p} = 1.5 V and V_{rms} = 1.5/√2 = **1.06 V**.
3. r_{z} = ΔV_{Z}/ΔI_{Z} in breakdown: the slope of the curve, not V/I at one point.
4. A mix of tunnelling (Zener) and avalanche. Their temperature coefficients are opposite (− and +), so they nearly cancel.
5. The series resistor R1. The extra current goes into the zener, and V_{o} barely moves.
6. Line: ΔV_{o}/ΔV_{in} × 100. Load: (V_{NL} − V_{FL})/V_{FL} × 100.
7. 3 + 0.7 = **3.7 V**.
8. A clipper reduces V_{pp}. A clamper keeps V_{pp} and shifts the DC level.
9. RC ≫ T (= 1 ms). Here RC = 10 ms.
10. Active: BE forward, BC reverse. Saturation: both forward. Cut-off: both reverse.
11. h_{ie} = ΔV_{BE}/ΔI_{B} (input curve, V_{CE} fixed). h_{re} = ΔV_{BE}/ΔV_{CE} (I_{B} fixed). h_{fe} = ΔI_{C}/ΔI_{B} (output curves, V_{CE} fixed). h_{oe} = ΔI_{C}/ΔV_{CE} (one output curve, I_{B} fixed).
12. The emitter bypass C_{E}. At high f, the transistor's internal junction capacitances (Miller effect) and stray capacitance shunt the signal.
13. BW = f_{H} − f_{L}, between the frequencies where the gain is 0.707 × max = −3 dB (half power).
14. A rising base voltage raises I_{C}, which increases the drop across R_{C}, so the collector voltage falls.
15. Gain ≈ 1 (slightly less), in phase; input resistance high, output resistance low; used as a buffer.
16. Current-series negative feedback. Gain becomes stable (independent of β), bandwidth widens, distortion and noise fall, input resistance rises.
17. g_{m} = ΔI_{D}/ΔV_{GS} (V_{DS} const), r_{d} = ΔV_{DS}/ΔI_{D} (V_{GS} const), μ = −ΔV_{DS}/ΔV_{GS} (I_{D} const) = (ΔV_{DS}/ΔI_{D}) × (ΔI_{D}/ΔV_{GS}) = r_{d}g_{m}.
18. I_{D} = I_{DSS}(1 − V_{GS}/V_{P})². I_{DSS} = drain current at V_{GS} = 0 in saturation. V_{P} = the V_{GS} at which I_{D} → 0.
19. A_{v} = −g_{m}(R_{D} ∥ R_{L}). The gate draws no current, so megohm resistors drop no voltage.
20. |Aβ| ≥ 1 and loop phase 360°. f = 1/(2πRC√6).
21. At the oscillation frequency, the three-section RC ladder attenuates the signal to 1/29.
22. Input low: MOSFET off, output = V_{DD}. Input high: MOSFET on, output ≈ 0. V_{M} = the input voltage at which V_{out} = V_{in}.
23. Gains multiply (dB add). Bandwidth shrinks.
24. `1Meg` (`1M` is milli). `.ac`.

<!--/ANSWERS-->
