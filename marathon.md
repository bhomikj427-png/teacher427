# Marathon — protocol

> A **marathon** is a long, question-driven study run over a defined book: the learner solves a large
> set of questions in one push, and solving them *is* the learning. Learner-designed and signed off
> 2026-10-17. `CLAUDE.md` carries the compressed rule; this file is the full protocol. Live state
> (which marathon is running, where it stopped) never lives here: it lives in the subject's
> `progress-log.md` and the marathon's own manifest (§7).

## 1. When it runs

- The learner starts it ("marathon on X"). The engine never starts one on its own.
- **Source = a defined book** (named title + edition + sections). That book is the authority for
  what's true, so a marathon **may run below the `stage-2✓` teaching gate** (the gate's only
  standing exception besides subject-scoped ones in the research queue). It never runs on slides,
  memory or a half-built KB alone.
- The scope is fixed up front from **what is known for sure** (syllabus, the learner's instructions).
  Unconfirmed extras are listed as "possible additions", never silently included.

## 2. Two modes, one format

| Mode | Which questions | Format |
|---|---|---|
| **Learning marathon** (default) | The engine curates (§3) | identical |
| **Assignment marathon** (learner says it's an assignment) | **Every** question in scope | identical |

The only difference is question selection. The solution block is always the shortest copyable
write-up, so an assignment needs no separate version.

## 3. Choosing questions (learning mode): never at the cost of mastery

- A question is **kept** if it adds anything: a new idea, a new twist on an old idea (a different
  arrangement, source type, sign trap, AC instead of DC, a dependent source, a different unknown,
  a different route to the answer), or a harder combination.
- A question is **dropped only if it is practically identical** to one already in the run: same
  structure, same method, same traps, only the numbers changed. When in doubt, keep it.
- There is no fixed count per topic. A topic gets as many questions as it takes for every twist the
  book offers to appear and be practised; that may be 5 or 40.
- Dropped questions are listed in the manifest with the question each one duplicates, so the cut
  is auditable.

## 4. The page for each question (fixed order)

1. **Question** with the book's own figure (cropped from the book, never redrawn).
2. **Try it first.** Cover the rest and solve.
3. **What's new (hint).** Only when the question carries a new idea or twist. It names the idea so
   the learner can finish unaided once they see it. It is a hint, not a solution.
4. **Solution, compact and copyable:** Given → To find → the equations of each step with every
   intermediate value → boxed answer. Intermediate values are always shown, so a wrong attempt can
   be matched line by line to find the exact step that broke (feedback = error → step,
   `research/04`).
5. **Side note** (optional): a trap, shortcut or link, only when it teaches something.

**Fading.** The explanation prose fades; the steps never do. Early and new-idea questions get full
explanations (inside the hint/side-note boxes, keeping the solution block clean). Later practice
questions get the bare compact solution. Worked examples → independent solving
(`research/02 §7`); explanation becomes redundant once the method is known (expertise reversal).

**Topic openers** follow the river rules (`learner-preferences.md §3`): each topic opens on where it
sits and what the learner already has, primes at most 3 terms, defines every term before first use,
and writes the bridge from the previous topic. The opener is short (a map + the statement + the
rules needed); the questions do the rest.

## 5. Order

- **Book-wise:** the solved book first (worked examples), then the unsolved book (independent
  solving), matching the fade.
- Within each book, **topic by topic (blocked)**, in the book's own order (`research/02 §6`:
  block first).
- The idea ledger (§7) decides which questions count as "new", so inserting questions later just
  recomputes the labels; nothing already written is rewritten.

## 6. Evidence, checking, and the learner's job

- **No marks, no pass marks, no checkpoints.** Evidence of learning = the learner solving the
  question unaided.
- **The learner reports only misses**, e.g. "5.7 needed the solution". Silence means solved.
  A miss → the engine adds a side note on that idea and, if the book has one, makes sure a further
  question with the same idea follows.
- **The engine does all checking.** Every answer is re-derived independently and checked a second
  way (node equation / direct solve / simulation). Printed answers are compared and marked
  "= book"; a mismatch is flagged as a possible book error, never silently copied. The learner never
  has to verify anything.

## 7. Files and logging

- Per marathon, in the subject folder: `<marathon-slug>/` containing `manifest.md` (every question:
  source + number, topic, idea tags, kept/dropped (+ duplicate of), book answer, verified answer,
  misses reported), `src/` (content + crop list + builder) and `pdf/` (the generated PDF).
- Built and delivered in **batches** (about one topic per batch), each in the frozen demo format.
- Log-first: a `progress-log.md` line precedes every batch. The resume point is the exact question
  ID, so an abrupt exit resumes cleanly.

## 8. After the marathon: the revision set

- The learner does not return to marathon questions.
- The engine builds a **revision set**: the smallest group of basic/set questions that together
  cover every idea in the ledger (about one per idea), saved beside the marathon.
- Revising from it once on a later day is the marathon's spaced retrieval. It is the cheap
  safeguard that keeps a cram from fading (`research/02 §2–§3`).

## 9. The cramming tension (named once, honoured)

The learner prefers one long massed session and says spaced sessions don't happen in practice.
The evidence: at retention intervals of a week or more, spacing nearly doubles recall
(`research/02 §2`). A marathon is therefore massed by design, logged as a **tension** in
`learner-preferences.md §7`, not a rule. Kept mechanisms: the learner **generates** every answer
before seeing it (retrieval, `research/02 §1`), and the revision set (§8) is the spaced re-test.
The engine does not lecture about it again.
