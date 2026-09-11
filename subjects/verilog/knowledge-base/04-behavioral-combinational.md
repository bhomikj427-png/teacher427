# U4 — Behavioral Combinational Logic (deep notes) ★ threshold T3 (latches)

> Deep pass 2026-06-15. The `always` block used for *combinational* logic — and the first place
> sim/synth mismatch bites a beginner.

## A. The combinational `always` block
- `always @(*)` (or `always @*`): a procedural block that re-evaluates whenever **any signal it
  reads** changes. Targets must be declared `reg` (assigned in a procedural block) even though the
  result is combinational (misconception M2 link). `[settled]`
- Inside: `if/else`, `case`, blocking assignments — lets you express muxes, decoders, ALUs more
  readably than raw `assign`. `[settled]`

## B. Rule: use **blocking `=`** in combinational always blocks (Cummings Guideline #3)
- Mechanism: blocking assignments take effect immediately in order within the block, so a computed
  intermediate feeds the next line correctly — matching how combinational logic composes. Using
  nonblocking `<=` here defers updates (U6), so a line reads a **stale** value → sim/synth mismatch
  (misconception M4). `[settled — Cummings SNUG 2000 #3]`

## C. Threshold T3a — unintended latch inference (the classic trap)
- **Mechanism:** in a combinational `always`, if **some path leaves an output unassigned** (an
  `if` with no `else`; a `case` with no `default`; an output not set in every branch), synthesis
  must *hold the previous value* → it **infers a latch**, silently turning your combinational logic
  into (buggy) sequential logic. `[settled — latch-inference literature]`
- **The two prevention rules:**
  1. **Assign every output in every branch** — or set **default values at the top** of the block
     before the `if`/`case`. `[settled]`
  2. **Complete sensitivity list** — use `always @*`, never a hand-listed partial list, or sim
     reacts to fewer signals than the synthesized hardware → mismatch (misconception M7). `[settled]`
- SystemVerilog's **`always_comb`** enforces both (auto sensitivity list + tool error if a latch
  would be inferred) — a strong reason a *professional* path leans SV (see U12). `[settled]`

## D. `case` hygiene
- Prefer full `case` with `default`; avoid `casex` (masks `x` bugs — U2.C); be wary of
  `parallel_case`/`full_case` synthesis pragmas (a documented sim/synth-mismatch source). `[settled
  — Cummings RTL-mismatch paper]`

## What the engine teaches from this
Latch inference is a **productive-failure** goldmine: have the learner write a mux with a missing
branch, *predict* the hardware, then confront the inferred latch. The lesson sticks because they
generated the bug. Gate U5 on "writes combinational always blocks with zero unintended latches and
can spot one."

## Confidence / gaps
All `settled`. No open items.
