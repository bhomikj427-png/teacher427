# 12a — Hypotheses, errors, significance level and critical region

<div class="sub">Professor's slides "Hypothesis Testing" (ppt 8) slides 2–19, 23–25 · Gupta & Kapoor §12.5–12.8 (null and alternative hypotheses, errors, critical region and level of significance, one- and two-tailed tests, critical values, steps), §16.2.4–16.2.7 (critical region W, size, power) · blueprint row 4 "null and alternative hypotheses, level of significance, critical region, Type I and Type II errors" · 13 real questions (slides 9, 10, 14; A4 MCQ 1, 2, 4–7; A5 A1(i)–(iv)) · needs 06 (tails, step 5), 07 (SE, step 5; z for an average, step 9), 11 (z_{α/2}, step 4)</div>

## Map

[[map:1 Is the claim wrong? > 2 Null and alternative hypotheses > 3 Writing H₀ and H₁ from a claim > 4 One- and two-tailed tests > 5 Type I and Type II errors > 6 Significance level and critical region > 7 β and power > 8 The steps of every test|here=1]]

File 11 used the curve of x̄ to give a range for μ. This file uses the same curve to **judge a claim** about μ: is the sample average far enough from the claimed value to reject the claim? Steps 1–4 write the two competing statements and say which direction counts against the claim; step 5 names the two ways the decision can go wrong; steps 6–7 put a probability on each, α and β; step 8 lists the steps every later test follows. File 12b computes α and β for the assignment's 6-mark questions, and files 13–16 run the steps of step 8 with the t, F, χ² and ANOVA statistics.

| Symbol | What it means in this file | Typical value |
|---|---|---|
| μ₀ | the value of μ the claim states | 1000 charges |
| H₀ | null hypothesis: the statement the test starts by assuming true (contains =, ≤ or ≥) | μ ≥ 1000 |
| H₁ | alternative hypothesis: what is concluded if H₀ is rejected (contains ≠, < or >) | μ < 1000 |
| x̄ | average of the sample tested | 990 charges |
| SE | standard error of x̄: σ/√n (07 step 5) | 50/√25 = 10 |
| z | (x̄ − μ₀)/SE: how many SEs the sample average sits from the claimed value | −1 |
| W | critical region: the values of the statistic for which H₀ is rejected | x̄ < 983.55 |
| α | level of significance: P(reject H₀ when H₀ is true) | 0.05 |
| β | P(do not reject H₀ when H₁ is true) | 0.36 at μ = 980 |
| 1 − β | power: P(reject H₀ when H₁ is true) | 0.64 |

**Running example.** Slide 10's battery maker claims an average life of **at least 1000 charges**. The pack adds numbers to test it: **σ = 50 charges, n = 25 batteries**, so SE = 50/√25 = 10 charges; the 25 batteries average **x̄ = 990**. Steps 1, 3 and 6–8 use it.

## The questions this file answers

- <span class="tag">A5 A1(i)–(iv)</span> Define (i) statistical hypothesis (ii) null hypothesis and alternative hypothesis (iii) one-tailed and two-tailed test (iv) significance level and critical region.
- <span class="tag">Slides p.9</span> State the null and alternative hypotheses: a university publicises that the proportion of its students who graduate in 4 years is 82%.
- <span class="tag">Slides p.10</span> Write the claim as a mathematical sentence; state H₀ and H₁ and identify which represents the claim: a manufacturer claims that its rechargeable batteries have an average life of at least 1,000 charges.
- <span class="tag">Slides p.14</span> Statesville college claims that 94% of their graduates find employment within six months of graduation. What will a Type I or a Type II error be?
- <span class="tag">A4 MCQ 1, 2, 4, 5, 6, 7</span> The alternative hypothesis; the critical region; an example of a Type I error; what a Type II error is; H₁ for "less than 3 kg"; the symbol for P(Type II error).

Blueprint row 4 asks these as 2-mark definitions; the 6-mark α–β calculation is file 12b.

---

## Build

### 1 · Is the claim wrong?

A maker says its batteries last at least 1000 charges on average. You cannot test every battery, so you test 25.

:::q Predict
The 25 batteries average x̄ = 990 charges, below 1000. The SE of an average of 25 is 10 charges (σ = 50). Does 990 prove the claim false?
:::

