# 09 — Internal rate of return (L18–L19)

**Numerical, and it builds directly on 08.** IRR is the rate that makes NPV zero. You can't solve for it
algebraically, so the exam method is **two trial rates + linear interpolation**. There are 3 professor problems here. One has a
**⚠ slide error** in its working.

## Map

```
 IRR = the i at which NPV = 0   (PV of inflows = initial outlay)
   ├─ can't be isolated algebraically ─► trial and error / interpolation / calculator / Excel IRR()
   ├─ method: find i₁ with NPV > 0 and i₂ with NPV < 0 ─► interpolate
   ├─ decision: IRR > required rate ⇒ accept
   └─ NPV vs IRR: rupee amount vs a percentage
```

---

## 1. Definition

**Q ▸** `[L18]` At 15% a machine's NPV is +$282. At 20% it is −$5,141. Somewhere in between, NPV is exactly zero.
What is that rate called, and what does it tell you?

**Internal rate of return (IRR)**: the **discount rate at which NPV = 0**, i.e. the rate at which the PV of the inflows equals
the initial outlay. It is the project's **own annual rate of return** (its "yield"), and it is **not a rupee amount**.
```
 0 = Σₙ₌₁ᵗ  Fₙ / (1 + IRR)ⁿ  −  P          P = initial investment
```
**Decision:** IRR > the required rate (cost of capital) → **accept**. IRR is also the break-even discount rate: at
that rate the project makes neither profit nor loss in present-value terms.

**NPV vs IRR (a 2–3 marker):**

| NPV | IRR |
|---|---|
| PV(inflows) − PV(outflows) | the rate at which that difference is 0 |
| a **money** amount | a **percentage** |
| needs the discount rate as an input | is the output. Compare it with the required rate |
| shows the **excess** of inflows over outflows | shows the **break-even** rate |

*(Notes p11: Excel's IRR assumes equally spaced periods. **XIRR** lets you give each cash flow its own date,
which makes it more accurate for irregular timing.)*

## 2. Interpolation

```
 i* = i₁ + (i₂ − i₁) × (y* − y₁) / (y₂ − y₁)

 i₁ = rate with POSITIVE NPV y₁      i₂ = rate with NEGATIVE NPV y₂      y* = 0
 equivalently  i* = i₁ + (i₂ − i₁) × y₁ / (y₁ − y₂)
```

**Q ▸** `[L18-19 demo]` NPV is +200 at 10% and −100 at 15%. Find the IRR.

i* = 10 + (15 − 10) × (0 − 200)/(−100 − 200) = 10 + 5 × 200/300 = **13.33%**

The two trial rates **must bracket** zero, one positive and one negative. Keep them close (within 5%), because
interpolation assumes a straight line and the true NPV curve bends.

## 3. Machine `[L18-19 · notes p11]`

> Initial cost −$50,000. Additional $15,000 each year for 5 years. Economic acceptability at (a) 10% (b) 15% (c) 20%.
> Also find the IRR.

**Q ▸** One annuity factor per rate. Which of the three NPVs will be negative?

```
 (a) 10%:  −50,000 + 15,000 × 3.7908 = +$6,861.80   acceptable
 (b) 15%:  −50,000 + 15,000 × 3.3522 =   +$282.33   barely acceptable
 (c) 20%:  −50,000 + 15,000 × 2.9906 = −$5,140.82   not justifiable
```
The sign changes between 15% and 20%:
```
 IRR = 15 + 5 × 282.33 / (282.33 + 5,140.82) = 15 + 0.26 = 15.26 %
```
(The exact IRR is 15.24%. Interpolation lands slightly high because the NPV curve is convex. Write 15.26%.)
**Accept if the required rate is below ≈ 15.2%.**

## 4. Equipment with salvage `[L18-19 · notes p10]` ⚠ slide error

> Equipment costs 5,00,000. Life 4 years, generating an additional 1,60,000 of annual profit. "In the fifth year, the company
> plans to sell the equipment for its salvage value of 50,000." Calculate the IRR.

**Q ▸** Which year does the 50,000 go in? Decide before reading on, because the two sources disagree.

**Reading 1, the slide:** the salvage arrives at the **end of year 4**, so the flows are −5,00,000, 1,60,000 × 3, then 2,10,000.
```
 NPV at 13% = −5,00,000 + 1,60,000/1.13 + 1,60,000/1.13² + 1,60,000/1.13³ + 2,10,000/1.13⁴ = +6,581
 NPV at 14% = … same with 1.14 …                                                           = −4,202
 IRR = 13 + 1 × 6,581 / (6,581 + 4,202) = 13.61 %
```
**⚠ The slide prints NPV₁₃ ≈ +9,635 and NPV₁₄ ≈ −6,774. Both are wrong. The correct values are +6,581 and −4,202.** Its final
IRR ≈ 13.61% is right (exact 13.61%).

**Reading 2, the handwritten notes:** the salvage arrives in **year 5** as a separate flow: −5,00,000, 1,60,000 × 4, then 50,000
→ **IRR ≈ 13.28%** (notes: 13.27%).

**In the exam:** state which year you put the salvage in, then follow it through. The year-4 reading matches "life of four
years" and is the professor's own slide answer.

---

## Traps

- NPV must be **positive at i₁ and negative at i₂**. If both have the same sign, pick another rate.
- Interpolation is **linear**, so the answer is approximate. Say "≈".
- IRR is compared against the **required rate**, not against 0.

---

## Self-test

1. Cost ₹10,000, inflows ₹4,000/yr for 3 years. The NPV at 9% and 10% brackets zero. Find both NPVs and interpolate the IRR.
2. Project NPV: +₹500 at 12%, −₹300 at 16%. Find the IRR.
3. The IRR is 14% and the cost of capital is 11%. Decision?

---

## Answers

1. 9%: −10,000 + 4,000 × 2.5313 = **+₹125.2**. 10%: −10,000 + 4,000 × 2.4869 = **−₹52.6**. IRR = 9 + 125.2/177.8 = **9.70%** (exact 9.70%).
2. 12 + 4 × 500/800 = **14.5%**
3. **Accept.** The project earns more than its capital costs.
