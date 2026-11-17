# Handoff — read at session start, then reset

> Written by the session that ended (2026-11-17, ~05:50); read and **reset** by the next one
> (`CLAUDE.md` §0c). History lives in `progress-log.md`s and git; this is only what is open.

## 0. First actions (in order)
1. `python auto.py status` — is a run active? (State is shared by `auto.py` and `auto-v2.py`.)
2. `git status` + `git log --oneline -8`. At hand-off: tree clean, HEAD = the hand-off commit,
   **~25 commits unpushed** → remind the learner: `! git push`.
3. Ask the learner whether they ran the two learner steps in §3 (Stats restart, agy permission).

## 1. ETE dates (settled): Stats **19 Nov** · DE **21 Nov** · EDC **24 Nov**

## 2. Stats (`sem-3/01-statistics-and-probability`) — v1.3 rebuild, run STOPPED
- Done at v1.3: S0, S1 (01, 02a, 02b), S2 (03a, 03b, 08), S3 (09a, 09b; session 8), S4 (04a, 04b, 05;
  session 9). verify.py 865 checks pass after S4.
- **S5 partial** (session 10 hit the usage limit, commit dd61029): `06-normal.md` mostly rewritten +
  figures + KB 02 facts; **07 not started**. Session 11 (recovery) was killed by low system memory after
  start-up reads; it wrote nothing.
- Left: S5 rest, S6 (11+12), S7 (13+14), S8 (15+16), S9 (10 + integration). Plan: its `sprints.md`.
- **Restart from the learner's own PowerShell window** (a background task here gets killed under
  memory pressure):
  `python auto-v2.py run sem-3/01-statistics-and-probability --soft-limit 180000 --hard-limit 210000 --sessions 12 --hours 14 --wait-on-limit --yes`
- Check per session (learner asked: tokens saved per session). Baselines: S3 = 55 calls, $2.85 list;
  S4 = 75 calls, $4.36. Old auto.py sprint ≈ $4.30. Read `.claude/auto/runs/*session-NNN.jsonl`
  `result` event (`total_cost_usd`, `usage`) + `boot_context` in `.claude/auto/log.jsonl`. First
  sessions with the new cuts (5-min cache, fewer-bigger-steps rule) have not been measured yet.

## 3. Token work (auto-v2) — state
- `auto-v2.py` + `auto-v2-contract.md` (commits 63c030a, 603e2c6): no CLAUDE.md/memory/skills/
  connectors; 8 tools incl. web; `FORCE_PROMPT_CACHING_5M=1`; contract has the "fewer, bigger steps"
  rules. Boot ≈ 10.5k (was 34k; ~53k after reads). `auto.py` is unchanged (kept as fallback).
- auto-v2 protects its own files: never edit `auto-v2.py`/contract while a run is active (tamper check).
- Graphify was evaluated and rejected (savings are for codebases; our reads are ~20% of a session).
- Parallel runs were discussed; learner declined (no token saving, limit drains faster).

## 4. Google helper lane (learner wants it used as much as safely possible, to save Claude tokens)
- **Gemini CLI is retired** for individual accounts ("migrate to Antigravity"). **Antigravity CLI `agy`
  1.0.3 is installed and logged in**; its default model is *Claude Sonnet 4.6 (Thinking)* (on Google's
  quota). **Learner's Google plan is promotional: Gemini Flash only, no Pro.**
- Files: `GEMINI.md` (rules + Flash-suited jobs: transcription, visual page checks, mechanical edits,
  inventories; never teaching text or truth calls) · `GEMINI-TASK.md` (current task: **DE S0a** —
  transcribe 15 decks + MTE + 2 practice sets into `study-pack-v12/src/brief.md` §1, question bank §2).
- **Driving agy from Claude: WORKS (tested 2026-11-17 ~06:10).** The learner added `Bash(agy *)` to
  `.claude/settings.local.json`. Command:
  `agy -p "<task>" --dangerously-skip-permissions --add-dir <scratch> --log-file <scratch>/agy.log`
  (run with `timeout`, `< /dev/null`; default `--print-timeout` is 5 min — raise it for long jobs).
  Test result: model **Gemini 3.8 Flash (High)** (learner set it via `/model` interactively; it carries
  over to `-p`), read GEMINI.md correctly, wrote its answer to a file. **stdout is empty in print mode**:
  every job must write its result to a file. Check the model per job: log line "Propagating selected
  model override". `~/.gemini/config/mcp_config.json` is empty/invalid (harmless log error).
- **Next step:** run DE S0a through agy one deck at a time (one `agy -p` per deck, a few minutes each),
  spot-check each against the PDF pages, then the MTE paper and practice sets; then review + commit.
- **Review rule:** every agy job → Claude reviews `git diff` (spot-check transcriptions against the
  source pages), then commits. Its facts are leads, not verified.
- **Planned agy jobs:** DE S0a (now) · EDC E0 transcription · page-render visual checks for every
  sprint (replace Claude viewing contact sheets) · Stats S9 mechanical part (START-HERE rows,
  cross-refs, mock re-pointing) · EDC E11 overlap/mechanical fixes · v12→v13 renames (§6).
- Adding agy to auto-v2 as a lane (sprint rows tagged `[agy]`) is **not built**; design it with the
  learner after the manual/driven trial shows Flash quality is acceptable.

## 5. DE and EDC
- DE (`sem-3/04-digital-electronics`): S0 split (2026-11-17) → **S0a agy** (task ready) / **S0b Claude**
  (review S0a, §3 constants vs KB, §4 file plan, figure list, `src/verify.py`); then S1–S9 per `sprints.md`.
- EDC (`sem-3/03-electronic-devices-1`): E0–E11 per `sprints.md`; E0 transcription → agy first.
- Order is by exam: Stats → DE → EDC. Weekly Claude limit is the binding constraint.

## 6. Still open from before
- **Rename `study-pack-v12/` → `study-pack-v13/`** per subject, only after its run finishes and never
  while auto is running: log line → `git mv` → `grep -rn "study-pack-v12"` and fix every path
  (sprints.md, progress-log resume, README, START-HERE, `src/build.py`, EDC `cheatsheet/`,
  `study-pack-format.md` §8, `study-pack-sprint-protocol.md`, research-queue, memory files; history
  lines stay) → full build + every `verify*.py` → commit. Good agy job, Claude verifies.
- **Repo visibility:** learner said the material "is already on github and public". CLAUDE.md requires
  the remote to stay **private** (`exam-pack/` is copyrighted). `gh` is not installed; ask the learner to
  check GitHub → Settings → visibility and make it private.
- Learner decisions pending: Assignment 1 LA 2 taught on the textbook's row (flagged in the slip table);
  one verify.py per pack vs per unit; whether overrun sessions count against the sprint budget.
- System memory was low (3.2 GB free of 16 GB, 7 `claude.exe` processes): suggest closing idle windows.
