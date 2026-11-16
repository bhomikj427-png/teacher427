# MAS2001 Statistics & Probability — Build Sprints (v1.3)

> **ETE: 2026-11-19** (learner, 2026-11-16). This plan runs first. Files land in priority order, so a run
> cut short by the exam leaves the highest-value files done; the learner studies the v1.2 file for any topic not yet rebuilt.
>
> **Learner rules:** one sprint = one session, fully finished, ending with the hand-off below.
> **Budget: 9–10 sprints per subject, 12 fine, more only if seriously necessary** (2026-11-16).
> This plan uses **10** (S0–S9).
>
> **Goal:** files 01–16 of `study-pack-v12/` rebuilt to `study-pack-format.md` **v1.3** (the v1.2 files
> are too compressed: ideas merged, symbols named but not explained). The KB is `stage-2✓` (all four
> units), so no research sprints; a missing fact goes into the KB inside the sprint that finds it.
> Written 2026-11-16.
>
> **Steps for every sprint: `../../../study-pack-sprint-protocol.md`.** This file holds only the
> table, hand-off, backlog and subject notes. Run unattended: `python auto.py run sem-3/01-statistics-and-probability`.

**Learner facts that shape every file** (progress log): novice in statistics; **dense notation
overloads** — introduce one symbol at a time, concrete before abstract, never a dense formula cold.
The concrete anchor (spec §6) matters more here than in any other pack.

**Order:** START-HERE priority, prerequisites first (spec §7.2). Rank 1 is 09 MoM/MLE, which needs
02 (PMF/PDF), 03 (expectation) and 08 (estimators); so S1–S2 build those, S3 builds 09.

**Every sprint's Inputs also include:** the protocol · `src/brief.md` sections for its files ·
`src/build.py` · the previous sprint's file header + symbol table. Until the first v1.3 file exists,
the format model is EDC `../03-electronic-devices-1/study-pack-v12/src/content/01b-fermi-level.md`
lines 1–100 (depth only; never copy its content).

---

## Sprint table

Old file = `study-pack-v12/src/content/<old>.md`. KB = `knowledge-base/` (+ `stage-2/`). Real questions
in `exam-pack/` (index: `exam-pack/README.md`): MTE 2026 paper + marking scheme, Assignments 1, 2, 4, 5,
the blueprint, three slide sets.

