# ECE2132 Data Structures & Algorithms Lab — progress log

> Written **live** (log-first artifact pairing). Pairs with ECE2104 (`../12-data-structures-and-algorithms`).

## Session resume
- Last session: 2026-11-01/02. Lab pack built: `study-pack/pdf/ECE2132-DSA-Lab-pack.pdf` (91 pp.) + all three lab packs
  merged into `../_lab-ete-pack/Sem3-Lab-ETE-pack.pdf` (222 pp.). Nothing taught live yet; no misses reported.
- Open: no Exp 9 file (chapter 8 = probable stack, to be confirmed by the learner).

## Where we stopped
- 2026-11-02: pack complete, verified (ALL PASS) and visually reviewed; merge done. Next: learner works through the pack
  (guess first, type programs from memory) and reports misses only; confirm what Exp 9 is.

## Mastery ledger
*(empty)*

## Spaced-review / relearning queue
*(empty)*

## Log
- `[2026-11-01]` Learner request (continuing the 2026-10-31 lab-prep request): DSA lab manuals uploaded ("all dsa lab
  manuals there are"); "only from those files do we need to actually be able to perform those experiments"; learner is at
  "almost complete zero of c++" and weak in C ("dont rely much on if i already know c"); "the codes actually have some
  errors in them, so make sure u correct them before u use them"; deliverable = one PDF that teaches everything needed
  for marks, then all three lab packs merged.
- `[2026-11-01]` `_inbox/` triage: 9 PDFs headed "Data Structures & Algorithms Lab, ECE2132" (Dr. D.V. Prashant,
  Dr. Kamal Kishore Upadhyay, AY 2026-27): Exp 1, 2, 3+4, 5+6, 7, 8, 10, 11, 12. **No Exp 9 file.** Exp 10's figure
  captions read "Enqueue/Dequeue Operation on Stack" (copied from a stack experiment) → Exp 9 is most likely Stack.
  ECE2132 had no folder (2025-26 scheme, absent from the 2023 seed; same precedent as 12-) → created
  `15-data-structures-and-algorithms-lab/`; manuals filed to `exam-pack/manual/`.
- `[2026-11-01]` Gate note: parent subject 12 is below `stage-1` (learner-logged MTE exception 2026-09-24). This pack runs
  under the defined-source exception: the manual is the scope source; truth = the compiler (g++ 16.2 with `-std=c++17
  -Wall -Wextra -pedantic-errors`, every program compiled and run on the manual's own sample inputs) + standard textbook
  results (handout textbook [1] Kanetkar, *Data Structures Through C++*, 2023) for complexities/definitions.
- `[2026-11-01]` Installed WinLibs MinGW g++ 16.2.0 via winget (`BrechtSanders.WinLibs.POSIX.UCRT`) — no compiler was on
  the machine; also usable by the learner for practice.
- `[2026-11-01]` Manual code read (listings are images; read visually, both the "PROGRAM" listing and the "IMPLEMENTATION"
  screenshot, which differ). Errors found: Exp 4 listing reads an unused `value` in all three branches (the manual's own
  sample input then blocks; the screenshot copy is correct); Exp 7 + 8 use `int arr[n]` (VLA, not standard C++, rejected
  by MSVC); Exp 8 aim/explanation promise bubble/selection/insertion/copyArray/`clock()` comparison but the code has only
  quick sort; Exp 10 screenshot does not compile (`enqueue(value);` after the if-block → dangling `else`, choice 3 prints
  "Program terminated", bare `else`); Exp 11 screenshot is garbled (traverse never advances → infinite loop; insert never
  links the node; corrupted menu text) while its listing is correct; Exp 12 listing does not compile (`insert(intvalue)`,
  menu `cout` strings unterminated, `delete temp;` outside the scope of `temp`) and its `main` is cut off (screenshot
  copy is complete); text slips: Exp 2 RESULT copied from Exp 1, Exp 4 algorithm says "insertion menu", Exp 5 algorithm
  step 7 is a stray deletion line + explanation table rows shifted by one, Exp 6 Fig 3 caption "A[i][j] to T[i][j]",
  Exp 8 heading "Characteristics of Insertion Sort" over quick-sort points, Exp 10 captions "on Stack".
- `[2026-11-01]` Corrected programs written: `study-pack/src/code/e01..e12` (+ `e08_sort_compare.cpp` = the missing
  bubble/selection/insertion + `clock()` comparison; `e09_stack.cpp` = probable Exp 9, written from the stack/queue
  pattern, flagged as not from the uploaded files). `src/verify.py`: strict compile of all + 28 runs on the manual's own
  sample inputs and edge cases (bad position, empty list, overflow/underflow, single-node circular delete) -> ALL PASS.
  The three manual copies (Exp 7 VLA, Exp 10 screenshot, Exp 12 listing) fail to compile as predicted; errors saved for
  the pack. Timing run (10 000 random ints): quick 1 ms, bubble 114 ms, selection 48 ms, insertion 33 ms. Queue edge
  test confirms the linear-queue flaw (Overflow after 2 dequeues with 2 free slots).
- `[2026-11-01]` Echo-transcript build (`src/echo.h`, force-included) so sample runs show typed input. Builds linked
  `-static`: a dynamic build failed with exit 127 (an older libstdc++-6.dll elsewhere on PATH).
- `[2026-11-01]` Next: manual ASSIGNMENT questions as tested functions (`src/code/variants/t_NN.cpp`), curated by the
  marathon rule (drop only items practically identical to the experiment itself).
- `[2026-11-01]` Assignment questions written as tested functions: `src/code/variants/t_03,04,05,07,08,10,11,12.cpp`
  (57 checks, all PASS) + full programs `e04b_array_menu.cpp` (menu insert+delete) and `e10b_circular_queue.cpp`
  (wrap-around, overflow only when truly full - tested). Curated out as identical to the experiment itself: Exp 4's
  first three items, Exp 5 "3x3 multiply" + "check if multipliable", Exp 6 "transpose"/"3x3 transpose", Exp 7/8 "separate
  functions", Exp 10 first item, Exp 11/12 "insert at end"/"delete from beginning". Hand-traced counts confirmed by the
  drivers: insertion sort on 5 2 4 6 1 3 = 12 comparisons / 9 shifts; quick sort (last pivot) on 10 7 8 9 1 5 = 11
  comparisons / 5 swaps; sorted input = n(n-1)/2 = 15 comparisons for both.
- `[2026-11-01]` Next: build.py + figures.py + content chapters -> `study-pack/pdf/ECE2132-DSA-Lab-pack.pdf`.
- `[2026-11-02]` Pipeline built: `src/build.py` (adapted from the DE pack; adds `[[code:]]`, `[[snip:]]`, `[[run:]]`,
  `[[err:]]` so the PDF quotes the tested files and real outputs; pygments 2.19.2 added to `requirements.txt`) and
  `src/figures.py` (16 hand-built SVG figures on the manual's own example data; rendered and visually checked, overlaps
  fixed). Primer programs `code/p01..p04` added to verify.py -> ALL PASS.
- `[2026-11-02]` Writing chapters `src/content/00..15`.
- `[2026-11-02]` Built `study-pack/pdf/ECE2132-DSA-Lab-pack.pdf`, 91 pp., 14 files: start-here (manual-errors table, Exp 9
  note), C++ from zero, Exp 1+2, 3, 4, 5+6, 7, 8 (+ comparison), 9 (probable stack), 10 (+ circular queue), 11, 12,
  exam day (expected outputs, complexity sheet, decisive lines, general viva), revision set (8 type-from-memory + 22
  short questions). Every chapter: map -> guess-first -> idea + figure -> corrected code -> real runs -> record block ->
  viva table -> tested assignment variants -> checks, answers at the end. All 91 pages visually reviewed; fixes made:
  menu reprints collapsed in transcripts, oversized page gaps (boxes may now split), record fields one per line, map
  separator clash in ch 11. Claim checked by compiling: an array named `queue` fails with `<bits/stdc++.h>` ("reference
  to 'queue' is ambiguous") and compiles with `<iostream>` alone.
- `[2026-11-02]` Next: merge ED (08) + DE (09) + DSA (15) packs into one PDF.
- `[2026-11-02]` Merged ED (83 pp.) + DE (47 pp.) + DSA (91 pp.) packs with a contents page and nested bookmarks: `../_lab-ete-pack/Sem3-Lab-ETE-pack.pdf`, 222 pp. (ED p.2, DE p.85, DSA p.132; script `../_lab-ete-pack/merge.py`). `.gitignore` now excludes `*.exe` (compiled test binaries, 122 MB). Research queue: ECE2132 row added.
- `[2026-11-02]` Learner request: "make me a 'to-write' file with only aim, a summary of theory, algorithm, program, flow
  chart and result for all experiments, a combined file". Read as the DSA lab (program + flowchart exist only there).
  Building `study-pack/src/record/` -> `study-pack/pdf/ECE2132-DSA-Lab-to-write.pdf`: one page-started section per
  experiment, programs = the verified files in `src/code/` (pack-internal "FIX" comments stripped), outputs = verify.py
  runs, flowcharts = Mermaid 10.9.1 (the project's pinned CDN version).
- `[2026-11-02]` Built `study-pack/pdf/ECE2132-DSA-Lab-to-write.pdf`, 54 pp., bookmarked per experiment: Exp 1-12 (9
  flagged probable), each = Aim, Theory (summary), Algorithm, Flowchart, Program (verified code, "FIX" comments
  stripped), Result + real output. 26 Mermaid flowcharts (menu programs split into a menu chart + one chart per
  operation); rendered with HTML labels after plain labels printed `&gt;` literally; 0 render errors; pages reviewed.
  Source: `study-pack/src/record/` (`to-write.md` + `build_record.py`).
- `[2026-11-02]` Learner: "rewrite theory, its too big, write atleast 50% less" (to-write file). Rewriting the 12 Theory sections of `study-pack/src/record/to-write.md` to <= 50% of their word count; keep definition + key rule + complexity.
- `[2026-11-02]` Theory sections rewritten: 1409 -> 570 words (40% of original; every experiment 29-48%). Rebuilt `ECE2132-DSA-Lab-to-write.pdf` (54 pp., 0 flowchart errors).
