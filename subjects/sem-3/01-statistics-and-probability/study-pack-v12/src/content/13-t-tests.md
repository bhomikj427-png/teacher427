# 13 — t-tests: one sample, two samples, paired

<div class="sub">Gupta & Kapoor §14.2, §14.2.10 · blueprint row 5 "testing of significance: t-test" · 9 real questions (Assignments 4, 5) · needs 08 (s²), 11 (t-distribution), 12 (the test steps)</div>

## Map

[[map:1 One-sample t from a summary > 2 One-sample t from raw data > 3 One test at two levels > 4 Two independent samples > 5 Paired samples|here=1]]

## The questions this file answers

- <span class="tag">A5 B1</span> A phone company claims calls average 8 minutes. 18 calls: mean 7.8 min, SD 0.5 min. Enough evidence at α = 0.05? (Table value 2.110.)
- <span class="tag">A5 C1</span> A machine should put 12 kg of nitrate in each bag. Ten bags: 11, 14, 13, 12, 13, 12, 13, 14, 11, 12. Is the machine defective? (t₀.₀₅,₉ = 2.262.)
- <span class="tag">A5 B4</span> Ten pesticide bags weigh 50, 49, 44, 52, 45, 48, 46, 45, 49, 45 kg. Can the average be taken as 50 kg? (Table value 2.262.)
- <span class="tag">A5 D2</span> 20 part weights, target 25.0 g: has the mean shifted? Test at 5% and 1%. (t₀.₀₅ = 2.093, t₀.₀₁ = 2.861 for 19 df.)
- <span class="tag">A5 C2</span> Class A: 12 students, mean 68, Σ(x − x̄)^{2} = 220. Class B: 10 students, mean 62, Σ = 180. (a) Test the difference of means at 5%. (b) 95% CI for the difference.
- <span class="tag">A5 C4</span> Sales in six shops before and after a campaign: 53/58, 28/29, 31/30, 48/55, 50/56, 42/45. Was the campaign a success at 5%? (Table value 2.02.)
- <span class="tag">A5 A2, A4</span> · <span class="tag">A4 MCQ 3</span> Null hypothesis of a paired t-test; a paired t from summary values; when the t-test is appropriate.

Row 5 (18 marks) holds the paper's only Part D (8 marks). A t-test with raw data is one of the four candidates.

---

## Build

### 1 · One-sample t from a summary

File 11 built the t-interval. The t-test asks the same quantity whether a claimed μ₀ is believable.

:::q <span class="tag">A5 B1</span>
A local telephone company claims that the average length of a phone call is 8 minutes. In a random sample of 18 calls, the sample mean was 7.8 minutes and the standard deviation was 0.5 minutes. Is there enough evidence to support this claim at α = 0.05? State the null and alternative hypotheses. (Tabulated value 2.110.)
:::

:::guess Guess first
7.8 is 0.2 below 8. Is that a lot, measured in standard errors?
:::

**Test statistic** (G&K §14.2). Normal population, σ unknown, H₀: μ = μ₀:

$$t = \frac{x̄ − μ_{0}}{s/√n},    df = n − 1,    s^{2} = \frac{Σ(x − x̄)^{2}}{n − 1}$$

<span class="tag">A4 MCQ 3</span>: σ unknown, normal population, small sample ⇒ **Student's t-test** (B).

**Answer.** H₀: μ = 8; H₁: μ ≠ 8 (two-tailed). df = 17, t₀.₀₅ = 2.110.
SE = 0.5/√18 = 0.11785. t = (7.8 − 8)/0.11785 = **−1.697**.
|t| = 1.697 < 2.110 ⇒ **do not reject H₀**: the data are consistent with the company's claim of 8 minutes.

:::note Which SD is "the standard deviation"?
The pack reads a given sample SD as s (n − 1 divisor). Gupta & Kapoor sometimes give the n-divisor SD instead; then t = (x̄ − μ₀)/(SD/√(n − 1)) = −0.2/(0.5/√17) = −1.649. The decision is the same. In the exam, write which reading you use.
:::

