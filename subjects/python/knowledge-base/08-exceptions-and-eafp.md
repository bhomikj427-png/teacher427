# U8 — Exceptions & the EAFP mindset (deep notes) ★ Threshold T6

> Deep pass 2026-06-16. Primary source: official glossary (EAFP/LBYL) verified 2026-06-16. The
> mindset shift: in Python, exceptions are *normal control flow*, not just catastrophe handling.
> Threshold T6.

## A. The mechanism
- An error **raises an exception object**; it propagates up the call stack until a matching
  `except` catches it, else the program stops with a traceback. Exceptions are **objects** with a
  class hierarchy (rooted at `BaseException`; catch `Exception` for normal errors). `[settled —
  exception hierarchy standard/uncontested (BaseException root)]`
- `try / except [as e] / else / finally`: the `else` clause "is useful for code that must be
  executed if the try clause does not raise an exception"; the `finally` clause "will execute as the
  last task… whether or not the try statement produces an exception." Catch **specific** exceptions,
  not bare `except:`. `[settled — tutorial/errors, verified 2026-06-16]`
- `raise` to throw; **`raise X from cause`** for explicit chaining ("a direct consequence of
  another"; `from None` suppresses chaining); define custom exceptions by subclassing `Exception`
  ("either directly or indirectly," names usually end in `Error`). `[settled — tutorial/errors,
  verified 2026-06-16]`
- **Exception groups** (`ExceptionGroup` + `except*`, 3.11/PEP 654): wrap several exceptions raised
  together; `except*` selectively handles matching members and lets the rest propagate. `[settled —
  tutorial/errors, verified 2026-06-16; version-gated 3.11+, present in 3.14]`

## B. EAFP vs LBYL (the mindset, Big Idea #6) `[settled]`
- **EAFP** — "Easier to Ask Forgiveness than Permission": *assume* the key/attr/file exists and
  **catch the exception** if not. "Clean and fast… characterized by many `try`/`except`." `[settled —
  glossary, verified 2026-06-16]`
- **LBYL** — "Look Before You Leap": test preconditions with `if` first. Glossary notes LBYL "can
  risk introducing a race condition between the looking and the leaping" in multi-threaded/IO cases
  (the thing might change between check and use). `[settled — glossary, verified 2026-06-16]`
- Python **prefers EAFP** for many cases (e.g. `try: d[k] except KeyError:` over `if k in d`),
  partly for the race-condition reason, partly for clarity. It's a *judgment*, not a law — teach
  when each fits. `[settled — glossary; contested-by-design which to use when]`

## C. Exceptions are part of the protocols
- `StopIteration` ends iteration (U7); `KeyError`/`IndexError`/`AttributeError` drive lookups;
  context managers (U12) use exceptions for cleanup. So exceptions aren't a bolt-on — they're woven
  into the data model. `[settled — glossary StopIteration; cross-ref U7]`

## D. Bites
- Bare `except:` swallowing everything (incl. `KeyboardInterrupt`) — violates Zen "errors should
  never pass silently." Catching too broadly; using exceptions for ordinary conditionals where a
  simple check is clearer. `[settled — PEP 20; standard guidance]`

## What the engine teaches from this
Reframe first (productive contrast): show an LBYL check with a TOCTOU-style hole, then the EAFP
version — the mindset is the threshold, the syntax is easy. Worked examples for try/except/else/
finally ordering (have them predict what prints when an exception fires mid-`try`). Tie
`StopIteration` back to U7.

## Confidence / gaps
EAFP/LBYL `settled` at glossary; try/except/else/finally, `raise from`, custom exceptions, and
exception groups `settled` at tutorial/errors (verified 2026-06-16). No open items.
