# U12 — Idiomatic Python & power tools (deep notes)

> Deep pass 2026-06-16. Primary sources: PEP 20 (Zen, full text) + PEP 8 + PEP 257 (all verified
> 2026-06-16). "Pythonic" becomes explicit and operational here. Decorators and
> context managers are the two power tools that depend on earlier thresholds (closures U6, the data
> model U10).

## A. The Zen of Python (PEP 20) `[settled]`
- 19 written aphorisms (Tim Peters, 2004), incl.: *Beautiful > ugly; Explicit > implicit; Simple >
  complex; Readability counts; Errors should never pass silently (unless explicitly silenced); In
  the face of ambiguity, refuse the temptation to guess; There should be one—and preferably only
  one—obvious way to do it; Namespaces are one honking great idea.* `[settled — PEP 20 full text,
  verified 2026-06-16]`
- These are *design values*, used to adjudicate style choices — teach them as the "why" behind the
  idioms, not as scripture to recite. `[settled]`

## B. PEP 8 (style) `[settled]`
- 4-space indentation (never tabs); lines ≤ **79** chars (docstrings/comments ≤ 72); naming:
  **`snake_case`** functions/variables, **`CapWords`** classes, **`UPPER_CASE`** constants,
  `_internal` convention; two blank lines between top-level defs; `is None` not `== None`. `[settled
  — PEP 8, verified 2026-06-16]`
- Philosophy: **"code is read much more often than it is written"**; consistency hierarchy (guide <
  project < module); "a foolish consistency is the hobgoblin of little minds" — break a rule when it
  *improves* readability. `[settled — PEP 8 verbatim, verified 2026-06-16]`
- **Docstrings (PEP 257):** a docstring is "a string literal that occurs as the first statement in a
  module, function, class, or method definition" → becomes `__doc__`; "always use triple double
  quotes"; one-line = summary on one line, multi-line = summary, blank line, details; write as an
  imperative ("Return X"). `[settled — PEP 257, verified 2026-06-16]`

## C. Pythonic idioms (the accumulation of earlier units)
- Truthiness checks (`if seq:`), `and`/`or` defaults, comprehensions over manual loops, EAFP over
  LBYL, unpacking/`enumerate`/`zip`, `with` for resources, f-strings for formatting, `is None`.
  Each traces to an earlier unit's mechanism. `[settled — cross-refs U4–U8]`

## D. Decorators `[settled — substance]`
- A **decorator** is a callable that takes a function and returns a (usually wrapping) function;
  `@dec` above `def f` means `f = dec(f)`. It **is a closure** (U6) over the wrapped function.
  **`functools.wraps`** copies the wrapped function's metadata onto the wrapper — "without [it]… the
  name… would have been `'wrapper'`, and the docstring… would have been lost." Powers caching
  (**`functools.lru_cache`** "memoizing callable that saves up to maxsize recent calls" / `cache`
  unbounded), `partial`, `reduce`, logging, timing, registration. `[settled — functools docs,
  verified 2026-06-16]`

## E. Context managers (`with`) `[settled — substance]`
- `with open(...) as f:` guarantees setup/teardown via the **`__enter__`/`__exit__`** protocol (data
  model, U10) — cleanup runs even on exception. Write your own via the protocol or
  **`@contextlib.contextmanager`** on a generator that **yields exactly once**: code **before
  `yield`** = `__enter__` (yielded value → the `as` target), code **after `yield`** = `__exit__`; an
  exception in the block is re-raised at the `yield`, so a `try/finally` around it ensures cleanup.
  `[settled — contextlib docs, verified 2026-06-16]`

## What the engine teaches from this
Idioms are taught by **refactoring the learner's own earlier code** to Pythonic form and naming the
Zen value each change serves (concrete → principle). Decorators: build one from a plain closure
(U6) step by step, then introduce `@`. Context managers: motivate with a leaked file handle, then
`with`. These are power tools — only after their prerequisites (U6 closures, U10 data model) are
solid.

## Confidence / gaps
All `settled` at primary source: Zen (PEP 20), PEP 8, PEP 257, `functools` (wraps/lru_cache/cache/
partial/reduce), `contextlib.contextmanager` — verified 2026-06-16. No open items.
