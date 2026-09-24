# 10 — Mock MTE (30 marks, 90 min)

**The format is assumed:** there is no MEE2003 paper yet, so this copies the ECE2108 MTE sat the same week (A: 2+2+3 · B: 3 × 5 ·
C: 1 × 8). **New numbers throughout**, so this tests the method, not memory of the slide answers. Every answer was
computed by script. Covers L1–L19 only (break-even and cost analysis haven't been uploaded).

Sit it closed-book, with a calculator, and write full working. **Answers are at the bottom.**

---

## Section A (7 marks)

**A1** (2) Differentiate between a *change in quantity demanded* and a *change in demand*, with a sketch.

**A2** (2) The price of a product falls from ₹40 to ₹36 and the quantity demanded rises from 500 to 600 units. Find the
price elasticity of demand and classify it.

**A3** (3) Annual demand 4,500 units. Ordering cost ₹100 per order. Unit price ₹50, carrying cost 20% of the unit price per
year. Find the EOQ, the number of orders per year, and the cycle time in days.

## Section B (15 marks)

**B1** (5) Demand Qd = 120 − 4P and supply Qs = 20 + 6P.
(i) Find the equilibrium price and quantity.
(ii) A tax of ₹5 per unit is imposed. Find the new equilibrium price and quantity, the Government's tax revenue, and the price
the seller actually realises.

**B2** (5) An investment of ₹1,00,000 yields ₹30,000, ₹40,000, ₹35,000 and ₹25,000 at the ends of years 1–4. The discount rate
is 10%. Find (i) the payback period and (ii) the NPV. Should the project be accepted?

**B3** (5) (a) Differentiate a ROM estimate from a definitive estimate (3).
(b) A past project of 12,000 lines of code took 1,800 person-hours. Estimate the effort for a similar 20,000-line project
and name the technique (2).

## Section C (8 marks)

**C1** (8) A machine costs ₹80,000 and yields ₹25,000 a year for 5 years.
(a) Simple payback period and ROR (2)
(b) NPV at 10% (2)
(c) IRR by interpolation between 16% and 18% (3)
(d) Accept or reject if the required rate is 12%? Justify with both NPV and IRR (1)

---
---

## Answers

**A1** Change in **quantity demanded**: caused by the good's **own price** → **movement along** the curve (expansion or contraction).
Change in **demand**: caused by **other factors** (income, tastes, related prices, population) → the **whole curve shifts** (right =
increase, left = decrease). Sketch: one curve with two points on it, next to two parallel curves D₁ → D₂.

**A2** ΔQ = 100, ΔP = −4. Eₚ = (100/−4) × (40/500) = **−2.0** → |Eₚ| > 1, **relatively elastic**.

**A3** H = 0.20 × 50 = ₹10.
EOQ = √(2 × 4500 × 100 / 10) = √90,000 = **300 units**.
Orders = 4500/300 = **15 per year**.
Cycle time = 300/4500 yr = 0.0667 yr = **24.3 days** (0.8 month).
*(Inventory cost at the EOQ = 1,500 + 1,500 = ₹3,000/yr.)*

**B1** (i) 120 − 4P = 20 + 6P → **P = ₹10, Q = 80**.
(ii) Qs′ = 20 + 6(P − 5) = 6P − 10 → 120 − 4P = 6P − 10 → **P′ = ₹13, Q′ = 68**.
Tax revenue = 5 × 68 = **₹340**. The seller realises 13 − 5 = **₹8**. (Buyers carry ₹3 of the tax, sellers ₹2.)

**B2** (i) Cumulative: 30,000 → 70,000 → 1,05,000. It crosses in year 3: 2 + 30,000/35,000 = **2.86 years**.
(ii) PVs: 27,272.73 + 33,057.85 + 26,296.02 + 17,075.34 = 1,03,701.93
NPV = 1,03,701.93 − 1,00,000 = **₹3,701.93 > 0 → accept**.

**B3** (a) ROM: earliest stage, minimal information, based on experience, accuracy −50% to +100%, used for go/no-go. Definitive:
final planning stage, complete scope and specs, detailed cost breakdown, accuracy −5% to +10%, used for funding approval.
(b) **Analogous** estimating: 1,800 × 20,000/12,000 = **3,000 person-hours**.

**C1** (a) Payback = 80,000/25,000 = **3.2 years**. ROR = 25,000/80,000 = **31.25%**.
(b) NPV₁₀ = −80,000 + 25,000 × 3.7908 = **₹14,770 > 0**.
(c) NPV₁₆ = −80,000 + 25,000 × 3.2743 = **+₹1,857**. NPV₁₈ = −80,000 + 25,000 × 3.1272 = **−₹1,821**.
IRR = 16 + 2 × 1,857/(1,857 + 1,821) = **≈ 17.01%** (exact 16.99%).
(d) **Accept.** NPV at 12% = +₹10,119 > 0, and IRR ≈ 17% > 12%.
