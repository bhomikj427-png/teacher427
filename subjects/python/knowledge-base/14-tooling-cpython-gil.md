# U14 — Tooling, the runtime & the GIL (deep notes) [professional]

> Deep pass 2026-06-16. Primary source: official glossary (GIL) verified 2026-06-16. This unit is
> partly **moving-field** (packaging tools, free-threading) — those claims carry a recheck horizon
> and must be re-verified before teaching (map §6).

## A. The CPython execution model `[settled — overview depth]`
- Source → **bytecode** (compiled, cached as `.pyc`) → evaluated by the **CPython VM** (the eval
  loop). Memory is managed by **reference counting** plus a **cyclic garbage collector**. `[settled
  — glossary bytecode; refcount/cyclic-GC overview standard/uncontested; deeper C-internals out of
  scope per map §6]`

## B. The GIL (Global Interpreter Lock) `[settled — with evolving caveat]`
- *"The mechanism used by the CPython interpreter to assure that only one thread executes Python
  bytecode at a time."* It makes the object model implicitly thread-safe but means **CPU-bound
  multithreading doesn't parallelize** in standard CPython. `[settled — glossary, verified
  2026-06-16]`
- It is **released on I/O** and by some C extensions during heavy computation → **threads do help
  I/O-bound** work. For CPU-bound parallelism, use **multiprocessing** (separate processes) or C
  extensions. `[settled — glossary, verified 2026-06-16]`
- **It's a CPython implementation fact, not a language spec** — other implementations differ.
  **Free-threading / no-GIL (PEP 703):** an optional build that removes the GIL — **experimental in
  3.13**, and **officially *supported* (no longer experimental) in 3.14 via PEP 779**, though **not
  the default build**; making it default is a future, uncommitted phase. Single-threaded overhead in
  free-threaded mode is now ~5–10%. `[settled-as-of 2026-06-16 — PEP 703/779 + docs howto; recheck
  horizon: default-build timeline is moving]`

## C. Concurrency model (orientation)
- `threading` (I/O-bound, GIL-limited for CPU), `multiprocessing` (CPU-bound, true parallel),
  `asyncio` (single-thread cooperative concurrency for I/O). Pick by workload. `[settled —
  concurrency-model concept standard/uncontested]`

## D. Environments, packaging, testing (moving field)
- **Stable concepts:** **isolation** (a per-project virtual environment), **dependency pinning /
  lockfiles**, and **`pyproject.toml`** as the project metadata/declaration standard. These are
  durable — teach them as the core. `[settled — PyPA guidance, verified 2026-06-16]`
- **Current tooling (verified 2026-06-16; moving field):** `venv` (built-in, 3.3+) + `pip` is the
  universally-available **baseline** every professional must know. **`uv`** (Astral, Rust) is the
  fast-rising 2026 all-in-one (env + install + Python-version + lockfile, 10–100× faster); Poetry/
  PDM/conda also in use. PyPA: "always use virtual environments." Teach the baseline; show `uv` as
  the modern default. `[settled-as-of 2026-06-16; recheck horizon — re-confirm before re-teaching]`
- Testing: `pytest` (de-facto standard) / `unittest`; debugging: `pdb` / `breakpoint()`, reading
  tracebacks; lint/format: ruff / black (ruff rising). Type-check: mypy / pyright (from U13).
  `[settled — concept; specific tool dominance is evolving]`

## What the engine teaches from this
Demonstrate the GIL concretely: a CPU-bound task threaded shows **no speedup**, then multiprocessing
does — productive contrast cements *why*. Teach environment isolation by hitting a dependency clash
first. Keep tool choices labeled **evolving** and honest; teach the stable concepts (isolation,
pinning, why testing) as the durable core.

## Confidence / gaps
GIL semantics `settled` at glossary; free-threading status (experimental 3.13 → supported-not-default
3.14, PEP 703/779) and current packaging/testing tooling **verified as-of 2026-06-16**. The only
standing items are **moving-field recheck horizons** (free-threading default-build timeline; tool
dominance) — re-confirm before re-teaching, per map §6. CPython internals covered to
working-professional depth (bytecode/VM, refcount + cyclic GC); C-source depth out of scope for this
goal.
