# ECE2108 Computer Architecture & Processor — Progress Log

> Written **live** as sessions happen (log-first artifact pairing; never reconstructed at
> wrap-up). Session-resume block is overwritten each session-end; Session history is append-only.
> See `../README.md`.

## Session resume
- Last session: 2026-09-23 (no teaching).
- Where we stopped: `study-pack-v3/` files **00 and 01 rebuilt question-first** and awaiting the
  learner's verdict on the shape; 02–10 unbuilt. `question-bank.md` built (35 assignment questions
  verbatim + 141 Mano problems, chs. 2–9). Mano 3e full text obtained — the 2026-09-12 limitation is
  closed; `exam-map.md`, `sources.md`, `00-map.md`, `CHANGELOG.md` updated accordingly.
- **v2 is dropped by learner instruction** (2026-09-23: "forget about v2"). The previously-pending task
  "after 16-09-2026 append A2 answer keys to v2 files 06–09" is therefore **cancelled, not overdue**.
  `study-pack-v2/` stays on disk as reference; v3 is the live pack.
- Next up: (1) learner verdict on the v3 00/01 question-first shape → then build 02–10 to it, in the
  order 03, 07, 08, 05 first (most marks per hour). (2) **Session 1** diagnostic, unchanged:
  (a) "what two things must be true for `DR ← M[AR]` to happen?"; (b) "give LD(AR) for the Basic
  Computer"; (c) "would a 12-stage pipeline be 12× faster?".
  (3) **Carry-over retrieval probe, still unattempted since 2026-09-15:** A2 Q7 / Mano 5-12 —
  PC = 3AF, M[3AF] = 932E, what is fetched next? It is now the closing question of v3 file 00, so ask
  it as the opening probe next session.
- Due for review today: nothing yet (no items mastered).

## Mastery ledger
*(empty — nothing mastered to criterion yet)*

## Spaced-review / relearning queue
*(empty — fills as items are mastered)*

## Session history
- [2026-09-12] Subject created and researched to `stage-2✓` (both stages, 8 units + stage-2 layer);
  exam material triaged into `exam-pack/` (course hand-out + 3 unit decks). Commit `45b7180`.
  No teaching event.
- [2026-09-12] Learner request: **study pack for Computer Architecture**, built to the universal
  preferences and to the same shape as the Digital Electronics pack. Scope decided **MTE = U1+U2+U3+U4**
  — `settled` from the hand-out's lecture plan, which prints the Mid-Term divider after L19
  (`knowledge-base/exam-map.md` §2). U5–U8 (I/O, memory, 8086, RISC-V) are ETE-only and excluded.
  Format per the 2026-09-11 §7 tension: **question-first** (Map → Attempt → Method → Worked → Traps →
  Self-test → Answers-at-bottom), real Unicode symbols, no TeX, small per-file maps.
  **Difference from the DE pack, stated to the learner:** ECE2108 has **no past paper at all**, so
  question *forms* are inference (`exam-map.md` §4 F1–F17), not evidence. Worked items are drawn from
  the professor's decks and Mano, and each is labelled with where it came from.
- [2026-09-12] `study-pack/` **built — 12 files, ~4,360 lines**, MTE scope. Files: 00 start-here/flow map,
  01 arch-vs-org + functional units + von Neumann/Harvard + RISC/CISC, 02 RTL + bus + memory transfers,
  03 microoperations + arithmetic circuit + ALSU, 04 Basic Computer registers + bus + instruction set,
  05 timing/control + instruction cycle + MRI + interrupt, 06 design of BC + accumulator logic,
  07 microprogrammed control + sequencer, 08 program control + status bits, 09 parallel processing +
  Flynn, 10 pipelining + speedup + hazards, 11 drill set (timed, 30 marks).
  Facts sourced from the Stage-1/Stage-2 KB (Mano 3e authority); framing and emphasis from the decks
  + hand-out. Deck errata carried through as corrections, not repeats (ISZ `D₆T₆` not `D₆T₄`;
  the muddled arch-vs-org row). **No teaching event — nothing taught, nothing assessed; mastery
  ledger and review queue unchanged.**
