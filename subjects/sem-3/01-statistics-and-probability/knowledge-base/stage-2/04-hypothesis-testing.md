# Unit 4 — Tests of Statistical Hypothesis — STAGE 2 (deep structure)

> **Stage 2 — IIT/Ivy depth.** Built on top of the exam-ready Stage-1 file
> (`../04-hypothesis-testing.md`), not replacing it. Stage 1 gave the *skeleton* and a *catalogue* of
> tests (z, t, χ², F, ANOVA). Stage 2 shows the catalogue is **one construction** (the
> likelihood-ratio test), proves it is **optimal** (Neyman–Pearson), explains **where the test
> distributions come from**, makes "power" **quantitative**, links tests to the U3 confidence
> intervals (**duality**), and confronts the **replication-crisis critique** of p < 0.05 head-on.
> Confidence `settled` unless marked; load-bearing specifics verified 2026-06-19 (`stage-2/sources.md`).

---

## 1. Neyman–Pearson — the optimal test exists, and it's the likelihood ratio

For the cleanest case — **simple H₀: θ=θ₀ vs simple H₁: θ=θ₁** — there is a *best possible* test.

**Neyman–Pearson lemma.** Among all tests with Type I error ≤ α, the one with the **highest power**
(smallest β) rejects H₀ when the **likelihood ratio**
  Λ(x) = L(x; θ₁) / L(x; θ₀) ≥ k,
with k chosen so the size is exactly α (randomizing on the boundary Λ=k if needed for exact α).
*(Verified: Stanford Stats 300A L13; Wikipedia "Neyman–Pearson lemma"; CUNY MTH410.)* `settled`
- *Mechanism:* to buy the most power per unit of Type-I risk, spend your rejection region on the points
  where the data are *most* relatively likely under H₁ — i.e. order outcomes by the likelihood ratio
  and reject from the top until you've used up α. It's a greedy "best bang per α" argument.
- **This is the deep reason Stage-1's tests look the way they do:** the z- and t-statistics *are*
  monotone functions of a likelihood ratio for the Normal model, so "reject when |t| large" is the
  NP-optimal rule in disguise.

**From simple to real (composite) hypotheses:**
- **Karlin–Rubin:** if the family has **monotone likelihood ratio** in a statistic T, the one-sided
  test "reject if T > c" is **uniformly most powerful (UMP)** for one-sided H₁ — no single best test
  generally exists for two-sided alternatives. `settled`
- *Why two-sided tests aren't UMP:* you can't simultaneously maximize power against θ>θ₀ and θ<θ₀ with
  one rejection region — hence the practical retreat to likelihood-ratio / unbiased tests.

---

## 2. The likelihood-ratio test (LRT) — the one construction behind the catalogue

Stage 1's z/t/χ²/F/ANOVA are not five inventions; they are the **generalized likelihood-ratio test**
applied to different models.

**GLRT statistic:** λ = [ sup_{θ∈Θ₀} L(θ) ] / [ sup_{θ∈Θ} L(θ) ]  — best fit under H₀ ÷ best fit
overall (0 ≤ λ ≤ 1; reject when λ small = H₀ fits much worse). `settled`

**Wilks' theorem (the asymptotic null distribution):** under H₀ and regularity, as n→∞,
  −2 log λ →ᵈ χ²_d,  with d = dim(Θ) − dim(Θ₀) (number of free parameters the null fixes).
*(Verified: Wikipedia "Wilks' theorem"; stephens999 fiveMinuteStats; Bohrium.)* `settled`
- **Limit (UG textbook never says this):** Wilks fails when the true parameter is on the **boundary**
  of the space (e.g. testing a variance component = 0); the limit becomes a mixture of χ², not a plain
  χ². `settled`
