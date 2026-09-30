# Site v2 design, session 1: record (2026-09-29 → 30)

> The learner asked to "save this conversation as a transcript or summary of it atleast". The
> learner's messages are quoted **verbatim**, with typos kept, because their exact words are the
> spec. The engine's turns are **summarised**. The resulting design is `../SITE-V2-DRAFT.md`.

---

## Turn 1: learner opens v2

> "alr alr, lets work on site v2, what i want next are 2 seprate things, first is structure and second
> is content. by structure i specifically want to define a few things and maybe u add onto it, and for
> content i mean is that its feeling a little weak as of now, maybe because u just made the demo one
> for digital electronics, but i feel like we can do much better in the terms of how we are just not
> reaching the true potential of it, taking an example for after effects, u could have directly
> explained and pointed out exactly what is where and how it works, how it looks visually which means
> just using a photo to explain but it levels the content up so so much, now that i have picked up
> content lets try refining the engine so that it truely scraps the content and aims for the potential
> i see this has"

### Engine response (summary)

**No build.** The engine followed design-first.

It diagnosed the weak content from the After Effects pack:
1. Every figure is code-drawn line art: 30 functions in `figures.py`. `ui_layout` is a box sketch of
   the AE window, not the window.
2. The deep stage-2 KB was cut down to a table plus a line per card. The "minimal" rule was applied to
   the content as well as the frame.
3. Nothing moves, although AE is about motion.
4. The pipeline never asks "what's the real thing to show?"

It proposed content engine v2:
- annotated real images (`[[shot:]]`, numbered markers);
- an image-scouting research step with sources recorded;
- real tool output (iverilog, ngspice, Python);
- motion figures;
- a 5-point depth bar per card.

It raised licensing as a concern for a public site (this was later overruled by the learner). It
asked for the learner's structure list.

## Turn 2: learner sets images rule + structure concepts

> "dont spend tokens uselessly on re-genrating images that are readly available, we are just using
> basic photos to teach myself and my close friends thats it, stop fearing license and shit, treat this
> as if i am keeping this local and chill out. now structure, i want to add the concept of focus,
> leaf-node-edge-trunk. focus is exactly how it sounds, when learning a concept i want to focus only
> and only on that, the visual weight should only be on that and nothing else. leaf-node-edge-trunk is
> self explainatory, but i want to add that in the tree concept there is a trunk where the entire
> subject revoulves around, there are concepts which actually need u to understand some previous
> concepts, so rather than making them both leaves, u can actually have me start with learning the
> leaves and then converge at a node which will better help me understand the node, so the big
> structural addition i want is to not keep it just diverging but converge as well with whatever is
> needed and better suited, it can be a web because thats how subjects work at times, but obviously a
> teaching flow, like water flowing thru rivers, it converges and diverges wherever suited. discuss
> further dont execute just yet"

### Engine response (summary)

It saved the images rule to memory (`site-images-use-real-photos`).

It restated the idea as a **river**:
- trunk = main river;
- leaf = source;
- node = confluence;
- edge = direction of flow.

So the model changes from a tree to a directed graph.

It proposed focus: zoom into the node, the map disappears, and a thin `from: A · B → [this] → leads
to: C` strip remains.

It pushed back or added:
1. The teaching flow must be acyclic. Flow edges are drawn; relates-to links are hidden.
2. The trunk is chosen, not computed.
3. Chapters could be regions or containers.
4. A full graph is too busy, so show it in progressive layers.
5. Use a layered graph layout (dagre or ELK) with a pinned trunk, flowing top to bottom.
6. "Next" becomes a topological teaching order.

It asked 5 questions: chapters, flow direction, focus strip, web visibility, and anything else on the
structure list.

## Turn 3: learner corrects definitions and answers

