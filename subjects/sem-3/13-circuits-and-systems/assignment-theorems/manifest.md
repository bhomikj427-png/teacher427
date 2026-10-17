# Manifest: ECE2107 theorems, assignment marathon

Protocol: `../../../../marathon.md`. Mode: **assignment** (every question in scope, nothing dropped).
Scope = the 171 confirmed questions (Ghosh & A K Chakraborty 4e ch. 5 solved 5.1–5.44; Alexander & Sadiku 5e
ch. 4 §4.3–4.8, ch. 10 §10.4–10.6, ch. 11 §11.3, end-of-chapter + practice problems). Possible additions if the
professor confirms ~300: Chakraborty reciprocity/Millman, exercises, MCQs; rest of Sadiku ch. 4.

Status key: `built` = in the PDF; `miss` = learner reported it unsolved (then: note added). Verified = full
circuit solve with all sources on + every partial (`src/verify.py`).

## Part A · Chakraborty · Superposition (batch 1)

| Q | Ideas (★ = new here) | Book answer | Verified answer | Status |
|---|---|---|---|---|
| 5.1 | ★method, ★switch-off rules, ★signs, ★series-with-I / parallel-with-V shortcuts | 0 | 0 A | built |
| 5.2 | ★AC phasors, ★complex dividers | 1 V | 1∠0° V | built |
| 5.3 | ★dependent source stays, ★controlling variable per case (VCVS) | −2/11 A | −2/11 A | built |
| 5.4 | ★source with angle, ★polar quadrant | 1.2∠123.7° A | 1.2∠123.7° A | built |
| 5.5a | practice | 2.9∠26.56° A | 2.91∠26.57° A | built |
| 5.5b | ★mixed frequencies (DC + AC), ★L short at DC, ★add in time domain | 2.63∠−63.58° A | 4 + 0.791 cos(4t − 71.57°) A | built · **book error** |
| 5.5c | ★redraw after switch-off | 0.81∠39.38° A | 1.19∠65.45° A | built · **book error** |
| 5.6 | ★reactance per ω, ★sin/cos kept separate | 4.631 sin(5t−81.12°) + 1.051 cos(10t−86.24°) | 4.631 sin(5t−81.12°) + 10.50 cos(10t−86.24°) V | built · **book uses 2 A, figure says 20 A** |
| 5.7 | ★current-controlled source (CCVS) | i = 0.5, i₀ = −0.5 A | i = 1.125, i₀ = 0.125 A | built · **book error** |
| 5.8 | practice (AC, sign of reversed branch current) | 1.733∠40.14° A | 1.73∠40.13° A | built |
| 5.9 | ★three sources, ★open terminals, ★source transformation inside a case | −5 V | −5 V | built |
| 5.10 | ★transform a dependent source, ★current source fixes mesh current | −2 A | −2 A | built |
| 5.11 | practice (dependent + three sources; figure omits 10 V label) | −6 V | −6 V | built |
| 5.12 | ★contributions cancel (zero answer) | 0 | 0 A | built |
| 5.13 | practice (AC; figure labels current source "V") | 6.89∠−163.67° A | 6.87∠−164.05° A | built |
| 5.14 | practice (VCVS) | 2.4 A | 2.4 A | built |

## Part A · Chakraborty · Thevenin / Norton (batch 2)

Verified = `src/verify_b2.py`: V_oc, I_sc and Z_th by full netlist solves, test-source cross-checks where
dependent sources appear, the full circuit with the load in place, and RK4 simulation for 5.28 / 5.30.

