# Unit 5 — Network Synthesis

> Confidence: `settled` (canonical; Van Valkenburg ch.10–13 — *the* synthesis anchor). LC/RC/RL
> driving-point properties and Foster/Cauer forms **verified this session** (eeeguide RC & RL DP
> pages; Wikipedia Foster's reactance theorem; Sanfoundry/testbook Cauer forms). The inverse of U4:
> given a realizable (PR) function → **build** a passive network that has it. Rests on U4 (PR/Hurwitz).

## Stage 1 (MUJ level)

### Framing — the synthesis problem
Analysis went circuit → Z(s). **Synthesis** goes **Z(s) → circuit.** Two stages: (1) **realizability** —
is Z(s) PR? (U4); (2) **realization** — a constructive procedure that extracts elements one at a time
until Z(s) is exhausted. The procedures: **Foster** (partial-fraction based) and **Cauer** (continued-
fraction/ladder based). Each yields a **canonical** network (minimum number of elements). We treat
three element-restricted classes — **LC**, **RC**, **RL** — because their pole-zero structure is
especially clean and they are what the syllabus ("the four reactance forms") asks for.

### LC (reactance / lossless) functions — Foster's reactance theorem
An LC driving-point immittance Z_LC(s) (or Y_LC) is a **reactance function**. Verified properties
(Foster's reactance theorem) `settled`:
- **Poles and zeros all lie on the jω axis, are simple, and alternate (interlace).** No RHP/LHP
  critical frequencies; none repeated.
- **Z_LC(s) is an odd rational function** (ratio of even/odd polynomials): Z(−s) = −Z(s).
- The **reactance X(ω) (where Z(jω)=jX) is monotonically increasing: dX/dω > 0** everywhere between
  poles. *Mechanism:* a lossless element stores energy; the slope condition is energy positivity.
- Both **s = 0 and s = ∞ are critical frequencies** (each is either a pole or a zero) — four canonical
  cases by what sits at 0 and ∞.
- **Residues at all poles are real and positive** (required for the partial-fraction realization).

**The four reactance-form realizations:**
- **Foster I (impedance / partial-fraction of Z):** expand Z(s) = k∞·s + k₀/s + Σ 2k_i s/(s²+ω_i²).
  Each term is an element: k∞s → **series L**; k₀/s → **series C**; each 2k_i s/(s²+ω_i²) → a
  **parallel L-C "tank"** in series. ⇒ **a chain of series-connected parallel-LC tanks** (+ possible
  end L and C). `settled`
- **Foster II (admittance / partial-fraction of Y):** expand Y(s) the same way ⇒ **parallel
  combination of series-LC branches** (the dual). `settled`
- **Cauer I (continued fraction about s = ∞):** remove the pole/term at **infinity** repeatedly →
  **ladder of series L's and shunt C's** (series inductor first when Z has a pole at ∞). Best for
  low-pass shapes. `settled` (verified)
- **Cauer II (continued fraction about s = 0):** remove the pole/term at the **origin** repeatedly →
  **ladder of series C's and shunt L's**. Best for high-pass shapes. `settled` (verified)
All four realize the *same* Z(s) with the same minimum element count; they differ in topology.

### RC driving-point functions — properties & realization
Verified properties of an **RC driving-point impedance Z_RC(s)** (eeeguide; testbook) `settled`:
- **Poles and zeros lie on the negative real axis, are simple, and alternate (interlace).**
- **The critical frequency nearest the origin is a POLE**; the one **farthest from the origin is a
  ZERO** (which may be at ∞). **No pole at infinity; no zero at the origin.**
- **Z_RC(0) > Z_RC(∞)** (impedance falls as frequency rises — the capacitor shorts out); the slope
  **dZ(σ)/dσ < 0** along the real axis (monotonically decreasing).
- **Residues (of the partial fraction of Z_RC) are real and positive.**
- *Realization:* **Foster I** → partial-fraction Z_RC = k₀/s + k∞ + Σ k_i/(s+σ_i): k₀/s → series C,
  k∞ → series R, each k_i/(s+σ_i) → **parallel R-C** in series. **Cauer** → continued fraction → RC
  ladder. (Note: a function that is RC as an *impedance* is RL as an *admittance* — same poles/zeros,
  dual reading.)

### RL driving-point functions — properties & realization
Verified properties of an **RL driving-point impedance Z_RL(s)** (eeeguide) `settled`:
- Poles and zeros on the **negative real axis, simple, alternate**.
- **The critical frequency nearest the origin is a ZERO** (may be at the origin); **no pole at the
  origin**. (The exact mirror of RC.)
- **Z_RL(0) < Z_RL(∞)** (impedance rises with frequency — the inductor); slope **dZ(σ)/dσ > 0**.
- The partial-fraction expansion of **Z_RL(s)/s** has **positive real residues** (equivalently, Y_RL
  behaves like an RC impedance). *Realization:* Foster → series-R + parallel-R-L sections; Cauer → RL
  ladder.

**The unifying picture (deep structure, exam-useful):** LC, RC, RL are the three two-element-kind
classes. Their critical frequencies live on the **jω axis (LC)**, the **negative-real axis (RC, RL)**;
the "nearest-to-origin is pole (RC-Z / LC depends) vs zero (RL-Z)" rule and the slope sign are how you
**identify** which class a given function belongs to and which element comes first in the ladder.

### Specifications for a reactance function (syllabus phrase)
"Specifications for a reactance function" = the realizability checklist above (jω-axis simple
alternating poles/zeros, positive residues, dX/dω>0, behavior at 0 and ∞). Given a candidate, you
**verify** it meets them, then **realize** it by Foster or Cauer.

### Worked-problem patterns
- Verify a given Z(s) is LC/RC/RL (apply the pole-zero/slope/residue tests) and identify its class.
- Realize a given LC function in **all four** forms (Foster I, Foster II, Cauer I, Cauer II).
- Realize a given RC (or RL) impedance in Foster and Cauer form; compute the element values.
- Given specs at 0 and ∞, decide which critical frequency is a pole vs zero, then synthesize.

---
**Stage 2 (deep structure) — ✓ BUILT (2026-06-22):** see `stage-2/05-network-synthesis.md`. *Adds:*
why the reactance-function slope dX/dω>0 follows from energy (Foster's theorem proof sketch); the
**Brune synthesis** for general PR functions (when LC/RC/RL restriction is lifted — ideal transformers,
the Brune cycle) and **Bott–Duffin** (transformerless RLC realization); minimum-positive-real /
Darlington synthesis; why Foster and Cauer are *canonical* (minimum element count) and how many
element-value degrees of freedom exist; the link to modern filter approximation (Butterworth/
Chebyshev) and to the image-parameter filters of U3.
