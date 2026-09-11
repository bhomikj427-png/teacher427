# Unit 2 — Transient Analysis

> Confidence: `settled` (canonical; Hayt ch.7–9, 14; Sudhakar-Shyammohan; Van Valkenburg ch.5–7).
> The circuit's response *while it is settling* after a switching/excitation change. Two engines:
> the **time-domain** differential equation, and the **transform-domain** (Laplace) algebraic solve —
> the same answer, two routes. Rests on the s-domain (★ threshold) and feeds network functions (U4).

## Stage 1 (MUJ level)

### The continuity rules (the foundation — most errors start here)
- **Inductor current and capacitor voltage cannot change instantaneously** for finite energy/voltage:
  **i_L(0⁺) = i_L(0⁻)** and **v_C(0⁺) = v_C(0⁻)**. *Mechanism:* a jump in i_L needs infinite v
  (v=L di/dt); a jump in v_C needs infinite i (i=C dv/dt). These are the **initial conditions** that
  pin the transient. (Capacitor *current* and inductor *voltage* CAN jump.)
- **t = 0⁻ vs 0⁺ (★):** 0⁻ = just before switching (find i_L, v_C from the old steady state); carry
  them across by continuity to 0⁺; everything else (resistor currents, source-driven branches) may
  jump at 0⁺ and is found from the post-switch circuit *with* i_L(0⁺), v_C(0⁺) fixed.

### Total response = natural + forced (= transient + steady-state)
- **Natural (source-free) response:** the homogeneous solution — set excitation to zero, solve the
  characteristic equation. Its exponents are the **natural frequencies = poles** of the network (the
  ★ link to U4). Decays for a stable (passive R-containing) circuit.
- **Forced response:** the particular solution — the steady-state the circuit settles into under the
  excitation (DC → constant; sinusoid → phasor steady state).
- **Total = natural + forced**, with the natural-part constants fixed by the initial conditions.

### First-order circuits (one L or one C → one time constant)
- The defining equation is first-order; solution **x(t) = x(∞) + [x(0⁺) − x(∞)] e^{−t/τ}**.
- **Time constant τ:** RC circuit **τ = R_eq C**; RL circuit **τ = L / R_eq**, where R_eq is the
  Thévenin resistance seen by the C or L (the U1 link). ~63 % of the change in one τ; ~99 % in 5τ.
- **Standard excitations:** step (switch a DC source — the classic charging/discharging exponential),
  ramp, impulse. Use the three-piece formula above for step; superpose for combinations.

### Second-order circuits (L and C together → ringing or damping)
The series (or parallel) RLC obeys a 2nd-order ODE; characteristic equation **s² + 2αs + ω₀² = 0**.
- **Series RLC:** α = R/2L (neper/damping coefficient), **ω₀ = 1/√(LC)** (undamped natural freq).
- **Parallel RLC:** α = 1/(2RC), same ω₀ = 1/√(LC). *(Note R's role flips: large R damps a series
  circuit, small R damps a parallel circuit.)*
- **Damping ratio ζ = α/ω₀.** Roots s = −α ± √(α²−ω₀²). Four regimes by the discriminant:
  - **Overdamped (α > ω₀, ζ>1):** two real negative roots → sum of two decaying exponentials, no
    oscillation.
  - **Critically damped (α = ω₀, ζ=1):** repeated real root → (A + Bt)e^{−αt}; **fastest non-
    oscillatory** settling.
  - **Underdamped (α < ω₀, ζ<1):** complex roots −α ± jω_d, **damped oscillation** e^{−αt}cos(ω_d t+φ)
    with **damped frequency ω_d = √(ω₀² − α²)**.
  - **Undamped (α = 0, R=0):** pure oscillation at ω₀.
- **Quality factor Q = ω₀/2α** (series Q = (1/R)√(L/C); parallel Q = R√(C/L)); high Q ⇒ lightly damped,
  long ringing. These map directly to pole locations in the s-plane (U4).

### Impulse, step, ramp & sinusoidal response
- **Impulse response h(t):** response to δ(t) — the system's fingerprint; its Laplace transform is the
  **network function H(s)** (U4). **Step response** = ∫h, **ramp response** = ∫∫h (integration in
  time = ÷s in transform). **Sinusoidal steady-state** response is H(jω) applied to the phasor.
- *Mechanism (why one function rules all):* for an LTI circuit, output = **convolution** h*input; the
  step/ramp are integrals of the impulse, so their responses are integrals of h. (Convolution↔H(s)
  multiplication is derived in Stage 2.)

### Transform-domain (Laplace) analysis — the algebraic route
- **Transform the circuit, not the equation:** replace each element by its s-domain impedance and put
  initial conditions in as sources. **R→R**, **L→sL** in series with a voltage source **L·i_L(0⁻)**
  (or sL ∥ current source i_L(0⁻)/s), **C→1/sC** in series with **v_C(0⁻)/s** (or 1/sC ∥ source
  C·v_C(0⁻)). Then solve by algebra (KVL/KCL, nodal/mesh) in s, and **inverse-transform** (partial
  fractions) to get the time response. *Mechanism:* Laplace turns d/dt into multiplication by s and
  bakes in initial conditions, converting the ODE into an algebraic equation.
- **Key transform pairs:** δ(t)↔1; u(t)↔1/s; t↔1/s²; e^{−at}↔1/(s+a); sin ωt↔ω/(s²+ω²);
  cos ωt↔s/(s²+ω²). **Differentiation:** ℒ{f′}=sF(s)−f(0⁻). The poles of the response are the network's
  natural frequencies plus the excitation's poles.

### Initial- and final-value theorems
- **Initial value:** **f(0⁺) = lim_{s→∞} s·F(s)** (valid when the limit exists / F strictly proper-ish).
- **Final value:** **f(∞) = lim_{s→0} s·F(s)** — **valid only if all poles of s·F(s) are in the open
  LHP** (no poles in RHP or on the jω axis except possibly a single one at the origin). Applying it to
  an oscillatory (jω-axis pole) response is the classic error — the limit then does not represent a
  real final value. `settled`

### Worked-problem patterns
- Find i(t)/v(t) in an RL/RC circuit after a switch (three-piece first-order formula; get τ via R_th).
- Classify a series/parallel RLC as over/critical/under-damped; write the form; apply i_L(0⁺),v_C(0⁺).
- Solve a switched second-order circuit by Laplace; partial-fraction back to time.
- Use initial/final-value theorems to spot-check a transform answer (and know when FVT is invalid).

---
**Stage 2 (deep structure) — ✓ BUILT (2026-06-22):** see `stage-2/02-transient-analysis.md`. *Adds:*
deriving the RLC ODE and the convolution h*x from LTI + time-invariance; the impulse response as
ℒ⁻¹{H(s)}; the state-variable (state-space) formulation and eigenvalues = poles; rigorous FVT/IVT
conditions and proofs; the s-plane geometry of damping (constant-α, constant-ω₀, constant-ζ loci);
zero-input vs zero-state decomposition and why it generalizes natural+forced.
