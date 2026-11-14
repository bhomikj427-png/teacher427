# Pedagogy — Research & Writing Sprints

> **Learner rule (stated 2026-11-15):** deep research runs in sprints. **One sprint = one
> session**, fully finished (researched *and* written), ending with a hand-off below so the next
> session starts from files, never from carried context. A sprint too big to finish splits into
> a/b — it is never half-done.

---

## Sprint protocol (every sprint, fixed order)

**Session entry (before anything else)**
0. `CLAUDE.md` session-start steps 0–0b as usual (load preferences; `git status`, commit any
   leftover work first). Sweep other subjects' spaced-review queues and *report* items due (do not
   run them unless the learner chooses). Research sprints skip the start-of-session learner recall
   (nothing has been taught yet); **the hand-off below is the resume.** The trigger phrase is just
   the sprint id ("S2").

**Start (context hygiene)**
1. Read only: this file's *Current hand-off* block → the sprint's **Inputs** list → `CLAUDE.md`
   rules already loaded. Do not read other KB files "for context"; if a file is needed, it must
   be in Inputs.
2. Log the sprint start in `progress-log.md` (log-first rule).

**Research**
3. Every load-bearing claim verified at a **primary or tier-1 source this session** (paper,
   meta-analysis, the person's own book/text). Web-summary pages and AI summaries are leads only.
4. Effect sizes: quote with study, N/k, and the caveat (publication bias; `research/07`). Never
   a single number as a promise.
5. Unverifiable this session → tag `uncertain` and add to the verify backlog; never written as fact.
5b. **Write-as-you-verify (learner-confirmed 2026-11-15).** Research and KB writing happen in the
    same sprint, interleaved claim by claim: verify one claim at its source → write it into the KB
    file immediately (source + confidence tag) → next claim. Never batch "research everything, then
    write" — a mid-session context compaction must never lose verified-but-unwritten findings.
    Study-pack writing is a different job and stays in its own sprints (S14+), built only from
    finished KB files.

**Write (content standard — a file is "done" only if all hold)**
6. Each claim carries a source + confidence tag (`settled` / `contested` / `uncertain` / `suspect`).
7. Each topic states the **mechanism** (why it works in the brain), not just the finding.
8. Every Part A topic is tagged with the **information type(s)** it concerns; every Part B entry
   ends with: *serves → Part A type* · *grade S/M/T/X* · *use as learner* · *use as teacher*.
9. **Misconceptions are a first-class output (learner-set 2026-11-15).** For every unit in the
   sprint: (a) write the full entry for each misconception it owns, in `misconceptions.md`
   format: *belief → why it feels true (the mechanism that makes it tempting) → correction with
   evidence and source ID → the question that exposes it → the unit that teaches it*; (b) **hunt**
   for new ones: at least 3 new per Part A unit, from the sources read that sprint, from common
   student/teacher beliefs, and from popularizer claims; (c) move each through the status ladder
   `seed → written → verified` (verified = correction checked at full text in Stage 2).
   A unit is not done while it has a `seed` misconception. Sources go to
   `knowledge-base/sources.md` (tiered); changes to `knowledge-base/CHANGELOG.md`.

**Close**
10. Self-check the sprint's **Done-when** list item by item; anything failing → stays open in the
    hand-off (sprint marked `partial`, never `done`).
11. Move every open item into **Verify backlog** (below; it persists, the hand-off is overwritten).
    Overwrite *Current hand-off* (template below); tick the sprint in the table; update
    `00-map.md` stage line if the stage changed; progress-log resume; commit + push.

---

## Sprint table

| # | Sprint | Inputs (read only these) | Outputs | Done when | Status |
|---|---|---|---|---|---|
| S0 | Scaffold + roster | — | progress-log, profile, 00-map, roster.md | roster ≥ 5 tiers, provisional grades | **done 2026-11-15** |
| S1 | **Map pass** | 00-map, roster | 00-map §prereq graph + threshold concepts; `sources.md` (tiered canon); `misconceptions.md` seed; **A3 framework decision** (which taxonomy is the spine); `justin-sung-claims.md` (inventory of his claims, each mapped to a research question) | prereq graph covers A1–A8 + B tiers; canon has ≥1 tier-1 source per unit; Sung inventory ≥ 15 claims with video/source refs | **done 2026-11-15** → stage-1 |
| S2 | A1 studying vs learning + A2 memory architecture | 00-map, sources, misconceptions | `A1-studying-vs-learning.md`, `A2-memory-architecture.md` | learning/performance, storage/retrieval strength, fluency illusions, WM limits, encoding→consolidation→retrieval, forgetting curve (replication) all sourced | **done 2026-11-15** |
| S3 | **A3 taxonomy of information** (the hub) | 00-map, sources, A1, A2 | `A3-kinds-of-information.md` | each type defined with an example, brain system, and how it fails; declarative/procedural, Krathwohl 4, Gagné 5, primary/secondary, element interactivity, SOLO, perceptual, motor reconciled into one table | **done 2026-11-15** |
| S4 | A4 bridge (type → method) + A5 schemas/expertise/transfer | 00-map, sources, A3 | `A4-type-to-method.md`, `A5-schemas-expertise-transfer.md` | bridge table: every A3 type → best-evidenced methods + grade; KLI framework checked; transfer near/far honest | **done 2026-11-15** |
| S5 | A6 depth/generative learning + A7 metacognition | 00-map, sources, A3, A4, justin-sung-claims | `A6-depth-and-generation.md`, `A7-metacognition.md`; Sung claims touched here marked | levels of processing, generation, elaboration, concept maps (meta), advance organizers, pretesting; calibration + SRL sourced | |
| S6 | A8 myths + Part A integration | all A files, misconceptions | `A8-myths.md`; cross-link pass; Part A README | every A file links to A3 types; no orphan claims | Part A stage-1 |
| S7 | B1 historical teachers | roster §1, A3, A4 | `B1-historical.md` | each roster §1 entry written to protocol step 8 or dropped with reason | |
| S8 | B2 mid-century method-builders + B3 classroom legends | roster §2–3, A3, A4 | `B2-method-builders.md`, `B3-classroom-legends.md` | same; Feynman-technique attribution sourced | |
| S9a | B4 researchers: memory & practice (Bjorks, Roediger/Karpicke/McDaniel, Dunlosky/Rawson, Rohrer/Carpenter, Woźniak, Matuschak/Nielsen, Ericsson, Kellman) | roster §4, A3, A4 | `B4a-researchers-memory.md` | same | |
| S9b | B4 researchers: instruction (Rosenshine, Sweller, Mayer/Fiorella, Kapur, Chi, Wiliam, Mazur, Wieman, Willingham, Kirschner/Hendrick, Agarwal, Learning Scientists, Nuthall, Hattie) | roster §4, A3, A4 | `B4b-researchers-instruction.md` | same; Hattie written as a methodology case | |
| S10 | B5 practitioners + **full Justin Sung audit** | roster §5, justin-sung-claims, A1–A8 | `B5-practitioners.md`, `justin-sung-audit.md` (each claim: verdict + evidence) | every Sung claim verdicted; rebuttal-video located or logged as not found | **stage-1✓** |
| S11 | Stage 2 — Part A verification sweep | all A files, sources | corrections in A files + CHANGELOG | every effect size checked at the paper; `uncertain` tags resolved or kept with reason | |
| S12 | Stage 2 — Part B verification + A↔B matrix | all B files, A3, A4 | `matrix.md` (info type × teacher/method × grade) | every B grade re-checked; matrix complete | |
| S13 | §0 surplus test + integrity audit | everything | audit note in CHANGELOG; 00-map stamp | surplus test recorded; zero unsourced claims | **stage-2✓** |
| S14 | Study-pack pilot (v1.2 spec) | study-pack-format.md, reference files, A1, A3 | `study-pack/00-START-HERE` + one topic file | learner sign-off | |
| S15+ | Pack build in START-HERE priority order | spec + the topic's KB file | one or two topic files per session | each file passes spec checks | |

---

## Hand-off template (overwrite *Current hand-off* each sprint end)

```
Sprint: Sx — <name> — done | partial (date)
Written: <files, one line each, with what they now contain>
Verified this sprint: <key claims + source>
Open (carried): <unverified claims, leads, anything failing Done-when>
Decisions made: <framework/scope choices the next sprint must respect>
Next sprint: Sy — first action: <one concrete step>
Read at start: <exact file list = Sy Inputs>
```

## Verify backlog (persistent — items leave only when resolved, with the sprint that closed them)

| Item | Raised | Close in |
|---|---|---|
| Schroeder et al. 2017 vol/pages; Nesbit & Adesope 2006 overall pooled ES + subgroup g values at full text | S1 | S5 |
| Barnett & Ceci 2002 exact dimension list (3 content + 6 context?) | S1 | S11 (not closed in S4) |
| Dunlosky et al. 2013 moderate-utility list at full text | S1 | S11 (not closed in S4) |
| Zimmerman 2002 exact phase labels | S1 | S5 |
| Dunlosky & Rawson 2012 → add to canon | S1 | S5 |
| BB92 chapter editors/pages (from recall) | S2 | S11 |
| RK06 one-week 61% vs 40% (press release) → paper's table | S2 | S11 |
| PR18 effect sizes 0.40 / 0.28 / 0.58 at full text | S2 | S11 |
| A2: priming → neocortex (not in Sq04 abstract) | S2 | S11 |
| LTM "no practical capacity limit" — find a source or drop | S2 | S11 |
| Justin Sung: locate the Learning-Sciences-PhD response video; caption-check every `digest` claim | S0/S1 | S10 |
| Roster open leads (Montessori meta, Kumon RCT full text, Nuthall 3 encounters, Suzuki/Moore evidence, gurukul/chavruta) | S0 | S7–S9b |
| S2 closed: Squire vol/issue ✓, BB92 + KB11 + PR18 added to canon ✓ | — | — |
| S3 closed: Krathwohl procedural wording ✓ (full text) · KLI typology ✓ (CRK22 full text) · Gagné ✓ (G84 full text replaces 1985 edition) | — | — |
| KCP12 original KC table + whether category learning sits under induction (A3 row 2) | S3 | S11 |
| CKS17 vol/pages + verbatim intrinsic-load sentence | S3 | S11 (not closed in S4) |
| CRK22 proceedings page numbers; look for replications of the fact/skill × practice/example interaction | S3 | S11 (not closed in S4) |
| KMS10 perceptual-learning efficacy (A3 row 7 is `uncertain`) | S3 | S11 (not closed in S4) |
| ATS17 numeric g (full-text host dead; engine seed g≈0.5–0.7 unverified) | S4 | S11 |
| BR19: no/reversed interleaving benefit for words/expository text — confirm at full text | S4 | S11 |
| SK21 vol/pages + how the bias-adjusted g = 0.87 was computed; fidelity moderator | S4 | S11 |
| GH80/83 solution percentages (10 / 30 / 75–92 / 52%) at full text | S4 | S11 |
| MHO14 vol/pages | S4 | S11 |
| Rawson et al. 2013 successive relearning → add to canon (A4 row 1 grade is seed-level) | S4 | S5 |
| Engine-seeded misconceptions M14 (learning pyramid), M15 (2σ), M17 (minimal guidance) → re-verify at primary source | S1 | S6 / S9b / S4 |

## Current hand-off

```
Sprint: S4 — A4 kind → method bridge + A5 schemas/expertise/transfer — done (2026-11-15)
Written: knowledge-base/A4-type-to-method.md (13-method evidence table with S/M/T grades and
  boundaries; A3 row → first choice / also / avoid; 3 cross-cutting rules: expertise changes the
  method, guidance-first vs productive failure reconciled by prerequisites, difficulty only within
  reach; encoding-vs-retrieval framed as "both, by row") · A5-schemas-expertise-transfer.md (chess
  chunks; novice surface vs expert structure; transfer taxonomy, analogy noticing bottleneck, schema
  induction from compared analogs; deliberate practice sized by domain) · misconceptions M6/M8/M9/M17
  written + new M31–M36 (36 total, 30 written) · sources +9 (47 total) · 00-map · CHANGELOG ·
  Sung claims file (A4 §4 pointers)
Verified this sprint: abstract level for all 9 new sources (no full text this sprint); several
  S3-backlog items NOT closed → re-targeted to S11 (marked in backlog)
Open (carried): Verify backlog — S5 row: Rawson 2013; plus S11 rows
Decisions made: method grades S/M/T fixed in A4 §1 — Part B grades must cite these; productive
  failure vs explicit instruction treated as compatible (prerequisites + instruction afterwards);
  engine notes for S12: ROUTE for all A3 rows; teach-back names the deep principle
Next sprint: S5 — A6 depth & generative learning + A7 metacognition. First action: Dunlosky &
  Rawson 2012 (overconfidence / judgments of learning) + Rawson et al. 2013 successive relearning;
  then A6: generation effect (Slamecka & Graf 1978; Bertsch 2007 meta), ICAP (Chi & Wylie 2014),
  advance organizers (Ausubel; Luiten 1980 meta), Justin Sung J2/J3/J9–J14
Read at start: sprints.md, knowledge-base/00-map.md, knowledge-base/sources.md,
  knowledge-base/misconceptions.md, knowledge-base/A3-kinds-of-information.md,
  knowledge-base/A4-type-to-method.md, knowledge-base/justin-sung-claims.md
```
