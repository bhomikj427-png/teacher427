# Unit 4 — Network Functions

> Confidence: `settled` (canonical; Van Valkenburg ch.9–10 — the anchor text; Sudhakar-Shyammohan).
> Hurwitz & positive-real conditions **verified this session** (Wikipedia positive-real function;
> Electrical4U; LBRCE synthesis notes). This unit is the **prerequisite spine** for two-ports (U3)
> and synthesis (U5): it defines the pole-zero language and the realizability gate. ★ threshold unit.

## Stage 1 (MUJ level)

### Framing — terminals, terminal pairs, and the network function
- A **port** = a terminal pair where current in one terminal = current out the other. **One-port** =
  driving-point; **two-port** = has a transfer relationship.
- A **network function H(s)** is the ratio (in the s-domain, zero initial conditions) of a response
  transform to an excitation transform. Two kinds:
  - **Driving-point function:** response and excitation at the **same** port — **driving-point
    impedance Z(s) = V/I** or **admittance Y(s) = I/V**. (Y = 1/Z.)
  - **Transfer function:** response and excitation at **different** ports — voltage ratio V₂/V₁,
    current ratio I₂/I₁, transfer impedance V₂/I₁, transfer admittance I₂/V₁.
- H(s) = N(s)/D(s), a **ratio of real-coefficient polynomials** in s. *Mechanism:* impedances are R,
  sL, 1/sC; any series/parallel combination is a rational function of s with real coefficients.

### Poles, zeros, and what they mean (★)
- **Zeros** = roots of N(s) (H = 0); **poles** = roots of D(s) (H = ∞). Plot them in the **s-plane**.
- **Poles are the network's natural frequencies** — the exponents e^{p t} in the source-free response
  (the U2 link). So pole location **is** transient behavior:
  - LHP (Re p < 0) → decaying → **stable**.
  - jω-axis simple pole (Re p = 0) → sustained oscillation (lossless LC).
  - RHP (Re p > 0) → growing → **unstable**.
  - repeated jω-axis pole → growing (t·sin) → unstable.
- **Real-coefficient ⇒ poles/zeros are real or in conjugate pairs** (symmetric about the real axis).
- H(jω) (poles/zeros evaluated on the jω axis) gives the **frequency response**: |H| from distances
  to zeros/poles, ∠H from angles — the geometric pole-zero interpretation of magnitude & phase.

### Stability & causality
- **Causal** = output cannot precede input (h(t)=0 for t<0); all physical circuits are causal.
- **Stable (BIBO)** = bounded input → bounded output ⇔ **all poles of H(s) in the open LHP** (for a
  driving-point function of a passive network, jω-axis poles are allowed if simple — lossless). The
  denominator of a stable function is a **Hurwitz polynomial** (next).
- *Why causality+stability matter for synthesis:* a function we want to *build* must correspond to a
  realizable, stable, causal network — which is exactly the **positive-real** condition below.

### Hurwitz polynomials (the stability test on the denominator)
A polynomial **P(s) is Hurwitz** if **all its roots have Re ≤ 0** (lie in the closed LHP); **strictly
Hurwitz** if all roots are in the open LHP (Re < 0). Verified properties (`settled`):
- **All coefficients are real and positive** (necessary, not sufficient for order >2). A **missing
  term** (zero coefficient) ⇒ not strictly Hurwitz, **except** an even or odd polynomial (all-even or
  all-odd powers) which can be Hurwitz with roots on the jω axis.
- **Test via continued-fraction / Routh–Hurwitz:** split P(s) = M(s) + N(s) into even part M and odd
  part N; form the continued-fraction expansion of M/N (or N/M). **P is Hurwitz iff every quotient
  term is positive** (all Routh-array first-column entries positive). A non-positive or vanishing
  quotient signals jω-axis or RHP roots.
- The denominator (and, for a PR function, also the numerator) of a realizable network function must
  be Hurwitz.

### Positive-real (PR) functions — the realizability gate (★)
**The central theorem of synthesis:** a rational function Z(s) is realizable as the **driving-point
impedance of a passive (RLCM) one-port** *if and only if* Z(s) is **positive-real**. Verified
definition (Wikipedia/Electrical4U/LBRCE) — Z(s) is PR iff **all** hold:
1. **Z(s) is real when s is real** (real coefficients).
2. **Re Z(s) ≥ 0 whenever Re s ≥ 0** — Z maps the closed right-half s-plane into the closed
   right-half Z-plane. (This is the defining condition; the rest are consequences/tests.)

Equivalent, *testable* conditions (the exam form):
- Z(s) has **no poles or zeros in the open RHP**; both N(s) and D(s) are **Hurwitz**.
- Any **poles/zeros on the jω axis are simple**, and the **residues at jω-axis poles are real and
  positive**.
- **Re Z(jω) ≥ 0 for all ω** (the real part on the boundary is non-negative — the practical numerical
  test, often reduced to checking that a certain even polynomial is ≥ 0).
- The degrees of N and D differ by **at most 1** (no multiple pole/zero at s = 0 or s = ∞).
`settled` (verified, triangulated).

*Mechanism / why PR = passive:* Re Z(jω) ≥ 0 means the one-port can **never deliver net average
power** — it only absorbs — which is exactly passivity; analyticity in the RHP is stability/causality.
PR is "passive + stable + causal" written as one analytic condition.

### Worked-problem patterns
- Given a circuit, write Z(s) or a transfer function; find and plot poles/zeros; read off stability.
- Test a given polynomial for Hurwitz (continued fraction / Routh array).
- Test a given Z(s) for positive-real (the conditions above) — *is this function realizable?*
- Sketch |H(jω)| from a pole-zero diagram (resonance near a jω-axis pole pair).

---
**Stage 2 (deep structure) — ✓ BUILT (2026-06-22):** see `stage-2/04-network-functions.md`. *Adds:*
proof that a passive driving-point impedance must be PR (passivity → Re Z(jω)≥0 via average power);
the bilinear/analytic-function argument behind condition 2; Brune's realization and the role of the
minimum-resistance/minimum-reactance functions; Hurwitz test proof via the Sturm/continued-fraction
theory; the Foster reactance theorem as the LC special case of PR; relation to Bode/Nyquist and to
passivity in control (the same PR condition is "passivity" in systems theory).
