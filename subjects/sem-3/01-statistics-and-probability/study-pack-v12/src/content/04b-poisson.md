# 04b — The Poisson distribution

<div class="sub">Gupta & Kapoor §7.3 (Poisson distribution: limit of the binomial, additive property) · blueprint row 2 "standard probability distributions: Poisson" · 9 real questions (MTE A2, MTE A4, A2 B1, C3, D3, MCQ 3, 7, 12; G&K Ex. 7.30 as a Check) · needs 01 (complement, step 5), 02a (PMF, step 3), 03a (E(X), Var), 03b (sums, step 2), 04a (binomial formula step 3, mean np step 4)</div>

## Map

[[map:1 Counting events at a rate > 2 Mean equals variance > 3 Finding λ from a probability > 4 At least, more than, rejected > 5 Poisson as a stand-in for the binomial > 6 Adding two Poisson counts|here=1]]

File 04a counted successes in a fixed number n of trials. Many counts have no n: demands at a help desk per day, emails per day, defects per metre. This file gives the distribution for such counts, the Poisson, which needs only the average rate λ. File 05 measures the gap between the same events (the exponential), and 06 approximates both by the normal.

| Symbol | What it means in this file | Typical value |
|---|---|---|
| λ | average number of events in the stated interval ("lambda"): set by the rate and the length of the interval | 2.5 demands per day |
| X | number of events in that interval: 0, 1, 2, … with no upper limit | 3 demands |
| e | the constant 2.71828…; e^{−λ} is the chance of no event | e^{−2.5} = 0.0821 |
| x! | x factorial, 1 × 2 × … × x; 0! = 1 | 3! = 6 |
| P(λ) | short name for "Poisson with mean λ" | P(2.5) |
| n, p | the binomial's trials and success chance (04a), used in step 5 | n = 200, p = 0.01 |

**Running example.** A small IT support desk has 3 technicians for field visits each day. The number of demands in a day is Poisson with mean **λ = 2.5** (A2 B1). Steps 1, 2 and 4 use it.

## The questions this file answers

- <span class="tag">A2 B1</span> A small IT support desk has 3 technicians available for field visits on a day-to-day basis. The number of demands for a technician is known to follow a Poisson distribution with a mean of 2.5. Find the probability of a day on which (i) there is no demand for a technician and (ii) the demand is rejected.
- <span class="tag">MTE A2 · 2 marks</span> In which distribution is the mean the sole parameter? Normal / Poisson / Binomial / Uniform.
- <span class="tag">MTE A4 · 2 marks</span> If X is a Poisson variate such that P(X = 0) = ½, then Var(X) is: (a) ln 2 (b) 1 (c) 2 (d) ln 3
- <span class="tag">A2 C3</span> Suppose the number of emails a researcher receives per day follows a Poisson distribution with a mean of 5. Find the exact probability that they will receive more than 2 emails in a given day.
- <span class="tag">A2 D3</span> One percent of jobs arriving at a computer system need to wait until weekend for scheduling, owing to core-size limitations. Find the probability using Poisson approximation to binomial that among a sample of 200 jobs, there are no jobs that have to wait until weekends.
- <span class="tag">A2 MCQ 3, 7, 12</span> A unique property of the Poisson; the distribution for rare events in a fixed interval; the distribution of X + Y for independent Poissons.

---

## Build

### 1 · Counting events at a rate

Start from the desk: demands arrive one by one, independently, about 2.5 a day on average, and nobody fixes how many could come.

:::q <span class="tag">A2 B1 (i)</span>
The number of demands in a day is Poisson with mean 2.5. Find the probability of a day on which there is no demand for a technician.
:::

:::guess Guess first
Is a day with no demand rare (under 10%), common (about 30%), or likely (over 50%)? Write your guess.
:::

:::note Terms
**λ:** the average number of events in the stated interval; it is set by the rate × the length of the interval. **Poisson distribution P(λ):** X = the number of events in a fixed interval when events happen independently, one at a time, at a constant average rate (G&K §7.3). X can be 0, 1, 2, … with no upper limit.
:::

$$P(X = x) = \frac{e^{−λ}λ^{x}}{x!},    x = 0, 1, 2, …$$

Read it back: e^{−λ} is the chance of **no** event; each extra event multiplies by λ and divides by its position x. So each term = the previous term × λ/x.

