# U5 — Collections & mutability (deep notes) ★ Threshold T2

> Deep pass 2026-06-16. Primary sources: Language Reference §3 (mutability) + Library Reference
> stdtypes + FAQ (verified 2026-06-16). The unit where T1 (binding) cashes out into the most common
> beginner bugs. Threshold T2.

## A. The four core collections
- **`list`** — ordered, **mutable**, heterogeneous, variable length. `[]`, indexing, slicing,
  `.append/.extend/.pop/.sort`. `[settled]`
- **`tuple`** — ordered, **immutable**; idiomatically a fixed-structure **record** (position has
  meaning), not "a frozen list" (M11). Unpacking: `x, y = point`. `[settled — §3; glossary]`
- **`dict`** — **mutable** mapping key→value; keys must be **hashable** (immutable value with stable
  `__hash__`/`__eq__`); **insertion-ordered** (a language guarantee since 3.7). `[settled — glossary
  hashable; ordering is standard 3.7+ guarantee]`
- **`set`** — **mutable** unordered collection of **hashable**, unique elements; `frozenset` is the
  immutable version. `[settled]`

## B. Mutability is the fault line (Big Idea #3) `[settled]`
- *"numbers, strings and tuples are immutable, while dictionaries and lists are mutable."* Mutable =
  value can change in place; immutable = a new object must be created for a new value. `[settled —
  Language Reference §3, verified 2026-06-16]`
- The immutability **nuance**: an immutable container (tuple) holding a mutable object (list) can
  *appear* to change because its contents changed — it's still immutable (its *references* can't be
  reassigned). Hence a tuple containing a list is **not hashable**. `[settled — §3 verbatim nuance,
  verified 2026-06-16]`

## C. Aliasing, copying, and the bugs (T1 → T2)
- Because names bind (U3), `b = a` aliases a mutable; mutate one, see it in both. `[settled — FAQ]`
- **Copy levels:** a **shallow copy** "constructs a new compound object and then… inserts
  *references* into it to the objects found in the original" (`a[:]` / `list(a)` / `.copy()`); a
  **deep copy** "recursively inserts *copies*" (`copy.deepcopy(a)`). So shallow-copy-then-mutate-
  nested changes both — the classic surprise. `[settled — `copy` module docs, verified 2026-06-16]`
- **Mutating while iterating** corrupts the iterator (M15) — iterate a copy or build new. `[settled]`

## D. The mutable-default-argument trap (preview of U6, root is here) `[settled]`
- `def f(acc=[])` shares one list across all calls because defaults are made **once at def time**.
  Fix: `=None` + create inside. Belongs to U6 mechanically but is *understood* from T2. `[settled —
  FAQ, verified 2026-06-16]`

## What the engine teaches from this
Productive failure on aliasing/shallow-copy (predict → run → reconcile). Gate progress on the
learner correctly predicting a shallow-copy nested-mutation case. Teach tuple-as-record vs
list-as-sequence as *intent*, not just immutability. Keep tying every surprise back to T1 (one fact,
many faces).

## Confidence / gaps
All `settled` at primary source (mutability §3, `copy` module, glossary verified 2026-06-16; dict
insertion-order is the standard 3.7+ guarantee). No open items.
