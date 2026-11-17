# 17 — Mock ETE paper (80 marks)

<div class="sub">Built to the official MAS2001 blueprint, July–Nov 2026 · 10 × 2 + 6 × 6 + 2 × 8 + 1 × 8 = 80 marks · every row in its blueprint proportion · all questions are practice items in the professor's forms (tagged with the form they copy) · needs 01–16</div>

## Map

[[map:Part A: 10 × 2 > Part B: 6 × 6 > Part C: 2 × 8 > Part D: 1 × 8 > Key and marking|here=1]]

[[fig:mock_blueprint|Marks per blueprint row. Estimation (row 3) is the heaviest.|w=66]]

**Conditions.** 3 hours, closed book, calculator, statistical tables. Write the full working: the key gives marks for steps.

| Blueprint row | Part A | Part B | Part C | Part D | Marks |
|---|---|---|---|---|---|
| 1 Probability, RVs, Chebyshev | A1, A2 | B1 | — | — | 10 |
| 2 Distributions, SE, CLT | A3, A4, A5 | B2 | C1 | — | 20 |
| 3 Estimation | A6 | B3, B4 | C2 | — | 22 |
| 4 Hypotheses, errors | A7, A8 | B5 | — | — | 10 |
| 5 t, F, χ², ANOVA | A9, A10 | B6 | — | D1 | 18 |

---

## Part A — 2 marks each

**A1** <span class="tag">form: A1 App 1</span> X takes 0, 1, 2 with probabilities 0.2, 0.5, 0.3. Find E(X) and Var(X).

**A2** <span class="tag">form: A1 App 4</span> X has mean 40 and SD 4. Use Chebyshev's inequality to find a lower bound for P(32 < X < 48).

**A3** <span class="tag">form: MTE A4</span> X is Poisson with P(X = 1) = P(X = 2). Find the mean of X and P(X = 0).

**A4** <span class="tag">form: A2 B7</span> A component's life is exponential with mean 4 years. Find P(it lasts more than 6 years | it has lasted 2 years).

**A5** <span class="tag">form: slides p.4</span> σ = 15. Find the standard error of the mean for n = 25, and the n that gives SE = 1.5.

**A6** <span class="tag">form: MTE C1(b)</span> X₁, X₂, X₃ is a random sample with mean μ and variance σ^{2}. Is T = (X₁ + 2X₂ + 3X₃)/6 unbiased for μ? Find Var(T).

**A7** <span class="tag">form: slides p.10</span> A maker claims its new battery lasts **more than** 500 cycles on average. Write H₀ and H₁ and say whether the test is one- or two-tailed.

**A8** <span class="tag">form: A5 A1</span> Define Type I error, Type II error and the power of a test.

**A9** <span class="tag">form: A5 A4</span> A paired t-test on 10 subjects has mean difference 2 and SD of the differences 3. Find t and its df.

**A10** <span class="tag">form: A5 A10</span> One-way ANOVA: k = 4 groups, N = 20, SSB = 36, SSW = 64. Find the df and F.

## Part B — 6 marks each

**B1** <span class="tag">form: MTE B2, A1 SA 3</span> X has pdf f(x) = kx(2 − x), 0 ≤ x ≤ 2. Find k, E(X), Var(X) and P(X < 0.5).

**B2** <span class="tag">form: A2 B4</span> The life of 2000 bulbs is normal with mean 1200 h and SD 150 h. How many bulbs are expected to last (i) more than 1500 h (ii) between 1050 and 1350 h? (φ(1) = 0.3413, φ(2) = 0.4772.)

**B3** <span class="tag">form: slides Ex. 14</span> A sample 0.2, 0.5, 0.7, 0.9 comes from f(x; θ) = θx^{θ−1}, 0 < x < 1, θ > 0. Find the maximum likelihood estimator of θ (show the second-derivative check) and its value.

**B4** <span class="tag">form: A4 B4</span> 16 measurements from a normal population give x̄ = 48.5 and s = 6. Construct a 95% confidence interval for μ (t₀.₀₅,₁₅ = 2.131) and interpret it.

