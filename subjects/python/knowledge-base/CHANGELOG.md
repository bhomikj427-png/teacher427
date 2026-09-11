# Python Knowledge Base — CHANGELOG (correction audit trail, protocol §10)

> Format: `[YYYY-MM-DD] <claim/topic> — <what changed> — <why> — <trigger> — <confidence old→new>`
> Never silently overwrite a claim; record the correction here.

- [2026-06-16] Knowledge base created — map pass + exhaustive deep pass — built and triangulated
  against **primary python.org sources reached this session** (Language Reference §3 data model &
  §4 execution model, Library Reference stdtypes, official glossary, Programming FAQ) and canonical
  PEPs (20, 8, 484), with Ned Batchelder (PyCon 2015) corroborating the names/values model —
  trigger: subject creation (learner request for full from-zero base) — confidence: load-bearing
  spine set to `settled`; version-gated/ecosystem items set `uncertain` with recheck horizon.
- [2026-06-16] Object identity/type/value + mutability (Big Ideas #1, #3) — verified verbatim at
  Language Reference §3 ("Every object has an identity, a type and a value"; immutability nuance for
  containers of mutables) — trigger: map pass — source: docs.python.org/3/reference/datamodel —
  confidence: uncertain(recall) → settled.
- [2026-06-16] Names bind to objects; LEGB; local-by-assignment; global/nonlocal;
  UnboundLocalError; late-binding closures (Big Idea #2, T1, T5, M1/M5/M12/M13) — verified at
  Language Reference §4 + Programming FAQ — trigger: map pass — confidence: uncertain(recall) →
  settled.
- [2026-06-16] Truth-value testing (Big Idea, T-adjacent, M8) — verified exact falsy list and
  __bool__/__len__ mechanism at Library Reference "Built-in Types" — trigger: map pass — confidence:
  uncertain(recall) → settled.
- [2026-06-16] Iteration protocol, duck-typing, EAFP/LBYL, hashable, GIL (Big Ideas #4,#5,#8; T3,
  T4, T6) — verified at official glossary; GIL noted as CPython-specific with 3.13 free-threading
  caveat — trigger: map pass — confidence: uncertain(recall) → settled (GIL free-threading status:
  evolving).
- [2026-06-16] Mutable default args, call-by-assignment, is-vs-== (+ interning caveat M3) — verified
  at Programming FAQ with the docs' own examples — trigger: map pass — confidence: uncertain(recall)
  → settled.
- [2026-06-16] PEP 20 Zen (full 19 aphorisms), PEP 8 (4-space indent, 79-char lines, naming
  conventions, "code is read more than written"), PEP 484 (hints not runtime-enforced; Python stays
  dynamically typed — M6) — verified at peps.python.org — trigger: map pass — confidence:
  uncertain(recall) → settled.
- [2026-06-16] Items left `uncertain` and logged to to-verify (00-map §6): learner end-goal (only
  learner-resolvable); version-gated syntax & free-threading/PEP 703; current packaging/venv tool
  recommendation; Fluent Python / PEP 257 page-level specifics; M9/M10/M14/M15 precise primary-source
  quotes (substance settled, exact wording queued to the relevant unit's deep pass).

--- COMPLETE DEEP DIVE (backlog closed) ---
- [2026-06-16] **End-goal locked = resume-grade *professional* Python**; **target version pinned =
  3.14** (3.14.6 current) — what changed: goal/version moved from assumed/open to set — trigger:
  learner instruction "lock in the end goal… Python being a skill I can put on my resume" + "complete
  deep dive, don't leave anything there" — source: python.org downloads / Real Python news —
  confidence: uncertain → settled. Propagated to 00-map §0, curriculum, learner-profile, progress-log.
- [2026-06-16] **Numeric ops & bool⊂int** (U2, M9) — verified verbatim (`/`→float, `//` floors toward
  −∞ with docs' examples, `divmod`, bool subclass-of-int) — source: Library Reference stdtypes —
  confidence: settled-standard → settled-sourced.
- [2026-06-16] **copy vs deepcopy** (U5) — verified (references vs recursive copies) — source: copy
  module docs — settled-sourced.
- [2026-06-16] **Import system** (U9, M14) — verified `sys.modules` caching/no re-execution, regular
  vs namespace packages, `__init__.py` — source: Language Reference import system — settled-sourced.
- [2026-06-16] **Data-model methods** (U10) — verified `__new__` vs `__init__`, `__repr__`/`__str__`
  fallback, `__eq__`/`__hash__` contract (override `__eq__` ⇒ `__hash__`=None) — source: datamodel —
  settled-sourced.
- [2026-06-16] **Classes/MRO** (U11, M10) — verified name mangling `__x`→`_Class__x`, no enforced
  privacy, shared-mutable class-variable pitfall (tutorial `tricks` example), `super()`/`__mro__`
  ("search starts from the class right after type") — source: tutorial/classes + functions#super —
  settled-sourced.
- [2026-06-16] **Exceptions** (U8) — verified try/except/else/finally semantics, `raise … from`,
  user exceptions, **ExceptionGroup/`except*`** (3.11) — source: tutorial/errors — settled-sourced.
- [2026-06-16] **Power tools** (U12) — verified `functools` (wraps/lru_cache/cache/partial/reduce),
  `contextlib.contextmanager` (pre/post-yield = enter/exit), **PEP 257** docstrings — source: library
  docs + PEP 257 — settled-sourced.
- [2026-06-16] **Version-gated syntax** (U4/U13) — verified `match` (3.10/634), `X|Y`+`X|None`
  (3.10/604), `list[int]` (3.9/585), `type`/`class C[T]` (3.12/695), `except*` (3.11/654) — source:
  typing docs / What's New / PEPs — confidence: uncertain → settled (all present in target 3.14).
- [2026-06-16] **Free-threading** (U14) — verified experimental 3.13 (PEP 703) → **supported, not
  default, in 3.14 (PEP 779)** — source: PEPs + docs howto — confidence: uncertain → settled (with
  recheck horizon on the default-build timeline).
- [2026-06-16] **Packaging** (U14) — verified venv+pip baseline, `pyproject.toml` standard, `uv`
  rising 2026 — source: PyPA guide + ecosystem survey — settled-as-of-date (recheck horizon).
- [2026-06-16] **M9/M10/M14/M15** upgraded from "verify-at-pass" to verified-sourced; all M1–M15 now
  primary-sourced. **00-map §6 backlog cleared** — only irreducible items remain (learner's prior-
  programming exposure; standing moving-field recheck horizon).

--- INTEGRITY AUDIT (annotation-drift reconciliation, no factual content change) ---
- [2026-06-16] **Consistency audit before first teaching** — what changed: the records (00-map §6,
  this changelog, progress-log, sources.md, misconceptions.md) declared the verify-backlog 100%
  closed and "nothing left on verify-later," yet ~13 unit-file annotations still read "page-verify at
  pass / queued," including **three flat self-contradictions** where the file body already carried
  `[verified 2026-06-16]` while its own header/inline note still said "queued/verify-later"
  (`02` §B bool⊂int; `11` header MRO/`super`; `12` header PEP 257) — trigger: learner-directed audit
  ("see if there are cracks in research") — resolution: (a) the three self-contradictions resolved in
  the **verified** direction (the body's primary-source citation is authoritative); (b) the remaining
  "page-verify at pass" notes on **standard/uncontested** facts (`01` VM-detail cross-ref; `04`
  for/else + chained-compare; `07` for-desugaring + comprehension-scope + builtin-laziness; `08`
  exception-hierarchy; `10` Fluent-Python corroboration; `11` classmethod/staticmethod + dataclass
  API; `14` refcount/GC depth + concurrency-model) **relabeled to `standard/uncontested`** to match
  their true epistemic status and each file's own *Confidence* section — these were never
  load-bearing-uncertain and were not re-pulled this pass — confidence: unchanged. **Verified the KB
  carries no live `page-verify/queued/verify-later` residue afterward.** No Python factual claim was
  altered (the content spine was independently re-checked and is correct).
