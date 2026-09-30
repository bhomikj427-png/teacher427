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
