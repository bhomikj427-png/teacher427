"""DE study PDF v2: demo chapter "Shift registers & shift counters".

River rules (learner-preferences §3, site/SITE-V2-DRAFT.md §14), applied to print:
start from what is already known; staircase map; ≤3 priming terms per stop; one idea per page;
bridges between stops are their own pages; guesses are answered on the NEXT page (turn = reveal).
A load test runs on the finished PDF: every page must stay inside the budget below.

Run:  python build.py
"""
import subprocess
from pathlib import Path

import figs as F

HERE = Path(__file__).resolve().parent
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
CHAPTER = "Shift registers & shift counters"
STOPS = ["D flip-flop", "Register", "Shift register", "Ring counter", "Johnson counter", "Decode + lock-out"]
BUDGET_WORDS, BUDGET_FIGS = 75, 1

pages = []


def page(kind, stop=None, title="", body="", fig="", cls=""):
    pages.append(dict(kind=kind, stop=stop, title=title, body=body, fig=fig, cls=cls))


def opener(i, terms):
    """Stop opener: where you are (staircase) + priming card of ≤3 terms."""
    assert len(terms) <= 3
    card = "".join(f"<div class='term'><b>{t}</b><span>{g}</span></div>" for t, g in terms)
    page("opener", i, STOPS[i],
         f"<div class='split'><div>{F.staircase(STOPS, i)}</div><div class='prime'><div class='lbl'>words you need</div>{card}</div></div>")


def bridge(i, text):
    page("bridge", i, "", f"<p class='big'>{text}</p>", F.bridge(STOPS[i - 1], STOPS[i], "why next?"))


Q = ("Anna University · EC6302 Digital Electronics · Apr/May 2015 · Q13(b)(i) · 8 marks",
     "Discuss the working of a 4 bit Johnson counter with neat block diagram.")

# ---------------------------------------------------------------- start
page("cover", None, CHAPTER,
     f"<div class='q'><div class='src'>{Q[0]}</div>{Q[1]}</div>"
     "<p class='big'>You can't answer this yet. Six short stops from now you will, and every stop starts from the one before it.</p>")
page("where", None, "Where this chapter sits",
     "<p>You already have flip-flops and counters from the MTE half. This chapter takes the flip-flop one step further.</p>",
     F.staircase(["Flip-flops (MTE)", "Shift registers", "Timing", "State machines", "Logic families"], 1,
                 note="← this chapter"))
page("map", None, "The six stops",
     "<p>Read top to bottom. Each stop needs only the stop above it.</p>", F.staircase(STOPS, -1))

# ---------------------------------------------------------------- stop 1: D flip-flop
opener(0, [("Clock (CLK)", "a signal that ticks 0 → 1 → 0 → 1 … forever"),
           ("Rising edge", "the instant the clock jumps from 0 to 1"),
           ("D flip-flop", "a 1-bit memory: input D, output Q")])
page("guess", 0, "Guess first",
     "<p class='big'>Q is 0. D is 1. The clock rises.<br><b>What is Q now?</b><br>Then D drops back to 0 before the next rise. <b>Does Q change?</b></p>"
     "<div class='pad'>write your guess here</div>")
page("idea", 0, "The rule: copy at the edge, then hold",
     "<p>At each rising edge, Q becomes whatever D is <b>at that instant</b>. Between edges Q holds still, whatever D does.</p>",
     F.dff_symbol())
page("idea", 0, "Watch it happen",
     "<p>Dotted lines = rising edges. Q only moves on a dotted line. D's wiggles between edges are ignored.</p>",
     F.dff_waves(answer=True))
page("check", 0, "Check: draw Q",
     "<p>Q starts at 0. Draw Q under this D. Watch the short pulse between the 2nd and 3rd edges.</p>",
     F.check1_waves(answer=False))
page("answer", 0, "Answer",
     "<p>Q = 1, 0, 0, 1 at the four edges. The short pulse (shaded) falls <b>between</b> edges, so it is never seen.</p>",
     F.check1_waves(answer=True))

# ---------------------------------------------------------------- stop 2: register
bridge(1, "One flip-flop remembers <b>one bit</b>. A 4-bit number needs four bits. So use four flip-flops.")
opener(1, [("Register", "a row of flip-flops that share one clock"),
           ("Parallel load", "all bits enter together, at the same edge")])
