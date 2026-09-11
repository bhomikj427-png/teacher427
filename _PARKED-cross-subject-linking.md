# PARKED DESIGN — Cross-subject concept linking (+ roadmap-as-live-tracker)

> ⚠ **PARKED. NOT IMPLEMENTED. NOT PART OF THE LIVE CONTRACT.** Do **not** consult this during
> teaching or treat any rule here as active. The engine was deliberately **reverted to its
> pre-session baseline on 2026-06-30** after a design discussion — nothing in this concept was kept
> in the running engine. This file is a **complete handoff** so a future session can design-finalize
> and *then* build it cleanly. Read it end-to-end before touching the engine for this feature.
>
> **Why parked:** the learner correctly stopped premature implementation. Two open design problems
> (the structural-tag vocabulary; per-concept-files vs spine) must be settled *before* any build. The
> learner's standing instruction this session: **discuss/design first, build only when settled.**

---

## 0. What the learner actually asked for (two related features)

- **F1 — Cross-subject concept linking.** While teaching concept **C** in subject **A**, surface a
  genuinely-related concept from **any other subject** — to *teach from* (analogy) or *contrast
  against* — when it helps. Explicitly includes both directions: a concept already **owned** (prior /
  mastered) **and** one **not yet learned** (future). The learner's framing: *"if it's a concept I
  know by heart, we can use that to teach new concepts, be that of any subject."*
- **F2 — Roadmap as a live progress tracker.** Make `subjects/_career-roadmap/roadmap.md` track *how
  far across a track* the learner is (teaching progress, not just KB status). **Separable and
  simpler** than F1 — could ship on its own.

The learner also specified the *shape* of F1's machinery: a **"linker pass"** that runs **as a step
in building any KB**, finding and connecting the new subject's concepts into the web that already
exists — **without** reading every existing KB (token cost is the constraint).

---

## 1. Why this is evidence-aligned (it must pass the engine's bar)

