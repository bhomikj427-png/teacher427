# 02a — Discrete random variables: PMF and CDF

<div class="sub">Gupta & Kapoor ch. 5 (§5.1–5.3) · blueprint row 1 "discrete and continuous random variables; PMF; CDF" · 9 real questions (MTE A1; Assignment 1 MCQ 1–3, SA 1, LA 2, LA 4, App 2) · needs 01 (sample space step 1, events step 2, conditional probability step 7)</div>

## Map

[[map:1 Outcome → number > 2 Discrete or continuous > 3 PMF by counting > 4 The two PMF rules > 5 Finding k > 6 Counting with combinations > 7 The CDF staircase > 8 Reading probabilities off F > 9 Conditional with a PMF|here=1]]

01 gave every event a probability, but events are words ("sum is 7"). This file turns outcomes into **numbers**, so a whole experiment becomes one table: each value and its probability (the PMF), and its running total (the CDF). 02b does the same for measured quantities, where the table becomes a curve. 03a uses the table to find an average.

| Symbol | What it means in this file | Typical value |
|---|---|---|
| X | a random variable: the rule that gives each outcome a number. Here, the number of boys in a family of 3 | X(BGB) = 2 |
| x | one particular value X can take | x = 0, 1, 2, 3 |
| p(x) | the PMF: the probability that X equals x, P(X = x) | p(2) = 3/8 |
| k | an unknown constant inside a PMF, set by "all probabilities add to 1" | k = 1/10 (LA 2) |
| C(n, r) | how many ways to choose r items from n, order ignored | C(20, 2) = 190 |
| F(x) | the CDF: the probability that X is at most x, P(X ≤ x) | F(1) = 4/8 |

**Running example.** A family has 3 children; each is a boy or a girl with chance ½, independently (A1 SA 1). There are 8 equally likely families. X = number of boys. Every figure and most Checks use it.

## The questions this file answers

- <span class="tag">MTE A1 · 2 marks</span> Which one of the following statements is not correct? (b) The number of calls received during a definite time-period is a continuous random variable. (c) The number of kings drawn from a pack of cards is a discrete random variable. (d) The life of an electric bulb is an example of a continuous random variable. *(Option (a), on independence, is in 03b.)*
- <span class="tag">A1 MCQ 1</span> Which of the following is a discrete random variable? Height of students / time taken to complete an exam / number of defective bulbs in a box / temperature of a city.
- <span class="tag">A1 MCQ 2</span> The cumulative distribution function (CDF) of a random variable is: P(X = x) / P(X ≤ x) / P(X ≥ x) / P(X > x).
- <span class="tag">A1 MCQ 3</span> Which of the following is true about a PMF? It can take negative values / its sum over all values equals 1 / it is decreasing / it is defined only for continuous variables.
- <span class="tag">A1 SA 1</span> Find the probability distribution of boys and girls in families with 3 children, assuming equal probabilities of boys and girls. Also give the distribution function.
- <span class="tag">A1 LA 4</span> Four bad oranges are mixed accidentally with 16 good oranges. Find the probability distribution of the number of bad oranges in a draw of two oranges.
- <span class="tag">A1 LA 2</span> X takes 0, 1, …, 7 with probabilities in terms of k. (i) Find k. (ii) Evaluate P(X > 6), P(X ≥ 6), P(0 < X < 5). (iii) Determine the distribution function. (iv) If P(X ≤ c) > ½, find the minimum value of c. (v) Find P(1.5 < X < 4.5 | X > 2).
- <span class="tag">A1 App 2</span> Customer calls per hour X = 0, 1, 2, 3 with P(X) = 0.15, 0.35, 0.30, 0.20. Find the CDF, P(X ≤ 2) and P(X > 1).

---

## Build

### 1 · A random variable turns each outcome into a number

01 described outcomes in words and letters. Arithmetic needs numbers.

