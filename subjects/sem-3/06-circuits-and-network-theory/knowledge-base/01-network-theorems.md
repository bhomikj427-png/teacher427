# Unit 1 — Network Theorems & Elements

> Confidence: `settled` (canonical; Hayt-Kemmerly-Durbin 8e / Sudhakar-Shyammohan 5e / Van Valkenburg).
> All four theorems are consequences of **linearity** of the network. They reduce a big circuit to a
> tiny equivalent so the rest of the course (transients, two-ports) is tractable.

## Stage 1 (MUJ level)

### Framing — why these theorems exist
A linear network maps sources → responses **linearly**: scale a source, the response it causes
scales; add sources, the responses add. Every theorem in this unit is that one fact, specialized.
The elements: **R** (v=Ri), **L** (v=L di/dt → impedance sL), **C** (i=C dv/dt → impedance 1/sC), plus
**independent** sources (fixed) and **dependent/controlled** sources (output ∝ some controlling v or
i elsewhere — VCVS, VCCS, CCVS, CCCS). Dependent sources are what make the unit non-trivial.

### Superposition
- **Statement:** in a linear network with several independent sources, the response (a particular
  branch voltage/current) equals the **sum of the responses** caused by each independent source
  acting alone, all *other independent* sources deactivated. *Mechanism:* linearity — the response is
  a linear combination of the source values, so it splits term-by-term.
- **Deactivate = replace by its zero:** independent **voltage** source → **short** (0 V); independent
  **current** source → **open** (0 A). **Dependent sources are NEVER deactivated** — they depend on
  circuit variables, not on the independent excitation; leave them fully active in every sub-problem.
- **Limits:** applies to **voltage/current** (linear in the sources), **not to power** (power ∝ I²,
  a *nonlinear* function — you cannot superpose powers). Nonlinear elements break it entirely.

### Thévenin's & Norton's theorems
- **Thévenin:** any linear two-terminal (one-port) network, seen from its terminals, is equivalent to
  a single voltage source **V_th** in series with an impedance **Z_th** (R_th for DC). *Mechanism:*
  linearity makes the terminal v–i relation a straight line `v = V_th − Z_th·i`; that line *is* a
  source-plus-resistor.
- **Norton:** the dual — a current source **I_N** in parallel with **Z_N**. Relations:
  **V_th = I_N · Z_th**, **Z_th = Z_N**. Source transformation converts one to the other.
- **Finding the three quantities (the exam method):**
  - **V_th** = open-circuit voltage at the terminals (V_oc).
  - **I_N** = short-circuit current through the terminals (I_sc).
  - **Z_th = V_oc / I_sc** (always valid), **or** deactivate all *independent* sources and find the
    equivalent impedance looking in.
  - **⚠ With dependent sources** you generally **cannot** just "look in" after deactivating, because
    dependent sources stay active. Use the **test-source method**: deactivate *independent* sources,
    apply a 1 V (or 1 A) **test source** at the terminals, find the resulting test current (voltage),
    and **Z_th = V_test / I_test**. (If the network has *no* independent source, V_th = 0 and this is
    the only way to get Z_th.)
- *Why it matters:* Z_th is exactly what reappears in transient analysis (the time constant of the
  one-port is L/R_th or R_th·C) and in maximum-power-transfer.

### Maximum Power Transfer
- **DC / resistive:** a source (V_th, R_th) delivers maximum power to a load **R_L when R_L = R_th**.
  Then P_max = V_th² / (4 R_th). *Mechanism:* P_L(R_L) = V_th² R_L/(R_th+R_L)²; set dP_L/dR_L = 0.
- **AC / complex (verified — Hayt; LibreTexts; Wikipedia):** with Thévenin impedance Z_th = R_th + jX_th
  and a fully adjustable load Z_L = R_L + jX_L, maximum *average* power transfers when
  **Z_L = Z_th\*** (conjugate match): R_L = R_th and **X_L = −X_th** (load reactance cancels source
  reactance). If only |Z_L| is adjustable (angle fixed) or only R_L is adjustable, the optimum
  differs (|Z_L| = |Z_th|, resp. R_L = √(R_th²+X_th²)). `settled`
- **Honest caveat:** maximum power transfer ⇒ **only 50 % efficiency** (equal power dissipated in
  R_th). It is a *signal/communications* objective (get the most signal into the load), **not** a
  *power-systems* objective (there you want high efficiency, R_L ≫ R_th). `settled`

### Networks with dependent sources (the recurring difficulty)
- Keep dependent sources **active** in every theorem application (superposition sub-problems, Z_th
  extraction). The controlling variable must be expressed in terms of the circuit's actual variables.
- **Z_th with dependent sources → test-source method** (above) is the single most-tested skill here.
- Other syllabus-adjacent theorems worth knowing (often appear as short questions): **reciprocity**
  (in a network with one source, no dependent sources, the ratio excitation/response is unchanged if
  source and response ports are swapped — *fails* when dependent sources are present); **Millman's**,
  **Tellegen's** (Σ v_k i_k = 0 over all branches — follows from KVL+KCL alone, holds for any lumped
  network even nonlinear/time-varying), **substitution**, **compensation**. `settled`

### Worked-problem patterns
- Find the Thévenin/Norton equivalent of a one-port **with a dependent source** (test-source method).
- Superposition with mixed independent V and I sources; find one branch current.
- Maximum power transfer: find R_L (DC) or Z_L (AC conjugate) and the resulting P_max.
- Source transformation chains to collapse a ladder of sources to one equivalent.

---
**Stage 2 (deep structure) — ✓ BUILT (2026-06-22):** see `stage-2/01-network-theorems.md`. *Adds:*
why linearity ⇒ the affine terminal law (proof); Thévenin via the superposition/test-source
derivation and its failure modes; Tellegen's theorem as the deep root (conservation, reciprocity,
sensitivity); the conjugate-match derivation and the |Z| / R-only constrained optima; substitution &
compensation theorems from first principles; when no Thévenin equivalent exists.
