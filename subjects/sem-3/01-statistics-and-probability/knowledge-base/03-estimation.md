# Unit 3 — Theory of Estimation

> Confidence: `settled` (canonical; Walpole 9e / Montgomery & Runger / Ross). The "data → parameter"
> inverse move. Rests on the **sampling distribution** idea (U1 ★ threshold).

## Stage 1 (MUJ level)

### Framing
- A **statistic** is any function of the sample (e.g. X̄, S²). It is itself a random variable with a
  **sampling distribution** (★ threshold — see `00-map.md`). An **estimator** θ̂ is a statistic used
  to guess a parameter θ. Properties we want: **unbiased** (E[θ̂]=θ), **consistent** (θ̂→θ as n→∞),
  **efficient** (smallest variance).

### Point estimation — two construction methods
- **Method of Moments (MoM):** set sample moments equal to population moments and solve for the
  parameters. *Mechanism:* moments are functions of the parameters; invert them. Quick, not always
  efficient.
- **Maximum Likelihood (MLE):** write the likelihood L(θ)=∏ f(xᵢ;θ); maximize (usually via
  log-likelihood ℓ(θ)=Σ log f(xᵢ;θ), set ℓ′(θ)=0). *Mechanism:* pick the parameter under which the
  observed data were most probable. Standard worked cases: MLE of Binomial p = x̄/n; of Poisson λ =
  x̄; of Normal μ = x̄ (and σ̂² = (1/n)Σ(xᵢ−x̄)², the biased version).
- **Sufficient statistic:** a statistic that captures all sample information about θ (formally, the
  conditional distribution of the data given it doesn't depend on θ; identify via the
  **factorization criterion** L = g(T(x),θ)·h(x)). *Mechanism:* you can throw away the rest of the
  data without losing information about θ.

### MLE and MoM properties — Gupta & Kapoor ch. 15 (verified on the page images, 2026-11-16, S3)
- §15.10 lists the methods of point estimation (MLE and MoM among them). §15.11: likelihood
  L = Π f(xᵢ, θ) (eq. 15·53); the MLE θ̂ is the value of θ that makes L greatest. `settled`
- Thm 15.11: under regularity conditions the MLE is **consistent**. Remark: the MLE of σ² (normal),
  s² with divisor n, is consistent but **not unbiased**. `settled`
- Thm 15.13: the MLE is **asymptotically normal** (large n). Thm 15.14: if a most efficient
  estimator exists, the likelihood equation gives it. Thm 15.15: if a sufficient estimator exists,
  the MLE is a function of it. Thm 15.17 (**invariance**): if θ̂ is the MLE of θ, then γ(θ̂) is the
  MLE of γ(θ). `settled`
- §15.13 MoM: equate the first k population moments μ′ᵣ (functions of the k parameters) to the
  sample moments m′ᵣ = (1/n)Σxᵢʳ and solve. Remarks: MoM estimators are consistent and asymptotically
  normal, but **generally less efficient than MLE**; they coincide with MLE when the density has the
  exponential-family form. `settled`
- Exercises (ch. 15, p. idx 1192 of the PDF): 20(b) f(x, θ) = θe^(−θx) (the book prints **θ**, not α);
  21 U(a, b) by MoM; 23(b) f(x) = (1 + θ)x^θ, 0 < x < 1, by MoM and MLE. `settled` (as printed)

### Bayesian estimation (named in the syllabus)
- Treat θ as random with a **prior** π(θ); update with data via Bayes to the **posterior**
  π(θ|x) ∝ L(x|θ)π(θ); the estimate is a posterior summary (mean/mode). *Mechanism:* inference is
  belief-updating; contrast with the frequentist MLE/MoM view (this contrast is itself worth
  teaching — not one side as "the truth").

### Interval estimation — confidence intervals for a mean
- **σ known (or n large, CLT):** CI for μ is **x̄ ± z_{α/2}·σ/√n**. *Mechanism:* X̄ ~ N(μ, σ²/n) by
  CLT (U1), so a centered z-band has the stated coverage.
- **σ unknown, n small, Normal data:** use **t** with n−1 df: **x̄ ± t_{α/2,n−1}·s/√n** (the t
  accounts for estimating σ by s — heavier tails).
- **Meaning (★ threshold, see misconceptions):** a 95% CI means the *procedure* covers the true μ
  95% of the time over repeated samples — **not** "95% probability μ is in this particular interval."
- **G&K §15.15** (PDF text layer, 2026-11-17, study-pack S6; `settled`): confidence interval (t₁, t₂) with
  P(t₁ < θ < t₂) = 1 − α; t₁, t₂ are the confidence limits, 1 − α the confidence coefficient; for the
  normal mean with σ known, x̄ ± 1·96 σ/√n (95%) and x̄ ± 2·58 σ/√n (99%); remark: σ unknown and n small
  → x̄ ± t_α s/√n with t for n − 1 d.f.

### Worked-problem patterns
- Derive an MLE/MoM estimator for a given distribution's parameter.
- Check unbiasedness / find the bias (e.g. why the n-divisor variance is biased, n−1 fixes it).
- Build a CI for a mean (choose z vs t correctly by what's known and n).
- Use the factorization criterion to identify a sufficient statistic.

---
**Stage 2 (deep structure) — ✓ BUILT (2026-06-19):** lives separately in `stage-2/03-estimation.md` — kept
out of this exam file on purpose. *Adds:* Cramér–Rao lower bound & Fisher information;
Rao–Blackwell and minimum-variance unbiased estimation; asymptotic normality & efficiency of the
MLE; conjugate priors and the full Bayesian decision-theory framing; exact derivation of the t and
χ² sampling distributions.
