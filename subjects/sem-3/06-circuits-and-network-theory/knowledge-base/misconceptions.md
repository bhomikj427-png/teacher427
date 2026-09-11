# ECE2120 Circuits & Network Theory — Misconceptions & predictable errors

> Per `subject-research-protocol.md §4`: the predictable wrong models novices hold, each confidence-
> marked. These feed the engine's productive-failure and feedback moves. Sourced to physics/EE
> education literature where it exists; ones resting on teaching experience / standard-text warnings
> rather than a documented-error study are marked `uncertain` and flagged to-verify. The list serves
> **both** stages.

## M1 — "Superpose the power." `settled`
Students sum the **power** contributions from each source the way they sum voltages/currents.
**Why wrong:** power ∝ I² is **nonlinear**; superposition holds only for quantities *linear* in the
sources. **Correct:** superpose voltages/currents, *then* compute power from the total. (Stated as an
explicit warning in Hayt and every standard text — `settled`.)

## M2 — "Deactivate dependent sources too." `settled`
When applying superposition or finding R_th, students zero out **dependent** sources along with
independent ones. **Why wrong:** a dependent source is not an excitation — it tracks a circuit
variable; killing it changes the network. **Correct:** deactivate only **independent** sources;
dependent sources stay active → use the **test-source method** for Z_th. (`01-network-theorems.md`.)

## M3 — "i_L or v_C can jump at switching." `settled`
Students let inductor current or capacitor voltage change instantaneously across t=0. **Why wrong:**
that demands infinite voltage (L di/dt) or infinite current (C dv/dt). **Correct:** i_L(0⁺)=i_L(0⁻),
v_C(0⁺)=v_C(0⁻); *other* variables (resistor currents, capacitor current, inductor voltage) **may**
jump. The single biggest source of transient-analysis errors. `settled`

## M4 — "Maximum power transfer = maximum efficiency." `settled`
Believing matching the load for max power is also "most efficient." **Why wrong:** at the match an
equal amount is burned in R_th → **efficiency is only 50 %**. **Correct:** max power transfer is a
signal/communications goal; power systems deliberately run R_L ≫ R_th for high efficiency.
(Verified — Wikipedia/LibreTexts max-power-transfer.) `settled`

## M5 — "For AC max power, set Z_L = Z_th (not the conjugate)." `settled`
Matching magnitudes/values rather than conjugating. **Why wrong:** the load reactance must **cancel**
the source reactance to maximize real power. **Correct:** **Z_L = Z_th\*** (R_L=R_th, X_L=−X_th).
Only when the load is constrained (pure resistance, or fixed angle) does the optimum change.
(Verified this session.) `settled`

## M6 — "Apply the final-value theorem to anything." `settled`
Using f(∞)=lim_{s→0} sF(s) on oscillatory or unstable responses. **Why wrong:** FVT is valid **only
if** all poles of sF(s) are in the open LHP (a single pole at the origin allowed). For a jω-axis pole
(undamped oscillation) the limit is meaningless. **Correct:** check pole locations before applying.
`settled`

## M7 — "Poles of H(s) are just math; they don't *mean* anything." `settled`
Treating the s-plane as algebra disconnected from behavior. **Why wrong:** poles **are** the natural
frequencies — their real part is the decay rate, imaginary part the oscillation frequency; LHP=stable.
**Correct:** read transient, frequency response, and stability straight off the pole-zero plot. The ★
threshold; failing it blocks U2/U4/U5. `settled`

## M8 — "Positive coefficients ⇒ Hurwitz / stable." `uncertain` (teaching-experience; verify vs text)
Assuming a polynomial with all positive coefficients is Hurwitz. **Why wrong:** positive coefficients
are **necessary but not sufficient** for order > 2; the continued-fraction/Routh test can still fail.
**Correct:** run the full Routh–Hurwitz test. *(Standard text warning; not yet tied to a documented-
error study — `uncertain`, to-verify.)*

## M9 — "RC and RL pole-zero rules are the same / interchangeable." `settled`
Mixing up which class has a pole nearest the origin. **Why wrong:** for **Z_RC** the critical
frequency nearest the origin is a **pole** (farthest is a zero); for **Z_RL** the nearest is a
**zero**. Slopes also differ (Z_RC falls, Z_RL rises with frequency). **Correct:** memorize via
mechanism — at DC a capacitor is open (high Z → pole behavior near origin for RC-Z), an inductor is a
short (low Z near origin for RL-Z). (Verified this session — eeeguide RC/RL DP pages.) `settled`

## M10 — "Two-port Z and Y parameters always exist (just invert)." `uncertain` (verify vs Van Valkenburg)
Assuming every two-port has all four parameter sets. **Why wrong:** [Y]=[Z]⁻¹ fails when [Z] is
singular; some networks (e.g. an **ideal transformer**, a series/shunt-only element) have **no Z or no
Y representation** at all, though they still have an ABCD matrix. **Correct:** check existence; ABCD
or h often exists where Z/Y doesn't. *(`uncertain` pending a clean textbook citation of the singular
cases.)*

## M11 — "Reciprocity means symmetry (and vice-versa)." `settled`
Conflating the two. **Why wrong:** reciprocity (Z₁₂=Z₂₁) holds for any bilateral network; **symmetry**
(Z₁₁=Z₂₂) additionally requires the two ports be interchangeable. **Symmetry ⇒ reciprocity, not the
reverse.** **Correct:** an asymmetric ladder of R,L,C is reciprocal but not symmetric. (Verified —
two-port parameter references.) `settled`

## Open to-verify (route to `00-map.md`)
- `[opened 2026-06-22]` M8, M10 rest on standard-text warnings / teaching experience, **not** a
  documented physics-EE-education error study. *Resolve by:* citing a specific source (Van Valkenburg
  remarks; circuits-misconceptions literature) or demoting if unsupported.