:::check Check 1
A sample of 16 has x̄ = 41.5 and s = 6. Test H₀: μ = 44 against H₁: μ ≠ 44 at 5% (t₀.₀₅,₁₅ = 2.131).
:::

### 2 · One-sample t from raw data

With raw data, compute x̄ and s first. Subtracting a round number keeps the arithmetic small.

:::q <span class="tag">A5 C1</span>
A fertiliser mixing machine is set to give 12 kg of nitrate per quintal bag. Ten 100 kg bags are examined; the percentages of nitrate are 11, 14, 13, 12, 13, 12, 13, 14, 11, 12. Is there any reason to believe the machine is defective? (t for 9 df at 5% = 2.262.)
:::

:::guess Guess first
x̄ is just above 12. Guess: reject or not?
:::

**Answer.** H₀: μ = 12 (machine fine); H₁: μ ≠ 12. df = 9.
Let d = x − 12: −1, 2, 1, 0, 1, 0, 1, 2, −1, 0. Σd = 5, Σd^{2} = 13.
x̄ = 12 + 0.5 = **12.5**. Σ(x − x̄)^{2} = 13 − 5^{2}/10 = 10.5; s^{2} = 10.5/9 = 1.1667, **s = 1.0801**.
t = (12.5 − 12)/(1.0801/√10) = 0.5/0.34157 = **1.464**.
|t| = 1.464 < 2.262 ⇒ **do not reject H₀**: no evidence the machine is defective.

[[fig:t_decision|Both bag questions on one t(9) curve: only the pesticide bags fall in the red region.|w=80]]

:::check Check 2
<span class="tag">A5 B4</span> Certain pesticide is packed into bags by a machine. Ten bags weigh 50, 49, 44, 52, 45, 48, 46, 45, 49, 45 kg. Test whether the average packing can be taken as 50 kg. (Table value 2.262.)
:::

### 3 · One test at two significance levels

A Part D question can ask for the decision at 5% and at 1%: one statistic, two critical values.

:::q <span class="tag">A5 D2 (test part)</span>
A company aims for a part weight of 25.0 g. 20 parts weigh 24.8, 25.1, 24.9, 25.0, 25.2, 24.7, 25.0, 25.1, 25.3, 24.9, 25.0, 24.8, 25.1, 24.9, 25.2, 25.0, 25.1, 24.8, 25.0, 25.2 g. The engineers fear the mean has shifted from 25.0 g. Test at the 5% and 1% levels. (19 df: t₀.₀₅ = 2.093, t₀.₀₁ = 2.861.)
:::

:::guess Guess first
If H₀ is not rejected at 5%, can it be rejected at 1%?
:::

**Answer.** From file 11 step 6: x̄ = 25.005, s = 0.16051, SE = 0.035891.
H₀: μ = 25.0; H₁: μ ≠ 25.0 (any shift). t = 0.005/0.035891 = **0.139**.
5%: 0.139 < 2.093 ⇒ do not reject. 1%: 0.139 < 2.861 ⇒ do not reject. **No evidence of a shift at either level.**
A smaller α moves the critical value outward, so "not rejected at 5%" always implies "not rejected at 1%".

:::check Check 3
A test gives |t| = 2.5 with 19 df. Decision at 5% and at 1%?
:::

### 4 · Two independent samples

Two groups, two means: is the difference real?

:::q <span class="tag">A5 C2</span>
A random sample of 12 students from Class A has mean score 68 and sum of squares of deviations from the mean 220. A sample of 10 students from Class B has mean 62 and sum of squares of deviations 180. (a) Test whether there is a significant difference between the mean scores at the 5% level. (b) Obtain the 95% confidence interval for the difference between the two population means.
:::

:::guess Guess first
The means differ by 6. Guess the SE of that difference: about 1, 2 or 5?
:::

**Test statistic** (G&K §14.2.10). Two independent normal samples, equal unknown variances, H₀: μ₁ = μ₂:

