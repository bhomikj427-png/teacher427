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

## Still to build

| Batch | Questions |
|---|---|
| 2 | Chakraborty 5.15–5.34 (Thevenin / Norton) |
| 3 | Chakraborty 5.35–5.44 (maximum power transfer) |
| 4+ | Sadiku ch. 4: practice problems 4.3–4.13; end-of-chapter 4.8–4.75 by section |
| later | Sadiku ch. 10 §10.4–10.6 (10.40–10.68 + PP 10.4–10.10); ch. 11 §11.3 (11.12–11.21 + PP 11.4–11.5) |

Draft Sadiku pages from the demo (PP 4.3, 4.8, 4.9) are parked in `src/later/`.
