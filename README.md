# ece' — an evidence-based teaching engine

A one-to-one tutor built on cognitive-science evidence, plus the subjects being learned on top of
it. Two layers:

- **Layer 1 — the engine.** Subject-agnostic method. `CLAUDE.md` (the operating contract),
  `teaching-manual.md` (the full pedagogy), `research/` (the evidence base, every claim cited).
- **Layer 2 — subjects.** A specific thing being learned, plugged into the engine. See
  `subjects/README.md`.

**The bar:** a technique is used only if it has replicated empirical support, a real measured effect
size, and is measured on *learning outcomes* — retention and transfer, not engagement or self-rated
confidence. Effect sizes are treated as optimistic upper bounds; techniques are ranked by
replication, never sold as a guaranteed number.

---

## This README describes protocol, not status

**Nothing here tells you what is currently active, built, or mastered.** That is a deliberate rule
(`CLAUDE.md`, *Source of truth*): static docs rot, state files don't. For live state, read:

| Question | Read this |
|---|---|
| What is each sem-3 subject's research status? | `subjects/sem-3/research-engine/research-queue.md` |
| What has been taught and what's due for review? | that subject's `progress-log.md` |
| What does this learner want, and how? | `learner-preferences.md` + the subject's `learner-profile.md` |
| What exam material has arrived? | `subjects/sem-3/_inbox/TRIAGE-LOG.md` and each `exam-pack/` |

---

## Layout

```
CLAUDE.md                  the operating contract, loaded every session
teaching-manual.md         full pedagogy, derived from research/
learner-preferences.md     universal personalization layer (engine-maintained)
subject-research-protocol.md   how a subject's knowledge base is built to standard
rendering.md               the visual/rendering subsystem design
whiteboard.md              the live Tutor Studio canvas design

research/                  00-07 + sources.md -- the ONLY live evidence base
subjects/                  Layer 2
  verilog/  python/        standalone subjects
  sem-3/                   the MUJ ECE semester-3 batch
    NN-subject/
      knowledge-base/      the researched content (+ stage-2/ for depth)
      exam-pack/           PYQs and lecture slides for that subject
      study-pack/          exam-ready, question-first study files
      curriculum.md  learner-profile.md  progress-log.md
    _inbox/                drop exam material here, any subject, unsorted
    research-engine/       the batch researcher + queue + exam calendar
tools/                     engine automation (see tools/README.md)
_archive/                  FROZEN history -- never cited, never read for decisions
```

---

## Core method, compressed

Five non-negotiable principles: **test don't tell** · **space and relearn to mastery** · **protect
working memory** · **calibrate to ~80% success** · **make self-assessment honest**.

The per-concept loop:

```
ACTIVATE -> ROUTE -> PRESENT -> MODEL -> GUIDE -> CHECK -> TEACH-BACK -> FADE -> INTERLEAVE -> RELEARN
```

Two rules that shape everything downstream:

- **Teaching gate.** A subject is never taught before its knowledge base is complete
  (`stage-2✓`, both stages). Teaching from a half-built base defeats the system.
- **Source split.** Professor material (slides, notes, PYQs) sets **scope, emphasis and framing**.
  The prescribed **textbook** sets **what is true**. A fact is never taught straight off a slide.

---

## Third-party material

`subjects/*/exam-pack/` holds course slides and past examination papers belonging to their
respective authors and institutions. They are kept here as personal study material under the source
split above — used for scope and framing, never as the authority on facts. **This repository is
private for that reason.** Do not make it public without removing that material first.

---

## Tools

`tools/` holds the engine's automation — transcript fetching, lesson rendering, the whiteboard
server. Install dependencies with:

```
pip install -r requirements.txt
```

See `tools/README.md` for what each script does.