page("idea", 1, "Four flip-flops, one clock",
     "<p>Each flip-flop has its own D and Q. Because they share CLK, one edge copies all four bits at once. That is a 4-bit register.</p>",
     F.register())
page("check", 1, "Check",
     "<p class='big'>D3 D2 D1 D0 = 1 0 1 1 are waiting at the inputs. Q is 0000. One rising edge arrives.<br><b>What is Q3 Q2 Q1 Q0?</b></p>"
     "<div class='pad'>write it here</div>")
page("answer", 1, "Answer",
     "<p class='big'>Q3 Q2 Q1 Q0 = <b>1 0 1 1</b>. Every flip-flop copied its own D at the same edge. Nothing moved sideways.</p>")

# ---------------------------------------------------------------- stop 3: shift register
bridge(2, "In a register every input comes from outside. Now wire each flip-flop's input to its <b>left neighbour's output</b> instead.")
opener(2, [("Shift register", "flip-flops in a chain: each Q feeds the next D"),
           ("Serial in", "the one input at the start of the chain"),
           ("Serial out", "the one output at the end")])
page("guess", 2, "Guess first",
     "<p class='big'>The chain holds Q0 Q1 Q2 Q3 = <b>1 0 0 0</b>. Serial in = 0. One rising edge.<br><b>What do the four flip-flops hold now?</b></p>"
     "<div class='pad'>write your guess here</div>")
page("idea", 2, "Everything moves one place",
     "<p>Each flip-flop copies its neighbour's <b>old</b> value, because all of them sample at the same edge (stop 1). So the 1 moves one place: <b>0 1 0 0</b>.</p>",
     F.chain("shift"))
page("idea", 2, "Feeding in a word, one bit per clock",
     "<table class='t'><tr><th>clock</th><th>serial in</th><th>Q0 Q1 Q2 Q3</th></tr>"
     "<tr><td>start</td><td>–</td><td>0 0 0 0</td></tr><tr><td>1</td><td>1</td><td>1 0 0 0</td></tr>"
     "<tr><td>2</td><td>0</td><td>0 1 0 0</td></tr><tr><td>3</td><td>1</td><td>1 0 1 0</td></tr>"
     "<tr><td>4</td><td>1</td><td>1 1 0 1</td></tr></table>"
     "<p>After 4 clocks the whole word 1011 is inside, readable all at once. Bits in one at a time, out all together: <b>serial-in, parallel-out</b>.</p>")
page("idea", 2, "Why anyone builds one",
     "<table class='t'><tr><th>use it as</th><th>what it does</th></tr>"
     "<tr><td>serial → parallel</td><td>a cable sends bits one at a time; the register collects a full word</td></tr>"
     "<tr><td>parallel → serial</td><td>load a word at once, shift it out bit by bit</td></tr>"
     "<tr><td>delay line</td><td>a bit comes out n clocks after it went in</td></tr></table>")
page("check", 2, "Check",
     "<p class='big'>A 4-bit chain starts at 0000. A single 1 enters on clock 1, then 0s.<br><b>On which clock does that 1 reach serial out (Q3)?</b></p>"
     "<div class='pad'>write it here</div>")
page("answer", 2, "Answer",
     "<p class='big'><b>Clock 4.</b> It enters Q0 on clock 1, then Q1, Q2, Q3 on clocks 2, 3, 4. A 4-stage chain delays a bit by 4 clocks.</p>")

# ---------------------------------------------------------------- stop 4: ring counter
bridge(3, "In a shift register the bit that reaches the end <b>falls off and is lost</b>. What if the end is wired back to the start?")
opener(3, [("Counter", "a circuit that steps through a fixed cycle of states, one per clock"),
           ("Mod-N", "the cycle has N states before it repeats"),
           ("Ring counter", "a shift register whose last Q feeds its first D")])
page("guess", 3, "Guess first",
     "<p class='big'>Start at <b>1 0 0 0</b>. Q3 now feeds D0. Write the next <b>four</b> states.</p>"
     "<div class='pad'>write your guess here</div>")