**B5** <span class="tag">form: A4 C2</span> To test H₀: p = 0.5 against H₁: p = 0.7, a coin is tossed 6 times and H₀ is rejected if 5 or more heads appear. Find α, β and the power.

**B6** <span class="tag">form: A5 C3</span> 200 workers are classified by training (trained / not) and performance (good / poor): trained-good 60, trained-poor 40, untrained-good 40, untrained-poor 60. Test at 5% whether training and performance are independent. (χ^{2}₀.₀₅,₁ = 3.841.)

## Part C — 8 marks each

**C1** <span class="tag">form: slides p.8–15</span> (a) State the Central Limit Theorem. (2) (b) Waiting times at a counter are skewed with μ = 60 s and σ = 12 s. For a random sample of 36 customers find P(X̄ > 63) and P(57 < X̄ < 62). (6) (φ(1) = 0.3413, φ(1.5) = 0.4332.)

**C2** <span class="tag">form: slides Ex. 12, MTE A3</span> A sample 3, 5, 4, 6, 2 is drawn from a Poisson(λ) population. (a) Derive the MLE of λ and find its value. (4) (b) Show that it is unbiased and consistent. (2) (c) Find the MLE of P(X = 0). (2)

<div style="break-before: page"></div>

## Part D — 8 marks

**D1** <span class="tag">form: A5 C6, D4</span> Output per hour of three machines:

| Machine | Hour 1 | Hour 2 | Hour 3 | Hour 4 |
|---|---|---|---|---|
| A | 8 | 10 | 12 | 10 |
| B | 14 | 12 | 16 | 14 |
| C | 9 | 11 | 10 | 10 |

Test at the 5% level whether the mean outputs differ. Present the ANOVA table. (F₀.₀₅(2, 9) = 4.26.)

<!--ANSWERS-->
## Key and marking

**Where each item is taught** (file § step): go there if an answer below surprises you.

| Item | Taught in | Item | Taught in |
|---|---|---|---|
| A1 | 03a §2, §4–5 | B1 | 02b §2, 03a §7 |
| A2 | 03b §6 | B2 | 06 §6, §8 |
| A3 | 04b §3 | B3 | 09b §8–9 |
| A4 | 05 §9 | B4 | 11 §7 |
| A5 | 07 §5–6 | B5 | 12b §5 |
| A6 | 08 §3–4, 03b §1–3 | B6 | 15 §5–6 |
| A7 | 12a §3–4 | C1 | 07 §7, §9–10 |
| A8 | 12a §5, §7 | C2 | 09b §4, §10; 08 §3, §6 |
| A9 | 13 §7 | D1 | 16 §4–7 |
| A10 | 16 §5–6 | | |

**A1.** E = 0.5 + 0.6 = **1.1**; E(X^{2}) = 0.5 + 1.2 = 1.7; Var = 1.7 − 1.21 = **0.49**. (1 + 1)

**A2.** 32–48 = μ ± 2σ: P ≥ 1 − 1/4 = **0.75**. (1 + 1)

**A3.** e^{−λ}λ = e^{−λ}λ^{2}/2 ⇒ **λ = 2**; P(0) = e^{−2} = **0.1353**. (1 + 1)

**A4.** Memoryless: P(X > 4) = e^{−4/4} = **e^{−1} = 0.3679**. (1 + 1)

**A5.** 15/5 = **3**; 15/√n = 1.5 ⇒ **n = 100**. (1 + 1)

**A6.** E(T) = (1 + 2 + 3)μ/6 = μ: **unbiased**. Var(T) = (1 + 4 + 9)σ^{2}/36 = **7σ^{2}/18**. (1 + 1)

**A7.** H₀: μ ≤ 500 (or μ = 500); H₁: μ > 500; **one-tailed (right)**. (1 + 1)

**A8.** Type I: rejecting a true H₀ (probability α). Type II: accepting a false H₀ (β). Power = 1 − β = P(reject H₀ | H₁ true). (2)

**A9.** t = 2/(3/√10) = **2.108**, df = **9**. (1 + 1)

**A10.** df = **3, 16**; MSB = 12, MSW = 4, **F = 3**. (1 + 1)

