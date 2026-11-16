# 04a — The binomial distribution

<div class="sub">Gupta & Kapoor §7.2 (binomial distribution; Example 7.4 = MTE B3, Example 7.7) · blueprint row 2 "standard probability distributions: binomial" · 3 real questions (MTE B3, A2 MCQ 2, A2 MCQ 9) · needs 01 (independence step 10, complement step 5), 02a (PMF steps 3–5, the 3-children PMF), 03a (E(X) step 1, Var step 4), 03b (sums of independent variables, steps 2–3)</div>

## Map

[[map:1 One yes/no trial > 2 Counting the orders > 3 The binomial formula > 4 Mean np, variance npq > 5 Solving for p > 6 Expected frequency N × P|here=1]]

File 02a built a PMF by listing outcomes (3 children, X = number of boys). Listing works for 8 outcomes, not for 1024. This file replaces the listing with one formula for any count of successes in repeated yes/no trials, then answers MTE B3. File 04b builds the Poisson from it, and 06 approximates it by the normal.

| Symbol | What it means in this file | Typical value |
|---|---|---|
| n | number of trials: how many times the same experiment is repeated (set by the question) | 10 throws |
| p | chance of a success on one trial (set by the coin, die or machine) | ½ (fair die, "even"); 5/8 (irregular die) |
| q | chance of a failure on one trial: q = 1 − p | ½; 3/8 |
| X | number of successes in the n trials: a whole number from 0 to n | 5 evens |
| C(n, x) | number of different orders in which x successes can sit among n trials ("n choose x") | C(10, 5) = 252 |
| B(n, p) | short name for "binomial with n trials and success chance p" | B(10, ½) |
| N | number of repeated sets of n trials (step 6) | 10 000 sets |

**Running example.** A die is thrown 10 times; a **success** is an even face (2, 4 or 6). For a fair die p = 3/6 = ½. MTE B3's die is irregular: steps 5–6 find its p = 5/8 from the data the question gives.

## The questions this file answers

- <span class="tag">MTE B3 · 4 marks</span> An irregular six-faced die is thrown and the expectation that in 10 throws it will give 5 even numbers is twice the expectation that it will give 4 even numbers. How many times in 10000 sets of 10 throws each would you expect it to give no even number? (G&K Example 7.4)
- <span class="tag">A2 MCQ 2</span> For a Binomial distribution where the number of trials is n = 10 and the probability of success is p = 0.5, what is the variance? a) 5 b) 2.5 c) 10 d) 0.25
- <span class="tag">A2 MCQ 9</span> In a Binomial distribution, if the probability of success is p = 0.5, the experiment is performed 12 times. What is the maximum number of successes that can occur: a) 6 b) 8 c) 10 d) 12

---

## Build

### 1 · One yes/no trial

Start with a single throw, before any formula.

:::q Predict
Throw a fair die once and call an even face a success. Count 1 for a success and 0 for a failure. What is the chance of a 1? What is the average of the count over many throws?
:::

:::guess Guess first
Write two numbers: P(count = 1) and the long-run average count.
:::

:::note Terms
**Bernoulli trial:** one experiment with exactly two results, success or failure. **p:** the chance of success on that one trial, set by the object (three even faces out of six gives p = 3/6). **q = 1 − p:** the chance of failure (G&K §7.2).
:::

| count | 0 (odd face) | 1 (even face) |
|---|---|---|
| probability | q = ½ | p = ½ |

Read with 03a: E(count) = 0 × q + 1 × p = **p**. E(count²) = 0² × q + 1² × p = p, so Var(count) = p − p² = p(1 − p) = **pq** (03a step 5, shortcut).

**Answer to the Predict.** P(count = 1) = ½; the long-run average count is p = ½: half the throws are even. Its variance is pq = ¼.

:::check Check 1
Throw a fair die once; success = "six". Find p, q, E(count) and Var(count).
:::

### 2 · Counting the orders

One trial gives p or q. Several trials give a string of successes and failures, and the same number of successes can come in different orders.

:::q Predict
Throw the fair die 3 times. List every string of E (even) and O (odd) that has exactly 2 evens. What is the chance of each string?
:::

