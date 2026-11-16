# 08 — Estimators and the four properties of a good one

<div class="sub">Gupta & Kapoor ch. 15 (§15.1–15.6), §12.11 · blueprint row 3 "parameter and statistic, point and interval estimation; characteristics of a good estimator" · 3 real questions (MTE C1(b), MTE A3; G&K ch. 15 objective Q1) · needs 01 (two-dice grid step 1), 03a (E step 1, Var step 4), 03b (rules for sums steps 2–3)</div>

## Map

[[map:1 Parameter, statistic, estimate > 2 Point and interval > 3 Unbiased > 4 Checking a formula > 5 Why s² divides by n − 1 > 6 Consistent > 7 Efficient > 8 Sufficient|here=1]]

In real problems the population's mean μ and variance σ² are unknown; only a sample is seen. A formula that turns the sample into a guess for μ (or σ²) is an **estimator**. Many formulas are possible, so this file sets out how to judge one: by how its guesses behave over **all the samples you might have drawn**. To make "all the samples" something you can actually list, the running example uses a population you know completely. Files 09a and 09b then build estimators (method of moments, maximum likelihood) and file 11 turns them into intervals.

| Symbol | What it means in this file | Typical value |
|---|---|---|
| θ | a parameter: a fixed but unknown number describing the population ("theta") | θ = μ = 3.5 |
| X₁, X₂, …, Xₙ | the sample: n independent draws from the population | two throws, n = 2 |
| T | an estimator: a formula in X₁, …, Xₙ used to guess θ; it varies from sample to sample | T = x̄ |
| E(T) | the long-run average of T over all possible samples (03a step 1) | 3.5 |
| bias | E(T) − θ: how far T's average misses the target | 0 for x̄ |
| Var(T) | the spread of T over all possible samples (03a step 4) | σ²/n |
| s² | the sample variance, Σ(xᵢ − x̄)²/(n − 1) | 4 for data 4, 6, 8 |

**Running example.** The population is one fair die's faces: μ = 3.5, σ² = 35/12 ≈ 2.92 (03a Checks 1 and 5). A sample of size n is n throws. For n = 2 there are exactly 36 possible samples, the cells of 01's dice grid, so "the average over all samples" is an average over 36 cells. Every step uses it.

## The questions this file answers

- <span class="tag">MTE C1(b) · 3 marks</span> Let X₁, X₂, X₃ be a random sample of size 3 from a population with mean μ and variance σ². T₁ = X₁ + X₂ − X₃ and T₂ = 3X₁ + 2X₃ − 3X₂ are used to estimate μ. Which of T₁, T₂ is unbiased? Justify.
- <span class="tag">MTE A3 · 2 marks</span> If an estimator t contains all the information of the sample regarding the population parameter θ, it is called: (a) efficient (b) sufficient (c) consistent (d) unbiased.
- <span class="tag">G&K ch. 15 objective Q1</span> True or false: (iii) a maximum likelihood estimator is always unbiased; (iv) an unbiased estimator is necessarily consistent; (vi) an unbiased estimator whose variance tends to zero as the sample size increases is consistent.

Blueprint row 3 (estimation) is the heaviest row: 22 of 80 marks.

---

## Build

### 1 · Parameter, statistic, estimate

Pretend you cannot see the die's faces; you can only throw it. You throw twice and get 2 and 6.

:::q Predict
From the two throws 2 and 6, what is your guess for the die's mean μ? Throw twice again: will you get the same guess? Will μ itself change?
:::

:::guess Guess first
Write your guess for μ, and "same/different" for each of the two questions.
:::

:::note Terms
**Parameter θ:** a number describing the whole population (here μ). It is fixed; it is unknown only because we cannot see the population. **Statistic:** any number computed from the sample (x̄, the larger throw, …). It changes from sample to sample. **Estimator T:** a statistic used to guess θ; it is a **rule** (formula). **Estimate:** the value the rule gives for one particular sample.
:::