**B1.** ∫₀^{2} x(2 − x) dx = 4 − 8/3 = 4/3 ⇒ **k = 3/4** (2). By symmetry about 1, **E(X) = 1** (1). E(X^{2}) = (3/4)∫₀^{2}(2x^{3} − x^{4})dx = (3/4)(8 − 32/5) = 1.2 ⇒ **Var = 0.2** (2). P(X < 0.5) = (3/4)[x^{2} − x^{3}/3]₀^{0.5} = (3/4)(0.25 − 0.04167) = **0.1563** (1).

**B2.** (i) z = 2: P = 0.5 − 0.4772 = 0.0228; 2000 × 0.0228 = **46 bulbs** (3). (ii) z = ±1: P = 0.6826; 2000 × 0.6826 = **1365 bulbs** (3).

**B3.** L = θ^{n}Πxᵢ^{θ−1}; ℓ = n ln θ + (θ − 1)Σ ln xᵢ (2). dℓ/dθ = n/θ + Σ ln xᵢ = 0 ⇒ **θ̂ = −n/Σ ln xᵢ** (2). d^{2}ℓ/dθ^{2} = −n/θ^{2} < 0 ✓ (1). Σ ln xᵢ = −1.6094 − 0.6931 − 0.3567 − 0.1054 = −2.7646 ⇒ **θ̂ = 4/2.7646 = 1.447** (1).

**B4.** SE = 6/4 = 1.5; margin = 2.131 × 1.5 = 3.197 (3). CI = **(45.30, 51.70)** (2). Intervals built this way contain μ in 95% of samples (1).

**B5.** α = P(X ≥ 5 | 0.5) = (6 + 1)/64 = **7/64 = 0.1094** (2). β = P(X ≤ 4 | 0.7) = 1 − [6(0.7)^{5}(0.3) + (0.7)^{6}] = 1 − (0.3025 + 0.1176) = **0.5798** (3). Power = **0.4202** (1).

**B6.** H₀: independent (1). χ^{2} = 200(60 × 60 − 40 × 40)^{2}/(100 × 100 × 100 × 100) = 200 × 2000^{2}/10^{8} = **8** (3). 8 > 3.841 ⇒ **reject H₀**: training and performance are associated (2).

**C1.** (a) For i.i.d. X₁, …, Xₙ with mean μ and finite variance σ^{2}, X̄ is approximately N(μ, σ^{2}/n) for large n, whatever the population's shape (2). (b) SE = 12/6 = 2 (1). P(X̄ > 63): z = 1.5, P = 0.5 − 0.4332 = **0.0668** (2). P(57 < X̄ < 62): z = −1.5 and 1, P = 0.4332 + 0.3413 = **0.7745** (3).

**C2.** (a) L = e^{−5λ}λ^{Σxᵢ}/Πxᵢ!; ℓ = −5λ + Σxᵢ ln λ − ln Πxᵢ!; dℓ/dλ = −5 + Σxᵢ/λ = 0 ⇒ λ̂ = x̄; second derivative −Σxᵢ/λ^{2} < 0 (3). Σxᵢ = 20 ⇒ **λ̂ = 4** (1). (b) E(X̄) = λ (unbiased); Var(X̄) = λ/n → 0 (consistent) (2). (c) Invariance: **e^{−4} = 0.0183** (2).

**D1.** H₀: μ_{A} = μ_{B} = μ_{C} (1). T = 40, 56, 40; G = 136; N = 12; CF = 1541.33; Σx^{2} = 408 + 792 + 402 = 1602 (2).
SST = **60.67**; SSB = (1600 + 3136 + 1600)/4 − 1541.33 = **42.67**; SSW = **18.00** (2).

| Source | SS | df | MS | F |
|---|---|---|---|---|
| Between | 42.67 | 2 | 21.33 | **10.67** |
| Within | 18.00 | 9 | 2.00 | |
| Total | 60.67 | 11 | | |

(2) 10.67 > 4.26 ⇒ **reject H₀**: the machines' mean outputs differ (Machine B highest) (1).
<!--/ANSWERS-->