| # | Sprint | Inputs (beyond the standing list) | Outputs | Done when | Status |
|---|---|---|---|---|---|
| S0 | **Brief** | every file in `exam-pack/` · KB `00-map`, `exam-map` · old 00 (ranking) · `src/verify.py` (constants) | `src/brief.md`: slides transcribed (equations shown only as images viewed), question bank (every MTE/assignment/slide question → file + step), constants/tables used (z, t, χ², F values) checked against the KB, figure list per file | every assignment and MTE question is mapped; every table value the questions need is listed with its source | ✓ 2026-11-16 |
| S1 | **01 + 02** probability basics; random variables (PMF, PDF, CDF) | old 01, 02 · KB `01` | `01-…`, `02-…` rebuilt (a/b if > 13 steps), figures in `src/figures.py`, numbers in `src/verify.py` | protocol 6–12 hold | partial 2026-11-16 (01, 02a written; 02b + verify + build left) |
| S2 | **03 + 08** expectation, variance, Chebyshev; estimator properties | old 03, 08 · KB `01`, `03` | `03-…`, `08-…` rebuilt | same | |
| S3 | **09** method of moments and MLE (rank 1; the slides' four MLE examples) | old 09 · KB `03` · slides MLE-and-Bayesian | `09a-method-of-moments.md`, `09b-mle.md` (split expected) | same; every slide MLE example re-derived in verify | |
| S4 | **04 + 05** binomial and Poisson; uniform and exponential | old 04, 05 · KB `02` · Assignment 2 | `04-…`, `05-…` rebuilt | same | |
| S5 | **06 + 07** normal; standard error and CLT | old 06, 07 · KB `02`, `03` · slides SE-and-CLT | `06-…`, `07-…` rebuilt | same; the slides' four SE/CLT examples reproduced | |
| S6 | **11 + 12** confidence interval for the mean; hypotheses and errors (α, β) | old 11, 12 · KB `03`, `04` · Assignment 4 · slides 08 | `11-…`, `12-…` rebuilt | same; Assignment 4 answers compared | |
| S7 | **13 + 14** t-tests; F-test | old 13, 14 · KB `04` · Assignment 5 | `13-…`, `14-…` rebuilt | same | |
| S8 | **15 + 16** χ² independence; ANOVA (the paper's only Part D) | old 15, 16 · KB `04` · Assignment 5 | `15-…`, `16-…` rebuilt | same; Assignment 5 answers compared | |
| S9 | **10 + integration** Bayesian; mock paper re-pointed; START-HERE ranks, times, map, slip table | old 10, 17 · `00-START-HERE.md` · KB `03` | `10-…` rebuilt; 00 and 17 updated; full build | grep finds no reference to a removed file; `verify.py` passes; build prints no `OVERLAP` | |

**Learner check-ins are not sprints:** report misses on any delivered file whenever you like; the next
sprint reads them first.

---

## Verify backlog (persistent — items leave only when resolved, with the sprint that closed them)

| Item | Raised | Close in |
|---|---|---|
| HT slides 20 (binomial α = 1/9, β = 11/16) and 22 (power function, α = 0.001, (0.1)⁴, (0.1)^(θ+1)) not used in v1.2 and not in `verify.py`: add checks + steps | S0 | S6 |
| v1.2 file 07's slide tags are off (ATM is p.11–12, impurity p.13–14, LED p.15–16, machine p.17–18, SE example p.5); SE/CLT p.14 prints z = −0.4 (true −0.94): note box | S0 | S5 |
| A5 C2(b) needs t(20) = 2.086 (not printed in the assignment): print it as the pack's value | S0 | S7 |
| New numbers in v1.3 01 and 02a (every Check, Self-test, step answer: dice counts 11/36, 1/2, 1/12, 1/18; bolts 0.968, 0.6074; Self-test 7 = 0.1538; 02a Check 5(b) 0.3028, ST 2–7) not yet in `verify.py` | S1 | S1 (continuation) |
| START-HERE slip table: A1 LA 2 row must say the printed row is k, 2k, 2k, 3k, 3k (differs at x = 0, 1, 3) and key (ii) 91/100 = G&K's 19/100 swapped (G&K page index 241 checked) | S1 | S1 (continuation) |

## Assumptions to review (persistent — the learner confirms or overrules)

| # | Assumption | Made in | Status |
|---|---|---|---|
| 1 | Build order = START-HERE priority with prerequisites first (spec v1.3 §7.2) | plan | open |
| 2 | One `figures.py` and one `verify.py` for the pack (as in v1.2) rather than one per unit; new figures use `tools/figlib.py` | plan | open |
| 3 | 09 splits into 09a (MoM) / 09b (MLE); other splits decided by step count | plan | open |
| 4 | Expected further splits from the brief's idea count: 02a/02b (discrete/continuous), 03a/03b (E, Var / rules + Chebyshev), 04a/04b (binomial/Poisson), 12a/12b (concepts / α-β computation); they fit S1, S2, S4, S6 as 3 files each, no new sprints | S0 | open |
| 5 | Table values live in KB `04-hypothesis-testing.md` (one section for z, t, χ², F) rather than split across units | S0 | open |
| 6 | 01's Bayes steps (11–12) use the bolts factory, not the dice: no natural "cause" on a dice grid. 02a teaches the LA 2 question on G&K's row (P(X=0) = 0), with a note box on the printed row | S1 | open |
| 7 | S1 overran one session: the continuation (02b + verify + build) is S1b, still inside the 10-sprint budget count as part of S1 | S1 | open |

## Current hand-off

```
Sprint: S1 — 01 + 02a + 02b — partial (2026-11-16, auto.py; stopped at the context limit)
Written: content/01-probability-basics.md — v1.3, 12 steps (S, events, m/n, axioms, complement,
  addition, conditional = shrunk grid, P(A|B)=1, multiplication, independence, total prob., Bayes),
  two-dice running example, symbol table, Exam form, Traps, Self-test 7, Answers.
  content/02a-discrete-random-variables.md — v1.3, 9 steps (RV, discrete/continuous, PMF by
  counting, PMF rules, find k + note box, combinations, CDF staircase + reading table, probabilities
  from F + key note box, conditional with a PMF), 3-children running example.
  src/figures.py — 16 new v1.3 figures at the end (on figlib): 01 uses dice_space, dice_events,
  dice_complement, venn_union, dice_shrunk, venn_subset, aces_tree, bolt_tree, bolt_bayes; 02a uses
  family_map, boys_pmf, boys_cdf; 02b is to use cable_pdf, cable_cdf, power_tail, life_cond (already
  written + viewed). Overlap check on all 16: clean.
Verified this sprint: A1 LA 2 printed row read off the page image; G&K's version + answers
  (81/100, 19/100, 4/5; F row) read in the book (page index 241). Numbers in 01/02a: by hand only —
  NOT yet in verify.py (backlog row 4).
Open (carried): 02b not written · verify.py checks for 01/02a/02b · build not run (new files never
  rendered; check the `P(A \| B)` escape in 01's symbol table renders as "|") · old
  content/02-random-variables.md + its html/pdf still present (remove after 02b) · START-HERE rows for
  01/02a/02b + slip-table fix (backlog row 5) · cross-refs `grep -rn "02-random\|file 02\|02 step" src/content`.
Decisions made: 01 Bayes on bolts (Assumption 6). 02a step numbers are cited by later files as
  "02a step N". 02b plan: 6 steps — 1 probability = area (cable f = 6x(1−x), P(0.2 ≤ X ≤ 0.5) = 0.396,
  reading table f(0.2)=0.96, f(0.5)=1.5, f(0.8)=0.96), 2 checking a PDF (A1 SA 3(i)), 3 continuous CDF
  F = 3x² − 2x³ (F(0.2)=0.104, F(0.5)=0.5, F(0.8)=0.896; f = F′), 4 median (SA 3(ii); 4b³ − 6b² + 1 =
  (2b − 1)(2b² − 2b − 1), other roots (1 ± √3)/2 outside [0,1]), 5 tail (A1 SA 2, by parts, 5e⁻⁴ =
  0.0916, key 0.0915 truncated; reading f(3)=0.1226, f(12)=0.0244, f(20)=0.0028), 6 conditional
  (A1 LA 1: 0.1544, 0.4863; f(50)=0.01875, f(60)=0.01728, f(70)=0.01323). Checks from old 02 C5–C6.
Assumptions to review: 6 (01 Bayes on bolts; LA 2 on G&K's row), 7 (S1 continuation = S1b)
Next sprint: S1b (finish S1) — first action: write content/02b-continuous-random-variables.md from the
  plan above (old content/02 steps 5–6 + Answers for the worked numbers), then add a
  "# ==== v1.3 S1" block to verify.py before its final print (all 01/02a/02b numbers), run it,
  `python src/build.py 01 02a 02b`, view pages, remove old 02 files, update START-HERE + slip table.
Read at start: this hand-off · ../../../study-pack-sprint-protocol.md · content/02a (header + symbol
  table + step 9 only, for format) · old content/02 lines 159–280 · verify.py lines 1–40 and 350–370 ·
  00-START-HERE.md (rank / what-each-file / slip sections only)
```
