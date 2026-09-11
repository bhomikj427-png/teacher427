# U10 — RTL Discipline, the Synthesizable Subset & Sim/Synth Mismatch (deep notes) ★ T3/T5

> Deep pass 2026-06-15. The professional core: writing Verilog that becomes the hardware you
> intend. Pulls together the mismatch threads from U2/U4/U5/U6.

## A. The RTL mindset (threshold T5)
- **Register-Transfer Level:** describe the design as **data moving register → combinational logic
  → register, each clock cycle.** Every synthesizable design ≈ flip-flops with combinational
  "clouds" between them. Think in *cycles and registers*, not statements. `[settled — Doulos RTL;
  Harris & Harris]`
- This reframe (T5) is what turns syntax knowledge into design ability — the goal state for a
  professional.

## B. The synthesizable subset (what becomes hardware)
- **Synthesizable:** `assign`, `always @*`/`always @(posedge clk)`, `if`/`case`, `for`/`generate`
  with **static bounds**, parameters, module instantiation, operators. `[settled — synthesizable-
  constructs refs]`
- **NOT synthesizable (sim-only — tools ignore or reject):** `initial` blocks, `#delay`,
  `while`/`forever` (and unbounded loops), `fork/join`, `force`/`release`, most `$system` tasks,
  `real`/`time` types. These live in **testbenches**. `[settled — synthesizable-constructs refs +
  chipverify initial-block]`
- Mechanism: synthesis maps RTL → a gate/flop netlist for a target library/FPGA; anything with no
  hardware meaning (delays, print tasks, initial-time stimulus) is ignored or errors. `[settled]`

## C. Sim/synth mismatch — the catalog (why this is a discipline)
The same source behaving differently in simulation vs synthesized hardware. Documented causes,
each cross-referenced: `[settled — Cummings RTL-mismatch paper; corroborating refs]`
1. **Incomplete sensitivity list** → sim under-reacts; hardware reacts to all inputs (U4, M7).
2. **Unintended latches** from incomplete `if`/`case` (U4, M6, T3).
3. **Blocking/nonblocking misuse** → races, ordering differences (U6, M3–M5).
4. **`x` assignments** → unknown in sim, **don't-care** in synthesis (U2.C, M9).
5. **`full_case`/`parallel_case` pragmas** → tell synthesis something sim doesn't honor.
6. **`casex`** masking `x` (U2.C).
- **Defensive discipline:** code combinational with `always @*` + full assignment; sequential with
  `<=`; avoid pragmas, `casex`, and `x` injection; lint + check pre/post-synthesis simulation.
  SystemVerilog `always_comb/_ff/_latch` make intent tool-checkable (U12). `[settled]`

## What the engine teaches from this
This is mostly a **consolidation/transfer** unit — by here the learner has met each mismatch
locally; U10 organizes them into a single discipline and the RTL mindset. Heavy **interleaving**
(given a snippet, "will this synthesize as intended? why/why not?"). T5 checked by having them
*describe a spec in register/cloud terms* before coding.

## Confidence / gaps
All `settled`. No open items.
