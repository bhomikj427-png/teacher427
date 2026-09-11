# U4 — Control flow & truthiness (deep notes)

> Deep pass 2026-06-16. Primary source: Library Reference "Truth Value Testing" (verified
> 2026-06-16). Control-flow syntax is light; the *deep* content is truthiness and short-circuiting.

## A. Branching & loops (mechanism, not just syntax)
- `if / elif / else`; blocks delimited by **indentation** (M7). `while` loops on a condition; `for`
  iterates an **iterable** (the iteration protocol — full mechanism in U7, here used concretely).
  `break` / `continue`; the often-missed **`for/else`** and **`while/else`**: the `else` runs iff
  the loop finished **without** `break`. `[settled — for/else semantics standard/uncontested]`
- `for` does **not** count an index — it pulls items from an iterator (seed U7). Teaching `for i in
  range(n)` as "counting" plants a wrong model; teach it as "iterate the items of range." `[settled —
  glossary iterator]`

## B. Truthiness — the deep content (misconception M8) `[settled]`
- *Any* object has a truth value. **Falsy:** `None`, `False`, numeric zero (`0`, `0.0`, `0j`,
  `Decimal(0)`, `Fraction(0,1)`), and **empty** containers (`''`, `()`, `[]`, `{}`, `set()`,
  `range(0)`). Everything else is **truthy**. `[settled — Library Reference, verified 2026-06-16]`
- Mechanism: an object is true unless its class defines `__bool__()` returning False, **or**
  `__len__()` returning 0. So `if mylist:` means **"non-empty"**, not "exists." `[settled — verified
  2026-06-16]`

## C. Boolean operators return *operands*, not bools (a real surprise) `[settled]`
- `and`/`or` **short-circuit and return one of their operands**, not necessarily `True`/`False`:
  `0 or "x"` → `"x"`; `"a" and "b"` → `"b"`; `None or []` → `[]`. This powers idioms like
  `name = user_input or "default"`. `not` always returns a bool. `[settled — Library Reference,
  verified 2026-06-16]`
- Comparison chaining: `0 < x < 10` is real and means `0 < x and x < 10`. `[settled — comparison
  chaining standard/uncontested]`

## D. Structural pattern matching — `match`/`case` (modern, 3.10+) `[settled]`
- `match subject: case pattern: ...` compares the subject against patterns and runs the first match.
  Crucially it is **not** a C/Java `switch` on values — it **inspects structure**: matches sequences,
  mappings, and class instances, and **destructures** them (binds names from the shape), e.g.
  `case Point(x=0, y=y):`. `[settled — PEP 634; What's New 3.10, verified 2026-06-16]`
- Version-gated: `match`/`case` is **new in 3.10**; on ≤3.9 it's a `SyntaxError`. Our target (3.14)
  has it. Teach it as the idiomatic multi-way branch on *shape*, after if/elif is solid. `[settled —
  verified 2026-06-16]`

## E. Common bite
- Writing `if x == True:` instead of `if x:` (and `if x == None` instead of `is None`). Tie back to
  M2/M8. `[settled]`

## What the engine teaches from this
Drive truthiness with prediction: give a list of values, have them sort truthy/falsy *before*
running. The `and`/`or`-returns-operands fact is high-yield — use it, don't just state it. Hold
the `for`-as-iteration framing so U7 lands cleanly.

## Confidence / gaps
Truthiness + boolean-operator semantics `settled` at primary source (verified 2026-06-16).
`match`/`case` `settled` (PEP 634, 3.10). `for/else` and chained comparison are standard/uncontested.
No open items.