:::q Predict
List the 8 families of 3 children (BBB, BBG, …). Next to each, write how many boys it has. Which numbers appear, and how often?
:::

:::guess Guess first
Make the list on paper before reading on.
:::

:::note Terms
**Random variable X:** a rule that gives **one number to each outcome** of S. Here the rule is "count the boys". It is random because the outcome is; the rule itself is fixed. **x:** one value X can take.
:::

[[fig:family_map|Left: the 8 equally likely families (B = boy, G = girl, oldest first). Each arrow is the rule X = "count the boys". Right: the four values X can take, with how many families land on each.|w=70]]

- Several outcomes can land on the same number: BGG, GBG and GGB all give X = 1.
- Every outcome lands on exactly one number. No outcome is left without a value.
- The **event** "X = 1" (01 step 2) is the group of outcomes the rule sends to 1: {BGG, GBG, GGB}.

**Answer to the Predict.** X = 0 (1 family), 1 (3 families), 2 (3 families), 3 (1 family). The values are **0, 1, 2, 3**.

:::check Check 1
Same families. Let Y = number of girls. (a) What is Y(BGG)? (b) Which outcomes form the event Y = 2?
:::

### 2 · Discrete or continuous: can the values be listed?

X takes 0, 1, 2, 3: values you can list. Not every random variable is like that.

:::q <span class="tag">MTE A1 · 2 marks</span>
Which one of the following statements is **not** correct? (b) The number of calls received during a definite time-period is a continuous random variable. (c) The number of kings drawn from a pack of cards is a discrete random variable. (d) The life of an electric bulb is an example of a continuous random variable.
:::

:::guess Guess first
For each of (b), (c), (d): can you list the possible values one by one (0, 1, 2, …)? Write "list" or "interval" next to each.
:::

:::note Terms
**Discrete random variable:** its values can be listed: separate points such as 0, 1, 2, … **Counts** are discrete. **Continuous random variable:** it can take **any** value in an interval, such as 1203.7 hours. **Measurements** (time, length, weight, temperature) are continuous.
:::

| Quantity | Values | Type |
|---|---|---|
| boys in 3 children | 0, 1, 2, 3 | discrete |
| calls in one hour | 0, 1, 2, … | discrete |
| kings drawn from a pack | 0, 1, 2, 3, 4 | discrete |
| life of a bulb | any time ≥ 0 | continuous |

**Answer.** Calls are **counted**, so the number of calls is discrete even though the calls arrive in time. Statement **(b)** is the incorrect one. (c) and (d) are correct.

:::check Check 2
<span class="tag">A1 MCQ 1</span> Which is a discrete random variable: height of students / time taken to complete an exam / number of defective bulbs in a box / temperature of a city?
:::

### 3 · The PMF: a probability for each value, built by counting

A discrete X has a list of values. The next job is a probability for each one.

:::q <span class="tag">A1 SA 1</span>
Find the probability distribution of boys and girls in families with 3 children, assuming equal probabilities of boys and girls. Also give the distribution function.
:::

:::guess Guess first
From step 1's list: what is P(X = 2)? Write it as a fraction.
:::

:::note Terms
**PMF (probability mass function) p(x):** the probability that X takes the value x, p(x) = P(X = x). "Probability distribution" in a question means this table.
:::

**Method** (01 step 3, count and divide):

1. List the outcomes (8 families, each 1/8).
2. Give each outcome its value of X (step 1).
3. Add the probabilities of the outcomes that share a value.

| x (boys) | families | p(x) |
|---|---|---|
| 0 | GGG | 1/8 |
| 1 | BGG, GBG, GGB | 3/8 |
| 2 | BBG, BGB, GBB | 3/8 |
| 3 | BBB | 1/8 |

[[fig:boys_pmf|What this graph plots: the PMF of X. Horizontal axis: the number of boys x. Bar height: p(x), the probability of exactly that many boys. The bar at x = 2 means "3 of the 8 families have exactly 2 boys".|w=58]]

