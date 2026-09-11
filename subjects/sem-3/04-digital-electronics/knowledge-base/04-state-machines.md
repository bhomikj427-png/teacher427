# U4 — State Machines (Stage 1, MUJ level)

> Scope (verbatim): *finite state machines; design of synchronous FSM; state reduction; timing
> issues in synchronous circuits; algorithmic state machines (ASM); synchronous circuits — pulse
> train generator, pseudorandom binary sequence generator, clock generation; asynchronous circuits.*
> This is where U1 (combinational minimization) and U3 (flip-flops) **fuse**. Tier-1: Anand Kumar,
> Jain, Brown & Vranesic; LFSR maximal-length triangulated vs Wikipedia+GfG+Analog Devices.

---

## 0. Frame — the universal model

Every synchronous sequential circuit is a **finite-state machine**: a **state register** (FFs) +
**next-state combinational logic** + **output combinational logic** (big idea 5). The whole unit is
*procedures over this one structure*. `settled`.

**Moore vs Mealy** (`settled`, triangulated):
- **Moore:** output = f(present state) only. Outputs are stable for a whole state/clock, change
  synchronously, may need **one more state** than Mealy.
- **Mealy:** output = f(present state, **input**). Fewer states, but outputs can change *between*
  clock edges with the input and can **glitch** (misconception M12). The two are convertible.

---

## 1. Synchronous FSM design procedure (the load-bearing pipeline)

The canonical exam method (`settled`, every text):
1. **State diagram** from the word spec (e.g. "detect 1011, overlapping").
2. **State table** (present state × input → next state, output).
3. **State reduction** (§2) — merge equivalent states.
4. **State assignment** — bind binary codes to states (choice affects logic cost & hazards;
   misconception M14). Common: binary, gray, one-hot.
5. **Choose FF type**; build the **transition/excitation table** using U3's excitation tables.
6. **K-map** each FF input + each output → minimal next-state & output equations.
7. Draw register + next-state logic + output logic.

**Exam pattern (the big one):** "Design a 1011 sequence detector (Mealy and Moore)." Carry it
end-to-end; it touches every skill in U1+U3+U4.

---

## 2. State reduction

Merge **equivalent states**: two states are equivalent iff, for *every* input sequence, they give the
same outputs **and** go to equivalent next states. Removing them shrinks FFs/logic **without changing
behavior** (misconception M13). `settled`.
- **Methods:** *implication chart* (systematic pairwise check) or *partitioning* (successive
  refinement into equivalence classes). `settled`.
