# Exam-aiming resources — PYQs & PPTs for Stage 1 (how to use them, and the honesty rule)

> Stage 1's goal is **marks on the MUJ exam**, not just textbook coverage. The fastest lever for
> that is the *actual exam evidence*: **previous year question papers (PYQs)** and the **course
> PPTs/notes** the instructor taught from. This file is the registry of where they live and — more
> importantly — the **rule for how to use them without lowering the bar.**

## The exam structure (verified: portals; weightage `uncertain`)

- MUJ B.Tech assessment runs on two written exams: **MTE** (Mid-Term Exam) and **ETE** (End-Term
  Exam), plus internal/continuous assessment. Confirmed across the student portals below.
- **`uncertain` / to-verify:** the exact **mark weightage** (MTE vs ETE vs internals) — could not be
  verified from an authoritative source this session (searches returned the MET *entrance* exam, not
  the internal scheme). **Do not invent the split.** Resolve from the official MUJ academic
  regulations / a course handout, then record it here.

## The student portals (community-run — free, Drive-backed)

| Portal | URL | Holds | Access notes |
|--------|-----|-------|--------------|
| MUJ Central / Exam 101 | `mujcentral.in/exam101` → `/pyq` | MTE & ETE PYQs, PPTs, books | Free, Google-Drive links. Catalog seen 2026-06-17 exposed 1st-yr + 2nd-yr CSE-family; **Sem-3 ECE not yet listed there** — re-check. |
| MUJ Stella | `mujstella.in` (was `mujstella.vercel.app`) | Notes, PYQs, campus tools | Free. **Do not try to scrape (probed 2026-06-17):** hash-routed Firebase SPA (`mujstella-prod`); file links are Google-Drive URLs in a **Firestore DB read by the app's SDK**; the Firestore REST API is **disabled (403)**, so links can't be pulled without a real browser. Browse manually; download files or copy the Drive links. |
| MUJ Toppers | `mujtoppers.in` | Toppers' notes, PYQs | Free. Returned HTTP 403 to automated fetch; browse manually. |
| Notes Ninja | `notesninja.in` | MUJ notes, PYQs | May be partly paid. |
| Ycotes | `theycotes.com` | B.Tech notes, PYQs | Free, mostly 1st-year. |
| Studocu | `studocu.com` (MUJ ECE) | Shared notes, syllabus | Often login/paywalled. |

Verified existence 2026-06-17. None gave the engine a clean machine path to the **ECE Sem-3** files
yet — they're best harvested by a human in a browser (see "Manual drop," below).

## ⚠ The honesty rule — split the two purposes (this is the whole point)

A PYQ or a topper's PPT is **two different kinds of evidence**, and they sit at *opposite* ends of
the source hierarchy depending on what you're asking it:

- **For "what is *tested*, in what *form*, with what *emphasis*" → these are TIER-1 (primary).** An
  actual past paper *is* the authoritative artifact for what the exam asks; the actual course PPT
  *is* primary evidence for what the instructor emphasised, the notation used, and where the scope
  was cut. Use them directly and confidently *for exam-targeting.*
- **For "what is *true*" → these are TIER-3/4 (low-trust).** Toppers' notes, hand-written solutions,
  and PPT bullet points contain **errors**, oversimplifications, and copied folklore. They are
  **never** the truth source. **All content correctness still comes from the prescribed textbooks**
  (`course-info.md`) under the full `../../../subject-research-protocol.md` bar.

**So: let PYQs/PPTs decide *what to cover and how it's asked; let the textbooks decide *what's
correct.* Never let a PYQ answer-key or a topper's note set a fact** — verify the fact against the
prescribed text, then attach it to the exam pattern the PYQ revealed. A wrong answer key taught
confidently is exactly the failure the protocol forbids.

## Manual drop (the reliable path while portals aren't machine-readable)

Because the engine can't reliably scrape these sites, the highest-yield workflow is:
1. **You** (in a browser) download the Sem-3 ECE PYQs (MTE + ETE) and PPTs from the portals above.
2. **Drop everything into the central `../_inbox/`** — one folder, any subject, unsorted, any
   filename. You don't have to know which subject a file is; the engine **triages** it and files it
   into the right `NN-subject/exam-pack/` (see `../_inbox/README.md`). *(Already know the subject?
   You can drop straight into `NN-subject/exam-pack/` instead — both work.)*
3. The engine ingests each subject's `exam-pack/` when it builds that subject's Stage 1.

**File formats that actually work (this machine, probed 2026-06-17):**
- ✅ **Text-layer PDF** (typed/official papers, PPT exported to PDF) — read via `pdftotext`. Best.
- ✅ **.pptx** — text extracted via `unzip` of the slide XML (diagrams/images won't come through).
- ✅ **Images — PNG/JPG/screenshots/phone photos** — read visually by the Read tool, **handwriting
  included.** This is the route for handwritten/scanned material.
- ❌ **Scanned/photographed paper saved as a *PDF*** — *not* readable here: no OCR (`tesseract`) and
  no PDF→image (`pdftoppm`) installed. Give scans as **images**, not as a scanned PDF.
- Fallback: paste the text directly. If the toolchain changes (poppler/tesseract installed later),
  scanned PDFs become readable too.

If instead you paste Drive/portal links into the subject's `course-info.md`, the engine will *try*
to fetch them, but treat manual drop as the dependable route.
