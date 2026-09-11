# Python — Known Misconceptions (novice wrong models)

> Per protocol §4: a subject with no misconception list is under-researched. Each entry is a
> *claim* and is confidence-marked + sourced. These feed `learner-profile.md`, the engine's
> productive-failure setups, and the feedback moves. Format: **the wrong model → why it's wrong /
> the correct model → where it bites.** Sourced to python.org primary docs (verified 2026-06-16)
> where marked.

---

## M1 — "Assignment copies the value; `b = a` makes an independent copy." `[settled]`
Wrong model: variables are boxes; `b = a` puts a copy of `a`'s value in box `b`.
Correct: a name is a **reference** to an object; assignment **binds** the name to the *same* object
— no copy is made. After `b = a`, `a is b` is True; they're two names for one object.
Bites: mutating through one name surprises the other (`a = [1,2]; b = a; b.append(3)` → `a` is now
`[1,2,3]`). Root of most aliasing bugs. *Source: Language Reference §4; FAQ "call by assignment";
Batchelder. Verified 2026-06-16.*

## M2 — "`==` and `is` are interchangeable ways to compare." `[settled]`
Wrong model: use either to test equality.
Correct: `==` tests **value equality** (via `__eq__`); `is` tests **identity** (same object;
`id(a)==id(b)`). Use `==` for values, `is` only for singletons (`is None`, `is True/False`) and
sentinels. *Source: Language Reference §3; FAQ "is vs ==". Verified 2026-06-16.*

## M3 — "Small ints / short strings being the same object means `is` works for them." `[settled]`
Wrong model: `a = 256; b = 256; a is b` is True, so `is` is fine for numbers.
Correct: CPython **caches** small ints (−5..256) and interns some strings as an *implementation
detail*, so `is` *sometimes* accidentally works — but it is **not guaranteed**. `a = 10_000_000;
c = 5_000_000 + 5_000_000; a is c` is **False** while `a == c` is True. Never use `is` on ints/strs.
*Source: FAQ "is vs ==" (explicit example + "not guaranteed to be singletons"). Verified 2026-06-16.*

## M4 — "A mutable default argument is created fresh on every call." `[settled]`
Wrong model: `def f(x, acc=[]):` gives a new empty list each call.
Correct: **default values are created exactly once, when the function is *defined*.** A mutable
default (`[]`, `{}`) is **shared across all calls** and accumulates state. Fix: default to `None`
and create inside (`if acc is None: acc = []`). *Source: FAQ "Why are default values shared between
objects?" Verified 2026-06-16.*

## M5 — "Python passes by value" / "Python passes by reference." `[settled]`
Wrong model: pick one of the two C-style answers.
Correct: **arguments are passed by assignment** ("call by object sharing"). The parameter name is
*bound to the same object* the caller passed. **Rebinding** the parameter (`x = [4,5]`) doesn't
affect the caller; **mutating** a shared mutable object (`x.append(4)`) does. *Source: FAQ "call by
reference?" Verified 2026-06-16.*

## M6 — "Type hints make Python check types at runtime." `[settled]`
Wrong model: `def f(n: int)` raises if you pass a str.
Correct: **annotations are not enforced at runtime** — Python ignores them for execution; they live
in `__annotations__` for *external* tools (mypy/pyright). "Python will remain a dynamically typed
language." *Source: PEP 484. Verified 2026-06-16.*

