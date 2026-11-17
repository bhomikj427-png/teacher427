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
| S6 | **11 + 12** confidence interval for the mean; hypotheses and errors (α, β) | old 11, 12 · KB `03`, `04` · Assignment 4 · slides 08 | `11-…`, `12-…` rebuilt | same; Assignment 4 answers compared | ✓ 2026-11-17 (11 8 steps, 12a 8 steps, 12b 7 steps; A4 B1–B5, C1–C3 compared with the key; HT slides 20–22 added; 6 figure-label fixes left, see hand-off) |
| S7 | **13 + 14** t-tests; F-test | old 13, 14 · KB `04` · Assignment 5 | `13-…`, `14-…` rebuilt | same | ✓ 2026-11-17 (sessions 13 + 14: 13 7 steps, 14 6 steps; every A5 t/F item worked; S6's six figure labels fixed) |
| S8 | **15 + 16** χ² independence; ANOVA (the paper's only Part D) | old 15, 16 · KB `04` · Assignment 5 | `15-…`, `16-…` rebuilt | same; Assignment 5 answers compared | ✓ 2026-11-17 (session 17: 15 8 steps, 16 8 steps; all 12 A5 χ²/ANOVA items worked and compared with the printed values/options) |
| S9 | **10 + integration** Bayesian; mock paper re-pointed; START-HERE ranks, times, map, slip table | old 10, 17 · `00-START-HERE.md` · KB `03` | `10-…` rebuilt; 00 and 17 updated; full build | grep finds no reference to a removed file; `verify.py` passes; build prints no `OVERLAP` | ✓ 2026-11-17 (session 18: 10 7 steps; START-HERE, mock key, README, brief count; 1492 checks, 0 failures; full build 263 pp., 0 flagged) |

**Learner check-ins are not sprints:** report misses on any delivered file whenever you like; the next
sprint reads them first.

---

## Verify backlog (persistent — items leave only when resolved, with the sprint that closed them)

| Item | Raised | Close in |
|---|---|---|
| ~~Textbook facts checked in S3 session 1 are only in the hand-off: write them into KB 03 + CHANGELOG~~ | review 2026-11-16 | **closed S3** (KB 03 "MLE and MoM properties", CHANGELOG, `sources.md` G&K entry) |
| ~~G&K ch. 15 ex. 20(b) prints θ, old 09 writes α~~ | review 2026-11-16 | **closed S3** (09a step 2 uses θ + note box; slip-table row) |
| ~~Table-value count: brief.md:131 and S0 log say 36, KB 04 table has ≈ 32~~ | review 2026-11-16 | **closed S9** (KB 04 table recounted: 32 values, 31 printed + t(20) needed; brief:131 corrected) |
| ~~START-HERE:142 claims every page viewed; 04, 07, 09 not logged as viewed~~ | review 2026-11-16 | **closed S9** (all were rebuilt later and page-checked per the log, S3–S5; the line now says each file was checked after its last build) |
| ~~HT slides 20 (binomial α = 1/9, β = 11/16) and 22 (power function, α = 0.001, (0.1)⁴, (0.1)^(θ+1)) not used in v1.2 and not in `verify.py`~~ | S0 | **closed S6** (12b steps 4, 7; `# ==== v1.3 S6` block) |
| ~~v1.2 file 07's slide tags are off; SE/CLT p.14 prints z = −0.4 (true −0.94): note box~~ | S0 | **closed S5** (07 re-tagged p.5, p.11–18; note box in 07 step 10; slip row) |
| ~~A5 C2(b) needs t(20) = 2.086 (not printed in the assignment): print it as the pack's value~~ | S0 | **closed S7** (13 steps 5–6 print it; `13 S5 t(20)` in verify) |
| ~~New numbers in v1.3 01 and 02a not yet in `verify.py`~~ | S1 | **closed S1b** (`# ==== v1.3 S1` block, 558 checks pass) |
| ~~START-HERE slip table: A1 LA 2 row~~ | S1 | **closed S1b** (row rewritten) |
| ~~02a's MTE A1 line says option (a) "is in 03b"~~ | S1b | **closed S2** (03 split; MTE A1(a) is 03b step 4) |
| ~~Old v1.2 `# ---- 03` / `# ---- 08` checks in `verify.py`~~ | S2 | **closed S2b** (pruned; 665 checks pass) |
| ~~Pack `README.md` still says "format v1.2"~~ | S1b | **closed S9** (v1.3) |
| START-HERE "how checked" line (≈ line 147) says verify has 1157 checks and 18 key mismatches; verify now prints 1420 checks and 19 key differences (`14 S5 F(4,4)` repeats the A5 D1 slip): rewrite the line | S8 | **closed S9** (1492 checks, 19 differences, the repeat named) |

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
| 18 | 12 split into 12a (concepts, 8 steps) and 12b (computing α and β, 7 steps). 12a's battery numbers (σ = 50, n = 25, x̄ = 990, true μ = 980) are pack-made; its β prints the table route (z ≈ 0.36, β = 0.3594, exact 0.3613) | S6 | open |
| 19 | START-HERE slip row for ppt 8 slide 7 removed: agy's transcription of the slide's images shows "≠, < or >" (the missing ≠ was a text-layer artifact, so brief §1.3's slip claim is wrong) and no milk / −0.545 example (v1.2's row had no source) | S6 | open |
| 20 | 11 uses pack-made items: the weather-forecast anchor, Check 2 bulbs (n = 64, σ = 120), the ci_coverage picture (20 simulated hospitals, seed 0, exactly one miss, checked in verify); 12b's Checks and Self-test are pack-made variants of the slide/assignment questions | S6 | open |
| 21 | 14 step 3 (A5 C5) and step 5 (A5 D1) compare a two-sided H₁ with the one-tail 5% value, as the questions print and as G&K §14.5.5 remark 1 does; a note gives the strict α/2 value (3.95; 9.60). 13 reads a given "SD" as s (n − 1) with a note on the n-divisor reading; 13/14 Checks, Self-tests, 13 step 4's one-sided Predict and 14 steps 1–2's tables are pack-made | S7 | open |
| 22 | Session 13 crashed after writing 13 and 14; session 14 accepted the text after reading both in full and recomputing every number in verify (one fix: 14 step 2's F₀.₀₁(7, 10) 3.95 → 5.20) | S7 | open |
| 23 | Pack-made items in 15/16: 15 step 1's Predict and Check 1, Check 3(b), Check 7 (500 students), Self-test; 16 step 1's two-panel data (tight F = 128, wide F = 1.29), step 2's classification table and Check 2, step 3's Predict (person reducing by 15), all Checks; 16 step 2 states F = t² for two groups, shown on numbers in Self-test 5 (verify `16 ST5 t^2 = F`), not cited to a text | S8 | open |
| 24 | G&K Fundamentals has no ANOVA formulas (§14.5.11 only names the technique), so 16 rests on two university-author notes: Chan (Rutgers Math 170S §9.3: SS definitions, computational forms, df, F, assumptions) and Lockhart (SFU STAT 330 lecture 20: decomposition and df only). F = MSB/MSW and the assumptions are therefore single-sourced at Chan, plus G&K §14.5.5's F ratio and KB stage-2 §3 | S8 | open |
| 25 | 10's pack-made items: step 1's two_views picture, the Predicts of steps 3, 4, 5, 7, Checks 1–4, 6, 7 and Self-test 3–5 (3–4 carried from v1.2). Slide tags moved p.10 → p.11 per brief §1.2. G&K ex. 4(d) Q3(f) is answered with independent draws; drawing from the finite shipments gives the same 0.4730 (in verify). Step 7 names the posterior median for absolute-error loss in one sentence (Balakrishnan, Chan) | S9 | open |
| 26 | Mock re-pointing = a "Where each item is taught" table at the top of the key; no mock question changed and no Bayesian item added (v1.2's mock had none; row 3 already has 4 items) | S9 | open |
| 27 | START-HERE's "Pages" line was rewritten to what the logs show (each file checked after its last build) instead of re-viewing all 263 pages; only 10, 00 and 17 were page-checked in S9 | S9 | open |
| 17 | Session 10 crashed after writing 06; session 11 accepted its 06 after reading it in full, recomputing every number (one rounding fix: MTE C1(a) 0.0669) and agy's page check, without re-reading G&K §8.2 | S5 | open |

## Current hand-off

```
Sprint: S9 — 10 + integration — done (2026-11-17, auto.py session 18). ALL SPRINTS S0–S9 DONE.
Written: content/10-bayesian.md — v1.3, 7 steps (running example slides Ex. 15, prior 0.6/0.4, n = 2): 1 two views of a
  parameter (slides p.11; two_views), 2 the prior (p.11–12), 3 likelihood (bayes_tree), 4 marginal g(x) (p.13),
  5 posterior (p.13; bayes_update0; Check 5(b) = G&K ex. 4(d) Q3(f), 0.4730), 6 full table (Ex. 15; prior_posterior
  reused), 7 posterior mean (bayes_means; MLE contrast; prior washing out at n = 20).
  figures.py (Sonnet): two_views, bayes_tree, bayes_update0, bayes_means. verify.py: block "# ==== v1.3 S9"; old
  "---- 10" checks pruned (LMS Ex15 key checks kept).
  00-START-HERE: rank 14 row (10 §1–2, 5–7, 30 min), what-each-file row 10, question counts recounted from the files'
  question lists (A 80, Slides 19, G&K 6, P1 110), facts line (two university notes where G&K is silent), how-checked
  (1492 checks, 19 differences), pages line. 17-mock-paper: "Where each item is taught" table in the key.
  README format v1.3. brief.md:131 table-value count 36 → 31.
  KB 03 "Verified S9" bullets; sources.md (Balakrishnan CMU 36-705 l.16; Chan Rutgers 170S §6.8; G&K §4·9); CHANGELOG.
Verified this sprint: G&K §4·9 remarks 1–3 and ex. 4(d) Q3(f) (PDF text layer; G&K has no Bayesian estimation);
  posterior = likelihood × prior / marginal and Bayes estimate = posterior mean under squared-error loss, median under
  absolute error: Balakrishnan Thm 16.5 + eq. 16.10, Chan §6.8 (both read as PDF text). Numbers: verify.py 1492 checks,
  0 failures, 19 key differences (unchanged list). Full build: 0 flagged lines, combined 263 pp.
  Done-when: no reference to a removed file (script scan of content, README, build.py, figures.py; no stale html/pdf).
  agy page check of 10 (12 pp.), 00 (7 pp.), 17 (5 pp.): 24 of 24 clean, no fixes (report <temp>/agy9-report.md).
Open (carried): none from S9. Persistent assumptions 1, 3–5, 8–9, 11–27 await the learner.
Decisions made: file 10 cites "10 §5" (posterior), "10 §7" (posterior mean). Mock pointers live in the key table.
Helpers: Sonnet = 4 figures + verify block + builds (1 job). agy = page check of 10, 00, 17 (agy9-report.md).
  Haiku: none. Own calls ≈ 40.
Assumptions to review: 25, 26, 27 (new, in the persistent section).
Next sprint: none — the plan (S0–S9) is finished. Next work is the learner's: study from 00-START-HERE, report misses
  (a learner check-in, not a sprint), and confirm or overrule the open assumptions.
```