page("idea", 3, "The 1 goes round and round",
     "<p>1000 → 0100 → 0010 → 0001 → <b>1000</b>. Four flip-flops, four states: a <b>mod-4</b> counter. Each Q is high in exactly one state, so no extra gates are needed to read it.</p>",
     F.chain("ring"))
page("idea", 3, "One catch",
     "<p class='big'>It must start with exactly one 1. Start at 0000 and the zeros circulate forever: it never counts. Real designs <b>preset</b> it to 1000 at power-on.</p>")
page("check", 3, "Check",
     "<p class='big'>How many flip-flops does a <b>mod-10</b> ring counter need?</p><div class='pad'>write it here</div>")
page("answer", 3, "Answer",
     "<p class='big'><b>10.</b> A ring counter has one state per flip-flop. That's wasteful: 4 bits could hold 16 patterns, and the ring uses only 4.</p>")

# ---------------------------------------------------------------- stop 5: Johnson
bridge(4, "The ring wastes flip-flops. <b>One inverter</b> in the feedback wire doubles the number of states.")
opener(4, [("Johnson counter", "a ring counter that feeds back the last Q inverted (Q3′)"),
           ("Q′ (Q-bar)", "the opposite of Q: 1 when Q is 0")])
page("guess", 4, "Guess first",
     "<p class='big'>Start at <b>0 0 0 0</b>. D0 now gets <b>Q3′</b>. Write states until it repeats.<br><b>How many did you get?</b></p>"
     "<div class='pad'>write your guess here</div>")
page("idea", 4, "It fills with 1s, then empties",
     "<table class='t mono'><tr><th>clk</th><th>Q0 Q1 Q2 Q3</th><th>clk</th><th>Q0 Q1 Q2 Q3</th></tr>"
     "<tr><td>0</td><td>0 0 0 0</td><td>4</td><td>1 1 1 1</td></tr><tr><td>1</td><td>1 0 0 0</td><td>5</td><td>0 1 1 1</td></tr>"
     "<tr><td>2</td><td>1 1 0 0</td><td>6</td><td>0 0 1 1</td></tr><tr><td>3</td><td>1 1 1 0</td><td>7</td><td>0 0 0 1</td></tr></table>"
     "<p>Q3 = 0 pushes in 1s; Q3 = 1 pushes in 0s. <b>8 states from 4 flip-flops: mod-2n.</b></p>",
     cls="tight")
page("idea", 4, "The circuit",
     "<p>Same chain as the ring. The only change is the inverter on the feedback wire.</p>", F.chain("johnson"))
page("idea", 4, "The waveforms",
     "<p>Each Q is a square wave lasting 8 clocks: on for 4, off for 4. Each one starts one clock after the one above it.</p>",
     F.johnson_waves())
page("check", 4, "Check",
     "<p class='big'>How many flip-flops does a <b>mod-10 Johnson</b> counter need?</p><div class='pad'>write it here</div>")
page("answer", 4, "Answer",
     "<p class='big'><b>5.</b> Johnson gives 2n states, so 2n = 10 → n = 5. The ring needed 10.</p>")

# ---------------------------------------------------------------- stop 6: decode + lock-out
bridge(5, "A counter is only useful if some gate can <b>tell which state it is in</b>.")
opener(5, [("Decode", "a gate whose output is 1 in exactly one state"),
           ("Lock-out", "the counter gets stuck cycling through states it was never meant to use")])
page("idea", 5, "Two neighbouring bits are enough",
     "<p>Look at state 1100 in the table: it is the only state where Q1 = 1 and Q2 = 0. So a 2-input AND decodes it. Every Johnson state has a pair like this.</p>",
     F.decode_gate())
page("idea", 5, "All eight decode terms",
     "<table class='t mono'><tr><th>state</th><th>term</th><th>state</th><th>term</th></tr>"
     "<tr><td>0000</td><td>Q0′Q3′</td><td>1111</td><td>Q0Q3</td></tr><tr><td>1000</td><td>Q0Q1′</td><td>0111</td><td>Q0′Q1</td></tr>"
     "<tr><td>1100</td><td>Q1Q2′</td><td>0011</td><td>Q1′Q2</td></tr><tr><td>1110</td><td>Q2Q3′</td><td>0001</td><td>Q2′Q3</td></tr></table>"
     "<p>Rule: AND the two bits where 1s meet 0s.</p>", cls="tight")