- Fewer states can mean fewer FFs (⌈log₂(#states)⌉), so reduction precedes assignment. `settled`.

---

## 3. Timing issues in synchronous circuits

Even with one clock, finite delay bites (extends U3 §6). `settled`:
- **Clock skew:** clock reaches FFs at different times → can violate setup (too much skew along data
  direction) or **hold** (skew against data direction → a fast path corrupts the next FF). The
  nastier one: hold violations can't be fixed by slowing the clock. `settled`.
- **Hazards/glitches in the output logic:** combinational outputs can momentarily glitch during a
  state transition (esp. Mealy) — register the output (Moore-style) or design glitch-free if the
  output is used asynchronously. `settled`.
- **Metastability at asynchronous inputs:** any input not synchronized to the clock can violate
  setup → use a **2-FF synchronizer** to reduce (not eliminate) failure probability. `settled`.

---

## 4. Algorithmic State Machine (ASM) charts

An **ASM chart** is a flowchart-style notation for FSMs, better than a state diagram for
datapath/control design. Three elements (`settled`, Brown & Vranesic / standard):
- **State box** (rectangle): one state per clock; lists Moore (unconditional) outputs.
- **Decision box** (diamond): tests an input → branches.
- **Conditional output box** (oval): Mealy outputs, active only on a branch.
- One **ASM block** = one state box + the decision/conditional boxes reachable from it in one clock;
  it defines exactly one clock cycle's behavior. Maps directly to next-state + output logic. `settled`.

**Exam pattern:** convert a state diagram ↔ ASM chart; read the next-state/output logic off an ASM block.

---

## 5. Standard synchronous-circuit applications

**Pulse-train (sequence) generator.** An FSM/counter + output logic that emits a fixed bit pattern,
one bit per clock (e.g. a counter addressing a pattern, or a Johnson counter decoded). Period = #states.
`settled`.

**Clock generation — two distinct meanings (cover both).**
- **(i) Frequency division (from an existing clock).** A mod-N counter divides a clock by N (output
  toggles every N counts → ÷2N for a square wave, or decode for ÷N). Chains of FFs give ÷2ᵏ. `settled`.
- **(ii) Generating the clock itself — the oscillator/multivibrator hardware** (this is the part the
  divider presupposes; **verified this session**, triangulated):
  - **Multivibrator taxonomy:** **astable** (no stable state → free-running oscillator, makes a clock),
    **monostable** (one stable state → one-shot pulse of fixed width, for debounce/timing), **bistable**
    (two stable states = a latch/flip-flop, U3). Misconception alert (M20). `settled`.
  - **555 timer — astable:** **f = 1.44 / ((R₁ + 2R₂)·C)** (the 1.44 = 1/ln2; t_high=0.693(R₁+R₂)C
    charges through R₁+R₂, t_low=0.693·R₂·C discharges through R₂ → **duty cycle always > 50%** in the
    standard config). **555 monostable:** pulse width **T = 1.1·R·C** (1.1 = ln3, charge 0→⅔V_CC).
    `settled` (allaboutcircuits + electronics-tutorials + circuitdigest).
  - **Ring oscillator:** an **odd** number N of inverters in a loop (no stable state) →
    **f = 1/(2·N·t_pd)**. On-chip, cheap, but frequency drifts with process/voltage/temperature → used
    for delay characterization, not precision timing. `settled` (JHU handout + elprocus).
  - **Crystal oscillator:** a quartz crystal sets frequency by mechanical resonance → very high
    stability/accuracy (ppm) → the real system clock source. `settled (standard)`.
  - **Schmitt trigger:** a comparator with **hysteresis** (two thresholds V_T+ > V_T−). Cleans slow/
    noisy edges into sharp logic transitions and rejects noise within the hysteresis band — used to
    condition a clock/input and (with an RC) to *build* a relaxation oscillator. Cross-links to noise
    margin (U5). `settled (standard)`.

**Pseudo-random binary sequence (PRBS) generator — LFSR** (**verified this session**, triangulated
Wikipedia + GfG + Analog Devices): an n-bit shift register with **XOR (or XNOR) feedback** from
selected **tap** positions. `settled`:
- With a **primitive feedback polynomial over GF(2)**, the LFSR is **maximal-length**: it cycles
  through **all 2ⁿ−1 non-zero states** before repeating (an *m-sequence*). `settled`.
- **The all-zeros state is a lockout** (XOR feedback: 0→0 forever) — so seed must be non-zero; an
  XNOR LFSR locks up on all-ones instead. `settled`.
- Output looks random (flat autocorrelation, balanced 1s/0s) but is deterministic & repeatable →
  used for test patterns (BIST), scramblers, spread-spectrum. `settled`.
- **Exam pattern:** for a given 4-bit LFSR with taps, trace the state sequence, find the period,
  confirm it's 2⁴−1=15 (maximal) or shorter (non-primitive).

---

## 6. Asynchronous (sequential) circuits

No clock — state changes follow **input changes** directly (the latches of U3 generalized).
`settled`:
- **Fundamental-mode** assumption: inputs change one at a time, circuit settles before the next change.
- **Analysis:** excitation/flow table with **stable states** (where next-state = present-state);
  transitions move between stables.
- **Hazards are first-class here:** **static-1 / static-0 hazards** (a glitch when a single input
  change should hold the output) removed by adding **consensus-term** redundant gates (U1 §1);
  **dynamic hazards**; **essential hazards** (cured by delay). `settled`.
- **Races:** two state variables change → **non-critical** (same final state regardless of order) vs
  **critical** (final state depends on order — a design bug). Fix by race-free state assignment. `settled`.
- Faster (no clock latency) but far harder to design correctly → why synchronous design dominates.
  `settled`.

**Exam pattern:** find static hazards in a given function and remove with consensus terms; identify a
critical race in a flow table.

---

## 7. Worked-problem patterns (Stage-1 exit targets)
1. Design a 101 / 1011 overlapping sequence detector, both Mealy and Moore (full pipeline).
2. Reduce a given state table (implication chart) and re-design with minimal FFs.
3. Trace a 4-bit LFSR; show maximal-length period and the all-zero lockout.
4. Draw an ASM chart for a given controller; derive its equations.
5. Remove a static-1 hazard with a consensus term; identify a critical race.
6. Design a ÷5 clock divider / a fixed pulse-train generator.

## Stage-1 exit test (this unit)
Representative (no PYQ → `uncertain` targeting): **(a)** Design a Mealy 1011 overlapping detector
end-to-end (diagram→table→reduce→assign→JK equations). **(b)** For a 3-bit LFSR with feedback x³+x+1,
list the state sequence and its period. **(c)** Why is the all-zeros LFSR state a lockout, and how does
a Mealy output differ in timing from a Moore one? → answerable from §1–§6 with verified LFSR facts.
**PASS** (mechanism shown; targeting unconfirmed).

---

→ **Stage 2** (`stage-2/04-...md`) will add: FSM minimization optimality + the implication-chart
proof; state-assignment as a graph-embedding/hazard-minimization problem; m-sequence algebra
(GF(2ⁿ), trace, correlation properties) and Gold/CDMA codes; ASMD (ASM + datapath) for RTL;
hazard-free async synthesis (Huffman), burst-mode/fundamental-mode theory; metastability MTBF.
Cross-link: this is exactly RTL FSM coding in `../../../verilog`.
