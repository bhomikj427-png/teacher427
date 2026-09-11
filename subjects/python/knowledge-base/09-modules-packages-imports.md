# U9 — Modules, packages, imports & namespaces (deep notes)

> Deep pass 2026-06-16. Import-system semantics **verified at primary source** (Language Reference
> "The import system"). "Namespaces are one honking great idea" (PEP 20) cashes out here.

## A. Modules & namespaces
- A **module** is a `.py` file (Python has "only one type of module object"); importing it runs its
  top-level code **once** and gives back a **module object** whose attributes are its top-level names
  — a **namespace**. `[settled — import system docs, verified 2026-06-16]`
- **Imports are cached:** *"the first place checked during import search is `sys.modules`… a cache of
  all modules previously imported"*; if present, that object satisfies the import (no re-run) — why
  side-effects fire once (M14). The module is added to `sys.modules` *before* its code executes, which
  prevents infinite recursion on circular imports. `[settled — import system docs, verified
  2026-06-16]`
- Import forms: `import mod` (→ `mod.name`), `from mod import name`, `import mod as m`. Avoid
  `from mod import *` (pollutes namespace; obscures origins — anti-Zen "explicit > implicit").
  `[settled — PEP 20; standard]`

## B. Packages
- A **regular package** is a directory with an `__init__.py` that is "implicitly executed" on import,
  binding the names it defines into the package namespace; importing `parent.one` runs
  `parent/__init__.py` then `parent/one/__init__.py`. A **namespace package** has *no*
  `__init__.py` and can span multiple directories. `[settled — import system docs, verified
  2026-06-16]`
- Absolute vs relative imports; the module search path (`sys.path`). `[settled — standard]`

## C. `if __name__ == "__main__":` `[settled — substance]`
- A module's `__name__` is `"__main__"` when **run as a script**, but its own name when
  **imported**. The guard runs script-only code (CLI entry) without firing it on import — directly
  follows from "import runs top-level code once" (A). `[settled — standard; follows from verified
  import semantics]`

## D. The standard library & ecosystem (orientation; tooling depth in U14)
- "Batteries included": `os`, `sys`, `pathlib`, `datetime`, `collections`, `itertools`,
  `functools`, `json`, `re`, `math`, `random`, etc. — reach for the stdlib before writing your own.
  Third-party packages via **pip**, isolated in **virtual environments** (concept here; current tool
  recommendation is evolving — U14). `[settled — concept; tool specifics `uncertain`/evolving]`

## What the engine teaches from this
Have them split a working script into modules and predict what runs on import vs. on direct run
(the `__name__` guard) — concrete, retrieval-driven. Emphasize namespaces as the payoff (PEP 20).
Defer pip/venv mechanics to U14 but introduce *why* isolation matters.

## Confidence / gaps
Import-system semantics (caching, regular vs namespace packages, `__init__.py`) `settled` at primary
source (verified 2026-06-16). `__name__ == "__main__"` follows directly. Packaging/venv *tooling*
specifics live in U14 (verified there). No open items here.
