# 14 — F-test for equality of two variances

<div class="sub">Gupta & Kapoor §14.5, §14.5.5 · blueprint row 5 "F-test" · 6 real questions (Assignment 5) · needs 08 (s²), 12 (test steps), 13 (pooled t)</div>

## Map

[[map:1 The F ratio > 2 F from sums of squares > 3 F from given SDs, two-tailed > 4 F from raw data > 5 Why F comes before the two-sample t|here=1]]

## The questions this file answers

- <span class="tag">A5 A5 · 2 marks</span> Two independent normal populations give sample variances 81 and 25 with sample sizes 10 and 12. The calculated F-statistic is: 1.80 / 2.50 / 3.24 / 5.60.
- <span class="tag">A5 C5</span> 8 observations with Σ(x − x̄)^{2} = 112; 11 observations with Σ = 140. Do the two populations have the same variance at 5%? (F₀.₀₅(7, 10) ≈ 3.14.)
- <span class="tag">A5 B2, B3</span> Hotel room rates: 13 rooms with SD $27.50, 16 rooms with SD $29.75. State H₀ and H₁; can the agency's claim of equal SDs be rejected at α = 0.01? (Table value 4.72.)
- <span class="tag">A5 D1</span> Heat capacity of coal (millions of calories per ton), Mine 1: 8260, 8130, 8350, 8070, 8340; Mine 2: 7950, 7890, 7900, 8140, 7920. Are the population variances equal? (Table value 5.19.)

---

## Build

### 1 · The F ratio

File 13's two-sample t assumed equal variances. The F-test checks that assumption.

:::q <span class="tag">A5 A5 · 2 marks</span>
Two independent normal populations have sample variances 81 and 25, with sample sizes 10 and 12. The calculated F-statistic is: (A) 1.80 (B) 2.50 (C) 3.24 (D) 5.60
:::

:::guess Guess first
If the two population variances are equal, what value should the ratio of sample variances be near?
:::

**Terms** (G&K §14.5, §14.5.5):

- **F-distribution** with (ν₁, ν₂) df: the distribution of the ratio of two independent variance estimates from normal populations with the same σ^{2}. Values are ≥ 0, right-skewed, centred near 1.
- **F-test for equality of variances**, H₀: σ₁^{2} = σ₂^{2}:

$$F = \frac{S_{1}^{2}}{S_{2}^{2}},  S_{1}^{2} ≥ S_{2}^{2},    S_{i}^{2} = \frac{Σ(x − x̄)^{2}}{n_{i} − 1},    df = (n_{1} − 1, n_{2} − 1)$$

The **larger** variance goes in the numerator (G&K remark 1), so F ≥ 1 and only the right-tail table is needed. ν₁ belongs to the numerator's sample.

**Answer.** F = 81/25 = **3.24** (C), with df (9, 11).

:::check Check 1
Sample variances 12 (n = 7) and 30 (n = 9). Write F and its df.
:::

### 2 · F from sums of squares

Most questions give Σ(x − x̄)^{2}, not the variance. Divide by n − 1 first.

:::q <span class="tag">A5 C5</span>
In one sample of 8 observations from a normal population, the sum of squares of deviations from the sample mean is 112. In another sample of 11 observations it is 140. Test at the 5% level whether the two populations have the same variance. (F₀.₀₅(7, 10) ≈ 3.14.)
:::

:::guess Guess first
112 is less than 140. Which sample has the larger variance estimate?
:::

**Answer.** H₀: σ₁^{2} = σ₂^{2}; H₁: σ₁^{2} ≠ σ₂^{2}.
S₁^{2} = 112/7 = **16**; S₂^{2} = 140/10 = **14**. The first is larger, so F = 16/14 = **1.143**, df (7, 10).
1.143 < 3.14 ⇒ **do not reject H₀**: the variances can be taken as equal.
(The smaller sum, 112, gave the larger variance because it is divided by fewer df.)

[[fig:f_curve|F(7, 10): only an F beyond 3.14 would reject equal variances.|w=72]]

:::check Check 2
n₁ = 10 with Σ(x − x̄)^{2} = 90; n₂ = 13 with Σ = 108. Find F and its df.
:::

### 3 · F from given SDs, two-tailed

H₁: σ₁ ≠ σ₂ is two-tailed, but with the larger variance on top only the upper tail is used, at α/2.

:::q <span class="tag">A5 B3</span>
A travel agency's brochure says the standard deviations of hotel room rates in two cities are the same. A random sample of 13 room rates in one city has SD $27.50 and a sample of 16 rates in the other city has SD $29.75. Can you reject the agency's claim at α = 0.01? (Tabulated value 4.72.)
:::

:::guess Guess first
The SDs differ by about 8%. Guess F before computing it.
:::

**Answer.** H₀: σ₁ = σ₂ (claim); H₁: σ₁ ≠ σ₂.
Treating the given SDs as s (n − 1 divisor): larger variance 29.75^{2} = 885.06 (n = 16), smaller 27.50^{2} = 756.25 (n = 13).
F = 885.06/756.25 = **1.170**, df (15, 12).
Two-tailed at α = 0.01 ⇒ upper α/2 = 0.005 point: F₀.₀₀₅(15, 12) = **4.72** (the table value given).
1.170 < 4.72 ⇒ **do not reject H₀**: no evidence against the agency's claim.

<span class="tag">A5 B2</span> asks only for the hypotheses: H₀: σ₁ = σ₂, H₁: σ₁ ≠ σ₂.

:::check Check 3
If the question had said α = 0.10, two-tailed, which table point would you need? (Name it; F₀.₀₅(15, 12) = 2.62.) Would the decision change?
:::

### 4 · F from raw data

The 8-mark form: compute both variances from data.