:::guess Guess first
Yes or no? How far below 1000 would x̄ have to be before you would call the claim false?
:::

:::note Terms
**Statistical hypothesis:** a statement about a population's parameter (here μ, the average life of all batteries) that a sample can be used to check (slide 2; G&K §12.5). **Test of significance:** a rule that compares the sample with the hypothesis and decides whether the difference is too big to be chance (slide 3).
:::

The SE says how far x̄ wanders from μ by chance alone (07 step 4). Measure 990 in SEs from the claimed 1000:

$$z = \frac{x̄ − μ₀}{SE} = \frac{990 − 1000}{10} = −1$$

| x̄ | z | P(x̄ this low or lower if μ really is 1000) |
|---|---|---|
| 990 | −1 | 0.1587 |
| 983.55 | −1.645 | 0.05 |
| 970 | −3 | 0.0013 |

The last column is 06 step 5's tail: P(Z < −1) = 0.5 − 0.3413 = 0.1587.

**Answer to the Predict.** No. Even if every battery averaged exactly 1000, about 16 samples in 100 would average 990 or less. A result that ordinary is no evidence against the claim. An x̄ of 970 (3 SEs low) would be: it happens 13 times in 10,000 if the claim is true. Steps 2–8 turn "too far to be chance" into a rule.

:::check Check 1
The 25 batteries had averaged 975 instead. (a) Find z. (b) Is this stronger or weaker evidence against the claim than 990?
:::

### 2 · Null and alternative hypotheses

Step 1 compared the sample with one claimed value. A test always sets up two statements, and only one of them is assumed true at the start.

:::q <span class="tag">Slides p.9</span>
State the null and alternative hypotheses for the following problem: a university publicises that the proportion of its students who graduate in 4 years is 82%.
:::

:::guess Guess first
Which statement contains "="? Write H₀ and H₁.
:::

:::note Terms
**Null hypothesis H₀:** the accepted fact or historical value, about a population parameter, never about a sample statistic; it always contains =, ≤ or ≥. The test **assumes H₀ true** and asks whether the data contradict it (slide 6; G&K §12.5 calls it "usually a hypothesis of no difference"). **Alternative hypothesis H₁:** the statement complementary to H₀, accepted if H₀ is rejected; it contains ≠, < or > (slide 7; G&K §12.5.1).
:::

| | H₀ | H₁ |
|---|---|---|
| role | assumed true until the data contradict it | concluded only if H₀ is rejected |
| sign | =, ≤, ≥ | ≠, <, > |
| about | a parameter (μ, p) | the same parameter |

**Answer to slides p.9.** The parameter is p, the proportion of **all** students who graduate in 4 years. The publicised value contains equality: **H₀: p = 0.82, H₁: p ≠ 0.82**.

**A4 MCQ 1.** "The alternative hypothesis is generally used to represent:" **(B) the claim that contradicts the null hypothesis.**

:::check Check 2
<span class="tag">A5 A1(i)–(ii)</span> Define statistical hypothesis, null hypothesis and alternative hypothesis, in one sentence each.
:::

### 3 · Writing H₀ and H₁ from a claim

Step 2's claim was an equality. Claims with "at least" or "at most" need one more rule: which side gets the equals sign.

:::q <span class="tag">Slides p.10</span>
Write the claim as a mathematical sentence. State the null and alternative hypotheses and identify which represents the claim: a manufacturer claims that its rechargeable batteries have an average life of at least 1,000 charges.
:::

:::guess Guess first
"At least 1000" is μ ? 1000. Does it go into H₀ or H₁?
:::

:::note Terms
**The claim:** the statement in the question's words. It can be H₀ or H₁: it is H₀ when it contains equality (=, ≤, ≥), and H₁ when it does not (≠, <, >). **Complement:** the other statement, which covers every value the claim leaves out.
:::

| Words in the question | Sign | The claim goes in |
|---|---|---|
| is, equals, no change | = | H₀ |
| at least, no less than | ≥ | H₀ |
| at most, no more than | ≤ | H₀ |
| is not, differs, has changed | ≠ | H₁ |
| less than, below, reduces | < | H₁ |
| more than, above, increases | > | H₁ |

