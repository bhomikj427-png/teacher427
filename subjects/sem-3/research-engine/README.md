# research-engine — autonomous, batch-wise subject researcher

This folder is a **self-driving researcher** for the Sem-3 batch. Point a fresh terminal at it and
it builds every subject's `knowledge-base/` to standard — **no input from the learner required.**

It does not invent method or relax the bar. It is an *orchestrator* that runs the existing subject
standard (`../../../subject-research-protocol.md`) across many subjects, to two escalating depths.

## The files

| File | Role |
|------|------|
| `AUTONOMOUS-RUN.md` | **Start here.** The fresh-terminal entrypoint: kickoff prompt + the work loop + the selection policy + the stop condition. |
| `two-stage-depth.md` | The two depth targets — **Stage 1 (MUJ level)** and **Stage 2 (IIT/Ivy level)** — with done-criteria and exit tests. |
| `exam-resources.md` | The PYQ/PPT student portals + the **honesty rule** (exam-targeting vs truth) + MTE/ETE structure. Makes Stage 1 aim for marks. |
| `research-queue.md` | The **live tracker**: per-subject status, priority order, parked items, open questions. Read first, updated as work happens. |
| `README.md` | This overview. |

## What "autonomous" and "batch-wise" mean here

- **Autonomous** — every decision the researcher would otherwise ask about is pre-specified: what
  to do next (the queue's priority order), how deep (the two stages), the bar (the protocol), and
  what to do when blocked (park it, log why, move on). It never needs the learner.
- **Batch-wise** — it treats all Sem-3 subjects as one batch and goes **breadth-first**: every
  subject to `stage-1✓` (exam-ready) *before* any subject is deepened to Stage 2. So the learner
  gets every course usable first, then each gets excellent.

## The bar (inherited, non-negotiable)

Everything written obeys `../../../subject-research-protocol.md`: sourced (not recalled),
triangulated when load-bearing, confidence-marked, mechanism-stated, **no hallucinated specifics**,
living/self-correcting. The researcher is a model — it verifies load-bearing claims against real
external sources *in-session* (web tools), and marks anything it can't verify `uncertain` + logs it
to the to-verify register rather than presenting recall as fact.

## Relationship to teaching

Research fills `knowledge-base/`. **Teaching** is separate and needs the learner — it adds
`curriculum.md` / `learner-profile.md` / `progress-log.md` and runs the `../../../CLAUDE.md` loop.
A subject is teachable **only once it reaches `stage-2✓`** — a *complete* base, both stages
(learner-set hard gate, `two-stage-depth.md`). `stage-1✓` is exam-ready and the breadth-first
research milestone, but the engine **never teaches from a partial base** — that defeats the system.
On activation, an under-researched subject is taken depth-first to `stage-2✓` before teaching.
