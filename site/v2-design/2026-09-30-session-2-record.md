# Site v2 design, session 2: record (2026-09-30)

> This file is written live, in order, as events happen (the no-drift rule). The learner's words are verbatim.
> Deliverable: `prototypes/compare.html`.

## Opening

- The learner asked: "start up, do session one or is it already done?" Answer: session 1 was done and pushed (commit
  9aa2397). The engine proposed DE for structure and AE for content, and asked for "go".
- The learner said: **"do session 2, get to work and dont slack off, i want this as good as i am visioning it to be"**.
  This was taken as a go on the proposed plan: Digital Electronics is the structure test subject.

## Events (in order)

1. **Read the DE knowledge base** (`00-map.md`, `01`, `03`, plus the section headings of `02`/`04`/`05`) and the v1
   site code (`build.py`, `static/*`).
2. **Built the DE concept graph**: `prototypes/de_graph.py`.
   - 117 concepts: the number-system and gate prerequisites plus units U1–U5.
   - 188 flow edges, each with a bridge sentence; 30 of them carry a predict-first question.
   - 18 relates-to links.
   - Every bridge was written from the KB mechanisms. The engine spot-checked the numeric and formula ones:
     f_max 23 ns, 3-bit Johnson = 6 states, 8-bit barrel = 3 stages, ring oscillator 1/(2N·t_pd), TTL NM 0.4 V,
     BCD 0111+0110.
3. **Auto-cutter v1** (greedy growth + affinity). The result was rejected by the engine itself:
   - 80/188 crossing edges;
   - chapter 1 mixed timing and logic-family levels into the trunk;
   - the last chapter had only 3 concepts.
4. **Auto-cutter v2**: a topic-coherent topological order followed by an optimal DP split. The result was better,
   but logic families landed at chapter 3, because their only prerequisite is the gates.
5. **Auto-cutter v3**: the syllabus unit order was added as the topic-switch key. The KB says U5 comes last on
   purpose (`00-map.md`), and the edges can't express that. Result:
   - 17 chapters, sizes 5–9, 85 crossing edges;
   - the order mirrors the syllabus;
   - duplicate names are disambiguated by the chapter's hub concept.
6. **Built the prototype**: `proto.html`, `proto.css`, `proto.js`, with dagre 1.1.4 vendored. It has:
   - L0 in three variants (river / lanes / strata);
   - L1 in three variants (strict / ports / connected);
   - L2 focus (strip, bridge popovers, predict-first, mark done, prev/next in teaching order);
   - L3 web panel (locked until done);
   - the growth rule (§2.1);
   - prototype controls and a progress slider.
7. **Screenshot pass 1 found and fixed:**
   - a CSS class clash with v1 `style.css` (`.bar span`, `.pn`);
   - labels overflowing their boxes;
   - the trunk tag overlapping the title;
   - river stage clusters producing a chaotic layout (switched to a plain DAG with a colour legend).
8. **Design finding 1:** with growth on, **hiding** not-yet edges left an unstarted chapter as scattered dots with no
   shape. Changed to **ghost edges** (faint dotted lines): the shape stays visible and turns solid as it's earned.
9. **Design finding 2:** the first version of the ports variant laid out the ports as graph nodes, and their dashed
   lines sprawled across the page. Redesigned as **rails**:
   - a "comes from" row of tags above the graph and a "leads to" row below;
   - a tiny stub on each concept that connects outside;
   - hover a tag and the concepts it feeds light up. No crossing lines.
10. **Headless Chrome won't lay out below ~500px**, so the first phone shots were wrong. Built `phone.html` (a 390px
    iframe) and `shoot.sh`.
11. **Self-test added** (`?selftest=1`): every layer × variant × chapter × concept, with growth on and off, plus data
    checks (order topological, every concept once). Result: **PASS, 576 renders, 0 errors**. Re-run after later
    fixes: PASS.
12. **Phone fixes:** the breadcrumb now keeps chapter › concept; the focus strip is one line that scrolls sideways.
13. **Wrote `prototypes/compare.html`**:
    - the decision page: 25 screenshots, pros and cons, the engine's picks, live links;
    - five openly listed problems:
      - L1 graph shrinks on a phone;
      - river unusable on a phone;
      - 17 chapters vs the 6–12 hoped for;
      - clunky auto-names;
      - the phone strip.

## Engine recommendations (in compare.html, pending the learner)

- **L0:** river on desktop and strata on a phone. Lanes is the compromise if one format everywhere is preferred.
- **L1:** container + ports (rails).
- **Growth:** on, with ghosts.

## Waiting on the learner

These are the picks listed in `compare.html`: L0, L1, growth, and what to do about the 17 chapters. Session 3 (the
real build) starts only after the learner picks.

## Session 2 rework (2026-09-30, later): the learner rejects L0

