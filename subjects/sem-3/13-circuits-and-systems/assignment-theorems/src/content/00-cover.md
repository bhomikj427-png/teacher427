# Circuit Theorems Assignment

<div class="sub">ECE2107 Circuits & Systems · assignment marathon · built so far: Part A Superposition (5.1–5.14), Thevenin &amp; Norton (5.15–5.34), maximum power (5.35–5.44); Part B Sadiku superposition (PP 4.3–4.5, 4.8–4.19), source transformation (PP 4.6–4.7, 4.20–4.32), Thevenin &amp; Norton (PP 4.8–4.12, 4.33–4.65), maximum power (PP 4.13, 4.66–4.75); AC superposition &amp; source transformation (PP 10.4–10.7, 10.40–10.54), AC Thevenin &amp; Norton (PP 10.8–10.10, 10.55–10.68)</div>

## How to use this

Every question follows the same order:

1. **Question**, with the figure taken straight from the book.
2. **Try it first** (yellow). Cover the rest of the question and solve it.
3. **Hint: what's new** (orange). Only when the question brings an idea you haven't met earlier in this PDF. If you're stuck, read it and try again.
4. **Solution** in compact assignment form: Given → To find → each step with its intermediate values → boxed answer. Copy it into your submission, or compare it line by line with your attempt to find the step that went wrong.
5. **Side note** (grey) or **book error** (red), only when there is something worth knowing.

The tag next to each question number shows how much teaching it carries:
<span class="lvl heavy">teach</span> full explanation · <span class="lvl light">new idea</span> one new thing · <span class="lvl plain">practice</span> plain solution.

If you couldn't solve one, just tell me its number. Nothing else needs marking.

## What's in it (full version)

| Part | Book | Questions | Count |
|---|---|---|---|
| A | Ghosh & A K Chakraborty, *Circuit Theory and Networks*, ch. 5 (**solved**) | Superposition 5.1–5.14 · Thevenin/Norton 5.15–5.34 · Max power 5.35–5.44 | 44 |
| B | Alexander & Sadiku, *Fundamentals of Electric Circuits* 5e (**unsolved**) | Practice problems + end-of-chapter: ch. 4 (superposition, source transformation, Thevenin/Norton, max power), ch. 10 (the same in AC), ch. 11.3 (AC max power) | 107 + practice problems |

Scope follows the official MUJ ECE2107 syllabus: superposition, Thevenin's and Norton's theorems, maximum power transfer, DC and AC, plus source transformation.

**Checking.** Every answer was worked out again and confirmed by a full circuit solve with all sources on (`src/verify.py`), including each case's partial answer. Matches with the book are marked "= book". Where the book is wrong, the correct answer is given and a red box explains the book's slip.

