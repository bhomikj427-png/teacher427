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
| S8a | B2 mid-century method-builders (Keller, Bloom, Gagné, Ausubel, Bruner, Engelmann, Kumon, lesson study, Oxbridge tutorial, Freire) | roster §2, A3, A4, B1 (summary only) | `B2-method-builders.md` | each entry to protocol step 8; M15 (2σ) seed written | **done 2026-11-15** |
| S8b | B3 classroom legends (Feynman, Escalante, Collins, Khan) | roster §3, A3, A4, A8 §2 myth 7 | `B3-classroom-legends.md` | same; Feynman-technique attribution sourced | **done 2026-11-15** |
| S9a | B4 researchers: memory & practice (Bjorks, Roediger/Karpicke/McDaniel, Dunlosky/Rawson, Rohrer/Carpenter, Woźniak, Matuschak/Nielsen, Ericsson, Kellman) | roster §4, A3, A4 | `B4a-researchers-memory.md` | same | **done 2026-11-15** |
| S9b | B4 researchers: instruction (Rosenshine, Sweller, Mayer/Fiorella, Kapur, Chi, Wiliam, Mazur, Wieman, Willingham, Kirschner/Hendrick, Agarwal, Learning Scientists, Nuthall, Hattie) — **split S9b-1 / S9b-2** (7 + 7) | roster §4, A3, A4 | `B4b-researchers-instruction.md` | same; Hattie written as a methodology case | **done 2026-11-15** (S9b-1 §1–7, S9b-2 §8–14) |
| S10a | **Full Justin Sung audit** | roster §5, justin-sung-claims, A1–A8 (pointers) | `justin-sung-audit.md` (each claim: verdict + evidence) | every Sung claim verdicted; rebuttal-video located or logged as not found | **done 2026-11-16** (J1–J28; Keep video found) |
| S10b | B5 practitioners (Sung entry from audit §5; Oakley, Scott Young + Feynman-technique items, Sherrington, Lemov, Christodoulou, Furst/Boxer/Mccrea/Harvard, Abdaal/Frank) | roster §5, justin-sung-audit §5, A3, A4, A8 §3 | `B5-practitioners.md` | each entry to protocol step 8 or dropped with reason; Feynman backlog rows closed or carried | split: **S10b-1 done 2026-11-16** (§1–4 Sung, Young, Oakley, Lemov) · **S10b-2 done 2026-11-16** (§5–8 + full summary) → **stage-1✓** |
| S11a | Stage 2 — Part A verification: **A1–A4** (+ backlog rows targeted S11 that belong to A1–A4) | sprints.md, A1–A4, sources (IDs) | corrections in A1–A4 + sources + CHANGELOG | every A1–A4 effect size checked at the paper (abstract or better; full-text gaps carried with reason — wording amended 2026-11-16 per review to match the bar applied) ; `uncertain` tags resolved or kept with reason | **done 2026-11-16** (partial in session 4; finished S11a-rest: A4 swept; ATS17 g + SK21 method carried to S12 with reason) |
| S11b | Stage 2 — Part A verification: **A5–A8** (+ their S11 backlog rows; engine 80% note) | sprints.md, A5–A8, sources (IDs) | corrections in A5–A8 + sources + CHANGELOG | same for A5–A8 | split (2026-11-16, context hygiene): **S11b-1 = A5 + A6** (GH80/83, Barnett & Ceci, MBF77, NA06, Pan & Carpenter 2023, LAA80/Stone) · **S11b-2 = A7 + A8 + engine 80% note** (Z02, DR12, DB08, RT11, P08, Y19, Dek12, 10%-brain, MPDK16, Ros12/80%) · **S11b-1 done 2026-11-16** (finished as S11b-1-rest; BC02, MBF77 primary, LAA80 numeric ES → S12 with reason) · **S11b-2 done 2026-11-16** (partial in session 7; finished S11b-2-rest in session 8: M87–M93, ladder) → **S11b done** |
| S12 | Stage 2 — Part B verification + A↔B matrix | all B files, A3, A4 | `matrix.md` (info type × teacher/method × grade) | every B grade re-checked; matrix complete | split (2026-11-16, context hygiene; ~50 backlog rows target S12): **S12a = B1** (backlog rows from S7a/S7b) · **S12b = B2 + B3** (rows from S8a/S8b) · **S12c = B4a + B4b** (rows from S9a/S9b) · **S12d = B5 + Sung + Part A stragglers** (rows from S10a/S10b + BC02, MBF77, LAA80, A2 priming, ATS17, SK21, CRK22, M85, DGBWR23) · **S12e = A↔B matrix** (`matrix.md`). Each part: re-check every grade in its files, work its backlog rows (close or carry with reason), Stage-2 ladder pass on its misconceptions |
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
| S11b-1 closed: NA06 full text ✓ (all .60; .82/.37 = NA06's own Table 2, not a subgroup) · "161 undergraduates" line sourced ✓ (Cap25 thesis, full text) · LAA80 3rd author Ackerson ✓ · Stone = JEE 1983 51(4) / ED220476 ✓ | — | — |
| LAA80 / Stone numeric mean ES (not in either abstract; only Bl84's secondary .20 held) | S11b-1 | S12 |
| Barnett & Ceci 2002 exact dimension list (3 content + 6 context?) — S11b-1: no free full text; Klahr & Chen 2011 CMU PDF 404; LS blog lists only 3 conditions | S1 | S12 |
| Zimmerman 2002 text itself (phase labels now confirmed via Pan17 full text, S11b-2; Bath host redirects, no Wayback copy) | S1 | S13 |
| S5 closed: DR12 + RDS13 added to canon ✓ (numbers still open, rows below) | — | — |
| A2: priming → neocortex placement (S11a: not-hippocampus settled via SS17; Squire full texts 403) | S2 | S12 |
| S10a closed: response video located (BK22 Keep 2022 + JS-CO) ✓; digest claims caption-checked except J8, J10, J13 (row below) | — | — |
| Sung J8 (course), J10, J13 (interview/summary) wording at a primary video; J22 SuperMemo page (404 on supermemo.guru) | S10a | S12 |
| ICS22 *Report on Learning* (iCanStudy 2022) — read if obtainable; any later peer-reviewed Sung outcome study | S10a | S12 |
| Roster open leads (Kumon RCT full text, Nuthall 3 encounters, gurukul/chavruta) — S7b closed: Montessori meta (Ra23 + Li25), Suzuki (LWW24), Moore (none found; IBL La14) | S0 | S8a–S9b |
| S11a closed: D13 moderate list ✓ · BB92 editors/pages ✓ · RK06 ✓ · PR18 ✓ · LTM capacity ✓ (St73, BKAO08) · KCP12 row 2 ✓ · CKS17 ✓ (quote replaced) · BR19 ✓ · RDS13 ✓ (DGBWR23) | — | — |
| S2 closed: Squire vol/issue ✓, BB92 + KB11 + PR18 added to canon ✓ | — | — |
| S3 closed: Krathwohl procedural wording ✓ (full text) · KLI typology ✓ (CRK22 full text) · Gagné ✓ (G84 full text replaces 1985 edition) | — | — |
| CRK22 proceedings page numbers (escholarship PDF returned empty S11a-rest; replication part closed) | S3 | S12 |
| S11a closed: KMS10 perceptual-learning efficacy → A3 row 7 `contested` (developer-lab evidence); peer-reviewed RCT question stays on the MPDK16 row | — | — |
| A4 items checked only at abstract in S11a (S11a Done-when amended to "abstract or better"): ATS17, C06, BR19, YLVYS21, YF19 — read at full text where obtainable | review 2026-11-16 | S13 |
| Misconception status-ladder pass: move every `written` entry whose correction now rests on a full-text read to `verified` (M19, M35 done 2026-11-16) | review 2026-11-16 | S13 |
| M85 `contested` beyond early-primary maths rests on one study (GC16) — check the wider reciprocal-effects (motivation ↔ achievement) literature | review 2026-11-16 | S12 |
| DGBWR23 year 2023 inferred from the PDF path — confirm at the e-book front matter | review 2026-11-16 | S12 |
| ATS17 numeric g (WSU 403, ERIC abstract has no number; numeric role moved to YLVYS21 in S11a-rest — row stays for completeness only) | S4 | S12 |
| SK21 how the bias-adjusted g = 0.87 was computed (paywalled; lead: Sinha's ETH 2020 thesis "Problem-Solving Followed by Instruction", research-collection 500 in S11a-rest) | S4 | S12 |
| S11a-rest closed: Bi18 full text ✓ · C06 abstract ✓ · MHO14 vol/pages ✓ · KACS03 bib ✓ · Ag19 full text ✓ (M75 verified) · CRK22 fact/skill replication ✓ (YF19 independent lab + RKC25 preprint) | — | — |
| S11b-1 closed: GH80/83 percentages ✓ (GH83 full text; 52% corrected to 45 vs 21%) · Pan & Carpenter 2023 ✓ (PC23 abstract; timing part stays `uncertain`) | — | — |
| DR12 numbers (overconfidence → early stopping → retention) — abstract elided; S11b-2: Crossref/OpenAlex/S2/web all failed | S5 | S13 |
| DB08 mean ES (0.61 vs 0.69 in secondaries) — S11b-2: moderators closed via Pan17; Dignath 2009 thesis PDF bot-blocked (publikationen.ub.uni-frankfurt.de/files/6984/Dissertation.pdf) | S5 | S13 |
| S11b-2 closed: RT11 split ✓ (TR21 full text: it is the *recall* split; cue-only delayed JOLs < overt retrieval) · Dek12 wording ✓ · Y19 effect sizes ✓ (full text) · Brain Gym ✓ (Hy07) · "10% brain" kept prevalence-only ✓ · MPDK16 peer-reviewed report: none found ✓ · engine 80% note ✓ (B4b §1; proposal awaits learner sign-off) | — | — |
| Morris, Bransford & Franks 1977 transfer-appropriate processing — read primary (bib ✓ S11b-1; no free PDF found; only secondaries; A6 §1 stays `uncertain`) | S5 | S12 |
| S8a closed: M15 (2σ) written from Bl84 full text + VL11 + NOQ24 ✓ | — | — |
| P08 full text (meshing criterion wording; number of studies) — S11b-2: UVA + APS PDF links return HTML | S6 | S13 |
| S10b-1 closed: Feynman Technique origin ✓ (SY-FT11 transcript full text + SY-FT24: Young's own method; Gleick not needed for attribution) | — | — |
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
| KKC79 numeric mean ES (PSI) + KKB90 numeric mean (abstracts give direction only) | S8a | S12 |
| Ke68 Keller's own five-feature wording (PMC scan; try image render) | S8a | S12 |
| Gagné nine events wording at primary (Gagné, Briggs & Wager) + any controlled test of the sequence | S8a | S12 |
| Ausubel "most important single factor" epigraph wording (1968); Bruner "intellectually honest form" (1960) | S8a | S12 |
| SMS24 journal-version numbers (working paper 2020 read) | S8a | S12 |
| Ash05 vol/pages; content-focused vs process-only PD claim (B2 §8) | S8a | S12 |
| VL11 answer-based tutoring ES (not in abstract) | S8a | S12 |
| Feynman *Lectures* preface wording ("did very well by the students", "the system is a failure") at the book (caltech site 403s; only secondary quotes) — Goodstein anecdote closed S10b-1 (Gd89 first-hand) | S8b | S12 |
| Chen & Oakley 2019 AERA paper (LHTL effectiveness: design, N, effect) — only quoted in OS19 | S10b-1 | S12 |
| Gd89 page range 70–75 (from PDF) — confirm at AIP record; SO09 effect sizes + moderators at full text | S10b-1 | S12 |
| Any controlled test of *Teach Like a Champion* training or of Cold Call on learning (not participation) | S10b-1 | S12 |
| Mat88 (Mathews *Escalante*) — Garfield year-by-year numbers, summer/Saturday sessions | S8b | S12 |
| Marva Collins: any independent Westside Prep evaluation; *Marva Collins' Way* (1982) primary | S8b | S12 |
| Systematic phonics evidence (B3 §3 mechanism, outside A3 scope) — decide include or drop | S8b | S12 |
| Teacher-expectancy effect size (M62) — Rosenthal & Jacobson + Jussim & Harber 2005 review | S8b | S12 |
| Kel08 vol/pages; Make It Stick (2014) not read; MN19 remaining 34k chars | S9a | S12 |
| Controlled test of SM-2 vs a fixed spacing schedule (B4a §5 `uncertain`) | S9a | S12 |
| S11b-2-rest closed: A7/A8 misconception pass ✓ (M87–M93 new; M42, M45, M47 → verified) · Wi19 authors + article no. ✓ (full text PMC6831579) | — | — |
| Full text for the A7/A8 misconceptions still at `written`: RT11 (M41), KoB08 (M88), CGNA96 (M46, APA paywall), Hy07 (M91) | S11b-2-rest | S13 |
| Og25's cited experiment [6] (Pomodoro-trained students beat fixed schedules on test performance) — identify and read | S11b-2-rest | S13 |
| Kap08 abstract/full text (only TLDR seen); Ben11, Smi09 author/vol checks; ICAP independent tests | S9b-1 | S12 |
| Mazur "30–70% first-vote" guideline — primary source | S9b-1 | S12 |
| Fre14 failure rates (21.8% vs 33.8%?) at full text; DSW11 effect size | S9b-2 | S12 |
| Nut07 three/four encounters at the book (pp. 63, 126); Nuthall death year (2001 vs 2004) | S9b-2 | S12 |
| Hat09 "800+ metas" + d = 0.40 hinge at the book; Willingham "residue of thought" wording | S9b-2 | S12 |
| *Seven Myths* chapter-level source check (book not read; EAP17 review only); *Teaching Secondary Science* (Boxer) claim at the book (LB-AB review only) | S10b-2 | S12 |
| Laming *Human Judgment* (2004) "no absolute judgement" rationale for CJ — read or soften (B5 §6 `uncertain`) | S10b-2 | S12 |
| GFG01 abstract/full text (motivation decline through school); Mccrea's expectation principle in his own words (only reviewer summaries) | S10b-2 | S12 |
| Abdaal's "2011 Swahili study" = KBa11? (design matches; confirm from video description/on-screen citation) + the "+50%" figure; TF19 description links | S10b-2 | S12 |
| Willingham 2003 deep/shallow knowledge (cited by Furst, EF26) — read | S10b-2 | S12 |
| Lead: EdWeek Oct 2026 report of an *EEPA* coaching RCT (ICP) with null effects on scores — check primary; may update KBH18 "shrinks at scale" line | S10b-2 | S12 |

## Research tooling notes (what worked, S7a–S7b — read with the hand-off)

- **Abstracts by DOI or title:** `python -I research-tools/abstract_lookup.py <DOI> "<title words>"` →
  Crossref (bib + often abstract), Europe PMC (abstract; best for psychology/medicine), Semantic
  Scholar (abstract/TLDR). Publisher-elided abstracts → try ERIC API
  (`api.ies.ed.gov/eric/?search=...&format=json`) or a university repository copy.
- **Old primary texts:** Project Gutenberg plain text (`gutenberg.org/cache/epub/<n>/pg<n>.txt`) and
  Internet Archive full text (`archive.org/download/<id>/<id>_djvu.txt`; find `<id>` via
  `archive.org/advancedsearch.php?...&output=json`) — curl to the scratchpad, then grep.
- **PDFs** WebFetch can't read are saved to tool-results → extract with `pypdf` (installed).
- **Blocked:** Springer/Wiley article pages and PDFs (login redirect), ctext.org (anti-scraping),
  PMC pages (reCAPTCHA) — go to Crossref/Europe PMC instead.
- **Scanned PDFs (no OCR installed):** render pages with `pymupdf` (`page.get_pixmap(dpi=125)`) to
  the scratchpad and Read the PNG — worked for Bl84 (S8a). Archive.org lending-library books return 401.
- **Author repository copies** (university DSpace: `.../server/api/core/bitstreams/<uuid>/content`) and
  gwern.net/doc PDFs often give full text of RER/AERA papers.
- **YouTube (S10a):** `python -I research-tools/yt_search.py "<query>"` lists id | channel | title; then
  `python -I tools/fetch_transcripts.py "https://www.youtube.com/watch?v=<id>" /tmp/<dir>` (keep captions
  out of the repo); read with `python -I research-tools/cap.py "<glob>" "<regex>" 250` (keyword windows,
  not whole 14k-word files). Only Bash can read %TEMP% (Read/cat are blocked there). Upload dates:
  `python -I -m yt_dlp --skip-download --print "%(id)s %(upload_date)s" <urls>`.
- **Shell:** long bash heredocs with apostrophes/quotes fail to parse (again in S10b-1) — **append to KB
  files with the Edit tool** (anchor on the file's last lines); short Python one-liners only for logs.
  `cd dir && <write>` compounds and `mkdir /tmp/...` need approval under auto.py — use absolute paths;
  scratch downloads go to `C:/Users/bhomi/AppData/Local/Temp/` (curl -o), WebFetch PDFs land in
  tool-results (extract with pypdf + `sys.stdout.reconfigure(encoding='utf-8')`).
- **Europe PMC full text (S10b-1):** open-access papers behind publisher logins (nature.com) →
  `ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:<doi>&format=json` for the PMCID, then
  `.../rest/<PMCID>/fullTextXML`.
- **S11b-1-rest:** Invenio repositories that 403 on WebFetch (openscholar.uga.edu) still serve
  `curl -sL -A "Mozilla/5.0" <record>/export/xm` (MARCXML: title, author, year, abstract, PDF link).
  Author home pages (e.g. `sfu.ca/~jcnesbit/articles/`) often host full RER PDFs. Keep each curl a
  single command (no `;`, `&&`, `for`, pipes into python) — compounds need approval under auto.py.

## Current hand-off

```
Sprint: S11b-2 — Stage 2 verification A7 + A8 + engine 80% note — done (2026-11-16; partial in
  session 7, finished S11b-2-rest in session 8) → S11b done
Written: misconceptions M87–M89 (A7: silent judging ≠ testing; one test result doesn't switch
  method; study-skills training differs by age) and M90–M93 (A8: brain knowledge doesn't protect;
  Brain Gym; ~80% not a proven optimum; "significant" ≠ large) · ladder: M41 rewritten (TR21),
  M42/M45/M47 → verified · A8 myth 5 Og25 design split · B4b §1 Wi19 limits · sources rows N13,
  Wi19, Og25 (205 rows) · CHANGELOG · S12 split a–e written into the table
Verified this sprint: full text — N13, Wi19 (authors/article no. confirmed), Og25, and earlier in
  S11b-2 TR21, Pan17, Y19, Dek12
Open (carried): see Verify backlog — S13: DR12, DB08 mean, Z02, P08, RT11/KoB08/CGNA96/Hy07 full
  text, Og25 [6]; S12d: Part A stragglers
Decisions made: S12 split into five parts by B file (a B1 · b B2+B3 · c B4a+B4b · d B5 + Sung +
  Part A stragglers · e matrix). Engine ~80% wording still awaits learner sign-off (B4b §1).
Assumptions to review (S11b-2-rest): (13) M42 marked verified on the authors' own full-text guide
  (DGBWR23) rather than RDS13 itself. (14) M92 placed in A8 §3 (test kit), shared with B4b §1.
  (15) Og25's cited test-score experiment noted as `uncertain` rather than read.
Next sprint: S12a — Part B verification, B1 — first action: from the Verify backlog take the rows
  first-noted S7a/S7b (EC05/Rein, RS1599 translator, Orbis Pictus, CSJ01, Vyg78/Chaiklin, Sm25/WBR76,
  KCE80, LM96/Piaget, Fröbel/Moore/Suzuki/Pólya primaries, La14/LWW24/Sk22/Li17, SK22, FMSG14,
  FN18/No22); close or carry each with reason; re-check every B1 grade in the Summary table against
  its entry; Stage-2 ladder pass on M49–M56 (≥3 new misconceptions only if the sources read turn
  them up — Part B has no fixed hunt quota). Tick S12a.
Read at start: sprints.md (hand-off + Verify backlog + Research tooling notes),
  knowledge-base/B1-historical.md (Summary §716–755 first; open single entries only as a backlog
  row needs them), knowledge-base/misconceptions.md (index + M49–M56 only),
  knowledge-base/sources.md (ID lookups by grep only)
--- previous sprint (closed) ---
Sprint: S11b-1 — Stage 2 verification A5 + A6 — done (2026-11-16; finished as S11b-1-rest)
Open (carried, all S12d in the backlog): BC02 dimension list; MBF77 primary; LAA80/Stone numeric ES
Decisions made: an unpublished thesis that goes against a framework is written as T3 + named
  boundary condition, never as a refutation, and never deleted for being inconvenient.
Assumptions to review (S11b-1): (6) GH83 from a gwern.net scan; GH80 numbers from the authors'
  recap in GH83. (7) Cap25 test: no delayed test reported. (8) A6 §4 range is the engine's reading.
Assumptions to review (S11b-2, session 7): (9) S11a Done-when reworded to the bar applied.
  (10) DB08 moderators from Pan17's quote of DB08 p. 246. (11) Wi19 authors from recall — now
  confirmed at full text (closed). (12) "10% of the brain" kept as prevalence-only.
```
