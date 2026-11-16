# 04 — Binomial and Poisson distributions

<div class="sub">Gupta & Kapoor ch. 7 (§7.2, §7.3) · blueprint row 2 "standard probability distributions: binomial, Poisson" · 11 real questions (MTE, Assignment 2) · needs 02a, 03</div>

## Map

[[map:1 Binomial: the formula > 2 Binomial mean and variance > 3 Poisson: counts of rare events > 4 Finding λ from a given probability > 5 Poisson as a limit of the binomial|here=1]]

## The questions this file answers

- <span class="tag">MTE B3 · 4 marks</span> An irregular six-faced die is thrown; the expectation that in 10 throws it gives 5 even numbers is twice the expectation that it gives 4 even numbers. In 10000 sets of 10 throws, how many times would you expect no even number?
- <span class="tag">MTE A2 · 2 marks</span> In which distribution is the mean the sole parameter? Normal / Poisson / Binomial / Uniform.
- <span class="tag">MTE A4 · 2 marks</span> If X is a Poisson variate with P(X = 0) = ½, then Var(X) is: ln 2 / 1 / 2 / ln 3.
- <span class="tag">A2 B1</span> 3 technicians; daily demand is Poisson with mean 2.5. P(no demand); P(demand is rejected).
- <span class="tag">A2 C3</span> Emails per day are Poisson with mean 5: P(more than 2).
- <span class="tag">A2 D3</span> 1% of jobs wait until the weekend. By the Poisson approximation, P(none of 200 jobs waits).
- <span class="tag">A2 MCQ 2, 3, 7, 9, 12</span> Binomial variance; Poisson property; rare events; maximum successes; sum of Poissons.

---

## Build

### 1 · The binomial formula

File 02a built PMFs by counting outcomes. When the same yes/no trial is repeated, one formula does the counting.

:::q <span class="tag">MTE B3 · 4 marks</span>
An irregular six-faced die is thrown and the expectation that in 10 throws it will give 5 even numbers is twice the expectation that it will give 4 even numbers. How many times in 10000 sets of 10 throws each would you expect it to give no even number?
:::

:::guess Guess first
"Irregular" means P(even) is not ½. Which is likelier on this die, even or odd? Write your guess.
:::

**Terms.**

- **Bernoulli trial**: one trial with two results, success (probability p) or failure (q = 1 − p).
- **Binomial X ~ B(n, p)**: the number of successes in **n independent** trials with the **same p**.

A particular order with x successes has probability p^{x}q^{n−x}; there are C(n, x) orders (G&K §7.2):

$$P(X = x) = C(n, x) p^{x} q^{n−x},    x = 0, 1, …, n$$

**Answer.** X = even numbers in 10 throws, X ~ B(10, p). "Expectation of 5 evens is twice that of 4" means P(X = 5) = 2P(X = 4):

$$C(10, 5)p^{5}q^{5} = 2 C(10, 4)p^{4}q^{6}  ⇒  252p = 2 × 210 q  ⇒  \frac{p}{q} = \frac{420}{252} = \frac{5}{3}$$

So 3p = 5(1 − p), **p = 5/8**, q = 3/8. P(X = 0) = q^{10} = (3/8)^{10} = 5.499 × 10^{−5}.
Expected number of sets with no even: 10000 × 5.499 × 10^{−5} = **0.55**, i.e. less than once in 10000 sets.