- *Unification payoff:* the **Pearson χ² goodness-of-fit** statistic Σ(Oᵢ−Eᵢ)²/Eᵢ is a second-order
  Taylor approximation to −2 log λ for the multinomial — which is **why** it is χ²-distributed with
  df = (categories − 1 − #estimated params). The "(O−E)²/E" formula and Wilks are the *same* test.
  Likewise the t, F and ANOVA tests are LRTs for Normal models. So the whole unit collapses to one idea.

---

## 3. Where the test distributions come from (χ², t, F from Normal sampling)

Carried over from Unit 3 §5 (the constructions live there) and completed for the two-sample / ANOVA
tests:
- **χ²_k = Σ Zᵢ²** (k iid standard normals); **(n−1)S²/σ² ~ χ²_{n−1}** → the one-variance test. `settled`
- **t_k = Z / √(V/k)**, Z~N(0,1), V~χ²_k independent → the one-mean and two-mean t-tests. `settled`
- **F_{d₁,d₂} = (V₁/d₁) / (V₂/d₂)**, V₁~χ²_{d₁}, V₂~χ²_{d₂} independent → the ratio is **F**.
  *Mechanism for Stage-1's two tools:* the **two-variance F-test** is (S₁²/σ₁²)/(S₂²/σ₂²), a ratio of
  two scaled χ²; **ANOVA's F** = (between-group MS)/(within-group MS) is the *same* F because, under
  H₀ (equal means), both mean-squares are independent unbiased estimates of σ², so their ratio is
  F-distributed. ANOVA is "an F-test on a variance decomposition," not a new method. `settled`
- *Deep structure:* **every Stage-1 test statistic is built from independent Normals → χ²/t/F.** The
  CLT (Unit 1) is what lets these Normal-theory tests apply approximately to non-Normal data at large n.

---

## 4. Power, quantified — error trade-offs and sample size

Stage 1 named α, β, power = 1−β. Stage 2 makes them a *design tool*.
- **Power function:** π(θ) = P(reject H₀ | true parameter θ). π(θ₀) = α; π rises toward 1 as θ moves
  into H₁. The whole curve, not a single number, characterizes a test. `settled`
- **The α–β trade-off is structural:** for fixed n, shrinking α (more conservative) **raises** β (lower
  power) — you can't reduce both at once; only **more data** (larger n) buys down both. *Mechanism:*
  moving the critical value trades the two tail areas against each other; increasing n shrinks the SE
  (σ/√n), separating the H₀ and H₁ sampling distributions so both errors fall. `settled`
- **Sample-size determination (one-mean z, two-sided):** to detect a true difference δ = μ₁−μ₀ with
  power 1−β at level α, n ≈ ( (z_{α/2} + z_β) σ / δ )². *Mechanism:* require the alternative's sampling
  distribution to sit far enough past the critical value that only β of it falls in the
  "fail-to-reject" zone. Shows concretely that **detecting a small effect needs large n** — the same
  fact that makes "significant ≠ important" (M10) cut the other way: tiny effects become detectable. `settled`
- **Effect size** (the missing Stage-1 concept): standardized effect (e.g. Cohen's d = δ/σ) is what
  power actually depends on — not the raw difference. This is the antidote to M10: report effect size +
  CI, not just "p < α".

---

## 5. Tests and confidence intervals are the same thing (duality — links to Unit 3)

**Duality theorem.** A level-α two-sided test of H₀: θ=θ₀ **fails to reject** θ₀ **iff** θ₀ lies inside
the (1−α) confidence interval for θ. Equivalently: *the confidence interval is exactly the set of null
values that would not be rejected.* `settled`
- *Mechanism:* both are built from the same pivot (estimate − θ₀)/SE; "|pivot| < critical value" is
  simultaneously the acceptance region and the CI inequality.
- *Payoff:* this is why the U3 CI and the U4 test are never independent facts — invert a test to get a
  CI, or read a CI as a family of tests. It also reframes M6/M10: a CI shows the *range of plausible
  effects* (magnitude + uncertainty), which a bare p-value hides — the practical reason modern practice
  prefers reporting intervals.

---

## 6. The replication crisis — the honest critique of p < 0.05 (`contested`, teach as live debate)

This is a genuine, ongoing methodological debate; the base teaches it as such (protocol §4), not as a
settled recipe.
- **ASA 2016 statement (six principles, Wasserstein & Lazar, *The American Statistician*).** Key ones:
  (1) a p-value measures incompatibility of the data with a specified model; (2) a p-value is **not**
  P(H₀ true) and **not** the probability the result is due to chance (re-states M8 with authority);
  (3) conclusions should **not** be based on whether p passes a threshold; (4) proper inference needs
  full reporting and transparency; (5) p-value ≠ effect size or importance (M10); (6) a p-value alone
  is a poor measure of evidence. *(Verified: amstat.org p-value statement PDF; Wasserstein & Lazar
  2016, TAS.)* `settled` (that the ASA said this) / `contested` (what to do instead).
- **Why a crisis:** the **file-drawer effect** (only significant results get published), **p-hacking /
  multiple comparisons**, and **low power** together make a "significant" finding far less likely to be
  true than the α=0.05 label suggests. *Mechanism:* if many analyses are run and only p<0.05 ones are
  reported, the published Type-I rate is nowhere near 5%. `settled`
- **The multiplicity fix — multiple-comparison corrections:**
  - **Family-wise error rate (FWER):** **Bonferroni** — test each of m hypotheses at α/m so the chance
    of *any* false positive stays ≤ α. Simple, conservative (low power for large m). `settled`
  - **False discovery rate (FDR):** **Benjamini–Hochberg** — control the *expected proportion* of false
    positives among rejections; far more powerful for large-scale testing (genomics, screening). `settled`
- **Proposed responses (genuinely contested — present as options, not a verdict):** lower the threshold
  to 0.005; abandon "statistical significance" as a label (Amrhein/Greenland/McShane); shift to
  estimation + CIs (§5); adopt Bayesian/Bayes-factor reasoning (Unit 3 §6). The base does **not** pick
  a winner. `contested`

---

## 7. Cross-topic unification (the expert's map)

- **One construction:** Neyman–Pearson (optimal for simple) → LRT (general) → Wilks (its null χ²) →
  every Stage-1 test (z/t/χ²/F/ANOVA/GOF) as an instance. The "catalogue" is one likelihood idea.
- **One likelihood theory with Unit 3:** score/information/MLE (estimation) and LRT/NP (testing) are
  the same log-likelihood differentiated and compared. Estimation and testing are dual faces; §5 makes
  the CI↔test duality explicit.
- **Built on the sampling distribution (★ threshold) and the CLT (Unit 1):** test statistics are
  functions of Normals → χ²/t/F; the CLT extends them approximately to non-Normal data. The same √n.
- **NP detection ↔ ECE (forward link):** the Neyman–Pearson detector is the foundation of **radar /
  communication receiver design and detection theory** (ECE signal detection) — same lemma, engineering
  dress. Bridges to **05 Signals & Systems**.

---

## 8. Stage-2 exit check ("why, not what")

- *Is there a provably best test?* → §1: yes, for simple-vs-simple — the likelihood ratio
  (Neyman–Pearson); UMP for one-sided MLR families; generally none for two-sided.
- *What unifies z/t/χ²/F/ANOVA/GOF?* → §2: all are (generalized) likelihood-ratio tests; −2 log λ ~ χ²_d
  (Wilks); even Pearson's (O−E)²/E is an approximation to it.
- *Where do χ², t, F come from?* → §3: sums/ratios of independent Normals; ANOVA's F is a variance-ratio.
- *Why can't you make α and β both tiny?* → §4: fixed-n trade-off; only larger n separates the
  distributions; sample size n ≈ ((z_{α/2}+z_β)σ/δ)².
- *How are CIs and tests related?* → §5: a CI is the set of non-rejected nulls (duality).
- *Why is "p<0.05" under fire?* → §6: file-drawer + p-hacking + low power inflate the real false-positive
  rate; fixes (Bonferroni/FDR, effect sizes + CIs, lower thresholds, Bayesian) are genuinely contested.

Open items → `../00-map.md`: whether MUJ expects Neyman–Pearson/LRT/Wilks and multiple-comparison
methods or only the Stage-1 test catalogue (scope, `uncertain` pending handout); "what should replace
p<0.05" stays `contested` on purpose.
