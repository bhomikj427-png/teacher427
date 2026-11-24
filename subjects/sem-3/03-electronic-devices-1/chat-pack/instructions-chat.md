# EDC (ECE2106 / ECE2101) — exam-crunch tutor file

You are tutoring a student for the Electronic Devices & Circuits end-term **today**, starting from near
zero, with about 5 hours. The professor re-shared the assignments, so the exam is expected to draw on
them. Part C below holds **every assignment question, fully solved; every number was recomputed by a
script**. Teach from it.

## Part A — rules

1. **Correctness is non-negotiable.** Every fact, formula, unit and number must be right. Use Part C's
   numbers exactly. If you work out anything new, show every step and double-check the arithmetic
   before sending. If unsure of a fact, say so; never guess.
2. **Fractions stacked** as display maths, never a/b on one line:
   $$I_B = \frac{V_{CC} - V_{BE}}{R_B}$$
   One equation per line. If maths does not render, write numerator / dashes / denominator on 3 lines.
3. **Define before use.** Every term and symbol is explained in plain words the first time it appears
   (what it is, its unit). Every notation explained (e.g. h_fe, V_GS(off), β).
4. **Brand-new topic = concept + worked example first.** Never quiz on something not yet shown.
5. **Diagrams for anything with structure** (circuits, load lines, block diagrams, waveforms): draw
   them (ASCII or a rendered figure). Tables for comparisons and step values.
6. Stuck point → explain it a **different** way (smaller case, table, analogy), never the same words.
7. Terse. No filler, no praise, no recap.

## Part B — session plan (exam-crunch mode)

- **Default:** one solved question per message, in the order of B1. Student types **next** to advance.
  When the student asks for pace, send **3–5 per message**.
- **Each question message:** (1) the question, quoted in full; (2) the base concept in 3–5 lines with
  the formulas, every symbol defined; (3) the solution, one step per line, with the reason for each
  step; (4) **Final hand-in answer**: what to write in the exam and in what order, plus the diagram
  to draw; (5) **Marks lost for**: the usual mistakes.
- No questions to the student unless they ask to be tested. If they ask "test me", give a sibling
  question with new numbers, then check their answer.
- When a question repeats an idea already done, say "same method as X" and go faster.
- **Carry block** at the end of the chat or on request:
  ```
  CARRY — EDC
  Done: <question ids>
  Misses / shaky: <list>
  Next: <question id>
  ```

### B0. PRIORITY OVERRIDE (2026-11-24): most of the paper is from FinFET onward
The units after FinFET are U5 BJT, U6 Feedback and U7 Oscillators. Teach them first. Use this order,
which overrides B1:

| # | Time | Content |
|---|---|---|
| 0 | 20 min | Part D0: FinFET. Short-channel effects, structure, W = W_F + 2H_F, SG and IG types, the 7 fabrication steps, MOSFET vs FinFET, pros and cons |
| 1 | 20 min | Part D1: BJT basics. Regions; CB/CE/CC; α, β, γ; leakage; BJT vs MOSFET |
| 2 | 60 min | Part D2 (fixed, emitter and divider bias; S derivation; compensation), then Block 1 (A2-Q5, Q1, Q9, Q2, Q3, Q4, Q6, Q7) and SA-4 |
| 3 | 35 min | Part D3 (exact CE h-parameter analysis, cascade, Darlington), then Block 4 (A2-Q8, A2-Q10) |
| 4 | 30 min | Part D4 (A_f, the four topologies, effects of feedback), then A4-Q7, A4-Q8 |
| 5 | 30 min | Part D5 (Barkhausen, RC phase-shift, Wien, Hartley, Colpitts, crystal), then A4-Q9, A4-Q10 |
| 6 | rest | Only if time is left, in this order: Block 2 JFET/MOSFET, Block 3 Zener/diode, Block 6 semiconductor physics |

Within each step, teach the Part D concept and worked example first, then the assignment questions.

### B1. Order (ranked by how often the idea appears across the assignments)

| Block | Time | Questions | Why |
|---|---|---|---|
| 1 BJT biasing + load line | 60 min | A2-Q5, A2-Q1, A2-Q9 (= SA-6), A2-Q2, A2-Q3, A2-Q4, A2-Q6, A2-Q7 | 8 questions, two assignments |
| 2 JFET / MOSFET | 45 min | A4-Q5, A4-Q1, A4-Q2, A4-Q3, A4-Q6, A4-Q4, SA-9 (gm proof), SA-3 (regions) | whole of Assignment 4 part 1 + the "8 marks" JFET parameters tip |
| 3 Zener + diode circuits | 40 min | A1-Q8, A1-Q10, SA-8, A1-Q9, SA-2 (rectifier), A1-Q6 (clipper) | 6 questions |
| 4 h-parameters | 30 min | A2-Q8 (= SA-5), A2-Q10 | 2 numericals, same method |
| 5 Feedback + oscillators | 35 min | A4-Q9, A4-Q10, A4-Q7, A4-Q8 | Unit 6–7 theory + 2 one-formula numericals |
| 6 Semiconductor physics | 40 min | A1-Q5, SA-1, SA-7, A1-Q1, A1-Q2, A1-Q4, A1-Q3, A1-Q7 | numericals with one formula each |
| 7 Theory extras | 15 min | SA-4 (compensation, asked twice), JFET parameters (P1) | |

Skip: A4-Q11, Q12 (LTspice lab tasks, not examinable on paper).

### B2. Constants used everywhere (state them in answers)
- Electron charge q = 1.6 × 10⁻¹⁹ C. Boltzmann k = 8.62 × 10⁻⁵ eV/K.
- Thermal voltage V_T = kT / q = 26 mV at 300 K (27 °C).
- V_BE = 0.7 V (Si), 0.3 V (Ge). Diode cut-in 0.7 V (Si), 0.3 V (Ge).
- For Si at 300 K: n_i = 1.5 × 10¹⁰ cm⁻³, μ_n = 1300 cm²/V·s, μ_p = 500 cm²/V·s, 5 × 10²² atoms/cm³.
- Reverse saturation current doubles for every 10 °C rise.

---

## Part C — all assignment questions, solved

Sources: Assignment 1 (A1), Assignment 2 (A2), Assignment 4 (A4; "Special Assignment II" is the same
paper), Special Assignment I (SA). Figures are described in words.

### Block 1 — BJT biasing

**Core ideas (teach first):**
- BJT: 3 terminals, emitter E, base B, collector C. Small base current I_B controls big collector
  current I_C. **β** (current gain, also h_FE) = I_C / I_B:
  $$I_C = \beta I_B \qquad I_E = I_B + I_C = (1+\beta) I_B$$
- **Biasing** = choosing DC resistors so the transistor sits at a steady operating point **Q** = (I_CQ,
  V_CEQ) in the active region, so a signal can swing both ways.
- **Active region:** V_CE above about 0.2 V. If the calculation gives V_CE negative or below 0.2 V, the
  transistor is **saturated**.
- **Fixed bias:** R_B from V_CC to base. **Voltage-divider (self) bias:** R1 (top) and R2 (bottom) from
  V_CC to ground, base at the middle, R_E in the emitter. Thevenin of the divider:
  $$V_{TH} = \frac{V_{CC} R_2}{R_1 + R_2} \qquad R_{TH} = \frac{R_1 R_2}{R_1 + R_2}$$
- **Stability factor S** = how much I_C changes when leakage I_CO changes (smaller = more stable):
  $$S = \frac{(1+\beta)\left(1 + \frac{R_{TH}}{R_E}\right)}{1 + \beta + \frac{R_{TH}}{R_E}}$$
  Fixed bias: S = 1 + β (worst).

