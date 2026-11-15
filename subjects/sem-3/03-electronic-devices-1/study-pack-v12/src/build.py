"""Build the ECE2106 EDC ETE study pack (format: study-pack-format.md v1.2).

Run:  python build.py [file-prefix ...]
Figures and numbers are reused from the v1 pack (../../study-pack/pdf/figs*.py, checked by its verify.py).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(HERE.parents[1] / "study-pack" / "pdf"))
from study_pack_build import build  # noqa: E402
import figs, figs2, figs3  # noqa: E402,E401
sys.path.insert(0, str(HERE))
import figs_u1, figs_u2  # noqa: E402,E401

ALL = {}
for m in (figs, figs2, figs3):
    ALL.update({k: getattr(m, k) for k in dir(m) if not k.startswith("_") and callable(getattr(m, k))})
ALL.update(figs_u1.FIGS)
ALL.update(figs_u2.FIGS)

if __name__ == "__main__":
    build(HERE, pack="ECE2106 Electronic Devices & Circuits · ETE Study Pack",
          combined="ECE2106-EDC-ETE-study-pack.pdf", figures=ALL, only=sys.argv[1:])
