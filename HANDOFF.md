# Handoff — read at session start, then reset

> Written 2026-11-19 ~05:40, before the learner's PC restart. History is in the progress logs and git;
> this file holds only what is open. Learner: "i have edc and one subject from scratch to do this week
> alone, so whatever changes we wanna do we gotta do now".

## 0. First, in this order
1. **Session-start checks:** `git status` (expect clean), `git log origin/main..main` (push if ahead).
2. **Ask the learner (one message, three questions):** (a) which subject is the from-scratch one, and its
   ETE date; (b) is "exam-ready, top-ranked topics first" (stage-1✓ + about 6–8 files, logged as a
   subject-scoped gate exception like MoT) acceptable for it, or full build; (c) OK to switch auto
   runs to **Sonnet builds / Opus checks** (§2) once a 1-sprint trial passes?
3. **Restart EDC** (it is not running; the learner chose to wait until after the PC restart):
   `DONE_MARK="E11 (done|complete)" bash tools/auto-chain/chain.sh sem-3/03-electronic-devices-1`
   from the repo root, Bash `run_in_background`. Then a watcher on `.claude/auto/log.jsonl` line
   count (one wake per session) and `python tools/auto-chain/audit.py <n>` on each session end.
   Before starting: the learner closes Brave / Antigravity IDE and sets the PC not to sleep (§3).

## 1. Where we are
| Subject | ETE | State |
|---|---|---|
| Stats | 19 Nov | done (S0–S9) |
| DE | 21 Nov | **done**: S0–S9 at v1.3, verify 821/0, 312 pp; last 24 pages checked + 4 figure fixes (46a3f69) |
| EDC | 24 Nov | **E0–E11 all not started.** Session 1 ran ~6 min then hit the usage limit (f30c7e8, nothing built). Session 2 died at start (Windows 0xC0000142, see §3). Head start: `study-pack-v12/src/e0-transcripts/` (16 agy transcripts, README) and the sprints.md note telling E0 to use them |
| from-scratch subject | ? | not chosen yet (§0.2) |

## 2. Token budget (the real constraint this week)
- Weekly limit resets **2026-11-25 22:30**. At 05:22 on 19 Nov it was **15%** used; the brake stops runs
  at **80%** (`tools/auto-chain/weekly_check.py`, THRESH). So **65 points** left this week.
- Measured (DE sessions 16–19, `audit.py`): a full sprint session = **3–5% weekly**, $4.9–7.1, of
  which Opus is $4.7–6.1. Crashes and recoveries make it ~1.9 sessions per sprint, so **~4–5% per sprint**.
- Need at current cost: EDC 12 sprints (6 include new research) ≈ **55–60%**; a from-scratch subject
  (KB research ~5–8 sessions + ~10 pack sprints) ≈ **60–80%**. Total ≈ 120–140% against 65 → **does not fit.**
- **Plan to make it fit (design agreed in outline with the learner; implement after the §0.2 answers):**
  1. **Sonnet builds, Opus checks.** `auto-v2.py` has no model option: the `claude -p` child runs the
     default (Opus). Add a `--model` passthrough (and keep it out of the protected/tamper set
     only if the contract allows; patch only at a run boundary: `python auto-v2.py stop` → patch → commit
     → restart). Sprint sessions on Sonnet; one short Opus check session per file (numbers, facts,
     verify output). Expected 2–3× cheaper. **Trial 1 sprint first and measure with audit.py**: EDC E1
     is a fair trial (diode circuits, well-sourced).
  2. **Scope the from-scratch subject to the exam:** stage-1✓ (exam-ready) + top-ranked files only,
     ~6–8 sprints, if the learner says yes (§0.2b). Log it as a subject-scoped exception in
     `research-queue.md` (the CLAUDE.md teaching-gate clause allows learner-logged exceptions).
  3. **agy for all mechanical work** (transcription, page checks, source lists): `tools/agy-edc-e0.sh`
     is the pattern. Only the learner can launch big agy batches (the classifier blocks Claude from
     starting many `--dangerously-skip-permissions` agy jobs); give them a script + `! bash <script>`.
  - Rough target with 1+2: ~20% per subject. EDC on Sonnet ≈ 25–30% + new subject ≈ 20–25% → fits in 65.
- Next week the learner needs **3 subjects** (not named yet): same setup, ~20% each ≈ 60%.

## 3. Machine problems seen this session (and what fixes them)
- **Low memory** (about 4 GB free) made Claude Code kill background jobs (chain wrapper, watchers) three
  times. After such a kill, restart only when the learner asks. Brave (~49 processes) and Antigravity
  IDE are the big users. `CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP=1` in Claude Code's environment
  stops the killing (learner's choice).
- **0xC0000142 / git returning nothing:** Windows could not start processes for over a minute (likely
  sleep/resume). The auto run then reads the branch as "" and refuses to commit. auto-v2 now retries
  that read for 60 s (b54348d); it was not enough on 19 Nov 05:11. Fix: PC set not to sleep during
  runs; if it recurs, make the empty-branch case wait longer or end the session as a CRASH (so the
  chain restarts) instead of a commit refusal.
- If the chain halts on "branch changed from main to ''": the work is still in the tree. Commit it by
  hand from the session's progress-log line (done once: e6ff646), then restart the chain.

## 4. Standing rules for this run (memory has the detail)
- Decide build/format calls yourself and log them; ask only for real forks (the §0.2 questions are forks).
- Opus only for Opus-worthy work; mechanical work goes to Sonnet subagents or agy.
- `GEMINI.md` is agy's rulebook (restored 2026-11-18, with a scope rule). Keep it; give tasks in the prompt.
- Remind the learner to `! git push` (auto commits are not pushed).
