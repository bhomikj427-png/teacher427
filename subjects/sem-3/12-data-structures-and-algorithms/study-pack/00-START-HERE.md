# Data Structures & Algorithms ECE2104 — MTE Study Pack

**Built 2026-09-24, ~2 hours before the mid-term.** Every section opens with a real question from
**Assignment 1** (A1, 50 marks) or a deck's "Activity beyond classroom" list. You try it first, then the
section teaches the concept, then you get an **exam answer** you can reproduce.

> **What this pack is and is not.** You asked me not to research the subject, so it is built from the
> 8 decks, Assignment 1 and the course hand-out. The **content** is standard textbook DSA (Kanetkar,
> the prescribed book, and every other DSA text agree on it). **Every C++ program in this pack was
> compiled and run** before it went in, and the outputs shown are real.

---

## ⚠ MTE blueprint (received 2026-09-24, this overrides the guesses below)

| Section | Q | CO | Marks | Kind | Study |
|---|---|---|---|---|---|
| A | Q1, Q2 | CO1 | 2 + 2 | theory | 01 |
| A | Q3 | CO2 | 2 | theory | 02–05 |
| A | Q4 | CO3 | 2 | theory | 06 §2–4, §6 |
| B | Q1 | CO2 | 4 | **coding** | 04 §3 · 05 §2 · 03 §6 · 02 §4 |
| B | Q2, Q3 | CO2 | 4 + 4 | theory | 03, 04, 05 |
| B | Q4 | CO3 | 3 | theory (BST) | 06 §6 |
| C | — | CO1 | 2 + **5 coding** | theory + class program | 01 §6–9 |

**CO1 = 11 · CO2 = 14 · CO3 = 5 (trees only up to BST, so AVL/Red-Black are out).** Only 2 coding
questions. Everything else is theory.

## What's on the MTE

| Source | Says |
|---|---|
| Hand-out lecture plan | **MID SEMESTER EXAMINATION** printed after **L16 (Recursion)** |
| Your professor (per you) | "till red-black tree" → you read it as **types of trees** |
| Marks | MTE **30** · CWS 30 (quiz, MOOC, assignment) · ETE 40 |

So the MTE is: **C++/OOP basics → arrays → linked list → stack → queue → recursion**, plus **tree
terminology and types** as a safety margin (file 06).

The ECE2108 MTE (same department, same week) was **A: 3 short (2/2/3) · B: 3 × 5 · C: 1 × 8**, and
5 of its 7 questions came straight from the assignments. **Expect the same here: Assignment 1 is the
best predictor you have.**

---

## The path (and the 2-hour plan)

```
 [01] C++ & OOP ─────────────── class/object, constructor, access specifiers,
  │    ~20 min                   call by value/ref, OOP features, the octal trap
  ▼
 [02] Arrays ────────────────── memory, address formula, traverse/insert/delete
  │    ~10 min
  ▼
 [03] Linked list ───────────── node, insert begin/end, delete, search, sort
  │    ~20 min                   ◄ in A1 three times, no deck covers it
  ▼
 [04] Stack ─────────────────── PUSH/POP, trace, infix→postfix, postfix eval
  │    ~25 min                   ◄ HIGHEST YIELD: 5 of A1's 23 questions
  ▼
 [05] Queue ─────────────────── FIFO, linear vs circular, which DS for which job
  │    ~15 min
  ▼
 [06] Recursion & trees ─────── base case, call stack; tree words + types
  │    ~15 min
  ▼
 [07] Mock paper ────────────── 30 marks, timed, answers at the bottom
       ~15 min (or skip, and do only its Section A)
```

**If you only have 1 hour:** 04 → 03 → 01 → the Section C/D answers in 05. Stack + linked list +
class programs are the bulk of A1's marks.

---

## Every Assignment 1 question → where it is answered

| A1 | Question (short) | Marks | File |
|---|---|---|---|
| A1 | Array traversal vs insertion vs deletion | 1 | 02 |
| A2 | for / while / do-while | 1 | 01 |
| A3 | Class and object | 1 | 01 |
| A4 | Constructor vs destructor | 1 | 01 |
| A5 | public / private / protected | 1 | 01 |
| A6 | FIFO; ENQUEUE vs DEQUEUE | 1 | 05 |
| A7 | Output of `zip = 021377` | 1 | 01 |
| A8 | What is a data structure | 1 | 02 |
| A9 | OOP vs structured; features of OOP | 1 | 01 |
| B1 | Singly linked list: insert begin/end, delete, search, traverse | 2 | 03 |
| B2 | Swap: call by value vs by reference | 2 | 01 |
| B3 | Infix → postfix `((A+B)/C)(D-E)` with stack | 2 | 04 |
| B4 | Array insert/delete at a position | 2 | 02 |
| B5 | Array stack: PUSH, POP, PEEK, DISPLAY | 2 | 04 |
| C1 | Stack trace, find overflow/underflow | 3 | 04 |
| C2 | Array vs stack vs queue vs linked list; pick for back button / printer / records | 3 | 05 |
| C3 | Student class with parameterized constructor + grade | 3 | 01 |
| C4 | Evaluate `12 3 4 * + 6 2 / -` with a stack | 3 | 04 |
| C5 | Linked list insertion program | 3 | 03 |
| D1 | Triangle area: default ctor + parameterized ctor + overloading | 4 | 01 |
| D2 | Sort a linked list by swapping data | 4 | 03 |
| D3 | Infix → postfix program | 4 | 04 |
| D4 | Queue using an array | 4 | 05 |

---

## How to use each file

When you hit a **Q ▸**, write a one-line guess on paper **before** reading on. Even a wrong guess
makes the answer stick better than reading it cold. With 2 hours left that sounds slow, but it
isn't: it's the difference between recognising an answer and being able to write one.

Every file ends with a **Self-test** (answers at the very bottom). Anything you miss there is what
you re-read in the last 10 minutes before the exam.

**Writing programs in the exam:** examiners mark (1) correct logic, (2) the boundary checks
(overflow/underflow/empty list), (3) a `main()` that demonstrates it. Missing the boundary check is
the most common place to lose marks.
