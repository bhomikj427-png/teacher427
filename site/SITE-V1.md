# Study site — v1 spec (frozen 2026-09-28)

> **This is the approved format.** The learner signed it off on 2026-09-28 ("i like this … i want this
> format to be the site-v1"). Git tag: `site-v1`. Every new subject and chapter follows this spec.
> A change to the *format* (not the content) is a v2 proposal: discuss it with the learner, get
> sign-off, then update this file. Do not drift from it silently.
>
> This file describes the **format only**. What is built, drawn or deployed lives in the subjects'
> `progress-log.md` files and in `site/public/` after a build. It is never recorded here.

---

## 1. What the site is for

- A personal, pictorial study website. Every subject is **one page, one tree** of everything
  there is to study in that material.
- It reads as a **map first**, then **one concept at a time**.
- **Guiding principle, in the learner's words:** "clean yet something that's efficient in the sense of
  conveying information yet not overwhelming, that sweet balance". **The balance is the key.** When
  in doubt, show less on screen and let the structure carry the meaning.
- **Hosting:** GitHub Pages, free, from a **separate public repo** that holds only the generated
  pages (`site/deploy.sh`). The engine repo stays private.

## 2. The tree (the core of v1)

**Hierarchy:** `subject → stage → chapter → group → concept`.

| Level | What it is | How it looks |
|---|---|---|
| Subject (root) | the course | bold title + one muted line (code · exam · marks · minutes) |
| Stage | a phase of the course; carries the **colour** | small uppercase label in the stage hue |
| Chapter | a study-pack chapter | `n  Title  ▂▄▆  count`: number in the stage hue, 3 exam-weight bars, concept count; "· soon" if not drawn |
| Group | an organising label inside a chapter (not clickable) | small muted semibold text |
| Concept | one unit of content, which opens a card | plain text; ★ gold = exam question, ! red = trap; ✓ after it once seen; grey = not drawn yet |

**Relations are encoded in the shape, not in extra ink:**
- **Fan** (curved lines from a group to each item): the items are **independent** and can be
  done in any order.
- **Spine** (a vertical line with a dot per item, `seq: true`): **each item builds on the one
  above it.** This is how "build on the concepts" is shown.
- **List:** a set of plain leaves with no internal structure (for example the drill set) sits
  directly under its chapter as a list.
- **Cross-links ("needs"):** a concept can depend on something outside its own group. These
  links are **not drawn** (too busy). They surface on **hover** (the prerequisites light up) and in
  the card as **"Builds on"** links.
- **Structure first, not a flat list.** Chapters are grouped into sequences and fans so the
  learner sees *how* ideas build. A flat bag of leaves is allowed only when the items really are
  unrelated.

## 3. Behaviour

- **Landing:** only the root, the 4 stages and the chapters, all **folded**. The whole course is
  readable at a glance with nothing open.
- **Open a chapter** (click): its branch **grows out in place** (animated). Only **one chapter
  is open at a time**. Other chapters **dim**, and the open branch's lines take the stage hue. The
  view scrolls smoothly to the open branch. Clicking the open chapter again folds it.
- **Hover or focus a concept:** its prerequisites (the previous item in a spine, plus its `needs`)
  highlight, and the line path to it brightens.
- **Open a concept** (click): a **card** grows from the node over a light blur. The card holds
  **exactly one concept.**
  - Header: path (`1 Boolean + K-map / Variations`, where the chapter is a link), title, one-line
    gist, and **Builds on** chips (clickable).
  - Body: the concept content (figures first, see §5).
  - Footer: `← previous title`, `n of N` within the chapter, `next title →`. The order follows the
    tree and continues across chapters.
- **Leaving:** Esc, ✕, the scrim or the browser Back button steps out one level (card → chapter
  → overview). ← / → walk concepts while a card is open.
- **URLs:** `''` overview · `#/ch/<chapter-id>` chapter open · `#/c/<chapter-id>/<concept-id>`
  card open. They can be bookmarked and Back works.
- **Not drawn yet:** outline concepts are grey and not clickable (tooltip "Not drawn yet"). The
  footer key shows "n of N drawn".
- **Seen:** opening a card marks the concept ✓. This is stored in `localStorage` for this viewer
  only. It is a navigation aid, **not** a mastery record (mastery lives in progress logs, gated
  by retrieval).
- **Phones (< 760px):** the same tree becomes an **indented outline** with elbow lines and
  spine dots. The card goes near full-screen.
- **Dark and light:** follows the OS; ◐ toggles and the choice is remembered.

## 4. Visual language (minimal: what it is and what it is not)

- **Is:** text-first; hairline 1.2px lines; generous whitespace; Inter + JetBrains Mono; colour
  only where it carries meaning:
  - the stage hue (blue = foundations, green = building blocks, violet = memory, amber = exam
    drill), used as a quiet accent on the open branch;
  - gold ★ for exam questions;
  - red ! for traps.
- **Is not** (rejected in v0.2, the "tacky" build): dotted canvas backgrounds, big coloured
  circles or hubs, kind badges on every node, pulsing rings, gradients, radial wheels,
  pan/zoom camera gymnastics, a sidebar, long scrolling pages.
- **Footer key:** one quiet line: ★ exam question · ! trap · spine = builds on the one above ·
  grey = not drawn yet · n of N drawn. (★ is left out on a page that has no exam questions.)
- **Top bar:** ◧ (all subjects) · subject title · exam line (muted) · ◐.

## 5. Card content rules (inherited from the pictorial pack rules)

- **Figure first.** A concept opens with its picture, and the text is its caption and explanation
  (roughly 60 words or fewer per block). Pictures must carry the structure, not decorate
  (coherence; `research/02 §9`).
- **Retrieval stays in the format.**
  - Chapters start with a **warm-up** (attempt first).
  - Concepts end with a **quick check** behind `:::reveal`.
  - Worked exam questions say "try it first" before step-through figures (`steps=`).
  - Answers are always hidden until clicked.
  - The site supports study; it does not replace the tutor's retrieval checks.
- **Correctness is machine-checked.** Every drawn answer is verified by the pack's `verify.py`
  (K-map groups, minimized forms). **Textbook sets truth**; professor material sets scope and
  framing (`subject-research-protocol.md` §2).
- **Symbols:** real Unicode (Σm, ΠM, ⊕, ≥, subscripts), never TeX or spelled-out names
  (`learner-preferences.md` §3).

## 6. Authoring: how a subject or chapter joins

Each subject has `subjects/<…>/study-pack/web/`:

```
meta.json      slug, code, title, blurb, exam {name, marks, minutes, sections}
               (or, for a subject with no exam, `line`: the muted top-bar text instead),
               stages [{id, title, hue: blue|green|violet|amber}],
               chapters [{id, n, title, stage, weight 0-3, tree, needs?}]
figures.py     functions returning SVG strings; ALL = {name: fn}. Generated, never hand-drawn.
verify.py      machine checks for every answer and drawn group in the figures
content/NN-<chapter-id>.md   one file per DRAWN chapter
```

- **`tree`** (per chapter) is a list whose items are:
  - `"concept-id"`: a written concept (must exist in the chapter's content file);
  - `["Title", "kind"]`: an outline concept, not drawn yet;
  - `{"group": "Title", "seq": true|false, "items": [...]}`: a group; `seq` = spine (each builds
    on the one above), otherwise a fan.
- **`needs`** (per chapter, optional): `{"concept-id": ["prereq-id", …]}`, the cross-links shown on
  hover and as "Builds on".
- **kinds:** `idea`, `method`, `exam` (★), `trap` (!), `practice`.
- **Content file:** concepts are split by header lines `@@ id | Title | kind | one-line gist`,
  followed by Markdown plus:
  - `[[fig:name|caption|w=60|steps=3]]`
  - `:::q / :::trap / :::check / :::note / :::key … :::`
  - `:::reveal Title … :::`
  - `$$ one-line equation $$`
- **Build guards** (`site/build.py` refuses to build if any fails): every written concept must sit
  in the tree **exactly once**, and every id in the tree must exist in the content file.
- **Workflow for a new chapter:**
  1. Log it first in the subject's progress log.
  2. Write `content/NN-*.md`, figure-first.
  3. Add figures to `figures.py`.
  4. Add checks to `verify.py` and run it.
  5. Swap the chapter's outline items for concept ids in `meta.json`.
  6. Run `python site/build.py` and check it by screenshot at desktop and 390px.
  7. Commit.

## 7. Code map

| File | Role |
|---|---|
| `site/build.py` | discovers every `study-pack/web/`, renders concept Markdown to `<template>`s, emits one page per subject + home |
| `site/static/tree.js` | model, tidy-tree layout (wide) / outline layout (narrow), wires, fans and spines, routing, card, hover prerequisites |
| `site/static/tree.css` | the minimal visual language (§4) |
| `site/static/style.css` | shared tokens (light/dark), figure/box/table styles used inside cards, home page |
| `site/static/app.js` | theme toggle + figure steppers (delegated, works inside cards) |
| `site/deploy.sh` | force-pushes `site/public/` to the public Pages repo |
| `site/public/` | build output, gitignored |

Layout facts worth keeping:
- Wide layout: leaves are stacked, each parent is centred on its children, and column x comes from
  the widest visible node per depth.
- Folded nodes collapse onto their ancestor (so opening animates out from the chapter).
- Layout re-runs after web fonts load.
- Gotcha fixed in v1: the global `main { max-width: 860px }` in `style.css` clipped the tree.
  `#stage` overrides it.

## 8. How v1 was reached (so the reasons aren't lost)

| Version | Date | What it was | Learner verdict |
|---|---|---|---|
| v0.1 | 2026-09-27 | long scrolling chapter pages, sidebar table of contents, figure-first | "too much info dump"; hates the sidebar; wants a map landing and one concept at a time |
| v0.2 | 2026-09-27 | zoomable radial map (chapter islands, coloured hubs, badges, pulse, pan/zoom camera) | "not tree like enough", "tacky"; leaf sets should be lists; show how concepts build; minimal; **balance is the key** |
| **v1** | 2026-09-27/28 | minimal tree (this spec) | "i like this … this format to be the site-v1" |

## 9. Open items (not part of v1; each needs its own discussion)

- **Deploy:** the public repo is not created yet. Run `bash site/deploy.sh <url>` once it exists.
- **Content:** Digital Electronics chapters 2–9 are outlined but not drawn. Chapter 7 (waveforms)
  is the next best candidate. Other subjects join by adding `study-pack/web/`.
- **Home page** is still the plain v0 card list and could be restyled to the v1 language.
- **Possible later:** cross-subject links (see `_PARKED-cross-subject-linking.md`).
