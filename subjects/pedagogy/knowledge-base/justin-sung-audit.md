# Justin Sung — Claim Audit (S10a, 2026-11-16)

> Verdicts for every claim in `justin-sung-claims.md` (J1–J22) plus six new claims found in his own
> videos this sprint (J23–J28). **Verdict scale:** `supported` (matches replicated evidence) ·
> `partly` (a true core with an over-reach or missing boundary) · `unsupported` (evidence against,
> or a factual claim with no source found) · `untestable` (no study could settle it as stated).
> **Wording check:** `captions` = re-checked against the video's own captions this sprint (S10 rule
> for `digest` claims); `human transcript` = TEDx talk (TED's volunteer transcript, cleaner than
> ASR); `not re-checked` = still digest/interview wording, verdict judged on the reported wording.
> Evidence IDs are in `sources.md`; Part A pointers say where the mechanism is argued.
>
> **Sources read this sprint (captions via `tools/fetch_transcripts.py`; transcripts kept out of
> the repo):** JS-TED (TEDxUOA, 2022-12-06) · JS-PRB ("The PROBLEM with Active Recall and Spaced
> Repetition", 2021-10-20) · JS-RNK ("Learning Expert Ranks Study Techniques…", 2023-12-13) · JS-6L
> ("6 Levels of Thinking…", 2024-06-07) · JS-SR ("What Everyone Gets WRONG About Spaced
> Repetition", 2022-07-22) · BK22 (Benjamin Keep, "What Study Gurus Get Wrong About Learning",
> 2022-10-19 — **the Learning-Sciences-PhD response video, found**) · JS-CO (Sung, "I got called
> out by a Stanford learning scientist", 2023-04-17 — joint reaction with Keep). Plus Ag19 and
> KGF19 abstracts (verified this sprint).

---

## 1. The central dispute, settled first: is retrieval "only" anti-forgetting? (J4, J6, J7, J16)

**What Sung said (JS-PRB, captions, 2021):** "the reason active recall and space repetition works in
the first place is by adjusting and working on this forgetting curve"; retrieval techniques are
"easier to learn … pretty much anyone can pick it up"; encoding needs cognitive load and is where
the gains are.

**The response (BK22, captions).** Keep's argument, in order: (1) what Sung criticises is a
*spaced retrieval system* — flashcard apps (Anki, SuperMemo, Quizlet) on "isolated,
decontextualized facts" — not *retrieval practice* as researched; (2) the desirable difficulties
(spacing, interleaving, contextual variation, testing) are thought to work partly *through*
retrieval; (3) Sung's own higher-order advice (compare, relate, evaluate) applies to *retrieval
prompts* too — solving problems or holding a conversation in a language *is* retrieval practice;
(4) the one direct encoding-vs-retrieval test he shows (concept mapping vs free recall — KB11)
favours retrieval, while learners predicted the reverse. Conclusion: "you don't have to choose
between encoding and retrieval — you can do both."

**Sung's reply (JS-CO, captions, 2023).** He agrees with the substance: "the biggest regret I have
is not clearly differentiating active recall versus space repetition"; he now says "spaced
retrieval" when writing for informed audiences; he accepts that flashcards are "better than doing
nothing" but not best. On KB11 he argues the mapping condition was not a strong mapping technique
— a fair *research-gap* point, not evidence that mapping wins.

**Verdicts.**

| # | Claim | Verdict | Evidence | Wording |
|---|---|---|---|---|
| J4 | Retrieval/spacing mainly fight the forgetting curve; little encoding value | **unsupported** (as stated in 2021) | Retrieval is itself a learning event that changes what is stored and supports inference questions (KB11, RK06; A1 §5). Higher-order retrieval prompts improve higher-order test performance (Ag19). Sung withdrew the framing himself (JS-CO). | captions |
| J6 | AR/SR become lower-order when over-relied on; he should have separated them | **partly** | True that *fact-only* prompts don't build higher-order performance (Ag19: fact quizzes did not improve higher-order tests). But the level is set by the **prompt**, not by retrieval as such (A1 §5; A3 row 1 vs 3/5). Self-correction confirmed in JS-CO. | captions (JS-CO) |
| J7 | Retrieval practice is essentially always effective | **supported, with a boundary** | JS-RNK: active recall "A, easily S … as long as you're recalling something from memory it tends to be pretty good". Matches D13 (practice testing: high utility) and RK06/McD11; boundary: retrieval of the *wrong kind* of item doesn't transfer up (Ag19), and feedback matters for low-success retrieval (A4). | captions |
| J16 | Spaced repetition is S-tier | **supported** (as a principle) | JS-RNK gives *spacing* S "as a general principle … you should be spacing retrieval sessions" and separates it from flashcards (D). Matches C06, RD11 (A1/A2). The J4 vs J16 "tension" is resolved: J16 rates the principle, J4 attacked a tool. | captions |

**Net:** the "Sung vs retrieval practice" dispute is mostly a **naming** dispute (flashcard apps ≠
retrieval practice) plus one real error (J4's "only fights forgetting"), which he has corrected.
The evidence-backed synthesis is the one both ended on: **encode by relating, and retrieve with
prompts at the level you'll be tested at.** This is already the engine's position (A4 bridge rows
1/3/5).

---

## 2. Higher-order learning, grouping, and effort (J1, J2, J3, J5, J9, J12, J21, J23)

| # | Claim | Verdict | Evidence | Wording |
|---|---|---|---|---|
| J1 | Studying ≠ learning; technique not hours | **supported** | JS-TED: "Studying is not the same thing as learning … you haven't learnt it until that knowledge is in your head and you can use it." Matches learning vs performance (SB15) and time ≠ learning (M1). | human transcript |
| J2 | Integrated (higher-order) learning is more time-efficient because you relearn less | **partly** | Mechanism is real: elaborated, related material is better retained (CL72 levels of processing; generation Be07; schemas A5). But no study measures "less total relearning time" for his method; and integration does **not** remove the need for spaced retrieval (RD11, KB11; see M77). His "snowball" point (prior knowledge speeds new learning) is supported (A5 schemas). | human transcript |
| J3 | Monitor the *feeling* of lower- vs higher-order learning; tally it | **partly** | Self-monitoring itself is part of SRL (Z02, DB08). But feelings *during* study are poor monitors of learning (BDK13, KoB08; Des19 learners felt they learned less in the better condition); delayed retrieval attempts are good ones (RT11). The "slipping out" feeling may be informative about isolation, but untested as a cue. | human transcript |
| J5 | Encoding needs cognitive load; learning rises with load up to a threshold, then falls | **partly** | The inverted-U is consistent with desirable difficulties (BB11) and CLT's overload limit (S10, CKS17). Over-reach: CLT distinguishes **intrinsic** load (worth keeping) from **extraneous** load (always cut); "more load is better" is false for extraneous load and for novices on high-interactivity material (expertise reversal, KACS03; A4). | captions |
| J9 | Group new information by similarity against the big picture; this forces higher-order learning | **partly** | Organizing/grouping is a generative strategy (FM16) and "constructive" in ICAP (CW14); comparison helps schema abstraction (GH80/83 via A5). Boundary: no test of his specific grouping procedure; generation fails on arbitrary material (A6). | human transcript (TED step 2) |
| J12 | The effort of deciding which relationships matter *is* the learning | **partly** | Matches generation (Be07) and constructive processing (CW14). Over-reach: effort is not itself the cause — effort is a by-product of the processing that helps (M16: not every difficulty is desirable). | human transcript |
| J21 | Students must master "6 levels of thinking" | **supported as description** | JS-6L: the six levels are Bloom's revised taxonomy (remember → create; he names it, 1956/2001). K02 confirms the six processes; he presents the levels loosely and reorders "create" as least important for most people (a judgment, not a finding). See M28 (not a strict ladder). | captions |
| J23 *(new)* | Start at level 5 (evaluate) and move down; "the brain forms memory more strongly at level five"; lower levels get filled in along the way | **partly** | Supported part: higher-order and mixed retrieval quizzes improved higher-order test performance, fact-only quizzes did not (Ag19, middle-school + college, lab + classroom). Over-reach: Ag19's learners still *studied* the material and mixed quizzes worked as well as higher-order ones; nothing shows facts are reliably "filled in" without being practised. Novices on high-interactivity content need worked guidance first (KSC06, KACS03). | captions |

---

## 3. Notes, mind maps, priming, and the technique tier list (J10, J11, J13, J14, J17–J20)

Tier-list wording re-checked in JS-RNK (captions); his list has **two parts** — tiers "as people
normally use" a technique, then upgrades. Tiers below are part 1.

| # | Claim | Verdict | Evidence | Wording |
|---|---|---|---|---|
| J10 | Use analogies to link new information to what you know | **partly** | Analogical comparison helps transfer when two cases are compared (GH80/83, A5); a *single* analogy often isn't spontaneously used. Advance organizers: small, old evidence (LAA80; M58). | not re-checked (interview) |
| J11 | Non-linear notes / mind maps build relationships; typical mind maps are C-tier, "barely any better and sometimes just worse than linear notes" | **partly** | Constructing concept maps beats reading/listening (Sch17: construct g 0.72 vs study 0.43; NA06) but loses to retrieval practice (KB11). His "C as normally used" agrees that the *tool* is not the active ingredient; his claim that a better mapping method would close the gap is **untested** (his own point in JS-CO). | captions (C tier) + human transcript |
| J13 | Build a personal question bank | **partly** | Self-generated questions are a form of generation/elaboration; elaborative interrogation is *moderate* utility (D13). Answering one's own questions later = retrieval. No direct test of his format. | not re-checked |
| J14 | Pre-study ("priming") done well is one of the most important things | **partly — wording corrected** | JS-RNK actually rates pre-study **B** ("mixed effectiveness") as normally done, upgradable. Evidence: prequestions help the asked items (g 0.54) but barely the rest (g 0.04; SCA24); errorful pretests help (RKK09, KHB09); advance organizers small (LAA80). "One of the most important" is not supported; "useful when it means attempting questions first" is. | captions |
| J15 | Sleep is S-tier | **supported** | JS-RNK: S, "sleep-dependent memory consolidation". RB13 (A2); M25. His mechanism line ("short-term memory … shunted over") is a loose paraphrase of systems consolidation. | captions |
| J17 | Flashcards are D-tier (as normally used) | **partly** | D13 rates practice testing **high**; flashcards are one format of it. The D grade only holds as a claim about *typical misuse* (too many isolated cards, no relational prompts) — he says this explicitly (JS-RNK: "I don't hate flash cards"). KLI: flashcards fit constant–constant facts (A3 row 1; CRK22) and not principles or procedures. | captions |
| J18 | Rereading and highlighting are D-tier | **supported** | JS-RNK: "plainly sucks … if there was an E it would be an E". D13 rates both low utility. M6. | captions |
| J19 | Watching videos/lectures, as usually done, is D-tier | **partly** | ICAP: passive viewing is the weakest mode (CW14), and active-learning classes beat lecture (Fre14). But a good explanation *is* useful for novices (worked examples, A4); the problem is passivity, not the medium. | captions |
| J20 | Ratings reflect normal use; many improve with modification | **supported (as framing)** | Moderators matter: D13 itself lists conditions per technique; feedback and prompt level change retrieval benefits (Ag19). The specific upgrade gains are untested. | captions |

---

## 4. Claims about evidence, data and capacity (J8, J22, J24–J28)

| # | Claim | Verdict | Evidence | Wording |
|---|---|---|---|---|
| J8 | Encoding skills have the most impact but should be developed last | **untestable as stated** | No study found that tests the order in which study skills should be trained. Sequencing advice is reasonable (SRL training effects are moderate and vary, DB08) but not evidenced. | not re-checked (course digest) |
| J22 | SuperMemo community says Sung contradicts Woźniak | **open — not located** | supermemo.guru page returned 404 (2026-11-16); search found no page linking the two. Stays `uncertain`; low priority (a partisan dispute, not an evidence question). | — |
| J24 *(new)* | ~5,000 students in 120 countries: his methods reach in 1–2 weeks the learning that normally takes 4 | **unsupported** | Company data (JS-TED), no control group, no published report; he said in 2021 he was "gearing up to publish it in journals" (JS-PRB). Searches 2026-11-16 (Crossref, Europe PMC, web) found **no peer-reviewed outcome study** by Sung; iCanStudy's 2022 "Report on Learning" is self-published and calls itself "a relatively superficial and brief summary". Commercial conflict of interest. | human transcript + captions |
| J25 *(new)* | Your tolerance for cognitive load "can actually be trained" | **unsupported** as a capacity claim | Working-memory training does not produce far transfer (MLH13; M22). What does change with practice is **knowledge**: schemas reduce the load a task imposes (A5; CKS17). Read charitably, his claim is the second one, which is supported. | captions (JS-PRB) |
| J26 *(new)* | Feeling confused is "a sign that your brain is engaging high efficiency learning pathways" | **partly** | Effortful strategies are often the better ones and learners misread effort as poor learning (misinterpreted-effort hypothesis, KGF19 — he names it in JS-TED and JS-6L, correctly). But confusion is not a reliable *sign*: overload and extraneous load also feel confusing (M16). Check learning with a delayed retrieval test, not a feeling (RT11). | captions |
| J27 *(new)* | "Some research says" more active recall/spaced repetition makes high achievers *worse* | **unsupported** | No source given; none found. Expertise reversal is real for *worked examples and guidance* (KACS03), not shown for retrieval practice. | captions (JS-PRB) |
| J28 *(new)* | After one week without retrieval you forget ~50–60% of a fact | **partly** | Steep early forgetting is replicated (MD15, Ebbinghaus savings, N = 1, nonsense syllables). Exact percentages depend on material, learning level and test; one number is not a law (M23). | captions (JS-PRB) |

---

## 5. Overall verdict on Justin Sung (feeds B5 §1)

- **What's sound:** studying ≠ learning (J1); relate and organize instead of transcribing (J9,
  J11 as normally used, J12); rereading/highlighting low (J18); spacing and sleep high (J15, J16);
  higher-order *practice* for higher-order exams (J23 core, Ag19); effortful ≠ ineffective (KGF19).
  These are mainstream findings, presented well.
- **What over-reaches:** "retrieval only fights forgetting" (J4 — withdrawn by him); effort or
  confusion as a reliable signal (J3, J26); trainable load capacity (J25); start-at-the-top
  (J23 beyond Ag19); "research shows AR/SR hurts high achievers" (J27, no source).
- **What can't be checked:** his own outcome data (J24) and the effect of his specific techniques
  — none published; commercial conflict of interest.
- **Grade (for B5):** as a **translator of mainstream findings → M**; for **his own method
  (iCanStudy system) → T** (testimonial, unpublished, COI). He is unusually willing to correct
  himself in public (JS-CO), which raises trust in his framing but is not evidence for the method.

**Engine impact:** none. The audit confirms existing engine rules (retrieval + spacing + relate;
CHECKs gate on delayed retrieval, not feelings). No design change needed.
