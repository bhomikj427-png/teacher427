# PARKED DESIGN — Pictorial, publishable study packs

> ⚠ **PARKED. NOT IMPLEMENTED. NOT PART OF THE LIVE CONTRACT.** Queued 2026-09-24, the night
> before the ECE2103 Signals & Systems + economics exams. The learner chose to **queue and discuss
> now, build after exams**. Nothing here is active. Settle the open decisions (§5) with the learner
> before editing `CLAUDE.md`, `rendering.md`, or `tools/`.

---

## 0. What the learner asked for (their words, 2026-09-24)

- "its not working for me, its too text-ual, i need it to be pictorial"
- When asked *where* it felt too textual: **study packs / notes** (not the terminal dialogue, not
  the live checks).
- When asked where pictures should live: **"i wanna publish it, i alone wont be using this"**, so
  the output has **other readers** (see open decision D1: classmates vs. the engine itself).

## 1. Diagnosis: why the engine comes out textual (verified 2026-09-24)

1. **Study packs are `.md` files.** For example, `subjects/sem-3/12-data-structures-and-algorithms/study-pack/`
   is prose, ASCII-art maps (`──►` trees), and markdown tables. It contains no rendered figures.
2. **Figures are opt-in.** `learner-preferences.md` §3 (2026-06-21, 2026-07-08) says to render
   "only what genuinely needs rendering", so the default path is text. Across the whole project
   only **2** rendered HTML lessons exist, both in verilog `00-orientation`.
3. **The Studio canvas was demoted** to figures-only (2026-07-08, "not polished yet"). Nothing
   pushes content to it by default.
4. **The evidence base is written with a text bias.** `research/02 §9` (dual coding) is headed
   *"How to apply (text/terminal-friendly)"*.

The rendering stack exists (`tools/render_lesson.py`, `tools/make_figure.py`, six primitives), but
no rule makes the engine use it.

## 2. Evidence anchor: this is not "learning styles"

Words + **relevant** graphics beat words alone **for everyone** (Mayer multimedia, `research/02 §9`;
magnitudes likely inflated, so keep the principles, not the d-values). This change applies to all
readers. It is not a modality match to one person (`research/06` stays intact). Constraints from the
same section:
- **coherence**: no decorative images
- **contiguity**: labels sit on the figure, not in a paragraph below it
- **signaling**
- **segmenting**

## 3. Proposed design (draft, not signed off)

- **Figure-first rule.** Every concept section opens with a figure. The text becomes the caption
  and explanation of that figure, roughly ≤60 words per block, and every symbol in the text points
  at something drawn.
- **Fixed content→picture map.** This extends the primitive table (`rendering.md` §2).

  | Content | Picture |
  |---|---|
  | signal / function | matplotlib plot of the signal. Never a formula alone |
  | convolution, sampling, modulation | step strip: flip → shift → multiply → sum, one panel each |
  | algorithm / data-structure op | state-snapshot sequence (stack after each PUSH/POP) |
  | concept overview | Mermaid flow map + small sub-maps (existing §3 multi-map rule) |
  | comparison | visual grid (primitive 5) |
  | circuit / block diagram | schemdraw / SVG (primitive 6) |
- **Study packs become rendered HTML** via `save_lesson`, not `.md`. Keep the spec script as the
  reproducible source.
- **Pictorial retrieval.** Questions like "sketch y(t)" get answered with a photo, which the engine
  reads and marks. Terminal dialogue is unchanged (not requested).
- **Per-subject visual registry.** S&S (plots), DE (timing and K-maps), DSA (state snapshots), etc.,
  each map onto the primitives above.
- **Pilot candidate:** Signals & Systems. It is the most picture-native subject.

## 4. Publishing: options discussed (learner has not chosen yet)

**Hard constraint:** `exam-pack/` (professor slides, PYQs, hand-outs) is third-party copyrighted.
The repo **stays private**. A published pack may contain only **original** explanations and
figures. It must never include copied slide text, scanned PYQs, or the professor's files.

| Option | How | Pros | Cons |
|---|---|---|---|
| **A. Claude Artifacts** | each pack published as a hosted page; share the link | zero infrastructure, works on phones, private until shared | lives on the learner's claude.ai account |
| **B. Static site** (GitHub Pages / Netlify) | a **separate public repo** holding only the generated HTML; never the private repo | own URL, durable, free, indexable | needs a build/export step and a copyright filter |
| **C. PDF export** | print the HTML packs to PDF | spreads easily in WhatsApp class groups | static, no interactivity |
| **D. Publish the engine itself** | open-source the tutor with learner state and exam material stripped | others get the whole tutor | much bigger; personal state must be separated from the engine |

**Leaning (to discuss):** HTML is the single source. Publish via **A** now (fast), export to **C**
for group sharing, and move to **B** if readership grows. **D** is a separate, larger project.

**Design implication if others read it:** a published pack cannot rely on this learner's
profile or preferences. It has to stand alone. This means splitting the **public product** (the
packs) from the **private tutor** (the loop, retrieval, progress logs).

## 5. Open decisions (settle before building)

- **D1.** Who is "not just me": classmates reading the packs, or other people running the engine
  (option D)?
- **D2.** Hosting: A / B / C / D, or a combination.
- **D3.** Does the figure-first rule apply to the terminal too, or only to packs? The learner
  flagged only packs.
- **D4.** Should old packs (DSA, Digital Electronics) be retrofitted, or should only new packs be
  pictorial?
- **D5.** Is the figure-first rule an **engine rule** (`CLAUDE.md` + `rendering.md`, applies to
  every subject), or a **universal preference** (`learner-preferences.md`)? Since other readers are
  involved, it is likely an engine rule.