**Answer to slides p.10.** "At least 1000" is μ ≥ 1000, which contains equality: **H₀: μ ≥ 1000 (the claim), H₁: μ < 1000 (the complement)**. The test of step 1 assumes the maker is right and asks whether 990 is low enough to reject that.

:::check Check 3
(a) <span class="tag">A4 MCQ 6</span> A researcher wants to test whether the average weight of newborn babies is **less than** 3 kg. Which alternative hypothesis is correct: H₁: μ = 3, μ < 3, μ > 3, μ ≠ 3? (b) A new process is claimed to **increase** mean output above 50 units per hour. Write H₀ and H₁ and say which one is the claim.
:::

### 4 · One- and two-tailed tests

The sign in H₁ also says which kind of sample counts against H₀: too small, too large, or either.

:::q <span class="tag">A5 A1(iii)</span>
Define one-tailed and two-tailed test.
:::

:::guess Guess first
For H₁: μ < 1000, which averages count as evidence against H₀: low ones, high ones, or both?
:::

:::note Terms
**Two-tailed test:** H₁ is ≠, so an x̄ far below **or** far above μ₀ counts against H₀; the rejection region is split between both tails of the curve. **One-tailed test:** H₁ is < (left-tailed: only low values count) or > (right-tailed: only high values count); the whole rejection region is in one tail (G&K §12.7.1).
:::

[[fig:two_tails|What this graph plots: three copies of the Z curve (across: the statistic z; up: how often it happens if H₀ is true). Red: where H₀ is rejected at α = 0.05. Left: H₁ is ≠, 0.025 in each tail beyond ±1.96. Middle: H₁ is <, all 0.05 below −1.645. Right: H₁ is >, all 0.05 above 1.645.|w=95]]

| H₁ | Test | Rejection region at α = 0.05 |
|---|---|---|
| μ ≠ μ₀ | two-tailed | z < −1.96 or z > 1.96 |
| μ < μ₀ | left-tailed | z < −1.645 |
| μ > μ₀ | right-tailed | z > 1.645 |

**Answer to A5 A1(iii).** A test is **one-tailed** when H₁ is one-sided (μ > μ₀ or μ < μ₀), so the critical region lies entirely in the right or the left tail of the statistic's curve; it is **two-tailed** when H₁ is μ ≠ μ₀, so the critical region is split between both tails. The batteries' H₁: μ < 1000 gives a **left-tailed** test: only low averages count.

:::check Check 4
Classify as left-, right- or two-tailed: (a) H₁: p ≠ 0.94 (b) a new process **reduces** mean defects below 5 (c) a coin is **not fair** (d) Check 3(b)'s output claim.
:::

### 5 · Type I and Type II errors

Step 4 fixed which samples lead to "reject". A sample is still chance, so the decision can be wrong, in two different ways.

:::q <span class="tag">Slides p.14</span>
Statesville college claims that 94% of their graduates find employment within six months of graduation. What will a Type I or a Type II error be?
:::

:::guess Guess first
Write H₀ first. Then: what is the mistake if you reject it but it was true?
:::

:::note Terms
**Type I error:** rejecting H₀ when H₀ is true; a false positive, "crying wolf" when there is no wolf (slides 16–17). **Type II error:** not rejecting H₀ when H₀ is false; a false negative (slide 18; G&K §12.6 and §16.2.6 write "accept H₀ when it is wrong").
:::

| Decision ↓ · Truth → | H₀ true | H₀ false (H₁ true) |
|---|---|---|
| do not reject H₀ | correct | **Type II error** |
| reject H₀ | **Type I error** | correct |

(slide 13). G&K §12.6 adds quality-control names: a Type I error rejects a good lot (**producer's risk**), a Type II error accepts a bad lot (**consumer's risk**).

:::note Slide wording (slides 18 and 23)
The slides say "accepting" H₀ for a Type II error. The pack writes "do not reject": the data failed to contradict H₀, which does not prove it true. Both wordings mark the same decision.
:::

**Answer to slides p.14.** H₀: p = 0.94 (the claim, with =), H₁: p ≠ 0.94.