- **Elaboration / connect-to-prior-knowledge.** Learning binds new material onto existing schema;
  richer connections = more durable + transferable. *[research/02; the loop's ACTIVATE]*
- **A *secure* anchor costs almost no working memory.** A concept "known by heart" is chunked in
  long-term memory, so invoking it adds little extraneous load — *protecting* principle 3. Anchoring
  on a *half-known* "related" concept instead *spends* WM. *[research/01 §2, principle 3]*
- **∴ The gate is structural-analogy + anchor-security, NOT subject-domain proximity.** This was the
  learner's key insight and it sharpens the whole design: a mastered concept from an *unrelated*
  subject is a *better* teaching anchor than a shaky one from a related subject.

**Hard constraints that must never be violated (these killed naive versions):**
1. **Teaching gate (`stage-2✓`) holds across subjects.** You may *teach* a linked concept only if its
   subject's KB is complete. A not-yet-learned / unbuilt concept may be **signposted/previewed**,
   never lectured.
2. **WM protection.** A link is one clean sentence/figure then back to **C**. If it fragments the
   concept or spends WM the learner needs now, **drop it.** The link is a bonus, never the spine.
3. **Retrieval-first.** Prefer *asking* for the bridge ("what does this remind you of?") over
   supplying it. The link never replaces CHECK / TEACH-BACK.
4. **No fuzzy similarity.** A plausible-but-wrong analogy is a **planted misconception** — same
   liability as a plausible-wrong figure (`rendering.md` §5). Links must be *individually
   defensible*, not statistically plausible. (See §6 — the external system makes this its core stance.)

---

## 2. The real problem decomposition (what's actually hard)

A side-registry "of links" is the wrong frame; it only addresses the easy part. The four sub-problems:

| Sub-problem | Status | Notes |
|---|---|---|
| **Retrieval** — cheap lookup of a concept's links at teach time | *easy / solved-in-principle* | scoped query against a compact index (§5); never load the whole corpus |
| **Discovery** — how a link is *found* in the first place | **the linchpin, unsolved** | cross-domain prose never names the other subject → reference-following (the external system's method) does NOT transfer. Needs the **structural-tag vocabulary** (§7) |
| **Ranking / worth** — is this link worth teaching; which is best | *direction set* | NOT a numeric score. Typed editorial gates + computed node degree (§6). "Best" depends on current mastery → evaluated live against the ledgers |
| **Freshness** — re-evaluate when any subject changes | *direction set* | global rebuild + deterministic audit (§6), not a drifting incremental index |

---

## 3. Decisions LOCKED this session (do not relitigate without cause)

- **D1 — Link, don't move.** Verilog stays at `subjects/verilog/`; the roadmap is a *linked tracker*,
  not a parent folder. Subjects stay flat; the `_`-prefix = engine-meta convention is preserved.
  (Moving Verilog under `_career-roadmap/` was rejected: breaks two conventions, makes non-roadmap
  subjects asymmetric.)
- **D2 — Scope = the whole `subjects/` tree.** Links may span *any* two subjects. The gate is
  structural analogy + anchor-security, **not** roadmap membership or domain. (Roadmap membership is a
  *separate axis* — F2, not F1.)
- **D3 — The linker pass is EAGER.** It verifies and writes edges at **KB-build time**, not lazily at
  teach time. Cost is a *bounded one-time* pass per subject (small after blocking); in return the
  graph is complete and queryable the moment a subject lands. The learner chose eager explicitly.

## 4. Decisions LEANING / COUPLED (resolve together, not yet final)

- **Edge storage — edge-list vs inline.** Two viable models, now known to be **coupled to the
  per-concept-files decision**:
  - *Separate edge-list file* (a normalized `from,to,type,…` table): edge stored once, mutation/audit
    centralized, easy to manage with **per-unit** KBs. (My initial recommendation.)
  - *Inline in each concept's `## Links` block* (the external system's way): works **because** edges
    are stored **forward-only** and backlinks are computed by grep, plus a deterministic auditor
    catches breakage — which neutralizes the duplication/drift objection. Presumes **per-concept
    files**.
  - **Coupling:** inline ↔ per-concept files; edge-list ↔ per-unit KBs. Decide storage *with* the
    next item.
- **Per-concept files vs derived spine — PARKED (learner deferred).** The external spec tilts toward
  **per-concept files** (filename = node ID, inline edges, grep-backlinks all assume it). But our KBs
  are currently **per-unit** (`01-…md … 12-…md`); refactoring to per-concept granularity is a large
  change. A middle path: keep per-unit KBs and **derive** the concept spine from each `00-map.md`
  (cheaper, but the spine can drift from the KB unless rebuilt). Unresolved — the learner wants to
  weigh this separately.

---

## 5. Token-management architecture (agreed shape — "linker pass without reading all KBs")

The web is **not** the KBs; it's a compact index. Discovery is **two-stage** (blocking → verify):

1. **The spine / manifest.** One small file, **one short row per concept** across all subjects:
   `id · subject · concept-name · one-line deep-structure descriptor · structural-tags`. Derived from
   each subject's `00-map.md` (which already enumerates big ideas + threshold concepts). *This* is
   what the linker reads — never the full KBs. (≈ the external system's `MANIFEST.tsv`.)
2. **Stage 1 — candidate generation (cheap, global).** For each concept in the *new* subject, find
   candidates by **shared structural-tag across a *different* subject** (the blocking key, §7). Reads
   only: the new subject's concepts + the spine. Output: a short candidate list.
3. **Stage 2 — verification (expensive, tiny N).** Only for those few candidates, read the **two
   specific concept notes** to confirm the analogy is *structural* (not surface), type it, and write
   the edge. Full-text reading happens for a handful of pairs, never the corpus.
4. **Cost** ≈ `spine + (k candidate pairs × 2 notes)`, independent of how many KBs exist.
   **Incremental:** only the new subject's nodes get linked; existing edges persist.

---

## 6. External system spec — the learner's *other* concept-linker (ADOPT / ADAPT / REJECT)

The learner runs a separate source-grounded knowledge-graph system whose whole purpose is linking
concepts (concepts = individual Markdown files). Its full portable spec was reviewed. Verdict: **very
useful — adopt the skeleton; adapt one part; reject one part.**

**ADOPT (lift wholesale):**
- **Compact manifest** instead of any embedding/ANN store → our spine (§5).
- **Closed, TYPED edge vocabulary; no generic "related"; NO weights.** Every edge commits to exactly
  one type or is dropped. This *is* the answer to "what's worth teaching": typed editorial gates, not
  a score.
- **Store each edge once; compute the reverse** (forward-only directional edges; backlinks by grep).
- **Deterministic GLOBAL rebuild + AUDIT** (not incremental — incremental indexes drift). The auditor
  flags: dangling stubs, orphans, illegal type-combos, and **phantom targets** (a link target within
  edit-distance 1 of a real file = a typo spawning a stray node). *This auditor is the "can't
  silently rot" guarantee the learner demanded.*
- **Editorial-author + machine-validate; NEVER machine-propose by similarity.** Their core stance:
  fuzzy similarity is the enemy (false equivalence). Aligns exactly with our constraint §1.4.
- **Node importance = computed degree** (how many concepts independently link it), an *output* not an
  input → hub concepts are natural high-value teaching anchors.

**Their edge types ≈ our pedagogical types (strong transfer):**
- `structurally-parallel-to` = our **ANALOGY** (build on it). e.g. Verilog `<=` ↔ Python swap.
- `often-conflated-with-NOT-equivalent` = our **CONTRAST / misconception-trap** — the *highest-value*
  link, because pre-empting a false equivalence is worth more than a plain analogy (e.g. Verilog T1:
  "looks like a program, isn't"). Their legal two-type combo (`structurally-parallel-to` +
  `often-conflated-with-NOT-equivalent`) = "really similar, but not identical" — exactly the T1 move.
- We'll also want a directional **PREREQUISITE / builds-on** type for forward signposts.

**ADAPT:**
- **Blocking key is INVERTED.** Theirs blocks *within* a family (tradition) for clustering. We must
  block **across** subjects on a **shared structural-tag** — because cross-subject links are the whole
  point (blocking within-subject would suppress exactly what we want).

**REJECT (doesn't transfer):**
- **Reference-following discovery.** Theirs finds candidates from names that appear in a concept's own
  prose (Rāhu's story literally names `samudra-manthana`). Our cross-domain analogies are **never**
  named in either side's prose (the Verilog KB won't mention Python). So discovery must come from the
  **structural-tag vocabulary** (§7), which is the one piece their system doesn't hand us.

---

## 7. THE net-new design problem for the future session: the structural-tag vocabulary

This is the **linchpin** — everything else is settled or adopted. Cross-domain discovery needs a
small set of **domain-neutral STRUCTURAL tags** that name *what a concept is shaped like*, not what
domain it's in. A concept gets tagged when authored; the tag is **both**:
- the **blocking key** (candidates = concepts sharing a tag in a *different* subject), and
- the **discovery seed** (replaces reference-following, which can't work cross-domain).

Then Stage-2 verification confirms the analogy is real and assigns the typed edge + a human
justification note.

**Example tag candidates** (illustrative, not final): `simultaneous-update / deferred-RHS-eval`,
`execution-order`, `concurrency-default`, `finite-state`, `binary-representation`,
`gate-level-mapping`, `parameterized-structure-gen`, `undefined-value`, `verification-assertion`,
`recursion`, `type-coercion`.

**Open questions to settle before building:**
- Who defines the vocabulary, and is it **fixed or extensible**? (Risk: ballooning into uselessness.)
- **Granularity** — too coarse → too many false candidates at Stage 1; too fine → misses real links.
- Where tags live (front-matter of concept files? a column in the spine?).
- How to keep two authors (or two build passes) from inventing divergent tags for the same structure
  (a controlled list + an audit for near-duplicate tags, mirroring the phantom-target check).

---

## 8. Seed content to preserve (real candidate links identified this session)

Start the eventual build with these — already vetted as genuine, with readiness flagged. **Readiness
rule:** *teachable-now* only if the OTHER subject's KB is `stage-2✓`; otherwise *signpost-only*.

| A-side (Verilog) | L-side | Type | Tag (provisional) | Readiness |
|---|---|---|---|---|
| Nonblocking `<=` (all RHS eval, *then* assign) | Python `a, b = b, a` | analogy (**strongest**) | simultaneous-update | teachable-now |
| Sequentiality *inside* a procedural block | Python top-to-bottom execution | contrast (conflated≠equiv; pre-empts T1) | execution-order | teachable-now |
| Concurrency default (`assign`/`always`/`initial` all parallel) | Python single-threaded default | contrast | concurrency-default | teachable-now |
| Self-checking testbench (expected vs actual) | Python `assert` / expected-vs-actual | analogy | verification-assertion | teachable-now |
| `parameter` / `generate` | Python comprehensions / factory fns | analogy (loose) | parameterized-structure-gen | teachable-now |
| 4-state `0/1/x/z`; `x` = unknown | Python `None` / sentinels | contrast (loose — flag disanalogy) | undefined-value | teachable-now |
| FSM coding (state reg + next-state + output), U7 | Digital Electronics Moore/Mealy | analogy | finite-state | **signpost** (DE KB not built) |
| Synth subset → gates/flip-flops, U10 | Digital Electronics gate-level | analogy | gate-level-mapping | **signpost** |
| Bit-vectors / two's-complement, U2 | Digital Electronics number systems | analogy | binary-representation | **signpost** |

(Verilog and Python KBs are both `stage-2✓`. The sem-3 subjects, incl. Digital Electronics, have
`course-info.md` only — no KB — hence signpost-only until built.)

---

## 9. F2 — Roadmap-as-live-tracker (separable; can ship independently of F1)

Self-contained design, ready to build on its own:
- **Track-status table → teaching-progress columns:** `KB | Teaching progress (units taught/total,
  e.g. U3/12) | Mastered (ledger count) | Last taught`.
- **Subject declares membership** via a `Roadmap: Goal N` pointer at the top of its `progress-log.md`.
- **Reflected upward at wrap-up:** copy the subject's current teaching position + mastery count into
  the roadmap table — *concrete-entries-only*, same no-drift rule as the subject log; the subject log
  is **ground truth**, the table is a **mirror**.
- **Roadmap operating rules to add:** (6) reflect-progress-upward; (7) cross-links are a *separate
  axis* from roadmap membership. Neither ever authorizes teaching from a roadmap row (the `stage-2✓`
  gate stands).

---

## 10. Teaching-loop integration (where F1 hooks, once built)

- **Hooks:** ACTIVATE (surface the owned anchor as the prior knowledge to build on), PRESENT
  (anchor/contrast the new concept), INTERLEAVE (once *both* concepts are solid, mix so the learner
  picks which model applies). **Never** overrides CHECK / TEACH-BACK.
- **Direction rule:** backward (owned/mastered → teach) freely; forward (not-yet-learned) =
  **signpost/preview only**, never teach (gate + WM).
- **Consult mechanism:** scoped lookup keyed by the current unit/concept against the spine — pull only
  that concept's edges, never the whole graph (§5). Cost bounded by the lesson in front of you.

---

## 11. Suggested build order for the future session

1. **Finalize the structural-tag vocabulary** (§7) — the linchpin; nothing else can be sound first.
2. **Resolve per-concept-files vs derived spine** (§4) — and with it, edge storage (inline vs
   edge-list), since they're coupled.
3. **Define the edge schema + closed type vocabulary + audit rules** (§6).
4. **Add the linker pass + manifest generation** as an explicit step in `subject-research-protocol.md`
   (KB build) and the `subjects/README.md` creation flow.
5. **Add teaching-loop hooks + the consult mechanism** to `CLAUDE.md` (§10) — minimal, surgical.
6. **Seed with §8's candidate links; run the audit; verify clean.**
7. **(Independent track) Ship F2** (§9) whenever — it doesn't depend on F1.

---

## 12. What was reverted this session (engine is at pre-session baseline)

All of the following premature edits were undone on 2026-06-30; the engine behaves exactly as before:
- **Deleted:** `subjects/_cross-links.md` (a hand-curated registry + consult-index — the wrong
  artifact; superseded by this design).
- **`CLAUDE.md`** — removed a "Cross-subject links" section, a session-end roadmap-reflection line,
  and two File-map entries. Restored to original.
- **`subjects/_career-roadmap/roadmap.md`** — reverted the Track-status table and removed operating
  rules 6–7. Restored to original.
- **`subjects/verilog/progress-log.md`** — removed the `Roadmap`/cross-anchor header block.
- **`subjects/verilog/curriculum.md`** — removed the cross-subject-anchors header block.

## 13. Meta-lesson (for whoever maintains the engine)

The learner flagged premature building **twice** this session. For engine-architecture changes:
**design and settle the open questions first, build only when the learner signs off.** Park, don't
prototype, until the linchpin (here, the tag vocabulary) is decided.