page("idea", 5, "The other 8 patterns",
     "<p>4 bits have 16 patterns and Johnson uses 8. The other 8 form <b>their own loop</b>. Start in one (say 0100 after a power glitch) and the counter never returns. Fix: reset to 0000 at power-on.</p>",
     F.two_loops())
page("check", 5, "Check",
     "<p class='big'>Which 2-input AND decodes state <b>0011</b>?</p><div class='pad'>write it here</div>")
page("answer", 5, "Answer",
     "<p class='big'><b>Q1′ · Q2</b>. In 0011 the 0-to-1 boundary sits between Q1 (0) and Q2 (1).</p>")

# ---------------------------------------------------------------- finish
page("cover", None, "Back to the exam question",
     f"<div class='q'><div class='src'>{Q[0]}</div>{Q[1]}</div>"
     "<p class='big'>Close this PDF. Write the full 8-mark answer from memory. Use the stops as your outline. Then turn the page.</p>")
page("idea", None, "What an 8-mark answer contains",
     "<table class='t'><tr><th>part</th><th>from stop</th></tr>"
     "<tr><td>Definition: shift register with Q3′ fed back to D0</td><td>5</td></tr>"
     "<tr><td>Block diagram: 4 D flip-flops, common clock, inverted feedback</td><td>3, 5</td></tr>"
     "<tr><td>State table: 8 states, fill then empty</td><td>5</td></tr>"
     "<tr><td>Waveforms: Q0–Q3, each f/8, one clock apart</td><td>5</td></tr>"
     "<tr><td>Decoding with 2-input ANDs</td><td>6</td></tr>"
     "<tr><td>mod-2n vs ring mod-n · lock-out + reset</td><td>4, 6</td></tr></table>", cls="tight")
page("map", None, "Chapter done: where it connects",
     "<table class='t'><tr><th>this</th><th>connects to</th></tr>"
     "<tr><td>Ring / Johnson</td><td>synchronous counters (MTE): one shared clock, so no ripple delay</td></tr>"
     "<tr><td>Shift register + feedback</td><td>LFSR (next): feed back an XOR of taps → pseudo-random sequence</td></tr>"
     "<tr><td>Register</td><td>memory (Unit 5): one memory word is a register</td></tr></table>")

# ---------------------------------------------------------------- render
CSS = """
@page { size: 254mm 142.875mm; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; font: 15pt/1.45 "Segoe UI", system-ui, sans-serif; color: #1c1f24; background: #fff;
  -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.pg { width: 254mm; height: 142.875mm; padding: 11mm 18mm 10mm; position: relative; overflow: hidden;
  break-after: page; display: flex; flex-direction: column; }
.hd { position: absolute; top: 5mm; left: 18mm; right: 18mm; display: flex; justify-content: space-between;
  font-size: 8.5pt; color: #9aa0a9; letter-spacing: .03em; }
.dots span { display: inline-block; width: 7px; height: 7px; border-radius: 50%; margin-left: 5px; background: #e3e3de; }
.dots span.done { background: #9aa0a9; } .dots span.now { background: #2f5bea; }
.kind { color: #e0661b; font-weight: 700; text-transform: uppercase; letter-spacing: .08em; font-size: 8.5pt; margin-bottom: 2mm; }
.kind.k-idea, .kind.k-opener, .kind.k-map, .kind.k-where { color: #2f5bea; }
.kind.k-check, .kind.k-answer { color: #12925a; }
h1 { font-size: 22pt; margin: 0 0 4mm; line-height: 1.15; }
.cover h1 { font-size: 28pt; }
p { margin: 0 0 3mm; max-width: 200mm; }
p.big { font-size: 18pt; line-height: 1.45; }
.body { flex: 1; display: flex; flex-direction: column; justify-content: center; }
.fig { display: flex; justify-content: center; margin-top: 2mm; }
.fig svg.mpl { max-width: 100%; max-height: 62mm; width: auto; height: auto; }
.bridge .fig svg.mpl { max-height: 28mm; }
.split { display: grid; grid-template-columns: 1.25fr 1fr; gap: 10mm; align-items: center; }
.split svg.mpl { width: 100%; height: auto; max-height: 92mm; }
.prime .lbl { font-size: 9pt; text-transform: uppercase; letter-spacing: .08em; color: #9aa0a9; margin-bottom: 3mm; }
.term { border-left: 3px solid #2f5bea; padding: 1mm 0 1mm 4mm; margin-bottom: 4mm; }
.term b { display: block; font-size: 15pt; } .term span { color: #555b64; font-size: 13pt; }
.q { background: #eef2fe; border-left: 4px solid #2f5bea; padding: 5mm 7mm; border-radius: 0 10px 10px 0; font-size: 18pt;
  margin-bottom: 6mm; max-width: 210mm; }
.q .src { font-size: 9pt; color: #2f5bea; font-weight: 600; margin-bottom: 1.5mm; }
.pad { border: 1.5px dashed #c9ccd2; border-radius: 10px; height: 26mm; max-width: 200mm; color: #c9ccd2;
  font-size: 11pt; padding: 3mm 5mm; margin-top: 3mm; }
table.t { border-collapse: collapse; font-size: 13.5pt; margin: 0 0 4mm; }
table.t th { text-align: left; font-size: 10pt; color: #7a808a; font-weight: 600; text-transform: uppercase; letter-spacing: .05em;
  padding: 0 12mm 2mm 0; border-bottom: 1px solid #e3e3de; }
table.t td { padding: 1.6mm 12mm 1.6mm 0; border-bottom: 1px solid #f0f0eb; }
table.mono td { font-family: Consolas, monospace; }
.tight p { font-size: 13.5pt; }
"""


