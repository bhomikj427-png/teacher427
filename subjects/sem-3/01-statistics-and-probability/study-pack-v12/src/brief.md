# MAS2001 Statistics & Probability — subject brief (spec v1.3 §7.1)

> Built in sprint S0 (2026-11-16). Each build sprint reads **only its files' sections** (§2 question
> bank rows + §4 file plan) instead of re-reading decks or assignments. Numbers: every printed answer
> below is already recomputed in `verify.py` (423 checks, 0 failures, 11 key differences on
> 2026-11-16); table values are in `../../knowledge-base/04-hypothesis-testing.md` → *Table values*.
>
> **Source tags** (use exactly these in the files): `MTE A1`… (MTE 2026 paper) · `A1 MCQ 7`, `A1 SA 2`,
> `A1 LA 3`, `A1 App 4` (Assignment 1) · `A2 MCQ 4`, `A2 B3`, `A2 C2`, `A2 D1` (Assignment 2) ·
> `A4 MCQ 8`, `A4 B1`, `A4 C2` (Assignment 4) · `A5 A4`, `A5 B6`, `A5 C6`, `A5 D4` (Assignment 5) ·
> `SE/CLT slides p.N`, `MLE slides p.N` / `Ex. 11–15`, `HT slide N` (decks, numbers as in §1) ·
> `G&K` (Gupta & Kapoor, textbook, P2: second priority).
>
> **Truth:** the textbook is Gupta & Kapoor (`../../books/`); the KB (`stage-2✓`) holds the facts.
> Slides and keys set scope only.

---

## 1. Slides transcribed

### 1.1 `slides-LMS-standard-error-and-CLT.pdf` (19 pp.; PDF page numbers — **v1.2's file 07 tags are off by 1–3 pages; re-tag in S5**)

| p. | Content |
|---|---|
| 1 | Title: Sampling concepts & limit theorems |
| 2 | Population (N): whole group; parameters μ, σ; often too large to measure; e.g. all 500,000 bulbs a month. Sample (n): random, representative subset; statistics x̄, s; e.g. 100 bulbs tested |
| 3 | (image) Population of 10 balls a–j (4 black) → three simple random samples of 4, without replacement |
| 4 | SE = variability of a statistic (usually x̄) across hypothetical repeated samples. **SE = σ/√n**. Larger n → smaller SE |
| 5 | Example: σ = 100 h; n = 25 → SE = 20 h; n = 100 → SE = 10 h. "Quadrupling n halves SE" |
| 6 | Section title: CLT |
| 7 | CLT: large samples → x̄ approximately normal whatever the population shape. Rules: centre μ_x̄ = μ; spread σ_x̄ = σ/√n; shape normal, "n ≥ 30 safely" |
| 8 | Note: (1) any population, **n > 30** → x̄ ≈ N(μ, σ/√n); (2) n ≤ 30 and normal population → x̄ exactly normal; (3) n ≤ 30, non-normal population → CLT cannot be applied |
| 9 | (image) IQ: (a) normal density, mean 100; (b) histogram of a small sample; (c) histogram of a large sample |
| 10 | (image) Grid: populations normal / uniform / skewed / bimodal ("Random"); rows n = 10 and n = 30 sampling distributions of x̄ → bell shapes at n = 30 |
| 11–12 | Example ATM: right-skewed wait, μ = 4 min, σ = 2 min, n = 36. P(x̄ > 4.5)? SE = 0.333; z = 1.50; upper tail 6.68% |
| 13–14 | Example 1 impurity: μ = 4.0 g, σ = 1.5 g, n = 50, P(3.5 < x̄ < 3.8). Slide: P(−2.36 < Z < −0.4) = 0.4909 − 0.3264 = 0.1644 |
| 15–16 | Example 2 LED: skewed, μ = 50,000 h, σ = 8,000 h, n = 64, P(x̄ < 48,000) = P(Z < −2) = 0.5 − 0.4772 = 0.0228 |
| 17–18 | Example 3 machine: normal population, μ = 7 y, σ = 1 y, n = 9, P(6.4 < x̄ < 7.2) = P(−1.8 < Z < 0.6) = 0.4641 + 0.2257 = 0.6898 |
| 19 | References: Devore (9e); Gupta & Kapoor (10e) |