:::guess Guess first
Write how many strings have exactly 2 evens, and the chance of one of them.
:::

:::note Terms
**Independent trials:** the result of one throw does not change the chances on the next (01 step 10), so the chance of a string is the product of its trial chances. **C(n, x)** ("n choose x") = n!/(x!(n − x)!): the number of ways to pick which x of the n trials are the successes.
:::

[[fig:binom_paths|What this graph plots: every possible result of three throws as a path, left to right. Each fork is one throw: up = E (even, chance p), down = O (odd, chance q). One end of the tree = one string of three results. Red strings have exactly two evens; each has chance p²q.|w=86]]

| string | chance (each factor = one throw) |
|---|---|
| E E O | p × p × q = p²q |
| E O E | p × q × p = p²q |
| O E E | q × p × p = p²q |

**Answer to the Predict.** Three strings: EEO, EOE, OEE, and C(3, 2) = 3!/(2! 1!) = **3** counts them without listing. Each has chance p²q = (½)²(½) = **1/8**, because the order of the factors does not change the product.

For 10 throws, listing is out of reach (2¹⁰ = 1024 strings), but the count is a formula: C(10, 5) = 10!/(5! 5!) = **252**, C(10, 4) = 10!/(4! 6!) = **210**.

:::check Check 2
(a) List the strings of 4 throws with exactly 2 evens and confirm C(4, 2). (b) Find C(10, 0) and say which string it counts.
:::

### 3 · The binomial formula

Step 2 found two pieces: how many orders, and the chance of one order. Multiplying them gives the whole probability.

:::q Predict
Fair die, 3 throws. Use step 2 to find P(X = 2), where X = number of evens. Then find P(X = 5) for 10 throws.
:::

:::guess Guess first
Write P(X = 2) as a fraction.
:::

:::note Terms
**Binomial distribution B(n, p):** X = the number of successes in **n independent** trials with the **same p** on every trial (G&K §7.2). X takes the values 0, 1, …, n.
:::

**Derivation** (each line from the one before):

1. One particular string with x successes and n − x failures has chance p^{x}q^{n−x} (step 2: multiply the trial chances).
2. Every string with x successes has the same chance (the factors only change order).
3. There are C(n, x) such strings (step 2).
4. The strings cannot happen together, so their chances add (01 step 6): C(n, x) copies of p^{x}q^{n−x}.

$$P(X = x) = C(n, x) p^{x} q^{n−x},    x = 0, 1, …, n$$

Read it back: **how many orders × the chance of one order**.

[[fig:binom_fair10|What this graph plots: the PMF of B(10, ½). Horizontal axis: x, the number of even faces in 10 throws of a fair die. Vertical axis: P(X = x). One bar = the chance of exactly that many evens. Red bar: x = 5.|w=78]]

| x | C(10, x) | P(X = x) = C(10, x)/1024 |
|---|---|---|
| 0 | 1 | 0.0010 |
| 2 | 45 | 0.0439 |
| 5 | 252 | **0.2461** |
| 8 | 45 | 0.0439 |

**Answer to the Predict.** P(X = 2) = C(3, 2)(½)²(½)¹ = 3 × 1/8 = **3/8**. This is 02a's 3-children PMF (1/8, 3/8, 3/8, 1/8): "boy" there is "even" here, both with p = ½. For 10 throws, P(X = 5) = 252 × (½)¹⁰ = 252/1024 = **0.2461**.

:::check Check 3
A fair coin is tossed 6 times. Find (a) P(exactly 4 heads); (b) P(at least 1 head), using the complement (01 step 5).
:::

### 4 · Mean np, variance npq

The formula gives each bar. Exam MCQs ask only for the centre and spread, straight from n and p.

:::q <span class="tag">A2 MCQ 2</span>
For a Binomial distribution where the number of trials is n = 10 and the probability of success is p = 0.5, what is the variance? a) 5 b) 2.5 c) 10 d) 0.25
:::

:::guess Guess first
X is the sum of 10 one-trial counts from step 1. Write its variance using 03b's rule for independent sums.
:::

**Derivation.**

