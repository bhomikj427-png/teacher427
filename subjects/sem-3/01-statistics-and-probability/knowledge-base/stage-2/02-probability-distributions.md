# Unit 2 — Probability Distributions — STAGE 2 (deep structure)

> **Stage 2 — IIT/Ivy depth.** Built on top of the exam-ready Stage-1 file
> (`../02-probability-distributions.md`), not replacing it. Stage 1 listed five distributions and
> their stories; Stage 2 shows they are **instances of one structure** (the exponential family),
> gives the **machine that generates their moments** (MGF/CF), explains **why their sums stay in the
> family** (convolution), and states **exactly when the famous approximations are valid**.
> Confidence `settled` unless marked; load-bearing specifics verified 2026-06-19 (`stage-2/sources.md`).

---

## 1. The exponential family — the structure under four of the five

Most named distributions are not a zoo; they are one template. A family is **exponential** if its
pmf/pdf can be written in **canonical form**
  p(x; η) = h(x) · exp( η·T(x) − A(η) )
where η = **natural parameter**, T(x) = **natural sufficient statistic**, A(η) = **log-partition
(cumulant) function**, h(x) = base measure. *(Verified: Stanford Stats 300A L2; Purdue Dasgupta
"Exponential Family"; Brown digest.)* `settled`

Members from this unit: **Binomial** (fixed n), **Poisson**, **Normal**, **Exponential** (and Gamma,
Bernoulli) are all exponential-family. **Uniform(a,b) is NOT** — its support depends on the
parameters, which breaks the form (a genuinely important exception). `settled`

**Why this is the deep structure, not trivia:**
- **A(η) is a moment machine.** dA/dη = E[T(X)], d²A/dη² = Var(T(X)). The mean and variance of the
  whole family come from differentiating one convex function. (This is *why* §2's MGF trick works —
  A is essentially the cumulant generating function.) `settled`
- **It explains Unit 3's "sufficient statistic" (forward link).** The factorization criterion
  Stage-1 U3 stated falls out instantly: T(x) in the exponent **is** the sufficient statistic, and
  Σᵢ T(xᵢ) is sufficient for an iid sample. The exponential family is exactly the class with a
  **fixed-dimension** sufficient statistic regardless of sample size (Pitman–Koopman–Darmois). `settled`
- **It explains Unit 3's conjugate priors (forward link).** Every exponential family has a conjugate
  prior, also exponential-family — that's why the Bayesian updates in U3 are clean.
- **Convexity:** the natural parameter space is convex and A(η) is convex — which underwrites the
  uniqueness of the MLE in these models. `settled`

---

## 2. Generating moments mechanically — MGF and CF

Stage 1 quoted E and Var for each distribution as facts to memorize. They all come from **one
operation**: differentiate a transform.

**MGF:** M_X(t) = E[e^{tX}]. Then M'(0) = E[X], M''(0) = E[X²], and in general M⁽ᵏ⁾(0) = E[Xᵏ].
*Mechanism:* e^{tX} = Σ (tX)ᵏ/k!, so M(t) is the exponential generating function of the moments.
**Caveat:** the MGF may not exist (heavy tails); the **CF** φ_X(t)=E[e^{itX}] (Unit 1 §4) always
does and plays the same role rigorously. `settled`

**The five, regenerated (each E/Var is two derivatives of these):**
- Binomial: M(t) = (1−p + p eᵗ)ⁿ.   Poisson: M(t) = exp(λ(eᵗ−1)).
- Normal(μ,σ²): M(t) = exp(μt + σ²t²/2).   Exponential(λ): M(t) = λ/(λ−t), t<λ.
- Uniform(a,b): M(t) = (e^{tb} − e^{ta}) / (t(b−a)).
*(Standard canonical MGFs; cross-checked against Walpole/Ross moment tables.)* `settled`
- *Cumulants:* log M(t) (the CGF) has the clean additivity used next; for the Normal the CGF is
  exactly μt+σ²t²/2 — **only first two cumulants nonzero**, the algebraic signature of "Gaussian."

---

## 3. Why sums stay in the family — convolution = multiply the transform

The single mechanism: **independent sum ⇒ MGFs/CFs multiply** (Unit 1 §4). Read off closure:

- **Poisson(λ₁) + Poisson(λ₂) = Poisson(λ₁+λ₂):** exp(λ₁(eᵗ−1))·exp(λ₂(eᵗ−1)) = exp((λ₁+λ₂)(eᵗ−1)). `settled`
- **Normal + Normal = Normal:** exp(μ₁t+σ₁²t²/2)·exp(μ₂t+σ₂²t²/2) = exp((μ₁+μ₂)t+(σ₁²+σ₂²)t²/2);
  means add, variances add (Stage-1 U1's Var-of-independent-sum, now as a *distributional* statement,
  not just a variance statement). `settled`
- **Σ of n iid Exponential(λ) = Gamma(n, λ) = Erlang:** the pdf is the n-fold convolution power; the
  result is Gamma with shape n, rate λ — pdf f(x)= λⁿ x^{n−1} e^{−λx} / (n−1)!, x≥0. *(Verified: W&M
  leemis UDR chart; randomservices.org Gamma; Univ. of Nairobi thesis "Sums of Exponential RVs".)*
  `settled`
- **Binomial(n,p) + Binomial(m,p) = Binomial(n+m,p)** (same p only): (1−p+peᵗ)ⁿ⁺ᵐ. `settled`

