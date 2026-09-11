# Unit 3 — Theory of Estimation — STAGE 2 (deep structure)

> **Stage 2 — IIT/Ivy depth.** Built on top of the exam-ready Stage-1 file (`../03-estimation.md`),
> not replacing it. Stage 1 gave the *recipes* (MoM, MLE, sufficiency, CIs) and the *properties we
> want* (unbiased, consistent, efficient). Stage 2 answers the questions those recipes beg: **how
> good can any estimator possibly be?** (Cramér–Rao), **how do we reach that optimum?**
> (Rao–Blackwell / Lehmann–Scheffé), **why is the MLE the default?** (asymptotics), and **where do
> the t and χ² distributions in the CI formulas actually come from?**
> Confidence `settled` unless marked; load-bearing specifics verified 2026-06-19 (`stage-2/sources.md`).

---

## 1. The score and Fisher information — the curvature of evidence

Two objects generate the whole theory.
- **Score:** U(θ) = ∂/∂θ log f(X;θ). Under regularity, **E[U(θ)] = 0** (the score is mean-zero at the
  truth). *Mechanism:* differentiating ∫f dx = 1 under the integral sign kills the mean.
- **Fisher information:** I(θ) = Var(score) = E[ (∂_θ log f)² ]. Under regularity this equals the
  **expected curvature**: I(θ) = −E[ ∂²_θ log f(X;θ) ]. *(Verified: Stanford Stats 200 L15; U.Regina
  ch.4 Fisher/CRLB; HBS CRLB notes.)* `settled`
- *Mechanism / meaning:* information = how sharply the log-likelihood peaks at the truth. A sharply
  curved log-likelihood (large I) pins θ down tightly; a flat one leaves θ poorly determined. For an
  iid sample, information **adds**: Iₙ(θ) = n·I₁(θ) — n independent observations carry n times the
  information. This single fact drives every √n in the unit.

---

## 2. Cramér–Rao — the hard floor on variance (the "how good is possible" answer)

**Cramér–Rao Lower Bound (CRLB).** For *any* unbiased estimator θ̂ of θ (regularity conditions
holding):
  Var(θ̂) ≥ 1 / I(θ) = 1 / (n·I₁(θ)).
More generally, for an unbiased estimator of g(θ): Var ≥ [g'(θ)]² / I(θ). *(Verified: Stanford 200
L15; U.Regina; HBS.)* `settled`
- *Mechanism:* it's the Cauchy–Schwarz inequality between θ̂ and the score — the correlation of any
  unbiased estimator with the score is fixed, which caps how small its variance can be.
