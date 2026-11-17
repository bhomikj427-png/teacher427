# 12b — Computing α and β

<div class="sub">Professor's slides "Hypothesis Testing" (ppt 8) slides 15, 20–22 · Gupta & Kapoor §16.2.4–16.2.7 (critical region W, α = P(x ∈ W ∣ H₀), β = P(x ∈ W̄ ∣ H₁), power function) · blueprint row 4 "critical region, Type I and Type II errors" · 6 real questions (A4 C1–C3; slides 20, 21, 22) · needs 12a (α, β, power, steps 5–7), 04a (the binomial formula, step 3), 05 (uniform length ratio, step 2; exponential survival, step 8), 02b (area under a density)</div>

## Map

[[map:1 α and β as areas > 2 A different critical region > 3 A curved density > 4 Counting instead of areas > 5 Reject on a high count > 6 Reject on a low count > 7 The power function|here=1]]

File 12a defined α, the chance of rejecting a true H₀, and β, the chance of keeping a false one, and found them for an average with the normal table. The assignment's 6-mark questions give a simpler setting: **one observation** (or one count), a density or a binomial under H₀ and another under H₁, and a critical region W. Then α is the probability of W under H₀'s distribution and β the probability of the rest under H₁'s. Steps 1–3 do this with areas (uniform, exponential), steps 4–6 with binomial sums, and step 7 lets the true parameter vary, giving the power function. Files 13–16 return to tests with tables.

| Symbol | What it means in this file | Typical value |
|---|---|---|
| θ | the parameter that H₀ and H₁ disagree about | 1 under H₀, 2 under H₁ |
| f(x, θ) | the density of the one observation X for that θ | 1/θ on 0 ≤ x ≤ θ |
| W | critical region: the x values for which H₀ is rejected | x ≥ 0.5 |
| W̄ | acceptance region: every other x | x < 0.5 |
| α | P(X in W) using H₀'s θ | 0.5 |
| β | P(X in W̄) using H₁'s θ | 0.25 |
| p | probability of success in one trial (binomial steps 4–6) | ½ under H₀ |
| P(θ) | power function: P(X in W) for any θ | (0.1)^{θ+1} |

**Running example.** A4 C1: one observation X from f(x, θ) = 1/θ on 0 ≤ x ≤ θ (a uniform, file 05); **H₀: θ = 1** (X uniform on 0 to 1) against **H₁: θ = 2** (X uniform on 0 to 2). Steps 1–2 use it.

## The questions this file answers

- <span class="tag">A4 C1</span> Given the frequency function f(x, θ) = 1/θ, 0 ≤ x ≤ θ, and f(x, θ) = 0 otherwise, you are testing H₀: θ = 1 against H₁: θ = 2 by means of a single observed value x. What would be the sizes of the Type I and Type II errors if you choose the following intervals as the critical regions? (i) 0.5 ≤ x (ii) 1 ≤ x ≤ 1.5.
- <span class="tag">Slides p.21</span> X has density f(x, θ) = (1/θ)e^{−x/θ}, x ≥ 0. H₀: θ = 5 is tested against H₁: θ = 10, rejecting H₀ if the observed x is 15 or more. Find α and β.
- <span class="tag">Slides p.20</span> In 4 binomial trials, H₀: p = 1/3 is tested against H₁: p = 1/2; H₀ is accepted if x ≤ 2 successes. Find α and β.
- <span class="tag">A4 C2</span> Let p be the probability that a coin will fall heads in a single toss. To test H₀: p = 1/2 against H₁: p = 3/4, the coin is tossed 5 times and H₀ is rejected if more than 3 heads are obtained. Find the probability of Type I error. (The key also gives β.)
- <span class="tag">A4 C3</span> A manufacturer claims that 75% of its products meet the required specifications. A random sample of 4 products is selected to test H₀: p = 0.75 against H₁: p = 0.5. Reject H₀ if fewer than 3 products meet the specifications. Calculate the probabilities of Type I and Type II errors.
- <span class="tag">Slides p.22</span> X has density f(x, θ) = (1 + θ)x^θ, 0 ≤ x ≤ 1. H₀: θ = 2 is tested with the critical region x ≤ 0.1. Find (i) α (ii) the probability of rejecting H₀ when θ = 3 (iii) the power function.

