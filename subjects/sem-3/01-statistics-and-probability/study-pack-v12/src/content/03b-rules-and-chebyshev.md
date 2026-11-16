# 03b — Rules for E and Var, and Chebyshev's inequality

<div class="sub">Gupta & Kapoor ch. 6 (§6.3–6.7, §6.13) · blueprint row 1 "mathematical expectation and variance, Chebyshev's inequality" · 9 real questions (MTE A1(a), B1; Assignment 1 SA 4, SA 5, SA 6, LA 3, App 4, MCQ 5, MCQ 10) · needs 01 (two-dice grid step 1, independence step 10), 03a (E step 1, Var step 4, shortcut step 5, σ step 6)</div>

## Map

[[map:1 Shift and scale > 2 The mean of a sum > 3 The variance of a sum > 4 The mean of a product > 5 An endless sum > 6 Chebyshev's inequality > 7 Bound versus exact > 8 A bound above 1 > 9 A lower bound for a count|here=1]]

03a found E(X) and Var(X) for one table. Exam questions change units, add random variables together, or multiply them; redoing every sum would be slow. Steps 1–5 give **rules** that compute E and Var of a new variable from the old ones. Steps 6–9 then use μ and σ alone to put a **guaranteed bound** on a probability, for any distribution: Chebyshev's inequality.

| Symbol | What it means in this file | Typical value |
|---|---|---|
| X₁, X₂ | the scores of the first and second die | each 1 to 6 |
| a, b | ordinary numbers (constants), not random | a = 10, b = −20 |
| independent | knowing one variable's value does not change the other's probabilities (01 step 10) | two separate dice |
| k | how many standard deviations away from μ | k = 2 |
| c | a distance from μ, in X's units; c = kσ | c = 3 |

**Running example.** Two fair dice (01's 36-outcome grid). One die: E = 3.5, Var = 35/12 (03a Checks 1 and 5). S = X₁ + X₂, the sum: E(S) = 7, Var(S) = 35/6 (steps 2–3). Steps 2, 3, 4 and 7 use it.

## The questions this file answers

- <span class="tag">MTE A1(a) · 2 marks</span> If X₁ and X₂ are independent random variables, then E(X₁ · X₂) = E(X₁) · E(X₂). Correct or not?
- <span class="tag">A1 LA 3</span> A lot of 25 items contains 5 defectives. A sample of 4 is drawn. Find the expected number of defectives (a) with replacement, (b) without replacement.
- <span class="tag">A1 SA 4</span> A coin is tossed until a head appears. Find the expected number of tosses.
- <span class="tag">A1 App 4</span> Marks of engineering students have mean 70 and variance 25. Use Chebyshev's inequality to estimate the minimum proportion scoring between 60 and 80.
- <span class="tag">A1 SA 5</span> Two unbiased dice are thrown; X is the sum. Show that P(|X − 7| ≥ 3) ≤ 35/54 and compare with the actual probability.
- <span class="tag">MTE B1 · 3 marks</span> X takes −1, 1, 3, 5 with probabilities 1/6, 1/6, 1/6, 1/2. By Chebyshev's inequality find the upper bound of P(|X − 3| ≥ 1).
- <span class="tag">A1 SA 6</span> A symmetric die is thrown 600 times. Find a lower bound for the probability of getting 80 to 120 sixes.
- <span class="tag">A1 MCQ 5, MCQ 10</span> Which inequality bounds the deviation from the mean · to which distributions Chebyshev's inequality applies.

---

## Build

### 1 · Shift and scale: E(aX + b) and Var(aX + b)

A game pays from a die score. The payout is a new random variable; its mean and spread should follow from the die's.

:::q Predict
X = one die's score (E = 3.5, Var = 35/12). You win Y = 10X − 20 rupees. Predict E(Y). Then: does the "− 20" change how spread out the winnings are? Does the "× 10"?
:::

:::guess Guess first
Write E(Y), and "yes/no" for each of the two spread questions.
:::

:::note Terms
**Constant:** a fixed number (a, b), not random. **aX + b:** multiply every value of X by a, then add b. The probabilities do not change; only the values move.
:::

[[fig:shift_scale|What this graph plots: three PMFs on one value axis. Top: one die X (1 to 6). Middle: X + 3, every bar moved 3 right. Bottom: 2X, the bars twice as far apart. Each bar has height 1/6.|w=72]]

**Reading the figure.**

| variable | values | mean | spread |
|---|---|---|---|
| X | 1 to 6 | 3.5 | bars 1 apart |
| X + 3 | 4 to 9 | 3.5 + 3 = 6.5 | unchanged |
| 2X | 2 to 12 | 2 × 3.5 = 7 | doubled distances |

$$E(aX + b) = aE(X) + b        Var(aX + b) = a^{2} Var(X)$$

Read them as: "the mean follows the same recipe as the values"; "adding b moves without spreading; multiplying by a stretches every distance by a, so squared distances by a²". Why: in 03a's sums, replace each x by ax + b; the p(x) are untouched.

**Answer to the Predict.**

1. E(Y) = 10(3.5) − 20 = **15 rupees**.
2. The − 20 shifts every payout equally: **no** change to the spread.
3. The × 10 stretches it: Var(Y) = 10² × 35/12 = **291.67**, σ_Y = 10 × 1.708 = **17.08 rupees**. (σ scales by |a|, not a².)

:::check Check 1
E(X) = 3, Var(X) = 4. Find E(2X − 5), Var(2X − 5) and the SD of 2X − 5.
:::

### 2 · The mean of a sum: always the sum of the means

:::q <span class="tag">A1 LA 3</span>
A lot of 25 items contains 5 defectives. A sample of 4 is drawn. Find the expected number of defectives (a) with replacement, (b) without replacement.
:::

:::guess Guess first
Without replacement, the draws depend on each other. Does that change the expected count? Guess yes or no.
:::

**Rule** (G&K §6.3, addition theorem of expectation), for **any** X and Y, independent or not:

$$E(X + Y) = E(X) + E(Y)$$

Read it as: "the average of a total is the total of the averages". Two dice: E(X₁ + X₂) = 3.5 + 3.5 = **7**. (Check on 01's grid: the 36 sums add to 252, and 252/36 = 7.)

**A count as a sum of 0s and 1s.** Let Iᵢ = 1 if the i-th item drawn is defective, 0 if not. The number of defectives is X = I₁ + I₂ + I₃ + I₄, and E(Iᵢ) = 1 × P(defective) + 0 = P(i-th item defective).

**Answer.**

1. With replacement, every draw has P(defective) = 5/25 = 0.2.
2. Without replacement, the i-th item drawn is still equally likely to be any of the 25 (nobody has looked at the earlier ones), so P(i-th defective) = 0.2 too.
3. E(X) = 0.2 + 0.2 + 0.2 + 0.2 = **0.8 in both cases**. The rule needed no independence, so the dependence of the draws does not matter.

:::note Key slip
Assignment 1's key gives 0.808 for "without replacement". The sum rule holds without independence, so the expectation is 0.8 both ways; only the variance differs between the two cases.
:::

:::check Check 2
Three dice are thrown. Find the expected sum.
:::

### 3 · The variance of a sum: add, but only if independent

:::q Predict
Two dice: each has Var = 35/12. Predict Var(X₁ + X₂). Then predict Var(X₁ − X₂), the difference of the scores: smaller, equal, or larger?
:::

:::guess Guess first
A difference "cancels" part of the scores. Does it cancel the spread?
:::

**Rule** (G&K §6.7), for **independent** X and Y:

$$Var(X + Y) = Var(X) + Var(Y)        Var(X − Y) = Var(X) + Var(Y)$$

Read it as: "independent spreads add, whether you add or subtract the variables". Why the minus does not subtract: X − Y = X + (−1)Y, and by step 1 Var((−1)Y) = (−1)² Var(Y) = +Var(Y).

**Answer to the Predict.** Var(X₁ + X₂) = 35/12 + 35/12 = **35/6 ≈ 5.83**. Var(X₁ − X₂) = **35/6** too: the same, not smaller. The difference runs from −5 to 5, eleven values, as spread out as the sum's 2 to 12. (Both checked by listing all 36 cells.)

Without independence the rule fails: if Y = X (the same die counted twice), X + Y = 2X and Var(2X) = 4 Var(X), not 2 Var(X).

:::check Check 3
X and Y independent, Var(X) = 4, Var(Y) = 1. Find Var(X + Y), Var(X − Y) and Var(2X − 3Y).
:::

### 4 · The mean of a product: needs independence

:::q <span class="tag">MTE A1(a) · 2 marks</span>
If X₁ and X₂ are independent random variables, then E(X₁ · X₂) = E(X₁) · E(X₂). Correct or not?
:::

:::guess Guess first
Is E(XY) = E(X)E(Y) true for every X and Y, or only some? Write your guess.
:::

**Rule** (G&K §6.4, multiplication theorem of expectation), for **independent** X and Y:

$$E(XY) = E(X) · E(Y)$$

Two separate dice: the 36 products x₁x₂ average to 12.25 = 3.5 × 3.5 ✓. One die multiplied by **itself** (not independent): E(X · X) = E(X²) = 91/6 ≈ 15.17, which is **not** 3.5² = 12.25 (03a step 3).

**Answer.** **Correct**, for independent X₁ and X₂ (the multiplication theorem). Without independence it can fail. In MTE A1 the statement that is not correct is (b) (02a step 2).

| Rule | Needs independence? |
|---|---|
| E(aX + b) = aE(X) + b | no |
| Var(aX + b) = a² Var(X) | no |
| E(X + Y) = E(X) + E(Y) | **no** |
| Var(X ± Y) = Var(X) + Var(Y) | **yes** |
| E(XY) = E(X) E(Y) | **yes** |

:::check Check 4
X and Y are independent with E(X) = 2, E(Y) = 5. Find E(3XY) and E(X(Y + 1)).
:::

### 5 · An endless sum: tossing until a head

Some random variables have no largest value. E(X) is then an infinite sum, and it can still be a finite number.

:::q <span class="tag">A1 SA 4</span>
A fair coin is tossed until a head appears. X = number of tosses needed (including the head). Find E(X).
:::

:::guess Guess first
Half the time the first toss is a head. Guess the average number of tosses.
:::

:::note Terms
X = x means x − 1 tails and then a head: P(X = x) = (½)^{x−1} × ½ = (½)^{x}, for x = 1, 2, 3, … . This is a **geometric** random variable (counting tosses up to and including the first head).
:::

E(X) = Σ x (½)^{x} = 1(½) + 2(¼) + 3(⅛) + 4(1/16) + … . The running total climbs towards a limit:

| terms added | 1 | 2 | 3 | 4 | 5 | 6 | 8 |
|---|---|---|---|---|---|---|---|
| running total | 0.5 | 1.0 | 1.375 | 1.625 | 1.781 | 1.875 | 1.961 |

The limit, from the series Σ x qˣ = q/(1 − q)² for 0 < q < 1:

1. With q = ½: Σ x (½)^{x} = (½)/(½)² = **2**.

**Answer.** **E(X) = 2 tosses.** In general, if each try succeeds with probability p, the expected number of tries up to the first success is **1/p** (here 1/½ = 2).

:::note Two ways of counting
Some books (G&K's geometric distribution) count only the **failures** before the first success; that count has mean q/p = 1/p − 1 (here 1). Read which one the question counts.
:::

:::check Check 5
A die is rolled until a six appears. Expected number of rolls?
:::

### 6 · Chebyshev's inequality: a bound from μ and σ alone

03a's σ said "typically give or take σ". Chebyshev makes that a guarantee: at most so much probability can lie far from μ, **whatever the shape**.

:::q <span class="tag">A1 App 4</span>
Marks of engineering students have mean μ = 70 and variance σ² = 25. Use Chebyshev's inequality to estimate the minimum proportion of students scoring between 60 and 80.
:::

:::guess Guess first
60 to 80 is 70 ± 10. With σ = 5, that is μ ± how many σ? Guess the minimum percentage inside.
:::

:::note Terms
**|X − μ|:** the distance of X from the mean, sign dropped. **k:** the number of standard deviations, so "within kσ of μ" means |X − μ| < kσ.
:::

**Chebyshev's inequality** (G&K §6.13). For any X with mean μ and finite variance σ², and any k > 0:

$$P(|X − μ| ≥ kσ) ≤ \frac{1}{k^{2}}        P(|X − μ| < kσ) ≥ 1 − \frac{1}{k^{2}}$$

Read them as: "at most 1/k² of the probability lies k or more SDs away; at least 1 − 1/k² lies closer". With a distance c in X's units (c = kσ, so 1/k² = σ²/c²):

$$P(|X − μ| ≥ c) ≤ \frac{σ^{2}}{c^{2}}        P(|X − μ| < c) ≥ 1 − \frac{σ^{2}}{c^{2}}$$

[[fig:cheb_shapes|What this graph plots: three PDFs with the same mean 70 and SD 5 but different shapes (bell, peaked, flat). Horizontal axis: marks. Height: density. Shaded band: 60 to 80, which is μ ± 2σ. Chebyshev guarantees at least 75% inside for every one of them.|w=78]]

**Reading the figure.** Area inside 60 to 80, computed for each curve: bell 0.954, peaked 0.941, flat 1.000. All are at least 0.75, as Chebyshev promises; it cannot do better without knowing the shape.

**Answer.**

1. σ = √25 = 5. 60 to 80 is |X − 70| < 10, and 10 = 2 × 5, so k = 2.
2. P(60 < X < 80) ≥ 1 − 1/2² = 1 − ¼ = **0.75**.

At least **75%** of the students score between 60 and 80.

<span class="tag">A1 MCQ 5</span> The inequality bounding deviation from the mean: **Chebyshev's** (d). <span class="tag">A1 MCQ 10</span> It applies to **any distribution with finite mean and variance** (b).

:::check Check 6
μ = 50, σ = 4. Give a lower bound for P(38 < X < 62).
:::

### 7 · Bound versus exact: two dice

When the whole distribution is known, the exact probability can be found too. How close is Chebyshev?

:::q <span class="tag">A1 SA 5</span>
Two unbiased dice are thrown; X is the sum. Show that P(|X − 7| ≥ 3) ≤ 35/54 and compare with the actual probability.
:::

:::guess Guess first
Is the true probability close to 35/54 ≈ 0.65, or much smaller?
:::

[[fig:dice_band|What this graph plots: the PMF of the sum of two dice. Horizontal axis: the sum. Bar height: its probability; the number on each bar counts its cells of the 36. Red bars: sums at distance 3 or more from 7 (4 or less, 10 or more).|w=70]]

**Reading the figure.** The red bars hold 1 + 2 + 3 + 3 + 2 + 1 = 12 of the 36 cells.

**Answer.**

1. μ = 7 (step 2), σ² = 35/6 (step 3).
2. Chebyshev with c = 3: P(|X − 7| ≥ 3) ≤ (35/6)/3² = 35/54 ≈ **0.648** ✓.
3. Exact: |X − 7| ≥ 3 means a sum of 4 or less, or 10 or more: 12 cells of 36, **1/3 ≈ 0.333**.

The bound holds but is loose: Chebyshev must cover every shape, so it is cautious for any one shape.

:::check Check 7
X takes 1, 2, 3 with probabilities ¼, ½, ¼. Find the Chebyshev bound for P(|X − 2| ≥ 1) and the exact value.
:::

### 8 · A bound above 1 says nothing

:::q <span class="tag">MTE B1 · 3 marks</span>
A random variable X takes values −1, 1, 3 and 5 with probabilities 1/6, 1/6, 1/6 and 1/2. By Chebyshev's inequality find the upper bound of P(|X − 3| ≥ 1).
:::

:::guess Guess first
Find μ first. Then guess whether σ is bigger or smaller than the distance c = 1.
:::

**Answer.**

1. μ = (−1 + 1 + 3)/6 + 5/2 = 3/6 + 15/6 = **3**.
2. E(X²) = (1 + 1 + 9)/6 + 25/2 = 11/6 + 75/6 = 86/6 = **43/3**.
3. σ² = 43/3 − 9 = **16/3** (σ ≈ 2.31).
4. Chebyshev with c = 1: P(|X − 3| ≥ 1) ≤ σ²/1² = **16/3**. (Professor's key: 16/3.)

:::note What the 16/3 means
Every probability is at most 1, so a bound of 16/3 ≈ 5.3 tells nothing new. σ²/c² is above 1 whenever c < σ: Chebyshev only bites for distances larger than σ. The exact value is 1 − P(X = 3) = **5/6**. Write the key's answer, then this one line: it shows you know what the bound means.
:::

:::check Check 8
Same X. Find the Chebyshev bound for P(|X − 3| ≥ 4) and the exact value.
:::

### 9 · A lower bound for a count

The rules of steps 2–3 give μ and σ² for a count of successes; Chebyshev's second form then bounds the count from below.

:::q <span class="tag">A1 SA 6</span>
A symmetric die is thrown 600 times. Find a lower bound for the probability of getting 80 to 120 sixes.
:::

:::guess Guess first
The expected number of sixes is 100. Is "80 to 120" a wide or a narrow window compared with σ?
:::

**Answer.**

1. One throw: I = 1 for a six, 0 otherwise. E(I) = 1/6; E(I²) = 1/6, so Var(I) = 1/6 − 1/36 = **5/36**.
2. X = number of sixes = sum of 600 independent I's. Step 2: μ = 600 × 1/6 = **100**. Step 3: σ² = 600 × 5/36 = **250/3 ≈ 83.3**. (04a gets the same as np and np(1 − p).)
3. 80 to 120 is |X − 100| ≤ 20, which contains |X − 100| < 20.
4. P(|X − 100| < 20) ≥ 1 − σ²/20² = 1 − (250/3)/400 = 1 − 5/24 = **19/24 ≈ 0.792**.

So the probability of 80 to 120 sixes is **at least 19/24**. (The exact binomial value is about 0.975: again the bound is safe but loose.)

:::check Check 9
A fair coin is tossed 400 times; X = number of heads. Use steps 2–3 and Chebyshev to bound P(180 < X < 220).
:::

---

## Exam form

**Rules** (a, b constants):

| Rule | Needs independence? |
|---|---|
| E(aX + b) = aE(X) + b · Var(aX + b) = a² Var(X) | no |
| E(X + Y) = E(X) + E(Y) | no |
| Var(X ± Y) = Var(X) + Var(Y) | yes |
| E(XY) = E(X) E(Y) | yes |

**Tries up to the first success** (success probability p): E = 1/p.

**Chebyshev's inequality** (any X with finite μ, σ²): P(|X − μ| ≥ kσ) ≤ 1/k²; P(|X − μ| < kσ) ≥ 1 − 1/k². With a distance c: P(|X − μ| ≥ c) ≤ σ²/c²; P(|X − μ| < c) ≥ 1 − σ²/c².

**Procedure: Chebyshev on a given distribution.**

1. μ = Σ x p(x); E(X²) = Σ x² p(x); σ² = E(X²) − μ².
2. Write the event as |X − μ| ≥ c (outside) or |X − μ| < c (inside); read off c.
3. Upper bound σ²/c² (outside) or lower bound 1 − σ²/c² (inside).
4. If asked, compute the exact probability from the table and compare; if the bound exceeds 1, say it gives no information.

## Traps

- Var(aX + b) = a Var(X) + b: wrong twice. The b vanishes and a is squared.
- Var(X − Y) = Var(X) − Var(Y): wrong. Independent variances **add**.
- E(XY) = E(X)E(Y) without independence.
- Thinking E(X + Y) = E(X) + E(Y) needs independence (A1 LA 3's key slip).
- In Chebyshev, using σ where σ² is needed, or c where c² is needed.
- An interval not centred on μ (e.g. 60 to 90 when μ = 70): Chebyshev needs a symmetric band |X − μ| < c; use the largest symmetric band inside it.

## Self-test

1. State Chebyshev's inequality in both forms, with k and with c.
2. E(X) = 10, Var(X) = 9. Find E(3X + 2), Var(3X + 2) and Var(2 − X).
3. X, Y independent with Var 2 and 3. Find Var(X − 2Y).
4. A card is drawn from a pack, with replacement, until an ace appears. Expected number of draws?
5. μ = 100, σ = 10. What does Chebyshev say about P(70 < X < 130)?
6. A fair coin is tossed 100 times. Use Chebyshev to bound P(40 < heads < 60).
7. Why can Chebyshev's bound be larger than 1, and what does that tell you?

<!--ANSWERS-->
## Answers

**Check 1.** E = 2(3) − 5 = **1**; Var = 2² × 4 = **16**; SD = **4**.

**Check 2.** 3 × 3.5 = **10.5**.

**Check 3.** Var(X + Y) = **5**; Var(X − Y) = **5**; Var(2X − 3Y) = 4(4) + 9(1) = **25**.

**Check 4.** E(3XY) = 3 × 2 × 5 = **30**. E(X(Y + 1)) = E(XY) + E(X) = 10 + 2 = **12**.

**Check 5.** p = 1/6, so E = **6 rolls**.

**Check 6.** 38 to 62 is 50 ± 12 = μ ± 3σ: P ≥ 1 − 1/9 = **8/9 ≈ 0.889**.

**Check 7.** μ = 2; E(X²) = ¼ + 2 + 9/4 = 4.5; σ² = 0.5. Bound: P ≤ 0.5/1² = **0.5**. Exact: P(X = 1 or 3) = **0.5**. Here the bound is reached exactly, so it cannot be improved in general.

**Check 8.** Bound: (16/3)/4² = **1/3**. Exact: |X − 3| ≥ 4 only for X = −1, so **1/6**.

**Check 9.** One toss: E = ½, Var = ½ − ¼ = ¼. μ = 400 × ½ = 200; σ² = 400 × ¼ = 100. |X − 200| < 20: P ≥ 1 − 100/400 = **0.75**.

**Self-test.**

1. P(|X − μ| ≥ kσ) ≤ 1/k²; P(|X − μ| < kσ) ≥ 1 − 1/k²; P(|X − μ| ≥ c) ≤ σ²/c²; P(|X − μ| < c) ≥ 1 − σ²/c².
2. **32**; **81**; Var(2 − X) = (−1)² × 9 = **9**.
3. 2 + 4 × 3 = **14**.
4. p = 4/52 = 1/13, so **13 draws**.
5. 70 to 130 is μ ± 3σ: P ≥ **8/9**.
6. μ = 50, σ² = 25. |X − 50| < 10: P ≥ 1 − 25/100 = **0.75**.
7. σ²/c² > 1 whenever c < σ. The bound is then true but gives no information.
<!--/ANSWERS-->
