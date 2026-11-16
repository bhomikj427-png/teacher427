# Study-pack sprint protocol (shared by every subject's `sprints.md`)

> The fixed steps of one study-pack sprint. A subject's `sprints.md` holds only its sprint table,
> hand-off, backlog and subject notes; it points here for the steps. The content standard is
> `study-pack-format.md` (v1.3). Written 2026-11-16 from EDC's S0 protocol.

## Definitions

- **Sprint = one fresh session**, fully finished (built and checked), ending with the hand-off
  written into `sprints.md`. A sprint too big to finish splits into a/b; it is never left half-done.
  **Budget: 9–10 sprints per subject, 12 fine, more only if seriously necessary** (spec §7.2).
- **Verified** = checked **this session** at a tier-1 text (the prescribed textbook; when none is
  readable, two agreeing university-author texts or notes) or recomputed by the pack's `verify_*.py`.
  A slide, web summary or AI answer is a lead, not verification. Anything else is tagged `uncertain`
  and goes to the Verify backlog.
- **Professor material = scope, textbook = truth.** A fact is never taught straight off a slide.
- **[learner]** marks a step that needs the learner; an unattended session reaching it stops with
  `STATUS: BLOCKED`.

## Steps (every sprint, fixed order)

**Entry**
0. `CLAUDE.md` session start 0b only (`git status`; under `auto.py`, no
   commit). Pack sprints skip step 0 (`learner-preferences.md`): the spec already holds its pack rules. No start-of-session recall: nothing has been taught; the hand-off is the resume.

**Start (lean: the start-up reads must stay under ~10k tokens; learner, 2026-11-16: "68k is outragous")**
1. Read only, each by line range (grep the heading for line numbers first, never the whole file):
   `sprints.md` *Current hand-off* block + this sprint's table row · spec §5 only · the brief's
   section for this sprint's files. **Do not read** `learner-preferences.md`, the whole `sprints.md`,
   the whole spec, or `progress-log.md` (it is append-only: add lines with a small Python append to
   `subjects/<group>/<subject>/progress-log.md` by its full path, never `subjects/sem-3/progress-log.md`;
   never read it to write it). Other Inputs are read when the step that needs them starts, by section.
2. Log the sprint start in `progress-log.md` (log first: before any other file changes).
2b. **The soft limit is a target, not a wall.** When auto.py's context notice arrives, "the current
   step" means: if what is left of the sprint is closing work (build, verify, page sheet, START-HERE
   and cross-references, hand-off), **finish the sprint**: that costs far less than a new session's
   start-up. If a whole file or a figure set is still unwritten, stop at a clean point instead. The
   hard limit (auto.py's kill, ~30k above the soft one) is the real wall: never start a file past
   the notice.
2a. **One sprint = one session.** Plan the context: two files fit if the start-up stays lean. View
   at most one contact sheet per file (4 pages per image), and only figures the overlap check or a
   new figure type flags.

**Research (only when the sprint's row says so, or a fact is missing from the KB)**
3. Every load-bearing claim (definition, formula, mechanism, constant) is verified (above) and
   written into the KB file at once, with source and confidence tag. Never batch.
4. Unverifiable this session → `uncertain` + Verify backlog row; never written as fact.
5. Sources → the KB's `sources.md`; one line in its `CHANGELOG.md`; ≥ 3 misconceptions added to
   `misconceptions.md` when a whole delta topic was researched.

**Build (content standard: spec §4–§6)**
6. Order inside a file follows the professor's deck for that topic. Real questions from the brief's
   question bank first (tagged), Predict prompts otherwise.
7. File opening: header (needs: file + step) → map → opening paragraph → symbol table → running
   example. First step opens on a concrete anchor.
8. Each step: bridge → question/Predict → guess → terms (what each counts, what sets it) → figure
   ("What this graph plots:" + a reading table for a quantitative curve) → teaching (formulas read
   back in words; numbered derivations, approximation named where it enters) → "Answer to the
   Predict" → Check. One idea per step; never merged.
9. Figures in the pack's figures module (one per unit or file), built on `tools/figlib.py`. Old
   figures are reused only if they meet the caption rule and pass the overlap check.
10. Every printed number (teaching, Checks, Self-test, answers) is recomputed in the pack's
    `verify_*.py` with the constants the pack prints; it passes, and every earlier script still passes.
11. Build the sprint's files (`python src/build.py <prefixes>`; the combined PDF stays complete).
    The build prints `OVERLAP` lines: fix each. Render the new pages at low resolution, 4 per image,
    one pass; zoom only on suspect figures.
12. Replace, don't duplicate: remove the old file's `content/`, `html/`, `pdf/` copies; update
    `00-START-HERE.md` (rank row, map, what-each-file table, slip table, how checked) and every
    cross-reference (`grep -rn "<old name>" src/content`); re-point the mock paper's rows.

**Close**
13. Check the sprint's **Done when** item by item; anything failing stays open (sprint `partial`).
14. Move open items to the **Verify backlog**, new assumptions to **Assumptions to review**;
    overwrite *Current hand-off*; tick the sprint; overwrite the progress log's *Where we stopped* /
    *Next up*. Commit + push (under `auto.py`: no git; it commits).

## Hand-off template (overwrite *Current hand-off* each sprint end)

```
Sprint: Sx — <name> — done | partial (date)
Written: <files, one line each, with what they now contain>
Verified this sprint: <key claims + source, or "numbers: verify_*.py, N checks pass">
Open (carried): <unverified claims, page fixes left, anything failing Done-when>
Decisions made: <scope/split/naming choices the next sprint must respect>
Assumptions to review: <new numbered items, also copied to the persistent section>
Next sprint: Sy — first action: <one concrete step>
Read at start: <exact file list = Sy Inputs>
```

## Tooling notes (all subjects)

- **Decks:** read `.pptx` text with `zipfile` + a regex on `ppt/slides/slideN.xml`; pictures in
  `ppt/media` (via `_rels`). Many equations exist only as images: view them. EDC's
  `research-tools/deck_extract.py` does this and can be called with any deck path.
- **PDF pages → PNG:** `pymupdf` (`import pymupdf`), or EDC's `research-tools/render_pages.py`.
- **Markup that bites:** `|` separates `[[fig:name|caption|w=NN]]` fields, so captions hold no `|`;
  `$$…$$` handles `\frac`, `\sqrt`, not `\left`/`\right`; box titles are uppercased by CSS (keep
  Greek out of titles); a line starting with "+" renders as a bullet.
- **Figures:** see `tools/figlib.py`'s docstring (mathtext fixes, labels outside drawings).
- **Windows:** run scripts that print non-ASCII with `PYTHONIOENCODING=utf8`. Git Bash heredocs
  mangle `\n` inside inline Python: write a `.py` file to the scratch folder and run it.
- **Under auto.py:** no `$VAR`, loops, or `cd … &&` with writes; long edits with the Edit tool;
  edits only inside the subject folder (changes to `tools/` or the spec go into the hand-off for an
  interactive session).
