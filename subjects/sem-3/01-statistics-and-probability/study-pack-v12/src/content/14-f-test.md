# 14 — F-test for equality of two variances

<div class="sub">Gupta & Kapoor §14.5.5 (F-test for equality of population variances; remark 1: larger variance on top; remark 2: right-tail critical values; two-tailed rule), §14.2.10 remark 3 (F before the two-sample t) · blueprint row 5 "F-test" · 6 real questions (A5 A5, B2, B3, C5, D1; C2 as the link) · needs 08 (s² with n − 1, step 5), 12a (H₀, H₁, tails, steps of a test: steps 2–4, 8), 13 (shift d = x − A, step 2; pooled t, step 5)</div>

## Map

[[map:1 Comparing two spreads: the F ratio > 2 Which on top, and the df order > 3 F from sums of squares > 4 Two-tailed F from given SDs > 5 F from raw data > 6 F before the two-sample t|here=1]]

File 13 compared **averages**. Its two-sample test (step 5) pooled the two groups' variances into one S², which only makes sense if the two populations have the same spread. This file tests that: is one population more variable than the other? The statistic is a ratio of the two variance estimates, F, read from an F table. File 16 (ANOVA) uses the same F table to compare three or more means.

| Symbol | What it means in this file | Typical value |
|---|---|---|
| S₁², S₂² | the two samples' variance estimates: Σ(x − x̄)²/(n − 1) for each | 16, 14 |
| σ₁², σ₂² | the two populations' true variances; H₀: σ₁² = σ₂² | unknown |
| F | S₁²/S₂² with the larger estimate on top: how many times bigger one spread is | 1.143 |
| ν₁, ν₂ | df of the top and of the bottom estimate: n − 1 of each sample, top first | (7, 10) |
| F_{α}(ν₁, ν₂) | table value: the F with area α to its right on the F(ν₁, ν₂) curve | F₀.₀₅(7, 10) = 3.14 |

**Running example.** A5 C5: sample 1 has **8 values with Σ(x − x̄)² = 112**, sample 2 has **11 values with Σ(x − x̄)² = 140**. So S₁² = 16, S₂² = 14, **F = 1.143 with (7, 10) df**, table value 3.14. Steps 2–3 use it.

## The questions this file answers

- <span class="tag">A5 A5 · 2 marks</span> Two independent normal populations give sample variances 81 and 25 with sample sizes 10 and 12. The calculated F-statistic is: 1.80 / 2.50 / 3.24 / 5.60.
- <span class="tag">A5 C5</span> 8 observations with Σ(x − x̄)² = 112; 11 observations with Σ(x − x̄)² = 140. Test at 5% whether the two populations have the same variance. (F₀.₀₅(7, 10) ≈ 3.14.)
- <span class="tag">A5 B2, B3</span> Hotel room rates: 13 rooms with SD $27.50, 16 rooms with SD $29.75. State H₀ and H₁; can the agency's claim of equal SDs be rejected at α = 0.01? (Table value 4.72.)
- <span class="tag">A5 D1</span> Heat capacity of coal (millions of calories per ton), Mine 1: 8260, 8130, 8350, 8070, 8340; Mine 2: 7950, 7890, 7900, 8140, 7920. Can the two population variances be taken as equal? (Table value 5.19.)

---

## Build

### 1 · Comparing two spreads: the F ratio

Two machines fill bags to the same average, but one machine's bags vary far more. To compare spreads, compare variances, and the natural comparison is "how many times bigger".

:::q <span class="tag">A5 A5 · 2 marks</span>
Two independent normal populations have sample variances 81 and 25, with sample sizes 10 and 12. The calculated F-statistic is: (A) 1.80 (B) 2.50 (C) 3.24 (D) 5.60
:::

:::guess Guess first
If the two populations had the same variance, what number would the ratio of the two sample variances be near?
:::

:::note Terms
**S²:** a sample's variance estimate, the squared deviations from its own average divided by n − 1 (08 step 5). **F = S₁²/S₂²:** how many times larger one estimate is than the other. Under H₀: σ₁² = σ₂², F varies around 1 from sample to sample. **F(ν₁, ν₂) curve:** the spread of that ratio over many pairs of samples when H₀ is true; ν₁ = n − 1 of the top sample, ν₂ = n − 1 of the bottom sample (G&K §14.5.5).
:::

[[fig:two_spreads|What this graph plots: the two populations as bell curves with the same centre. Horizontal axis: the measured value; height: share of values near it. Wide curve: SD 9 (variance 81); narrow curve: SD 5 (variance 25). F compares the variances, 81/25 = 3.24, not the SDs, 9/5 = 1.8.|w=78]]

| S₁² | S₂² | F = S₁²/S₂² | reads as |
|---|---|---|---|
| 25 | 25 | 1 | same spread |
| 50 | 25 | 2 | top sample twice as variable |
| 81 | 25 | 3.24 | A5 A5 |

