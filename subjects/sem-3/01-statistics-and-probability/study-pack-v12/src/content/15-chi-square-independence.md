# 15 — Chi-square test of independence of attributes

<div class="sub">Gupta & Kapoor §13.7.3 (independence of attributes: expected frequency (13·16), χ² with (r − 1)(s − 1) df (13·16a)), §13.5 remarks 2 and 4 (conditions for validity; right-tail critical values), note on degrees of freedom, Example 13·16 (2 × 2: one cell fixes the rest), Example 13·17 (2 × 2 formula) · blueprint row 5 "chi-square test" · 8 real questions (A5 A3, A6, A7, A8, B5, B6, C3, D3) · needs 01 step 10 (independent events: P(A and B) = P(A) × P(B)), 12a steps 6 and 8 (critical region; the steps of a test), 14 step 2 (right-tail table values)</div>

## Map

[[map:1 Counts in a table > 2 Expected frequency > 3 The χ² statistic > 4 Degrees of freedom > 5 A 2 × 2 test > 6 The 2 × 2 shortcut > 7 Building the table from a story > 8 A 3 × 3 table|here=1]]

Files 13 and 14 tested **measurements**: weights, nitrate, heat capacity. Some questions give no measurements at all, only **counts**: how many men smoke and have a lung ailment, how many families have low income and use a government school. The question is then whether two yes/no-type characteristics go together. This file builds the test for that from one idea: if the two have nothing to do with each other, the counts should look like a prediction we can compute, and a statistic called χ² ("chi-square") measures how far the real counts are from that prediction.

| Symbol | What it means in this file | Typical value |
|---|---|---|
| O | an **observed** count: how many units the data put in one cell of the table | 75 |
| E | the **expected** count: how many would be in that cell if the two characteristics were unrelated | 60 |
| Rᵢ, Cⱼ, N | the total of row i, of column j, and of the whole table | 180, 100, 300 |
| r, c | the number of rows and of columns of the table | 2, 2 |
| χ² | Σ(O − E)²/E over every cell: one number for how far the table is from "unrelated" | 14.06 |
| df | (r − 1)(c − 1): how many cells can be filled freely once the totals are fixed | 1 |
| χ²_{α} | table value: the χ² with area α to its right for that df | χ²₀.₀₅ = 3.841 (1 df) |

**Running example.** A5 C3: 300 men aged 40–50, **180 smokers and 120 non-smokers; 100 with a lung ailment, 200 without**. Observed: smokers 75 with an ailment, 105 without; non-smokers 25 with, 95 without. If smoking had nothing to do with the ailment, 60 smokers would have one; the test gives **χ² = 14.06 with 1 df**, against the table value 3.841. Steps 1–5 build this.

## The questions this file answers

- <span class="tag">A5 C3</span> 300 men: smokers 75 with lung ailment, 105 without; non-smokers 25 with, 95 without. Can it be concluded that smoking and lung ailments are independent? (Table value 3.841.)
- <span class="tag">A5 D3</span> 1000 families: low income 370 public school, 430 government school; high income 130, 70. Test whether income and type of schooling are independent. (Table value 3.841.)
- <span class="tag">A5 B5</span> Of 2000 families, 1400 consume tea; of 1800 Hindu families, 1236 consume tea. Is there a significant difference in tea consumption between Hindu and non-Hindu families? (Table value 3.841.)
- <span class="tag">A5 B6</span> 200 seismic test records: test result Good / Fair / Bad against oil yield High / Medium / Low. Are oil yield and test result associated at 1%? (Table value 13.28.)
- <span class="tag">A5 A3, A6, A7, A8</span> Which test checks independence of attributes; the expected-frequency formula; the df of an r × c table.

---

## Build

### 1 · Counts in a table

Files 13–14 compared averages and spreads of measurements. Here each man gives no measurement, only two labels: smoker or not, ailment or not.

:::q Predict
In A5 C3's sample, 75 of the 180 smokers have a lung ailment, and 25 of the 120 non-smokers. Before any formula: do these counts suggest that smoking and lung ailment go together? What would the counts look like if they did not?
:::