**Answer.** p(0) = **1/8**, p(1) = **3/8**, p(2) = **3/8**, p(3) = **1/8**. The number of girls is 3 − X, so its PMF is the same table read backwards. The distribution function is step 7.

:::check Check 3
(a) Two fair coins are tossed; X = number of heads. Write the PMF. (b) Two dice are thrown; X = the larger of the two numbers. Find p(1) and p(6).
:::

### 4 · The two rules every PMF obeys

Any proposed table can be tested. 01's axioms give the test.

:::q <span class="tag">A1 MCQ 3</span>
Which of the following is true about a PMF? (a) It can take negative values. (b) Its sum over all values equals 1. (c) It is decreasing. (d) It is defined only for continuous variables.
:::

:::guess Guess first
Add the four values of step 3's table. Then pick the option.
:::

1. **p(x) ≥ 0 for every x.** Each p(x) is a probability (axiom 1, 01 step 4).
2. **Σ p(x) = 1, adding over every value of X.** The events X = 0, X = 1, … share no outcome and together cover S (axioms 2 and 3).

$$p(x) ≥ 0    and    Σ p(x) = 1$$

Read it as: **no negative bars, and the bars together make the whole.** Step 3's table: 1/8 + 3/8 + 3/8 + 1/8 = 8/8 = 1 ✓.

**Answer.** Option **(b)**. (a) breaks rule 1. (c) fails: the boys' PMF rises then falls. (d) is backwards: a PMF belongs to a **discrete** X.

:::check Check 4
Is each table a valid PMF? Give the rule it breaks if not. (a) p = 0.3, 0.5, 0.3 (b) p = 0.5, −0.1, 0.6 (c) p = 0.25, 0.40, 0.25, 0.10
:::

### 5 · Finding an unknown k from Σ p(x) = 1

Rule 2 is also an equation. When a table holds an unknown, it finds it.

:::q <span class="tag">A1 LA 2 (i)</span>
X takes 0, 1, …, 7 with probabilities 0, k, 2k, 2k, 3k, k², 2k², 7k² + k. Find k. *(Row as in Gupta & Kapoor; the assignment prints a different row: note below.)*
:::

:::guess Guess first
Add the eight entries and set the sum to 1. What equation in k do you get?
:::

1. Σ p(x) = 0 + k + 2k + 2k + 3k + k² + 2k² + 7k² + k = 10k² + 9k.
2. Rule 2: 10k² + 9k = 1, so 10k² + 9k − 1 = 0.
3. Factor: (10k − 1)(k + 1) = 0, so k = 1/10 or k = −1.
4. Rule 1: k = −1 would make p(1) = k negative. Reject it.

**Answer.** **k = 1/10.** The table is then 0, 0.1, 0.2, 0.2, 0.3, 0.01, 0.02, 0.17 (sum 1 ✓).

:::note The assignment's table is not the textbook's
Assignment 1 prints the row as **k, 2k, 2k, 3k, 3k**, k², 2k², 7k² + k. That sums to 10k² + 12k = 1, giving k = (−6 + √46)/10 ≈ 0.0782, and none of the key's answers follow. The key's answers (k = 1/10, F = 0, 1/10, 3/10, …) belong to the Gupta & Kapoor table **0, k, 2k, 2k, 3k**, k², 2k², 7k² + k (G&K ch. 5, worked example on the distribution function), which this pack uses.
:::

:::check Check 5
(a) X = 1, 2, 3, 4 with P(X = x) = cx. Find c. (b) X = 0, 1, 2 with p = k, 2k, k². Find k.
:::

### 6 · Counting with combinations: draws without replacement

The 3-children list was short. Drawing 2 oranges from 20 has too many outcomes to list, so count them instead.

:::q <span class="tag">A1 LA 4</span>
Four bad oranges are mixed accidentally with 16 good oranges. Find the probability distribution of the number of bad oranges in a draw of two oranges.
:::

