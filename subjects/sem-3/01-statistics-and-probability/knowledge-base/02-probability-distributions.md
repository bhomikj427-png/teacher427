# Unit 2 — Probability Distributions

> Confidence: `settled` (canonical results; Walpole 9e / Ross; standard moment formulas). The five
> named distributions in the official syllabus + when each arises (mechanism, not just formulas).

## Stage 1 (MUJ level)

For each: the *generating story* (mechanism — when does this distribution arise?), pmf/pdf, and
mean/variance. **The story is the point** — experts pick a distribution by recognizing its
mechanism, not by matching a formula.

### Discrete

**Binomial(n, p)** — *story:* number of successes in n independent Bernoulli(p) trials.
- pmf: P(X=k)=C(n,k) pᵏ(1−p)ⁿ⁻ᵏ, k=0…n.  **E=np, Var=np(1−p).**
- *Mechanism:* sum of n iid Bernoulli(p); mean/var follow by linearity & independence (U1).

**Poisson(λ)** — *story:* count of rare events in a fixed interval; the **limit of Binomial** as
n→∞, p→0 with np→λ.
- pmf: P(X=k)=e⁻λ λᵏ/k!, k=0,1,2,…  **E=λ, Var=λ** (mean = variance is the Poisson signature).
- *Mechanism:* law of rare events (Poisson limit theorem — verified orientation via Wikipedia,
  2026-06-16). Used for arrivals, defects, photon counts.

### Continuous

**Uniform(a, b)** — *story:* "no information beyond the range"; all points in [a,b] equally likely.
- pdf: f(x)=1/(b−a) on [a,b].  **E=(a+b)/2, Var=(b−a)²/12.**

**Normal(μ, σ²)** — *story:* the CLT attractor; sums/averages of many small independent effects.
- pdf: f(x)=1/(σ√(2π)) · exp(−(x−μ)²/(2σ²)).  **E=μ, Var=σ².**
- **Standardization:** Z=(X−μ)/σ ~ N(0,1); read probabilities from the standard-normal table.
- *Mechanism:* its dominance is *explained by* the CLT (U1), not assumed — this is the conceptual
  link the exam (and Stage 2) cares about.

**Exponential(λ)** — *story:* waiting time until the next Poisson event; the **memoryless**
continuous distribution.
- pdf: f(x)=λe⁻λˣ, x≥0.  **E=1/λ, Var=1/λ².**  CDF F(x)=1−e⁻λˣ.
- **Memorylessness:** P(X>s+t | X>s)=P(X>t) — the unique continuous distribution with this property;
  *mechanism:* the process "forgets" elapsed waiting. (Pairs with Poisson: counts vs gaps.)

### The connecting web (deep structure, kept at Stage-1 depth)
- Binomial --(n→∞, np→λ)--> Poisson;  Poisson counts ↔ Exponential gaps;  sums/means of *any* of
  these --(CLT)--> Normal. Recognizing these links is how an expert navigates the unit.

### Worked-problem patterns
- Identify the right distribution from a word problem (the story), then plug E/Var or compute a
  probability.
- Normal: standardize and use the Z-table; "find x such that P(X≤x)=0.95".
- Binomial→Poisson or Binomial→Normal approximation for large n (and when each is valid).
- Exponential/Poisson duality problems (arrivals per hour ↔ time between arrivals).

---
**Stage 2 (deep structure) — ✓ BUILT (2026-06-19):** lives separately in
`stage-2/02-probability-distributions.md` — kept out of this exam file on purpose. *Adds:* the exponential family and why these
distributions share structure; MGFs and deriving moments from them; sums/convolutions (sum of
Poissons is Poisson; sum of exponentials is Gamma/Erlang); the Normal as max-entropy for fixed
variance; exact validity bounds of the Binomial→Poisson/Normal approximations.
