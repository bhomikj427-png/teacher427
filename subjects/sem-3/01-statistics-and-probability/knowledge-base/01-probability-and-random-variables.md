# Unit 1 — Probability & Random Variables

> Confidence: `settled` (canonical, triangulated: Walpole 9e; Ross; MIT OCW 18.600; Wikipedia/CMU
> for exact inequality & CLT statements, verified 2026-06-16). Mechanism-level, exam-ready.

## Stage 1 (MUJ level)

### Probability basics (one lecture, per the syllabus)
- Sample space Ω, events as subsets, axioms: P(A)≥0, P(Ω)=1, countable additivity for disjoint
  events. Consequences: P(Aᶜ)=1−P(A), inclusion–exclusion.
- **Conditional probability** P(A|B)=P(A∩B)/P(B); **multiplication rule**; **independence**
  A⊥B ⇔ P(A∩B)=P(A)P(B). **Bayes' theorem** P(A|B)=P(B|A)P(A)/P(B). *Mechanism:* conditioning
  re-normalizes probability to the sub-universe B.

### Random variables
- An **RV** X is a function Ω→ℝ. *Mechanism:* it pushes the probability on Ω forward onto numbers,
  so we can do arithmetic with randomness. The **distribution** of X is the whole object.
- **CDF** F(x)=P(X≤x): non-decreasing, right-continuous, F(−∞)=0, F(∞)=1. Works for discrete &
  continuous alike — the unifying description.
- **Discrete RV:** pmf p(x)=P(X=x), Σp(x)=1. **Continuous RV:** pdf f(x)≥0, ∫f=1, with
  P(a≤X≤b)=∫ₐᵇ f, and f(x)=F′(x). For continuous X, P(X=x)=0 (probability is area, not height).
- **Independent RVs:** joint factorizes — F(x,y)=Fₓ(x)F_Y(y) (equivalently pmf/pdf factorizes).

### Expectation & variance (the linear-operator core)
- **E[X]** = Σ x·p(x) (discrete) or ∫ x·f(x)dx (continuous). **Linearity (always, even dependent):**
  E[aX+bY+c]=aE[X]+bE[Y]+c. **LOTUS:** E[g(X)]=Σg(x)p(x) or ∫g(x)f(x)dx.
- **Variance** Var(X)=E[(X−μ)²]=E[X²]−(E[X])². **Var(aX+b)=a²Var(X).** For **independent** X,Y:
  Var(X+Y)=Var(X)+Var(Y) (the independence is what kills the covariance term).
- SD σ=√Var. *Mechanism for the whole unit's computation:* push E through linearity; get Var from
  the second moment.

### Chebyshev's inequality (verified exact form)
- For any ε>0: **P(|X−μ| ≥ ε) ≤ Var(X)/ε².** *(verified: Wikipedia / CMU Stat-700 notes, 2026-06-16)*
- *Mechanism:* a distribution-free tail bound — spread (variance) caps how much probability can sit
  far from the mean. Loose but universal; it's the lever that proves the LLN.

### Law of Large Numbers & Central Limit Theorem (the engine — ★ threshold)
- **(Weak) LLN:** the sample mean X̄ₙ → μ in probability as n→∞ (provable from Chebyshev). *Why:*
  Var(X̄ₙ)=σ²/n → 0, so X̄ concentrates on μ.
- **CLT:** for iid X₁…Xₙ with mean μ, finite variance σ², the standardized sum
  **Zₙ = (X̄ₙ − μ)/(σ/√n) → N(0,1)** in distribution. *(verified: Wikipedia "Central limit theorem";
  MIT OCW 18.600, 2026-06-16.)* *Mechanism / why it matters:* sums of many independent contributions
  are approximately Normal **regardless of the original distribution** — this is why the Normal is
  ubiquitous and why √n shows up everywhere in inference (the sampling distribution of X̄ is
  ≈ N(μ, σ²/n)). This is the bridge to U3/U4.

### Worked-problem patterns (what the exam asks)
- Compute E, Var from a given pmf/pdf; find the constant that normalizes a pdf.
- Use the CDF to get probabilities / the pdf (differentiate).
- Apply Chebyshev for a "at least how much probability within k SD" bound (≥ 1 − 1/k²).
- Use CLT to approximate P(X̄ in range) or P(sum in range) for large n.

---
**Stage 2 (deep structure) — ✓ BUILT (2026-06-19):** lives separately in
`stage-2/01-probability-and-random-variables.md` — kept out of this exam file on purpose. *Adds:* measure-theoretic RV
definition; modes of convergence and which the LLN/CLT use; proof of CLT via characteristic
functions; Lindeberg/Lyapunov conditions for non-iid CLT; Chebyshev as a special case of Markov;
Berry–Esseen rate of convergence.
