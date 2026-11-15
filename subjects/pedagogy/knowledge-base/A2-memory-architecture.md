# A2 — Memory Architecture: Where Information Goes and Why It Gets Lost

> **Information type:** all types. This unit gives the *machinery* that A3 classifies. The
> declarative/nondeclarative split here becomes a column of the A3 table.
> **Threshold concept 2:** a narrow working-memory bottleneck in front of a large long-term memory.
> Confidence tags: `settled` / `contested` / `uncertain` / `suspect`. Source IDs → `sources.md`.

---

## 1. The pipeline (one picture)

```
 input ──> WORKING MEMORY ──encode──> LONG-TERM MEMORY ──consolidate (incl. sleep)──> stable trace
           (~4 chunks,                (declarative +           │
            seconds unless             nondeclarative          └──retrieve (cue-dependent)──> back into WM
            rehearsed)                 systems)                      (retrieving changes the memory: A1 §5)
```
Each arrow is a place where learning can fail. §6 maps failures to causes.

## 2. Working memory: the bottleneck `settled` (limit) / `contested` (exact number)

- **What it is:** the small workspace where you hold and manipulate information right now:
  reading this sentence, carrying a digit, comparing two options.
- **Capacity ≈ 4 chunks** (Cowan, C01).
  - Miller's famous "7 ± 2" (1956) was a rough estimate that mixed in rehearsal and chunking.
  - When those are blocked, the core limit is about 3–5 chunks.
  - A **chunk** = a unit already bound together in long-term memory ("FBI" = 1 chunk for an
    English reader, 3 letters for someone else).
  - `contested`: commentators accept a fundamental chunk limit, but say the physiological basis
    of "4" specifically is unclear (C01 commentary).
- **Structure (Baddeley, B00):**
  - central executive: attention control
  - phonological loop: speech-based
  - visuospatial sketchpad: images and space
  - episodic buffer (added 2000): binds information from the subsystems and long-term memory
    into one multimodal episode, and is accessed through awareness
- **Why it matters for learning:**
  - New, unconnected information must squeeze through ~4 slots.
  - Information that is already chunked (from long-term memory) passes through as one unit.
  - This is why novices overload on what experts find easy (→ A5), and why element
    interactivity sets difficulty (→ A3, S10).
- **Can you train it bigger?** No good evidence.
  - Working-memory training improves performance on tasks like the trained ones, briefly.
  - It does not transfer to reasoning, reading or arithmetic compared with active controls
    (MLH13; 2016 update). `settled`
  - The route to "more working memory" for a subject is more chunks in long-term memory, not
    training the slots.

## 3. Long-term memory: multiple systems `settled` (split) / `contested` (boundaries)

