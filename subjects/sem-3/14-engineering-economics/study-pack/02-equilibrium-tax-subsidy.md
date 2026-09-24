# 02 — Market equilibrium, tax and subsidy (L4–L5)

**Numerical file. The 4 deck problems are all answered here, and every answer was checked with exact fractions.**
These are pure algebra once you know the one rule for tax and the one rule for subsidy.

## Map

```
 demand eqn + supply eqn ──► set Qd = Qs ──► P*, then Q*
          │
          ├── TAX T per unit ──► seller keeps P − T ──► supply becomes g(P − T)
          │                        └► new P′, Q′ · tax revenue = T × Q′ · seller gets P′ − T
          │
          ├── SUBSIDY S per unit ─► deck puts it on the demand side: f(P − S)
          │                        └► new P′, Q′ · total subsidy = S × Q′
          │
          └── factor cost changes ─► supply curve itself shifts ─► re-solve
```

---

## 1. Equilibrium

**Equilibrium**: the price at which **quantity demanded = quantity supplied**. Solve the two equations
simultaneously. Always find **P first, then substitute to get Q**, and check it in **both** equations.

## 2. Tax: which curve moves and why

**Q ▸** (L4-5) The market price is ₹100 and the tax is ₹10 per unit. How much does the producer actually get,
and which equation changes?

₹100 − ₹10 = **₹90**. The producer responds to the price **net of tax**, so the **supply** equation changes:

```
 Sₜ = g(Pₜ − T)        replace every P in the supply equation by (P − T)
```

The market price rises by less than T, the quantity falls, the government collects **T × Q′**, and the seller
**realises P′ − T**.

## 3. Subsidy (the deck's convention)

A subsidy is Government assistance that lowers the buyer's effective price. The deck writes it into
**demand**:

```
 Dₜ = f(Pₜ − S)        replace P in the demand equation by (P − S)
```

P′ is then the **market price the seller receives**. The buyer effectively pays **P′ − S**. The total
subsidy is **S × Q′**.

---

## 4. Problem 1 (tax) `[L4-5 P1]`

> Xd = ½(5 − P), Xs = 2P − 3. (i) equilibrium price and quantity (ii) new price and quantity with a tax of
> ₹6/5 per unit (iii) total tax revenue (iv) price actually realised by the seller.

**Q ▸** Set up (i) before reading on.

**(i)** ½(5 − P) = 2P − 3 → 5 − P = 4P − 6 → 5P = 11 → **P = 11/5 = ₹2.20**
Xd = ½(5 − 11/5) = ½ · 14/5 = **7/5 = 1.4 units** (check: Xs = 22/5 − 3 = 7/5 ✓)

**(ii)** New supply: Xs′ = 2(P′ − 6/5) − 3 = 2P′ − 27/5
½(5 − P′) = 2P′ − 27/5 → 5 − P′ = 4P′ − 54/5 → 5P′ = 79/5 → **P′ = 79/25 = ₹3.16**
Q′ = 2(79/25) − 27/5 = 158/25 − 135/25 = **23/25 = 0.92 units**

**(iii)** Tax revenue = T × Q′ = 6/5 × 23/25 = **138/125 = ₹1.104**

**(iv)** Seller realises P′ − T = 79/25 − 30/25 = **49/25 = ₹1.96**

Read the result: the price rose from 2.20 to 3.16, which is **less than the ₹1.20 tax**. Buyers carry 0.96 of it and sellers
0.24 (2.20 → 1.96).

## 5. Problem 2 (subsidy) `[L4-5 P2]`

> Demand P = 5 − 2X, supply P = ½(X + 5). (i) equilibrium (ii) new price and quantity with a subsidy of ₹5/2 per
> unit (iii) total subsidy.

**Q ▸** Which equation gets the subsidy, and how?

**(i)** 5 − 2X = ½(X + 5) → 10 − 4X = X + 5 → **X = 1**, **P = 5 − 2 = ₹3**