def render_page(p):
    dots = ""
    if p["stop"] is not None:
        dots = "".join(f"<span class='{'done' if i < p['stop'] else 'now' if i == p['stop'] else ''}'></span>"
                       for i in range(len(STOPS)))
    where = f"Stop {p['stop'] + 1} · {STOPS[p['stop']]}" if p["stop"] is not None else ""
    label = {"opener": "stop", "guess": "guess first", "idea": "", "check": "check", "answer": "answer",
             "bridge": "bridge", "map": "", "where": "", "cover": ""}[p["kind"]]
    fig = f"<div class='fig'>{p['fig']}</div>" if p["fig"] else ""
    title = f"<h1>{p['title']}</h1>" if p["title"] else ""
    return (f"<section class='pg {p['kind']} {p['cls']}'><div class='hd'><span>{CHAPTER}{'  ·  ' + where if where else ''}</span>"
            f"<span class='dots'>{dots}</span></div><div class='body'>"
            f"{'<div class=\"kind k-' + p['kind'] + '\">' + label + '</div>' if label else ''}{title}{p['body']}{fig}</div></section>")


def build():
    html = ("<!doctype html><html><head><meta charset='utf-8'><title>DE v2 demo</title>"
            f"<style>{CSS}</style></head><body>{''.join(render_page(p) for p in pages)}</body></html>")
    src = HERE / "DE-v2-demo.html"
    src.write_text(html, encoding="utf-8")
    out = HERE / "DE-v2-demo.pdf"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={out}",
                    src.as_uri()], check=True, capture_output=True)
    return out


def load_test(pdf):
    """Visual-load budget per page: body words (header excluded) and figure count."""
    import pymupdf
    doc = pymupdf.open(pdf)
    assert len(doc) == len(pages), f"page overflow: {len(doc)} PDF pages for {len(pages)} specs"
    worst, fails = 0, []
    for i, (pg, spec) in enumerate(zip(doc, pages)):
        words = [w for w in pg.get_text("words") if w[1] > 14 * 2.835]       # below the header strip
        n = len(words) - (sum(len(s.split()) for s in STOPS) + 9 if spec["kind"] in ("opener",) else 0)
        nfig = 1 if spec["fig"] or "<svg" in spec["body"] else 0
        worst = max(worst, n)
        if n > BUDGET_WORDS or nfig > BUDGET_FIGS:
            fails.append((i + 1, spec["kind"], n))
    print(f"{len(doc)} pages · worst page {worst} words (budget {BUDGET_WORDS}) · failures: {fails or 'none'}")
    return not fails


if __name__ == "__main__":
    pdf = build()
    print(pdf)
    load_test(pdf)
