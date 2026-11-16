"""Pull the text and pictures out of one professor deck, slide by slide.

Usage:  python -I deck_extract.py <deck.pptx|deck.ppt> <out_dir> [first_slide] [last_slide]

.pptx  -> <out_dir>/slides.txt ("=== slide N ===" blocks, in slide order) and every picture
          as <out_dir>/sNNN-<name>.<ext>. The last lines list the slides that are mostly
          pictures: read those PNG/JPEGs with the Read tool, the text alone misses them.
.ppt   -> (old binary format; no slide order available without olefile) <out_dir>/slides.txt
          holds the text runs in file order, and every embedded PNG/JPEG is saved as
          <out_dir>/pic-NNN.<ext>.

Standard library only. out_dir should be outside the repo (the auto.py scratch folder).
"""
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"


def pptx(deck, out, first, last):
    z = zipfile.ZipFile(deck)
    names = [n for n in z.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)]
    names.sort(key=lambda n: int(re.search(r"(\d+)", n.split("/")[-1]).group(1)))
    lines, picture_only = [], []
    for name in names:
        k = int(re.search(r"(\d+)", name.split("/")[-1]).group(1))
        if k < first or k > last:
            continue
        root = ET.fromstring(z.read(name))
        paras = []
        for p in root.iter(A + "p"):
            t = "".join(x.text or "" for x in p.iter(A + "t")).strip()
            if t:
                paras.append(t)
        rels_name = "ppt/slides/_rels/%s.rels" % name.split("/")[-1]
        pics = []
        if rels_name in z.namelist():
            rels = ET.fromstring(z.read(rels_name))
            targets = {r.get("Id"): r.get("Target") for r in rels}
            for blip in root.iter(A + "blip"):
                tgt = targets.get(blip.get(R + "embed"))
                if not tgt:
                    continue
                src = "ppt/" + tgt.replace("../", "")
                if src in z.namelist():
                    dst = out / ("s%03d-%s" % (k, Path(src).name))
                    dst.write_bytes(z.read(src))
                    pics.append(dst.name)
        lines.append("=== slide %d ===" % k)
        lines += paras
        if pics:
            lines.append("[pictures: %s]" % ", ".join(pics))
        if pics and sum(len(p) for p in paras) < 120:
            picture_only.append(k)
    (out / "slides.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("slides %d-%d -> %s" % (first, min(last, len(names)), out / "slides.txt"))
    print("mostly-picture slides (Read their images): %s" % (picture_only or "none"))


def ppt(deck, out):
    data = Path(deck).read_bytes()
    runs = []
    for m in re.finditer(rb"(?:[\x20-\x7e\xa0-\xff][\x00-\x03]){4,}", data):   # UTF-16LE text
        t = m.group().decode("utf-16-le", "ignore").strip()
        if len(t) >= 4:
            runs.append(t)
    for m in re.finditer(rb"[\x20-\x7e]{6,}", data):                           # 8-bit text atoms
        t = m.group().decode("latin-1").strip()
        if " " in t:
            runs.append(t)
    seen, uniq = set(), []
    for t in runs:
        if t not in seen:
            seen.add(t)
            uniq.append(t)
    (out / "slides.txt").write_text("\n".join(uniq) + "\n", encoding="utf-8")
    n = 0
    for sig, end, ext in ((b"\x89PNG\r\n\x1a\n", b"IEND\xaeB`\x82", "png"), (b"\xff\xd8\xff", b"\xff\xd9", "jpg")):
        i = data.find(sig)
        while i != -1:
            j = data.find(end, i + len(sig))
            if j == -1:
                break
            j += len(end)
            if j - i > 2000:
                n += 1
                (out / ("pic-%03d.%s" % (n, ext))).write_bytes(data[i:j])
            i = data.find(sig, j)
    print("text runs -> %s; %d pictures saved (file order, not slide order)" % (out / "slides.txt", n))


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    deck, out = Path(sys.argv[1]), Path(sys.argv[2])
    first = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    last = int(sys.argv[4]) if len(sys.argv) > 4 else 10 ** 6
    out.mkdir(parents=True, exist_ok=True)
    if deck.suffix.lower() == ".pptx":
        pptx(deck, out, first, last)
    elif deck.suffix.lower() == ".ppt":
        ppt(deck, out)
    else:
        sys.exit("not a .pptx/.ppt: %s (PDF decks: use render_pages.py)" % deck)


if __name__ == "__main__":
    main()
