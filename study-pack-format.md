# Study-pack format — v1.3

> **The one format for every study pack** (PDF or `.md`, any subject). Loaded by reference from
> `CLAUDE.md`. A pack is built to this file, **not copied from another pack**. If this file and an
> existing pack disagree, this file wins.
>
> **Reference: exactly three files, frozen** in `study-pack-reference/` (each with its `.md` source),
> copied from the Circuits & Systems pack on 2026-11-14: `00-START-HERE` (the start page),
> `01-elements-and-sources` (a theory topic) and `05-superposition` (a numerical topic built on real
> questions). They are the reference for **shape and page look**. **Depth** is set by the rules in
> §4–§6, which were taken from the EDC files the learner approved (`01a`, `01b`, 2026-11-15). Those
> files show the rules applied; they are not copied. **Nothing else is a reference.** Where the three
> frozen files differ from the rules below (§8), the rules win.
>
> **This file regulates itself** (§9): every format change the learner states is written here, in the
> rule it changes, the same session.

---

## 1. What a pack is for

A pack is something the learner studies from alone. It must teach from the learner's actual level,
make them produce an answer before they read one, and tell them what to write in the exam. A pack that
reads as a summary has failed, however correct it is. A pack that assumes the learner already knows
a term has failed in the same way.

## 2. Pack layout

- `00-START-HERE` first, then **one file per topic**, numbered in the order the professor teaches
  (`01-…`, `02-…`), then a mock paper as the last file.
- Output: one PDF per file **and** one combined, bookmarked PDF.
- **The number of ideas sets a file's length, not a page count.** A topic file holds about 8–13 Build
  steps. A topic with more ideas is split into `a`/`b` files (`03a-pn-junction-equilibrium`,
  `03b-diode-iv-capacitance`), each named after its idea. A topic is never compressed to fit.

## 3. `00-START-HERE` (fixed sections, in this order)

1. **Priority order: if time is short, study in this order.** A ranked table: rank · file · why it
   ranks here (the evidence: past-paper questions, board questions, marks flagged by the professor) ·
   what to do first in that file · rough time. State plainly how strong the evidence is.
2. **The path through the pack.** A flow map of the files in order, grouped by unit, and one
   paragraph on which file needs which.
