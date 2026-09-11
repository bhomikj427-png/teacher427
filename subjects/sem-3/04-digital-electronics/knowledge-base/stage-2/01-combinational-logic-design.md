# U1 — Combinational Logic Design (Stage 2: deep structure + frontier)

> Extends `../01-combinational-logic-design.md` — does **not** replace it. First-principles,
> model limits, unification, frontier, harder problems. Primary: Brown & Vranesic, De Micheli,
> Weste-Harris; parallel-prefix + 2's-complement verified this session (`sources.md`).

---

## A. Boolean algebra is a *structure*, not a bag of identities

A Boolean algebra is the algebraic structure ⟨B, +, ·, ′, 0, 1⟩ satisfying the **Huntington
postulates** (commutativity, distributivity *both ways*, identities 0/1, complement). Two faces of
the *same* structure, and this duality is the deep reason every identity comes in pairs:
- **As a complemented distributive lattice:** + = join (⊔), · = meet (⊓), with a partial order
  a ≤ b ≝ a·b = a. Minterms are the **atoms**; every element is a unique join of atoms → *that* is
  why the SOP canonical form is unique (it's the atomic decomposition). `settled (standard)`.
- **As a Boolean ring (GF(2)-algebra):** with XOR as "+", AND as "·", every element idempotent
  (a²=a). This is the **Reed–Muller / algebraic-normal-form** world: any function = XOR of AND-terms,
  f = c₀ ⊕ c₁x₁ ⊕ … ⊕ c₁₂x₁x₂ ⊕ … The ANF is what makes XOR-heavy logic (parity, crypto, arithmetic)
  compact where SOP explodes. `settled (standard)` (Brown & Vranesic; standard algebra).
- **Duality principle** (proved, not asserted): any theorem stays true under (+↔·, 0↔1) because the
  axioms are self-dual. Saves half the proofs. `settled`.
- **Stone's representation theorem** (the why-it's-built-this-way): *every* finite Boolean algebra is
  isomorphic to the power set of its atoms (2ⁿ truth table). So "function of n bits" and "subset of
  the 2ⁿ minterms" are the same object — the truth table *is* the algebra. `settled (standard)`.

---

## B. Minimization — what's really being optimized, and its hardness

- **Two-level (SOP) minimization is exact but NP-hard.** Quine–McCluskey finds *all* prime implicants
  (exponential in the worst case) then solves a **minimum-cover** problem (the PI chart = a set-cover /
  unate-covering instance, NP-hard). **Petrick's method** turns the chart into a POS of "this minterm
  must be covered" clauses, multiplies out, and picks the minimum-cost product → the provably minimal
  cover. K-maps are just the human-pattern-matcher for ≤4 vars. `settled (standard)` (De Micheli §7).
- **ESPRESSO** (the industrial heuristic) abandons exactness for EXPAND/REDUCE/IRREDUNDANT iteration —
  near-minimal in polynomial time. The lesson: **exact minimization doesn't scale; real tools are
  heuristic.** This is where the UG K-map story stops and synthesis begins. `settled (standard)`.
