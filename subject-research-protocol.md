# Subject Research Protocol — How to Build a Subject's Knowledge Base (Layer 2)

> The engine teaches **from** a subject's knowledge base. The best method on Earth cannot rescue
> shallow or wrong content — *garbage in, garbage out.* This file is the evidentiary bar for
> **subject content**, the exact analogue of `research/00`'s bar for teaching techniques. Same
> ethos: depth, authoritative sources, triangulation, honest uncertainty, **no pop-science, no
> hallucination, no surface-level bullshit.**
>
> It governs how `subjects/<name>/knowledge-base/` is built. `curriculum.md` is *derived* from
> that base, exactly as `teaching-manual.md` is derived from `research/`.
>
> The base is a **living, self-correcting artifact** — built to a high bar *and* kept honest over
> time (§10). **Room for improvement is a core mechanism, not an afterthought:** a base that can't
> revise itself teaches yesterday's error, confidently, forever.

---

## 0. Prime directive of subject research

**Build a base you could teach from with ~10× surplus.** You teach from overflow, never from a
position equal to what you're teaching. The target is the **deep structure** — the generative
principles an expert reasons *from* — not a surface list of facts. If you understand only as much
as you're about to say, you haven't researched it; you've previewed it.

And the base is **never finished or frozen.** You build the best current reconstruction, mark how
sure you are of each part, and stay ready to correct it the moment something doesn't hold (§10).
"Done" means *good enough to teach from now*, not *closed to revision.*

**Test the surplus — don't feel it.** "10×" is unfalsifiable by introspection, and §6 warns that
mistaking your own fluency for understanding is a failure mode — so the *same* introspection can't
be the only check. Probe depth by **output**: generate several expert-level / edge-case / "why,
not what" questions for the unit and confirm the base answers them **from mechanism**, with
sources. A base that only answers the questions you intend to *ask the learner* has no surplus —
it has a preview (§6).

---

## 1. The non-negotiable standard (what counts as "researched")

A claim enters the knowledge base only if **all** hold:
1. **Sourced** to an authoritative origin — not a derivative summary of a summary, **and not your
   own recall** (see "the researcher is a model," below).
2. **Triangulated** across ≥2 *independent* quality sources for anything **load-bearing**,
   surprising, or contested.
3. **Confidence-marked** — `settled` / `contested` / `uncertain` (with `suspect` as the quarantine
   flag of §10). See the confidence scale at the end of this section.
4. **Mechanism-stated** — you can say *why/how* (the cause), not only *what* (the statement).

If a claim can't clear this, you **flag the gap** — you never paper over it. (Mirrors the honesty
discipline of `research/`.)

