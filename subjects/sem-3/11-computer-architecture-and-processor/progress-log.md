# ECE2108 Computer Architecture & Processor — Progress Log

> Written **live** as sessions happen (log-first artifact pairing; never reconstructed at
> wrap-up). Session-resume block is overwritten each session-end; Session history is append-only.
> See `../README.md`.

## Session resume
- Last session: 2026-09-13 (no teaching).
- Where we stopped: `study-pack/` built to MTE scope (U1–U4) and `video-lectures.md` built
  (two-layer lecture map). Learner has not worked any drill and has not reported watching anything.
- Next up: **Session 1** — diagnostic before any teaching. Place level with three probes:
  (a) RTL-is-hardware probe — "what two things must be true for `DR ← M[AR]` to happen?";
  (b) the control-derivation scan — "give LD(AR) for the Basic Computer";
  (c) pipeline ceiling probe — "would a 12-stage pipeline be 12× faster?".
  Then open U1 via the loop at the placed level. Digital Electronics is an assumed prerequisite
  (registers, decoders, MUX, flip-flops, adders, tri-state) — verify by retrieval, teach only gaps.
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
