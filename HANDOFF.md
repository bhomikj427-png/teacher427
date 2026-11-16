# Handoff — read at session start, then reset

> Written by the session that ended; read and **reset** by the next one (`CLAUDE.md`, session start
> step 0c). Holds only what the next session needs to start. History lives in `progress-log.md`s and git.

## Task (from the learner, 2026-11-16)

**After the v1.3 sprint runs finish** (`python auto.py status`; plans in each subject's `sprints.md`),
rename each pack folder `study-pack-v12/` → `study-pack-v13/` (learner: "rename it to v13 after the
runs finish"). Do it only for a subject whose run is finished; never while `auto.py` is running.

Subjects: `sem-3/01-statistics-and-probability` (ETE 19 Nov) · `sem-3/04-digital-electronics` (21 Nov) ·
`sem-3/03-electronic-devices-1` (24 Nov). Runs go in that order; Stats started 2026-11-16 21:00.

Per subject:
1. Progress-log line first (log-first rule).
2. `git mv study-pack-v12 study-pack-v13`.
3. Fix every path reference: `grep -rn "study-pack-v12"` across the repo (sprints.md, progress-log resume,
   README, START-HERE, `src/build.py` path comments, EDC `cheatsheet/` paths, `study-pack-format.md` §8,
   `study-pack-sprint-protocol.md`, research-queue, memory files). History lines in progress logs stay as
   they are (they record what was true then).
4. Full build (`python study-pack-v13/src/build.py`) + every `verify*.py` passes, to prove nothing broke.
5. Commit.
