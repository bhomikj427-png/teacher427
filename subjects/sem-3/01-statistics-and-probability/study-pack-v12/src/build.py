"""Build the MAS2001 Statistics & Probability ETE study pack (format: study-pack-format.md v1.2).

Run:  python verify.py && python build.py [file-prefix ...]
content/*.md -> ../html/*.html -> ../pdf/*.pdf + the combined bookmarked PDF.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(HERE))
from study_pack_build import build  # noqa: E402
from figures import ALL  # noqa: E402

if __name__ == "__main__":
    build(HERE, pack="MAS2001 Statistics & Probability · ETE Study Pack",
          combined="MAS2001-Statistics-and-Probability-ETE-study-pack.pdf", figures=ALL, only=sys.argv[1:],
          extra_css="table { break-inside: auto; } tr { break-inside: avoid; } thead { display: table-header-group; }")
