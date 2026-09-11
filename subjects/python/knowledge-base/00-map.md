# Python — Knowledge Base Map (Layer 2)

> Built per `../../../subject-research-protocol.md`. Map pass (big ideas, prerequisite graph,
> threshold concepts, scope, source canon) **plus the full exhaustive deep pass** — at the
> learner's request (2026-06-16) the §8 "build the entire base upfront" option was taken, so
> per-unit deep notes `01`–`14` exist for the whole curriculum, not just the next unit. Confidence-
> marked throughout: `settled` / `contested` / `uncertain` / `suspect`. Sources tiered in `sources.md`.
>
> **Date built:** 2026-06-16. Python is a *living, fast-moving but stable-core* language (current
> series Python 3.x; the data model, object model, and core semantics are stable across the 3.x
> line). Version-sensitive claims (new syntax, free-threading, library specifics) carry a recheck
> horizon (§10 of the protocol). The **load-bearing spine below was verified against primary
> sources this session** (python.org Language Reference, Library Reference, glossary, FAQ; PEPs
> 8/20/484) — not from model recall. See `CHANGELOG.md` and `sources.md`.
>
> **Stage status: `stage-2✓-equivalent` (provisional — stamped 2026-07-05, engine audit).** This
> base predates the two-stage vocabulary; its map + exhaustive deep pass (units 01–14, full
> verify-backlog closed at primary source, integrity-audited 2026-06-16) is the same complete-base
> standard the teaching gate requires. *Provisional because* no formal §0 surplus exit test is on
> record — run one and upgrade this line. Version-gated claims keep their recheck horizon
> (pinned: Python 3.14).

---

## 0. Scope & goal calibration

- **Learner goal:** **resume-grade *professional* Python proficiency** — Python listed as a skill
  the learner can defend in an interview and use on the job: correct, idiomatic ("Pythonic") code,
  fluent with the object/data model, OOP, iteration/generators, exceptions, modules/packaging,
  **type hints, testing, virtual environments**, and an honest grasp of the CPython runtime (the
  GIL/free-threading, concurrency model). `[settled — stated by learner 2026-06-16]` Starting level
  is **absolute zero** (stated). So the base is built **deep and complete**, teaching **climbs from
  zero** but is **aimed all the way to Phase IV** — the professional units are the target, not
  optional. The bar is "could pass a junior/mid Python screen and write maintainable code," so
  correctness, idiom, typing, and testing are held to a high standard from early on.
- **Target Python version: 3.14** (current stable: **3.14.6**, released 2026-06-10; 3.13 in
  maintenance; 3.15 hit feature freeze June 2026). Teach modern syntax (`match`, `X | Y` unions,
  built-in generics, `type` aliases) and note the version each feature landed in. `[settled —
  python.org downloads / Real Python news, verified 2026-06-16]`
- **What "Python" is:** a **high-level, general-purpose, dynamically-typed, interpreted**
  programming language emphasizing **readability** and a **uniform object model** ("everything is
  an object"). The reference implementation is **CPython** (compiles source to bytecode, run by a
  virtual machine). `[settled — python.org docs; near-universal]`
- It is **not** a typeless or "magic" language: its behavior is *generated from a small set of
  consistent rules* (the data model + the execution model). The whole point of this base is to
  teach those generative rules, so the learner reasons *from mechanism*, never memorizes surface
  recipes. `[settled — Language Reference §3, §4]`

---

## 1. The big ideas (the deep structure — what an expert reasons *from*)

Everything in the subject hangs off these. If a lesson can't be traced to one, it's drifting.