**Answer to the Predict.** The sample mean gives (2 + 6)/2 = **4**: an estimate of μ. A new pair of throws gives a new x̄ (the 36 pairs give 11 different values); μ = 3.5 stays where it is. The estimator x̄ = (X₁ + X₂)/2 is the rule; 4 is one estimate it produced.

:::check Check 1
Label each as parameter, estimator or estimate: (a) the mean height of all students in the college; (b) the formula (X₁ + … + X₂₅)/25; (c) "our 25 students average 168.2 cm".
:::

### 2 · Point and interval estimation

:::q Predict
A lab reports "mean haemoglobin is 12.5 g/dL" and another reports "mean haemoglobin is between 12.1 and 12.9 g/dL with 95% confidence". What does the second report tell you that the first does not?
:::

:::guess Guess first
One phrase: what extra information does a range carry?
:::

:::note Terms
**Point estimation:** one number for θ (x̄ = 12.5). **Interval estimation:** a range of values, with a stated confidence that the range has caught θ (12.1 to 12.9 at 95%). Built in file 11. (G&K §15.1.)
:::

**Answer to the Predict.** The range shows **how precise** the guess is. A single number never says how far off it might be.

:::check Check 2
Point or interval? (a) "The defect rate is 3%." (b) "The defect rate is 3% ± 1% (95% confidence)." (c) "The mean life is at least 1450 h with 99% confidence."
:::

### 3 · Unbiased: right on average

A good rule should not aim systematically too high or too low. Test two rules for μ on all 36 two-throw samples.

:::q Predict
Rule A: the mean of the two throws, x̄. Rule B: the larger of the two throws. Over all 36 samples, which rule averages exactly 3.5? Does the other average above or below?
:::

:::guess Guess first
The larger of two throws is never below either throw. Which way does that push its average?
:::

:::note Terms
**Unbiased:** T is unbiased for θ if E(T) = θ, whatever the true θ is: its average over all possible samples hits the target (G&K §15.4). Otherwise **bias** = E(T) − θ.
:::

[[fig:xbar_vs_max|What this graph plots: the 36 two-throw samples sorted by the value each rule gives. Left: x̄. Right: the larger throw. Horizontal axis: the rule's value. Bar height: how many of the 36 samples give it. Dashed line: μ = 3.5. Triangle: the rule's average over all 36.|w=88]]

**Reading the figure.**

| rule | values it can give | most common value | average over 36 | bias |
|---|---|---|---|---|
| x̄ | 1, 1.5, …, 6 | 3.5 (6 samples) | 126/36 = **3.5** | 0 |
| larger throw | 1, 2, …, 6 | 6 (11 samples) | 161/36 = **4.47** | +0.97 |

**Answer to the Predict.** **x̄ averages exactly 3.5**: unbiased. The larger throw averages **4.47**: biased upwards, because it always picks the higher value.

x̄ is unbiased in general: E(x̄) = (1/n)(μ + … + μ) = μ, by 03b step 1 and step 2.

:::check Check 3
Rule C: the **smaller** of the two throws. Without listing all 36, say whether its average is above or below 3.5, and why. (Bonus: it is 91/36.)
:::

### 4 · Checking a formula for bias

The exam gives formulas in X₁, X₂, X₃ and asks which are unbiased. The rules of 03b answer it in two lines.

:::q <span class="tag">MTE C1(b) · 3 marks</span>
Let X₁, X₂, X₃ be a random sample of size 3 from a population with mean μ and variance σ². T₁ = X₁ + X₂ − X₃ and T₂ = 3X₁ + 2X₃ − 3X₂ are used to estimate μ. Which of T₁, T₂ is unbiased? Justify your answer.
:::

:::guess Guess first
Add up the numbers in front of X₁, X₂, X₃ in each formula. What do you notice?
:::

Every Xᵢ is a draw from the population, so E(Xᵢ) = μ. By 03b steps 1–2 (no independence needed):

$$E(c_{1}X_{1} + c_{2}X_{2} + c_{3}X_{3}) = (c_{1} + c_{2} + c_{3}) μ$$

Read it as: "the average of the formula is μ times the sum of its coefficients". So a formula of this kind is unbiased for μ exactly when its coefficients add to 1.

