# 08 — Time value of money and NPV (L15–L17)

**The single most important file.** NPV takes up 3 lectures and appears in the deck, in the older Payback deck, and in
the handwritten notes. There are **8 professor problems here, all recomputed**. One of them has a **⚠ slide error**.

## Map

```
 time value of money: ₹1 today > ₹1 tomorrow
    ├─ future value   F = P(1+i)ⁿ
    ├─ present value  P = F / (1+i)ⁿ          (1+i)⁻ⁿ = present worth factor
    ├─ annuity PV     P = A · [1 − (1+i)⁻ⁿ] / i     (A every year for n years)
    └─ NPV = Σ Fₙ/(1+i)ⁿ − initial investment
           ├─ decision: > 0 accept · < 0 reject · = 0 indifferent
           ├─ comparing projects: higher NPV wins
           ├─ comparing costs (furnace): lower PV of cost wins
           └─ effect of the discount rate
```

---

## 1. Why money has a time value

**Q ▸** `[L15]` Grandfather offers ₹1,00,000 at the end of year 5, or ₹75,000 today. Which do you take?

**₹75,000 today** (the deck's answer): the present is **certain**, ₹75,000 can be **invested to earn a return**, and
inflation erodes ₹1,00,000 by year 5. Put a number on it: at 10%, ₹1,00,000 in 5 years is worth only
1,00,000/1.1⁵ = **₹62,092 today**, which is less than ₹75,000. (₹75,000 grows to ₹1,00,000 at only 5.9% a year, so the lakh wins only if
you can't earn even 5.9%.)

## 2. Future value and present value

Compound interest, built step by step (the deck and notes use P = 100, i = 5%):

```
 F₁ = P + Pi        = P(1+i)         100 × 1.05   = 105
 F₂ = F₁ + F₁i      = P(1+i)²        100 × 1.05²  = 110.25
 ⋮
 Fₙ = P(1+i)ⁿ                          (simple interest would be F = P(1 + ni))
```
Rearranged, it gives the **present value** of a future amount:
```
 P = F / (1+i)ⁿ = F(1+i)⁻ⁿ         (1+i)⁻ⁿ is the PRESENT WORTH FACTOR (PWF)
```

**Q ▸** `[L15 · notes p3]` Someone promises you $1000 in 5 years. At 10%, what amount today is equivalent?

P = 1000 / 1.1⁵ = 1000 / 1.61051 = **$620.92 ≈ $621**

## 3. Present value of a series (annuity)

If the same amount A arrives at the end of each of n years:
```
 Pₙ = A/(1+i) + A/(1+i)² + … + A/(1+i)ⁿ
    = A · [1 − (1+i)⁻ⁿ] / i            (sum of a geometric progression with ratio 1/(1+i))
```
The bracket is the **annuity factor (P/A, i, n)**. Values used in this pack:

| i, n | factor | i, n | factor |
|---|---|---|---|
| 10%, 5 | 3.7908 | 10%, 10 | 6.1446 |
| 12%, 3 | 2.4018 | 12%, 8 | 4.9676 |
| 15%, 5 | 3.3522 | 20%, 5 | 2.9906 |
| 30%, 10 | 3.0915 | | |

## 4. NPV: definition and decision rule

**Net present value** = PV of cash inflows − PV of cash outflows:
```
 NPV = Σₙ₌₁ᵗ  Fₙ / (1+i)ⁿ  −  F₀          F₀ = initial investment (the cash outlay at time 0)
```
| NPV | Meaning | Decision |
|---|---|---|
| > 0 | inflows are worth more than the outlay, today | **accept** |
| < 0 | the project destroys value | **reject** |
| = 0 | it exactly earns the discount rate | indifferent (may accept or reject) |

The discount rate **i** is the **expected return from the alternative investment** (the cost of capital). A **higher** i
shrinks far-future cash flows more.
(Deck example: Company X valuing Company A discounts A's 10-year projected cash flows at its WACC, the weighted average cost of capital,
and subtracts the purchase price.)

---

## 5. Single project `[L16-17 · notes p8]`

> Initial investment $2000. Cash flow $100 for 3 years plus $2500 in the third year. Target rate 10%. Find the NPV.

**Q ▸** Write the four discounted terms.

```
 NPV = 100/1.1 + 100/1.1² + 100/1.1³ + 2500/1.1³ − 2000
     = 90.91 + 82.64 + 75.13 + 1878.29 − 2000
     = $126.97  > 0  → accept
```

## 6. Choosing between two projects `[L16-17]` ⚠ slide error

> Initial investment $10,000 each. Cost of capital 10%. Cash flows years 1–4: A = 5000, 4000, 3000, 1000 · B = 1000, 3000,
> 4000, 6750. Find the NPV of each. Which project should the firm choose?

| Year | A | PV of A | B | PV of B |
|---|---|---|---|---|
| 1 | 5000 | 4545.45 | 1000 | 909.09 |
| 2 | 4000 | 3305.79 | 3000 | 2479.34 |
| 3 | 3000 | 2253.94 | 4000 | **3005.26** |
| 4 | 1000 | 683.01 | 6750 | 4610.34 |
| Σ PV | | 10,788.20 | | 11,004.03 |
| **NPV** | | **$788.20** | | **$1,004.03** |

**NPV(B) > NPV(A) → choose B.**
**⚠ The slide shows NPV A = $780.18 (its PV sum is mis-added) and NPV B = $1052.19 (it gives B's year-3 PV as 3053.43, which should be
4000/1.331 = 3005.26).** The conclusion is the same. Use the corrected figures.

## 7. Comparing costs: furnaces `[L16-17 · notes p4–5]`

> A standard furnace costs $100 and uses $40/yr of fuel for 10 years. A high-efficiency furnace costs $200 and uses $20/yr for 10 years.
> At 10%, which is the better investment?

**Q ▸** These are all costs, so which PV do you want: the higher or the lower?

The **lower** PV of total cost:
```
 PV(standard) = 100 + 40 × 6.1446 = $345.78  ≈ $346
 PV(high-eff) = 200 + 20 × 6.1446 = $322.89  ≈ $323
 → high-efficiency is cheaper by ≈ $23
```
**Or directly (incremental NPV):** pay $100 extra, save $20/yr → −100 + 20 × 6.1446 = **+$22.89 > 0** → buy the high-efficiency one.

**Effect of the discount rate.** At **30%**: −100 + 20 × 3.0915 = **−$38.17 < 0** → the **standard** furnace wins.
A high discount rate means the money could earn a lot elsewhere, so future savings count for little and the option with the
**lower initial cost** is preferred.

## 8. Payback and NPV disagree `[L16-17 · notes p6]`

> Discount rate 10%. Year 0–5: A = −1200, 400, 400, 400, 200, 200 · B = −1200, 400, 400, 350, 800, 800. Evaluate by
> payback and by NPV, and select one.

**Payback:** A recovers 1200 exactly at the end of year 3 → **3 years**.
B: 400 + 400 + 350 = 1150 after year 3, 50 left → 3 + 50/800 = **3.0625 years**.
**NPV:**
```
 A = −1200 + 400/1.1 + 400/1.1² + 400/1.1³ + 200/1.1⁴ + 200/1.1⁵ =  $55.53
 B = −1200 + 400/1.1 + 400/1.1² + 350/1.1³ + 800/1.1⁴ + 800/1.1⁵ = $800.32
```
**Select B.** Payback prefers A by about 3 weeks (0.0625 yr), but ignores B's large years 4–5 flows. NPV counts them. This is the
"ignores flows after payback" con made concrete.

## 9. Real estate `[L16-17 practice problem]`

> Land costs ₹2,00,000. It generates ₹30,000/yr for the next 3 years. Cost of capital 12%. Find the NPV. Viable?

PV = 30,000 × 2.4018 = **₹72,055**
NPV = −2,00,000 + 72,055 = **−₹1,27,945 < 0 → not financially viable**

*Notes version (8 years):* PV = 30,000 × 4.9676 = ₹1,49,029 → NPV = **−₹50,971**, still not viable. Check which duration your
paper states.

## 10. Straight annuity `[notes p9]`

> Initial investment ₹1,50,000, cash flow ₹50,000 each year, discount rate 10%, 5 years.

NPV = −1,50,000 + 50,000 × 3.7908 = −1,50,000 + 1,89,539 = **₹39,539 > 0 → accept**

---

## Traps

- **Year 0 is not discounted.** The investment enters at full value.
- For **costs-only** comparisons (furnace), pick the **lowest** PV. For income projects, pick the **highest** NPV.
- Use the annuity factor only when the flows are **equal** every year. Otherwise discount each year separately.
- Show one line of substitution before jumping to the factor value.

---

## Self-test

1. ₹5,000 invested at 8% compound for 3 years. Find F.
2. PV of ₹10,000 received in 4 years at 12%.
3. Cost ₹20,000, returns ₹6,000/yr for 5 years, i = 10%. NPV and decision.
4. In one line: why does raising the discount rate favour the low-first-cost option?

---

## Answers

1. F = 5000 × 1.08³ = **₹6,298.56**
2. P = 10,000 / 1.12⁴ = **₹6,355.18**
3. NPV = −20,000 + 6,000 × 3.7908 = **₹2,744.72 > 0 → accept**
4. A higher rate discounts distant savings more heavily, so the extra money spent up front is recovered in smaller present-value terms.
