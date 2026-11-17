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
| S4 | **04 + 05** binomial and Poisson; uniform and exponential | old 04, 05 · KB `02` · Assignment 2 | `04-…`, `05-…` rebuilt | same | ✓ 2026-11-17 (04a 6 steps, 04b 6 steps, 05 10 steps; every A2/MTE item of 04/05 compared with its key) |
| S5 | **06 + 07** normal; standard error and CLT | old 06, 07 · KB `02`, `03` · slides SE-and-CLT | `06-…`, `07-…` rebuilt | same; the slides' four SE/CLT examples reproduced | ✓ 2026-11-17 (sessions 10 + 11: 06 11 steps, 07 12 steps; all four slide examples recomputed in verify) |
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
| ~~v1.2 file 07's slide tags are off; SE/CLT p.14 prints z = −0.4 (true −0.94): note box~~ | S0 | **closed S5** (07 re-tagged p.5, p.11–18; note box in 07 step 10; slip row) |
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
| 2 | One `figures.py` and one `verify.py` for the pack (as in v1.2) rather than one per unit; new figures use `tools/figlib.py` | plan | **confirmed 2026-11-17** (learner delegated; chosen as the lower-token option) |
| 3 | 09 splits into 09a (MoM) / 09b (MLE); other splits decided by step count | plan | open |
| 4 | Expected further splits from the brief's idea count: 02a/02b (discrete/continuous), 03a/03b (E, Var / rules + Chebyshev), 04a/04b (binomial/Poisson), 12a/12b (concepts / α-β computation); they fit S1, S2, S4, S6 as 3 files each, no new sprints | S0 | open |
| 5 | Table values live in KB `04-hypothesis-testing.md` (one section for z, t, χ², F) rather than split across units | S0 | open |
| 6 | 01's Bayes steps (11–12) use the bolts factory, not the dice: no natural "cause" on a dice grid. 02a teaches the LA 2 question on G&K's row (P(X=0) = 0), with a note box on the printed row | S1 | **confirmed 2026-11-17** (engine decision, learner delegated) |
| 7 | S1 overran one session: the continuation (02b + verify + build) is S1b, still inside the 10-sprint budget count as part of S1 | S1 | **confirmed 2026-11-17** (engine decision, learner delegated) |
| 8 | 08's running example is the die as a known population (36 two-throw / 216 three-throw samples enumerated) instead of the brief's bare X₁, X₂, X₃: makes "average over all samples" concrete for a novice; MTE C1(b) still asked as printed | S2 | open |
| 9 | 03b SA 6 is solved with indicator sums (03b steps 2–3) rather than the binomial np, npq, so 03b needs nothing from 04 | S2 | open |
| 10 | S2 overran: S2b (build + view + cleanup) counts inside S2, like S1b | S2 | **confirmed 2026-11-17** (engine decision, learner delegated) |
| 11 | 09a uses pack-made data (bus waits 2, 5, 1, 4; U(0, θ) samples 1, 1, 10 and 1, 2, 9; U(a, b) data 8, 9, 11, 12) to make G&K 20(b) and 21 concrete; the G&K questions are still quoted as printed. Step 3 ("impossible estimate") is a pack addition, answered by 09b Check 9 (MLE of U(0, θ) = largest value) | S3 | open |
| 12 | 09b opens on a coin (H, H, T) and works the Bernoulli MLE as the five-step demo (step 3) before the slide examples; the restarted S3 wrote the KB facts from S3 session 1's page reading (2026-11-16) without re-reading the book | S3 | open |
| 13 | 04a runs a fair die (p = ½) through steps 1–4 and MTE B3's irregular die (p = 5/8) in steps 5–6; 04a steps 1–3 and 04b step 6 (two desks, λ = 2.5 + 1.5) are pack-made Predicts/examples | S4 | open |
| 14 | A2 C3's key 0.8754 vs 0.8753 is treated as last-digit rounding (noted in 04b's answer, not added to the slip table); 05's split into a/b was not needed (10 steps) | S4 | open |
| 15 | S4's G&K facts were read on the PDF's text layer (OCR), not on page images; section and example numbers matched the old v1.2 citations | S4 | open |
| 16 | 07's three ball samples (acfh, bdej, cgij) are pack-made stand-ins for slide p.3's image samples; steps 3–4 (all 210 samples, SE = 0.2 by enumeration) and the note on drawing without replacement (0.2 vs σ/√n = 0.245) are pack additions | S5 | open |
| 17 | Session 10 crashed after writing 06; session 11 accepted its 06 after reading it in full, recomputing every number (one rounding fix: MTE C1(a) 0.0669) and agy's page check, without re-reading G&K §8.2 | S5 | open |

## Current hand-off

