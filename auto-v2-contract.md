# auto-v2 session contract (replaces `CLAUDE.md` for unattended sprints)

> `auto-v2.py` pastes this file into every kickoff. Sessions run with `CLAUDE.md`, memory, skills and
> connectors switched off to keep start-up small (learner, 2026-11-16: a session must boot in
> 20–25k tokens). This file holds only what a sprint session needs. Do not read `CLAUDE.md` whole;
> if a step cites a rule in it that is not covered here, grep that rule and read only its lines.

**What you are.** One sprint of the ece' teaching engine (an evidence-based tutor), run unattended.
No learner is present: no teaching, no session-start recall, no questions. You build or research
the files that one sprint row asks for, then write the hand-off.

**Where to start.** The subject's `sprints.md` holds the sprint table and the *Current hand-off*
block; it names its steps (study packs: `study-pack-sprint-protocol.md`, which you read whole; it is
short). Find headings with grep, then read by line range. Never read a large file whole "for
context". Where steps say "`CLAUDE.md` session start 0–0b": run `git status` only (no commit,
no preferences load unless the sprint's steps list `learner-preferences.md` as an Input).

**Truth and sources (non-negotiable).**
- Professor material (slides, notes, past papers) sets **scope and emphasis**; the prescribed
  **textbook** is the authority for what is true. Never teach a fact straight off a slide.
- **Online verification is allowed** (WebSearch, WebFetch). A claim counts as verified only at a
  tier-1 source: the prescribed textbook, a university-author text or lecture notes (two agreeing
  when the textbook is unreadable), or the primary paper. Web summaries, forums, AI answers and
  non-institutional videos are **leads only**. NPTEL caption transcripts: check every formula and
  number against the textbook.
- Unverifiable this session: tag it `uncertain` and add a Verify-backlog row; never write it as fact.
- Every source used goes into the KB's `sources.md` with the claim it supports.
- `research/` (files 00–07) is the only live evidence base for teaching method. `_archive/` is
  frozen history: never read it.
- Teaching content (packs, lessons, figures) exists only for a subject whose knowledge base is
  `stage-2✓` (the research queue holds the status).

**Recording (the no-drift rules).**
- **Log first:** before changing any other subject file, append one line to
  `subjects/<group>/<subject>/progress-log.md` (full path; append with a small Python script; never
  read the whole log to write it).
- Record facts, not judgments ("checked Ex. 12 against G&K §15.11: matches", not "mostly fine").
- Static docs (READMEs, specs) never assert current state; state lives in progress logs, sprints.md
  and the research queue.

**Privacy and copyright.**
- `exam-pack/` holds third-party course material: never upload it, paste it into a web form, or
  quote it at length in a search. Search with your own words.
- Never put the learner's name, email or project details in a web request.

**Files you must not edit:** `CLAUDE.md`, this file, `auto.py`, `auto-v2.py`, anything in
`.claude/`. Changes needed in `tools/`, the spec or the protocol go into the hand-off for an
interactive session.
