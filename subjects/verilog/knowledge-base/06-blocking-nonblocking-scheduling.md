# U6 — Blocking vs Nonblocking & the Event Queue (deep notes) ★★ keystone threshold T2

> Deep pass 2026-06-15. The single most consequential beginner topic (Cummings: "one of the most
> misunderstood constructs in the language"). Mechanism verified against the IEEE-1364-derived
> scheduling description (Accellera extract) + corroborating sources.

## A. The stratified event queue (the mechanism under everything)
A simulation **time step** processes events in ordered **regions** (IEEE 1364 §5 scheduling). The
load-bearing four for RTL: `[settled — Accellera/IEEE 1364 extract; chipverify corroborates]`
1. **Active** — blocking assignments, continuous assignments, gate/primitive evaluation, and the
   **evaluation of nonblocking RHS expressions**. Events here may run **in any order** (the source
   of nondeterminism/races). `[settled]`
2. **Inactive** — `#0`-delayed events (avoid these — Cummings #8).
3. **NBA (nonblocking-assign update)** — the **left-hand-side updates** of nonblocking assignments,
   applied *after* all active/inactive events. `[settled]`
4. **Monitor/postponed** — `$monitor`, `$strobe` read final settled values. `[settled]`
(Processing can loop back: NBA updates can schedule new active events within the same time step.)

## B. What each assignment actually does
- **Blocking `=`:** evaluates RHS and updates LHS **immediately**, in the **active** region, before
  the next statement in the block runs. Behaves "sequentially" within a block. `[settled]`
- **Nonblocking `<=`:** **RHS evaluated now (active region) using current values; LHS update
  deferred to the NBA region.** So *every* `<=` in a clocked block reads pre-edge values, and all
  update together at end of step. `[settled — Accellera extract; chipverify]`

## C. Why `<=` models flip-flops and `=` models combinational composition
- A real clock edge fires all flops at once from their *old* inputs → that is **exactly**
  RHS-from-old-values-then-simultaneous-update = nonblocking. Hence **Guideline #1: sequential →
  `<=`**. `[settled]`
- Combinational logic composes: intermediate result feeds the next gate **now** → blocking. Hence
  **Guideline #3: combinational always → `=`**. `[settled]`

## D. The race conditions (why the guidelines exist)
Because active-region events run in *any order*, two coding patterns create order-dependent,
simulator-dependent results — and sim/synth mismatch:
- Blocking in clocked logic (M3): one flop's new value feeds another within the same edge. `[settled]`
- Nonblocking in combinational logic (M4): stale reads. `[settled]`
- **The 8 Cummings guidelines (verbatim, SNUG 2000 — the canonical reference):** `[settled]`
  1. Sequential logic → nonblocking.
  2. Latches → nonblocking.
  3. Combinational logic in an always block → blocking.
  4. Both sequential & combinational in the same always block → nonblocking.
  5. Don't mix blocking and nonblocking in the same always block.
  6. Don't assign the same variable from more than one always block.
  7. Use `$strobe` to display nonblocking-assigned values.
  8. Don't use `#0` delays.
  > "Adherence … will remove 90–100% of the Verilog race conditions encountered by most designers."

## What the engine teaches from this
This is **★★ keystone** — budget the most time. Teach via prediction tables: give the shift-register
and a same-variable case, have the learner **predict the waveform** under `=` then `<=`, then run.
The event queue is the *mechanism* that explains the guideline — teach the why, not the rule alone
(or it won't transfer). Gate everything downstream on this.

## Confidence / gaps
`settled`. **Open item resolved:** exact event-region terminology/order now sourced (Accellera
extract of IEEE 1364-2001 §5 + corroboration), upgraded from `uncertain` → `settled`. Residual
nicety: full verbatim IEEE 1364-2005 §5 text not read (PDF/paywall) — terminology triangulated
across two independent descriptions, sufficient for teaching; logged as a minor standing check.
