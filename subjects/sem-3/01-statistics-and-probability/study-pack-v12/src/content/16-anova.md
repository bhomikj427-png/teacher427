# 16 — Analysis of variance (one-way ANOVA)

<div class="sub">Gupta & Kapoor §14.5.11 ("F-test for equality of several means … by the technique of analysis of variance") · knowledge base (Walpole; Montgomery & Runger) · blueprint row 5 "Analysis of Variance (ANOVA)" · 4 real questions (Assignment 5) · needs 13, 14</div>

## Map

[[map:1 Why compare variances to compare means > 2 Sums of squares and the ANOVA table > 3 One-way ANOVA, equal groups > 4 One-way ANOVA, unequal groups|here=1]]

## The questions this file answers

- <span class="tag">A5 C6</span> Blood-pressure reduction under three techniques: medication 10, 12, 9, 15, 13; exercise 6, 8, 3, 0, 2; diet 5, 9, 12, 8, 4. Test at 5% whether the mean reductions differ. (Tabulated value given: 19.41.)
- <span class="tag">A5 D4</span> Annual household income (Rs 1000) in three areas: (1) 70, 72, 75, 80, 83; (2) 100, 110, 108, 112, 113, 120, 100; (3) 60, 65, 57, 84, 84, 70. Can the average incomes be considered the same at α = 0.01? (Tabulated value 6.36.)
- <span class="tag">A5 A9 · 2 marks</span> In one-way ANOVA with k groups and N observations, the df between and within groups are: k and N / k − 1 and N − k / N − 1 and k − 1 / N − k and N − 1.
- <span class="tag">A5 A10 · 2 marks</span> One-way ANOVA with SSB = 120, SSW = 180, k = 4, N = 24: the F-statistic is 4.00 / 5.00 / 6.00 / 8.00.

Assignment 5 lists the ANOVA topics as introduction, assumptions, classification and one-way ANOVA. Row 5 holds the paper's only Part D (8 marks); A5 D4 is the assignment's Part D version of this question.

---

## Build

### 1 · Why compare variances to compare means

File 13's t-test compares two means. With three or more groups, ANOVA does it in one test.

:::q Predict
Three blood-pressure techniques give group means 11.8, 3.8 and 7.6. Within each group the values scatter by a few units. What would convince you that the techniques really differ, and not just by chance?
:::

:::guess Guess first
Write one sentence comparing "spread between the group means" with "spread inside each group".
:::

**Terms.**

- **ANOVA (analysis of variance)**: a test of H₀: μ₁ = μ₂ = … = μₖ that splits the total variation of the data into parts with different causes.
- **Between-group variation**: how far the group means are from the grand mean (caused by the treatments if they differ).
- **Within-group (error) variation**: scatter of values around their own group mean (chance alone).

[[fig:anova_dots|Group means far apart compared with the scatter inside each group: evidence the means differ.|w=78]]

**Answer.** If the treatments have no effect, both variations estimate the same σ^{2} and their ratio F is near 1. A large F (between ≫ within) is evidence that the means differ.

**Assumptions:** each group comes from a normal population; all groups have the **same variance** σ^{2}; observations are independent.
**Classification:** **one-way** ANOVA (one factor, e.g. technique) and **two-way** ANOVA (two factors, e.g. technique and age group). This file covers one-way, as Assignment 5 does.

:::check Check 1
Why not run three separate t-tests (A–B, A–C, B–C) at 5% each instead of one ANOVA?
:::

### 2 · Sums of squares and the ANOVA table

The method needs three sums of squares and one table.

:::q <span class="tag">A5 A10 · 2 marks</span>
In one-way ANOVA, SSB = 120, SSW = 180, k = 4 groups and N = 24 observations. The calculated F-statistic is: (A) 4.00 (B) 5.00 (C) 6.00 (D) 8.00
:::

:::guess Guess first
Is F = 120/180? What has to be divided first?
:::

**Notation.** k groups; group i has nᵢ values with total Tᵢ; N = Σnᵢ; grand total G = ΣTᵢ.

$$CF = \frac{G^{2}}{N},    SST = Σx^{2} − CF,    SSB = Σ\frac{T_{i}^{2}}{n_{i}} − CF,    SSW = SST − SSB$$

