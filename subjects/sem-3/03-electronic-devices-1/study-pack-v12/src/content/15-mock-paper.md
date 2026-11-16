# 15 — Mock end-term paper

<div class="sub">Closed book, on paper, 3 hours · do it after the rest · then mark it with the key on the last pages and redo anything you missed</div>

No ECE2106 end-term paper or blueprint has been seen, so the format is a guess. This paper copies the layout of the one official blueprint in hand (MAS2001, July–Nov 2026): Part A 10 × 2, Part B 6 × 6, Part C 2 × 8, Part D 1 × 8, total 80. Questions tagged <span class="tag">Sheet</span> are from the professor's numerical sheets and are not used earlier in the pack.

## Part A · 10 × 2 = 20 marks

1. Define mobility and give its unit.
2. State the mass-action law.
3. Give two reasons why silicon is preferred over germanium.
4. Define peak inverse voltage. What is the PIV of each diode in a bridge rectifier?
5. Give two differences between Zener and avalanche breakdown.
6. Define the pinch-off voltage of a JFET.
7. <span class="tag">Sheet Q6</span> A reverse gate voltage of 15 V gives a gate current of 10^{−3} μA. Find the gate–source resistance.
8. Why is an enhancement MOSFET called "normally off"?
9. Write the relation between α and β. Find β when α = 0.99.
10. State the Barkhausen criterion.

## Part B · 6 × 6 = 36 marks

11. Derive the conductivity of a semiconductor. Find the resistivity of intrinsic Ge at 300 K: n_{i} = 2.5 × 10^{13} cm^{−3}, μ_{n} = 3800, μ_{p} = 1800 cm^{2}/V·s.
12. Draw a centre-tapped full-wave rectifier and explain it with waveforms. Secondary 9 V–0–9 V rms, load 1 kΩ, ideal diodes: find V_{dc}, I_{dc} and the PIV.
13. <span class="tag">Sheet Q29</span> A D-MOSFET amplifier: V_{DD} = +15 V, R_{D} = 620 Ω, gate to ground through R_{G} = 10 MΩ (V_{GS} = 0), source grounded, load R_{L} = 8.2 kΩ capacitor-coupled to the drain. I_{DSS} = 12 mA, g_{m} = 3.2 mS. Find (i) V_{DS} and (ii) the AC output voltage for v_{in} = 500 mV.
14. Divider bias: V_{CC} = 16 V, R_{1} = 62 kΩ, R_{2} = 9.1 kΩ, R_{C} = 3.9 kΩ, R_{E} = 0.68 kΩ, β = 150. Approximate method: V_{B}, I_{C}, V_{CE}. Then S.
15. <span class="tag">Book P3</span> h_{ic} = 1.1 k, h_{rc} = 1, h_{fc} = −51, h_{oc} = 25 μA/V. Find A_{I}, A_{V}, A_{VS}, R_{i} and R_{o} for CC with R_{S} = R_{L} = 10 k.
16. Draw the block diagram of a negative-feedback amplifier and derive its gain. A = 60 dB, Z_{o} = 10 kΩ, voltage-series feedback with β = 0.05: find A_{f} (number and dB) and Z_{of}.

## Part C · 2 × 8 = 16 marks

17. Define the four characteristic parameters of a JFET, stating what is held constant. Derive μ = g_{m}r_{d}. From Shockley, show g_{m} = g_{m0}(1 − V_{GS}/V_{GS(off)}).
18. Explain the RC phase-shift oscillator with a circuit and state the conditions for oscillation. Design one for 1 kHz with 0.01 μF capacitors.

## Part D · 1 × 8 = 8 marks

19. (a) <span class="tag">Sheet Q31</span> An E-MOSFET is biased by a divider: V_{DD} = 24 V, R_{1} = 100 kΩ (top), R_{2} = 15 kΩ, R_{D} = 470 Ω, source grounded. I_{D(on)} = 500 mA at V_{GS} = 10 V, V_{GS(th)} = 1 V. Find V_{GS} and V_{DS}. (b) Draw a two-input CMOS NAND and explain it with a truth table.

