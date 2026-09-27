# site/ — the pictorial study website

- **Build:** `python site/build.py` → `site/public/` (gitignored; open `site/public/index.html` directly, links are relative).
- **Publish:** `bash site/deploy.sh <public-repo-url>` force-pushes only the generated pages to a separate public repo served by GitHub Pages. This private repo is never pushed there.
- **Add content:** a subject joins the site by having `study-pack/web/` with `meta.json`, `figures.py` (`ALL = {name: fn → SVG}`) and `content/NN-*.md`. Only chapters with a content file get a page; the rest show as "coming soon" on the learning path.
- **Syntax** (on top of Markdown): see the docstring of `build.py` — `[[fig:name|caption|w=60|steps=3]]`, `[[map:A > B|here=1]]`, `:::q/trap/check/note/key`, `:::reveal` (hidden answer), `$$ … $$`.
- **Look:** `static/style.css` (light + dark tokens; figure SVGs are styled by class so they follow the theme), `static/app.js` (theme toggle, figure steppers, TOC highlight).
- Pilot: Digital Electronics ch. 1 (`subjects/sem-3/04-digital-electronics/study-pack/web/`, answers machine-checked by its `verify.py`). Design history: `_PARKED-visual-study-packs.md`.
