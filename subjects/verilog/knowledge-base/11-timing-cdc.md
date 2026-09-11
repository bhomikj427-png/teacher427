# U11 — Timing: Setup/Hold, Metastability, Clock-Domain Crossing (deep notes) [PROFESSIONAL]

> Deep pass 2026-06-15. The physical-reality layer that constrains all synchronous design. Verilog
> RTL doesn't *express* most of this directly, but professional RTL is written *for* it.

## A. Setup & hold time
- **Setup time:** input data must be stable for a window **before** the clock edge. **Hold time:**
  stable for a window **after** the edge. Violate either → the flop may go **metastable**.
  `[settled — timing/metastability refs]`
- The **max clock frequency** of a synchronous design is set by the **longest combinational path**
  between flops (must settle within one period minus setup) — the static-timing-analysis (STA)
  critical path. `[settled]`

## B. Metastability
- A setup/hold violation can leave a flop output at an **unresolved intermediate voltage** for an
  unpredictable time before settling to 0 or 1 (or the wrong value). It always resolves
  *eventually*, but the resolution time is probabilistic. `[settled]`
- It cannot be eliminated for truly asynchronous inputs — only made **improbable enough** (MTBF).

## C. Clock-domain crossing (CDC) & synchronizers
- A signal crossing from one clock domain to an asynchronous other has nonzero probability of
  violating the destination flop's setup/hold → metastability. `[settled — CDC refs]`
- **Two-flop synchronizer:** two destination-clocked flops in series; the first may go metastable,
  the second gets ~a full clock period to let it resolve before the value is used. Reduces failure
  probability dramatically. Three flops for very high reliability/fast clocks. `[settled]`
- **MTBF** (mean time between failures) quantifies residual risk; depends on technology, clock
  frequency, resolution time between flops, and input toggle rate. `[settled — MTBF refs]`
- **Multi-bit CDC needs more than a 2-flop sync** (bits could resolve in different cycles) — use
  gray-coded buses, handshakes, or async FIFOs. `[settled — CDC literature]`

## What the engine teaches from this
Professional-tier; sequenced after the learner designs real clocked logic/FSMs. Largely conceptual
+ pattern recognition (recognize a CDC, apply the right synchronizer). Productive failure: show a
single-flop async input and have them reason out why it can corrupt state.

## Confidence / gaps
All `settled` at the conceptual level taught. Exact MTBF formula constants/library-specific numbers
are tool/process-dependent — teach the *form* and dependencies, not invented constants. No open
items requiring re-verification before teaching at this depth.