- **Type I error:** the true proportion **is** 0.94, but the sample leads us to reject H₀: we wrongly conclude the college's figure is false.
- **Type II error:** the true proportion is **not** 0.94, but the sample does not lead us to reject H₀: we keep believing the 94%.

**A4 MCQ 4.** Concluding a new medicine is effective when it is not: H₀ "not effective" is true and was rejected, so **(A) Type I error**. **A4 MCQ 5.** A Type II error occurs when a researcher **(C) fails to reject a false null hypothesis**.

:::check Check 5
A court's H₀ is "the accused is innocent". (a) Describe its Type I and Type II errors. (b) For the batteries (H₀: μ ≥ 1000), describe a Type II error in the maker's terms.
:::

### 6 · Significance level and critical region

Step 5 named the errors. A test is designed by fixing, **before** the data, how often a Type I error is allowed.

:::q <span class="tag">A4 MCQ 2</span>
The critical region in hypothesis testing is the region in which we: (A) always accept the null hypothesis (B) reject the null hypothesis (C) calculate the sample mean (D) increase the sample size.
:::

:::guess Guess first
Pick an option, then find the battery average below which you would reject H₀ if only 5% of true-H₀ samples may be rejected.
:::

:::note Terms
**Critical region W:** the values of the statistic for which H₀ is rejected; the rest is the acceptance region (G&K §12.7). **Level of significance α:** P(statistic in W when H₀ is true), the probability of a Type I error, fixed before sampling; usually 0.10, 0.05 or 0.01 (slide 24; G&K calls it the **size** of the critical region, §16.2.6). **Critical value:** the boundary between W and the acceptance region (slide 25; G&K §12.7.2).
:::

[[fig:crit_battery|What this graph plots: across: x̄, the average life of 25 batteries; up: how often each x̄ happens if H₀ is true with μ = 1000 (normal, SE = 10). Red: the critical region x̄ < 983.55, holding 5% of the area. The dashed line is the critical value.|w=82]]

**Finding the critical value** (left-tailed, α = 0.05):

1. The left tail must hold 0.05, so z = −1.645 (06 step 4: area 0 to 1.645 is 0.45).
2. Convert back to charges: x̄ = μ₀ + z × SE = 1000 − 1.645 × 10 = **983.55**.
3. W = {x̄ < 983.55}: reject the maker's claim only if the 25 batteries average below 983.55.

| α | z, two-tailed | z, right-tailed | z, left-tailed |
|---|---|---|---|
| 0.10 | ±1.645 | 1.28 | −1.28 |
| 0.05 | ±1.96 | 1.645 | −1.645 |
| 0.01 | ±2.58 | 2.33 | −2.33 |

