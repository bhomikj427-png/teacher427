# sem-3 — Semester 3 batch (B.Tech ECE, Manipal University Jaipur)

A container for **all Semester-3 ECE subjects at once**, plus an autonomous **research engine**
that builds each subject's knowledge base to standard with no input required from the learner.

This is pure file management on top of the Layer-1 engine (`../../CLAUDE.md`,
`../../teaching-manual.md`, `../../research/`) and the subject standard
(`../../subject-research-protocol.md`). Nothing here overrides those — it *organises* many
subjects and *automates* the research that the subject protocol already mandates.

## Source of the course list (authoritative)

The subjects below are the official **Third Semester** scheme for **B.Tech Electronics &
Communication Engineering**, pulled from MUJ FoSTA:

- Curriculum / scheme PDF: `B Tech ECE Curriculum_2023 onwards.pdf`
  <https://jaipur.manipal.edu/fosta/img/programs/btech/B%20Tech%20ECE%20Curriculum_2023%20onwards.pdf>
- Detailed syllabus PDF: `B Tech ECE Syllabus_2023 onwards.pdf`
  <https://jaipur.manipal.edu/fosta/img/programs/btech/B%20Tech%20ECE%20Syllabus_2023%20onwards.pdf>

Pulled 2026-06-16. The scheme is "2023 onwards"; re-confirm against the live PDF if the batch year
differs. Each subject's exact official text + textbooks live in its `course-info.md`.

## The subjects (official Sem-3 scheme)

| # | Folder | Code | Course | L-T-P-C |
|---|--------|------|--------|---------|
| 01 | `01-statistics-and-probability` | MAS2001 | Statistics & Probability | 3-0-0-3 |
| 02 | `02-management-of-technology` | MBB21XX | Management of Technology | 3-0-0-3 |
| 03 | `03-electronic-devices-1` | ECE2101 | Electronic Devices-I | 3-1-0-4 |
| 04 | `04-digital-electronics` | ECE2102 | Digital Electronics | 3-1-0-4 |
| 05 | `05-signals-and-systems` | ECE2103 | Signals and Systems | 3-1-0-4 |
| 06 | `06-circuits-and-network-theory` | ECE2120 | Circuits & Network Theory *(Flexi Core 1, option A)* | 3-0-2-4 |
| 07 | `07-linear-integrated-circuits` | ECE2121 | Linear Integrated Circuits *(Flexi Core 1, option B)* | 3-0-2-4 |
| 08 | `08-electronic-devices-lab-1` | ECE2130 | Electronic Devices Lab-I | 0-0-2-1 |
| 09 | `09-digital-electronics-lab` | ECE2131 | Digital Electronics Lab | 0-0-2-1 |
| 10 | `10-project-based-learning-1` | ECE2170 | Project-Based Learning 1 | 0-0-2-1 |

**Flexi Core 1 (06/07):** the official scheme requires the learner to take *one* of ECE2120 /
ECE2121. Both are scaffolded here (learner has not yet confirmed which). Research covers whichever
is needed; only the chosen one needs teaching.

## Dumping material: the central `_inbox/`

Got PYQs, PPTs, or notes but don't want to sort them? Drop **everything into `_inbox/`** — one
folder, any subject, unsorted. The engine triages each file and routes it to the right subject's
`exam-pack/`, then rebuilds that subject's exam-map. See `_inbox/README.md`. (You can still drop
straight into a known subject's `exam-pack/` if you prefer.)

## Two-layer shape of each subject folder

Each subject mirrors the standard subject shape (`../README.md`), built in two phases:

```
NN-subject/
├── course-info.md     # seeded NOW: official MUJ code, L-T-P-C, official syllabus text,
│                       #   prescribed textbooks, source URLs + confidence flags
├── knowledge-base/     # built by the RESEARCH ENGINE. Empty until researched.
│   ├── (00-map.md, per-unit notes, misconceptions.md, sources.md, CHANGELOG.md)  ← STAGE 1 (exam)
│   └── stage-2/         # STAGE 2 (IIT/Ivy depth) — physically separate so exam study stays clean
├── curriculum.md       # created when the subject is first TAUGHT (derived from 00-map)
├── learner-profile.md  # created when the subject is first TAUGHT
└── progress-log.md     # created when the subject is first TAUGHT (session-resume record)
```

**Two distinct activities, do not confuse them:**
- **Research** (autonomous, no learner needed) → fills `knowledge-base/`. Run by the
  `research-engine/`. See `research-engine/AUTONOMOUS-RUN.md`.
- **Teaching** (needs the learner) → adds `curriculum.md` + `learner-profile.md` +
  `progress-log.md` and runs the `../../CLAUDE.md` loop. Created only when a subject is activated.

## The research engine

`research-engine/` is the **batch-wise autonomous researcher**. It works through every subject in
this folder and builds each knowledge base to two escalating depths — **Stage 1 (MUJ level)** then
**Stage 2 (IIT / Ivy level)** — with **no input required** from the learner. Start it from a fresh
terminal by following `research-engine/AUTONOMOUS-RUN.md`. Progress lives in
`research-engine/research-queue.md` so any session resumes exactly where the last stopped.

## How to teach a sem-3 subject (later)

To activate a subject for teaching, tell the tutor (e.g. "let's start Digital Electronics"). It
will: **confirm the knowledge base is COMPLETE (`stage-2✓`, both stages) — and if it is below that,
run/resume the research engine to bring this subject to `stage-2✓` first (depth-first), never
teaching from a partial base** (the hard teaching gate, `research-engine/two-stage-depth.md`); then
diagnose level, derive `curriculum.md` from `knowledge-base/00-map.md`, init the profile + progress
log, and begin the loop. Universal preferences (`../../learner-preferences.md`) apply throughout.
