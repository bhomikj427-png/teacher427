/* Site v2 · session 2 rework: the river. Throwaway prototype, judged by look.
   L0 (chapters) and L1 (one chapter's concepts) share ONE river engine: the page waits for an input, and each input
   lets the water flow on to the next stop, whose priming card appears beside it. L2 is a sprint (content only, a way
   out, one small step at a time). L3 is the web: the full chapter map, with the concept's links revealed one per input.
   Routes:  #/  L0 · #/ch/<ch>  L1 · #/c/<ch>/<id>  L2 sprint · #/web[/<id>]  L3 · #/web/<id|->/e/<a>/<b>  link sprint
   Query:   l0=step|units|scroll  color=kind|unit|role|layer  prime=terms|line|q  l3=merged|split
            motion=0  dots=0  p=<concepts done>  s=<river step>  chrome=0  theme=dark  selftest=1 */
(() => {
  "use strict";
  const D = window.DATA;
  const C = {}, CH = {}, UN = {}, KD = {}, chapterOf = {}, preds = {}, succs = {}, EDGE = {}, orderIdx = {}, rel = {};
  D.kinds.forEach(k => KD[k.id] = k);
  D.concepts.forEach(c => { C[c.id] = c; preds[c.id] = []; succs[c.id] = []; });
  D.chapters.forEach(ch => { CH[ch.id] = ch; ch.concepts.forEach(i => chapterOf[i] = ch.id); });
  D.units.forEach(u => UN[u.id] = u);
  D.edges.forEach(e => { preds[e.to].push(e.from); succs[e.from].push(e.to); EDGE[e.from + ">" + e.to] = e; });
  D.order.forEach((id, k) => orderIdx[id] = k);
  D.relates.forEach(r => {
    (rel[r.a] = rel[r.a] || []).push({ other: r.b, note: r.note });
    (rel[r.b] = rel[r.b] || []).push({ other: r.a, note: r.note });
  });
  const unitOf = id => "u" + C[id].unit;

  // ------------------------------------------------------------------ settings (prototype variants)
  const Q = new URLSearchParams(location.search);
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const S = {
    l0: Q.get("l0") || "step", color: Q.get("color") || "kind", prime: Q.get("prime") || "terms", l3: Q.get("l3") || "merged",
    motion: Q.get("motion") !== "0" && !reduce, dots: Q.get("dots") !== "0", chrome: Q.get("chrome") !== "0",
    p: Q.has("p") ? +Q.get("p") : null, s: Q.has("s") ? +Q.get("s") : null,
  };
  function saveQ() {
    const q = new URLSearchParams();
    q.set("l0", S.l0); q.set("color", S.color); q.set("prime", S.prime); q.set("l3", S.l3);
    if (!S.motion) q.set("motion", "0");
    if (!S.dots) q.set("dots", "0");
    if (S.p != null) q.set("p", S.p);
    if (!S.chrome) q.set("chrome", "0");
    history.replaceState(null, "", "?" + q + location.hash);
  }

  // ------------------------------------------------------------------ progress (navigation state, never a mastery record)
  let done = new Set(), doneL = new Set(), pos = {};
  const store = {
    get(k, d) { try { const v = localStorage.getItem("v2r-" + k); return v ? JSON.parse(v) : d; } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem("v2r-" + k, JSON.stringify(v)); } catch (e) { } },
  };
  function load() {
    done = new Set(store.get("done", [])); doneL = new Set(store.get("links", [])); pos = store.get("pos", {});
    if (S.p != null) { done = new Set(D.order.slice(0, S.p)); pos = {}; }
  }
  const persist = () => { store.set("done", [...done]); store.set("links", [...doneL]); store.set("pos", pos); };
  const isDone = id => done.has(id);
  const chDone = ch => ch.concepts.filter(isDone).length;
  const linkKey = l => l.type === "relates" ? [l.a, l.b].sort().join("~") : l.a + ">" + l.b;

  // ------------------------------------------------------------------ helpers
  const $ = s => document.querySelector(s);
  const NS = "http://www.w3.org/2000/svg";
  function el(tag, attrs, parent, text) {
    const n = document.createElementNS(NS, tag);
    for (const k in attrs || {}) n.setAttribute(k, attrs[k]);
    if (text != null) n.textContent = text;
    if (parent) parent.appendChild(n);
    return n;
  }
  function h(tag, attrs, html) {
    const n = document.createElement(tag);
    for (const k in attrs || {}) { if (k === "class") n.className = attrs[k]; else n.setAttribute(k, attrs[k]); }
    if (html != null) n.innerHTML = html;
    return n;
  }
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const narrow = () => innerWidth < 760;
  const clamp = (x, a, b) => Math.max(a, Math.min(b, x));
  const short = (t, n) => t.length > n ? t.slice(0, n - 1).trimEnd() + "…" : t;
  function basis(p) {  // d3 curveBasis through dagre's edge points
    if (p.length < 3) return `M${p[0].x},${p[0].y}L${p[p.length - 1].x},${p[p.length - 1].y}`;
    let d = `M${p[0].x},${p[0].y}`, x0 = p[0].x, y0 = p[0].y, x1 = p[1].x, y1 = p[1].y;
    d += `L${(5 * x0 + x1) / 6},${(5 * y0 + y1) / 6}`;
    for (let i = 2; i < p.length; i++) {
      const x = p[i].x, y = p[i].y;
      d += `C${(2 * x0 + x1) / 3},${(2 * y0 + y1) / 3},${(x0 + 2 * x1) / 3},${(y0 + 2 * y1) / 3},${(x0 + 4 * x1 + x) / 6},${(y0 + 4 * y1 + y) / 6}`;
      x0 = x1; y0 = y1; x1 = x; y1 = y;
    }
    return d + `C${(2 * x0 + x1) / 3},${(2 * y0 + y1) / 3},${(x0 + 2 * x1) / 3},${(y0 + 2 * y1) / 3},${x1},${y1}`;
  }
  function dag(graph) {
    const g = new dagre.graphlib.Graph();
    g.setGraph(Object.assign({ rankdir: "TB", marginx: 40, marginy: 40 }, graph));
    g.setDefaultEdgeLabel(() => ({}));
    return g;
  }
  // The staircase (learner, 2026-10-01: "for every map i feel very lost"): dagre keeps the river's shape sideways,
  // but every stop sits strictly lower than the stop before it in teaching order, so reading top to bottom IS the
  // numerical order. Stops dagre put on one row become a gentle stair; edges are redrawn as downward curves.
  const STAIR = 44;
  function staircase(g, ids) {
    const pos = {};
    let prev = -Infinity;
    ids.forEach(id => { const n = g.node(id); const y = Math.max(n.y, prev + STAIR); pos[id] = { x: n.x, y }; prev = y; });
    const path = (a, b) => {
      const A = pos[a], B = pos[b], d = (B.y - A.y) * 0.55;
      return `M${A.x},${A.y} C${A.x},${A.y + d} ${B.x},${B.y - d} ${B.x},${B.y}`;
    };
    return { P: id => pos[id], W: g.graph().width, H: Math.max(g.graph().height, prev + 44), path };
  }
  function restart(node, cls) { node.classList.remove(cls); void node.getBoundingClientRect(); node.classList.add(cls); }

  // ------------------------------------------------------------------ colour modes
  const KIND_ORDER = D.kinds.map(k => k.id);
  function mixOf(ids) {
    const n = {}; ids.forEach(i => n[C[i].kind] = (n[C[i].kind] || 0) + 1);
    return KIND_ORDER.filter(k => n[k]).map(k => ({ k, n: n[k], c: `var(--k-${k})` }));
  }
  const dominant = mix => mix.slice().sort((a, b) => b.n - a.n)[0].c;
  const layerCol = n => `var(--l${n})`;
  // role (SITE-V2-DRAFT §2): trunk = base chapter; leaf = one visible connection; node = two or more (state-dependent, §2.1)
  const roleOf = (trunk, vdeg) => trunk ? "trunk" : vdeg >= 2 ? "node" : "leaf";
  function legend(layer) {
    if (S.color === "kind") return D.kinds.map(k => `<span><i style="background:var(--k-${k.id})"></i>${k.label}</span>`).join("");
    if (S.color === "unit") return D.units.map(u => `<span><i style="background:var(--u-${u.id})"></i>${u.n}</span>`).join("");
    if (S.color === "role") return ["trunk", "node", "leaf"].map(r => `<span><i style="background:var(--r-${r})"></i>${r}</span>`).join("") +
      `<span><i class="line" style="background:var(--r-edge)"></i>edge</span>`;
    return `<span><i style="background:${layerCol(layer)}"></i>L${layer} ${["subject", "chapter", "focus", "web", "link"][layer]}</span>`;
  }

  // ------------------------------------------------------------------ the river engine (L0 and L1)
  let active = null;         // the river (or web) currently taking keyboard input
  let firstStep = S.s;       // screenshot aid: ?s= sets the first river's step
  function river(host, spec) {
    const N = spec.stops.length, idx = {};
    spec.stops.forEach((s, i) => idx[s.id] = i);
    const phone = narrow();
    const g = dag({ nodesep: phone ? 30 : spec.nodesep || 80, ranksep: phone ? 46 : 84 });
    spec.stops.forEach(s => g.setNode(s.id, { width: 36, height: 30 }));
    spec.edges.forEach(([a, b]) => g.setEdge(a, b));
    dagre.layout(g);
    const L = staircase(g, spec.stops.map(s => s.id));
    const GW = L.W, GH = L.H, P = L.P;

    host.innerHTML = "";
    const scroll = spec.input === "scroll";
    const STEP = 90;
    let outer = host;
    if (scroll) { outer = h("div", { class: "rv-scroll" }); host.appendChild(outer); }
    const root = h("div", { class: "rv" });
    outer.appendChild(root);
    if (scroll) outer.appendChild(h("div", { class: "rv-spacer", style: `height:${(N - 1) * STEP}px` }));
    const box = h("div", { class: "rv-river" }), cam = h("div", { class: "rv-cam" });
    const svg = el("svg", { class: "rv-svg", width: GW, height: GH, viewBox: `0 0 ${GW} ${GH}` });
    cam.appendChild(svg); box.appendChild(cam); root.appendChild(box);
    const hint = h("div", { class: "rv-hint" }); box.appendChild(hint);
    const capBox = h("div", { class: "rv-cap" }), cap = h("div", { class: "cap" });
    capBox.appendChild(cap); root.appendChild(capBox);
    (phone ? box : capBox).appendChild(h("div", { class: "rv-legend" }, legend(spec.layer)));
    if (!phone) box.style.width = Math.max(Math.min(460, innerWidth - 470), Math.min(GW + 48, innerWidth - 470)) + "px";

    const gE = el("g", {}, svg), gT = el("g", {}, svg), gS = el("g", {}, svg);
    const edges = spec.edges.map(([a, b]) => {
      const p = el("path", { class: "e", d: L.path(a, b) }, gE);
      return { a, b, p };
    });
    edges.forEach(e => e.p.style.setProperty("--len", Math.ceil(e.p.getTotalLength() || 400)));
    const nodes = spec.stops.map((s, i) => {
      const { x, y } = P(s.id);
      const n = el("g", { class: "st hid", transform: `translate(${x},${y})` }, gS);
      el("circle", { class: "halo", r: 22 }, n);
      el("circle", { class: "ghost-c", r: 16 }, n);
      const core = el("g", { class: "core" }, n);
      const fill = el("circle", { class: "fill", r: 20 }, core);
      const ring = el("g", { class: "ring" }, core);
      el("circle", { class: "trunkring", r: 26 }, core);
      const num = el("text", { class: "num", "text-anchor": "middle", y: 4.5 }, n, s.n);
      const lab = el("text", { class: "lab", x: 0, y: 25, "text-anchor": "middle" }, n, short(s.label, spec.labelMax || 22));
      el("circle", { class: "hit", r: 22 }, n);
      n.addEventListener("click", ev => { ev.stopPropagation(); onStop(i); });
      return { n, fill, ring, num, lab };
    });

    let K = 0, cur = 0, overview = false, idle = null;
    const saved = pos[spec.key];
    if (firstStep != null) { K = cur = clamp(firstStep, 0, N - 1); firstStep = null; }
    else if (saved) { K = clamp(saved.k, 0, N - 1); cur = clamp(saved.cur == null ? K : saved.cur, 0, K); }
    if (spec.startAt != null) { cur = clamp(spec.startAt, 0, N - 1); K = Math.max(K, cur); }

    function paint(i, vdeg) {
      const s = spec.stops[i], nd = nodes[i], p = spec.paint(s, vdeg);
      nd.fill.setAttribute("style", `fill:${p.fill};stroke:${p.fill}`);
      nd.n.classList.toggle("has-ring", !!p.ring);
      nd.n.classList.toggle("trunk-mark", !!p.trunk);
      nd.n.querySelector(".halo").setAttribute("style", `stroke:${p.fill}`);
      nd.ring.innerHTML = "";
      if (p.ring) {
        el("circle", { class: "ringbg", r: 20 }, nd.ring);
        const tot = p.ring.reduce((a, m) => a + m.n, 0), R = 17, L = 2 * Math.PI * R;
        let off = 0;
        p.ring.forEach(m => {
          const len = L * m.n / tot;
          el("circle", { r: R, fill: "none", "stroke-width": 6, style: `stroke:${m.c}`, transform: "rotate(-90)",
            "stroke-dasharray": `${Math.max(0, len - 1.5)} ${L}`, "stroke-dashoffset": -off }, nd.ring);
          off += len;
        });
        nd.num.setAttribute("style", "fill:var(--ink)");
      } else nd.num.removeAttribute("style");
    }

    function render(anim) {
      const end = K === N - 1;
      const vdeg = {};
      edges.forEach(e => {
        const vis = idx[e.a] <= K && idx[e.b] <= K;
        if (vis) { vdeg[e.a] = (vdeg[e.a] || 0) + 1; vdeg[e.b] = (vdeg[e.b] || 0) + 1; }
      });
      if (spec.extraDeg) spec.stops.forEach((s, i) => { if (i <= K) vdeg[s.id] = (vdeg[s.id] || 0) + spec.extraDeg(s); });
      spec.stops.forEach((s, i) => {
        const nd = nodes[i];
        const state = i === cur && !overview ? "cur" : i <= K ? "past" : i === K + 1 ? "ghost" : "hid";
        const labOn = state === "past" && (overview || i === cur - 1 || i === K - 1);
        nd.n.setAttribute("class", `st ${state}${s.done ? " done" : ""}${labOn ? " lab-on" : ""}`);
        nd.lab.textContent = overview && phone ? String(s.n) : short(s.label, overview ? 20 : spec.labelMax || 22);
        paint(i, vdeg[s.id] || 0);
      });
      edges.forEach(e => {
        const ia = idx[e.a], ib = idx[e.b];
        const col = spec.edgeColor(spec.stops[ib], spec.stops[ia]);
        e.p.setAttribute("style", `stroke:${col};--len:${e.p.style.getPropertyValue("--len")}`);
        let cls = "e";
        if (ia <= K && ib <= K) cls += ib === cur && !overview ? " on live" : !overview && ib < K - 2 && ib < cur - 2 ? " on old" : " on";
        else if (ib === K + 1 && ia <= K && !overview) cls += " trickle";
        e.p.setAttribute("class", cls);
        if (anim && ib === K && ia <= K) restart(e.p, "draw");
      });
      if (anim) restart(nodes[K].n, "pop");
      tributaries();
      camera();
      caption();
      hints();
      pos[spec.key] = { k: K, cur }; persist();
    }

    function tributaries() {
      gT.innerHTML = "";
      if (!spec.tribs || overview) return;
      const s = spec.stops[cur], list = spec.tribs(s);
      const { x, y } = P(s.id);
      list.forEach((t, j) => {
        const sx = x - 120 + j * 8, sy = y - 64 - j * 22;
        const gg = el("g", { class: "trib-g" }, gT);
        el("path", { class: "trib", d: `M${sx},${sy} C${sx + 60},${sy} ${x - 40},${y - 8} ${x - 20},${y}` }, gg);
        el("text", { class: "trib-t", x: sx - 6, y: sy + 4, "text-anchor": "end" }, gg, t.label);
      });
    }

    function camera() {
      const bw = box.clientWidth, bh = box.clientHeight;
      let sc = Math.min(1, (bw - 24) / GW);
      let ty;
      if (overview) { sc = Math.min(sc, (bh - 110) / GH); ty = (bh - GH * sc) / 2; }
      else ty = bh * (phone ? 0.42 : 0.55) - P(spec.stops[cur].id).y * sc;
      const tx = (bw - GW * sc) / 2;
      svg.style.setProperty("--inv", (1 / sc).toFixed(3));
      cam.style.transform = `translate(${tx}px,${ty}px) scale(${sc})`;
    }

    function caption() {
      cap.innerHTML = "";
      const inner = overview && spec.endCaption ? spec.endCaption(api) : spec.caption(spec.stops[cur], api, cur);
      inner.classList.add("ci");
      cap.appendChild(inner);
    }

    function hints() {
      clearTimeout(idle);
      hint.classList.remove("wait");
      const end = K === N - 1;
      if (end) {
        hint.innerHTML = `<span>${overview ? "tap a stop to open it" : "the whole flow"}</span>` +
          `<button class="mini" data-a="restart">↺ again</button>` + (overview ? "" : `<button class="mini" data-a="all">⤢ see it all</button>`);
      } else {
        hint.innerHTML = `<button class="nx" data-a="next" aria-label="Next stop">▾</button>` +
          `<span>${scroll ? "scroll" : phone ? "tap" : "space · ↓"}</span>` +
          `<button class="mini" data-a="all" title="Skip to the whole map">⤢ all</button>`;
        idle = setTimeout(() => hint.classList.add("wait"), 1400);
      }
      hint.querySelectorAll("[data-a]").forEach(b => b.addEventListener("click", ev => {
        ev.stopPropagation();
        ({ next, restart: restartR, all }[b.dataset.a])();
      }));
    }

    function step(to, anim) {
      to = clamp(to, 0, N - 1);
      if (scroll) { outer.scrollTo({ top: to * STEP, behavior: S.motion ? "smooth" : "auto" }); return; }
      const fwd = to > K;
      overview = false; K = to; cur = to;
      render(fwd && S.motion && anim !== false);
    }
    function next() {
      if (cur < K && !overview) { cur = K; render(false); return; }
      if (K === N - 1) { overview = true; render(false); return; }
      step(K + 1);
    }
    function back() { if (overview) { overview = false; render(false); return; } step(K - 1, false); }
    function restartR() { overview = false; if (scroll) outer.scrollTo({ top: 0 }); K = 0; cur = 0; render(S.motion); }
    function all() {
      if (scroll) { outer.scrollTo({ top: (N - 1) * STEP }); }
      K = N - 1; cur = N - 1; overview = true; render(false);
    }
    function onStop(i) {
      if (i > K) { if (i === K + 1) next(); return; }
      if (i === cur && !overview) { spec.open(spec.stops[i]); return; }
      overview = false; cur = i; render(false);
    }
    const api = { next, back, all, open: () => spec.open(spec.stops[cur]), stops: spec.stops };

    box.addEventListener("click", () => next());
    if (scroll) {
      outer.scrollTop = K * STEP;
      outer.addEventListener("scroll", () => {
        const k = clamp(Math.round(outer.scrollTop / STEP), 0, N - 1);
        const atEnd = outer.scrollTop >= (N - 1) * STEP - 2;
        if (k !== K) { const fwd = k > K; K = k; cur = k; overview = false; render(fwd && S.motion); }
        else if (atEnd && !overview && k === N - 1 && spec.overviewOnScrollEnd) { overview = true; render(false); }
      });
    }
    active = {
      key(e) {
        if (["ArrowDown", "PageDown", "ArrowRight", " "].includes(e.key)) { e.preventDefault(); if (scroll) outer.scrollBy({ top: STEP, behavior: "smooth" }); else next(); }
        else if (["ArrowUp", "PageUp", "ArrowLeft"].includes(e.key)) { e.preventDefault(); if (scroll) outer.scrollBy({ top: -STEP, behavior: "smooth" }); else back(); }
        else if (e.key === "Enter") { e.preventDefault(); if (!overview) spec.open(spec.stops[cur]); }
        else if (e.key === "Home") restartR();
        else if (e.key === "End") all();
      },
      resize() { camera(); },
      state: () => ({ K, cur, N, overview }),
      next, back, all,
    };
    render(S.motion && K === 0 && !saved);
    return active;
  }

  // ------------------------------------------------------------------ caption building blocks (the priming card)
  function primeBlock(q, line, terms, key) {
    const w = h("div");
    const body = () => {
      const b = h("div");
      if (S.prime === "line") b.appendChild(h("p", { class: "cap-line" }, esc(line)));
      else b.appendChild(h("ul", { class: "terms" }, terms.map(t => `<li><b>${esc(t.t)}</b><span>${esc(t.g)}</span></li>`).join("")));
      return b;
    };
    if (S.prime === "q" && q) {
      w.appendChild(h("p", { class: "cap-q" }, esc(q)));
      if (revealed.has(key)) w.appendChild(body());
      else {
        const rb = h("button", { class: "revealb", type: "button" }, "guess, then reveal the words");
        rb.addEventListener("click", ev => { ev.stopPropagation(); revealed.add(key); rb.replaceWith(body()); });
        w.appendChild(rb);
      }
    } else w.appendChild(body());
    return w;
  }
  const revealed = new Set();
  function mixBar(ids) {
    if (S.color !== "kind") return null;
    const m = mixOf(ids), tot = ids.length;
    return h("div", { class: "mixbar", title: m.map(x => `${x.n} ${KD[x.k].label.toLowerCase()}`).join(" · ") },
      m.map(x => `<span style="flex:${x.n / tot};background:${x.c}"></span>`).join(""));
  }
  function actions(label, fn, extra) {
    const a = h("div", { class: "cap-act" });
    const b = h("button", { class: "go", type: "button" }, label);
    b.addEventListener("click", ev => { ev.stopPropagation(); fn(); });
    a.appendChild(b);
    if (!narrow()) a.appendChild(h("span", { class: "kbd" }, "enter"));
    (extra || []).forEach(x => a.appendChild(x));
    return a;
  }

  // ------------------------------------------------------------------ L0: the subject as a river of chapters
  function paintChapterLike(ids, trunk, vdeg, unitId, layer) {
    const mix = mixOf(ids);
    if (S.color === "kind") return { fill: dominant(mix), ring: mix };
    if (S.color === "unit") return { fill: `var(--u-${unitId})` };
    if (S.color === "role") return { fill: `var(--r-${roleOf(trunk, vdeg)})`, trunk };
    return { fill: layerCol(layer) };
  }
  function edgeColChapter(ids, unitId, layer) {
    if (S.color === "kind") return dominant(mixOf(ids));
    if (S.color === "unit") return `var(--u-${unitId})`;
    if (S.color === "role") return "var(--r-edge)";
    return layerCol(layer);
  }
  function chapterCaption(ch) {
    const w = h("div");
    const n = chDone(ch);
    w.appendChild(h("div", { class: "cap-meta" }, `<span>Ch ${ch.n}</span><span>·</span><span>${ch.concepts.length} concepts</span>` +
      (ch.trunk ? `<span>·</span><span>the base</span>` : "") + (n ? `<span>·</span><span class="done-tag">${n}/${ch.concepts.length} done</span>` : "")));
    w.appendChild(h("h2", {}, esc(ch.title)));
    const mb = mixBar(ch.concepts); if (mb) w.appendChild(mb);
    w.appendChild(primeBlock(ch.q, ch.line, ch.terms, ch.id));
    w.appendChild(actions("Open chapter ▸", () => go(`#/ch/${ch.id}`)));
    return w;
  }
  function renderL0(view) {
    setLayer(0, []);
    if (S.l0 === "units") return renderUnits(view);
    const stops = D.chapters.map(ch => ({ id: ch.id, n: ch.n, label: ch.title, ch, done: chDone(ch) === ch.concepts.length }));
    return river(view, {
      key: "L0", layer: 0, stops, input: S.l0 === "scroll" ? "scroll" : "step", overviewOnScrollEnd: true,
      edges: D.chapterEdges.filter(e => e.direct).map(e => [e.from, e.to]),
      paint: (s, vdeg) => paintChapterLike(s.ch.concepts, s.ch.trunk, vdeg, s.ch.unitId, 0),
      edgeColor: s => edgeColChapter(s.ch.concepts, s.ch.unitId, 0),
      caption: s => chapterCaption(s.ch),
      endCaption: () => {
        const w = h("div");
        w.appendChild(h("div", { class: "cap-meta" }, `${D.chapters.length} chapters · ${D.concepts.length} concepts`));
        w.appendChild(h("h2", {}, esc(D.subject.title)));
        w.appendChild(h("p", { class: "cap-line" }, "The whole flow, top to bottom. Tap any stop to open that chapter."));
        const wb = h("button", { class: "go soft", type: "button" }, "The web · L3");
        wb.addEventListener("click", ev => { ev.stopPropagation(); go("#/web"); });
        w.appendChild(actions("Start at Ch 1 ▸", () => go("#/ch/ch1"), [wb]));
        return w;
      },
      open: s => go(`#/ch/${s.id}`),
    });
  }
  function renderUnits(view) {
    const cu = {};
    D.chapters.forEach(ch => cu[ch.id] = ch.unitId);
    const pairs = new Set();
    D.chapterEdges.forEach(e => { const a = cu[e.from], b = cu[e.to]; if (a !== b) pairs.add(a + ">" + b); });
    // transitive reduction on the unit graph, so only direct flows are drawn
    const succ = {}; [...pairs].forEach(p => { const [a, b] = p.split(">"); (succ[a] = succ[a] || []).push(b); });
    const reach = (a, b, skip) => { const st = (succ[a] || []).filter(x => x !== skip), seen = new Set();
      while (st.length) { const x = st.pop(); if (x === b) return true; if (!seen.has(x)) { seen.add(x); st.push(...(succ[x] || [])); } } return false; };
    const edges = [...pairs].map(p => p.split(">")).filter(([a, b]) => !reach(a, b, b));
    const idsOf = u => u.chapters.flatMap(c => CH[c].concepts);
    const stops = D.units.map(u => ({ id: u.id, n: u.n.slice(1), label: u.title, u, done: idsOf(u).every(isDone) }));
    return river(view, {
      key: "L0u", layer: 0, stops, input: "step", edges, nodesep: 150, labelMax: 26,
      paint: (s, vdeg) => paintChapterLike(idsOf(s.u), s.u.id === "u0", vdeg, s.u.id, 0),
      edgeColor: s => edgeColChapter(idsOf(s.u), s.u.id, 0),
      caption: s => {
        const u = s.u, w = h("div"), ids = idsOf(u);
        w.appendChild(h("div", { class: "cap-meta" }, `<span>${u.n}</span><span>·</span><span>${u.chapters.length} chapter${u.chapters.length > 1 ? "s" : ""}</span>` +
          `<span>·</span><span>${ids.length} concepts</span>`));
        w.appendChild(h("h2", {}, esc(u.title)));
        const mb = mixBar(ids); if (mb) w.appendChild(mb);
        w.appendChild(primeBlock(u.q, u.line, u.terms, u.id));
        const chips = h("div", { class: "chips" });
        u.chapters.forEach(c => {
          const b = h("button", { type: "button" }, `<span class="cn">${CH[c].n}</span>${esc(CH[c].title)}`);
          b.addEventListener("click", ev => { ev.stopPropagation(); go(`#/ch/${c}`); });
          chips.appendChild(b);
        });
        w.appendChild(chips);
        return w;
      },
      open: s => go(`#/ch/${s.u.chapters.find(c => chDone(CH[c]) < CH[c].concepts.length) || s.u.chapters[0]}`),
    });
  }

  // ------------------------------------------------------------------ L1: the same river, inside one chapter
  function outsidePreds(id, chId) {
    const by = {};
    preds[id].filter(p => chapterOf[p] !== chId).forEach(p => (by[chapterOf[p]] = by[chapterOf[p]] || []).push(p));
    return Object.keys(by).sort((a, b) => CH[a].n - CH[b].n).map(c => ({ ch: c, ids: by[c] }));
  }
  function predictFor(id) {
    const e = preds[id].map(p => EDGE[p + ">" + id]).find(x => x.predict);
    return e ? e.predict : null;
  }
  function kindChip(c) {
    const k = KD[c.kind];
    const col = S.color === "kind" ? `var(--k-${c.kind})` : "var(--muted)";
    return `<span class="kchip" style="--c:${col}">${k.label} <em>· ${k.verb}</em></span>`;
  }
  function conceptCaption(c, chId) {
    const w = h("div");
    w.appendChild(h("div", { class: "cap-meta" }, kindChip(c) + (isDone(c.id) ? `<span class="done-tag">✓ done</span>` : "")));
    w.appendChild(h("h2", {}, esc(c.title)));
    const q = S.prime === "q" ? predictFor(c.id) : null;
    if (q && !revealed.has(c.id)) {
      w.appendChild(h("p", { class: "cap-q" }, esc(q)));
      const rb = h("button", { class: "revealb", type: "button" }, "guess, then reveal");
      rb.addEventListener("click", ev => { ev.stopPropagation(); revealed.add(c.id); rb.replaceWith(h("p", { class: "cap-line" }, esc(c.gist))); });
      w.appendChild(rb);
    } else w.appendChild(h("p", { class: "cap-line" }, esc(c.gist)));
    const outs = outsidePreds(c.id, chId);
    if (outs.length) w.appendChild(h("div", { class: "cap-from" }, "builds on " + outs.map(o => `Ch ${CH[o.ch].n}`).join(" · ")));
    const extra = [];
    if (isDone(c.id)) {
      const wb = h("button", { class: "go soft", type: "button" }, "Connect it · web");
      wb.addEventListener("click", ev => { ev.stopPropagation(); go(`#/web/${c.id}`); });
      extra.push(wb);
    }
    w.appendChild(actions(isDone(c.id) ? "Sprint again ▸" : "Sprint ▸", () => go(`#/c/${chId}/${c.id}`), extra));
    return w;
  }
  function renderL1(view, chId) {
    const ch = CH[chId];
    setLayer(1, [[`#/ch/${chId}`, `Ch ${ch.n} · ${ch.title}`]]);
    const stops = ch.concepts.map((id, i) => ({ id, n: i + 1, label: C[id].title, c: C[id], done: isDone(id) }));
    const inside = D.edges.filter(e => chapterOf[e.from] === chId && chapterOf[e.to] === chId).map(e => [e.from, e.to]);
    const startAt = pendingAdvance[chId]; delete pendingAdvance[chId];
    return river(view, {
      key: "L1:" + chId, layer: 1, stops, edges: inside, input: "step", nodesep: 130, startAt,
      extraDeg: s => outsidePreds(s.id, chId).length,
      tribs: s => outsidePreds(s.id, chId).map(o => ({ label: `Ch ${CH[o.ch].n} · ${short(C[o.ids[0]].title, 18)}` })),
      paint: (s, vdeg) => {
        if (S.color === "kind") return { fill: `var(--k-${s.c.kind})` };
        if (S.color === "unit") return { fill: `var(--u-${unitOf(s.id)})` };
        if (S.color === "role") return { fill: `var(--r-${roleOf(false, vdeg)})` };
        return { fill: layerCol(1) };
      },
      edgeColor: s => S.color === "kind" ? `var(--k-${s.c.kind})` : S.color === "unit" ? `var(--u-${unitOf(s.id)})` :
        S.color === "role" ? "var(--r-edge)" : layerCol(1),
      caption: s => conceptCaption(s.c, chId),
      endCaption: () => {
        const w = h("div"), n = chDone(ch);
        const outs = [...new Set(ch.concepts.flatMap(i => succs[i]).filter(s => chapterOf[s] !== chId).map(s => chapterOf[s]))]
          .sort((a, b) => CH[a].n - CH[b].n);
        w.appendChild(h("div", { class: "cap-meta" }, `Ch ${ch.n} · ${n}/${ch.concepts.length} done`));
        w.appendChild(h("h2", {}, esc(ch.title)));
        w.appendChild(h("p", { class: "cap-line" }, outs.length ? "Flows on into " + outs.map(o => `Ch ${CH[o].n} ${esc(CH[o].title)}`).join(", ") + "." : "An end of the flow."));
        const nx = D.chapters[ch.n];
        w.appendChild(actions(nx ? `Next: Ch ${nx.n} ▸` : "Back to the subject ▸", () => go(nx ? `#/ch/${nx.id}` : "#/")));
        return w;
      },
      open: s => go(`#/c/${chId}/${s.id}`),
    });
  }
  const pendingAdvance = {};

  // ------------------------------------------------------------------ L2: the sprint (content only, one small step at a time)
  function splitBody(html) {
    const tmp = h("div", {}, html), steps = [];
    let textBuf = [];
    const flush = () => { if (textBuf.length) { steps.push({ t: "block", html: textBuf.join("") }); textBuf = []; } };
    [...tmp.children].forEach(n => {
      if (n.matches("details.reveal")) {
        flush();
        let q = n.querySelector("summary").textContent.replace(/^Quick check:\s*/i, "");
        q = q.charAt(0).toUpperCase() + q.slice(1);
        n.querySelector("summary").remove();
        steps.push({ t: "check", q, a: n.innerHTML });
      } else if (n.matches("figure, table, .eq")) { flush(); steps.push({ t: "block", html: n.outerHTML }); }
      else {
        textBuf.push(n.outerHTML);
        if (textBuf.join("").replace(/<[^>]+>/g, "").length > 200) flush();
      }
    });
    flush();
    return steps;
  }
  function conceptSteps(cid) {
    const c = C[cid], steps = [];
    const q = predictFor(cid);
    if (q) steps.push({ t: "guess", q });
    steps.push({ t: "hook" });
    if (c.body) steps.push(...splitBody(c.body));
    else steps.push({ t: "soon" });
    steps.push({ t: "finish" });
    return steps;
  }
  const sp = $("#sprint");
  function sprint(opts) {
    // opts: steps, draw(step, node), onExit, onFinish(node)
    sp.hidden = false; sp.innerHTML = "";
    document.body.classList.add("in-sprint");
    const x = h("button", { class: "sp-x", type: "button", "aria-label": "Leave the sprint", title: "Leave (Esc)" }, "×");
    x.addEventListener("click", opts.onExit);
    const stage = h("div", { class: "sp-stage" }), foot = h("div", { class: "sp-foot" });
    sp.appendChild(x); sp.appendChild(stage); sp.appendChild(foot);
    let i = 0, pending = null, idle = null;
    function show(dir) {
      stage.innerHTML = ""; pending = null;
      const st = opts.steps[i], node = h("div", { class: "sp-step" + (dir < 0 ? " back" : "") });
      opts.draw(st, node, fn => pending = fn);
      stage.appendChild(node); stage.scrollTop = 0;
      if (window.initSteppers) window.initSteppers(node);
      foot.innerHTML = "";
      if (S.dots) foot.appendChild(h("div", { class: "sp-dots" }, opts.steps.map((_, j) => `<i class="${j < i ? "on" : j === i ? "at" : ""}"></i>`).join("")));
      if (st.t !== "finish") {
        const nb = h("button", { class: "sp-next", type: "button", "aria-label": "Next step" }, "▸");
        nb.addEventListener("click", ev => { ev.stopPropagation(); fwd(); });
        foot.appendChild(nb);
        clearTimeout(idle); idle = setTimeout(() => nb.classList.add("wait"), 2500);
      }
    }
    function fwd() { if (pending) { const f = pending; pending = null; f(); return; } if (i < opts.steps.length - 1) { i++; show(1); } }
    function bwd() { if (i > 0) { i--; show(-1); } }
    stage.addEventListener("click", ev => {
      if (ev.target.closest("button, a, summary, details, .stepper, input")) return;
      if (opts.steps[i].t !== "finish") fwd();
    });
    active = {
      key(e) {
        if (e.key === "Escape") { e.preventDefault(); opts.onExit(); }
        else if ([" ", "ArrowRight", "ArrowDown", "Enter"].includes(e.key)) {
          e.preventDefault();
          if (opts.steps[i].t === "finish") { const g = sp.querySelector(".go"); if (g && e.key === "Enter") g.click(); } else fwd();
        } else if (["ArrowLeft", "ArrowUp", "Backspace"].includes(e.key)) { e.preventDefault(); bwd(); }
      },
      resize() { }, state: () => ({ i, n: opts.steps.length }), next: fwd,
    };
    const start = +(Q.get("step") || 0); i = clamp(start, 0, opts.steps.length - 1);
    show(1);
  }
  function closeSprint() { sp.hidden = true; sp.innerHTML = ""; document.body.classList.remove("in-sprint"); }

  function renderSprint(chId, cid) {
    const c = C[cid];
    document.body.dataset.layer = 2;
    const steps = conceptSteps(cid);
    sprint({
      steps,
      onExit: () => go(`#/ch/${chId}`),
      draw(st, node, setPending) {
        if (st.t === "guess") {
          node.innerHTML = `<div class="sp-lab">guess first</div><p class="sp-q">${esc(st.q)}</p><p class="sp-hint">Answer it in your head or on paper, then go on.</p>`;
        } else if (st.t === "hook") {
          node.innerHTML = `<div>${kindChip(c)}</div><h1>${esc(c.title)}</h1><p class="sp-gist">${esc(c.gist)}</p>`;
        } else if (st.t === "block") {
          node.appendChild(h("div", { class: "blk content" + (/^<(figure|table|div)/.test(st.html) ? "" : " blk-text") }, st.html));
        } else if (st.t === "check") {
          node.innerHTML = `<div class="sp-lab">check</div><p class="sp-q">${esc(st.q)}</p>`;
          const b = h("button", { class: "revealb", type: "button" }, "answer, then reveal");
          const reveal = () => { b.replaceWith(h("div", { class: "sp-ans" }, st.a)); };
          b.addEventListener("click", ev => { ev.stopPropagation(); reveal(); setPending(null); });
          node.appendChild(b);
          setPending(reveal);
        } else if (st.t === "soon") {
          node.innerHTML = `<p class="sp-soon">The full card for this concept is written by content engine v2 (session 4): the real picture, the mechanism, right vs wrong, why it matters, and a check, one small step each.<br><br>The K-map chapter (Ch 3) has real cards now, so the sprint can be judged there.</p>`;
        } else if (st.t === "finish") {
          done.add(cid); S.p = null; persist(); saveQ();
          const k = CH[chId].concepts.indexOf(cid);
          pendingAdvance[chId] = Math.min(k + 1, CH[chId].concepts.length - 1);
          const nx = CH[chId].concepts[k + 1];
          node.classList.add("sp-done");
          node.innerHTML = `<div class="tick">✓</div><h1>${esc(c.title)}</h1><p class="sp-hint">${nx ? "Next on the river: " + esc(C[nx].title) : "That was the last stop in this chapter."}</p>`;
          const wb = h("button", { class: "go soft", type: "button" }, "Connect it · web");
          wb.addEventListener("click", () => go(`#/web/${cid}`));
          node.appendChild(actions("Back to the river ▸", () => go(`#/ch/${chId}`), [wb]));
        }
      },
    });
  }

  // ------------------------------------------------------------------ L3: the web
  let chapterLayout = null;
  function layoutChapters() {
    const phone = narrow();
    const g = dag({ nodesep: phone ? 30 : 80, ranksep: phone ? 46 : 84 });
    D.chapters.forEach(ch => g.setNode(ch.id, { width: 36, height: 30 }));
    D.chapterEdges.filter(e => e.direct).forEach(e => g.setEdge(e.from, e.to));
    dagre.layout(g);
    return staircase(g, D.chapters.map(ch => ch.id));
  }
  function linksOf(cid) {
    if (!cid) return D.relates.map(r => ({ a: r.a, b: r.b, type: "relates", text: r.note }));
    const me = chapterOf[cid], L = [];
    preds[cid].filter(p => chapterOf[p] !== me).forEach(p => L.push({ a: p, b: cid, type: "needs", text: EDGE[p + ">" + cid].bridge, predict: EDGE[p + ">" + cid].predict }));
    succs[cid].filter(s => chapterOf[s] !== me).forEach(s => L.push({ a: cid, b: s, type: "feeds", text: EDGE[cid + ">" + s].bridge, predict: EDGE[cid + ">" + s].predict }));
    (rel[cid] || []).forEach(r => L.push({ a: cid, b: r.other, type: "relates", text: r.note }));
    return L;
  }
  const TYPE = { needs: { lab: "needs", c: "var(--w-needs)", v: "how it leads here" }, feeds: { lab: "feeds", c: "var(--w-feeds)", v: "where it goes next" },
    relates: { lab: "relates to", c: "var(--w-relates)", v: "what they share" } };
  function renderWeb(view, cid) {
    const crumbs = cid ? [[`#/ch/${chapterOf[cid]}`, `Ch ${CH[chapterOf[cid]].n}`], [`#/web/${cid}`, C[cid].title]] : [["#/web", "the web"]];
    setLayer(3, crumbs);
    const links = linksOf(cid);
    const g = chapterLayout = layoutChapters();
    const GW = g.W, GH = g.H, P = g.P;
    view.innerHTML = "";
    const root = h("div", { class: "rv" }), box = h("div", { class: "rv-river" }), cam = h("div", { class: "rv-cam" });
    const svg = el("svg", { class: "rv-svg", width: GW, height: GH, viewBox: `0 0 ${GW} ${GH}` });
    cam.appendChild(svg); box.appendChild(cam); root.appendChild(box);
    box.appendChild(h("div", { class: "rv-legend" }, Object.values(TYPE).map(t => `<span><i class="line" style="background:${t.c}"></i>${t.lab}</span>`).join("")));
    const hint = h("div", { class: "rv-hint" }); box.appendChild(hint);
    const capBox = h("div", { class: "rv-cap" }), cap = h("div", { class: "cap" });
    capBox.appendChild(cap); root.appendChild(capBox); view.appendChild(root);
    if (!narrow()) box.style.width = Math.min(GW + 48, innerWidth - 470) + "px";
    D.chapterEdges.filter(e => e.direct).forEach(e => el("path", { class: "wm-e", d: g.path(e.from, e.to) }, svg));
    const me = cid ? chapterOf[cid] : null;
    const gL = el("g", {}, svg), gD = el("g", {}, svg), gT = el("g", {}, svg);
    D.chapters.forEach(ch => {
      const { x, y } = P(ch.id);
      el("circle", { class: "wm-dot" + (ch.id === me ? " me" : ""), cx: x, cy: y, r: ch.id === me ? 9 : 5 }, gD);
      const t = el("text", { class: "wm-lab" + (ch.id === me ? " me" : ""), x: x + 13, y: y + 4, "data-ch": ch.id }, gD, narrow() ? ch.n : short(ch.title, 20));
      el("title", {}, t, `Ch ${ch.n} ${ch.title}`);
    });
    const chLabs = [...gD.querySelectorAll(".wm-lab")];
    const paths = links.map((l, i) => {
      const A = P(chapterOf[l.a]), B = P(chapterOf[l.b]);
      let d;
      if (A === B) d = `M${A.x},${A.y} C${A.x - 70},${A.y - 60} ${A.x - 70},${A.y + 60} ${A.x},${A.y}`;
      else {
        const mx = (A.x + B.x) / 2, my = (A.y + B.y) / 2, dx = B.x - A.x, dy = B.y - A.y, len = Math.hypot(dx, dy) || 1;
        const bend = (i % 2 ? 1 : -1) * Math.min(90, len * 0.28);
        d = `M${A.x},${A.y} Q${mx - dy / len * bend},${my + dx / len * bend} ${B.x},${B.y}`;
      }
      const p = el("path", { class: `wl ${l.type}`, d, style: `stroke:${TYPE[l.type].c}` }, gL);
      p.style.setProperty("--len", Math.ceil(p.getTotalLength() || 300));
      return p;
    });
    const key = "L3:" + (cid || "all");
    let K = -1;
    if (firstStepWeb != null) { K = clamp(firstStepWeb, -1, links.length - 1); firstStepWeb = null; }
    else if (pendingWeb[key] != null) { K = pendingWeb[key]; delete pendingWeb[key]; }
    else if (pos[key]) K = clamp(pos[key].k, -1, links.length - 1);
    let idle = null;
    function tag(x, y, text, anchor) {
      const gg = el("g", { class: "wtag" }, gT);
      const t = el("text", { x, y: y + 4, "text-anchor": anchor }, gg, text);
      const bb = t.getBBox();
      gg.insertBefore(el("rect", { x: bb.x - 6, y: bb.y - 3, width: bb.width + 12, height: bb.height + 6, rx: 6 }), t);
    }
    function render(anim) {
      paths.forEach((p, i) => {
        const l = links[i];
        p.setAttribute("class", `wl ${l.type}${i < K ? " on" : ""}${i === K ? " cur" : ""}${doneL.has(linkKey(l)) ? " done" : ""}`);
        p.style.display = i <= K ? "" : "none";
        if (anim && i === K) restart(p, "fresh");
      });
      const bw = box.clientWidth, bh = box.clientHeight;
      const sc = Math.min(1, (bw - 24) / GW, (bh - 100) / GH);
      svg.style.setProperty("--inv", (1 / sc).toFixed(3));
      const touched = new Set([me]);
      links.forEach((l, i) => { if (i <= K) { touched.add(chapterOf[l.a]); touched.add(chapterOf[l.b]); } });
      chLabs.forEach(t => t.style.opacity = touched.has(t.dataset.ch) ? 1 : 0);
      gT.innerHTML = "";
      if (K >= 0) {
        const l = links[K], A = P(chapterOf[l.a]), B = P(chapterOf[l.b]);
        tag(A.x - 14, A.y - 16, short(C[l.a].title, 24), "end");
        if (A !== B) tag(B.x - 14, B.y - 16, short(C[l.b].title, 24), "end");
        else tag(A.x - 14, A.y + 26, short(C[l.b].title, 24), "end");
      } else if (cid) tag(P(me).x - 14, P(me).y - 16, short(C[cid].title, 24), "end");
      cam.style.transform = `translate(${(bw - GW * sc) / 2}px,${(bh - GH * sc) / 2}px) scale(${sc})`;
      cap.innerHTML = "";
      const w = h("div", { class: "ci" });
      if (K < 0) {
        w.appendChild(h("div", { class: "cap-meta" }, cid ? kindChip(C[cid]) : `${links.length} links across the subject`));
        w.appendChild(h("h2", {}, cid ? esc(C[cid].title) : "The web"));
        w.appendChild(h("p", { class: "cap-line" }, links.length ?
          `${links.length} link${links.length > 1 ? "s" : ""} reach out from ${cid ? "here" : "concepts in different chapters"}. Each one is a small idea of its own.` :
          "Nothing outside its chapter connects to this one."));
      } else {
        const l = links[K], T = TYPE[l.type], dn = doneL.has(linkKey(l));
        w.appendChild(h("div", { class: "cap-meta" }, `<span class="wtype" style="--c:${T.c}">${T.lab}</span><span>·</span><span>${K + 1} of ${links.length}</span>` +
          (dn ? `<span class="done-tag">✓</span>` : "")));
        w.appendChild(h("h2", {}, `${esc(C[l.a].title)} <span style="color:var(--muted)">${l.type === "relates" ? "↔" : "→"}</span> ${esc(C[l.b].title)}`));
        w.appendChild(h("div", { class: "cap-from" }, `Ch ${CH[chapterOf[l.a]].n} ${esc(CH[chapterOf[l.a]].title)} ${l.type === "relates" ? "↔" : "→"} Ch ${CH[chapterOf[l.b]].n} ${esc(CH[chapterOf[l.b]].title)}`));
        const path = `#/web/${cid || "-"}/e/${l.a}/${l.b}`;
        if (S.l3 === "merged") {
          w.appendChild(actions("Sprint this link ▸", () => go(path)));
        } else {
          w.appendChild(actions("Explain it · L4 ▸", () => go(path)));
        }
      }
      cap.appendChild(w);
      clearTimeout(idle); hint.classList.remove("wait");
      if (K < links.length - 1) {
        hint.innerHTML = `<button class="nx" data-a="next" aria-label="Next link">▾</button><span>${narrow() ? "tap" : "space · ↓"}</span>`;
        idle = setTimeout(() => hint.classList.add("wait"), 1400);
      } else hint.innerHTML = links.length ? `<span>all ${links.length} links</span><button class="mini" data-a="restart">↺ again</button>` : "";
      hint.querySelectorAll("[data-a]").forEach(b => b.addEventListener("click", ev => { ev.stopPropagation(); b.dataset.a === "next" ? nx() : (K = -1, render(false)); }));
      pos[key] = { k: K }; persist();
    }
    const nx = () => { if (K < links.length - 1) { K++; render(S.motion); } };
    const bk = () => { if (K > -1) { K--; render(false); } };
    box.addEventListener("click", nx);
    active = {
      key(e) {
        if (["ArrowDown", "ArrowRight", " "].includes(e.key)) { e.preventDefault(); nx(); }
        else if (["ArrowUp", "ArrowLeft"].includes(e.key)) { e.preventDefault(); bk(); }
        else if (e.key === "Enter" && K >= 0) { e.preventDefault(); const l = links[K]; go(`#/web/${cid || "-"}/e/${l.a}/${l.b}`); }
      },
      resize() { render(false); }, state: () => ({ K, N: links.length }), next: nx,
    };
    render(S.motion);
  }
  let firstStepWeb = null;
  const pendingWeb = {};

  function renderLinkSprint(cid, a, b) {
    const L = linksOf(cid).find(l => (l.a === a && l.b === b));
    if (!L) { go(cid ? `#/web/${cid}` : "#/web"); return; }
    const layer = S.l3 === "split" ? 4 : 3;
    document.body.dataset.layer = layer;
    const T = TYPE[L.type];
    const steps = [{ t: "pair" }, { t: "guess" }, { t: "bridge" }, { t: "finish" }];
    const back = () => go(cid ? `#/web/${cid}` : "#/web");
    sprint({
      steps, onExit: back,
      draw(st, node) {
        const end = id => `<div class="end"><b>${esc(C[id].title)}</b><span>${esc(C[id].gist)}</span></div>`;
        if (st.t === "pair") {
          node.innerHTML = `<div class="sp-lab" style="color:${T.c}">${layer === 4 ? "L4 · " : ""}${T.lab}</div>` +
            `<div class="pair">${end(L.a)}<span class="arr">${L.type === "relates" ? "↔" : "→"}</span>${end(L.b)}</div>`;
        } else if (st.t === "guess") {
          const q = L.predict || (L.type === "relates" ? `What do ${C[L.a].title} and ${C[L.b].title} have in common?` : `How does ${C[L.a].title} lead to ${C[L.b].title}?`);
          node.innerHTML = `<div class="sp-lab">guess first</div><p class="sp-q">${esc(q)}</p><p class="sp-hint">One line, in your head or on paper.</p>`;
        } else if (st.t === "bridge") {
          node.innerHTML = `<div class="sp-lab" style="color:${T.c}">${T.v}</div><p class="sp-bridge">${esc(L.text)}</p>`;
        } else {
          doneL.add(linkKey(L)); persist();
          const key = "L3:" + (cid || "all"), all = linksOf(cid), k = all.indexOf(all.find(x => x.a === a && x.b === b));
          pendingWeb[key] = Math.min(k + 1, all.length - 1);
          node.classList.add("sp-done");
          node.innerHTML = `<div class="tick">✓</div><h1>${esc(C[L.a].title)} ${L.type === "relates" ? "↔" : "→"} ${esc(C[L.b].title)}</h1>`;
          node.appendChild(actions("Back to the web ▸", back));
        }
      },
    });
  }

  // ------------------------------------------------------------------ chrome, routing, zoom
  function setLayer(n, crumbs) {
    document.body.dataset.layer = n;
    $("#lbadge").textContent = "L" + n;
    const parts = [`<a href="#/" class="${crumbs.length ? "far" : ""}">${esc(D.subject.title)}</a>`];
    crumbs.forEach(([href, t], i) => parts.push(`<span class="sep">›</span>` + (i === crumbs.length - 1 ? `<b>${esc(t)}</b>` : `<a href="${href}">${esc(t)}</a>`)));
    $("#crumbs").innerHTML = parts.join("");
  }
  let clickPt = null;
  document.addEventListener("pointerdown", e => { clickPt = { x: e.clientX, y: e.clientY }; }, true);
  function go(hash) { if (location.hash === hash) route(); else location.hash = hash; }
  let lastBase = null;
  function route() {
    const parts = location.hash.replace(/^#\/?/, "").split("/").filter(Boolean);
    const view = $("#view");
    let base, over = null;
    if (parts[0] === "ch" && CH[parts[1]]) base = ["L1", parts[1]];
    else if (parts[0] === "c" && CH[parts[1]] && C[parts[2]]) { base = ["L1", parts[1]]; over = () => renderSprint(parts[1], parts[2]); }
    else if (parts[0] === "web") {
      const cid = parts[1] && parts[1] !== "-" && C[parts[1]] ? parts[1] : null;
      base = ["L3", cid];
      if (parts[2] === "e" && C[parts[3]] && C[parts[4]]) over = () => renderLinkSprint(cid, parts[3], parts[4]);
    } else base = ["L0"];
    const key = base.join(":");
    if (over) {
      // the sprint covers everything: the layer underneath is drawn only if it is not already there
      if (lastBase !== key) { drawBase(view, base); lastBase = key; }
      over();
      return;
    }
    closeSprint();
    const changed = lastBase !== key;
    drawBase(view, base);
    lastBase = key;
    if (changed && S.motion && clickPt) {
      view.style.transformOrigin = `${clickPt.x}px ${clickPt.y - 50}px`;
      restart(view, "enter");
    }
  }
  function drawBase(view, base) {
    view.classList.remove("enter");
    if (base[0] === "L1") renderL1(view, base[1]);
    else if (base[0] === "L3") renderWeb(view, base[1]);
    else renderL0(view);
  }
  document.addEventListener("keydown", e => {
    if (e.target.closest && e.target.closest("input, textarea")) return;
    if (e.key === "Escape" && sp.hidden) {
      const parts = location.hash.replace(/^#\/?/, "").split("/").filter(Boolean);
      if (parts[0] === "ch") go("#/");
      else if (parts[0] === "web") go(parts[1] && parts[1] !== "-" ? `#/ch/${chapterOf[parts[1]]}` : "#/");
      return;
    }
    if (active) active.key(e);
  });
  let rt = null;
  addEventListener("resize", () => { clearTimeout(rt); rt = setTimeout(() => { lastBase = null; route(); }, 150); });
  addEventListener("hashchange", route);

  // ------------------------------------------------------------------ prototype controls (not part of the design)
  function panel() {
    const pp = $("#pp");
    const row = (label, key, opts) => `<div class="row"><span>${label}</span>` +
      opts.map(([v, t]) => `<button data-k="${key}" data-v="${v}" class="${String(S[key]) === String(v) ? "on" : ""}">${t}</button>`).join("") + `</div>`;
    pp.innerHTML = `<div class="t">Prototype controls</div>` +
      row("L0 variant", "l0", [["step", "A · step river"], ["units", "B · units first"], ["scroll", "C · scroll river"]]) +
      row("Colour by", "color", [["kind", "kind"], ["unit", "topic (unit)"], ["role", "trunk/node/leaf/edge"], ["layer", "layer"]]) +
      row("Priming card", "prime", [["terms", "3 key terms"], ["line", "one sentence"], ["q", "guess first"]]) +
      row("L3 web", "l3", [["merged", "L3 map + link sprints"], ["split", "L3 map · L4 explains"]]) +
      row("Motion", "motion", [[true, "on"], [false, "off"]]) +
      row("Sprint step dots", "dots", [[true, "on"], [false, "off"]]) +
      `<div class="row"><span>Progress (concepts done, in order)</span>` +
      [0, 5, 24, 60, 117].map(n => `<button data-p="${n}">${n}</button>`).join("") + `</div>` +
      `<div class="row"><button data-reset="1">reset river positions</button></div>`;
    pp.querySelectorAll("[data-k]").forEach(b => b.addEventListener("click", () => {
      const k = b.dataset.k, v = b.dataset.v;
      S[k] = v === "true" ? true : v === "false" ? false : v;
      document.body.classList.toggle("still", !S.motion);
      document.body.classList.toggle("cm-layer", S.color === "layer");
      saveQ(); panel(); lastBase = null; route();
    }));
    pp.querySelectorAll("[data-p]").forEach(b => b.addEventListener("click", () => {
      S.p = +b.dataset.p; done = new Set(D.order.slice(0, S.p)); doneL = new Set(); pos = {}; persist(); saveQ(); lastBase = null; route();
    }));
    pp.querySelector("[data-reset]").addEventListener("click", () => { pos = {}; persist(); lastBase = null; route(); });
  }
  $("#ppbtn").addEventListener("click", () => { $("#pp").hidden = !$("#pp").hidden; });

  // ------------------------------------------------------------------ self-test: every layer × variant × step, plus a visual-load budget
  async function selftest() {
    const errs = [], tick = () => new Promise(r => setTimeout(r, 0));
    const nav = hsh => { history.replaceState(null, "", location.pathname + location.search + hsh); lastBase = null; route(); };
    window.addEventListener("error", e => errs.push(e.message));
    S.motion = false; document.body.classList.add("still");
    let renders = 0, maxLabels = 0, maxAt = "";
    const countLoad = where => {
      // visible text on the map (labels + tributary tags) while walking, i.e. not in the chosen overview
      const st = active && active.state ? active.state() : {};
      if (st.overview) return;
      const labs = [...document.querySelectorAll("#view .st.lab-on .lab, #view .trib-t, #view .wtag text")].length;
      if (labs > maxLabels) { maxLabels = labs; maxAt = where; }
    };
    const walk = async (where) => {
      const st = active.state();
      for (let k = 0; k < (st.N || 0) + 1; k++) { active.next(); renders++; countLoad(where + " k" + k); await tick(); }
    };
    try {
      for (const l0 of ["step", "units", "scroll"]) for (const color of ["kind", "unit", "role", "layer"]) for (const prime of ["terms", "line", "q"]) {
        Object.assign(S, { l0, color, prime }); pos = {}; nav("#/");
        if (l0 !== "scroll") await walk(`L0 ${l0}/${color}/${prime}`); else renders++;
      }
      S.l0 = "step";
      for (const p of [0, 60]) {
        done = new Set(D.order.slice(0, p));
        for (const color of ["kind", "role"]) {
          S.color = color;
          for (const ch of D.chapters) { pos = {}; nav(`#/ch/${ch.id}`); await walk(`L1 ${ch.id}/${color}`); }
        }
      }
      for (const cid of D.order) {
        nav(`#/c/${chapterOf[cid]}/${cid}`);
        const n = active.state().n;
        for (let i = 0; i < n + 2; i++) { active.next(); renders++; await tick(); }
        closeSprint();
      }
      for (const l3 of ["merged", "split"]) {
        S.l3 = l3;
        for (const cid of [null, ...D.order]) {
          pos = {}; nav(cid ? `#/web/${cid}` : "#/web");
          await walk(`L3 ${cid || "all"}`);
          const L = linksOf(cid);
          if (L.length && l3 === "merged") {
            nav(`#/web/${cid || "-"}/e/${L[0].a}/${L[0].b}`);
            for (let i = 0; i < 5; i++) { active.next(); renders++; await tick(); }
          }
        }
      }
      // motion: a forward step must draw the incoming water and pop the new stop
      S.motion = true; document.body.classList.remove("still"); S.l0 = "step"; S.color = "kind";
      pos = {}; nav("#/");
      for (let k = 0; k < 6; k++) {
        active.next(); await tick();
        const K = active.state().K;
        if (!document.querySelector("#view .st.pop")) errs.push(`motion: no pop at L0 step ${K}`);
        if (K > 0 && !document.querySelector("#view .e.draw")) errs.push(`motion: no water drawn at L0 step ${K}`);
        if (K < active.state().N - 1 && !document.querySelector("#view .st.ghost")) errs.push(`motion: no waiting ghost at L0 step ${K}`);
      }
      S.motion = false; document.body.classList.add("still");
      // staircase: on every map, each stop is strictly lower than the one before it in teaching order
      const stair = (ids, Lx, where) => ids.forEach((id, k) => { if (k && !(Lx.P(id).y > Lx.P(ids[k - 1]).y)) errs.push(`staircase broken: ${where} ${ids[k - 1]} → ${id}`); });
      stair(D.chapters.map(c => c.id), layoutChapters(), "L0/L3");
      // data checks
      const seen = new Set();
      D.order.forEach((id, k) => { preds[id].forEach(p => { if (orderIdx[p] > k) errs.push(`order: ${p} after ${id}`); }); seen.add(id); });
      if (seen.size !== D.concepts.length) errs.push("order does not cover every concept once");
      D.chapters.forEach(ch => { if (ch.terms.length > 3) errs.push(`${ch.id}: more than 3 priming terms`); });
    } catch (e) { errs.push("THROW " + e.message + " " + (e.stack || "").split("\n")[1]); }
    const budget = 6;
    if (maxLabels > budget) errs.push(`visual load: ${maxLabels} map labels at once (${maxAt}), budget ${budget}`);
    document.title = (errs.length ? "FAIL " : "PASS ") + `${renders} renders, ${errs.length} errors, max map labels ${maxLabels} (budget ${budget})`;
    document.body.insertAdjacentHTML("afterbegin", `<pre id="st" style="position:fixed;z-index:99;top:60px;left:10px;right:10px;background:var(--card);padding:10px;border:1px solid var(--line);max-height:60vh;overflow:auto;font-size:12px">${esc(document.title)}\n${esc(errs.slice(0, 40).join("\n"))}</pre>`);
  }

  // ------------------------------------------------------------------ boot
  load();
  if (!S.chrome) document.body.classList.add("nochrome");
  document.body.classList.toggle("still", !S.motion);
  document.body.classList.toggle("cm-layer", S.color === "layer");
  if (Q.has("s") && /web/.test(location.hash)) { firstStepWeb = S.s; firstStep = null; }
  panel();
  if (Q.get("panel") === "1") $("#pp").hidden = false;
  if (Q.get("selftest") === "1") selftest(); else { route(); if (Q.get("ov") === "1" && active && active.all) active.all(); }
})();
