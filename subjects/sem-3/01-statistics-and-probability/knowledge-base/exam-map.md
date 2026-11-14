# MAS2001 — Exam map (marks-aiming)

> The marks-aiming map: per topic → exam frequency, recurring question types + marks, MTE/ETE split,
> instructor emphasis. Built from `../exam-pack/`. **Status (2026-11-15):** official ETE blueprint +
> 2026 MTE paper and key + Assignments 1, 2, 4, 5 + three LMS decks in hand. No past ETE paper yet.

## Exam structure
- MTE (30 marks, 1.5 h; 2026 paper filed) + ETE (80 marks on the blueprint below). How each scales into the final grade: not stated.

## Evidence: official blueprint, July–Nov 2026 (`../exam-pack/BLUEPRINT-MAS2001-July-Nov-2026.md`), added 2026-11-13

Question counts and weightage by content row are **`settled`** (printed). Marks per part are **derived** (A = 2, B = 6, C = 8, D = 8; unique solution). The paper is 80 marks.

| Blueprint row | KB unit | A | B | C | D | Marks | Share |
|---|---|---|---|---|---|---|---|
| 1 Probability + random variables, Chebyshev | U1 | 2 | 1 | — | — | 10 | 12.5% |
| 2 Distributions + sampling, standard error, **CLT** | U2 (+ CLT/SE from U1/U4) | 3 | 1 | 1 | — | 20 | 25% |
| 3 **Estimation**: MoM, MLE, Bayesian intro, CI for mean | U3 | 1 | 2 | 1 | — | **22** | **27.5%** |
| 4 Hypothesis-testing concepts, Type I/II | U4 (first half) | 2 | 1 | — | — | 10 | 12.5% |
| 5 t, F, chi-square, **ANOVA** | U4 (second half) | 2 | 1 | — | 1 | 18 | 22.5% |

**What it changes:**
- **Estimation (U3) is the single heaviest row (22).** The old inferred map had it "Medium". Promote MoM/MLE derivations + CI for mean to top priority alongside distributions.
- **The only 8-mark Part D sits in row 5 (significance tests)**, so expect one long t/F/chi-square/ANOVA problem. ANOVA moves up from "lower / short".
- The two 8-mark Part C items are in rows 2 and 3 (a distribution/CLT problem and an estimation problem).
- The blueprint places **CLT and standard error with the distributions** (row 2), not with probability theory or testing as `course-info.md` listed them. Teach them where the paper tests them.
- Rows 1 and 4 have only short items (A + one B). Definitions and quick numericals are enough there.

## Evidence: MTE 2026 paper + Assignments 1, 2, 4, 5 + LMS slides (added 2026-11-15)

Filed in `../exam-pack/` (index in its README). **The MTE is 30 marks** (A 4 × 2, B 3 + 3 × 4, C 4 + 3), so the 80-mark blueprint above is the **ETE**.

| Blueprint row | MTE 2026 items | Assignment items | Slides |
|---|---|---|---|
| 1 | A1, B1 (Chebyshev, bound 16/3), B2 (pdf constants) | A1: 10 MCQ, 6 SA, 4 LA, 4 application | — |
| 2 | A2, A4 (Poisson), B3 (binomial), B4 (uniform), C1(a) (normal + binomial) | A2: 12 MCQ, 8 B, 4 C, 4 D | SE + CLT deck: 4 worked examples |
| 3 | A3 (sufficient), C1(b) (unbiased) | A4 B1–B5 (CI for mean, z and t) | MLE/Bayes deck: Ex. 11–15 |
| 4 | — | A4 MCQ 1–7, C1–C3 (α, β computations) | ppt 8: 3 worked α/β examples |
| 5 | — | A5: 10 A, 6 B, 6 C, 4 D (t, paired t, F, χ² independence, one-way ANOVA) | — |

**Question forms confirmed.** Row 3 is examined as MLE/MoM derivations (slides), unbiasedness checks (MTE C1(b)) and CI for mean with given table values (A4). Row 4's long form is α/β for a stated critical region (A4 C1–C3, ppt 8). Row 5's Part D form in A5 is a raw-data test: F (two mines), t at two levels, χ² 2 × 2, one-way ANOVA with unequal groups. ANOVA is **one-way only** (A5 topic list). Bayesian is the slides' discrete-prior posterior (Ex. 15). Chi-square is the **test of independence** only (no goodness-of-fit item in any assignment).

**Answer-key slips found** (11; recomputed by `../study-pack-v12/src/verify.py`): A5 C6 table value 19.41 = F(12, 2), should be F(2, 12) = 3.89 (decision flips); A5 D1 5.19 = F(4, 5), should be F(4, 4) = 6.39; A5 D2 CI; A5 A4, A10 options; A2 B5; A2 C2; A1 LA2 table/key mismatch; A1 LA3; A1 App 3 rounding. Listed with corrections in the study pack's START-HERE.

Still missing: Assignment 3 (probably the estimation assignment), any past ETE paper.

## Provisional priority (INFERRED, superseded where the blueprint above speaks)
- **High (expected heavy):** Normal distribution + standardization; CIs and one/two-mean tests
  (numerical, high-mark); applying CLT; computing E/Var from a given distribution.
- **Medium:** Binomial/Poisson/Exponential numericals; MLE/MoM derivations; chi-square test.
- **Lower / short:** axioms & definitions, Chebyshev bound, ANOVA setup (often short or theory).

## To-verify (route to `00-map.md` register)
- `[opened 2026-06-17]` **No MAS2001 PYQ/PPT ingested** — download MTE+ETE papers + course PPTs into
  `../exam-pack/`, then rebuild this map from real evidence (topic frequency, exact question types,
  marks). *Resolve by:* manual drop from MUJ Central/Stella/Toppers (`exam-resources.md`).
- `[opened 2026-06-17]` **MTE/ETE mark weightage** unverified. `[2026-11-13]` Partly closed: the blueprint gives the per-row split of an 80-mark paper. Which exam it is (MTE/ETE) and how it scales are still open.
