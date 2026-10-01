# Study site — v2 design DRAFT (not built, not frozen)

> **Status: DRAFT, design phase.** Nothing here is implemented. Written 2026-09-29/30 at the end of v2
> design session 1, where the learner set the direction. `SITE-V1.md` is still the live, built format
> until this draft is prototyped, built and frozen as `SITE-V2.md`.
>
> **Why this file is long:** session 1 holds context that would otherwise be lost. The learner asked
> for "as much context as u can". The verbatim record of that session is in
> [`v2-design/2026-09-29-session-1-record.md`](v2-design/2026-09-29-session-1-record.md). Read it
> before changing this draft. Where this draft and the learner's own words disagree, **the learner's
> words win.**
>
> **Rules for working on it** (learner, 2026-09-29):
> - "this is a massive work-load and i dont want half-assed work, divide this in two or more sessions."
> - Design first, build after sign-off ([[design-first-no-premature-build]]).
> - Each session below ends with something the learner can judge.

---

## 0. The two workstreams

v2 has two separate parts, as the learner framed them:

1. **Structure:** how a subject is shaped and navigated. Covered by §1 to §7.
2. **Content:** what each concept card actually carries, and the engine that produces it. Covered by §8.
   - The learner's diagnosis: the content "is feeling a little weak … we are just not reaching the true
     potential of it".
   - Their example: for After Effects "u could have directly explained and pointed out exactly what is
     where and how it works, how it looks visually … just using a photo … levels the content up so so
     much".

Both parts serve one goal the learner stated: **"i want no work from my side when i need to study,
just dropping the material and thats it, i want automation"**. See §7.

---

## 1. From a tree to a river

v1 is a **tree**: it only ever splits (fans and spines). v2 is a **flowing graph**, and it converges
as well as diverges.

> "the big structural addition i want is to not keep it just diverging but converge as well with
> whatever is needed and better suited, it can be a web because thats how subjects work at times, but
> obviously a teaching flow, like water flowing thru rivers, it converges and diverges wherever
> suited."

- **Flow is top to bottom** (learner-chosen). The base is at the top and everything flows down out of
  it. On a phone this becomes a vertical stream with no change of axis.
- **The teaching flow cannot loop.** Subjects are webs, but a teaching order has to go one way. So
  there are two kinds of link:
  - **Flow edges:** directed and drawn. They set the teaching order. The build refuses any cycle in
    them.
  - **Relates-to links:** capture the web. They are never on the map. They appear only in the web
    layer (L3), and only after the concept is done (§3).

## 2. Vocabulary (learner-defined; these are the definitions)

