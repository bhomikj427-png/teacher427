# 15 — Chi-square test of independence of attributes

<div class="sub">Gupta & Kapoor §13.5, §13.7 (Example 13.17) · blueprint row 5 "chi-square test" · 8 real questions (Assignment 5) · needs 01 (independence), 12 (test steps)</div>

## Map

[[map:1 Contingency table and expected frequency > 2 The χ² statistic and its df > 3 A 2 × 2 test > 4 The 2 × 2 shortcut > 5 Building the table from a story > 6 A 3 × 3 table|here=1]]

## The questions this file answers

- <span class="tag">A5 C3</span> 300 men: smokers 75 with lung ailment, 105 without; non-smokers 25 with, 95 without. Are smoking and lung ailments independent? (Table value 3.841.)
- <span class="tag">A5 D3</span> 1000 families: low income 370 public / 430 government school; high income 130 / 70. Are income and type of schooling independent? (Table value 3.841.)
- <span class="tag">A5 B5</span> Of 2000 families, 1400 consume tea; of 1800 Hindu families, 1236 consume tea. Is tea consumption different for Hindu and non-Hindu families? (Table value 3.841.)
- <span class="tag">A5 B6</span> 200 seismic tests: results Good / Fair / Bad against oil yield High / Medium / Low (44, 22, 13; 15, 19, 26; 6, 8, 47). Are oil yield and test result associated at 1%? (Table value 13.28.)
- <span class="tag">A5 A3, A6, A7, A8</span> Which test checks independence of attributes; expected frequency formula; df for an r × c table.

---

## Build

### 1 · Contingency table and expected frequency

Files 13–14 tested means and variances of measurements. Some data are only **counts in categories**.

:::q <span class="tag">A5 A7 · 2 marks</span>
The expected frequency in a cell of a contingency table, under the hypothesis of independence, is calculated as: (A) row total + column total (B) row total × column total (C) (row total × column total)/grand total (D) grand total/row total
:::

:::guess Guess first
180 of 300 men smoke and 100 of 300 have an ailment. If smoking and ailment were unrelated, how many smokers with an ailment would you expect?
:::

**Terms.**

- **Attribute**: a qualitative characteristic (smoker or not, income group).
- **Contingency table**: counts of N units cross-classified by two attributes, r rows × c columns.
- **Expected frequency E**: the count a cell would have if the attributes were independent.

From file 01: independent ⇒ P(row i and column j) = P(row i) × P(column j). Multiplying by N:

$$E_{ij} = N × \frac{R_{i}}{N} × \frac{C_{j}}{N} = \frac{R_{i} × C_{j}}{N}$$

**Answer.** **(C)**. Smokers with ailment: E = 180 × 100/300 = **60** (observed 75).

:::check Check 1
Find the other three expected frequencies for the smoking table (row totals 180, 120; column totals 100, 200).
:::

### 2 · The χ² statistic and its degrees of freedom

Expected counts in hand, one number measures how far the observed table is from them.

:::q <span class="tag">A5 A8 · 2 marks</span>
For a chi-square test of independence in an r × c contingency table, the degrees of freedom are: (A) rc − 1 (B) r + c − 2 (C) (r − 1)(c − 1) (D) (r − 1)c
:::

:::guess Guess first
In a 2 × 2 table with fixed totals, fill in one cell. How many others are then forced?
:::

**Statistic** (G&K §13.7), H₀: the two attributes are independent:

$$χ^{2} = Σ \frac{(O − E)^{2}}{E},    df = (r − 1)(c − 1)$$

Large χ^{2} = observed far from independence ⇒ reject H₀. The test is always **right-tailed**.

**Answer.** **(C)**. With row and column totals fixed, only (r − 1)(c − 1) cells can be filled freely; the rest follow. A 2 × 2 table has 1 df.

<span class="tag">A5 A3</span> The test of independence of attributes is based on the **χ^{2}** test. <span class="tag">A5 A6</span> It is the **chi-square test of independence** (C).

**Conditions** (G&K §13.5): N reasonably large (≥ 50), every expected frequency at least 5 (pool small cells otherwise), observations independent.

:::check Check 2
Find the df for a 4 × 3 table, and the number of cells whose expected frequency must be computed from the formula before the rest follow by subtraction.
:::

### 3 · A 2 × 2 test

:::q <span class="tag">A5 C3</span>
A tobacco company claims that there is no relationship between smoking and lung ailments. A random sample of 300 males aged 40–50 are given a medical test:

