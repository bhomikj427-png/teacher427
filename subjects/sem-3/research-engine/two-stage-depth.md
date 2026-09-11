# Two-Stage Depth — how deep the research engine goes, and when

> This file defines the **two depth targets** the autonomous researcher builds each subject to.
> It does **not** relax `../../../subject-research-protocol.md` — every claim in *either* stage
> still must be sourced, triangulated when load-bearing, confidence-marked, and mechanism-stated,
> with **no hallucinated specifics**. The stages differ only in **scope and depth target**, never
> in honesty. (Recall: the researcher is a model; recall ≠ sourced. Verify load-bearing claims
> against a real external source *this session* — protocol §1.)

The whole point: a subject is useful to a MUJ student long before it is researched to expert
depth. So we lock in **exam-ready coverage of the official syllabus first** (Stage 1), across the
*whole batch*, then come back and deepen each subject to the **generative deep structure** an
expert reasons from (Stage 2). Stage 2 is built **on top of** Stage 1, never instead of it.

---

## Per-subject status values (used by `research-queue.md`)

```
stage-0   scaffold only — course-info.md seeded, knowledge-base/ empty
stage-1   Stage-1 (MUJ level) in progress
stage-1✓  Stage-1 complete — every official unit covered to exam-ready depth
stage-2   Stage-2 (IIT/Ivy level) in progress
stage-2✓  Stage-2 complete — deep structure + frontier, §0 surplus test passed
```

**Teaching requires a COMPLETE knowledge base — `stage-2✓`. This is a hard gate (learner-set
rule): never teach a subject before *both* stages are done.** Teaching from an incomplete base
defeats the entire purpose of the system — the tutor must teach from a researched, verified
overflow, not a half-built one. So:
- `stage-1✓` is the **breadth-first research milestone** (every subject reaches exam-ready before
  anyone is deepened) and the clean exam-revision set — but it is **not** the teaching gate.
- A subject becomes **teach-ready only at `stage-2✓`** (both stages complete, §0 surplus test
  passed). "Break it into two passes" (Stage 1 then Stage 2) is *how* the base is built when one
  pass is too big — not permission to teach after only the first.
- **On-demand override:** when the learner activates a subject for teaching, bring *that* subject
  to `stage-2✓` ahead of the breadth-first queue (depth-first for the activated subject), then
  teach. Scoring-over-depth still governs the *teaching order* (lead with exam-relevant material),
  but only once the full base exists.

---

## STAGE 1 — MUJ level (exam-ready, syllabus-complete)

**Definition of done:** *Every topic in the official MUJ syllabus unit list is covered to the depth
of the prescribed textbooks — enough that a strong MUJ student could score top marks, solve any
tutorial/exam problem from the syllabus, and explain the mechanism behind each result.*

**Anchor.** The subject's `course-info.md` — the official unit list + prescribed textbooks. Stage 1
is *bounded by the official syllabus*: cover all of it, don't wander past it yet.

**Sources (tier order, protocol §2).**
1. **Prescribed textbooks** named in `course-info.md` (Boylestad, Oppenheim & Willsky, Van
   Valkenburg, Gayakwad, Sedra-Smith, etc.) — these *are* the tier-1 ground for **content truth.**
2. The **official MUJ syllabus / course handout** (defines scope, not truth).
3. Reputable course material for triangulation: **NPTEL, MIT OCW** lecture notes, standard problem
   sets. Use to confirm, not as the final word.

**Exam-aiming inputs — PYQs & PPTs (the "aim for marks" lever).** See `exam-resources.md`. Stage 1
targets the *actual MUJ exam* (MTE + ETE), so it is **driven by previous year papers and the course
PPTs**, with a strict split of purpose (the honesty rule):
- **PYQs / course PPTs are TIER-1 for *what is tested, in what form, with what emphasis*** — a past
  paper is the authoritative artifact for the exam's question types, recurring topics, and topic
  weightage; a course PPT is primary evidence for the instructor's emphasis, notation, and scope
  cuts. Use them to decide **what to cover and how it's asked.**
