# 16 — Analysis of variance (one-way ANOVA)

<div class="sub">Gupta & Kapoor §14.5.11 (the F-test for equality of several means "is carried out by the technique of Analysis of Variance"), §14.5.5 (F ratio, right-tail table values) · the ANOVA formulas (sums of squares, df, mean squares, F, assumptions): S. H. Chan, Rutgers Math 170S notes §9.3, and R. Lockhart, SFU STAT 330 lecture 20 · blueprint row 5 "Analysis of Variance (ANOVA)" · 4 real questions (A5 A9, A10, C6, D4) · needs 08 step 5 (dividing by n − 1), 12a step 8 (the steps of a test), 13 step 5 (pooled variance of two samples), 14 steps 1–2 (F ratio; df order and right-tail table)</div>

## Map

[[map:1 Spread between groups against spread inside them > 2 Assumptions and one-way classification > 3 Splitting the total: SST = SSB + SSW > 4 Computing the sums from totals > 5 Degrees of freedom and mean squares > 6 The ANOVA table and F > 7 One-way ANOVA, equal groups > 8 One-way ANOVA, unequal groups|here=1]]

File 13 compared the averages of **two** groups with a t-test. Often there are three or more: three ways of lowering blood pressure, three areas' household incomes. ANOVA (analysis of variance) answers "are all the group averages equal?" in one test. It does so by comparing two spreads: how far the **group averages** are from each other, and how far the **values inside each group** scatter. The comparison is an F ratio read from the same F table as file 14.

| Symbol | What it means in this file | Typical value (A5 C6) |
|---|---|---|
| k | the number of groups (treatments) being compared | 3 |
| nᵢ, N | the number of values in group i; the number of values in all groups together | 5; 15 |
| Tᵢ, G | the total of group i; the grand total of all N values | 59, 19, 38; 116 |
| x̄ᵢ, x̄ | the average of group i (Tᵢ/nᵢ); the grand average of all values (G/N) | 11.8, 3.8, 7.6; 7.73 |
| SSB | between-groups sum of squares: how far the group averages sit from the grand average | 160.13 |
| SSW | within-groups sum of squares: how far the values sit from their own group's average | 104.80 |
| SST | total sum of squares: how far all values sit from the grand average; SST = SSB + SSW | 264.93 |
| MSB, MSW | mean squares: SSB/(k − 1) and SSW/(N − k) | 80.07, 8.73 |
| F | MSB/MSW: how many times larger the between spread is than the within spread | 9.17 |

**Running example.** A5 C6: blood-pressure reduction in 15 people, 5 per technique. Medication 10, 12, 9, 15, 13 (average 11.8); exercise 6, 8, 3, 0, 2 (3.8); diet 5, 9, 12, 8, 4 (7.6). The test gives **F = 9.17 with (2, 12) df**, against the 5% table value 3.89. Steps 1 and 3–7 use it.

## The questions this file answers

- <span class="tag">A5 C6</span> Blood-pressure reduction under three techniques: medication 10, 12, 9, 15, 13; exercise 6, 8, 3, 0, 2; diet 5, 9, 12, 8, 4. Test at 5% whether the mean reductions differ. (Tabulated value given: 19.41.)
- <span class="tag">A5 D4</span> Annual household income (Rs 1000) in three areas: (1) 70, 72, 75, 80, 83; (2) 100, 110, 108, 112, 113, 120, 100; (3) 60, 65, 57, 84, 84, 70. Can the average incomes be considered the same at α = 0.01? (Tabulated value 6.36.)
- <span class="tag">A5 A9 · 2 marks</span> In one-way ANOVA with k groups and N observations, the df between and within groups are: k and N / k − 1 and N − k / N − 1 and k − 1 / N − k and N − 1.
- <span class="tag">A5 A10 · 2 marks</span> One-way ANOVA with SSB = 120, SSW = 180, k = 4, N = 24: the F-statistic is 4.00 / 5.00 / 6.00 / 8.00.

