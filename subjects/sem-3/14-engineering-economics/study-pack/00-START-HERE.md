# Engineering Economics MEE2003 — MTE Study Pack

**Built 2026-09-25 from what you uploaded:** 10 decks (L1–L19), the L13 EOQ practice sheet, the
handwritten L14–19 notes and the course hand-out. No assignment has been uploaded yet, so the
**professor's own problems** play the assignment's role. Every section opens with one of them, you guess
first, then the section teaches what the question needs.

> **Accuracy.** You asked for a pack, not research, so this is built from the slides. The content is standard
> engineering economics (Panneerselvam, the prescribed text, agrees). **Every number in this pack was
> recomputed by script.** Where a slide's arithmetic is wrong, the pack gives the correct figure and marks
> it **⚠ slide error**. There are 3 of them: `04` §2, `08` §5, `09` §4.

---

## What's on the MTE

| Source | Says |
|---|---|
| Hand-out lecture plan | **MID TERM EXAM printed after L24** |
| Marks | MTE **30** · CWS 30 (quiz, assignment) · ETE 40 |
| Question format | unknown. No PYQ yet. The ECE2108 MTE the same week was **A: 2+2+3 · B: 3 × 5 · C: 1 × 8**, and `10` uses that |

**MTE syllabus = L1–L24.** This pack covers **L1–L19** (everything uploaded).
**⚠ Not covered, because no deck has arrived:** L20 cost concepts and elements of cost · L21 life cycle cost and
project financing · L22–24 **break-even analysis (3 lectures of numericals)**. Upload those decks and they
get added. Break-even alone is likely worth a full long question.

---

## The path

```
 [01] Economics basics ──────── scarcity, micro/macro, economic systems, PPC,
  │                              efficiency, demand & supply theory           (L1–3)
  ▼
 [02] Equilibrium numericals ── Qd = Qs, then add a tax or a subsidy           (L4–5)  ◄ NUMERICAL
  │
  ▼
 [03] Elasticity ────────────── price / income / cross / promotional          (L6–7)  ◄ NUMERICAL
  │
  ▼
 [04] Economic decision making  process, key elements, decision types, EAC   (L8–9)
  │
  ▼
 [05] Types of estimates ────── ROM, budget, definitive, parametric,
  │                              analogous, bottom-up                          (L10–12) ◄ NUMERICAL (easy)
  ▼
 [06] EOQ ───────────────────── √(2DS/H), orders/yr, cycle time, ROP          (L13)   ◄ NUMERICAL
  │
  ▼
 [07] Payback + ROR ─────────── even / uneven cash flow                        (L14)   ◄ NUMERICAL
  │
  ▼
 [08] TVM + NPV ─────────────── F = P(1+i)ⁿ, annuity PV, NPV decisions         (L15–17) ◄ NUMERICAL
  │
  ▼
 [09] IRR ───────────────────── NPV = 0, trial rates, interpolation            (L18–19) ◄ NUMERICAL
  │
  ▼
 [10] Mock MTE ──────────────── 30 marks, answers at the bottom
```

**Priority if time is short:** 08 → 06 → 07 → 09 → 02 → 03 (all numerical, which is where the marks are) → 05 →
04 → 01. The last three are theory and can be answered by writing the definitions and points.

**Calculator:** every numerical here needs powers such as 1.1⁵. Practise `(1 + i)^n` and the annuity factor
`(1 − (1+i)^−n) / i` on your own calculator before the exam.

---

## Every professor-set question → where it is answered

| Source | Question (short) | File |
|---|---|---|
| L1 | Case: solar farm / high-speed rail, economics vs engineering economics view | 01 |
| L2 | Technical vs economic efficiency | 01 |
| L4-5 P1 | Xd = ½(5−P), Xs = 2P−3; tax ₹6/5 | 02 |
| L4-5 P2 | P = 5−2X, P = ½(X+5); subsidy ₹5/2 | 02 |
| L4-5 P3 | Qd = 200−10P, Qs = 50+15P → Qs′ = 100+15P | 02 |
| L4-5 P4 | 3Q+4P = 24, P = ¼Q+3; tax ₹1/3 | 02 |
| L7 P1 | Price ₹50→48, demand 100→110: Eₚ | 03 |
| L7 P2 | Income ₹100→200, qty 25→30: Eᵧ | 03 |
| L7 P3 | Advertising ₹6000→12000, qty 8000→10000: Eₐ | 03 |
| L8-9 | Cloud server: on-demand vs reserved (EAC) **⚠ slide error** | 04 |
| L8-9 | Petrol car vs electric car, 8-year total cost | 04 |
| L8-9 | Audi vs BMW: rational decision steps | 04 |
| L10-12 | ROM: office building, software duration, gadget, web app | 05 |
| L10-12 | Budget estimate: building, software product | 05 |
| L10-12 | Parametric: house, steel shafts, PCB assembly | 05 |
| L10-12 | Analogous: CMS 10,000 → 15,000 lines | 05 |
| L10-12 | Bottom-up: CMS task list + 20% contingency | 05 |
| L13 | Car dealer: D = 5000, S = 15000, H = 500 | 06 |
| L13 | 16000 units, ₹2, S = ₹45, carrying 10%: EOQ + cycle time | 06 |
| L13 sheet Q1 | Batteries: current cost, EOQ, orders/yr | 06 |
| L13 sheet Q2 | Indian Telecom: EOQ, orders, reorder point | 06 |
| L13 sheet Q3 | 20 units/yr, lead time 3 months: EOQ, ROP | 06 |
| L13 sheet Q4 | Bicycle tyres: EOQ, orders, total cost | 06 |
| L14 | Payback: $10500 / $2500 · beverage equipment · $200,000 uneven · ₹50000 uneven | 07 |
| L14 | ROR of the $10500 project · lighting retrofit (notes) | 07 |
| L15 | ₹75,000 today vs ₹1,00,000 in 5 years · $1000 in 5 years at 10% | 08 |
| L16-17 | $2000 project, $100 ×3 + $2500 | 08 |
| L16-17 | Project A vs B, $10,000, 10% **⚠ slide error** | 08 |
| L16-17 | Standard vs high-efficiency furnace (10% and 30%) | 08 |
| L16-17 | Project A vs B by payback AND NPV (−1200 …) | 08 |
| L16-17 | Real estate ₹200000, ₹30000/yr, 12% | 08 |
| Notes | ₹150000, ₹50000 × 5, 10% | 08 |
| L18-19 | Machine −$50,000, $15,000 × 5 at 10/15/20% + IRR | 09 |
| L18-19 | Interpolation demo: +200 at 10%, −100 at 15% | 09 |
| L18-19 | Equipment ₹500000, ₹160000 × 4, salvage ₹50000 **⚠ slide error** | 09 |

---

## How to use each file

When you hit a **Q ▸**, write a one-line guess or first step on paper **before** reading on. A wrong
guess still makes the answer stick better than reading it cold. Every file ends with a **Self-test**, and its
answers are at the very bottom. Whatever you miss there is what you revise last.

**How numericals are marked:** (1) the formula written out, (2) the substitution shown, (3) the answer
with units, (4) a **one-line decision** (accept/reject, which option). Leaving out the decision line is the
easiest way to lose a mark.
