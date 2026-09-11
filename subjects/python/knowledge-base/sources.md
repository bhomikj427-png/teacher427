# Python — Sources (tiered per protocol §2)

> Tiered by authority. `[verified 2026-06-16]` = reached and read at primary level **this session**
> via web fetch (not model recall — protocol §1: recall ≠ sourced). Python docs are versioned; the
> object/execution/data-model semantics below are stable across the Python 3.x line, but
> version-specific syntax/library claims carry a recheck horizon (§10).

## Tier 1 — Primary / foundational
- **The Python Language Reference — §3 "Data model"** — the canonical definition of objects
  (identity/type/value), mutability, and the special ("dunder") method protocols. *The real ground
  for Big Ideas #1, #3, #4.* `[verified 2026-06-16]`
  https://docs.python.org/3/reference/datamodel.html
- **The Python Language Reference — §4 "Execution model"** — names, binding, scopes/namespaces
  (LEGB), `global`/`nonlocal`, the local-by-assignment rule, `UnboundLocalError`/`NameError`. *The
  ground for Big Idea #2 and threshold T5.* `[verified 2026-06-16]`
  https://docs.python.org/3/reference/executionmodel.html
- **The Python Standard Library — "Built-in Types" (stdtypes)** — truth-value testing rules
  (what is falsy; `__bool__`/`__len__`), numeric/sequence/mapping/set type behavior, methods.
  *Ground for truthiness (U4) and the collection types (U5).* `[verified 2026-06-16: truth-value
  testing section]`
  https://docs.python.org/3/library/stdtypes.html
- **The Python Glossary** — authoritative short definitions: duck-typing, EAFP, LBYL, iterable,
  iterator, generator, generator iterator, mutable, immutable, hashable, GIL. *Ground for Big Ideas
  #4, #5, #8 and thresholds T3, T4, T6.* `[verified 2026-06-16]`
  https://docs.python.org/3/glossary.html
- **Python FAQ — "Programming FAQ"** — official explanations of the canonical gotchas: mutable
  default arguments (and the `None` fix), call-by-assignment / no call-by-reference, `is` vs `==`
  with the interning caveat, late-binding closures in loops. *Ground for the misconception list and
  U5/U6/U7.* `[verified 2026-06-16]`
  https://docs.python.org/3/faq/programming.html
