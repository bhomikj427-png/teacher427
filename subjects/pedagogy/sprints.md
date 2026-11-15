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
| S10b | B5 practitioners (Sung entry from audit §5; Oakley, Scott Young + Feynman-technique items, Sherrington, Lemov, Christodoulou, Furst/Boxer/Mccrea/Harvard, Abdaal/Frank) | roster §5, justin-sung-audit §5, A3, A4, A8 §3 | `B5-practitioners.md` | each entry to protocol step 8 or dropped with reason; Feynman backlog rows closed or carried | **stage-1✓** |
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
| S10a closed: response video located (BK22 Keep 2022 + JS-CO) ✓; digest claims caption-checked except J8, J10, J13 (row below) | — | — |
| Sung J8 (course), J10, J13 (interview/summary) wording at a primary video; J22 SuperMemo page (404 on supermemo.guru) | S10a | S12 |
| ICS22 *Report on Learning* (iCanStudy 2022) — read if obtainable; any later peer-reviewed Sung outcome study | S10a | S12 |
| Ag19 full text: experiment Ns, effect sizes, whether fact knowledge was tested after higher-order quizzes (M75 boundary) | S10a | S11 |
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
| S8a closed: M15 (2σ) written from Bl84 full text + VL11 + NOQ24 ✓ | — | — |
| "10% of the brain" + coordination exercises / Brain Gym: find a primary refutation or drop from A8 | S6 | S11 |
| P08 full text (meshing criterion wording; number of studies) | S6 | S11 |
| Y19 effect sizes (grades, lower-achievers) at full text | S6 | S11 |
| Feynman Technique: check Gleick *Genius* / Feynman's own texts for any described method; Scott Young's 2011 post body | S6 | S10b |
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
| KKC79 numeric mean ES (PSI) + KKB90 numeric mean (abstracts give direction only) | S8a | S12 |
| Ke68 Keller's own five-feature wording (PMC scan; try image render) | S8a | S12 |
| Gagné nine events wording at primary (Gagné, Briggs & Wager) + any controlled test of the sequence | S8a | S12 |
| Ausubel "most important single factor" epigraph wording (1968); Bruner "intellectually honest form" (1960) | S8a | S12 |
| SMS24 journal-version numbers (working paper 2020 read) | S8a | S12 |
| Ash05 vol/pages; content-focused vs process-only PD claim (B2 §8) | S8a | S12 |
| VL11 answer-based tutoring ES (not in abstract) | S8a | S12 |
| Feynman *Lectures* preface + Goodstein "freshman lecture" anecdote at a primary/first-hand source | S8b | S10b |
| Mat88 (Mathews *Escalante*) — Garfield year-by-year numbers, summer/Saturday sessions | S8b | S12 |
| Marva Collins: any independent Westside Prep evaluation; *Marva Collins' Way* (1982) primary | S8b | S12 |
| Systematic phonics evidence (B3 §3 mechanism, outside A3 scope) — decide include or drop | S8b | S12 |
| Teacher-expectancy effect size (M62) — Rosenthal & Jacobson + Jussim & Harber 2005 review | S8b | S12 |
| MPDK16 peer-reviewed report of the PLM efficacy RCT (→ upgrade A3 row 7 / KMS10) | S9a | S11 |
| Kel08 vol/pages; Make It Stick (2014) not read; MN19 remaining 34k chars | S9a | S12 |
| Controlled test of SM-2 vs a fixed spacing schedule (B4a §5 `uncertain`) | S9a | S12 |
| Engine note: principle 4 "~80% success" rests partly on correlational process-product data (Ros12) — check research/01 §5 + 03 §1 sources; any change → design sign-off | S9b-1 | S11 |
| Kap08 abstract/full text (only TLDR seen); Ben11, Smi09 author/vol checks; ICAP independent tests | S9b-1 | S12 |
| Mazur "30–70% first-vote" guideline — primary source | S9b-1 | S12 |
| Fre14 failure rates (21.8% vs 33.8%?) at full text; DSW11 effect size | S9b-2 | S12 |
| Nut07 three/four encounters at the book (pp. 63, 126); Nuthall death year (2001 vs 2004) | S9b-2 | S12 |
| Hat09 "800+ metas" + d = 0.40 hinge at the book; Willingham "residue of thought" wording | S9b-2 | S12 |

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
- **Shell:** long bash heredocs with apostrophes/quotes have failed to parse twice — write long
  content with the Write tool to the scratchpad, then append via a short Python script.

## Current hand-off

```
Sprint: S10a — Full Justin Sung audit — done (2026-11-16)
Written: knowledge-base/justin-sung-audit.md — §1 retrieval dispute (J4/J6/J7/J16), §2 higher-order
  & effort (J1–3, J5, J9, J12, J21, J23), §3 notes/mind maps/priming/tier list (J10–J20), §4 evidence &
  capacity claims (J8, J22, J24–J28), §5 overall verdict + B5 grade (translator M / own method T)
  · misconceptions M74–M77 · sources +10 (166) · justin-sung-claims.md status line
Verified this sprint: captions — JS-TED, JS-PRB, JS-RNK, JS-6L, JS-CO, BK22 (Keep response video,
  read in full); abstracts — Ag19 (higher-order quizzes > fact quizzes for higher-order tests),
  KGF19 (misinterpreted-effort hypothesis); no peer-reviewed Sung outcome study found (Crossref/EPMC/web)
Open (carried): J8/J10/J13 wording not caption-checked; J22 page 404; ICS22 unread; Ag19 full text
Decisions made: S10 split → S10a (audit) + S10b (B5 practitioners, Sung entry summarises audit §5,
  does not re-argue it). J-verdict scale: supported / partly / unsupported / untestable. Engine impact
  of the audit: none.
Assumptions to review (unattended run): (1) split S10 into S10a/S10b without asking — the hand-off
  predicted it; (2) added research-tools/yt_search.py + cap.py (helpers, no engine change);
  (3) caption transcripts kept in %TEMP%, not committed (third-party text).
Next sprint: S10b — B5 practitioners. First action: write B5 §1 Justin Sung from audit §5 (short),
  then Scott Young (resolve the two Feynman-technique backlog rows: Young's 2011 post body; Gleick /
  Feynman Lectures preface), Oakley (diffuse mode, chunking — find any primary test), Sherrington,
  Lemov, Christodoulou, Furst/Boxer/Mccrea/Harvard (group entry), Abdaal/Frank (include only where a
  claim maps to research). Likely split S10b-1 (Sung, Young, Oakley, Lemov) / S10b-2 (rest).
Read at start: sprints.md (hand-off + Research tooling notes), knowledge-base/roster.md §5,
  knowledge-base/justin-sung-audit.md §5 only, knowledge-base/A4-type-to-method.md §1–2,
  knowledge-base/A8-myths.md §3 (test kit), knowledge-base/sources.md (ID list only),
  knowledge-base/B4b-researchers-instruction.md first 15 lines (entry format)
```
