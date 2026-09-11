# Verilog — Known Misconceptions (novice wrong models)

> Per protocol §4: a subject with no misconception list is under-researched. Each entry is a
> *claim* and is confidence-marked + sourced. These feed `learner-profile.md`, the engine's
> productive-failure setups, and the feedback moves. Format: **the wrong model → why it's wrong /
> the correct model → where it bites.**

---

## M1 — "Verilog runs top-to-bottom like a program." `[settled]`
Wrong model: the code executes sequentially, one line at a time, like Python/C.
Correct: it *describes hardware* that all exists and operates concurrently; `assign` statements,
gate instances, and `always` blocks all run in parallel, continuously. Order between blocks is
**not** defined by source order. Sequencing exists only *within* a single procedural block.
Bites: expecting a later `assign` to "overwrite" an earlier one; expecting block A to finish
before block B. *Source: IEEE 1364 scope; Cummings (parallel-block ordering undefined).*

## M2 — "`reg` means a register / flip-flop; `wire` is just a wire." `[settled]`
Wrong model: declaring `reg` creates storage / a flip-flop.
Correct: `reg` only means "a variable you may assign **inside a procedural block** (`always`/
`initial`)." It synthesizes to a flip-flop **only** if assigned on a clock edge; combinational
`reg` becomes plain logic/wires. The keyword name is misleading (SystemVerilog adds `logic`).
Bites: assuming any `reg` costs a flip-flop; confusion over when storage is actually inferred.
*Source: corroborated across secondary refs; standard SV motivation for `logic`.*

## M3 — "Use blocking (`=`) in clocked/sequential logic." `[settled]`
Wrong model: `=` is fine everywhere.
Correct: in `always @(posedge clk)`, blocking assignments create **race conditions** and
simulation/synthesis mismatches because one line's result feeds the next within the same edge.
Use **nonblocking (`<=`) for sequential logic** (Cummings Guideline #1).
Bites: shift registers/pipelines collapse; sim and synthesized hardware disagree.
*Source: Cummings SNUG 2000, Guideline #1; beginner-mistakes corroboration.*

## M4 — "Use nonblocking (`<=`) in combinational logic." `[settled]`
Wrong model: `<=` is the "safe default" everywhere.
Correct: in combinational `always @*`, nonblocking can read a stale value (updates deferred to
end of time step), causing sim/synth mismatch. Use **blocking (`=`) for combinational logic in an
always block** (Cummings Guideline #3).
Bites: combinational output lags by a delta-cycle in sim; mismatches.
*Source: Cummings SNUG 2000, Guideline #3.*

## M5 — "Mixing `=` and `<=` to the same variable, or driving one variable from two always
blocks, is fine." `[settled]`
Correct: mixing assignment types to one variable (Guideline #5) or assigning one variable from
multiple always blocks (Guideline #6) creates races / multiple-driver conflicts with undefined
results. *Source: Cummings SNUG 2000, Guidelines #5, #6.*

## M6 — "An incomplete `if`/`case` (no `else`/`default`) in combinational logic is harmless."
`[settled]`
Wrong model: leaving an output unassigned in some branch just defaults to something sensible.
Correct: synthesis **infers a latch** to hold the old value, silently turning intended
combinational logic into (buggy) sequential logic. Assign every output in every branch (or use a
default assignment / `always_comb` intent in SV).
Bites: unintended latches — a classic sim-passes / hardware-broken bug.
*Source: latch-inference sources; SystemVerilog `always_comb`/`always_latch` motivation.*

## M7 — "Incomplete sensitivity list is just a style nit." `[settled]`
Wrong model: listing only some signals in `always @(a, b)` is fine.
Correct: simulation only re-evaluates on listed signals, but synthesis builds hardware reacting to
**all** read signals → sim/synth mismatch. Use `always @*` (or SV `always_comb`).
*Source: latch/sensitivity-list sources; sim-vs-synth literature.*

## M8 — "A module is like a function I call and that returns a value." `[settled]`
Wrong model: instantiating a module = calling a subroutine that runs and returns.
Correct: instantiation **places a copy of that hardware** into the design, permanently wired in
and running concurrently. There is no "call" or "return"; ports are physical connections.
Bites: expecting sequential call semantics; misusing outputs.
*Source: structural-modeling / module-instantiation refs; follows from M1.*

## M9 — "`x` and `z` are just like 0 and 1." `[settled — resolved at deep pass 2026-06-15]`
Correct: Verilog values are **4-state** (0, 1, x=unknown, z=high-impedance). In *simulation* `x`
means unknown (comparisons to `x` yield false/unknown); in *synthesis* an `x` **assignment** is
typically treated as a **don't-care** the tool may resolve either way — a documented sim/synth
mismatch ("X-optimism"). `z` models tri-state/undriven nets. Related trap: **`casex`** treats both
`x` and `z` as don't-care and can **mask bugs** — prefer full `case` or `casez` with `?`.
Bites: a bug visible as `x` in sim disappears (or appears) in hardware; `casex` hiding an
uninitialized signal. *Source: sim/synth-mismatch literature; verilogpro "X-optimism"; casex/casez
refs. See `02-modules-and-datatypes.md` §C, `10-rtl-synthesis-subset.md` §C.*

---

### Maintenance
New misconceptions surface **from teaching** (protocol §10: teaching is the base's stress test).
When the learner reveals a wrong model not listed here, add it with date + source/confidence and
note it in `CHANGELOG.md`.
