# 07 — Simple payback and rate of return (L14)

**Easy marks.** There are two formulas, one table method, and one decision line. The deck, the Payback deck and the handwritten
notes all use the same 5 problems, so they are very likely to come up.

## Map

```
 payback period = time to recover the initial investment
    ├─ EVEN cash flow ───► PB = initial investment / annual cash inflow
    ├─ UNEVEN cash flow ─► cumulative table ─► PB = years before full recovery
    │                                                 + unrecovered cost / cash flow in that year
    ├─ decision ─────────► accept if PB ≤ the maximum desired payback
    ├─ pros / cons ──────► simple · ignores TVM and post-payback flows
    └─ ROR = annual saving / initial investment = 1 / PB
```

---

## 1. Payback period: even cash flow

**Q ▸** `[L14 · Payback deck]` Company X's project costs $10,500 and returns $2,500 a year for 7 years. When does it pay for itself?

**Payback period**: the length of time needed to **recover the initial investment** from the project's net cash
inflows. When every year's inflow is the same:

```
 Payback = initial investment / annual net cash inflow = 10,500 / 2,500 = 4.2 years
```

Notes version `[handwritten notes p1]`: a lighting retrofit costs $1,000 and saves $250/yr → SP = 1000/250 = **4 years**.

## 2. Net inflow first, then payback `[L14 · beverage equipment]`

> Equipment $37,500, life 10 years, maximum desired payback 4 years. Annual sales $75,000. Annual outflows:
> ingredients $45,000, salaries $13,500, maintenance $1,500. Should XYZ Beverage buy it (payback method)?

**Q ▸** What goes in the denominator: the sales, or something else?

The **net** annual inflow:
Net = 75,000 − (45,000 + 13,500 + 1,500) = **$15,000**
Payback = 37,500 / 15,000 = **2.5 years**

**Decision:** 2.5 < 4 (the maximum desired) → **purchase the equipment.**

## 3. Uneven cash flow: the cumulative table `[L14]`

> Investment $200,000. Inflows: Y1 70,000 · Y2 60,000 · Y3 55,000 · Y4 40,000 · Y5 30,000 · Y6 25,000. Find the payback.
> Invest if management wants recovery within 3 years?

**Q ▸** Build the cumulative column and find the year the total crosses 200,000.

| Year | Inflow | Cumulative |
|---|---|---|
| 1 | 70,000 | 70,000 |
| 2 | 60,000 | 1,30,000 |
| 3 | 55,000 | **1,85,000** ← still short |
| 4 | 40,000 | 2,25,000 ← crosses 2,00,000 |
| 5 | 30,000 | 2,55,000 |
| 6 | 25,000 | 2,80,000 |

```
 Payback = years before full recovery + (unrecovered cost at start of the year / cash flow during that year)
         = 3 + (200,000 − 185,000) / 40,000 = 3 + 0.375 = 3.375 years
```

**Decision:** 3.375 > 3 → **don't invest** (the 3-year target is missed).

**The unrecovered-balance version** `[L14 · notes p1]`:

> Investment ₹50,000. Cash flows ₹15,000, ₹20,000, ₹14,000, ₹16,000 over the next 4 years.

| Year | Cash flow | Balance still to recover |
|---|---|---|
| 0 | −50,000 | −50,000 |
| 1 | 15,000 | −35,000 |
| 2 | 20,000 | −15,000 |
| 3 | 14,000 | **−1,000** |
| 4 | 16,000 | +15,000 ← recovered during year 4 |

Payback = 3 + 1,000 / 16,000 = **3.0625 years**

## 4. Pros and cons (2–3 marks)

| Pros | Cons |
|---|---|
| very simple and cheap to compute | **ignores the time value of money** |
| links annual cash flow directly to the investment | **ignores everything after payback**, and so ignores overall profitability |
| favours quick cash return, which is useful for **cash-poor firms** | |

(File 08 §6 shows the second con in action: two projects with nearly the same payback have very different NPVs.)

## 5. Rate of return (ROR) `[L14]`

**Q ▸** For the $10,500 / $2,500 project, what fraction of the investment comes back each year?

**ROR** = the annual return on the investment, which is the **reciprocal of simple payback**:
```
 ROR = saving per year / initial investment = 2,500 / 10,500 = 0.2381 = 23.8 %
 check: 1 / 4.2 = 0.238 ✓
```
Lighting retrofit (notes): 250 / 1000 = **25%** (= 1/4).

---

## Traps

- Use **net** inflow (inflow − outflows), never gross sales.
- In the fraction, the denominator is the **cash flow of the year in which recovery happens**, not the last year's.
- Write the **decision** against the stated target.

---

## Self-test

1. Cost ₹48,000, saving ₹12,000/yr. Find the payback and the ROR.
2. Cost ₹60,000. Flows ₹20,000, ₹25,000, ₹30,000. Find the payback.
3. Why can payback pick the wrong project?

---

## Answers

1. PB = **4 years**. ROR = 12,000/48,000 = **25%**.
2. After year 2: 45,000 recovered, 15,000 left → 2 + 15,000/30,000 = **2.5 years**.
3. It ignores the time value of money and every cash flow after payback, so a project with big later returns (higher NPV) can lose to one that merely recovers faster.
