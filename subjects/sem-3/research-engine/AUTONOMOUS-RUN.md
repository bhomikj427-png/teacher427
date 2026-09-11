# AUTONOMOUS-RUN — start (or resume) the batch researcher from a fresh terminal

> **Purpose.** Let any fresh Claude session research the Sem-3 subjects autonomously, to the two
> depths in `two-stage-depth.md`, **with zero further input from the learner.** Everything needed
> to decide *what to do next* is in `research-queue.md`; everything about *how deep* is in
> `two-stage-depth.md`; everything about *the bar* is in `../../../subject-research-protocol.md`.

---

## To start it: paste this into a fresh terminal

```
Run the Sem-3 autonomous research engine. Read
subjects/sem-3/research-engine/AUTONOMOUS-RUN.md and follow the loop. Do not ask me anything —
all decisions are specified. Work the research-queue until you hit the stop condition, updating
it live, then report what you completed.
```

That is the entire kickoff. No other instruction is required. (Optional: wrap it in the `/loop`
skill to have it self-pace across many turns.)

---

## Boot sequence (every session, before any research)

1. **Load the contract & standards** (they may not all be auto-loaded):
   - `../../../CLAUDE.md` — the engine's operating contract (auto-loaded).
   - `../../../subject-research-protocol.md` — the evidentiary bar. **The whole job obeys this.**
   - `two-stage-depth.md` — the Stage 1 / Stage 2 depth targets and done-criteria.
   - `exam-resources.md` — the PYQ/PPT portals + the **honesty rule** (exam-targeting vs truth) +
     the MTE/ETE structure. Stage 1 aims for marks, so this governs the exam-aiming inputs.
   - `research-queue.md` — current per-subject status and the next action.
2. **Confirm web tools are available** (`WebSearch`, `WebFetch`). They are required: the protocol
   forbids promoting load-bearing claims past `uncertain` on recall alone (§1). If web tools are
   unavailable this session, you may still draft from prescribed textbooks but **must** mark every
   recalled specific `uncertain` and log it to the unit's to-verify register — never present recall
   as verified.

## Inbox triage (run FIRST, before the work loop)

If `../_inbox/` contains any files (beyond its `README.md` / `TRIAGE-LOG.md` / empty `_unsorted/`),
run the triage routine in `../_inbox/README.md` before anything else:
- For each file: read it (`pdftotext` for text PDFs, `unzip` for `.pptx`, view images directly),
  identify which of the 10 Sem-3 subjects it belongs to, **move** it into that subject's
  `exam-pack/`, and append a line to `../_inbox/TRIAGE-LOG.md`.
- Can't classify confidently → move to `_inbox/_unsorted/` and log it asking the learner to confirm.
  **Never guess-file into the wrong subject.**
- Then rebuild `knowledge-base/exam-map.md` for any subject that gained material.

Triage only routes/reads; it never promotes a file's claims to truth (the honesty rule still holds).

## The selection policy (how "what next" is decided — no user input)

Read `research-queue.md` and pick the next work item by this **fixed priority** (breadth-first —
"batch-wise"):

1. **Bring the whole batch to `stage-1✓` before deepening anyone to Stage 2.** Among subjects not
   yet `stage-1✓`, take them in the queue's listed order (01 → 10). Skip subjects marked
   `parked` (see below). This guarantees every course is exam-ready before any goes deep.
2. **Then** deepen subjects to Stage 2, again in listed order, until `stage-2✓`.
3. Within a subject, do units in the order set by its `00-map.md` prerequisite graph (prereqs
   first). If `00-map.md` doesn't exist yet, the **map pass is the first work item** for that
   subject (protocol §8: map first — and triangulate the prereq graph + threshold concepts to full
   standard during the map pass, even while leaf detail waits).

**Teaching gate & on-demand override.** A subject is **teach-ready only at `stage-2✓`** (complete
base, both stages — learner-set rule in `two-stage-depth.md`); the engine never teaches from a
partial base. The breadth-first order above is for *autonomous background building*. But **the
moment the learner activates a subject for teaching, that subject jumps the queue and is taken
depth-first to `stage-2✓`** (Stage 1 then Stage 2, back-to-back) before teaching begins — don't
make them wait for the whole batch's Stage 1.

