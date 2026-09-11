# U7 — Finite State Machines (deep notes)

> Deep pass 2026-06-15. The first "real design" pattern; composes U4 (comb next-state/output) +
> U5/U6 (clocked state register). Sources: Berkeley EECS151 FSM note, Xilinx/AMD lab, course notes.

## A. The model
- An FSM = **state register** (current state) + **next-state logic** (combinational, from state +
  inputs) + **output logic** (combinational, from state [+ inputs]). `[settled — Harris & Harris;
  EECS151]`
- **Moore:** outputs depend on **state only** → outputs are glitch-free/registered-friendly, change
  only at clock boundaries. `[settled]`
- **Mealy:** outputs depend on **state + current inputs** → fewer states, faster reaction, but
  outputs can be combinationally sensitive to inputs (can glitch). `[settled]`

## B. Coding styles (style-contested — teach as judgment)
- **Two-block (recommended common idiom):** one `always @(posedge clk)` for the state register
  (nonblocking, U6), one `always @*` for next-state + output logic (blocking, full assignment to
  avoid latches, U4). `[settled — widely taught; EECS151]`
- **Three-block:** split next-state and output into separate combinational blocks (clarity).
- **One-block:** everything in the clocked block (compact, registered outputs, but mixes concerns).
- No single style is "correct"; choose for clarity/registered-output needs. `[contested — by design]`

## C. State encoding
- Symbolic states via `localparam`/`parameter` (or SV `enum`). Encodings: **binary** (fewest
  flops), **one-hot** (one flop per state — fast next-state logic, FPGA-friendly), **gray**
  (adjacent transitions flip one bit). Tool can auto-encode. `[settled]`
- **Always handle the default/unreachable state** (reset to a known state; `default` in the case)
  — avoids lockup and latch inference. `[settled — links U4 latch rule]`

## What the engine teaches from this
First place all prior units must be *combined* — so it's the earliest legitimate **interleaving**
point (comb vs seq decisions in one design, `research/02 §6`). Teach two-block first (block before
interleave), worked-example then independent design (a sequence detector / traffic light). Probe
Moore-vs-Mealy by having the learner *choose and justify* for a given spec.

## Confidence / gaps
Core `settled`; style choice `contested` by design. No open items.