- **Efficiency** (Stage 1's undefined word, now precise): an unbiased estimator is **efficient** if it
  *attains* the CRLB; **relative efficiency** of two estimators is the ratio of their variances.
- **When the bound is attainable:** equality holds **iff** the model is exponential-family and θ̂ is
  the natural sufficient statistic's mean (the score is then linear in θ̂). This is the exact link to
  Unit 2 §1 — the exponential family is the class where efficient unbiased estimators exist in finite
  samples. `settled`
- **Where the UG textbook hand-waves:** the CRLB needs **regularity** — the support must not depend on
  θ. For Uniform(0,θ) the support moves with θ, the CRLB does **not apply**, and the MLE (the sample
  max) beats the "bound" — its variance shrinks like 1/n² , faster than any 1/n CRLB. A crucial
  counterexample, never mentioned at Stage 1. `settled`

---

## 3. Reaching the optimum — Rao–Blackwell and Lehmann–Scheffé

Stage 1 introduced sufficiency as "captures all information about θ." Here is what it *buys* you:

- **Rao–Blackwell:** if U is any unbiased estimator and T is sufficient for θ, then **Û = E[U | T]**
  is unbiased and **Var(Û) ≤ Var(U)**. *Mechanism:* conditioning on a sufficient statistic averages
  away noise that carries no information about θ; the law of total variance does the rest. *(Verified:
  Wisconsin Shao Stat-709 L15; Springer R–B chapter.)* `settled`
  → *So:* improve any estimator by Rao–Blackwellizing it onto a sufficient statistic.
- **Completeness** (the missing ingredient): T is **complete** if E[h(T)]=0 for all θ implies h≡0 — i.e.
  T admits no non-trivial unbiased estimator of zero. *Mechanism:* completeness makes the
  Rao–Blackwellized estimator **unique**.
- **Lehmann–Scheffé:** if T is **complete and sufficient** and h(T) is unbiased for θ, then h(T) is the
  **unique UMVUE** (uniformly minimum-variance unbiased estimator). *(Verified: Wikipedia
  Lehmann–Scheffé; Stanford 300A L4; Wisconsin Shao.)* `settled`
  → *This is the constructive route to "best unbiased":* find a complete sufficient T (the exponential
  family hands you one), take any unbiased function of it, done.

**The estimation big picture (deep structure):** CRLB sets the *floor*; Rao–Blackwell *descends
toward* it by removing non-sufficient noise; Lehmann–Scheffé *certifies* you've hit the unique best
unbiased estimator. Sufficiency (U1/U3 threshold) is the hinge of all three.

---

## 4. Why the MLE is the default estimator — its asymptotics

Stage 1 taught *how* to compute the MLE; Stage 2 says *why it's the one you reach for*. Under
regularity, as n→∞:
- **Consistent:** θ̂_MLE →ᵖ θ.
- **Asymptotically normal:** √n(θ̂_MLE − θ) →ᵈ N(0, I₁(θ)⁻¹).
- **Asymptotically efficient:** its limiting variance is the CRLB — no (regular) estimator does better
  for large n. *(Verified: Stanford 200 L15; Karlin/Charles Univ. MLE theory summary.)* `settled`
- **Invariant:** the MLE of g(θ) is g(θ̂) — Stage 1 never stated this; it's why MLEs compose cleanly.
- *Mechanism:* a Taylor expansion of the score around the truth, U(θ̂)=0, plus the CLT on the score
  (which is a sum of iid mean-zero terms, Unit 1) and the LLN on its derivative. So **MLE asymptotics
  are the CLT wearing a statistics hat** — the same √n.
- **Honest caveat (`contested`/limits):** these are *large-sample* guarantees. In small samples the
  MLE can be biased (e.g. Normal σ̂² divides by n — Stage-1 M7) and need not attain the CRLB. "MLE is
  optimal" is an asymptotic statement, not a finite-sample one. `settled`

---

## 5. Where the t and χ² in the CI formulas come from (deriving Stage-1's tools)

Stage 1 used "x̄ ± t·s/√n" and asserted t "has heavier tails." Here is the actual construction, from
iid Normal(μ,σ²) data:
1. **χ² is a sum of squared standard normals:** χ²_k = Σ_{i=1}^k Zᵢ², Zᵢ iid N(0,1). Mean k, variance 2k. `settled`
2. **Independence of X̄ and S² (Normal-only):** for Normal data, X̄ ⟂ S². *Mechanism:* X̄ and the
   deviations (Xᵢ−X̄) are uncorrelated and jointly normal ⇒ independent (provable via Cochran's
   theorem / orthogonal decomposition; also a Basu's-theorem corollary). This independence is a
   **special property of the Normal** — it characterizes it. `settled`
3. **Sample variance is scaled χ²:** (n−1)S²/σ² ~ χ²_{n−1}. *(Cochran's theorem; the n−1 df = n data
   minus 1 estimated mean.)* `settled`
4. **Student's t is a normal over a scaled chi:** t_k = Z / √(V/k), with Z~N(0,1), V~χ²_k, independent.
   Plug in: (X̄−μ)/(S/√n) = [(X̄−μ)/(σ/√n)] / √[ ((n−1)S²/σ²)/(n−1) ] = Z/√(V/(n−1)) ~ t_{n−1}. `settled`

*Now Stage-1's claims have mechanism:* the t-distribution's heavy tails come from the **extra
randomness of estimating σ by S** in the denominator (a random divisor); as n→∞, S→σ, V/(n−1)→1, and
**t_{n−1} → N(0,1)** — the t *becomes* the z, which is exactly why "σ known / large n ⇒ use z." The df
n−1 is the cost of spending one degree of freedom on X̄. *(Triangulated: Walpole/Montgomery sampling-
distribution chapters + standard mathematical-statistics derivations.)*

---

## 6. The Bayesian frame, made rigorous — conjugacy and decision theory

Stage 1 named Bayesian estimation; Stage 2 gives its structure and its honest contrast with the
frequentist view.
- **Conjugate priors:** a prior is conjugate if the posterior stays in the same family. Standard
  conjugate pairs: **Beta prior – Binomial likelihood → Beta posterior**; **Gamma – Poisson → Gamma**;
  **Normal – Normal (known variance) → Normal**. *Mechanism:* every exponential-family likelihood
  (Unit 2 §1) has a conjugate prior — the prior and likelihood multiply to the same exponential form,
  so updating just adds natural parameters / "pseudo-counts." `settled`
  - The Normal-Normal posterior mean is a **precision-weighted average** of the prior mean and the
    sample mean — concretely shows the prior acting as extra data, dissolving as n grows.
- **Decision theory (what "the estimate" *is*):** choose a loss; the Bayes estimator minimizes
  *posterior expected loss*. Squared-error loss → **posterior mean**; absolute-error loss → posterior
  **median**; 0–1 loss → posterior **mode (MAP)**. This is *why* Stage-1's "posterior mean or mode" —
  each answers a different loss. `settled`
- **Honest frequentist vs Bayesian framing (`contested` by design — teach as a real debate, not one
  side):** frequentist θ is a fixed unknown and probability describes the *procedure* (this is why the
  CI means what M6 says); Bayesian θ is random and probability describes *belief*. A Bayesian credible
  interval *can* be read as "95% probability θ is in here" — precisely the statement that is **wrong**
  for a frequentist CI. Same numbers often, opposite interpretations. Genuinely contested foundations;
  the base teaches the distinction, never collapses it. `settled` (that they differ) / `contested` (which is "right").

---

## 7. Cross-topic unification (the expert's map)

- **One spine: the likelihood.** Score → information → CRLB → MLE asymptotics → likelihood-ratio tests
  (Unit 4) are all derivatives/uses of log f(X;θ). Estimation and testing are **one likelihood theory**.
- **Exponential family (Unit 2 §1) is where everything is clean:** finite-dim sufficient statistic,
  attainable CRLB, complete sufficient statistic for Lehmann–Scheffé, conjugate prior for Bayes.
- **Everything rests on the sampling distribution (★ threshold):** unbiasedness, variance, CIs, the
  t/χ² constructions in §5 — all are statements about the *distribution of a statistic*, the U1 idea.
- **The CLT (Unit 1) underwrites the large-sample CIs and MLE normality** — same √n throughout.

---

## 8. Stage-2 exit check ("why, not what")

- *How good can an unbiased estimator possibly be?* → §2: Var ≥ 1/I(θ); attained only in
  exponential families.
- *When does the CRLB fail?* → §2: non-regular support, e.g. Uniform(0,θ), where the MLE beats it (1/n²).
- *How do you construct the best unbiased estimator?* → §3: Rao–Blackwell onto a complete sufficient T;
  Lehmann–Scheffé certifies uniqueness.
- *Why default to the MLE?* → §4: consistent, asymptotically normal, asymptotically efficient — with
  the small-sample-bias caveat.
- *Where do t and χ² actually come from?* → §5: χ²=Σ Z²; (n−1)S²/σ²~χ²_{n−1}; t=Z/√(V/k); t→z as n→∞.
- *Why can a Bayesian say "95% probability θ is in here" but a frequentist cannot?* → §6: random θ vs
  fixed θ; belief vs procedure.

Open items → `../00-map.md`: whether MUJ's syllabus expects CRLB/Fisher information and UMVUE theory or
only MoM/MLE/sufficiency/CIs (scope, `uncertain` pending handout); frequentist/Bayesian "which is
right" stays `contested` on purpose.
