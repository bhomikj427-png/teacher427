# 04 — Economic decision making (L8–L9)

**Mostly theory**, and long-answer friendly: "Explain the rational decision-making process" or "importance of
economic decision making in engineering projects" are 5-mark questions answered by listing the points. There are two
small numericals, and **one of them has a slide error**.

## Map

```
 economic decision = choose the best alternative (max benefit / min cost) under constraints
   ├─ process: 5-step short form · 9-step rational process
   ├─ key elements: scarcity, opportunity cost, marginal analysis, incentives,
   │                trade-offs, rationality, decision models
   ├─ types: programmed vs non-programmed
   ├─ importance in engineering projects (9 points)
   ├─ factors influencing engineering decisions (12 points)
   └─ numericals: cloud server (EAC) · petrol vs electric car
```

---

## 1. Definition and process

**Economic decision making**: choosing, from the available alternatives, the one that **maximizes utility or benefit
or minimizes cost** within the constraints. It rests on rational weighing of costs and benefits. Individuals,
firms and governments all do it.

Decisions are made about **problems** (undesirable situations, e.g. cutting costs 10%) and **opportunities**
(desirable ones, e.g. unexpected extra profit). Whether a decision was right may not be known for a long time.

**Short process (5 steps):** identify the problem → list the alternatives → evaluate costs and benefits → select the
best → implement and review.

**Rational decision-making process (9 steps). Memorize this order:**

1. Recognize the problem
2. Define the goal or objective
3. Assemble relevant data (is more data worth its cost?)
4. Identify feasible alternatives
5. Select the criterion for choosing (economic, political, environmental, social, or a composite)
6. Mathematically model the interrelationships
7. Predict the outcome of each alternative
8. Choose the best alternative
9. Audit the results

