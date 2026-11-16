# Prompt: give a subject pedagogy-style sprints + hand-offs (so auto.py can run it)

Paste into a fresh window, replacing `<SUBJECT>` with the folder under `subjects/`
(e.g. `sem-3/03-electronic-devices-1`, `verilog`). One subject per window.

---

<SUBJECT>: set this subject up for automated sprints, with hand-offs exactly like pedagogy's.

Template: `subjects/pedagogy/sprints.md`. Copy its **structure and rules**, not its content. Read its protocol, hand-off template, sprint table and backlog sections. Don't read pedagogy's knowledge base.

1. **Find where this subject really stands.** Read its `progress-log.md`, learner profile and plan/state files (e.g. `research-queue.md`, `two-stage-depth.md`, exam calendar, any manifest). Check them against the files actually in the subject folder (newest dated artifacts). State the gate stage (stage-1✓ / stage-2✓ / teaching) and what work is left.

2. **Write `subjects/<SUBJECT>/sprints.md`** with these sections, in pedagogy's order and format:
   - **Header rule:** one sprint = one session, fully finished (researched *and* written), ending with a hand-off. A sprint too big to finish splits into a/b, never half-done.
   - **Sprint protocol:** pedagogy's steps, adapted to this subject's sourcing rules (`subject-research-protocol.md`; professor material = scope, textbook = truth; NPTEL via `tools/fetch_transcripts.py`). Keep:
     - session entry;
     - "read only the Inputs";
     - log-first;
     - write-as-you-verify;
     - confidence tags;
     - misconceptions as a first-class output, if the subject has misconceptions;
     - Done-when self-check;
     - move open items to the Verify backlog;
     - overwrite the hand-off.
   - **Define "verified" once in the protocol and use only that rule.** Example: "checked at the textbook/primary source this session; abstract or slide only = not verified".
   - **Sprint table:** `# | Sprint | Inputs (read only these) | Outputs | Done when | Status`. It covers all remaining work up to the subject's goal (stage-2✓, and the study pack if one is planned). Size each sprint to finish well inside one session: about 100–150k tokens, one or two KB files or one pack topic file. Make Done-when items checkable facts, not judgments.
   - **Mark learner-only work.** Any sprint that needs the learner (live teaching, a sign-off, choosing between options, exam dates) is marked **[learner]** and placed at the end of a run of sprints that can run unattended. An unattended session stops there with STATUS: BLOCKED.
   - **Hand-off template:** pedagogy's, plus an *Assumptions to review* line.
   - **Verify backlog:** a persistent table; rows leave only when resolved, naming the sprint that closed them.
   - **Assumptions to review:** a persistent section. Assumptions never live only in the hand-off, which is overwritten every sprint.
   - **Research tooling notes:** helper scripts live in `subjects/<SUBJECT>/research-tools/` (committed), never in a temp folder.
   - **Current hand-off:** filled in for the first sprint, with its first concrete action and its "Read at start" list.

3. **Make the hand-off findable.** In `progress-log.md`'s Session resume, add one line: "Research/build runs in sprints: resume from `sprints.md` → *Current hand-off*." Write the progress-log line first, before writing `sprints.md` (log-first rule).

4. **Don't duplicate state.** If a plan already lives elsewhere (`research-queue.md` row, `two-stage-depth.md`), `sprints.md` becomes the plan for this subject. The old place gets a one-line pointer to it; nothing is copied twice.

5. **Don't touch:**
   - `CLAUDE.md`, `.claude/`, `auto.py`, or other subjects;
   - don't start auto.py.

   Commit and push as usual (CLAUDE.md §5c).

6. **Finish with a short report:**
   - the stage you found;
   - the sprint list, with the **[learner]** sprints marked;
   - how many sprints can run unattended before the first **[learner]** stop;
   - a ready auto.py command, e.g. `python auto.py run <SUBJECT> --until "S5 done"`.

   If almost all the remaining work is live teaching, which can't run unattended, say so and create only the sprints that can.
