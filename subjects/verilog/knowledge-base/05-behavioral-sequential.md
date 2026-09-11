# U5 — Behavioral Sequential Logic (deep notes) ★ threshold T4

> Deep pass 2026-06-15. Clocked storage: flip-flops, reset, counters. The "reg actually becomes a
> register here" unit. Pairs tightly with U6 (must use `<=`).

## A. The clocked `always` block
- `always @(posedge clk)`: the block's assignments happen **on the rising clock edge** → this is
  what **infers flip-flops** (state). A `reg` assigned here becomes a real register (resolving M2:
  *this* is when `reg` earns its name). `[settled — Harris & Harris Ch.3]`
- Mechanism: edge-triggered = sample inputs at the edge, hold until the next edge. State persists
  between edges. This is the literal hardware D flip-flop.

## B. Rule: use **nonblocking `<=`** in sequential blocks (Cummings Guideline #1)
- Why (full mechanism in U6): a clock edge fires *all* flip-flops "simultaneously"; nonblocking
  evaluates every right-hand side from the **pre-edge** values, then updates all left-hand sides
  together — exactly a bank of flip-flops. Blocking `=` here makes one assignment feed the next
  *within the same edge*, corrupting shift registers/pipelines and causing sim/synth mismatch
  (misconception M3). `[settled — Cummings SNUG 2000 #1]`
- Canonical contrast (the teaching crux): a 3-stage shift register
  `q1<=d; q2<=q1; q3<=q2;` (with `<=`) shifts one stage per clock; with `=` all three collapse to
  `d` in one clock. Same code, opposite hardware. `[settled]`

## C. Reset (contested-by-design — teach the tradeoff, not a law)
- **Synchronous reset:** reset sampled with the clock (`if(rst) ... else ...` inside
  `@(posedge clk)`). Pros: clean timing, no async deassertion hazard, friendly to gated clocks.
  Cons: needs a running clock; can be optimized into the data path. `[settled — Cummings SNUG 2002]`
- **Asynchronous reset:** `always @(posedge clk or posedge rst)`. Pros: immediate, works without a
  clock (power-up). Cons: **deassertion** can violate recovery/removal timing across many flops →
  needs a *reset synchronizer*; tool/library variability. `[settled — Cummings SNUG 2002]`
- **Practitioner guidance (not absolute):** common modern advice is *async assert, sync deassert*
  (reset synchronizer), or sync reset where the flow allows. Cummings SNUG 2002 is the canonical
  discussion. Teach as **engineering judgment**, mark `contested`. `[contested — by design]`

## D. Common sequential building blocks
Registers, counters (up/down/loadable), shift registers, edge detectors, simple pipelines — all
"flop + combinational next-value." This is the RTL pattern (forward link to U10). `[settled]`

## What the engine teaches from this
Worked-example-first for the flop idiom (it's a procedure), then **productive failure on `=` vs
`<=`** with the shift register (predict, then run). T4 ("reg is now a register, but only because of
the clock edge") is checked by retrieval: "what made this a flip-flop?" Answer must cite the edge,
not the keyword. Reset taught as a tradeoff with the learner choosing and justifying.

## Confidence / gaps
Core `settled`; reset strategy intentionally `contested`. No open items.
