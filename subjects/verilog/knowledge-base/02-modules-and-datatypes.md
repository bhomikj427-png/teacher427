# U2 — Modules, Data Types, Values & Operators (deep notes)

> Deep pass 2026-06-15. The structural vocabulary + the value system + operator gotchas.

## A. Modules — the unit of hardware
- A `module` is a named block of hardware with a **port list** (inputs/outputs/inouts). It is the
  reuse and hierarchy unit. `[settled]`
- **Instantiation places a *copy* of that hardware into the design** and wires its ports in. It is
  **not a function call** (misconception M8): no "call", no "return", no execution-then-resume. An
  instance is permanent, concurrent, physically present. `[settled]`
- **Port connection:** by order (positional) or **by name** (`.clk(clk)`). By-name is the
  professional default — order-independent, error-resistant. `[settled]`
- Hierarchy: modules instantiate modules → a tree. The leaf is gates/primitives.

## B. Nets vs variables — `wire` vs `reg` (threshold T4, misconception M2)
- **`wire` (a net):** a physical connection driven *continuously* by something else (a gate, a
  `assign`, a module output). Cannot hold state; reflects its driver. `[settled]`
- **`reg` (a variable):** something you assign **inside a procedural block** (`always`/`initial`).
  The name is **misleading** — `reg` does **not** mean "register/flip-flop." It synthesizes to a
  flip-flop **only** if assigned on a clock edge; a combinational `reg` becomes plain wires/logic.
  `[settled — corroborated; the exact reason SystemVerilog introduces `logic` to replace both]`
- **The real rule:** the choice is about **assignment context**, not hardware: driven by
  continuous assignment/gate → `wire`; assigned inside a procedural block → `reg`. Hardware
  inferred is decided by *how* it's assigned (clocked vs not), not by the keyword. `[settled]`

## C. The 4-state value system (misconception M9 — now resolved)
- Verilog values are **4-state: `0`, `1`, `x`, `z`.** `[settled]`
  - `x` = **unknown/indeterminate** (in simulation). Not a hardware value — a sim concept for
    "could be 0 or 1, we don't know" (e.g. uninitialized reg, contention).
  - `z` = **high-impedance** — undriven / tri-stated net. Models real tri-state buses. `[settled]`
- **Sim vs synthesis divergence (a real mismatch source):** in simulation `x` propagates as
  unknown and comparisons to `x` yield false/unknown; in **synthesis** an `x` *assignment* is
  typically treated as a **don't-care** the tool may optimize either way. So sim can show `x`
  (catching a bug) while hardware silently picks a value — or vice versa. `[settled — sim/synth-
  mismatch literature; verilogpro "X-optimism"]`
- **`casex`/`casez` caution:** `casez` treats `z`/`?` as don't-care; `casex` treats **both `x` and
  `z`** as don't-care — which can **mask bugs** (an accidental `x` matches anything). Guidance:
  avoid `casex` in synthesizable code; prefer `casez` with `?`, or full `case`. `[settled —
  multiple refs; aligns w/ Cummings-style guidance]`

## D. Vectors, numbers, operators — and the gotchas
- **Vectors/buses:** `[MSB:LSB]` ranges, e.g. `wire [7:0] data`. Part-selects, concatenation
  `{a,b}`, replication `{4{a}}`. `[settled]`
- **Sized literals:** `4'b1010`, `8'hFF`, `8'd255`. Unsized integer literal defaults to ≥32 bits
  and **signed**. `[settled]`
- **Bit-width rules (a top bug source):** an expression's width is context-dependent; `a+b` of two
  8-bit values is 8 bits unless the *destination/context* is wider — a carry-out can be **silently
  truncated** if you assign to an 8-bit target. Size the destination (e.g. 9 bits) deliberately.
  `[settled — bit-width/truncation refs]`
- **Signed/unsigned (a subtle bug source):** `reg`/net are **unsigned by default**; `integer` is
  signed. **If *any* operand in an expression is unsigned, the whole expression is evaluated
  unsigned** — negative values silently "vanish." Use the `signed` keyword deliberately and watch
  mixed expressions. `[settled — Tumbush DVCon'05; corroborated]`
- **`%` follows the sign of the first operand** (`-7 % 3 == -1`). `[settled]`

## What the engine teaches from this
wire-vs-reg as *assignment context* (kill M2 early via retrieval, not by restating the keyword);
4-state values as a sim-vs-hardware idea (sets up T3); bit-width/truncation taught **on the
learner's own adder** (their carry-out is the live example). Signed arithmetic deferred until needed.

## Confidence / gaps
All `settled`. M9 resolved (4-state + x/z synthesis treatment verified). No open items.