**Q ▸** (L8-9) Map buying a car (Audi vs BMW) onto the steps.
Need a car → a high-level security system → gather technical and financial data → alternatives: Audi, BMW →
criterion: minimum total cash outlay → choose Audi (the deck's outcome).

## 2. Key elements

| Element | Meaning | Deck example |
|---|---|---|
| **Scarcity** | limited resources, unlimited wants | a Govt can't build highways, hospitals and schools all at once |
| **Opportunity cost** | the value of the **next-best alternative forgone** | ₹50,000 on a laptop = the skills/income from the course you skipped |
| **Marginal analysis** | compare the **additional** benefit and cost of one more unit | MC = 120, MB = 150 → MB > MC, so produce it |
| **Incentives** | rewards/penalties that change behaviour | higher wages → more effort. Tax rebates → more saving |
| **Trade-offs** | give up one thing to get another | quality vs cost. Defence vs welfare |
| **Rationality** | agents act logically to maximize utility/profit (not the same as selfishness) | buy the best satisfaction within budget, not necessarily the cheapest |
| **Decision models** | systematic frameworks | cost–benefit analysis, utility maximization, PPC |

## 3. Types of decisions

| | Programmed | Non-programmed |
|---|---|---|
| Nature | routine, repetitive, follows **predefined rules** | unstructured, rare, novel |
| Traits | structured, predictable, frequent, based on past experience | non-routine, complex, uncertain, needs **judgment** |
| Deck analogy | a train on a fixed track | a train at a junction where a human picks the direction |
| Examples | a McDonald's Big Mac procedure, Starbucks supply reordering | mergers, acquisitions, new facilities/products, labour contracts, legal issues |
| Who makes it | lower levels, by procedure | **top management**, using intuition and experience |

## 4. Importance in engineering projects (list for a long answer)

1. **Cost control**: compare designs/materials, stay within budget without losing quality
2. **Risk management**: cost overruns, delays, price swings, with the best risk–reward option chosen
3. **Return on investment**: large capital, so pick the higher-ROI alternative
4. **Life cycle cost**: initial + operating + maintenance + replacement + disposal, not just first cost
5. **Sustainability**: include environmental/social costs
6. **Stakeholder alignment**: numbers give a common basis
7. **Project feasibility**: reject unviable projects early
8. **Resource optimization**: materials, labour, time, energy
9. **Competitiveness**: viable, high-return projects attract investors and clients

**Factors influencing engineering economic decisions:** cost–benefit analysis · budget constraints ·
technological feasibility · resource availability · life cycle costs · market demand and competition · regulatory
and environmental rules · risk assessment · time constraints · government policies and incentives · stakeholder
expectations · scalability and flexibility.

**Case (L8-9): electronics firm, domestic vs international plant.** Factors to weigh: labour cost vs
shipping/logistics · market potential · regulatory environment · supply chain · political/economic stability ·
brand perception · financial viability (revenue, expenses, ROI in each scenario).

---

## 5. Petrol car vs electric car `[L8-9 case]`

> | | Petrol | Electric |
> |---|---|---|
> | Purchase | 8,00,000 | 12,00,000 |
> | Running cost / yr | 90,000 | 35,000 |
> | Life | 8 yr | 8 yr |
> | Resale after 8 yr | 2,00,000 | 3,00,000 |
>
> Which car should the student buy based on total cost over 8 years?

**Q ▸** Guess first: does the ₹4 lakh higher price get paid back?

| | Petrol | Electric |
|---|---|---|
| Purchase | 8,00,000 | 12,00,000 |
| + running × 8 | 7,20,000 | 2,80,000 |
| − resale | 2,00,000 | 3,00,000 |
| **Net 8-year cost** | **13,20,000** | **11,80,000** |

**Electric, cheaper by ₹1,40,000.** It saves ₹55,000/yr in running cost (₹4,40,000 over 8 years) plus ₹1,00,000 more
at resale, and that outweighs the ₹4,00,000 higher price.
*(The deck ignores the time value of money here. File 08 shows how you would discount it.)*

## 6. Cloud hosting: on-demand vs reserved `[L8-9 example]` ⚠ slide error

> A: on-demand, setup 0, ₹15,000/month. B: reserved, ₹2,50,000 upfront + ₹7,000/month. 3 years, interest
> 10% per year. Which is economically better?

**Q ▸** Before reading on: B's upfront ₹2.5 lakh has to be spread over 3 years **with interest**. How?

That is the **equivalent annual cost (EAC)**: convert every cost into an equal annual amount, then compare. An upfront
P becomes an annual amount using the **capital recovery factor**:

```
 (A/P, i, n) = i / (1 − (1+i)⁻ⁿ)          (A/P, 10%, 3) = 0.10 / (1 − 1.1⁻³) = 0.40211
```

| | A (on-demand) | B (reserved) |
|---|---|---|
| Running cost / yr | 15,000 × 12 = 1,80,000 | 7,000 × 12 = 84,000 |
| Upfront, annualized | 0 | 2,50,000 × 0.40211 = 1,00,529 |
| **EAC** | **₹1,80,000** | **₹1,84,529** |

**At 10%, A (on-demand) is cheaper, by ≈ ₹4,529/yr.**

**⚠ The slide states EAC(B) = ₹1,40,000 and chooses B. That doesn't follow from its own data.** Even ignoring
interest completely, B = 84,000 + 2,50,000/3 = ₹1,67,333, not 1,40,000. With no interest B would win, but at 10% interest
A wins. (This treats the monthly costs as annual sums, which is the slide's simplification.) **In the exam:**
show the working. If this exact question appears, write the computed answer and one line on the assumption.

---

## Self-test

1. Define opportunity cost and give an engineering example.
2. List the 9 steps of the rational decision-making process.
3. Programmed vs non-programmed: give 3 differences and one example of each.
4. MC = ₹200, MB = ₹180. Produce the extra unit? Why?
5. What is the capital recovery factor (A/P, i, n) used for?

---

## Answers

1. The value of the next-best alternative forgone. E.g. using a machine for product X means giving up the profit it would have made on product Y.
2. Recognize problem → define goal → assemble data → identify feasible alternatives → select criterion → model → predict outcomes → choose best → audit.
3. Routine vs novel. Rule-based vs judgment-based. Lower-level vs top management (also frequent vs rare). Examples: reordering supplies / a merger.
4. **No**. MB < MC, so the extra unit loses ₹20.
5. To convert a present (upfront) amount into an equivalent **equal annual** amount over n years at rate i. It is used for EAC comparisons.