---

## Formula recall

Cover the right column, write each formula from the cue, then uncover. Any row you miss, go back to the file named.

| Cue | Recall |
|---|---|
| 01 Mass action, Fermi | n·p = n_{i}^{2} · n ≈ N_{D} · f(E) = 1/(1 + e^{(E − E_{F})/kT}) · E_{F} = (E_{C} + E_{V})/2 |
| 02 Drift, diffusion | σ = q(nμ_{n} + pμ_{p}) · R_{s} = ρ/t · D/μ = V_{T} · J_{n} = qnμ_{n}E + qD_{n}dn/dx |
| 02 Continuity, Poisson | ∂n/∂t = (1/q)∂J_{n}/∂x − (R − G) · dE/dx = ρ/ε |
| 03a, 03b Junction, diode | V_{bi} = V_{T}ln(N_{A}N_{D}/n_{i}^{2}) · W ∝ √(V_{bi} − V_{a}) · I_{D} = I_{s}(e^{V_{D}/ηV_{T}} − 1) · r_{d} = 26 mV/I_{D} |
| 04 Rectifiers | HW 0.318V_{m}, r 1.21, η 40.6% · FW 0.636V_{m}, r 0.482, η 81.2% · PIV: V_{m} (HW, bridge), 2V_{m} (CT) |
| 05 Clamper, Zener | start with the ON half; 5RC ≫ T/2 · Zener ON if V_{i}R_{L}/(R + R_{L}) ≥ V_{Z}; I_{Z} = I_{R} − I_{L} |
| 07 JFET | I_{D} = I_{DSS}(1 − V_{GS}/V_{GS(off)})^{2} · μ = g_{m}r_{d} · g_{m0} = 2I_{DSS}/|V_{GS(off)}| · self-bias V_{GS} = −I_{D}R_{S} |
| 08 MOSFET | K(V_{GS} − V_{T})^{2} if V_{DS} ≥ V_{GS} − V_{T} · K = I_{D(on)}/(V_{GS(on)} − V_{T})^{2} · g_{m} = 2√(KI_{D}) |
| 07, 08 Amplifiers | CS −g_{m}(r_{d} ∥ R_{D}) · CD g_{m}R_{S}/(1 + g_{m}R_{S}) · CG +g_{m}R_{D}, R_{in} = 1/g_{m} |
| 09 CMOS | pull-down: series AND, parallel OR; pull-up dual; 2n transistors |
| 10 BJT | I_{E} = I_{C} + I_{B} · β = α/(1 − α) · I_{CEO} = (1 + β)I_{CBO} |
| 11 Bias, S | emitter I_{B} = (V_{CC} − 0.7)/(R_{B} + (β + 1)R_{E}) · S = (1 + β)/(1 − β dI_{B}/dI_{C}) · with R_{E}: (1 + β)(1 + R_{B}/R_{E})/(1 + β + R_{B}/R_{E}) |
| 12 h-parameters | A_{i} = −h_{f}/(1 + h_{o}R_{L}) · R_{i} = h_{i} + h_{r}A_{i}R_{L} · A_{v} = A_{i}R_{L}/R_{i} · Y_{o} = h_{o} − h_{f}h_{r}/(h_{i} + R_{s}) · β_{D} ≈ β_{1}β_{2} |
| 13 Feedback | A_{f} = A/(1 + βA) · BW × (1 + βA) · series × (1 + βA), shunt ÷ |
| 14 Oscillators | |βA| = 1, 0° · phase-shift 1/(2πRC√6), gain 29 · Wien 1/(2πRC), gain 3 · Colpitts C_{eq} = C_{1}C_{2}/(C_{1} + C_{2}) |

<!--ANSWERS-->

## Key

**Part A.**

