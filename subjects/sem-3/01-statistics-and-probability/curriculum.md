# MAS2001 Statistics & Probability — Curriculum (Stage-1, derived from knowledge-base/00-map.md)

> Ordered objectives, **prerequisites first** (cognitive-load order). Strictly downstream of the
> map's prerequisite graph. Derived from a **Stage-1 (MUJ-level)** knowledge base — exam-ready;
> Stage-2 depth will deepen each unit later. Mastery-gated: a unit opens only when the prior is
> *demonstrated*. ★ marks threshold units (extra time + productive-failure setups).
>
> **No learner activated yet** — this curriculum exists because the demo built the KB. When the
> learner starts this subject, the engine diagnoses level first, then begins.

## U1 — Probability & Random Variables ★ (sampling-distribution + CLT thresholds)
- Probability axioms, conditional probability, Bayes, independence.
- RV as a function; CDF; pmf vs pdf; P(X=x)=0 for continuous.
- Expectation (linearity, LOTUS), variance (E[X²]−μ², Var of independent sums).
- Chebyshev → LLN → **CLT** (the bridge to inference).
- Outcome: computes E/Var from a distribution; applies CLT to a sample-mean probability; explains
  *why* the sample mean is ≈Normal with SD σ/√n.

## U2 — Probability Distributions
- Binomial, Poisson (as Binomial limit), Uniform, Normal (CLT attractor), Exponential (memoryless).
- For each: the generating *story* (mechanism), pmf/pdf, mean, variance; the connecting web.
- Outcome: picks the right distribution from a word problem by its story; standardizes & uses the
  Normal table; handles Binomial→Poisson/Normal approximations and Poisson↔Exponential duality.

## U3 — Theory of Estimation (depends on U1's sampling-distribution idea)
- Estimator properties (unbiased/consistent/efficient); MoM and **MLE** (log-likelihood method);
  sufficiency (factorization); Bayesian estimation (prior→posterior); **confidence intervals** for
  a mean (z vs t).
- Outcome: derives an MLE/MoM estimator; builds a correct CI; states the *procedure* meaning of a CI
  (not the misinterpretation).

## U4 — Tests of Statistical Hypothesis ★ (p-value / significance meaning threshold)
- The universal test skeleton; Type I/II errors, α, β, power; critical region & p-value.
- One/two-mean tests (z, t); variance tests (χ², F); chi-square goodness-of-fit & independence;
  one-way ANOVA.
- Outcome: selects the right test, runs it, and concludes *in context* at a stated α; avoids the p-
  value / significance misinterpretations.

## Teaching notes carried from the map
- Budget extra time on the **sampling distribution** (★) and **CLT** — most downstream errors trace
  to them (`knowledge-base/misconceptions.md` M4/M5).
- Confidence flags survive into teaching: present the CI/p-value *meanings* carefully (M6/M8–M10);
  the unit-boundary `uncertain` flag means re-confirm scope against the official handout before a
  graded push.
