# Study-pack format — v1.2

> **The one format for every study pack** (PDF or `.md`, any subject). Loaded by reference from
> `CLAUDE.md`. A pack is built to this file, **not copied from another pack**. If this file and an
> existing pack disagree, this file wins.
>
> **Reference build:** `subjects/sem-3/13-circuits-and-systems/study-pack/` (read `pdf/00-START-HERE.pdf`
> and `pdf/01-elements-and-sources.pdf`; source in `src/content/*.md`, builder `src/build.py`). It shows
> what a finished pack looks like. Where it differs from the rules below (§8), the rules win.
>
> **This file regulates itself** (§9): every format change the learner states is written here, in the
> rule it changes, the same session.

---

## 1. What a pack is for

A pack is something the learner studies from alone. It must teach from the learner's actual level,
make them produce an answer before they read one, and tell them what to write in the exam. A pack that
reads as a summary has failed, however correct it is.

## 2. Pack layout

- `00-START-HERE` first, then **one file per topic**, numbered in the order the professor teaches
  (`01-…`, `02-…`), then a mock paper as the last file.
- Output: one PDF per file **and** one combined, bookmarked PDF.
- A topic file is short: roughly 4–8 pages. A long topic is split into two files, never compressed.

## 3. `00-START-HERE` (fixed sections, in this order)

1. **Priority order: if time is short, study in this order.** A ranked table: rank · file · why it
   ranks here (the evidence: past-paper questions, board questions, marks flagged by the professor) ·
   what to do first in that file · rough time. State plainly how strong the evidence is.
2. **The path through the pack.** A flow map of the files in order, grouped by unit, and one
   paragraph on which file needs which.
