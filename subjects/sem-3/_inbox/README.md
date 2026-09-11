# _inbox/ — drop ALL Sem-3 material here (one place, any subject, unsorted)

This is the **single dump folder** for every bit of Sem-3 material you get your hands on — PYQs,
PPTs, notes, question banks, photos of papers — for **any subject, in any order, with any
filename.** You don't have to know which subject a file belongs to or sort it yourself. Just drop it
here. The engine **triages** each file, figures out which subject it belongs to, and files it into
that subject's `exam-pack/` — then builds the exam-maps from it.

## How to use it (your side — dead simple)
1. Got a file? Drop it in `sem-3/_inbox/`. Mixed subjects, weird names, whole folders — all fine.
2. Tell the tutor **"sort the inbox"** (or it runs automatically on the next research pass).
3. Done. Check `TRIAGE-LOG.md` to see where everything went.

## What the engine does (the triage routine)
For each file in `_inbox/` (recursively):
1. **Identify the subject** — read the file (course name/code, header, content via `pdftotext` /
   image view) and match it to one of the 10 Sem-3 subjects (`../README.md` table; codes in each
   `course-info.md`).
2. **Route it** — **move** the file into that subject's **`exam-pack/`**, renamed clearly if needed
   (e.g. `ETE-2023.pdf`, `unit3-ppt.pdf`).
3. **Log it** — append one line to `TRIAGE-LOG.md`: file → subject → type (PYQ/PPT/notes) → date.
   (Moving + logging = nothing is lost; the inbox empties as things are processed, like the rest of
   the system's live, resumable logging.)
4. **Can't classify confidently?** Move it to `_inbox/_unsorted/` and add a line to `TRIAGE-LOG.md`
   asking you to confirm the subject — **never guess-file it into the wrong subject.**
5. **One file spanning several subjects** (e.g. a combined question bank): keep the original in
   `_unsorted/`, note it, and copy/reference the relevant parts into each subject's `exam-pack/`.
6. After routing, **rebuild the affected subjects' `knowledge-base/exam-map.md`** from the new
   evidence (`../research-engine/exam-resources.md`).
7. **If a routed file covers a unit that was already taught**, the teaching engine runs the
   **delta diagnosis** before any re-teaching — re-scope, don't replay: teach only genuine gaps or
   exam-framing reframes, fold the rest into spaced revision (`../../../subject-research-protocol.md`
   §2, "Late-arriving material RE-SCOPES"). New material never triggers a re-lecture of mastered
   items.

## The honesty rule still applies (`../research-engine/exam-resources.md`)
A PYQ/PPT tells us **what is tested and how** (trust it for that) — it does **not** set facts
(answer keys & notes have errors; content is verified against the prescribed textbooks). Triage only
*routes and reads*; it never promotes a file's claims to truth.

## File formats that work here (this machine, probed 2026-06-17)
- ✅ **Text-layer PDF** (typed/official papers, PPT→PDF) — read via `pdftotext`.
- ✅ **.pptx** — text extracted via `unzip` (diagrams/images won't come through).
- ✅ **Images — PNG/JPG/screenshots/phone photos** — read visually, **handwriting included.**
- ❌ **Scanned/photographed paper saved as a *PDF*** — not readable (no OCR / no PDF→image here).
  Give scans as **images**, not as scanned PDFs.

## Folders
- `_inbox/` — you drop here.
- `_inbox/_unsorted/` — engine parks anything it can't confidently classify (needs your confirm).
- `_inbox/TRIAGE-LOG.md` — append-only record of every routing decision.