:::q <span class="tag">A5 D1</span>
Heat-producing capacity of coal from two mines (millions of calories per ton): Mine 1: 8260, 8130, 8350, 8070, 8340. Mine 2: 7950, 7890, 7900, 8140, 7920. Can it be concluded that the two population variances are equal? (Tabulated value 5.19.)
:::

:::guess Guess first
Look at the spreads: Mine 1 runs 8070–8350, Mine 2 runs 7890–8140. Which variance is larger?
:::

**Answer.** Shift and scale to keep numbers small: u = (x − 8000)/10.
Mine 1: u = 26, 13, 35, 7, 34; Σu = 115, ū = 23; Σu^{2} = 676 + 169 + 1225 + 49 + 1156 = 3275; Σ(u − ū)^{2} = 3275 − 115^{2}/5 = 630. S₁^{2} = 630/4 × 100 = **15,750**. (x̄₁ = 8230.)
Mine 2: u = −5, −11, −10, 14, −8; Σu = −20, ū = −4; Σu^{2} = 25 + 121 + 100 + 196 + 64 = 506; Σ(u − ū)^{2} = 506 − 80 = 426. S₂^{2} = 426/4 × 100 = **10,650**. (x̄₂ = 7960.)
F = 15,750/10,650 = **1.479**, df (4, 4).
1.479 is below every critical value of F(4, 4) used here ⇒ **do not reject H₀**: the variances can be taken as equal.

:::note Table value slip
The assignment's 5.19 is F₀.₀₅(4, **5**). With 5 and 5 observations the df are (4, 4): F₀.₀₅(4, 4) = **6.39** (two-tailed 5%: F₀.₀₂₅(4, 4) = 9.60). The decision is the same with any of these values.
:::

:::check Check 4
For the coal data, are the two means significantly different? Use file 13's pooled t at 5% (t₀.₀₅,₈ = 2.306).
:::

### 5 · Why F comes before the two-sample t

:::q <span class="tag">A5 C2 (link)</span>
In file 13's class-score question, Class A had Σ(x − x̄)^{2} = 220 with n = 12, Class B 180 with n = 10. Was the pooled t-test justified?
:::

:::guess Guess first
Compute the two variance estimates before deciding.
:::

The pooled two-sample t (file 13 step 4) assumes σ₁^{2} = σ₂^{2}. Gupta & Kapoor (§14.2.10, remark 3): "before applying the t-test for the equality of means it is theoretically desirable to test the equality of population variances by applying the F-test."

**Answer.** S_{A}^{2} = 220/11 = 20; S_{B}^{2} = 180/9 = 20. F = 20/20 = **1.00**: perfectly consistent with equal variances, so the pooled t was justified.

:::check Check 5
Two samples give S₁^{2} = 50 (n = 6) and S₂^{2} = 8 (n = 6). F₀.₀₅(5, 5) = 5.05. Should the pooled t-test be used?
:::

---

## Exam form

**Statement.** To test H₀: σ₁^{2} = σ₂^{2} for two independent normal samples:
F = S₁^{2}/S₂^{2} with S₁^{2} ≥ S₂^{2}, Sᵢ^{2} = Σ(x − x̄)^{2}/(nᵢ − 1), which follows F(n₁ − 1, n₂ − 1) under H₀.

**Procedure.**

1. H₀: σ₁^{2} = σ₂^{2}; H₁: σ₁^{2} ≠ σ₂^{2} (or one-sided).
2. Compute both S^{2} (divide sums of squares by n − 1).
3. Put the larger on top; df = (n − 1 of the numerator sample, n − 1 of the denominator sample).
4. Compare with F_{α}(ν₁, ν₂) (one-sided) or F_{α/2}(ν₁, ν₂) (two-sided).
5. F < table ⇒ variances may be taken as equal.

**Assumptions.** Normal populations; independent random samples.

## Traps

- Putting the smaller variance on top (F < 1, wrong tail).
- Swapping the df: ν₁ goes with the numerator sample.
- Using Σ(x − x̄)^{2} directly as the variance: divide by n − 1 first.
- Using n instead of n − 1 for the df.

## Self-test

1. Write the F statistic for two variances and its df.
2. Why is the larger variance put in the numerator?
3. S₁^{2} = 24 (n = 11), S₂^{2} = 15 (n = 16). Find F and df; decide at 5% with F₀.₀₅(10, 15) = 2.54.
4. Samples: A = 2, 4, 6; B = 1, 5, 9. Find F.
5. Which test should come before the pooled two-sample t-test, and why?

<!--ANSWERS-->
## Answers

**Check 1.** F = 30/12 = **2.5**, df **(8, 6)**.

**Check 2.** S₁^{2} = 90/9 = 10; S₂^{2} = 108/12 = 9; F = **1.111**, df **(9, 12)**.

**Check 3.** The upper 0.05 point, F₀.₀₅(15, 12) = 2.62. 1.170 < 2.62: no change, do not reject.

**Check 4.** S^{2} = (630 + 426) × 100/8 = 13,200; SE = √(13,200 × 0.4) = 72.66; t = (8230 − 7960)/72.66 = **3.716** > 2.306 ⇒ the means differ significantly.

**Check 5.** F = 50/8 = 6.25 > 5.05: the variances differ, so the pooled t is **not** justified.

**Self-test.**

1. F = S₁^{2}/S₂^{2} (larger on top), df (n₁ − 1, n₂ − 1).
2. So that F ≥ 1 and the right-tail table applies.
3. F = 24/15 = **1.6**, df (10, 15); 1.6 < 2.54: do not reject.
4. S_{A}^{2} = 8/2 = 4; S_{B}^{2} = 32/2 = 16; F = 16/4 = **4**, df (2, 2).
5. The F-test, because the pooled t assumes equal population variances.
<!--/ANSWERS-->
