# subjects/ — Layer 2 (where subjects plug in)

The **engine** (Layer 1: `../CLAUDE.md`, `../teaching-manual.md`, `../research/`) is built and
active. This folder is where **subjects** plug in. It was kept empty until the engine was proven;
**live subjects now exist**: `verilog/`, `python/`, and the `sem-3/` batch. Current status lives
in each subject's `progress-log.md` and `sem-3/research-engine/research-queue.md` — this README
describes the *shape* of a subject, never live state.

**Two layouts exist:** standalone subjects sit flat (`subjects/<name>/`); the sem-3 batch nests
one level (`subjects/sem-3/<NN-subject>/`, same internal shape) with its shared research engine in
`sem-3/research-engine/` and intake in `sem-3/_inbox/`. Tools that take a subject name accept the
nested form (e.g. `save_lesson` with `subject="sem-3/01-statistics-and-probability"`).

## Stage status & the teaching gate (engine-level — applies to EVERY subject)

The status vocabulary and the teaching gate were first written down for the sem-3 batch
(`sem-3/research-engine/two-stage-depth.md` — full definitions live there), but they are
**engine-level rules**, not sem-3 rules:

- Status values: `stage-0` → `stage-1` → `stage-1✓` (exam-ready) → `stage-2` → `stage-2✓`
  (complete: deep structure + §0 surplus test passed) · `parked`.
- **Teaching gate (hard, learner-set): a subject is teachable only at `stage-2✓`** — both stages
  done, never a partial base. Learner-logged, subject-scoped exceptions live in the research queue
  (currently: Management of Technology, `stage-1✓` gate, 2026-06-26).
- **Standalone subjects carry the status too.** A subject built before this vocabulary existed
  (verilog, python — "exhaustive deep pass" builds) is stamped in its `00-map.md` with an explicit
  equivalence line (`stage-2✓-equivalent`, provisional until a recorded §0 surplus exit test) so
  the gate is checkable for every subject, not just the batch.

## What a subject is

A subject is one specific thing being learned, layered on top of the subject-agnostic engine.
The engine supplies *how* to teach; a subject supplies *what* to teach and *who* is learning it.

## What each subject will contain

When the first subject is created, it will live in `subjects/<subject-name>/` and hold:

```
subjects/<name>/
├── knowledge-base/    # the deep-dive research output — sourced, organized by deep structure
│                      #   (00-map.md, per-topic notes, misconceptions.md, sources.md)
│                      #   built to ../subject-research-protocol.md — this is what's taught FROM
├── curriculum.md      # DERIVED from knowledge-base/00-map: ordered objectives, prereqs first
├── learner-profile.md # current level, goals, known misconceptions
│                      #   + a "Preferences (overrides)" section (see below)
├── progress-log.md    # what's been mastered, the spaced-review queue
│                      #   (each item + when it's next due), AND the session-resume record
└── lessons/           # rendered browser lesson surfaces (the Visual & Rendering subsystem,
                        #   ../rendering.md): <YYYY-MM-DD>-<concept-slug>.html, dated so re-renders
                        #   never clobber older copies; optional <unit-slug>/ subfolders. Saved via
                        #   save_lesson() — permanent, never a temp dir. Only exists once a subject
                        #   is at stage-2✓ (figures are gated on a complete base).
```

### `progress-log.md` — the session-resume record (how you pick up exactly where you left off)

`progress-log.md` is what makes every session continue from the last. It has a fixed shape:

```
## Session resume   ← engine OVERWRITES this each session-end; READS it first each start
- Last session: YYYY-MM-DD
- Where we stopped: <unit / concept — incl. mid-step if a unit was left partway>
- Recap (what happened): 2–4 bullets — covered, mastered, where you struggled
- Next up: the immediate next move
- Due for review today: <items from the queue whose next-due date ≤ today>

## Mastery ledger        ← what's locked in
- <item> — mastered YYYY-MM-DD — to recall criterion

## Spaced-review / relearning queue   ← drives the start-of-session review
- <item> — last retrieved YYYY-MM-DD — next due YYYY-MM-DD — interval

## Session history       ← append-only; never overwritten (the audit trail)
- [YYYY-MM-DD] covered X · mastered Y · struggled with Z · stopped at W · next: V
```