- [2026-09-13] Learner request: **video lectures for the subject** — framed by the learner as
  compensating for being the **first batch** (no PYQ will ever exist for this cohort). Searched and
  verified candidate courses by listing their actual lecture titles with `yt-dlp --flat-playlist`
  (not from recall). **Core finding: no single course matches this syllabus.** The Tier-1 NPTEL
  courses (IITG COA, IITM Raman, IITKGP HPCA) teach COA from a MIPS/RISC or generic-CPU angle and
  never cover Mano's Basic Computer chapter-for-chapter; the courses that *do* follow Mano unit by
  unit are individual-educator YouTube channels = **Tier 4** (`subject-research-protocol.md` §2).
  Resolution: a **two-layer** map — Tier-1 for mechanism/correctness, Tier-4 for syllabus coverage
  with verify-before-trust — rather than pretending one source does both. Next artifact:
  `video-lectures.md`.
- [2026-09-13] ⚠ **Engine finding (tooling, not content): the NPTEL transcript path is currently
  rate-limited, not broken.** `tools/fetch_transcripts.py` reported "No captions found" for three
  test videos (one Tier-4, two NPTEL). Diagnosed: captions **do** exist — `yt-dlp --list-subs` shows
  `en`, `en-orig` and an official `English - NPTEL Official` track — but the caption download returns
  **HTTP 429 Too Many Requests** after this session's playlist enumeration. Also logged: yt-dlp now
  warns **no JS runtime (deno) installed**, deprecated for YouTube extraction. *Consequence:* no
  transcript was ingested this session; the videos are recommended from **verified lecture titles**
  only, never from claimed content. *Resolve by:* retrying spaced out, and installing deno.
- [2026-09-13] `video-lectures.md` **built** — unit-by-unit lecture map (U1-U4 first, ETE units
  after), every entry carrying a direct video ID/URL taken from a live playlist listing, tier label,
  and channel-provenance caveat where the uploader could not be confirmed as institutional. **No
  teaching event.**
- [2026-09-13] **Transcript pull succeeded on the 3rd retry (~25 min).** The HTTP 429 was
  time-based as diagnosed; all 5 target lectures fetched (21k-36k chars each). Retry driver:
  `scratchpad/pull_tutorials.py`. **Three findings, all of which change `video-lectures.md`:**
  - **(a) The [IITG-ACA] playlist's titles do not match its content** — verified by transcript, not
    assumed. `deKUGMHZjB4`, titled *"Tutorial 1: Instruction Pipeline and Performance"*, opens
    *"Welcome to the fourth lecture of the course… dedicated on discussion related to pipeline
    hazards"* = **Lec 4**. `IQql2ojVzsU`, titled *"Lec 4: Pipeline Hazards"*, opens *"Welcome to
    lecture number five… control hazards and branch prediction"* = **Lec 5**. So the re-upload is
    mis-titled and **the real "Tutorial 1" content was not found at its labelled link.** The §6
    provenance caveat about re-uploads is now an observed fact, not a precaution.
  - **(b) The [IITM-CO] "Problem Exercise" claim was WRONG and is retracted.** L13 (`F5pU5LbmLVg`)
    is instruction-format / operand-count design (opcode field sizing on a non-Mano machine);
    L14 (`hhvl7nbVpLo`) is a conceptual recap (data path, control signals, microinstruction as one
    step, ALU + controller = CPU) that then **moves into memory** = U6/ETE. Neither is a worked
    control-unit problem. That §5 claim was title-inference; the transcripts refute it. ASR quality
    on these two is also poor ("up code" = opcode, "for nyman" = von Neumann).
  - **(c) [IITG-ACA] Tutorial 2 (`MjjFqj01PzU`) is genuine and good — but formulated differently
    from this syllabus.** It is a real week-2 tutorial: 8 true/false items + 3 numericals. However
    it works in **MIPS 5-stage / CPI / RAW-WAR-WAW** terms, not Mano's FI-DA-FO-EX and
    S = n·tₙ/((k+n−1)·tₚ). Importing it wholesale would drill the wrong formula.
