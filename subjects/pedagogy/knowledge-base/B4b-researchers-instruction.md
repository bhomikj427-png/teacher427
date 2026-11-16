# B4b — Researchers who turned instruction findings into methods

> Part B unit, same format as B4a: what they made into a usable method → its best real-use
> test → mechanism (pointer to Part A, not re-argued) → **serves** (A3 row) · **grade** · **use as
> learner** · **use as teacher**. Grade = method in practice / mechanism.
>
> Written S9b-1 (2026-11-15): §1–7 Rosenshine → Mazur. S9b-2 (2026-11-15): §8–14 Wieman → Hattie.

---

## 1. Barak Rosenshine (1930–2017) — Principles of Instruction

**What he built (Ros12, *American Educator* Spring 2012, 12–19, 39 — read at full text).** Ten
principles drawn from "three sources: (a) research in cognitive science, (b) research on master
teachers, and (c) research on cognitive supports", verbatim:
1. Begin a lesson with a short review of previous learning.
2. Present new material in small steps with student practice after each step.
3. Ask a large number of questions and check the responses of all students.
4. Provide models.
5. Guide student practice.
6. Check for student understanding.
7. Obtain a high success rate.
8. Provide scaffolds for difficult tasks.
9. Require and monitor independent practice.
10. Engage students in weekly and monthly review.

**Where "80% success" comes from.** Principle 7: in a fourth-grade maths study, "82 percent of
students' answers were correct in the classrooms of the most successful teachers, but the least
successful teachers had a success rate of only 73 percent"; "the optimal success rate for
fostering student achievement appears to be about 80 percent." Source type: **process-product
research** — observing which teachers' classes gained most and coding what they did. That is
**correlational** (the 80% describes effective classrooms; it was not manipulated). Note for the
engine: principle 4's "~80% success" (`research/01 §5`, `03`) rests partly on this strand —
consistent, but its own evidence base is observational.
**S11b-2 check (read-only grep of `research/`):** the engine's ~80% traces *only* to Rosenshine
2012 (`research/03 §1` principle 7; `01 §5` and `05` point back to `03`). The nearest
experimental result found is Wi19 (Wilson et al. 2019, abstract): for gradient-descent learners
on binary classification, learning is fastest at ≈85% training accuracy (error ≈15.87%) — shown
in artificial and "biologically plausible" neural-network models, **not** in classrooms or with
human learners. So the number is a sensible band with two weak supports (correlational
classroom data + a model result), not a measured human optimum. `uncertain` as a *number*;
the *principle* (hard but mostly successful) stays supported by A1/A4 (desirable difficulties
need a competence floor). Engine proposal (learner sign-off needed; nothing edited): word
principle 4 as "aim for a high success band (~80%; observational + model-based, not a measured
optimum)".

**Mechanism (pointers).** 1 & 10 = retrieval + spacing (A4 S); 2 = segmenting / working-memory
limits (A2, CLT); 3 & 6 = retrieval + formative checking; 4–5, 8–9 = worked examples → guided →
independent practice (fading, A4 S); 7 = calibration (principle 4).

**Serves:** A3 rows 1 and 4 most directly (facts, procedures); the structure applies to row 3.

**Grade:** **M–S** — a synthesis, not a tested package; each principle maps to an S-grade
mechanism except the 80% figure (correlational, T–M as a *number*). Widely adopted (England's
teacher-training framework uses it) — adoption is not evidence.

**Use as learner.** Run his 1 and 10 on yourself: start every session by recalling the last one;
keep a weekly and a monthly review slot.

**Use as teacher.** Use the ten as a lesson checklist. Treat "80%" as a rough band (most answers
right during practice, not all), not a target to engineer to the percent.

---

## 2. John Sweller — cognitive load theory (CLT)

**What he built.** From the finding that conventional problem solving (means–ends analysis) uses
working-memory capacity that is then "unavailable for schema acquisition" (Swe88, abstract),
a set of instructional effects: the **worked-example effect** (study solved problems instead of
solving cold), **completion problems**, **split-attention** (integrate text and diagram),
**redundancy**, the **expertise-reversal effect** (KACS03), and later the reframing of intrinsic
load as **element interactivity** relative to the learner's expertise (S10, CKS17).

**Mechanism.** → A2 (working memory), A3 (element interactivity column), A4 worked-example row,
A5 (schemas). Already sourced there; not re-argued.

