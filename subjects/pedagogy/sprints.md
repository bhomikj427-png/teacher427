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
| S5 | A6 depth/generative learning + A7 metacognition | 00-map, sources, A3, A4, justin-sung-claims | `A6-depth-and-generation.md`, `A7-metacognition.md`; Sung claims touched here marked | levels of processing, generation, elaboration, concept maps (meta), advance organizers, pretesting; calibration + SRL sourced | **done 2026-11-15** |
| S6 | A8 myths + Part A integration | all A files, misconceptions | `A8-myths.md`; cross-link pass; Part A README | every A file links to A3 types; no orphan claims | **done 2026-11-15** (Part A written) |
| S7a | B1 historical teachers: Socrates → Herbart | roster §1, A3, A4 | `B1-historical.md` §1–7 + summary | each of the 7 entries written to protocol step 8 or dropped with reason | **done 2026-11-15** |
| S7b | B1 historical teachers: Fröbel → Skinner (10) | roster §1, A3, A4, B1 (summary only) | `B1-historical.md` §8–17 + full summary | each of the 10 entries written to protocol step 8 or dropped with reason | **done 2026-11-15** (B1 complete) |
| S8a | B2 mid-century method-builders (Keller, Bloom, Gagné, Ausubel, Bruner, Engelmann, Kumon, lesson study, Oxbridge tutorial, Freire) | roster §2, A3, A4, B1 (summary only) | `B2-method-builders.md` | each entry to protocol step 8; M15 (2σ) seed written | |
| S8b | B3 classroom legends (Feynman, Escalante, Collins, Khan) | roster §3, A3, A4, A8 §2 myth 7 | `B3-classroom-legends.md` | same; Feynman-technique attribution sourced | |
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
| Nesbit & Adesope 2006 pooled ES + whether 0.82/0.37 is an NA06 subgroup (Sch17 closed S5: 30(2) 431–455; g 0.58, construct 0.72, study 0.43) | S1 | S11 (part-closed S5) |
| Barnett & Ceci 2002 exact dimension list (3 content + 6 context?) | S1 | S11 (not closed in S4) |
| Dunlosky et al. 2013 moderate-utility list at full text | S1 | S11 (not closed in S4) |
| Zimmerman 2002 exact phase labels + sub-processes (Bath PDF host dead in S5) | S1 | S11 |
| S5 closed: DR12 + RDS13 added to canon ✓ (numbers still open, rows below) | — | — |
| BB92 chapter editors/pages (from recall) | S2 | S11 |
| RK06 one-week 61% vs 40% (press release) → paper's table | S2 | S11 |
| PR18 effect sizes 0.40 / 0.28 / 0.58 at full text | S2 | S11 |
| A2: priming → neocortex (not in Sq04 abstract) | S2 | S11 |
| LTM "no practical capacity limit" — find a source or drop | S2 | S11 |
| Justin Sung: locate the Learning-Sciences-PhD response video; caption-check every `digest` claim | S0/S1 | S10 |
| Roster open leads (Kumon RCT full text, Nuthall 3 encounters, gurukul/chavruta) — S7b closed: Montessori meta (Ra23 + Li25), Suzuki (LWW24), Moore (none found; IBL La14) | S0 | S8a–S9b |
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
| DR12 numbers (overconfidence → early stopping → retention) — abstract elided by publisher | S5 | S11 |
| RDS13 course-exam / long-term retention numbers (≈40% month-later claim is secondary) | S5 | S11 |
| DB08 mean ES 0.69 + moderators at full text | S5 | S11 |
| RT11 cue-only vs cue-target JOL split (0.70 vs 0.03 via Tekin & Roediger 2021) | S5 | S11 |
| Morris, Bransford & Franks 1977 transfer-appropriate processing — read primary | S5 | S11 |
| Pan & Carpenter 2023 prequestion review (answer-must-follow condition) | S5 | S11 |
| LAA80 third author spelling (Ackerson/Ackerman) + any numeric ES; Stone 1982 vs 1983 | S5 | S11 |
| Engine-seeded M15 (2σ) → re-verify at primary source (M14 closed S6 via LH18; M17 closed S4 via KSC06) | S1 | S9b |
| "10% of the brain" + coordination exercises / Brain Gym: find a primary refutation or drop from A8 | S6 | S11 |
| P08 full text (meshing criterion wording; number of studies) | S6 | S11 |
| Y19 effect sizes (grades, lower-achievers) at full text | S6 | S11 |
| Feynman Technique: check Gleick *Genius* / Feynman's own texts for any described method; Scott Young's 2011 post body | S6 | S10 |
| Dek12 "commercial programmes" link — confirm wording in abstract | S6 | S11 |
| SK22 moderators (text type, delay, age) at full text | S7a | S12 |
| FMSG14 numbers (how many studies, outcomes) — abstract elided by publisher | S7a | S12 |
| FN18 vol/pages (Educational Review 71(4) 403–422 from recall); No22 author list beyond first | S7a | S12 |
| EC05 exact title/pages; ideally read Rein directly for the five steps | S7a | S12 |
| RS1599 translator (Farrell 1970?) for the Kolbe English text | S7a | S12 |
| *Orbis Pictus* "first illustrated textbook" — find a primary/scholarly source or soften | S7a | S12 |
| CSJ01 full text: prompt-only condition N, measures | S7a | S12 |
| Vyg78 primary read (ZPD wording p. 86) + Chaiklin 2003 chapter | S7b | S12 |
| Sm25 full text (effect sizes, conditions); WBR76 full text (six functions — 1976 or 1978?) | S7b | S12 |
| KCE80 effect size (programmed instruction, college) — numbers not found | S7b | S12 |
| LM96 abstract/full text; any Piaget primary for stages | S7b | S12 |
| Fröbel gifts/occupations primary (*Pedagogics of the Kindergarten*); Moore method primary accounts (Parker 2005); Suzuki *Nurtured by Love*; Pólya *How to Solve It* | S7b | S12 |
| La14, LWW24, Sk22, Li17 co-author lists / volume numbers | S7b | S12 |

