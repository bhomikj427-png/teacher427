"""Write compare-river.html: the decision page for the session-2 rework (the river). Reuses compare.html's styles."""
from pathlib import Path

HERE = Path(__file__).resolve().parent
head = (HERE / "compare.html").read_text(encoding="utf-8")
style = head[head.index("<style>"):head.index("</style>") + 8]
extra = """<style>
.film { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px; }
.film.f5 { grid-template-columns: repeat(5, minmax(0, 1fr)); }
.film.f3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
@media (max-width: 900px) { .film, .film.f5, .film.f3 { grid-template-columns: 1fr 1fr; } }
.phones { display: grid; grid-template-columns: repeat(4, minmax(0, 200px)); gap: 10px; }
@media (max-width: 900px) { .phones { grid-template-columns: 1fr 1fr; } }
h3 { font-size: 16px; margin: 22px 0 10px; }
.big-live { display: inline-flex; gap: 10px; flex-wrap: wrap; margin: 10px 0 4px; }
.big-live a { background: var(--ink); color: var(--bg); padding: 9px 16px; border-radius: 999px; font-weight: 600; font-size: 14.5px; }
.big-live a.soft { background: transparent; color: var(--ink); border: 1px solid var(--line); }
.big-live a:hover { text-decoration: none; opacity: .88; }
.dot { display: inline-block; width: 9px; height: 9px; border-radius: 50%; margin-right: 6px; vertical-align: 0; }
code { font: 600 12.5px "JetBrains Mono", monospace; background: var(--soft); padding: 1px 6px; border-radius: 5px; }
</style>"""
R = "river.html?"


def fig(n, cap, live=None):
    link = f' · <a href="{live}">live</a>' if live else ""
    return f'<figure><img src="shots/river/{n}.png" alt="{cap}" loading="lazy"><figcaption>{cap}{link}</figcaption></figure>'


