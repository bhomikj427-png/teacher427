# Handoff — read at session start, then reset

> Written by the session that ended; read and **reset** by the next one (`CLAUDE.md`, session start
> step 0c). Holds only what the next session needs to start. History lives in `progress-log.md`s and git.

## Task (from the learner, 2026-11-16)

Two jobs. **Design first: build nothing until the learner signs off.**

1. **Write study-pack-format v1.3.** Start from v1.2 plus what the learner approved in EDC 01a/01b
   (`subjects/sem-3/03-electronic-devices-1/study-pack-v12/src/content/01a-*.md`, `01b-*.md`: the new depth model):
   - one idea per step, never merged
   - every symbol explained in words: what it counts, what sets it
   - every graph states its axes and what one point means (already in v1.2 §5.4)
   - a long topic is split into a/b files, not compressed (replaces the 4–8 page rule)

   Also add the efficiency rules agreed 2026-11-15:
   - a per-subject brief, built once before any file: slides transcribed (equations and slips included), question bank,
     constants checked against the KB, gaps filled up front, figure list
   - a shared figure library and an automatic label-overlap check in `tools/`
   - `tools/study_pack_build.py`: building one file must not overwrite the combined PDF
   - one short fresh session per 1–3 files (`auto.py` where possible)

   Show the learner the v1.3 diff and the plan, then wait for sign-off.
2. **After sign-off:** plan the upgrade of the three v1.2 packs to v1.3:
   `01-statistics-and-probability` (18 files), `03-electronic-devices-1` (19), `04-digital-electronics` (21), all in
   `study-pack-v12/`. Order: each pack's START-HERE priority. EDC 01a/01b already meet v1.3, so don't redo them.
   Give the learner the order, the per-session batches, and the decisions they need to make.

## Read first

`study-pack-format.md` · EDC `01a`/`01b` content files above · `subjects/sem-3/03-electronic-devices-1/study-pack-v12/src/{build.py,figs_u1.py,verify_u1.py}`
· `tools/study_pack_build.py` · `auto.py` (memory: unattended runner).