- [2026-09-13] **Two numericals from Tutorial 2 verified by independent re-computation** and added
  to `study-pack/10` as a clearly-labelled appendix (NOT as "Drill C" — fewer items survived the
  scope screen than expected, so a third full paper was not warranted):
  - CPI speedup: 1.5 GHz unpipelined / CPI 5 → 3.33 ns; pipelined 1 GHz, effective CPI
    1 + (0.30×0.05×50) + (0.20×0.30×2) + (0.10×1) = 1 + 0.75 + 0.12 + 0.10 = **1.97** → speedup
    3.33/1.97 = **1.69**. Arithmetic re-derived here, matches the lecture.
  - Load/Add dependency chain, 2000 instructions: without forwarding 5 + 1999×4 = **8001** cycles,
    CPI ≈ **4**; with forwarding 7 + 999×3 = **3004**, CPI = **1.502**. Re-derived, matches.
  - **Justification for including a non-Mano formulation:** the hand-out marks **L16/L17 as
    `*` practitioner-delivered (industry)**, so a CPI/MIPS framing of pipelining is a live
    possibility for those two lectures. Labelled `uncertain` and kept separate from the Mano method.
  - Branch-prediction numerical (2-bit predictor, (1,2) correlating) **excluded** — stage-2 depth,
    outside MTE scope.
- [2026-09-13] `tools/fetch_transcripts.py` hardened from this session's failure: passes
  `--js-runtimes node` (Node v20 present; deno never needed — yt-dlp's deprecation warning is
  satisfied), adds `--sleep-requests`, and now reports **HTTP 429 as rate-limiting with a
  retry-later message** instead of the misleading "No captions found".
- [2026-09-13] Raw transcripts kept at `_transcripts/` (5 files, ~142 kB) with a README recording
  what each **actually** contains vs what its playlist title claimed, so the retractions above can be
  checked against evidence rather than taken on trust. ASR caveat restated there.
- [2026-09-15] Learner dropped **two professor-set assignments** in `_inbox/`: `A1. ECE2108-CAP -
  Assignment 1 v2.pdf` (20 Q, 200 marks, submitted by 24-08-2026) and `2. ECE2108 Assignment 2.pdf`
  (15 Q, 150 marks, **due 16-09-2026 16:30**). Request: **study-pack-v2** built from them, to the
  universal preferences. These are the **first first-party question-form evidence** for ECE2108
  (previously all forms were inference). Routing: triage → `exam-pack/`; delta diagnosis vs the KB
  before any file is written.
- [2026-09-15] **Delta diagnosis (A1+A2 vs KB) — results:**
  - **Covered by KB, no delta:** A1 Q2, Q4, Q6, Q10–Q12, Q14–Q16, Q18–Q20; A2 Q1–Q4, Q6–Q7, Q9–Q15.
  - **Gaps (not in KB, researched this session, sourced):** A1 Q1 (definitions of digital computer),
    Q3 (**generations of computers** + contributors), Q5 (**types of computers**), Q13 (**named bus
    standards**). A1 Q7–Q9 are Digital-Electronics prerequisites → taken from the DE KB + Mano ch. 2–3.
  - **⚠ ERROR FOUND in KB U1 §10 and in `study-pack/03`:** the ALSU function table there uses the
    arithmetic-circuit ordering (`0000 1` = add with carry). The **professor's own ALSU slide** (deck 1
    p. 32, image extracted and read) and **Mano Table 4-8** (confirmed via an Adelphi Univ.
    reproduction) give `0000 0` = transfer A, `0000 1` = increment, `0001 0` = add, `0001 1` = add
    with carry, `0010 0/1` = subtract w/ borrow / subtract, `0011 0/1` = decrement / transfer,
    `0100–0111` = AND/OR/XOR/complement, `10xx` shr, `11xx` shl. The two tables are consistent only if
    the ALSU's MUX is wired **0 → 0, 1 → B, 2 → B′, 3 → 1**. A1 Q17 asks exactly this item.
  - **New verification source:** the *Solutions Manual, Mano CSA* (uobabylon.edu.iq reproduction).
    **A2 Q1, Q2, Q3, Q4b, Q6, Q7, Q9, Q10, Q12, Q13, Q14, Q15 are Mano end-of-chapter problems
    5-1, 5-3, 5-4, 5-6, 5-9, 5-12, 5-20, 5-21, 9-3, 9-5, 9-10, 9-11**; A1 Q16 = 4-12, Q18 = 4-19.
    Manual answers cross-checked by re-derivation; **two manual typos caught**: 5-12(c) prints
    AR = 7AC (must be 9AC); 5-21 prints `RT7` and `rB4 + (AC15)′` (must be `RT2` and `rB4(AC15)′`).
  - **A2 Q5 wording** `C₇T₃: SC ← 0` matches no BC signal; read as `D₇T₃` (textbook form `D₃T₄`),
    flagged `uncertain` in the pack.
