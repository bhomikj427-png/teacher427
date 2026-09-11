# Unit 4 — Tests of Statistical Hypothesis

> Confidence: `settled` (canonical; Walpole 9e / Montgomery & Runger). The second inverse move:
> decide between claims about a parameter. Same skeleton for every test (big idea 5, `00-map.md`).

## Stage 1 (MUJ level)

### The universal skeleton (learn once, reuse for every test)
1. **Hypotheses:** null **H₀** (the status quo / "no effect") vs alternative **H₁**.
2. **Test statistic:** a statistic whose **sampling distribution under H₀ is known** (z, t, χ², F).
3. **Errors & significance:**
   - **Type I error** = reject H₀ when it's true; its probability is **α** (the chosen significance
     level). **Type II error** = fail to reject H₀ when it's false, probability **β**; **power =
     1−β**.
   - *Mechanism:* α is the false-alarm rate you're willing to tolerate; it sets the threshold.
4. **Critical region / decision:** reject H₀ if the statistic falls in the rejection region (or
   equivalently if **p-value < α**). The p-value = P(a result this extreme or more | H₀ true).
5. **Standard error (SE):** the SD of the sampling distribution of the statistic (e.g. σ/√n for X̄);
   the test statistic is (estimate − H₀ value)/SE.

### The standard tests (instances of the skeleton)
- **Test about one mean:** z-test (σ known / large n) or **t-test** (σ unknown, df=n−1):
  t=(x̄−μ₀)/(s/√n).
- **Equality of two means:** two-sample t (pooled or Welch depending on equal-variance assumption).
- **Test of variances:** **χ² test** for one variance ((n−1)s²/σ₀² ~ χ²_{n−1}); **F test** for the
  ratio of two variances.
- **Chi-square tests:** goodness-of-fit and independence in contingency tables —
  χ² = Σ (Oᵢ−Eᵢ)²/Eᵢ (observed vs expected counts). *Mechanism:* large when data deviate from the
  model's expected frequencies.
- **ANOVA (Analysis of Variance):** compare ≥3 means by an **F = (between-group variance)/(within-
  group variance)**. *Mechanism:* if group means truly differ, between-group variance inflates
  relative to within; F gets large. (One-way ANOVA at Stage 1.)

### Critical reading (★ threshold — see `misconceptions.md`)
- "Fail to reject H₀" ≠ "H₀ is true" — absence of evidence isn't evidence of absence.
- The p-value is **not** P(H₀ true); α is **not** the probability you made a mistake on this test.
- Statistical significance ≠ practical importance (large n can make trivial effects "significant").

### Worked-problem patterns
- Pick the right test from the question (one mean? two means? variance? counts? ≥3 groups?).
- State H₀/H₁, compute the statistic, compare to the critical value / get the p-value, conclude **in
  context** at the stated α.
- One-tailed vs two-tailed selection and its effect on the critical value.
- Identify/limit Type I vs Type II error in a described scenario.

---
**Stage 2 (deep structure) — ✓ BUILT (2026-06-19):** lives separately in
`stage-2/04-hypothesis-testing.md` — kept out of this exam file on purpose. *Adds:* Neyman–Pearson lemma & most-powerful
tests; the likelihood-ratio test as the unifying construction; power-function analysis & sample-size
determination; the duality between confidence intervals and tests; exact derivation of the F and χ²
distributions from Normal sampling; multiple-comparison corrections and the replication-crisis
critique of p<0.05.
