# U13 — Type hints (deep notes)

> Deep pass 2026-06-16. Primary source: PEP 484 (verified 2026-06-16). The load-bearing fact —
> **hints are not runtime-enforced** — is the whole reason this unit exists where it does. Some
> syntax is version-sensitive (recheck horizon).

## A. What hints are (Big Idea #7) `[settled]`
- PEP 484 (Python 3.5, 2014) added **annotation syntax**: `def f(name: str, n: int = 0) -> bool:`
  and `x: list[int] = []`. They are stored in `__annotations__`. `[settled — PEP 484, verified
  2026-06-16]`
- **They are NOT enforced at runtime:** *"no type checking happens at runtime."* Python "will remain
  a dynamically typed language… [hints are not] mandatory." External tools (**mypy**, **pyright**)
  check them statically; the interpreter ignores them for execution (M6). `[settled — PEP 484
  verbatim, verified 2026-06-16]`

## B. Why hint at all (the value, honestly framed)
- Catch bugs before running (static checking), document intent precisely, power editor autocomplete/
  refactoring. Cost: extra verbosity; can over-constrain duck-typed code. It's **opt-in and
  gradual** — type the interfaces that matter, leave the rest dynamic. Teach as judgment, calibrated
  to the learner's goal (more valuable for larger/long-lived codebases). `[settled — PEP 484 intent;
  adoption extent is judgment]`

## C. The vocabulary (version provenance — verified; target is 3.14, all present) `[settled]`
| Feature | Syntax | Since | PEP |
|---|---|---|---|
| Built-in generics | `list[int]`, `dict[str,int]` | **3.9** | 585 |
| Union / Optional | `int \| str`, `X \| None` (= `Optional[X]`) | **3.10** | 604 |
| Type-alias statement + generic syntax | `type Vec = list[float]`, `class C[T]`, `def f[T]` | **3.12** | 695 |
- Older equivalents still work (`typing.List`, `typing.Union`, `typing.Optional`, `TypeVar` +
  `Generic[T]`) — teach modern syntax (3.14) but recognize legacy. `Any`, `Callable`, `Iterable`,
  protocols also live in `typing`. `[settled — typing docs version notes, verified 2026-06-16]`

## What the engine teaches from this
Demonstrate the non-enforcement directly: annotate `n: int`, pass a `str`, show it **runs anyway**,
then show a type checker flagging it — the contrast cements M6. Introduce hints on code the learner
already wrote (concrete). Keep it opt-in; don't let typing become cargo-cult ceremony (anti-Zen).

## Confidence / gaps
Non-enforcement (PEP 484) + the version provenance of `list[int]` (3.9), `X|Y` (3.10), `type`/
`class C[T]` (3.12) all `settled` at primary source (verified 2026-06-16); target 3.14 has them all.
mypy/pyright tool specifics → U14. No open items (re-confirm only if the learner targets a Python
older than 3.12).
