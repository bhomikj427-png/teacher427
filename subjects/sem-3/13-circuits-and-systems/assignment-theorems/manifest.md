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
| 5.3 | ★dependent source stays, ★controlling variable per case (VCVS) | −2/11 A | −2/11 A | built · **miss 2026-10-21** → v2 demo (How/What/Why) |
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

## Part B · Sadiku 5e · §4.3 Superposition (batch 4)

Verified = `src/verify_b4.py`: full netlist solve with all sources on, plus every independent source alone
(dependent sources kept); the partials must add to the full answer. "= App. D" = Appendix D odd-number answer.

| Q | Ideas (★ = new here) | Book answer | Verified answer | Status |
|---|---|---|---|---|
| PP 4.3 | practice | 7.4 V | 7.4 V (5 + 2.4) | built |
| PP 4.4 | practice (VCCS) | 31.25 V | 31.25 V (6.25 + 25) | built |
| PP 4.5 | practice (three sources) | 375 mA | 0.375 A (0.5 − 0.375 + 0.25) | built |
| 4.8 | ★one-node KCL shortcut | (even) | 54/13 = 4.154 V | built |
| 4.9 | ★linearity from measurements | 2 A | 2 A | built |
| 4.10 | ★design problem (one sample design) | multiple answers | V=12, R=4, I=3, k=2 → 8 V | built |
| 4.11 | practice (CCCS) | 1.799 A, 17.99 V | 1.8 A, 18 V | built |
| 4.12 | practice (current source between nodes) | (even) | −0.125 V | built |
| 4.13 | practice | 8.696 V | 200/23 = 8.696 V | built |
| 4.14 | practice | (even) | 8 V | built |
| 4.15 | practice (power after summing) | 1.875 A, 10.55 W | same | built |
| 4.16 | practice | (even) | 1/9 = 0.111 A | built |
| 4.17 | practice | −8.571 V | −60/7 V | built |
| 4.18 | practice (VCCS) | (even) | 11.2 V | built |
| 4.19 | ★floating dependent source in the return wire | −26.67 V | −26.67 V | built |

## Part B · Sadiku 5e · §4.4 Source transformation (batch 5)

Verified = `src/verify_b5.py`: every circuit solved as drawn (no transformation).

| Q | Ideas (★ = new here) | Book answer | Verified answer | Status |
|---|---|---|---|---|
| PP 4.6 | practice | 1.78 A | 1.7797 A | built |
| PP 4.7 | practice (dependent V-source transformed) | 7.059 mA | 7.0588 mA | built |
| 4.20 | reduce to one source | (even) | 160/7 V, 40/7 Ω | built |
| 4.21 | design (sample) | multiple | V=20, R1=5, R2=20, I=2 → 24 V, −0.8 A | built |
| 4.22 | practice | (even) | 5/9 A | built |
| 4.23 | practice (power) | 1 A, 8 W | same | built |
| 4.24 | practice (VCCS) | (even) | 2.979 V | built |
| 4.25 | ★all sources transform → one loop | −6.6 V | −6.6 V | built |
| 4.26 | practice | (even) | 7/11 A | built |
| 4.27 | practice | −48 V | −48 V | built |
| 4.28 | practice (VCCS) | (even) | 2 A | built |
| 4.29 | ★only return path | 3 V | 3 V | built |
| 4.30 | practice (CCCS) | (even) | 0.2548 A | built |
| 4.31 | practice (VCVS) | 3.652 V | 84/23 V | built |
| 4.32 | practice (CCCS) | (even) | 1.6 A | built |

## Part B · Sadiku 5e · §4.5–4.6 Thevenin / Norton, part 1 (batch 6a)

Verified = `src/verify_b6a.py`: V_oc, I_sc, R_th = V_oc/I_sc and a test-source R_th (sources off).

| Q | Book answer | Verified answer | Status |
|---|---|---|---|
| PP 4.8 | 6 V, 3 Ω, 1.5 A | same | built |
| PP 4.9 | 5.333 V, 444.4 mΩ | same | built |
| PP 4.10 | 0 V, −7.5 Ω | same | built |
| PP 4.11 | 3 Ω, 4.5 A | same | built |
| PP 4.12 | 1 Ω, 10 A | same | built |
| 4.33 | 40 V, 20 Ω, 1.6 A | same | built |
| 4.34 | design | sample: 6 V, 4 Ω | built |
| 4.35 | −125 mV | −0.125 V | built |
| 4.36 | (even) | 0.5 A | built |
| 4.37 | 10 Ω, 666.7 mA | same | built |
| 4.38 | (even) | 12.8 V | built |
| 4.39 | 20 Ω, −49.2 V | same | built |
| 4.40 | (even) | 60 V, 2.857 kΩ | built |
| 4.41 | 4 Ω, −8 V, −2 A | same | built |
| 4.42 | (even) | 10 V, 10 Ω | built |
| 4.43 | 10 Ω, 0 V | same; i_x = 0 | built |
| 4.44 | (even) | (a) 4 V, 27/7 Ω; (b) 15 V, 45/14 Ω | built |
| 4.45 | 3 Ω, 2 A (Norton form) | 6 V, 3 Ω, I_N 2 A | built |
| 4.46 | design | sample: 3 A, 4 Ω | built |
| 4.47 | 1.1905 V, 476.2 mΩ, 2.5 A | same | built |
| 4.48 | (even) | I_N 3 A, R_N −4 Ω | built |

