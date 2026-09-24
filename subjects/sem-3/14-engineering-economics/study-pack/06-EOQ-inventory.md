# 06 — Inventory and EOQ (L13 + the EOQ practice sheet)

**High-yield numerical.** The professor handed out a practice sheet for this lecture, which is the nearest thing to an
assignment you have. **All 4 sheet questions and both deck examples are answered here, and every number was recomputed.**

## Map

```
 inventory ─► demand: dependent / independent
     ├─ costs: ordering S · holding H · shortage
     ├─ control: continuous (fixed quantity) vs periodic (fixed time)
     └─ EOQ model
          assumptions ─► TC = DC + (D/Q)S + (Q/2)H ─► dTC/dQ = 0 ─► Q* = √(2DS/H)
          then: orders/yr = D/Q* · cycle time = Q*/D · ROP = demand rate × lead time
```

---

## 1. The words

- **Inventory**: a stock of items kept to meet future demand (the shop's 50 phones). Managing it means answering
  **how many to order** and **when to order**.
- **Dependent demand**: items used to make a final product (tyres for cars). **Independent demand**: items bought by
  external customers (cars, appliances, houses).
- **Costs:** **ordering cost S** (the cost of placing/replenishing one order) · **holding/carrying cost H** (the cost of
  keeping one unit in stock for a year) · **shortage cost** (sales lost when demand can't be met).
- **Continuous (fixed-order-quantity) system:** order a **fixed amount** when stock falls to a set level ("at 50
  sugar packets, reorder"). **Periodic (fixed-time-period) system:** check at **fixed intervals** and order a **variable**
  amount ("check monthly, top up").

## 2. The EOQ model

**Q ▸** Order in huge batches and you rarely pay the ordering cost, but you store a lot. Order in tiny batches and
storage is cheap, but you pay the ordering cost constantly. Where is the minimum?

**EOQ (Economic Order Quantity)** is the order size Q that **minimizes total inventory cost**.

**Assumptions** (a common 2-marker): demand known, constant and deterministic · ordering cost per order fixed ·
holding cost per unit per year constant · instant replenishment (zero lead time) · no shortages · constant unit price.

**Building the total cost** (D = annual demand, C = unit price, S = cost per order, H = holding cost/unit/yr):

```
 Purchasing cost = D × C                 (fixed, since you buy D whatever Q is)
 Ordering cost   = (D / Q) × S           number of orders × cost per order
 Holding cost    = (Q / 2) × H           stock falls uniformly Q → 0, so the average is Q/2

 TC = DC + (D/Q)S + (Q/2)H
```

**Derivation** (write it for a 5-marker):
```
 dTC/dQ = −DS/Q² + H/2 = 0   ⇒   Q² = 2DS/H   ⇒   Q* = √(2DS / H)
```
**At Q\*, ordering cost = holding cost.** That is the trade-off picture: the ordering cost falls as Q rises, the holding cost
climbs, and the total cost is U-shaped with its bottom where the two cross.

**After Q\*:**
```
 number of orders / yr = D / Q*
 cycle time            = Q* / D  years   (× 12 for months, × 365 for days)
 reorder point (ROP)   = demand rate × lead time      (lead time = order placed → order received)
 H given as a %?       H = % × unit price
```

---

## 3. Car dealer `[L13 example]`

> Demand 5,000 cars/yr. It costs 15,000 to have cars shipped (per order). Holding cost 500 per car per year. How many
> times should the dealer order, and what should the order size be?

**Q ▸** Identify D, S and H first.

D = 5,000 · S = 15,000 · H = 500
Q* = √(2 × 15,000 × 5,000 / 500) = √3,00,000 = **548 cars per order**
Orders/yr = 5,000 / 548 = **9.13 ≈ 9 times a year**, roughly every 40 days.

## 4. Raw material, with carrying cost as a % `[L13 example]`

> 16,000 units/yr at ₹2 per unit. Ordering cost ₹45. Carrying cost 10% per year per unit of the average inventory.
> Find the EOQ and the cycle time.

**Q ▸** H isn't given in rupees. Get it first.

H = 10% × ₹2 = **₹0.20** per unit per year
Q* = √(2 × 16,000 × 45 / 0.20) = √72,00,000 = **2,683 units**
Orders/yr = 16,000 / 2,683 = **5.96 ≈ 6**
Cycle time = 2,683 / 16,000 = 0.168 yr = **≈ 2 months (61 days)**

## 5. Batteries `[EOQ sheet Q1]`

> Annual demand ≈ 1,200 batteries. Cost ₹28 each. Holding cost 30% of the battery's cost. ₹20 per order. The supplier currently
> orders 100 per month. (a) inventory cost of the current order quantity (b) EOQ (c) orders per year at the EOQ.

H = 0.30 × 28 = **₹8.40**, S = 20, D = 1,200

**(a)** Q = 100: ordering = (1200/100) × 20 = **₹240**. Holding = (100/2) × 8.40 = **₹420**. **Total ₹660/yr**
*(the sheet writes `(1200*100)/20` here. It means (1200/100) × 20, and the result, 240, is right.)*

**(b)** Q* = √(2 × 1200 × 20 / 8.40) = √5714.3 = **75.6 ≈ 76 batteries**

**(c)** 1200 / 75.6 = **15.9 ≈ 16 orders/yr**

At the EOQ the cost is 317.5 + 317.5 = **₹635/yr**, which saves ₹25/yr over the current policy. Ordering = holding, as predicted.

## 6. Indian Telecom, with a reorder point `[EOQ sheet Q2]`

> Indian Telecom contracts to buy 12,500 instruments during the year at ₹2.50 each. "The deliveries of the instruments
> will be made each time twice a month after the order is placed." Carrying cost ₹48 per instrument per annum. Paperwork,
> follow-up, transport and receipt work out to ₹2,000. How frequently should orders be placed? What is the re-order point?

**Q ▸** Which of the given numbers is S, and which is H?

S = ₹2,000 (per order) · H = ₹48 · D = 12,500
EOQ = √(2 × 12,500 × 2,000 / 48) = √10,41,667 = **1,021 instruments**
Orders/yr = 12,500 / 1,021 = **12.2 ≈ 12** (about once a month)
Lead time: the sheet reads the garbled delivery sentence as **½ month = 1/24 yr** (state that assumption) → **ROP = 12,500 / 24 = 521 units**. Reorder when the stock falls to 521.
(The ₹2.50 unit price doesn't enter the EOQ, because H is already given in rupees.)

## 7. Lead time in months `[EOQ sheet Q3]`

> Consumption 20 units/yr. Procurement cost ₹40 per order. Unit cost ₹100. Carrying cost 16% of the average stock. (i) EOQ
> (ii) with a lead time of 3 months, the reorder point.

H = 0.16 × 100 = **₹16** *(the sheet prints "0.16%". It means 16%, because 0.16% would make H ₹0.16 and the EOQ 100.)*
EOQ = √(2 × 20 × 40 / 16) = √100 = **10 items**
Consumption rate = 20/12 per month → ROP = (20/12) × 3 = **5 units**

## 8. Bicycle tyres `[EOQ sheet Q4]`

> 450 bicycles a month. Tyres at ₹20 each. Carrying cost 15% of cost. Ordering cost ₹50 per order. (i) EOQ (ii) orders per year
> (iii) total cost.

**Q ▸** What is D? (Look at "bicycles" and "tyres" again.)

D = 2 tyres × 450 × 12 = **10,800 tyres/yr** (**the trap: 2 tyres per bicycle, and monthly → annual**)
H = 0.15 × 20 = **₹3**, S = 50
EOQ = √(2 × 10,800 × 50 / 3) = √3,60,000 = **600 tyres**
Orders = 10,800 / 600 = **18 per year**
**(iii)** Ordering = 18 × 50 = ₹900. Holding = (600/2) × 3 = ₹900 → inventory cost **₹1,800**.
Including purchase (10,800 × 20 = ₹2,16,000): **TC = ₹2,17,800/yr**. *(The sheet stops before (iii). Give both
figures and label them.)*

---

## Traps

- **H must be in ₹ per unit per year.** If it is given as a %, multiply by the unit price.
- **D must be annual.** Convert monthly figures, and check units per product (tyres per bike).
- The EOQ never depends on the purchase price C directly, only through H when H is a %.
- ROP needs the lead time in the **same time unit** as the demand rate.
- Round the EOQ to whole units, and say so.

---

## Self-test

1. D = 2,400/yr, S = ₹50, H = ₹6. Find the EOQ, orders/yr, cycle time, and the total inventory cost.
2. Same item, lead time ½ month. Find the ROP.
3. Show that ordering cost = holding cost at Q\*.
4. State 4 assumptions of the EOQ model.

---

## Answers

1. Q* = √(2 × 2400 × 50 / 6) = √40,000 = **200**. Orders = **12/yr**. Cycle = 200/2400 yr = **1 month**. Cost = 12 × 50 + 100 × 6 = 600 + 600 = **₹1,200**.
2. ROP = (2400/12) × ½ = **100 units**.
3. Put Q* = √(2DS/H) into (D/Q)S: D·S/√(2DS/H) = √(DSH/2). And (Q/2)H = √(2DS/H)·H/2 = √(DSH/2). They are equal.
4. Demand known and constant · fixed cost per order · constant holding cost · instant replenishment / no shortages · constant price.