body = f"""
<div class="wrap">
<h1>Site v2 · the river</h1>
<p class="lede">The session 2 rework, built from your feedback. L0 and L1 now use the same river: it waits for your input, and each input lets the water flow on to the next stop. Each stop shows its heading and three key words, nothing more. L2 is a sprint with only the content on screen. L3 is the web, where each link is its own small idea.</p>
<p class="lede"><b>Screenshots can't show the motion.</b> Open the live page and press space (or tap).</p>
<div class="big-live"><a href="river.html">Open the live river (fresh start)</a><a class="soft" href="{R}p=24">…with 24 concepts done</a><a class="soft" href="{R}selftest=1">self-test</a></div>
<p class="q">The ⚙ button (bottom left) switches every variant live: L0 variant, colour mode, priming card, L3 split, motion, progress.</p>

<div class="facts">
<div class="fact"><b>17 · 6</b><span>chapter stops (A) · unit stops (B)</span></div>
<div class="fact"><b>117</b><span>concepts, each tagged with one of 5 kinds</span></div>
<div class="fact"><b>≤ 3</b><span>labels on the map at once while walking (budget 6, checked by the self-test)</span></div>
<div class="fact"><b>1</b><span>caption on screen at a time</span></div>
<div class="fact"><b>PASS</b><span>2662 renders, 0 errors, plus motion checks (water drawn, stop pops, waiting ghost)</span></div>
</div>

<h2><span class="k">ALL</span> One interaction on every layer</h2>
<table>
<tr><th>Layer</th><th>On screen</th><th>Your input</th><th>Load</th></tr>
<tr><td><span class="n">L0</span> subject</td><td>The river of chapters. Only the stops you have reached: the current one is big and older ones shrink to dots. The next stop waits as a faint dotted ghost, with water trickling toward it.</td><td>space / ↓ / tap: the water flows on to the next stop and its priming card appears</td><td>1 card, ≤ 3 labels; older links fade</td></tr>
<tr><td><span class="n">L1</span> chapter</td><td>The same river, made of the chapter's concepts. A stop that needs something from another chapter shows a dotted <i>tributary</i> flowing in, e.g. <code>Ch 9 · D flip-flop</code>.</td><td>the same keys; Enter or a tap on the current stop starts its sprint</td><td>1 card: the concept's kind and one sentence</td></tr>
<tr><td><span class="n">L2</span> sprint</td><td>Nothing but the content, one small step at a time: guess → the idea → each figure → each point → check → done. An × to leave. The top bar and the from/to strip are gone.</td><td>space / → / tap to go on; ← back; Esc to leave</td><td>1 step</td></tr>
<tr><td><span class="n">L3</span> web</td><td>The full chapter map as faint dots. The concept's links to other chapters are revealed one per input, each as a curved line with its two concept names.</td><td>the same keys; Enter sprints the current link</td><td>1 link lit at a time</td></tr>
<tr><td><span class="n">L4</span> link <i>(split variant)</i></td><td>A link sprint: the two ends → guess the connection → the bridge → done.</td><td>as in L2</td><td>1 step</td></tr>
</table>

<h2><span class="k">L0</span> Three rivers</h2>
<p class="q">Every variant waits for input. On each step:</p>
<ul class="q"><li>the water draws itself down the edges into the new stop;</li><li>the stop pops in;</li><li>a pulse marks where you are;</li><li>a trickle runs toward the dotted ghost of the next stop.</li></ul>
<h3>A · Step river: one chapter per input (17 stops)</h3>
<div class="film">{fig("a-s0", "step 1: only the base", R + "s=0#/")}{fig("a-s3", "step 4", R + "s=3#/")}{fig("a-s8", "step 9: two streams join", R + "s=8#/")}{fig("a-s13", "step 14", R + "s=13#/")}</div>
<div class="grid2" style="margin-top:10px">{fig("a-all", "at the end, ⤢ see it all: the whole flow, only if you ask for it", R + "ov=1#/")}<div class="phones">{fig("a-s5-phone", "phone, step 6")}{fig("a-all-phone", "phone, see it all")}</div></div>
<h3>B · Units first (6 stops; each unit lists its chapters)</h3>
<div class="grid2">{fig("b-s3", "unit 3: three key words, then its 5 chapters as buttons", R + "l0=units&s=3#/")}<div class="phones">{fig("b-s3-phone", "phone")}</div></div>
<h3>C · Scroll river (scrolling drives the flow)</h3>
<div class="grid2">{fig("c-s5", "looks like A; the input is the scroll wheel or a swipe", R + "l0=scroll#/")}<div></div></div>
<div class="grid3" style="margin-top:16px">
<div class="opt rec"><h3>A · step river <span class="tag">engine's pick</span></h3><ul>
<li class="plus">every chapter gets its own priming stop</li><li class="plus">you can see convergence: streams join at a stop</li>
<li class="minus">17 inputs to see all of it the first time (⤢ all skips ahead)</li><li class="minus">the middle of the DE graph is wide, so some streams cross</li></ul></div>
<div class="opt"><h3>B · units first</h3><ul>
<li class="plus">6 stops: inside the 6–12 target, and the lowest load</li><li class="plus">straight down, no crossings</li>
<li class="minus">chapters become a list and lose their own priming</li><li class="minus">the web between chapters is hidden</li></ul></div>
<div class="opt"><h3>C · scroll</h3><ul>
<li class="plus">the most natural gesture on a phone</li>
<li class="minus">easy to scroll past a stop without reading it, which works against the point of priming</li><li class="minus">the pace belongs to the wheel, not to you</li></ul></div>
</div>

<h2><span class="k">L0</span> The priming card</h2>
<p class="q">Your idea of “priming” has an evidenced form:</p>
<ul class="q">
<li><b>Pretraining</b> (Mayer): learn the names and key traits of the parts before the lesson. It helped in 13 of 16 tests. The median effect was large, and that size is probably inflated.</li>
<li><b>Advance organizers</b> (a short overview up front): a modest benefit.</li>
<li><b>Pretesting</b> (guess before you're taught): strong.</li>
</ul>
<p class="q">The pop-science idea of priming (hidden cues quietly changing behaviour) mostly failed to replicate. None of this uses it.</p>
<div class="film f3">{fig("a-s8", "3 key terms, each with a short gloss (default): pretraining", R + "s=8#/")}{fig("a-s8-line", "one sentence: an advance organizer", R + "prime=line&s=8#/")}{fig("a-s8-q", "guess first: a question, then the words on a tap (pretesting)", R + "prime=q&s=8#/")}</div>

<h2><span class="k">COLOUR</span> Four ways to colour the river</h2>
<div class="film">{fig("a-s8", "kind (default): the ring shows the chapter's mix", R + "s=8#/")}{fig("a-s8-unit", "topic: the syllabus unit", R + "color=unit&s=8#/")}{fig("a-s8-role", "trunk · node · leaf · edge (grows as links appear)", R + "color=role&s=8#/")}{fig("a-s8-layer", "layer: the page takes the layer's tint", R + "color=layer&s=8#/")}</div>
<div class="grid2" style="margin-top:10px">{fig("a-s8-light", "light theme", R + "theme=light&s=8#/")}
<div class="opt"><h3>The five kinds <span class="tag">engine-chosen</span></h3>
<p>Each kind also tells you <i>how to study it</i>, which is why there are five and not two:</p>
<ul>
<li><span class="dot" style="background:#3b5bdb"></span><b>Logic</b> · work it out (22). You can derive these from earlier ideas, e.g. De Morgan, carry look-ahead.</li>
<li><span class="dot" style="background:#e8590c"></span><b>Memorise</b> · remember it (17). Facts, values and tables, e.g. BCD, excitation tables, PDP.</li>
<li><span class="dot" style="background:#2b8a3e"></span><b>Method</b> · do it (35). Step-by-step recipes, e.g. K-map grouping, synchronous counter design.</li>
<li><span class="dot" style="background:#7048e8"></span><b>Circuit</b> · draw it (40). Blocks to recognise and draw, e.g. MUX, SR latch, CMOS inverter.</li>
<li><span class="dot" style="background:#e03131"></span><b>Trap</b> · avoid it (3). Where marks are lost.</li>
</ul><p>Why study by kind: procedures go better when you see a worked example first, while concepts go better when you try them first (<code>research/03 §5</code>). Things to memorise need retrieval practice (<code>research/02 §1</code>).</p></div></div>

<h2><span class="k">L1</span> The same river inside a chapter</h2>
<div class="film">{fig("l1-ch3-s0", "Ch 3 K-maps, the first stop", R + "p=17&s=0#/ch/ch3")}{fig("l1-ch3-s4", "stop 5, already done", R + "p=24&s=4#/ch/ch3")}{fig("l1-ch12-s0", "a tributary: Ch 9's D flip-flop flows in", R + "p=60&s=0#/ch/ch12")}{fig("l1-ch12-s3-role", "role colours: a leaf becomes a node as links appear", R + "color=role&p=60&s=3#/ch/ch12")}</div>
<div class="phones" style="margin-top:10px">{fig("l1-ch12-s0-phone", "phone")}</div>

<h2><span class="k">L2</span> The sprint: content only</h2>
<p class="q">Don't-cares, one step at a time. Only the K-map chapters (Ch 3–4) have real cards so far. Every other concept shows the idea plus a note that its full card comes with content engine v2 (session 4).</p>
<div class="film f5">{fig("l2-dc-0", "the idea: its kind, its name, one line", R + "#/c/ch4/dont-cares")}{fig("l2-dc-1", "the figure, alone")}{fig("l2-dc-3", "check: answer, then reveal")}{fig("l2-dc-4", "done → back to the river, one stop further on")}{fig("l2-gs-1", "another card: bigger group, fewer letters", R + "#/c/ch3/group-size")}</div>
<div class="phones" style="margin-top:10px">{fig("l2-dc-1-phone", "phone")}{fig("l2-mux-0", "a concept without a card yet", R + "#/c/ch6/mux")}</div>

<h2><span class="k">L3</span> The web, and where the edges get explained</h2>
<div class="film f3">{fig("l3-mux-s0", "the multiplexer's web: 6 links waiting", R + "p=60&s=-1#/web/mux")}{fig("l3-mux-s2", "link 3 of 6: feeds ALU (merged: L3 map + link sprints)", R + "p=60&s=2#/web/mux")}{fig("l3-all-s6", "the whole-subject web: the 18 relates-to links", R + "p=60&s=6#/web")}</div>
<div class="film f3" style="margin-top:10px">{fig("l3-mux-s2-split", "split: L3 only shows the link; L4 explains it", R + "l3=split&p=60&s=2#/web/mux")}{fig("l4-link-0", "L4 link sprint: the two ends", R + "l3=split#/web/mux/e/mux/alu")}{fig("l3-link-2", "the bridge: the link's own content")}</div>
<div class="phones" style="margin-top:10px">{fig("l3-mux-phone", "phone")}</div>
<div class="grid2" style="margin-top:16px">
<div class="opt rec"><h3>Merged: L3 = map + link sprints <span class="tag">engine's pick</span></h3><ul><li class="plus">one fewer layer to keep in mind</li><li class="plus">a link's sprint opens from the map you're looking at</li></ul></div>
<div class="opt"><h3>Split: L3 map · L4 explains</h3><ul><li class="plus">L3 stays purely visual</li><li class="minus">the only real difference is a name and one more step down; the sprint is identical</li></ul></div>
</div>

<h2><span class="k">!</span> Honest problems</h2>
<div class="note"><b>1.</b> The middle of the DE chapter graph is wide (5 chapters on one row), so in variant A some streams cross around steps 9–13. Old links fade to 16% so the current one still reads. A custom river layout that keeps a main channel could do better; that belongs in the session 3 build.</div>
<div class="note"><b>2.</b> The kinds, priming lines and key terms are hand-written. They stand in for the automatic step, the same way <code>de_graph.py</code> does. Some tags are judgement calls, e.g. Gray code as a method. In v2 proper the engine writes these from the knowledge base.</div>
<div class="note"><b>3.</b> Sprints only have real content where v1 cards exist (9 K-map concepts). Content engine v2 (session 4) fills in the rest.</div>
<div class="note"><b>4.</b> L3 works at chapter level: chapters are dots, and each link shows the concepts at its two ends. Putting all 117 concepts on one screen would break the visual-load rule, so that wasn't built.</div>
<div class="note"><b>5.</b> On a phone, “see it all” fits only chapter numbers, not names. It is the one dense view, and you only see it if you ask for it.</div>

<div class="pick"><b>Your picks</b> (answer in any form, e.g. “A, terms, kind, merged”):
<ol>
<li><b>L0 variant:</b> A step river · B units first · C scroll. Engine: <code>A</code></li>
<li><b>Priming card:</b> 3 terms · one sentence · guess first. Engine: <code>3 terms</code> on L0 stops, and guess first on L1 stops automatically wherever a real predict question exists</li>
<li><b>Default colour:</b> kind · topic · role · layer. Engine: <code>kind</code>, with role as a toggle</li>
<li><b>L3:</b> merged · split (L4). Engine: <code>merged</code></li>
<li><b>Sprint:</b> step dots on or off. Engine: <code>on</code></li>
<li>Anything that still feels like too much, on any screen?</li>
</ol></div>
</div>
<div class="zoom" id="zoom"><img alt=""></div>
<script>
document.querySelectorAll('figure img').forEach(i => i.addEventListener('click', () => {{ const z = document.getElementById('zoom'); z.querySelector('img').src = i.src; z.classList.add('on'); }}));
document.getElementById('zoom').addEventListener('click', e => e.currentTarget.classList.remove('on'));
</script>
"""

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Site v2 · the river · pick</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@600;700&display=swap" rel="stylesheet">
{style}
{extra}
</head>
<body>{body}</body>
</html>
"""
(HERE / "compare-river.html").write_text(html, encoding="utf-8")
missing = [n for n in __import__("re").findall(r'shots/river/([a-z0-9-]+)\.png', html) if not (HERE / "shots/river" / f"{n}.png").exists()]
print("missing:", missing)