$$F = \frac{S_{1}^{2}}{S_{2}^{2}},    S_{i}^{2} = \frac{Σ(x − x̄)^{2}}{n_{i} − 1},    df = (n_{1} − 1, n_{2} − 1)$$

In words: F = (larger variance estimate) ÷ (smaller variance estimate); the df pair is (top sample's n − 1, bottom sample's n − 1).

**Answer to the question.** F = 81/25 = **3.24**, option **(C)**, with df (10 − 1, 12 − 1) = (9, 11). Option (A) 1.80 is the trap: 9/5, the ratio of the SDs. Answer to the guess: near 1.

:::check Check 1
Sample variances 12 (n = 7) and 30 (n = 9). Write F and its df.
:::

### 2 · Which on top, and the df order

Step 1 put the larger variance on top. That choice fixes which table value to read, and the df pair must follow it.

:::q Predict
The 5% table value for F(7, 10) is 3.14. Is the 5% value for F(10, 7), the same two df swapped, also 3.14?
:::

:::guess Guess first
Same, smaller or larger?
:::

[[fig:f_df_order|What this graph plots: two F curves. Horizontal axis: the value of F; height: how often pairs of samples give an F near that value when the variances are equal. Blue: F(7, 10), 5% right tail beyond 3.14. Orange: F(10, 7), 5% right tail beyond 3.64. Swapping the df moves the critical value.|w=82]]

| df (ν₁, ν₂) | 5% table value | 1% table value |
|---|---|---|
| (7, 10) | 3.14 | 3.95 |
| (10, 7) | 3.64 | 6.62 |
| (4, 4) | 6.39 | 15.98 |
| (4, 5) | 5.19 | 11.39 |

**The two rules** (G&K §14.5.5, remarks 1–2):

1. The **greater** of the two variance estimates goes in the numerator, so F ≥ 1.
2. The F tables give **right-tail** critical values F_{α}(ν₁, ν₂), with P(F > F_{α}) = α; ν₁ is the df of the numerator's sample.

Putting the larger on top means only the right tail is ever needed; ν₁ then belongs to the sample with the larger S².

**Answer to the Predict.** Larger: F₀.₀₅(10, 7) = **3.64**, not 3.14. The df order matters; reading (ν₂, ν₁) gives a wrong boundary. Step 5 shows an assignment key that did this.

:::check Check 2
Sample 1: n = 13, S² = 756. Sample 2: n = 16, S² = 885. Which goes on top, and which df pair does the table need?
:::

### 3 · F from sums of squares

Most questions give Σ(x − x̄)², not the variance. Divide each by its own n − 1 first, then compare.

:::q <span class="tag">A5 C5</span>
In one sample of 8 observations from a normal population, the sum of squares of deviations from the sample mean is 112. In another sample of 11 observations it is 140. Test at the 5% level whether the two populations have the same variance. (F₀.₀₅(7, 10) ≈ 3.14.)
:::

:::guess Guess first
112 is smaller than 140. Which sample has the larger variance estimate?
:::