- [2026-09-15] **Pack decision (A2 due tomorrow):** A2's own questions appear as attempt items with
  method + a fully worked **twin** (different numbers) for each; A2's exact answer key is **held back
  until after the 16-09-2026 16:30 deadline**; learner offered marking of their own answers. A1
  (already submitted) gets full answers.
- [2026-09-15] Triage: A1 → `exam-pack/ASSIGNMENT-A1-ECE2108-2026-08.pdf`, A2 →
  `exam-pack/ASSIGNMENT-A2-ECE2108-2026-09.pdf`; recorded in `../_inbox/TRIAGE-LOG.md` and
  `exam-pack/README.md`. KB edits following from the delta: U1 §10 ALSU table corrected + new U1 §11
  (definitions, generations, computer types, bus standards) with sources; `CHANGELOG.md`,
  `sources.md`, `misconceptions.md` (M24), `exam-map.md` §4 (A1/A2 forms now **evidence**).
  `study-pack/03` ALSU table corrected in place with a dated correction note.
- [2026-09-15] Started `study-pack-v2/` (assignment-anchored). Planned files: 00 start-here, 01
  foundations (A1 Q1–6, Q20), 02 digital building blocks (A1 Q7), 03 RTL + bus (A1 Q10–14), 04
  microoperations + signed arithmetic (A1 Q8–9, Q15–16, Q18–19), 05 ALSU (A1 Q17), 06 BC format + bus
  control (A2 Q1–4), 07 timing + traces (A2 Q5–8), 08 control-gate derivation (A2 Q9–10), 09 pipeline
  numericals + branching (A2 Q11–15), 10 mock paper. All numbers pre-verified by
  `scratchpad/verify_v2.py` (A1 Q8/9/16/18/19, A2 Q7, every twin, every speedup).
- [2026-09-15] `study-pack-v2/` **built — 11 files**: 00 start-here, 01 foundations, 02 digital
  building blocks, 03 RTL + common bus, 04 microoperations + signed arithmetic, 05 ALSU, 06 BC format +
  bus control, 07 timing + traces, 08 control-gate derivation, 09 pipelining numericals, 10 mock paper
  (30 marks, layout assumed from the DE sibling MTE). A1 answers complete; A2 items carry method +
  worked twin, key withheld to deadline. Twin/mock numbers re-verified by script (1250/720 = 1.74,
  12500/6120 = 2.04, 3900/1495 = 2.61, 39000/13195 = 2.96, 195/65 = 3.0). Also added to file 09:
  the two delay conventions (register delay inside vs separate), found while reconciling Mano 9-5 with
  the KB's FP-adder example. v1 `00-START-HERE` points to v2. **No teaching event — mastery ledger and
  review queue unchanged.**
- [2026-09-15] Learner: "what is even Mano? can't find much online"; videos are gap-fillers, not the
  starting point. Pack used "Mano" without ever defining it. Fix: `study-pack-v2/00-START-HERE.md`
  gains a "The textbook" section (full title, chapter → unit map, how to get it).
- [2026-09-15] Learner approved: verify the Tier-4 [MANO-SA] videos by transcript against the KB and
  update `video-lectures.md` (incl. re-pointing to study-pack-v2). Transcript pull started in the
  background → `_transcripts/MANO-SA/`.
- [2026-09-15] **First teaching exchange:** learner asked "what is fetch?" (unprompted, basic).
  Explained the fetch phase (definition, BC T₀/T₁ microoperations, why AR, why PC increments at T₁),
  then posed one retrieval check. Outcome pending.
- [2026-09-15] Fetch retrieval check (PC = 3AF, M[3AF] = 932E) **not attempted** — learner moved on to
  the video task. Carry it into the next teaching session as an opening probe.