The **Session resume** block is a fresh snapshot rewritten at the end of each session; **Session
history** is an append-only log you never edit, so the whole arc is recoverable.

**Startup is a memory test, not a readout.** The engine first asks *you* to recall, from memory,
what last session covered and where you stopped — a delayed retrieval test across the gap — then
checks your recall against the resume block, surfaces what you forgot (those become review
priorities), and continues. So the snapshot is the engine's ground truth; your recall is what gets
tested against it.

This file is **written live as the session happens**, not summarized at the end — each mastered
item, each stopping point, each outcome is logged concretely *the moment it occurs* (exact item,
exact position like "worked example 3, step 2", outcome as fact not judgment). So the record can't
drift from what actually happened: there's no end-of-session reconstruction to get wrong.

You pack a session up by saying **"wrap up"** whenever you need to leave — the cue for the engine's
wrap-up ritual (`../CLAUDE.md` session-end). Because the log is already current, wrap-up only
**finalizes** it (stamps the date, writes the resume + history line *from the entries already
recorded*) — it never reconstructs anything and never asks you to summarize. So **any** exit — a
full "wrap up", one word, or an abrupt "I have to go now" with nothing — leaves the same accurate,
resumable state. The summarizing happens at the *start* of next session instead, where it doubles
as the retention test above.

`knowledge-base/` is to `curriculum.md` what `../research/` is to `../teaching-manual.md`: the
researched *what is true*, from which the ordered *how to teach it* is derived. It is built to the
**`../subject-research-protocol.md`** standard — authoritative sources, triangulation, honest
uncertainty, no surface-level filler.

This structure is what makes the tutor **remember the learner across sessions**: on startup the
engine loads the active subject's profile and progress, runs spaced review of items that are
*due*, then continues the curriculum. The *engine's method* stays identical every session; the
*learner's state* is what evolves — and it evolves here, not in the engine.

### Personalization: universal + subject-specific (inherited)

The universal personalization layer lives in `../learner-preferences.md` (how this learner wants
to be taught, across *every* subject). Each subject **inherits** it and may **override** it for
that subject only, via a *Preferences (overrides)* section in its `learner-profile.md`. Subject
overrides win inside the subject; the universal file applies everywhere else. The engine maintains
both via the self-update protocol in `../CLAUDE.md` — preferences tune *how* the method is
delivered, never *whether* a core principle applies.

## How a subject gets created (later)

When ready to add the first subject, tell the tutor what you want to learn. It will:
1. Diagnose your current level (a few questions — no canned lecture).
2. **Map pass** — research the subject's deep structure to the `../subject-research-protocol.md`
   standard: big ideas, prerequisite graph, threshold concepts, misconceptions, source canon
   (→ `knowledge-base/00-map.md` + `sources.md`). You can't draft a sound curriculum without it.
3. **Build the COMPLETE knowledge base before any teaching** — the deep pass across *all* units, to
   full depth (`stage-2✓`). **Teaching is gated on a complete base** (learner-set rule): the tutor
   never teaches from a half-built KB — that defeats the system. If the base is too big for one
   pass, split it (Stage 1 exam-ready, then Stage 2 depth), but finish *both* before teaching.
4. Draft `curriculum.md` from the map; initialize `learner-profile.md` + an empty `progress-log.md`.
5. Begin teaching via the loop in `../CLAUDE.md`, scheduling spaced review as it goes. On re-entry,
   only **re-verify** stale/`contested` claims — the base is already complete.

Until then, the engine stands on its own.