- **PYQs / PPTs / toppers' notes are TIER-3/4 for *what is true*** — answer keys and notes contain
  errors. **Never let a PYQ key or a PPT bullet set a fact.** Verify every content claim against the
  prescribed textbook (source 1), then attach the verified content to the pattern the PYQ revealed.
- Files live in `NN-subject/exam-pack/` (you drop them) — see `exam-resources.md` "Manual drop."

**Depth target.** "Prescribed-textbook level + enough surplus to teach." For each official topic:
- State the **mechanism**, not just the result ("X causes Y via Z").
- Carry the **standard derivation / problem method** the exam expects (e.g. find Thevenin
  equivalent; take a Laplace transform and solve; bias a MOSFET; design a 2nd-order active filter).
- Capture the **canonical worked-problem patterns** for that unit (the question types that recur).
- Surplus here is modest (~2–3× the exam) — deliberately. The 10× surplus is Stage 2's job.

**Artifacts produced (per subject, in `knowledge-base/`):**
- `00-map.md` — big ideas, **prerequisite graph** + **threshold concepts** (triangulated to full
  standard even in Stage 1 — protocol §8: prereq edges are load-bearing), scope = the official
  units, and the standing **Open questions / to-verify** register.
- `exam-map.md` — **the marks-aiming map, built from the PYQs/PPTs in `exam-pack/`:** per topic →
  how often it appears, the recurring **question types** (with marks), MTE-vs-ETE split, and the
  instructor's emphasis from PPTs. This is what makes Stage 1 *exam-targeted* rather than just
  *syllabus-complete*. Cite each pattern to the specific paper/PPT; mark `uncertain` if no PYQ is in
  hand yet. **Drives revision priority and the exit test below.**
- `<unit>.md` per official unit — mechanism-level notes, key formulas (verified exactly), standard
  derivations, worked-problem patterns, confidence marks. **Weighted by `exam-map.md`:** spend most
  depth on what the PYQs actually test.
- `misconceptions.md` — the predictable novice errors for this subject, **sourced** to discipline
  education / documented-error literature where possible; each one confidence-marked (protocol §4).
- `sources.md` — every source, tiered, dated, with confidence.
- `CHANGELOG.md` — correction audit trail (protocol §10 format).

**Stage-1 exit test.** Prefer **real PYQ questions** (from `exam-pack/`) over invented ones: pick
3–5 spanning the units — weighted toward the high-frequency topics in `exam-map.md` — and confirm
the base answers each **from mechanism**, with the method shown, citing a prescribed text. If no PYQ
is in hand, use representative textbook/tutorial problems and flag that the exam-targeting is
unconfirmed. If a unit can't pass this, it is not `stage-1✓`.

---

## STAGE 2 — IIT / Ivy League level (deep structure + frontier)

**Definition of done:** *The base carries the generative deep structure an expert reasons from —
the §0 "10× surplus." It could support a graduate-level treatment, survive a top-school qualifier
on the topic, and it knows where the undergraduate textbook simplifies or lies.*

**Built on top of Stage 1, but stored separately.** Stage 2 **extends** Stage 1 — it must not edit
or clutter the exam-ready Stage-1 files. It is written to a separate `knowledge-base/stage-2/`
folder (see "Where the two stages live," below), so the learner can finish exam prep from the clean
Stage-1 set and only then open the depth.

**Sources (tier order climbs to primary).**
1. **Primary / foundational** — Sze & Ng *Physics of Semiconductor Devices*, Streetman & Banerjee,
   Razavi, graduate Oppenheim/Proakis, Van Valkenburg advanced network synthesis, original
   papers, IEEE standards, **MIT OCW graduate courses, advanced NPTEL**, canonical monographs.
2. **Authoritative secondary** — respected graduate surveys/reviews, expert-consensus references.
3. Triangulate anything load-bearing across **≥2 independent** tier-1 sources (protocol §5).

