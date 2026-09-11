# U4 — State Machines (Stage 2: deep structure + frontier)

> Extends `../04-state-machines.md`. Deep idea: **FSMs are the bridge from automata theory to silicon**,
> and the LFSR is **linear algebra over GF(2)**. Primary: Brown & Vranesic, De Micheli, Unger, Golomb;
> m-sequence postulates verified this session (`sources.md`).

---

## A. State minimization — the theory behind the implication chart

- **Equivalence is a congruence.** "p ≡ q iff ∀ input strings they emit the same output" is an
  equivalence relation that is a **congruence** w.r.t. the transition function (equivalent states go to
  equivalent states). The quotient machine (states = equivalence classes) is the **unique minimal**
  completely-specified machine — the Myhill–Nerode theorem specialized to a finite Moore/Mealy machine.
  `settled (standard)` (Brown & Vranesic; Kohavi). The **implication chart** is just the algorithm that
  computes this congruence by successive refinement (partition coarsening); Hopcroft's version is
  O(n log n). `settled`.
- **The white lie:** "minimize then it's optimal." For **incompletely-specified** machines (don't-care
  outputs/transitions — the usual case), "compatibility" is **not transitive**, minimization becomes a
  **maximal-compatible / minimum-closed-cover** problem that is **NP-hard** — you can't just merge
  pairwise. UG courses only ever show the completely-specified easy case. `settled (standard)` (De Micheli §9).

---

## B. State assignment = the real optimization (and hazard control)

The binary codes you assign to states determine the next-state/output **logic cost** and its
**hazards** — it is *not* arbitrary (Stage-1 misconception M14, now resolved):
- **One-hot** (1 FF/state): trivial, fast next-state logic, no decode — standard for FPGAs (FFs are
  free, logic is the LUT). **Dense binary**: ⌈log₂N⌉ FFs, more next-state logic. **Gray/adjacent**
  assignment minimizes simultaneous bit changes → fewer output glitches and easier async. The choice is
  an **embedding/cost-minimization** problem (NSC, MUSTANG heuristics). `settled (standard)` (De Micheli §9).
- **Output glitches:** Mealy outputs are combinational functions of (state,input) → they **glitch**
  during transitions; register them (→ Moore-style "registered Mealy") if used to gate clocks/resets.
  This is why a state machine that "works in simulation" can fail driving an async load. `settled`.

---

## C. The LFSR is linear algebra over GF(2) (the real m-sequence theory)

An n-bit LFSR is a linear map **s(t+1) = A·s(t)** over GF(2), A the companion matrix of the feedback
polynomial g(x). Everything follows from g(x):
- **Maximal length 2ⁿ−1 ⇔ g(x) is primitive** (irreducible, and x is a generator of the multiplicative
  group of GF(2ⁿ)). Then the state visits **every nonzero vector once** before repeating — the nonzero
  states are the powers of a primitive element. The **all-zeros state is the fixed point 0** (A·0=0),
  hence the lockout (XNOR variant fixes at all-ones). ✓ structure verified this session. `settled`.
- **m-sequences satisfy Golomb's three randomness postulates** (✓ verified: IIT-G/Springer/Golomb):
  **R1 balance** (2ⁿ⁻¹ ones vs 2ⁿ⁻¹−1 zeros, differ by 1); **R2 run** distribution (½ runs length-1,
  ¼ length-2, …); **R3 two-level autocorrelation** (peak 2ⁿ−1, off-peak −1) — *that flat
  autocorrelation* is exactly what makes them "pseudo-noise." `settled`.
- **Why it matters (cross-topic):** the same GF(2) machinery is **CRC/checksum** (LFSR = polynomial
  division), **scramblers**, **BCH/Reed–Solomon** error correction, and **Gold/CDMA spreading codes**
  (sums of m-sequence pairs with bounded cross-correlation). The U4 toy is the kernel of coding theory
  and spread-spectrum comms. `settled (standard)` (Golomb; standard coding texts).
- **Fibonacci vs Galois LFSR:** external-XOR (Fibonacci) vs distributed-XOR (Galois) — same sequence
  set, the Galois form has shorter critical path (one XOR delay) → preferred in fast hardware. `settled (standard)`.

---

## D. Asynchronous sequential circuits — the hard theory (Huffman)

Clockless design is *harder*, and Stage 2 makes the hazards rigorous (Unger/Huffman):
- **Huffman synthesis:** primitive flow table → merge compatible rows → **race-free (critical-race-free)
  state assignment** (often needs unit-distance codes / extra states, e.g. via a "shared row" or
  one-hot) → excitation equations. `settled (standard)` (Unger 1969).
- **Essential hazards** are the killer: a hazard *inherent to the state diagram* (not removable by
  adding consensus terms — those only kill **logic/static hazards**). Detected when an input change,
  if it propagates faster than a state variable, drives the machine to a wrong stable state. **Cured
  only by adding delay** in the feedback path. This is the deep reason synchronous design dominates:
  the clock turns every essential hazard into a non-issue. `settled (standard)` (Unger; confirm exact
  minimal-delay condition — `likely`, to source).
- **Fundamental-mode vs input-output (burst) mode**, and **delay-insensitive / speed-independent**
  async (the modern resurgence: NoCs, low-EMI, energy-proportional logic). `likely` (frontier).

---

## E. Cross-topic unification
- **FSM = automaton (theory) = state register + combinational logic (silicon)** — U1 (minimization) and
  U3 (FFs) literally fuse here; next-state/output logic *is* the combinational problem of U1.
- **Counter ⊂ FSM ⊂ sequential machine**; an ASM chart = an FSM = a Verilog `always` state block
  (→ `../../../verilog`); the datapath+control (ASMD) split is the basis of all RTL/CPU design.
- **LFSR ↔ GF(2) linear algebra ↔ U1 XOR/ANF ↔ coding theory** — one algebraic thread.

## F. Harder problems (§0 surplus test)
1. Prove the minimal completely-specified FSM is unique (congruence/Myhill–Nerode); why does it fail
   for incompletely-specified machines? ✓ (§A).
2. Show maximal length ⇔ primitive g(x); why is all-zeros a fixed point? ✓ (§C).
3. Verify Golomb R1–R3 for a 4-bit m-sequence (period 15). ✓ (§C).
4. Exhibit an essential hazard and show consensus terms can't fix it — only delay can. ✓ (§D).
5. Compare one-hot vs binary assignment on logic cost and glitch behavior. ✓ (§B).
6. Explain an LFSR as polynomial division → a CRC. ✓ (§C).

**§0 surplus exit (U4 Stage 2): PASS** — minimization theory, GF(2) m-sequence algebra (verified),
and async essential hazards answered from mechanism; cited to Brown & Vranesic/De Micheli/Unger/Golomb.
Essential-hazard exact delay bound flagged `likely` in register.
