# exam-pack/ — ECE2104 exam & course material

Material for **Data Structures and Algorithms [ECE2104]**. Routed here from `../../_inbox/` on
2026-09-24. Audit trail: `../../_inbox/TRIAGE-LOG.md`.

## What's here

| File | Slides | Covers | Beyond-class activity |
|---|---|---|---|
| `slides-01-cpp-overview.pptx` | 17 | C++ overview (header code "ECE/VDT 2104") | 3 starter programs (print, table of 5, conditionals) |
| `slides-02-cpp-basic-terms-operations.pptx` | 9 | why C++, C++ vs C abstractions (new/delete, iostream, references) | — |
| `slides-03-conditionals-loops-functions.pptx` | 16 | if/else, for/while/do-while, functions | 6 programs: call by value/reference, overloading `area()`, prime check, grade calculator |
| `slides-04-class-objects-access-specifiers.pptx` | 18 | classes, objects, public/private/protected | 5 programs: Student, Rectangle, Car, access specifiers, protected + single inheritance |
| `slides-05-class-constructor-destructor.pptx` | 16 | constructors, destructors | 10 short-answer questions (class vs object, data hiding, encapsulation…) |
| `slides-06-arrays.pptx` | 13 | linear arrays: memory representation, traversal O(N), insert/delete shifting | — |
| `slides-07-stack.pptx` | 18 | stack ADT, LIFO, PUSH/POP algorithms (overflow/underflow), infix/prefix/postfix | — |
| `slides-08-queue-pointers.pptx` | 27 | queue, FIFO, circular queue, pointers (`&`, `*`) | 6 items incl. array queue + circular queue programs |
| `ASSIGNMENT-A1-ECE2104-2026-08.pdf` | 50 marks | **Assignment 1** (CWS), due 27-08-2026. 23 Q: A 9×1 / B 5×2 / C 5×3 / D 4×4. Arrays, loops, classes/constructors, access specifiers, stack (array, trace, infix→postfix, postfix eval), queue, **singly linked list**, call by value/reference | first professor-set questions |
| `slides-08-queue-pointers-COPY.pptx` | 27 | **duplicate of deck 8**, identical slide text | kept, not deleted. Safe to remove |

Most slides are image-heavy. Only the text layer was read at triage (`unzip`), so figures and code
screenshots are not yet captured.

## What's missing (worth chasing)
1. **The course hand-out.** It gives the syllabus, the prescribed textbook, the MTE/ETE split and the
   lecture plan. ECE2108's hand-out was the most useful single document in the batch.
2. **Any MTE paper** for ECE2104 (Assignment 1 is here; the MTE window was ~mid/late Sept 2026).
3. **The linked-list deck.** Assignment 1 asks linked-list questions but no deck covers them. Also any
   later decks (trees, graphs, sorting/searching) if the course goes that far.

## Honesty rule (`../../research-engine/exam-resources.md`)
These decks set **scope and emphasis**, not facts. Deck 6 already shows why. Its line that no other
application can borrow memory from inside an array block, "guaranteeing absolute locality of
reference", is imprecise framing. Every deck credits an "AI Tool for making slides attractive".
Verify everything against the textbook.
