"""Build the Unit 1-2 formula cheat sheet (look of the v1.2 pack; figures reused from it).

Run:  python build.py      content/*.md -> html/ -> pdf/ + one combined PDF.
Numbers: python verify.py
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "src"))
from build import ALL  # noqa: E402  (the v1.2 pack's figure registry)
from study_pack_build import build  # noqa: E402

if __name__ == "__main__":
    build(HERE, pack="ECE2106 EDC · Units 1–2 formula cheat sheet",
          combined="EDC-U1-U2-formula-cheatsheet.pdf", figures=ALL)
