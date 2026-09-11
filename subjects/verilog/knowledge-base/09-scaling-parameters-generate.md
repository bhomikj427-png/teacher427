# U9 — Scaling: Parameters, Generate, Reuse (deep notes)

> Deep pass 2026-06-15. How one design becomes a family of designs — the reuse machinery.

## A. Parameters
- **`parameter`:** a compile-time constant **configurable at instantiation** (e.g. bus `WIDTH`).
  Lets one `adder #(.WIDTH(8))` become 4/8/16-bit. `[settled]`
- **`localparam`:** a constant **fixed inside** the module (not overridable) — for derived/internal
  constants (e.g. state encodings, `DEPTH = 1<<ADDR_W`). `[settled]`
- Override by name at instantiation: `module #(.WIDTH(16)) u_inst (...)`. `[settled]`

## B. Generate blocks
- **`generate` + `genvar` for-loops** *replicate* hardware at **elaboration** (compile) time —
  e.g. instantiate N full adders to build an N-bit ripple adder programmatically. The loop is
  **unrolled into hardware**, not executed at runtime. `[settled — generate/genvar refs]`
- **`if`/`case` generate:** conditionally include hardware based on parameters (e.g. include a
  pipeline stage only if `PIPELINED`). `[settled]`
- `genvar` is elaboration-only; each unrolled instance gets an implicit index localparam. `[settled]`
- Contrast with a procedural `for` loop: a `for` inside `always` describes repeated *logic within
  one block*; `generate for` replicates *structure/instances*. Both synthesizable when bounds are
  static. `[settled — loops/synthesis refs]`

## C. Why this matters
This is the bridge from "I wrote a 4-bit adder" to "I wrote an N-bit adder generator" — the
parameterized, reusable style professional RTL is built in. Directly extends the learner's adder.
`[settled]`

## What the engine teaches from this
Worked-example-first (it's procedural machinery), anchored to **their** adder: "make your 4-bit
adder an N-bit adder." Retrieval check: "what runs at elaboration vs at clock time?" (separates
generate from runtime logic — reinforces T1).

## Confidence / gaps
All `settled`. No open items.