[[fig:f_curve|What this graph plots: the F curve with (7, 10) df, the spread of F when the two population variances are equal. The red right tail beyond 3.14 holds 5%: the critical region. The green line is A5 C5's F = 1.143, far from the tail.|w=82]]

| F | share of F(7, 10) values above it |
|---|---|
| 1.143 (A5 C5) | 0.410 |
| 2 | 0.155 |
| 3.14 (table value) | 0.05 |

**Answer to the question.**

1. H₀: σ₁² = σ₂²; H₁: σ₁² ≠ σ₂².
2. S₁² = 112/(8 − 1) = **16**; S₂² = 140/(11 − 1) = **14**.
3. The first is larger, so F = 16/14 = **1.143**, df (7, 10).
4. 1.143 < 3.14: **do not reject H₀**. The two populations can be taken to have the same variance.

Answer to the guess: sample 1. Its smaller sum is divided by fewer df (7 instead of 10).

:::check Check 3
n₁ = 10 with Σ(x − x̄)² = 90; n₂ = 13 with Σ(x − x̄)² = 108. Find F and its df, and decide at 5% (F₀.₀₅(9, 12) = 2.80).
:::

### 4 · Two-tailed F from given SDs

"The SDs are the same" is broken by either city being more variable, so H₁ is two-sided (12a step 4). With the larger variance on top, the left tail never comes into play; the whole test uses the right tail at **α/2**.

:::q <span class="tag">A5 B3</span>
A travel agency's brochure says the standard deviations of hotel room rates in two cities are the same. A random sample of 13 room rates in one city has SD $27.50 and a random sample of 16 rates in the other city has SD $29.75. Can you reject the agency's claim at α = 0.01? (Tabulated value 4.72.)
:::

:::guess Guess first
The SDs differ by about 8%. Guess F, then guess whether it gets near 4.72.
:::

| two-tailed α | upper point needed | F(15, 12) table value |
|---|---|---|
| 0.10 | F₀.₀₅ | 2.62 |
| 0.05 | F₀.₀₂₅ | 3.18 |
| 0.01 | F₀.₀₀₅ | 4.72 |

G&K §14.5.5: the two-tailed test of σ₁² = σ₂² rejects if F > F_{α/2}(ν₁, ν₂) or F < F_{1−α/2}(ν₁, ν₂). With the larger estimate on top F ≥ 1 and the second condition cannot hold, so only F_{α/2} is compared.

**Answer to the question.**

1. H₀: σ₁ = σ₂ (the agency's claim); H₁: σ₁ ≠ σ₂ (two-tailed). This is <span class="tag">A5 B2</span>'s answer.
2. Reading the given SDs as s (n − 1 divisor): 29.75² = 885.06 (n = 16) and 27.50² = 756.25 (n = 13).
3. Larger on top: F = 885.06/756.25 = **1.170**, df (15, 12).
4. Two-tailed at α = 0.01 needs the upper α/2 = 0.005 point: F₀.₀₀₅(15, 12) = **4.72**, the printed value.
5. 1.170 < 4.72: **do not reject H₀**. The data give no reason to reject the agency's claim.

Answer to the guess: F = 1.17, nowhere near 4.72. An 8% gap in SDs is a 17% gap in variances, and with 13 and 16 values that is ordinary sampling variation.

:::check Check 4
If the question had asked at α = 0.10 (two-tailed), which table point would you need, and would the decision change?
:::

### 5 · F from raw data

The 8-mark form: compute both variances from the data, then step 3.

:::q <span class="tag">A5 D1</span>
Heat-producing capacity of coal from two mines (millions of calories per ton): Mine 1: 8260, 8130, 8350, 8070, 8340. Mine 2: 7950, 7890, 7900, 8140, 7920. Can it be concluded that the two population variances are equal? (Tabulated value 5.19.)
:::

:::guess Guess first
Mine 1 runs from 8070 to 8350, Mine 2 from 7890 to 8140. Which variance is larger, and is F near 1, 2 or 5?
:::

[[fig:coal_dots|What this graph plots: each mine's five measurements as dots on one axis of heat capacity (millions of calories per ton); the tick on each row marks that mine's average (8230 and 7960). Mine 1's dots are more spread out.|w=78]]

Shift and scale so the numbers stay small: u = (x − 8000)/10. Dividing by 10 divides the variance by 100, so multiply back by 100 at the end (13 step 2's shift, plus a scale).

| | u values | Σu | Σu² | Σ(u − ū)² = Σu² − (Σu)²/5 |
|---|---|---|---|---|
| Mine 1 | 26, 13, 35, 7, 34 | 115 | 3275 | 3275 − 2645 = 630 |
| Mine 2 | −5, −11, −10, 14, −8 | −20 | 506 | 506 − 80 = 426 |

**Answer to the question.**

1. H₀: σ₁² = σ₂²; H₁: σ₁² ≠ σ₂².
2. S₁² = 630/4 × 100 = **15,750**; S₂² = 426/4 × 100 = **10,650**. (x̄₁ = 8230, x̄₂ = 7960.)
3. F = 15,750/10,650 = **1.479**, df (4, 4).
4. The correct table values: F₀.₀₅(4, 4) = **6.39**; for a two-tailed 5% test F₀.₀₂₅(4, 4) = 9.60.
5. 1.479 is below both: **do not reject H₀**. The two variances can be taken as equal.

:::note Table value slip (A5 D1)
The assignment prints 5.19, which is F₀.₀₅(4, **5**). Five values in each mine give (4, 4) df, and F₀.₀₅(4, 4) = **6.39** (two-tailed 5%: 9.60). Here the decision is the same with any of these values; the pack uses 6.39.
:::

Answer to the guess: Mine 1, and F ≈ 1.5. Mine 1's SD (125.5) is about 22% above Mine 2's (103.2); squaring makes it about 48%.

:::check Check 5
Sample A = 2, 4, 6; sample B = 1, 5, 9. Find F and its df, and decide at 5% (F₀.₀₅(2, 2) = 19.0).
:::

### 6 · F before the two-sample t

File 13 step 5's pooled S² assumed the two classes have equal variances. G&K §14.2.10 remark 3: before applying the t-test for equality of means it is "theoretically desirable" to test the equality of the population variances by the F-test; if they are unequal, the pooled t-test is not valid.

:::q <span class="tag">A5 C2 (link)</span>
In file 13's class-score question, Class A had Σ(x − x̄)² = 220 with n = 12, Class B 180 with n = 10. Was the pooled t-test justified?
:::

:::guess Guess first
Compute the two variance estimates in your head first. Equal, or not?
:::

| class | n | Σ(x − x̄)² | S² |
|---|---|---|---|
| A | 12 | 220 | 220/11 = 20 |
| B | 10 | 180 | 180/9 = 20 |

**Answer to the question.** S_{A}² = 20 and S_{B}² = 20, so F = 20/20 = **1.00**, the value equal variances predict. Nothing to reject: the pooled t-test was justified.

The order in a two-sample exam question: (1) F-test on the variances; (2) if not rejected, pool them and run the t-test (13 step 5).

:::check Check 6
Two samples give S₁² = 50 (n = 6) and S₂² = 8 (n = 6). F₀.₀₅(5, 5) = 5.05. Should the pooled t-test be used?
:::

---

## Exam form

**Statement** (G&K §14.5.5). For two independent random samples from normal populations, under H₀: σ₁² = σ₂²,
F = S₁²/S₂², with Sᵢ² = Σ(x − x̄)²/(nᵢ − 1) and the larger estimate on top, follows the F distribution with (n₁ − 1, n₂ − 1) df (numerator's sample first).

**Procedure.**

1. H₀: σ₁² = σ₂²; H₁: σ₁² ≠ σ₂² (or one-sided).
2. Both variance estimates: Σ(x − x̄)²/(n − 1). From SDs: square them. From raw data: shift (and scale) first.
3. Larger on top; df = (n − 1 of the top sample, n − 1 of the bottom sample).
4. Table value: F_{α}(ν₁, ν₂) for a one-sided H₁, F_{α/2}(ν₁, ν₂) for H₁: σ₁² ≠ σ₂².
5. F below the table value: the variances can be taken as equal; above: they differ.

**Assumptions.** Normal populations; independent random samples.

**Use.** Run it before the pooled two-sample t-test (13 step 5), which assumes equal variances.

## Traps

- The ratio of SDs instead of variances (A5 A5's option 1.80 = 9/5).
- The smaller variance on top (F < 1: the right-tail table no longer applies).
- Swapped df: ν₁ goes with the numerator's sample (F₀.₀₅(10, 7) = 3.64, F₀.₀₅(7, 10) = 3.14).
- Treating Σ(x − x̄)² as the variance: divide by n − 1 first.
- A two-tailed question compared with F_{α} instead of F_{α/2}.

## Self-test

1. Write the F statistic for two variances and its df.
2. Why is the larger variance put in the numerator?
3. S₁² = 24 (n = 11), S₂² = 15 (n = 16). Find F and its df; decide at 5% with F₀.₀₅(10, 15) = 2.54.
4. Two SDs, 6 (n = 9) and 4 (n = 9). Find F.
5. For the coal data of step 5, test whether the two mines' mean heat capacities differ, using 13 step 5's pooled t at 5% (t₀.₀₅ for 8 df = 2.306).
6. Which test comes before the pooled two-sample t-test, and why?

<!--ANSWERS-->
## Answers

**Check 1.** Larger on top: F = 30/12 = **2.5**, df **(8, 6)** (the variance-30 sample has n = 9).

**Check 2.** 885 is larger, so sample 2 goes on top: F = 885/756 = 1.17 with df **(15, 12)**, not (12, 15).

**Check 3.** S₁² = 90/9 = 10; S₂² = 108/12 = 9; F = 10/9 = **1.111**, df **(9, 12)**. 1.111 < 2.80: do not reject; the variances can be taken as equal.

**Check 4.** α/2 = 0.05: the upper 0.05 point F₀.₀₅(15, 12) = 2.62. 1.170 < 2.62: no change, do not reject.

**Check 5.** S_{A}² = (4 + 0 + 4)/2 = 4; S_{B}² = (16 + 0 + 16)/2 = 16. B on top: F = 16/4 = **4**, df (2, 2). 4 < 19.0: do not reject.

**Check 6.** F = 50/8 = **6.25** > 5.05: the variances differ, so the pooled t-test is **not** justified.

**Self-test.**

1. F = S₁²/S₂² with the larger on top, df (n₁ − 1, n₂ − 1), numerator's sample first.
2. So that F ≥ 1 and the right-tail F table applies (G&K §14.5.5 remark 1).
3. F = 24/15 = **1.6**, df (10, 15); 1.6 < 2.54: do not reject.
4. F = 36/16 = **2.25**, df (8, 8).
5. S² = (630 + 426) × 100/8 = 13,200; SE = √(13,200 × (1/5 + 1/5)) = 72.66; t = (8230 − 7960)/72.66 = **3.716** > 2.306: the mean heat capacities differ significantly. (Step 5's F-test allowed the pooling.)
6. The F-test, because the pooled t assumes equal population variances.
<!--/ANSWERS-->