3. **What each file teaches.** Table: file · syllabus item · what it teaches · how many real questions.
4. **Where the questions come from.** The source tags used in the pack, and how many questions are
   real (P1: professor's papers, board questions, assignments) and how many are textbook (P2).
5. **How each file runs.** The parts of §4 in one small table, and the one rule: guess on paper
   before reading on.
6. **Units and symbols used everywhere.**
7. **Where the professor's material disagrees with the pack**, if anywhere (the slip table).
8. **How the pack was checked.**

## 4. A topic file (fixed sections, in this order)

| Section | Contents |
|---|---|
| **Header line** | Source (deck + slide numbers / pages) · syllabus item · how many real questions · which earlier files and steps it needs |
| **Map** | A flow map of the file's steps, one node per step, the current one highlighted |
| **Opening paragraph** | What the earlier file ended with, what this file adds, and which file uses it next |
| **Symbol table** | Symbol · what it means in this file (what it counts, what sets it) · typical value. Every symbol the file uses |
| **Running example** | Where numbers recur: one set of values (e.g. N_{A} = 10^{17}, N_{D} = 10^{16}) used by every graph and most Checks |
| **The questions this file answers** | The real questions, quoted, each with its source tag and marks |
| **Build** | Numbered steps. This is the teaching (§5) |
| **Exam form** | Exactly what to reproduce in the exam: statements, procedures and derivations as numbered steps, the formulas |
| **Traps** | The mistakes that cost marks, each in one line |
| **Self-test** | 5–8 questions covering the file, mixed recall and application |
| **Answers** | On the last page(s) of the file: every Check, then the Self-test |

## 5. A Build step (the unit of teaching)

Each step teaches **one idea**. Its heading names that idea. It runs in this order:

0. **Bridge.** One line: why this idea is needed now, from the step before.
1. **Question or Predict.** A real question, quoted and tagged (professor's material first, the
   prescribed textbook second, never invented and passed off as real). If no real question exists for
   the idea, a **Predict** prompt, labelled as such.
2. **Guess first.** One line that asks for an answer on paper before reading on. This line is the
   mechanism (pretesting, `research/02 §1, §5`); it is never dropped.
3. **Terms.** At most three new terms, each defined before use **by what it counts and what sets its
   value, not by its name**. ("N_{C}: effective density of states" fails. "N_{C}: the number of seats
   that, all placed at E_{C}, would hold the same electrons" passes.)
4. **Figure.** The figure that carries the idea comes before the prose about it. **Every graph says
   what it plots** in a caption starting "What this graph plots:" or a "Reading the figure" line:
   each axis, and what one point means. A quantitative curve is then read at 3–4 points in a small
   table with numbers.
5. **Teaching.** Short: about 60 words per block, a list or table where the content is a list or a
   table. Concrete first, general statement after. Every formula is read back in words ("N_{C} = how
   many seats; the exponential = the chance one is filled"). **Derivations are numbered lines, each
   following from the line before**, with an approximation named on the line where it enters.
6. **Answer.** Every opening question or Predict is answered explicitly ("Answer to the Predict: …"),
   worked with every intermediate value.
7. **Check.** One to three questions on this step only. Answers go to the end of the file.

A topic has as many steps as it has ideas: there is no fixed count, and ideas are never merged to save
space (EDC 01b has 10 steps on what v1.2 had put into one).

## 6. Rules that apply to every page

- **Start from zero.** Assume no prior knowledge of the subject unless the learner's profile says
  otherwise. Every term is defined before first use.
- **Open on a concrete anchor.** Each file's first step starts from something everyday or already
  known (01b: "electrons = seats × the chance a seat is filled", a cinema), before any formula. Later
  formulas are read back in the anchor's words.
- **Build up, then combine.** Every variable in a formula gets its own explanation (what it counts,
  its unit, what sets its value, and a typical number) before the formula appears. A result that joins
  several earlier pieces is reached in its own step that names each piece and the step it came from,
  then puts them together line by line. A term from an earlier file is recalled in one line where it
  is used, with the file and step it came from.
- **One idea in focus per page.** A page holds at most one figure-led idea plus its Check.
- **Pictorial.** Figures carry structure; text is the caption. Generated figures by default; real
  photos or screenshots where they exist and show the thing better. Provenance on every borrowed image.
- **Real symbols.** Σ Π ⊕ ≥ ≤ √ and true subscripts/superscripts. No TeX source, no spelled-out
  substitutes.
- **Every sentence adds value.** No narration about the pack itself, no reassurance, no process talk.
- **No marking by the learner.** The pack never asks for self-scores or tick boxes. The learner
  reports only misses.
- **Slips in the professor's material** are flagged in a note box where they occur (with the slide
  number), with the corrected version used in the pack, and listed in START-HERE's slip table.
- **Page look:** the reference files': A4, one accent colour, coloured boxes for question / guess /
  check / trap / note, generous white space, footer with pack name and page number.

## 7. Building and checking

### 7.1 Before any file: the subject brief

Built once per subject, in its first session, as `study-pack-v12/src/brief.md` (or the pack's `src/`):

1. **Slides transcribed.** Every deck the pack uses, slide by slide, including equations that exist
   only as images (view them). Slips noted with slide numbers.
2. **Question bank.** Every real question (papers, assignments, sheets, deck examples), tagged, with
   marks, each mapped to the file and step that will use it.
3. **Constants.** Every constant and typical value the slides or questions use, checked against the
   knowledge base. A gap is researched and written into the KB **before** building (log line first).
4. **Figure list.** Per file: each figure, what it plots, and whether `tools/figlib.py` already has it.

Each later session reads the brief's section for its files instead of re-reading decks.

### 7.2 Sessions and sprints

- **One short fresh session builds 1–3 files**, run unattended by `auto.py` from the subject's
  `sprints.md` where possible. Each session ends by writing the next one's hand-off.
- **Sprint budget per subject: aim for 9–10. Up to 12 is fine. Over 12 only if seriously necessary,
  and the reason is written in `sprints.md`** (learner, 2026-11-16: "i cant commit 27 … sprints to
  any one subject"). Research a delta topic needs goes into the same sprint as the file that uses
  it, not into a sprint of its own.
- **Order.** After the pilot, files are built in START-HERE priority order, **but a file's
  prerequisites (its header's "needs") are built first**, because each file recalls terms from them.
- Changes to `tools/` or this spec are made in an interactive session (`auto.py` sessions edit only
  the subject folder).

### 7.3 Tooling (in `tools/`)

- `study_pack_build.py`: building some files (`only=`) rebuilds their PDFs and then reassembles the
  combined PDF from **every** per-file PDF; a partial build never shrinks the combined PDF.
- `figlib.py`: the shared figure helpers (SVG export, mathtext labels, axes, boxes, arrows) and their
  known fixes. Subject figure modules import it instead of copying helpers.
- `fig_overlap_check.py`: draws every figure and reports labels that overlap each other or are cut by
  the figure edge. It runs in every build; a reported overlap is fixed before delivery.

### 7.4 Rules

- **Pilot first.** For a new subject, build `00` and one topic file, get the learner's sign-off, then
  build the rest. A full pack is never built on an unconfirmed shape.
- **The engine does all verification.** Every number and every derived expression is recomputed by a
  script in the pack's `src/` (one `verify_*.py` per unit or file, using the constants the pack
  prints; independent method where one exists), and every script passes before a build. Printed
  answers are compared with the book's; mismatches are flagged as possible book errors.
- **Source of truth is the source.** Text in `src/content/`, figures in a figures module, one build
  script. PDFs are generated and never edited by hand.
- **Facts** come from the prescribed textbook via the subject's knowledge base. Professor material
  sets scope, emphasis and question forms.
- **Log first.** A progress-log line precedes the build (`CLAUDE.md`, live logging).
- **Page review, one pass.** Render the new files' pages at low resolution, 4 pages per image; look
  at each; zoom only on suspect figures.
- **Acceptance check before delivery** (all must be true):
  - START-HERE has the ranked table with evidence and times.
  - Every topic file has the symbol table, and every symbol it uses is in it.
  - Every Build step names one idea and has a bridge, a guess line, an explicit answer and a Check.
  - Every graph caption states its axes and what one point means.
  - Every file has Exam form, Traps, Self-test, and Answers at the end.
  - No term is used before it is defined.
  - The verification scripts and the overlap check pass, and every page has been looked at after
    the final build.

## 8. Naming, and what does not conform

- **"v1" is not a format.** A pack is named `<SUBJECT>-study-pack` (optionally with the exam: `-MTE`,
  `-ETE`). If the learner says "v1" or "like the last one", check the pack they mean against this file
  before building; if it does not conform, say so and build to this file.
- **Packs that do not conform and must not be copied:**
  - `subjects/sem-3/04-digital-electronics/study-pack/pdf/DE-v1.pdf` (rejected 2026-10-17)
  - `subjects/sem-3/03-electronic-devices-1/study-pack/pdf/EDC-ETE-v1.pdf` (rejected 2026-11-14)
  - `subjects/sem-3/04-digital-electronics/study-pack/pdf-ete/DE-ETE-v1.pdf` (rejected 2026-11-14)

  They have one question and one Check per whole topic, dense pages, no ranked start page, no Exam
  form, no Traps, no Self-test. Their figures, questions and verification scripts are sound and are
  reused when they are rebuilt.
- **v1.2 files that do not meet v1.3** (too compressed: ideas merged, symbols named but not
  explained; learner, 2026-11-15/16). Their questions, figures and verify numbers are reused:
  - `01-statistics-and-probability/study-pack-v12/` files 01–16
  - `04-digital-electronics/study-pack-v12/` files 01–19
  - `03-electronic-devices-1/study-pack-v12/` files 04–14 (01a–03b are built at v1.3 depth)
- **Where the reference files differ from this spec** (do not copy these parts):
  - Its START-HERE asks the learner to mark each Check clean / struggle / wrong. The spec has no marking.
  - Topic files with no board question open on Predict prompts throughout; that is allowed, but a real
    question is used wherever one exists.
  - They have no symbol table and no running example, and are shorter than §2 allows.

## 9. Self-regulation

This file is the single place the format lives. It is kept true by rule:

- **Trigger.** The learner states a preference about how packs are made ("from now on…", "this isn't
  what I wanted", approval or rejection of a pack), or approves a pilot that differs from this file.
- **Action, same session, before any further building:**
  1. Edit the rule it changes in §2–§8. A new rule that contradicts an old one replaces it; nothing
     is left standing in two versions.
  2. **Do not make a new version for a small change.** Amend the current version in place and add a
     dated line under it in the changelog, quoting the learner's words. A new version number is made
     only when the learner asks for one, or when the section order of a file or the order of a Build
     step changes; the title and `CLAUDE.md`'s pointer are then updated together.
  3. Keep the changelog line short: what changed and the learner's words.
  4. Add the matching one-line entry to `learner-preferences.md` §3 if it is a general preference.
  5. If an existing pack now fails the acceptance check, add it to §8's list.
- **Guardrail.** A requested change that would remove the guess line, the per-step Check, or the
  engine's verification breaks a core principle (`CLAUDE.md`). It is not applied silently: name the
  conflict, offer the nearest alternative, and log it under *Tensions* in `learner-preferences.md`.
- **Observed patterns** (not stated by the learner) are proposed to the learner, not written in.
- **The format changes only through the learner.** Building, editing or adding files in any pack,
  including the Circuits & Systems pack the reference was copied from, never changes this spec or the
  frozen reference. A new file that drifts from the spec is a defect in that file, not a new format.
  The reference copies are replaced only when the learner says so.
- **Rebuilds follow, they do not lead.** Changing this file does not by itself rebuild old packs; the
  learner decides which ones to redo and in what order.

## Changelog

- **v1.0 — 2026-09-15/23.** Shape designed with the learner on `11-computer-architecture-and-processor/
  study-pack-v3` ("i am loving this"): Predict → Build with a Check after each step → Exam form →
  Traps → Self-test → answers at the bottom; question-first with real, tagged questions.
- **v1.1 — 2026-09-25.** `13-circuits-and-systems/study-pack`: PDF output with generated figures, a
  ranked START-HERE, per-file and combined PDFs. Reference build.
- **v1.2 — 2026-11-14.** Written down as a spec for the first time, after three packs were built in a
  dense format copied from `DE-v1.pdf` (learner: "this isnt really what i wanted", "v1 isnt good at
  all", "isnt tier 2 supposed to be default?"). Adds pictorial pages, start-from-known / priming /
  bridges / one idea per page, engine does all verification and no learner marking, pilot before a
  full build, build in priority order, the acceptance check, the "v1 is not a format" rule, and
  self-regulation. Amended 2026-11-14 (reference frozen to three named files; small changes amend in
  place), 2026-11-15 (every graph states what it plots; symbols defined in words), 2026-11-16 ("Build
  up, then combine").
- **v1.3 — 2026-11-16.** Asked for by the learner after approving EDC 01a/01b ("this looks good") and
  rejecting the compressed v1.2 files ("its not a build from scratch explaining every term and
  variable and then combining them together properly"). Topic file gains an opening paragraph, a
  symbol table and a running example (§4). Build step gains a bridge line, terms defined by what they
  count, a "What this graph plots" caption plus a reading table, numbered derivations, and an
  explicit answer to every Predict (§5). Files open on a concrete anchor (§6). Length set by ideas,
  a/b split replaces the 4–8 page rule (§2). §7 gains the subject brief, the session and sprint
  budget (learner: "i cant commit 27 … sprints to any one subject … much better would be 9-10
  sprints … only if it is seriously nessesery does it go upto 15"), build order with prerequisites
  first, and the build, figure and overlap tooling. v1.2 files listed as not meeting v1.3 (§8).