[[fig:pois_desk|What this graph plots: the PMF of P(2.5), the desk's demands. Horizontal axis: x, demands in one day. Vertical axis: P(X = x). One bar = the chance of exactly that many demands. Red bars (x ≥ 4) are used in step 4.|w=78]]

| x | P(X = x) | from the previous term |
|---|---|---|
| 0 | e^{−2.5} = **0.0821** | — |
| 1 | 0.2052 | 0.0821 × 2.5/1 |
| 2 | 0.2565 | 0.2052 × 2.5/2 |
| 3 | 0.2138 | 0.2565 × 2.5/3 |

**Answer to the question.** P(X = 0) = e^{−2.5} = **0.0821**: about one day in 12 has no demand.

**Changing the interval.** λ belongs to the interval named in the question. A rate of 2 calls per hour gives λ = 2 for one hour and λ = 6 for three hours.

:::check Check 1
Calls arrive at 2 per hour on average (Poisson). Find (a) P(exactly 3 calls in an hour); (b) P(no call in 3 hours).
:::

### 2 · Mean equals variance

The binomial needed two numbers, n and p (04a step 4). The Poisson formula holds only λ.

:::q <span class="tag">MTE A2 · 2 marks</span>
In which distribution is the mean the sole parameter? Normal / Poisson / Binomial / Uniform.
:::

:::guess Guess first
Count the letters each formula needs: normal (μ, σ), binomial (n, p), uniform (a, b), Poisson (?). Write your answer.
:::

:::note Terms
**Parameter:** a number that must be given before the formula gives probabilities. The Poisson's only parameter is λ, and E(X) = λ, **Var(X) = λ** (G&K §7.3).
:::

**Derivation of the mean** (each line from the one before):

1. E(X) = Σ x × e^{−λ}λ^{x}/x!, summed over x = 0, 1, 2, … (03a step 1).
2. The x = 0 term is 0; for x ≥ 1, x/x! = 1/(x − 1)!.
3. Take out one λ: E(X) = λ × Σ e^{−λ}λ^{x−1}/(x − 1)!, x = 1, 2, …
4. The sum is the whole P(λ) PMF again (put y = x − 1), which adds to 1.
5. E(X) = **λ**. The same route on E(X(X − 1)) = λ² gives Var(X) = λ² + λ − λ² = **λ**.

| distribution | mean | variance | mean vs variance |
|---|---|---|---|
| binomial B(10, ½) (04a) | 5 | 2.5 | variance smaller |
| Poisson P(2.5) (desk) | 2.5 | 2.5 | **equal** |

**Answer to the question.** **Poisson**: its one parameter λ is the mean.

<span class="tag">A2 MCQ 3</span> "A unique property of the Poisson distribution": (c) **the mean and the variance are strictly equal**.
<span class="tag">A2 MCQ 7</span> "Best suited to model the number of rare events occurring in a fixed interval of time or space": (c) **Poisson**.

:::check Check 2
A Poisson count has variance 4. Find its mean, its SD, and P(X = 0).
:::

### 3 · Finding λ from a probability

Some questions give a probability instead of the mean. Since everything follows from λ, solve for λ first.

:::q <span class="tag">MTE A4 · 2 marks</span>
If X is a Poisson variate such that P(X = 0) = ½, then Var(X) is: (a) ln 2 (b) 1 (c) 2 (d) ln 3
:::

:::guess Guess first
Put x = 0 in the formula of step 1. What is left?
:::

**Derivation.**

1. P(X = 0) = e^{−λ}λ⁰/0! = e^{−λ}.
2. Set it equal to the given value: e^{−λ} = ½.
3. Take natural logs: −λ = ln ½ = −ln 2, so **λ = ln 2 = 0.6931**.
4. Step 2: Var(X) = λ.

**Answer to the question.** Var(X) = **ln 2** ≈ 0.6931, option (a).

**Two probabilities equal.** If P(X = 1) = P(X = 2): e^{−λ}λ = e^{−λ}λ²/2. Divide by e^{−λ}λ: 1 = λ/2, so **λ = 2**.

:::check Check 3
<span class="tag">G&K Ex. 7.30</span> X is Poisson with P(X = 2) = 9P(X = 4) + 90P(X = 6). Find λ.
:::

### 4 · "At least", "more than", "rejected"

The PMF has no last value, so "more than 3" has infinitely many terms. The complement (01 step 5) turns it into four.

:::q <span class="tag">A2 B1 (ii)</span>
With the same desk (3 technicians, λ = 2.5), find the probability of a day on which a demand is rejected.
:::

:::guess Guess first
Write the event "a demand is rejected" as an inequality in X before computing.
:::

**Terms.** Nothing new. Three technicians serve at most 3 demands, so a demand is rejected when **X > 3**, that is X ≥ 4.

**Derivation.**

1. P(X > 3) = 1 − P(X ≤ 3) (complement, 01 step 5).
2. P(X ≤ 3) = P(0) + P(1) + P(2) + P(3) = 0.0821 + 0.2052 + 0.2565 + 0.2138 = 0.7576 (step 1's table).
3. P(X > 3) = 1 − 0.7576 = **0.2424**.

In the step 1 figure, this is the total of the red bars.

**Answer to the question.** **0.2424**: about one day in four, at least one demand is turned away.

| words in the question | event | compute as |
|---|---|---|
| at least one | X ≥ 1 | 1 − P(0) |
| more than 2 | X ≥ 3 | 1 − [P(0) + P(1) + P(2)] |
| rejected with 3 servers | X ≥ 4 | 1 − [P(0) + … + P(3)] |

:::check Check 4
<span class="tag">A2 C3</span> Suppose the number of emails a researcher receives per day follows a Poisson distribution with a mean of 5. Find the exact probability that they will receive more than 2 emails in a given day.
:::

### 5 · Poisson as a stand-in for the binomial

The Poisson is what the binomial becomes when there are very many trials and each success is rare (04a's formula with large n is heavy to compute).

:::q <span class="tag">A2 D3</span>
One percent of jobs arriving at a computer system need to wait until weekend for scheduling, owing to core-size limitations. Find the probability using Poisson approximation to binomial that among a sample of 200 jobs, there are no jobs that have to wait until weekends.
:::

:::guess Guess first
How many of the 200 jobs wait, on average? Write that number first.
:::

:::note Terms
**Poisson approximation:** if n is large and p is small, with np = λ held fixed, B(n, p) is close to P(λ) (G&K §7.3: the Poisson is the limit of the binomial as n → ∞, p → 0, np = λ finite). Working rule: n ≥ 20 and p ≤ 0.05. **Approximation enters** at the line where B(n, p) is replaced by P(np).
:::

[[fig:pois_limit|What this graph plots: two PMFs side by side for each x. Horizontal axis: x, the number of jobs out of 200 that wait. Vertical axis: P(X = x). Blue bars: the exact binomial B(200, 0.01). Green bars: the Poisson with λ = np = 2. Each pair is nearly the same height.|w=80]]

| x | binomial B(200, 0.01) | Poisson P(2) |
|---|---|---|
| 0 | 0.1340 | 0.1353 |
| 1 | 0.2707 | 0.2707 |
| 2 | 0.2720 | 0.2707 |

**Derivation.**

1. Exactly: X ~ B(200, 0.01), X = jobs that wait.
2. λ = np = 200 × 0.01 = 2.
3. **Approximation:** replace B(200, 0.01) by P(2).
4. P(X = 0) ≈ e^{−2} = **0.1353**.

**Answer to the question.** ≈ **0.1353**. The exact binomial value is 0.99²⁰⁰ = 0.1340: the approximation is off by 0.0013.

:::check Check 5
2% of fuses are defective. In a box of 100, use the Poisson approximation to find P(at most 2 defective).
:::

### 6 · Adding two Poisson counts

Two desks, two Poisson counts. The total is again a count of independent events at a constant rate.

:::q <span class="tag">A2 MCQ 12</span>
If X and Y are independent Poisson random variables with parameters λ₁ and λ₂ respectively, then the distribution of X + Y follows: a) A Binomial distribution with mean λ₁ + λ₂ b) A Poisson distribution with mean λ₁λ₂ c) A Poisson distribution with mean λ₁ + λ₂ d) An Exponential distribution with mean λ₁ + λ₂
:::