- [2026-09-15] Transcript pull hit **HTTP 429** on videos 01–04 (same time-based rate limit as
  2026-09-13; triggered right after the playlist listing). Loop stopped; restarted with a 20-min
  initial wait, 90 s spacing, 10-min backoff. Meanwhile `video-lectures.md` re-pointed to study-pack-v2.
- [2026-09-15] Learner, on `study-pack-v2/01`: terse is still wanted, but the file "expects that I
  already know" — it is not teaching. **Diagnosis (from the file, not the learner):** v2 01 is a
  reference sheet — it uses register, clock pulse, instruction set, addressing mode, word, bus before
  defining any of them, and opens with exam questions a novice cannot attempt (contract: never open
  with unguided struggle for a true novice). Learner level for ECE2108 = **novice** (signals: asked
  "what is fetch?", "what is Mano?"). Request: **study-pack-v3, files 00 and 01 only**, to iterate on
  the shape before the rest is built.
- [2026-09-15] v3 shape decided: **Predict → Build (one idea per step, concrete, every term defined
  before use, a covered Check after each step) → Exam form → Attempt (assignment Qs moved AFTER the
  build) → Traps → Self-test → Answers at bottom.** One running example across both files: a
  3-instruction Basic Computer program (LDA 200 / ADD 201 / STA 202 → 3 + 5 = 8), opcodes verified
  against KB U2 (LDA 2xxx, ADD 1xxx, STA 3xxx; 4096 × 16-bit memory). 00 = start page + ground zero
  (bit → binary/hex → word → memory/address → register → clock → instruction/program); 01 =
  foundations rebuilt on it. Facts from KB U1 §1–§4, §11.
- [2026-09-15] `study-pack-v3/` **built — 2 files**: `00-START-HERE.md` (file shape, path, textbook,
  ground zero in 9 steps with Checks) and `01-foundations.md` (7 build steps with Checks, exam-form
  tables carried from v2, A1 attempt set, traps, 6 self-test items, answers at bottom). Awaiting
  learner feedback on the shape before 02–10. **No teaching event — mastery ledger and review queue
  unchanged.**