> "this is a massive work-load and i dont want half-assed work, divide this in two or more sessions, u
> have captured exactly what i want for focus. for trunk i would say its more of the handful concepts
> that the subject starts with, the base, can be its through line but doesnt have to be, its more of a
> starting chapter of the subject. leaf is just anything that only connects to one thing, it can mean
> it starts from scratch like aphabets, and ends like a fact that isnt needed anywhere else but just
> needs to be remembered as a fact. node is both converging and diverging depending and edge is just
> something that is connecting two concepts, an edge itself can be something aka a paragraph or
> explination that actually connects the two concepts and not just a line showing that a leads to b.
> for chapters we can have chapters dictate mental load, there is only so much i can see and understand
> all at once, so chapters can be the defining factor that breaks the whole huge subject tree into
> different sections for easier digestion. i need u to heavily think 4. because i cannot agree more, i
> would absolutely love layers, that was my initial vision when i tried introducing the concept of a
> tree like map, where the first layer the very first thing u get is a map of what all is there in the
> subject without overwhelming the viewer. we can try different things till we land on the thing i
> like the most. i dont yet know if i want them to visually be strict containers so there is less
> visual weight and viewer can focus only on one thing or if i want them connected so that it
> extablishes better web connection, flow i would like top to bottom, focus is full takeover and strips
> and fine, relates to links be a second thing that pops up so that it doesnt distract and add to the
> visual load, only when i have already done what was being focused on that i move on to conecting it
> to the web"

### Decisions captured

- Focus is confirmed as designed.
- The trunk is the base or starting chapter.
- A leaf has degree 1, as a start or an end.
- A node has degree ≥ 2.
- An **edge is content (a bridge)**.
- A chapter is a **mental-load budget**.
- Flow is **top to bottom**.
- Focus is a **full takeover with the strip**.
- Relates-to links appear **only after the concept is done**.
- **Layers are the core vision.**
- Containers vs connected is **undecided**; try variants.
- The work is split across sessions.

### Engine response (summary)

It proposed the layer model:
- **L0:** chapters only, with summarised edges;
- **L1:** one chapter's graph, one screen by construction;
- **L2:** focus;
- **L3:** the web, unlocked after "done".

Moving between layers is a zoom, not a jump, with a breadcrumb.

For the container question it proposed **ports** as a middle option (small labels on the container's
edge, no crossing lines), to be prototyped against the two extremes.

It raised these risks:
- merging-graph layout is hard (edge crossings);
- chapters must also flow one way;
- chapter cutting is a real design job.

It gave a 5-session plan. It proposed DE as the structure test subject and AE as the content test
subject.

It asked two things: may it write the draft, and which test subject(s).

## Turn 4: learner, automation + write the draft

> "i dont know about my aproval, just use leafs to indroduce concepts and then later on u can make the
> leaf into a node as my understanding broadens for deciding where the chapter split, i want no work
> from my side when i need to study, just dropping the material and thats it, i want automation,
> obviously write the draft.md now, this is the the session where all the juicy context is, write down
> as much context as u can, maybe even save this conversation as a transcript or summry of it atleast"

### Decisions captured

- **No learner approval step** for chapter cuts. Fully automatic.
- **Progressive growth:** a concept is introduced as a leaf and becomes a node as understanding widens
  (edges light up as their ends are done). This is `SITE-V2-DRAFT.md` §2.1.
- **Automation target:** the learner drops material, and everything else happens on its own
  (`SITE-V2-DRAFT.md` §7).

### Engine response

- Wrote `site/SITE-V2-DRAFT.md` and this record.
- Updated memory.
- The test-subject question is still open. It is listed in the draft §12.

---

## Next session (session 2) starts here

1. Re-read `site/SITE-V2-DRAFT.md` and this record.
2. Confirm the test subject(s) with the learner (proposed: DE for structure, AE for content).
3. Build **throwaway prototypes** of L0 and L1 variants (draft §3.1) on real data, at desktop and
   390px. Show them side by side. The learner picks.
4. Nothing in `site/build.py` or `site/static/` changes until the learner picks a variant.
