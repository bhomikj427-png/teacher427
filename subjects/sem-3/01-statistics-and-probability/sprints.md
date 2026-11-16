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
| S1 | **01 + 02** probability basics; random variables (PMF, PDF, CDF) | old 01, 02 · KB `01` | `01-…`, `02-…` rebuilt (a/b if > 13 steps), figures in `src/figures.py`, numbers in `src/verify.py` | protocol 6–12 hold | ✓ 2026-11-16 (S1 + S1b: 01, 02a, 02b) |
| S2 | **03 + 08** expectation, variance, Chebyshev; estimator properties | old 03, 08 · KB `01`, `03` | `03-…`, `08-…` rebuilt | same | ✓ 2026-11-16 (S2 + S2b: 03a, 03b, 08) |
| S3 | **09** method of moments and MLE (rank 1; the slides' four MLE examples) | old 09 · KB `03` · slides MLE-and-Bayesian | `09a-method-of-moments.md`, `09b-mle.md` (split expected) | same; every slide MLE example re-derived in verify | ✓ 2026-11-17 (09a 5 steps, 09b 11 steps; all four slide MLE examples re-derived numerically) |
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
| ~~Textbook facts checked in S3 session 1 are only in the hand-off: write them into KB 03 + CHANGELOG~~ | review 2026-11-16 | **closed S3** (KB 03 "MLE and MoM properties", CHANGELOG, `sources.md` G&K entry) |
| ~~G&K ch. 15 ex. 20(b) prints θ, old 09 writes α~~ | review 2026-11-16 | **closed S3** (09a step 2 uses θ + note box; slip-table row) |
| Table-value count: brief.md:131 and S0 log say 36, KB 04 table has ≈ 32 (t(20) not printed); A5 A10 is a computed F ratio, not a table value: recount and correct | review 2026-11-16 | S9 |
| START-HERE:142 claims every page viewed; 04, 07, 09 rebuilt in S2b were not logged as viewed | review 2026-11-16 | S9 |
| HT slides 20 (binomial α = 1/9, β = 11/16) and 22 (power function, α = 0.001, (0.1)⁴, (0.1)^(θ+1)) not used in v1.2 and not in `verify.py`: add checks + steps | S0 | S6 |
| v1.2 file 07's slide tags are off (ATM is p.11–12, impurity p.13–14, LED p.15–16, machine p.17–18, SE example p.5); SE/CLT p.14 prints z = −0.4 (true −0.94): note box | S0 | S5 |
| A5 C2(b) needs t(20) = 2.086 (not printed in the assignment): print it as the pack's value | S0 | S7 |
| ~~New numbers in v1.3 01 and 02a not yet in `verify.py`~~ | S1 | **closed S1b** (`# ==== v1.3 S1` block, 558 checks pass) |
| ~~START-HERE slip table: A1 LA 2 row~~ | S1 | **closed S1b** (row rewritten) |
| ~~02a's MTE A1 line says option (a) "is in 03b"~~ | S1b | **closed S2** (03 split; MTE A1(a) is 03b step 4) |
| ~~Old v1.2 `# ---- 03` / `# ---- 08` checks in `verify.py`~~ | S2 | **closed S2b** (pruned; 665 checks pass) |
| Pack `README.md` still says "format v1.2": update when all files are v1.3 | S1b | S9 |

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
| 8 | 08's running example is the die as a known population (36 two-throw / 216 three-throw samples enumerated) instead of the brief's bare X₁, X₂, X₃: makes "average over all samples" concrete for a novice; MTE C1(b) still asked as printed | S2 | open |
| 9 | 03b SA 6 is solved with indicator sums (03b steps 2–3) rather than the binomial np, npq, so 03b needs nothing from 04 | S2 | open |
| 10 | S2 overran: S2b (build + view + cleanup) counts inside S2, like S1b | S2 | open |
| 11 | 09a uses pack-made data (bus waits 2, 5, 1, 4; U(0, θ) samples 1, 1, 10 and 1, 2, 9; U(a, b) data 8, 9, 11, 12) to make G&K 20(b) and 21 concrete; the G&K questions are still quoted as printed. Step 3 ("impossible estimate") is a pack addition, answered by 09b Check 9 (MLE of U(0, θ) = largest value) | S3 | open |
| 12 | 09b opens on a coin (H, H, T) and works the Bernoulli MLE as the five-step demo (step 3) before the slide examples; the restarted S3 wrote the KB facts from S3 session 1's page reading (2026-11-16) without re-reading the book | S3 | open |

## Current hand-off

```
Sprint: S3 — 09a + 09b — done (2026-11-17, auto.py session 8; session 7 = commit 7a17c26 crashed on the
  usage limit after logging its start, nothing else lost)
Written: KB 03-estimation.md "MLE and MoM properties — G&K ch. 15" + CHANGELOG line + sources.md G&K entry.
  content/09a-method-of-moments.md — v1.3, 5 steps (1 population vs sample moments (die), 2 one parameter
  = G&K 20(b) with θ (bus waits 2, 5, 1, 4), 3 impossible estimate U(0, θ), 4 two parameters = G&K 21,
  5 new density = G&K 23(b)(i) 0.3474 + MoM-efficiency note).
  content/09b-mle.md — v1.3, 11 steps (1 coin likelihood, 2 log keeps the peak, 3 five steps (Bernoulli),
  4 Poisson Ex. 12, 5 rats Ex. 13 16.2, 6 normal μ Ex. 11a, 7 normal σ² Ex. 11b + slide note, 8 Ex. 14
  0.3970 + slide note, 9 second derivative, 10 properties (G&K Thms 15.11–15.17, invariance 0.0617),
  11 MoM vs MLE = G&K 23(b)(ii) 0.7279).
  figures.py: mom_match, mom_uniform, coin_like, coin_L_lnL, rats_loglik, ex14_loglik (v1.2
  likelihood_curve deleted). verify.py: block "# ==== v1.3 S3" (each MLE found by numeric maximisation);
  old v1.2 "# ---- 09" pack checks pruned.
  Old 09 md/html/pdf removed. START-HERE: rank 1 row, Unit 3 map, file table (09a, 09b), stuck tip,
  prerequisite line, slip table (Ex. 14 → 09b §8; new rows Ex. 11 and G&K 20(b)), check count 741.
  Cross-refs re-pointed: 08 (lines 9, 264, 269), 10 (header, lines 22, 62, 115). Mock 17 names no file.
Verified this sprint: numbers: verify.py 741 checks, 0 failures, 15 key differences (unchanged set).
  Build 00 08 09a 09b 10: no OVERLAP; combined PDF 175 pp. Sheets viewed: 09a-1, 09b-2 (no fixes).
  G&K facts: from S3 session 1's page reading (2026-11-16), not re-read (assumption 12).
Open (carried): none for S3. Backlog unchanged otherwise (S5, S6, S7, S9 rows).
Decisions made: 09 split into 09a (MoM) / 09b (MLE); later files cite "09a step N", "09b step N".
Assumptions to review: 11, 12 (new, in the persistent section).
Next sprint: S4 — 04 + 05 (brief plans 04 → 04a/04b, so 3 files). First action: log the S4 start,
  then read brief §2 rows 04/05 (lines 109–110) and §4 rows 04/05 (lines 151–152).
Read at start: this hand-off · ../../../study-pack-sprint-protocol.md · spec §5 (study-pack-format.md
  lines 68–95) · brief lines 109–110, 151–152 · content/04-binomial-poisson.md (213 lines),
  05-uniform-exponential.md (238 lines) · KB 02 by section · 09a lines 1–20 (format model) ·
  Assignment 2 only for questions the brief rows cite. Do not re-read src/build.py: use the how-to below.
Build/view how-to (works under auto.py; scratch scripts in the auto.py temp folder, rewrite if gone):
  from study-pack-v12/ run `python -I <temp>/run_build.py verify.py` and
  `python -I <temp>/run_build.py build.py <prefixes>` (sets PYTHONIOENCODING=utf8, prints OVERLAP/FAIL
  lines); `python -I <temp>/sheets.py <pdf-stem> ...` renders 4 pages per PNG at 55 dpi into <temp>/sheets.
  Progress-log append: write the line to <temp>/line.txt, run `python -I <temp>/logline.py <temp>/line.txt`.
  New figures: functions in figures.py's v1.3 block (before ALL), built on FL (tools/figlib.py).
Split reminder for S4: when 04 splits, update START-HERE rank 10 row, file table, Unit 2 map, slip rows
  naming 04, and grep "04 §\|file 04\|04-binomial" across content (03b, 05, 06, 12 and the mock cite 04).
```