- [2026-09-23] Learner review of `study-pack-v3` 00/01: shape approved ("i like v3 so far"), with two
  changes. (1) **Make it question-oriented**: open each teaching step with a **real quoted question**
  — from the assignments first, from the textbook second — that the learner *would obviously not know
  the answer to*, then answer it to teach the concept. (2) **Build a Mano question base as priority 2**
  ("most of my assignment is built from mano anyways"). Scope held to **00 and 01 only** as the test
  piece. v2 explicitly dropped from consideration ("forget about v2").
  **Engine note (principle 1, kept):** question-then-answer is honoured as **pretesting / errorful
  generation** (`research/02 §1, §5`; contract ACTIVATE "have them predict/attempt first — wrong
  guesses help"). Each opening question therefore carries an explicit *guess before you read on* line.
  Without it the shape degrades into a Q&A lecture and produces fluency, not learning.
- [2026-09-23] ✅ **LIMITATION RESOLVED — a clean full copy of Mano 3e was obtained.** The open item
  `[opened 2026-09-12]` in `knowledge-base/00-map.md` ("could not obtain a clean full copy… 8 download
  attempts, truncating; *resolve by:* the learner supplying a Mano PDF") is closed **without** the
  learner supplying anything. Source: **archive.org item `computer-system-architecture-morris-mano-third-edition`**,
  OCR full text at `https://archive.org/download/computer-system-architecture-morris-mano-third-edition/computer-system-architecture-morris-mano-third-edition_djvu.txt`
  (HTTP 200, 1,100,795 bytes, complete through ch. 12 references). Verified as the right book by
  matching problem 5-1 verbatim against the professor's Assignment 2 Q1. Route note: `curl` reached
  archive.org; the earlier-recorded host (uobabylon.edu.iq) is now `ECONNREFUSED`, and the
  pdfcoffee/epdf copies are a truncated preview and an answers-only solutions manual respectively —
  **only the archive.org route works**, so it is recorded in `sources.md`. The file is **not committed**
  (whole third-party textbook); the identifier above re-fetches it in one command.
- [2026-09-23] ⚠ **KB CORRECTION — the "12 of A2's 15 items are verbatim Mano problems" claim is wrong;
  it is 15 of 15.** With the book itself readable, every A2 item was matched to its Mano source by
  statement text, and the pairing cross-anchored on two items already independently verified from the
  solutions manual on 2026-09-15 (5-9 = the CLA trace, 5-12 = the PC-3AF trace). Map:
  A2 Q1=**5-1**, Q2=**5-3**, Q3=**5-4**, Q4=**5-6**, Q5=**5-8**, Q6=**5-9**, Q7=**5-12**, Q8=**5-16**,
  Q9=**5-20**, Q10=**5-21**, Q11=**9-1**, Q12=**9-3**, Q13=**9-5**, Q14=**9-10**, Q15=**9-11**.
  The two previously missed are **5-8** (the `C₇T₃: SC ← 0` timing diagram) and **5-16** (the 65,536×8
  three-word-instruction fetch). Assignment 2 is Mano ch. 5 + ch. 9, unaltered, with sub-parts dropped.
- [2026-09-23] **New finding — Assignment 1 is also Mano-derived, but *adapted*, not copied.** Traced:
  A1 Q10 ← Mano **4-7** (memory-transfer statements, list changed); Q12 ← **4-1** (`yT₃` → `yT₂`);
  Q14(ii) ← **4-5** (tri-state + decoder bus); Q14(i) ← **4-6** (16×32 registers → 4×4); Q16 ← **4-12**
  (adder-subtractor — the professor's two cases *are* Mano's rows (a) and (d), unchanged);
  Q18 ← **4-19** (registers renamed AR/BR/CR/DR → R1–R4, values and microoperation sequence identical);
  Q19 ← **4-21** (`R = 11011101` → `11111111`, shifts reordered). Q17 (ALSU) is not a numbered problem —
  it is Mano §4-7 / Fig. 4-13 itself. **Consequence for teaching order:** the professor copies ch. 5 and
  ch. 9 outright and *re-numbers* ch. 4 — so for U2/U4 the Mano problem is the exam item, while for U1
  the Mano problem predicts the *form* but the numbers will move. Recorded in `exam-map.md` §4a.
- [2026-09-23] Built `question-bank.md` — the two-priority question base the learner asked for.
  P1 = the professor's A1 (20 Q) + A2 (15 Q), transcribed verbatim from the `exam-pack` PDFs (pypdf).
  P2 = Mano's end-of-chapter problems for the MTE scope, transcribed from the archive.org full text:
  ch. 3 (26), ch. 4 (23), ch. 5 (25), ch. 7 (24), ch. 9 (20), plus the ch. 2 items A1 Q7 examines and
  the ch. 8 status-bit items. Each P1 item carries its Mano source; each P2 item carries its v3 file.
  OCR-damaged passages are marked, not silently repaired.
- [2026-09-23] `study-pack-v3/` 00 and 01 **rebuilt question-first** (test piece; 02–10 still unbuilt).
  New per-step shape: **Q (quoted, with its source and marks) → "guess first, on paper" → the answer,
  taught → Check.** Every Build step in both files now opens on a real question, none invented.
  File 00 opens its nine steps on A1 Q1(i), Mano 3-1, Mano 3-5, A2 Q1 (=Mano 5-1), A1 Q10(iii),
  A1 Q18, A2 Q5 (=Mano 5-8), A2 Q4 (=Mano 5-6), A2 Q7 (=Mano 5-12). File 01 opens its seven on
  A1 Q1, Q4, Q6, Q2, Q20, Q3, Q5 — 1:1, the whole 76-mark A1 foundations block.
  **Honest gap stated in file 01:** Mano contributes **no** questions to it — his book has no
  architecture-vs-organization, von Neumann/Harvard, generations or types problems, so P2 for
  foundations is genuinely empty and the file says so rather than inventing items. Mano's question
  base starts at file 02 and dominates 03–09.
  File 00's closing question is **A2 Q7 / Mano 5-12 (PC = 3AF, M[3AF] = 932E)** — deliberately the
  same probe logged unattempted on 2026-09-15, now reachable from ground zero.
  **No teaching event — mastery ledger and review queue unchanged.**
- [2026-09-23] **Catch-up (Session start §0b/§5c):** the tree carried uncommitted work from the session
  that ended abruptly after 2026-09-15 — `_transcripts/MANO-SA/` (18 caption files + two yt-dlp `tmp-0x`
  scratch dirs whose `log.txt` records the HTTP 429 diagnosis). Committed first, as its own commit,
  before this session's work.
  ⚠ **Quality check on those transcripts, done now rather than assumed: they are only partly usable.**
  4 of 18 (`07`, `12`, `14`, `20`) are clean ASR. The other 14 are contaminated with YouTube
  caption-spam — file `06` contains the word "subscribe" **146 times**, `21` 82 times, `02` 70 — injected
  mid-sentence through the technical content, so whole passages are unreadable ("…transfer time t-20
  have initiated the transfer… subscribe and subscribe the Channel…"). This is worse than ordinary ASR
  mangling: it is not noise around the facts, it replaces them. **Consequence:** [MANO-SA] transcripts
  stay Tier 4 and are **not** a usable verification source for the video-lecture map except for those
  four files. The two claims retracted on 2026-09-15 stay retracted; no new claim rests on these.
- [2026-09-23] Learner approved the question-first shape ("i am loving this") and asked to **finish
  study-pack-v3 in the same format**.
  ⚠ **Gap found before building — v3's path omits U3 entirely.** The path in `00-START-HERE` was
  inherited from v2, which was *assignment*-anchored; **neither assignment touches U3**, so v2 had no
  U3 file and v3 copied that hole. But `exam-map.md` §2 is `settled` first-party: **MTE = U1+U2+U3+U4**,
  with U3 = "Control unit design & microprogrammed control", L12–L15. Building 02–10 as listed would
  have shipped a pack that silently omits an examinable unit.
  **Fix: path extended from 11 files to 13** (00–12). New: **09 microprogrammed control** and
  **10 program control + status bits** (both U3); pipelining moves to 11, mock paper to 12.
  U3's questions come from Mano ch. 7 (24 problems) and ch. 8 (the status-bit subset) — the only
  question evidence that exists for the unit, now transcribed in `question-bank.md`.
- [2026-09-23] v3 **files 02–05 built** (U1 complete), same question-first shape.
  02 digital building blocks — 6 steps on A1 Q7(i)–(vi), Mano 2-6/2-8/2-13/2-15 as follow-ups; the
  clock-gating trap (Mano 2-10) taught as the wrong-way/right-way contrast.
  03 RTL + common bus — 8 steps on A1 Q10, Q11, Q12(=Mano 4-1), Q13, Q14(i)(ii)(=Mano 4-6/4-5),
  Mano 4-7, Mano 4-23. Threshold idea (★1, KB U1 §5) taught explicitly: the simultaneous swap needs
  no temp register, and A1 Q12 is set to catch the "impossible" answer.
  04 microoperations + signed arithmetic — 8 steps on A1 Q15, Q8, Q9, Q18(=4-19), Q16(=4-12),
  Q19(=4-21), Mano 4-18, 4-20. **A1 Q9 verified to overflow** (+64 + 84 = 148 > +127; carry-in to
  sign 1, carry-out 0 → V=1; stored pattern 10010100 = −108) — the file is built around that being
  the answer.
  05 ALSU — 6 steps on Mano 4-15, 4-17, A1 Q17. Carries the **corrected** ALSU table (professor's
  deck p.32 = Mano Table 4-8) and a dedicated step 6 on why it differs from the standalone
  arithmetic-circuit ordering (MUX wired 0,B,B′,1 vs B,B′,0,1) — the error corrected in the KB on
  2026-09-15, now taught as a trap with the defensive move (label the MUX inputs).
  All numerics re-derived in-file, not copied: A1 Q16 (i) S=1101 C₄=0, (ii) S=1011 C₄=0;
  A1 Q18 → R1=01001001, R2=00000000, R3=10101000, R4 unchanged; A1 Q19 sequence
  01111111 → 10111111 → 01111110 → 11111100; Mano 2-13 six-shift table.
  **No teaching event.**