:::guess Guess first
What values can X = number of bad oranges take? Which do you expect to be most likely?
:::

:::note Terms
**C(n, r)** ("n choose r"): the number of ways to pick r items from n when order does not matter. C(n, 2) = n(n − 1)/2: pick one of n, then one of the n − 1 left, and halve because each pair was counted in both orders.
:::

1. All equally likely draws: C(20, 2) = 20 × 19/2 = **190**.
2. X = 0: both from the 16 good: C(16, 2) = 16 × 15/2 = 120.
3. X = 1: one of 4 bad and one of 16 good: 4 × 16 = 64.
4. X = 2: both from the 4 bad: C(4, 2) = 6.
5. Count and divide (01 step 3), then check rule 2: 120 + 64 + 6 = 190 ✓.

| x (bad oranges) | 0 | 1 | 2 |
|---|---|---|---|
| ways | 120 | 64 | 6 |
| p(x) | 120/190 = **12/19** | 64/190 = **32/95** | 6/190 = **3/95** |

**Answer.** p(0) = 12/19, p(1) = 32/95, p(2) = 3/95. X = 0 is the most likely: 16 of the 20 oranges are good.

:::check Check 6
A box has 3 defective and 7 good items; 2 are drawn without replacement. Find the PMF of X = number of defectives.
:::

### 7 · The CDF: a running total that climbs like a staircase

The PMF answers "exactly x". Most questions say "at most", "at least" or "more than": a running total.

:::q <span class="tag">A1 MCQ 2</span>
The cumulative distribution function (CDF) of a random variable is: (a) P(X = x) (b) P(X ≤ x) (c) P(X ≥ x) (d) P(X > x)
:::

:::guess Guess first
"Cumulative" means "running total". A running total of which probabilities? Pick the option.
:::

:::note Terms
**CDF (cumulative distribution function, or distribution function) F(x):** the probability that X is **at most** x, F(x) = P(X ≤ x). It is defined for every real x, not only the values X takes.
:::

For a discrete X, add the PMF from the left up to x:

$$F(x) = P(X ≤ x) = Σ_{t ≤ x} p(t)$$

[[fig:boys_cdf|What this graph plots: F(x), the chance of at most x boys, for every x on the horizontal axis. Between the values of X it stays flat; at each value it jumps up by p(x). Filled dot = the value F takes at the jump.|w=60]]

**Reading the figure.**

| x | −1 | 0 | 1 | 1.5 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|---|
| F(x) | 0 | 1/8 | 4/8 | 4/8 | 7/8 | 1 | 1 |
| why | no value ≤ −1 | p(0) | 1/8 + 3/8 | no new value in (1, 1.5] | + 3/8 | + 1/8 | everything |

- F never goes down; it starts at 0 far left and ends at 1 far right.
- Each jump's height is a bar of the PMF.

**Answer.** Option **(b)**. For A1 SA 1, the distribution function at x = 0, 1, 2, 3 is **1/8, 4/8, 7/8, 1**.

:::check Check 7
(a) For the two-coin X of Check 3(a), write F(0), F(1), F(2). (b) For the boys' X, find F(2.7) and F(−0.5).
:::

### 8 · Reading probabilities off F: "at most", "more than", "between"

F is a running total. Every interval question is a difference of two totals.

:::q <span class="tag">A1 App 2</span>
Customer calls per hour X = 0, 1, 2, 3 with P(X) = 0.15, 0.35, 0.30, 0.20. Find (1) the CDF, (2) P(X ≤ 2), (3) P(X > 1).
:::

:::guess Guess first
Write the four running totals first.
:::

| Asked | Use | Why |
|---|---|---|
| P(X ≤ a) | F(a) | the definition |
| P(X > a) | 1 − F(a) | complement of "≤ a" (01 step 5) |
| P(a < X ≤ b) | F(b) − F(a) | up to b, minus up to a |
| P(X < a), X whole numbers | F(a − 1) | "< 2" means "≤ 1" |