(G&K §12.7.2's table.) A one-tailed test at α uses the two-tailed value for 2α.

**Answer to A4 MCQ 2.** **(B)**: the critical region is where H₀ is rejected. For the batteries, x̄ = 990 is not below 983.55, so at α = 0.05 the claim is **not rejected**, matching step 1.

**A5 A1(iv).** **Significance level α:** the probability of rejecting H₀ when it is true (the largest Type I error probability allowed), fixed before sampling. **Critical region:** the set of values of the test statistic for which H₀ is rejected.

:::check Check 6
For the batteries, find the critical value at α = 0.01 (z = −2.33). Would x̄ = 980 be rejected at α = 0.05? At α = 0.01?
:::

### 7 · β and power

Step 6 controlled α, the Type I error. The Type II error has its own probability, and it depends on what μ really is.

:::q Predict
Suppose the maker is wrong and the true average is **μ = 980** charges. With the rule "reject if x̄ < 983.55", how often will the test fail to catch it?
:::

:::guess Guess first
More or less than half the time?
:::

:::note Terms
**β:** P(do not reject H₀ when H₁ is true), the probability of a Type II error; it is computed under a stated value from H₁ (slides 15, 18). **Power 1 − β:** P(reject H₀ when H₁ is true): how often the test catches a false H₀. As a function of the true parameter it is the **power function** (G&K §16.2.7).
:::

[[fig:beta_battery|What this graph plots: across: x̄; up: how often each x̄ happens. Blue: the curve if H₀ is true (μ = 1000). Purple: the curve if μ is really 980. Dashed line: the critical value 983.55. Red: α, the part of the blue curve in the rejection region. Amber: β, the part of the purple curve in the do-not-reject region.|w=86]]

**Working** (the purple curve: μ = 980, SE = 10):

1. Not rejected means x̄ ≥ 983.55.
2. z = (983.55 − 980)/10 = 0.355 ≈ 0.36.
3. β = P(Z > 0.36) = 0.5 − 0.1406 = **0.3594** (exact z: 0.3613; the figure prints 0.36).
4. Power = 1 − β ≈ **0.64**.

**Answer to the Predict.** Less than half, but still often: about **36%** of samples would fail to reject the false claim; the test catches it about 64% of the time.

**The trade-off.** Make α smaller (α = 0.01, critical value 1000 − 2.33 × 10 = 976.7) and the red area shrinks, but the amber one grows: β = P(x̄ ≥ 976.7 | μ = 980) = P(Z > −0.33) = 0.5 + 0.1293 = **0.6293**. With n fixed, lowering one error raises the other; only a larger n (a smaller SE, narrower curves) lowers both.

| α | critical value | β at μ = 980 | power |
|---|---|---|---|
| 0.05 | 983.55 | 0.36 | 0.64 |
| 0.01 | 976.7 | 0.63 | 0.37 |

**A4 MCQ 7.** The probability of a Type II error is denoted by **(B) β**.

:::check Check 7
Rule "reject if x̄ < 983.55" (SE = 10). Find β and the power if the true mean is μ = 970. (Use z rounded to 2 decimals.)
:::

### 8 · The steps of every test

Steps 2–7 gave every piece of a test. Put together, they make one procedure, and files 13–16 follow it with different statistics.

:::q Predict
The battery test, from claim to conclusion: list what you would write, in order.
:::

:::guess Guess first
Write your list before reading on.
:::

:::note Terms
**Test statistic:** the number computed from the sample whose curve is known **when H₀ is true** (z, t, χ², F); for one mean it has the shape (estimate − value under H₀)/SE (G&K §12.7.2).
:::

**The steps** (G&K §12.8):

1. **H₀** (step 2): μ ≥ 1000.
2. **H₁** (steps 3–4): μ < 1000, left-tailed.
3. **Level of significance** (step 6): α = 0.05, fixed before the sample.
4. **Test statistic** under H₀: z = (x̄ − μ₀)/SE = (990 − 1000)/10 = −1.
5. **Critical value** (step 6): −1.645; reject if z < −1.645.
6. **Decision:** −1 is not below −1.645, so **do not reject H₀**.
7. **Conclusion in the question's words:** at the 5% level, the 25 batteries give no evidence that the average life is below 1000 charges.

**Answer to the Predict.** The seven lines above. In an exam each line is worth writing out: the hypotheses, α, the statistic and the critical value usually carry marks of their own.

:::check Check 8
A two-tailed z-test at α = 0.05 gives z = −2.3. (a) State the decision and the reason. (b) Would the decision change at α = 0.01?
:::

---

## Exam form

**Definitions** (G&K §12.5–12.7, §16.2.4–16.2.7; slides 2–25).

- **Statistical hypothesis:** a statement about a population parameter that a sample can test.
- **Null hypothesis H₀:** the status quo about a parameter, assumed true; contains =, ≤ or ≥. **Alternative H₁:** the complementary statement, accepted if H₀ is rejected; contains ≠, < or >.
- **One-tailed test:** H₁ one-sided (> or <), critical region in one tail. **Two-tailed test:** H₁ is ≠, critical region in both tails.
- **Type I error:** reject H₀ when H₀ is true (probability α). **Type II error:** do not reject (accept) H₀ when H₀ is false (probability β). **Power:** 1 − β = P(reject H₀ | H₁ true).
- **Level of significance:** α = P(reject H₀ | H₀ true), the maximum Type I error probability, fixed in advance (also called the size of the critical region).
- **Critical region W:** the statistic values for which H₀ is rejected. **Critical value:** the boundary of W.

**Formulas.** α = P(statistic ∈ W | H₀) · β = P(statistic ∉ W | H₁) · power = P(statistic ∈ W | H₁) = 1 − β.

**Steps of a test.** H₀ · H₁ (tails) · α · statistic under H₀ · critical value · decision · conclusion in context.

## Traps

- Putting the claim in H₀ automatically: the statement with =, ≤ or ≥ is H₀, claim or not.
- Writing H₀ about x̄ or p̂: hypotheses are about parameters (μ, p).
- Using ±1.96 for a one-tailed test at 5% (it is 1.645).
- Computing β under H₀: β always uses a value from H₁.
- Writing "H₀ is proved" after not rejecting: the data only failed to contradict it.
- Swapping α (Type I, false positive) and β (Type II, false negative).
- Expecting a smaller α to cost nothing: with n fixed it raises β.

## Self-test

1. Define Type I error, Type II error and power.
2. State H₀ and H₁: (a) "the mean life of a tyre is 40,000 km"; (b) "the new drug lowers mean blood pressure below 140".
3. What is a critical region? What is a critical value? How does α fix them?
4. Which errors can occur if H₀ is (a) rejected (b) not rejected?
5. Batteries again (SE = 10, H₀: μ ≥ 1000, α = 0.05): would x̄ = 985 be rejected? Give z.
6. Why can α and β not both be made very small without increasing n?
7. A smoke alarm's H₀ is "no fire". Which is worse, a Type I or a Type II error, and how should α be set?

<!--ANSWERS-->
## Answers

**Check 1.** (a) z = (975 − 1000)/10 = **−2.5**. (b) **Stronger**: 2.5 SEs below the claim; P(Z < −2.5) = 0.5 − 0.4938 = 0.0062, so it would happen about 6 times in 1000 if the claim were true.

**Check 2.** A **statistical hypothesis** is a statement about a population parameter that sample data can test. The **null hypothesis** H₀ is the status-quo statement (with =, ≤ or ≥) that the test assumes true and tries to contradict. The **alternative hypothesis** H₁ is its complement (with ≠, < or >), accepted if H₀ is rejected.

**Check 3.** (a) **H₁: μ < 3** (B). (b) "Above 50" has no equality, so it is H₁: **H₀: μ ≤ 50, H₁: μ > 50 (the claim)**.

**Check 4.** (a) two-tailed (b) left-tailed (H₁: μ < 5) (c) two-tailed (H₁: p ≠ ½) (d) right-tailed (H₁: μ > 50).

**Check 5.** (a) Type I: convicting an innocent person. Type II: acquitting a guilty person. (b) The true average is below 1000 charges, but the 25 batteries do not lead to rejecting the claim: the over-statement goes undetected.

**Check 6.** α = 0.01: critical value 1000 − 2.33 × 10 = **976.7**. x̄ = 980: below 983.55, so **rejected at α = 0.05**; not below 976.7, so **not rejected at α = 0.01**.

**Check 7.** z = (983.55 − 970)/10 = 1.355 ≈ 1.36; β = P(Z > 1.36) = 0.5 − 0.4131 = **0.0869**; power = **0.9131**. A false claim far from 1000 is caught far more often.

**Check 8.** (a) |z| = 2.3 > 1.96: **reject H₀** at the 5% level. (b) 2.3 < 2.58: **not rejected** at the 1% level, so the decision changes.

**Self-test.**

1. Type I: rejecting H₀ when it is true (probability α). Type II: not rejecting H₀ when it is false (probability β). Power: P(reject H₀ | H₁ true) = 1 − β.
2. (a) H₀: μ = 40,000 km, H₁: μ ≠ 40,000 km. (b) H₀: μ ≥ 140, H₁: μ < 140 (the claim).
3. The critical region is the set of statistic values for which H₀ is rejected; the critical value is its boundary. α is the area of the region under H₀'s curve, so choosing α fixes where the boundary goes (e.g. −1.645 for a left tail of 0.05).
4. (a) Only a Type I error (if H₀ was true). (b) Only a Type II error (if H₀ was false).
5. z = (985 − 1000)/10 = −1.5 > −1.645: **not rejected**.
6. With n fixed, moving the critical value to shrink α enlarges the acceptance region, which raises β, and the reverse. A larger n shrinks SE, narrows both curves, and lowers both errors.
7. H₀ "no fire": a Type I error is a false alarm, a Type II error misses a real fire. The Type II error is worse, so a **larger α** (a sensitive alarm) is accepted to keep β small.
<!--/ANSWERS-->