Squire (Sq04):
| System | Holds | Expressed as | Brain basis (main) |
|---|---|---|---|
| **Declarative** (explicit) — *semantic* (facts, concepts) and *episodic* (events you lived) | "Knowing that" | Conscious recollection; can be true or false | Medial temporal lobe / hippocampus |
| **Nondeclarative** (implicit) — skills and habits | "Knowing how" | Performance, without awareness of the content | Striatum (basal ganglia) |
| — priming | Faster or biased processing after exposure | Performance | **Not hippocampus-dependent** — "dependent on other brain systems" (SS17, Squire lab, full text) `settled`. The usual textbook placement "neocortex" stays `uncertain` (Sq04 / Squire 1996 / 2015 full texts all 403'd in S11a; not load-bearing) |
| — simple conditioning | Learned emotional or motor responses | Performance | Amygdala (emotional), cerebellum (motor) |

- **Why it matters:** different systems learn by different rules.
  - Declarative memory can form in one exposure but is fragile without retrieval and spacing.
  - Skills form gradually through repetition with feedback.
  - This is the brain-level reason A3/A4 match methods to information type.
- `contested`: the boundary is not absolute. Some tasks can be learned either declaratively or
  nondeclaratively (Sq04 discussion), and skill learning usually *starts* declarative ("first
  put the clutch in, then…") before becoming automatic (→ A3, procedural row).
- **Capacity:** no practical limit on long-term *storage* has been found where it has been
  measured. `settled` for recognition, scoped (S11a):
  - Standing 1973 (St73): single-trial picture learning up to 10,000 items; recognition capacity
    for pictures "almost limitless" under appropriate conditions; retained amount grows as a
    power law of amount presented.
  - Brady, Konkle, Alvarez & Oliva 2008 (BKAO08): 2,500 objects in 5.5 h; two-alternative
    recognition 92% (vs a new category), 88% (vs a same-category object), 87% (same object, other
    state/pose) — thousands of items stored *with detail*.
  - **Boundary:** these are *recognition* tests. Recall is far lower (St73), so the practical
    bottleneck is **retrieval**, not storage — the same split as storage vs retrieval strength (A1
    §3). The engine reading: "you're not out of space; you're out of retrieval routes."

## 4. Encoding → consolidation → retrieval

**Encoding** (getting it in)
- What gets stored depends on how the information was processed: depth and meaning (CL72 → A6),
  links to prior knowledge, and whether it was generated or merely read (→ A6). `settled`

**Consolidation** (making it last) `settled` (sleep benefit) / `contested` (mechanism details)
- A new memory stays vulnerable for a while after encoding.
- Wixted (W04) argues everyday forgetting is mostly *interference with traces that have not yet
  consolidated*, i.e. new learning disrupting recent learning, rather than passive decay.
  `contested` (a position review, but it integrates psychology, pharmacology and neuroscience).
- **Sleep** (RB13): sleep is a brain state optimised for consolidation, while waking is optimised
  for encoding. During slow-wave sleep, recently encoded memories are **reactivated** and
  reorganised into long-term networks (active systems consolidation).
  - Practical consequence: study → sleep → retrieve is a real sequence. Spacing *across nights*
    gets consolidation in between. This is why the engine schedules across-night relearning.
  - Mechanism detail (exactly which sleep stages do what) = `contested`.

**Retrieval** (getting it out) `settled`
- **Encoding specificity (TT73):** a cue works to the extent it was part of how the memory was
  encoded.
  - Classic finding: people failed to *recognise* a word they had studied, yet recalled it when
    given the weak cue word it had been paired with.
  - Consequence: memories are cue-bound. Material studied in one way, place or wording is easiest
    to retrieve that way. Varying cues and contexts during practice widens the routes in
    (→ A1 desirable difficulties, A5 transfer).
- Retrieval modifies memory: it strengthens it and makes it easier to reach next time (A1 §5).

## 5. Forgetting: the curve, and what it actually says `settled`

- **Ebbinghaus (1885)** taught himself nonsense-syllable lists and measured **savings**: how much
  less time relearning took after a delay.
- **Murre & Dros 2015 (MD15)** replicated it: one participant, about 70 hours, delays from 20
  minutes to 31 days. The result closely matches the original curve.
  - Steep early loss that levels off.
  - The curve is not perfectly smooth: there is an upward bump at the 24-hour point, consistent
    with a sleep benefit.
  - Caveat: N = 1 by design (as in the original), and nonsense material (no meaning to link to).
- **What the curve does *not* say:** that you "lose 70% in a day" of everything. Meaningful,
  connected, well-retrieved material is forgotten far more slowly. The famous curve describes
  the worst case: isolated, meaningless items learned once.
- **Savings = storage strength survives** (A1 §3): even when you cannot recall something,
  relearning it is faster. Nothing studied properly is wasted.

## 6. Failure map — where learning breaks

| Breaks at | Symptom | Cause | Fix (→ A4) |
|---|---|---|---|
| Working memory | "I'm lost", can't follow a derivation | Too many new interacting elements at once (C01, S10) | Smaller steps, worked examples, pre-learn the parts |
| Encoding | Read it, can't explain it | Shallow processing, no links to prior knowledge (CL72) | Generate, explain, connect (A6) |
| Consolidation | Knew it yesterday, gone today | Interference, no sleep between sessions (W04, RB13) | Space across nights; avoid cramming similar material back-to-back |
| Retrieval | "It's on the tip of my tongue", or only works with the book's wording | Cue-bound encoding (TT73) | Retrieve with varied cues; mix contexts |
| Wrong system | Can explain the method, can't execute it fast | Declarative knowledge not yet turned into skill (Sq04) | Repeated practice with feedback until automatic |

## 7. Uses
- **As a learner:** protect the bottleneck (one new element at a time when it's hard); sleep
  between sessions on purpose; practise retrieving from different angles; for skills, practise
  until fast, not only until understood.
- **As a teacher:** count the new interacting elements in a lesson and cut them. Teach with
  varied examples and contexts. Never treat "I explained it" as "they stored it".
- **For the engine:** confirms protect working memory (principle 3) and across-night relearning
  (principle 2). Nothing to change.

## Misconceptions owned
M3 (shared with A1), M4, M22, M23, M24, M25 → `misconceptions.md`.
