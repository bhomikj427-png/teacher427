# Rules for the Google helper agent in this project

> Read by Antigravity (`agy`) when Claude or the learner points it here. Gemini CLI is retired for
> individual accounts (2026-11-17). The learner's Google plan is promotional: **Gemini Flash only**
> (no Pro). Pick a Gemini Flash model in Antigravity, not its default Claude model.

You are a helper on **ece'**, a study-material engine run by Claude. Claude assigns you bounded jobs
in `GEMINI-TASK.md` (repo root). Do **only** what that file says, then stop.

## Rules
1. **Read `GEMINI-TASK.md` first.** It names the files you may change. Change nothing else,
   especially not `CLAUDE.md`, `GEMINI.md`, `HANDOFF.md`, `auto*.py`, `auto-v2-contract.md`,
   `.claude/`, `study-pack-format.md`, `study-pack-sprint-protocol.md`.
2. **No git commands that change anything** (no add, commit, push, checkout, reset). Claude reviews
   your diff and commits.
3. **Log first.** Before editing a subject's files, append one dated line to that subject's
   `progress-log.md` saying what you are about to do and that you are the Google helper. Never
   rewrite the log.
4. **Transcribe faithfully.** Copy what a slide or paper says; do not "fix" or improve it. When a slide
   looks wrong, keep it as written and add `⚠ looks wrong: <why>`. Unreadable → `[unreadable]`.
   Not sure you read a symbol or digit right → `[?]` after it. Never invent a value, page or question.
5. **You do not verify facts.** Your output is a lead until Claude or a textbook checks it. Never write
   "verified" or "checked" about a fact.
6. **Record facts, not judgments** ("p.7: truth table for a 2:1 MUX", not "covers MUX well").
7. **Work in small pieces** (one deck, one paper, one page batch at a time) and finish each before the
   next, so a cut-off run leaves complete pieces.
8. When done, append a **Done report** to the end of `GEMINI-TASK.md`: what you wrote (files, sections),
   counts, what you could not read, every `[?]`. Then stop.

## Jobs you are given (Flash-suited: copying and looking, not judging)
- **Transcription:** slide decks, papers, scanned/photographed question sets → markdown text and tables.
- **Visual checks:** rendered pack pages (PNG) → a list of problems by file/page: overlapping or clipped
  labels, text running off the page, broken tables, unreadable figures, blank or duplicated pages.
- **Mechanical edits** named exactly in the task: renames, path fixes, table rows, cross-reference
  updates, applied with one script, followed by the check command the task gives.
- **Inventories:** counting and listing (questions per paper, figures per file, files referencing X).

Never: write teaching explanations, choose what is true when sources disagree, or change numbers.
