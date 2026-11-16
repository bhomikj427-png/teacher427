# Statistics & Probability — Study Pack (ETE)

<div class="sub">MAS2001 · B.Tech Sem 3 · July–Nov 2026 · built on the official ETE blueprint, the 2026 MTE paper and its marking scheme, Assignments 1, 2, 4, 5, and the professor's LMS slides · facts from Gupta & Kapoor and the subject knowledge base · every number recomputed by script</div>

## Priority order: if time is short, study in this order

The ranking is driven by **marks**. The ETE blueprint (official) fixes the marks per syllabus row: probability and RVs 10, distributions and CLT 20, **estimation 22**, hypotheses 10, **t/F/χ²/ANOVA 18 including the only 8-mark Part D**. Within a row, files rank by how many assignment, MTE and slide questions hit them. The blueprint is hard evidence; how the marks split between files inside a row is an estimate.

| Rank | Study | Why it ranks here | Do first | Rough time |
|---|---|---|---|---|
| **1** | **09 MoM and MLE** | Row 3 (22 marks): two 6-mark and one 8-mark slot; the professor's slides work four MLE examples | 09 §3–7, mock B3, C2 | 70 min |
| **2** | **11 Confidence interval for mean** | Named in row 3; Assignment 4 has five CI questions, Assignment 5 two more | 11 §2, 5, 6 | 45 min |
| **3** | **16 ANOVA** | Row 5 holds the paper's only Part D (8 marks); Assignment 5's Part D includes an ANOVA | 16 §2–4, mock D1 | 45 min |
| **4** | **13 t-tests** | Row 5; six t-test questions in Assignment 5, one of them Part D | 13 §2, 4, 5 | 60 min |
| **5** | **06 Normal** | Row 2 (20 marks, one Part C); MTE C1(a) was 4 marks; five Assignment 2 numericals | 06 §2–5 | 50 min |
| **6** | **07 SE and CLT** | Named in row 2; four worked slide examples; a Part C candidate | 07 §2–5, mock C1 | 40 min |
| **7** | **15 χ² independence** | Row 5; four numericals in Assignment 5 | 15 §3–4 | 40 min |
| **8** | **08 Estimator properties** | Row 3; MTE A3 (2) and C1(b) (3) | 08 §2, exam form | 35 min |
| **9** | **12 Hypotheses and errors** | Row 4 (10 marks); α/β questions A4 C1–C3 fit its 6-mark slot | 12 §3, 5, 6 | 50 min |
| **10** | **04 Binomial and Poisson** | Row 2; MTE A2, A4, B3 (8 marks) | 04 §1, 3, 4 | 40 min |
| **11** | **14 F-test** | Row 5; four Assignment 5 numericals; quick to learn | 14 §2, 4 | 30 min |
| **12** | **05 Uniform and exponential** | Row 2; MTE B4 (4 marks); eight short Assignment 2 items | 05 §2, 5 | 35 min |
| **13** | **03 Expectation, variance, Chebyshev** | Row 1 (10 marks); MTE B1, B2 (7 marks) | 03 §5–6 | 45 min |
| **14** | **10 Bayesian** | Blueprint says "introduction of"; one slide example | 10 §3 | 25 min |
| **15** | **02a Discrete RVs · 02b Continuous RVs** | Row 1; needed by 03, 08, 09 | 02a §3, 5, 7–8; 02b §1–3, 5 | 60 min |
| **16** | **01 Probability basics** | Row 1 definitions; Bayes' theorem feeds 10 | 01 §6–7, 11–12 | 40 min |
| **last** | **17 Mock paper** | All rows in blueprint proportion | closed book | 3 h |

Two rules for using the ranking:

- **Short on time:** go down the list doing only the "Do first" column, then the matching mock items.
- **Stuck in 08–09:** they need E(X), Var(X) and PDFs. Go back to 02b §1–3 and 03 §1–4 first.

## The path through the pack

The order is the syllabus order, which is also the order of the assignments (1, 2, …, 5).

**Unit 1 — probability and random variables** (blueprint row 1)

[[map:01 Probability basics > 02a Discrete RVs > 02b Continuous RVs > 03 Expectation, variance, Chebyshev|here=1]]

**Unit 2 — distributions and sampling** (row 2)

[[map:04 Binomial, Poisson > 05 Uniform, exponential > 06 Normal > 07 SE and CLT]]

**Unit 3 — estimation** (row 3)

[[map:08 Estimator properties > 09 MoM and MLE > 10 Bayesian > 11 CI for the mean]]