Assignment 5 lists the ANOVA topics as introduction, assumptions, classification and one-way ANOVA. Blueprint row 5 holds the paper's only Part D (8 marks); A5 D4 is the assignment's Part D version of this question.

---

## Build

### 1 · Spread between groups against spread inside them

File 13 step 5 compared two averages. With three groups, the question "are the averages different?" needs one measure for all three at once.

:::q Predict
The figure shows two experiments with the **same three group averages**, 11.8, 3.8 and 7.6. In (a) the five values of each group lie close together; in (b) they scatter widely. In which experiment are you convinced that the three techniques really differ, and why?
:::

:::guess Guess first
Write one sentence comparing "how far apart the group averages are" with "how far the values scatter inside each group".
:::

:::note Terms
**Group (treatment):** one of the k things being compared (medication, exercise, diet). **Between-groups spread:** how far the group averages are from the grand average of all values; if the treatments differ, this is large. **Within-groups spread:** how far each value is from its own group's average; it comes from chance alone (people differ), whatever the treatments do.
:::

[[fig:anova_spread_pair|What this graph plots: two experiments, each with three groups of five values (dots). Vertical axis: reduction in blood pressure; the short solid lines are the group averages 11.8, 3.8 and 7.6, the same in both panels; dashed line: the grand average 7.73. In (a) the groups are tight and F = 128; in (b) they overlap and F = 1.29.|w=88]]

| Experiment | spread of the averages | scatter inside groups | F = between ÷ within |
|---|---|---|---|
| (a) tight | same | small (each value within 1 of its average) | 128 |
| (b) wide | same | large (values from −6 to 21) | 1.29 |

Reading the table: the same gap between averages is convincing in (a) and not in (b). What decides is the gap **compared with** the scatter inside the groups. ANOVA measures both as variances and divides one by the other: F = (between-groups variance estimate) ÷ (within-groups variance estimate).

If all groups have the same true average (H₀), both estimates measure the same chance scatter σ², so F is near 1. If the averages differ, the between estimate grows and F becomes large.

**Answer to the Predict.** Experiment (a). Its groups do not overlap, so the gap between averages cannot be chance scatter (F = 128). In (b) the scatter inside each group is larger than the gaps, so the same averages could come from three identical techniques (F = 1.29, near 1).

:::check Check 1
Why not compare the three techniques with three separate t-tests (A–B, A–C, B–C) at 5% each? Estimate the chance of at least one false rejection if the three tests were independent.
:::

### 2 · Assumptions and one-way classification

Step 1 compared two variance estimates. Both are honest estimates of one σ² only under certain conditions, and the design decides which ANOVA applies.

:::q Predict
File 13 step 5's pooled two-sample t assumed normal populations, equal variances and independent random samples (G&K §14.2.10 remark 3). ANOVA does the same job for k groups. Which of these assumptions do you expect it to keep?
:::

:::guess Guess first
All three, some, or none?
:::

:::note Terms
**Factor:** the one thing the experimenter changes between groups (the technique; the area). **Level:** one value of the factor (medication, exercise, diet are three levels). **One-way ANOVA:** the groups differ in one factor only; **two-way ANOVA:** two factors at once (for example technique and age group), each with its own F.
:::

**Assumptions of one-way ANOVA** (Rutgers notes §9.3):

1. Each group's values come from a **normal** population.
2. All k populations have the **same variance** σ² (only their means may differ).
3. The observations are **independent** random samples.

Assumption 2 is what lets the within-groups scatter of all groups be pooled into one estimate of σ², exactly as file 13 step 5 pooled two samples (step 5 below).

**Classification.**

| Design | Factor(s) | Which ANOVA |
|---|---|---|
| A5 C6: three techniques, reduction measured | technique | one-way |
| A5 D4: three areas, income measured | area | one-way |
| four fertilisers tried on plots with two irrigation levels | fertiliser and irrigation | two-way |

This file covers one-way ANOVA, as Assignment 5 does. With k = 2 groups one-way ANOVA gives F = t², where t is file 13's pooled t: the two tests agree (Self-test 5 shows it on numbers).