CF is the correction factor; SST = SSB + SSW.

| Source | SS | df | MS = SS/df | F |
|---|---|---|---|---|
| Between groups | SSB | k − 1 | MSB | MSB/MSW |
| Within groups | SSW | N − k | MSW | |
| Total | SST | N − 1 | | |

Under H₀, F ~ F(k − 1, N − k); reject H₀ if F > F_{α}(k − 1, N − k).

<span class="tag">A5 A9</span> The df are **k − 1 and N − k** (B).

**Answer.** MSB = 120/3 = 40; MSW = 180/20 = 9; F = 40/9 = **4.44**.

:::note A5 A10's options
None of the options equals 4.44; (A) 4.00 is the nearest. Write F = MSB/MSW = 40/9 = 4.44 with the working.
:::

:::check Check 2
k = 3, N = 15, SSB = 60, SST = 150. Fill in the ANOVA table and find F.
:::

### 3 · One-way ANOVA, equal groups

:::q <span class="tag">A5 C6</span>
Three techniques (medication, exercises and special diet) are randomly assigned to individuals with high blood pressure. After four weeks the reduction in each person's blood pressure is recorded:

| Technique | Person 1 | Person 2 | Person 3 | Person 4 | Person 5 |
|---|---|---|---|---|---|
| Medication | 10 | 12 | 9 | 15 | 13 |
| Exercise | 6 | 8 | 3 | 0 | 2 |
| Diet | 5 | 9 | 12 | 8 | 4 |

Test at the 5% level whether there is a significant difference in mean reduction among the three techniques.
:::

:::guess Guess first
Guess F: near 1, near 3, or near 10?
:::

**Answer.** H₀: μ₁ = μ₂ = μ₃; H₁: not all equal. k = 3, n = 5 each, N = 15.
Totals: T₁ = 59, T₂ = 19, T₃ = 38; G = 116. CF = 116^{2}/15 = 13456/15 = 897.07.
Σx^{2} = (100 + 144 + 81 + 225 + 169) + (36 + 64 + 9 + 0 + 4) + (25 + 81 + 144 + 64 + 16) = 719 + 113 + 330 = 1162.
SST = 1162 − 897.07 = **264.93**. SSB = (59^{2} + 19^{2} + 38^{2})/5 − 897.07 = 5286/5 − 897.07 = 1057.2 − 897.07 = **160.13**. SSW = **104.80**.

| Source | SS | df | MS | F |
|---|---|---|---|---|
| Between | 160.13 | 2 | 80.07 | **9.17** |
| Within | 104.80 | 12 | 8.73 | |
| Total | 264.93 | 14 | | |

F₀.₀₅(2, 12) = **3.89**. 9.17 > 3.89 ⇒ **reject H₀**: the mean reductions differ (medication highest, x̄ = 11.8).

:::note Table value slip
Assignment 5 gives 19.41, which is F₀.₀₅(**12, 2**): the df reversed. The numerator df is k − 1 = 2 and the denominator df is N − k = 12, so the table value is F₀.₀₅(2, 12) = 3.89. With 19.41 the decision would wrongly be "do not reject".
:::

:::check Check 3
Three machines, 4 items each. Totals 40, 48, 56; Σx^{2} = 1840. Find SST, SSB, SSW and F.
:::

### 4 · One-way ANOVA, unequal groups

With unequal group sizes, each Tᵢ^{2} is divided by its own nᵢ.

:::q <span class="tag">A5 D4</span>
A department store chain compares average household incomes (Rs 1000) across three areas:
Area 1: 70, 72, 75, 80, 83 (total 380). Area 2: 100, 110, 108, 112, 113, 120, 100 (total 763). Area 3: 60, 65, 57, 84, 84, 70 (total 420).
Test if the average income per household in all these localities can be considered the same at α = 0.01. (Tabulated value 6.36.)
:::

:::guess Guess first
Area 2's incomes are all ≥ 100, the others mostly below 85. Reject or not?
:::