For a discrete X, **< and ≤ differ**: P(X < 2) leaves out p(2); P(X ≤ 2) keeps it.

**Answer.** (1) F(0) = **0.15**, F(1) = 0.15 + 0.35 = **0.50**, F(2) = 0.50 + 0.30 = **0.80**, F(3) = **1.00**. (2) P(X ≤ 2) = F(2) = **0.80**. (3) P(X > 1) = 1 − F(1) = **0.50**: half of all hours bring 2 or more calls, which is how many staff are planned.

:::q <span class="tag">A1 LA 2 (ii)–(iv)</span>
With k = 1/10 (step 5): (ii) evaluate P(X > 6), P(X ≥ 6), P(0 < X < 5); (iii) determine the distribution function; (iv) if P(X ≤ c) > ½, find the minimum value of c.
:::

| x | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| p(x) | 0 | 0.1 | 0.2 | 0.2 | 0.3 | 0.01 | 0.02 | 0.17 |
| F(x) | 0 | 1/10 | 3/10 | 5/10 | 8/10 | 81/100 | 83/100 | 1 |

**Answer.**

- (ii) P(X > 6) = 1 − F(6) = **0.17**. P(X ≥ 6) = 1 − F(5) = **0.19**. P(0 < X < 5) = F(4) − F(0) = **0.8 = 4/5**.
- (iii) The F row of the table.
- (iv) F(3) = 0.5 is **not** greater than ½; F(4) = 0.8 is. Minimum **c = 4**.

:::note The key answers a different question
The key prints (ii) as 81/100, 91/100, 4/5. Gupta & Kapoor's version of this question asks P(X **<** 6), P(X ≥ 6), P(0 < X < 5), with answers 81/100, 19/100, 4/5. So the key's 81/100 is P(X < 6), and 91/100 is 19/100 with its digits swapped. For the question as printed the answers are **17/100, 19/100, 4/5**.
:::

:::check Check 8
From the calls table: (a) P(1 ≤ X ≤ 2) using F only. (b) P(X < 2).
:::

### 9 · Conditional probability with a PMF

01 step 7's rule, P(A | B) = P(A∩B)/P(B), works unchanged; the events are now ranges of X.

:::q <span class="tag">A1 LA 2 (v)</span>
Find P(1.5 < X < 4.5 | X > 2).
:::

:::guess Guess first
Which whole numbers lie in 1.5 < X < 4.5? Which of them are also > 2?
:::

1. A = {1.5 < X < 4.5} = {X = 2, 3, 4}. B = {X > 2} = {X = 3, 4, 5, 6, 7}.
2. A∩B = {X = 3, 4}: P(A∩B) = 0.2 + 0.3 = 0.5.
3. P(B) = 1 − F(2) = 1 − 0.3 = 0.7.
4. P(A | B) = 0.5/0.7.

**Answer.** P(1.5 < X < 4.5 | X > 2) = **5/7** ≈ 0.714.

:::check Check 9
Boys' X: find P(X = 3 | X ≥ 2).
:::

---

## Exam form

**Definitions (one line each).** Random variable: a rule giving a number to each outcome · discrete: values can be listed (counts) · continuous: any value in an interval (measurements) · PMF p(x) = P(X = x) · CDF F(x) = P(X ≤ x).

**PMF rules.** p(x) ≥ 0 for every x; Σ p(x) = 1.

**CDF properties.** 0 ≤ F(x) ≤ 1; F never decreases; F(−∞) = 0, F(∞) = 1; for a discrete X, F is a staircase that jumps by p(x) at each value x.

**Probabilities from F.** P(X ≤ a) = F(a); P(X > a) = 1 − F(a); P(a < X ≤ b) = F(b) − F(a).

**Procedure: build a PMF.**

1. List the outcomes (or count them with C(n, r)).
2. Give each outcome its value of X.
3. Add probabilities of outcomes with the same value.
4. Check Σ p(x) = 1.

