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

### Table values the course's questions use (added 2026-11-16, study-pack S0)
Every table value printed in the MTE 2026 paper, Assignments 2, 4, 5 and the LMS slides, recomputed
with `scipy.stats` (norm, t, chi2, f): confidence `settled` (exact computation of the standard
distributions' quantiles and areas). "Area 0..z" = P(0 < Z < z).

| Value | Exact (4 d.p.) | Printed in |
|---|---|---|
| area 0..0.1 / 0.24 / 0.5 / 0.6 | 0.0398 / 0.0948 / 0.1915 / 0.2257 | A2 C2 (as 0.04, 0.095), A2 B3, CLT slides |
| area 0..0.94 / 1.04 / 1.2 / 1.28 / 1.34 | 0.3264 / 0.3508 / 0.3849 / 0.3997 / 0.4099 | CLT slides, A2 B6 (0.35, 0.40), A2 B3–B4, A2 C2 (0.41) |
| area 0..1.5 / 1.6 / 1.8 / 2 / 2.36 | 0.4332 / 0.4452 / 0.4641 / 0.4772 / 0.4909 | A2 B4, MTE C1(a), CLT slides |
| P(−1 < Z < 1); P(Z > 1.5) | 68.27%; 6.68% | A2 MCQ 11; CLT slides |
| z for 95% / 99% two-sided | 1.960 / 2.576 | A4 B1–B3 |
| t(5) one-sided 5% | 2.015 (printed 2.02) | A5 C4 |
| t(9) two-sided 5% | 2.262 | A4 B4, A5 B4, C1 |
| t(17) two-sided 5% | 2.110 | A5 B1 |
| t(19) two-sided 10% / 5% / 1% | 1.729 / 2.093 / 2.861 | A4 B5, A5 D2 |
| t(20) two-sided 5% | 2.086 (not printed; needed) | A5 C2 |
| χ²(1) 5%; χ²(4) 1% | 3.841; 13.277 | A5 B5, C3, D3; A5 B6 |
| F(7,10) upper 5% | 3.136 (printed 3.14) | A5 C5 |
| F(15,12) upper 0.5% (= two-sided 1%) | 4.721 (upper 1% would be 4.010) | A5 B2, B3 |
| F(2,12) upper 5% | **3.885** (key prints 19.41 = F(12,2): slip, decision flips) | A5 C6 |
| F(4,4) upper 5% | **6.388** (key prints 5.19 = F(4,5): slip) | A5 D1 |
| F(2,15) upper 1% | 6.359 | A5 D4 |

**Rule the slips teach:** F(ν₁, ν₂) takes the numerator's df first; swapping them changes the value.

### Prescribed-textbook locations (G&K, read on the PDF text layer 2026-11-17, study-pack S6) — `settled`
- **§12.5** null hypothesis H₀: "a definite statement about the population parameter", "usually a hypothesis
  of no difference". **§12.5.1** alternative H₁: any hypothesis complementary to H₀; for H₀: μ = μ₀,
  H₁: μ ≠ μ₀ (two-tailed), μ > μ₀ (right-tailed) or μ < μ₀ (left-tailed).
- **§12.6** Type I error: reject H₀ when it is true; Type II error: accept H₀ when it is wrong (H₁ true);
  in quality control α and β are the **producer's risk** and **consumer's risk**.
- **§12.7** critical region ω: the region of the sample space that amounts to rejecting H₀;
  P(t ∈ ω ∣ H₀) = α, P(t ∈ ω̄ ∣ H₁) = β; ω̄ is the acceptance region; α is fixed before sampling.
  **§12.7.1** one-tailed test when H₁ is one-sided, two-tailed when H₁ is ≠; the critical region lies in
  one tail or both. **§12.7.2** critical (significant) value: separates the critical and acceptance
  regions; depends on α and on the tails; the one-tailed value at α equals the two-tailed value at 2α.
  Table of critical z: two-tailed 2·58 / 1·96 / 1·645, right-tailed 2·33 / 1·645 / 1·28 (α = 1%, 5%, 10%).
- **§12.8** steps: H₀ · H₁ (tails) · level of significance (fixed in advance) · test statistic
  Z = (t − E(t))/S.E.(t) under H₀ · compare with the tabulated value and conclude.
- **§16.2.4–16.2.7** critical region W and acceptance region W̄; α = P(x ∈ W ∣ H₀) is the size of the
  critical region (level of significance); β = P(x ∈ W̄ ∣ H₁); 1 − β is the power function, its value at
  a parameter point the power of the test there. **§16.3** steps of a testing problem (W chosen,
  reject H₀ if t ∈ W).

---
**Stage 2 (deep structure) — ✓ BUILT (2026-06-19):** lives separately in
`stage-2/04-hypothesis-testing.md` — kept out of this exam file on purpose. *Adds:* Neyman–Pearson lemma & most-powerful
tests; the likelihood-ratio test as the unifying construction; power-function analysis & sample-size
determination; the duality between confidence intervals and tests; exact derivation of the F and χ²
distributions from Normal sampling; multiple-comparison corrections and the replication-crisis
critique of p<0.05.
