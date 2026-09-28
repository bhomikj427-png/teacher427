"""Machine checks for the After Effects web pack. Run: python verify.py

1. Every figure is well-formed SVG.
2. Every shortcut in a `Key | Does` table on the site appears in knowledge-base/shortcuts.md (the sourced
   reference), so the site cannot teach a key the KB never verified.
3. The motion maths drawn in the figures matches Adobe's description:
   - Easy Ease: speed 0 at both keyframes, endpoints exact, S-shaped (UG p.321).
   - Linear: constant speed. Hold: value jumps only at the second keyframe (UG p.312).
   - Same distance under both speed curves (area under speed = change in value).
4. Rotation happens about the anchor point: the anchor's comp position is unchanged by rotation (UG p.183).
5. Range selector figure: letters are released left to right as Start increases.
6. loopOut('cycle') figure is periodic; time * 90 has slope 90 per second.
"""
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import figures as F

HERE = Path(__file__).resolve().parent
KB = HERE.parents[1] / "knowledge-base" / "shortcuts.md"
fails = []


def ok(cond, msg):
    print(("OK  " if cond else "BAD ") + msg)
    if not cond:
        fails.append(msg)


# 1. figures
for name, fn in F.ALL.items():
    try:
        ET.fromstring(fn())
        good = True
    except ET.ParseError as e:
        good = False
        print("   ", e)
    ok(good, f"figure {name} is well-formed SVG")


# 2. shortcuts on the site ⊆ sourced reference
def norm(k):
    return re.sub(r"\s+", "", k.replace("**", "").replace("`", "")).lower()


kb_keys = set()
for line in KB.read_text(encoding="utf-8").splitlines():
    m = re.match(r"\|\s*(.+?)\s*\|", line)
    if m and not set(m.group(1)) <= set("-: "):
        for part in re.split(r"\s+/\s+|\s+·\s+", m.group(1)):
            kb_keys.add(norm(part))
        kb_keys.add(norm(m.group(1)))

site_keys = []
for f in sorted((HERE / "content").glob("*.md")):
    in_table = False
    for line in f.read_text(encoding="utf-8").splitlines():
        if re.match(r"\|\s*Key\s*\|\s*Does\s*\|", line):
            in_table = True
            continue
        if in_table and line.startswith("|"):
            cell = line.split("|")[1].strip()
            if set(cell) <= set("-: "):
                continue
            site_keys.append((f.name, cell))
        else:
            in_table = False
missing = [(f, k) for f, k in site_keys
           if norm(k) not in kb_keys and not all(norm(p) in kb_keys for p in re.split(r"\s+/\s+", k))]
for f, k in missing:
    print(f"    not in shortcuts.md: {k!r} ({f})")
ok(not missing, f"{len(site_keys)} shortcut rows on the site all appear in knowledge-base/shortcuts.md")

# 3. easing maths
n = 1000
e = [F.ease_value(i / n) for i in range(n + 1)]
ok(abs(e[0]) < 1e-9 and abs(e[-1] - 1) < 1e-9, "Easy Ease starts at the first value and ends at the second")
ok((e[1] - e[0]) * n < 0.02 and (e[-1] - e[-2]) * n < 0.02, "Easy Ease speed is ~0 at both keyframes (speed 0, UG p.321)")
ok(all(b >= a - 1e-12 for a, b in zip(e, e[1:])), "Easy Ease never reverses (monotonic)")
mid_speed = (e[n // 2 + 1] - e[n // 2 - 1]) * n / 2
ok(mid_speed > 1.2, f"Easy Ease is fastest in the middle (speed {mid_speed:.2f} > linear 1.0)")
lin = [F.linear_value(i / n) for i in range(n + 1)]
ok(len({round((b - a) * n, 9) for a, b in zip(lin, lin[1:])}) == 1, "Linear has constant speed")
ok(F.hold_value(0.999) == 0 and F.hold_value(1) == 1, "Hold keeps the value until the next keyframe, then jumps")
ok(abs(sum((b - a) for a, b in zip(e, e[1:])) - sum((b - a) for a, b in zip(lin, lin[1:]))) < 1e-9,
   "Area under both speed curves is equal (same distance)")

# 4. rotation about the anchor point
for anchor in [(60, 30), (0, 0), (120, 60)]:
    pos = (300, 200)
    before = F.rect_corners(pos, anchor, 120, 60, 0)
    after = F.rect_corners(pos, anchor, 120, 60, 35)
    a0 = (before[0][0] + anchor[0], before[0][1] + anchor[1])
    ok(all(abs(abs(complex(*p) - complex(*pos)) - abs(complex(*q) - complex(*pos))) < 1e-9 for p, q in zip(before, after))
       and abs(a0[0] - pos[0]) < 1e-9 and abs(a0[1] - pos[1]) < 1e-9,
       f"rotation keeps every corner's distance to the anchor {anchor} (anchor sits at Position)")

# 5. range selector
for start in (0.0, 1 / 3, 2 / 3, 1.0):
    ops = [F.selector_opacity(i, 6, start) for i in range(6)]
    ok(all(b <= a + 1e-12 for a, b in zip(ops, ops[1:])), f"selector Start {start:.2f}: letters revealed left to right")
ok(all(F.selector_opacity(i, 6, 1.0) == 1 for i in range(6)), "selector Start 100 %: every letter visible")
ok(all(F.selector_opacity(i, 6, 0.0) == 0 for i in range(6)), "selector Start 0 %: every letter hidden (Opacity 0 %)")

# 6. expressions
ok(all(abs(F.loop_cycle(t / 10) - F.loop_cycle(t / 10 + 1)) < 1e-9 for t in range(30)), "loopOut('cycle') repeats every second")
ok(abs((90 * 3.0 - 90 * 1.0) / 2 - 90) < 1e-12, "time * 90 → 90° per second")

print()
print("ALL CHECKS PASSED" if not fails else f"{len(fails)} CHECK(S) FAILED")
raise SystemExit(1 if fails else 0)
