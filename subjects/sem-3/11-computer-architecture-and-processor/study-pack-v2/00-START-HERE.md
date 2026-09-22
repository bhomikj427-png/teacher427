# Computer Architecture & Processor ECE2108 — Study Pack v2

Built from the professor's **Assignment 1** (20 Q, 200 marks) and **Assignment 2** (15 Q, 150 marks).
Every file is anchored to specific assignment questions. v1 (`../study-pack/`) stays as the
topic-organized reference; v2 is organized around **what this professor actually asks**.

> **⭐ Superseded by v3 (2026-09-23):** `../study-pack-v3/` is the live pack — same assignment anchoring,
> but every concept is introduced by the real question it answers, and it covers **U3**, which this pack
> omits entirely because neither assignment tests it. U3 is still on the mid-term. Use v3.

---

## The textbook ("Mano")

**"Mano" = M. Morris Mano, *Computer System Architecture*, 3rd edition, Pearson (2007).** Reference 1 on
your course hand-out; every "Ref: M. M. Mano" on the professor's slides means this book. Searching
"Mano" alone returns nothing — search the full title with the author's name.

| Mano chapter | Your unit |
|---|---|
| 4 — Register Transfer and Microoperations | U1 |
| 5 — Basic Computer Organization and Design | U2 |
| 7 — Microprogrammed Control | U3 |
| 8 — Central Processing Unit (program control) | U3 |
| 9 — Pipeline and Vector Processing | U4 |
| 11 — Input-Output Organization · 12 — Memory Organization | U5, U6 (after the MTE) |

The professor's decks are built from chapters 4, 5 and 9, and Assignment 2 copies its end-of-chapter
problems. Get it from the college library or as the Pearson India paperback. This pack and the
knowledge base already contain what you need from it; the book is for the extra end-of-chapter
problems.

---

## What the assignments changed

| | v1 | **v2** |
|---|---|---|
| Question forms | inference | **evidence** — the professor's own questions |
| Anchor | textbook topic order | assignment question clusters |
| ALSU select codes | ⚠ wrong ordering (fixed in v1 on 2026-09-15) | professor's slide table |

**Three findings worth knowing before you start:**

1. **12 of Assignment 2's 15 questions are verbatim Mano end-of-chapter problems** (5-1, 5-3, 5-4, 5-6,
   5-9, 5-12, 5-20, 5-21, 9-3, 9-5, 9-10, 9-11). Mano's exercises are this professor's question bank.
2. **The ALSU table is not the arithmetic-circuit table.** The professor's ALSU slide puts
   *transfer A* at `00000` and *add with carry* at `00011`; the arithmetic-circuit slide puts
   *add with carry* at `001`. v1 had used the wrong one for the ALSU. File 05.
3. **Digital-Electronics circuits are examinable here.** A1 Q7 is 24 marks of flip-flops, decoders,
   MUXes and registers drawn from gates. File 02.

---

## Assignment 2 — answer policy

A2 is due **16-09-2026, 16:30**. In files 06–09, every A2 question has the **method** and a fully
worked **twin** — same method, different numbers. A2's own answer key goes in after the deadline.
Send your A2 answers and they get marked.

A1 is submitted, so its answers are complete.

---

## The learning path

```
   [01] Foundations                     A1 Q1–6, Q20    definitions, generations,
        |                                                types, von Neumann/Harvard, RISC/CISC
        v
   [02] Digital building blocks         A1 Q7           D FF, decoder, MUX, registers
        |
        v
   [03] RTL + common bus          *     A1 Q10–14       THE GATE: everything after is RTL
        |
        v
   [04] Microoperations + signed        A1 Q8–9,        2's complement, adder-subtractor,
        arithmetic                      Q15–16, Q18–19  register traces, shifts
        |
        v
   [05] ALSU                      *     A1 Q17          16 marks, the professor's slide question
        |
        v
   [06] BC instruction format +         A2 Q1–4         bit sizing, S₂S₁S₀ ↔ transfer, hex decode
        bus control
        |
        v
   [07] Timing + execution traces *     A2 Q5–8         SC timing, register traces, fetch design
        |
        v
   [08] Control-gate derivation   *     A2 Q9–10        JK inputs from RTL, PC's LD/INR/CLR
        |
        v
   [09] Pipelining numericals           A2 Q11–15       register tables, k+n−1, speedup,
        + branching                                      branch hardware, FI-DA-FO-EX
        |
        v
   [10] Mock paper (timed)              all
```

`*` = highest marks per hour. Files 01–05 are U1; 06–08 are U2; 09 is U4. **File 09 does not depend on
06–08** — do it any time after 03.

**If you have one evening:** 05 → 07 → 08 → 09. Those carry the design and numerical marks.

---

## File shape

```
## Map         where the topic sits (3–6 nodes)
## Attempt     the assignment's questions — no answers
## Learn       the compact content needed
## Worked      full solutions (A1) / twins (A2)
## Traps
## Self-test   new questions
## Answers     at the bottom
```

**Write an attempt before scrolling.** A wrong attempt you then correct is retained better than a
correct answer you only read.

Mark each self-test item:

- **clean** → revisit in 3 days
- **with struggle** → revisit tomorrow
- **missed** → redo today, again tomorrow

---

## Files

| File | Assignment questions | Unit | Marks in assignment |
|---|---|---|---|
| `01-foundations.md` | A1 Q1, Q2, Q3, Q4, Q5, Q6, Q20 | U1 | 76 / 200 |
| `02-digital-building-blocks.md` | A1 Q7 | DE → U1 | 24 / 200 |
| `03-rtl-and-common-bus.md` | A1 Q10, Q11, Q12, Q13, Q14 | U1 | 48 / 200 |
| `04-microoperations-and-signed-arithmetic.md` | A1 Q8, Q9, Q15, Q16, Q18, Q19 | U1 | 36 / 200 |
| `05-alsu.md` | A1 Q17 | U1 | 16 / 200 |
| `06-bc-format-and-bus-control.md` | A2 Q1, Q2, Q3, Q4 | U2 | 40 / 150 |
| `07-timing-and-execution-traces.md` | A2 Q5, Q6, Q7, Q8 | U2 | 40 / 150 |
| `08-control-gate-derivation.md` | A2 Q9, Q10 | U2 | 20 / 150 |
| `09-pipelining-numericals.md` | A2 Q11, Q12, Q13, Q14, Q15 | U4 | 50 / 150 |
| `10-mock-paper.md` | twins of both | all | 30-mark paper |

**Not in either assignment:** U3 (microprogrammed control, program control). It is still MTE scope —
use v1 files 07 and 08 for it.

---

## Source honesty

- **Scope and question forms:** the two assignments + the professor's decks (Tier 0).
- **Facts and answers:** the knowledge base (Mano 3e authority), re-verified this build against the
  **Mano Solutions Manual**. Every numerical answer was recomputed by script, not copied.
- **Two typos in the Solutions Manual**, not reproduced here: 5-12(c) prints AR = 7AC (correct: 9AC);
  5-21 prints `RT7` and `rB4 + (AC15)′` (correct: `RT2` and `rB4·AC15′`).
- **Generations-of-computers dates vary by author by a few years.** File 01 gives approximate ranges
  and says so.
- **A2 Q5's `C₇T₃`** is not a signal in the Basic Computer. Most likely `D₇T₃`. File 07.