**Answer to the Predict.** All three: normal populations, equal variances, independent random samples. ANOVA is the pooled t-test extended to k groups.

:::check Check 2
Classify each design as one-way or two-way: (a) the hardness of steel from four furnaces; (b) the yield of wheat under three seed types and two fertilisers; (c) the marks of students taught by three methods.
:::

### 3 · Splitting the total: SST = SSB + SSW

Step 1 named two spreads. This step measures each as a sum of squares and shows that together they make up the total spread.

:::q Predict
One person on medication reduced by 15. The grand average of all 15 people is 7.73 and the medication average is 11.8. Split this person's distance from the grand average, 15 − 7.73, into a part due to the group and a part due to the person.
:::

:::guess Guess first
Which part is bigger: group or person?
:::

:::note Terms
**SST:** the total sum of squares, Σ(x − x̄)² over all N values: the whole spread around the grand average. **SSB:** Σnᵢ(x̄ᵢ − x̄)²: each group average's squared distance from the grand average, counted once for every value in that group. **SSW:** Σ(x − x̄ᵢ)² within each group, added over the groups: each value's squared distance from its own group's average.
:::

[[fig:anova_dots|What this graph plots: A5 C6's fifteen reductions, one dot per person, in three columns (medication, exercise, diet). Vertical axis: reduction in blood pressure. Short solid lines: the group averages 11.8, 3.8, 7.6; dashed line: the grand average 7.73. SSB measures the distances of the solid lines from the dashed line; SSW the distances of the dots from their own solid line.|w=80]]

For every value, the distance to the grand average splits into two pieces:

$$x − x̄ = (x̄_{i} − x̄) + (x − x̄_{i})$$

In words: (how far its group sits from the grand average) + (how far the value sits from its group). Squaring and adding over all values gives the decomposition (Rutgers notes §9.3; Lockhart lecture 20):

$$SST = SSB + SSW$$

The cross terms add to zero, because within each group the distances x − x̄ᵢ sum to 0.

On A5 C6 (x̄ = 116/15 = 7.733):

1. SSB = 5(11.8 − 7.733)² + 5(3.8 − 7.733)² + 5(7.6 − 7.733)² = 5(16.538) + 5(15.471) + 5(0.018) = **160.13**.
2. SSW: medication Σ(x − 11.8)² = 22.8; exercise Σ(x − 3.8)² = 40.8; diet Σ(x − 7.6)² = 41.2; total **104.80**.
3. SST = 160.13 + 104.80 = **264.93** (the same as Σ(x − 7.733)² over all 15 values).

[[fig:ss_split|What this graph plots: A5 C6's total sum of squares, 264.93, as one bar split into the between-groups part SSB = 160.13 (60 percent) and the within-groups part SSW = 104.80 (40 percent).|w=80]]

**Answer to the Predict.** 15 − 7.73 = 7.27 = (11.8 − 7.73) + (15 − 11.8) = **4.07 (group) + 3.2 (person)**. Here the group part is bigger.

:::check Check 3
Groups A = 2, 4, 6 and B = 6, 8, 10. Find the grand average, SSB, SSW and SST from the definitions, and check SST = SSB + SSW.
:::

### 4 · Computing the sums from totals

Step 3's definitions need every distance to a decimal average like 7.733. Exam questions are faster with totals and whole numbers.

:::q Predict
A5 C6's grand total is G = 116 over N = 15 values. Without computing any average, find SST.
:::

:::guess Guess first
Will the answer equal step 3's 264.93 exactly?
:::

:::note Terms
**Correction factor CF = G²/N:** the square of the grand total divided by the number of values; it is N × x̄², the part of Σx² that only reflects where the grand average sits. **Σx²:** the sum of the squares of all N values. **Tᵢ²/nᵢ:** a group total squared over its size, equal to nᵢ × x̄ᵢ².
:::

The working formulas (the same sums as step 3, rearranged; Rutgers notes §9.3 write CF as N x̄²):

$$CF = \frac{G^{2}}{N},    SST = Σx^{2} − CF,    SSB = Σ\frac{T_{i}^{2}}{n_{i}} − CF,    SSW = SST − SSB$$

In words: SST = (sum of all squares) minus CF; SSB = (each group total squared over its size, added) minus CF; SSW is what is left.

On A5 C6:

1. T₁ = 59, T₂ = 19, T₃ = 38; G = 116; CF = 116²/15 = 13,456/15 = **897.07**.
2. Σx² = (100 + 144 + 81 + 225 + 169) + (36 + 64 + 9 + 0 + 4) + (25 + 81 + 144 + 64 + 16) = 719 + 113 + 330 = **1162**.
3. SST = 1162 − 897.07 = **264.93**.
4. SSB = (59² + 19² + 38²)/5 − 897.07 = 5286/5 − 897.07 = 1057.2 − 897.07 = **160.13**.
5. SSW = 264.93 − 160.13 = **104.80**.

Keep CF to two decimals or more: SST and SSB are small differences of large numbers. Subtracting the same constant from every value (for example 80 from every income in step 8) leaves SST, SSB and SSW unchanged, because every distance stays the same.

**Answer to the Predict.** SST = Σx² − G²/N = 1162 − 897.07 = **264.93**, exactly step 3's value.

:::check Check 4
Three machines, 4 items each. Totals 40, 48, 56; Σx² = 1840. Find CF, SST, SSB and SSW.
:::

### 5 · Degrees of freedom and mean squares

SSB and SSW are sums over different numbers of free pieces. Before comparing them, each is divided by its degrees of freedom, as file 08 step 5 divided by n − 1.

:::q <span class="tag">A5 A9 · 2 marks</span>
In one-way ANOVA with k groups and N total observations, the degrees of freedom for between-group and within-group variation are: (A) k and N (B) k − 1 and N − k (C) N − 1 and k − 1 (D) N − k and N − 1
:::

:::guess Guess first
SSB is built from 3 group averages around 1 grand average. How many of those 3 are free?
:::

:::note Terms
**df of SSB:** k − 1. The k group averages must average (weighted by size) to the grand average, so one is fixed by the others. **df of SSW:** N − k. Each group's distances from its own average sum to 0, which costs one df per group. **Mean square:** a sum of squares divided by its df, a variance estimate: MSB = SSB/(k − 1), MSW = SSW/(N − k).
:::

| Sum of squares | built from | df | A5 C6 |
|---|---|---|---|
| SSB | k group averages around the grand average | k − 1 | 3 − 1 = 2 |
| SSW | N values around their k group averages | N − k | 15 − 3 = 12 |
| SST | N values around the grand average | N − 1 | 14 = 2 + 12 |

The df add up like the sums of squares: (k − 1) + (N − k) = N − 1.

On A5 C6: MSB = 160.13/2 = **80.07**; MSW = 104.80/12 = **8.73**.

MSW is file 13 step 5's pooled variance extended to k groups: (22.8 + 40.8 + 41.2)/(4 + 4 + 4) = 104.8/12 = 8.73, the within-group squared distances of all groups divided by all their df together.

**Answer to the question.** **(B)**, k − 1 and N − k. Answer to the guess: 2 of the 3 averages are free.

:::check Check 5
k = 5 groups, N = 30 values. Write the df between, within and total.
:::

### 6 · The ANOVA table and F

The two mean squares are the two variance estimates of step 1. Their ratio is the test statistic, and every ANOVA answer is laid out in one standard table.

:::q <span class="tag">A5 A10 · 2 marks</span>
In one-way ANOVA, SSB = 120, SSW = 180, k = 4 groups and N = 24 observations. The calculated F-statistic is: (A) 4.00 (B) 5.00 (C) 6.00 (D) 8.00
:::

:::guess Guess first
Is F = 120/180? What has to happen to each sum first?
:::

:::note Terms
**F = MSB/MSW:** between-groups variance estimate over within-groups variance estimate. **Under H₀ (all means equal):** F follows the F distribution with (k − 1, N − k) df, numerator df first (file 14 step 2). **Critical region:** F > F_{α}(k − 1, N − k), right tail only: only a between spread **larger** than the within spread is evidence that the means differ (Rutgers notes §9.3: reject H₀ if MS(T)/MS(E) ≥ F_{α}(m − 1, n − m)).
:::

| Source | SS | df | MS = SS/df | F |
|---|---|---|---|---|
| Between groups | SSB | k − 1 | MSB | MSB/MSW |
| Within groups | SSW | N − k | MSW | |
| Total | SST | N − 1 | | |

In words: each row's MS is its SS shared out over its df; F compares the two MS.

**Answer to the question.**

1. df: k − 1 = 3, N − k = 20.
2. MSB = 120/3 = 40; MSW = 180/20 = 9.
3. F = 40/9 = **4.44**.

Answer to the guess: no; 120/180 = 0.67 skips the df. Each SS is divided by its own df first.

:::note A5 A10's options
None of the options equals 4.44; the assignment's key gives (A) 4.00, the nearest. In the exam write F = MSB/MSW = 40/9 = 4.44 with the working, and mark the nearest option.
:::

:::check Check 6
k = 3, N = 15, SSB = 60, SST = 150. Fill in the ANOVA table and find F.
:::

### 7 · One-way ANOVA, equal groups

Steps 3–6 built every piece on A5 C6. This step runs the whole test as the exam asks it.

:::q <span class="tag">A5 C6</span>
Three techniques, medication, exercises and special diet, are randomly assigned to individuals diagnosed with high blood pressure. After four weeks the reduction in each person's blood pressure is recorded:

| Technique | Person 1 | Person 2 | Person 3 | Person 4 | Person 5 |
|---|---|---|---|---|---|
| Medication | 10 | 12 | 9 | 15 | 13 |
| Exercise | 6 | 8 | 3 | 0 | 2 |
| Diet | 5 | 9 | 12 | 8 | 4 |

Test at the 5% level whether there is a significant difference in mean reduction of blood pressure among the three techniques. (Tabulated value 19.41.)
:::

:::guess Guess first
F is 9.17 (steps 4–5). Is the right table value F₀.₀₅(2, 12) or F₀.₀₅(12, 2)?
:::

:::note Terms
**F₀.₀₅(2, 12):** the F value with 5% of the F(2, 12) curve to its right, read with the between df (2) as the numerator df and the within df (12) as the denominator df.
:::

[[fig:anova_f_curve|What this graph plots: the F curve with (2, 12) df, the values F takes by chance when all three techniques have the same mean. Horizontal axis: the value of F; height: how often chance gives a value near it. Red tail beyond 3.89: the 5 percent critical region. Green line: A5 C6's F = 9.17. Orange dashed line: 19.41, the table value with the df swapped.|w=84]]

| F | share of F(2, 12) values above it |
|---|---|
| 2 | 0.178 |
| 3.89 (5% table value) | 0.05 |
| 6.93 (1% table value) | 0.01 |
| 9.17 (A5 C6) | 0.004 |

**Answer to the question.**

1. H₀: μ₁ = μ₂ = μ₃ (the three techniques give the same mean reduction); H₁: not all equal. k = 3, n = 5 each, N = 15.
2. CF = 116²/15 = 897.07; Σx² = 1162 (step 4).
3. SST = 264.93, SSB = 160.13, SSW = 104.80.

| Source | SS | df | MS | F |
|---|---|---|---|---|
| Between techniques | 160.13 | 2 | 80.07 | **9.17** |
| Within techniques | 104.80 | 12 | 8.73 | |
| Total | 264.93 | 14 | | |

4. F₀.₀₅(2, 12) = **3.89**. 9.17 > 3.89: **reject H₀**. The mean reductions differ between the techniques; medication gives the largest average reduction (11.8).

Answer to the guess: F₀.₀₅(2, 12), numerator df first.

:::note Table value slip (A5 C6)
The assignment prints 19.41, which is F₀.₀₅(**12, 2**): the df reversed (file 14 step 2). The numerator df is k − 1 = 2 and the denominator df is N − k = 12, so the table value is F₀.₀₅(2, 12) = 3.89. Compared with 19.41 the decision would wrongly be "do not reject". In the exam, state the df, give 3.89, and say why the printed value does not apply.
:::

ANOVA says only that the means are **not all equal**; it does not say which pair differs.

:::check Check 7
Would A5 C6's decision change at the 1% level (F₀.₀₁(2, 12) = 6.93)?
:::

### 8 · One-way ANOVA, unequal groups

A5 C6 had 5 values in every group. When the groups differ in size, each group total is divided by its own size.

:::q <span class="tag">A5 D4</span>
A department store chain is considering a new store at one of three locations. Since household income is a key factor, a survey compared average incomes across the areas (annual household income, Rs 1000):

| Area (1) | Area (2) | Area (3) |
|---|---|---|
| 70 | 100 | 60 |
| 72 | 110 | 65 |
| 75 | 108 | 57 |
| 80 | 112 | 84 |
| 83 | 113 | 84 |
| – | 120 | 70 |
| – | 100 | – |
| 380 | 763 | 420 |

Test if the average income per household in all these localities can be considered the same at α = 0.01. (Tabulated value 6.36.)
:::

:::guess Guess first
Area 2's incomes are all 100 or more; the others are mostly below 85. Reject or not?
:::

:::note Terms
**Unequal groups:** nᵢ differs between groups (5, 7, 6). SSB = ΣTᵢ²/nᵢ − CF with each group's own nᵢ; everything else is as in step 7.
:::

[[fig:income_dots|What this graph plots: A5 D4's household incomes, one dot per household, in three columns (Area 1 with 5 households, Area 2 with 7, Area 3 with 6). Vertical axis: income in Rs 1000. Short solid lines: area averages 76, 109 and 70; dashed line: the grand average 86.8. Area 2 sits above the other two with no overlap.|w=80]]

**Answer to the question.**

1. H₀: μ₁ = μ₂ = μ₃; H₁: not all equal. n = 5, 7, 6; N = 18; T = 380, 763, 420; G = 1563.
2. CF = 1563²/18 = 2,442,969/18 = **135,720.5**.
3. Σx² = 28,998 + 83,477 + 30,086 = 142,561; SST = 142,561 − 135,720.5 = **6840.5**.
4. ΣTᵢ²/nᵢ = 380²/5 + 763²/7 + 420²/6 = 28,880 + 83,167 + 29,400 = 141,447; SSB = 141,447 − 135,720.5 = **5726.5**.
5. SSW = 6840.5 − 5726.5 = **1114.0**.

| Source | SS | df | MS | F |
|---|---|---|---|---|
| Between areas | 5726.5 | 2 | 2863.25 | **38.55** |
| Within areas | 1114.0 | 15 | 74.27 | |
| Total | 6840.5 | 17 | | |

6. F₀.₀₁(2, 15) = 6.36 (the printed value is right: numerator df 2, denominator df 15). 38.55 > 6.36: **reject H₀**. The average household income is not the same in the three areas; Area 2's is highest (average 109).

Answer to the guess: reject, by a wide margin.

:::check Check 8
Recompute A5 D4's SSB from the definition SSB = Σnᵢ(x̄ᵢ − x̄)², with area averages 76, 109, 70 and x̄ = 1563/18 = 86.83.
:::

---

## Exam form

**Definition.** Analysis of variance splits the total variation of the data into a between-groups part and a within-groups part to test H₀: μ₁ = μ₂ = … = μₖ (G&K §14.5.11: the F-test for equality of several means).

**Assumptions.** Normal populations; equal variances; independent random samples. **Classification:** one-way (one factor), two-way (two factors).

**Procedure (one-way).**

1. H₀: all k means are equal; H₁: at least two differ.
2. Tᵢ, nᵢ, G, N; CF = G²/N.
3. SST = Σx² − CF; SSB = ΣTᵢ²/nᵢ − CF; SSW = SST − SSB.
4. MSB = SSB/(k − 1), MSW = SSW/(N − k), F = MSB/MSW.
5. Compare with F_{α}(k − 1, N − k), numerator df first; F larger: reject H₀.
6. Present the ANOVA table and a one-line conclusion in the words of the question.

**Shortcut.** Subtracting a constant from every value (for example 80 in A5 D4) leaves every sum of squares unchanged.

## Traps

- F = SSB/SSW without dividing each by its df (A5 A10: 120/180).
- Reversing the df when reading the F table (A5 C6's printed 19.41 = F₀.₀₅(12, 2)).
- Using one n for all groups when the groups are unequal (A5 D4).
- Rounding CF early: SST and SSB are small differences of large numbers.
- Concluding which group differs from ANOVA alone: it only says "not all equal".
- Testing in the left tail: a small F is never evidence that the means differ.

## Self-test

1. State the null hypothesis and the assumptions of one-way ANOVA.
2. Write the ANOVA table headings with the df.
3. k = 4, N = 20, SSB = 36, SSW = 64. Find F; decide at 5% (F₀.₀₅(3, 16) = 3.24).
4. Why is the ANOVA test right-tailed only?
5. Groups A = 2, 4, 6; B = 6, 8, 10. Find SSB, SSW and F, and compare F with the square of file 13's pooled t for the same data.

<!--ANSWERS-->
## Answers

**Check 1.** Each test has a 5% chance of a false rejection; with three tests, the chance of at least one is about 1 − 0.95³ = **0.14** (if the tests were independent), nearly three times 5%. ANOVA keeps one test at α.

**Check 2.** (a) **one-way** (factor: furnace). (b) **two-way** (seed type and fertiliser). (c) **one-way** (teaching method).

**Check 3.** Grand average 36/6 = 6. SSB = 3(4 − 6)² + 3(8 − 6)² = 12 + 12 = **24**. SSW = (4 + 0 + 4) + (4 + 0 + 4) = **16**. SST = 16 + 4 + 0 + 0 + 4 + 16 = **40** = 24 + 16 ✓.

**Check 4.** G = 144, N = 12, CF = 144²/12 = **1728**. SST = 1840 − 1728 = **112**; SSB = (1600 + 2304 + 3136)/4 − 1728 = 1760 − 1728 = **32**; SSW = **80**.

**Check 5.** Between k − 1 = **4**; within N − k = **25**; total N − 1 = **29**.

**Check 6.** SSW = 150 − 60 = 90; df 2, 12, 14; MSB = 30, MSW = 7.5; **F = 4**.

**Check 7.** No: 9.17 > 6.93, still reject H₀ at 1%.

**Check 8.** 5(76 − 86.833)² + 7(109 − 86.833)² + 6(70 − 86.833)² = 5(117.36) + 7(491.36) + 6(283.36) = 586.8 + 3439.5 + 1700.2 = **5726.5** ✓.

**Self-test.**

1. H₀: μ₁ = … = μₖ. Normal populations, equal variances, independent random samples.
2. Source · SS · df (k − 1, N − k, N − 1) · MS · F.
3. MSB = 36/3 = 12, MSW = 64/16 = 4, **F = 3** < 3.24: do not reject.
4. Only a between-groups spread **larger** than the within-groups spread is evidence that the means differ; under H₀ both estimate σ² and F is near 1.
5. Averages 4 and 8, grand average 6. SSB = 3(4) + 3(4) = **24**; SSW = 8 + 8 = **16**; F = (24/1)/(16/4) = **6**. Pooled t: S² = 16/4 = 4, t = (8 − 4)/√(4(1/3 + 1/3)) = 4/1.633 = 2.449, and t² = **6** = F.
<!--/ANSWERS-->