**(ii)** Demand becomes (P′ − 5/2) = 5 − 2X′ → P′ = 15/2 − 2X′
15/2 − 2X′ = ½(X′ + 5) → 15 − 4X′ = X′ + 5 → **X′ = 2**
P′ = ½(2 + 5) = **7/2 = ₹3.50**, the market price the seller receives. The buyer effectively pays 3.50 − 2.50 = **₹1**.

**(iii)** Total subsidy = S × X′ = 5/2 × 2 = **₹5**

## 6. Problem 3 (supply shift) `[L4-5 P3]`

> Qd = 200 − 10P, Qs = 50 + 15P. (i) equilibrium. (ii) A factor-input price change gives Qs′ = 100 + 15P′.
> Analyse the new equilibrium against the old.

**(i)** 200 − 10P = 50 + 15P → 150 = 25P → **P = ₹6**, Q = 200 − 60 = **140 units**
**(ii)** 200 − 10P′ = 100 + 15P′ → 100 = 25P′ → **P′ = ₹4**, Q′ = 200 − 40 = **160 units**

**Analysis (write this sentence):** the intercept rose from 50 to 100, so more is supplied at every price. The input got
**cheaper** and **supply increased** (the curve shifted right). The **equilibrium price fell (6 → 4) and the quantity rose
(140 → 160)**.

## 7. Problem 4 (tax) `[L4-5 P4]`

> Demand 3Q + 4P = 24, supply P = ¼Q + 3. (i) equilibrium (ii) tax ₹1/3 per unit (iii) tax revenue (iv) price
> realised by the seller.

**Q ▸** Rewrite the demand as P = … first.

Demand: 4P = 24 − 3Q → P = 6 − ¾Q

**(i)** 6 − ¾Q = ¼Q + 3 → **Q = 3**, **P = ¾ + 3 = 15/4 = ₹3.75**

**(ii)** Supply with tax: P′ − ⅓ = ¼Q + 3 → P′ = ¼Q + 10/3
6 − ¾Q = ¼Q + 10/3 → Q′ = 6 − 10/3 = **8/3 ≈ 2.67 units**
P′ = ¼ · 8/3 + 10/3 = 2/3 + 10/3 = **₹4**

**(iii)** Revenue = ⅓ × 8/3 = **8/9 ≈ ₹0.89**
**(iv)** Seller realises 4 − ⅓ = **11/3 ≈ ₹3.67**

---

## Traps

- If the equation is in **P = …** form (inverse supply), the tax goes in as **(P − T) = …**, i.e. P′ = old RHS + T.
  If it is in **Q = …** form, replace P by (P − T). Both say the same thing.
- **Revenue uses the new quantity Q′**, never the old one.
- Keep fractions until the last line. The deck's answers are fractions (79/25, 138/125).
- Always state the **seller's price = P′ − T** separately. It is its own sub-question in 2 of the 4 problems.

---

## Self-test

1. Qd = 100 − 5P, Qs = 20 + 3P. Find the equilibrium.
2. Same market, with a tax of ₹8 per unit. Find the new P′, Q′, the tax revenue and the seller's price.
3. Same market (no tax), with a subsidy of ₹4 per unit on the demand side (deck convention). Find P′, Q′, what the buyer pays, and the total subsidy.
4. In one line: why does the price rise by less than the tax?

---

## Answers

1. 100 − 5P = 20 + 3P → **P = 10, Q = 50**.
2. Qs′ = 20 + 3(P − 8) = 3P − 4 → 100 − 5P = 3P − 4 → **P′ = 13, Q′ = 35**. Revenue = 8 × 35 = **₹280**. Seller gets 13 − 8 = **₹5**.
3. Qd′ = 100 − 5(P − 4) = 120 − 5P = 20 + 3P → **P′ = 12.5, Q′ = 57.5**. Buyer pays 12.5 − 4 = **₹8.5**. Subsidy = 4 × 57.5 = **₹230**.
4. The quantity falls as the price rises, so the burden is **shared**: buyers pay part (a higher P′) and sellers absorb part (a lower net price).
