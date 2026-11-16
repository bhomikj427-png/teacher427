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
| 13 | 04a runs a fair die (p = ½) through steps 1–4 and MTE B3's irregular die (p = 5/8) in steps 5–6; 04a steps 1–3 and 04b step 6 (two desks, λ = 2.5 + 1.5) are pack-made Predicts/examples | S4 | open |
| 14 | A2 C3's key 0.8754 vs 0.8753 is treated as last-digit rounding (noted in 04b's answer, not added to the slip table); 05's split into a/b was not needed (10 steps) | S4 | open |
| 15 | S4's G&K facts were read on the PDF's text layer (OCR), not on page images; section and example numbers matched the old v1.2 citations | S4 | open |

## Current hand-off

```
Sprint: S4 — 04a + 04b + 05 — done (2026-11-17, auto.py session 9)
Written: KB 02-probability-distributions.md "Prescribed-textbook locations (G&K)" + CHANGELOG + sources.md
  (G&K entry extended: ch. 7 §7.2–7.3, ch. 8 §8.1, §8.6).
  content/04a-binomial.md — v1.3, 6 steps (1 one yes/no trial, 2 counting orders C(n, x) (3-throw tree),
  3 formula (= 02a's 3-children PMF; B(10, ½) P(5) = 0.2461), 4 np, npq (A2 MCQ 2, 9; G&K Ex. 7.7 note),
  5 solve p = 5/8 (MTE B3 = G&K Ex. 7.4), 6 expected frequency 0.55).
  content/04b-poisson.md — v1.3, 6 steps (1 desk λ = 2.5, A2 B1(i), interval rescaling, 2 mean = variance
  (MTE A2, A2 MCQ 3, 7; proof of E = λ), 3 λ from a probability (MTE A4; Check = G&K Ex. 7.30),
  4 complements (A2 B1(ii) 0.2424; Check = A2 C3), 5 Poisson ≈ binomial (A2 D3), 6 sums (A2 MCQ 12)).
  content/05-uniform-exponential.md — v1.3, 10 steps (1 flat density A2 B2, 2 length ratio + clipping
  A2 MCQ 10 / D4, 3 bus MTE B4, 4 absolute values A2 B8(i–iii) / C4, 5 mean and variance A2 MCQ 4,
  6 find K A2 B8(iv), 7 exponential A2 MCQ 8, 8 survival A2 D2 / B7(i), 9 memoryless A2 B7(ii), MCQ 5,
  C1, 10 not memoryless A2 B5 0.6225 + key-slip note).
  figures.py: binom_paths, binom_fair10, binom_die58, pois_desk, pois_limit, unif_rect, unif_bus,
  unif_abs, expo_tail, expo_memory (v1.2 binom_poisson, poisson_limit, uniform_bus, expo_memoryless
  deleted). verify.py: block "# ==== v1.3 S4"; old v1.2 "# ---- 04/05" pack checks pruned.
  Old 04 md/html/pdf removed. START-HERE: rank 10 and 12 rows, Unit 2 map, file table (04a, 04b, 05),
  prerequisite line, A2 B5 slip row (05 §10 + G&K ex. 7(a)), check count 865 / 16 key differences.
  Cross-refs re-pointed: 06 (header, line 105), 09b (header, lines 146, 153), 10 (header), 12 (header,
  line 167). Mock 17 names no file.
Verified this sprint: numbers: verify.py 865 checks, 0 failures, 16 key differences (the 15 before + A2 B5
  checked again in the S4 block). Build 00 04a 04b 05 06 09b 10 12: no OVERLAP; combined PDF 193 pp.
  Sheets viewed: 04a-1, 04b-1, 05-3 (fixes: 04a formula comma, expo_memory right-panel zoom, 05 step 8
  integral written in words). G&K facts read on the PDF text layer (assumption 15).
Open (carried): none for S4. Backlog unchanged (S5, S6, S7, S9 rows).
Decisions made: 04 split into 04a (binomial) / 04b (Poisson); 05 kept whole (10 steps). Later files cite
  "04a step N", "04b step N", "05 step N" (05's step numbers changed: old §6 = new §10).
Assumptions to review: 13, 14, 15 (new, in the persistent section).
Next sprint: S5 — 06 + 07 (normal; SE and CLT). First action: log the S5 start, then read brief §2 rows
  06/07 (lines 111–112) and §4 rows 06/07 (lines 153–154), and the backlog row on 07's slide tags.
Read at start: this hand-off · ../../../study-pack-sprint-protocol.md · spec §5 (study-pack-format.md
  lines 68–95) · brief lines 111–112, 153–154 · content/06-normal.md (239 lines),
  07-sampling-se-clt.md (219 lines) · KB 02 (normal) and 03 (SE/CLT) by section · 05 lines 1–20 (format
  model) · slides SE-and-CLT only for the pages the brief rows cite. Do not re-read src/build.py.
Build/view how-to (works under auto.py; scratch scripts in the auto.py temp folder, rewrite if gone):
  from study-pack-v12/ run `python -I <temp>/run_build.py verify.py` and
  `python -I <temp>/run_build.py build.py <prefixes>` (sets PYTHONIOENCODING=utf8, prints OVERLAP/FAIL
  lines); `python -I <temp>/sheets.py <pdf-stem> ...` renders 4 pages per PNG at 55 dpi into <temp>/sheets.
  Progress-log append: write the line to <temp>/line.txt, run `python -I <temp>/logline.py <temp>/line.txt`.
  G&K text search: `python -I <temp>/gkscan.py <first page idx> <last> <regex> ...` (0-based PDF pages;
  ch. 7 ≈ 450–560, ch. 8 ≈ 565–730).
  New figures: functions in figures.py's v1.3 block (before ALL), built on FL (tools/figlib.py).
  Markup: never put an ASCII "|" inside a table cell or a [[fig:…]] caption; use "∣" (U+2223).
Cross-ref reminder for S5: other files cite 06 and 07 by step number (not counted this sprint); grep
  "06 §\|07 §\|file 06\|file 07" across content after renumbering steps.
```
