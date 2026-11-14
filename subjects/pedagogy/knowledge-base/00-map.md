# Pedagogy — Knowledge Base Map (Layer 2)

> Built per `../../../subject-research-protocol.md`. Work runs in sprints (`../sprints.md`).
> **Stage status: `stage-1`** (S1 map pass; S2 A1 + A2; S3 A3 — 2026-11-15).
> Teaching gate = `stage-2✓` (no exception). Delivery once complete = study pack
> (`study-pack-format.md` v1.2).

## 0. Scope & goal
- **Learner goal (stated 2026-11-15):** three equal aims: (1) learn better as a learner,
  (2) teach others well, (3) understand and upgrade this tutor engine. Every topic carries all three uses.
- **Shape:** Part A = the science of learning, organised by *kind of information*. Part B = the
  teachers and method-makers (`roster.md`), each method tied to the Part A information type it
  serves and graded for evidence.
- **Core distinction (learner's framing):** *studying* = sitting down with the intent to learn;
  *learning* = a durable, transferable change in what you can do unaided. Anchor: learning vs
  performance (SB15).
- **Relation to the engine:** `../../../research/` is a seed only; every claim is re-verified at
  primary source for this KB. Findings that would change the engine become a proposal (design
  sign-off first), never a direct edit.
- **Files:** `sources.md` (tiered canon, IDs used everywhere) · `misconceptions.md` ·
  `roster.md` (Part B people) · `justin-sung-claims.md` (claim inventory → S10 audit) ·
  `CHANGELOG.md`.

## 1. Part A — units
| Unit | Content | Anchor sources (IDs → `sources.md`) |
|---|---|---|
| A1 | Studying vs learning; performance vs learning; fluency illusions; storage vs retrieval strength | SB15, BB92, BB11, RK06, KB11, PR18, KoB08 — **written S2** (`A1-studying-vs-learning.md`) |
| A2 | Memory architecture: working memory (~4 chunks), long-term memory, memory systems, encoding → consolidation (sleep) → retrieval, forgetting | C01, B00, Sq04, MLH13, RB13, W04, TT73, MD15 — **written S2** (`A2-memory-architecture.md`) |
| A3 | **Kinds of information** (the hub) — see §3 decision | K02 [full], G84 [full], CRK22 [full], KCP12, A82, FP67, KMS10, G08, S10, CKS17, Sq04, BC82 — **written S3** (`A3-kinds-of-information.md`) |
| A4 | **Bridge: kind of information → method** | KCP12, D13, FM16 |
| A5 | Schemas, chunking, novice vs expert, transfer | CS73, CFG81, BC02, BC82 |
| A6 | Depth of processing & generative learning (Justin Sung's terrain): levels of processing, generation, elaboration, concept maps, advance organizers, pretesting | CL72, FM16, NA06, Sch17, RKK09 |
| A7 | Metacognition & self-regulated learning; calibration | Z02 (+ Dunlosky & Rawson 2012 → add S5) |
| A8 | Myths | P08 (+ research/06 seeds → re-verify S6) |

## 2. Prerequisite graph

```
A1 studying vs learning ──┐
                          ├──> A3 kinds of information ──> A4 kind → method ──┬──> A5 schemas / expertise / transfer
A2 memory architecture ───┘          (hub)                                     ├──> A6 depth & generation
                                                                              └──> A7 metacognition (needs A1 too)
A8 myths: after A1 + A2 (each myth is refuted by a mechanism taught there)

Part B: every tier needs A3 + A4 (each entry ends "serves → A3 type")
  B1 historical, B2 method-builders, B3 classroom legends: A3 + A4
  B4a researchers (memory & practice): + A1, A2
  B4b researchers (instruction): + A5, A6
  B5 practitioners + Justin Sung audit: all of A1–A7
```

## 3. A3 spine decision (S1, 2026-11-15)

**Problem:** four taxonomies of "kinds of information" compete, and each answers a different question.
| Taxonomy | Answers | Strength | Gap |
|---|---|---|---|
| Krathwohl 2002 (K02): factual / conceptual / procedural / metacognitive | *What* is being learned (objective-writing) | Clear, widely used, readable | Says nothing about how each kind is learned |
| Gagné (G85): verbal information / intellectual skills / cognitive strategies / motor skills / attitudes | Which *conditions* each learned capability needs | Links type to method directly; includes motor and attitudes | Pre-cognitive-science; no memory-systems or load grounding |
| KLI, Koedinger et al. 2012 (KCP12) | Which *learning process* (memory & fluency / induction & refinement / understanding & sense-making) and so which instruction each knowledge component needs | Only one built to link knowledge → learning → instruction, from a large body of classroom experiments | Abstract; knowledge-component types need full-text verification |
| Brain systems (Sq04) + Geary (G08) + Sweller (S10) + SOLO (BC82) | Where it is stored · whether evolution prepared us for it · how many elements interact · how connected it is | Explain *why* methods differ | Not a teaching taxonomy on their own |

**Decision:** A3 uses **one combined table**.
- **Rows** = kinds of information: Krathwohl's four, plus Gagné's motor skills and perceptual
  (pattern-recognition) knowledge as separate rows.
- **Columns** = what explains how each row is learned:
  - brain system (declarative / nondeclarative)
  - primary or secondary (Geary)
  - typical element interactivity (Sweller)
  - target SOLO level
  - KLI learning process
- **A4** then reads method off the KLI-process column. That is the link Part B attaches to.

*Rationale:* the readable labels come from Krathwohl. The link from kind of information to method
comes from KLI and Gagné. The mechanism comes from the brain-systems, Geary, Sweller and SOLO
columns. No single taxonomy gives all three. **S3 outcome (2026-11-15):** KLI typology confirmed at full text via CRK22 (Koedinger co-author)
— facts = constant–constant, skills = variable–variable. Two refinements: Geary moved from a
column to a cross-cutting lens (every school row is secondary, so it doesn't vary by row); a
separate row 5 *conditional knowledge* added (Krathwohl Cc/Db). Final table: A3 §3.

## 4. Threshold concepts (each changes how the rest is seen; teach slowly, check hard)
1. **Learning ≠ performance** (A1). Without it, every fluent session looks like success.
2. **The working-memory bottleneck vs a large long-term memory; schemas get around the bottleneck** (A2 → A5).
3. **The best method depends on the kind of information** (A3/A4, KLI). This is the bridge from Part A to Part B.
4. **Retrieval is itself an encoding event** (A1/A6). This settles the encoding-vs-retrieval
   split at the centre of the Justin Sung audit (J4, J6, J7, J16).
5. **Some forgetting is useful** (A1/A2, storage vs retrieval strength).

## 5. Build order
See `../sprints.md` (S2 → S13 to `stage-2✓`, then S14 study-pack pilot).
