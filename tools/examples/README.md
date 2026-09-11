# tools/examples/ — subsystem demos + acceptance tests

Two end-to-end lessons for the Visual & Rendering subsystem (`../../rendering.md`). They prove the
primitive map is **subject-agnostic** (see `rendering.md` §9 acceptance criteria):

| Script | Subject | Proves |
|--------|---------|--------|
| `lesson_rc_lowpass.py` → `rc-lowpass.html` | `ece` | the structural-**registry** path (schemdraw) + universal primitives |
| `lesson_sorting.py` → `sorting.html` | `python` | the **universal** path with **no** primitive-6 renderer registered |

```
python tools/examples/lesson_rc_lowpass.py          # writes rc-lowpass.html here
python tools/examples/lesson_sorting.py --open       # writes sorting.html here and opens it
```

**These `.html` files are regenerable demos, not teaching lessons.** They live here permanently
(beside their scripts) and are overwritten each run — on purpose. They deliberately use
`render(spec, <here>)` rather than `save_lesson()`, so they do **not** land in any subject's
`subjects/<subject>/lessons/`. Real lessons do (dated, per-subject, never clobbered) — see
`../README.md` and `../../rendering.md` §8. The script is the reproducible source; a deleted `.html`
is one command away.
