"""Contact sheets of cropped figures for visual checking. Run: python sheets.py <regex> <outdir>"""
import math, re, sys
from pathlib import Path
from PIL import Image, ImageDraw

pat, outdir = re.compile(sys.argv[1]), Path(sys.argv[2])
figs = sorted(f for f in Path(__file__).resolve().parent.parent.joinpath("figs").glob("*.png") if pat.fullmatch(f.stem))
for sheet in range(math.ceil(len(figs) / 8)):
    group = figs[sheet * 8:(sheet + 1) * 8]
    ims = [Image.open(f).convert("RGB") for f in group]
    ims = [im.resize((int(im.width * min(1, 560 / im.width)), int(im.height * min(1, 560 / im.width)))) for im in ims]
    rows = [list(range(i, min(i + 2, len(ims)))) for i in range(0, len(ims), 2)]
    H = sum(max(ims[k].height for k in r) + 30 for r in rows)
    out = Image.new("RGB", (1180, H), "white"); d = ImageDraw.Draw(out); y = 0
    for r in rows:
        x = 0
        for k in r:
            im = ims[k]
            d.rectangle([x, y, x + im.width + 4, y + im.height + 24], outline="red")
            d.text((x + 3, y + 2), group[k].stem, fill="red"); out.paste(im, (x + 2, y + 20)); x += 590
        y += max(ims[k].height for k in r) + 30
    out.save(outdir / f"sheet{sheet}.png"); print(outdir / f"sheet{sheet}.png")