| Term | Definition (learner's, 2026-09-29) | Engine meaning |
|---|---|---|
| **Trunk** | "more of the handful concepts that the subject starts with, the base, can be its through line but doesnt have to be, its more of a starting chapter of the subject." | The **base chapter**. It sits at the **top** of the flow. The engine chooses it as the smallest self-contained starting set (§6). |
| **Leaf** | "just anything that only connects to one thing, it can mean it starts from scratch like alphabets, and ends like a fact that isnt needed anywhere else but just needs to be remembered as a fact." | A concept with **degree 1**. It is a **starting leaf** (feeds one thing, needs nothing) or an **ending leaf** (fed by one thing, feeds nothing: a fact to memorise). The engine classifies these automatically from the edges. |
| **Node** | "both converging and diverging depending" | A concept with **degree ≥ 2**. It converges (several in), diverges (several out) or both. |
| **Edge** | "just something that is connecting two concepts, an edge itself can be something aka a paragraph or explination that actually connects the two concepts and not just a line showing that a leads to b." | A **first-class piece of content**: a short **bridge** explaining *how/why A leads to B*. It can also hold a **prediction prompt** ("you know A, so what must B be?") that is answered before B is opened. See §4. |
| **Chapter** | "chapters can be the defining factor that breaks the whole huge subject tree into different sections for easier digestion … there is only so much i can see and understand all at once" | A **cognitive-load budget**, not a textbook boundary. It holds as much as can be taken in at once. The engine cuts chapters automatically (§6). Textbook chapters are only hints. |

### 2.1 Progressive growth: leaves become nodes (learner, 2026-09-30)

> "just use leafs to introduce concepts and then later on u can make the leaf into a node as my
> understanding broadens"

- The graph is **not static.** It is shown relative to what the learner has already done.
- **When a concept is introduced**, it appears as a **leaf**: one connection, the one it needs right
  now. Its other connections are hidden. The new thing arrives with the least possible load
  (principle 3, one new element at a time).
- **As later concepts get done**, the edges already in the data light up, one by one. The concept gains
  connections and becomes a **node**. Understanding widens, and the map widens with it.
- **Engine rule:** a flow edge is *visible* only when both of its ends are unlocked. A concept's
  *visible degree* grows over time. "Leaf" and "node" are therefore **state-dependent labels on the
  visible graph**. The full graph always exists in the data.
- **Link to L3 (§3):** relates-to links are the last stage of this growth. They surface only after the
  concept is done.
- **Evidence:**
  - introduce with low element interactivity, add connections later (`research/01 §2`, cognitive
    load);
  - connections to prior knowledge get re-surfaced across time, so each lit-up edge is a spaced
    re-encounter of both of its ends (`research/02 §2`);
  - block first, then interleave (`research/02 §6`).

## 3. Layers (semantic zoom): the core of v2

> "i would absolutely love layers, that was my initial vision when i tried introducing the concept of a
> tree like map, where the first layer the very first thing u get is a map of what all is there in the
> subject without overwhelming the viewer. we can try different things till we land on the thing i
> like the most."

This is **one map shown at several depths.** Each layer shows a *different kind of thing*, not a
bigger picture of the same thing.

| Layer | Shows | Answers | Load cap |
|---|---|---|---|
| **L0: subject** | **Chapters only**, no concepts. The trunk chapter is at the top and the rest flow down. Chapter-to-chapter edges are **summarised**: if anything in chapter X feeds anything in chapter Y, one line joins X and Y. Each block shows a title, a small concept count and progress. | "What is in this subject?" | roughly 6 to 12 blocks; readable without scrolling |
| **L1: chapter** | That chapter's concepts as a small graph, top to bottom: starting leaves at the top, converging into nodes, diverging to ending leaves. Concepts not yet unlocked are shown per §2.1. | "What is in this part, and how does it build?" | fits on one screen, **by construction** (the chapter-size cap, §6) |
| **L2: focus** | **One concept, full takeover.** Nothing else on screen except a thin strip: `from: A · B → [this] → leads to: C`. Tapping an item in the strip opens that **edge's bridge text** (§4). | "What is this, exactly?" | one concept |
| **L3: web** | That concept's **relates-to** links across the subject. It **unlocks only after the concept is done.** | "How does this connect to everything else?" | shown on request, never by default |

**Focus (learner, 2026-09-29):** "when learning a concept i want to focus only and only on that, the
visual weight should only be on that and nothing else." They confirmed the design: *"u have captured
exactly what i want for focus … focus is full takeover and strips and fine"*.

**Web (learner, 2026-09-29):** "relates to links be a second thing that pops up so that it doesnt
distract and add to the visual load, only when i have already done what was being focused on that i
move on to conecting it to the web". This is the evidenced order: block first, then interleave
(`research/02 §6`).

**Moving between layers:**
- It is a **zoom, not a jump.** A chapter block *grows into* its interior, and a concept node grows
  into the focus view. Where things sit in space stays continuous, so the learner always knows where
  they are.
- There is always a breadcrumb: `subject › chapter › concept`.
- **Esc** or **Back** goes up one layer. **← / →** walk the teaching order while in focus.
- **URLs** (extending v1's routes):
  - `''` → L0
  - `#/ch/<id>` → L1
  - `#/c/<ch>/<concept>` → L2
  - `#/c/<ch>/<concept>/web` → L3

**What counts as "done"** (it gates L3 and the §2.1 growth): the concept's quick check has been
revealed *and* the learner has pressed "done". It is stored per viewer (localStorage, as with v1's
"seen"). **Honest limit:** this is a navigation state, not a mastery record. Mastery still comes only
from the tutor's retrieval checks and the progress logs (principle 5).

### 3.1 The open question: containers vs connected (prototype it, don't argue it)

The learner has **not decided**: "i dont yet know if i want them to visually be strict containers so
there is less visual weight and viewer can focus only on one thing or if i want them connected so that
it extablishes better web connection".

Session 2 prototypes three variants **side by side, on real data**:

1. **Strict container:** L1 shows only this chapter. No sign of the outside at all.
2. **Container with ports** (the engine's candidate): the chapter is a strict container, but links to
   other chapters show as small **port labels** on its edge:
   - at the top, `← from Ch 1: truth table`;
   - at the bottom, `feeds Ch 4 →`.

   No lines cross the page. Clicking a port goes across. The web is present at near-zero visual
   weight.
3. **Connected in place:** L1 expands *inside* L0, and neighbouring chapters stay visible, dimmed, with
   real edges running into them.

The learner picks by looking at them. The choice may differ between desktop and phone.

L0 variants to try as well:
- **(a)** chapter blocks with summarised edges (river);
- **(b)** a metro-map style, where lines are threads of the subject and stations are chapters;
- **(c)** horizontal strata, one band per chapter, with thin connectors.

## 4. Edges as content: bridges

An edge between A and B carries:
- **`bridge`**: 1 to 4 sentences on *how A becomes or enables B*. This is the explanation the learner
  asked for ("a paragraph or explination that actually connects the two concepts").
- **`predict`** (optional): a question asked *before* B opens: "Given A, what do you expect B to
  be/do?" Wrong guesses help (`research/02 §1, §5`, pretesting). It is answered by opening B.
- **`kind`** (optional): `needs` (hard prerequisite), `generalises`, `special-case`, `contrasts`,
  `applies`.

Where bridges surface:
- **L2 focus:** tap an item in the from/to strip.
- **L1:** hover or tap an edge (a light preview only).
- **Walking the teaching order:** crossing an edge can show its `predict` first. This is test-first
  built into navigation (principle 1).

**Evidence:** explaining *why* one idea leads to another is self-explanation and elaborative
interrogation (`research/02 §4`). Bridges make the connection itself something you actively learn.

## 5. Teaching order on a graph

- "Next" means the next item in a **valid teaching order** (a topological order):
  - the trunk first;
  - within a chapter, starting leaves first;
  - a node only after everything that feeds it;
  - among concepts that are ready at the same time, the more exam-relevant one first (scoring before
    depth, CLAUDE.md sourcing rules).
- The engine computes the order. Nobody writes it by hand.
- If a concept is opened out of order (for example from a bookmark), focus shows `needs first: X, Y`
  as links. It never blocks the learner.

## 6. Automatic chapter cutting and trunk choice (no learner approval step)

> "for deciding where the chapter split, i want no work from my side when i need to study"

The engine cuts chapters itself. The learner does not approve cuts. The algorithm:

1. **Build the full concept graph** from the knowledge base: concepts plus flow edges, taken from the
   KB's own prerequisites and concept map.
2. **Trunk** = the smallest set of top-of-flow concepts (nothing feeds them) that most of the rest of
   the graph depends on, capped at one chapter's load. It becomes chapter 1.
3. **Cut the rest into chapters** by walking the topological order and closing a chapter when either
   of these is true:
   - it reaches the **load cap**;
   - a natural seam appears (few edges cross it).

   Cuts minimise the number of edges crossing chapter boundaries. Textbook and professor chapter
   breaks act as tie-breakers so the site still maps onto the syllabus.
4. **Load cap:** a starting value of about 7 concepts per chapter, and never more than one screen at
   L1. It is tunable. (The number is a design parameter, not an evidence claim. The principle is
   `research/01 §2`: working memory is small, so chunk.)
5. **Hard guards** (the build refuses if any fail):
   - the chapter graph must itself flow one way (if chapter X needs Y then Y cannot need X);
   - there are no flow-edge cycles;
   - every concept sits in exactly one chapter;
   - every edge has a bridge;
   - every chapter is within the cap.
6. **Tangled layout is a smell.** If a chapter's graph cannot be laid out without heavy edge crossing,
   the engine re-cuts it rather than shipping a tangle.

The learner can still override any of this, but nothing waits on them.

## 7. Automation: "drop the material and that's it"

The target pipeline. It builds on the existing `_inbox/` triage and research engine:

```
learner drops material (PDF / slides / PYQs / notes / screenshots) into _inbox/
  → triage routes it to the subject (existing)
  → research engine brings KB to stage-2✓ (existing; teaching gate unchanged)
  → GRAPH EXTRACTION: concepts + flow edges + bridges + relates-to links
  → AUTO-CHAPTERING + trunk (§6)
  → CONTENT ENGINE v2 per concept (§8): real images, generated plots/sim output, card text
  → VERIFY (machine checks: answers, K-maps, sim results) + build guards
  → BUILD → site ready; progress log records it (log-first rule)
```

- **The learner's only job:** drop material, then study.
- **Late material** follows the existing rule: it re-scopes, it doesn't re-teach. A re-run updates the
  graph, and cuts are kept as stable as possible so the map doesn't reshuffle under the learner. Stable
  concept ids make this possible.

## 8. Content engine v2

### 8.1 Real images first (learner rule, 2026-09-29)

> "dont spend tokens uselessly on re-genrating images that are readly available, we are just using
> basic photos to teach myself and my close friends thats it, stop fearing license and shit, treat this
> as if i am keeping this local and chill out."

- **If a real photo or screenshot exists, download it.** Don't redraw it as code-drawn SVG. Note the
  source in a line, with no licence commentary. The audience is the learner and close friends.
- **Annotated real images** become the core block, `[[shot:…]]`:
  - a real screenshot or photo with **numbered markers** overlaid at x/y positions;
  - hover or tap a marker to see "this is X, it does Y";
  - an optional "click here → this happens" before/after pair.

  This is the "point out exactly what is where" block.
- **Image scouting is a research step.** For every concept, the engine asks what the real thing to
  show is, and fetches it into the pack's `img/` folder with its source recorded in `images.json`.
- **Generated figures stay only for computed things:** plots, waveforms, K-maps, curves. These are
  faithful by construction.

### 8.2 Real output from real tools

Instead of drawing what a tool *would* show, the engine runs the tool:
- `iverilog` / GTKWave-style traces for Verilog timing;
- `ngspice` for circuit responses;
- Python for DSP and signals.

What the learner sees on the card is what they will see in the lab.

### 8.3 Motion where the subject is motion

Short animated figures, generated from the same maths. Example: a dot easing along a path next to its
speed graph. The main use is After Effects (ease and interpolation), but the idea is general: any
time-varying concept.

### 8.4 The depth bar: a card ships only if it answers

1. **What it looks like** (a real image where one exists).
2. **Where it is** (location in the UI, the circuit, the system).
3. **How it works** (the mechanism figure plus text).
4. **What right vs wrong looks like** (the result, the common failure, the trap).
5. **Why it matters** (what it feeds downstream, or its exam angle).

Retrieval stays built into every card (it is inherited from v1 §5): a warm-up per chapter, a quick
check behind a reveal, "try it first" on worked examples.

**The diagnosis behind §8** (session 1):
- v1 AE figures are all code-drawn line art (for example `ui_layout` is a box sketch of the AE window,
  not the window);
- the cards distilled a deep stage-2 KB down to a table plus a line, because v1's "minimal" rule was
  applied to the *content* when it should only apply to the *frame*;
- nothing moves;
- the pipeline never asks what the real thing to show is.

**v2 principle:** the frame is minimal and the content is rich.

## 9. What v2 keeps from v1

- The guiding balance: "clean yet … efficient in … conveying information yet not overwhelming, that
  sweet balance". **The balance is the key.**
- The minimal visual language (§4 of v1): hairlines, whitespace, Inter + JetBrains Mono, colour only
  where it carries meaning, and none of the rejected v0.2 "tacky" elements.
- One concept at a time. Hash routes. Esc/Back step out one level. The phone layout. Light and dark.
- Figure-first cards, retrieval built in, "seen/done" as navigation only, Unicode symbols (no TeX).

**What v2 replaces:**
- groups, fans and spines as *authored* structure (they are now derived from edges);
- `needs` as a hover-only side channel (edges are now first-class);
- hand-authored chapter trees (chapters are now auto-cut);
- code-drawn pictures of real things.

## 10. Data model (proposed)

Per subject, in `study-pack/web/`:

```
meta.json          slug, title, line/exam (unchanged)
graph.json         concepts: [{id, title, kind, gist}]
                   edges:    [{from, to, kind, bridge, predict?}]      # flow, acyclic
                   relates:  [{a, b, note}]                             # web layer only
chapters.json      GENERATED by the auto-cutter: [{id, title, concepts[], trunk?:bool}]
                   (committed so cuts are stable across re-runs; regenerated on material change)
content/<concept-id>.md   one file per concept, depth-bar sections, [[shot:]] / [[fig:]] blocks
images.json        {name: {file, source, markers:[{n, x, y, label, text}]}}
img/               downloaded images
figures.py / verify.py    generated figures + machine checks (unchanged role)
```

- `leaf` and `node` are **never stored**. They are computed from the visible degree (§2.1).
- `order` (the teaching order) is computed at build time.

## 11. Session plan

| # | Deliverable | Learner judges |
|---|---|---|
| **1** ✓ | This draft plus the session record (2026-09-29/30) | the direction (given in-session) |
| **2** ✓ built, then reworked | Throwaway prototypes. The first round (§13) was rejected; the rework is "the river" (§14). | river picks (**pending**) |
| **3** | **Real build:** graph data model, auto-chaptering, bridges, focus (L2), zoom transitions, §2.1 growth; migrate the test subject | the working site |
| **4** | **Content engine v2** (§8) on the content test subject: real images with markers, tool output, depth bar | content quality ("does it reach the potential?") |
| **5** | L3 web layer, the full "drop material" automation (§7), move other subjects over; freeze as `SITE-V2.md` + tag `site-v2` | freeze |

**Test subjects (proposed, not yet confirmed):**
- **Digital Electronics** for structure (sessions 2–3), because it has real multi-input convergence
  (K-maps and minimisation);
- **After Effects** for content (session 4), because it gains the most from real screenshots.

## 12. Open questions carried forward

1. Containers vs ports vs connected (§3.1): decided by prototype in session 2.
2. L0 visual metaphor (river blocks / metro / strata): decided by prototype in session 2.
3. Test-subject split (DE for structure, AE for content): not yet confirmed by the learner.
4. Load-cap number (starting at about 7 concepts per chapter): tune once real chapters are on screen.
5. How graph extraction from the KB is made reliable enough to need no learner input. Probably:
   - KB concept files carry explicit prerequisites;
   - the extractor proposes bridges;
   - the verify step checks for cycles and orphans.

   Design this in session 3.
6. Deployment: the learner said "treat this as if i am keeping this local". Public Pages deploy is no
   longer a goal. Local build first, and share with friends however is easiest (decide later).

## 13. Session 2 results (2026-09-30; built, awaiting the learner's picks)

Everything is in `v2-design/prototypes/`. Start at `compare.html`. The record is
`v2-design/2026-09-30-session-2-record.md`.

**What exists:**
- The whole of Digital Electronics as a v2 graph: 117 concepts, 188 bridged flow edges (30 with predict-first), 18
  relates-to links.
- The automatic chapter cutter (§6), working: 17 chapters of 5–9 concepts; 85/188 edges cross chapter boundaries.
- Live L0–L3 prototypes, and a self-test (576 renders, 0 errors).

**How §6 is implemented (prototype):**
1. Validate.
2. Build a topological order that keeps each KB topic together. It takes topics in **syllabus unit order**, then
   shallowest first. This signal is needed because edges alone would put U5 logic families at chapter 3, while the
   KB says they go last on purpose.
3. Run a DP split, minimising edges that cross chapters plus a penalty for mixing topics, with chapter size in
   [5, 9].
4. Refine with single-concept moves.
5. Name each chapter from its dominant topics, disambiguating repeats by the hub concept.

**Design changes that came out of building:**
- **§2.1, ghost edges.** Growth must not *hide* not-yet edges: an unstarted chapter became shapeless dots. Not-yet
  edges are now faint dotted ghosts and turn solid when earned.
- **§3.1 variant 2, rails replace port nodes.** Ports laid out as graph nodes sprawled dashed lines across the page.
  Now:
  - a "comes from" tag rail sits above the chapter graph and a "leads to" rail below;
  - a small stub marks each concept with an outside link;
  - hovering a tag lights up its concepts. No crossing lines.

**Open problems found** (listed in `compare.html`):
- On a phone, the L1 graph scales down to about 70%. A phone-specific chapter layout may be needed.
- River L0 does not work on a phone.
- 17 chapters exceeds the 6–12 hoped for at L0 (the floor is ⌈117/9⌉ = 13). Options: accept it, or show stages first.
- The auto chapter names are clunky.
- The phone focus strip is one sideways-scrolling line.

**Engine's picks** (the learner decides):
- L0: river on desktop, strata on a phone;
- L1: ports (rails);
- growth: on, with ghosts.

## 14. Session 2 rework: the river (2026-09-30; built, awaiting the learner's picks)

The learner rejected §13's L0: "this is the web and not what i wanted, this would suit L3 better … its just too much
same problem as v1". The verbatim feedback is in `v2-design/2026-09-30-session-2-record.md`. **This section
supersedes §3's layer table, §3.1 and §13 wherever they disagree.**

**The river interaction (L0 and L1 share it; L1 is "the same flow as L0, just applied on a chapter"):**
- The page **waits for input**: a bobbing ▾, a dotted ghost of the next stop, and water trickling toward it.
- Each input (space, ↓, a tap, or scroll in variant C) lets the water flow on to the next stop, which pops in with its
  **priming card**.
- Only the stops you have reached are shown. Past stops shrink to dots; older links fade.
- **Visual-load budget:** one card and at most 6 map labels at a time. The self-test enforces it (the maximum
  measured is 3).
- "See it all" is available, but only when you ask for it.
- **Staircase rule** (learner, 2026-10-01: "for every map i feel very lost"):
  - On every map, each stop sits strictly lower than the one before it in teaching order: y = max(layout y,
    previous stop's y + step).
  - Reading top to bottom is the numbered order; no two stops share a row.
  - Sideways position still shows the river's branches.

**Priming (the learner's word).** Evidenced as pretraining (Mayer: names and characteristics first; 13 of 16 tests,
with a likely inflated median effect), advance organizers (modest), and pretesting (`research/02 §5`, strong). A stop
shows:
- its heading;
- then either at most 3 key terms with short glosses (default), or one sentence, or a guess question with the words
  revealed on a tap.

**To do:** add pretraining and advance organizers to `research/` properly before citing them as the engine's evidence.

**Concept kinds** (the learner: "3 kinds or even more … take initiative"). Five kinds, each with a study verb:
- Logic · work it out;
- Memorise · remember it;
- Method · do it;
- Circuit · draw it;
- Trap · avoid it.

**Colour modes:** kind (default) / topic (unit) / role (trunk, node, leaf, edge, grown per §2.1) / layer.

**L2 = a sprint.**
- The from/to strip is **removed**. Only the content and an exit are on screen ("the focus only exists to be a
  sprint").
- The concept is broken into the simplest steps: guess → idea → each figure → each point → check → done.
- Connecting it to other concepts belongs to L3.

**L3 = the web.** It is the full L0 chapter map, plus the concept's cross-chapter links and relates-to links, revealed
one per input. Edges are content, so each link has its own **link sprint**: the two ends → guess → bridge → done.
Two variants, to be picked:
- **merged:** the link sprints live inside L3;
- **split:** L3 is visual only, and L4 explains.

**Prototype:**
- `v2-design/prototypes/river.html`: live, with a ⚙ panel for every variant;
- `v2-design/prototypes/compare-river.html`: the decision page;
- `v2-design/prototypes/priming.py`: stand-in for the automatic kind and priming step;
- `v2-design/prototypes/build_river.py`: the data build.

**Engine's picks:**
- L0 A (step river);
- priming: 3 terms at L0, guess first at L1 where a sourced predict question exists;
- colour: kind, with role as a toggle;
- L3 merged;
- sprint dots on.

**Open problems:**
- In variant A, the wide middle of the DE graph causes some stream crossings (a custom main-channel layout is a
  session-3 item).
- Kinds and priming are hand-written stand-ins.
- Sprints have real content for 9 concepts only.
- L3 is at chapter level on purpose: all 117 concepts on one screen would be overload.
- On a phone, "see it all" shows numbers only.
