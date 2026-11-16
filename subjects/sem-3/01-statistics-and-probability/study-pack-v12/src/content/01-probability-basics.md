# 01 — Probability: outcomes, events and the rules that combine them

<div class="sub">Gupta & Kapoor ch. 4 (§4.3, 4.6–4.8) · blueprint row 1 "basic terminology and concepts of probability theory" · 4 real questions (Assignment 1 MCQ 6–9); other openers are Predict prompts · needs nothing earlier: this is the start</div>

## Map

[[map:1 Outcomes and S > 2 Events > 3 Count and divide > 4 The three axioms > 5 Complement > 6 Addition rule > 7 Conditional: a smaller S > 8 P(A | B) = 1 > 9 Multiplication rule > 10 Independence > 11 Total probability > 12 Bayes' theorem|here=1]]

This is the first file. It builds the language every later file speaks: an experiment, its list of outcomes, events, and the rules that turn them into numbers between 0 and 1. All of it is shown on one picture, the 36 results of throwing two dice. 02a uses the same language to define a **random variable**; 10 (Bayesian estimation) is built on step 12.

| Symbol | What it means in this file | Typical value |
|---|---|---|
| S | the sample space: the list of every outcome the experiment can give | 36 cells for two dice |
| n | how many equally likely outcomes S holds | n = 36 |
| A, B, C | events: groups of outcomes. Here A = "sum is 7", B = "first die is 6", C = "sum is at least 10" | A has 6 cells |
| m | how many outcomes of S belong to the event | m = 6 for A |
| P(A) | the probability of A: a number from 0 to 1 | P(A) = 6/36 = 1/6 |
| Aᶜ | "not A": every outcome of S outside A | 30 cells |
| A∪B | "A or B (or both)": outcomes in at least one of the two | 11 cells |
| A∩B | "A and B": outcomes in both | 1 cell, (6, 1) |
| ∅ | the empty event: no outcomes at all | — |
| P(A \| B) | probability of A once we know B happened | P(C \| B) = 1/2 |
| M₁, M₂, D | step 11–12 factory: machine 1, machine 2, "bolt is defective" | P(D) = 0.032 |

**Running example.** Two fair dice, thrown once: a red one ("first die") and a blue one ("second die"). Every step reads its rule off the same 6 × 6 grid. Steps 9, 11 and 12 add one card-drawing and one factory example, where a tree shows the rule better than a grid.

## The questions this file answers

- <span class="tag">A1 MCQ 7</span> A box contains 4 red and 6 blue balls. One ball is selected randomly. The probability of selecting a red ball is: 0.2 / 0.4 / 0.6 / 0.8.
- <span class="tag">A1 MCQ 9</span> A card is drawn from a standard deck of 52 cards. The probability of drawing an Ace is: 1/13 / 1/4 / 4/13 / 1/52.
- <span class="tag">A1 MCQ 6</span> The conditional probability of A given B is defined as: P(B)/P(A) / P(A∩B)/P(B) / P(A) + P(B) / P(A∩B)/P(A).
- <span class="tag">A1 MCQ 8</span> If P(A | B) = 1, then: A is impossible whenever B occurs / A always occurs whenever B occurs / A and B are mutually exclusive / none of these.

The ETE blueprint gives row 1 (probability and random variables) 10 of 80 marks; files 01–03 share it.

---

## Build

### 1 · Outcomes and the sample space S

:::q Predict
You throw a red die and a blue die. How many different results can you see, if "red 2, blue 5" counts as different from "red 5, blue 2"?
:::

:::guess Guess first
Write a number on paper before reading on.
:::

:::note Terms
**Random experiment:** an action whose result is not known in advance but whose possible results are (throwing the two dice). **Outcome:** one possible result, written as a pair (red, blue), e.g. (2, 5). **Sample space S:** the full list of outcomes; n counts how many there are.
:::

[[fig:dice_space|The sample space of two dice. Each cell is one outcome: row = what the first (red) die shows, column = what the second (blue) die shows. The cell "2,5" is red 2, blue 5.|w=58]]

- The red die has 6 faces; for **each** of them the blue die has 6. So the grid has 6 rows × 6 columns.
- Every cell is equally likely when the dice are fair: no face is favoured, so no pair is.
- (2, 5) and (5, 2) are different cells: the dice are different colours.

**Answer to the Predict.** 6 × 6 = **36** outcomes. n = 36.

:::check Check 1
(a) A coin is tossed twice. Write S and give n. (b) A coin is tossed and a die is thrown. What is n?
:::

### 2 · Events: groups of outcomes

S lists the outcomes. Most questions ask about a **group** of them ("the sum is 7"), not one cell.

:::q Predict
On the grid, which cells give "sum is 7"? Which give "first die is 6"? Is any cell in both groups?
:::

:::guess Guess first
Mark the cells on the grid from step 1 before reading on.
:::

:::note Terms
**Event:** a group of outcomes, named by a capital letter. A = "sum is 7". **A∩B** ("A and B"): the cells in both groups. **A∪B** ("A or B"): the cells in at least one group.
:::

[[fig:dice_events|Two events on the dice grid. Blue: A = "sum is 7", the 6 cells on the diagonal from 1,6 to 6,1. Orange: B = "first die is 6", the bottom row. Purple: A∩B, the one cell in both.|w=78]]

- A = {(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)}: 6 cells.
- B = {(6,1), (6,2), …, (6,6)}: 6 cells.
- A∩B = {(6,1)}: 1 cell. A∪B = 6 + 6 − 1 = 11 cells (the shared cell is counted once).
- Two events with **no** shared cell, A∩B = ∅, are called **mutually exclusive**: they cannot both happen. "Sum is 2" and "sum is 12" are mutually exclusive.

**Answer to the Predict.** A is the diagonal, B is the bottom row, and they share exactly one cell, **(6, 1)**.

:::check Check 2
(a) List the cells of C = "sum is at least 10". How many are there? (b) Are C and A mutually exclusive?
:::

### 3 · Classical probability: count and divide

Events are groups of cells. A probability turns a group into a number.

:::q <span class="tag">A1 MCQ 7</span>
A box contains 4 red and 6 blue balls. One ball is selected randomly. The probability of selecting a red ball is: (a) 0.2 (b) 0.4 (c) 0.6 (d) 0.8
:::

:::guess Guess first
Pick an option and write one line saying why.
:::

:::note Terms
**Equally likely:** no outcome is favoured over another; "selected randomly", "fair", "unbiased" all say this. **Favourable outcomes m:** how many outcomes of S belong to the event.
:::

When all n outcomes are equally likely (G&K §4.3):

$$P(A) = \frac{m}{n} = \frac{favourable outcomes}{all outcomes}$$

Read it as: **the share of the grid the event covers.** On the dice grid, P(A) = P(sum is 7) = 6/36 = **1/6**; P(B) = 6/36 = **1/6**.

**Answer.** n = 4 + 6 = 10 balls (each equally likely), m = 4 red. P(red) = 4/10 = **0.4**, option **(b)**.

:::q <span class="tag">A1 MCQ 9</span>
A card is drawn from a standard deck of 52 cards. The probability of drawing an Ace is: (a) 1/13 (b) 1/4 (c) 4/13 (d) 1/52
:::

**Answer.** n = 52 cards, m = 4 aces. P = 4/52 = **1/13**, option **(a)**.

:::check Check 3
(a) Two dice: find P(C), C = "sum is at least 10". (b) A bag has 3 white, 5 black and 2 green balls; one is drawn at random. Find P(green).
:::

### 4 · The three axioms: rules every probability obeys

Counting works only when outcomes are equally likely. The rules below hold for **every** probability, counted or not.

:::q Predict
Could a probability ever be −0.2? Or 1.3? What must P(sum = 2) + P(sum = 3) + … + P(sum = 12) equal?
:::

:::guess Guess first
Answer all three on paper.
:::

:::note Terms
**Axiom:** a rule taken as the starting point, not proved. Every other rule in this file is derived from these three.
:::

1. **P(A) ≥ 0** for every event A. (A share of the grid is never negative.)
2. **P(S) = 1.** (Something in S always happens: the whole grid is 36/36.)
3. **If A∩B = ∅, then P(A∪B) = P(A) + P(B).** (Mutually exclusive events: no cell is counted twice, so the shares add.)

From 1 and 2 with step 5's rule: **0 ≤ P(A) ≤ 1**. P = 0: impossible (sum is 13). P = 1: certain (sum is at most 12).

**Answer to the Predict.** No and no: every probability lies between 0 and 1. The eleven sums 2, …, 12 are mutually exclusive and together cover S, so their probabilities add to **P(S) = 1**.

:::check Check 4
P(sum = 2) = 1/36 and P(sum = 12) = 1/36. Find P(sum is 2 or 12), and name the axiom you used.
:::

### 5 · The complement: "not A"

Axioms 2 and 3 give a shortcut for "at least one" questions.

:::q Predict
Two dice: find P(at least one six). Counting the cells that hold a six is one way. Is counting the cells with **no** six easier?
:::

:::guess Guess first
Write your answer as a fraction of 36.
:::

:::note Terms
**Complement Aᶜ:** every outcome of S that is **not** in A. A and Aᶜ never share a cell and together fill S.
:::

[[fig:dice_complement|Orange: the 11 cells with at least one six (bottom row and right column, which share 6,6). White: the 25 cells with no six, a 5 × 5 block.|w=78]]

A and Aᶜ are mutually exclusive and A∪Aᶜ = S. Axiom 3 then axiom 2:

1. P(A) + P(Aᶜ) = P(A∪Aᶜ) = P(S) = 1
2. so **P(Aᶜ) = 1 − P(A)**

Read it as: the share **outside** the event = whole grid minus the share inside. The usual use: **P(at least one) = 1 − P(none)**.

**Answer to the Predict.** No six: 5 × 5 = 25 cells. P(at least one six) = 1 − 25/36 = **11/36**. (Counting directly: 6 + 6 − 1 = 11 cells, the same.)

:::check Check 5
(a) Two dice: find P(sum is not 7). (b) A coin is tossed 3 times. Find P(at least one head) using the complement.
:::

### 6 · The addition rule: "A or B"

Axiom 3 adds probabilities only when events share nothing. A and B of step 2 share one cell.

:::q Predict
P(A) = 6/36 and P(B) = 6/36. Is P(A∪B) = 12/36? Check against the 11 cells counted in step 2.
:::

:::guess Guess first
Write which number is right and why the other is off.
:::

[[fig:venn_union|Venn diagram: the rectangle is S, each circle an event. A∪B is everything inside either circle. A∩B, the overlap, lies inside both.|w=62]]

P(A) counts the overlap once, P(B) counts it again. Subtract it once (G&K §4.6):

$$P(A ∪ B) = P(A) + P(B) − P(A ∩ B)$$

Read it as: **cells in A, plus cells in B, minus the cells counted twice.** For mutually exclusive events P(A∩B) = 0 and this is axiom 3.

**Answer to the Predict.** 12/36 counts (6, 1) twice. P(A∪B) = 6/36 + 6/36 − 1/36 = **11/36**, the 11 cells of step 2.

:::check Check 6
(a) One card from 52: find P(Ace or Heart). (b) P(A) = 0.5, P(B) = 0.3, P(A∩B) = 0.1. Find P(A∪B) and P(neither A nor B).
:::

### 7 · Conditional probability: the sample space shrinks

So far nothing was known about the throw. Now a friend looks and says: "the first die is a 6."

:::q <span class="tag">A1 MCQ 6</span>
The conditional probability of A given B is defined as: (a) P(B)/P(A) (b) P(A∩B)/P(B) (c) P(A) + P(B) (d) P(A∩B)/P(A)
:::

:::guess Guess first
First: knowing the first die is 6, what is the chance the sum is at least 10? Then pick the formula that gives the same number.
:::

:::note Terms
**P(C | B)**, read "probability of C given B": the probability of C when we already know B happened. B is the **given** event.
:::

[[fig:dice_shrunk|Knowing B ("first die is 6") rules out the top five rows (faded). The new sample space is B's 6 cells (orange frame). C = "sum ≥ 10" survives only in its cells inside B: 6,4, 6,5 and 6,6.|w=78]]

- Before the news: C has 6 cells of 36, P(C) = 1/6.
- After it: only B's 6 cells remain. C's cells inside B: (6,4), (6,5), (6,6) = C∩B, 3 cells.
- So P(C | B) = 3/6 = **1/2**. The news tripled the chance.

Divide the counts by 36 and the same share is written with probabilities (G&K §4.7):

$$P(C | B) = \frac{P(C ∩ B)}{P(B)},   P(B) > 0$$

Read it as: **of B's share, the part that is also C.**

**Answer.** Option **(b)**: P(A∩B)/P(B). Option (d) divides by P(A): that is P(B | A), the condition the other way round. Check: P(C∩B)/P(B) = (3/36)/(6/36) = 1/2 ✓.

:::check Check 7
Two dice. (a) Find P(A | B): sum is 7, given the first die is 6. (b) Find P(B | C): first die is 6, given the sum is at least 10.
:::

### 8 · P(A | B) = 1: B forces A

A conditional probability can reach the ends of the 0–1 scale. The MCQ asks what the top end means.

:::q <span class="tag">A1 MCQ 8</span>
If P(A | B) = 1, then: (a) A is impossible whenever B occurs (b) A always occurs whenever B occurs (c) A and B are mutually exclusive (d) none of these.
:::

:::guess Guess first
On the dice grid, find an event that is certain once you know the first die is 6.
:::

[[fig:venn_subset|B drawn wholly inside A. Once B is known to have happened, the outcome is inside A too.|w=55]]

1. P(A | B) = 1 means P(A∩B)/P(B) = 1.
2. So P(A∩B) = P(B): every outcome of B is also in A.
3. So whenever B happens, A happens.

Dice: given the first die is 6, the sum is at least 7 in all six cells of row 6. P(sum ≥ 7 | first is 6) = 6/6 = 1.

**Answer.** Option **(b)**. The other end, P(A | B) = 0, is the mutually exclusive case (c): B rules A out.

:::check Check 8
Two dice. Find P(sum ≤ 6 | first die is 6). Which option of the MCQ describes this case?
:::

### 9 · The multiplication rule: "A and B" in stages

Step 7's formula, turned around, gives P(A∩B) when an experiment happens in stages.

:::q Predict
Two cards are drawn one after the other, **without** putting the first back. Find P(both are aces).
:::

:::guess Guess first
Is it (4/52) × (4/52)? Write what changes for the second card.
:::

Multiply step 7's formula by P(B):

$$P(A ∩ B) = P(B) · P(A | B)$$

Read it as: **chance the first stage goes B's way × chance the second goes A's way, given the first.** A **tree** draws this: one branch per stage, multiply along a path.

[[fig:aces_tree|Tree for two cards drawn without replacement. Each branch carries the probability of that stage given the branches before it. A path's probability is the product along it.|w=78]]

Dice check: P(B∩C) = P(B) · P(C | B) = (1/6)(1/2) = **1/12** = 3/36, the 3 cells of step 7 ✓.

**Answer to the Predict.** After one ace is drawn, 3 aces remain among 51 cards. P(both aces) = (4/52)(3/51) = 12/2652 = **1/221**. (4/52)² would be right only **with** replacement.

:::check Check 9
A bag holds 3 red and 2 blue balls. Two are drawn without replacement. Find P(both red) and P(first red, second blue).
:::

### 10 · Independence: when the news changes nothing

In step 7 knowing B changed C's chance. Sometimes the news changes nothing.

:::q Predict
From Check 7(a): P(A | B) = 1/6. Compare it with P(A) = 1/6 from step 3. What does knowing the first die tell you about "sum is 7"?
:::

:::guess Guess first
One sentence.
:::

:::note Terms
**Independent events:** knowing one happened does not change the chance of the other, P(A | B) = P(A).
:::

Put P(A | B) = P(A) into step 9's rule:

$$A, B independent  ⇔  P(A ∩ B) = P(A) · P(B)$$

Read it as: **for independent events, multiply the separate chances.** This is the test used in exams.

| Pair | P(·∩B) | P(·) × P(B) | Independent? |
|---|---|---|---|
| A = sum 7, B = first 6 | 1/36 | (1/6)(1/6) = 1/36 | yes |
| C = sum ≥ 10, B = first 6 | 3/36 = 1/12 | (1/6)(1/6) = 1/36 | no |

**Answer to the Predict.** Nothing: whatever the first die shows, exactly one blue face makes the sum 7. A and B are independent. C and B are not: a 6 first makes a big sum more likely.

:::trap Independent is not mutually exclusive
Mutually exclusive events (each with P > 0) are always **dependent**: if one happens, the other's chance drops to 0. "Sum is 2" and "sum is 12" are exclusive, and dependent.
:::

:::check Check 10
(a) P(A) = 0.4, P(B) = 0.5. Find P(A∩B) if A and B are independent, and if they are mutually exclusive. (b) A coin is tossed and a die thrown. Find P(head and six).
:::

### 11 · Total probability: adding the paths of a tree

The tree of step 9 had one starting branch. When an event can come about through several **causes**, add the paths that reach it.

:::q Predict
Machine M₁ makes 60 % of a factory's bolts, machine M₂ makes 40 %. 2 % of M₁'s bolts and 5 % of M₂'s bolts are defective. What share of **all** bolts is defective?
:::

:::guess Guess first
Is it the average of 2 % and 5 %, more, or less? Write a number.
:::

:::note Terms
**Partition:** events M₁, M₂, … that are mutually exclusive and together fill S (every bolt comes from exactly one machine). **D:** the event "the bolt is defective".
:::

[[fig:bolt_tree|Tree for one bolt. First branch: which machine made it. Second branch: defective or good, given that machine. The two paths ending in "defective" are multiplied out on the right and added.|w=82]]

1. Path through M₁: P(M₁) · P(D | M₁) = 0.6 × 0.02 = 0.012 (step 9).
2. Path through M₂: P(M₂) · P(D | M₂) = 0.4 × 0.05 = 0.020.
3. The paths are mutually exclusive, so add (axiom 3):

$$P(D) = P(M_{1})P(D | M_{1}) + P(M_{2})P(D | M_{2})$$

Read it as: **the chance of D = sum over every cause of (chance of the cause × chance of D from that cause).**

**Answer to the Predict.** P(D) = 0.012 + 0.020 = **0.032**, i.e. 3.2 %. Not the plain average 3.5 %: M₁, the cleaner machine, makes more of the bolts.

:::check Check 11
Same factory. Find P(good) in two ways: from the tree, and with the complement rule.
:::

### 12 · Bayes' theorem: from the effect back to the cause

Step 11 went forward: cause → defective. The question that matters on the shop floor goes backward.

:::q Predict
A bolt picked at random is found defective. Which machine more likely made it?
:::

:::guess Guess first
M₂ makes fewer bolts but more of them are bad. Write which machine you bet on.
:::

:::note Terms
**Prior P(Mᵢ):** the chance of cause i **before** seeing the bolt (0.6, 0.4). **Posterior P(Mᵢ | D):** its chance **after** seeing that the bolt is defective. File 10 uses both words.
:::

[[fig:bolt_bayes|The whole bar is P(D) = 0.032, the defective share of all bolts. Blue: the part coming through M₁ (0.012). Orange: through M₂ (0.020). Each posterior is its part's share of the bar.|w=78]]

1. P(M₂ | D) = P(M₂∩D)/P(D) (step 7).
2. P(M₂∩D) = P(M₂)P(D | M₂) (step 9), and P(D) is the sum of step 11:

$$P(M_{i} | D) = \frac{P(M_{i}) P(D | M_{i})}{Σ_{j} P(M_{j}) P(D | M_{j})}$$

Read it as: **one path to D, divided by all paths to D.** (G&K §4.8.)

**Answer to the Predict.** P(M₁ | D) = 0.012/0.032 = **0.375**. P(M₂ | D) = 0.020/0.032 = **0.625**. M₂ is the more likely source: its higher defect rate outweighs its smaller output. The two posteriors add to 1.

:::check Check 12
(a) A bolt is found **good**. Find P(M₁ | good). (b) Urn I holds 2 white and 3 black balls, urn II 4 white and 1 black. An urn is chosen by a coin toss and a ball drawn from it is white. Find P(urn I | white).
:::

---

## Exam form

**Definitions (one line each).** Random experiment · outcome · sample space S (all outcomes) · event (a group of outcomes) · mutually exclusive (A∩B = ∅) · complement Aᶜ · equally likely · independent (P(A∩B) = P(A)P(B)).

**Formulas.**

1. Classical: P(A) = m/n, when the n outcomes are equally likely.
2. Axioms: P(A) ≥ 0; P(S) = 1; A∩B = ∅ ⇒ P(A∪B) = P(A) + P(B). Hence 0 ≤ P(A) ≤ 1.
3. Complement: P(Aᶜ) = 1 − P(A); P(at least one) = 1 − P(none).
4. Addition: P(A∪B) = P(A) + P(B) − P(A∩B).
5. Conditional: P(A | B) = P(A∩B)/P(B), P(B) > 0.
6. Multiplication: P(A∩B) = P(B) · P(A | B); independent: P(A∩B) = P(A) · P(B).
7. Total probability: P(D) = Σ P(Mᵢ) P(D | Mᵢ), over a partition M₁, M₂, ….
8. Bayes: P(Mᵢ | D) = P(Mᵢ) P(D | Mᵢ) / Σⱼ P(Mⱼ) P(D | Mⱼ).

**Procedure for a Bayes question.**

1. Name the causes M₁, M₂, … and the observed event D.
2. Write the priors P(Mᵢ) and the chances P(D | Mᵢ) from the question.
3. Multiply along each path: P(Mᵢ)P(D | Mᵢ).
4. Add the paths: P(D).
5. Divide the asked path by P(D).

## Traps

- Adding P(A) + P(B) when A and B overlap: subtract P(A∩B).
- Swapping P(A | B) and P(B | A): the **given** event goes in the denominator.
- Treating "mutually exclusive" as "independent": exclusive events with P > 0 are dependent.
- Multiplying unconditional chances for draws **without** replacement: the second stage is conditional.
- Using m/n when outcomes are not equally likely (sums of two dice: 11 sums, but not each 1/11).
- In Bayes, dividing by P(Mᵢ) instead of by P(D).

## Self-test

1. Two dice: find P(sum = 8) and P(both dice show the same number).
2. Two dice: find P(at least one die shows 1).
3. P(A) = 0.6, P(B) = 0.5, P(A∪B) = 0.8. Find P(A∩B) and P(A | B).
4. Are the A and B of question 3 independent? Show the test.
5. A family has two children. Given that at least one is a boy, find P(both are boys).
6. Two dice: find P(sum is 8 | both dice are even).
7. 1 % of people have a condition. A test is positive for 90 % of those with it and for 5 % of those without. A person tests positive. Find P(has the condition).

<!--ANSWERS-->
## Answers

**Check 1.** (a) S = {HH, HT, TH, TT}, n = 4. (b) n = 2 × 6 = **12**.

**Check 2.** (a) C = {(4,6), (5,5), (6,4), (5,6), (6,5), (6,6)}: **6 cells** (sum 10: 3, sum 11: 2, sum 12: 1). (b) **Yes**: no cell has sum 7 and sum ≥ 10.

**Check 3.** (a) P(C) = 6/36 = **1/6**. (b) 2/10 = **0.2**.

**Check 4.** "Sum is 2" and "sum is 12" share no cell, so by **axiom 3**: 1/36 + 1/36 = **1/18**.

**Check 5.** (a) 1 − 1/6 = **5/6**. (b) P(no head) = (1/2)³ = 1/8, so P(at least one head) = **7/8**.

**Check 6.** (a) 4/52 + 13/52 − 1/52 = 16/52 = **4/13** (the ace of hearts is in both). (b) P(A∪B) = 0.5 + 0.3 − 0.1 = **0.7**; P(neither) = 1 − 0.7 = **0.3**.

**Check 7.** (a) A∩B = {(6,1)}: P(A | B) = (1/36)/(6/36) = **1/6**. (b) B∩C = 3 cells, C = 6 cells: P(B | C) = 3/6 = **1/2**.

**Check 8.** Row 6 has sums 7–12: no cell has sum ≤ 6. P = 0/6 = **0**. That is option (c): the two events are mutually exclusive.

**Check 9.** P(both red) = (3/5)(2/4) = **3/10**. P(red, then blue) = (3/5)(2/4) = **3/10**.

**Check 10.** (a) Independent: 0.4 × 0.5 = **0.2**. Mutually exclusive: **0**. (b) (1/2)(1/6) = **1/12**.

**Check 11.** Tree: 0.6 × 0.98 + 0.4 × 0.95 = 0.588 + 0.380 = **0.968**. Complement: 1 − 0.032 = **0.968** ✓.

**Check 12.** (a) P(M₁ | good) = 0.588/0.968 = **0.6074**. (b) P(white) = ½(2/5) + ½(4/5) = 0.2 + 0.4 = 0.6; P(I | white) = 0.2/0.6 = **1/3**.

**Self-test.**

1. Sum 8: (2,6), (3,5), (4,4), (5,3), (6,2) → **5/36**. Same number: 6 cells on the main diagonal → 6/36 = **1/6**.
2. No 1 on either die: 5 × 5 = 25 cells. P = 1 − 25/36 = **11/36**.
3. P(A∩B) = 0.6 + 0.5 − 0.8 = **0.3**; P(A | B) = 0.3/0.5 = **0.6**.
4. P(A)P(B) = 0.6 × 0.5 = 0.30 = P(A∩B), so **independent** (also P(A | B) = 0.6 = P(A)).
5. S = {BB, BG, GB, GG}; "at least one boy" = {BB, BG, GB}, 3 cells. P(BB | at least one boy) = **1/3**.
6. Both even: 3 × 3 = 9 cells. Of these, sum 8: (2,6), (4,4), (6,2) = 3. P = 3/9 = **1/3**.
7. P(+) = 0.01 × 0.90 + 0.99 × 0.05 = 0.009 + 0.0495 = 0.0585. P(condition | +) = 0.009/0.0585 = **0.1538**.
<!--/ANSWERS-->
