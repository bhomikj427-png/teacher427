# Python — Curriculum (derived from knowledge-base/00-map.md)

> Ordered objectives, **prerequisites first** (cognitive-load order, `research/01 §2`). Strictly
> downstream of the map's prerequisite graph (§2). **The full deep pass is already done** (learner
> requested the exhaustive build): every unit has a deep note in `knowledge-base/01`–`14`. Still
> re-confirm/refresh each unit's note (esp. version-gated/evolving items) before teaching it.
> Mastery-gated: a unit opens only when the prior one is *demonstrated*, not merely seen. Threshold
> units (★) get extra time + productive-failure setups. **Unit → deep note:** U1→01 … U14→14.
>
> **Goal: resume-grade *professional* Python** (Python 3.14). `[locked 2026-06-16]` All four phases
> are the target — Phase IV (typing, tooling, testing, the runtime) is *required*, not optional —
> because the bar is "defensible on a resume / passes a junior–mid screen." Correctness, idiom,
> type hints, and testing are held high from early on.
>
> **Learner entry point: U1 (absolute zero).** First session diagnoses prior programming exposure
> (if any) — the only remaining open variable — then begins.

---

## Phase 0 — Orientation

**U1. What Python is & how code runs** *(framing; install the right model early)*
- What Python is (high-level, dynamic, interpreted-via-bytecode, CPython); REPL vs script.
- Get running fast (hello world, one script); comments; indentation **is** syntax (M7).
- Seed (don't yet unpack) "names point at objects, not boxes."
- Outcome: can run code two ways; can state that values are objects and Python has no "boxes."

## Phase I — Core data & control

**U2. Values, types, objects**
- `int`/`float`/`str`/`bool`/`None`; `type()` & `id()`; bool⊂int; arbitrary-precision ints.
- Division traps: `/` (float) vs `//` (floor) vs `%`/`**` (M9). Conversions create new objects.
- Outcome: predicts `type()`/division results; explains object = identity+type+value.

**U3. Names bind to objects; identity vs equality** ★★(T1 — master threshold)
- Assignment **binds**, never copies; aliasing vs rebinding; `is` vs `==`; never `is` on int/str
  (interning, M1/M2/M3).
- Outcome: correctly predicts an aliasing/rebinding case and explains *why* (one shared object).

**U4. Control flow & truthiness**
- `if/elif/else`, `while`, `for` (as iteration, not counting), `break`/`continue`, `for/else`.
- Truthiness (falsy set; `__bool__`/`__len__`, M8); `and`/`or` **return operands**; chained compares.
- **`match`/`case`** structural pattern matching (3.10+) — branch on *shape*, destructure.
- Outcome: sorts values truthy/falsy correctly; uses `if seq:`; predicts `and`/`or` results; uses
  `match` to destructure a small data structure.

**U5. Collections & mutability** ★(T2)
- `list`/`tuple`/`dict`/`set` (+`frozenset`); mutable vs immutable; tuple-as-record vs list-as-
  sequence (M11); hashable keys; aliasing; shallow vs `deepcopy`; don't mutate while iterating (M15).
- Outcome: predicts a shallow-copy nested-mutation case; chooses the right collection with reason.

**U6. Functions, arguments & scope** ★(T5)
- `def`/`return`; positional/keyword/default/`*args`/`**kwargs`; **call by assignment** (M5);
  **mutable-default trap** (M4); LEGB; **local-by-assignment** → `UnboundLocalError` (M13);
  `global`/`nonlocal`; closures + **late binding** (M12).
- Outcome: predicts `UnboundLocalError` and the loop-closure result, and fixes both.

## Phase II — Pythonic idiom

**U7. Iteration protocol, comprehensions & generators** ★(T4)
- iterable→iterator→`__next__`→`StopIteration`; `for` desugaring; one-shot iterators; list/dict/set
  comprehensions & generator expressions; `yield`/laziness; `enumerate`/`zip`/`range`/`itertools`.
- Outcome: hand-writes an iterator; converts a loop to a comprehension; explains laziness.

**U8. Exceptions & the EAFP mindset** ★(T6)
- `try/except/else/finally`, `raise`, `raise … from`, custom exceptions, the hierarchy; exception
  groups / `except*` (3.11+); **EAFP vs LBYL** (incl. the race-condition argument); catch
  specifically; "errors should never pass silently."
- Outcome: rewrites an LBYL check as EAFP and justifies which fits a given case.

**U9. Modules, packages, imports & namespaces**
- Module = file = namespace; imports run once & cache (M14); import forms (avoid `import *`);
  packages; `if __name__ == "__main__":`; stdlib orientation; *why* environments isolate (→ U14).
- Outcome: splits a script into modules; predicts run-as-script vs import behavior.

## Phase III — Objects & abstraction

**U10. Everything-is-an-object & the data model** ★(T3)
- Classes/instances/`self`/`__init__`; **dunder protocols** (`__repr__`/`__eq__`/`__len__`/
  `__iter__`/`__call__`…); operators & builtins dispatch to dunders; **duck typing**.
- Outcome: makes a custom object work with `print`/`==`/`len`/`for` by implementing protocols.

**U11. OOP in depth**
- Inheritance (MRO/`super`) **vs composition** (judgment); class vs instance attrs (shared-state
  trap); `@property`; `@classmethod`/`@staticmethod`; no enforced privacy (M10); `@dataclass`;
  **when *not* to use a class**.
- Outcome: refactors to a class only when state+behavior cohere; explains MRO on a 2-level example.

## Phase IV — Professional

**U12. Idiomatic Python & power tools** — PEP 20 (Zen), PEP 8 (style), Pythonic idioms; **decorators**
(closures applied); **context managers** (`with`, the `__enter__`/`__exit__` protocol).
**U13. Type hints** — PEP 484 annotation syntax; **not runtime-enforced** (M6); modern syntax
(`list[int]` 3.9, `X|Y` 3.10, `type`/`class C[T]` 3.12 — all in 3.14); mypy/pyright; opt-in,
gradual. *Resume-grade: be fluent reading and writing typed code.*
**U14. Tooling, runtime & the GIL** — CPython bytecode/VM, refcount + cyclic GC; **the GIL** (I/O vs
CPU; threading/multiprocessing/asyncio); **free-threading** (experimental 3.13 → supported-not-
default 3.14); **virtual environments + packaging** (venv/pip baseline, `pyproject.toml`, `uv`);
**testing** (pytest), debugging (pdb/tracebacks), lint/format (ruff). *(Moving field — re-verify
free-threading + tooling before re-teaching.)*

---

### Notes
- **Block before interleave** (`research/02 §6`): each unit solid before mixing (e.g. interleaving
  collection-choice + comprehension + EAFP decisions) — earliest at U7+.
- Threshold units (★/★★) use **productive failure first** where the goal is concept/transfer
  (`research/03 §5`) — T1, T2, T4, T6, T3 reframes; worked-examples-first where it's procedure
  (syntax of functions, comprehensions, try/except, classes).
- **Goal locked** = resume-grade professional (map §0): all phases are in scope; don't truncate at
  Phase II. A small **portfolio-worthy capstone project** (and tests for it) near the end is the
  natural proof-of-skill for a resume — fold it into U12–U14.
- **Re-verify before re-teaching** the moving-field bits of U14 (free-threading default-build
  timeline, packaging tool dominance), per the map's recheck horizon and
  `subject-research-protocol.md` §8/§10. Everything else is verified `settled` for 3.14.