1. X = count₁ + count₂ + … + countₙ: each count is 1 for a success, 0 for a failure (step 1).
2. Means add (03b step 2): E(X) = p + p + … + p = **np**.
3. The trials are independent, so variances add (03b step 3): Var(X) = pq + … + pq = **npq**.
4. SD σ = √(npq).

Read back: the mean is "trials × chance per trial"; the variance shrinks by the factor q. Since q < 1, a binomial's variance is always **less than its mean** (G&K §7.2).

| die, 10 throws | n | p | mean np | variance npq | σ |
|---|---|---|---|---|---|
| fair | 10 | ½ | 5 | 2.5 | 1.581 |
| irregular (step 5) | 10 | 5/8 | 6.25 | 2.344 | 1.531 |

**Answer to the question.** Var = npq = 10 × 0.5 × 0.5 = **2.5**, option (b).

<span class="tag">A2 MCQ 9</span> X counts successes in n trials, so it runs from 0 to n whatever p is: 12 trials give at most **12** successes, option (d). The mean, 6, is the centre, not the maximum.

:::note Impossible pair
G&K Example 7.7: "the mean of a binomial is 3 and the variance is 4" cannot be true: npq = 4 and np = 3 give q = 4/3 > 1.
:::

:::check Check 4
A binomial has mean 4 and variance 3. Find q, p and n.
:::

### 5 · Solving for p from a ratio

So far p was given. MTE B3 hides it inside a sentence about two probabilities.

:::q <span class="tag">MTE B3 · 4 marks</span>
An irregular six-faced die is thrown and the expectation that in 10 throws it will give 5 even numbers is twice the expectation that it will give 4 even numbers. How many times in 10000 sets of 10 throws each would you expect it to give no even number?
:::

:::guess Guess first
"Irregular" means p is not ½. Is an even face likelier or less likely than on a fair die? Write your guess.
:::

**Terms.** Nothing new: X = number of evens in 10 throws, X ~ B(10, p), p unknown. "The expectation that it gives 5 evens is twice that for 4" means P(X = 5) = 2 P(X = 4).

[[fig:binom_die58|What this graph plots: the PMF of B(10, 5/8), the irregular die once p is found. Horizontal axis: x, evens in 10 throws. Vertical axis: P(X = x). Red bars: x = 4 and x = 5; the x = 5 bar is twice the x = 4 bar. The x = 0 bar is too small to see.|w=78]]

**Derivation.**

1. Write both sides with step 3's formula: C(10, 5)p⁵q⁵ = 2 × C(10, 4)p⁴q⁶.
2. Put in the counts from step 2: 252 p⁵q⁵ = 420 p⁴q⁶.
3. Divide both sides by p⁴q⁵ (neither is 0): 252 p = 420 q.
4. So p/q = 420/252 = **5/3**.
5. Use q = 1 − p: 3p = 5(1 − p), so 8p = 5, **p = 5/8**, q = 3/8.

| x | P(X = x) for p = 5/8 |
|---|---|
| 4 | 0.0891 |
| 5 | 0.1782 (= 2 × 0.0891) |
| 0 | 0.000055 |

**Answer (first half).** p = 5/8 = 0.625: even faces are likelier than on a fair die.

:::check Check 5
X ~ B(6, p) and P(X = 3) = P(X = 2). Find p.
:::

### 6 · Expected frequency N × P

The second half of MTE B3 repeats the whole 10-throw experiment many times and asks for a count of sets, not a probability.

:::q <span class="tag">MTE B3 (second half)</span>
How many times in 10000 sets of 10 throws each would you expect it to give no even number?
:::

:::guess Guess first
Is the answer more than 1, about 1, or less than 1? Write a guess before computing.
:::

:::note Terms
**Expected frequency:** in N repeated sets, the expected number of sets showing an event = N × (its probability in one set). It is a mean (03a step 1) of a count of sets, so it need not be a whole number.
:::

**Derivation.**

1. No even in 10 throws: P(X = 0) = C(10, 0)p⁰q¹⁰ = q¹⁰.
2. q = 3/8 (step 5): (3/8)¹⁰ = 59049/1073741824 = 5.499 × 10⁻⁵.
3. Expected sets: N × P(X = 0) = 10000 × 5.499 × 10⁻⁵ = **0.55**.

