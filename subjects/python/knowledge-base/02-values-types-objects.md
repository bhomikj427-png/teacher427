# U2 — Values, types, and objects (deep notes)

> Deep pass 2026-06-16. Builds Big Idea #1 (everything is an object with identity/type/value) at
> the level a beginner can act on. Primary source: Language Reference §3 (verified 2026-06-16).

## A. Every object has identity, type, value `[settled]`
- Verbatim: *"Every object has an identity, a type and a value."* Identity = its fixed "which object
  is this" (`id()`, `is`); **never changes**. Type = the operations it supports (`type()`); **never
  changes**. Value = its contents; **may or may not change** (mutability, U5). `[settled — Language
  Reference §3, verified 2026-06-16]`
- Mechanism to teach: `type(x)` answers "what kind," `id(x)` answers "which one," `x` (the name)
  is just a label pointing at it.

## B. The core built-in scalar types
- `int` — arbitrary precision (no overflow); `float` — IEEE-754 double; `complex`; `bool` (a
  **subclass of int**: `True == 1`, `False == 0`). `str` — text (Unicode), immutable. `NoneType` —
  the single `None` object (a singleton). `[settled — Library Reference stdtypes; bool⊂int verified
  verbatim 2026-06-16 — see §D]`
- **Arbitrary-precision int** is a genuine differentiator vs C/Java (no silent overflow) — worth
  flagging. `[settled — stdtypes numeric]`

## C. Operators are syntax over methods (seed for the data model, U10)
- `a + b` dispatches to `a.__add__(b)`; `len(x)` to `x.__len__()`; etc. So "what works on this
  value" = "what dunders its type defines" (duck typing, U10). Don't teach the dunders yet — just
  plant that operators aren't magic, they're method calls. `[settled — Language Reference §3]`

## D. Numbers: the division traps (misconception M9)
- `/` is **true division → always float** (`5/2 == 2.5`); `//` is **floor division** "always
  rounded towards minus infinity" — docs' examples `1//2==0`, `(-1)//2==-1`, so `-5//2 == -3`; `%`
  is remainder, `**` power, `divmod(x,y)==(x//y, x%y)`. Mixed int/float → float. `[settled —
  Library Reference stdtypes, verified 2026-06-16]`
- `bool` **is a subclass of `int`** (`True`==1, `False`==0), though "relying on this is discouraged
  — explicitly convert using `int()`." `[settled — stdtypes, verified 2026-06-16]`

## E. Conversions are *new objects*, not in-place changes
- `int("3")`, `str(3)`, `float(3)` **create new objects** (immutables can't change in place). This
  reinforces T1/T2. `[settled — follows from immutability, §3]`

## What the engine teaches from this
Make them *predict* `type()`/`id()` results and division outcomes before running (retrieval +
desirable difficulty). The bool⊂int and `/` vs `//` facts are high-yield surprises — use productive
failure (ask "what is `5/2`?" and let the float surprise land).

## Confidence / gaps
All `settled` at primary source (division, divmod, bool⊂int verified verbatim 2026-06-16). Dunder
dispatch seeded here, taught in U10. No open items.
