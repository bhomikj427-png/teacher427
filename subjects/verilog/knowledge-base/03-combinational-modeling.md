# U3 — Combinational Modeling: Structural & Dataflow (deep notes)

> Deep pass 2026-06-15. The learner's current home turf (adders). Two of the three abstraction
> levels for combinational hardware; behavioral (`always`) is U4.

## A. Structural / gate-level modeling
- Instantiate built-in **primitives** (`and`, `or`, `not`, `xor`, `nand`, `nor`, `buf`) and/or
  sub-modules, and **wire them together** explicitly. Lowest abstraction; you draw the schematic
  in text. `[settled — standard taxonomy]`
- This is how a **full adder** is naturally built from gates, and a **4-bit ripple-carry adder**
  from four full adders (carry chained out→in). The learner's stated next step. `[settled]`
- Mechanism to stress: all instances are **concurrent** — wiring, not sequence. The structure
  *is* the circuit.

## B. Dataflow modeling — continuous assignment
- **`assign`** drives a `wire` with a continuous expression: `assign sum = a ^ b ^ cin;`. `[settled]`
- **"Continuous" = always live:** the left side re-evaluates **whenever any right-side signal
  changes**, forever. There is no "execution" — it's a permanent connection (a gate network).
  This is the cleanest concrete instance of T1/concurrency. `[settled — dataflow refs]`
- Multiple `assign`s in a file all run in parallel; **source order is irrelevant**. Two `assign`s
  driving the *same* wire = a multiple-driver conflict (→ `x`/contention), not "last wins."
  `[settled]`
- Operators (U2) make dataflow expressive: `assign {cout,sum} = a + b + cin;` is the whole full
  adder in one line — and teaches the bit-width lesson (the `{cout,sum}` 5-bit/2-bit target
  catches the carry).

## C. Same hardware, two descriptions
A full adder written structurally (gates) and in dataflow (`assign`) synthesize to the **same
logic**. Showing both is the engine's concreteness-fading bridge: from explicit gates → to the
abstract expression. `[settled]`

## What the engine teaches from this
This is the **routing point**: building a procedure (the 4-bit adder wiring) → *worked-example-
first*; building the *concept* (why order doesn't matter, why `assign` is always-live) →
*productive-failure-first* (ask them to predict before telling). Use **their** adder as the spine;
extend to dataflow `+`, then parameterize (forward link to U9). Bit-width truncation gets taught
live here on the carry-out.

## Confidence / gaps
All `settled`. No open items.
