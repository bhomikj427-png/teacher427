# U3 — Names bind to objects; identity vs equality (deep notes) ★ Threshold T1

> Deep pass 2026-06-16. **The master threshold.** Primary sources: Language Reference §4
> (execution model) + Programming FAQ + Batchelder (verified 2026-06-16). Budget extra time here;
> everything downstream (mutability, scope, closures, the "gotchas") is a corollary.

## A. The core claim `[settled]`
- *"Names refer to objects. Names are introduced by name binding operations."* Assignment `a = obj`
  **binds the name `a` to the object** — it does **not** copy the object and does **not** create a
  "box." `[settled — Language Reference §4, verified 2026-06-16]`
- Batchelder's sharpening: names *are* Python's variables, but they **refer to values**; assignment
  "makes a name refer to a value," and it works **identically for mutable and immutable** objects.
  `[settled — Batchelder PyCon 2015, verified 2026-06-16]`

## B. The mechanism, made visual
- `a = [1, 2]` → one list object exists; `a` points at it.
- `b = a` → **no new object**; `b` points at the *same* list. `a is b` → True.
- `b.append(3)` → the one shared object changes; `a` sees `[1,2,3]` too (**aliasing**).
- `b = [9]` → **rebinding** `b` to a new object; `a` unaffected. *Rebinding ≠ mutating* — the single
  most important distinction in the unit. `[settled — §4; FAQ aliasing examples]`

## C. Identity vs equality (misconceptions M1, M2, M3)
- `==` → **value equality** (`__eq__`); `is` → **identity** (same object; `a is b` ⟺ `id(a)==id(b)`).
  `[settled — FAQ, verified 2026-06-16]`
- Use `is` only for **singletons/sentinels** (`is None`, `is True/False`). **Never** `is` on
  ints/strs: caching of small ints (−5..256) and interned strings makes `is` *accidentally* work,
  but it's an implementation detail. FAQ's own counterexample: `a=10_000_000; c=5_000_000+5_000_000;
  a is c` → **False**, `a == c` → True. `[settled — FAQ "is vs ==", verified 2026-06-16]`

## D. Where this threshold bites (and how to detect crossing)
- Diagnostic: "After `b = a; b.append(3)`, what is `a`?" A box-model learner says `[1,2]`; a crossed
  learner says `[1,2,3]` and can explain *why* (one shared object). `[settled]`
- Productive-failure setup: have them **predict** the aliasing example, run it, reconcile the
  surprise — this is where the model actually reorganizes (`research/03 §5`).

## What the engine teaches from this
This unit is taught as a **threshold**, not a syntax lesson: productive failure first (predict →
run → reconcile), heavy retrieval, and don't advance to collections (U5) until the alias/rebind
distinction is demonstrated, not just nodded at. Re-anchor here whenever a later gotcha (mutable
defaults, closures, scope) surfaces — they're all the same fact.

## Confidence / gaps
All core claims `settled` at primary source. No open items.