## Part B · Sadiku 5e · §4.5–4.6 Thevenin / Norton, part 2 (batch 6b)

Verified = `src/verify_b6b.py` (same method as 6a).

| Q | Book answer | Verified answer | Status |
|---|---|---|---|
| 4.49 | 28 Ω, 3.286 A | same | built |
| 4.50 | (even) | I_N −0.4 A, 10 Ω; i = 2.4 A | built |
| 4.51 | (a) 2 Ω, 7 A (b) 1.5 Ω, 12.667 A | same | built |
| 4.52 | (even) | −80 V, 2 kΩ | built |
| 4.53 | 3 Ω, 1 A | same | built |
| 4.54 | (even) | 2 V, −16.67 Ω (= Chakraborty 5.27 with 50 Ω) | built |
| 4.55 | 100 kΩ, −20 mA | same | built |
| 4.56 | (even) | V_o = −0.2857 V | built |
| 4.57 | 10 Ω, 166.67 V, 16.667 A | same | built |
| 4.58 | (even) | R_th → ∞ (current-source output) | built |
| 4.59 | 22.5 Ω, 40 V, 1.7778 A | same | built |
| 4.60 | (even) | 10 V, 3.333 Ω, 3 A | built |
| 4.61 | 1.2 Ω, 9.6 V, 8 A | same | built |
| 4.62 | (even) | 0 V, 31.72 Ω | built |
| 4.63 | −3.333 Ω, 0 A | same | built |
| 4.64 | (even) | 0 V, −1 Ω | built |
| 4.65 | V_o = 24 − 5I_o | same | built |

## Part B · Sadiku 5e · §4.8 Maximum power (batch 7)

Verified = `src/verify_b7.py`: Thevenin by netlist + sweep of the load on the full circuit.

