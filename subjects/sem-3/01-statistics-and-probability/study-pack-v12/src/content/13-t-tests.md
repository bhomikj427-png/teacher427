# 13 — t-tests: one sample, two samples, paired

<div class="sub">Gupta & Kapoor §14.2 (t-test for a single mean, Example 14·6), §14.2.10 (difference of means; remarks 3–4: assumptions, paired t-test) · blueprint row 5 "testing of significance: t-test" · 9 real questions (A5 A2, A4, B1, B4, C1, C2, C4, D2; A4 MCQ 3) · needs 08 (s with n − 1, step 5), 11 (the t-distribution and its table, step 7; A5 D2's x̄ and s, step 8), 12a (H₀, H₁, tails, steps of a test: steps 2–4, 8)</div>

## Map

[[map:1 σ unknown: the t statistic > 2 s and t from raw data > 3 One test at two levels > 4 One tail or two? > 5 Two independent samples > 6 An interval for μ₁ − μ₂ > 7 Paired samples|here=1]]

File 12a ran a test with z = (x̄ − μ₀)/SE, where SE = σ/√n needed the population's σ. In the assignment questions nobody gives σ: there is only the sample. This file swaps σ for the sample's own s, which turns z into **t**, and uses file 11's t table for the critical value. Steps 1–4 test one mean; steps 5–6 compare the means of two separate groups; step 7 compares two measurements on the same units. File 14 tests the equal-variance assumption that step 5 needs; file 16 compares three or more means.

| Symbol | What it means in this file | Typical value |
|---|---|---|
| μ₀ | the mean the claim or target states (H₀: μ = μ₀) | 12 kg nitrate |
| n | how many items were measured | 10 bags |
| x̄ | the sample's average | 12.5 |
| s | sample SD: spread of the n values, squared deviations divided by n − 1 (08 step 5) | 1.080 |
| SE | s/√n: how far x̄ typically sits from μ, estimated from the sample | 0.3416 |
| t | (x̄ − μ₀)/SE: how many estimated SEs x̄ sits from μ₀ | 1.464 |
| df | degrees of freedom: which t curve (and which table row) to use; n − 1 for one sample | 9 |
| S² | pooled variance: both groups' squared deviations added, divided by n₁ + n₂ − 2 (step 5) | 20 |
| d, d̄, s_{d} | for paired data: each unit's change, their average, their SD (step 7) | d̄ = 3.5 |

**Running example.** A5 C1's fertiliser machine should put **12 kg of nitrate** in every 100 kg bag. Ten bags hold 11, 14, 13, 12, 13, 12, 13, 14, 11, 12 kg: **n = 10, x̄ = 12.5, s = 1.080, SE = 0.3416, t = 1.464, df = 9**, table value 2.262. Steps 2–4 use it.

## The questions this file answers

- <span class="tag">A5 B1</span> A phone company claims calls average 8 minutes; 18 calls average 7.8 min with SD 0.5 min. Enough evidence at α = 0.05? State H₀ and H₁. (Table value 2.110.)
- <span class="tag">A5 C1</span> The nitrate machine above: is there any reason to believe it is defective? (t for 9 df at 5% = 2.262.)
- <span class="tag">A5 B4</span> Ten pesticide bags weigh 50, 49, 44, 52, 45, 48, 46, 45, 49, 45 kg. State H₀ and H₁ that the average packing can be taken as 50 kg. (Table value 2.262.)
- <span class="tag">A5 D2 (test part)</span> 20 part weights, target 25.0 g: has the mean shifted? Test at 5% and 1%. (19 df: t₀.₀₅ = 2.093, t₀.₀₁ = 2.861.)
- <span class="tag">A5 C2</span> Class A: 12 students, mean 68, Σ(x − x̄)² = 220. Class B: 10 students, mean 62, Σ(x − x̄)² = 180. (a) Test the difference of means at 5%. (b) 95% confidence interval for the difference.
- <span class="tag">A5 C4</span> Sales in six shops before and after a campaign: 53/58, 28/29, 31/30, 48/55, 50/56, 42/45. Was the campaign a success at 5%? (Table value 2.02.)
- <span class="tag">A5 A2, A4</span> · <span class="tag">A4 MCQ 3</span> The null hypothesis of a paired t-test; a paired t from summary values; when the t-test is the right test.

Blueprint row 5 (18 marks) holds the paper's only Part D (8 marks); a t-test on raw data (D2) is one of the four candidates.

---

## Build

### 1 · σ unknown: the t statistic

A phone company's claim about its average call length is a claim about μ. 12a step 8 tests such a claim with z, but z needs σ, and here only the sample's SD is known.

:::q <span class="tag">A5 B1</span>
A local telephone company claims that the average length of a phone call is 8 minutes. In a random sample of 18 phone calls, the sample mean was 7.8 minutes and the standard deviation was 0.5 minutes. Is there enough evidence to support this claim at α = 0.05? State the null and alternative hypotheses. (Tabulated value 2.110.)
:::

:::guess Guess first
7.8 is 0.2 minutes below 8. One call varies by about 0.5 minutes; an average of 18 calls varies by much less. Is 0.2 a big gap for an average of 18? Yes or no.
:::

:::note Terms
**s:** the sample SD, the typical distance of one call from the sample's average, with the squared deviations divided by n − 1 (08 step 5). It stands in for the unknown σ. **SE = s/√n:** the typical distance of an average of n calls from μ, now estimated from the sample. **t = (x̄ − μ₀)/SE:** the gap between the sample's average and the claimed mean, counted in SEs: the same count as 12a's z, with s in place of σ.
:::

[[fig:t_calls|What this graph plots: the t curve with 17 df, the spread of t over many samples of 18 calls if the claim μ = 8 is true. Horizontal axis: the value of t; height: how often samples give a t near that value. Red tails beyond ±2.110 hold 5% of samples together; the green line is these 18 calls' t = −1.697.|w=82]]

| t (either sign) | share of samples further out than this, if μ = 8 (17 df) |
|---|---|
| 1 | 0.331 |
| 1.697 (this sample) | 0.108 |
| 2.110 (table value) | 0.05 |
| 2.898 | 0.01 |

The t curve is file 11's (step 7): wider-tailed than the normal curve because s itself varies from sample to sample, and the fewer the values, the wider. **df = n − 1** picks the curve: 18 calls, 17 df, so the 5% two-tailed value is 2.110 instead of z's 1.96.

$$t = \frac{x̄ − μ_{0}}{s/√n},    df = n − 1$$

Read in words: t = (sample average − claimed mean) ÷ (estimated SE of the average), compared with the t table's row n − 1 (G&K §14.2).

**Answer to the question.**

1. H₀: μ = 8 minutes (the claim); H₁: μ ≠ 8 (a shorter or longer average both contradict it: two-tailed).
2. SE = s/√n = 0.5/√18 = 0.5/4.2426 = 0.11785 minutes.
3. t = (7.8 − 8)/0.11785 = −0.2/0.11785 = **−1.697**.
4. df = 18 − 1 = 17; table value t₀.₀₅ = 2.110.
5. The size of t, 1.697, is less than 2.110: t is not in the critical region. **Do not reject H₀**: at the 5% level the 18 calls are consistent with the claimed 8 minutes. (The guess: 0.2 minutes is 1.7 SEs, an ordinary gap; about 11 samples in 100 land this far out when μ really is 8.)

:::note Which SD is "the standard deviation"?
The pack reads a given SD as s (n − 1 divisor). Some Gupta & Kapoor problems give the n-divisor SD instead; then t = (x̄ − μ₀)/(SD/√(n − 1)) = −0.2/(0.5/√17) = −1.649. The decision is the same. In the exam, write which reading you use.
:::

<span class="tag">A4 MCQ 3</span> asks when this test applies: a normal population, σ unknown, a small sample: **Student's t-test**. With σ known, 12a's z-test applies.

:::check Check 1
A sample of 16 values has x̄ = 41.5 and s = 6. Test H₀: μ = 44 against H₁: μ ≠ 44 at 5% (t₀.₀₅ for 15 df = 2.131).
:::

### 2 · s and t from raw data

Step 1 was handed x̄ and s. A 6-mark question hands over the raw values, and computing s is most of the work.

:::q <span class="tag">A5 C1</span>
A fertiliser mixing machine is set to give 12 kg of nitrate per quintal bag. Ten 100 kg bags are examined; the nitrate per bag is 11, 14, 13, 12, 13, 12, 13, 14, 11, 12. Is there any reason to believe that the machine is defective? (Value of t for 9 df at the 5% level: 2.262.)
:::

:::guess Guess first
The bags average just above 12. Defective or not? Guess before computing.
:::

[[fig:nitrate_dots|What this graph plots: the ten bags as dots on a nitrate axis (kg per bag); bags with equal nitrate are stacked. The dashed line is the target 12, the solid line the sample's average 12.5.|w=72]]

The values sit on both sides of 12; the average is pulled half a kilogram up by the two 14s. To measure that half kilogram in SEs, find s first. Subtracting a round number A from every value (here A = 12, d = x − 12) keeps the squares small and does not change the spread:

| x | 11 | 14 | 13 | 12 | 13 | 12 | 13 | 14 | 11 | 12 | total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| d = x − 12 | −1 | 2 | 1 | 0 | 1 | 0 | 1 | 2 | −1 | 0 | Σd = 5 |
| d² | 1 | 4 | 1 | 0 | 1 | 0 | 1 | 4 | 1 | 0 | Σd² = 13 |

$$Σ(x − x̄)^{2} = Σd^{2} − \frac{(Σd)^{2}}{n}$$

In words: the sum of squared deviations from the average = the sum of squared shifted values minus (their total)² ÷ n.

**Answer to the question.**

1. H₀: μ = 12 kg (the machine works); H₁: μ ≠ 12 kg (it puts in too much or too little).
2. x̄ = 12 + Σd/n = 12 + 5/10 = **12.5**.
3. Σ(x − x̄)² = 13 − 5²/10 = 13 − 2.5 = 10.5.
4. s² = 10.5/(10 − 1) = 1.1667; **s = 1.0801**.
5. SE = 1.0801/√10 = 1.0801/3.1623 = 0.34157.
6. t = (12.5 − 12)/0.34157 = **1.464**, df = 9.
7. 1.464 < 2.262: **do not reject H₀**. The ten bags give no reason to believe the machine is defective.

:::check Check 2
<span class="tag">A5 B4</span> Ten pesticide bags weigh 50, 49, 44, 52, 45, 48, 46, 45, 49, 45 kg. State H₀ and H₁, then test at 5% whether the average packing can be taken as 50 kg (table value 2.262). Use d = x − 48.
:::

### 3 · One test at two significance levels

A Part D question can ask for the decision at 5% and at 1%: one t, two critical values.

:::q <span class="tag">A5 D2 (test part)</span>
A company aims for a part weight of 25.0 g. 20 parts weigh 24.8, 25.1, 24.9, 25.0, 25.2, 24.7, 25.0, 25.1, 25.3, 24.9, 25.0, 24.8, 25.1, 24.9, 25.2, 25.0, 25.1, 24.8, 25.0, 25.2 g. The engineers fear the average has shifted away from 25.0 g. Test at the 5% and 1% levels. (19 df: t₀.₀₅ = 2.093, t₀.₀₁ = 2.861.)
:::

:::guess Guess first
If H₀ is not rejected at 5%, can it be rejected at 1%?
:::

[[fig:t_levels|What this graph plots: the t curve with 19 df. The 5% critical values ±2.093 (orange) and the 1% critical values ±2.861 (red) are marked; a smaller α pushes the boundary further out. Green: the parts' t = 0.139; purple: Check 3's t = 2.5.|w=82]]

| α (two-tailed) | critical value, 19 df | a t of 2.5 is… |
|---|---|---|
| 0.10 | 1.729 | rejected |
| 0.05 | 2.093 | rejected |
| 0.01 | 2.861 | not rejected |

**Answer to the question.** File 11 step 8 computed the parts' x̄ = 25.005, s = 0.16051, SE = 0.16051/√20 = 0.035891.

1. H₀: μ = 25.0 g; H₁: μ ≠ 25.0 g ("shifted away" = either direction).
2. t = (25.005 − 25.0)/0.035891 = **0.139**, df = 19.
3. 5%: 0.139 < 2.093, do not reject. 1%: 0.139 < 2.861, do not reject.
4. **No evidence that the average weight has shifted**, at either level.

Answer to the guess: no. The 1% boundary lies outside the 5% boundary, so a t inside the 5% boundary is inside the 1% boundary too. The reverse can happen: a t between them (Check 3) is rejected at 5% but not at 1%.

:::check Check 3
A test with 19 df gives t = 2.5. Decide at 5% and at 1%.
:::

### 4 · One tail or two?

Steps 1–3 were two-tailed because the question allowed a shift either way. 12a step 4 showed that a one-sided H₁ puts the whole α in one tail; on the t curve that moves the critical value inward.

:::q Predict
The farmers only complain if the machine puts in **too much** nitrate, so the test becomes H₀: μ = 12 against H₁: μ > 12 at 5%. Is the critical value for 9 df still 2.262, smaller, or larger?
:::

:::guess Guess first
Pick one: smaller, the same, larger.
:::

[[fig:t_one_two|What this graph plots: two copies of the t curve with 9 df. Top: two-tailed test at 5%, 0.025 in each tail beyond ±2.262. Bottom: right-tailed test at 5%, all 0.05 beyond 1.833. The green line is the nitrate t = 1.464 in both.|w=82]]

| test at α = 0.05, 9 df | critical region | table column to read |
|---|---|---|
| H₁: μ ≠ 12 | t < −2.262 or t > 2.262 | two-tailed 0.05 |
| H₁: μ > 12 | t > 1.833 | two-tailed 0.10 (= one-tailed 0.05) |
| H₁: μ < 12 | t < −1.833 | two-tailed 0.10 (= one-tailed 0.05) |

The one-tailed value at α equals the two-tailed value at 2α (G&K §12.7.2), because a two-tailed 0.10 leaves exactly 0.05 in each tail. Words that make a test one-tailed: "more than", "less than", "increased", "reduced", "improved", "a success".

**Answer to the Predict.** Smaller: **1.833**. The nitrate t = 1.464 is still below it, so even the one-sided test does not reject: no evidence of too much nitrate.

:::check Check 4
Suppose the ten bags had averaged 12.7 kg with the same s = 1.0801. (a) Find t. (b) Decide against H₁: μ > 12 and against H₁: μ ≠ 12, both at 5%.
:::

### 5 · Two independent samples

Steps 1–4 compared one sample with a stated number. Often there is no stated number, only two groups: two classes, two diets, two machines. The question becomes whether their means differ.

:::q <span class="tag">A5 C2(a)</span>
A random sample of 12 students from Class A has mean score 68 and sum of squares of deviations from the mean 220. A sample of 10 students from Class B has mean 62 and sum of squares of deviations 180. Test whether there is a significant difference between the mean scores of the two classes at the 5% level.
:::

:::guess Guess first
The averages differ by 6 marks. Guess the SE of that difference: about 1, 2 or 5 marks?
:::

:::note Terms
**x̄₁ − x̄₂:** the gap between the two sample averages; under H₀: μ₁ = μ₂ its average over many pairs of samples is 0. **S² (pooled variance):** one estimate of the common σ² from both groups: all squared deviations (each from its own group's average) added, divided by n₁ + n₂ − 2. **df = n₁ + n₂ − 2:** each group loses one df to its own average.
:::

[[fig:class_curves|What this graph plots: the two classes' scores as two bell curves (horizontal axis: score; height: share of students near that score), centred on the sample averages 62 and 68, both with the pooled SD √20 = 4.47 marks. The gap between the centres is the 6 marks being tested.|w=80]]

| class | n | x̄ | Σ(x − x̄)² | s² = Σ(x − x̄)²/(n − 1) |
|---|---|---|---|---|
| A | 12 | 68 | 220 | 20 |
| B | 10 | 62 | 180 | 20 |

$$S^{2} = \frac{Σ(x_{1} − x̄_{1})^{2} + Σ(x_{2} − x̄_{2})^{2}}{n_{1} + n_{2} − 2},    t = \frac{x̄_{1} − x̄_{2}}{S√(1/n_{1} + 1/n_{2})},    df = n_{1} + n_{2} − 2$$

Read in words: t = (gap between the averages) ÷ (SE of that gap); the SE uses the pooled S and both sample sizes (G&K §14.2.10).

**Assumptions** (G&K §14.2.10, remark 3): (i) both populations normal; (ii) equal, unknown variances; (iii) the two samples random and independent of each other. File 14 tests (ii).

**Answer to the question.**

1. H₀: μ_{A} = μ_{B}; H₁: μ_{A} ≠ μ_{B} (two-tailed: "a difference").
2. S² = (220 + 180)/(12 + 10 − 2) = 400/20 = **20**.
3. SE = √(20 × (1/12 + 1/10)) = √(20 × 0.18333) = √3.6667 = **1.9149**.
4. t = (68 − 62)/1.9149 = **3.133**, df = 20.
5. t₀.₀₅ for 20 df = **2.086** (the assignment prints no table value; this is the t table's entry). 3.133 > 2.086: **reject H₀**. The two classes' mean scores differ significantly.

Answer to the guess: about 2 (1.91).

:::check Check 5
Two samples: n₁ = 8, x̄₁ = 15, s₁² = 4; n₂ = 8, x̄₂ = 13, s₂² = 5 (both s² with n − 1). Test equality of means at 5% (t₀.₀₅ for 14 df = 2.145). Hint: Σ(x − x̄)² = (n − 1)s².
:::

### 6 · An interval for μ₁ − μ₂

Step 5 said the classes differ. Part (b) asks by how much: file 11's interval idea, applied to the difference.

:::q <span class="tag">A5 C2(b)</span>
Obtain the 95% confidence interval for the difference between the two population means.
:::

:::guess Guess first
Will the interval contain 0? Use step 5's decision to guess.
:::

[[fig:diff_ci|What this graph plots: a number line for μ_{A} − μ_{B} in marks. The dot is the sample difference 6; the bar is the 95% interval 2.006 to 9.994; the dashed line marks 0, "no difference", which lies outside the bar.|w=78]]

$$(x̄_{1} − x̄_{2}) ± t_{0.05} × S√(1/n_{1} + 1/n_{2})$$

In words: the sample difference, plus or minus (table t for n₁ + n₂ − 2 df) × (SE of the difference): the same shape as file 11's x̄ ± t × SE.

**Answer to the question.**

1. Difference 68 − 62 = 6; SE = 1.9149 (step 5); t₀.₀₅ for 20 df = 2.086.
2. Margin = 2.086 × 1.9149 = 3.994.
3. Interval: 6 ± 3.994 = **(2.006, 9.994)** marks.
4. 0 is outside the interval, which matches step 5's rejection of μ_{A} = μ_{B} at 5%: a two-tailed test at α rejects exactly when the (1 − α) interval misses the H₀ value.

:::check Check 6
Find the 99% interval for the same difference (t₀.₀₁ for 20 df = 2.845). Does it contain 0? What does that say about the test at 1%?
:::

### 7 · Paired samples

Step 5's groups were different students. When the **same** units are measured twice (each shop before and after), the two lists are linked, and step 5's formula throws that link away.

:::q <span class="tag">A5 C4</span>
The sales of an item in six shops before and after a special promotional campaign: A 53 → 58, B 28 → 29, C 31 → 30, D 48 → 55, E 50 → 56, F 42 → 45. Can the campaign be judged a success? Test at the 5% level. (Tabulated value 2.02.)
:::

:::guess Guess first
"A success" means sales went up. One-tailed or two-tailed? And which matters more: the big gap between shops (28 to 58) or each shop's own change?
:::

:::note Terms
**d:** one unit's change, after − before (shop A: 58 − 53 = 5). **d̄:** the average change. **s_{d}:** the SD of the changes, with n − 1. H₀: μ_{d} = 0, the true average change is zero (G&K §14.2.10 remark 4: the changes are only sampling fluctuation).
:::

[[fig:paired_diff|What this graph plots: each shop's sales before (left) and after (right), joined by a line; green lines went up, red went down. Each label gives that shop's change d. The shops differ a lot from each other, but five of the six lines rise.|w=72]]

$$t = \frac{d̄}{s_{d}/√n},    df = n − 1  (n = number of pairs)$$

In words: the paired test is step 1's one-sample t applied to the list of changes, with μ₀ = 0.

**Answer to the question.**

1. H₀: μ_{d} = 0 (no effect); H₁: μ_{d} > 0 (sales rise: right-tailed). df = 6 − 1 = 5; one-tailed t₀.₀₅ = 2.015 (printed as 2.02).
2. d = 5, 1, −1, 7, 6, 3. Σd = 21, **d̄ = 3.5**.
3. Σd² = 25 + 1 + 1 + 49 + 36 + 9 = 121; Σ(d − d̄)² = 121 − 21²/6 = 121 − 73.5 = 47.5.
4. s_{d}² = 47.5/5 = 9.5; **s_{d} = 3.082**; SE = 3.082/√6 = 1.2583.
5. t = 3.5/1.2583 = **2.782** > 2.02: **reject H₀**. The campaign raised sales: a success at the 5% level.

Answer to the guess: one-tailed, and each shop's own change. Run step 5's two-sample test on the same numbers and t = 0.511: the 30-unit spread between shops buries the 3.5-unit rise. Pairing removes the shop-to-shop spread.

<span class="tag">A5 A2</span> The null hypothesis of a paired t-test: **μ_{d} = 0**, the population mean of the differences is zero.

:::note A5 A4's options
"A paired t-test on 15 subjects: mean difference 3.2, SD of differences 4.0. The t-value is: 1.55 / 2.10 / 3.00 / 3.87." Exact: t = 3.2/(4.0/√15) = 3.2/1.0328 = **3.098**. No option is exact; (C) 3.00 is the nearest. In the exam write 3.098 with the working, then mark (C).
:::

:::check Check 7
Five patients' blood pressure before → after a drug: 140 → 132, 150 → 148, 135 → 128, 160 → 150, 145 → 142. Test at 5% whether the drug lowers blood pressure (one-tailed t₀.₀₅ for 4 df = 2.132). Take d = before − after.
:::

---

## Exam form

| Test | When | H₀ | Statistic | df |
|---|---|---|---|---|
| One sample | one sample vs a stated μ₀, σ unknown | μ = μ₀ | t = (x̄ − μ₀)/(s/√n) | n − 1 |
| Two independent samples | two separate groups | μ₁ = μ₂ | t = (x̄₁ − x̄₂)/(S√(1/n₁ + 1/n₂)), S² = [Σ(x₁ − x̄₁)² + Σ(x₂ − x̄₂)²]/(n₁ + n₂ − 2) | n₁ + n₂ − 2 |
| Paired | same units measured twice | μ_{d} = 0 | t = d̄/(s_{d}/√n) | n − 1 (n pairs) |

**Interval for μ₁ − μ₂:** (x̄₁ − x̄₂) ± t_{α} × S√(1/n₁ + 1/n₂), t from the n₁ + n₂ − 2 row.

**Procedure** (12a step 8): H₀ → H₁ and its tails → α → statistic and df → compute (shift d = x − A for raw data) → table value (two-tailed column at α, or at 2α for one tail) → compare → conclusion in the question's words.

**Shortcut.** Σ(x − x̄)² = Σd² − (Σd)²/n for any shift d = x − A.

**Assumptions.** Normal population(s); σ unknown; random samples. Two samples: independent, equal variances (file 14). Paired: the same units, n pairs.

## Traps

- Running the two-sample test on paired data (before/after on the same shops): t drops from 2.782 to 0.511.
- df = n instead of n − 1; df = n₁ + n₂ − 1 instead of n₁ + n₂ − 2.
- A two-tailed table value for a one-tailed question ("increased", "reduced", "a success"): use the 2α column.
- Dividing a given Σ(x − x̄)² by n − 1 and then again by n₁ + n₂ − 2: add the two sums first, divide once.
- Writing "H₀ is true" instead of "no significant evidence against H₀".

## Self-test

1. Write the one-sample, two-sample and paired t statistics with their df.
2. List the three assumptions of the two-sample t-test.
3. n = 25, x̄ = 52, s = 5. Test H₀: μ = 50 against μ ≠ 50 at 5% (t₀.₀₅ for 24 df = 2.064).
4. n₁ = n₂ = 6, Σ(x₁ − x̄₁)² = 30, Σ(x₂ − x̄₂)² = 20, x̄₁ − x̄₂ = 3. Find t and its df.
5. When is a paired test used instead of a two-sample test?
6. A paired test on 10 pairs gives d̄ = 1.2, s_{d} = 1.5. Find t and decide at 5% two-tailed (t₀.₀₅ for 9 df = 2.262).
7. For 9 df, which table value does a right-tailed test at 5% use, and why is it smaller than 2.262?

<!--ANSWERS-->
## Answers

**Check 1.** SE = 6/√16 = 1.5; t = (41.5 − 44)/1.5 = **−1.667**; 1.667 < 2.131: do not reject H₀.

**Check 2.** H₀: μ = 50 kg; H₁: μ ≠ 50 kg. d = x − 48: 2, 1, −4, 4, −3, 0, −2, −3, 1, −3; Σd = −7, Σd² = 69. x̄ = 48 − 0.7 = **47.3**; Σ(x − x̄)² = 69 − 49/10 = 64.1; s² = 64.1/9 = 7.122, s = **2.669**; SE = 2.669/√10 = 0.8439. t = (47.3 − 50)/0.8439 = **−3.199**; 3.199 > 2.262: **reject H₀**. The average packing cannot be taken as 50 kg.

**Check 3.** 5%: 2.5 > 2.093, reject. 1%: 2.5 < 2.861, do not reject.

**Check 4.** (a) t = (12.7 − 12)/0.34157 = **2.049**. (b) H₁: μ > 12: 2.049 > 1.833, **reject**. H₁: μ ≠ 12: 2.049 < 2.262, **do not reject**. The one-sided test is more sensitive in the direction it looks.

**Check 5.** Σ(x − x̄)² = 7 × 4 = 28 and 7 × 5 = 35; S² = 63/14 = 4.5; SE = √(4.5 × (1/8 + 1/8)) = 1.0607; t = 2/1.0607 = **1.886** < 2.145: do not reject H₀.

**Check 6.** Margin = 2.845 × 1.9149 = 5.448; interval 6 ± 5.448 = **(0.552, 11.448)**. It does not contain 0, so the two-tailed test also rejects μ_{A} = μ_{B} at 1% (t = 3.133 > 2.845).

**Check 7.** H₀: μ_{d} = 0; H₁: μ_{d} > 0 (pressure falls). d = 8, 2, 7, 10, 3; d̄ = 30/5 = 6; Σ(d − d̄)² = 4 + 16 + 1 + 16 + 9 = 46; s_{d}² = 46/4 = 11.5, s_{d} = 3.391. t = 6/(3.391/√5) = **3.956** > 2.132: **reject H₀**. The drug lowers blood pressure.

**Self-test.**

1. See Exam form.
2. Both populations normal; equal, unknown variances; samples random and independent.
3. SE = 5/√25 = 1; t = (52 − 50)/1 = **2** < 2.064: do not reject.
4. S² = (30 + 20)/10 = 5; SE = √(5 × (1/6 + 1/6)) = 1.291; t = 3/1.291 = **2.324**, df = 10.
5. When each value in one sample is matched with one in the other: the same unit before and after, twins, matched pairs.
6. t = 1.2/(1.5/√10) = **2.530** > 2.262: reject.
7. 1.833, the two-tailed 10% entry: the whole 0.05 sits in one tail, so the boundary moves inward.
<!--/ANSWERS-->
