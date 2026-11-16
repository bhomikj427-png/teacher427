# 12 — Hypotheses, critical region, Type I and Type II errors

<div class="sub">Professor's slides "ppt 8 Hypothesis Testing" (26 slides) · Gupta & Kapoor §12.4–12.7, §16.2–16.3 · blueprint row 4 "null and alternative hypotheses, level of significance, critical region, Type I and Type II errors" · 15 real questions (Assignments 4, 5, slides) · needs 04a, 04b, 05, 07</div>

## Map

[[map:1 Null and alternative hypotheses > 2 One- and two-tailed > 3 Type I and Type II errors > 4 Significance level and critical region > 5 α and β for a continuous test > 6 α and β for a discrete test > 7 The steps of every test|here=1]]

## The questions this file answers

- <span class="tag">Slides p.9</span> A university publicises that the proportion of its students who graduate in 4 years is 82%. State H₀ and H₁.
- <span class="tag">Slides p.10</span> A manufacturer claims its batteries last at least 1,000 charges on average. State H₀ and H₁; which is the claim?
- <span class="tag">Slides p.14</span> A college claims 94% of graduates find jobs within six months. What would a Type I and a Type II error be?
- <span class="tag">A4 C1</span> f(x, θ) = 1/θ, 0 ≤ x ≤ θ; test H₀: θ = 1 against H₁: θ = 2 with one observation. Sizes of Type I and II errors for the critical regions (i) x ≥ 0.5 (ii) 1 ≤ x ≤ 1.5.
- <span class="tag">A4 C2</span> Coin tossed 5 times to test H₀: p = ½ against H₁: p = ¾; reject H₀ if more than 3 heads. Find α and β.
- <span class="tag">A4 C3</span> H₀: p = 0.75 against H₁: p = 0.5 with 4 products; reject if fewer than 3 meet specifications. Find α and β.
- <span class="tag">A4 MCQ 1–7</span> · <span class="tag">A5 A1(i)–(iv)</span> Definitions: alternative hypothesis, critical region, Type I/II, β, one- and two-tailed tests, significance level.

Row 4 is 10 marks: two 2-mark items and one 6-mark item. An α-and-β calculation like A4 C1–C3 fits the 6-mark slot.

---

## Build

### 1 · Null and alternative hypotheses

Files 08–11 estimated a parameter. Testing asks a yes/no question about it.

:::q <span class="tag">Slides p.9</span>
State the null and alternative hypotheses for the following problem: a university publicises that the proportion of its students who graduate in 4 years is 82%.
:::

:::guess Guess first
Which statement contains "="? Write H₀ and H₁.
:::

**Terms** (slides p.2–7; G&K §12.5):

- **Statistical hypothesis**: a statement about a population parameter that can be tested with data.
- **Null hypothesis H₀**: the status quo, "no difference"; always contains =, ≤ or ≥. The test **assumes H₀ is true** and asks whether the data contradict it.
- **Alternative hypothesis H₁ (Hₐ)**: what is accepted if H₀ is rejected; contains ≠, < or >; usually what the researcher wants to show.

**Answer.** p = 0.82 contains equality: **H₀: p = 0.82, H₁: p ≠ 0.82**.

<span class="tag">A4 MCQ 1</span> The alternative hypothesis represents **the claim that contradicts the null** (B).

:::check Check 1
<span class="tag">A4 MCQ 6</span> A researcher wants to test whether the average weight of newborns is **less than** 3 kg. Which H₁ is correct: μ = 3, μ < 3, μ > 3, μ ≠ 3?
:::

### 2 · One-tailed and two-tailed tests

The form of H₁ decides where the evidence against H₀ lies.

:::q <span class="tag">Slides p.10</span>
Write the claim as a mathematical sentence. State the null and alternative hypotheses and identify which represents the claim: a manufacturer claims that its rechargeable batteries have an average life of **at least** 1,000 charges.
:::

:::guess Guess first
"At least 1,000" is μ ? 1000. Does that go in H₀ or H₁?
:::

**Answer.** "At least" = μ ≥ 1000, which contains equality: **H₀: μ ≥ 1000 (the claim), H₁: μ < 1000**. H₁ is the complement of H₀.

**Terms** (G&K §12.7):

- **Two-tailed test**: H₁: μ ≠ μ₀; evidence in either direction.
- **One-tailed test**: H₁: μ > μ₀ (right-tailed) or μ < μ₀ (left-tailed).

[[fig:two_tails|Same α = 0.05, placed in one tail or split between two.|w=95]]

:::note Slide slip
Slide 7's milk example (on the alternative hypothesis) writes the alternative as "H₀: μ > −0.545 °C". It is the **alternative**: H₁: μ > −0.545 °C (added water raises the freezing point), a right-tailed test.
:::

:::check Check 2
Classify as one- or two-tailed: (a) H₁: p ≠ 0.94 (b) a new process **reduces** mean defects below 5 (c) a coin is **not fair**.
:::

### 3 · Type I and Type II errors

A test decides from a sample, so it can be wrong in two ways.