| Q | Ideas (★ = new here) | Book answer | Verified answer | Status |
|---|---|---|---|---|
| 5.15 | ★Thevenin recipe, ★R_th by switching off | i = 1.40625 A | 45/11 V, 10/11 Ω, i = 45/32 A | built (book typo i₁ = 5/11, is 35/11) |
| 5.16 | ★dependent source ⇒ V_oc/I_sc, ★sign of I_sc, ★negative R_th | I = 2 A | V_th = 8 V, R_th = −2 Ω, no solution with 2 Ω load | built · **book error** (sign dropped) |
| 5.17 | ★iterative Thevenin (ladder) | 0.002 A | 2.160 V, 1052.3 Ω, 2.033 mA | built |
| 5.18 | ★ideal op-amp rules, ★1 A test source | 1 mA | 4.8 V, 800 Ω, 1 mA | built |
| 5.19 | practice (VCCS; element in series with I-source) | R_th = 4.22 Ω | 10 V, 38/9 Ω | built |
| 5.20 | ★floating terminals V_a − V_b (AC) | 9.45∠−169.1° A | 9.449∠−169.11° A | built |
| 5.21a | practice (AC, source transformation) | 67.08∠−63.4°, 7.07∠−81.86° | 67.08∠−63.43° V, 1 − j7 Ω | built |
| 5.21b | practice (AC) | 10∠0°, 5.59∠−26.56° | 10∠0° V, 5 − j2.5 Ω | built (book typo j120) |
| 5.21c | practice (AC, load across AB) | 29.553∠−34.16°, 5.33∠−0.5° | 29.55∠−34.16° V, 5.328∠−0.47° Ω | built |
| 5.21d | ★s-domain Thevenin | 4s/((s²+4)(s+2)), 1 Ω | same (checked at 3 values of s) | built |
| 5.21e | ★V_th and I_N separately (AC, CCCS) | 3.48∠84.3°, 0.6∠31°, 5.8∠53.3° | 3.483∠84.29°, 0.600∠30.96°, 5.802∠53.33° | built |
| 5.22 | practice (AC, dependent source transformed) | V₀ = 1.27∠32° V | V_th 3.073∠−39.81°, I_N 1.342∠63.43°, V₀ = 2.299∠16.70° V | built · **book error** (mesh-2 self-impedance −j6 for −j10) |
| 5.23 | ★Norton form | 3.33 A ∥ 3.75 Ω | same; V_th = 12.5 V | built |
| 5.24 | ★equivalent from a v–i line | 40 A ∥ 1/8 Ω | same (figure's i arrow reversed → note) | built |
| 5.25 | practice (I_sc by superposition) | 9/5 A, 5/3 Ω, 3 V | same | built |
| 5.26 | (broken question) | −29 V, 38.67 kΩ | figure has no A, B; solution circuit: −29.03 V, 38.71 kΩ | built · **book error** (figure ≠ solution) |
| 5.27 | practice (negative R_th) | 2 V, 16.67 Ω | 50 kΩ (figure): 1.5004 V, −12.50 Ω; 50 Ω: 2 V, −16.67 Ω | built · **book error** (50 Ω vs 50 kΩ; sign dropped) |
| 5.28 | ★transient via Norton in s-domain | 3/4 − 3/4e^{−2t} − 3/2e^{−t}sin t | C = 2 F: 3/4 − 3/4e^{−2t} − 3/2·t·e^{−t} A | built · **book error** (uses C = 1 F) |
| 5.29 | practice (VCCS, Thevenin with negative V_th) | −125 V, 25 Ω | same | built |
| 5.30 | ★initial-condition sources L·i(0) | 10/3 − 2e^{−10t} + 2/3e^{−30t} | same (RK4 agrees) | built |
| 5.31 | ★symbolic Thevenin | proof | proof; numeric check at 2 points | built |
| 5.32 | practice (AC, current source) | 111.8∠93.43°, 50∠36.87° | same | built |
| 5.33 | practice (CCCS) | 7.2 V, 2 Ω | same | built |
| 5.34 | ★no independent source ⇒ V_th = 0, test source | V_th = 0, −3.33 Ω | same | built |

## Part A · Chakraborty · Maximum power transfer (batch 3)

Verified = `src/verify_b3.py`: V_th, Z_th by netlist solve, then the load power maximised by brute-force
sweep of the full circuit (never using the theorem). Phasor magnitudes taken as rms (book convention).

| Q | Ideas (★ = new here) | Book answer | Verified answer | Status |
|---|---|---|---|---|
| 5.35 | ★powers don't superpose; ± current signs give max/min | 245/5 W; 1080/0 W | same | built (book typo in (b) bracket) |
| 5.36a | ★MPT DC: R = R_th, P = V²/4R | 0.85 Ω, 12 W | 0.85 Ω, 12.05 W | built |
| 5.36b | ★element across a V-source dropped; source transformations | 7/4 Ω, 1.08 W | same | built |
| 5.36c | ★R between two non-ground nodes | 5.33 Ω, 0.188 W | 5.33 Ω, 0.1875 W | built |
| 5.37 | ★AC conjugate match | 1.8 + j2.4 Ω, 0.694 W | same | built |
| 5.38a | practice (Z_L only) | 7.5 + j2.4 Ω | 7.5 + j2.5 Ω | built (book typo) |
| 5.38b | practice (Z_L only, mixed sources) | 5.316 − j3.07 Ω | 5.3165 − j3.0718 Ω | built |
| 5.39 | ★resistive-only load: R = \|Z_th\| (or calculus) | 0.5 Ω, 1 W | same | built (book typo 4 × 0.4) |
| 5.40 | practice (CCVS, V_oc/I_sc) | 37.5 W | 6 Ω, 37.5 W | built |
| 5.41 | practice (AC) | 1.6 − j6.4 Ω, 1062.5 W | same | built |
| 5.42 | practice (AC, two sources) | 4.23 + j1.154 Ω, 5.676 W | 4.231 + j1.154 Ω, 5.682 W | built (book rounds \|V\| to 9.8) |
| 5.43 | ★Z_th from terminal measurements | 12 + j5 Ω; 12 − j5 Ω; 1408.33 W | same | built |
| 5.44 | practice (AC, two sources) | 2.54 − j0.22 Ω | same | built |

**Part A complete: 44/44 in-scope Chakraborty solved problems built.**

## Still to build

| Batch | Questions |
|---|---|
| 4+ | Sadiku ch. 4: practice problems 4.3–4.13; end-of-chapter 4.8–4.75 by section |
| later | Sadiku ch. 10 §10.4–10.6 (10.40–10.68 + PP 10.4–10.10); ch. 11 §11.3 (11.12–11.21 + PP 11.4–11.5) |

Draft Sadiku pages from the demo (PP 4.3, 4.8, 4.9) are parked in `src/later/`.