**Answer.** H₀: μ₁ = μ₂ = μ₃. n = 5, 7, 6; N = 18; G = 1563. CF = 1563^{2}/18 = 2,442,969/18 = 135,720.5.
Σx^{2} = 28,998 + 83,477 + 30,086 = 142,561 ⇒ SST = **6840.5**.
ΣTᵢ^{2}/nᵢ = 380^{2}/5 + 763^{2}/7 + 420^{2}/6 = 28,880 + 83,167 + 29,400 = 141,447 ⇒ SSB = **5726.5**. SSW = **1114.0**.

| Source | SS | df | MS | F |
|---|---|---|---|---|
| Between | 5726.5 | 2 | 2863.25 | **38.55** |
| Within | 1114.0 | 15 | 74.27 | |
| Total | 6840.5 | 17 | | |

F₀.₀₁(2, 15) = 6.36. 38.55 > 6.36 ⇒ **reject H₀**: average household income differs between the areas (Area 2 is highest, mean 109).

:::check Check 4
Recompute SSB for A5 D4 using the group means: SSB = Σnᵢ(x̄ᵢ − x̄)^{2}, with x̄ = 86.83.
:::

---

## Exam form

**Definition.** ANOVA splits total variation into between-group and within-group parts to test H₀: μ₁ = … = μₖ.

**Assumptions.** Normal populations; equal variances; independent random samples. **Classification:** one-way (one factor), two-way (two factors).

**Procedure (one-way).**

1. H₀: all means equal; H₁: at least two differ.
2. Tᵢ, nᵢ, G, N; CF = G^{2}/N.
3. SST = Σx^{2} − CF; SSB = ΣTᵢ^{2}/nᵢ − CF; SSW = SST − SSB.
4. MSB = SSB/(k − 1), MSW = SSW/(N − k), F = MSB/MSW.
5. Compare with F_{α}(k − 1, N − k); F larger ⇒ reject H₀.
6. Present the ANOVA table and a one-line conclusion.

**Shortcut.** Subtracting a constant from every value (e.g. 80 in A5 D4) leaves all sums of squares unchanged.

## Traps

- Computing F = SSB/SSW without dividing by the df.
- Reversing the df when reading the F table (numerator df = k − 1).
- Using n instead of each nᵢ when groups are unequal.
- Rounding CF early: keep CF to two decimals or more.
- Concluding which group differs from an ANOVA alone: it only says "not all equal".

## Self-test

1. State the null hypothesis and assumptions of one-way ANOVA.
2. Write the ANOVA table headings with the df.
3. k = 4, N = 20, SSB = 36, SSW = 64. Find F; decide at 5% (F₀.₀₅(3, 16) = 3.24).
4. Why is the ANOVA test right-tailed only?
5. Groups A = 2, 4, 6; B = 6, 8, 10. Find SSB, SSW and F.

<!--ANSWERS-->
## Answers

**Check 1.** Each test has a 5% Type I error; three tests raise the chance of at least one false rejection well above 5%. ANOVA keeps one test at α.

**Check 2.** SSW = 90; df 2, 12, 14; MSB = 30, MSW = 7.5; **F = 4**.

**Check 3.** G = 144, N = 12, CF = 144^{2}/12 = 1728. SST = 1840 − 1728 = **112**; SSB = (1600 + 2304 + 3136)/4 − 1728 = 1760 − 1728 = **32**; SSW = **80**; F = (32/2)/(80/9) = **1.8**.

**Check 4.** x̄₁ = 76, x̄₂ = 109, x̄₃ = 70; x̄ = 1563/18 = 86.833. SSB = 5(10.833)^{2} + 7(22.167)^{2} + 6(16.833)^{2} = 586.8 + 3439.5 + 1700.2 = **5726.5** ✓.

**Self-test.**

1. H₀: μ₁ = … = μₖ. Normal populations, equal variances, independent random samples.
2. Source · SS · df (k − 1, N − k, N − 1) · MS · F.
3. MSB = 12, MSW = 4, **F = 3** < 3.24: do not reject.
4. Only between-group variation **larger** than within-group variation is evidence of different means.
5. x̄_{A} = 4, x̄_{B} = 8, grand mean 6. SSB = 3(4) + 3(4) = **24**; SSW = 8 + 8 = **16**; F = (24/1)/(16/4) = **6**.
<!--/ANSWERS-->