:::guess Guess first
The means of a sum add (03b step 2). Which options does that rule out?
:::

:::note Terms
**Additive property** (G&K §7.3): if X ~ P(λ₁) and Y ~ P(λ₂) are independent, then X + Y ~ P(λ₁ + λ₂). The total stays Poisson; its mean is the sum of the means.
:::

**Worked case.** A second desk gets 1.5 demands a day on average, independent of the first (2.5). The total is P(4).

| route | P(no demand at either desk) |
|---|---|
| total is P(4) | e^{−4} = **0.0183** |
| both zero, independent (01 step 10) | e^{−2.5} × e^{−1.5} = 0.0821 × 0.2231 = **0.0183** |

The two routes agree.

**Answer to the question.** (c): **Poisson with mean λ₁ + λ₂**. (b) multiplies the means; (a) and (d) are not counts with no upper limit.

:::check Check 6
Line A gets 3 calls an hour and line B gets 2 calls an hour, independent Poisson counts. Find P(exactly 2 calls in total in an hour).
:::

---

## Exam form

| | Poisson P(λ) |
|---|---|
| Story | number of events in a fixed interval; independent events at a constant average rate |
| PMF | P(X = x) = e^{−λ}λ^{x}/x!, x = 0, 1, 2, … |
| Mean | λ |
| Variance | λ (= mean) |
| Parameter | λ only |
| Recurrence | P(x + 1) = P(x) × λ/(x + 1) |
| Sum | independent P(λ₁) + P(λ₂) = P(λ₁ + λ₂) |
| From binomial | B(n, p) ≈ P(np) when n is large and p small |

