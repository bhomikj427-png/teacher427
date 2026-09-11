# U7 — Iteration protocol, comprehensions & generators (deep notes) ★ Threshold T4

> Deep pass 2026-06-16. Primary source: official glossary (iterable/iterator/generator) verified
> 2026-06-16. The unit that unifies `for`, comprehensions, unpacking, files, and many builtins under
> one protocol — and introduces laziness. Threshold T4.

## A. The protocol (the mechanism behind `for`) `[settled]`
- **iterable** — an object that can return its members one at a time; has `__iter__()` (or
  sequence `__getitem__`). **iterator** — represents a *stream*; `__next__()` returns successive
  items, raising **`StopIteration`** when exhausted. `iter(obj)` gets an iterator; `next(it)` pulls
  one. `[settled — glossary, verified 2026-06-16]`
- **`for x in obj:`** desugars to: get an iterator via `iter(obj)`, repeatedly `next()` it, bind
  each to `x`, stop on `StopIteration`. *This* is why `for` works on lists, strings, dicts, files,
  ranges, generators — anything iterable. `[settled — glossary; `for`-desugaring
  standard/uncontested]`
- **Iterators are one-shot:** exhausted after one pass; a fresh `iter()` is needed to reiterate.
  An iterator's `__iter__` returns itself. `[settled — glossary; standard]`

## B. Comprehensions (idiomatic construction)
- `[f(x) for x in it if cond]` (list), `{...}` (set/dict), and **generator expressions**
  `(f(x) for x in it)`. They are the Pythonic replacement for build-a-list-with-a-loop. Comprehension
  variables are **scoped to the comprehension** (don't leak). `[settled — comprehension scoping
  standard/uncontested (Py3)]`

## C. Generators & laziness (Big Idea #5) `[settled]`
- A **generator function** contains `yield`; calling it returns a **generator iterator**. Each
  `yield` **suspends execution, remembering local state** (variables, pending `try`), and **resumes**
  where it left off on the next `next()` — unlike a normal function that starts fresh. `[settled —
  glossary "generator iterator", verified 2026-06-16]`
- Consequence: **lazy, on-demand** production — stream data too large for memory, build infinite
  sequences, pipeline transforms. Generator expressions give the same laziness inline. `[settled —
  glossary]`

## D. The iteration toolkit
- `enumerate` (index+item), `zip` (parallel iterate), `range` (lazy arithmetic sequence),
  `map`/`filter` (lazy), `sorted`/`reversed`, `sum`/`min`/`max`/`any`/`all`. Many are **lazy
  iterators** themselves (consume once). `itertools` for advanced composition. `[settled — Library
  Reference; per-builtin laziness standard/uncontested]`
- Bite: mutating a collection while iterating (M15); consuming a one-shot iterator twice.

## What the engine teaches from this
Teach the protocol by **building an iterator by hand** (implement `__iter__`/`__next__`), then show
`for` doing the same — concept-first/productive failure, since the payoff is the unifying model.
Then comprehensions (procedure: worked-example-first). Generators: contrast a list-returning vs a
yielding version on a large input to make laziness concrete. Gate on predicting iterator exhaustion.

## Confidence / gaps
Protocol + generator semantics `settled` at glossary primary source (verified 2026-06-16). `for`
desugaring, comprehension scoping, and per-builtin laziness are standard/uncontested (consistent
with the glossary protocol definitions). No open items.
