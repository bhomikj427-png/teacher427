# Learner Preferences — Universal (cross-subject)

> **The personalization layer.** This file records *how this specific learner wants the method
> delivered* — across **every** subject. It is loaded at session start alongside `CLAUDE.md`, and
> the engine **maintains it itself** (see *Self-update protocol* below and in `CLAUDE.md`).
>
> Scope split: **universal** preferences live here; **subject-specific** ones live in that
> subject's `subjects/<name>/learner-profile.md` under *Preferences (overrides)* and win inside
> that subject. Universal applies everywhere a subject hasn't overridden it.

---

## Guardrail — read before adding anything

Preferences tune **how** the method is delivered. They **never** override the five non-negotiable
principles in `CLAUDE.md`. Concretely:

- ✅ Legitimate to honor: tone, verbosity, pace, session length, example domains/interests,
  notation/language, amount of encouragement, autonomy choices, review cadence. These serve
  **autonomy & relatedness**, which is itself evidenced (SDT, `research/05 Part B`).
- ⚠️ **Not obeyed if it breaks the prime directive** — e.g. "just tell me, don't make me retrieve,"
  "don't make me struggle at all," "let me re-read instead of recall," "cram before the deadline."
  Honor the *spirit* (cut friction, soften framing) while keeping the *mechanism* (retrieval and
  desirable difficulty still happen). Name the tradeoff honestly. Log it under **§7 Tensions**, not
  as a rule.
- 🚫 **This is NOT "learning styles."** Catering = communication, tone, autonomy, interests,
  scheduling. The debunked myth is matching a *modality* (visual/auditory/etc.) to a person — never
  do that (`research/06`). Tailor to **prior knowledge + the task** and to **stated communication
  preferences**, never to a "style."

## Entry format & provenance

Each entry is one line:
`- [stated|observed YYYY-MM-DD] <the preference> → <how to apply it>`

- `[stated]` — the learner said it explicitly. Strong; honor unless it hits the guardrail.
- `[observed]` — inferred from a **stable, repeated** pattern. Weaker; **revisable** the moment
  later behavior contradicts it. Prune stale entries rather than hoarding guesses.

---

## 1. Communication & tone
- [observed 2026-06-15] Values candor about evidence and strength of claims; dislikes
  pop-pedagogy and overselling → be honest about uncertainty and tradeoffs; never quote a single
  effect size as a promise; flag when something is "well-supported" vs. "thin."
