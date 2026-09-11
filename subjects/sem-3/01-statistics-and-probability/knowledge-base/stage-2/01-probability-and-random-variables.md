# Unit 1 — Probability & Random Variables — STAGE 2 (deep structure)

> **Stage 2 — IIT/Ivy depth.** Built *on top of* the exam-ready Stage-1 file
> (`../01-probability-and-random-variables.md`), never replacing it. This is the generative
> machinery an expert reasons *from*: what an RV *really* is, the convergence zoo, and a real proof
> of the CLT plus its rate and its failure modes.
> Confidence: `settled` unless marked. Load-bearing specifics verified against external sources this
> session (2026-06-19) — see `stage-2/sources.md`. Stage-1 facts are not repeated here.

---

## 0. What Stage 1 quietly assumed (the white lies to repair)

Stage 1 said "an RV is a function Ω→ℝ" and "P(X=x)=0 for continuous X" and "the standardized sum →
N(0,1)". Each hides a piece of machinery:
- "Function Ω→ℝ" omits **measurability** — and without it, P(X≤x) need not even be defined.
- "P(X=x)=0" is a *consequence* of how a measure treats single points, not a special continuous-case
  rule. Discrete and continuous are two faces of **one** object (a probability measure / its CDF);
  the pmf/pdf split is a convenience, not a dichotomy.
- "→ N(0,1)" hides **which mode of convergence** (distribution, not probability or a.s.), **why**
  (characteristic functions), and **how fast** (Berry–Esseen) — and what conditions make it fail.

Stage 2 supplies all three.

---

## 1. A random variable, rigorously — the measure-theoretic definition

**Setup.** A probability space is a triple (Ω, ℱ, P): Ω the sample space, ℱ a **σ-algebra** of
events (closed under complement and countable union), P a measure with P(Ω)=1.