**Unit 4 — testing** (rows 4 and 5)

[[map:12 Hypotheses, errors > 13 t-tests > 14 F-test > 15 χ² > 16 ANOVA > 17 Mock]]

02a needs 01's probability rules; 02b needs 02a's CDF. 03 needs 02a's PMF and 02b's PDF. 04–06 use 03's E and Var. 07 needs 03 (variance of a sum) and 06 (normal table). 08–09 need 03, 07 and the distributions of 04–05. 10 uses 01's Bayes' theorem. 11 needs 06–08. 12 needs 04–05 for α and β. 13 builds on 11's t; 14 checks 13's equal-variance assumption; 16 uses 14's F.

| File | Blueprint item | What it teaches | Real Qs |
|---|---|---|---|
| 01 | row 1 · basic terminology | sample space, events, count and divide, axioms, complement, addition, conditional, multiplication, independence, total probability, Bayes | 4 |
| 02a | row 1 · discrete RVs, PMF, CDF | random variable, discrete vs continuous, PMF by counting, PMF rules, finding k, combinations, CDF staircase, reading F, conditionals | 9 |
| 02b | row 1 · continuous RVs, PDF, CDF | probability as area, checking a PDF, smooth CDF, median, tail areas, conditionals | 3 |
| 03 | row 1 · expectation, variance, Chebyshev | E, Var, rules for sums, Chebyshev both forms, bound vs exact | 13 |
| 04 | row 2 · binomial, Poisson | formulas, mean/variance, finding λ, Poisson limit | 11 + 1 textbook |
| 05 | row 2 · uniform, exponential | probability as length, absolute-value intervals, waiting times, memoryless | 13 |
| 06 | row 2 · normal | standardising, the φ table, counts, normal + binomial, inverse problems | 9 |
| 07 | row 2 · population, sample, SE, CLT | parameter vs statistic, SE = σ/√n, CLT and its three cases | 6 |
| 08 | row 3 · good estimators | unbiased, n − 1, consistent, efficient, sufficient | 2 + textbook |
| 09 | row 3 · MoM, MLE | one- and two-parameter MoM, the five MLE steps, four slide MLEs, both methods | 4 + 3 textbook |
| 10 | row 3 · Bayesian (intro) | prior, posterior, the slide's defectives example, posterior mean | 1 |
| 11 | row 3 · CI for mean | meaning, z-interval, levels, function of μ, t-interval, raw data | 7 |
| 12 | row 4 | H₀/H₁, tails, Type I/II, α, β, power, critical region, test steps | 15 |
| 13 | row 5 · t-test | one-sample (summary, raw), two levels, pooled two-sample, paired | 9 |
| 14 | row 5 · F-test | F ratio, sums of squares, two-tailed, raw data, before the t | 6 |
| 15 | row 5 · χ² | expected frequency, df, 2 × 2, shortcut, building tables, 3 × 3 | 8 |
| 16 | row 5 · ANOVA | idea, assumptions, sums of squares, ANOVA table, equal and unequal groups | 4 |
| 17 | all rows | an 80-mark paper on the blueprint, with a marking key | 19 practice |

## Where the questions come from

A question that opens a step is quoted from the professor's material where one exists, and tagged:

| Tag | Source | Questions used |
|---|---|---|
| <span class="tag">MTE A1</span> … | Mid-term exam, Jul–Nov 2026 (30 marks) and its marking scheme | all 10 parts |
| <span class="tag">A1</span> <span class="tag">A2</span> <span class="tag">A4</span> <span class="tag">A5</span> | Assignments 1, 2, 4, 5 (no Assignment 3 was available) | ~100 |
| <span class="tag">Slides</span> | LMS slides: "Sampling & Limit Theorems", "MLE and Bayesian Estimation", "ppt 8 Hypothesis Testing" | 13 |
| <span class="tag">G&K</span> | Gupta & Kapoor, *Fundamentals of Mathematical Statistics* (the reference the slides cite) | 6 |
| Predict | no real question exists for that idea; labelled "Predict" | — |