:::q <span class="tag">Slides p.14</span>
Statesville college claims that 94% of their graduates find employment within six months of graduation. What will a Type I or a Type II error be?
:::

:::guess Guess first
Write H₀ first. Then: what is the mistake if we reject it but it was true?
:::

**Terms** (slides p.11–16, 23; G&K §12.6):

| Decision ↓ / Truth → | H₀ true | H₀ false |
|---|---|---|
| Do not reject H₀ | correct | **Type II error** (false negative), probability **β** |
| Reject H₀ | **Type I error** (false positive), probability **α** | correct; probability **1 − β = power** |

The slides' examples: Type I = the shepherd "crying wolf" when there is no wolf; Type II = failing to detect that fluoride does protect against cavities.

**Answer.** H₀: p = 0.94, H₁: p ≠ 0.94. **Type I**: the true proportion is 0.94, but H₀ is rejected (we conclude it is not 0.94). **Type II**: the true proportion is not 0.94, but H₀ is not rejected (we keep believing 0.94).

<span class="tag">A4 MCQ 4</span> Concluding a medicine works when it does not: **Type I** (A). <span class="tag">A4 MCQ 5</span> A Type II error is **failing to reject a false H₀** (C). <span class="tag">A4 MCQ 7</span> Its probability is **β** (B).

:::check Check 3
A court's H₀ is "the accused is innocent". Describe its Type I and Type II errors.
:::

### 4 · Significance level and critical region

α is chosen before the data; it fixes where "reject" starts.

:::q <span class="tag">A4 MCQ 2 · 1 mark</span>
The critical region in hypothesis testing is the region in which we: (A) always accept H₀ (B) reject H₀ (C) calculate the sample mean (D) increase the sample size.
:::

:::guess Guess first
Pick an option.
:::

**Terms** (slides p.24–25; G&K §12.7):

- **Level of significance α**: the maximum allowed probability of a Type I error, fixed in advance (0.10, 0.05, 0.01).
- **Critical (rejection) region W**: the values of the test statistic for which H₀ is rejected. Its complement is the acceptance region.
- **Critical value**: the boundary between them.

$$α = P(x ∈ W | H₀),    β = P(x ∉ W | H₁),    power = 1 − β = P(x ∈ W | H₁)$$

**Answer.** **(B)**: H₀ is rejected when the statistic falls in the critical region.

Critical values for z:

| α | Two-tailed | Right-tailed | Left-tailed |
|---|---|---|---|
| 0.05 | ±1.96 | 1.645 | −1.645 |
| 0.01 | ±2.576 | 2.326 | −2.326 |

:::check Check 4
For a fixed sample size, what happens to β if α is made smaller? Why?
:::

### 5 · α and β for a continuous test

The 6-mark question gives the distributions under H₀ and H₁ and a critical region: both errors are areas.

:::q <span class="tag">A4 C1</span>
Given the frequency function f(x, θ) = 1/θ, 0 ≤ x ≤ θ (0 otherwise), you test H₀: θ = 1 against H₁: θ = 2 by means of a single observed value x. What are the sizes of the Type I and Type II errors if you choose as critical region (i) 0.5 ≤ x (ii) 1 ≤ x ≤ 1.5?
:::

:::guess Guess first
Under H₀, X ~ U(0, 1); under H₁, X ~ U(0, 2). For (i), guess α and β.
:::

[[fig:alpha_beta|Red: rejecting when H₀ is true (α). Amber: accepting when H₁ is true (β).|w=80]]

**Answer.**
(i) W = {x ≥ 0.5}. α = P(X ≥ 0.5 | θ = 1) = (1 − 0.5)/1 = **0.5**. β = P(X < 0.5 | θ = 2) = 0.5/2 = **0.25**.
(ii) W = {1 ≤ x ≤ 1.5}. α = P(1 ≤ X ≤ 1.5 | θ = 1) = **0** (under H₀, X never exceeds 1). β = 1 − P(1 ≤ X ≤ 1.5 | θ = 2) = 1 − 0.5/2 = **0.75**.
Region (ii) never makes a Type I error but misses H₁ three times in four.

:::check Check 5
<span class="tag">Slides p.21</span> X has f(x, θ) = (1/θ)e^{−x/θ}, x ≥ 0. H₀: θ = 5 is rejected in favour of H₁: θ = 10 if the observation is 15 or more. Find α and β.
:::

### 6 · α and β for a discrete test

