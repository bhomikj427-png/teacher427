# MAS2001 — Sources (tiered, dated, confidence-noted)

> Per `../../../../subject-research-protocol.md` §2. Stage-1 anchors on canonical engineering-
> statistics texts; exact statements of load-bearing results were verified against external sources
> this session (2026-06-16). MUJ's *prescribed* list is unconfirmed (to-verify, `00-map.md`).

## Tier 1 — Primary / foundational (canonical textbooks)
- **Walpole, Myers, Myers & Ye — *Probability & Statistics for Engineers & Scientists* (9e).**
  Primary anchor for all four units. `settled`.
- **Montgomery & Runger — *Applied Statistics and Probability for Engineers*.** Estimation &
  testing anchor. `settled`.
- **Sheldon Ross — *A First Course in Probability* / *Intro to Probability & Statistics for
  Engineers & Scientists*.** Probability & RVs, limit theorems. `settled`.

- **Gupta & Kapoor — *Fundamentals of Mathematical Statistics* (prescribed textbook; PDF in
  `../books/`).** Ch. 15 §15.10–15.13 (MLE definition eq. 15·53, Thms 15.11, 15.13, 15.14, 15.15,
  15.17; MoM + remarks) and ch. 15 exercises 20(b), 21, 23(b): read on the page images 2026-11-16
  (sprint S3); supports `03-estimation.md` "MLE and MoM properties". `settled`.
  Ch. 7 §7.2–7.3 (Ex. 7.4, 7.7) and ch. 8 §8.1, §8.6 (Ex. 8.40, exercise 7(a)): read on the PDF text layer
  2026-11-17 (sprint S4); supports `02-probability-distributions.md` "Prescribed-textbook locations".
  Ch. 14 §14.2 (Ex. 14·6 and the one-tailed example before it), §14.2.10 (remarks 3–4, Ex. 14·7), §14.5.5 (remarks 1–2, Ex. 14·20): read on the
  PDF text layer 2026-11-17 (sprint S7); supports `04-hypothesis-testing.md` "Prescribed-textbook locations"
  (t-tests, F-test) and study-pack files 13, 14.
  Ch. 8 §8.2 (normal; §8.2.2 properties, areas 0·6826 / 0·9544 / 0·9973), §8.10 (CLT; Lindeberg–Lévy
  iid form, mean form eq. 8·31-2) and ch. 12 §12.3 (parameter vs statistic), §12.3.2 (standard error):
  read on the PDF text layer 2026-11-17 (sprint S5); supports the same KB section (S5 bullets).
  Ch. 12 §12.5–12.8 (hypotheses, errors, critical region, tails, critical values, steps), ch. 15 §15.15
  (confidence interval and limits), ch. 16 §16.2.4–16.3 (W, size, power function, steps): read on the PDF
  text layer 2026-11-17 (sprint S6); supports `04-hypothesis-testing.md` "Prescribed-textbook locations"
  and the §15.15 bullet in `03-estimation.md`.

## Tier 1/2 — Authoritative course material (verification this session, 2026-06-16)
- **MIT OpenCourseWare 18.600 / 18.440 *Probability and Random Variables*** — confirmed the topic
  set and CLT framing. <https://ocw.mit.edu/courses/18-600-probability-and-random-variables-fall-2019/>
- **Wikipedia — *Central Limit Theorem*** (orientation + exact standardized statement). Tier 3 used
  only to confirm a `settled` canonical statement; cross-checked with MIT OCW. 2026-06-16.
- **Wikipedia / CMU Stat-700 lecture notes — Chebyshev inequality exact form**
  P(|X−μ|≥ε) ≤ Var(X)/ε². <https://www.stat.cmu.edu/~larry/=stat700/Lecture6.pdf>. 2026-06-16.
- **Wikipedia — *Poisson limit theorem*** (Binomial→Poisson mechanism). Orientation only. 2026-06-16.
- **`scipy.stats` (norm, t, chi2, f) — exact computation** of every table value the course's questions
  print (`04-hypothesis-testing.md` → *Table values*). Computation, not a citation; the study pack's
  `src/verify.py` re-runs the same values. 2026-11-16.

## Tier 3/4 — Derivative (leads only, not citable as final word)
- Study-notes aggregator search result — **MAS2001 unit list** (used to seed scope; flagged
  `uncertain`, to be reconciled with the official handout). 2026-06-16.

## Official scope documents (to fetch / reconcile)
- "Course Handout MAS2001 — July–Nov 2025" (MUJ Dept. of Mathematics & Statistics / Scribd) — the
  authoritative unit boundaries + prescribed text. **Not yet fetched** (open question, `00-map.md`).
- MUJ ECE Curriculum/Scheme PDF (confirms code + 3-0-0-3): see `../course-info.md`.

## Independence note (protocol §5)
The textbook trio (Walpole / Montgomery / Ross) are independent authoritative texts; the exact
forms of Chebyshev and the CLT were additionally checked against MIT OCW / CMU notes — two distinct
external origins reached this session, satisfying triangulation for these load-bearing results.
