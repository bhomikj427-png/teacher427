# Unit 3 — Two-Port Networks

> Confidence: `settled` (canonical; Van Valkenburg ch.11; Sudhakar-Shyammohan; Hayt ch.16).
> Parameter conversions and reciprocity/symmetry conditions **verified this session** (RF-Wireless-
> World, Wikipedia two-port, testbook). *Teaching order:* taught **after** U4 (network functions)
> because each parameter is itself a network function of s. A two-port = a 2×2 matrix relating the
> two port voltages and currents; four equivalent coordinate systems for one black box.

## Stage 1 (MUJ level)

### Framing
A two-port has an input port (V₁, I₁) and output port (V₂, I₂), with currents defined **into** the
top terminal of each port (standard convention). The box is fully described by **two** linear
equations relating these four quantities — pick which two are "causes" and which two are "effects"
and you get a different parameter set. **Assumption for these parameters:** linear, and (for the
matrices to be 2×2 with no source terms) **no independent internal sources**.

### The four parameter sets (definition = the equations + how each parameter is measured)

- **Z (open-circuit impedance) parameters** — V in terms of I:
  V₁ = Z₁₁I₁ + Z₁₂I₂,  V₂ = Z₂₁I₁ + Z₂₂I₂.
  Each Z_ij found by **open-circuiting** a port (set an I = 0): Z₁₁ = V₁/I₁|_{I₂=0}, Z₁₂ = V₁/I₂|_{I₁=0}, etc.
- **Y (short-circuit admittance) parameters** — I in terms of V:
  I₁ = Y₁₁V₁ + Y₁₂V₂,  I₂ = Y₂₁V₁ + Y₂₂V₂. Found by **short-circuiting** a port (set a V = 0).
  **[Y] = [Z]⁻¹** (as matrices).
- **h (hybrid) parameters** — mix; the transistor-model set:
  V₁ = h₁₁I₁ + h₁₂V₂,  I₂ = h₂₁I₁ + h₂₂V₂.
  h₁₁ = V₁/I₁|_{V₂=0} (input impedance, output shorted), h₁₂ = V₁/V₂|_{I₁=0} (reverse voltage gain),
  h₂₁ = I₂/I₁|_{V₂=0} (forward current gain, e.g. β), h₂₂ = I₂/V₂|_{I₁=0} (output admittance).
- **ABCD (transmission / chain) parameters** — input in terms of output, with **I₂ defined OUT of the
  port** (the transmission convention): V₁ = A V₂ − B I₂,  I₁ = C V₂ − D I₂.
  A = V₁/V₂|_{I₂=0} (reverse voltage ratio), B = −V₁/I₂|_{V₂=0} (transfer impedance),
  C = I₁/V₂|_{I₂=0} (transfer admittance), D = −I₁/I₂|_{V₂=0} (reverse current ratio).
  *(Sign of B, D depends on the I₂-direction convention — state it. We use the standard "I₂ out.")*

### Interrelations (the conversion skill — heavily tested)
- All four sets describe the same box, so each converts to the others by algebra. **[Y]=[Z]⁻¹** is the
  cleanest. The full conversion table (Z↔Y↔h↔ABCD) is standard; the exam expects you to **derive** a
  needed conversion, not memorize all 24 entries. Worked example: Z from Y via the 2×2 inverse
  Z = (1/ΔY)[[Y₂₂, −Y₁₂],[−Y₂₁, Y₁₁]].
- **Reciprocity (verified):** a network with **no dependent sources** (only R,L,C,M, transformers) is
  reciprocal, and then **Z₁₂ = Z₂₁**, **Y₁₂ = Y₂₁**, **h₁₂ = −h₂₁**, **AD − BC = 1**. *Mechanism:*
  reciprocity is a structural property of bilateral elements (Tellegen/reciprocity theorem, U1).
- **Symmetry (verified):** the two ports are interchangeable (electrically identical) ⇒ **Z₁₁ = Z₂₂**,
  **Y₁₁ = Y₂₂**, **A = D**. Symmetry ⇒ reciprocity but not conversely.

### Interconnection of two-ports (why the matrices are worth it)
- **Series connection** (ports in series): **Z matrices add** — [Z] = [Z_a] + [Z_b].
- **Parallel connection** (ports in parallel): **Y matrices add** — [Y] = [Y_a] + [Y_b].
- **Cascade / chain** (output of one → input of next): **ABCD matrices multiply** — [T] = [T_a][T_b].
  *This is why ABCD exists* — it makes a chain of stages a matrix product. *(Caveat: series/parallel
  addition is valid only when the **Brune/port condition** holds — the port currents stay balanced
  after connection; flagged in Stage 2.)*

### Filters, image impedance, symmetric T & π (the classical-filter corner)
- **Image impedance Z_I:** the impedance that, terminating a port, is *seen* at the other port — a
  two-port is "image-matched" when each port is terminated in its image impedance, giving reflection-
  free cascading. For a symmetric network the two image impedances are equal (the **characteristic /
  iterative impedance**). Used to design constant-k / m-derived filters. `settled`
- **Symmetric T and π networks:** the two canonical symmetric two-ports. A **T** (two series arms +
  one shunt) and a **π** (one series arm + two shunt) can each realize any symmetric reciprocal
  two-port; they interconvert via the **Y–Δ (star-delta) transformation**. Characteristic impedance
  and **propagation constant γ = α + jβ** (image-impedance design): for a symmetric network
  cosh γ = A (the ABCD parameter), giving attenuation α and phase β per section. `settled`
- **Constant-k and m-derived filters** (classical image-parameter LPF/HPF/BPF) are built by cascading
  such symmetric sections; cutoff and image impedance set by the L,C values. (Image-parameter method
  is older than modern network-synthesis filter design, U5; the syllabus lists it here.) `settled`

### Worked-problem patterns
- Compute Z (or Y, h, ABCD) parameters of a given resistive/LC two-port from the definitions.
- Convert one parameter set to another (esp. Z↔Y, find ABCD of a network).
- Test a network for reciprocity/symmetry from its parameters.
- ABCD of a **cascade** by multiplying the section matrices; find overall gain/impedance.
- Design/analyze a symmetric T or π; find image impedance and propagation constant.

---
**Stage 2 (deep structure) — ✓ BUILT (2026-06-22):** see `stage-2/03-two-port-networks.md`. *Adds:*
the full conversion table derived + when each set **fails to exist** (singular cases, e.g. an ideal
transformer has no Z or Y); reciprocity from Tellegen's theorem rigorously; the validity condition for
series/parallel interconnection (Brune test) and why naïve addition can be wrong; image vs iterative
impedance and the γ = arccosh(A) derivation; ABCD as a transfer matrix and the bridge to scattering
(S) parameters used at RF; constant-k/m-derived filter theory vs modern synthesis (U5).
