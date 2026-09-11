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