- [stated 2026-06-21] **Every sentence must add value — concrete, permanent language rule.** Strip
  ALL of: meta-narration that announces/justifies what's coming ("Before any detail, the map,"
  "let me walk you through"), reassurance and hand-holding ("say 'no idea' freely," "a blank is not
  failure," "take your time"), and self-justifying asides ("so I won't waste your time…"). The
  learner knows they can ask anything — that's why the engine exists; never re-explain the
  interaction model. → keep necessary *explanations* (the actual teaching content); cut everything
  that isn't the map, the question, the fact, or a required instruction. Default to terse; if a
  sentence isn't carrying information, delete it. Supersedes/extends the prior filler entry; pairs
  with §3 clean-scannable-UI.
- [stated 2026-06-15] Will not accept teaching from unverified recall; expects the knowledge base
  to be researched to the subject-research-protocol standard (with cited sources) **before** any
  instruction → for every subject, complete the map/deep pass and cite before teaching; never
  present model-recall as fact. (Holds the engine to its own §0 "researcher is a model" rule.)
- [stated 2026-07-03] **No procedural/self-referential scaffolding language — hard extension of the
  every-sentence-adds-value rule above.** Cut question labels and back-references ("Q1", "the two
  probes still open", "I asked three") and all process/status meta-narration about the teaching act
  itself ("these are the ones that place you", "this calibrates the tree", "diagnosis done"). The
  learner will not spend reading time on the engine's bookkeeping — only the question, the fact, or
  the map. -> ask a question plainly, no label, no rationale for asking it; state a finding only when
  it IS teaching content, never as workflow narration. If a sentence describes the process rather
  than the subject, delete it.
- [stated 2026-09-15] **Terse ≠ assuming knowledge.** A minimal-word file that uses undefined terms
  "is not teaching me, it expects I already know." → keep sentences earning, but define every term
  before its first use, build from the learner's actual level (diagnose; default novice for a new
  subject), and teach before testing with exam questions. Cut filler, never cut the explanation
  steps. Found on ECE2108 study-pack-v2/01; v3 shape (Predict → Build with per-step Checks → Exam
  form → Attempt) is the response.

## 2. Pace & session shape
- [stated 2026-06-21] **Wants pace as fast as possible — "feed big, not small."** Deliver in large
  chunks at speed; do NOT spoon-feed tiny increments by default → present a big block, then use
  frequent retrieval checks to *find where the learner lags*. The retrieval checks are the
  lag-detector and stay non-negotiable (see §7) — they're what makes "feed big" safe rather than
  blind. Default to the top of the difficulty band (principle 4 from above).
- [stated 2026-06-21] **Big chunks stay the DEFAULT; the learner sets when to slow down — not the
  engine.** Do NOT pre-emptively shrink to small steps on a stumble. When a check reveals a lag,
  fix that one piece in place but stay big/fast; only switch into slow, small-step mode when the
  learner explicitly says so → keep big as the standing default; if a check shows real slippage,
  name it and *offer* to slow down on that piece, but don't unilaterally drop into spoon-feed mode.
  Pacing-down is learner-triggered; surfacing the lag is engine-triggered.

## 3. Format & representation
*(NOT modality/“learning styles” — this is about clarity preferences: e.g. likes worked tables,
prefers minimal prose, wants diagrams described, etc.)*
- [stated 2026-06-19] **LaTeX / `$...$` math does NOT render in the learner's terminal — it shows as
  raw symbols and reads as clutter.** Found this teaching stats. → in the **terminal**, write ALL
  math in **plain ASCII**: spell operators in words where clearer ("given", "and"), write fractions
  inline as `top / bottom` or stacked on their own lines, introduce one symbol at a time, keep each
  line short. Never use `$`, `\frac`, `\mid`, or other TeX in the terminal. Pairs with the learner's
  low tolerance for dense notation. → for **genuinely rendered** math/derivations, use the **browser
  lesson surface** (`rendering.md` §2, primitive 1 = MathJax) and reference it by figure/section
  number; the terminal stays ASCII. The tab supplements, never replaces, the terminal dialogue.
- [stated 2026-06-21] **Demands a clean, scannable UI for every teaching session — understandable at
  a glance.** Low tolerance for cluttered, messy output. → structure every teaching turn for
  visual clarity: clear section headers, generous whitespace between blocks, one idea per line;
  prefer short bullets / compact tables over walls of prose; bold the key term/answer being tested;
  consistent layout turn-to-turn so the eye knows where to look. Cut decoration that doesn't carry
  meaning (no emoji spam, no redundant restating). Pairs with §3 ASCII-math and low-dense-notation
  prefs. If a concept needs a diagram, draw a clean ASCII one in the terminal for quick reference —
  or, when it needs real fidelity (a plot, a circuit schematic, a truth/timing grid), render it to
  the **browser lesson surface** (`rendering.md`: primitives 4/5/6) and point at it by figure
  number. Either way the terminal stays uncluttered.
- [stated 2026-06-21] **Wants the bigger picture first — "step back."** When introducing anything
  (subject, chapter, or concept), open with the **concept tree / map**: lay out what's in the whole
  unit and how the pieces connect *before* drilling into any one piece, so the learner has the
  overview to slot details into. → lead every new chapter/subject with a short structural map
  (advance organizer); name where each upcoming concept sits in it; only then go concrete→detail.
  Evidence-aligned: structure-before-detail manages intrinsic load (research/01 §2, research/02 §8–9).
- [stated 2026-06-24] **[SUPERSEDED 2026-07-03 — see the multi-map/flow rule at the end of §3.]**
  ~~The "step back" overview must be the *whole* picture, not just the trunk.~~
  When stepping back, don't show only the main branches — expand **almost all sub-branches** and
  **sum up everything** so the entire map is visible at once. → render the structural map to **full
  depth**: top-level branches **and** their sub-branches (and the notable leaves under those), each
  with a one-line summary of what it is, so the learner sees the complete terrain in a single view
  rather than a skeleton. Keep it scannable (§3 clean-UI: compact tree, one node per line) — full
  *coverage*, not full *prose*. The concept-map-first rule (above) gives the trunk; this makes that
  opening map exhaustive in breadth. Still respects intrinsic-load management: it's a dense **index/
  overview**, the *teaching* of each node still unfolds one concept at a time via the loop.
- [stated 2026-07-05] **Teaching surface = the one-window Tutor Studio, not a terminal/browser
  split.** The learner wants a proper interactive window ("not jugad"): they type, draw, or
  photograph their notebook (camera/paste/drop) in the window, and the teacher answers *in the
  window* with explanation, diagrams, and corrections — one-on-one. → run live sessions through
  `whiteboard.md` Studio mode (`wb.start` → `wb.listen` loop); terminal is the fallback surface
  only. All core principles (retrieval-first, CHECK gating, feedback rules) apply unchanged
  inside the window.
- [stated 2026-07-05] **Refinement — the teacher's content IS the whiteboard (canvas mode).** Not
  a stream with a separate sketch panel: one shared infinite canvas where the teacher's
  explanations/diagrams land as objects and the learner draws/types *directly over them* ("circle
  it and ask why"). Asking sends the annotated board snapshot to the teacher. → default surface =
  `whiteboard.md` §0 canvas mode; read every `ask` event's board PNG before answering; place
  answers near the learner's marks when spatially relevant.
- [stated 2026-07-05] **Images: the teacher may generate OR download, whichever fits the
  situation** (supersedes the engine's old blanket no-generation rule). → prefer programmatic
  generation (plots/schematics/SVG — faithful by construction) for quantitative/structural
  content; download authoritative images (with citation) for what can't be computed; any
  AI-generated imagery (if an API is ever wired) is verified before being taught. Provenance is
  always stated on the figure.
- [stated 2026-07-08] **Amends the 2026-07-05 Studio prefs: Studio/canvas = diagrams and figures
  ONLY, for now.** The learner judges the tool "not polished yet" and too token-heavy for the
  dialogue channel. → dialogue, retrieval, CHECKs, and code exchange run in the **terminal**
  (ASCII rules above); push to the board only what genuinely needs rendering (maps, plots,
  schematics, tables). Studio-as-default resumes only when the learner says the polish is there.
- [stated 2026-07-03] **SUPERSEDES the 2026-06-24 "whole picture in one view" rule.** One big
  full-depth map is too much and reads as messy — the learner cannot find an entry point ("I don't
  even know where to start"). Deliver the overview as **(a) a clean learning-FLOW map first** — the
  ordered path through the major areas, showing sequence + dependencies + the learner's current
  position, ~8-12 nodes, so there is an obvious START and a "you are here / next"; then **(b)
  multiple small connected sub-maps**, one per area, each digestible (roughly 3-6 nodes), instead of
  one exhaustive tree. Maps connect by shared stage numbering/naming. Near-term areas get their
  sub-map now; distant areas stay single nodes on the flow map until we reach them. Full breadth is
  still covered, but split across linked maps + an explicit order — never one dense view. Better
  intrinsic-load management than the superseded rule (principle 3). Applies to **every subject**.

- [stated 2026-09-11] **Use the real symbol, never a spelled-out or ASCII-substitute name — HARD
  rule, every generated document and every terminal turn.** Writing `Sigma-m`, `Pi-M`, `(+)`, `>=`
  forces the learner to decode the substitute back into the symbol: "really costing me precious
  processing time." → write **Σ Π ⊕ ⊙ ≥ ≤ ≠ ± √ ∞ ∈ ∴ Δ Ω μ** and superscripts/subscripts
  (2ⁿ, log₂, Q₀) directly as Unicode. Standard domain notation stays as the domain writes it —
  `A'` for complement, `·` for AND, `+` for OR are correct as-is and are NOT substitutes.
  **This refines, and does not contradict, the 2026-06-19 ASCII-math rule above:** that rule bans
  **TeX** (`$...$`, `\frac`, `\mid`) because it does not render — Unicode symbols render fine
  everywhere, including the terminal, and the knowledge base already used Σm. Applies to
  study-pack generation, lessons, KB files and terminal dialogue alike. Retrofitted across all 10
  Digital Electronics study-pack files the day it was stated.

## 4. Autonomy & choice
*(How much the learner wants to steer — pick next topic, choose examples, set pace. Unseeded.)*

## 5. Scheduling & review cadence
*(Preferred session length, days available, how aggressive the spaced-review queue should be.
Unseeded — defaults to the engine's expanding-interval scheme until set.)*

## 6. Motivation & feedback framing
*(How the learner best receives correction and encouragement, within the feedback protocol.
Unseeded.)*

## 7. Tensions to manage
*(Preferences that rub against a core principle. Recorded here so the engine honors the spirit
without breaking the method.)*
- [stated 2026-06-21] **"Feed big + fast" vs. principle 3 (protect working memory) & principle 4
  (~80% success).** The learner wants large fast chunks; large chunks risk overload, and the only
  way "catch me up" works is if lag is caught *early*. **Honor the spirit** (big blocks stay the
  default, fast, minimal spoon-feeding; pacing-down is learner-triggered, not engine-triggered)
  **while keeping the mechanism:** retrieval checks after each big block stay frequent and
  non-negotiable — they are the lag-detector. On demonstrated overload, do NOT silently drop to
  small steps — *surface* the lag and offer to slow down; switch to slow/small-step mode only when
  the learner says so. Never trade away the checks themselves to go faster — that would make the
  approach blind, not fast. (The check is mandatory; the pacing response to it is the learner's call.)

- [stated 2026-09-11] **"Prepare study .md files I can study from" vs. principle 1 (retrieval)
  and the never-do rule on re-reading.** Files that are read are the weakest study format; the
  learner explicitly asked for them, with an exam near. **Honored the spirit, kept the mechanism:**
  every study file is built **question-first** — Attempt block before any exposition, Self-test
  after, and **answers placed at the bottom, separated from the questions** — so the artifact
  forces retrieval instead of inviting re-reading. The cost was named to the learner in one line,
  not preached. → when the learner asks for reference/study documents in future, build them in this
  shape by default rather than as summaries; do not refuse the format, and do not silently convert
  it into a lecture transcript.

---

## Changelog
- 2026-06-15 — File created. Personalization layer established; one observed universal entry
  seeded (candor about evidence). All other sections unseeded — no subject has run yet.
- 2026-06-15 — First subject (Verilog) created. Added stated §1 preference: research-before-teach,
  no teaching from unverified recall.
- 2026-06-16 — Second subject (Python) created, absolute-zero start. Re-affirmed the §1
  research-before-teach preference (learner again directed a sourced deep dive before any
  instruction); no new universal preference added — existing §1 entry already covers it.
- 2026-06-21 — Added two stated universal prefs: §2 fast pace / "feed big, find the lag, catch up";
  §3 concept-tree / bigger-picture-first. Logged the §7 tension keeping retrieval checks
  non-negotiable as the lag-detector under fast pacing.
- 2026-06-21 — Refined §2/§7: big chunks are the standing default; pacing-down is **learner-
  triggered**, not engine-triggered. Engine still surfaces the lag and offers to slow, but only
  switches to small-step mode on the learner's say-so.
- 2026-06-21 — Added §3 pref: clean, scannable UI for every teaching session (headers, whitespace,
  bullets/tables over prose, no clutter).
- 2026-06-24 — Annotated the two §3 rendering prefs (ASCII-math, clean-UI/diagrams) to route
  genuinely-rendered math/plots/schematics to the new **browser lesson surface** (`rendering.md`),
  keeping the terminal ASCII. No preference reversed — the terminal rules still hold; the tab is an
  added surface. (Closes out the Visual & Rendering subsystem build interrupted by the token shortage.)
- 2026-06-24 — Extended the §3 "step back" pref: the overview map must be **full-depth** (main
  branches + almost all sub-branches + notable leaves, each one-lined), not just the trunk — the
  whole picture in one view. Coverage-exhaustive but still scannable; per-node teaching still
  unfolds one concept at a time via the loop.
- 2026-07-03 — **Superseded** the 2026-06-24 full-depth-map rule: one exhaustive tree read as messy
  ("I don't even know where to start"). New §3 rule: overview = a clean learning-FLOW map (~8-12
  nodes, ordered path + "you are here") **then** small connected per-area sub-maps (3-6 nodes);
  distant areas stay single nodes until reached.
- 2026-07-03 — Added §1 hard extension of every-sentence-adds-value: **no procedural /
  self-referential scaffolding language** (no question labels/back-references, no process/status
  meta-narration about the teaching act). Also logged a Verilog-scoped override the same day
  (no gate-level reproduction drills — see `subjects/verilog/learner-profile.md`).
- 2026-07-05 — *(engine audit)* Changelog back-filled: the two 2026-07-03 entries above were added
  to §1/§3 on the day but never logged here — repaired from the dated entries themselves.
- 2026-07-05 — Added two stated §3 prefs (Teacher 2.0): (1) live sessions run in the **one-window
  Tutor Studio** (type/draw/camera in the window, teacher answers in the window; terminal =
  fallback); (2) teacher images may be **generated or downloaded situationally** (supersedes the
  blanket no-generation rule; provenance always stated). CLAUDE.md Visual protocol §1/§5 updated
  to match; full design in `whiteboard.md`.
- 2026-07-08 — Amended the Studio prefs (learner, mid-session): Studio = **diagrams/figures only**
  until polished (tool judged unpolished + token-heavy); dialogue/retrieval/code stay in the
  terminal. Not a reversal of canvas mode — a scope-down until the polish exists.
- 2026-07-05 — Refined the Studio pref (learner): **canvas mode** — teacher content *is* the
  whiteboard (one shared Excalidraw canvas, learner annotates directly over it, Ask sends the
  annotated board snapshot). Built same day after a tool-research pass (Excalidraw MIT chosen
  over tldraw/licensing and over off-the-shelf apps that can't be engine-driven). Mic added the
  same day (Web Speech, `via:"voice"` read tolerantly).
- 2026-09-11 — Logged a §7 tension: learner requested readable study .md files (Digital Electronics
  MTE). Resolved by making every file question-first with answers separated to the bottom —
  format honored, retrieval mechanism preserved. Sets the default shape for future study documents.
- 2026-09-11 — Added a hard §3 notation rule (learner, mid-session): **real symbols only — Σ, Π, ⊕,
  ≥, superscripts — never spelled-out or ASCII-substitute names.** Reason given: decoding
  substitutes costs reading time. Clarified that it refines rather than reverses the ASCII-math
  rule (TeX is still banned; Unicode is not TeX). All 10 Digital Electronics study-pack files
  retrofitted the same day.
