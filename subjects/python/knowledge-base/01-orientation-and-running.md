# U1 — Orientation: what Python is & how code runs (deep notes)

> Deep pass 2026-06-16. The framing unit. Mechanism-first, confidence-marked. Light on syntax —
> its job is to install the correct mental model of *what is happening* before any real code.

## A. What Python is (and isn't)
- **High-level, general-purpose, dynamically typed, interpreted** language; reference implementation
  **CPython**. `[settled — python.org]`
- **Interpreted, but via bytecode:** CPython **compiles** your source to **bytecode** (`.pyc`), then
  a **virtual machine** evaluates it. So "interpreted" doesn't mean "executed line-by-line from
  text" — there's a compile step, just an implicit/fast one. `[settled — glossary "bytecode";
  runtime/VM depth → U14 (covered to working-professional level there)]`
- **Dynamically typed:** types live on **values (objects)**, not on names. A name can refer to an
  int now and a str later. Type errors surface at **runtime**, when an operation meets an
  unsupported object. `[settled — follows from Language Reference §3/§4]`

## B. How you run it (the three modes a beginner meets)
- **REPL** (interactive `>>>`): type an expression, it's evaluated and the result **echoed**. The
  REPL auto-prints expression results; a *script* does not (you must `print`). This distinction
  confuses beginners — name it. `[settled]`
- **Script:** `python file.py` runs the file top to bottom. `[settled]`
- **Notebook / IDE:** same engine, different shell. (Tooling specifics → U14.)

## C. The smallest correct mental model (seed for T1, fully taught in U3)
- Running a program = **creating objects** and **binding names** to them, then asking objects to do
  things. Even at "hello world": the string `"hello"` is an **object**; `print` is an **object** (a
  function) you call. `[settled — Language Reference §3 "all data… is objects"]`
- Plant the flag now: *Python has no "boxes." Names point at objects.* Don't fully unpack yet — U3
  does — but never teach a box model even loosely, because U3/U5 must un-teach it.

## D. Readability is a feature, not etiquette
- **Indentation is syntax** (delimits blocks). `[settled — misconception M7]`
- The language is opinionated toward one clear way (PEP 20, taught fully U12). Mentioning it early
  sets the expectation that "Pythonic" is a real standard, not vibes. `[settled — PEP 20]`

## What the engine teaches from this
Open with retrieval of any prior programming exposure (diagnose!). Get them running code (REPL +
one script) fast — concrete first. Seed the "names point at objects" idea but **defer the depth to
U3**. Watch for an imported box/variable model from prior languages; flag it for T1.

## Confidence / gaps
Core claims `settled`. Bytecode/VM internals deferred to U14 (glossary-depth only here). Learner's
prior-programming background is `open` until session 1.