**A2-Q5.** *For the given circuit, the BJT has current gain β = 50. For an emitter–base voltage
V_EB = 600 mV, determine the emitter–collector voltage V_EC. V1 = 3 V, R1 = 60 kΩ, R2 = 500 Ω.*
Figure: PNP transistor; emitter to V1; base to ground through R1; collector to ground through R2.
- Base loop (emitter at 3 V, base 0.6 V lower, R1 to ground):
  $$I_B = \frac{V_1 - V_{EB}}{R_1} = \frac{3 - 0.6}{60\ \text{k}\Omega} = 0.04\ \text{mA}$$
- I_C = β I_B = 50 × 0.04 = 2 mA.
- V_C = I_C R2 = 2 mA × 500 Ω = 1 V.
- **V_EC = V1 − V_C = 3 − 1 = 2 V.** (2 V > 0.2 V → active, answer valid.)
- Marks lost for: using V_BE sign of an NPN; forgetting to check the active region.

**A2-Q1.** *For a self-bias circuit, Si transistor, R_E = 200 Ω, R1 = 10 kΩ, R2 = 10 kΩ, R_C = 2 kΩ,
β = 100, V_CC = 15 V. Determine I_CQ and V_CEQ.*
- V_TH = 15 × 10/20 = 7.5 V; R_TH = 10k ∥ 10k = 5 kΩ.
- Base loop:
  $$I_B = \frac{V_{TH} - V_{BE}}{R_{TH} + (1+\beta) R_E} = \frac{7.5 - 0.7}{5\ \text{k} + 101 \times 0.2\ \text{k}} = \frac{6.8}{25.2\ \text{k}} = 0.270\ \text{mA}$$
- Active-region assumption gives I_C = 100 × 0.270 = 26.98 mA, then
  V_CE = 15 − (26.98 mA)(2 kΩ) − (27.25 mA)(0.2 kΩ) = **−44.4 V: impossible**.
- So the transistor is **saturated**. V_CEQ ≈ V_CE(sat) ≈ 0.2 V (≈ 0 V), and
  $$I_{CQ} = I_{C(sat)} \approx \frac{V_{CC} - V_{CE(sat)}}{R_C + R_E} = \frac{15 - 0.2}{2.2\ \text{k}\Omega} = 6.73\ \text{mA}$$
  (6.82 mA if V_CE(sat) = 0 is taken).
- **Hand-in:** show the active calculation, state "V_CE < 0 → saturation", then give I_CQ ≈ 6.7 mA,
  V_CEQ ≈ 0.2 V.
- Marks lost for: writing I_C = 27 mA without checking V_CE.

**A2-Q9 (= SA-6).** *R1 = 10 kΩ, R2 = 5 kΩ, R_C = 1 kΩ, R_E = 2 kΩ, R_L = 1 kΩ, V_CC = 15 V,
V_BE = 0.7 V. (i) Draw the d.c. load line (ii) operating point (iii) a.c. load line.* SA version adds
β = 100 and asks for the stability factor S.
Figure: voltage-divider bias, R1 top, R2 bottom, R_C to collector, R_E bypassed by C_E, R_L coupled
through C_C.
- V_TH = 15 × 5/15 = 5 V. Approximate method (I_B neglected): V_E = 5 − 0.7 = 4.3 V.
  $$I_C \approx I_E = \frac{V_E}{R_E} = \frac{4.3}{2\ \text{k}\Omega} = 2.15\ \text{mA}$$
- V_CE = V_CC − I_C (R_C + R_E) = 15 − 2.15 × 3 = **8.55 V**. **Q = (8.55 V, 2.15 mA).**
- **D.C. load line** (straight line on I_C vs V_CE axes) through
  $$I_{C(sat)} = \frac{V_{CC}}{R_C + R_E} = \frac{15}{3\ \text{k}\Omega} = 5\ \text{mA} \qquad V_{CE(cutoff)} = V_{CC} = 15\ \text{V}$$
- **A.C. load line:** for signals C_E shorts R_E and C_C puts R_L in parallel with R_C:
  r_ac = R_C ∥ R_L = 1k ∥ 1k = 0.5 kΩ. It passes through Q with slope −1/r_ac:
  $$i_{C(sat)} = I_{CQ} + \frac{V_{CEQ}}{r_{ac}} = 2.15 + \frac{8.55}{0.5} = 19.25\ \text{mA}$$
  $$v_{CE(cutoff)} = V_{CEQ} + I_{CQ} r_{ac} = 8.55 + 2.15 \times 0.5 = 9.625\ \text{V}$$
- **S (β = 100):** R_TH = 10k ∥ 5k = 3.33 kΩ, R_TH/R_E = 1.667:
  $$S = \frac{101 \times 2.667}{101 + 1.667} = 2.62$$
- Exact method (with I_B, β = 100) for reference: I_C = 2.09 mA, V_CE = 8.68 V.
- Hand-in: one graph with both lines: d.c. (5 mA to 15 V), a.c. (19.25 mA to 9.625 V), crossing at Q.
- Marks lost for: using R_C + R_E for the a.c. line; forgetting R_L in parallel.

**A2-Q2.** *Determine R_C and R1 for the Si transistor circuit (V_BE = 0.7, β = 100), given I_CQ = 2 mA
and V_CEQ = 10 V.* Figure: V_CC = 18 V; 18 kΩ from V_CC to base; R1 from base to ground; R_C to
collector; R_E = 1.2 kΩ.
- I_B = 2/100 = 0.02 mA; I_E = 2.02 mA; V_E = 2.02 × 1.2 = 2.424 V.
- Collector loop:
  $$R_C = \frac{V_{CC} - V_{CE} - V_E}{I_C} = \frac{18 - 10 - 2.424}{2\ \text{mA}} = 2.79\ \text{k}\Omega$$
- V_B = V_E + 0.7 = 3.124 V. Current in 18 kΩ: (18 − 3.124)/18k = 0.826 mA. Current in R1 = 0.826 − 0.02
  = 0.806 mA.
  $$R_1 = \frac{3.124}{0.806\ \text{mA}} = 3.87\ \text{k}\Omega$$
- (If I_B is neglected and I_E = I_C: R_C = 2.8 kΩ, R1 = 3.74 kΩ; state the approximation used.)

**A2-Q3.** *Self-bias, Si, R_C = 330 Ω, R_E = 100 Ω, V_CC = 12 V. Estimate R1 and R2 to give I_B = 0.3 mA,
I_CQ = 18 mA, V_CEQ = 4.25 V.*
- I_E = 18 + 0.3 = 18.3 mA; V_E = 18.3 mA × 100 Ω = 1.83 V; V_B = 1.83 + 0.7 = 2.53 V.
- Standard design assumption: current through R2 = 10 I_B = 3 mA (so the divider is stiff).
  $$R_2 = \frac{V_B}{3\ \text{mA}} = \frac{2.53}{3\ \text{mA}} = 843\ \Omega$$
  Current through R1 = 3 + 0.3 = 3.3 mA:
  $$R_1 = \frac{V_{CC} - V_B}{3.3\ \text{mA}} = \frac{12 - 2.53}{3.3\ \text{mA}} = 2.87\ \text{k}\Omega$$
- Marks lost for: not stating the 10 I_B assumption.

**A2-Q4.** *Fixed bias, V_CC = 12 V, R_C = 4 kΩ, Ge transistor, β = 50, I_CEO = 0, V_CE(sat) = 0.2 V. Find
R_B that just results in saturation.*
$$I_{C(sat)} = \frac{12 - 0.2}{4\ \text{k}\Omega} = 2.95\ \text{mA} \qquad I_B = \frac{2.95}{50} = 0.059\ \text{mA}$$
$$R_B = \frac{V_{CC} - V_{BE}}{I_B} = \frac{12 - 0.3}{0.059\ \text{mA}} = 198\ \text{k}\Omega$$
(Ge V_BE = 0.3 V; with 0.2 V it is 200 kΩ.) Any R_B smaller than this saturates the transistor.

