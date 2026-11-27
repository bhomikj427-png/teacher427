# Task: build `<subject>-instrV2.md` (an exam chat file) for <SUBJECT>

Read every file in the subject's `exam-pack/`: assignments, notes/slides, hand-out, PYQs (past papers). Also read `chat-pack-template/reference-instcV2-CAP.md`, a finished file for another subject (CAP). **Copy its structure and teaching rules; do not copy its content.** Output one file, `subjects/<…>/<subject>/chat-pack/<subject>-instrV2.md`, which a separate chat session will use to tutor me (Bhomik) for the <SUBJECT> exam.

## Why the old files failed
They were good answer keys but bad teaching sequences: every question jumped straight to "Step 1" of the solution, with no picture of what's going on, no diagrams, and lists to memorise. I can't memorise lists (formulas are fine). If I don't understand something, I don't retain it. The flow that worked is in the reference file under **How to teach** and **Example flow**.

## File structure (in this order)

1. **Header**: subject, exam date (ask me if it isn't in the material), and "this file is the truth authority". Then **"Missing — ask Bhomik"**: everything needed but absent, with the assumption in force.
2. **How to teach Bhomik**: copy the 8 rules from the reference word for word, except rule 0 (the trunk), which you rewrite for this subject (see 3). Where a copied rule names CAP-only examples, keep the rule as it is and add one line of this subject's equivalents under it. Also copy the "Switching to a new session" rule.
3. **The trunk**: the one central idea of the subject that every topic hangs on, in 5 lines, plus a table mapping every syllabus topic onto it. Choose a lens that the material clearly supports. Previous trunks:
   - CAP: **WHICH** box / **WHAT** bits / **WHEN** (address/select, data, control/clock).
   - DSA: **WHERE** the data sits / **HOW** you move through it / **HOW MUCH** it costs.
4. **Example flow**: 2–3 example replies in the reference's skeleton (picture → [diagram description] → Write | Why → Try with its answer below). Use real PYQ questions. Keep the "Don't do this" line.
5. **Progress table**: all topics "not started"; "Next" = the top-ranked question.
6. **Paper pattern + what repeats**, from the PYQs: sections, marks, and which question types recur, with paper names. Note any evidence that the current professor reuses a paper (word-for-word overlap with assignments).
7. **§Q question bank**, ranked by (chance of appearing × marks), with columns: rank · question type · marks · seen in · **rote load (low/med/high)** · minutes. Mark high-rote, low-mark items "only if time is left".
8. **One entry per §Q row**, each with these parts in this order:
   - **Question**, copied exactly as a paper prints it (cite the paper).
   - **Picture**: 3–5 plain lines on what the thing physically is and what each part does. Define every term on first use.
   - **Diagram spec**: what the chat session must draw, one bracketed line per diagram. For algorithms/procedures, add a **state table** (one row per step).
   - **Exam answer** as a Write | Why table. Code goes in a code block with a one-line comment per line; then trace it on one small input in a state table.
   - **Try**: 1–2 variants with their answers shown right below.
9. Solved past papers and assignments: the answer key, cross-referenced to the §Q entries.

## Hard rules
- Every number, trace and output must be correct: **run every program** on the inputs you show and paste the real output; recompute every numeric/trace answer with a checker script kept beside the file (`chat-pack/verify_<subject>.py`).
- Third-party "solutions" are never the authority: re-derive them, and flag any that are wrong as a **Trap**.
- Derive, don't list: results come from counting or reasoning on the picture. Never present a bare table to memorise.
- Plain words; define every term on first use; no attention hooks; math typeset with $$ (never inside code blocks).
- If something needed is missing (exam date, syllabus unit, paper pattern), list it at the top under "Missing — ask Bhomik" instead of guessing.
- Temporary/extracted files (PDF page renders, text dumps) go in the project's `tmp/`, never the system Temp folder.
