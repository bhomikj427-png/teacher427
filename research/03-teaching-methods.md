# 03 — Teaching Methods (How to Sequence Instruction)

`02` is what the *learner* does; this is how the *teacher* sequences and delivers. Carries over
Dive 1's methods, adds the productive-failure reconciliation, and keeps the de-mythologized
tutoring numbers.

---

## 1. Explicit / direct instruction — Rosenshine's Principles

Rosenshine (2012) distilled **ten principles** from three converging sources (cognitive science,
master-teacher observation, tutoring research) — the convergence is what gives it weight:

1. Begin with a short **review** of prior learning (spacing + retrieval).
2. Present new material in **small steps**, with practice after each (respects WM limits).
3. Ask a **large number of questions**; check all responses.
4. Provide **models** / worked examples.
5. **Guide** initial practice.
6. **Check for understanding** frequently.
7. Aim for a **high success rate (~80%)** in guided practice.
8. Provide **scaffolds** for hard tasks; fade them.
9. Require **independent practice** toward fluency/automaticity.
10. **Weekly and monthly review** (spacing).

**Scope (honest):** strongest for mastering a defined body of knowledge or a clear-step
procedure. *Unguided* discovery for novices is poorly supported (no schemas to discover with).

## 2. Scaffolding & the Zone of Proximal Development (Vygotsky)

Teach in the band just beyond independent ability but reachable **with support**. Scaffolds
(hints, partial solutions, structure) are **temporary** and withdrawn as the skill is
internalized — the pedagogical sibling of guidance fading and the ~80% calibration.

**Apply:** find the edge of current ability, pitch tasks just beyond it, give the **minimum hint**
that keeps them moving (not the answer), withdraw support as they succeed.

## 3. Mastery learning (Bloom)

Require demonstrated mastery (~80–90% on a formative check) **before** progressing; non-masters
get corrective instruction and re-test. The bar is fixed; time varies. Modern effects are more
modest than Bloom's original ~1σ, but the logic — *don't build on a shaky foundation* — is sound
and complements CLT (no higher schema on missing prerequisites). Pairs naturally with **successive
relearning** (`02 §3`).

## 4. Tutoring & Bloom's "2 sigma" — myth corrected

Bloom (1984) reported ~**2 SD** for 1:1 tutoring. The honest current picture:
- Modern randomized meta-analysis (Nickow, Oreopoulos & Quan, 2020): average ≈ **0.37 SD**;
  **none of 96 studies reached 2σ.**
- Intelligent tutoring systems (VanLehn): **d ≈ 0.76**, near human tutoring's **d ≈ 0.79**.

**Takeaway:** the mythic 2σ is *not* reliably reproduced — but tutoring's *real* effect
(~0.4–0.8 SD) is still among the most powerful interventions known. A 1:1 adaptive tutor (this
engine) operates in the best-evidenced format there is. **Claim the realistic number, not the
legend** — and note this shrinkage is the same effect-size-inflation story as `07`.

## 5. The worked-example ↔ productive-failure reconciliation (key decision rule)

These look contradictory: worked examples say **instruct first**; productive failure says
**struggle first**. They are not — they serve **different goals**:

| Goal | Best opening move | Why | Evidence |
|---|---|---|---|
| **Procedural fluency** (execute a method) | **Worked example first** (instruct → practice) | Problem-solving first overloads novice WM with means-ends search | Worked-example effect (`02 §7`) |
| **Conceptual understanding & transfer** (grasp *why*) | **Productive failure first** (attempt → instruct) | The failed attempt reveals the knowledge gap and primes the learner to encode the principle | Sinha & Kapur 2021 (`02 §5`) |

**Decision rule for the engine:** ask *"is the objective to perform a procedure, or to understand
a concept?"* Procedure → show, then fade. Concept/transfer → let them attempt and fail
productively (briefly, supported), then instruct. This also tracks the assistance dilemma (`04`):
don't rescue conceptual struggle too early; do scaffold procedural acquisition.

## 6. Socratic questioning / guided discovery — where it fits

Its benefit comes from the **retrieval, generation, and self-explanation** it forces (`02`), not
"discovery" itself. It works **when the learner has prior knowledge to reason from**; for true
novices it collapses into guessing and overload. Use it to *activate and extend* existing
knowledge; lead with explicit instruction + worked examples when there's no foothold yet.

## 7. The synthesized instructional sequence

```
1. ACTIVATE   → spaced review of prior material + predict/attempt (generation/pretesting)
                → DIAGNOSE level here
2. ROUTE      → procedure? → worked example first.   concept/transfer? → productive failure first.
3. PRESENT    → small steps, low extraneous load, words + clean visual; concrete → fade to abstract
4. MODEL      → worked example + think-aloud; learner self-explains it
5. GUIDE      → completion problems + heavy questioning; minimum hint; ~80% success
6. CHECK      → retrieval-based; probe Apply/Analyze, not just Recall; gate on mastery
7. TEACH-BACK → learner explains/teaches it back (protégé effect)
8. FADE       → withdraw scaffolds; independent practice toward fluency
9. INTERLEAVE → once several skills are solid, mix them (block first!)
10. RELEARN   → schedule successive relearning at expanding, across-night intervals
```

Every step traces to an evidenced principle (cited in `01`–`02`). Trivial material collapses the
loop, but the shape — *activate → make them generate/retrieve → check → schedule relearning* — is
always present.
