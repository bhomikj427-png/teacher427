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

## Current hand-off

```
Sprint: S3 — 09a + 09b — partial (2026-11-16, auto.py; operator stopped the run early)
Written: nothing in the pack yet (only progress-log lines: S3 start + stop).
Verified this sprint (G&K page images, book page index in the PDF): §15.10 methods list (idx 1165);
  §15.11 MLE, L = Π f(xᵢ, θ) eq. 15·53 (idx 1165); Thm 15.11 consistent + remark "MLE(σ²) = s²
  (n-divisor) consistent, not unbiased", Thm 15.13 asymptotic normality, Thm 15.14 most efficient
  (idx 1167); Thm 15.15 MLE is a function of a sufficient estimator (idx 1168); Thm 15.17 invariance
  (hint on idx 1190); §15.13 MoM, remarks 1–3: consistent, asymptotically normal, generally less
  efficient than MLE, identical to MLE for exponential-family form (idx 1182–1183). Exercises idx 1192:
  20(b) prints f(x, θ) = θe^(−θx) (v1.2 wrongly wrote α: use θ); 21 U(a, b) and 23(b) (1 + θ)x^θ as v1.2.
Open (carried): the whole S3 build: write 09a (MoM ≈ 5–6 steps: population vs sample moments ·
  one parameter = G&K 20(b) · Check U(0, θ) · two parameters = G&K 21 · MoM on data = G&K 23(b)(i))
  and 09b (≈ 11 steps per brief §4 row 09b: coin-anchor likelihood · log · five steps · Ex. 12 ·
  Ex. 13 rats 16.2 · Ex. 11a · Ex. 11b · Ex. 14 (0.3970) · 2nd-derivative · properties (the Thm
  numbers above) · MoM vs MLE = G&K 23(b)(ii) 0.7279); figures (likelihood curve exists in v1.2 as
  likelihood_curve; add L vs ln L, ln L for Ex. 14, moment-matching picture); verify.py block
  "# ==== v1.3 S3" with all four slide MLE examples; build 00 09a 09b; view; remove old 09; START-HERE
  + cross-refs (reminder below).
Decisions made: none new.
Next sprint: S3 (restart) — first action: log the S3 restart, then read old 09 (270 lines; v1.2 content
  is correct apart from the α/θ label) + brief §2/§4 rows 09a/09b (lines 114–115, 156–157).
Read at start: this hand-off · ../../../study-pack-sprint-protocol.md · src/brief.md lines 43–61 and
  114–115, 156–157 · content/09-mom-mle.md · 08 lines 1–30 (format model) · src/build.py. The G&K
  facts above are already verified: don't re-read the book unless a new fact is needed.
Build/view how-to and the split reminder: as in the S2 hand-off below (scratch scripts run_build.py,
  sheets.py and gkpage.py are in the auto.py temp folder).
```

S2 hand-off (kept for the build how-to and the 09 split reminder):
```
Sprint: S2 — 03a + 03b + 08 — done (2026-11-16, via S2b, auto.py)
S2b did: build 00 03a 03b 08 (no OVERLAP; all pages viewed, no fixes); old 03 md/html/pdf removed;
  START-HERE rank rows 8 and 13, stuck tip, Unit 1 map, prerequisite line, file table, slip rows
  (03b §2, 03a §6, 03b §8); cross-refs 04 (×3), 07, 09 re-pointed; old v1.2 03/08 verify checks pruned:
  verify.py 665 checks, 0 failures, 15 key differences (START-HERE says 665 / 15). Rebuilt 00 04 07 09;
  combined PDF 160 pp.
Open (carried): none for S2. Backlog: README v1.2 → S9 (unchanged).
Build/view how-to (works under auto.py): cd into study-pack-v12 alone, then run a scratch script that
  calls `python src/build.py <prefixes>` with PYTHONIOENCODING=utf8 (scratch: run_build.py takes
  "build.py <prefixes>" or "verify.py"); render pages with pymupdf, 4 per sheet at 55 dpi (sheets.py).
  Both scripts sit in the auto.py temp folder and may be gone: rewrite them (≈ 20 lines each).
Next sprint: S3 — 09 → 09a (MoM) + 09b (MLE), rank 1. First action: log the S3 start, then read old
  09 + brief §2 rows 09a/09b (line ~114) + brief §4 rows 09a/09b (line ~156).
Read at start: this hand-off · ../../../study-pack-sprint-protocol.md · src/brief.md lines 43–61
  (MLE slides) and the 09a/09b rows of §2 and §4 · content/09-mom-mle.md · KB 03 (MoM/MLE section only)
  · 08's header + symbol table (format model) · src/build.py.
Reminder: when 09 splits, update START-HERE rank 1 row ("09 §3–7"), file table, slip row
  "Slides MLE Ex. 14 (09 §6)", the Unit 3 map, and grep "file 09\|09 §\|09-mom" across content
  (08 cites "file 09" for the factorisation test and Check 8; mock 17 B3/C2).
```