Blueprint row 4's 6-mark slot fits exactly one of these.

---

## Build

### 1 · α and β as areas

File 12a found α and β as tail areas of a normal curve. With one observation from a flat density, the areas are rectangles.

:::q <span class="tag">A4 C1 (i)</span>
f(x, θ) = 1/θ, 0 ≤ x ≤ θ. Test H₀: θ = 1 against H₁: θ = 2 with one observed x. Find the sizes of the Type I and Type II errors if the critical region is 0.5 ≤ x.
:::

:::guess Guess first
Under H₀, X is spread evenly over 0 to 1. What share of that lies at 0.5 or above?
:::

:::note Terms
**Size of the Type I error:** α = P(X ∈ W ∣ H₀), the area of H₀'s density over W. **Size of the Type II error:** β = P(X ∈ W̄ ∣ H₁), the area of H₁'s density over the acceptance region (G&K §16.2.6). "Size" here just means "probability".
:::

[[fig:alpha_beta|What this graph plots: across: the observed x; up: its density. Blue: H₀ (θ = 1), height 1 on 0 to 1. Purple: H₁ (θ = 2), height ½ on 0 to 2. Dashed line: x = 0.5, the start of the critical region. Red: the area of H₀ over the critical region (α). Amber: the area of H₁ over the acceptance region (β).|w=80]]

**Working** (05 step 2: for a uniform, probability = length × height):

1. W = {x ≥ 0.5}, W̄ = {x < 0.5}.
2. α = P(X ≥ 0.5 ∣ θ = 1) = (1 − 0.5) × 1 = **0.5**.
3. β = P(X < 0.5 ∣ θ = 2) = (0.5 − 0) × ½ = **0.25**.

**Answer to A4 C1 (i).** **α = 0.5, β = 0.25** (power 1 − β = 0.75). Half of all true-H₀ observations are wrongly rejected: a poor test, but a valid answer.

| Region | Under H₀ (θ = 1) | Under H₁ (θ = 2) |
|---|---|---|
| W: x ≥ 0.5 | α = 0.5 | power = 0.75 |
| W̄: x < 0.5 | 0.5 | β = 0.25 |

Each column adds to 1: one curve, split into two pieces.

:::check Check 1
Same H₀ and H₁, critical region x ≥ 0.8. Find α and β.
:::

### 2 · A different critical region

Step 1's region rejected half the true-H₀ values. Part (ii) moves W to where H₀ cannot reach.

:::q <span class="tag">A4 C1 (ii)</span>
Same test: find the sizes of the Type I and Type II errors if the critical region is 1 ≤ x ≤ 1.5.
:::

:::guess Guess first
Can an observation from H₀ (0 to 1) land between 1 and 1.5? What does that make α?
:::

