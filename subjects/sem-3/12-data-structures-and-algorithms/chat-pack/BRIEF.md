# Task: build `instructions-chat.md` for DSA

Read every file in this project: assignments, notes/slides, PYQs (past papers). Also read `instcV2.md`, which is a finished file for another subject (CAP). **Copy its structure and teaching rules; do not copy its content.** Output one file, `instructions-chat.md`, which a separate chat session will use to tutor me (Bhomik) for the DSA exam.

## Why the old files failed
They were good answer keys but bad teaching sequences: every question jumped straight to "Step 1" of the solution, with no picture of what's going on, no diagrams, and lists to memorise. I can't memorise lists (formulas are fine). If I don't understand something, I don't retain it. The flow that worked is in `instcV2.md` under **How to teach** and **Example flow**.

## File structure (in this order)

1. **Header**: subject, exam date (ask me if it isn't in the material), and "this file is the truth authority".
2. **How to teach Bhomik**: copy the 8 rules from `instcV2.md` word for word, except rule 0 (the trunk), which you rewrite for DSA (see 3). Also copy the "Switching to a new session" rule.
3. **The trunk**: the one central idea of DSA that every topic hangs on, stated in 5 lines plus a table mapping every syllabus topic onto it. Default lens (check it against the material; change it only if the material clearly needs something else):
   - **WHERE** does the data sit? (layout: contiguous array, nodes + pointers, tree levels, hash buckets)
   - **HOW** do you move through it? (index jump, follow next, recurse left/right, BFS/DFS, swap/compare)
   - **HOW MUCH** does it cost? (Big-O time and space, as the count of the HOW steps)
4. **Example flow**: write 2–3 example replies for DSA in the same skeleton as `instcV2.md`'s Example flow (picture → [diagram description] → Write | Why → Try with its answer below). Use real PYQ questions. Keep the "Don't do this" line.
5. **Progress table**: all topics "not started"; "Next" = the top-ranked question.
6. **Paper pattern + what repeats**, from the PYQs: sections, marks, and which question types recur, with paper names.
7. **§Q question bank**, ranked by (chance of appearing × marks), with columns: rank · question type · marks · seen in · **rote load (low/med/high)** · minutes. Mark high-rote, low-mark items "only if time is left".
8. **One entry per §Q row**, each with these parts in this order:
   - **Question**, copied exactly as a paper prints it (cite the paper).
   - **Picture**: 3–5 plain lines on what the structure physically looks like and what each part does. Define every term on first use.
   - **Diagram spec**: what the chat session must draw, in one bracketed line per diagram, e.g. "[linked list 3→7→9; new node 5 inserted between 3 and 7; old arrow dashed, new arrows coral]". For algorithms, add a **state table** (one row per step: variables, array contents, pointer positions).
   - **Exam answer** as a Write | Why table. Code goes in a code block with a one-line comment per line; then trace the code on one small input in a state table.
   - **Try**: 1–2 variants with their answers shown right below.
9. Solved past papers and assignments: the answer key, as in the old files.

## Hard rules
- Every number, trace and output must be correct: **run every program** on the inputs you show and paste the real output.
- Derive, don't list: complexities come from counting steps on the picture (e.g. "each level halves the array → log n levels"). Never present a bare table to memorise.
- Plain words; define every term on first use; no attention hooks; math typeset with $$ (never inside code blocks).
- If something needed is missing (exam date, syllabus unit, paper pattern), list it at the top under "Missing — ask Bhomik" instead of guessing.