## M7 — "Indentation is just style; braces would do the same." `[settled]`
Wrong model: whitespace is cosmetic.
Correct: **indentation is syntax** — it delimits blocks (the role braces play elsewhere). Wrong
indentation changes meaning or raises `IndentationError`/`TabError` (don't mix tabs and spaces).
*Source: Language Reference (lexical/compound statements); PEP 8 (4 spaces). Verified 2026-06-16
(PEP 8).*

## M8 — "`if x:` checks whether x equals True / exists." `[settled]`
Wrong model: only booleans go in an `if`.
Correct: **any object has a truth value.** Falsy: `None`, `False`, numeric zeros (`0`, `0.0`, `0j`),
and **empty** sequences/collections (`''`, `()`, `[]`, `{}`, `set()`, `range(0)`); everything else
is truthy. Determined by `__bool__` then `__len__`. So `if mylist:` means "non-empty," not
"defined." *Source: Library Reference "Truth Value Testing." Verified 2026-06-16.*

## M9 — "`/` does integer division like in C/Java." `[settled]`
Wrong model: `5 / 2 == 2`.
Correct: in Python 3, **`/` is true division and always returns a float** (`5 / 2 == 2.5`);
**`//` is floor division**, "always rounded towards minus infinity" — docs' own examples: `1//2`
is `0`, `(-1)//2` is `-1`. So `-5 // 2 == -3`. *Source: Library Reference stdtypes (numeric ops),
verified 2026-06-16.*

## M10 — "Underscore-prefixed names are private and enforced." `[settled]`
Wrong model: `_x` / `__x` can't be accessed from outside.
Correct: *"'Private' instance variables that cannot be accessed except from inside an object don't
exist in Python."* A single `_name` is a *convention* ("non-public part of the API"); a double
`__name` is **textually replaced with `_classname__name`** (name mangling, to avoid subclass
clashes) but is still reachable. Encapsulation is by convention, not enforcement.
*Source: Tutorial "Classes" (private variables), verified 2026-06-16.*

## M11 — "A tuple is just a constant/immutable list." `[settled]`
Wrong model: tuple = frozen list, same role.
Correct: tuples are immutable, but idiomatically they signal **heterogeneous, fixed-structure
records** (position has meaning, like a row), while lists signal **homogeneous, variable-length
sequences**. Also: a tuple is immutable but can *contain* mutable objects, so it isn't necessarily
hashable. *Source: Language Reference §3 (immutability nuance: immutable container of mutables);
glossary. Verified 2026-06-16 (the immutability nuance).*

## M12 — "Closures capture the *value* a variable had when the closure was created." `[settled]`
Wrong model: a `lambda`/function defined in a loop freezes the loop variable's current value.
Correct: closures capture the **variable (the binding), not the value** — the name is looked up
**when the closure is called**, not when defined. All closures from a loop see the *final* value.
Fix: bind per-iteration via a default arg (`lambda n=x: ...`). *Source: FAQ "Why do lambdas defined
in a loop... all return the same result?" Verified 2026-06-16.*

## M13 — "If I assign to a name in a function, I'm modifying the outer/global one." `[settled]`
Wrong model: `count = count + 1` inside a function updates the global `count`.
Correct: **assigning a name anywhere in a function makes it local for the whole function** → reading
it first raises `UnboundLocalError`. To rebind an outer name, declare `global` (module level) or
`nonlocal` (enclosing function). *Source: Language Reference §4 (local-by-assignment rule + example).
Verified 2026-06-16.*

## M14 — "`import`ing a module again re-runs it." `[settled]`
Wrong model: each `import` executes the module's code.
Correct: a module's top-level code runs **once**, on first import; *"the first place checked during
import search is `sys.modules`… a cache of all modules previously imported"* — if present, that
cached object satisfies the import. This is why side-effects fire once and `if __name__ ==
"__main__":` guards run-as-script code. *Source: Language Reference "The import system", verified
2026-06-16.*

## M15 — "Mutating a list while iterating over it is fine." `[settled]`
Wrong model: you can `for x in lst: lst.remove(x)`.
Correct: adding/removing items from a collection during iteration corrupts the iterator (skips
items / `RuntimeError: dictionary changed size during iteration`). Iterate a copy (`for x in
lst[:]`) or build a new collection (comprehension). *Source: follows from the iterator protocol
(glossary, verified 2026-06-16) + Library Reference stdtypes mutation-during-iteration behavior.*

---

### Maintenance
New misconceptions surface **from teaching** (protocol §10: teaching is the base's stress test).
When the learner reveals a wrong model not listed here, add it with date + source/confidence and
note it in `CHANGELOG.md`. **All M1–M15 are now verified `settled` against primary python.org
sources** (the complete deep dive, 2026-06-16) — no entry is left on recall or "verify-later."
