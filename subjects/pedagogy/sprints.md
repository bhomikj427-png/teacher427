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
| S12 | Stage 2 — Part B verification + A↔B matrix | all B files, A3, A4 | `matrix.md` (info type × teacher/method × grade) | every B grade re-checked; matrix complete | split (2026-11-16, context hygiene; ~50 backlog rows target S12): **S12a = B1** (backlog rows from S7a/S7b) · **S12b = B2 + B3** (rows from S8a/S8b) · **S12c = B4a + B4b** (rows from S9a/S9b) · **S12d = B5 + Sung + Part A stragglers** (rows from S10a/S10b + BC02, MBF77, LAA80, A2 priming, ATS17, SK21, CRK22, M85, DGBWR23) · **S12e = A↔B matrix** (`matrix.md`). Each part: re-check every grade in its files, work its backlog rows (close or carry with reason), Stage-2 ladder pass on its misconceptions · **S12a done 2026-11-16** (partial in session 9; finished S12a-rest in session 10: grades re-checked, M49–M56 all verified, book primaries carried to S13 with reason) · **S12b done 2026-11-16** (session 12: grades re-checked, Bruner CPA → M−; M15/M57/M59/M61/M63 verified; 8 sources added, 217) · **S12c partial 2026-11-16** (session 13: grades re-checked, 8 backlog rows closed, M66/M69/M70/M73 verified; open → S12c-rest: SM-2 controlled test, MN19 rest) |
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
| S12a closed: SK22 moderators ✓ (full text) · FN18 + No22 bib ✓ · EC05/Rein ✓ (RV1893 primary) · RS1599 translator = Farrell ✓ · *Orbis Pictus* softened ✓ · CSJ01 design ✓ (full text) · La14/LWW24/Sk22/Li17 ✓ · LM96 abstract ✓ (full text closed) · Sm25 full text ✓ | — | — |
| S12a-rest closed: B1 grade re-check ✓ (Pestalozzi fading → M−) · Fröbel gifts primary ✓ (Fr-PK) · WBR76 design ✓ (via Sm25 quotes) · KCE80 bounded by KKC80-RER ✓ (exact number row below) · M50/M51/M54–M56 verified ✓ | — | — |
| WBR76 six-function list at the paper (Wiley pdfdirect returns HTML; design now confirmed via Sm25) | S7b | S13 |
| Piaget primary for stages (LM96 full text closed; in-copyright books, no licensed open copy) | S7b | S13 |
| FMSG14 numbers (S12a-rest: OpenAlex closed, no repository copy, web search no PDF) | S7a | S13 |
| KCE80 exact mean ES (EEPA closed; S12a-rest web search bib only; authors say ≈ CBI's .25) | S7b | S13 |
| Vyg78 primary read (ZPD wording p. 86; only a ch. 2 excerpt legitimately online) + Chaiklin 2003 chapter | S7b | S13 |
| Fröbel occupations (gifts done S12a); Moore method primary (Parker 2005); Suzuki *Nurtured by Love*; Pólya *How to Solve It* — in-copyright books, no licensed open copy found | S7b | S13 |
| LH16 full text (rug.nl PDF 403, utwente no file; abstract numbers used) | S12a-rest | S13 |
| S12b closed: VL11 answer-based 0.31 ✓ (table via VL11-sl) · SMS24 journal abstract = WP ✓ · Ash05 bib ✓ · PD claim checked → `contested` (LHGP19 vs Ken16) ✓ · Gagné outcome meta found (LY25; sequence still untested) ✓ · phonics included as pointer (ENSW01) ✓ · M62 sourced at JH05 + Ra84 abstracts ✓ · Kumon RCT lead ✓ | — | — |
| KKC79 numeric mean ES (PSI) + KKB90 numeric mean — S12b: both closed at OpenAlex, typeset copy HTML; only an auto-generated 0.52 online. BKK91 (full text) used for the mechanism instead | S8a | S13 |
| Ke68 Keller's own five-feature wording — S12b: Europe PMC render, UNL (403), CORE, Göttingen (404), Athabasca (504) all failed | S8a | S13 |
| Gagné nine events wording at Gagné, Briggs & Wager; Ausubel 1968 epigraph; Bruner 1960 line — in-copyright books, no licensed open copy | S8a | S13 |
| JH05 + Ra84 full text (mean expectancy ES); M58 (LAA80/Stone numbers) and M60 (KKB90 full text) to reach `verified` | S12b | S13 |
| Feynman *Lectures* preface wording ("did very well by the students", "the system is a failure") at the book (caltech site 403 again S12b) — Goodstein closed S10b-1 (Gd89) | S8b | S13 |
| Chen & Oakley 2019 AERA paper (LHTL effectiveness: design, N, effect) — only quoted in OS19 | S10b-1 | S12 |
| Gd89 page range 70–75 (from PDF) — confirm at AIP record; SO09 effect sizes + moderators at full text | S10b-1 | S12 |
| Any controlled test of *Teach Like a Champion* training or of Cold Call on learning (not participation) | S10b-1 | S12 |
| Mat88 (Mathews *Escalante*) — Garfield year-by-year numbers, summer/Saturday sessions (in-copyright book) | S8b | S13 |
| Marva Collins: any independent Westside Prep evaluation (none found); *Marva Collins' Way* (1982, in-copyright) | S8b | S13 |
| S12c closed: Kel08 bib ✓ (Crossref) · Kap08 abstract ✓ (design corrected) · Ben11 + Smi09 bib ✓ · ICAP independent test ✓ (Cap25, contrary) · Mazur band ✓ (CM01 full text: 35–70%) · Fre14 21.8/33.8% ✓ · DSW11 2.5 SD ✓ (full text) · Nuthall 1935–2004 ✓ (UC) · Willingham idea ✓ (Wil03; phrase = 2009 book) | — | — |
| MN19 remaining ~34k chars (S12c-rest) · *Make It Stick* (2014, in-copyright book, not read) | S9a | S12c-rest / S13 |
| Controlled test of SM-2 vs a fixed spacing schedule (B4a §5 `uncertain`) | S9a | S12c-rest |
| S11b-2-rest closed: A7/A8 misconception pass ✓ (M87–M93 new; M42, M45, M47 → verified) · Wi19 authors + article no. ✓ (full text PMC6831579) | — | — |
| Full text for the A7/A8 misconceptions still at `written`: RT11 (M41), KoB08 (M88), CGNA96 (M46, APA paywall), Hy07 (M91) | S11b-2-rest | S13 |
| Og25's cited experiment [6] (Pomodoro-trained students beat fixed schedules on test performance) — identify and read | S11b-2-rest | S13 |
| Nut07 three/four encounters at the book (pp. 63, 126) or NA93 full text (AERJ, closed) | S9b-2 | S13 |
| Hat09 d = 0.40 hinge at the book ("over 800" is its subtitle); Willingham 2009 book "residue of thought" wording | S9b-2 | S13 |
| *Seven Myths* chapter-level source check (book not read; EAP17 review only); *Teaching Secondary Science* (Boxer) claim at the book (LB-AB review only) | S10b-2 | S12 |
| Laming *Human Judgment* (2004) "no absolute judgement" rationale for CJ — read or soften (B5 §6 `uncertain`) | S10b-2 | S12 |
| GFG01 abstract/full text (motivation decline through school); Mccrea's expectation principle in his own words (only reviewer summaries) | S10b-2 | S12 |
| Abdaal's "2011 Swahili study" = KBa11? (design matches; confirm from video description/on-screen citation) + the "+50%" figure; TF19 description links | S10b-2 | S12 |
| Willingham 2003 deep/shallow knowledge (cited by Furst, EF26) — read | S10b-2 | S12 |
| B4 misconceptions still `written`: M64 (McD11, RAMM11), M65 (RD11), M67 (KN11) — paywalled, no repository copy found S12c; M71 (NA93 full text); M72 (Sim17: Durham repository 403 to WebFetch + curl) | S12c | S13 |
| M68 to `verified` needs SK21 full text (already an S12d row) | S12c | S12d |
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
Sprint: S12c — Part B verification, B4a + B4b — partial (2026-11-16, session 13) — auto.py
  milestone still 3 of 5 (S12c counts when S12c-rest finishes it)
Written: B4b §4 Kap08 design corrected (no instruction phase in 2008) · §5 ICAP grade reason (CW14
  full text + Cap25 contrary) · §7 Mazur band 35–70% (CM01) · §8 DSW11 2.5 SD, Fre14 21.8/33.8%,
  Des19 crossover +0.46 SD · §9 Wil03 · §11 ANB21 no-meta note · §13 Nuthall 1935–2004 + NA93 ·
  misconceptions M66/M69/M70/M73 → verified · sources +NA93, +Wil03, CW14 duplicate merged
  (218 unique IDs) · roster Nuthall dates · CHANGELOG · backlog
Verified this sprint: full text — Fre14 (PMC), DSW11, Des19, RDHC20, ANB21 (preprint), KSC06, CM01,
  Wil03; abstract — Kap08, NA93; bib — Ben11, Smi09, Kel08, NAL95; UC page — Nuthall dates
Open (carried): S12c-rest — SM-2 vs fixed-schedule controlled test (search); MN19 remaining text.
  S13 — M64/M65/M67 sources paywalled; M71 NA93 full text; M72 Sim17 (403); Nut07, Hat09,
  Willingham 2009, Make It Stick (books). S12d — SK21 full text (also lifts M68).
Decisions made: a misconception goes to `verified` only when its load-bearing source is read at
  full text (M68 held back on SK21 abstract). A developer's practice rule found at the primary is
  written as "practice rule, not a tested threshold" (Mazur band).
Assumptions to review (open): (6) GH83 gwern scan / GH80 via recap. (7) Cap25 no delayed test.
  (8) A6 §4 range = engine's reading. (9) S11a Done-when reworded. (10) DB08 moderators via Pan17.
  (12) "10% brain" prevalence-only. (13) M42 verified via DGBWR23. (14) M92 placed in A8 §3.
  (15) Og25 [6] `uncertain`. (16) RS1599 = Farrell from intro + catalog. (17) CSJ01 = Chi lab copy.
  (18) Orbis Pictus "first" dropped. (19) Pestalozzi fading lowered to M− on one abstract-level
  study (BG13) + an underspecified theory. (20) M50/M51/M54 verified where part of the correction
  rests on abstracts and the load-bearing part on full text. (21) VL11 table from VanLehn's own
  slides. (22) M15/M63 verified on the same rule as (20). (23) LY25 author initials from the
  paper header. (24) Phonics included as a pointer. (25) Log-first slip on the S12b VL11 edit. New:
  (26) ANB21 numbers taken from the PsyArXiv preprint, not the journal version. (27) KSC06 read
  from a course-reading copy (davidlewisphd.com). (28) Nuthall death year from the University of
  Canterbury trust page (no obituary read). (29) M70 verified with D13 lists checked only in S11a.
Next sprint: S12c-rest — first action: search for a controlled test of SM-2 (or any adaptive
  scheduler) vs a fixed expanding schedule on delayed retention; write the result into B4a §5;
  then read the rest of MN19 (numinous.productions/ttft) for any further numbers/caveats → B4a §6;
  close both rows; Done-when check; tick S12c (milestone 4 of 5); then S12d.
Read at start: sprints.md (hand-off + Verify backlog + tooling notes),
  knowledge-base/B4a-researchers-memory.md §5–§6 only, knowledge-base/sources.md (grep by ID).
  Scratch helpers in the temp dir: cr.py, oa.py, epmc.py, pdfgrep.py, logadd.py (+ add.txt),
  rowsub.py (edit one sources row), rowins.py (insert a row after an ID), dedup.py; cap.py lives
  in subjects/pedagogy/research-tools (use the absolute path).
```