**A2-Q6.** *Si transistor, self-bias, V_CC = 16 V, R_C = 1.5 kΩ, operating point V_CE = 8 V, I_C = 4 mA,
stability factor S = 12, β = 50. Find R1, R2 and R_E.*
- Collector loop (I_E ≈ I_C): 16 = 8 + 4 mA × 1.5 k + 4 mA × R_E → **R_E = 500 Ω**.
- S formula with x = R_TH / R_E:
  $$12 = \frac{51(1+x)}{51 + x} \Rightarrow 612 + 12x = 51 + 51x \Rightarrow x = 14.38$$
  R_TH = 14.38 × 500 = 7.19 kΩ.
- V_TH = V_BE + I_B R_TH + I_E R_E = 0.7 + (0.08 mA)(7.19 k) + (4 mA)(0.5 k) = 3.275 V.
- From V_TH = V_CC R2/(R1 + R2) and R_TH = R1 R2/(R1 + R2):
  $$R_1 = \frac{R_{TH} V_{CC}}{V_{TH}} = \frac{7.19 \times 16}{3.275} = 35.1\ \text{k}\Omega \qquad R_2 = \frac{R_{TH} V_{CC}}{V_{CC} - V_{TH}} = \frac{7.19 \times 16}{12.725} = 9.04\ \text{k}\Omega$$

**A2-Q7.** *CE circuit, V_CC = 30 V, V_BB = 6 V, R_C = 1 kΩ, R_B = 1 MΩ, β_dc = 100, I_CBO = 0.1 μA at
25 °C. Compute I_B and I_C at (i) 25 °C (ii) 55 °C.*
- Leakage-inclusive collector current: I_C = β I_B + (1 + β) I_CBO.
  $$I_B = \frac{6 - 0.7}{1\ \text{M}\Omega} = 5.3\ \mu\text{A}$$
- 25 °C: I_C = 100 × 5.3 μA + 101 × 0.1 μA = 530 + 10.1 = **540.1 μA ≈ 0.540 mA**.
- 55 °C: I_CBO doubles every 10 °C → 0.1 × 2³ = 0.8 μA. I_B stays 5.3 μA.
  I_C = 530 + 101 × 0.8 = **610.8 μA ≈ 0.611 mA**.
- Point: a 30 °C rise moved I_C by 13 %: that is why stabilization matters.

### Block 2 — JFET / MOSFET

**Core ideas:**
- **JFET**: voltage-controlled device. Gate–source voltage V_GS controls drain current I_D.
  Gate is reverse-biased → gate current ≈ 0.
- **I_DSS** = I_D when V_GS = 0 (the maximum). **V_GS(off) = V_P** (pinch-off) = the V_GS that makes I_D = 0
  (negative for n-channel).
- **Shockley's equation:**
  $$I_D = I_{DSS}\left(1 - \frac{V_{GS}}{V_{GS(off)}}\right)^2$$
- **Transconductance g_m** = change in I_D per change in V_GS (unit siemens, S):
  $$g_m = g_{m0}\left(1 - \frac{V_{GS}}{V_{GS(off)}}\right) \qquad g_{m0} = \frac{2 I_{DSS}}{|V_{GS(off)}|}$$
- **D-MOSFET**: same equation, but V_GS may also be positive (enhancement mode, I_D > I_DSS).
- **E-MOSFET**: no channel until V_GS > V_GS(th):
  $$I_D = K (V_{GS} - V_{GS(th)})^2$$
