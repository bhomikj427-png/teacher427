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

### Prescribed-textbook locations (G&K, checked on the PDF text 2026-11-17, sprint S4) — `settled`
- §7.2 Binomial: pmf C(n, x)pˣqⁿ⁻ˣ; central moment μ₂ = npq, mean np; **Example 7.4** is the
  MTE B3 irregular-die question verbatim (P(X = 5) = 2P(X = 4) ⇒ p = 5/8). **Example 7.7**: "mean 3,
  variance 4" is impossible for a binomial (npq < np since q < 1).
- §7.3 Poisson: obtained as the limit of the binomial with n → ∞, p → 0, np = λ finite; additive
  (reproductive) property: independent P(λ₁) + P(λ₂) = P(λ₁ + λ₂); mean = variance = λ.
- §8.1 Rectangular (uniform) distribution on (a, b): f = 1/(b − a); "rectangular" because y = f(x) is a
  rectangle over (a, b); moments in §8.1.1 (mean (a + b)/2, variance (b − a)²/12).
- §8.6 Exponential: **Example 8.40** "the exponential distribution lacks memory": P(Y ≥ x | X ≥ a) =
  P(X ≥ x), Y = X − a. Ch. 8 exercise 7(a) is Assignment 2 B5 verbatim: P(X < 1 | X < 2) with mean 2,
  printed answer (1 − e^{−θ})/(1 − e^{−2θ}), θ = ½ = 0.6225 (the assignment key's 0.5679 disagrees).
- (S5, PDF text layer, 2026-11-17) §8.2 Normal: first found by De Moivre (1733) as a limit of the binomial
  (§8.2.1: n → ∞, neither p nor q very small); §8.2.2 "chief characteristics": bell-shaped, symmetric
  about μ, mean = median = mode, and areas P(μ ± σ) = 0·6826, P(μ ± 2σ) = 0·9544, P(μ ± 3σ) = 0·9973
  (G&K's 4-place values; exact 0.68269, 0.95450, 0.99730, which the course writes 68.27%, 95.45%, 99.73%).
- §8.10 Central Limit Theorem; Lindeberg–Lévy form: X₁, …, Xₙ independent and identically distributed with
  mean μ₁, variance σ₁² ⇒ the sum Sₙ is asymptotically normal with mean nμ₁, variance nσ₁²; written for the
  mean (eq. 8·31-2): P(a ≤ (X̄ₙ − μ₁)/(σ₁/√n) ≤ b) → Φ(b) − Φ(a) as n → ∞. The "n ≥ 30" cut-off is a
  course/slide rule of thumb, not in G&K (stage-2 U1 §5 says the same).
- Ch. 12 §12.3: **parameter** = a constant of the population (μ, σ²); **statistic** = a measure computed
  from the sample alone (x̄, s²); §12.3.1 sampling distribution = the values of a statistic over all
  possible samples; §12.3.2: "the standard deviation of the sampling distribution of a statistic is known
  as its standard error"; for the mean, S.E. = σ/√n (follows from Var(X̄) = σ²/n for independent draws).

---
**Stage 2 (deep structure) — ✓ BUILT (2026-06-19):** lives separately in
`stage-2/02-probability-distributions.md` — kept out of this exam file on purpose. *Adds:* the exponential family and why these
distributions share structure; MGFs and deriving moments from them; sums/convolutions (sum of
Poissons is Poisson; sum of exponentials is Gamma/Erlang); the Normal as max-entropy for fixed
variance; exact validity bounds of the Binomial→Poisson/Normal approximations.