[[fig:ab_region2|What this graph plots: the same two densities as step 1. The critical region is now 1 to 1.5 (between the dashed lines). Blue: the area of H₁ over that region (power 0.25). Amber: the rest of H₁, which leads to "do not reject" (β = 0.75). H₀'s density is zero beyond x = 1, so it has no area in the region.|w=80]]

**Working.**

1. α = P(1 ≤ X ≤ 1.5 ∣ θ = 1). Under H₀, X ≤ 1, and the single point x = 1 has zero area, so **α = 0**.
2. P(1 ≤ X ≤ 1.5 ∣ θ = 2) = 0.5 × ½ = 0.25 (the power).
3. β = 1 − 0.25 = **0.75**.

**Answer to A4 C1 (ii).** **α = 0, β = 0.75.** This region never rejects a true H₀, but misses a true H₁ three times in four.

| Region | α | β |
|---|---|---|
| (i) x ≥ 0.5 | 0.5 | 0.25 |
| (ii) 1 ≤ x ≤ 1.5 | 0 | 0.75 |

The trade-off of 12a step 7 again: shrinking one error grew the other.

:::check Check 2
Same test, critical region x ≥ 1. Find α and β. Compare with (ii): which region is better, and why?
:::

### 3 · A curved density

Steps 1–2 had flat densities, so areas were rectangles. With a curved density the area is an integral; for the exponential it has a short form (05 step 8).

:::q <span class="tag">Slides p.21</span>
X has density f(x, θ) = (1/θ)e^{−x/θ}, x ≥ 0. H₀: θ = 5 is tested against H₁: θ = 10, rejecting H₀ if the observed x is 15 or more. Find α and β.
:::

:::guess Guess first
Under H₀ the mean is 5, so 15 is three means out. Is α large or small?
:::

:::note Terms
**θ here is the mean** of the exponential (rate λ = 1/θ, file 05). **Survival:** P(X ≥ c) = e^{−c/θ}, the area to the right of c (05 step 8 with λ = 1/θ).
:::

[[fig:expo_ab|What this graph plots: across: the observed x; up: its density. Blue: H₀ (θ = 5), steep. Purple: H₁ (θ = 10), flatter. Dashed line: x = 15, the start of the critical region. Red: the thin area of H₀ beyond 15 (α). Amber: the area of H₁ below 15 (β).|w=82]]

| x | H₀ density (1/5)e^{−x/5} | H₁ density (1/10)e^{−x/10} |
|---|---|---|
| 0 | 0.200 | 0.100 |
| 5 | 0.0736 | 0.0607 |
| 15 | 0.0100 | 0.0223 |
| 30 | 0.0005 | 0.0050 |

**Working.**

1. α = P(X ≥ 15 ∣ θ = 5) = ∫₁₅^∞ (1/5)e^{−x/5} dx = e^{−15/5} = e^{−3} = **0.0498**.
2. β = P(X < 15 ∣ θ = 10) = ∫₀¹⁵ (1/10)e^{−x/10} dx = 1 − e^{−15/10} = 1 − e^{−1.5} = 1 − 0.2231 = **0.7769**.
3. Power = e^{−1.5} = 0.2231.

**Answer to slides p.21.** **α = e^{−3} ≈ 0.0498, β = 1 − e^{−3/2} ≈ 0.7769.** A small α (about 5%), bought with a large β: one observation cannot tell the two curves apart well.

:::check Check 3
Same densities, but reject H₀ if x ≥ 10. Find α and β.
:::

### 4 · Counting instead of areas

Steps 1–3 had a continuous X. When X is a count of successes, probabilities are bars, and α and β become sums of binomial probabilities (04a step 3).

:::q <span class="tag">Slides p.20</span>
In 4 binomial trials, H₀: p = 1/3 is tested against H₁: p = 1/2; H₀ is accepted if x ≤ 2 successes. Find α and β.
:::

:::guess Guess first
Write W as a list of counts. Which p do you use for α?
:::

:::note Terms
**X:** the number of successes in n = 4 trials; P(X = k) = C(4, k) p^{k} (1 − p)^{4−k} (04a step 3). **W:** "accept if x ≤ 2" means **reject if x = 3 or 4**.
:::

[[fig:binom_ab|What this graph plots: across: x, the number of successes in 4 trials; up: its probability. Left: if H₀ is true (p = 1/3); the red bars x = 3, 4 are the critical region, and they add to α. Right: if H₁ is true (p = 1/2); the amber bars x = 0, 1, 2 lead to "accept H₀", and they add to β.|w=88]]

**Working.**

1. W = {3, 4}, W̄ = {0, 1, 2}.
2. α = P(X ≥ 3 ∣ p = 1/3) = C(4, 3)(1/3)³(2/3) + (1/3)⁴ = 4 × 2/81 + 1/81 = 8/81 + 1/81 = 9/81 = **1/9**.
3. β = P(X ≤ 2 ∣ p = 1/2) = 1 − P(X ≥ 3 ∣ ½) = 1 − [C(4, 3)(½)⁴ + (½)⁴] = 1 − 5/16 = **11/16**.

**Answer to slides p.20.** **α = 1/9 ≈ 0.111, β = 11/16 = 0.6875.** Using the complement in line 3 (two terms instead of three) is the usual shortcut.

:::check Check 4
Same test, but H₀ is rejected only if x = 4. Find α and β.
:::

### 5 · Reject on a high count

Step 4's procedure, on the assignment's coin. The words "more than 3" decide W.

:::q <span class="tag">A4 C2</span>
Let p be the probability that a coin will fall heads in a single toss. To test H₀: p = 1/2 against H₁: p = 3/4, the coin is tossed 5 times and H₀ is rejected if more than 3 heads are obtained. Find the probability of Type I error. (The key also gives the Type II error.)
:::

:::guess Guess first
"More than 3 heads" is which counts? Guess α as a fraction of 32.
:::

[[fig:binom_coin|What this graph plots: across: x, the number of heads in 5 tosses; up: its probability. Left: a fair coin (H₀, out of 32); the red bars x = 4, 5 are the critical region. Right: p = 3/4 (H₁, counts out of 1024); the amber bars x = 0 to 3 lead to "do not reject".|w=88]]

**Working.** X = number of heads ~ B(5, p).

1. "More than 3" = 4 or 5: W = {4, 5}, W̄ = {0, 1, 2, 3}.
2. α = P(X ≥ 4 ∣ p = ½) = [C(5, 4) + C(5, 5)] × (½)⁵ = (5 + 1)/32 = 6/32 = **3/16 = 0.1875**.
3. P(X ≥ 4 ∣ p = ¾) = C(5, 4)(¾)⁴(¼) + (¾)⁵ = 5 × 81/1024 + 243/1024 = (405 + 243)/1024 = 648/1024.
4. β = 1 − 648/1024 = 376/1024 = **47/128 = 0.3672**.
5. Power = 648/1024 = 81/128 = 0.6328.

**Answer to A4 C2.** **α = 3/16**; β = 47/128 (both match the key).

:::check Check 5
Same coin, but H₀ is rejected if **at least 3** heads are obtained. Find α and β.
:::

### 6 · Reject on a low count

Steps 4–5 rejected on high counts, because H₁'s p was larger. When H₁'s p is smaller, the critical region moves to the low counts.

:::q <span class="tag">A4 C3</span>
A manufacturer claims that 75% of its products meet the required specifications. A random sample of 4 products is selected to test H₀: p = 0.75 against H₁: p = 0.5. Reject H₀ if fewer than 3 products meet the specifications. Calculate the probabilities of Type I and Type II errors.
:::

:::guess Guess first
"Fewer than 3" is which counts? Under H₀, is that likely or unlikely?
:::

[[fig:binom_c3|What this graph plots: across: x, the number of the 4 products that meet the specifications; up: its probability. Left: H₀, p = 0.75 (counts out of 256); the red bars x = 0, 1, 2 are the critical region. Right: H₁, p = 0.5 (out of 16); the amber bars x = 3, 4 lead to "do not reject".|w=88]]

**Working.** X = number meeting the specifications ~ B(4, p).

1. "Fewer than 3" = 0, 1 or 2: W = {0, 1, 2}, W̄ = {3, 4}.
2. Under H₀ (p = ¾, q = ¼), with 4⁴ = 256 as the denominator: P(0) = 1/256, P(1) = 4 × 3/256 = 12/256, P(2) = 6 × 9/256 = 54/256.
3. α = (1 + 12 + 54)/256 = 67/256 = **0.2617**.
4. β = P(X ≥ 3 ∣ p = ½) = [C(4, 3) + C(4, 4)]/16 = 5/16 = **0.3125**.

**Answer to A4 C3.** **α = 0.2617, β = 0.3125** (both match the key).

| | W (reject) | W̄ (do not reject) |
|---|---|---|
| "more than 3" (A4 C2) | 4, 5 | 0–3 |
| "fewer than 3" (A4 C3) | 0, 1, 2 | 3, 4 |
| "accept if x ≤ 2" (slide 20) | 3, 4 | 0, 1, 2 |

:::check Check 6
Same products, but reject H₀ only if **fewer than 2** meet the specifications. Find α and β.
:::

### 7 · The power function

Steps 1–6 found β for **one** value of θ under H₁. The power function gives P(reject H₀) for **every** θ at once.

:::q <span class="tag">Slides p.22</span>
X has density f(x, θ) = (1 + θ)x^θ, 0 ≤ x ≤ 1. H₀: θ = 2 is tested with the critical region x ≤ 0.1. Find (i) α (ii) the probability of rejecting H₀ when θ = 3 (iii) the power function.
:::

:::guess Guess first
Under θ = 2 the density is 3x², tiny near x = 0. Is α large or small?
:::

:::note Terms
**Power function P(θ):** P(X ∈ W) computed with the parameter equal to θ. At θ = H₀'s value it equals α; at a value from H₁ it equals the power 1 − β (G&K §16.2.7).
:::

**Working.**

1. For any θ: P(X ≤ 0.1) = ∫₀^{0.1} (1 + θ)x^θ dx = [x^{θ+1}]₀^{0.1} = (0.1)^{θ+1}.
2. (i) θ = 2: α = ∫₀^{0.1} 3x² dx = (0.1)³ = **0.001**.
3. (ii) θ = 3: P(reject) = ∫₀^{0.1} 4x³ dx = (0.1)⁴ = **0.0001**, so β = 1 − 0.0001 = 0.9999.
4. (iii) **Power function P(θ) = (0.1)^{θ+1}.**

[[fig:power_fn|What this graph plots: across: θ, the true parameter; up (log scale: each grid line is 10 times the one below): the probability (0.1)^{θ+1} that the test rejects H₀. The dot at θ = 2 is α; the other dots are the power at θ = 0, 1 and 3.|w=78]]

| θ | 0 | 1 | 2 (H₀) | 3 |
|---|---|---|---|---|
| P(reject) = (0.1)^{θ+1} | 0.1 | 0.01 | 0.001 = α | 0.0001 |

**Answer to slides p.22.** **(i) α = 0.001; (ii) (0.1)⁴ = 0.0001; (iii) P(θ) = (0.1)^{θ+1}.** The power falls as θ grows: a larger θ piles the density near x = 1, so small x become rarer. This region catches alternatives with θ **below** 2, not above; against θ = 3 it rejects less often than when H₀ is true.

:::check Check 7
(a) Same test: find the power at θ = −0.5. (b) Change the critical region to x ≤ 0.2: find α at θ = 2.
:::

---

## Exam form

**Definitions** (G&K §16.2.4–16.2.7). Critical region W: the observations for which H₀ is rejected; W̄: the rest. Size of the Type I error α = P(x ∈ W ∣ H₀). Size of the Type II error β = P(x ∈ W̄ ∣ H₁). Power 1 − β = P(x ∈ W ∣ H₁). Power function P(θ) = P(x ∈ W ∣ θ); P(θ₀) = α.

**Procedure (6 marks).**

1. Write W and W̄ as sets of x (turn "more than 3" into {4, 5}, "fewer than 3" into {0, 1, 2}).
2. α: the probability of W under **H₀'s** distribution (area for a density, sum of pmf values for a count).
3. β: the probability of W̄ under **H₁'s** distribution (or 1 − P(W ∣ H₁)).
4. Power = 1 − β if asked; P(θ) for every θ if a power function is asked.

**Tools.** Uniform: length × height. Exponential (mean θ): P(X ≥ c) = e^{−c/θ}. Binomial: C(n, k) p^{k} q^{n−k}. Density (1 + θ)x^θ: P(X ≤ c) = c^{θ+1}.

## Traps

- Computing β with H₀'s parameter: β always uses H₁'s.
- "More than 3" is {4, 5}, not {3, 4, 5}; "fewer than 3" is {0, 1, 2}.
- β is P(**not** rejecting under H₁), not P(rejecting under H₁): that is the power.
- For the exponential written as (1/θ)e^{−x/θ}, θ is the mean, so P(X ≥ c) = e^{−c/θ}, not e^{−θc}.
- Forgetting that H₀'s density can be zero over part of W (A4 C1 (ii): α = 0).
- Expecting a power function to be large wherever H₀ is false: it depends on which side W was built for.

## Self-test

1. One observation from U(0, θ). H₀: θ = 1, H₁: θ = 1.5; reject H₀ if x > 0.9. Find α and β.
2. One observation from f(x, θ) = (1/θ)e^{−x/θ}. H₀: θ = 1, H₁: θ = 3; reject H₀ if x ≥ 3. Find α and β.
3. X ~ B(6, p). H₀: p = 0.5, H₁: p = 0.8; reject H₀ if x ≥ 5. Find α and β.
4. Slide 22's density with the critical region x ≥ 0.9: find the power function, and α for H₀: θ = 2.
5. Why does β need a stated value of the parameter under H₁, while α does not?
6. In Self-test 3, can a critical region of the form x ≥ c give α exactly 0.05? Why not?

<!--ANSWERS-->
## Answers

**Check 1.** α = P(X ≥ 0.8 ∣ θ = 1) = 0.2 × 1 = **0.2**. β = P(X < 0.8 ∣ θ = 2) = 0.8 × ½ = **0.4**.

**Check 2.** α = P(X ≥ 1 ∣ θ = 1) = **0**. β = P(X < 1 ∣ θ = 2) = 1 × ½ = **0.5**. **x ≥ 1 is better**: the same α = 0, but β falls from 0.75 to 0.5, because it rejects on every x that H₀ cannot produce (1 to 2), not only 1 to 1.5.

**Check 3.** α = P(X ≥ 10 ∣ θ = 5) = e^{−2} = **0.1353**. β = P(X < 10 ∣ θ = 10) = 1 − e^{−1} = **0.6321**. Compared with step 3, α rose and β fell.

**Check 4.** α = P(X = 4 ∣ 1/3) = (1/3)⁴ = **1/81 ≈ 0.0123**. β = P(X ≤ 3 ∣ ½) = 1 − 1/16 = **15/16 = 0.9375**.

**Check 5.** W = {3, 4, 5}. α = (10 + 5 + 1)/32 = **16/32 = ½**. β = P(X ≤ 2 ∣ ¾) = [1 + 5 × 3 + 10 × 9]/1024 = (1 + 15 + 90)/1024 = 106/1024 = **53/512 ≈ 0.1035**.

**Check 6.** W = {0, 1}. α = (1 + 12)/256 = **13/256 ≈ 0.0508**. β = P(X ≥ 2 ∣ ½) = (6 + 4 + 1)/16 = **11/16 = 0.6875**.

**Check 7.** (a) (0.1)^{0.5} = √0.1 = **0.3162**. (b) α = (0.2)³ = **0.008**.

**Self-test.**

1. α = P(X > 0.9 ∣ θ = 1) = **0.1**. β = P(X ≤ 0.9 ∣ θ = 1.5) = 0.9/1.5 = **0.6**.
2. α = e^{−3/1} = **0.0498**. β = 1 − e^{−3/3} = 1 − e^{−1} = **0.6321**.
3. α = P(X ≥ 5 ∣ 0.5) = (6 + 1)/64 = **7/64 ≈ 0.1094**. P(X ≥ 5 ∣ 0.8) = 6(0.8)⁵(0.2) + (0.8)⁶ = 0.393216 + 0.262144 = 0.65536, so β = **0.34464**.
4. P(X ≥ 0.9) = 1 − (0.9)^{θ+1}, so P(θ) = **1 − (0.9)^{θ+1}**; at θ = 2, α = 1 − 0.729 = **0.271**.
5. α is computed under H₀, which states one value (θ = θ₀). H₁ usually allows many values, and β is different for each, so a value must be chosen; as a function of that value, 1 − β is the power function.
6. **No.** X takes only whole values, so α can only be one of the tail sums 1/64, 7/64, 22/64, …; 0.05 lies between 1/64 ≈ 0.016 and 7/64 ≈ 0.109.
<!--/ANSWERS-->
