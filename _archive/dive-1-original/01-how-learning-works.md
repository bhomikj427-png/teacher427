# 01 — How Learning Works (Cognitive Architecture)

Every technique in `02` is a consequence of how human memory is built. Understand this and
the techniques stop being a list to memorize and become *derivable*.

## 1. The two-store model: working memory vs. long-term memory

**Working memory (WM)** is where conscious thought happens. It is severely limited:

- Holds only ~**4 ± 1** novel elements at once (Cowan's estimate; the older "7 ± 2" from
  Miller is now considered an overcount for genuinely novel items).
- Information decays in **seconds** without rehearsal.
- This bottleneck is the single biggest constraint on learning. Overload it and learning stops.

**Long-term memory (LTM)** is effectively unlimited and durable. Expertise *is* large,
well-organized LTM. Crucially, LTM **expands working memory's effective capacity**: an expert
chess player sees "a board position" (one chunk) where a novice sees 20 separate pieces. The
expert isn't smarter in WM terms — they have *schemas* in LTM that do the chunking.

> **Implication:** The goal of teaching is to build organized **schemas** in LTM, while never
> overloading the fragile WM bottleneck during the process.

## 2. Cognitive Load Theory (Sweller)

Total load on WM has three sources:

- **Intrinsic load** — the inherent difficulty of the material (how many elements interact at
  once). A novice can't reduce it except by building schemas; a teacher can *sequence* it.
- **Extraneous load** — load imposed by *poor presentation* (clutter, split attention,
  redundancy, searching for information). This is wasted and must be minimized.
- **Germane load** — the productive effort of actually building schemas. This is what we want
  WM capacity spent on.

**The teaching levers that follow directly:**
- Cut extraneous load ruthlessly (clean explanations, no decorative noise).
- Manage intrinsic load by sequencing — teach prerequisites first, isolate elements before
  combining them (the "isolated/interacting elements" effect).
- Spend the freed capacity on germane load (retrieval, self-explanation, connection-building).

Reference: Sweller; Paas & van Merriënboer (2020). Note: CLT has been refined over time and
is best treated as a robust *framework* rather than a precise predictive model.

## 3. The expertise reversal effect

What helps a novice can *hurt* an expert, and vice versa. Worked examples and heavy guidance
help novices (they lack schemas to guide problem-solving) but become redundant — even
harmful — for experts (the guidance conflicts with existing schemas, adding extraneous load).

> **Implication:** Instruction must adapt to the learner's current level. This is why the
> engine *diagnoses before it teaches* — the right move depends entirely on where the learner is.

## 4. Storage strength vs. retrieval strength (Bjork & Bjork, "New Theory of Disuse")

A memory has two independent strengths:

- **Storage strength** — how deeply learned/durable it is. Essentially only grows.
- **Retrieval strength** — how accessible it is *right now*. Rises fast and falls fast.

The counterintuitive payoff: **conditions that make retrieval feel easy now (massing,
rereading) produce little durable storage. Conditions that make retrieval feel hard now
(spacing, testing, interleaving) build storage strength.** Performance during practice is a
*misleading* indicator of learning.

This is the theoretical engine behind "desirable difficulties."

## 5. Desirable difficulties (Bjork)

Difficulties that *enhance* long-term learning when introduced during study:

- **Retrieval practice** (testing yourself rather than reviewing)
- **Spacing** (distributing study over time)
- **Interleaving** (mixing problem types rather than blocking)
- **Varying conditions** of practice
- **Generation** (producing an answer before being shown it)

They are "desirable" because they slow apparent progress while *increasing real, durable
learning and transfer*. They are still difficulties — push too far past the learner's ability
and they stop being desirable. Calibration matters.

## 6. The fluency illusion (why learners mis-judge themselves)

Re-reading and watching an expert make material feel *familiar and fluent*. Learners
misread this fluency as mastery and stop studying too early. This is the **single most common
self-sabotage in learning**, and it is why subjective confidence is a poor guide and why the
engine relies on *retrieval-based evidence* of understanding, not the learner's say-so.

## 7. Forgetting is the default

Ebbinghaus's forgetting curve: newly learned material decays rapidly without reinforcement.
Forgetting is not failure — it is the normal operation of memory. The job of instruction is
not to prevent forgetting in one pass but to schedule **retrieval at expanding intervals** so
each successful effortful recall flattens the curve. (This is the basis of spaced repetition
systems like Leitner boxes / SM-2 algorithms.)

## Summary: the chain of reasoning

```
WM is tiny and fragile  ─┐
LTM schemas chunk info   ─┼─►  manage cognitive load + build schemas
                          │
Storage ≠ retrieval      ─┼─►  make retrieval effortful (desirable difficulties)
strength                  │      → retrieval practice, spacing, interleaving, generation
                          │
Fluency ≠ learning       ─┴─►  trust retrieval evidence, not the feeling of knowing
Forgetting is default    ────►  schedule expanding-interval review
```

Everything in `02` is just this chain, made concrete.
