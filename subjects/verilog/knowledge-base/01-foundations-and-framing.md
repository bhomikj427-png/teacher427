# U1 — Digital-Logic Foundations & the HDL Framing (deep notes)

> Deep pass 2026-06-15. Covers the prerequisite digital logic the language *describes*, and the
> master reframe (threshold T1). Mechanism-first, confidence-marked.

## A. The hardware Verilog describes (prerequisite, must be solid before modeling it)
- **Binary & boolean algebra.** Bits (0/1), AND/OR/NOT/XOR, truth tables, De Morgan. Any logic
  function = a boolean expression = a network of gates. `[settled]`
- **Combinational logic.** Output is a pure function of *current* inputs — no memory. Adders,
  muxes, decoders, comparators. Settles after a propagation delay; no clock. `[settled — Harris &
  Harris Ch.2]`
- **Sequential logic.** Output depends on inputs *and stored state*. Built from **flip-flops**
  (edge-triggered storage) — the D flip-flop captures D on the clock edge and holds it. State +
  a clock = memory of the past. `[settled — Harris & Harris Ch.3]`
- **The clock.** A periodic signal whose edges (usually rising) mark *when* flip-flops sample.
  Synchronous design = (almost) everything updates on the same clock edge. This regularity is what
  makes large designs tractable. `[settled]`
- **Why this matters for Verilog:** combinational vs sequential is the **fundamental fork** the
  whole language is organized around (continuous/`always @*` vs `always @(posedge clk)`); if the
  learner is shaky here, every later distinction (wire/reg, blocking/nonblocking, latch inference)
  is built on sand. **Diagnose this explicitly** — adders prove combinational only.

## B. Threshold T1 — Verilog describes concurrent hardware; it is not a running program
- **The core claim:** Verilog source maps to *physical structure* (gates, wires, registers) that
  all exists simultaneously and operates in parallel, continuously. There is no program counter
  stepping through your lines. `[settled — IEEE 1364 scope; Cummings; universal]`
- **Mechanism of the illusion:** simulators *do* run on a CPU via an event queue (see U6), so it
  can *look* sequential — but that's the simulator's bookkeeping, not the hardware's behavior. The
  synthesized chip has no queue; it's just gates settling.
- **Where sequencing legitimately exists:** *inside* one procedural (`always`/`initial`) block,
  statements have ordering semantics — but even that describes hardware, and the ordering rules
  differ for `=` vs `<=` (U6). Across blocks/assignments, **order is undefined** (Cummings).
- **Diagnostic value:** asking "does this run top-to-bottom?" cleanly separates a learner who has
  crossed T1 from one who hasn't, regardless of how much syntax they know.

## What the engine teaches from this
Open the subject by confirming the foundation (retrieval, not lecture) and probing T1 directly. A
learner who has built adders but answers "yes, top-to-bottom" is **pre-threshold** — route to
productive contrast (show two `assign`s and ask which "runs first"; the answer is "both, always").

## Confidence / gaps
All `settled`. No open items for this unit.