- **Multilevel logic** (real circuits aren't 2-level): factoring (e.g. ab+ac+ad = a(b+c+d)) trades
  levels (delay) for literals (area). Technology mapping then binds to a real cell library / LUTs.
  The K-map minimizes *literals*; a synthesizer minimizes a **delay×area×power** cost under a real
  library. `settled (standard)`.
- **Where the UG textbook lies:** "minimal = fewest gates" is false at speed — fan-in, fan-out, wire
  load, and glitch power all matter; a "minimal" 2-level SOP can be slower and burn more power than a
  factored multilevel form. Minimization is multi-objective. `settled`.

---

## C. Arithmetic, derived from the ring ℤ/2ⁿℤ

- **Why 2's complement (not sign-magnitude / 1's complement):** n-bit hardware computes in the ring
  **ℤ mod 2ⁿ**. 2's complement maps {−2ⁿ⁻¹ … 2ⁿ⁻¹−1} onto residues so that **−x ≡ 2ⁿ − x (mod 2ⁿ)**,
  hence **A − B = A + (2ⁿ − B) = A + B̄ + 1** — *one* adder does add and subtract, with **no special
  end-around carry** (1's complement needs that) and a **single zero**. Overflow = "carry-in to the
  sign bit ≠ carry-out of it." This is *derived* from modular arithmetic, not a convention to memorize.
  ✓ reasoning verified this session. `settled`.
- **Carry-lookahead, properly: carry is a prefix computation.** Define the operator on (g,p) pairs:
  (g₁,p₁) ∘ (g₀,p₀) = (g₁ + p₁·g₀, p₁·p₀). This operator is **associative** (the key fact) → carries
  are the **prefix products** C_i = (G:P)_{i-1} ∘ … ∘ (g₀,p₀). Associativity means the prefix can be
  computed as a **balanced tree in O(log n) depth** instead of ripple's O(n). ✓ verified this session.
  `settled`:
  - **Kogge–Stone:** depth = log₂n, lower fan-out, **fastest**, but most area/wiring (O(n log n) cells).
  - **Brent–Kung:** depth = **2·log₂n − 2**, ~half the cells/wiring, slower — the area/speed dual.
  - Sklansky, Han-Carlson interpolate. This is the deep generalization of the Stage-1 CLA: **CLA is a
    1-level prefix; KS/BK are the log-depth optimum.** Cross-topic: same prefix-scan pattern as parallel
    reduction in software. `settled`.
- **Carry-save adder (CSA):** for *summing many numbers* (multipliers), keep carries un-propagated as
  a second vector; an n-operand sum needs only **one** carry-propagate at the very end (Wallace/Dadda
  trees). The ripple/lookahead delay is paid **once**, not per operand. `settled (standard)`.
- **BCD/excess-3, derived:** the "+6" of Stage-1 is "skip the 6 illegal codes of a 4-bit field used
  base-10"; excess-3 is self-complementing (9's complement = bit-complement) — *why* some BCD
  arithmetic prefers it. `settled (standard)`.
- **Booth multiplication (adjacent — lives in Computer Arithmetic/COA, flagged for completeness):** a
  signed-multiply algorithm that recodes runs of 1s to cut partial products; the *combinational* form is
  a Wallace/Dadda tree of carry-save adders + a final CPA (§above). Mechanism noted; full treatment is
  out of this course's scope (→ COA). `likely`.

---

## C½. Error-control coding (parity → Hamming) — IIT/NPTEL-standard, beyond MUJ verbatim

This is **not in the MUJ verbatim syllabus** but is standard in IIT/NPTEL digital courses and is the
natural depth behind U1's parity generator; included as enrichment, flagged as out-of-MUJ-scope.
- **Parity** = 1 XOR-tree bit → single-error **detection**, zero correction. `settled`.
- **Hamming (SEC):** place r parity bits at positions 2⁰,2¹,… each checking a fixed bit-subset; the
  XOR of failed checks (the **syndrome**) gives the *position* of a single bit error → **single-error
  correction.** Bound (✓ verified this session): **2ʳ ≥ m + r + 1** (m data bits) — e.g. the **(7,4)
  Hamming code** (m=4, r=3). Adding one overall parity bit → **SEC-DED** (Hamming distance 4). `settled`
  (angms.science ITC notes + Hamming's original paper).
- **Deep tie:** parity/Hamming/CRC/BCH/Reed–Solomon are all **GF(2) linear algebra** — the *same*
  algebra as the LFSR (`stage-2/04` §C: LFSR = polynomial division = a CRC). One thread: XOR logic →
  ANF (§A) → linear codes → m-sequences. `settled`.

---

## D. Cross-topic unification
- **MUX = Shannon expansion (→ U2), decoder = full minterm basis, PROM = truth table in silicon
  (→ U5), LUT = the same idea in an FPGA (→ `../../../verilog`).** "Implement any function" has one
  root: a complete set of minterms + a programmable OR.
- **Adders ↔ counters ↔ FSMs:** an adder is the next-state logic of a binary counter; arithmetic is
  just a structured combinational function feeding the U3/U4 state register.
- **Parity/XOR ↔ ANF ↔ error-correcting codes ↔ LFSR (→ U4):** all live in GF(2) linear algebra.

## E. Harder problems (the §0 surplus test — answer from mechanism)
1. Prove the (g,p) carry operator is associative; use it to derive Kogge-Stone depth. ✓ (§C).
2. Show 2's-complement subtraction needs no end-around carry but 1's-complement does — from ℤ/2ⁿℤ. ✓.
3. Give a function whose minimal SOP is *slower* than a factored multilevel form; explain. ✓ (§B).
4. Convert a 3-var function to ANF (Reed–Muller) and explain when ANF beats SOP. ✓ (§A).
5. Why is exact 2-level minimization NP-hard? Map the PI chart to set cover; apply Petrick. ✓ (§B).
6. Build an 8-operand adder with one carry-propagate (carry-save tree); count the CPA delays. ✓ (§C).

**§0 surplus exit (U1 Stage 2): PASS** — base answers each from mechanism with primary sourcing
(parallel-prefix + modular arithmetic verified this session; algebra/synthesis cited to De Micheli /
Brown & Vranesic).

→ Frontier/open: approximate adders (error-tolerant DSP), in-memory/threshold logic, post-CMOS
(reversible/quantum adders — see arXiv Toffoli-depth work). Logged to register, not load-bearing here.