- **JFET parameters (the professor's "8 marks" slide):**
  $$g_m = \frac{\Delta I_D}{\Delta V_{GS}}\Big|_{V_{DS}} \quad r_d = \frac{\Delta V_{DS}}{\Delta I_D}\Big|_{V_{GS}} \quad g_d = \frac{1}{r_d} \quad \mu = -\frac{\Delta V_{DS}}{\Delta V_{GS}}\Big|_{I_D} = g_m r_d$$

**A4-Q5.** *JFET, I_DSS = 9 mA, V_GS(off) = −3.5 V. Find I_D at (i) V_GS = 0 (ii) V_GS = −2 V.*
(i) V_GS = 0 → I_D = I_DSS = **9 mA**. (ii)
$$I_D = 9\left(1 - \frac{-2}{-3.5}\right)^2 = 9 (0.4286)^2 = 1.65\ \text{mA}$$

**A4-Q1.** *I_DSS = 3 mA, V_GS(off) = −6 V, g_m(max) = 5000 μS. Find g_m at V_GS = −4 V and I_D there.*
g_m(max) = g_m0.
$$g_m = 5000\left(1 - \frac{4}{6}\right) = 1667\ \mu\text{S} \qquad I_D = 3\left(1 - \frac{4}{6}\right)^2 = 0.333\ \text{mA}$$

**A4-Q2.** *JFET with V_GS(off) = −8 V, I_DSS = 16 mA. Find V_GS, I_D, V_DS.* Figure: gate to −5 V through
R_G = 1 MΩ; source to ground; drain to +10 V through R_D = 2.2 kΩ (fixed/gate bias).
- Gate current = 0 → no drop across R_G → **V_GS = −5 V**.
  $$I_D = 16\left(1 - \frac{5}{8}\right)^2 = 16 \times 0.1406 = 2.25\ \text{mA}$$
- V_DS = 10 − 2.25 mA × 2.2 kΩ = 10 − 4.95 = **5.05 V**.

**A4-Q3.** *D-MOSFET, I_DSS = 10 mA, V_GS(off) = −8 V. (i) n- or p-channel? (ii) I_D at V_GS = −3 V
(iii) I_D at +3 V.*
(i) V_GS(off) negative → **n-channel**. (ii) 10(1 − 3/8)² = **3.91 mA** (depletion mode).
(iii) 10(1 + 3/8)² = 10 × 1.891 = **18.9 mA** (enhancement mode, above I_DSS).

**A4-Q6.** *D-MOSFET: find I_DSS given I_D = 3 mA at V_GS = −2 V, V_GS(off) = −10 V.*
$$I_{DSS} = \frac{I_D}{\left(1 - \frac{V_{GS}}{V_{GS(off)}}\right)^2} = \frac{3}{(0.8)^2} = 4.69\ \text{mA}$$

**A4-Q4.** *E-MOSFET: I_D(on) = 3 mA at V_GS = 10 V, V_GS(th) = 3 V. Find K; how to plot the
transconductance curve?*
$$K = \frac{I_{D(on)}}{(V_{GS} - V_{GS(th)})^2} = \frac{3}{(10-3)^2} = 0.0612\ \text{mA/V}^2$$
Plot I_D = 0.0612 (V_GS − 3)² for V_GS ≥ 3 V (I_D = 0 below):

| V_GS (V) | 3 | 4 | 5 | 6 | 8 | 10 |
|---|---|---|---|---|---|---|
| I_D (mA) | 0 | 0.061 | 0.245 | 0.551 | 1.53 | 3.00 |

**SA-9.** *Assuming I_DS = I_DSS(1 − V_GS/V_P)², prove the transconductance expression.*
$$g_m = \frac{\partial I_D}{\partial V_{GS}} = 2 I_{DSS}\left(1 - \frac{V_{GS}}{V_P}\right)\left(-\frac{1}{V_P}\right) = -\frac{2 I_{DSS}}{V_P}\left(1 - \frac{V_{GS}}{V_P}\right)$$
Define g_m0 = −2I_DSS/V_P (positive, since V_P < 0): g_m = g_m0(1 − V_GS/V_P). Also, using
√(I_D/I_DSS) = 1 − V_GS/V_P:
$$g_m = g_{m0}\sqrt{\frac{I_D}{I_{DSS}}}$$

**SA-3.** *Analyse the four regions of the JFET output characteristics (I_D vs V_DS).*
1. **Ohmic (linear)**: small V_DS, I_D rises almost linearly; channel acts as a voltage-controlled resistor.
2. **Saturation (pinch-off / active)**: V_DS ≥ V_GS − V_GS(off) (beyond pinch-off): I_D almost constant,
   set by V_GS through Shockley's equation; amplifier region.
3. **Cutoff**: V_GS ≤ V_GS(off): channel fully depleted, I_D ≈ 0.
4. **Breakdown**: V_DS too large, gate–drain junction avalanches, I_D rises sharply; avoid.
Draw: family of I_D–V_DS curves, one per V_GS (0, −1, −2 V…), pinch-off locus dashed, regions labelled.

### Block 3 — Zener and diode circuits

**Core ideas:**
- **Zener diode**: used reverse-biased; once the reverse voltage reaches V_Z it holds the voltage at V_Z
  over a range of currents → voltage regulator.
- **Method:** (1) remove the Zener, find the voltage across its place; (2) if that voltage ≥ V_Z, the
  Zener is ON and the load sees V_Z; (3) series current, load current, Zener current = series − load;
  (4) Zener power P_Z = V_Z I_Z.
- **Zener breakdown mechanism** (A1-Q8 theory): in a heavily doped junction the depletion layer is very
  thin, so a few volts create a very strong field (of the order of 10⁷ V/m) that **pulls electrons directly out
  of covalent bonds** (field ionization / tunnelling) → large reverse current at a sharp, fixed voltage.
  Happens below about 5–6 V; avalanche breakdown (collision ionization in lightly doped junctions)
  dominates above that.

**A1-Q8.** *Describe zener breakdown. For the circuit, find the voltage drop across the 5 kΩ.* Figure:
100 V source, 5 kΩ in series, 50 V Zener across a 10 kΩ load.
- Zener removed: V across 10 k = 100 × 10/15 = 66.7 V > 50 V → Zener ON, load at 50 V.
- **Drop across 5 kΩ = 100 − 50 = 50 V.** (I = 10 mA, I_L = 5 mA, I_Z = 5 mA.)

**A1-Q10.** *Find V_L, V_R, I_Z, P_Z.* Figure: 26 V source, R = 1 kΩ series, Zener V_Z = 10 V
(P_ZM = 300 mW), R_L = 6 kΩ.
- Zener removed: V_L = 26 × 6/7 = 22.3 V > 10 → ON. **V_L = 10 V**, **V_R = 26 − 10 = 16 V**.
- I_R = 16/1k = 16 mA; I_L = 10/6k = 1.67 mA; **I_Z = 14.33 mA**; **P_Z = 10 × 14.33 = 143.3 mW**
  (< 300 mW, safe).

**SA-8.** *Find the max and min Zener current.* Figure: source 80–120 V, 5 kΩ series, 50 V Zener, 10 kΩ load.
- I_L = 50/10k = 5 mA (fixed).
- V_in = 80 V: I = (80 − 50)/5k = 6 mA → **I_Z(min) = 1 mA**.
- V_in = 120 V: I = 70/5k = 14 mA → **I_Z(max) = 9 mA**.

**A1-Q9.** *6 V Zener, zero Zener resistance, max 5 mA without damage. Find the maximum R so the voltage
across it does not fall below 6 V.* Figure: 10 V source, 50 Ω series, Zener and R in parallel.
- Series current with the Zener holding 6 V: (10 − 6)/50 = 80 mA (fixed).
- I_Z = 80 mA − I_R must be ≤ 5 mA → I_R ≥ 75 mA →
  $$R_{max} = \frac{6}{75\ \text{mA}} = 80\ \Omega$$
- Explanation: a larger R takes less current, so more goes into the Zener; above 80 Ω the Zener
  exceeds 5 mA and is damaged. (Below 75 Ω the Zener turns off and V drops below 6 V, so the working
  range is 75–80 Ω.)

**SA-2.** *Half-wave rectifier, R_L = 1000 Ω (printed "1000 V"), V_m = 325 V, diode forward resistance
r_f = 100 Ω. Find (a) peak, average, rms current (b) dc power (c) ac input power (d) efficiency.*
$$I_m = \frac{V_m}{r_f + R_L} = \frac{325}{1100} = 0.2955\ \text{A} \qquad I_{dc} = \frac{I_m}{\pi} = 0.0940\ \text{A} \qquad I_{rms} = \frac{I_m}{2} = 0.1477\ \text{A}$$
$$P_{dc} = I_{dc}^2 R_L = 8.84\ \text{W} \qquad P_{ac} = I_{rms}^2 (r_f + R_L) = 24.0\ \text{W} \qquad \eta = \frac{P_{dc}}{P_{ac}} = 36.8\ \%$$
(Max possible for half-wave is 40.6 %; r_f lowers it.)

**A1-Q6.** *Draw the output waveform.* Input: triangle wave ±20 V. Circuit: series R; across the output,
branch 1 = Si diode in series with a 10 V battery, branch 2 = Ge diode (reversed) in series with a
5 V battery; R_L across the output.
- Read from a low-resolution figure: branch 1 conducts when V_out > 10 + 0.7 = **10.7 V**, branch 2
  conducts when V_out < −(5 + 0.3) = **−5.3 V**. (Confirm the battery polarities on the student's copy.)
- Output: follows the input between −5.3 V and +10.7 V; flat at **+10.7 V** while the input is above it;
  flat at **−5.3 V** while the input is below it (assume R_L ≫ R).
- Draw: input triangle dashed, output solid with flat tops at 10.7 V and flat bottoms at −5.3 V.

### Block 4 — h-parameters

**Core ideas:** the transistor as a two-port box for small signals.
- h_ie = input resistance (Ω); h_re = reverse voltage ratio (no unit); h_fe = forward current gain;
  h_oe = output conductance (S).
- CE amplifier with load R_L, source R_s:
  $$A_I = \frac{-h_{fe}}{1 + h_{oe} R_L} \qquad Z_i = h_{ie} + h_{re} A_I R_L \qquad A_V = \frac{A_I R_L}{Z_i}$$
  $$Y_o = h_{oe} - \frac{h_{fe} h_{re}}{h_{ie} + R_s} \qquad Z_o = \frac{1}{Y_o} \qquad A_P = A_V A_I$$
- Approximate model (h_re, h_oe neglected): Z_i ≈ h_ie, A_I ≈ −h_fe, A_V ≈ −h_fe R_L / h_ie.

**A2-Q8 (= SA-5).** *h_ie = 1000 Ω, h_fe = 50, h_re = 2.5 × 10⁻⁴, h_oe = 25 × 10⁻⁶ A/V, R_L = 10 kΩ,
R_s = 100 Ω. Find input resistance, output resistance, voltage, current and power gains.*
- h_oe R_L = 25 × 10⁻⁶ × 10⁴ = 0.25. **A_I = −50/1.25 = −40.**
- **Z_i = 1000 + (2.5 × 10⁻⁴)(−40)(10⁴) = 1000 − 100 = 900 Ω.**
- **A_V = (−40)(10 000)/900 = −444.4.**
- Y_o = 25 × 10⁻⁶ − (50 × 2.5 × 10⁻⁴)/1100 = 25 × 10⁻⁶ − 11.36 × 10⁻⁶ = 13.64 × 10⁻⁶ S →
  **Z_o = 73.3 kΩ.**
- **A_P = (−444.4)(−40) = 17 778.**

**A2-Q10.** *CE, h_ie = 2000 Ω, h_oe = 10⁻⁴ S, h_re = 10⁻³, h_fe = 50, a.c. load r_L = 600 Ω. Find input
impedance, current gain, voltage gain using reasonable approximations.*
- h_oe r_L = 0.06 ≪ 1 and h_re small → approximate model is fine:
  **Z_i ≈ 2 kΩ, A_I ≈ −50, A_V ≈ −50 × 600/2000 = −15.**
- Exact values for comparison: A_I = −47.2, Z_i = 1972 Ω, A_V = −14.35 (approximation within 6 %).

### Block 5 — Feedback and oscillators

**Core ideas:**
- **Feedback:** part of the output (fraction β) is returned to the input. Negative feedback subtracts.
  With open-loop gain A:
  $$A_f = \frac{A}{1 + A\beta}$$
  (1 + Aβ) is the **desensitivity factor**; Aβ is the **loop gain**.
- Four types, named *sampling–mixing*: voltage-series, voltage-shunt, current-series, current-shunt.
  Series mixing raises input impedance; shunt mixing lowers it. Voltage sampling lowers output
  impedance; current sampling raises it. Each by the factor (1 + Aβ).
- **Oscillator:** positive feedback, no input. **Barkhausen criterion:** loop gain |Aβ| = 1 and total
  phase shift around the loop = 0° (or 360°).

**A4-Q7.** *Explain how negative feedback acts on loop gain, frequency, distortion, input impedance and
output impedance.* Table answer:

| Property | Effect of negative feedback (factor 1 + Aβ) |
|---|---|
| Gain | reduced: A_f = A/(1 + Aβ); becomes stable, set by β, insensitive to transistor changes |
| Bandwidth (frequency response) | increased: f_H,f = f_H(1 + Aβ), f_L,f = f_L/(1 + Aβ); gain × bandwidth constant |
| Distortion, noise | reduced by (1 + Aβ) |
| Input impedance | series mixing: ×(1 + Aβ); shunt mixing: ÷(1 + Aβ) |
| Output impedance | voltage sampling: ÷(1 + Aβ); current sampling: ×(1 + Aβ) |

**A4-Q8.** *Block diagram of current-series feedback; derive R_if and R_of.*
- Block diagram: source V_s → mixer (series, subtracting) → amplifier (transconductance G_M = I_o/V_i)
  → output current I_o through load R_L → feedback network senses I_o (series with load) and returns
  V_f = β I_o in series with the input.
- **R_if:** V_s = V_i + V_f = V_i + β G_M V_i = V_i(1 + βG_M); I_i = V_i/R_i →
  $$R_{if} = \frac{V_s}{I_i} = R_i (1 + \beta G_M)$$
- **R_of:** set V_s = 0, apply V at the output: V_i = −V_f = −β I. Output current I = V/R_o − G_M V_i
  = V/R_o + βG_M I → I(1 + βG_M) = V/R_o →
  $$R_{of} = \frac{V}{I} = R_o (1 + \beta G_M)$$
- Both increase (series mixing raises input, current sampling raises output impedance).

**A4-Q9.** *Colpitts oscillator, L = 40 mH, C1 = 100 pF, C2 = 500 pF. Find the frequency.*
$$C_{eq} = \frac{C_1 C_2}{C_1 + C_2} = \frac{100 \times 500}{600} = 83.33\ \text{pF} \qquad f = \frac{1}{2\pi\sqrt{L C_{eq}}} = 87.2\ \text{kHz}$$
(Colpitts: capacitive divider C1, C2 + one inductor. Hartley is the opposite: L1 + L2 + M with one C,
f = 1/(2π√((L1 + L2 + 2M)C)).)

**A4-Q10.** *RC phase-shift oscillator, R = 200 kΩ, C = 100 pF (three of each). Find the frequency.*
$$f = \frac{1}{2\pi R C \sqrt{6}} = \frac{1}{2\pi \times 200\ \text{k}\Omega \times 100\ \text{pF} \times 2.449} = 3.25\ \text{kHz}$$
(Three RC sections give 180°, the inverting amplifier the other 180°; the amplifier gain must be
|A| ≥ 29 to sustain oscillation.)

### Block 6 — Semiconductor physics

**Core ideas:**
- **Conductivity** σ (S/m or S/cm) = how easily current flows; resistivity ρ = 1/σ.
  $$\sigma = q(n \mu_n + p \mu_p)$$
  n, p = electron and hole concentrations; μ = mobility (drift speed per unit field).
- Intrinsic: n = p = n_i. Doped n-type: n ≈ N_D. p-type: p ≈ N_A. **Mass-action law:** n p = n_i².
- "1 donor in 10⁸ atoms": N_D = (atoms per volume)/10⁸.
- **Diode equation:** I = I_0(e^{V/ηV_T} − 1), η = 1 (Ge), 2 (Si, low current) — these questions use η = 1.
  Static resistance R = V/I; dynamic resistance r = ηV_T/(I + I_0).
- **Drift velocity** v = μE.

**A1-Q5.** *Si atom density 5 × 10²⁸ /m³; donor 1 in 10⁸; n_i = 1.5 × 10¹⁶ /m³; μ_n = 0.135 m²/V·s.
Find the resistivity.*
N_D = 5 × 10²⁸/10⁸ = 5 × 10²⁰ /m³ ≫ n_i → n = 5 × 10²⁰.
$$\rho = \frac{1}{q N_D \mu_n} = \frac{1}{1.6\times10^{-19} \times 5\times10^{20} \times 0.135} = 0.0926\ \Omega\,\text{m}$$

**SA-1.** *Conductivity of Si (a) intrinsic at 300 K (b) donor 1 in 10⁸ (c) acceptor 1 in 5 × 10⁷
(d) both together.* Data from B2 (n_i = 1.5 × 10¹⁰ cm⁻³, μ_n = 1300, μ_p = 500, 5 × 10²² atoms/cm³).
(a) σ = 1.6 × 10⁻¹⁹ × 1.5 × 10¹⁰ × 1800 = **4.32 × 10⁻⁶ S/cm**.
(b) N_D = 5 × 10¹⁴ cm⁻³: σ = qN_Dμ_n = **0.104 S/cm**.
(c) N_A = 10¹⁵ cm⁻³: σ = qN_Aμ_p = **0.080 S/cm**.
(d) Net acceptors N_A − N_D = 5 × 10¹⁴ (p-type): σ = q × 5 × 10¹⁴ × 500 = **0.040 S/cm**.

**SA-7.** *n-type Si at 300 K with σ = 300 S/cm: find hole and electron concentrations; same for p-type.
n_i = 1.5 × 10¹⁰, μ_n = 1300, μ_p = 500.*
- n-type: n = σ/(qμ_n) = 300/(1.6 × 10⁻¹⁹ × 1300) = **1.44 × 10¹⁸ cm⁻³**; p = n_i²/n = **156 cm⁻³**.
- p-type: p = 300/(1.6 × 10⁻¹⁹ × 500) = **3.75 × 10¹⁸ cm⁻³**; n = n_i²/p = **60 cm⁻³**.

**A1-Q1.** *Intrinsic Ge: ρ = 0.47 Ω·m, μ_n = 0.39, μ_p = 0.19 m²/V·s. Find n_i and the drift velocities at
E = 10 kV/m.*
$$n_i = \frac{1}{\rho q(\mu_n + \mu_p)} = \frac{1}{0.47 \times 1.6\times10^{-19} \times 0.58} = 2.29\times10^{19}\ /\text{m}^3$$
v_n = 0.39 × 10⁴ = **3900 m/s**; v_p = 0.19 × 10⁴ = **1900 m/s**.

**A1-Q2.** *Ge diode at 27 °C: I = 10 mA at V_D = 0.3 V. (a) I at 0.4 V (b) reverse saturation current.*
(a) Ratio of diode equations (the −1 is negligible):
$$I_2 = I_1 e^{(V_2 - V_1)/V_T} = 10\ \text{mA} \times e^{0.1/0.026} = 468\ \text{mA}$$
(b)
$$I_0 = \frac{I}{e^{V/V_T} - 1} = \frac{10\ \text{mA}}{e^{0.3/0.026}} = 9.75\times10^{-8}\ \text{A} \approx 0.1\ \mu\text{A}$$

**A1-Q4.** *Ge diode, 27 °C, I_0 = 1 μA, forward bias 0.2 V: static and dynamic resistance; current change
if T rises to 40 °C.*
- I = 1 μA × (e^{0.2/0.026} − 1) = **2.19 mA**. Static R = 0.2/2.19 mA = **91.3 Ω**. Dynamic r = 0.026/2.19 mA
  = **11.9 Ω**.
- 40 °C: I_0 = 1 μA × 2^{1.3} = 2.46 μA; V_T = 8.62 × 10⁻⁵ × 313 = 0.02698 V;
  I = 2.46 μA × (e^{0.2/0.02698} − 1) = **4.08 mA** → increase ≈ **1.89 mA** (current nearly doubles).

**A1-Q3.** *Minority hole density: N_D = 1.5 × 10¹⁶ cm⁻³, T = 270 K, n_i = 2 × 10⁹ cm⁻³, forward bias
0.93 V (Si PN junction).*
- Equilibrium: p_n0 = n_i²/N_D = 4 × 10¹⁸/1.5 × 10¹⁶ = **266.7 cm⁻³**.
- At the junction edge under forward bias (law of the junction), V_T = 8.62 × 10⁻⁵ × 270 = 0.02327 V:
  $$p_n(0) = p_{n0}\, e^{V/V_T} = 266.7 \times e^{39.96} = 6.0\times10^{19}\ \text{cm}^{-3}$$
- Write both values; the question is ambiguous about which is wanted.

**A1-Q7.** *N_C = 1.5 × 10²⁴ /m³, N_V = 1.3 × 10²⁵ /m³, E_G = 1.43 eV, T = 300 K. (a) intrinsic Fermi level
relative to midgap and to E_V (b) n_i.*
kT = 0.02586 eV.
$$E_{Fi} - E_{mid} = \frac{kT}{2}\ln\frac{N_V}{N_C} = 0.01293 \times \ln 8.667 = +0.0279\ \text{eV}$$
(above midgap). E_Fi − E_V = 1.43/2 + 0.0279 = **0.743 eV**.
$$n_i = \sqrt{N_C N_V}\, e^{-E_G/2kT} = 4.42\times10^{24} \times e^{-27.65} = 4.34\times10^{12}\ /\text{m}^3$$

### Block 7 — theory extras

**SA-4 (asked twice). Compensation techniques for amplifier (bias) stabilization.**
- Stabilization (R_E, divider) uses feedback; **compensation** uses temperature-sensitive devices that
  cancel the drift.
1. **Diode compensation for V_BE**: a diode in the emitter/divider circuit at the same temperature;
   V_BE falls ≈ 2.5 mV/°C and the diode voltage falls equally, so the changes cancel and I_C stays put.
2. **Diode compensation for I_CO**: a reverse-biased diode across the base supply; its reverse current
   rises with temperature exactly like I_CO and draws it away from the base.
3. **Thermistor** (negative temperature coefficient) in place of R2 or in the emitter: resistance falls
   as T rises, lowering V_B and counteracting the rise of I_C.
4. **Sensistor** (positive coefficient) in place of R1 / in parallel: same effect, opposite sign.
Draw: voltage-divider circuit with the diode/thermistor shown in its position.

---

## Part D: FinFET and the units after it (U4 FinFET, U5 BJT, U6 Feedback, U7 Oscillators). Teach these first (see B0)

These come from the professor's decks L20–L27, the U6 feedback deck and the U7 oscillator decks.
Every number has been recomputed. Teach each item in the Part B format: concept, worked example
with a reason for every step, final hand-in answer, marks lost for. Write the formulas below in
LaTeX with \frac so that fractions stack.

### D0. FinFET (two U4 decks: "structure vs MOSFET" and "types and fabrication")
Teach this first. Expect short answers (4–8 marks): why FinFET, structure, types, fabrication
steps, comparison with the MOSFET, advantages and disadvantages. Draw a 3-D sketch of a fin with
the gate wrapped over it, and label S, D, G, the fin, the oxide and the substrate.

- **Why multigate (short-channel effects).** When a planar MOSFET is scaled to tens of nanometres,
  the drain is so close to the source that its field reaches into the channel, and the gate loses
  control. This causes three short-channel effects:
  1. the threshold voltage V_th shifts (falls);
  2. the subthreshold slope degrades, so the transistor no longer turns off sharply;
  3. the off-state current I_OFF rises (leakage).
  Overall performance (the figure of merit) drops. A multigate FinFET fixes this, so scaling can
  continue.
- **Structure.** FinFET stands for Fin Field-Effect Transistor. It is a non-planar (3-D) multigate
  MOSFET.
  - The channel is a thin vertical **fin** of silicon between source and drain. It is named after
    the back fin of a fish.
  - The **gate** wraps over the fin on **three sides**: both side walls and the top. This gives
    strong electrostatic control of the whole thin body.
  - Source and drain play the same roles as in a MOSFET.
  - The substrate is the base; it can be bulk silicon or SOI (silicon-on-insulator).
  - It is still a 3-terminal device (G, D, S), except for the IG type below.
- **Effective width.** Current flows on three faces of the fin, so the width of one fin is
  W = W_F + 2H_F, where W_F is the fin width and H_F the fin height.
  - Worked example: W_F = 6 nm, H_F = 50 nm gives W = 6 + 2(50) = **106 nm** per fin.
  - H_F is fixed by the process, so a wider transistor needs **more fins**: n fins give n × W.
    Width is therefore quantized.
- **Fin spacing S_F** is fixed by the technology.
  - Too close: the fields of neighbouring fins interact, parasitic capacitance rises, and the gate
    loses independent control of each fin.
  - Too far apart: poor area efficiency, because fewer fins fit in the layout.
- **Channel doping is optional.** A planar MOSFET dopes its channel to fight short-channel effects
  and set V_th. The FinFET's thin body and wrap-around gate already suppress those effects. Leaving
  the channel undoped gives less variation from dopants and higher mobility. The result is a lower
  V_th, faster operation and lower power.
- **Types:**
  - **Shorted-gate (SG, 3-terminal):** the two side gates are tied together and control the channel
    jointly. Higher I_on, but also higher I_off.
  - **Independent-gate (IG, 4-terminal):** the two gates are driven separately. The back-gate bias
    tunes the front gate's V_th linearly. The cost is a large area penalty, because it needs two
    gate contacts.
- **Fabrication steps (bulk wafer):**
  1. **Substrate:** a lightly p-doped wafer, with a hard mask (silicon nitride) and a patterned resist on top.
  2. **Fin etch:** a highly anisotropic etch. It is time-based, because a bulk wafer has no etch-stop
     layer. In a 22 nm process the fins are 10–15 nm wide and ideally at least twice as tall.
  3. **Oxide deposition:** an oxide with high-aspect-ratio fill, to isolate the fins from each other.
  4. **Planarization:** chemical-mechanical polishing (CMP), with the hard mask as the stop layer.
  5. **Recess etch:** etch the oxide back to expose the fins and leave lateral isolation.
  6. **Gate oxide:** thermal oxidation on the fins. A high-dose angled implant at the base of each
     fin completes the isolation.
  7. **Gate deposition:** n⁺ polysilicon over the fins, which gives up to three gates (two sides, plus
     the top depending on how thick the top oxide is).
- **MOSFET vs FinFET (the deck's table; write at least 6 rows):**

  | | MOSFET | FinFET |
  |---|---|---|
  | Gates | single gate | multigate |
  | Shape | planar | non-planar, 3-D fins |
  | Power | more | less |
  | Switching speed | slower | faster |
  | Leakage current | more | less |
  | Parasitic R and C | less | more (3-D shape) |
  | Voltage gain | less | more (better control → higher g_m) |
  | Fabrication | easy and cheap | complex and costly |

- **Advantages:**
  - better channel control and suppressed short-channel effects;
  - lower static leakage, so low standby power;
  - faster switching and a sharp on/off;
  - higher drain current;
  - lower switching voltage and lower power.
- **Disadvantages:**
  - self-heating (heat is hard to remove from a thin fin);
  - quantized device width (whole fins only);
  - higher parasitics and very high capacitance;
  - corner effect;
  - high fabrication cost.
- **Marks lost for:**
  - Saying the gate covers four sides (that is gate-all-around, not FinFET).
  - Listing "leakage" without naming the three short-channel effects.
  - Writing the width as W_F alone instead of W_F + 2H_F.
  - Leaving out the disadvantages when asked for a comparison.

### D1. BJT basics (decks L20–L25)
- **Structure:** n-p-n or p-n-p, so two junctions, EB and CB. The emitter is heavily doped so that
  it injects carriers. The base is thin and lightly doped so that only about 1% of those carriers
  recombine there. The collector is the largest region because it dissipates the most heat.
- **Regions:**
  - Active: EB forward, CB reverse; I_C = βI_B. Used as an amplifier.
  - Saturation: both junctions forward; V_CE(sat) ≈ 0.2 V. Closed switch.
  - Cutoff: both junctions reverse; I_C ≈ 0. Open switch.
- **Currents:** I_E = I_C + I_B. α = I_C / I_E (0.95–0.995). β = I_C / I_B (50–400). γ = I_E / I_B = 1 + β.
- **Relations** (derive by substituting I_E = I_C + I_B):
  β = α / (1 − α), α = β / (1 + β), γ = 1 / (1 − α).
- **Leakage:** I_C = αI_E + I_CBO, and I_C = βI_B + (1 + β)I_CBO. Hence I_CEO = (1 + β)I_CBO.
- **CB / CE / CC comparison table:**

  | | CB | CE | CC |
  |---|---|---|---|
  | Input / output | E / C | B / C | B / E |
  | Current gain | α < 1 | β, high | 1 + β |
  | Voltage gain | high | high | just under 1 |
  | R_in | very low | about 1 kΩ | very high |
  | R_out | very high | medium | very low |
  | Phase | 0° | 180° | 0° |
  | Use | high frequency | general amplifier (highest power gain) | buffer |

- **Characteristics:**
  - CB input: I_E against V_EB, like a forward diode.
  - CE input: I_B against V_BE, like a forward diode; the curve shifts right as V_CE rises (Early effect).
  - CE output: I_C against V_CE, one curve per I_B. Nearly flat in the active region; the saturation
    region is near V_CE = 0; cutoff is below the I_B = 0 curve.
  - Draw all of these with labelled axes and regions.
- **Worked example 1:** β = 100, I_CBO = 20 nA. Then α = 100/101 = **0.990** and
  I_CEO = 101 × 20 nA = **2.02 μA**.
- **Worked example 2:** α = 0.98. Then β = 0.98/0.02 = **49** and γ = **50**.
- **Worked example 3:** I_E = 10 mA, α = 0.99. Then I_C = **9.9 mA** and I_B = **0.1 mA**.
- **BJT vs MOSFET (write at least 8 rows):**

  | | BJT | MOSFET |
  |---|---|---|
  | Control | current-controlled | voltage-controlled |
  | Carriers | bipolar | unipolar |
  | R_in | about 1 kΩ | 10¹⁰ Ω or more |
  | Law | exponential | square law |
  | g_m | higher (I_C/V_T = 38 mS at 1 mA) | lower |
  | Temperature | thermal runaway risk | self-limiting (mobility falls) |
  | Switching | slower (stored charge) | faster |
  | Static power in logic | yes | CMOS ≈ 0 |
  | Density | lower | far higher |
  | Static damage | robust | oxide damaged by static |

- **Marks lost for:** swapping α and β; leaving out the (1 + β) on the leakage; saying CC has voltage gain.

### D2. Biasing and stability (decks L26–L27)
- **Fixed bias, deck slide 15.** V_CC = 12 V, R_B = 240 kΩ, R_C = 2.2 kΩ, β = 50.
  - I_B = (V_CC − 0.7)/R_B = **47.08 μA**; I_C = βI_B = **2.35 mA**.
  - V_CE = V_CC − I_C·R_C = **6.82 V**; I_C(sat) = V_CC/R_C = **5.45 mA**.
  - Load-line ends: (12 V, 0) and (0, 5.45 mA).
  - Follow-up: with β = 100, I_C becomes 4.71 mA and V_CE 1.64 V, so Q moves to near saturation.
    This shows that fixed bias is β-dependent.
- **Why Q drifts:**
  - I_CO doubles for every 10 °C rise.
  - V_BE falls by 2.5 mV per °C.
  - β rises with temperature and varies between devices.
  - All three raise I_C. The result is thermal runaway: more I_C, more heat, more I_C.
- **Stability factors:** S = ∂I_C/∂I_CO (ideal 1; smaller is better), S′ = ∂I_C/∂V_BE, S″ = ∂I_C/∂β.
- **Derivation:** start from I_C = βI_B + (1 + β)I_CO and differentiate with respect to I_C.
  This gives S = (1 + β) / (1 − β·dI_B/dI_C).
- **Table of S:**
  - Fixed bias: dI_B/dI_C = 0, so S = 1 + β (worst).
  - Emitter bias: S = (1 + β)(1 + R_B/R_E) / (1 + β + R_B/R_E).
  - Voltage-divider bias: the same with R_B → R_Th (best, because R_Th is small).
  - Collector-to-base bias: S = (1 + β) / (1 + βR_C/(R_B + R_C)).
- **Emitter bias, deck slide 27.** V_CC = 20 V, R_B = 430 kΩ, R_C = 2 kΩ, R_E = 1 kΩ, β = 50.
  - I_B = (V_CC − 0.7)/(R_B + (β + 1)R_E) = 19.3/481k = **40.1 μA**; I_C = **2.01 mA**.
  - V_CE = 20 − 2.01(2) − 2.05(1) = **13.94 V**.
  - S = 51 × 431/481 = **45.7**, against 51 for fixed bias.
  - How R_E stabilises: if I_C rises, V_E rises, so I_B falls and pulls I_C back (negative feedback).
- **Voltage-divider bias.** V_CC = 22 V, R1 = 39k, R2 = 3.9k, R_C = 10k, R_E = 1.5k, β = 100.
  - Thévenin: E_Th = 2.0 V, R_Th = 3.55 kΩ.
  - Exact: I_B = 1.3/(3.55k + 151.5k) = 8.38 μA, so **I_C = 0.838 mA** and **V_CE = 12.35 V**; **S = 3.29**.
  - Approximate (valid when βR_E ≥ 10R2: 150k ≥ 39k ✓): V_E = 1.3 V, so **I_C ≈ 0.867 mA**.
- **Compensation** (the same as SA-4): a diode in the base circuit tracks V_BE; a thermistor in the
  R2 arm; a sensistor in the R1 arm or the emitter.
- **Marks lost for:**
  - Leaving out the R_E drop in V_CE.
  - Missing the (β + 1) in front of R_E.
  - Not checking βR_E ≥ 10R2.
  - Writing I_C(sat) = V_CC/R_C when R_E is present (it is V_CC/(R_C + R_E)).

### D3. h-parameters, multistage, Darlington (deck L26–27 and the book sheet pp. 131–145)
- **Model:** v_be = h_ie·i_b + h_re·v_ce and i_c = h_fe·i_b + h_oe·v_ce.
  - h_ie: input resistance, measured with the output shorted (Ω).
  - h_re: reverse voltage ratio, measured with the input open.
  - h_fe: forward current gain, measured with the output shorted.
  - h_oe: output admittance, measured with the input open (S).
  - They are "hybrid" because their units are mixed. Draw the equivalent circuit.
- **Exact CE analysis.** Do it in this order, because each step uses the one before:
  1. A_i = −h_fe/(1 + h_oe·R_L)
  2. R_i = h_ie + h_re·A_i·R_L
  3. A_v = A_i·R_L/R_i
  4. Y_o = h_oe − h_fe·h_re/(h_ie + R_s)
  - Also: A_vs = A_v·R_i/(R_i + R_s), A_p = A_i·A_v, R_ot = R_o ∥ R_L.
  - Approximate (valid when h_oe·R_L < 0.1): A_i = −h_fe, R_i = h_ie, A_v = −h_fe·R_L/h_ie.
- **Worked example (book P9).** R_s = 800 Ω, R_L = 2k, h_ie = 1.1k, h_fe = 50, h_oe = 25 μS,
  h_re = 2.5 × 10⁻⁴.
  - **A_i = −47.6**, **R_i = 1076.2 Ω**, **A_v = −88.5**, A_vs = −50.75.
  - Y_o = 18.42 μS, so **R_o = 54.29 kΩ**; **R_ot = 1.93 kΩ**; **A_p = 4214**.
  - Approximate: A_i = −50, R_i = 1100, A_v = −90.9. Error in A_i = **5%**.
- **Cascade:** the overall gain is the product of the loaded stage gains. Gains of 40 and 60 give
  **2400**, which is **67.6 dB** (in dB the stage gains add).
  - Couplings: RC (cheap, blocks DC), transformer (impedance matching, bulky),
    direct (amplifies down to DC, but drift is amplified).
- **Darlington:** β_D = β1β2 + β1 + β2 ≈ β1β2. Derive it from I_E1 = I_B2.
  - V_BE ≈ 1.4 V and the input resistance is very high.
  - β = 100 each gives **10 200**.
- **Marks lost for:** finding R_i before A_i; dropping the minus signs; reading μmho as mho;
  leaving R_s out of Y_o.

### D4. Feedback amplifiers (U6 deck, 51 slides)
- **Closed-loop gain:** V_i = V_s − βV_o, so A_f = A/(1 + βA).
  - Loop gain = βA. Desensitivity D = 1 + βA.
  - When βA ≫ 1, A_f ≈ 1/β.
- **Worked example (deck slide 32).** β = 0.01.
  - A = 1000 gives A_f = **90.9**. A = 10 000 gives A_f = **99.0**.
  - A changes by 900% but A_f by only 9%. The slide prints 98.3 for A = 5000; the correct value is 98.0.
- **The four amplifier types:**
  - Voltage amplifier: high R_i, low R_o.
  - Current amplifier: low R_i, high R_o.
  - Transconductance amplifier: high R_i, high R_o.
  - Transresistance amplifier: low R_i, low R_o.
- **The four topologies (sampling – mixing):**
  - Voltage-series: Z_if ×(1+βA), Z_of ÷(1+βA). Example: emitter follower.
  - Voltage-shunt: Z_if ÷, Z_of ÷. Example: collector-to-base resistor.
  - Current-series: Z_if ×, Z_of ×. Example: CE with an unbypassed R_E.
  - Current-shunt: Z_if ÷, Z_of ×. Example: two stages, 2nd emitter → 1st base.
  - Rule: a series connection raises the resistance at that port; a shunt connection lowers it.
- **Effects of negative feedback:**
  - Gain is reduced to A/(1 + βA).
  - Gain is stabilised: dA_f/A_f = (dA/A)/(1 + βA). Derive this by differentiating A_f.
  - Bandwidth widens: f_Hf = f_H(1 + βA) and f_Lf = f_L/(1 + βA).
  - Distortion and noise fall: D_f = D/(1 + βA).
  - Impedances change as in the topology list above.
  - Disadvantages: lower gain, so more stages are needed; possible oscillation.
- **Worked example.** A = 1000, f_H = 20 kHz, Z_i = 2k, Z_o = 20k, 10% distortion; voltage-series
  feedback with β = 0.1.
  - 1 + βA = 101, so **A_f = 9.90** and **f_Hf = 2.02 MHz**.
  - **Z_if = 202 kΩ**, **Z_of = 198 Ω**, distortion **0.099%**.
- **Marks lost for:** confusing the feedback β with the transistor's β; saying current sampling
  lowers Z_o.

### D5. Oscillators (U7 decks)
- **Barkhausen criterion:** |βA| = 1 and a total loop phase of 0° or 360°.
  - With positive feedback A_f = A/(1 − βA), which is infinite when βA = 1.
  - Oscillation starts from noise with |βA| slightly above 1.
  - Types: RC for audio (phase-shift, Wien); LC for 100 kHz–100 MHz (Hartley, Colpitts);
    crystal (very stable); relaxation.
- **RC phase-shift oscillator:**
  - An inverting amplifier (180°) plus three RC sections (180°).
  - f₀ = 1/(2πRC√6); β = 1/29, so |A| ≥ 29 and R_f = 29R.
  - BJT version: f₀ = 1/(2πRC√(6 + 4R_C/R)), h_fe ≥ 23 + 29R/R_C + 4R_C/R.
  - **Design example:** 800 Hz with C = 10 nF gives R = **8.12 kΩ** (use 8.2k) and R_f = **238 kΩ**.
- **Wien bridge oscillator:**
  - A non-inverting amplifier and a lead-lag network (0°).
  - f₀ = 1/(2πRC); β = 1/3, so A = 3 and R2 = 2R1.
  - **Example:** R = 10k, C = 10 nF gives f₀ = **1.59 kHz**; R2 = **20k**.
  - Compare it with the phase-shift oscillator: a table of amplifier, network, f₀, β, gain, tuning.
- **Hartley vs Colpitts:**
  - Hartley taps the inductor: L_eq = L1 + L2 (+2M if coupled) and f₀ = 1/(2π√(L_eq·C)).
  - Colpitts taps the capacitor: C_eq = C1C2/(C1 + C2) and f₀ = 1/(2π√(L·C_eq)).
  - **Colpitts example:** C1 = C2 = 200 pF, L = 1 mH gives C_eq = 100 pF and f₀ = **503 kHz**.
  - **Hartley example:** L1 = L2 = 1 mH, C = 100 pF gives f₀ = **356 kHz**.
- **Crystal oscillator:**
  - Piezoelectric effect: squeezing quartz produces a voltage. Inverse effect: a voltage makes it vibrate.
  - Equivalent circuit: R_s, L_s, C_s in series, all in parallel with C_p.
  - f_s = 1/(2π√(L_sC_s)) and f_p = f_s√(1 + C_s/C_p).
  - **Example:** L_s = 1 H, C_s = 0.01 pF, R_s = 1k, C_p = 10 pF.
    f_s = **1.592 MHz**, f_p is **796 Hz** above it, and **Q = 10 000** (an LC tank has about 100),
    which is why it is very stable.
- **Marks lost for:** swapping 29 and 3; adding C1 + C2 in a Colpitts; leaving out the √6 or the
  square root.
