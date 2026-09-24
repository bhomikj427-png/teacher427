# 05 — Types of estimates (L10–L12)

**Theory plus one-line numericals.** Expect "explain X estimate with an example" or "differentiate ROM and
definitive". Each type has a one-line formula, so learn the formula with the definition.

## Map

```
 estimate = predict cost / time / resources BEFORE the project happens
                                                           accuracy
 early, little info ─► ROM (ballpark) ─────────────────  −50% … +100%
                   └─► Budget estimate (preliminary funding)
 late, full design ──► Definitive ─────────────────────  −5% … +10%
 TECHNIQUES
   ├─ Parametric  = rate per unit × quantity (statistical relation)
   ├─ Analogous   = past project × (new size / old size)   ("top-down")
   └─ Bottom-up   = Σ every small task (+ contingency)      most accurate, slowest
```

---

## 1. ROM (Rough Order of Magnitude) estimate `[L10-12]`

**Q ▸** "How long from Delhi to Mumbai?" You answer "1–2 hours by flight, 20–25 by train" without checking
a schedule. What kind of estimate is that?

A **ROM** (ballpark) estimate: a very high-level, deliberately imprecise estimate of cost, time or resources, made
in the **earliest planning stage** from experience and limited information. **Accuracy ≈ −50% to +100%**
(the slide's range).

Key points (write 4–5): **approximate** (often given as a range) · **limited detail** (it ignores the full scope and risks) ·
**quick** feasibility check · useful for **communicating** a first idea to stakeholders · a **basis for further planning** ·
**subject to change**, so it is replaced by better estimates later and is never the sole basis for critical decisions.

**The ROM numericals (the method is to take the average of the range, then multiply):**

| Deck problem | Working | ROM |
|---|---|---|
| Office building, ₹150–200/sq ft, 10,000 sq ft | (150+200)/2 = 175 × 10,000 | **₹17,50,000** |
| Software project, similar ones took 6–9 months | (6+9)/2 | **7.5 months** |
| Gadget, ₹50–70/unit, 5,000 units | 60 × 5,000 | **₹3,00,000** |
| College web app: dev 25,000 + hosting 2,000 + tools 2,000 | 29,000 | **~₹30,000**, range 15,000–60,000 |

(The web-app range is −50% / +100% of 30,000.)

## 2. Budget estimate

More refined than ROM but still based on limited information. It is a **preliminary** assessment of the money needed,
made **before detailed planning**, and it is used to judge feasibility and **set initial funding limits**.

| Deck problem | Working | Budget |
|---|---|---|
| Building: materials 2,00,000 + labour 3,00,000 + equipment 1,00,000 + overhead 10% of direct | direct = 6,00,000. Overhead = 60,000 | **₹6,60,000** |
| Software: R&D 1,50,000 + testing 80,000 + marketing 50,000 + misc 20,000 | sum | **₹3,00,000** |

## 3. Definitive estimate

The **most accurate** estimate (**−5% to +10%**), produced **late**, once the scope, drawings and specifications are
complete. It uses a comprehensive cost breakdown (materials, labour, equipment, overhead, contingency).

Characteristics (list for 5 marks): detailed scope · comprehensive plans and specs · accurate quantities · accurate
cost breakdown · reliable data (current prices, history) · few, documented assumptions · low risk · high accuracy ·
used for **approval and funding** · final planning stage.
Downsides: costly and slow to prepare, and unsuitable when the scope is still changing.
Deck examples: an ERP implementation and an e-commerce app, both going scope → WBS → resources → cost → risk →
schedule → QA → client review → final estimate.

**ROM vs definitive: the likely "differentiate" question**

| | ROM | Definitive |
|---|---|---|
| When | earliest stage | final planning stage |
| Information | minimal | complete design and specs |
| Accuracy | −50% … +100% | −5% … +10% |
| Effort | minutes, from experience | large (detailed breakdown) |
| Used for | go/no-go, first idea | funding approval, contracts |

## 4. Parametric estimate

**Q ▸** Houses around you cost ₹200/sq ft to build. Yours is 2,000 sq ft. Estimate it.

Cost = rate × quantity = 200 × 2,000 = **₹4,00,000**. That is **parametric** estimating: a **statistical relationship**
between a parameter (sq ft, kg, components) and cost/time, taken from historical data, then applied to the new
project's parameter value. It is quick, but it assumes the relationship still holds, so it is weak for unusual projects.

| Deck problem | Parameter | Working | Estimate |
|---|---|---|---|
| Steel shafts: ₹180/kg, 250 shafts × 2.5 kg | weight | 625 kg × 180 | **₹1,12,500** |
| PCBs: ₹35 per component, 1,200 PCBs × 80 components | components | 96,000 × 35 | **₹33,60,000** |

## 5. Analogous estimate `[L10-12]`

> Previous CMS: 10,000 lines of code, 1,000 person-hours. New CMS: 15,000 lines. Estimate the effort.

**Q ▸** Set up the ratio.

**Analogous (top-down)** estimating scales a **similar past project**:
```
 Estimated effort = previous effort × (new size / previous size)
                  = 1,000 × 15,000 / 10,000 = 1,500 person-hours
```
Process: identify a reference project → gather its data → analyse similarities and differences → apply
**adjustment factors** (e.g. + % for stricter regulation) → calculate. It is rough, and its accuracy depends on how similar the
projects really are.

**Parametric vs analogous:** parametric uses a **statistical rate from many past data points** (₹/kg). Analogous
scales **one comparable project** with judgment.

## 6. Bottom-up estimate `[L10-12]`

> CMS tasks: requirements 40 h, database 20, UI 30, backend 300, frontend 250, testing 80, deployment 20.
> Add a 20% contingency.

**Q ▸** Total, then contingency.

Σ = 40 + 20 + 30 + 300 + 250 + 80 + 20 = **740 hours** → × 1.20 = **888 hours**

**Bottom-up**: break the project into the smallest tasks (a WBS), estimate each, and **aggregate**. It is the **most accurate**
technique and the **most time-consuming**. Workflow: task identification → task estimation → aggregation → **contingency** →
validation with stakeholders → documentation.

---

## Self-test

1. Give the accuracy ranges of ROM and definitive estimates (as on the slides).
2. A bridge costs ₹8 crore per km historically. The new one is 2.5 km. Name the technique and give the estimate.
3. A past 20-storey tower took 30 months. Estimate a 30-storey one by analogy.
4. Tasks of 12, 30 and 18 days plus a 15% contingency. Name the technique and give the estimate.
5. Why should a ROM estimate never be the sole basis for a critical decision?

---

## Answers

1. ROM −50% to +100%. Definitive −5% to +10%.
2. Parametric: 8 × 2.5 = **₹20 crore**.
3. Analogous: 30 × 30/20 = **45 months** (then adjust for differences).
4. Bottom-up: 60 × 1.15 = **69 days**.
5. It is based on minimal information and assumptions and ignores the full scope and risks, so the actual figure can be twice the estimate.