**Answer.**

1. E(T₁) = E(X₁) + E(X₂) − E(X₃) = μ + μ − μ = μ ⇒ **T₁ is unbiased**.
2. E(T₂) = 3μ + 2μ − 3μ = 2μ ≠ μ ⇒ **T₂ is biased**, bias = 2μ − μ = μ.

Die check: E(T₂) = 2 × 3.5 = 7, not 3.5.

:::check Check 4
For the same sample, find λ so that T₃ = (λX₁ + X₂ + X₃)/3 is unbiased for μ.
:::

### 5 · Why the sample variance divides by n − 1

The most-used unbiased estimator after x̄ is s². Its divisor n − 1 is why the t, χ² and F formulas of files 11–16 use n − 1.

:::q Predict
For each of the 36 two-throw samples, compute the spread Σ(xᵢ − x̄)², then divide by n = 2. Will the average over the 36 samples be σ² = 2.92, more, or less?
:::

:::guess Guess first
Deviations are measured from x̄, the centre of the two throws themselves. Are the throws closer to x̄ or to μ?
:::

:::note Terms
**Σ(xᵢ − x̄)²:** the sum of squared distances of the sample values from their own mean. **Sample variance s²** = Σ(xᵢ − x̄)²/(n − 1). **Degrees of freedom n − 1:** once x̄ is fixed, only n − 1 of the deviations are free (they must sum to 0).
:::

| divisor | average over the 36 samples | compared with σ² = 35/12 ≈ 2.92 |
|---|---|---|
| n = 2 | 35/24 ≈ **1.46** | half: too small |
| n − 1 = 1 | 35/12 ≈ **2.92** | exact |

The general result (G&K §12.11):

$$E[Σ(X_{i} − X̄)^{2}] = (n − 1) σ^{2}$$

1. Divide by n: average (n − 1)σ²/n, below σ² (biased).
2. Divide by n − 1: average σ² exactly, so **s² is unbiased** for σ².

**Answer to the Predict.** **Less**: about 1.46, half of 2.92 (for n = 2, (n − 1)/n = ½). x̄ sits inside the sample, so the values are closer to x̄ than to μ, and dividing by n under-counts the spread; n − 1 corrects it.

:::note Notation in this pack
Gupta & Kapoor sometimes write s² for the n-divisor and S² for the (n − 1)-divisor. This pack writes **s² with n − 1** throughout, and says so wherever a question's data could be read either way.
:::

:::check Check 5
Data 4, 6, 8. Compute Σ(x − x̄)²/n and s².
:::

### 6 · Consistent: closing in as n grows

Unbiased is about the centre at one sample size. Consistency asks what happens as the sample grows.

:::q <span class="tag">G&K ch. 15 objective Q1 (iv), (vi)</span>
True or false: (iv) an unbiased estimator is necessarily consistent; (vi) an unbiased estimator whose variance tends to zero as the sample size increases is consistent.
:::

:::guess Guess first
T₁ = X₁ + X₂ − X₃ (step 4) uses three throws however many you make. Does it get better as n grows?
:::

:::note Terms
**Consistent:** Tₙ (the estimator from n observations) is consistent for θ if, as n → ∞, the probability that Tₙ lies within any small distance of θ tends to 1 (G&K §15.3).
:::

[[fig:xbar_shrink|What this graph plots: the exact distribution of x̄ for the die with n = 1, 4 and 16 throws. Horizontal axis: the value of x̄. Line height: its probability. Dashed line: μ = 3.5. The title of each row gives the SD of x̄.|w=74]]

**Reading the figure.**

| n | Var(x̄) = σ²/n | SD of x̄ | picture |
|---|---|---|---|
| 1 | 2.92 | 1.71 | flat: any face equally likely |
| 4 | 0.73 | 0.85 | a hump around 3.5 |
| 16 | 0.18 | 0.43 | a narrow spike at 3.5 |

**Sufficient condition** (G&K §15.4.2, Theorem 15.2): if E(Tₙ) → θ **and** Var(Tₙ) → 0 as n → ∞, then Tₙ is consistent.

