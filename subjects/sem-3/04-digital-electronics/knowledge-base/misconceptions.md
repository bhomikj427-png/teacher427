# ECE2102 Digital Electronics — misconceptions (predictable novice errors)

> Per `../../../../subject-research-protocol.md` §4. Each is a *claim* and is confidence-marked.
> Sourced to digital-design-education / documented-error literature and the prescribed texts where
> possible; recall-only ones are `uncertain` and flagged to-verify. This is the **map-pass seed** —
> expanded and sourced per unit as Stage 1 builds. **A subject with no misconception list is
> under-researched** (§4).

Status legend: `settled` (well-documented error) · `likely` (standard teaching folklore, strong but
single-/derivative-sourced) · `uncertain` (recall-only, to-verify).

## Combinational / Boolean (U1–U2)
- **M1 — "More gates = more powerful / a different function."** Students think a bigger circuit does
  something a minimized one doesn't. Truth: a function's minimal and non-minimal forms are *logically
  identical*; minimization changes cost/speed, not behavior. `likely`.
- **M2 — Treating the K-map as a magic grid, not visual Boolean algebra.** Not knowing groups must be
  powers of two, must use gray-code adjacency (incl. edge wrap-around), and that a group of 2^k cells
  eliminates k variables. Leads to invalid groupings. `likely` (Brown & Vranesic notes this stall).
- **M3 — Don't-cares must be assigned a fixed 0 or 1 before mapping.** Students force don't-cares
  instead of using each as whichever value enlarges a group. `likely`.
- **M4 — XOR is "either-or" / same as OR.** Confusing inclusive OR with exclusive OR; missing that
  XOR = inequality detector / parity / controlled-inverter — central to adders and comparators. `likely`.
- **M5 — Confusing active-low vs active-high and the bubble notation** on decoders/encoders/enables;
  reading an active-low enable as active-high. `likely`.
- **M6 — Encoder = decoder run backwards, with no caveats.** Missing that a plain encoder breaks on
  multiple simultaneous active inputs (→ need a *priority* encoder), and the all-zero ambiguity. `likely`.

## Sequential (U3)
- **M7 — A latch and a flip-flop are the same thing.** Missing the level-sensitive (latch) vs
  edge-triggered (FF) distinction — the root of most timing bugs. `settled` (universal text treatment).
- **M8 — The JK "race" / "indeterminate" confusion.** Thinking SR's forbidden state (S=R=1) and JK's
  *toggle* at J=K=1 are the same; or that a *level-triggered* JK at J=K=1 doesn't race (it does —
  this is exactly why master-slave/edge-trig exists). `likely`.
- **M9 — A flip-flop changes output "whenever the clock is high."** Missing that an edge-triggered FF
  samples only at the active *edge*; the rest of the period it holds. `likely`.
- **M10 — Ripple (asynchronous) counters are just slower synchronous counters.** Missing that ripple
  counters accumulate stage delays → transient false counts/decoding spikes, and have no common clock.
  `likely`.
- **M11 — "Setup/hold are the same as propagation delay."** Conflating the FF's input timing window
  with its output delay. `likely`.

## FSM / state machines (U4)
- **M12 — Moore and Mealy are interchangeable with identical outputs.** Missing that Mealy outputs
  can change asynchronously with inputs mid-state (and can glitch), Moore outputs are registered/stable
  per state; the I/O timing differs. `likely`.
- **M13 — State reduction changes what the machine does.** Thinking merging equivalent states alters
  behavior; truth: equivalent states are externally indistinguishable, reduction only shrinks cost.
  `likely`.
- **M14 — Any state assignment is as good as any other.** Missing that encoding choice affects
  next-state logic cost and can create/avoid hazards. `settled` (resolved Stage 2: it's an NP-hard
  embedding/cost+hazard optimization — one-hot vs binary vs adjacent; De Micheli §9, Brown & Vranesic.
  See `stage-2/04` §B).

## Clock generation / multivibrators (U4)
- **M20 — "Multivibrator" means oscillator; a flip-flop is something separate.** Truth: the three
  multivibrators are one family — **astable** (oscillator, no stable state), **monostable** (one-shot),
  **bistable** (= the latch/flip-flop of U3). The FF *is* the bistable multivibrator. `likely`.
- **M21 — A 555 astable can give exactly 50% duty cycle in the basic config.** Truth: C charges
  through R₁+R₂ but discharges only through R₂ → duty cycle is always **> 50%** unless a diode/extra
  network is added. `likely`.

## Timing & logic families (U5)
- **M15 — Logic 0 and logic 1 are exact voltages (0 V and 5 V).** Missing the *band* model
  (V_OL/V_OH output bands, V_IL/V_IH input thresholds) and the forbidden region — which is the whole
  basis of noise margin. `settled`.
- **M16 — Higher fan-out is always better.** Missing that exceeding rated fan-out degrades V_OH/V_OL
  past the noise-margin guarantee and slows edges. `likely`.
- **M17 — "TTL and CMOS interface directly because both are 5 V."** Missing the V_IH/V_IL mismatch
  (TTL V_OH can be as low as ~2.4 V; CMOS needs ~3.5 V) → needs pull-ups/level handling. `likely`.
- **M18 — CMOS draws no power.** Missing that *static* power is ~zero but *dynamic* power (CV²f) and
  short-circuit current during switching are real and dominate at speed. `settled`.
- **M19 — A floating (unconnected) CMOS input is a safe logic 0.** Truth: high input impedance leaves
  it indeterminate/noise-driven → must be tied. `likely`.

## Open to-verify (misconceptions to source in Stage 1/2)
- M14 state-assignment cost — source to Brown & Vranesic / De Micheli.
- Confirm M8 JK-race framing against Anand Kumar's exact treatment.
- Add memory-specific misconceptions (volatile vs non-volatile, ROM "read-only" literalism, address
  vs data width) when U5 memories is built.
