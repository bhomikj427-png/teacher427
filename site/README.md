# site/ — the pictorial study website

- **Build:** `python site/build.py` → `site/public/` (gitignored; open `site/public/index.html` directly, links are relative).
- **Publish:** `bash site/deploy.sh <public-repo-url>` force-pushes only the generated pages to a separate public repo served by GitHub Pages. This private repo is never pushed there.
- **Shape:** each subject is ONE page, a zoomable map. Chapters are islands coloured by stage; concepts are numbered nodes with a kind badge (idea, method, exam, trap, practice). Click a chapter to zoom in; click a concept and its card opens (one concept at a time, ◀ ▶ to walk, Esc/Back to zoom out). Routes are URL hashes (`#/ch/ID`, `#/c/ID/CID`). Phones get a concept list under the ring.
- **Add content:** a subject joins the site by having `study-pack/web/` with `meta.json` (stages, chapters, outline `concepts` for chapters not yet drawn, edges), `figures.py` (`ALL = {name: fn → SVG}`) and `content/NN-*.md` split into concepts by `@@ id | Title | kind | gist` lines.
- **Syntax** (on top of Markdown): see the docstring of `build.py` — `[[fig:name|caption|w=60|steps=3]]`, `[[map:A > B|here=1]]`, `:::q/trap/check/note/key`, `:::reveal` (hidden answer), `$$ … $$`.
- **Look:** `static/style.css` (light + dark tokens; figure SVGs are styled by class so they follow the theme), `static/map.css` + `static/map.js` (the map: layout, camera, cards), `static/app.js` (theme toggle, figure steppers).
- Pilot: Digital Electronics ch. 1 (`subjects/sem-3/04-digital-electronics/study-pack/web/`, answers machine-checked by its `verify.py`). Design history: `_PARKED-visual-study-packs.md`.
