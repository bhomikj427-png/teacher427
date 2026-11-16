# MAS2001 Statistics & Probability — Progress Log

> Written **live** as sessions happen (not reconstructed at wrap-up). Session-resume block is
> overwritten each session-end; Session history is append-only. See `../../README.md`.

## Session resume
- **Study pack (2026-11-16):** rebuild to v1.3 runs in sprints: resume from `sprints.md` → *Current hand-off* (S0–S9; S0 brief done 2026-11-16; S1 done: 01, 02a, 02b at v1.3; next = S2 (03 + 08); `python auto.py run sem-3/01-statistics-and-probability`). The teaching lines below are unchanged.
- Last session: 2026-06-19 (Stage-2 research pass — subject brought to the teaching gate)
- Where we stopped: **KB complete — `stage-2✓` for all 4 units; subject is now TEACH-READY.** No
  concept taught yet (teaching gate was correctly enforced before any lesson).
- Recap (what happened):
  - Learner asked to "start" Stats & Prob. Gate check found the KB at `stage-1✓`, **not** the
    `stage-2✓` teaching gate. Flagged that the prior 2026-06-19 note ("began opening U1") had jumped
    the gate. Learner directed: **"complete the KB first, both stages."**
  - Ran the full Stage-2 depth pass: built `knowledge-base/stage-2/01–04` + `stage-2/sources.md`,
    mechanism-level and confidence-marked; every load-bearing specific (CRLB/Fisher, Neyman–Pearson,
    Wilks, Berry–Esseen, exponential family, max-entropy Normal, t/χ²/F constructions, ASA p-value)
    **verified vs external sources this session** (protocol §1). Stage-1 files untouched except
    footer pointers (Stage-2 now "✓ BUILT").
  - Promoted misconceptions **M3/M7/M11** `uncertain → settled` (ed-research verified).
  - Updated CHANGELOG, 00-map register, research-queue (→ `stage-2✓`), course-info (→ `stage-2✓`).
- Standing learner facts (carry into first lesson): novice in stats / developing in basic prob;
  **complex notation overloads — dominant delivery constraint** (one symbol at a time, concrete→abstract,
  never a dense formula cold); **LaTeX `$...$` does not render — plain ASCII math only**; dislikes
  trivially-easy probes (calibrate diagnostics up to ~80% edge); goal = **depth**.
- Next up (first real teaching session): open **U1** via the loop — ACTIVATE with a calibrated probe
  above simple counting (conditional probability / RV-as-function is the likely edge), then teach U1
  scoring-relevant material first. Teaching order: U1 → U2 → U3 → U4 (00-map prereq graph).
- Due for review today: nothing yet (no items mastered).

## Mastery ledger
*(empty — nothing mastered to criterion yet)*

## Spaced-review / relearning queue
*(empty — fills as items are mastered)*

## Session history
- [2026-06-19] **Stage-2 research pass → `stage-2✓` (teach-ready).** Gate check caught KB at
  `stage-1✓`; learner directed "complete both stages first." Built `stage-2/01–04` + `stage-2/sources.md`
  (all load-bearing specifics externally verified); promoted M3/M7/M11 to `settled`; updated CHANGELOG/
  map/queue/course-info. No teaching yet — gate enforced. Next session = begin teaching U1.
- [2026-06-19] Subject **activated** (first learner session). Initialised learner-profile + this log.
  Diagnosed level: novice in statistics, developing in basic probability (coin-probe correct),
  prerequisite math available but complex notation overloads — logged as the dominant delivery
  constraint. Goal = depth (no exam date/material). KB pre-existing (Stage-1, units 01–04). Began
  opening U1; no concept mastered yet.
- [2026-11-13] Inbox triage (no teaching): `WhatsApp Image 2026-11-12 at 3.53.24 PM.jpeg` → `exam-pack/BLUEPRINT-MAS2001-July-Nov-2026.jpeg`,
  plus a typed transcription `exam-pack/BLUEPRINT-MAS2001-July-Nov-2026.md`. **First exam evidence for this subject.** Official question
  blueprint for MAS2001, July–Nov 2026: 5 content rows × Parts A/B/C/D, weightage 10/20/22/10/18 = 80. The marks per part
  are not printed; solved uniquely from the rows as A = 2, B = 6, C = 8, D = 8 (all five rows check). `knowledge-base/exam-map.md`
  priority section rewritten from it.