## Current hand-off

```
Sprint: S7b — B1 historical teachers, Fröbel → Skinner — done (2026-11-15); B1 complete
Written: knowledge-base/B1-historical.md §8 Montessori, §9 Vygotsky (+ scaffolding), §10 Skinner,
  §11 Dewey, §12 Piaget, §13 Fröbel, §14 Ebbinghaus (pointer to A2), §15 Pólya, §16 R. L. Moore,
  §17 Suzuki; "Summary (B1, all 17)" table + B1 pattern (4 points) · misconceptions M53–M56 ·
  sources +19 (98 total)
Verified this sprint: full text — Montessori Handbook, Skinner 1958, Democracy and Education,
  Education of Man, Schoenfeld 1992; abstracts — Li17, Li25 (PNAS 2025 national RCT), Ra23
  (g 0.24 academic), WWM78, VVB10, Sm25 (failed replication), LH16 (d 0.50), Sk22, La14, LWW24
Open (carried): backlog rows added S7b (Vygotsky primary, Sm25/WBR76 full text, KCE80 numbers,
  LM96, Fröbel/Moore/Suzuki/Pólya primaries, co-author lists)
Decisions made: §8 Montessori written out of birth order (tested as a package) — numbering is final;
  Ebbinghaus kept as a pointer entry (scientist → A2). "Grade method / mechanism" two-part format
  kept. S8 split into S8a (B2, 10 entries) and S8b (B3, 4 entries)
Next sprint: S8a — B2 method-builders. First action: write M15 (2-sigma) properly — Bloom 1984
  (Educational Researcher 13(6) 4–16) at primary + VanLehn 2011 + Nickow et al. 2020 tutoring meta;
  then Keller PSI (Kulik, Kulik & Cohen 1979; Kulik, Kulik & Bangert-Drowns 1990 mastery meta),
  Engelmann DI (Stockard et al. 2018, RER), Kumon (J. Human Capital RCT), Gagné nine events
  (link to A3 §2.2 G84), Ausubel (link to A6 §5 LAA80), Bruner (spiral, CPA; link B1 §6),
  lesson study, Oxbridge tutorial, Freire.
Read at start: sprints.md, knowledge-base/roster.md §2 + "Open search leads",
  knowledge-base/B1-historical.md (header + "Summary (B1, all 17)" only),
  knowledge-base/A3-kinds-of-information.md §3 (table only), knowledge-base/A4-type-to-method.md §1–2,
  knowledge-base/misconceptions.md (M15 seed line only), knowledge-base/sources.md (ID list only)
```