**Procedure "more than k" / "rejected"**: write the event as X ≥ k + 1; compute 1 − [P(0) + … + P(k)] with the recurrence.

**Procedure "λ from a probability"**: write the given probability with the PMF; cancel e^{−λ} where both sides have it; solve for λ (logs when only P(0) is given).

**Proof of E(X) = λ** (when asked): step 2's derivation, lines 1–5.

## Traps

- Using the rate for the wrong interval: λ = 2 per hour means λ = 6 for 3 hours.
- "More than 3" computed as 1 − P(X ≤ 2): that is "at least 3".
- Adding P(0) … P(3) and forgetting the complement: that is P(X ≤ 3), not P(X > 3).
- Using the Poisson approximation with p not small (p = 0.3): the binomial and Poisson differ.
- Multiplying the λs for a sum of Poissons: they add.

## Self-test

1. Write the Poisson PMF and say what λ counts.
2. A Poisson variate has P(X = 1) = P(X = 2). Find P(X = 0).
3. Accidents average 3 per week. Find P(no accident in a week) and P(no accident in 2 weeks).
4. Show in one line of algebra that the Poisson mean is λ.
5. 5% of items are defective. In a sample of 40, find P(exactly 1 defective) by the Poisson approximation.
6. Defects average 1.2 per metre of cable. Find P(at least one defect in a metre).
7. X ~ P(1) and Y ~ P(2) are independent. Find the mean and variance of X + Y.

<!--ANSWERS-->
## Answers

**Check 1.** (a) λ = 2: e^{−2}2³/3! = 0.1353 × 8/6 = **0.1804**. (b) λ = 6 for 3 hours: e^{−6} = **0.0025**.

**Check 2.** Mean = variance = **4**; SD = **2**; P(X = 0) = e^{−4} = **0.0183**.

**Check 3.** e^{−λ}λ²/2 = 9e^{−λ}λ⁴/24 + 90e^{−λ}λ⁶/720. Multiply by 8/(e^{−λ}λ²): 4 = 3λ² + λ⁴, so λ⁴ + 3λ² − 4 = 0, (λ² + 4)(λ² − 1) = 0, **λ = 1**.

**Check 4.** λ = 5: P(0) + P(1) + P(2) = e^{−5}(1 + 5 + 12.5) = 18.5 × 0.006738 = 0.1247; 1 − 0.1247 = **0.8753**. (The assignment's key prints 0.8754: a rounding difference in the last digit.)

**Check 5.** λ = 100 × 0.02 = 2: e^{−2}(1 + 2 + 2) = 5e^{−2} = **0.6767**.

**Check 6.** Total ~ P(5): e^{−5}5²/2! = 0.006738 × 12.5 = **0.0842**.

**Self-test.**

1. P(X = x) = e^{−λ}λ^{x}/x!; λ = the average number of events in the stated interval.
2. λ = 2 (step 3); P(0) = e^{−2} = **0.1353**.
3. e^{−3} = **0.0498**; λ = 6 for 2 weeks: e^{−6} = **0.0025**.
4. E(X) = Σ x e^{−λ}λ^{x}/x! = λ Σ e^{−λ}λ^{x−1}/(x − 1)! = λ × 1.
5. λ = 40 × 0.05 = 2: P(1) = 2e^{−2} = **0.2707**.
6. 1 − e^{−1.2} = 1 − 0.3012 = **0.6988**.
7. X + Y ~ P(3): mean **3**, variance **3**.
<!--/ANSWERS-->