**Procedure: find a constant k.** Set Σ p(x) = 1, solve, reject any root that makes a p(x) negative.

## Traps

- Calling a **count** of calls or arrivals continuous: counts are discrete even when they happen in time.
- For a discrete X, P(X < 2) = F(1), not F(2).
- Forgetting to reject the root of k that makes a probability negative.
- "Minimum c with F(c) > ½": F(c) = ½ exactly does **not** qualify.
- Building a PMF and not checking that it adds to 1.
- In a conditional, dividing by 1 instead of by P(given event).

## Self-test

1. Define random variable, PMF and CDF in one line each.
2. A family has 4 children (each a boy with chance ½). Find P(exactly 2 boys).
3. A box has 2 defective and 3 good items; 2 are drawn without replacement. Find the PMF of the number of defectives.
4. p(x) = kx² for x = 1, 2, 3. Find k and F(2).
5. For A1 LA 2 (k = 1/10), find P(2 ≤ X ≤ 4) and P(X ≥ 5).
6. A fair die is thrown; X = the number shown. Find F(3.5) and P(X > 4).
7. For the boys' X, find P(1 ≤ X ≤ 2) using F only.

<!--ANSWERS-->
## Answers

**Check 1.** (a) Y(BGG) = **2**. (b) Y = 2: {BGG, GBG, GGB}.

**Check 2.** **Number of defective bulbs in a box**: a count. The other three are measurements.

**Check 3.** (a) p(0) = **1/4**, p(1) = **1/2**, p(2) = **1/4** (HH, HT, TH, TT). (b) p(1) = **1/36**: only (1, 1). p(6) = 1 − 25/36 = **11/36**: at least one six (01 step 5).

**Check 4.** (a) **No**: sum 1.1 (rule 2). (b) **No**: −0.1 < 0 (rule 1). (c) **Yes**: all ≥ 0, sum 1.

**Check 5.** (a) c(1 + 2 + 3 + 4) = 10c = 1, **c = 1/10**. (b) k² + 3k − 1 = 0, k = (−3 + √13)/2 = **0.3028** (the other root is negative).

**Check 6.** C(10, 2) = 45. p(0) = C(7, 2)/45 = 21/45 = **7/15**; p(1) = 3 × 7/45 = 21/45 = **7/15**; p(2) = C(3, 2)/45 = 3/45 = **1/15**. Sum 1 ✓.

**Check 7.** (a) F(0) = **1/4**, F(1) = **3/4**, F(2) = **1**. (b) F(2.7) = F(2) = **7/8**; F(−0.5) = **0**.

**Check 8.** (a) F(2) − F(0) = 0.80 − 0.15 = **0.65**. (b) P(X < 2) = F(1) = **0.50**.

**Check 9.** P(X = 3 | X ≥ 2) = (1/8)/(3/8 + 1/8) = **1/4**.

**Self-test.**

1. Random variable: a rule giving a number to each outcome. PMF: p(x) = P(X = x), for a discrete X. CDF: F(x) = P(X ≤ x).
2. 16 equally likely families; C(4, 2) = 6 have 2 boys. P = **6/16 = 3/8**.
3. C(5, 2) = 10. p(0) = C(3, 2)/10 = **3/10**; p(1) = 2 × 3/10 = **6/10**; p(2) = 1/10 = **1/10**.
4. k(1 + 4 + 9) = 14k = 1, **k = 1/14**. F(2) = (1 + 4)/14 = **5/14**.
5. P(2 ≤ X ≤ 4) = 0.2 + 0.2 + 0.3 = **0.7**. P(X ≥ 5) = 0.01 + 0.02 + 0.17 = **0.2**.
6. F(3.5) = P(X ≤ 3) = **1/2**. P(X > 4) = 2/6 = **1/3**.
7. F(2) − F(0) = 7/8 − 1/8 = **6/8 = 3/4**.
<!--/ANSWERS-->
