# Handoff — read at session start, then reset

> Written 2026-11-17 ~22:45 by the session that drove Stats → DE (its context reached 214k, so the
> learner moved to a new terminal). History lives in progress logs and git; this is only what is open.

## 1. Task: restart DE's auto run (learner said: don't restart until the new terminal)
- **State:** Stats is **DONE** (S0–S9, 1492 checks, 263 pp). DE: S0a, S0b, S1, S2, S3, S4 done; **S5
  partial** (see `subjects/sem-3/04-digital-electronics/sprints.md` → Current hand-off). S6–S9 left.
- Start it with the chain (handbrakes + crash restarts), **from the repo root, in the background**:
  `bash tools/auto-chain/chain.sh sem-3/04-digital-electronics`
  - It runs `auto-v2.py run … --soft-limit 180000 --hard-limit 210000 --sessions 12 --hours 20
    --wait-on-limit --yes --check weekly_check.py` and loops: crash-stop → wait for the network,
    restart (3 in a row → halt); `--sessions`/`--hours` cap → fresh run; usage limit → retry in 1h;
    tamper/stuck/BLOCKED/stop-requested → halt (needs a human). Logs: `tools/auto-chain/chain.log`,
    `run-<subject>.log`. Stop between runs: `touch tools/auto-chain/STOP`. Graceful stop now:
    `python auto-v2.py stop`.
  - The auto run is a **child of the Claude session that starts it**: closing that terminal kills it.
- **Weekly brake:** off until the weekly reset (~2026-11-18 22:30). Weekly was 75% at 18:26. After
  the reset the learner will ask for **80%**: set `THRESH` in `tools/auto-chain/weekly_check.py`
  (re-read every check; no restart needed).
- **Per-session audit** (learner asked): `python tools/auto-chain/audit.py <session-number>` → calls,
  Sonnet/agy use, cost, weekly %, denied commands. Wake on each session end with a background
  until-loop on the line count of `.claude/auto/log.jsonl` (one wake per session; cheaper than Monitor).
- **Contract changes need a run boundary** (editing `auto-v2-contract.md` mid-run trips the tamper
  brake and halts the run): wait for a session to end → `python auto-v2.py stop` → patch → commit → restart.

## 2. Measured this run (for the audit)
- A heavy Opus sprint is $3–5; the 5-hour window, not the weekly one, is what stops work
  (one window ≈ 3–4 DE sprints); auto sleeps through it.
- Sonnet delegation of figure code is now mandatory in the contract (S1 had skipped it: $5.01 all
  Opus); S3 onward complies. agy (`--model gemini-3.8-flash-high`) does page checks; it sometimes
  times out once (exit 124) and succeeds on retry.
- Hard-limit crashes in DE sessions 4 and 9 (a whole-file Write started at ~172k) → contract rule
  added: no whole-file Write above 150k.

## 3. After DE
- EDC (`sem-3/03-electronic-devices-1`, ETE 24 Nov): E0 transcription → **agy first** (pattern: one
  `agy --model gemini-3.8-flash-high -p` job per deck writing to a scratch file, split decks over ~40
  image-only pages, check page coverage by script, spot-check, assemble brief, commit), then
  `DONE_MARK="E11 (done|complete)" bash tools/auto-chain/chain.sh sem-3/03-electronic-devices-1`
  (EDC sprints are E0–E11; DONE_MARK is a regex over the progress log: the logs write "S3 done" or
  "S1 complete", rarely "Sprint …"; check EDC's wording first).
- `study-pack-v12` → `v13` rename (per subject, only when no run is active): see the previous
  hand-off in git history (commit 2148328) §6.
- Remind the learner: `! git push` (auto commits are not pushed).