**Answer to the question.** About **0.55** sets: in 10000 sets of 10 throws, a set with no even face is expected less than once.

:::check Check 6
A fair coin is tossed 6 times, and the 6 tosses are repeated as 640 sets. In how many sets do you expect exactly 4 heads?
:::

---

## Exam form

**Conditions for B(n, p)** (state them when asked "when is the binomial used?"):
1. a fixed number n of trials;
2. each trial has two results, success or failure;
3. the same success chance p on every trial;
4. the trials are independent.

| | Binomial B(n, p) |
|---|---|
| PMF | P(X = x) = C(n, x)p^{x}q^{n−x}, x = 0, 1, …, n |
| Mean | np |
| Variance | npq (always less than the mean) |
| SD | √(npq) |
| Range | 0 to n |

**Procedure "find p from a ratio of probabilities"** (MTE B3):
1. Write each probability with the PMF.
2. Cancel the common powers of p and q.
3. Solve for p/q, then use q = 1 − p.

**Procedure "expected number of sets"**: probability for one set × the number of sets, N × P(X = x).

**Quick table.** P(x + 1) = P(x) × \frac{n − x}{x + 1} × \frac{p}{q}.

## Traps

- Using the binomial when items are drawn **without replacement** from a small lot: p changes from draw to draw (use 02a step 6's combinations).
- "At least one" by adding n terms: use 1 − P(X = 0) = 1 − qⁿ.
- Forgetting C(n, x): p^{x}q^{n−x} is the chance of **one** order only.
- Reporting the mean np as the largest possible value (A2 MCQ 9): the range is 0 to n.
- Accepting a mean smaller than the variance: impossible for a binomial (G&K Example 7.7).

## Self-test

1. State the four conditions for a binomial distribution.
2. X ~ B(5, 0.3). Find P(X = 2) and the mean.
3. A binomial has mean 6 and variance 2.4. Find n and p.
4. Comment: "a binomial distribution has mean 3 and variance 4".
5. In 160 families with 4 children each, how many families are expected to have exactly 2 boys (p = ½)?
6. Find C(8, 3) and say what it counts for 8 throws of a die.
7. X ~ B(4, p) and P(X = 1) = P(X = 2). Find p.

<!--ANSWERS-->
## Answers

**Check 1.** p = 1/6, q = 5/6; E(count) = p = **1/6**; Var = pq = 5/36 = **0.139**.

**Check 2.** (a) EEOO, EOEO, EOOE, OEEO, OEOE, OOEE: 6 strings = C(4, 2) = 4!/(2! 2!) = **6**. (b) C(10, 0) = **1**: the single string with no even face, OOOOOOOOOO.

**Check 3.** (a) C(6, 4)(½)⁶ = 15/64 = **0.2344**. (b) 1 − P(no head) = 1 − (½)⁶ = **63/64** = 0.9844.

**Check 4.** q = 3/4, so p = **1/4**, and n = 4/p = **16**.

**Check 5.** C(6, 3)p³q³ = C(6, 2)p²q⁴ ⇒ 20p = 15q ⇒ p/q = 3/4 ⇒ 4p = 3(1 − p) ⇒ **p = 3/7**.

**Check 6.** P(4 heads) = 15/64 (Check 3); 640 × 15/64 = **150** sets.

**Self-test.**

1. Fixed n; two results per trial; same p each trial; independent trials.
2. C(5, 2)(0.3)²(0.7)³ = 10 × 0.09 × 0.343 = **0.3087**; mean np = **1.5**.
3. q = 2.4/6 = 0.4, p = 0.6, n = 6/0.6 = **10**.
4. Impossible: q = 4/3 > 1; a binomial's variance is less than its mean.
5. P(2 boys) = C(4, 2)/16 = 6/16; 160 × 6/16 = **60** families.
6. C(8, 3) = **56**: the number of orders in which exactly 3 of the 8 throws are even.
7. C(4, 1)pq³ = C(4, 2)p²q² ⇒ 4q = 6p ⇒ p/q = 2/3 ⇒ **p = 2/5**.
<!--/ANSWERS-->