**Definition.** An RV is a **measurable function** X: Ω→ℝ — meaning for every Borel set B⊆ℝ, the
preimage X⁻¹(B) = {ω : X(ω)∈B} ∈ ℱ. *Mechanism / why measurability:* we want to ask "P(X∈B)"; that
only makes sense if {X∈B} is an event P can score. Measurability is exactly the condition that every
question about X pulls back to a legitimate event. It is enough to require X⁻¹((−∞,x]) ∈ ℱ for all x
— which is why the **CDF F(x)=P(X≤x) is the universal handle** (Stage 1's "works for discrete &
continuous alike" is *because* the CDF is the primitive and pmf/pdf are derived). `settled`

**The distribution is a pushforward measure.** X carries P on Ω forward to a measure P_X on ℝ:
P_X(B) = P(X⁻¹(B)). This *is* Stage 1's "the distribution is the whole object," made precise — the
distribution is a measure on the number line, and pmf/pdf/CDF are three encodings of it. `settled`

**One integral unifies discrete and continuous.** E[X] = ∫_Ω X dP = ∫_ℝ x dP_X(x) (Lebesgue
integral). When P_X has a density f w.r.t. Lebesgue measure → ∫ x f(x) dx; when it is a sum of atoms
→ Σ x p(x). *Mechanism:* the discrete/continuous formulas in Stage 1 are **the same Lebesgue
integral** against two different reference measures (counting vs Lebesgue) — via the Radon–Nikodym
derivative f = dP_X/dμ. This is why "P(X=x)=0 for continuous X" needs no special rule: a density puts
zero mass on any single point because Lebesgue measure does. `settled`
- **Where the UG textbook simplifies:** it presents discrete and continuous as two species with two
  rule-sets. They are one species (a measure) in two coordinate systems. There are even mixed RVs
  (atoms + density), which the pmf/pdf framing can't name but the CDF handles natively (jumps + slopes).

---

## 2. The convergence zoo — *which* convergence each limit law uses (the most-confused point)

Stage 1 wrote both LLN and CLT with "→" as if it were one arrow. It is not. Four modes, strongest to
weakest, for Xₙ → X:

1. **Almost sure (a.s.):** P(Xₙ → X) = 1. The realizations themselves converge.
2. **In probability (→ᵖ):** P(|Xₙ−X| > ε) → 0 for every ε>0.
3. **In Lᵖ (mean-square when p=2):** E|Xₙ−X|ᵖ → 0.
4. **In distribution (→ᵈ):** Fₙ(x) → F(x) at every continuity point of F. (Only about the
   *distributions*, not the variables — they needn't even live on one space.)

**The implication lattice (load-bearing, verified):**
a.s. ⇒ in probability ⇒ in distribution; and Lᵖ ⇒ in probability ⇒ in distribution. None of the
reverse arrows hold in general; a.s. and Lᵖ don't imply each other. *(Triangulated: Iowa 22S:194 /
standard graduate probability notes — see sources.)* `settled`

**Now the limit laws are precise:**
- **Weak LLN (WLLN):** X̄ₙ →ᵖ μ. (Stage 1's "in probability" — provable from Chebyshev.)
- **Strong LLN (SLLN):** X̄ₙ → μ **almost surely** (Kolmogorov; needs only E|X|<∞ for iid). Strictly
  stronger than WLLN; Stage 1 never mentioned it. *Mechanism difference:* WLLN says "far-off behavior
  is rare at each large n"; SLLN says "the single sample path settles down forever." `settled`
- **CLT:** Zₙ = √n(X̄ₙ−μ)/σ →ᵈ N(0,1) — **convergence in distribution only.** *Mechanism / why not
  stronger:* Zₙ does **not** settle to a number (its variance stays 1 forever), so a.s./Lᵖ
  convergence is impossible; only the *shape* of its distribution stabilizes. This is the precise
  content of Stage-1 misconception **M5** ("the data become normal") — it's the *distribution of the
  standardized mean* whose shape converges, nothing converges pointwise. `settled`

> **Why this matters for teaching:** the master threshold (sampling distribution, ★) is exactly the
> distinction between "a sequence of numbers settling" (LLN, a.s./prob) and "a sequence of *shapes*
> settling" (CLT, in distribution). Most downstream confusion is a mode-of-convergence confusion.

---

## 3. Chebyshev is not fundamental — Markov is (the inequality hierarchy)

Stage 1 presented Chebyshev as a standalone tool. It is one line of a hierarchy:

- **Markov's inequality (the root):** for Y ≥ 0 and a>0, P(Y ≥ a) ≤ E[Y]/a. *Mechanism:* E[Y] ≥
  E[Y·1{Y≥a}] ≥ a·P(Y≥a); rearrange. One non-negativity argument generates everything below.
- **Chebyshev = Markov applied to Y=(X−μ)², a=ε²:** P(|X−μ|≥ε) = P((X−μ)²≥ε²) ≤ E[(X−μ)²]/ε² =
  Var(X)/ε². So Stage 1's bound is *derived*, not axiomatic. `settled`
- **Chernoff = Markov applied to Y=e^{tX}:** P(X≥a) ≤ e^{−ta} E[e^{tX}], then optimize over t>0.
  Gives **exponentially** small tail bounds (vs Chebyshev's polynomial 1/ε²) when the MGF exists —
  the workhorse behind concentration inequalities. `settled`
- **Generalization:** Markov with Y=|X|ᵏ gives the k-th moment bound; higher moments → sharper tails.

*Deep-structure payoff:* "distribution-free tail control" is **one idea** (bound a non-negative
functional by its mean), tuned by *which* functional you feed it. Chebyshev (square) → LLN; Chernoff
(exponential) → large-deviations and the entire concentration-of-measure toolkit.

---

## 4. The CLT, actually proved — characteristic functions

**Characteristic function (CF):** φ_X(t) = E[e^{itX}]. Unlike the MGF it **always exists** (|e^{itX}|=1),
which is why it, not the MGF, is the rigorous engine. Key properties:
- It **determines the distribution** (inversion formula) and is continuous.
- **Independence → multiply:** φ_{X+Y}(t)=φ_X(t)φ_Y(t).
- **Taylor at 0:** if E[X²]<∞, φ_X(t) = 1 + itE[X] − t²E[X²]/2 + o(t²).

**Lévy continuity theorem (the bridge):** if φ_{Xₙ}(t) → φ(t) pointwise and φ is continuous at t=0,
then Xₙ →ᵈ X where φ is X's CF. *(Verified: Wikipedia "Lévy's continuity theorem"; IISc CLT notes.)*

**Proof of the CLT (iid, mean 0, variance σ², standardized).** Let Y_i = X_i/σ so Var(Y_i)=1, and
Sₙ = (Y₁+…+Yₙ)/√n. Then
  φ_{Sₙ}(t) = [ φ_Y(t/√n) ]ⁿ        (independence)
            = [ 1 − t²/(2n) + o(t²/n) ]ⁿ   (Taylor, since E[Y]=0, E[Y²]=1)
            → e^{−t²/2}              (the (1+a/n)ⁿ → eᵃ limit).
And e^{−t²/2} is exactly the CF of N(0,1). By Lévy continuity, Sₙ →ᵈ N(0,1). ∎
*(Triangulated: IISc notes 16–18; Fairfield "CF and the CLT"; Filmus "Two Proofs of the CLT".)* `settled`
- *Why this is the "real why":* normality is forced because **only the second moment survives the
  1/√n rescaling** — the linear term vanishes by centering, higher terms die as o(1/n). Any
  finite-variance shape gets washed to the same Gaussian fixed point. The Gaussian is the *attractor*
  of the rescaling map (Stage 1 called it "the CLT attractor"; this is the mechanism).

---

## 5. Generalizing and breaking the CLT (assumptions, limits, rate)

**Beyond iid — Lindeberg & Lyapunov.** For independent but *not* identically distributed Xᵢ with
μᵢ, σᵢ², write sₙ² = Σσᵢ².
- **Lindeberg condition:** for every ε>0, (1/sₙ²) Σᵢ E[(Xᵢ−μᵢ)² · 1{|Xᵢ−μᵢ| > ε sₙ}] → 0. Then
  (1/sₙ) Σ(Xᵢ−μᵢ) →ᵈ N(0,1) (**Lindeberg–Feller**). *Mechanism:* no single term may contribute a
  non-vanishing share of the total variance — "no one dominates." `settled`
- **Lyapunov condition (stronger, easier to check):** for some δ>0, (1/sₙ^{2+δ}) Σᵢ E|Xᵢ−μᵢ|^{2+δ} → 0
  ⇒ Lindeberg holds ⇒ CLT. *(Verified: Lyapunov-CLT survey; Iowa 7110 Lindeberg–Feller notes.)* `settled`

**Where the CLT FAILS (the limits the UG course never states):**
- **Infinite variance.** With heavy tails (e.g. Cauchy, or Pareto with index <2) there is *no* finite
  σ², and sums rescaled by √n do **not** go Gaussian — they converge to **α-stable** laws instead.
  The Gaussian is just the α=2 member of the stable family. `settled` (mechanism: the variance the
  proof in §4 relied on doesn't exist).
- **Strong dependence.** Independence (or weak mixing) is essential; strongly correlated terms can
  converge to non-Gaussian limits.

**How fast? Berry–Esseen (the rate Stage 1 omitted).** If ρ = E|X−μ|³ < ∞, then
  supₓ |Fₙ(x) − Φ(x)| ≤ C · ρ / (σ³ √n).
So the CDF error shrinks like **1/√n**, and this rate is best-possible in general. The constant: the
original (Esseen, 1942) was large; the **best known universal value is C < 0.4748** (Shevtsova,
2011), with a known lower bound ≈0.409 — i.e. the *exact* optimal C is still open. `contested`
(the existence/form of the bound is `settled`; the **best constant is an open/evolving number** —
teach it as "≈0.47, not yet pinned"). *(Verified: numberanalytics Berry–Esseen; emergentmind
Berry–Esseen rates.)*
- *Practical upshot / repairs the "n>30" folklore:* "n ≥ 30 ⇒ CLT applies" is a **rule of thumb,
  not a theorem.** Berry–Esseen says the error depends on ρ/σ³ (the standardized third moment =
  skewness scale): symmetric light-tailed data are nearly Gaussian at small n; heavily skewed data
  need *much* more than 30. The right statement is "convergence rate scales with skewness," not a
  magic number. `settled`

---

## 6. Cross-topic unification (what an expert sees)

- **CF ↔ Fourier transform.** φ_X(t) is the Fourier transform of the density. "Convolution of
  densities = product of CFs" (independence) is just the Fourier convolution theorem — the *same*
  fact ECE students meet in Signals & Systems. Sums of independent RVs ≈ LTI filtering of
  distributions. (Bridges to **05 Signals & Systems**.)
- **Smoothing → Gaussian.** Repeated convolution (adding RVs) is a smoothing operation; the Gaussian
  is its fixed point — the probabilistic mirror of "repeated low-pass filtering smooths a signal."
- **Entropy view (forward link to Unit 2 §Normal):** among fixed-variance distributions the Gaussian
  is max-entropy; the CLT can be read as entropy *increasing* to that maximum under convolution.

---

## 7. Stage-2 exit check (the §0 surplus test — "why, not what")

- *Why is CLT convergence "in distribution" and not stronger?* → §2: Zₙ has fixed variance 1, never
  settles pointwise; only its shape stabilizes.
- *Where does Gaussianity actually come from in the proof?* → §4: only the t² term survives 1/√n
  rescaling; Lévy continuity converts CF-convergence to distributional convergence.
- *When does the CLT break, and what replaces it?* → §5: infinite variance → α-stable limits;
  strong dependence → non-Gaussian.
- *Is "n>30" a theorem?* → §5: no; error ∝ skewness/√n (Berry–Esseen).
- *Why no special rule for P(X=x)=0?* → §1: single points are Lebesgue-null; it's the measure, not a
  continuous-case exception.

Open items pushed to `../00-map.md` register: best Berry–Esseen constant (open math problem, mark
`contested`); whether MUJ's syllabus expects SLLN or only WLLN (scope, `uncertain` pending handout).
