# U11 — OOP in depth (deep notes)

> Deep pass 2026-06-16. MRO/`super` and name mangling verified at primary source (2026-06-16);
> class/method-kind and dataclass APIs are standard/stable. Builds on U10's data model. Much here is
> **judgment, taught as judgment, not law** (§5 contested-by-design).

## A. Inheritance vs composition `[contested — taught as judgment]`
- **Inheritance** = "is-a"; subclass extends/overrides a base; method lookup follows the **MRO**
  (the `__mro__` list, computed by C3 linearization). **`super()`** returns "a proxy object that
  delegates method calls to a parent or sibling class"; the search **"starts from the class right
  after"** the current one in the MRO (e.g. MRO `D→B→C→A→object`, inside `B`, `super()` searches
  `C→A→object`). `[settled — functions.html#super + datamodel `__mro__`, verified 2026-06-16]`
- **Composition** = "has-a"; hold other objects and delegate. Often preferable to deep inheritance
  ("favor composition over inheritance"). Multiple inheritance/mixins exist but carry MRO complexity.
  Teach the tradeoff, not a rule. `[contested-by-design]`

## B. Attributes, properties, encapsulation
- Instance vs class attributes: "instance variables are for data unique to each instance and class
  variables are for attributes… shared by all instances." A **mutable class attribute** is a shared-
  state trap — the tutorial's own `tricks = []` `Dog` example shows one list "unexpectedly shared by
  all dogs." Sibling of the mutable-default bug (T2). `[settled — tutorial/classes, verified
  2026-06-16]`
- **`@property`** turns attribute access into method calls (computed/validated attributes) without
  changing the caller's syntax — Pythonic alternative to Java getters/setters. `[settled — standard]`
- **No enforced privacy** (M10): *"'Private' instance variables… don't exist in Python."* `_name` =
  convention ("non-public part of the API"); `__name` is **textually replaced with `_classname__name`**
  (name mangling), still reachable. `[settled — tutorial/classes, verified 2026-06-16]`

## C. Method kinds
- **Instance** methods (`self`); **`@classmethod`** (`cls`; alternative constructors); **`@static
  method`** (no implicit first arg; namespaced function). `[settled — classmethod/staticmethod standard/uncontested]`

## D. Reducing boilerplate
- **`@dataclass`** auto-generates `__init__`/`__repr__`/`__eq__` from annotated fields (mind
  **mutable default fields** → `field(default_factory=...)`, again the T2 trap). `namedtuple`/
  `enum` for other record/constant needs. `[settled — dataclasses stable since 3.7;
  `default_factory` standard (present in 3.14)]`

## E. When NOT to use a class (Big Idea #6) `[contested — taught as judgment]`
- Python doesn't force OOP. A module of functions, a dict, or a dataclass is often clearer than a
  class with one method. "Do I need a class?" → "what state+behavior actually travel together?"
  Teach against reflexive Java/C#-style class-everything. `[contested-by-design; PEP 20 simple>complex]`

## What the engine teaches from this
Refactor a procedural solution into a class **only when state+behavior cohere**, and show a case
where a class is *worse* (productive contrast). Properties: start with a public attribute, hit a
validation need, introduce `@property` without breaking callers. Inheritance taught after
composition, with the tradeoff explicit. Gate on explaining MRO/`super` on a 2-level example.

## Confidence / gaps
MRO/`super`, `self`, name mangling, class-vs-instance vars (+ shared-mutable pitfall) `settled` at
primary source (verified 2026-06-16). `@property`, `@classmethod`/`@staticmethod`, `@dataclass` are
standard/stable (dataclasses since 3.7; present in 3.14). Inheritance-vs-composition and
class-vs-no-class remain **contested/judgment by design**. No open items.
