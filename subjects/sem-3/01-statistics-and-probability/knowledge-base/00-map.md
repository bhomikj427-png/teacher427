# MAS2001 Statistics & Probability — 00 MAP (Stage 1, MUJ level)

> Big ideas, prerequisite graph, threshold concepts, scope, and the standing to-verify register.
> Built to `../../../../subject-research-protocol.md`. Scope = the official unit list in
> `../course-info.md` (unit *boundaries* are `uncertain` pending the official handout; the
> *content* is settled textbook material).

## The handful of big ideas (the expert's organizing schema)

1. **A random variable is a function from outcomes to numbers; its *distribution* is the whole
   object.** Everything (probabilities, expectation, variance, tail bounds) is read off the
   distribution (pmf/pdf and CDF). Master "distribution as the object" and the course unifies.
2. **Expectation is a linear operator; variance measures spread.** Most computation is "push the
   linear operator through" + a few named results (linearity of E, Var of independent sums).
3. **Independence + summation → limit laws.** Summing many independent RVs is *the* engine: it
   yields Chebyshev's bound, the Law of Large Numbers, and the **Central Limit Theorem** (sums tend
   to Normal). This is why the Normal distribution is everywhere and why inference works.
4. **Inference inverts the arrow.** Probability goes parameters → data; **statistics** goes data →
   parameters. Estimation (point + interval) and hypothesis testing are the two inverse moves, both
   resting on the **sampling distribution of a statistic** (which CLT usually supplies).
5. **Every test/interval is the same skeleton:** a statistic with a known sampling distribution + a
   decision rule calibrated by a chosen error rate. Learn the skeleton once; the t/z/χ²/F tests are
   instances.

## Prerequisite graph (load-bearing — triangulated, `settled`)

```
Probability basics ─┬─► Random variables (pmf/pdf, CDF) ─┬─► Expectation & variance ─┐
                    │                                     │                          │
                    └─► Independence ─────────────────────┴──► Sums of RVs ──► Chebyshev ─► LLN ─► CLT
                                                                                              │
Named distributions (Binomial, Poisson, Uniform, Normal, Exponential) ◄── pmf/pdf+E/Var ──────┤
                                                                                              ▼
                                              Sampling distribution of a statistic  ◄──── CLT
                                                       │                    │
                                              Estimation (MLE, MoM,    Hypothesis testing
                                              sufficiency, CIs)        (Type I/II, z/t/χ²/F, ANOVA)
```

Teaching order is this graph topologically: **U1 (prob + RVs + E/Var + CLT) → U2 (named
distributions) → U3 (estimation) → U4 (testing).** U3 and U4 both depend on the *sampling
distribution* idea, which is U1's CLT applied to a statistic.

## Threshold concepts (budget extra teaching here — where learners stall)

- **★ The sampling distribution of a statistic.** The single hardest idea: a statistic (e.g. the
  sample mean) is *itself* a random variable with its own distribution. Confusing the population
  distribution, the sample, and the sampling distribution is the root of most downstream errors.
- **★ The Central Limit Theorem as the bridge.** *Why* normality appears even when data aren't
  normal; why "n large" rescues inference. Once grasped, U3 and U4 stop being a list of recipes.
- **★ What a confidence interval / p-value actually means** (and does *not* mean). The classic
  misinterpretations (see `misconceptions.md`) are threshold-level, not careless slips.

## Scope (Stage 1 = the official units; cover all, don't exceed)

U1 Probability & random variables · U2 Probability distributions · U3 Theory of estimation ·
U4 Tests of statistical hypothesis. Per-unit notes: `01`–`04`.

## Open questions / to-verify register

- `[opened 2026-06-16]` **Exact MUJ unit boundaries** — seeded from a derivative aggregator, not the
  official "Course Handout MAS2001" PDF. *Resolve by:* fetching the official handout and reconciling
  the 4-unit split (esp. whether CLT sits in U1 or U2, and the exact estimation topics). Content is
  settled; only the boundary is `uncertain`.
- `[opened 2026-06-16]` **MUJ's prescribed textbook** for MAS2001 — using canonical engineering-
  statistics texts (Walpole/Ross/Montgomery) as the tier-1 anchor pending the official list.
- `[opened 2026-06-17]` **No PYQ/PPT ingested** — `exam-map.md` is a provisional stub; revision
  priority is inferred, not evidence-based. *Resolve by:* dropping MTE+ETE papers + PPTs into
  `../exam-pack/` and rebuilding the exam-map. (See `../../research-engine/exam-resources.md`.)
- `[opened 2026-06-19]` **Best Berry–Esseen constant C** — `contested`/open math problem (best known
  C < 0.4748, lower bound ≈0.409); exact optimum unresolved. *Resolve by:* nothing to resolve — teach
  as "≈0.47, not pinned"; recheck on re-entry for any new best bound. (`stage-2/01` §5.)
- `[opened 2026-06-19]` **Stage-2 scope vs MUJ syllabus** — whether MAS2001 actually examines the
  Stage-2 topics (CRLB/Fisher, UMVUE, Neyman–Pearson/LRT/Wilks, multiple-comparison methods, SLLN) or
  only the Stage-1 catalogue. `uncertain`. *Resolve by:* the official handout + PYQs (same blocker as
  unit boundaries). Stage-2 is deep-structure surplus regardless; this only affects exam-weighting.
- `[resolved 2026-06-19]` ~~Misconceptions M3/M7/M11 unsourced~~ — verified + promoted to `settled`
  (see `misconceptions.md`, `stage-2/sources.md`).