**Boundary.** Expertise reversal: the same worked example that helps a novice wastes an expert's
capacity (KACS03, CKS17). CLT predicts *when* guidance helps, not that guidance always helps.
The KSC06 argument (minimal guidance fails for novices) is CLT applied to inquiry teaching;
`contested` at the edges by the 2007 rebuttals (scaffolded inquiry ≠ minimal guidance).

**Serves:** A3 rows 3 and 4 (high element interactivity for novices).

**Grade:** **S** for worked examples → fading with novices (A4); CLT as a theory — productive,
with measurement problems around "germane load" (not reviewed; `uncertain`).

**Use as learner.** New procedure: study 2–3 fully worked examples and explain each step before
attempting one; once you can do them, stop reading examples and solve.

**Use as teacher.** Put labels *on* the diagram, not in a separate legend (split attention);
don't narrate text that is also on screen word-for-word (redundancy); fade examples as students
improve.

---

## 3. Richard E. Mayer & Logan Fiorella — multimedia principles and generative learning

**What they built.** (a) Mayer's **multimedia design principles** (coherence, signalling,
redundancy, spatial and temporal contiguity, segmenting, pre-training, modality, multimedia,
personalization …) from the cognitive theory of multimedia learning. (b) Fiorella & Mayer's
**eight generative learning strategies** — summarizing, mapping, drawing, imagining,
self-testing, self-explaining, teaching, enacting (FM16).

**Evidence.** **No22** (meta-meta-analysis, 29 reviews, 1,189 studies, 78,177 participants): 11
design principles with positive meta-analytic effects; largest for second-language captions,
contiguity and signalling; good design matters more for complex material and system-paced
lessons. Generative strategies: the strongest of the eight are the ones with their own S-grade
metas (self-testing → retrieval; self-explaining → Bi18 g = 0.55); drawing and mapping M
(Sch17 for maps); summarizing low in D13 when untrained (A6).

**Mechanism.** → A2 (dual channels, limited capacity), A6 (generation, depth). Note: the
multimedia principle ("words + pictures > words alone") is *not* learning styles — it holds for
everyone (A8, M on learning styles).

**Serves:** A3 rows 2–3 (concepts, principles, explanations of systems).

**Grade:** design principles **M–S** (No22: positive across principles, sizes vary, many lab
studies with short retention intervals); generative strategies vary by strategy (S → T).

**Use as learner.** Turn text into something you *produce*: a labelled diagram from memory, an
explanation of each step, a self-test — not a highlighted page.

**Use as teacher.** Strip decorative extras (coherence), signal the key structure, put words next
to the parts they describe, and let learners control the pace of complex animations.

---

## 4. Manu Kapur — productive failure (PF)

**What he built.** Learners first attempt a **complex, ill-structured problem** designed to
activate prior knowledge and expose its limits, *before* instruction; then the teacher builds the
canonical solution by comparing and contrasting the students' attempts (Kap08, *Cognition and
Instruction* 26(3) 379–424 — "existence proof": unsupported group problem solving followed by
instruction outperformed well-structured, scaffolded problem solving on later problems).