**What "load-bearing" means** (it carries the whole triangulation burden, so it can't stay vague):
a claim is load-bearing if **other claims depend on it** (a prerequisite or definition), **the
learner will act on or be assessed on it**, or **it would cascade if wrong** (§10.6). When unsure,
treat it as load-bearing — under-triangulating is the failure mode, not over-.

**⚠ The researcher is a model — your default "source" fails this bar.** The thing executing this
protocol recalls most of its knowledge from training: a blended, uncitable, AI-internal summary —
exactly the tier-4 "AI-generated summary" §2 distrusts, and the prime hiding place for the
hallucinated specifics §6 forbids. So:
- **Recall ≠ sourced.** A claim you only *remember* is tier-3 **at best** and stays `uncertain`
  until checked against an actual external source *this session*.
- **For load-bearing claims, verify against a real source** — use the web tools (search/fetch) to
  reach the primary or authoritative-secondary source before promoting past `uncertain`.
- **If you have no source access this session,** you may still teach — but every specific (number,
  date, name, formula, edge case) recalled from training is marked `uncertain` and logged to the
  to-verify register (§10); you say so plainly rather than presenting recall as verified fact.

**Confidence scale (one vocabulary, used everywhere):** `settled` (triangulated, ≥2 independent
authoritative sources, mechanism stated) → `contested` (authorities genuinely disagree; teach the
disagreement, never one side as closed) → `uncertain` (single-source, inferred, or recalled-only;
carries a standing to-verify flag) → `suspect` (a §10 trigger has fired; **quarantined**, nothing
else may pull from it until re-verified). Confidence moves **both directions** along this scale as
evidence arrives (§10).

---

## 2. Source hierarchy (prefer the top; distrust the bottom)

Tier every source before leaning on it:

0. **Instructor-provided material — top priority for SCOPE, not for truth.**

   Material from the learner's professor — slides, handouts, notes, and especially **past-year
   papers / PYQs** — is the priority source for **what to cover, how it is asked, and what is
   emphasised**. It is the highest-leverage lever for scoring. But it does **not set facts**:
   slides, answer-keys, and toppers' notes contain errors, so every *content claim* is still
   verified against the prescribed **textbook** (Tier 1) under §1–§5.
   - **The honesty split** (worked out in full in
     `subjects/sem-3/research-engine/exam-resources.md`): a PYQ/PPT is **Tier-1 for *what's
     tested*** (question types, recurring topics, weightage, the instructor's notation/emphasis)
     and **Tier-3/4 for *what's true*** (never let a key or a slide bullet settle a fact). Let the
     material decide *what to cover and how it's asked*; let the textbook decide *what's correct.*

   **Exam-ready coverage comes before depth.** Cover the instructor's scope to exam-ready depth
   first; deepen toward expert structure second. **Scoring outranks depth** — never trade exam
   coverage for early depth. The sem-3 batch implements this as two **physically separate** KB
   stages — **Stage 1 (exam-ready, syllabus-bounded)** then **Stage 2 (deep structure)** — see
   `subjects/sem-3/research-engine/two-stage-depth.md`. Teach from the Stage-1 set first; open
   Stage-2 only after.

   **When no instructor material exists for a unit**, skip straight to the prescribed **textbook +
   NPTEL** as primary — do not wait for material that has not arrived. (Per unit, not per subject:
   one unit can be exam-ready while another has no material yet.)

   **Late-arriving material RE-SCOPES, it does not RE-TEACH.** When material arrives for a unit
   already taught, **do not replay it** — that wastes the learner's time on what they already know.
   Run a **delta diagnosis**: a fast retrieval check of the unit *against the professor's version*
   (just "diagnose before teaching" + "test, don't tell" applied to re-entry). Three outcomes:
   - **Gap** — covers something not yet mastered, or now newly in exam scope → teach *only that gap*.
   - **Reframe** — same content, different notation / method / emphasis the exam expects → teach
     *only the mapping* to the professor's framing, briefly. Don't re-derive the concept.
   - **No delta** — already mastered and matches → **teach nothing**; fold the unit into the
     spaced-review / successive-relearning queue (`research/02 §2–§3`).

   The diagnosis honors principle 5: a "quick confirm" that exposes weak recall means it **is** a
   gap — teach it. Mastered items are confirmed by a single retrieval probe, **never re-lectured**.
   This is the teaching-side response to new material; intake/routing is handled by the central
   `_inbox/` triage (`subjects/sem-3/_inbox/README.md`).

   **Practical ingestion — the verified automated path (tested this session).** NPTEL course /
   `archive.nptel.ac.in` web pages are JS/tab-driven and **do not fetch cleanly** (404s, empty
   WebFetch). The working automated route is NPTEL's own **YouTube lectures → captions → cleaned
   text**, via `tools/fetch_transcripts.py` (yt-dlp). Default workflow when a unit needs NPTEL:
   1. Identify the NPTEL course's YouTube playlist (or a search query) matching the syllabus unit.
   2. Run `python tools/fetch_transcripts.py "<playlist-url>" "subjects/<name>/knowledge-base/_transcripts/"`.
   3. Read the resulting `.txt` transcripts as the lecture source.

   **Caption transcripts are Tier-1 *with caveats*.** They are ASR output: reliable for narrative,
   structure, and intuition, but they **mangle math, symbols, and numbers** (e.g. `1024`→`1 024`,
   formulas rendered as words). So every **load-bearing specific** (formula, constant, definition,
   named result) read from a transcript stays `uncertain` until **triangulated against the canonical
   textbook** (§1, §5) — the transcript never settles a formula by itself. Manual PDF drop by the
   learner is the fallback only when no captioned lecture covers the unit.

1. **Primary / foundational** — canonical textbooks, original works, peer-reviewed literature,
   official specs/standards/docs, datasets. *The real ground.* For this project's subjects, the
   **canonical textbook of each subject** is the ground truth for content and the depth spine;
   **NPTEL** (IIT/IISc-produced, syllabus-aligned, exam-style practice) is the structured lecture
   companion and the default primary when no Tier-0 material and no obvious canonical text apply.
2. **Authoritative secondary** — respected references, expert-consensus statements, well-regarded
   surveys/reviews.
3. **Derivative** — encyclopedic summaries. *Orientation and leads only — never the final word.*
4. **Low-trust** — SEO/content-farm tutorials, undated blogs, AI-generated summaries, forum
   folklore. *A pointer to chase down, never a citable fact.*

Rules: **go to the source the summary is summarizing.** Watch for **circular sourcing** (everyone
quoting the same one blog — a cascade, not corroboration). Prefer **domain-native authorities**.
Record **edition/date** for anything in a moving field.

**On video / YouTube (resolves the "should we analyse YT videos" question).** A text model
ingests video *least* efficiently and least verifiably — the transcript is the real payload, not
the footage. So:
- **Institutional video** (NPTEL, MIT OCW, a professor's own recording) is tiered by its *content*
  (Tier 0–1), but is **consumed as its transcript/notes**, never as raw video.
- **Non-institutional YouTube** (random tutorials) is **Tier 4** — a lead to chase, never a
  citable fact — same as any content-farm source.
- Video is a **fallback, used only when** a topic genuinely needs visual/animated intuition *and*
  no text source carries it. In that narrow case, pull the **transcript** (`yt-dlp` captions, or a
  multimodal model such as Gemini to extract structured notes from the URL) and then **run the
  extracted claims through §1–§5 like any other source** — the extraction does not exempt them
  from triangulation. Building a Gemini/transcript pipeline is only worth it for that fallback,
  not as the primary content path.

**For tacit / craft / skill subjects** (a language, an instrument, drawing, cooking, negotiation),
the deep structure lives in practitioner expertise, not citable documents. The tier model still
holds — it just re-maps: "primary" becomes **expert consensus and demonstrated, reproducible
practice** (canonical method, what skilled practitioners reliably do and why), "low-trust" stays
the same (folklore, content-farm tutorials). Triangulate across *independent expert sources*, and
keep the mechanism requirement (§3): "do X because it causes Y," never "do X because that's how
it's done."

---

## 3. Depth — reach the deep structure, not the surface features

- Find the **handful of big ideas** the whole subject hangs on — the expert's organizing schema.
  Everything else should hang off them. If you can't name them, you don't have the subject yet.
- For each concept, capture the **mechanism**: "X causes Y via Z," not "Y is the case."
- Separate **deep structure** (the principle) from **surface features** (the specific cover story
  or example). Experts sort by deep structure, novices by surface — the base must be organized by
  deep structure so the engine can teach it that way (concreteness fading, `research/02 §8`).
- Map the **web**, not a list: where each idea comes from and what it connects to.

---

## 4. Map the terrain the teaching engine actually needs

The deep dive must explicitly surface these, because the engine **consumes** them:

- **Prerequisite structure** — the real dependency graph (what must be understood before what).
  This *is* the spine of `curriculum.md` and enforces cognitive load order (`research/01 §2`).
- **Threshold concepts** — the few ideas that, once grasped, transform understanding *and* are
  where learners predictably stall. Flag them; budget extra teaching there.
- **Known misconceptions & common errors** — the predictable wrong models novices hold. Feeds
  `learner-profile.md` and the engine's productive-failure and feedback moves (`research/02 §5`,
  `research/04`). **A subject with no misconception list is under-researched.** But the list is
  itself a set of claims — and a plausible-sounding *invented* misconception is exactly the kind of
  hallucination §6 forbids. So **source misconceptions** to the discipline-based education /
  documented-error literature where it exists, and **confidence-mark each one** like any other
  claim. A misconception you can only *guess* is `uncertain` and flagged to-verify — never asserted
  as "the common error" on recall alone.
- **Settled vs. contested vs. evolving** — never teach a live debate as a closed fact.

---

## 5. Verification & triangulation (the anti-bullshit core)

- Load-bearing or surprising claim → confirm in **≥2 independent** authoritative sources before
  it counts as "known." Independent = not citing each other (watch the citation cascade of §2).
- **Independence is the hard part for a model.** Two things you *recall* are **not** independent
  sources — they may both come from the same place in training, so "I remember it two ways" is one
  source, not two. Real independence means **two distinct external sources that don't trace to a
  common origin**, reached this session (§1). When you can't establish independence, you have one
  source; mark it `uncertain`.
- **Verify exactly:** numbers, dates, named results, formulas, edge cases, definitions. This is
  precisely where hallucination and surface-error hide.
- **Separate verified from inferred.** Label inference as inference; never launder a guess into a
  fact by stating it confidently.
- **When sources conflict, don't average them into mush** — record the disagreement and which is
  better-grounded (the reconciliation discipline of `research/00`).
- **Honest uncertainty beats false confidence.** "I could not verify X" is a valid, *required*
  output — not a failure.

---

## 6. The surface-level failure modes — the "bullshit" to refuse (blacklist)

- ❌ Regurgitating an encyclopedia intro / first page of Google as if it were understanding.
- ❌ Buzzword lists with no mechanism ("it uses attention") — *why, how, under what conditions?*
- ❌ **Tutorial-only knowledge:** how to run the steps, zero grasp of why (procedure, no schema).
- ❌ **Hallucinated specifics** — inventing a citation, number, quote, date, or edge case. Unsure → say so.
- ❌ Single-source confidence; citation-cascade laundering.
- ❌ Recency/popularity bias — newest or most-blogged ≠ most correct or most foundational.
- ❌ Smoothing over real disagreement or uncertainty to sound authoritative.
- ❌ Stopping at the depth you intend to teach (no surplus — violates §0).
- ❌ Mistaking **your own fluency** for understanding — the same illusion the engine warns the
  *learner* about (`research/01 §6`) applies to *you, the researcher.*
- ❌ **Improvised teaching content that never passed the bar.** The protocol governs the
  knowledge-base artifacts — but the engine also *generates content live* during a lesson:
  examples, analogies, worked numbers, "what if" cases. Those are claims too, and a fabricated one
  bypasses §1–§5 entirely. A **load-bearing** improvisation (a worked result the learner will
  generalize from, a factual specific) gets verified or pulled from the base like anything else; a
  purely **illustrative** one is fine, but flagged as illustration, never smuggled in as a sourced
  fact. The research bar follows the content, not the file it lives in.

---

## 7. Calibrate depth to the goal — but always over-research

Depth scales with the learner's goal (casual literacy vs. mastery vs. professional use — from
`learner-profile.md`). But the base **always** runs deeper than the teaching surface (the §0 10×
rule), and the **map** can be researched fully even when full detail is deferred (§8).

---

## 8. When to research — map first, detail just-in-time (default workflow)

1. **Map pass — upfront, whole subject.** Establish the big ideas, the prerequisite graph,
   threshold concepts, the misconception list, the scope, and the source canon. Cheap, high
   leverage — this is what makes `curriculum.md` sound. **But the map is not the *low-bar* pass.**
   Leaf facts can wait for the deep pass; the **prerequisite edges and threshold-concept claims
   cannot** — they are load-bearing by definition (§1), they set teaching order, and a wrong edge
   mis-sequences everything downstream and is costly to undo once teaching starts. So **triangulate
   the prereq graph and threshold claims to the full §1 standard during the map pass**, even while
   leaf detail is deferred.
2. **Deep pass — just-in-time, per unit.** Before teaching a unit, run the full §1–§6 deep dive on
   *that* unit. Keeps the base fresh, avoids over-researching units the learner may never reach,
   and lets the learner's demonstrated level tune the depth.

Why hybrid: a curriculum built without the map has broken prerequisites; researching every detail
upfront is wasteful and goes stale. (This mirrors how the **engine** was built — full research base
first — but a subject can be far larger than the engine, so detail is paced.)

> **Switchable — and for THIS project, switched.** The learner has set a standing rule: **the
> complete knowledge base (both stages, `stage-2✓`) is built before any teaching** — teaching from
> a partial base defeats the system. So the just-in-time-per-unit default does **not** apply at
> teaching time here: research a subject exhaustively first, then teach. (Map-first + staged build
> is still *how* the base is constructed; "just-in-time" survives only as **re-verification** of
> stale/`contested` claims on re-entry, §10 — never first-time research mid-lesson.)

---

## 9. Output — what the deep dive produces (artifacts)

Mirror the engine's own shape (`research/` → manual → contract):

```
subjects/<name>/
├── knowledge-base/        # the deep-dive output — sourced, organized by DEEP STRUCTURE
│   ├── 00-map.md          # big ideas, prerequisite graph, threshold concepts, scope,
│   │                      #   + a standing "Open questions / to-verify" register (§10)
│   ├── <topic>.md …       # per-unit deep notes (mechanism-level, cited, confidence-marked)
│   ├── misconceptions.md  # known novice errors / predictable wrong models
│   ├── sources.md         # every source, tiered (§2), with confidence + date notes
│   └── CHANGELOG.md       # correction audit trail (§10): what changed, why, what triggered it
├── curriculum.md          # DERIVED from 00-map: ordered objectives, prerequisites first
├── learner-profile.md     # level, goals, misconceptions + Preferences (overrides)
└── progress-log.md        # mastered items + the spaced-review / relearning queue
```

`curriculum.md` is to `knowledge-base/` what `teaching-manual.md` is to `research/`: the derived,
ordered *how to teach this*, strictly downstream of the researched *what is true*.

**Confidence markers must survive derivation.** When `curriculum.md` and live teaching pull from
the base, a `contested` / `uncertain` claim stays flagged as such to the learner — never flattened
into a settled fact in the hand-off (§4: "never teach a live debate as a closed fact"). The honesty
discipline is enforced in the base *and* carried through to what's said.

**Entry formats** (so the audit artifacts don't drift in shape across subjects — mirroring the
precise preference-line format in `CLAUDE.md`):
- `CHANGELOG.md` — one entry per correction:
  `[YYYY-MM-DD] <claim/topic> — <what changed> — <why> — <trigger: learner Q / conflict / new source / downstream failure> — <confidence: old → new>`
- `00-map.md` "Open questions / to-verify" register — one line per gap:
  `[opened YYYY-MM-DD] <claim or question> — <why uncertain / single-sourced> — <what would resolve it>`

---

## 10. Self-correction & the living knowledge base (the core mechanism)

§1–§5 are how you get a claim right the *first* time. This is how you keep it right *over* time. A
claim's confidence is a **live value that moves both ways** as evidence arrives, and the base
carries a standing backlog of its own weak spots. Treat every entry as *the best current
reconstruction*, revisable on cause — never a closed verdict.

**What makes a claim "suspicious" (re-examination triggers):**
- A learner's question exposes it, or they supply a **counterexample** that contradicts it.
- You catch an **internal inconsistency** — two notes in the base disagree.
- While teaching it you find you **can't state the mechanism** (the §0 surplus wasn't really there).
- A claim marked `uncertain` or single-sourced meets a **better-grounded contradicting source.**
- A **downstream result fails** — a procedure taught from the base doesn't work; a prediction misses.
- **Better information surfaces** — a newer edition, or a primary source you'd only seen summarized.
- **Time, for moving fields** — the triggers above are all event-driven; a stale claim that nothing
  happens to fire on sits confidently forever (the exact failure this file's intro warns of). So
  any claim in a moving field (the ones §2 says to date) is **re-checked on subject re-entry**, and
  `evolving`/`contested` claims carry a recheck horizon — staleness is itself a trigger.

**The correction loop (when a claim is suspect):**
1. **Quarantine** — stop teaching it as settled; mark it `suspect` so nothing else pulls from it meanwhile.
2. **Re-verify** — re-run §1–§5 *on that claim*: back to authoritative/primary, re-triangulate.
3. **Reconcile** — sources conflict? Don't average to mush; record the disagreement and take the
   better-grounded one (the `research/00` discipline).
4. **Update** — rewrite the note, move its confidence marker (up *or* down), fix `sources.md`.
5. **Log** — append to `knowledge-base/CHANGELOG.md`: what changed, why, and the source/event that
   triggered it. **Never silently overwrite** — keep the audit trail (the engine preserves its
   history too).
6. **Propagate** — if the corrected claim was a **prerequisite**, walk the dependency graph (§4)
   and re-check everything built on it. A correction that doesn't cascade is half-done.

**Teaching is the base's stress test.** The teaching loop in `CLAUDE.md` is also a continuous audit
of the *content*: every learner question, error, and "wait, why?" is a probe that can expose a weak
or wrong entry. *Errors are data here too* — a question the base can't answer is a correction
request, not a nuisance; route it into the loop above.

**In-session fallback (when a claim is exposed mid-lesson).** The full loop above (back to primary,
re-triangulate) is not a live operation if you have no source access during the lesson — so don't
pretend to re-research on the spot. Instead: **quarantine** the claim (`suspect`), **teach the
uncertainty honestly** ("I'm not certain of this — let's not bank on it"), keep going, and **log it
to the to-verify register** so the real re-verification (steps 2–6) happens before the claim is
taught as settled again. Honest uncertainty in the moment beats inventing a confident patch.

**The confidence ratchet & improvement backlog:**
- Confidence is **promoted** by independent corroboration, **demoted** by contradiction — never
  stamped once and forgotten.
- Every `uncertain` / single-source claim keeps a standing **to-verify** flag.
- Maintain an **Open questions / to-verify** register (in `00-map.md`): known gaps, unresolved
  conflicts, believed-but-unconfirmed claims. Work it down over time. The base is *supposed* to get
  better — an empty backlog usually means you stopped looking, not that you're finished.

---

## 11. Self-audit (the researcher's mirror of the teacher's)

Before any claim is allowed into the knowledge base, answer:
- What's my source — authoritative or derivative? Did I reach the primary? **Or am I just recalling
  it from training?** (Recall ≠ sourced — §1.)
- Did I triangulate anything load-bearing across independent sources?
- Can I state the **mechanism**, or only the surface statement?
- Have I separated **verified** from **inferred**?
- Have I logged what I **could not** verify?
- Did anything I taught or reviewed feel off — and did I **flag it `suspect` and route it to §10**,
  rather than teach it again unchanged?

If any answer fails → it's surface-level, or it's rotting. Go deeper, correct it, or flag the gap.
(The engine's own self-audit in `CLAUDE.md`, applied to **content** instead of **method**.)