**Answer.**

- (iv) **False.** T₁ is unbiased but Var(T₁) = 3σ² (03b step 3) for every n: it never closes in on μ.
- (vi) **True.** That is Theorem 15.2. Example: E(x̄) = μ and Var(x̄) = σ²/n → 0, so x̄ is consistent (the figure).

:::check Check 6
X = number of successes in n independent trials, each with success probability p (E(X) = np, Var(X) = np(1 − p)). Is X/n a consistent estimator of p? Use the condition.
:::

### 7 · Efficient: the smaller spread wins

Two unbiased rules: both are right on average. Prefer the one whose guesses stray less.

:::q Predict
Three throws. T₁ = X₁ + X₂ − X₃ and x̄ = (X₁ + X₂ + X₃)/3 are both unbiased for μ = 3.5 (step 4). Which would you rather use, and roughly how many times smaller is its variance?
:::

:::guess Guess first
T₁ can give values from −4 to 11; x̄ only from 1 to 6. Guess the ratio of the variances.
:::

:::note Terms
**More efficient:** of two unbiased estimators, the one with the smaller variance. **Efficiency** of T′ relative to T = Var(T)/Var(T′); below 1 means T′ is worse (G&K §15.5).
:::

[[fig:t1_vs_xbar|What this graph plots: all 216 three-throw samples sorted by the value of each rule. Left: T₁ = X₁ + X₂ − X₃. Right: x̄. Horizontal axis: the rule's value. Line height: how many of the 216 samples give it. Dashed line: μ = 3.5.|w=88]]

**Reading the figure.** Both pictures are centred on 3.5 (both unbiased). T₁ spreads from −4 to 11 (SD 2.96); x̄ stays within 1 to 6 (SD 0.99).

By 03b steps 1 and 3 (independent throws; squared coefficients):

1. Var(T₁) = (1² + 1² + (−1)²)σ² = **3σ²**. Die: 3 × 35/12 = **8.75**.
2. Var(x̄) = (1/3)² × 3σ² = **σ²/3**. Die: 35/36 ≈ **0.97**.
3. Efficiency of T₁ relative to x̄ = (σ²/3)/(3σ²) = **1/9**.

**Answer to the Predict.** Use **x̄**: its variance is **9 times smaller**.

:::check Check 7
T₄ = (X₁ + 2X₂ + X₃)/4. Is it unbiased? Find Var(T₄) in terms of σ² and its efficiency relative to x̄.
:::

### 8 · Sufficient: keeping all the information

The last property is about information, not centre or spread.

:::q <span class="tag">MTE A3 · 2 marks</span>
If an estimator t contains all the information of the sample regarding the population parameter θ, it is called: (a) efficient (b) sufficient (c) consistent (d) unbiased.
:::

:::guess Guess first
A coin with unknown P(head) = p is tossed 5 times: H T T H H. Once you know "3 heads in 5", does the **order** tell you anything more about p?
:::

:::note Terms
**Sufficient:** T is sufficient for θ if, once T's value is known, the rest of the sample carries no further information about θ (G&K §15.6).
:::

Coin example. Every sequence with 3 heads and 2 tails has the same probability, p³(1 − p)², whatever the order: HTTHH, HHHTT and the other 8 orders are all equally likely for every p. So the order says nothing about p, and the **number of heads** is sufficient for p.

**Factorisation test** (used in 09b Check 11): the probability of the whole sample, written as a function of θ (the likelihood L), splits as L = g(T, θ) × h(x), where h does not contain θ. Coin: L = p³(1 − p)² depends on the data only through the count 3.

**Answer.** **Sufficient**: (b).

:::check Check 8
<span class="tag">G&K ch. 15 objective Q1 (iii)</span> True or false: "a maximum likelihood estimator is always unbiased." (Hint: 09b step 7 shows that the MLE of σ² divides by n; compare step 5.)
:::

---

## Exam form

**Definitions** (write all four when asked for "characteristics of a good estimator"):

1. **Unbiased**: E(T) = θ; bias = E(T) − θ.
2. **Consistent**: Tₙ → θ in probability as n → ∞; sufficient condition E(Tₙ) → θ and Var(Tₙ) → 0.
3. **Efficient**: among unbiased estimators, the smallest variance; efficiency of T′ relative to T = Var(T)/Var(T′).
4. **Sufficient**: contains all the sample's information about θ; L = g(T, θ) h(x).

**Standard results.** x̄ is unbiased and consistent for μ, Var(x̄) = σ²/n. s² = Σ(x − x̄)²/(n − 1) is unbiased for σ²; the n-divisor version is biased (E = (n − 1)σ²/n) but consistent.

**Procedure: is T unbiased?** Take E of each term (E(Xᵢ) = μ), add, compare with θ; state "unbiased" or "biased, bias = …".

**Procedure: which is more efficient?** Check both are unbiased; Var(Σ cᵢXᵢ) = (Σ cᵢ²)σ²; smaller variance wins.

## Traps

- Calling a formula unbiased because it "looks like" a mean: check that its coefficients add to 1.
- Unbiased does not imply consistent (T₁), and consistent does not imply unbiased (the n-divisor variance).
- Var(aX₁ − bX₂) = (a² + b²)σ²: the minus sign does not subtract variances.
- Comparing efficiency of a biased estimator: efficiency compares **unbiased** estimators.
- Swapping "efficient" (small variance) and "sufficient" (all the information).

## Self-test

1. Define unbiased, consistent, efficient and sufficient estimators.
2. X₁, X₂ from a population with mean μ. Is (2X₁ + 3X₂)/5 unbiased? Is (X₁ + X₂)/3?
3. Find the variances of the two estimators in question 2 (population variance σ²).
4. Why is s² divided by n − 1?
5. Give an estimator of μ that is unbiased but not consistent.
6. Die population, two throws: the rule "first throw only" (T = X₁). Is it unbiased? What is its variance, and its efficiency relative to x̄?
7. For a coin tossed n times, which statistic is sufficient for p?

<!--ANSWERS-->
## Answers

**Check 1.** (a) parameter; (b) estimator; (c) estimate.

**Check 2.** (a) point; (b) interval; (c) interval (a one-sided one).

**Check 3.** **Below** 3.5: the smaller throw is never above either throw, so it is pulled down. Its average is 91/36 ≈ **2.53** (bias ≈ −0.97, the mirror of the larger throw's +0.97).

**Check 4.** E(T₃) = (λ + 1 + 1)μ/3 = μ ⇒ λ + 2 = 3 ⇒ **λ = 1**.

**Check 5.** x̄ = 6; Σ(x − x̄)² = 4 + 0 + 4 = 8. n-divisor: 8/3 = **2.67**; s² = 8/2 = **4**.

**Check 6.** E(X/n) = np/n = p and Var(X/n) = np(1 − p)/n² = p(1 − p)/n → 0: **consistent**.

**Check 7.** Coefficients ¼ + ½ + ¼ = 1: **unbiased**. Var = (1 + 4 + 1)σ²/16 = **3σ²/8**. Efficiency relative to x̄ = (σ²/3)/(3σ²/8) = **8/9**.

**Check 8.** **False**: the MLE of σ² is Σ(x − x̄)²/n, which is biased (step 5).

**Self-test.**

1. See Exam form.
2. 2/5 + 3/5 = 1: **unbiased**. 1/3 + 1/3 = 2/3: **biased** (E = 2μ/3).
3. (4 + 9)σ²/25 = **13σ²/25**; (1 + 1)σ²/9 = **2σ²/9**.
4. E[Σ(X − X̄)²] = (n − 1)σ², so dividing by n − 1 makes the average exactly σ² (unbiased).
5. T = X₁ (the first observation alone): E = μ, but Var = σ² for every n.
6. E(X₁) = 3.5: **unbiased**. Var = σ² = 35/12 ≈ **2.92**. Var(x̄) = 35/24, so efficiency = (35/24)/(35/12) = **½**.
7. The **number of heads** (equivalently the proportion of heads).
<!--/ANSWERS-->
