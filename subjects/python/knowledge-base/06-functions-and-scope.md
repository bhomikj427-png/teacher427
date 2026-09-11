# U6 — Functions, arguments & scope (deep notes) ★ Threshold T5

> Deep pass 2026-06-16. Primary sources: Language Reference §4 (scope) + Programming FAQ (verified
> 2026-06-16). Functions are easy; **scope and argument-passing are the threshold** (T5).

## A. Defining & calling
- `def name(params): ...`; `return` (a bare/absent return yields `None`). Functions are **objects**
  (first-class): assignable, passable, returnable — seed for U10/U12. `[settled — Language Reference
  §3 "even functions are objects"]`

## B. Parameters & arguments (the full model)
- **Positional** vs **keyword** args; **defaults** (`x=1`); **`*args`** (extra positionals → tuple);
  **`**kwargs`** (extra keywords → dict); **keyword-only** params (after a bare `*`) and
  **positional-only** params (before `/`, PEP 570, 3.8+). `[settled — standard/uncontested; `/`,`*`
  are stable syntax in 3.14]`
- **Arguments are passed by assignment** ("call by object sharing"): the parameter name is **bound
  to the same object** the caller passed. No call-by-reference. Rebinding the param doesn't affect
  the caller; **mutating a shared mutable does** (M5). `[settled — FAQ, verified 2026-06-16]`

## C. The mutable-default trap (misconception M4) `[settled]`
- Defaults are evaluated **once, at function-definition time**, and the *same* default object is
  reused every call. A mutable default (`[]`/`{}`) **accumulates state across calls**. Fix: default
  to `None`, create inside (`if x is None: x = []`). `[settled — FAQ verbatim, verified 2026-06-16]`

## D. Scope: LEGB & the local-by-assignment rule (T5) `[settled]`
- Name resolution: **Local → Enclosing → Global → Builtin.** `[settled — Language Reference §4,
  verified 2026-06-16]`
- **The rule that bites:** *"If a name binding operation occurs anywhere within a code block, all
  uses of the name within the block are treated as references to the current block."* So assigning a
  name *anywhere* in a function makes it **local for the whole function** — reading it before that
  assignment raises **`UnboundLocalError`** (M13). `[settled — §4 verbatim, verified 2026-06-16]`
- **`global`** → bind/refer to the module-level name; **`nonlocal`** → bind/refer to the nearest
  enclosing *function* scope (SyntaxError if none). Both must precede use. `[settled — §4, verified
  2026-06-16]`

## E. Closures & late binding (misconception M12) `[settled]`
- A nested function that refers to an enclosing variable is a **closure**; it captures the
  **variable (binding), not the value** — looked up **when called**, not when defined. Loop-created
  closures all see the *final* value; fix with a per-iteration default arg (`lambda n=x: ...`).
  `[settled — FAQ late-binding-closures, verified 2026-06-16]`

## What the engine teaches from this
Args/defaults: worked-example-first (it's procedure). Scope/closures: productive-failure-first (it's
a concept threshold) — have them predict the `UnboundLocalError` and the loop-closure result, then
reconcile. Gate U7 on a correct prediction of both. Decorators (which *are* closures) wait for U12.

## Confidence / gaps
Argument-passing, defaults, LEGB, local-by-assignment, global/nonlocal, closures all `settled` at
primary source (Language Reference §4 + FAQ, verified 2026-06-16). Positional-only/keyword-only
syntax is standard/uncontested. No open items.
