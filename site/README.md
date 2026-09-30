# site/ — the pictorial study website

**The format is frozen as v1: read [`SITE-V1.md`](SITE-V1.md) before changing anything.** v2 is in design (not built): [`SITE-V2-DRAFT.md`](SITE-V2-DRAFT.md) + session records in [`v2-design/`](v2-design/). It covers
the tree, its behaviour, the visual language, the content rules, authoring and the code map.

- **Build:** `python site/build.py` → `site/public/` (gitignored; open `site/public/<subject>/index.html`, links are relative).
- **Publish:** `bash site/deploy.sh <public-repo-url>` force-pushes only the generated pages to a separate public repo served by GitHub Pages. This private repo is never pushed there.
- **Add a subject/chapter:** `SITE-V1.md` §6.
- Design history: `SITE-V1.md` §8 and `../_PARKED-visual-study-packs.md`.