1. **Everything is an object; every object has an identity, a type, and a value.** "All data in a
   Python program is represented by objects or by relations between objects." Identity never
   changes (`is` / `id()`); type never changes; *value* may or may not change (that's mutability).
   Functions, classes, modules, even code are objects. This uniformity is the root simplicity of
   the language. `[settled — Language Reference §3 "Data model", verified 2026-06-16]`
2. **Names are references to objects, not boxes that hold values.** Assignment **binds a name** to
   an object; it never copies the object. `a = b` makes `a` refer to the *same* object as `b`.
   Argument passing is the same act ("call by assignment / by object sharing") — so there is no
   call-by-reference. Almost every "spooky" Python behavior (aliasing, the mutable-default trap,
   `is` vs `==`, late-binding closures) is a corollary of this one fact. `[settled — Language
   Reference §4 "Execution model"; FAQ; Batchelder, verified 2026-06-16]`
3. **Mutability is the central fault line.** Objects are either **mutable** (value can change in
   place: `list`, `dict`, `set`, most user objects) or **immutable** (value fixed once created:
   `int`, `float`, `str`, `tuple`, `frozenset`, `bytes`, `bool`). Combined with Big Idea #2, this
   governs copying, equality/hashing, dict keys, default arguments, and shared-state bugs. `[settled
   — Language Reference §3; glossary; verified 2026-06-16]`
4. **Behavior comes from the data model (dunder protocols) + duck typing.** What an object *can do*
   is determined by the special ("dunder") methods its type implements (`__len__`, `__iter__`,
   `__eq__`, `__bool__`, `__repr__`, `__add__`, …), not by a declared class hierarchy. Python code
   asks "does it support this operation?" (duck typing / EAFP), not "what type is it?" Operators,
   `for`, `len()`, truthiness, `with`, etc. are all syntax that dispatches to dunders. `[settled —
   Language Reference §3; glossary "duck-typing"/"EAFP", verified 2026-06-16]`
5. **Iteration is a protocol, and laziness is first-class.** `for`, comprehensions, unpacking, and
   many builtins run on the **iterable → iterator → `__next__()` → `StopIteration`** protocol.
   Generators (`yield`) produce values lazily, one at a time, remembering state between resumes —
   enabling streaming over data too large to hold in memory. `[settled — glossary
   iterable/iterator/generator, verified 2026-06-16]`
6. **Readability and "one obvious way" are part of the language, not optional polish.** Python is
   deliberately opinionated (PEP 20 "Zen of Python"; PEP 8 style). "Pythonic" = using the idiom the
   language was designed for (EAFP, comprehensions, context managers, truthiness) rather than
   transliterating another language. Code is read far more than written. `[settled — PEP 20, PEP 8,
   verified 2026-06-16]`
7. **Dynamically typed at runtime; optionally statically *hinted*.** Types are checked at runtime
   on values, not declared on names. **Type hints (PEP 484) are annotations only — Python does
   *not* enforce them at runtime**; external tools (mypy, pyright) check them voluntarily. The
   language "will remain a dynamically typed language." `[settled — PEP 484, verified 2026-06-16]`
8. **CPython is an interpreter over a uniform runtime; the GIL is part of its model.** Source →
   bytecode → evaluated by a VM. The **Global Interpreter Lock** lets only one thread execute Python
   bytecode at a time in CPython (simplifies the object model; matters for CPU-bound threading).
   It's a *CPython implementation* fact, not a language-spec fact; it's released on I/O and can be
   disabled in 3.13+ free-threaded builds (PEP 703). `[settled — glossary GIL; PEP 703, verified
   2026-06-16; free-threading status is evolving — recheck horizon]`

---

## 2. Prerequisite graph (the spine of `curriculum.md`)

`→` = "must precede." Triangulated for the load-bearing edges (protocol §8). The learner starts at
**(A)** (absolute zero). The big unclimbed thresholds are **(C), (E), (G), (I)**.

```
(A) Orientation ──→ (B) Values, types, objects ──→ (C) ★Names bind to objects
   what Python is,     int/float/str/bool,            assignment = binding, not copy
   REPL, run a file,   type()/id(), expressions       aliasing; is vs ==
   print, comments     vs statements                  [THRESHOLD T1 — master]
   [START HERE]                                              │
        ┌──────────────────────────────────────────────────┘
        ▼
(D) Control flow ──→ (E) ★Collections & mutability ──→ (F) Functions & scope ★
   if/elif/else,        list/tuple/dict/set,              def, args/returns,
   truthiness, bool,    mutable vs immutable, aliasing,   call-by-assignment,
   while, for, break    copy vs deepcopy                  mutable-default trap,
   [needs C]            [THRESHOLD T2]                    LEGB scope, closures
        │                                                 [THRESHOLD T5]
        ▼                                                      │
(G) ★Iteration & comprehensions ──────────────────────────────┘
   iterable/iterator protocol, for-loop mechanism,
   list/dict/set comprehensions, generators/yield, laziness
   [THRESHOLD T4]
        │
        ▼
(H) Exceptions & EAFP ──→ (I) ★Objects & the data model ──→ (J) OOP in depth
   try/except/else/finally,   classes, self, __init__,        inheritance vs
   raise, custom exc,         dunder methods, duck typing,    composition, properties,
   EAFP vs LBYL [T6]          everything-is-an-object [T3]    classmethod/static
        │                                                          │
        ▼                                                          ▼
(K) Modules, packages, imports, stdlib, venv/pip ──→ (L) Idiom & power tools [PROF]
   namespaces, __name__=="__main__"                    decorators, context managers,
        │                                               PEP 8/Zen, common patterns
        ▼                                                          │
(M) Type hints (PEP 484, mypy) ──→ (N) Tooling: testing, debugging, packaging, CPython/GIL [PROF]
```

**Note on (A)–(C):** absolute-zero learners can run code (B) before they truly grasp binding (C);
the danger is letting them build a *box* mental model that T2/T5 later contradict. So **C is taught
explicitly and early**, with retrieval, before collections — it's the cheapest place to install the
correct model and the most expensive to retrofit.

---

## 3. Threshold concepts (budget extra teaching; learners predictably stall here)

The "once you get it, everything reorganizes" ideas — and documented stall points.

- **T1 — Names are references to objects; assignment binds, it does not copy.** The master
  threshold. Coming from a "variable = box holding a value" model (school algebra, or C), learners
  expect `b = a` to copy. It doesn't. Owns aliasing, `is` vs `==`, and sets up T2/T5. `[settled —
  Language Reference §4; FAQ; Batchelder PyCon 2015]`
- **T2 — Mutable vs immutable & aliasing.** Two names can share one mutable object, so mutating
  "one" changes "both"; immutables can't be changed in place so they *feel* like copies. The source
  of the most common beginner bugs (shared lists, `copy` vs `deepcopy`, mutating while iterating).
  `[settled — Language Reference §3; FAQ]`
- **T3 — Everything is an object and behavior comes from the data model.** Functions/classes/modules
  are values you can pass around; operators and builtins dispatch to dunder methods; "type" is not
  a tag but a set of supported operations (duck typing). Reorganizes OOP from "boilerplate" into
  "implement the protocols you need." `[settled — Language Reference §3; glossary]`
- **T4 — Iteration as a protocol + lazy evaluation.** `for` doesn't "loop an index"; it pulls from
  an iterator until `StopIteration`. Generators produce on demand. Once grasped, comprehensions,
  `zip`/`enumerate`/`map`, files-as-iterables, and streaming all unify. `[settled — glossary]`
- **T5 — Scope (LEGB), the local-by-assignment rule, and closures.** "If a name is assigned
  anywhere in a function, it is local *throughout*" → `UnboundLocalError`; `global`/`nonlocal`;
  closures capture *variables, not values* (late binding). Predictable, documented stalls. `[settled
  — Language Reference §4; FAQ late-binding-closures]`
- **T6 — Exceptions as normal control flow (EAFP).** In Python you often *try and catch* rather
  than *check first* (LBYL). Exceptions aren't only for catastrophes; `try/except/else/finally` and
  `StopIteration`/`KeyError` are part of normal flow. A mindset shift from defensive-checking
  languages. `[settled — glossary EAFP/LBYL]`

---

## 4. Known misconceptions

Maintained in `misconceptions.md` (sourced + confidence-marked per protocol §4). Summary pointers:
assignment copies values; `==` and `is` are interchangeable; `int`/`str` identity is reliable
(interning); mutable default arguments are re-created each call; Python passes by value (or by
reference); type hints are enforced at runtime; indentation is cosmetic; integer/float division
behave like other languages; "private" with underscores is enforced; a tuple is "a constant list";
re-importing re-runs a module; closures capture values.

---

## 5. Settled vs. contested vs. evolving

- **Settled & stable across 3.x:** the object model, names/binding, mutability, the data
  model/dunder protocols, iteration protocol, truthiness rules, scope/LEGB, exceptions, the import
  system, PEP 8/PEP 20. These are the spine and were verified at primary source this session.
- **Version-gated syntax (now verified; teach with the version note):** structural pattern matching
  `match`/`case` (3.10, PEP 634); `X | Y` unions incl. `X | None` for Optional (3.10, PEP 604);
  built-in generics `list[int]`/`dict[str,int]` (3.9, PEP 585); `type` alias statement + generic
  syntax `class C[T]`/`def f[T]` (3.12, PEP 695); exception groups / `except*` (3.11, PEP 654).
  `[settled — verified at typing docs / What's New / PEPs 2026-06-16]`
- **Evolving (verified as-of 2026-06-16; carry a recheck horizon):** **free-threading / no-GIL** —
  experimental in 3.13 (PEP 703), **officially *supported* (not default) in 3.14 (PEP 779)**; making
  it the default is a future, uncommitted phase. The *recommended* packaging stack — `venv`+`pip`
  (built-in baseline, universally available) with **`pyproject.toml`** as the metadata standard,
  while **`uv`** (Astral) is the fast-rising 2026 all-in-one tool. Teach the *stable concepts*
  (isolation, dependency pinning, lockfiles) as durable; tool choice as evolving. `[settled-as-of
  2026-06-16 — verified; recheck before re-teaching U14]`
- **Style-contested (teach as judgment, not law):** OOP vs. functional/procedural for a given
  problem; when to use classes at all; inheritance vs. composition; how much typing to adopt; which
  third-party tools. Teach the tradeoffs, not one as "correct." `[contested — by design]`

---

## 6. Open questions / to-verify register  *(protocol §9/§10 format)*

> **Status: COMPLETE DEEP DIVE done (2026-06-16) — backlog cleared.** At the learner's request
> ("complete deep dive, don't leave anything there") the deferred page-verify items were resolved
> against primary sources this session. The entire load-bearing + secondary spine is now `settled`
> against python.org primary docs / canonical PEPs. Only two genuinely-irreducible items remain
> (one learner-only, one moving-field recheck horizon) — neither is a research gap.

**Resolved**
- [resolved 2026-06-16] Object identity/type/value + mutability — Language Reference §3. See `01`,`05`.
- [resolved 2026-06-16] Names/binding, LEGB, local-by-assignment, global/nonlocal, late-binding
  closures — Language Reference §4 + FAQ. See `03`,`06`.
- [resolved 2026-06-16] Truth-value testing — Library Reference (stdtypes). See `04`.
- [resolved 2026-06-16] iterable/iterator/generator/duck-typing/EAFP/LBYL/GIL/hashable — glossary.
  See `07`,`08`,`10`,`14`.
- [resolved 2026-06-16] Mutable default args, call-by-assignment, `is` vs `==` (interning) — FAQ.
- [resolved 2026-06-16] PEP 20 / PEP 8 / PEP 484 — peps.python.org. See `12`,`13`.
- [resolved 2026-06-16] **Numeric ops** — `/` float, `//` floor toward −∞ (verbatim examples), `%`,
  `**`, `divmod`, **bool⊂int** — Library Reference stdtypes; `→ settled`. See `02`. (M9)
- [resolved 2026-06-16] **copy vs deepcopy** (references vs recursive copies) — copy module docs.
  See `05`.
- [resolved 2026-06-16] **Import system** — `sys.modules` caching / no re-execution, module=one
  type, regular vs namespace packages & `__init__.py` — Language Reference (import system). See `09`.
  (M14)
- [resolved 2026-06-16] **Data model methods** — `__new__` vs `__init__`, `__repr__`/`__str__`
  fallback, `__eq__`/`__hash__` contract (override `__eq__` ⇒ `__hash__` set to None) — datamodel.
  See `10`.
- [resolved 2026-06-16] **Classes (tutorial)** — `self` is convention, **name mangling**
  `__x`→`_Class__x`, no enforced privacy, **shared mutable class-variable** pitfall (the `tricks`
  example) — tutorial/classes. See `11`. (M10)
- [resolved 2026-06-16] **MRO / `super()`** — proxy delegating along `__mro__`, "search starts from
  the class right after type" — functions.html#super. See `11`.
- [resolved 2026-06-16] **Exceptions** — try/except/else/finally semantics, `raise … from`,
  user-defined exceptions, **ExceptionGroup/`except*`** — tutorial/errors. See `08`.
- [resolved 2026-06-16] **functools** (`wraps`, `lru_cache`/`cache`, `partial`, `reduce`) +
  **contextlib.contextmanager** (pre-yield=`__enter__`, post-yield=`__exit__`) + **PEP 257**
  docstrings — library docs + PEP. See `12`.
- [resolved 2026-06-16] **Version-gated syntax** — `match` (3.10/PEP634), `X|Y` & `X|None` (3.10/
  PEP604), `list[int]` (3.9/PEP585), `type`+`class C[T]` (3.12/PEP695), `except*` (3.11/PEP654) —
  typing docs / What's New / PEPs. See `04`,`13`.
- [resolved 2026-06-16] **Free-threading** — experimental 3.13 (PEP703), **supported-not-default
  3.14 (PEP779)** — docs/howto + PEPs. See `14`.
- [resolved 2026-06-16] **Packaging** — `venv`+`pip` baseline, `pyproject.toml` standard, `uv`
  rising — packaging.python.org guidance + 2026 ecosystem survey. See `14`.
- [resolved 2026-06-16] **Target Python version** — 3.14 (3.14.6 current). Was learner-open; now set.

**Still open (genuinely irreducible — not a research gap, not deferrable busywork)**
- [open 2026-06-16] Learner's **prior programming exposure** (any other language?) — **only
  resolvable by the learner**, in session 1. Tunes pacing and which imported misconceptions to probe
  (a C/Java background makes the "box" model T1 *more* likely). The *end-goal* is now resolved
  (resume-grade professional).
- [open — recheck horizon, not now] Free-threading default-build timeline, the packaging tool
  landscape, and any post-3.14 syntax are a **moving field** (§2 dating). Verified current as of
  2026-06-16; **re-confirm before re-teaching U13/U14**, per protocol §10. CPython internals are
  covered to working-professional depth (bytecode/VM, refcount+cyclic GC, GIL); the C-source level
  is out of scope for this goal and would only be opened if the learner pivots to CPython hacking.