- [2026-11-15] Inbox triage (no teaching): 10 MAS2001 files in `_inbox/_unsorted/` filed. `exam-pack/`: `PYQ-MTE-2026-question-paper.pdf`
  (30 marks: A1–A4 2 each, B1 3, B2–B4 4 each, C1 4+3), `PYQ-MTE-2026-solution-and-marking-scheme.pdf` (handwritten key),
  `ASSIGNMENT-1-random-variables-chebyshev.pdf`, `ASSIGNMENT-2-distributions.pdf`, `ASSIGNMENT-4-CI-and-hypothesis-errors.pdf`,
  `ASSIGNMENT-5-t-F-chisq-ANOVA.pdf`, `slides-LMS-standard-error-and-CLT.pdf`, `slides-LMS-MLE-and-Bayesian.pdf`,
  `slides-08-hypothesis-testing.pptx`. `books/Gupta-Kapoor-Fundamentals-of-Mathematical-Statistics.pdf` (1303 pp.; the professor's
  slides cite it as the reference text). No Assignment 3 in the drop. **Finding:** the MTE is 30 marks, so the 80-mark blueprint is the ETE.
- [2026-11-15] Learner request (stated): "make me a v1.2 and do make a combined pdf at the end, take as long as u need". Building
  `study-pack-v12/` to `study-pack-format.md` v1.2, full build (learner asked for the whole pack, so no separate pilot stop).
  Questions from the MTE 2026 paper, Assignments 1, 2, 4, 5 and the professor's slides (P1), Gupta & Kapoor (P2). Facts from the
  `stage-2✓` KB + Gupta & Kapoor. **No teaching event.**
- [2026-11-15] `knowledge-base/exam-map.md` updated from the new evidence: MTE = 30 marks so the blueprint is the ETE; per-row table of
  MTE/assignment/slide items; confirmed forms (one-way ANOVA only, χ² independence only, discrete-prior Bayes); the 11 key slips.
  (Logged right after the edit, not before it, which breaks the log-first rule for this one line.)
- [2026-11-15] **v1.2 ETE pack built**: `study-pack-v12/pdf/` = `00-START-HERE` + 16 topic files (01 probability basics … 16 ANOVA) +
  `17-mock-paper` (80 marks on the blueprint, with a marking key) + combined `MAS2001-Statistics-and-Probability-ETE-study-pack.pdf`
  (121 pp., bookmarked). Every step has a question or Predict, a guess line and a Check; every file has Exam form, Traps, Self-test,
  Answers. Questions: all 10 MTE parts, ~100 assignment items, 13 slide examples (P1); 6 Gupta & Kapoor (P2). `src/verify.py`:
  423 checks, 0 failures; 11 professor-key mismatches flagged in the files and in START-HERE (A5 C6 table value 19.41 → F(2, 12) = 3.89
  flips the decision). 29 generated figures (`src/figures.py`). All pages viewed after the final build; fixes made on viewing: tables
  allowed to split between rows, list spacing, nested superscripts, an accidental Markdown link, 8 figure label overlaps.
  The pilot step was skipped because the learner asked for the full pack in one go. **No teaching event; mastery ledger unchanged.**
  **Where we stopped:** pack delivered; learner has not worked any Check.