**Slips:** p.14 prints z = −0.4 for 3.8 g; correct z = (3.8 − 4)/(1.5/√50) = −0.94 (the slide's area 0.3264 is the z = 0.94 area, so its answer stands: 0.1645, slide 0.1644 by rounding). p.7 says n ≥ 30, p.8 says n > 30: one rule ("n ≥ 30") in the pack, with the note.

### 1.2 `slides-LMS-MLE-and-Bayesian.pdf` (16 pp.; equations are images, viewed)

| p. | Content |
|---|---|
| 1 | Title ("Likelyhood" sic) |
| 2 | MLE of θ = value maximising the likelihood. Step 1: write f(x; θ). Step 2: L(θ) = Π f(xᵢ; θ). Step 3: ℓ(θ) = log L(θ). Step 4: dℓ/dθ = 0, solve for θ̂. Step 5: d²ℓ/dθ² < 0 |
| 3 | Properties of MLE: consistent, most efficient, sufficient. **Ex. 11**: normal population, MLE of (a) μ with σ² known, (b) σ² with μ known |
| 4 | Ex. 11 solution: L = (2π)^(−n/2)(σ²)^(−n/2) exp[−½ Σ((xᵢ−μ)/σ)²]; ln L = −(n/2)ln 2π − (n/2)ln σ² − ½Σ((xᵢ−μ)/σ)²; ∂/∂μ = Σ(xᵢ−μ)/σ²; ∂/∂σ² = −n/(2σ²) + Σ(xᵢ−μ)²/(2σ⁴); → Σxᵢ − nμ = 0 and nσ² = Σ(xᵢ−μ)²; μ̂ = x̄ |
| 5–6 | **Ex. 12** Poisson f(x|μ) = e^(−μ)μˣ/x!, sample x₁…xₙ. L = e^(−nμ) μ^(Σxᵢ) / Πxᵢ!; ln L = −nμ + Σxᵢ ln μ − ln Πxᵢ!; derivative −n + Σxᵢ/μ = 0 → μ̂ = x̄ |
| 7–8 | **Ex. 13** 10 rats, survival months 14, 17, 27, 18, 12, 8, 22, 13, 19, 12; exponential f(x, β) = (1/β)e^(−x/β), x > 0. ln L = −10 ln β − (1/β)Σxᵢ; −10/β + Σxᵢ/β² = 0 → β̂ = x̄ = 16.2; second derivative negative |
| 9–10 | **Ex. 14** sample 12, 11.2, 13.5, 12.3, 13.8, 11.9 from f(x; θ) = θ/x^(θ+1), x > 1, θ > 0. L = θⁿ/(Πxᵢ)^(θ+1); ln L = n ln θ − (θ+1)Σ ln xᵢ; n/θ − Σ ln xᵢ = 0 → θ̂ = n/Σ ln xᵢ = 6/15.11 = 0.3970; second derivative −n/θ² < 0 |
| 11 | Bayesian: parameters treated as random variables (vs classical/frequentist). Subjective probability: rain tomorrow, stock up, merger — differs between people |
| 12 | Conditional perspective: inference from the observed data; prior distribution = subjective distribution of the parameter, the experimenter's prior belief; after data, knowledge = data + prior. Applications list |
| 13 | Posterior π(θ|x) = f(x|θ)π(θ)/g(x); marginal g(x) = Σ_θ f(x|θ)π(θ) (discrete θ) or ∫ f(x|θ)π(θ)dθ (continuous) |
| 14–15 | **Ex. 15** prior p: 0.1 → 0.6, 0.2 → 0.4; x = defectives in a sample of 2; posterior of p. X ~ b(x; 2, p); g(x) = C(2,x)[(0.1)ˣ(0.9)^(2−x)(0.6) + (0.2)ˣ(0.8)^(2−x)(0.4)]; g(0), g(1), g(2) = 0.742, 0.236, 0.022; π(0.1|0) = 0.6550, π(0.2|0) = 0.3450; π(0.1|1) = 0.4576, π(0.2|1) = 0.5424; π(0.1|2) = 0.2727, π(0.2|2) = 0.7273 |
| 16 | References: Meyer (2e); Miller, Freund & Johnson (8e) |

**Slips:** Ex. 11 asks two separate cases but the slide solves them jointly and only writes μ̂ = x̄ (σ̂² = Σ(xᵢ − μ)²/n, μ known, follows from its own line). Ex. 13 calls the parameter β (the mean), not the rate λ: say so in the pack. Ex. 14 writes L(x₁, …, x₁₀; θ) for a sample of 6.

### 1.3 `slides-08-hypothesis-testing.pptx` (26 slides; images viewed)

| Slide | Content |
|---|---|
| 1 | Title |
| 2 | Hypothesis: a testable assumption about data modelled as values of random variables (examples are images) |
| 3 | Test of significance: formal procedure comparing data with a hypothesis |
| 4 | IQ example: population mean 100; values 60, 85, 100, 115, 130 on a curve |
| 5 | Hypothesis testing: checks whether results are meaningful; two parts, null and alternate |
| 6 | Null H₀: accepted fact / status quo; about a population parameter, never a statistic; contains =, ≤ or ≥; may or may not be rejected |
| 7 | Alternate H₁: opposite of H₀; what the researcher tries to prove; contains ≠, < or > |
| 8 | Section title: examples of H₀ and H₁ |
| 9 | Example: 82% graduate in 4 years → H₀: p = 0.82, H₁: p ≠ 0.82 |
| 10 | Example: batteries average life **at least** 1,000 charges → H₀: μ ≥ 1000 (claim), H₁: μ < 1000 (complement) |
| 11 | "Two types of errors we can make" |
| 12 | Always begin assuming H₀ true; decisions: reject H₀ or fail to reject H₀. Type I: reject H₀ when true. Type II: fail to reject H₀ when false |
| 13 | Decision table: rows do-not-reject / reject; columns H₀ true / false → correct, Type II / Type I, correct |
| 14 | Example: 94% employed; H₀: p = 0.94 (claim), H₁: p ≠ 0.94; Type I = it is 0.94 but rejected; Type II = it is not 0.94 but not rejected |
| 15 | α = P(reject H₀ | H₀ true) = size = level of significance (maximum P of Type I); β = P(accept H₀ | H₁ true); power 1 − β = P(reject H₀ | H₁ true) |
| 16–17 | Type I = false positive; "crying wolf" when no wolf |
| 18 | Type II = false negative; β; power = 1 − β |
| 19 | Fluoride example of a Type II error |
| 20 | **Example (binomial)**: 4 trials, H₀: p = 1/3 vs H₁: p = 1/2; accept if x ≤ 2. α = P(x > 2 | 1/3) = 4C3(1/3)³(2/3) + (1/3)⁴ = 1/9; β = P(x ≤ 2 | 1/2) = 1 − [4C3(0.5)⁴ + (0.5)⁴] = 11/16 |
| 21 | **Example (exponential)**: f = (1/θ)e^(−x/θ); H₀: θ = 5 vs H₁: θ = 10; reject if x ≥ 15. α = ∫₁₅^∞ (1/5)e^(−x/5)dx = e^(−3); β = ∫₀^15 (1/10)e^(−x/10)dx = 1 − e^(−3/2) |
| 22 | **Example (power function)**: f = (1 + θ)x^θ, 0 ≤ x ≤ 1; H₀: θ = 2; critical region x ≤ 0.1. (i) α = ∫₀^0.1 3x² dx = 0.001; (ii) θ = 3: P(reject) = 4∫₀^0.1 x³ dx = (0.1)⁴; (iii) power function = (0.1)^(θ+1) |
| 23 | Type I vs Type II comparison (false positive α / false negative β) |
| 24 | Level of significance = maximum allowable P(Type I); common α = 0.10, 0.05, 0.01; α = 0.10 → 10% chance of rejecting a true H₀ |
| 25 | Critical (rejection) region: test-statistic values where H₀ is rejected; critical value C.V. separates it from the non-critical region |
| 26 | References: S. P. Gupta, Statistical Methods; Gupta & Kapoor |

**Slips:** slide 7 drops the ≠ symbol (empty quotes); slide 18 and 23 say "accepting" H₀ (the pack says "fail to reject", and notes the slide's word). **v1.2 file 12 never used slides 20 and 22**: S6 adds them.

### 1.4 `BLUEPRINT` and MTE key
Blueprint analysed in `../../knowledge-base/exam-map.md` (rows 1–5, A 2 / B 6 / C 8 / D 8 marks). The MTE key is handwritten; its answers are in `verify.py` (`MTE …` checks): B1 bound 16/3 (exact 5/6), B2 a = −6, b = 6, B3, B4 1/3, C1(a), C1(b) T₁ unbiased, T₂ biased (E = 2μ).

---

## 2. Question bank → file and step

Every MTE, assignment and slide question is mapped (S0 cross-check: all 10 MTE parts, A1 24 items,
A2 28, A4 16, A5 26, slide examples 13 + 2 unused in v1.2: HT slides 20, 22). "Step" = idea in the §4 plan.

| File | Questions (tag → idea) |
|---|---|
| 01 | A1 MCQ 7, MCQ 9 → classical probability · A1 MCQ 6 → conditional probability · A1 MCQ 8 → P(A|B) = 1 |
| 02 | MTE A1 (b, c, d) + A1 MCQ 1 → discrete vs continuous · A1 MCQ 3, LA 2(i) → PMF rules, find k · A1 SA 1, LA 4 → PMF by counting · A1 MCQ 2, App 2, LA 2(iii) → CDF · LA 2(ii), (iv), (v) → probabilities from a PMF · A1 SA 3 → PDF check + median · A1 SA 2 → tail from a PDF · A1 LA 1 → conditional with a PDF |
| 03 | A1 MCQ 4, App 1, App 3 → E[X], Var, SD · A1 SA 4 → geometric expectation · MTE B2 → E for a continuous X (constants) · MTE A1(a), A1 LA 3 → rules for sums / products · A1 MCQ 5, MCQ 10, App 4 → Chebyshev statement · MTE B1, A1 SA 5, SA 6 → Chebyshev on a distribution |
| 04 | MTE B3 → binomial pmf, solving for p, expected frequency · A2 MCQ 2, MCQ 9 → np, npq, range · A2 B1, C3 → Poisson pmf, complements · MTE A2, A2 MCQ 3 → mean = variance · MTE A4 (+ G&K Ex. 7.30) → λ from a probability · A2 MCQ 7, D3 → Poisson approximation · A2 MCQ 12 → sum of Poissons |
| 05 | A2 B2, D4, MCQ 10 → uniform probability = length ratio · MTE B4 → bus word problem · A2 B8, C4 → absolute values, find K · A2 MCQ 4 → uniform variance · A2 MCQ 8, B7(i), D2 → exponential, survival · A2 MCQ 5, B7(ii), C1 → memoryless · A2 B5 → conditional that is not memoryless |
| 06 | A2 MCQ 1, MCQ 6 → shape, standard normal · A2 B3 → between two values · A2 MCQ 11 → 68% · A2 B4, D1 → expected counts · MTE C1(a) → normal inside binomial · A2 B6 → percentages → μ, σ · A2 C2 → two-condition inverse + percentile |
| 07 | SE/CLT slides p.2–3 → population / sample · p.4–5, A4 MCQ 8 → SE · p.7, p.9–10 → CLT rules · p.8 → n ≥ 30 cases · p.11–12 (ATM) → z for a mean · p.13–14 (impurity) → between two values · p.15–16 (LED) → lower tail · p.17–18 (machine) → normal population, small n |
| 08 | MTE C1(b) → unbiased linear combinations · MTE A3 → sufficient · G&K ch. 15 objective Q1 (iii), (iv), (vi) → consistent, sufficient |
| 09a | G&K ch. 15 ex. 20(b) → MoM one parameter · G&K ch. 15 ex. 21 → MoM two parameters · G&K ch. 15 ex. 23(b) → both methods on one data set |
| 09b | MLE slides p.2 → five steps · Ex. 12 → Poisson · Ex. 13 → exponential from data · Ex. 11 → normal μ, σ² · Ex. 14 → product of powers · p.3 → properties |
| 10 | MLE slides p.11–12 → Bayesian view, subjective probability, prior · p.13 → posterior, marginal · Ex. 15 → posterior table |
| 11 | A5 A1(v) → meaning of an interval · A4 B3 → z-interval · A4 B1 → 99% · A4 B2 → interval for 2μ + 7 · A4 B4, B5 → t-interval · A5 D2 (CI) → t-interval from raw data |
| 12 | HT slides 2–7, A5 A1(i)–(ii) → hypothesis, H₀, H₁ · slides 9, 10, 14, A4 MCQ 1, MCQ 6 → writing H₀/H₁ · A5 A1(iii) → one/two-tailed · slides 12–13, 16–19, A4 MCQ 4, 5, 7 → Type I/II · slides 15, 24–25, A4 MCQ 2, A5 A1(iv) → α, critical region · slide 15, 18 → β, power · A4 C1 → α/β uniform · slide 21 → α/β exponential · A4 C2, C3, slide 20 → α/β binomial · slide 22 → power function |
| 13 | A5 B1, A4 MCQ 3 → one-sample t, summary · A5 C1, B4 → raw data · A5 D2 (test) → two levels · A5 C2 → two independent samples (+ CI part b, t(20) = 2.086 not printed) · A5 C4, A2, A4 → paired |
| 14 | A5 A5 → F ratio · A5 C5 → from sums of squares · A5 B2, B3 → two-tailed from SDs · A5 D1 → raw data |
| 15 | A5 A7 → expected frequency · A5 A3, A6, A8 → χ², df · A5 C3 → 2 × 2 · A5 D3 → 2 × 2 shortcut · A5 B5 → table from a story · A5 B6 → 3 × 3 |
| 16 | A5 A9 → df · A5 A10 → F from SSB, SSW · A5 C6 → equal groups · A5 D4 → unequal groups |
| 17 mock | re-point rows to the new file/step names in S9 |

**Answer-key slips (11, all in `verify.py`, keep in START-HERE's slip table):** A1 LA 3 (0.808 → 0.8), A1 App 3 SD (0.98 → 0.973), A2 B5 (0.5679 → 0.6225), A2 C2 (μ 37.5 → 37.18, mark 30.43 → 30.40), A5 A4 (key 3.00 → exact 3.098; option C is only the nearest), A5 A10 (4.00 → 4.44), A5 D1 (5.19 = F(4,5) → F(4,4) = 6.39), A5 D2 CI (24.945, 25.075 → 24.93, 25.08), A5 C6 (19.41 = F(12,2) → F(2,12) = 3.89; decision flips). Slide slips: §1 above.

---

## 3. Constants and table values

No physical constants. **Every table value** the questions and slides print (36) is recomputed and
listed in `../../knowledge-base/04-hypothesis-testing.md` → *Table values the course's questions use*
(added this sprint; all match except the two key slips). The pack prints the question's own value,
and the exact value where they differ. Needed but not printed: t(20) two-sided 5% = 2.086 (A5 C2).

---

## 4. File plan (ideas → steps, running example, figures)

Learner constraint: novice, dense notation overloads → **one symbol per step, concrete first**. The
step lists are the ideas found in the questions + KB; the sprint fixes the final order (deck order,
protocol 6) and splits when over 13 steps. `figlib` has only helpers (fig, canvas, box, arrow, axes,
svg): **every figure below is built in `figures.py` on those helpers**; "v1.2: name" = an old figure
that may be reused only if it meets the caption rule and passes the overlap check.

| File | Ideas (one step each) | Running example | Figures (one per idea that needs a picture) |
|---|---|---|---|
| 01 | outcome & sample space · event · classical count-and-divide · axioms · complement · addition rule (exclusive / not) · conditional = shrunk sample space · P(A|B) = 1 · multiplication rule · independence · total probability · Bayes (12) | two dice, 36 outcomes (reused in 03 Chebyshev SA 5) | 6 × 6 dice grid with events shaded (new) · Venn (v1.2: venn) · shrunk-space grid · tree (v1.2: cond_tree) · Bayes tree reversed |
| 02 → **02a/02b** | a: RV as a rule outcome → number · discrete vs continuous · PMF + its two rules · find k · PMF by counting · CDF as a staircase · probabilities from PMF/CDF · b: PDF as area · normalising / checking a PDF · continuous CDF & median · tail probability · conditional with a PDF | a: 3 children, X = number of boys (A1 SA 1); b: f(x) = 6x(1 − x) (A1 SA 3) | 8 outcomes → X arrows · PMF bars (v1.2: pmf_cdf) · CDF staircase · PDF area shaded (v1.2: pdf_area) · CDF curve with median · tail area of x e^(−x/3)/9 |
| 03 → **03a/03b** | a: E[X] as balance point · E[X] from a table · E[X²] / E[g(X)] · variance as mean squared distance · shortcut E[X²] − μ² · SD · E and Var for a continuous X · b: E[aX + b], Var(aX + b) · sums and independent products · geometric expectation · Chebyshev statement · Chebyshev on a distribution · Chebyshev lower bound | a: sensors PMF 0.25/0.40/0.25/0.10 (A1 App 1, E = 1.2, Var = 0.86); b: dice sum (A1 SA 5) | balance beam (v1.2: balance) · squared-distance bars · continuous balance (ax² + bx) · Chebyshev bound vs true tail (v1.2: chebyshev) · k-σ band on dice-sum PMF |
| 04 → **04a/04b** | a: Bernoulli trial · counting nCx · binomial pmf · mean np, variance npq, range · solving for p from a ratio · expected frequency N·P · b: Poisson pmf (λ = rate) · mean = variance · λ from a probability · complements ("at least", "rejected") · Poisson ≈ binomial · sum of Poissons | a: irregular die, 10 throws (MTE B3); b: IT desk λ = 2.5, 3 technicians (A2 B1) | binomial bars (v1.2: binom_poisson) · paths tree for nCx · Poisson bars with "> 3" shaded · binomial → Poisson convergence (v1.2: poisson_limit) |
| 05 | uniform: flat height 1/(b − a) · probability = length ratio (clip at b) · bus word problem · absolute values · mean and variance · find K · exponential density, β = 1/λ · survival e^(−λx) · memoryless · a conditional that is not memoryless (10) | U(−3, 3) (A2 B8); exponential mean 2 (A2 B5, B7) | rectangle with shaded strip · timeline 7:00–7:30 (v1.2: uniform_bus) · |X| < 2 band · exponential curve with tail · memoryless shift (v1.2: expo_memoryless) |
| 06 | bell shape, μ and σ · standard normal Z · standardise z = (x − μ)/σ · read table area 0..z · between two values · tails · 68–95–99.7 · expected counts N·P · normal inside a binomial · percentages → μ, σ · two-condition inverse + percentile (11) | batteries μ = 1500, σ = 100 (A2 B4) | curve with μ, σ marked (v1.2: normal_rule) · x-axis ↔ z-axis · table-area picture · shaded between/tail · inverse (v1.2: normal_inverse) |
| 07 | population vs sample · parameter vs statistic · sampling distribution of x̄ · SE = σ/√n · n × 4 → SE ÷ 2 · CLT three rules · n ≥ 30 cases · z for a mean (ATM) · between two values · lower tail · normal population, small n (11) | ATM μ = 4, σ = 2, n = 36 | balls → samples (redraw slide p.3) · SE vs n (v1.2: se_shrink) · population shapes → x̄ shapes (v1.2: clt_hist) · x̄ curve with shaded tail |
| 08 | parameter / estimator / estimate · point vs interval · unbiased · checking linear combinations · n − 1 in s² · consistent · efficient · sufficient (8) | X₁, X₂, X₃ with mean μ (MTE C1(b)) | targets (v1.2: targets) · two sampling curves (bias vs spread) · variance shrinking with n |
| 09a | population vs sample moments · MoM, one parameter · MoM, two parameters · MoM on data (G&K 23(b)) (≈ 5–6) | G&K ex. 20(b) | moment matching picture |
| 09b | likelihood as a product (coin anchor) · log turns product to sum · the five steps · Poisson (Ex. 12) · exponential from data (Ex. 13) · normal μ (Ex. 11a) · normal σ² (Ex. 11b) · product of powers (Ex. 14) · second-derivative check · properties · MoM vs MLE (≈ 11) | rats data, x̄ = 16.2 (Ex. 13) | likelihood curve peak (v1.2: likelihood_curve) · L vs ln L same peak · ln L for Ex. 14 |
| 10 | frequentist vs Bayesian · subjective probability · prior · likelihood f(x|p) · marginal g(x) · posterior · full posterior table · Bayes point estimate (8) | Ex. 15 (prior 0.6 / 0.4) | prior vs posterior bars (v1.2: prior_posterior) · tree prior → data |
| 11 | what an interval means · z-interval σ known · confidence level → z · width vs n · interval for 2μ + 7 · why t · t-interval · t-interval from raw data (8) | haemoglobin n = 100, x̄ = 12.5, σ = 2 (A4 B3) | 20 intervals around μ (v1.2: ci_coverage) · z vs t curves (v1.2: z_vs_t) · width vs n |
| 12 → **12a/12b** | a: hypothesis, test of significance · H₀ and H₁ (signs) · writing them from a claim · one/two-tailed · Type I/II table · α, critical region · β and power · b: α/β uniform (A4 C1) · α/β exponential (slide 21) · α/β binomial (slide 20, A4 C2, C3) · power function (slide 22) · steps of every test | a: battery claim μ ≥ 1000 (slide 10); b: H₀ θ = 1 vs θ = 2 uniform (A4 C1) | decision table · tails (v1.2: two_tails) · α/β areas (v1.2: alpha_beta) · binomial bars under H₀ and H₁ · power curve (0.1)^(θ+1) |
| 13 | t statistic from a summary · s from raw data (n − 1) · decide at 5% and 1% · one vs two tails · pooled two-sample t · CI for μ₁ − μ₂ · paired t (7) | nitrate bags (A5 C1) | t curve with critical values (v1.2: t_decision) · two groups dots · paired differences (v1.2: paired_diff) |
| 14 | F = larger s² / smaller s² · df order matters · from sums of squares · two-tailed from SDs · raw data · F before pooled t (6) | A5 C5 (SS 112, 140) | F curve with 5% tail (v1.2: f_curve) · two spreads side by side |
| 15 | contingency table · expected = row × column / total · χ² = Σ(O − E)²/E · df (r − 1)(c − 1) · 2 × 2 test · 2 × 2 shortcut · table from a story · 3 × 3 (8) | smokers 2 × 2 (A5 C3) | observed vs expected bars (v1.2: obs_exp) · χ² curve (v1.2: chi_curve) |
| 16 | why compare variances · assumptions, one-way · SST = SSB + SSW · df k − 1, N − k · ANOVA table and F · equal groups · unequal groups (7) | blood pressure 3 × 5 (A5 C6) | group dots with means (v1.2: anova_dots) · SS split bar |

**Sprint consequences (Assumption 4, new):** the expected splits (02a/b, 03a/b, 04a/b, 09a/b, 12a/b)
fit the sprint table without new sprints: S1 = 01 + 02a + 02b, S2 = 03a + 03b + 08, S4 = 04a + 04b + 05,
S6 = 11 + 12a + 12b.
