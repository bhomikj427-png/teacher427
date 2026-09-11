# U10 — Everything-is-an-object & the data model (deep notes) ★ Threshold T3

> Deep pass 2026-06-16. Primary source: Language Reference §3 + glossary (duck-typing) verified
> 2026-06-16. This unit converts the early "everything is an object" slogan into the *generative*
> understanding of how behavior is built. Threshold T3. (Fluent Python corroborates only; every
> load-bearing claim here is verified at the primary datamodel docs.)

## A. Classes & instances (mechanism, not boilerplate)
- `class C:` creates a **type object**; `C()` creates an **instance**. **`__new__` creates** the
  instance ("the return value… should be the new object instance"); **`__init__` initializes** it —
  "called after the instance has been created (by `__new__()`), but before it is returned." `__init__`
  must **not return a non-None value** (TypeError). `self` is the instance, passed explicitly first.
  `[settled — datamodel, verified 2026-06-16]`
- **Attributes** live in namespaces (`instance.__dict__`, then the class). Attribute lookup walks
  instance → class → base classes along the **MRO** (U11). `[settled — §3; MRO verified at U11]`

## B. The data model: behavior via dunder methods (Big Idea #4) `[settled]`
- Operators and builtins are **syntax that dispatches to special methods**: `len(x)`→`__len__`,
  `x+y`→`__add__`, `x==y`→`__eq__`, `repr(x)`/`str(x)`→`__repr__`/`__str__`, `if x:`→`__bool__`/
  `__len__`, `for`→`__iter__`/`__next__`, `with`→`__enter__`/`__exit__`, `x[i]`→`__getitem__`,
  `x()`→`__call__`. To make your object behave like a built-in, **implement the relevant protocol**.
  `[settled — Language Reference §3, verified 2026-06-16]`
- `__repr__` "information-rich and unambiguous… for debugging," ideally a valid expression to
  recreate the object; `__str__` "more convenient or concise" for users and **falls back to
  `__repr__`** by default — so define `__repr__` at minimum. `__eq__` + `__hash__` travel together:
  **overriding `__eq__` without `__hash__` sets `__hash__` to `None`** (instances become unhashable);
  "objects which compare equal must have the same hash value." `[settled — datamodel, verified
  2026-06-16]`

## C. Duck typing (Big Idea #4) `[settled]`
- "If it looks like a duck and quacks like a duck…": code uses an object via the **interface
  (methods/attrs) it supports**, not its declared type — avoids `type()`/`isinstance()` checks,
  favors `hasattr`/EAFP. Enables polymorphic substitution without inheritance. ABCs (abstract base
  classes) can *formalize* an interface when needed. `[settled — glossary duck-typing, verified
  2026-06-16]`

## D. Why this is a threshold
- It reorganizes OOP from "ceremony required to make a program" into "implement exactly the
  protocols your object needs to participate in Python's syntax." A learner who gets T3 stops asking
  "do I need a class?" reflexively and starts asking "what protocol does this need to support?"
  `[settled — follows from §3]`

## What the engine teaches from this
Build a small class and **make it work with built-in syntax** by adding dunders one at a time
(`__repr__`, then `__eq__`, then `__len__`, then `__iter__`) — each addition tested by using the
*built-in* (`print`, `==`, `len`, `for`). Productive-failure framing: "make this object printable /
comparable / iterable" before showing the dunder. Tie back to U2 ("operators are method calls")
and U7 (iterator protocol) — same idea, now from the implementer's side.

## Confidence / gaps
All `settled` at primary source: data-model dispatch + duck typing (datamodel §3 + glossary);
`__new__`/`__init__`, `__repr__`/`__str__`, `__eq__`/`__hash__` contract verified verbatim
2026-06-16; MRO verified at U11. No open items.