**What Stage 2 adds (the deep-structure checklist):**
- **First-principles derivations & proofs** — derive the results Stage 1 merely *stated* (e.g.
  derive the diode equation from carrier statistics; prove convolution = LTI output; derive the
  positive-real condition for network synthesis).
- **Assumptions & limits of every model** — where the standard model breaks, what it approximates,
  the regime of validity ("ideal op-amp fails when…", "small-signal model assumes…").
- **Where the UG textbook simplifies or lies** — explicitly flag the white lies (e.g. "depletion
  approximation," "ideal switch," "the textbook's hand-wave at short-channel effects").
- **Cross-topic unification** — the connections an expert sees: Laplace↔Fourier↔z; network
  functions ↔ stability ↔ control; MOSFET physics ↔ digital logic families ↔ VLSI scaling.
- **Contested / evolving frontier** — modern device physics (FinFET/GAA), modern DSP, current
  research directions; teach live debates as debates (protocol §4).
- **Harder problem classes** — GATE-advanced, grad-qualifier, and conceptual "why not what"
  questions; edge cases and counterexamples.
- **History / why-it's-built-this-way** — the design rationale, not just the design.

**Stage-2 exit test (the §0 surplus test, by *output* not feeling).** Generate several
expert-level / edge-case / "why, not what" questions for the subject and confirm the base answers
each **from mechanism, with primary sources**. Work the Open-questions register down. An empty
register usually means you stopped looking, not that you're finished (protocol §10).

---

## What is identical across both stages (never compromised)

- Sourced, not recalled. Triangulated when load-bearing. Confidence-marked. Mechanism-stated.
- No hallucinated specifics — unsure → say so, flag to the register.
- Confidence markers survive into anything derived/taught (protocol §9): a `contested`/`uncertain`
  claim stays flagged, never flattened.
- The base is **living** (protocol §10): confidence moves both ways; corrections are logged to
  `CHANGELOG.md`; the to-verify register is worked down.

## Where the two stages live — PHYSICALLY SEPARATE (study exams first, then depth)

The two stages live in **different places**, on purpose, so exam study is never cluttered by depth:

```
NN-subject/
└── knowledge-base/
    ├── 00-map.md            ┐
    ├── 01-<unit>.md         │  STAGE 1 — the clean, exam-ready set.
    ├── 02-<unit>.md         ├─ Open this folder to study for the MUJ exam: everything here
    ├── misconceptions.md    │   is Stage-1 (MUJ level), nothing deeper.
    ├── sources.md           │
    └── CHANGELOG.md         ┘
    └── stage-2/             ┐  STAGE 2 — the deep dive, tucked one level down.
        ├── 01-<unit>.md     ├─ Mirrors the Stage-1 unit files (same numbering/titles), but holds
        ├── 02-<unit>.md     │   the first-principles / limits / unification / frontier material.
        └── sources.md       ┘   Built only after Stage 1; created when Stage 2 runs.
```

**Rules that make "exams first, then depth" work:**
- Stage-1 unit files stay **exam-only** — Stage 2 work **never edits them** and never adds depth
  into them. So when you're revising for the exam, the top-level `knowledge-base/` is exactly your
  syllabus, nothing more.
- Stage 2 lives entirely in `stage-2/`, a mirrored set of unit files. Want depth on a unit? Open
  `stage-2/<same-unit>.md`. Ignore the folder entirely while exam-prepping.
- Each Stage-1 unit file ends with a **one-line pointer** to its `stage-2/` counterpart (and lists
  what Stage 2 *will* add), so you always know depth exists without it intruding.
- Shared artifacts: `00-map.md`, `misconceptions.md`, `CHANGELOG.md` stay single (the map and
  misconception list serve both); Stage 2 may keep its **own** `stage-2/sources.md` for the
  primary/graduate sources it pulls, leaving the Stage-1 `sources.md` clean.