3. **What each file teaches.** Table: file · syllabus item · what it teaches · how many real questions.
4. **Where the questions come from.** The source tags used in the pack, and how many questions are
   real (P1: professor's papers, board questions, assignments) and how many are textbook (P2).
5. **How each file runs.** The six parts of §4 in one small table, and the one rule: guess on paper
   before reading on.
6. **Units and symbols used everywhere.**
7. **Where the professor's material disagrees with the pack**, if anywhere.
8. **How the pack was checked.**

## 4. A topic file (fixed sections, in this order)

| Section | Contents |
|---|---|
| **Header line** | Source pages · syllabus item · how many real questions · which earlier files it needs |
| **Map** | A flow map of the file's steps (≈ 3–8 nodes), the current one highlighted. A small table or figure of the whole idea may follow |
| **The questions this file answers** | The real questions, quoted, each with its source tag and marks |
| **Build** | Numbered steps. This is the teaching (§5) |
| **Exam form** | Exactly what to reproduce in the exam: statements, procedures as numbered steps, the formulas |
| **Traps** | The mistakes that cost marks, each in one line |
| **Self-test** | 5–8 questions covering the file, mixed recall and application |
| **Answers** | On the last page(s) of the file: every Check, then the Self-test |

## 5. A Build step (the unit of teaching)

Each step teaches **one idea** and runs in this order:

1. **Question or Predict.** A real question, quoted and tagged (professor's material first, the
   prescribed textbook second, never invented and passed off as real). If no real question exists for
   the idea, a **Predict** prompt, labelled as such.
2. **Guess first.** One line that asks for an answer on paper before reading on. This line is the
   mechanism (pretesting, `research/02 §1, §5`); it is never dropped.
3. **Terms.** At most three new terms, each defined before it is used.
4. **Figure.** The figure that carries the idea comes before the prose about it.
5. **Teaching.** Short: about 60 words per block, a list or table where the content is a list or a
   table. Concrete first, general statement after.
6. **Answer** to the opening question, worked with every intermediate value.
7. **Check.** One to three questions on this step only. Answers go to the end of the file.

A step is about half a page. A topic has as many steps as it has ideas: there is no fixed count, and
ideas are never merged to save space.

## 6. Rules that apply to every page

- **Start from zero.** Assume no prior knowledge of the subject unless the learner's profile says
  otherwise. Every term is defined before first use.
- **Open on where the topic sits.** Each file's header and map say what it builds on; the first step
  starts from something the learner already has.
- **Bridges.** Between steps, one sentence on why the next idea is needed.
- **One idea in focus per page.** A page holds at most one figure-led idea plus its Check.
- **Pictorial.** Figures carry structure; text is the caption. Generated figures by default; real
  photos or screenshots where they exist and show the thing better. Provenance on every borrowed image.
- **Real symbols.** Σ Π ⊕ ≥ ≤ √ and true subscripts/superscripts. No TeX source, no spelled-out
  substitutes.
- **Every sentence adds value.** No narration about the pack itself, no reassurance, no process talk.
- **No marking by the learner.** The pack never asks for self-scores or tick boxes. The learner
  reports only misses.
- **Slips in the professor's material** are flagged in a note box where they occur, with the corrected
  version used in the pack.
- **Page look:** the reference build's: A4, one accent colour, coloured boxes for question / guess /
  check / trap / note, generous white space, footer with pack name and page number.

## 7. Building and checking

- **Pilot first.** For a new subject, build `00` and one topic file, get the learner's sign-off, then
  build the rest. A full pack is never built on an unconfirmed shape.
- **Priority order.** After the pilot, build files in the order of the START-HERE ranking, so an
  interrupted build leaves the highest-value files done.
- **The engine does all verification.** Every number and every derived expression is recomputed by a
  script in the pack's `src/` (independent method where one exists), and the script passes before a
  build. Printed answers are compared with the book's; mismatches are flagged as possible book errors.
- **Source of truth is the source.** Text in `src/content/`, figures in a figures module, one build
  script. PDFs are generated and never edited by hand.
- **Facts** come from the prescribed textbook via the subject's knowledge base. Professor material
  sets scope, emphasis and question forms.
- **Log first.** A progress-log line precedes the build (`CLAUDE.md`, live logging).
- **Acceptance check before delivery** (all must be true):
  - START-HERE has the ranked table with evidence and times.
  - Every Build step has a guess line and a Check.
  - Every file has Exam form, Traps, Self-test, and Answers at the end.
  - No term is used before it is defined.
  - The verification script passes, and every page has been looked at after the final build.

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
- **Where the reference build differs from v1.2** (do not copy these parts):
  - Its START-HERE asks the learner to mark each Check clean / struggle / wrong. v1.2 has no marking.
  - Topic files with no board question open on Predict prompts throughout; that is allowed, but a real
    question is used wherever one exists.

## 9. Self-regulation

This file is the single place the format lives. It is kept true by rule:

- **Trigger.** The learner states a preference about how packs are made ("from now on…", "this isn't
  what I wanted", approval or rejection of a pack), or approves a pilot that differs from this file.
- **Action, same session, before any further building:**
  1. Edit the rule it changes in §2–§8. A new rule that contradicts an old one replaces it; nothing
     is left standing in two versions.
  2. Bump the version (v1.2 → v1.3 for a rule change; v2.0 if the file or step order changes) in the
     title and in `CLAUDE.md`'s pointer.
  3. Add a dated changelog line below, quoting the learner's words.
  4. Add the matching one-line entry to `learner-preferences.md` §3 if it is a general preference.
  5. If an existing pack now fails the acceptance check, add it to §8's list.
- **Guardrail.** A requested change that would remove the guess line, the per-step Check, or the
  engine's verification breaks a core principle (`CLAUDE.md`). It is not applied silently: name the
  conflict, offer the nearest alternative, and log it under *Tensions* in `learner-preferences.md`.
- **Observed patterns** (not stated by the learner) are proposed to the learner, not written in.
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
  all", "isnt tier 2 supposed to be default?"). Adds the preferences stated since v1.1: pictorial
  pages (2026-09-27), start-from-known / priming / bridges / one idea per page (2026-10-17), engine
  does all verification and no learner marking (2026-10-17), pilot before a full build, build in
  priority order, the acceptance check, the "v1 is not a format" rule, and self-regulation (learner:
  "make it be self regulating with whatever changes i make be made in the ruleset itself").