:::guess Guess first
Write the share of smokers with an ailment and the share of non-smokers with an ailment as percentages.
:::

:::note Terms
**Attribute:** a characteristic that sorts units into classes instead of measuring them (smoker / non-smoker; ailment / none). **Contingency table:** the counts of N units sorted by two attributes at once, one attribute's classes as rows and the other's as columns; with r rows and c columns it is an r × c table (G&K writes r × s). **Independent attributes:** knowing a unit's row class does not change the chances of its column class (file 01 step 10: P(A and B) = P(A) × P(B)).
:::

| | Lung ailment | No lung ailment | Row total |
|---|---|---|---|
| Smokers | 75 | 105 | 180 |
| Non-smokers | 25 | 95 | 120 |
| Column total | 100 | 200 | N = 300 |

[[fig:smoke_split|What this graph plots: one bar per row of A5 C3's table, split into the share of that row with a lung ailment and the share without. Horizontal axis: share of the row in percent. Dashed line: the share of all 300 men with an ailment, 33.3 percent. If the attributes were independent, both bars would split near the dashed line.|w=80]]

| Row | with ailment | share of the row |
|---|---|---|
| Smokers | 75 of 180 | 41.7% |
| Non-smokers | 25 of 120 | 20.8% |
| All men | 100 of 300 | 33.3% |

Reading the table: if the ailment had nothing to do with smoking, smokers and non-smokers would each show about the overall 33.3%. Here smokers show twice the non-smokers' share. Counts always wobble from sample to sample, so the question the test answers is: **is a gap this big too large to be chance?**

**Answer to the Predict.** 41.7% of smokers against 20.8% of non-smokers: the counts suggest the two go together. With no link, both rows would split close to 33.3% : 66.7%. Steps 2–5 turn "close to" into a number and a decision.

:::check Check 1
Of 60 boys, 30 passed; of 40 girls, 20 passed. Write the 2 × 2 table with totals and the pass share of each row. Do the counts suggest that passing depends on gender?
:::

### 2 · Expected frequency

Step 1 said "with no link, each row would split like the whole sample". This step turns that into a count for each cell.

:::q <span class="tag">A5 A7 · 2 marks</span>
The expected frequency in a cell of a contingency table, under the hypothesis of independence, is calculated as: (A) row total + column total (B) row total × column total (C) (row total × column total)/grand total (D) grand total/row total
:::

:::guess Guess first
If smoking had nothing to do with the ailment, how many of the 180 smokers would you expect to have one?
:::

:::note Terms
**Expected frequency E:** the count a cell would have if the attributes were independent and the totals stayed as observed. **Rᵢ, Cⱼ, N:** the row total, the column total and the grand total that the cell sits in.
:::

Concrete first: 100 of the 300 men (one third) have an ailment. If smoking does not matter, one third of the 180 smokers should have it: 180 × 100/300 = **60**.

The same reasoning in general (G&K §13.7.3, eq. 13·16):

1. P(a unit is in row i) = Rᵢ/N; P(a unit is in column j) = Cⱼ/N.
2. Independent attributes (file 01 step 10): P(row i and column j) = (Rᵢ/N) × (Cⱼ/N).
3. Expected count = N × that probability:

$$E_{ij} = N × \frac{R_{i}}{N} × \frac{C_{j}}{N} = \frac{R_{i} × C_{j}}{N}$$

In words: expected count = (its row total) × (its column total) ÷ (grand total).

| Cell | R × C / N | E | O |
|---|---|---|---|
| smoker, ailment | 180 × 100/300 | 60 | 75 |
| smoker, none | 180 × 200/300 | 120 | 105 |
| non-smoker, ailment | 120 × 100/300 | 40 | 25 |
| non-smoker, none | 120 × 200/300 | 80 | 95 |

The E's have the same row and column totals as the O's (60 + 120 = 180, 60 + 40 = 100): independence moves counts around inside the table, never the totals.

**Answer to the question.** **(C)**, (row total × column total)/grand total. Answer to the guess: **60** smokers with an ailment (75 observed).

:::check Check 2
In A5 D3 (low income: 370 public, 430 government; high income: 130 public, 70 government; N = 1000), find the expected count of low-income families in public schools, then the other three by subtraction from the totals.
:::

### 3 · The χ² statistic

Each cell now has an observed and an expected count. One number has to summarise how far the whole table is from "independent".

:::q <span class="tag">A5 A6 · 2 marks</span>
Which statistical test is commonly used to examine the independence of two categorical attributes? (A) Paired t-test (B) F-test (C) Chi-square test of independence (D) One sample t-test
:::

:::guess Guess first
In the smoking table, the non-smoker–ailment cell is off by 15 (25 against 40) and the smoker–none cell is also off by 15 (105 against 120). Which miss is more surprising?
:::

:::note Terms
**O − E:** how far one cell's count is from the independence prediction. **(O − E)²/E:** that miss squared (so + and − misses both count) and divided by E (a miss of 15 is large when 40 are expected, small when 120 are). **χ²:** the sum of (O − E)²/E over all cells (Karl Pearson's statistic, G&K §13.7.3, eq. 13·16a).
:::

[[fig:obs_exp|What this graph plots: for each of A5 C3's four cells, the observed count O (left bar) and the count E that independence predicts (right bar). Vertical axis: number of men. Smokers have more ailments than predicted (75 against 60) and non-smokers fewer (25 against 40).|w=78]]

$$χ^{2} = Σ \frac{(O − E)^{2}}{E}$$

In words: for every cell, square the miss and divide by the expected count; add over all cells. χ² = 0 when every O equals its E; it grows as the table moves away from independence.

| Cell | O | E | O − E | (O − E)²/E |
|---|---|---|---|---|
| smoker, ailment | 75 | 60 | +15 | 225/60 = 3.750 |
| smoker, none | 105 | 120 | −15 | 225/120 = 1.875 |
| non-smoker, ailment | 25 | 40 | −15 | 225/40 = 5.625 |
| non-smoker, none | 95 | 80 | +15 | 225/80 = 2.8125 |
| | | | sum | χ² = **14.0625** |

**Answer to the question.** **(C)**, the chi-square test of independence. <span class="tag">A5 A3</span> "The test of independence of attributes is based on the **χ² (chi-square)** test." Answer to the guess: the miss of 15 on an expected 40 (contributes 5.625) is more surprising than 15 on 120 (1.875).

:::check Check 3
(a) In every 2 × 2 table the four values of |O − E| are equal. Why? (b) A table has O = 30, 20 (row 1) and 20, 30 (row 2). Find every E and χ².
:::

### 4 · Degrees of freedom

χ² = 14.06 is "big" only compared with what chance alone produces, and that depends on how many cells are free to wobble.

:::q <span class="tag">A5 A8 · 2 marks</span>
For a chi-square test of independence in an r × c contingency table, the degrees of freedom are: (A) rc − 1 (B) r + c − 2 (C) (r − 1)(c − 1) (D) (r − 1)c
:::

:::guess Guess first
In the smoking table keep all the totals (180, 120; 100, 200; 300) and write any number in the top-left cell. How many of the other three cells can you still choose?
:::

:::note Terms
**Degrees of freedom (df):** the number of cells that can be filled freely once the row and column totals are fixed (G&K, note on degrees of freedom: the number of observations less the number of independent constraints). **χ² curve with ν df:** how often chance alone gives each value of χ² when the attributes are independent; more df, more cells adding up misses, so the curve lies further right.
:::

Derivation (G&K's note on degrees of freedom):

1. An r × c table has rc cells.
2. The r row totals and the c column totals are fixed: r + c constraints.
3. Both sets of totals add up to N, so one constraint repeats: r + c − 1 independent constraints.
4. df = rc − (r + c − 1) = rc − r − c + 1 = **(r − 1)(c − 1)**.

2 × 2: (1)(1) = 1 df (the top-left cell fixes all three others: G&K Ex. 13·16). 3 × 3: (2)(2) = 4 df.

[[fig:chi_df_curves|What this graph plots: the χ² curves for 1 df and for 4 df, the values χ² takes by chance alone when the attributes are independent. Horizontal axis: the value of χ²; height: how often chance gives a value near it. Each shaded tail holds 5 percent: beyond 3.841 for 1 df, beyond 9.488 for 4 df.|w=82]]

| χ² | share above it, 1 df | share above it, 4 df |
|---|---|---|
| 2 | 0.157 | 0.736 |
| 3.841 | 0.05 | — |
| 6.635 | 0.01 | — |
| 9.488 | — | 0.05 |
| 13.28 | — | 0.01 |

Reading the table: with 1 df, chance alone exceeds 3.841 only 5% of the time; with 4 df the same 5% sits at 9.488, because four free cells add up more chance misses.

**Answer to the question.** **(C)**, (r − 1)(c − 1). Answer to the guess: none; once the top-left cell is written, the totals force the other three. So a 2 × 2 table has 1 df.

:::check Check 4
Find the df of (a) a 4 × 3 table and (b) a 2 × 3 table. (c) In the 4 × 3 table, how many expected frequencies must be computed from R × C/N before the rest follow from the totals?
:::

### 5 · A 2 × 2 test

χ², its df and the table value are all in place. This step runs the whole test on the running example.

:::q <span class="tag">A5 C3</span>
A tobacco company claims that there is no relationship between smoking and lung ailments. To investigate the claim, a random sample of 300 males aged 40–50 are given a medical test:

| | Lung ailment | No lung ailment | Total |
|---|---|---|---|
| Smokers | 75 | 105 | 180 |
| Non-smokers | 25 | 95 | 120 |
| Total | 100 | 200 | 300 |

Based on this information, can it be concluded that smoking and lung ailments are independent? (The table value = 3.841.)
:::

:::guess Guess first
χ² = 14.06 from step 3, table value 3.841. Reject or not?
:::

:::note Terms
**H₀ for this test:** the two attributes are independent. **H₁:** they are associated. **Critical region:** χ² larger than the table value χ²_{α}(df). Only large χ² is evidence against H₀ (a perfect match, χ² = 0, is never evidence against it), so the test uses the **right tail** only (G&K §13.5 remark 4: the tables give upper α-points).
:::

[[fig:chi_curve|What this graph plots: the χ² curve for 1 df, the values chance alone gives when smoking and ailment are independent. Horizontal axis: the value of χ²; height: how often chance gives a value near it. Red tail beyond 3.841: the 5 percent critical region. Green line: A5 C3's χ² = 14.06, far inside it.|w=82]]

| χ² | share of chance values above it (1 df) |
|---|---|
| 2 | 0.157 |
| 3.841 (table value) | 0.05 |
| 14.06 (A5 C3) | 0.0002 |

**Conditions** (G&K §13.5 remark 2), checked before the test: the observations are independent; N is reasonably large (G&K: more than 50); **no expected frequency is below 5** (pool a small cell with a neighbour and lose its df otherwise). Here N = 300 and the smallest E is 40.

**Answer to the question.**

1. H₀: smoking and lung ailment are independent; H₁: they are associated.
2. Expected counts (step 2): 60, 120, 40, 80.
3. χ² = 3.750 + 1.875 + 5.625 + 2.8125 = **14.06** (step 3).
4. df = (2 − 1)(2 − 1) = 1; χ²₀.₀₅(1) = 3.841.
5. 14.06 > 3.841: **reject H₀**. Smoking and lung ailment are associated; the company's claim of no relationship is not supported by the data.

Answer to the guess: reject. χ² is more than three times the table value.

:::check Check 5
(a) A 2 × 2 table gives χ² = 2.9. Decide at 5%. (b) Would A5 C3's decision change at the 1% level (χ²₀.₀₁(1) = 6.635)?
:::

### 6 · The 2 × 2 shortcut

Steps 2–3 needed four expected counts and four contributions. For a 2 × 2 table one formula does it in one line.

:::q <span class="tag">A5 D3</span>
1,000 families were selected at random in a city to test the belief that high-income families usually send their children to public schools and low-income families to government schools:

| Income | Public school | Government school | Total |
|---|---|---|---|
| Low | 370 | 430 | 800 |
| High | 130 | 70 | 200 |
| Total | 500 | 500 | 1000 |

Test whether income and type of schooling are independent. (Tabulated value 3.841.)
:::

:::guess Guess first
Low-income families: 370 of 800 (46%) in public schools. High-income: 130 of 200 (65%). Will χ² be above 3.841?
:::

:::note Terms
**a, b, c, d:** the four cells read row by row (a, b first row; c, d second row). **ad − bc:** the "cross difference"; it is 0 exactly when both rows split in the same proportion, that is when O = E in every cell.
:::

Where the shortcut comes from (G&K Ex. 13·17):

1. E(a) = (a + b)(a + c)/N (step 2).
2. a − E(a) = [a(a + b + c + d) − (a + b)(a + c)]/N = (ad − bc)/N.
3. b, c and d miss their E's by the same amount (Check 3), with signs − , − , +.
4. So χ² = (ad − bc)²/N² × [1/E(a) + 1/E(b) + 1/E(c) + 1/E(d)].
5. The bracket simplifies to N³/[(a + b)(c + d)(a + c)(b + d)], which gives

$$χ^{2} = \frac{N(ad − bc)^{2}}{(a + b)(c + d)(a + c)(b + d)}$$

In words: N times the squared cross difference, divided by the product of the two row totals and the two column totals.

**Answer to the question.**

1. H₀: income and type of school are independent; H₁: associated.
2. a = 370, b = 430, c = 130, d = 70. ad − bc = 25,900 − 55,900 = −30,000; (ad − bc)² = 9 × 10⁸.
3. χ² = 1000 × 9 × 10⁸/(800 × 200 × 500 × 500) = 9 × 10¹¹/(4 × 10¹⁰) = **22.5**.
4. df = 1; 22.5 > 3.841: **reject H₀**. Income and type of school are associated (the data support the belief).

Cross-check by the long way: E = 400, 400, 100, 100; contributions 2.25 + 2.25 + 9 + 9 = 22.5. Answer to the guess: yes, far above.

:::check Check 6
Recompute A5 C3's χ² with the shortcut.
:::

### 7 · Building the table from a story

Some questions give only some counts in words. The table has to be completed by subtraction before any formula.

:::q <span class="tag">A5 B5</span>
In a certain sample of 2,000 families, 1,400 are consumers of tea. Out of 1,800 Hindu families, 1,236 families consume tea. State whether there is any significant difference between consumption of tea among Hindu and non-Hindu families. (Tabulated value 3.841.)
:::

:::guess Guess first
How many non-Hindu families are there, and how many of them drink tea?
:::

:::note Terms
**"Significant difference between groups" for counts:** the same question as "are the attributes (group, tea) independent?". If the tea share does not depend on the group, the attributes are independent.
:::

Fill by subtraction (each step uses one total):

| | Tea | No tea | Total |
|---|---|---|---|
| Hindu | 1236 | 1800 − 1236 = 564 | 1800 |
| Non-Hindu | 1400 − 1236 = 164 | 200 − 164 = 36 | 2000 − 1800 = 200 |
| Total | 1400 | 2000 − 1400 = 600 | 2000 |

Shares: Hindu 1236/1800 = 68.7% drink tea; non-Hindu 164/200 = 82%; all families 70%.

**Answer to the question.**

1. H₀: tea consumption is independent of community (no difference); H₁: it differs.
2. E = R × C/N: 1800 × 1400/2000 = 1260; then 540, 140, 60 from the totals.
3. Contributions, (O − E)² = 24² = 576 in every cell: 576/1260 + 576/540 + 576/140 + 576/60 = 0.4571 + 1.0667 + 4.1143 + 9.6000.
4. χ² = **15.24**, df 1; 15.24 > 3.841: **reject H₀**. Tea consumption differs significantly between Hindu and non-Hindu families.

The shortcut agrees: 2000 × (1236 × 36 − 564 × 164)²/(1800 × 200 × 1400 × 600) = 15.24. Answer to the guess: 200 non-Hindu families, 164 of them drink tea.

:::check Check 7
Of 500 students, 300 passed. Of the 200 girls, 140 passed. Write the full 2 × 2 table, find χ² with the shortcut and decide at 5%.
:::

### 8 · A 3 × 3 table

The same formula works for any r × c table; only the number of cells and the df grow.

:::q <span class="tag">A5 B6</span>
An oil corporation runs a seismic test on land to assess whether oil can be extracted. From 200 past records:

| Test result | High | Medium | Low | Total |
|---|---|---|---|---|
| Good | 44 | 22 | 13 | 79 |
| Fair | 15 | 19 | 26 | 60 |
| Bad | 6 | 8 | 47 | 61 |
| Total | 65 | 49 | 86 | 200 |

Can we say, at the 1% level of significance, that oil yields and test results are associated? (Tabulated value 13.28.)
:::

:::guess Guess first
Look at the corners: Good–High 44, Bad–Low 47, Good–Low 13, Bad–High 6. Association or not?
:::

:::note Terms
**Contribution of a cell:** its (O − E)²/E; the cells with the largest contributions show **where** the table departs from independence. **χ²₀.₀₁(4):** the 1% table value for (3 − 1)(3 − 1) = 4 df, 13.28.
:::

E = R × C/200 for each cell (row totals 79, 60, 61; column totals 65, 49, 86):

| | High | Medium | Low |
|---|---|---|---|
| Good | 25.68 | 19.36 | 33.97 |
| Fair | 19.50 | 14.70 | 25.80 |
| Bad | 19.83 | 14.95 | 26.23 |

Every E is at least 5 (smallest 14.70), so the test applies.

[[fig:oil_contrib|What this graph plots: one square per cell of A5 B6's table; the colour and the top number give that cell's contribution (O − E) squared over E, the line below gives O and E. Darker squares are where the records depart most from independence.|w=80]]

**Answer to the question.**

1. H₀: oil yield and test result are independent; H₁: associated.
2. Contributions (O − E)²/E: Good 13.08, 0.36, 12.94; Fair 1.04, 1.26, 0.00; Bad 9.64, 3.23, 16.45.
3. χ² = **58.00**; df = (3 − 1)(3 − 1) = 4; χ²₀.₀₁(4) = 13.28.
4. 58.00 > 13.28: **reject H₀** at 1%. Oil yield and test result are associated: a Good result goes with High yield (44 against 25.68 expected), a Bad result with Low yield (47 against 26.23).

Answer to the guess: association. The corners are far from what independence predicts.

:::check Check 8
Which three cells contribute most to χ² in A5 B6, and is each one above or below its expected count?
:::

---

## Exam form

**Statement** (G&K §13.7.3). For N units classified by two attributes into an r × c contingency table, under H₀: the attributes are independent, the expected frequencies are Eᵢⱼ = RᵢCⱼ/N and χ² = Σ(O − E)²/E approximately follows the χ² distribution with (r − 1)(c − 1) df (large N).

**Procedure.**

1. Complete the table (fill missing cells from the totals); write Rᵢ, Cⱼ, N.
2. H₀: the attributes are independent; H₁: associated.
3. Eᵢⱼ = RᵢCⱼ/N; check every E ≥ 5 and N > 50.
4. χ² = Σ(O − E)²/E; for a 2 × 2 table, χ² = N(ad − bc)²/[(a + b)(c + d)(a + c)(b + d)].
5. df = (r − 1)(c − 1); table value χ²_{α}(df) from the right tail.
6. χ² > table value: reject H₀ (associated); otherwise the attributes may be taken as independent. Conclude in the words of the question.

**Table values used.** χ²₀.₀₅: 3.841 (1 df), 5.991 (2 df), 9.488 (4 df), 12.592 (6 df). χ²₀.₀₁: 6.635 (1 df), 13.28 (4 df).

## Traps

- E = R × C, forgetting ÷ N (A5 A7's option B).
- df = rc − 1: that counts only one constraint; independence fixes both sets of totals, so (r − 1)(c − 1).
- Leaving a story's table incomplete (A5 B5): fill every cell by subtraction first.
- Putting percentages into the formula: χ² needs counts.
- Treating χ² as two-tailed: only large values reject.
- Using the test with an expected count below 5: pool cells first.

## Self-test

1. State H₀ and the χ² statistic for a test of independence, with its df.
2. Give the expected-frequency formula and the reason behind it.
3. A 2 × 2 table: a = 20, b = 30, c = 30, d = 20. Find χ² and decide at 5%.
4. Why must every expected frequency be at least 5?
5. A 2 × 3 table gives χ² = 7.2. Decide at 5% (χ²₀.₀₅(2) = 5.991).

<!--ANSWERS-->
## Answers

**Check 1.** Boys: 30 passed, 30 failed (60). Girls: 20 passed, 20 failed (40). Totals: 50 passed, 50 failed, 100. Pass share 50% in both rows (and overall): no sign that passing depends on gender. Here every O equals its E, so χ² = 0.

**Check 2.** Low income, public: 800 × 500/1000 = **400**. Then low, government 800 − 400 = **400**; high, public 500 − 400 = **100**; high, government 200 − 100 = **100**.

**Check 3.** (a) O and E have the same row and column totals, so a miss of +k in one cell forces −k in its row-mate, −k in its column-mate and +k in the opposite cell. (b) All totals are 50 and N = 100, so every E = 50 × 50/100 = 25; each contribution 5²/25 = 1; χ² = **4**.

**Check 4.** (a) (4 − 1)(3 − 1) = **6**. (b) (2 − 1)(3 − 1) = **2**. (c) **6** cells from R × C/N (one per df); the other 6 follow from the totals.

**Check 5.** (a) 2.9 < 3.841: do not reject; the attributes may be taken as independent. (b) No: 14.06 > 6.635, still reject.

**Check 6.** 300 × (75 × 95 − 105 × 25)²/(180 × 120 × 100 × 200) = 300 × 4500²/432,000,000 = 6,075,000,000/432,000,000 = **14.06** ✓.

**Check 7.** Girls: 140 passed, 60 failed (200). Boys: 160 passed, 140 failed (300). Totals: 300 passed, 200 failed, 500. ad − bc = 140 × 140 − 60 × 160 = 19,600 − 9,600 = 10,000. χ² = 500 × 10⁸/(200 × 300 × 300 × 200) = 5 × 10¹⁰/(3.6 × 10⁹) = **13.89** > 3.841: reject H₀; passing and gender are associated (girls 70%, boys 53%).

**Check 8.** Bad–Low 16.45 (47 observed, above 26.23), Good–High 13.08 (44, above 25.68), Good–Low 12.94 (13, below 33.97). The test result predicts the yield.

**Self-test.**

1. H₀: the attributes are independent; χ² = Σ(O − E)²/E with (r − 1)(c − 1) df.
2. Eᵢⱼ = RᵢCⱼ/N: under independence P(row and column) = P(row) × P(column) = (Rᵢ/N)(Cⱼ/N); multiply by N.
3. N = 100; ad − bc = 400 − 900 = −500; χ² = 100 × 250,000/(50 × 50 × 50 × 50) = **4** > 3.841: reject (associated).
4. χ² = Σ(O − E)²/E only approximately follows the χ² curve; G&K: the approximation fails ("cannot maintain its character of continuity") when an expected frequency is below 5.
5. 7.2 > 5.991: **reject H₀**.
<!--/ANSWERS-->