- **PEP 20 — "The Zen of Python"** (Tim Peters, 2004) — the 19 written aphorisms; the design
  philosophy the language is built around. *Ground for Big Idea #6.* `[verified 2026-06-16: full
  text]`  https://peps.python.org/pep-0020/
- **PEP 8 — "Style Guide for Python Code"** (van Rossum, Warsaw, Coghlan) — indentation (4 spaces),
  line length (79; 72 for docstrings/comments), naming (snake_case / CapWords / UPPER_CASE), "code
  is read more than written," consistency hierarchy. *Ground for U12.* `[verified 2026-06-16]`
  https://peps.python.org/pep-0008/
- **PEP 484 — "Type Hints"** (2014, Python 3.5) — annotation syntax, the `typing` module, and the
  load-bearing fact that **hints are not enforced at runtime** and Python "will remain a dynamically
  typed language." *Ground for Big Idea #7 and U13.* `[verified 2026-06-16]`
  https://peps.python.org/pep-0484/
- **The Python Tutorial (official)** — canonical "from zero" teaching order; sections **Classes**
  (name mangling, `self`, class-vs-instance vars + shared-mutable pitfall) and **Errors** (try/
  except/else/finally, `raise … from`, user exceptions, ExceptionGroup/`except*`) read at primary
  level. *Tier 1.* `[verified 2026-06-16: tutorial/classes, tutorial/errors]`
  https://docs.python.org/3/tutorial/index.html
- **Library Reference — `copy` module** — shallow vs deep copy (references vs recursive copies).
  `[verified 2026-06-16]`  https://docs.python.org/3/library/copy.html
- **Language Reference — "The import system"** — `sys.modules` caching / no re-execution, module
  object, regular vs namespace packages, `__init__.py`. `[verified 2026-06-16]`
  https://docs.python.org/3/reference/import.html
- **Library Reference — Built-in `super()`** — proxy delegating along `__mro__`; "search starts from
  the class right after type." `[verified 2026-06-16]`
  https://docs.python.org/3/library/functions.html#super
- **Library Reference — `functools`** — `wraps`/`update_wrapper`, `lru_cache`/`cache`, `partial`,
  `reduce`. `[verified 2026-06-16]`  https://docs.python.org/3/library/functools.html
- **Library Reference — `contextlib`** — `@contextmanager` (pre-yield=`__enter__`,
  post-yield=`__exit__`). `[verified 2026-06-16]`  https://docs.python.org/3/library/contextlib.html
- **Library Reference — `typing`** — version notes for `X|Y` (3.10), `Optional`=`X|None`, built-in
  generics (3.9), `type`/`class C[T]` (3.12). `[verified 2026-06-16]`
  https://docs.python.org/3/library/typing.html
- **PEP 257 — Docstring Conventions** — docstring = first statement; `__doc__`; one/multi-line
  conventions; triple double quotes. `[verified 2026-06-16]`  https://peps.python.org/pep-0257/
- **PEPs 634 (match), 604 (X|Y), 585 (built-in generics), 695 (type params), 654 (exception
  groups), 703 (free-threading), 779 (free-threading supported status)** — version/feature
  provenance. `[verified 2026-06-16 via PEPs / What's New / docs howto]`
  https://peps.python.org/pep-0779/
- **Python Packaging User Guide (PyPA) + 2026 ecosystem survey** — `venv`+`pip` baseline,
  `pyproject.toml` standard, `uv` rising. `[verified 2026-06-16; moving field — recheck horizon]`
  https://packaging.python.org/

## Tier 2 — Authoritative secondary
- **Ned Batchelder — "Facts and Myths about Python names and values"** (PyCon 2015 talk + written
  article) — the field's canonical treatment of the names-are-references model; corroborates and
  clarifies Language Reference §4 ("Names are Python's variables: they refer to values"; assignment
  works the *same* for mutable and immutable). Tier 2 expert / documented-error reference. `[verified
  2026-06-16 via search excerpt + article URL]`  https://nedbatchelder.com/text/names
- **Luciano Ramalho — *Fluent Python* (2nd ed., O'Reilly)** — widely respected deep treatment of
  the data model, sequences, dicts/sets, iterables/generators, classes/protocols. Tier 2 for the
  expert organizing schema. *No claim in this base rests on it alone — every load-bearing claim it
  would support has been independently verified at the primary docs above.* `[corroborative only]`

## Tier 3 — Derivative (orientation / leads only)
- **Real Python** (realpython.com) — high-quality tutorial site; good for orientation and worked
  examples on scope, comprehensions, OOP, decorators. **Leads, not final word** — triangulate any
  load-bearing claim back to the docs.
- **Wikipedia — "Python (programming language)"** — history, design, version lineage; corroboration
  and orientation only.

## Tier 4 — Low-trust (chased, not cited)
- Content-farm "learn Python in X" pages, Q&A folklore, AI-generated summaries surfaced in search —
  used only to locate Tier 1–2 originals; **never** the basis of a claim.

---
### To upgrade (standing)
- **Backlog cleared (2026-06-16).** The complete deep dive resolved the previously-deferred items
  (numeric ops, copy, import system, data-model methods, MRO/super, name mangling, exceptions,
  functools/contextlib, PEP 257, version-gated syntax, free-threading, packaging). All now verified
  at primary source.
- **Standing recheck horizon only** (moving field, not a gap): free-threading default-build
  timeline, packaging tool landscape, and any post-3.14 syntax — re-confirm before re-teaching
  U13/U14. Target version pinned to **Python 3.14**; update doc links if the learner uses another.