Previous hand-off (S2, kept for its step lists):
```
Sprint: S2 — 03a + 03b + 08 — partial (2026-11-16, auto.py; stopped at the context limit)
Written: content/03a-expectation-variance.md — v1.3, 7 steps (1 long-run average, 2 balance point,
  3 E(X²)/E(g(X)), 4 variance by definition, 5 shortcut E(X²) − μ², 6 SD, 7 continuous X = MTE B2);
  sensors running example (A1 App 1), battery = A1 App 3 + MCQ 4; key-rounding note (SD 0.98 → 0.973).
  content/03b-rules-and-chebyshev.md — v1.3, 9 steps (1 aX + b, 2 E of a sum = A1 LA 3 + key slip,
  3 Var of sum/difference, 4 E(XY) = MTE A1(a) + rules table, 5 geometric = A1 SA 4, 6 Chebyshev =
  A1 App 4 + MCQ 5/10, 7 bound vs exact = A1 SA 5, 8 bound > 1 = MTE B1, 9 lower bound = A1 SA 6).
  content/08-estimators-properties.md — rewritten v1.3, 8 steps (1 parameter/statistic/estimate,
  2 point vs interval, 3 unbiased (x̄ vs larger throw), 4 coefficients = MTE C1(b), 5 n − 1,
  6 consistent = G&K Q1 (iv)/(vi), 7 efficient (T₁ vs x̄), 8 sufficient = MTE A3 + G&K Q1 (iii)).
  figures.py: 9 new figures (block "# ---- 03a" … "# ---- 08" before ALL). verify.py: "# ==== v1.3 S2".
Verified this sprint: numbers: verify.py 683 checks, 0 failures, 15 key differences (new two = the
  known A1 LA 3 and A1 App 3 slips, both flagged in note boxes). G&K section numbers read from the
  book's contents: §6.3 addition, §6.4 multiplication, §6.7 variance of a linear combination, §6.13
  Chebyshev; §12.11 unbiased s²; §15.2–15.6, Theorem 15.2 (§15.4.2). Figures: overlap check clean.
Open (carried): NOT DONE — (1) build `python src/build.py 00 03a 03b 08` (run from study-pack-v12/;
  check how S1 ran it), fix every OVERLAP, view all pages of 03a/03b/08 at low res, 4 per image;
  (2) remove old content/03-expectation-variance-chebyshev.md + its html/ and pdf/ copies;
  (3) START-HERE: rank row 13 (03 → 03a + 03b, "03 §5–6" → "03b steps 6–8"), line 32 stuck-tip
  ("03 §1–4" → "03a, 03b steps 1–4"), Unit 1 map label, prerequisite line 54, file table row 61 (split
  into 03a/03b; 08 row), slip rows 130–132 (A1 LA 3 → 03b step 2, A1 App 3 → 03a step 6, MTE B1 →
  03b step 8), "How checked" count → 683 checks, 15 mismatches; (4) cross-refs: 04 lines 66, 69, 150
  ("file 03" → 03b steps 2–3 / step 2), 07 line 67 (→ 03b step 3), 09 line 147 (→ 08 step 5), and
  the mock 17 if it names 03; (5) prune old v1.2 03/08 checks (backlog row); README v1.2 → S9.
Decisions made: 03 splits into 03a (E, Var, one variable) / 03b (rules + Chebyshev). Step numbers as
  listed above; later files cite "03a step N", "03b step N", "08 step N".
Assumptions to review: 8, 9, 10 (new, copied to the persistent section).
Next sprint: S2b — first action: log the S2b start, then run the build for 00 03a 03b 08.
Read at start: this hand-off · ../../../study-pack-sprint-protocol.md (steps 11–14) ·
  content/00-START-HERE.md · the lines named in Open (4) · src/build.py · S1's progress-log lines
  for how the build/view was run
```