$$t = \frac{x̄_{1} − x̄_{2}}{S√(1/n_{1} + 1/n_{2})},    S^{2} = \frac{Σ(x_{1} − x̄_{1})^{2} + Σ(x_{2} − x̄_{2})^{2}}{n_{1} + n_{2} − 2},    df = n_{1} + n_{2} − 2$$

S^{2} is the **pooled variance**. Assumptions: both populations normal; equal variances (testable by file 14's F-test); samples independent.

**Answer.** (a) H₀: μ_{A} = μ_{B}; H₁: μ_{A} ≠ μ_{B}. df = 20, t₀.₀₅ = 2.086.
S^{2} = (220 + 180)/20 = **20**. SE = √(20 × (1/12 + 1/10)) = √3.6667 = 1.9149.
t = (68 − 62)/1.9149 = **3.133** > 2.086 ⇒ **reject H₀**: the class means differ significantly.
(b) CI = (x̄₁ − x̄₂) ± t₀.₀₅ × SE = 6 ± 2.086 × 1.9149 = 6 ± 3.994 = **(2.006, 9.994)**. It excludes 0, matching (a).

:::check Check 4
Two samples: n₁ = 8, x̄₁ = 15, s₁^{2} = 4; n₂ = 8, x̄₂ = 13, s₂^{2} = 5 (s^{2} with n − 1). Test equality of means at 5% (t₀.₀₅,₁₄ = 2.145).
:::

### 5 · Paired samples

When the same units are measured twice, the two samples are not independent. Test the differences instead.

:::q <span class="tag">A5 C4</span>
The sales data of an item in six shops before and after a special promotional campaign: A 53 → 58, B 28 → 29, C 31 → 30, D 48 → 55, E 50 → 56, F 42 → 45. Can the campaign be judged a success? Test at the 5% level. (Tabulated value 2.02.)
:::

:::guess Guess first
"A success" means sales went **up**. One-tailed or two-tailed?
:::

[[fig:paired_diff|Each shop is its own control: only the differences d matter.|w=70]]

**Paired t-test** (G&K §14.2.10, remark 4). For n pairs, dᵢ = afterᵢ − beforeᵢ; H₀: μ_{d} = 0:

$$t = \frac{d̄}{s_{d}/√n},    s_{d}^{2} = \frac{Σ(d − d̄)^{2}}{n − 1},    df = n − 1$$

<span class="tag">A5 A2</span>: the null hypothesis of a paired t-test is **μ_{d} = 0**: the mean difference is zero (no effect).

**Answer.** H₀: μ_{d} = 0; H₁: μ_{d} > 0 (sales increase; right-tailed). df = 5; one-tailed t₀.₀₅ = 2.015 (the table value 2.02).
d = 5, 1, −1, 7, 6, 3. Σd = 21, d̄ = **3.5**. Σd^{2} = 121; Σ(d − d̄)^{2} = 121 − 21^{2}/6 = 47.5; s_{d}^{2} = 9.5, **s_{d} = 3.082**.
t = 3.5/(3.082/√6) = 3.5/1.2583 = **2.782** > 2.02 ⇒ **reject H₀**: the campaign increased sales.

:::note A5 A4's options
"A paired t-test on 15 subjects: mean difference 3.2, SD of differences 4.0. The t-value is: 1.55 / 2.10 / 3.00 / 3.87." Exact value: t = 3.2/(4.0/√15) = 3.2/1.0328 = **3.10**. No option matches; 3.00 (C) is the nearest. Write 3.10 and the working.
:::

:::check Check 5
Five patients' blood pressure before/after a drug: 140/132, 150/148, 135/128, 160/150, 145/142. Test at 5% whether the drug lowers blood pressure (one-tailed t₀.₀₅,₄ = 2.132).
:::

---

## Exam form

| Test | H₀ | Statistic | df |
|---|---|---|---|
| One sample | μ = μ₀ | t = (x̄ − μ₀)/(s/√n) | n − 1 |
| Two independent samples | μ₁ = μ₂ | t = (x̄₁ − x̄₂)/(S√(1/n₁ + 1/n₂)), S^{2} = [Σ(x₁ − x̄₁)^{2} + Σ(x₂ − x̄₂)^{2}]/(n₁ + n₂ − 2) | n₁ + n₂ − 2 |
| Paired | μ_{d} = 0 | t = d̄/(s_{d}/√n) | n − 1 |

**Assumptions.** Normal population(s); σ unknown; random samples; for two samples, independent with equal variances; for paired, the same units measured twice.

**Procedure.** H₀, H₁ (tails) → α → statistic and df → compute (use d = x − A to simplify) → table value → compare |t| with it → conclusion in the problem's words.

**Shortcut.** Σ(x − x̄)^{2} = Σd^{2} − (Σd)^{2}/n for any shift d = x − A.

## Traps

- Using the two-sample test on paired data (before/after on the same shops).
- df = n instead of n − 1; df = n₁ + n₂ − 1 instead of n₁ + n₂ − 2.
- Two-tailed table value for a one-tailed question ("increased", "reduced", "success").
- Using s^{2} (n − 1 divisor) when the question already gives Σ(x − x̄)^{2}: just add the sums and divide by n₁ + n₂ − 2.
- Concluding "H₀ is true" instead of "no significant evidence against H₀".

## Self-test

1. Write the one-sample, two-sample and paired t statistics with their df.
2. List the assumptions of the two-sample t-test.
3. n = 25, x̄ = 52, s = 5. Test H₀: μ = 50 at 5% (t₀.₀₅,₂₄ = 2.064).
4. n₁ = n₂ = 6, Σ(x₁ − x̄₁)^{2} = 30, Σ(x₂ − x̄₂)^{2} = 20, x̄₁ − x̄₂ = 3. Find t.
5. When is a paired test used instead of a two-sample test?
6. A paired test on 10 pairs gives d̄ = 1.2, s_{d} = 1.5. Find t and decide at 5% two-tailed (t₀.₀₅,₉ = 2.262).

<!--ANSWERS-->
## Answers

**Check 1.** SE = 6/4 = 1.5; t = −2.5/1.5 = **−1.667**; |t| < 2.131: do not reject.

**Check 2.** d = x − 48: 2, 1, −4, 4, −3, 0, −2, −3, 1, −3; Σd = −7, Σd^{2} = 69. x̄ = **47.3**; Σ(x − x̄)^{2} = 69 − 4.9 = 64.1; s^{2} = 7.122, s = **2.669**. t = (47.3 − 50)/(2.669/√10) = **−3.199**; |t| > 2.262 ⇒ **reject H₀**: the average packing is not 50 kg.

**Check 3.** 5%: 2.5 > 2.093 ⇒ reject. 1%: 2.5 < 2.861 ⇒ do not reject.

**Check 4.** S^{2} = (7 × 4 + 7 × 5)/14 = 4.5; SE = √(4.5 × ¼) = 1.0607; t = 2/1.0607 = **1.886** < 2.145: do not reject.

**Check 5.** d = before − after = 8, 2, 7, 10, 3: d̄ = 6, Σ(d − d̄)^{2} = 4 + 16 + 1 + 16 + 9 = 46, s_{d}^{2} = 11.5, s_{d} = 3.391. t = 6/(3.391/√5) = **3.956** > 2.132 ⇒ **reject H₀**: the drug lowers blood pressure.

**Self-test.**

1. See Exam form.
2. Both populations normal; equal (unknown) variances; samples random and independent.
3. t = 2/(5/5) = **2** < 2.064: do not reject.
4. S^{2} = 50/10 = 5; SE = √(5 × ⅓) = 1.291; t = **2.324**.
5. When each observation in one sample is matched with one in the other (same unit before/after, twins, matched pairs).
6. t = 1.2/(1.5/√10) = **2.530** > 2.262: reject.
<!--/ANSWERS-->