**Parked subjects.** `02-management-of-technology` *was* parked on a missing syllabus — **un-parked
2026-06-24** (code resolved MBB2101; official topic list found — see the queue's "Resolved un-park").
The **Flexi Core** pair `06`/`07` — research *both* (learner hasn't chosen), but they are lower priority than the
five always-taken cores (01, 03, 04, 05) and the labs. The queue encodes the exact order; follow
it. A subject becomes un-parked the moment its `course-info.md` open questions are resolved.

## The work loop (one item at a time)

For the selected `(subject, stage, unit)`:

1. **Set status** in `research-queue.md` to in-progress for that subject (live update).
2. **Read** the subject's `course-info.md` (official scope + prescribed textbooks), any existing
   `knowledge-base/` notes, and the subject's **`exam-pack/`** if present (dropped PYQs/PPTs).
   - For Stage 1, **build/refresh `knowledge-base/exam-map.md` first** from `exam-pack/`: topic →
     frequency, question types + marks, MTE/ETE split, PPT emphasis. Apply the **honesty rule**
     (`exam-resources.md`): PYQs/PPTs are tier-1 for *what/how it's tested*, tier-3/4 for *truth* —
     never let an answer key set a fact. If `exam-pack/` is empty, write the exam-map as `uncertain`
     and log "no PYQ in hand" to the to-verify register; proceed syllabus-driven. Optionally attempt
     the portal links in `course-info.md`, but don't block on them.
3. **Research to the stage's depth** (`two-stage-depth.md`), running the protocol's pass:
   - *Map pass* (if no `00-map.md`): big ideas, prerequisite graph, threshold concepts,
     misconception list seed, scope, source canon → write `00-map.md` + start `sources.md`.
     Triangulate prereq edges + threshold claims now (load-bearing).
   - *Deep pass* (per unit): run §1–§6 on that unit to the stage's target. **Use `WebSearch` /
     `WebFetch` to reach the prescribed textbook / primary source and verify every load-bearing
     specific** (formula, number, derivation, edge case). Triangulate across ≥2 independent sources
     for load-bearing claims.
4. **Write the artifacts** (mechanism-level, confidence-marked) — **Stage 1 and Stage 2 are stored
   in separate locations** (see "Where the two stages live" in `two-stage-depth.md`):
   - *Stage 1* → `knowledge-base/<unit>.md` (the clean exam-ready set). End each with a one-line
     pointer to its `stage-2/` counterpart.
   - *Stage 2* → `knowledge-base/stage-2/<unit>.md` (mirrored file). **Never edit the Stage-1 file
     to add depth** — exam material must stay uncluttered.
   - Update `misconceptions.md` + `sources.md` (Stage 2 may use its own `stage-2/sources.md`), and
     append any correction to `CHANGELOG.md`.
   - Anything you couldn't verify → the `00-map.md` **Open questions / to-verify** register.
5. **Run the stage exit test** for the unit/subject (the worked-problem test for Stage 1; the §0
   surplus "why not what" test for Stage 2). Only then mark the unit done.
6. **Update `research-queue.md` LIVE** — units done/total, status, `last-updated` date,
   `next-action`. This is the resume record: an abrupt exit must leave an exact, true position
   (same no-drift discipline as `progress-log.md`).
7. Loop to the next item per the selection policy.

## Stop condition

Stop and report when **any** of these is true:
- The queue is fully `stage-2✓` (or `stage-1✓` if Stage 2 was not requested this run).
- A blocking gap appears that genuinely needs the learner (e.g. a parked subject's official
  syllabus can't be located after a real search) — **park it, log why in the queue, and continue
  with the next subject.** Do not stop the whole run for one parked subject; do not invent a
  syllabus.
- You are running under a turn/loop budget that's exhausted — leave the queue accurate and stop.

On stop, write a short report: subjects advanced, stages reached, open questions opened, anything
parked and why.

## Hard "do nots" (inherited, restated for the autonomous context)

- **Do not ask the learner anything** — every decision is specified here or in the queue. If truly
  blocked on one subject, park it and move on.
- **Do not hallucinate** a syllabus, a citation, a number, or an edge case. Unsure → `uncertain` +
  to-verify register.
- **Do not present recall as sourced.** Reach the real source this session for load-bearing claims.
- **Do not skip the map pass** or sequence units against the prerequisite graph.
- **Do not let Stage 2 overwrite Stage 1** — extend, don't replace.
- **Do not reconstruct the queue from memory at the end** — it's updated live, item by item.