| Q | Book answer | Verified answer | Status |
|---|---|---|---|
| PP 4.13 | 4.222 Ω, 2.901 W | same | built |
| 4.66 | (even) | 1.6 Ω, 0.625 W | built |
| 4.67 | 25 Ω, 7.84 W | same | built |
| 4.68 | (even) | R = 0, 1.6 W (R is on the source side) | built |
| 4.69 | ∞ (theoretically) | R_th = −1363.6 Ω ⇒ P → ∞ | built |
| 4.70 | (even) | 104.75 Ω, 21.5 mW | built |
| 4.71 | 8 kΩ, 1.152 W | same | built |
| 4.72 | (even) | 40 V, 12 Ω; 2 A; 12 Ω; 33.33 W | built |
| 4.73 | 20.77 W | same | built |
| 4.74 | (even) | R1∥R2 + R3∥R4, V_th²/4R_th | built |
| 4.75 | 1 kΩ, 3 mW | same (three R's meet at the output) | built |

**Sadiku ch. 4 complete (PP 4.3–4.13, Probs. 4.8–4.75).**

## Part B · Sadiku 5e · ch. 10 §10.4–10.5 AC superposition + source transformation (batch 8)

Verified = `src/verify_b8.py`: each frequency solved as its own full phasor circuit.

| Q | Book answer | Verified answer | Status |
|---|---|---|---|
| PP 10.4 (§10.3) | 6.089∠5.94° A | same | built |
| PP 10.5 | 5.97∠65.45° A | same (= Chakraborty 5.5(c) circuit; confirms that book error) | built |
| PP 10.6 | 11.577 sin(5t−81.12°) + 3.154 cos(10t−86.24°) | 3.151 for the second term (book rounding) | built |
| PP 10.7 | 9.863∠99.46° A | same | built |
| 10.40 | (even) | 4 + 0.791 cos(4t−71.57°) A (= Chakraborty 5.5(b) corrected) | built |
| 10.41 | 4.243 cos(2t+45°) + 3.578 sin(4t+25.56°) | 26.57° (App. D typo) | built |
| 10.42 | design | sample: I_o = 1.768∠−45° A | built |
| 10.43 | 9.902 cos(2t−129.17°) A | same | built |
| 10.44 | (even) | 21.41 sin(2t−15.52°) + 147.7 cos(6t+26.50°) V | built |
| 10.45 | 791.1 cos(10t+21.47°) + 299.5 sin(4t+176.6°) mA | same | built |
| 10.46 | (even) | 10 + 10.73 cos(3t−26.57°) + 21.47 sin(2t+26.57°) V | built |
| 10.47 | 4 + 0.504 sin(t+19.1°) + 0.3352 cos(3t−76.43°) A | same | built |
| 10.48 | (even) | 0.1 + 0.2175 cos(2000t+134.12°) + 1.178 sin(4000t−172.62°) A | built |
| 10.49 | 4.472 sin(200t+56.56°) A | same | built |
| 10.50 | design | sample: 4.472 cos(2t−63.43°) V | built |
| 10.51 | 109.3∠30° mA (unknown design) | B86 design: 1.768∠−45° A | built |
| 10.52 | (even) | 5.239∠17.35° A | built |
| 10.53 | 3.529 − j5.883 V | same | built |
| 10.54 | (even; = Prob. 10.7) | 124.08∠−153.96° V (= App. D 10.7) | built |

## Part B · Sadiku 5e · ch. 10 §10.6 AC Thevenin / Norton (batch 9)

Verified = `src/verify_b9.py` (phasor V_oc, I_sc, test-source Z_th).

| Q | Book answer | Verified answer | Status |
|---|---|---|---|
| PP 10.8 | 12.4 − j3.2 Ω, 63.24∠−51.57° V | same | built |
| PP 10.9 | 4.473∠−7.64° Ω, 7.35∠72.9° V | same | built |
| PP 10.10 | 3.176 + j0.706 Ω, 8.396∠−32.68° A, 1.9714∠−2.10° A | same | built |
| 10.55 | (a) 22.63∠−63.43° Ω, 50∠−150° V, 2.236∠−86.6° A; (b) 10∠26°, 33.92∠58°, 3.392∠32° | (a) 22.36 (App. D digit swap); (b) same | built |
| 10.56 | (even) | (a) 6 − j4 Ω, 14.42∠−33.69° V, 2∠0° A; (b) 5.423∠−77.47° Ω, 19.40∠−59.04° V, 3.578∠18.43° A | built |
| 10.57 | design | sample: j10 V, 3 + j2 Ω | built |
| 10.58 | (even) | 55.90∠71.57° V, 10 + j5 Ω | built |
| 10.59 | −6 + j38 Ω | same | built |
| 10.60 | (even) | (a) 9.615∠33.69° V, 1.333 Ω; (b) 9.615∠56.31° V, 2.667 − j4 Ω | built |
| 10.61 | −24 + j12 V, −8 + j6 Ω | same | built |
| 10.62 | (even) | v_o = 2.299 cos(t − 163.30°) V (= Chakraborty 5.22 circuit, sign-flipped source; confirms A22 correction) | built |
| 10.63 | 1 kΩ, 5.657 cos(200t + 75°) A | same | built |
| 10.64 | (even) | 20 + j40 Ω, 3∠60° A | built |
| 10.65 | design | sample: i_o = 4.472∠−63.43° A | built |
| 10.66 | (even) | 29.79∠−3.62° V, 44.43∠−133.18° A, −0.427 + j0.517 Ω | built |
| 10.67 | 4.945∠−69.76° V, 0.4378∠−75.24° A, 11.243 + j1.079 Ω | 4.944∠−69.66°, 0.4377∠−75.14° (0.1° off), Z same | built |
| 10.68 | (even) | 11.52 sin(10t − 50.19°) V, 1.230 − j1.475 Ω | built |

## Part B · Sadiku 5e · ch. 11 §11.2–11.3 AC max average power (batch 10)

Verified = `src/verify_b10.py` (peak phasors, P = ½Re(VI*); every maximum also found by sweeping the load).

| Q | Book answer | Verified answer | Status |
|---|---|---|---|
| PP 11.4 (§11.2) | −60 W, −40 W, 100 W, 0 | same | built |
| PP 11.5 | 3.415 − j0.7317 Ω, 51.47 W | 51.43 W (book rounding) | built |
| 11.12 | (even) | 0.823 + j0.864 Ω, 4.230 kW | built |
| 11.13 | 28.36 W | same | built |
| 11.14 | design | sample: 10 Ω, 62.5 W | built |
| 11.15 | 90 W | 0.5 − j0.5 Ω, 90 W | built |
| 11.16 | (even) | 1.670 − j3.648 Ω, 10.57 W | built |
| 11.17 | 20 Ω, 31.25 W | same | built |
| 11.18 | (even) | 21.23 − j20.15 Ω | built |
| 11.19 | 258.5 W | R = 2.576 Ω, 258.5 W | built |
| 11.20 | (even) | 6.793 Ω, 21.51 W | built |
| 11.21 | 19.58 Ω | same | built |

## Status

**Confirmed scope complete (2026-10-18):** Part A Chakraborty 5.1–5.44 (44) + Part B Sadiku ch. 4 (PP 4.3–4.13,
Probs. 4.8–4.75), ch. 10 (PP 10.4–10.10, Probs. 10.40–10.68 incl. 10.54's reference Prob. 10.7), ch. 11 (PP 11.4–11.5,
Probs. 11.12–11.21). 127 numbered entries in Part B (B1–B127).

Possible additions if the professor confirms ~300: Chakraborty 5.45–5.56 (reciprocity / Millman), Chakraborty
exercises + MCQs, rest of Sadiku ch. 4 (4.76–4.97: PSpice + applications).
