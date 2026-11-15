"""cap.py — read a caption transcript without flooding context.

Usage:
  python -I research-tools/cap.py <file-or-glob>                 -> whole text, cleaned
  python -I research-tools/cap.py <file-or-glob> <regex> [width] -> each hit with +-width chars
Cleans &nbsp; and whitespace. Transcripts live outside the repo (copyrighted; scratch only).
"""
import glob
import html
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
path = glob.glob(sys.argv[1])[0]
t = open(path, encoding="utf-8", errors="replace").read()
t = re.sub(r"\s+", " ", html.unescape(t).replace("\xa0", " "))
if len(sys.argv) == 2:
    print(t)
    sys.exit()
w = int(sys.argv[3]) if len(sys.argv) > 3 else 400
last = -1
for m in re.finditer(sys.argv[2], t, re.I):
    if m.start() < last:
        continue
    a, b = max(0, m.start() - w), min(len(t), m.end() + w)
    print(f"[{m.start()}] ...{t[a:b]}...\n")
    last = b