| | Lung ailment | No lung ailment | Total |
|---|---|---|---|
| Smokers | 75 | 105 | 180 |
| Non-smokers | 25 | 95 | 120 |
| Total | 100 | 200 | 300 |

Can it be concluded that smoking and lung ailments are independent? (Table value 3.841.)
:::

:::guess Guess first
75 observed against 60 expected. Do you expect χ^{2} above or below 3.841?
:::

[[fig:obs_exp|Observed counts against the counts independence predicts.|w=75]]

**Answer.** H₀: smoking and lung ailment are independent. df = 1; χ^{2}₀.₀₅ = 3.841.

| Cell | O | E | (O − E)^{2}/E |
|---|---|---|---|
| smoker, ailment | 75 | 60 | 225/60 = 3.750 |
| smoker, none | 105 | 120 | 225/120 = 1.875 |
| non-smoker, ailment | 25 | 40 | 225/40 = 5.625 |
| non-smoker, none | 95 | 80 | 225/80 = 2.8125 |

χ^{2} = **14.06** > 3.841 ⇒ **reject H₀**: smoking and lung ailments are associated. The company's claim is not supported.

[[fig:chi_curve|14.06 lies far into the 5% tail of χ² with 1 df.|w=70]]

:::check Check 3
In a 2 × 2 table every |O − E| is the same number. Why?
:::

### 4 · The 2 × 2 shortcut

For a 2 × 2 table one formula replaces the four-row table.

:::q <span class="tag">A5 D3</span>
1,000 families were selected at random to test the belief that high-income families usually send their children to public schools and low-income families to government schools:

| Income | Public | Government | Total |
|---|---|---|---|
| Low | 370 | 430 | 800 |
| High | 130 | 70 | 200 |
| Total | 500 | 500 | 1000 |

Test whether income and type of schooling are independent. (Table value 3.841.)
:::

:::guess Guess first
Low-income families split 370 : 430; high-income 130 : 70. Same pattern or different?
:::

**Shortcut** (G&K Example 13.17): for the table with cells a, b (first row) and c, d (second row),

$$χ^{2} = \frac{N(ad − bc)^{2}}{(a + b)(c + d)(a + c)(b + d)}$$

**Answer.** a = 370, b = 430, c = 130, d = 70.
ad − bc = 25,900 − 55,900 = −30,000; (ad − bc)^{2} = 9 × 10^{8}.
χ^{2} = 1000 × 9 × 10^{8}/(800 × 200 × 500 × 500) = 9 × 10^{11}/(4 × 10^{10}) = **22.5** > 3.841 ⇒ **reject H₀**: income and type of school are associated.

:::check Check 4
Recompute the smoking table's χ^{2} with the shortcut.
:::

### 5 · Building the table from a story

Some questions give only some of the counts. Fill the table by subtraction first.

:::q <span class="tag">A5 B5</span>
In a sample of 2,000 families, 1,400 are consumers of tea. Out of 1,800 Hindu families, 1,236 consume tea. State whether there is any significant difference between consumption of tea among Hindu and non-Hindu families. (Table value 3.841.)
:::

:::guess Guess first
Hindu: 1236/1800 = 69% drink tea. Non-Hindu: find the percentage before testing.
:::

**Answer.** Fill by subtraction:

| | Tea | No tea | Total |
|---|---|---|---|
| Hindu | 1236 | 564 | 1800 |
| Non-Hindu | 164 | 36 | 200 |
| Total | 1400 | 600 | 2000 |

Non-Hindu tea drinkers: 164/200 = 82%. H₀: tea consumption is independent of community.
Expected: 1260, 540, 140, 60. Contributions: 576/1260 + 576/540 + 576/140 + 576/60 = 0.4571 + 1.0667 + 4.1143 + 9.6000.
χ^{2} = **15.24** > 3.841 ⇒ **reject H₀**: tea consumption differs significantly between the two groups.

:::check Check 5
Of 500 students, 300 passed. Of the 200 girls, 140 passed. Write the full 2 × 2 table.
:::

### 6 · A 3 × 3 table

Larger tables use the same formula with more cells and more df.

:::q <span class="tag">A5 B6</span>
An oil corporation's seismic test assesses whether land can yield oil. From 200 past records:

| Test result | High | Medium | Low | Total |
|---|---|---|---|---|
| Good | 44 | 22 | 13 | 79 |
| Fair | 15 | 19 | 26 | 60 |
| Bad | 6 | 8 | 47 | 61 |
| Total | 65 | 49 | 86 | 200 |

Can we say, at the 1% level, that oil yields and test results are associated? (Table value 13.28.)
:::

:::guess Guess first
Look at the diagonal (Good–High, Bad–Low). Association or not?
:::

**Answer.** H₀: yield and test result are independent. df = (3 − 1)(3 − 1) = 4; χ^{2}₀.₀₁ = 13.28.
E = R × C/200:

| | High | Medium | Low |
|---|---|---|---|
| Good | 25.68 | 19.36 | 33.97 |
| Fair | 19.50 | 14.70 | 25.80 |
| Bad | 19.83 | 14.95 | 26.23 |

(O − E)^{2}/E: Good 13.08, 0.36, 12.94; Fair 1.04, 1.26, 0.00; Bad 9.64, 3.23, 16.45.
χ^{2} = **58.00** > 13.28 ⇒ **reject H₀**: test results and oil yield are associated (a good test result goes with high yield).

:::check Check 6
Which three cells contribute most to χ^{2} here, and what do they say about the test?
:::

---

## Exam form

**Hypothesis.** H₀: the two attributes are independent; H₁: they are associated.

**Procedure.**

1. Complete the contingency table (row totals Rᵢ, column totals Cⱼ, N).
2. Expected frequencies Eᵢⱼ = RᵢCⱼ/N (check every E ≥ 5).
3. χ^{2} = Σ(O − E)^{2}/E (or, for 2 × 2, N(ad − bc)^{2}/[(a + b)(c + d)(a + c)(b + d)]).
4. df = (r − 1)(c − 1).
5. χ^{2} > χ^{2}_{α} (table) ⇒ reject H₀ (associated); otherwise independent.

**Table values used.** χ^{2}₀.₀₅: 3.841 (1 df), 9.488 (4 df). χ^{2}₀.₀₁: 6.635 (1 df), 13.28 (4 df).

## Traps

- E = R × C (forgetting ÷ N).
- df = rc − 1: that is for goodness of fit to fixed proportions, not independence.
- Leaving a table incomplete: always fill the missing cells by subtraction first.
- Using percentages instead of counts in the formula.
- Treating χ^{2} as two-tailed: only large values reject.

## Self-test

1. State H₀ and the χ^{2} statistic for a test of independence, with its df.
2. Give the expected-frequency formula and the reason behind it.
3. A 2 × 2 table: a = 20, b = 30, c = 30, d = 20. Find χ^{2} and decide at 5%.
4. Why must every expected frequency be at least 5?
5. A 2 × 3 table gives χ^{2} = 7.2. Decide at 5% (χ^{2}₀.₀₅,₂ = 5.991).

<!--ANSWERS-->
## Answers

**Check 1.** Smoker, none: 180 × 200/300 = **120**. Non-smoker, ailment: 120 × 100/300 = **40**. Non-smoker, none: 120 × 200/300 = **80**.

**Check 2.** df = 3 × 2 = **6**; 6 cells from the formula, the rest by subtraction from the totals.

**Check 3.** Row and column totals are fixed and equal in O and E, so a +k in one cell forces −k in its row-mate and column-mate and +k in the opposite cell.

**Check 4.** 300 × (75 × 95 − 105 × 25)^{2}/(180 × 120 × 100 × 200) = 300 × 4500^{2}/432,000,000 = **14.06** ✓.

**Check 5.** Girls: 140 passed, 60 failed (200). Boys: 160 passed, 140 failed (300). Totals: 300 passed, 200 failed, 500.

**Check 6.** Good–High (13.08, more than expected), Good–Low (12.94, fewer than expected), Bad–Low (16.45, more than expected): the test result predicts the yield.

**Self-test.**

1. H₀: independent; χ^{2} = Σ(O − E)^{2}/E with (r − 1)(c − 1) df.
2. Eᵢⱼ = RᵢCⱼ/N; under independence P(row and column) = P(row)P(column).
3. N = 100; ad − bc = 400 − 900 = −500; χ^{2} = 100 × 250,000/(50 × 50 × 50 × 50) = **4** > 3.841: reject (associated).
4. The χ^{2} distribution is only a good approximation when expected counts are not small.
5. 7.2 > 5.991: **reject H₀**.
<!--/ANSWERS-->
