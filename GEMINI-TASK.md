# Gemini task — DE S0a: transcribe the course material, build the question bank

> Written by Claude, 2026-11-17. Rules: `GEMINI.md`. Run in Antigravity (`agy`; Gemini CLI is retired
> for individual accounts). Model: a Gemini Pro model (not Flash; not a Claude model).

**Subject folder:** `subjects/sem-3/04-digital-electronics/` (all paths below are inside it).

**You may change only:** `study-pack-v12/src/brief.md` (create it) and append one line to
`progress-log.md`.

## Inputs
- `exam-pack/README.md` (what each file is)
- `exam-pack/slides-01-…pdf` through `slides-15-…pdf` (15 decks)
- `exam-pack/PYQ-MTE-2025-09-25.pdf` (mid-term paper)
- `exam-pack/practice-set-01-combinational.png`, `practice-set-02-flipflops-counters.png`
- `study-pack-v12/src/content/` file names only (`01-…md` to `20-…md`): the topic files questions map to
- Format model (structure only, never content): `../01-statistics-and-probability/study-pack-v12/src/brief.md`, sections 1–2

## Write `study-pack-v12/src/brief.md`

```
# ECE2102 Digital Electronics — subject brief (v1.3 build)
> S0a by Gemini (transcription, unverified), 2026-11-17. S0b (Claude) adds §3–§5.

## 1. Slides transcribed
### 1.N `<deck file name>` (<page count> pp.)
| Page | Content |
```
- **One row per page**, every deck, in deck order. Row = the page's title + its substance:
  definitions and formulas **exactly as printed**; truth tables, K-maps, state tables copied as
  markdown tables; circuit/timing diagrams described in one line ("p.12: 4-bit ripple counter, 4 JK FFs,
  Q0 clocks FF1…"); worked examples with their given numbers and the slide's answer.
- Mark each slide example `EX <deck>.<page>`. Skip only title/blank/"thank you" pages (say "title").
- Slide errors: keep as printed + `⚠ looks wrong: <why>`.

```
### 1.16 `PYQ-MTE-2025-09-25.pdf`
### 1.17 Practice sets 1 and 2
```
- Every question **verbatim** with its number, marks and any figure/table described fully enough to
  solve it from the text. Tag them `MTE Q1`…, `PS1 Q1`…, `PS2 Q1`….

```
## 2. Question bank → file and step
| File | Questions (tag → idea) |
```
- One row per topic file `01`–`19` (by its name in `content/`). Every MTE, practice-set and `EX` item
  appears **exactly once**, mapped to the file and the idea it tests (e.g. "MTE Q4 → 4-variable K-map
  with don't-cares"). Items that fit no file: list them under "Unmapped".
- End §2 with a count line: "MTE: n parts · PS1: n · PS2: n · slide examples: n · unmapped: n".

## Done when
- Every deck has every page row; every MTE and practice-set question is transcribed and mapped once.
- The count line adds up. Then write the Done report below (see `GEMINI.md` rule 7) and stop.

## Done report (Gemini appends here)
