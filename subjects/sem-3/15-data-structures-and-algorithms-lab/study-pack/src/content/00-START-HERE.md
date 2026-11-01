# ECE2132 Data Structures & Algorithms Lab — Start here

<div class="sub">Built from the 9 manual files you uploaded (Exp 1–8, 10–12; AY 2026-27). Every program in this pack was compiled with g++ in strict mode and run on the manual's own sample inputs. The output boxes are copied from those real runs.</div>

[[map:C++ from zero > Pointers (1–2) > Arrays (3–4) > Matrices (5–6) > Sorting (7–8) > Stack (9) > Queue (10) > Linked lists (11–12) > Exam day|here=1]]

## What the lab exam asks of you

You will be given one experiment (possibly with a small change, like the manual's ASSIGNMENT lines). To score, you need four things:

1. **Write the record part**: aim, short algorithm, time/space complexity, result.
2. **Type the program** from memory, compile it, and fix your own typos from the compiler's messages.
3. **Run it** on a sample input and show the right output.
4. **Answer viva questions**: why this line, what happens if…, what is the complexity.

Each experiment chapter gives you those four, in that order.

## How to use each chapter

:::key The one rule
**Guess before you read.** Each chapter opens with a question box. Answer it in your head or on paper *before* reading on, even if you're unsure. A wrong guess still helps: the right answer sticks better after you've tried. Then type the program yourself, without looking. Re-reading feels like studying but doesn't make you able to type it from scratch.
:::

- **Code boxes** (light grey) contain the corrected program. Type it yourself; don't copy-paste.
- **Screen boxes** (black) show what the program printed in a real run, with the typed input included.
- **Red boxes** show real compiler errors from the manual's broken versions, so you learn to read them.
- **Check** questions close each chapter. Answers are at the end of that chapter.
- **"If the examiner changes the question"** sections hold the manual's ASSIGNMENT variants. Each one is tested.

## Manual errors found (and fixed in this pack)

The manual's listings are images, and many experiments print the code twice (a PROGRAM listing and an IMPLEMENTATION screenshot) that **don't match**. Everything below was checked by compiling and running it.

| Exp | Problem in the manual | Effect | Fix in this pack |
|---|---|---|---|
| 2 | RESULT paragraph copied from Exp 1 | Wrong result statement | Own result written |
| 3 | No check on position or free space | Position 0 or 50 corrupts memory | Position 1…n+1 checked |
| 4 | Every option asks "Enter value:" and reads a number it never uses (listing only; the screenshot is right) | With the manual's own sample input, the program waits forever for a value | Prompt removed; deleted element printed |
| 4 | Algorithm step 5 says "insertion menu" | Text slip | — |
| 5 | Algorithm step 7 is a stray deletion line; explanation table rows are shifted by one | Text slips | Correct table in chapter |
| 6 | Fig. 3 caption "A[i][j] to T[i][j]" | Should be T[j][i] | — |
| 7, 8 | `int arr[n];` with `n` read at run time | Not standard C++. Visual Studio refuses it; g++ only allows it as an extension | `int arr[100];` + range check |
| 8 | Aim and explanation promise Bubble, Selection, Insertion, `copyArray()` and `clock()` timing, but the code has only Quick Sort | Half the experiment is missing | Full comparison program added |
| 8 | Heading "Characteristics of Insertion Sort" over quick sort points | Text slip | — |
| 10 | Figure captions say "…Operation on **Stack**" | Copied from a stack experiment | — |
| 10 | Screenshot copy: `enqueue(value);` outside its `if`, choice 3 prints "Program terminated", bare `else` | Doesn't compile | Listing version used, braces fixed |
| 10 | Array named `queue` | Clashes with `std::queue` if `<bits/stdc++.h>` is included | Renamed `queueArr` |
| 11 | Screenshot copy: traverse never moves `temp` (infinite loop), insert never links the node, menu text corrupted | Broken | Listing version used (it is correct) |
| 12 | Listing: `insert(intvalue)`, menu strings without closing quotes, `delete temp;` outside the block where `temp` exists, `main` cut off | Doesn't compile | Fixed and completed |

:::note Experiment 9 is missing
No "Exp 9" file was uploaded. Exp 10's figure captions read "Enqueue Operation on Stack", so Exp 9 is almost certainly **Stack using arrays**. Chapter 8 of this pack covers it, written in the same style as the Queue experiment. It is **not** from your manual; check with a classmate whether Exp 9 really is Stack.
:::

## The compiler on your laptop

To practise at home you need a C++ compiler. One is now installed on this laptop: **g++ 16.2 (WinLibs MinGW)**. Chapter 1 shows how to use it. In the lab you'll use whichever editor is there (VS Code, Code::Blocks or Dev-C++). The programs in this pack run the same on all three.