- The learner reviewed the prototypes and rejected them, verbatim:
  > "sooo no, session 2 needs quite alot of work, this is not at all what i want, lets start from L0, this is the
  > web and not what i wanted, this would suit L3 better, L0 needs visual direction, and this is a mess, maybe
  > because its just too much, i like river the best and is exactly what i am hoping for but its just too much
  > same problem as v1, how about adding animations, showing the flow and letting the viewer control the flow,
  > what i mean literally is that maybe some indication that the page is waiting for an input and that input lets
  > them see the next connections and next stops, i want some actually info being dropped in L0, look up
  > priming, thats what i want for this, the headings of every topic that make me guess or atleast fimilarise me
  > to the words and topics thru just one small sentance at max or at max to max a small list, the bubbles-like
  > structure being connected is fine, u can color code the topics and connections as well, color coding them on
  > the basis of what they are, logical concepts or just concepts that need to be remembered, color coding layers
  > is fine too i dont mind that but i would like to try everything"
- Decisions captured:
  - The current all-chapters, all-edges L0 is really the **web**. It moves to L3.
  - L0 keeps the river metaphor but is too dense.
  - L0 flow is **animated and controlled by the viewer**. The page shows it is waiting for input, and each input
    reveals the next connections and stops.
  - L0 **primes**: every stop shows its heading plus one sentence at most, or a small list at most.
  - Connected bubbles are fine.
  - Colour coding: by concept kind (logical vs to-be-remembered), by topic, and by layer. Try all of them.
- Research lookup on "priming". Folk "priming" is not the evidenced mechanism. The replicated forms are:
  - Mayer's **pretraining principle**: teach names and characteristics of the key components first. It was
    supported in 13 of 16 tests, with a median d ≈ 0.75. Magnitude is likely inflated (`research/07`).
  - **Advance organizers** (Ausubel): a modest positive effect.
  - **Pretesting** (`research/02 §5`, strong).
  - **Segmenting** (learner-paced chunks, `research/02 §9`) backs the idea that the viewer controls the flow.
- Status: the engine proposed an L0 redesign and is waiting for the learner's go. No build yet.

## The learner gives the go, and extends the redesign to every layer

- Verbatim:
  > "oh absolutely 3 kinds or even more if u feel its going to be usefull, take initiative in that sense, add
  > always, i am not perfect in any sense and u might just complete my weak areas and make this project reach its
  > true potential, so dont slack off, i want L1 to follow the same flow as L0, just applied on a chapter, thats
  > the entire point of even having them in layers, man i am going to need u to really think about visual load on
  > every step, it should never be overwhelming, or my efforts and time making this is useless, for focus i want
  > even more isolation, i only want the content to be seen and some way to get out of focus, what i mean is in L2
  > the strip on the top to be removed, the focus only exists to be a sprint, think about time effeciency and just
  > breaking that one concept into the simplest possible steps and finishing it since connecting it with other
  > concepts is L3, now L3 can be the full map of L0 but then adding the nodes that make it into a web and
  > explaining why since the edges are concepts themselves, so either we can have L3 be only visual and add a L4
  > that is explaining the edges or we can have L3 have both visual and edge focus sprints. color coding add a 4th
  > one where its color coded by what it is, an edge node trunk or leaf"
- Decisions:
  - **Go** on the L0 plan (step / unit-first / scroll river variants, priming stops, colour toggles).
  - **Concept kinds:** three or more; the engine chooses. The engine may add things on its own initiative
    ("add always").
  - **L1 uses the same river flow as L0,** applied inside one chapter.
  - **Visual load is the top constraint** at every step.
  - **L2 focus becomes a sprint:**
    - the strip is removed; only the content and an exit remain;
    - the concept is broken into the simplest steps.
  - **L3** is the full L0 map plus the web links, with the edges explained. Two options, to be prototyped:
    - L3 visual only, plus a separate L4 for edge sprints;
    - L3 holding both the visual and the edge sprints.
  - **A fourth colour mode:** by structural role (trunk / node / leaf / edge).

## Rework build events (in order)

1. **Concept kinds and priming** (`prototypes/priming.py`). This is a hand-written stand-in for the automatic step.
   - The engine chose **5 kinds**, each with a study verb:
     - Logic · work it out (22);
     - Memorise · remember it (17);
     - Method · do it (35);
     - Circuit · draw it (40);
     - Trap · avoid it (3).
   - Every one of the 17 chapters and the 6 syllabus units got:
     - a heading;
     - a guess question;
     - one sentence;
     - at most 3 key terms with short glosses.
   - Chapter headings replaced the clunky auto-names.
2. **Data build**: `prototypes/build_river.py` → `out/river-data.js`. Guards: every concept has a kind, the priming
   keys match the auto-cut, and no stop has more than 3 terms.