- [2026-11-16] Spec now **v1.3** (`study-pack-format.md`); the v1.2 files 01–16 are listed as not meeting it. Writing `sprints.md` (S0–S9, 10 sprints, learner's budget 9–10): S0 builds the subject brief, then 1–3 files per sprint in START-HERE priority with prerequisites first, run by `auto.py` (shared steps: `../../../study-pack-sprint-protocol.md`). **No teaching event.**
- [2026-11-16] ETE dates (learner-stated): Stats 19 Nov, DE 21 Nov, EDC 24 Nov (`research-engine/exam-calendar.md`). Sprint runs in that order; `sprints.md` header gets the date. **No teaching event.**
- [2026-11-16] **Sprint S0 (brief) started** under `auto.py` (unattended): writing `study-pack-v12/src/brief.md` from every `exam-pack/` file (slides transcribed, question bank mapped to files, table values checked against the KB, figure list). **No teaching event.**
- [2026-11-16] S0 finding: the KB held **no statistical table values**, though the questions print 36 of them (z areas, t, χ², F). All recomputed with scipy (every printed value matches except the two known key slips, A5 C6 and A5 D1, and A5 A10's option); writing them into `knowledge-base/04-hypothesis-testing.md` (new section "Table values the course's questions use") + CHANGELOG + sources line.
- [2026-11-16] **Sprint S0 done.** `study-pack-v12/src/brief.md` written: three decks transcribed (MLE/Bayes and hypothesis-testing equations viewed as images), slips noted (CLT p.14 z = −0.4 → −0.94; MLE Ex. 14 "x₁₀" for n = 6; HT slides 7, 18, 23); question bank maps every MTE (10), A1 (24), A2 (28), A4 (16), A5 (26) item and 15 slide examples to a file + idea; HT slides 20 and 22 found unused in v1.2 (backlog → S6); per-file idea/figure plan with expected splits 02a/b, 03a/b, 04a/b, 12a/b. `verify.py` re-run: 423 checks, 0 failures, 11 key differences. `sprints.md`: S0 ticked, 3 backlog rows, Assumptions 4–5, hand-off → S1. **No teaching event.**
- [2026-11-16] **Sprint S1 (01 + 02a + 02b) started** under `auto.py` (unattended): rebuilding `study-pack-v12/src/content/01-probability-basics.md` and splitting old 02 into `02a-discrete-random-variables.md` + `02b-continuous-random-variables.md` (v1.3), new figures in `src/figures.py`, numbers in `src/verify.py`. **No teaching event.**
- [2026-11-16] S1 progress (stopped at the context limit; sprint **partial**): 16 new figures appended to `src/figures.py` on `tools/figlib.py` (dice_space, dice_events, dice_complement, venn_union, dice_shrunk, venn_subset, aces_tree, bolt_tree, bolt_bayes, family_map, boys_pmf, boys_cdf, cable_pdf, cable_cdf, power_tail, life_cond), overlap check clean, viewed. `content/01-probability-basics.md` rewritten to v1.3 (12 steps, two-dice running example). `content/02a-discrete-random-variables.md` written (9 steps, 3-children running example). Finding (checked on the A1 page image + G&K p. index 241): A1 LA 2's printed row is k, 2k, 2k, 3k, 3k, … (not only x = 0 differs, as v1.2 said); the key answers G&K's question P(X < 6) = 81/100, and its 91/100 is G&K's 19/100 with digits swapped. Not yet done: 02b, verify.py checks for the new numbers, build, old 02 removal, START-HERE. **Where we stopped:** S1, 02a written; next = write 02b. **No teaching event.**
- [2026-11-16] **Sprint S1b (S1 continuation) started** under `auto.py` (unattended): writing `content/02b-continuous-random-variables.md` from the hand-off plan, adding the 01/02a/02b numbers to `src/verify.py`, building 01 02a 02b, removing old 02, updating START-HERE + slip table. **No teaching event.**
- [2026-11-16] **Sprint S1 done (via S1b).** `content/02b-continuous-random-variables.md` written (v1.3, 6 steps: area, PDF rules, smooth CDF, median, tail by parts, conditional; cable running example; 4 figures). `src/verify.py` gained a `# ==== v1.3 S1` block (01/02a/02b numbers by enumeration, exact fractions and scipy quad): **558 checks, 0 failures**, 13 key differences (the 2 new ones = A1 LA 2 (ii), flagged in 02a's note box). Build 00 01 02a 02b: no `OVERLAP`; all pages viewed. Fixes from the view: 01 map cut at the "|" of "P(A | B)" (label → "When B forces A"); 01 figure `dice_shrunk` showed A∩B instead of the text's C∩B and did not fade the ruled-out rows (redrawn); 01 Self-test 7 wording; 02b "^∞" literal. Old `02-random-variables` md/html/pdf removed; cross-refs in 03, 04, 05, 06 re-pointed to 02a/02b; START-HERE rank 15/16 rows, Unit 1 map, prerequisite line, file table (01, 02a, 02b) and A1 LA 2 slip row rewritten; "How checked" now says 558 checks, 13 mismatches. **Where we stopped:** S1 done; next = S2 (03 + 08). **No teaching event.**