```
Sprint: S5 — 06 + 07 — done (2026-11-17, auto.py sessions 10 + 11; session 10 crashed on the usage
  limit after writing 06, committed in dd61029)
Written: content/06-normal.md — v1.3, 11 steps (session 10): 1 bell μ, σ (A2 MCQ 1), 2 Z (A2 MCQ 6),
  3 standardise, 4 φ table, 5 tails (A2 B4 i–ii), 6 between (A2 B3), 7 68–95–99.7 (A2 MCQ 11), 8 counts
  (A2 B4, D1), 9 normal inside binomial (MTE C1(a)), 10 inverse (A2 B6), 11 two conditions (A2 C2).
  Session 11 fixed step 9: 1 − 0.9772³ = 0.066852 ≈ 0.0669 (was 0.0668); marking-scheme note updated.
  content/07-sampling-se-clt.md — v1.3, 12 steps: 1 population/sample (10 balls), 2 parameter/statistic,
  3 sampling distribution (all 210 samples), 4 SE = its SD (0.2), 5 SE = σ/√n derived from 03b steps 1–3
  (slides p.5; A4 MCQ 8 in Check 5), 6 n × 4 halves SE, 7 CLT (G&K §8.10), 8 when (slides p.8; p.7/p.8
  note), 9 ATM p.11–12, 10 impurity p.13–14 (p.14 z slip note), 11 LED p.15–16, 12 machine p.17–18.
  figures.py: 06 norm_* (session 10); 07 ball_samples, ball_sampling, atm_tail, impur_band, led_tail,
  machine_two (session 10), se_n, clt_shapes (session 11); v1.2 se_shrink, clt_hist removed (normal_std,
  normal_rule, normal_inverse kept: 06 uses them). verify.py: block "# ==== v1.3 S5"; old "---- 06/07"
  pack checks pruned. START-HERE: rank 5/6 rows, prerequisite line, 07 file row, slip table (CLT p.14 →
  07 §10, p.7/p.8 n ≥ 30 row, MTE C1(a) row, A2 C2 → 06 §11), 983 checks / 18 key differences.
Verified this sprint: numbers: verify.py 983 checks, 0 failures, 18 key differences (new: 06 S11 μ and
  mark = A2 C2's slip checked again). G&K facts: KB 02 S5 bullets (§8.2, §8.10, §12.3; session 10, PDF
  text layer). Build 00 06 07: no OVERLAP; combined PDF 211 pp. agy page check of all 31 pages of 06 + 07:
  no problems; sheet 07-2 viewed by me: fixed se_n (arrow under the axis) and a note title with Greek.
Open (carried): none for S5. Backlog rows left for S6, S7, S9.
Decisions made: 06 and 07 kept whole (11 and 12 steps). Later files cite "06 step N", "07 step N":
  SE = 07 step 5, CLT = 07 step 7, its conditions = 07 step 8. 11 and 12 cite "file 07" only (still true).
Helpers: agy = visual check of 31 pages (report agy5-report.md). No Sonnet/Haiku jobs (the verify block
  needed the values worked out anyway; writing it directly was one call).
Assumptions to review: 16, 17 (new, in the persistent section).
Next sprint: S6 — 11 + 12 (CI for the mean; hypotheses, α, β). First action: log the S6 start, then read
  brief §2 rows 11/12 and §4 rows 11/12 (grep "^| 1[12] " in src/brief.md), the backlog row on HT slides
  20 and 22, and content/11 and 12.
Read at start: this hand-off · ../../../study-pack-sprint-protocol.md · spec §5 (study-pack-format.md
  lines 68–95) · brief rows 11/12 (§2, §4) and §1.3 (slides 08, lines 62–93) · content/11-…, 12-… ·
  KB 03 "Interval estimation" and KB 04 by section · Assignment 4 only for the items the brief maps ·
  07 lines 1–20 (format model). Do not re-read src/build.py.
Build/view how-to (scratch scripts in the auto.py temp folder, rewrite if gone):
  `python -I <temp>/run_build.py verify.py` and `python -I <temp>/run_build.py build.py <prefixes>`
  (prints OVERLAP/FAIL lines); `python -I <temp>/sheets.py <pdf-stem> ...` (4 pages per PNG, 55 dpi);
  `python -I <temp>/pages_for_agy.py <pdf-stem> ...` (one PNG per page, 80 dpi, into <temp>/agy5) then
  agy as in the contract. Progress log: write <temp>/line.txt, run `python -I <temp>/logline.py
  <temp>/line.txt` (absolute paths; no `cd … &&` before a write). G&K text search:
  `python -I <temp>/gkscan.py <first idx> <last> <regex>` (0-based PDF pages). Edits of several strings:
  a script in <temp> that asserts each match once; print with ascii() (cp1252 console).
  Markup: no ASCII "|" inside a table cell or a [[fig:…]] caption (use "∣"); no Greek in box titles.
```