**Evidence.** → A4 productive-failure row: SK21 meta, 53 studies / 166 comparisons, PS-I vs I-PS
**g = 0.36** [0.20, 0.51]; reversed for young learners (grades 2–5) and domain-general skills; the
reported bias-adjusted g = 0.87 is an unusual *upward* correction (`contested`); depends on design
fidelity (instruction must use the students' failed attempts).

**Mechanism.** → A6 (pretesting/generation activates prior knowledge and shows the gap; A1
desirable difficulty); A5 (contrasting cases highlight deep features).

**Boundary vs Sweller.** Not a contradiction: PF works for **conceptual** understanding when
learners have relevant prior knowledge and the instruction phase is strong; worked examples win
for **procedural** learning by novices (A4 bridge rows 3 vs 4; engine ROUTE step).

**Serves:** A3 row 3 (principles, concepts — e.g. variance, a formula's meaning).

**Grade:** **M** (one meta with real moderators; `contested` size).

**Use as learner.** Before reading how a concept is defined, spend 10–15 minutes inventing your
own way to solve a problem it answers; then read and compare.

**Use as teacher.** Use PF for the *idea* behind a formula, with students who have the
prerequisites; always follow with instruction that uses their attempts. Do not use it for
early-years learners or for teaching a procedure.

---

## 5. Michelene T. H. Chi — self-explanation, ICAP, novice/expert

**What she built.** (a) The **self-explanation effect** (Chi et al. 1989; prompting it → Bi18
g = 0.55). (b) **Novice vs expert categorization** (CFG81: novices sort by surface features,
experts by deep principles → A5). (c) Tutoring studies (CSJ01: prompting-only tutors as effective
— B1 §1). (d) The **ICAP framework** (CW14, Chi & Wylie 2014, abstract): engagement modes
**Interactive > Constructive > Active > Passive**, defined by overt behaviour; the ICAP
hypothesis predicts learning increases along that order; validated by reviewing studies on note
taking, concept mapping and self-explaining; also a tool to "dictate the proper choice of a
control condition".

**Mechanism.** → A6 (generation), A4 self-explanation row, A5 (expertise). ICAP is a
classification of activities by what the learner *produces*: passive (receiving), active
(manipulating — highlighting, copying), constructive (generating beyond the material —
explaining, mapping), interactive (co-constructing with a partner who also contributes).

**Serves:** A3 row 3 (principles), row 2 (categories via deep features); ICAP is a lens over all
rows.

**Grade:** self-explanation **S**; ICAP **M** (a framework supported by the authors' review of
three activity types; independent tests of the full ordering not reviewed here → `uncertain`).

**Use as learner.** Check your study activity's ICAP level: copying notes is *active*, not
*constructive*; explaining why each step works, or arguing it with a partner who pushes back, is
higher.

**Use as teacher.** Design tasks one level up: replace "highlight the key terms" with "write one
sentence explaining how A causes B"; replace solo reading with partner explanation where both
must add something.

---

## 6. Dylan Wiliam (with Paul Black) — formative assessment / assessment for learning

**What he built.** Black & Wiliam's review (BW98, *Assessment in Education* 5(1) 7–74) and the
practitioner pamphlet *Inside the Black Box* (1998) launched "assessment for learning": use
in-class evidence of what students know to adjust teaching, through questioning, feedback without
grades, peer- and self-assessment, and sharing success criteria. Wiliam's later five strategies
(clarifying intentions, eliciting evidence, feedback that moves learners forward, peers as
resources, learners as owners) — book-level, not read.

**Evidence and the size dispute.** The widely quoted effect of 0.4–0.7 SD is the contested part:
- **KN11** (Kingston & Nash 2011, abstract): "An effect size of about 0.70 (or 0.40–0.70) is often
  claimed … but is not supported by the existing research base." Of 300+ studies, "only 13 …
  provided sufficient information"; 42 effect sizes; median 0.25; random-effects weighted mean
  **0.20**; ELA 0.32, maths 0.17, science 0.09; PD-based and computer-based implementations 0.30
  and 0.28.
- **Ben11** (Bennett 2011, *Assessment in Education*, abstract): the term "does not yet represent a
  well-defined set of artefacts or practices"; "the magnitude of commonly made quantitative claims
  for effectiveness is suspect, deriving from untraceable, flawed, dated, or unpublished sources."
- **MVV13** (McMillan, Venable & Varier 2013): argue KN11's own selection and definitions limit its
  conclusions — the evidence base is thin on both sides.
- BW98 itself was a narrative review (no single pooled meta-analytic estimate); the 0.4–0.7 range
  circulates from it and from *Inside the Black Box*.

**Mechanism.** The components with strong evidence are **feedback** that targets the task and
process (engine feedback protocol; `research/04`), **retrieval** (questions all students must
answer), and **calibration** (A7). "Formative assessment" is a label for a family of practices,
so its average effect is small and variable.

**Serves:** all A3 rows (it is a loop around teaching, not a content method).

**Grade:** **M** for the components (feedback, retrieval checks); the package as usually
implemented **T–M** (≈0.2 SD in the best-documented studies, KN11). The 0.4–0.7 claim: **X** as a
promise (M67).

**Use as learner.** Before studying, write the success criteria (what you must be able to *do*);
check yourself against them, not against how familiar the material feels.

**Use as teacher.** Get an answer from every student (mini-whiteboards, hinge questions) and
change what you do next based on it — that is the active ingredient. Don't expect a big effect
from relabelling existing practice.

---

## 7. Eric Mazur — Peer Instruction (PI) and ConcepTests

**What he built.** In lectures, a conceptual multiple-choice question (ConcepTest) → students
vote individually → discuss with neighbours ("convince your neighbour") → revote → explanation.
Pre-class reading with written responses replaced reading quizzes (CM01).

**Evidence.**
- **CM01** (Crouch & Mazur 2001, abstract): ten years of PI in Harvard introductory physics:
  "increased student mastery of both conceptual reasoning and quantitative problem solving";
  further gains after adding pre-class written responses and cooperative learning. Single site,
  developer data, before/after comparisons.
- **Hak98** (Hake 1998, 62 courses, N = 6,542): average normalized gain on the Force Concept
  Inventory **0.23** in 14 traditional courses vs **0.48** in 48 interactive-engagement courses.
  Caveat: not randomized; courses self-reported; "interactive engagement" covers many methods.
- **Smi09** (Smith et al. 2009, *Science*, genetics course): after discussion, students did
  better on a *new isomorphic* question answered alone — "peer discussion enhances understanding,
  even when none of the students in a discussion group originally knows the correct answer."
  This rules out "they just copied the knowledgeable neighbour".

**Mechanism.** Commit to an answer first (pretesting/generation, A6) → explain and argue with a
peer (self-explanation + ICAP *interactive*, §5) → immediate feedback (A4) → targets
misconceptions in A3 row 3 (refutation, SK22).

**Serves:** A3 row 3 (principles — physics misconceptions), row 6 (calibration through the vote).

**Grade:** **M–S** — consistent quasi-experimental gains across many courses (Hak98), a
mechanism-isolating experiment (Smi09), and the underlying active-learning meta (Freeman et al.
2014 → S9b-2, Wieman). No large RCT of PI itself was reviewed.

**Use as learner.** In a study group: everyone answers a conceptual question silently first,
then argues, then answers a *different* question on the same idea alone.

**Use as teacher.** Pick questions where 30–70% get it right on the first vote (discussion is
most productive there — Mazur's practice guideline, `uncertain` source); always revote, and
follow with an isomorphic question to check it was understanding, not copying.

---

## 8. Carl Wieman — active learning in university science; the "feeling of learning"

**What he built.** Through the Carl Wieman Science Education Initiative (UBC, Colorado): replace
lecture with research-based active instruction — pre-class reading, in-class clicker questions
with peer discussion, small-group tasks with immediate feedback, the instructor responding to
what students produce ("deliberate practice" framing in class).

**Evidence.**
- **DSW11** (Deslauriers, Schelew & Wieman 2011, *Science*, abstract): two large sections
  (N = 267, 271) of introductory physics; one week (3 hours) taught by an experienced, highly
  rated lecturer vs a trained but inexperienced instructor using research-based active
  instruction: "increased student attendance, higher engagement, and **more than twice the
  learning**". Caveats: one week, one topic set, test written by the researchers, the active
  instructors were co-authors.
- **Fre14** (Freeman et al. 2014, *PNAS*, abstract — the meta Wieman's movement relies on):
  225 studies of undergraduate STEM: exam/concept-inventory scores **+0.47 SD** under active
  learning (158 studies); odds ratio for failing **1.95** under lecturing (67 studies) — "1.5
  times more likely to fail"; holds across disciplines and class sizes (largest in classes ≤ 50);
  trim-and-fill and fail-safe N "suggest that the results are not due to publication bias";
  robust to study rigor. (Roster's "failure 34% → 21%" is the paper's body, not abstract →
  backlog.)
- **Des19** (Deslauriers et al. 2019, *PNAS*, abstract): randomized students, identical content,
  active vs passive instruction (passive = "lectures by experienced and highly rated
  instructors"): students in the active classroom **learned more but felt they learned less**;
  the gap was partly caused by the greater cognitive effort; an early intervention explaining
  this to students helped.

**Mechanism.** Retrieval + feedback + interactive/constructive engagement (B4b §5, §7); the
Des19 result is A1's fluency illusion measured in a real course — effortful learning feels worse
(desirable difficulties, B4a §1).

**Serves:** A3 rows 3 and 5 (principles; choosing approaches in problems); row 6 (calibration).

**Grade:** **S** for active learning vs traditional lecturing in undergraduate STEM (Fre14, large
meta, bias checks) — with the caveat that "active learning" is a family, not one method;
DSW11's "twice the learning" is a one-week demonstration (T–M as a number).

**Use as learner.** If a class or method *feels* less productive because you are working
harder, that is the expected signal (Des19) — judge it by your delayed test result.

**Use as teacher.** Tell students in week 1 that active classes feel less effective and why;
replace some lecture time with questions every student answers, then discussion, then feedback.

---

## 9. Daniel Willingham — translating cognitive science for teachers

**What he does.** Translation, not new methods: *Why Don't Students Like School?* (2009; 2nd ed.
2021 — book, not read this sprint), the "Ask the Cognitive Scientist" column (*American
Educator*), and reviews such as **WHD15** (Willingham, Hughes & Dobolyi 2015, abstract):
learning-styles theories hold that people learn best in different ways, "but, in fact,
scientific support for these theories is lacking"; educators' time is "better spent on other
theories."

**Mechanism.** Points to Part A: memory as "the residue of thought" (what you think about is what
you remember — A6 depth of processing; book claim, wording `uncertain`), background knowledge as
the basis of critical thinking (A5), learning styles unsupported (A8).

**Serves:** A3 rows 1–3 and 6 (the knowledge-first message).

**Grade:** **M** as a synthesis (sound translations of S-grade findings; no new method to test).
Check every quoted line against the primary source he cites — that is how translators are used
in this KB (tier T3 for books, T1 for his reviews).

**Use as learner.** Use translators to find the right primary paper, then read its abstract.

**Use as teacher.** Plan lessons around what students will *think about* (if the activity makes
them think about the poster paint, they will remember the paint, not the history).

---

## 10. Paul A. Kirschner & Carl Hendrick — *How Learning Happens*; against minimal guidance

**What they do.** Kirschner co-authored KSC06 (minimal guidance fails for novices — A4, B4b §2);
with Hendrick, *How Learning Happens* (2020, book, not read): summaries of ~28 seminal papers for
teachers. Kirschner & De Bruyckere 2017 (**KD17**, abstract): "there is no such thing as a
digital native who is information-skilled simply because (s)he has never known a world that was
not digital", and the claimed ability to **multitask** "does not exist"; designing education that
assumes it "hinders rather than helps learning."

**Mechanism.** Guidance for novices (A4, CLT); working-memory limits make multitasking a series of
costly switches (A2).

**Serves:** A3 rows 3–4 (guided instruction), row 6 (myths about learners).

**Grade:** **M** as translators (sound summaries of S-grade evidence); KSC06 **S** for novices /
`contested` at the edges.

**Use as learner.** Study with one task open; switching between study and messages is not a
generational skill (KD17).

**Use as teacher.** Don't design for "digital natives"; design for working memory.

---

## 11. Pooja K. Agarwal — retrieval practice in real classrooms

**What she built.** Co-author of the classroom quizzing studies (McD11, RAMM11 — B4a §2); the
practitioner site retrievalpractice.org and *Powerful Teaching* (Agarwal & Bain 2019, book, not
read). Key review: **ANB21** (Agarwal, Nunes & Blunt 2021, *Educational Psychology Review* 33(4)
1409–1453, abstract): narrow definition of "classroom research"; ≈2,000 abstracts screened;
**50 experiments, 49 effect sizes, n = 5,374; 57% showed medium or large benefits**; benefits
across education levels, subjects, designs, delays, formats and feedback timing; **only 6% of
experiments in non-WEIRD countries**.

**Mechanism.** → A4 retrieval-practice row; A1.

**Serves:** A3 rows 1 and 3.

**Grade:** **S** (systematic review of classroom experiments, consistent). Caveat that matters for
this learner: almost all evidence is from WEIRD countries — no reason to expect the memory
mechanism to differ, but classroom implementation evidence is thin elsewhere.

**Use as learner.** Retrieval works for you whatever your level or subject (ANB21's range); the
form (MC, short answer, free recall) matters less than doing it with feedback.

**Use as teacher.** Low-stakes retrieval at the start of lessons ("brain dumps", two-things
recall), with feedback, works across the settings tested.

---

## 12. The Learning Scientists (Yana Weinstein, Megan Sumeracki, Oliver Caviglioli) — six strategies

**What they built.** Free teacher/student materials on **six strategies** — spaced practice,
interleaving, retrieval practice, elaboration, concrete examples, dual coding — with posters by
Caviglioli. The academic version: **WMS18** (Weinstein, Madan & Sumeracki 2018, *Cognitive
Research: Principles and Implications* 3, tutorial review, abstract): six strategies "that have
received robust support from decades of research", with basic and applied research and
implementation examples.

**Mechanism.** Spacing, retrieval, interleaving → A4 (S, S, M); elaboration → A4 elaborative
interrogation (M); concrete examples → B1 §6 / concreteness fading (M); dual coding → No22
multimedia (M–S).

**Serves:** A3 rows 1–5.

**Grade:** **M–S** (faithful translation; the six are not equally strong — "robust support" is
true for spacing and retrieval, moderate for the others). Uniform posters can make all six look
equally proven (M70).

**Use as learner.** Start with the two strongest (retrieval + spacing); add interleaving once you
have several problem types; use elaboration and examples for understanding.

**Use as teacher.** Their materials are a good student handout — add the strength ranking.

---

## 13. Graham Nuthall (1935–2001*) — *The Hidden Lives of Learners*

*\*Year of death: summaries say 2004; roster's 2001 is unverified → backlog.*

**What he did.** Decades of fine-grained classroom observation in New Zealand: individual
microphones on students, recording everything each student heard, said and did during a unit,
then testing what they learned and remembered up to a year later. Peer-reviewed: **NAL95**
(Nuthall & Alton-Lee 1995, *AERJ*, abstract): 14 students; a model of how students use
"multilayered episodic and semantic memory" to answer test items; **Nut00** (Nuthall 2000,
*Cognition and Instruction* 18(1) 83–139, abstract): recollection 12 months later "replaced
details with inferences and summaries, and direct recall with deductions from related generic
schemas."

**The "three encounters" claim.** In *The Hidden Lives of Learners* (2007, posthumous; not read),
p. 63 as quoted by a secondary source (Watson, Learning & the Brain blog — T3): a student needed to
encounter the **full set of information** about a concept on **at least three different
occasions** to learn it; the same secondary source notes p. 126 says **four**. Wexler (T3)
reports Nuthall's rule predicted learning with **80–85%** accuracy. Status: `uncertain` — the
count and accuracy come from very small observational samples, and the exact wording is
unverified at the book (backlog).

**Mechanism.** Repeated encounters spaced across a unit = **spacing** + multiple retrieval or
re-encoding opportunities (A4 S); "full set of information" = complete schema components (A5);
12-month reconstruction from schemas = A2 (reconstructive memory).

**Serves:** all A3 rows (it is a claim about exposure count).

**Grade:** **T–M**: rich observational evidence, very small N, no manipulation of encounter count;
the "three" is a useful planning heuristic, not a law (M71).

**Use as learner.** Plan to meet every key idea at least 3–4 times, complete each time, on
separate days — first teaching, then two or three retrievals.

**Use as teacher.** Track, for each key concept, how many *complete* encounters each student has
had — a student who missed one lesson may have had only two.

---

## 14. John Hattie — *Visible Learning* (2009): a methodology case

**What he built.** A synthesis of (by his account) 800+ meta-analyses, converted to a common
effect size (Cohen's d) and **ranked** as a league table of "influences" on achievement, with a
"hinge point" of **d = 0.40** as the average to beat (book, not read; figures as widely reported
→ `uncertain`). Also a sound primary review: **HT07** (Hattie & Timperley 2007, "The Power of
Feedback", *RER* 77(1) 81–112, abstract): feedback is "one of the most powerful influences on
learning and achievement, but this impact can be either positive or negative"; type and delivery
matter; a model of effective feedback.

**The methodological critique (why this is a cautionary case).**
- **Sim17** (Simpson 2017, *Journal of Education Policy* 32(4) 450–466, abstract): standardized
  effect size "is open to researcher manipulations which violate the assumptions required for
  legitimately comparing and combining studies"; league tables "may, instead, be hierarchies of
  openness to research design manipulations." (Effect sizes depend on the test, the sample's
  spread, the comparison condition and the study length — B2 pattern: Bloom's 3-week 2σ vs
  Slavin's semester-long +.04.)
- **Ber17** (Bergeron 2017, *McGill Journal of Education*, statistician's critique, abstract):
  calls the method "pseudoscience" because Cohen's d "simply cannot be used as some sort of
  universal measure of impact" across such different studies.
- Averaging meta-analyses of different quality, outcomes and comparison groups mixes things that
  are not the same quantity; the hinge point d = 0.40 inherits all of that.

**Mechanism.** Not a method. The *individual* findings often point the right way (feedback,
clarity, formative evaluation rank high; learning styles low) — but the ranking and the numbers
should not be used to choose between methods. Use the primary metas behind each line instead
(this KB's approach: A4 grades by replication and moderators, never by one d).

**Serves:** none (meta-level).

**Grade:** league table as a decision tool **X** (methodology); HT07 feedback model **M**
(narrative review; the "can be positive or negative" point agrees with Kluger & DeNisi 1996, the
engine's ~38% figure, `research/04`).

**Use as learner.** When anyone quotes "d = 0.7, top of Hattie's list", ask which studies, which
test, what comparison — the A8 §3 kit.

**Use as teacher.** Use Hattie as a pointer to topics worth reading about (feedback, formative
evaluation), then go to the primary meta-analysis for that topic.

---

## Summary (B4b, all 14)

| Researcher(s) | Method made usable | Serves (A3) | Grade (method / mechanism) |
|---|---|---|---|
| Rosenshine | 10 principles of instruction | 1, 4 (3) | **M–S** synthesis / mechanisms S; 80% = correlational |
| Sweller | CLT: worked examples, split attention, expertise reversal | 3, 4 | **S** for novices / theory productive |
| Mayer & Fiorella | multimedia principles; 8 generative strategies | 2, 3 | **M–S** (No22) / strategies vary |
| Kapur | productive failure | 3 | **M** (SK21 g 0.36, `contested` size) |
| Chi | self-explanation; ICAP; novice/expert | 3, 2 | self-explanation **S**; ICAP **M** |
| Wiliam (& Black) | formative assessment | all | components M; package **T–M** (KN11 ≈0.20); 0.4–0.7 claim **X** |
| Mazur | Peer Instruction + ConcepTests | 3, 6 | **M–S** (Hak98, Smi09, CM01) |
| Wieman | active learning in STEM; feeling-of-learning | 3, 5, 6 | **S** (Fre14 0.47 SD, OR fail 1.95; Des19 RCT) |
| Willingham | translation; learning styles unsupported | 1–3, 6 | **M** (translator) |
| Kirschner & Hendrick | translation; against minimal guidance, digital-native and multitasking myths | 3, 4, 6 | **M** (translators); KSC06 S novices |
| Agarwal | classroom retrieval practice | 1, 3 | **S** (ANB21: 50 experiments, 57% medium/large; 6% non-WEIRD) |
| Learning Scientists | six strategies | 1–5 | **M–S** (WMS18; strengths unequal) |
| Nuthall | 3–4 complete encounters; hidden classroom learning | all | **T–M** (observational, small N; count `uncertain`) |
| Hattie | effect-size league tables; feedback model | — | league table **X** as decision tool; HT07 **M** |

**Pattern across B4b.** (1) The **instruction** researchers converge on one lesson shape: review
→ small steps with models → every student answers → feedback → guided then independent practice
→ spaced review (Rosenshine's list is that convergence written down; Wieman's and Mazur's active
classes are its university version). (2) The **labels** are weaker than their components:
"formative assessment" ≈0.2 as a package, "active learning" a family with a strong average,
"Visible Learning" rankings not a decision tool — always grade the mechanism inside the label.
(3) **Effortful learning feels worse** (Des19; Bjork B4a §1) — this is the single most practically
important finding for learners, because it predicts they will abandon the methods that work.
(4) **Numbers travel without their conditions**: the 80% success rate (correlational), 0.4–0.7
(untraceable), 2σ (3 weeks), d = 0.40 hinge (mixed metas) — every famous number in this unit
needed its source re-read.

## Misconceptions owned (B4b)
§1–7: M67 (formative assessment 0.4–0.7 SD), M68 (productive failure vs CLT), M69 (busy = active
learning). §8–14: M70 (all six "Learning Scientists" strategies are equally proven), M71 ("students
need exactly three encounters" as a law), M72 (Hattie's rankings tell you which method to choose),
M73 (if a class feels like I'm learning less, I am) — full entries in `misconceptions.md`.