*Deep-structure payoff:* "stable under addition" is **not** five separate coincidences — it is one
fact (transforms multiply) plus whether the product stays in the family's functional form. This also
re-derives Stage-1's Poisson↔Exponential duality: Exponential gaps **sum** to the Gamma waiting time
for the n-th Poisson event — counts and gaps are the same process read two ways.

---

## 4. The Normal as the max-entropy / CLT fixed point (closing the U1 loop)

Stage 1 said the Normal "is the CLT attractor." Stage 2 gives the second, independent reason it is
special:

**Max-entropy theorem:** among *all* distributions on ℝ with a given mean and variance, the one with
maximum (differential) entropy is **Normal(μ,σ²)**. *Mechanism:* maximizing entropy subject to fixed
∫f, ∫xf, ∫x²f via Lagrange multipliers forces f ∝ exp(a+bx+cx²) — a Gaussian; equivalently, for any
other density g with the same variance, KL(g‖normal) ≥ 0 gives H(g) ≤ H(normal). *(Verified: Cover &
Thomas-style derivations; medium/Gibbs-inequality proof; sgfin max-entropy derivation.)* `settled`
- **Unification:** "fewest assumptions beyond a known variance" (max-entropy) and "what sums converge
  to" (CLT) pick out the **same** distribution. The exponential-family form exp(η·T−A) with
  T(x)=(x,x²) is the max-entropy answer for fixed first two moments — so §1, §4 and Unit 1's CLT are
  three views of one object. (Bridges to information theory / ECE communication theory.)
- **Why "fixed variance" matters:** entropy is unbounded without a scale constraint; the variance is
  the constraint that makes "most spread-out distribution" well-posed.

---

## 5. The approximations, with their *actual* validity (repairing the rules of thumb)

Stage 1 said "Binomial→Poisson or →Normal for large n." Stage 2 states **when**, and flags that these
are heuristics, not theorems (consistent with Unit 1 §5 Berry–Esseen — error depends on the
distribution, not a magic n).

- **Binomial → Poisson** (law of rare events): valid when n large, p small, with λ=np moderate. Common
  rule of thumb: n ≥ 20 and p ≤ 0.05, or n ≥ 100 and np ≤ 10. *Mechanism:* the Poisson limit theorem
  (Unit 2 Stage-1) — keep np fixed while p→0. Error is O(p) per the Le Cam bound (the total-variation
  distance is ≤ Σpᵢ² ≤ np² type bounds). `settled` (rule-of-thumb thresholds `uncertain`/conventional).
- **Binomial → Normal** (de Moivre–Laplace, a special CLT): valid when **np ≥ 5 and n(1−p) ≥ 5** (some
  texts use ≥10). Apply the **continuity correction** (±0.5) because you approximate a discrete pmf by
  a continuous pdf. *Mechanism:* Binomial is a sum of n iid Bernoulli → CLT; skew is worst when p is
  near 0 or 1, which is exactly when the np≥5 guard fails (Berry–Esseen again: rate ∝ skewness). `settled`
- **Which approximation when:** small p, large n, rare events → Poisson; p near ½, large n → Normal.
  Both are the *same* sum-of-Bernoullis viewed under different scaling regimes.

**Where the UG textbook over-promises:** "n>30 / np>5 and you're fine" hides that the true error is
governed by the standardized third moment (skewness). Skewed binomials (p≈0.02, n=200, np=4) are
*not* well-approximated by a Normal even though n is large — use Poisson there. The thresholds are
mnemonics, not guarantees.

---

## 6. Cross-topic unification (the expert's map)

- **One template (exponential family) → moments (A(η) or MGF) → closure under sums (multiply
  transforms) → limiting shape (CLT/max-entropy Normal).** That single chain organizes the whole unit.
- **Poisson process ties it together:** Exponential inter-arrivals (memoryless), Poisson counts in a
  window, Gamma/Erlang waiting time for the n-th arrival — one process, three of the five
  distributions. (Bridges to **05 Signals & Systems** / queueing, and to reliability in **03 Devices**.)
- **Uniform as the seed:** every other distribution is generated from Uniform(0,1) via the
  **inverse-CDF transform** X = F⁻¹(U) — the basis of simulation/Monte-Carlo (forward link to any
  computational stats). This is *why* Uniform sits in the unit despite not being exponential-family.

---

## 7. Stage-2 exit check ("why, not what")

- *Why do Poisson/Normal/Binomial sums stay in their family but two arbitrary distributions don't?*
  → §3: transforms multiply; closure depends on the functional form surviving the product.
- *What do Binomial, Poisson, Normal, Exponential share that Uniform lacks?* → §1: exponential-family
  form with parameter-independent support; Uniform's support moves with (a,b).
- *Two independent reasons the Normal is special?* → §4: CLT attractor (Unit 1) **and** max-entropy
  for fixed variance — same distribution from two principles.
- *Is "np>5" a theorem?* → §5: no; it's a skewness-driven heuristic (Berry–Esseen).
- *Where do the memorized E/Var come from?* → §2: two derivatives of the MGF / of A(η).

Open items → `../00-map.md`: exact rule-of-thumb thresholds are conventional (`uncertain`); whether
MUJ expects Gamma/MGF explicitly or only the five named distributions (scope, pending handout).
