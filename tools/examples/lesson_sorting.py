#!/usr/bin/env python3
"""
Acceptance Test B — UNIVERSAL path, NO structural renderer (subject: python).

Concept: comparison sorting. This subject registers **no** primitive-6 renderer and must not need
one. It exercises only the universal primitives:
  concept map (2) -> flowchart (3) -> matplotlib complexity plot (4)
  -> highlighted code -> comparison table (5) -> one CHECK.

If the subsystem were still ECE-coupled it would silently reach for a circuit renderer or break.
It does neither: there is no `structural` block here, and `make_figure`'s registry is never touched.
That is the generalization proof.

Run:  python tools/examples/lesson_sorting.py        # writes sorting.html beside this file
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # tools/ on path
from render_lesson import render


# --- primitive 4 data: growth curves, computed in Python ---
n = np.arange(1, 101)
quadratic = (n ** 2).astype(float)
nlogn = (n * np.log2(n, where=n > 0)).astype(float)


MERGE_SORT = '''\
def merge_sort(a):
    if len(a) <= 1:                      # base case: 0 or 1 element is already sorted
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])           # divide
    right = merge_sort(a[mid:])
    return _merge(left, right)           # conquer: linear-time merge of two sorted halves

def _merge(left, right):
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:          # <= keeps equal keys in order -> stable
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:]); out.extend(right[j:])
    return out
'''


SPEC = {
    "title": "Comparison Sorting — Why O(n log n) Wins",
    "subject": "python",
    "intro": "Sorting rearranges a sequence into order by **comparing** elements. The whole story "
             "is one question: how does the work grow as the input grows? **Quadratic** sorts double "
             "their cost fourfold; **n log n** sorts barely flinch.",
    "sections": [
        # -- primitive 2: concept-map-first --
        {"heading": "The family (open here)", "blocks": [
            {"type": "map", "caption": "Comparison sorts, by strategy",
             "mermaid": (
                "graph TD\n"
                "  S[Comparison sorts] --> Q[Quadratic O(n^2)]\n"
                "  S --> D[Divide & conquer O(n log n)]\n"
                "  Q --> BUB[Bubble]\n"
                "  Q --> INS[Insertion]\n"
                "  D --> MRG[Merge sort]\n"
                "  D --> QCK[Quicksort]\n"
                "  MRG -. stable, O(n) extra space .-> NOTE1[ ]\n"
                "  QCK -. in-place, O(n^2) worst case .-> NOTE2[ ]"
             )},
        ]},
        # -- primitive 3: process / flowchart (Mermaid) --
        {"heading": "How merge sort runs", "blocks": [
            {"type": "process", "caption": "Divide until trivial, then merge back up",
             "mermaid": (
                "flowchart TD\n"
                "  A[Receive list a] --> B{len a <= 1 ?}\n"
                "  B -- yes --> C[Return a: already sorted]\n"
                "  B -- no --> D[Split at midpoint]\n"
                "  D --> E[merge_sort left half]\n"
                "  D --> F[merge_sort right half]\n"
                "  E --> G[Merge two sorted halves in linear time]\n"
                "  F --> G\n"
                "  G --> H[Return merged sorted list]"
             )},
        ]},
        # -- primitive 4: matplotlib quantitative plot --
        {"heading": "The reason it matters", "blocks": [
            {"type": "plot", "caption": "Operations vs input size. The gap is the whole game.",
             "figure": {"kind": "matplotlib",
                        "series": [
                            {"x": n.tolist(), "y": quadratic.tolist(), "label": "O(n^2)  bubble/insertion"},
                            {"x": n.tolist(), "y": nlogn.tolist(), "label": "O(n log n)  merge/quick", "style": "--"},
                        ],
                        "xlabel": "input size  n", "ylabel": "comparisons (approx)"}},
        ]},
        # -- support primitive: highlighted code --
        {"heading": "Merge sort, in Python", "blocks": [
            {"type": "code", "lang": "python", "code": MERGE_SORT},
        ]},
        # -- primitive 5: comparison table --
        {"heading": "The trade-offs at a glance", "blocks": [
            {"type": "table", "caption": "Pick by constraint: memory, stability, worst-case guarantee",
             "headers": ["Sort", "Avg time", "Worst time", "Stable?", "In-place?"],
             "rows": [
                 ["Bubble", "O(n^2)", "O(n^2)", "yes", "yes"],
                 ["Insertion", "O(n^2)", "O(n^2)", "yes", "yes"],
                 ["Merge", "O(n log n)", "O(n log n)", "yes", "no (O(n) extra)"],
                 ["Quicksort", "O(n log n)", "O(n^2)", "no", "yes"],
             ],
             "highlight_row": 2}],
        },
        # -- CHECK --
        {"heading": "Check", "blocks": [
            {"type": "check",
             "q": "You must sort a huge list and you need a **guaranteed** worst-case time bound, "
                  "with stability. Which of the four above do you pick, and what is the one cost "
                  "you accept for it?",
             "answer": "**Merge sort.** It is the only one that is *both* stable *and* O(n log n) in "
                       "the **worst** case (quicksort degrades to O(n^2) worst-case; the quadratic "
                       "sorts are O(n^2) always). The cost you accept: **O(n) extra memory** — merge "
                       "sort is not in-place."},
        ]},
    ],
}


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sorting.html")
    render(SPEC, out, open_browser="--open" in sys.argv)