1. Drift velocity per unit field, μ = v_{d}/E; cm^{2}/V·s. (02)
2. In equilibrium n·p = n_{i}^{2}, whatever the doping. (01)
3. Any two: larger gap, so far smaller leakage; works at higher temperature (≈ 150 °C against 75 °C); higher PIV; cheap, forms a good oxide. (01a, 03b)
4. The largest reverse voltage across a diode while it blocks. Bridge: **V_{m}**. (04)
5. Zener: heavy doping, thin region, field pulls electrons from bonds, below ≈ 5 V, negative coefficient. Avalanche: light doping, wide region, multiplication by collision, above ≈ 6 V, positive coefficient. (05)
6. The V_{DS}, at V_{GS} = 0, at which the channel pinches off and I_{D} levels at I_{DSS}; equal to |V_{GS(off)}|. (07)
7. 15 V/10^{−9} A = **1.5 × 10^{10} Ω**.
8. It has no channel at V_{GS} = 0, so no current flows until V_{GS} &gt; V_{T}. (08)
9. β = α/(1 − α) = 0.99/0.01 = **99**. (10)
10. |βA| = 1 and loop phase 0° or 360°. (14)

**Part B.**

11. J = q(nμ_{n} + pμ_{p})E = σE (02). σ = 1.6 × 10^{−19} × 2.5 × 10^{13} × 5600 = 0.0224 (Ω·cm)^{−1}; **ρ = 44.6 Ω·cm**.
12. Circuit: 04 §4. V_{m} = 9√2 = 12.73 V. **V_{dc} = 8.10 V**, **I_{dc} = 8.10 mA**, **PIV = 2V_{m} = 25.5 V**.
13. (i) I_{D} = I_{DSS} = 12 mA; **V_{DS} = 15 − 12 × 0.62 = 7.56 V**. (ii) R_{AC} = 620 ∥ 8200 = 576 Ω; v_{out} = 3.2 mS × 576 Ω × 500 mV = **922 mV**, inverted.
14. βR_{E} = 102 kΩ ≥ 10R_{2} = 91 kΩ ✓. **V_{B} = 2.05 V**, V_{E} = 1.35 V, **I_{C} ≈ 1.98 mA**, **V_{CE} = 16 − 1.98 × 4.58 = 6.92 V**. R_{Th} = 7.94 kΩ, R_{Th}/R_{E} = 11.7; **S = 151 × 12.7/162.7 = 11.8**. (11)
15. A_{I} = 51/1.25 = **40.8**. R_{i} = 1.1 k + 1 × 40.8 × 10 k = **409.1 kΩ**. A_{V} = 40.8 × 10 k/409.1 k = **0.997**. Y_{o} = 25 μS + 51/11.1 k = 4.62 mS, **R_{o} = 216 Ω**. A_{VS} = 0.997 × 409.1/419.1 = **0.974**. An emitter follower. (12)
16. Derivation: 13 §1. A = 1000; 1 + βA = 51. **A_{f} = 19.6 = 25.8 dB**. **Z_{of} = 196 Ω**.

**Part C.**

17. 07 §3 in full. Last part: dI_{D}/dV_{GS} = 2I_{DSS}(1 − V_{GS}/V_{GS(off)})(−1/V_{GS(off)}) = g_{m0}(1 − V_{GS}/V_{GS(off)}), g_{m0} = 2I_{DSS}/|V_{GS(off)}|.
18. 14 §2. Conditions: three sections give 180° at f_{0} = 1/(2πRC√6); the inverting amplifier gives 180°; |A| ≥ 29. **R = 6.50 kΩ**, **R_{f} = 29R = 188 kΩ**.

**Part D.**

19. (a) V_{GS} = 24 × 15/115 = **3.13 V**. K = 6.17 mA/V^{2}; I_{D} = 6.17 × 2.13^{2} = 28.0 mA; **V_{DS} = 24 − 28.0 × 0.47 = 10.8 V** (saturation: 10.8 ≥ 2.13 ✓). (b) 09 Self-test 1.

<!--/ANSWERS-->