[[fig:binom_poisson|Left: the die's B(10, 5/8). Right: the Poisson of step 3.|w=92]]

:::check Check 1
A fair coin is tossed 6 times. Find P(exactly 4 heads) and P(at least 1 head).
:::

### 2 · Binomial mean and variance

Exam MCQs ask for the mean and variance straight from n and p.

:::q <span class="tag">A2 MCQ 2 · 1 mark</span>
For a binomial distribution with n = 10 and p = 0.5, what is the variance? (a) 5 (b) 2.5 (c) 10 (d) 0.25
:::

:::guess Guess first
X is a sum of 10 independent 0-or-1 trials. Use 03b step 3's rule for the variance of a sum.
:::

One trial: E = p, Var = p − p^{2} = pq. A binomial is a sum of n independent trials, so by 03b steps 2–3:

$$E(X) = np,    Var(X) = npq,    σ = √(npq)$$

Since q < 1, a binomial always has variance **less** than its mean.

**Answer.** Var = 10 × 0.5 × 0.5 = **2.5**, option (b).

<span class="tag">A2 MCQ 9</span> p = 0.5, 12 trials: the maximum number of successes is **12** (d). The values run from 0 to n whatever p is.

:::check Check 2
A binomial has mean 4 and variance 3. Find n and p.
:::

### 3 · Poisson: counts of rare events

The binomial needs a fixed n. Many counts have no natural n: calls per hour, defects per metre, demands per day.

:::q <span class="tag">A2 B1</span>
A small IT support desk has 3 technicians available for field visits each day. The number of demands for a technician follows a Poisson distribution with mean 2.5. Find the probability of a day on which (i) there is no demand; (ii) a demand is rejected.
:::

:::guess Guess first
When is a demand rejected? Write the event in terms of X before calculating.
:::

**Term.** **Poisson X ~ P(λ)**: the number of events in a fixed interval when events occur independently at a constant average rate λ (G&K §7.3):

$$P(X = x) = \frac{e^{−λ}λ^{x}}{x!},    x = 0, 1, 2, …        E(X) = Var(X) = λ$$

One parameter, λ, is the mean **and** the variance.

**Answer.** λ = 2.5. (i) P(X = 0) = e^{−2.5} = **0.0821**.
(ii) A demand is rejected when more than 3 arrive: P(X > 3) = 1 − [P(0) + P(1) + P(2) + P(3)].
P(0) = 0.0821, P(1) = 0.0821 × 2.5 = 0.2052, P(2) = 0.2052 × 2.5/2 = 0.2565, P(3) = 0.2565 × 2.5/3 = 0.2138.
Sum = 0.7576, so P(X > 3) = **0.2424**. (Each term = previous × λ/x.)

<span class="tag">MTE A2</span> The distribution whose mean is its sole parameter: **Poisson** (b). <span class="tag">A2 MCQ 3</span> Its unique property: **mean = variance** (c). <span class="tag">A2 MCQ 7</span> Rare events in a fixed interval: **Poisson** (c).

:::check Check 3
<span class="tag">A2 C3</span> Emails per day are Poisson with mean 5. Find P(more than 2 emails).
:::

### 4 · Finding λ from a given probability

Some questions give a probability instead of the mean. Solve for λ first.

:::q <span class="tag">MTE A4 · 2 marks</span>
If X is a Poisson variate such that P(X = 0) = ½, then Var(X) is: (a) ln 2 (b) 1 (c) 2 (d) ln 3
:::

:::guess Guess first
Write P(X = 0) from the formula. What is left when x = 0?
:::

**Answer.** P(X = 0) = e^{−λ} = ½ ⇒ λ = ln 2. For a Poisson, Var = λ = **ln 2** (a).

**Same idea, two probabilities.** If P(X = 1) = P(X = 2): e^{−λ}λ = e^{−λ}λ^{2}/2 ⇒ λ = 2.

:::check Check 4
X is Poisson with P(X = 2) = 9P(X = 4) + 90P(X = 6). Find λ. <span class="tag">G&K Ex. 7.30</span>
:::

### 5 · Poisson as the limit of the binomial

When n is large and p small, the binomial's arithmetic is heavy; the Poisson replaces it.

:::q <span class="tag">A2 D3</span>
One percent of jobs arriving at a computer system wait until the weekend for scheduling. Using the Poisson approximation to the binomial, find the probability that among 200 jobs none waits until the weekend.
:::

:::guess Guess first
What is the mean number of waiting jobs among 200?
:::

**Rule** (G&K §7.3): if n → ∞ and p → 0 with np = λ fixed, B(n, p) → P(λ). Use it when n is large (≳ 20) and p small (≲ 0.05).

[[fig:poisson_limit|B(200, 0.01) and P(2) are almost the same bars.|w=70]]

**Answer.** λ = np = 200 × 0.01 = 2. P(X = 0) ≈ e^{−2} = **0.1353**. (The exact binomial 0.99^{200} = 0.1340.)

<span class="tag">A2 MCQ 12</span> X, Y independent Poisson(λ₁), Poisson(λ₂): X + Y is **Poisson with mean λ₁ + λ₂** (c). Means add (03b step 2), and the sum of two independent Poisson counts is again a count of rare events.

:::check Check 5
2% of fuses are defective. In a box of 100, use the Poisson approximation to find P(at most 2 defective).
:::

---

## Exam form

| | Binomial B(n, p) | Poisson P(λ) |
|---|---|---|
| Story | successes in n independent trials, same p | events in a fixed interval at rate λ |
| PMF | C(n, x)p^{x}q^{n−x}, x = 0…n | e^{−λ}λ^{x}/x!, x = 0, 1, 2, … |
| Mean | np | λ |
| Variance | npq (< mean) | λ (= mean) |
| Parameters | n, p | λ only |

**Recurrences** (fast tables): binomial P(x + 1) = P(x) · \frac{n − x}{x + 1} · \frac{p}{q}; Poisson P(x + 1) = P(x) · \frac{λ}{x + 1}.

**Approximation.** B(n, p) ≈ P(np) when n is large and p is small.

**Procedure for "expected number of times".** Find the probability for one set, then multiply by the number of sets (N · P(X = x)).

## Traps

- Using the binomial when trials are drawn **without replacement** from a small lot (p changes; file 02a step 6's combinations apply).
- "At least one" by adding many terms: use 1 − P(0).
- Reading "the mean" in a Poisson question as n or p: λ is the mean for the stated interval. Rescale λ if the interval changes (rate 2 per hour → λ = 6 for 3 hours).
- Rejecting "more than 3" with P(X ≥ 3) instead of P(X > 3) = P(X ≥ 4).

## Self-test

1. State the conditions for a binomial distribution.
2. B(5, 0.3): find P(X = 2) and the mean.
3. Mean 6, variance 2.4 for a binomial: find n and p.
4. A Poisson variate has P(X = 1) = P(X = 2). Find P(X = 0).
5. Accidents average 3 per week. Find P(no accident in a week) and P(no accident in 2 weeks).
6. Show the Poisson mean is λ in one line of algebra.
7. 5% of items are defective. In a sample of 40, find P(exactly 1 defective) by the Poisson approximation.

<!--ANSWERS-->
## Answers

**Check 1.** C(6, 4)/64 = **15/64**; 1 − (½)^{6} = **63/64**.

**Check 2.** q = 3/4, p = 1/4, n = 4/p = **16**.

**Check 3.** 1 − e^{−5}(1 + 5 + 12.5) = 1 − 18.5 × 0.006738 = **0.8753**.

**Check 4.** e^{−λ}λ^{2}/2 = 9e^{−λ}λ^{4}/24 + 90e^{−λ}λ^{6}/720 ⇒ multiply by 8/(e^{−λ}λ^{2}): 4 = 3λ^{2} + λ^{4} ⇒ λ^{4} + 3λ^{2} − 4 = 0 ⇒ (λ^{2} + 4)(λ^{2} − 1) = 0 ⇒ **λ = 1**.

**Check 5.** λ = 2: e^{−2}(1 + 2 + 2) = 5e^{−2} = **0.6767**.

**Self-test.**

1. Fixed number n of trials; two outcomes each; same p each trial; trials independent.
2. C(5, 2)(0.3)^{2}(0.7)^{3} = 10 × 0.09 × 0.343 = **0.3087**; mean **1.5**.
3. q = 2.4/6 = 0.4, p = 0.6, n = 6/0.6 = **10**.
4. λ = 2; P(0) = e^{−2} = **0.1353**.
5. e^{−3} = **0.0498**; λ = 6 for 2 weeks: e^{−6} = **0.0025**.
6. E(X) = Σ x e^{−λ}λ^{x}/x! = λ Σ e^{−λ}λ^{x−1}/(x − 1)! = λ × 1.
7. λ = 2: P(1) = 2e^{−2} = **0.2707**.
<!--/ANSWERS-->