3. **One river engine for L0 and L1** (`river.html`, `river.css`, `river.js`). Only reached stops are shown:
   - the current stop is a big bubble with a pulse;
   - past stops shrink to dots, filled if done and hollow if not;
   - the next stop is a dotted ghost, with water trickling toward it.
   Each input (space, ↓ or a tap) draws the water into the next stop and pops the stop in. The camera follows, and the
   priming card sits beside the current stop. Links older than 2 steps fade to 16%.
   - L0 comes in three variants: A step river (17 chapters), B units first (6 units, each listing its chapters as
     buttons), C scroll river.
   - L1 uses the same engine inside a chapter, plus dotted **tributaries** for prerequisites from other chapters.
4. **L2 sprint**: a full takeover, with no top bar and no strip. Only the content and an × (Esc) are on screen.
   - Steps: guess (from a real predict question, if one exists) → the idea → each figure → each text block → check
     (answer, then reveal) → done.
   - Done marks the concept, and the river returns one stop further on.
   - Real content exists only for the 9 v1 K-map cards; the rest show a session-4 note.
5. **L3 web**: the full chapter map as faint dots. The concept's cross-chapter needs/feeds links and its relates-to
   links are revealed one per input. `#/web` shows all 18 relates-to links.
   - Two variants for explaining links: **merged** (the link sprint sits inside L3) and **split** (L3 is visual only,
     and an L4 link sprint explains). A link sprint runs: the two ends → guess → bridge → done.
6. **Colour modes** (switch in the ⚙ panel):
   - kind: a ring shows the chapter's kind mix, plus a mix bar in the card;
   - topic, i.e. the syllabus unit;
   - role: trunk / node / leaf / edge, grown from the visible degree (§2.1);
   - layer: a page tint, and the layer badge is always tinted.
   Priming modes: 3 terms / one sentence / guess first.
7. **Screenshot fixes**:
   - v1 `style.css` clashes (`.bar`, `.home`, `main {max-width: 860px}`) were shrinking the map. Renamed and overridden.
   - The river and card were composed as a centred pair so the card sits next to the bubble.
   - Labels were centred under the dots with a halo, alternating below and above along a row.
   - Overview labels are scaled to screen size.
   - On a phone, the overview shows chapter numbers.
   - L3 text keeps a constant screen size.
8. **Self-test** (`river.html?selftest=1`):
   - it covers every L0 variant × colour × priming mode × step; every chapter's L1 walk; every concept's sprint; every
     L3 web in both variants; and link sprints;
   - it adds motion checks (water drawn, the stop pops, the waiting ghost appears);
   - it enforces a **visual-load budget** of at most 6 map labels at once while walking.
   Result: **PASS, 2662 renders, 0 errors, max 3 labels**.
9. **Decision page**: `prototypes/compare-river.html`, built by `make_compare_river.py`. It has 37 screenshots in
   `shots/river/`, pros and cons, 5 honest problems, and the engine's picks:
   - L0: A;
   - priming: 3 terms at L0, guess first at L1 wherever a predict question exists;
   - colour: kind, with role as a toggle;
   - L3: merged;
   - sprint dots: on.
   Waiting on the learner.
10. **Wrap-up (2026-10-01)**: the learner said "wrap up and also open the new demo".
    - The session was committed and pushed.
    - Next session: collect the picks from `compare-river.html`, then session 3 (the real build).
11. **Learner feedback (2026-10-01), verbatim:**
    > "dont hate this, but for every map i feel very lost, i want every node/leaf to be not horizontally aligned but
    > rather atleast very slightly in vertical numerical order, meaning the first leaf/node is going to be slightly
    > vertically up than the next one"
12. **The staircase rule is built** (`river.js` `staircase()`, applied to every map: L0 A/B/C, L1, L3).
    - dagre still sets each stop's x position.
    - In teaching order, each stop's y = max(dagre y, previous stop's y + 44 px). Reading top to bottom is therefore
      always the numbered order.
    - Edges are redrawn as downward curves. They always flow down, because the order is topological.
    - The row-alternating labels are removed: the 44 px step already keeps neighbouring labels apart.
    - ranksep went from 96 to 84 to offset the extra height.
    - The self-test now asserts the staircase on the chapter map. Result: PASS, 2662 renders, 0 errors, max 3 labels.
    - All 37 screenshots were retaken, and `compare-river.html` was regenerated with a note on the staircase.
    - **Draft rule (§14):** on every map, vertical position follows teaching order, strictly.
13. **PARKED (2026-10-01).** The learner said "park this".
    - Site v2 stops here.
    - The river picks in `compare-river.html` are still open.
    - Resume by collecting those picks, then session 3 (the real build).
    - The learner moved on to an engine gap: teaching by everyday examples and analogies.