With a count (file 04a's binomial), the areas become sums of probabilities.

:::q <span class="tag">A4 C2</span>
Let p be the probability that a coin falls heads. To test H₀: p = ½ against H₁: p = ¾, the coin is tossed 5 times and H₀ is rejected if more than 3 heads are obtained. Find the probability of Type I error (and of Type II error).
:::

:::guess Guess first
Write W as a set of head-counts. Then α uses which p?
:::

**Answer.** X = heads ~ B(5, p); W = {4, 5}.
α = P(X ≥ 4 | p = ½) = (C(5, 4) + C(5, 5)) × (½)^{5} = (5 + 1)/32 = **3/16**.
β = P(X ≤ 3 | p = ¾) = 1 − [C(5, 4)(¾)^{4}(¼) + (¾)^{5}] = 1 − (405 + 243)/1024 = 376/1024 = **47/128**.
Power = 1 − 47/128 = 81/128.

:::check Check 6
<span class="tag">A4 C3</span> A manufacturer claims 75% of products meet specifications. 4 products are tested: H₀: p = 0.75 against H₁: p = 0.5; reject H₀ if fewer than 3 meet them. Find α and β.
:::

### 7 · The steps of every test

Files 13–16 run the same procedure with different statistics.

:::q Predict
For a test about a mean, list in order what you would write in an exam answer, from the hypotheses to the conclusion.
:::

:::guess Guess first
Write your list of steps.
:::

**The steps** (G&K §16.3):

1. State H₀ and H₁ (and one- or two-tailed).
2. Choose α.
3. Choose the test statistic and its distribution under H₀ (z, t, F or χ^{2}) with its df.
4. Compute it from the data.
5. Find the critical value from the table.
6. Decide: |calculated| > tabulated ⇒ reject H₀; otherwise do not reject.
7. Conclude in the words of the problem.

**The statistic** always has the shape (estimate − value under H₀)/SE: the SE of file 07, in the numerator's units.

:::check Check 7
A two-tailed z-test at α = 0.05 gives z = −2.3. State the decision and the reason.
:::

---

## Exam form

**Definitions.** Statistical hypothesis · null hypothesis H₀ (status quo; =, ≤, ≥) · alternative H₁ (≠, <, >) · one-tailed / two-tailed test · Type I error (reject true H₀), probability α · Type II error (accept false H₀), probability β · power 1 − β · level of significance (maximum α) · critical region W (reject H₀ when the statistic is in W) · critical value.

**Formulas.** α = P(x ∈ W | H₀) · β = P(x ∈ W̄ | H₁) · power = P(x ∈ W | H₁).

**Procedure for α, β.** (1) Write W and its complement W̄. (2) α: probability of W under H₀'s distribution. (3) β: probability of W̄ under H₁'s distribution. (4) Power = 1 − β if asked.

## Traps

- Putting the claim in H₀ automatically: the hypothesis with = (or ≤, ≥) is H₀, claim or not.
- Computing β under H₀: β always uses H₁'s distribution.
- "Accept H₀" means "do not reject": the data did not contradict it; it is not proved.
- "More than 3" is X ≥ 4; "fewer than 3" is X ≤ 2.
- Swapping α (Type I) and β (Type II).

## Self-test

1. Define Type I error, Type II error and power.
2. State H₀ and H₁: "the mean life of a tyre is 40,000 km"; "the new drug lowers mean blood pressure".
3. What is a critical region? What is a critical value?
4. One observation from U(0, θ). H₀: θ = 1, H₁: θ = 1.5; reject H₀ if x > 0.9. Find α and β.
5. B(4, p): H₀: p = 1/3 against H₁: p = ½; accept H₀ if x ≤ 2. Find α and β.
6. Why can α and β not both be made very small without increasing n?

<!--ANSWERS-->
## Answers

**Check 1.** **μ < 3** (B).

**Check 2.** (a) two-tailed (b) one-tailed (left) (c) two-tailed.

**Check 3.** Type I: convicting an innocent person. Type II: acquitting a guilty person.

**Check 4.** β increases: shrinking W enlarges the acceptance region, so more false H₀ are accepted.

**Check 5.** α = P(X ≥ 15 | θ = 5) = e^{−15/5} = **e^{−3} = 0.0498**. β = P(X < 15 | θ = 10) = **1 − e^{−1.5} = 0.7769**.

**Check 6.** α = P(X ≤ 2 | p = 0.75) = 0.0039 + 0.0469 + 0.2109 = **0.2617**. β = P(X ≥ 3 | p = 0.5) = (4 + 1)/16 = **0.3125**.

**Check 7.** |z| = 2.3 > 1.96: **reject H₀** at the 5% level.

**Self-test.**

1. Type I: rejecting H₀ when it is true (α). Type II: not rejecting H₀ when it is false (β). Power: P(reject H₀ | H₁ true) = 1 − β.
2. H₀: μ = 40,000, H₁: μ ≠ 40,000. H₀: μ_{new} = μ_{old} (or ≥), H₁: μ_{new} < μ_{old}.
3. The set of statistic values leading to rejection of H₀; the boundary value(s) of that set.
4. α = P(X > 0.9 | θ = 1) = **0.1**. β = P(X ≤ 0.9 | θ = 1.5) = 0.9/1.5 = **0.6**.
5. α = P(X ≥ 3 | 1/3) = 4(1/27)(2/3) + 1/81 = 8/81 + 1/81 = **1/9**. β = P(X ≤ 2 | ½) = 1 − 5/16 = **11/16** (slides p.20).
6. For fixed n, enlarging the acceptance region lowers α but raises β, and the reverse; only more data reduces both.
<!--/ANSWERS-->