**P1 (professor's papers, assignments, slides): about 120 questions. P2 (textbook): 6.** The mock paper's 19 items are practice questions written in the professor's forms and say which form each copies.

## How each file runs

| Part | What happens |
|---|---|
| **Map** | the file's steps, in order |
| **Questions** | the real questions the file answers |
| **Build** | each step: question → you guess → the answer teaches the idea → a Check |
| **Exam form** | what to write in the exam: statements, procedures, formulas |
| **Traps** | the mistakes that cost marks |
| **Self-test**, **Answers** | answers to every Check and Self-test are on the last pages of the file |

:::key The one rule that makes this work
When you reach a **Guess first** box, write a guess on paper **before** reading on: one line, however wrong. A wrong guess that gets corrected sticks better than a right answer you only read.
:::

## Units and symbols used everywhere

- **X** = a random variable; **x** = a value it takes. **P(A | B)** = probability of A given B.
- **μ, σ, σ^{2}** = population mean, SD, variance (parameters). **x̄, s, s^{2}** = sample mean, SD, variance (statistics).
- **s^{2} = Σ(x − x̄)^{2}/(n − 1)** throughout. Where a question's "SD" could be the n-divisor version, the file says so.
- **SE** = standard error = σ/√n (or s/√n).
- **φ(z)** = area under the standard normal curve **from 0 to z** (the table the professor gives in questions).
- **H₀, H₁** = null and alternative hypotheses; **α, β** = probabilities of Type I and Type II errors; **df** = degrees of freedom.
- t_{α/2, ν}, F_{α}(ν₁, ν₂), χ^{2}_{α} = table values with α in the upper tail.

## Where the professor's material disagrees with the pack

Every answer in the assignments and the MTE key was recomputed. These differ; the pack uses the corrected value and flags it where it occurs.

| Where | Material says | Pack says | Why |
|---|---|---|---|
| **A5 C6** (16 §3) | table value 19.41 | **F₀.₀₅(2, 12) = 3.89** | 19.41 is F(12, 2): df reversed. **The decision flips**: F = 9.17 rejects H₀ |
| A5 D1 (14 §4) | table value 5.19 | F₀.₀₅(4, 4) = 6.39 | 5.19 is F(4, 5); same decision |
| A5 D2 (11 §6) | CI (24.945, 25.075) | (24.930, 25.080) | the key's half-width does not match the data's s = 0.1605 |
| A5 A4 (13 §5) | options 1.55/2.10/3.00/3.87 | t = 3.10 | no option matches; nearest is 3.00 |
| A5 A10 (16 §2) | options 4/5/6/8 | F = 4.44 | no option matches; nearest is 4.00 |
| A2 B5 (05 §6) | 0.5679 | 0.6225 | recomputed two ways |
| A2 C2 (06 §6) | μ = 37.5 | μ = 37.18, re-exam mark 30.40 | the key's own 30.43 implies μ ≈ 37.2 |
| A1 LA 2 (02a §5, §8) | row printed as k, 2k, 2k, 3k, 3k, k², 2k², 7k² + k; key (ii) 81/100, 91/100, 4/5 | Gupta & Kapoor's row 0, k, 2k, 2k, 3k, … (differs at x = 0, 1, 3); P(X > 6) = 17/100, P(X ≥ 6) = 19/100, P(0 < X < 5) = 4/5 | the key answers G&K's question: 81/100 is P(X < 6), and 91/100 is 19/100 with its digits swapped. The printed row gives k ≈ 0.0782 |
| A1 LA 3 (03 §4) | 0.808 without replacement | 0.8 in both cases | expectation of a sum needs no independence |
| A1 App 3 (03 §2) | SD ≈ 0.98 | 0.973 | the key rounded the variance first |
| MTE B1 (03 §6) | bound 16/3 | 16/3 (correct), plus: a bound above 1 says nothing; exact value 5/6 | an addition, not a correction |
| Slides CLT p.11 (07 §4) | z = −0.4 | z = −0.94 | typo; the slide's area uses 0.94 |
| Slides MLE Ex. 14 (09 §6) | L(x₁, …, x₁₀; θ) | n = 6 | label only |
| ppt 8 slide 7 (12 §2) | "H₀: μ > −0.545" | H₁: μ > −0.545 | the alternative was labelled H₀ |

## How this pack was checked

- **Facts:** from the subject's knowledge base (researched to both stages from Walpole, Montgomery & Runger and Ross; every load-bearing claim checked against sources) and from Gupta & Kapoor, the reference the slides cite. Section numbers are quoted where a formula is used.
- **Numbers:** `src/verify.py` recomputes every number in the pack, 558 checks, by an independent route (scipy distributions, numerical integration and optimisation, library t, F, χ² and ANOVA routines, simulation). It passes with no failures. Each professor's key is compared too; the 13 mismatches are the slips in the table above.
- **Pages:** every page was viewed after the final build.
