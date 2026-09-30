/* Site v2 prototype (session 2): layers L0–L3 over the auto-cut Digital Electronics graph.
   Throwaway code: it exists so the learner can *see* the variants (SITE-V2-DRAFT §3.1) and pick.
   Routes:  #/  (L0 subject)  ·  #/ch/<ch>  (L1 chapter)  ·  #/c/<ch>/<id>  (L2 focus)  ·  #/c/<ch>/<id>/web  (L3)
   Query:   l0=river|lanes|strata  l1=strict|ports|connected  growth=0  p=<n done>  chrome=0  theme=dark */
(() => {
  "use strict";
  const D = window.DATA;
  const C = {}, CH = {}, STAGE = {}, chapterOf = {}, preds = {}, succs = {}, EDGE = {}, orderIdx = {}, rel = {};
  D.concepts.forEach(c => { C[c.id] = c; preds[c.id] = []; succs[c.id] = []; });
  D.stages.forEach(s => STAGE[s.id] = s);
  D.chapters.forEach(ch => { CH[ch.id] = ch; ch.concepts.forEach(i => chapterOf[i] = ch.id); });
  D.edges.forEach(e => { preds[e.to].push(e.from); succs[e.from].push(e.to); EDGE[e.from + ">" + e.to] = e; });
  D.order.forEach((id, k) => orderIdx[id] = k);
  D.relates.forEach(r => {
    (rel[r.a] = rel[r.a] || []).push({ other: r.b, note: r.note });
    (rel[r.b] = rel[r.b] || []).push({ other: r.a, note: r.note });
  });
  const hue = chId => STAGE[CH[chId].stage].hue;
  const fullDeg = id => preds[id].length + succs[id].length;

  // ------------------------------------------------------------------ settings
  const Q = new URLSearchParams(location.search);
  const S = {
    l0: Q.get("l0") || "river", l1: Q.get("l1") || "ports", growth: Q.get("growth") !== "0",
    chrome: Q.get("chrome") !== "0", p: Q.has("p") ? +Q.get("p") : null, min: false,
  };
  function saveQ() {
    const q = new URLSearchParams();
    q.set("l0", S.l0); q.set("l1", S.l1);
    if (!S.growth) q.set("growth", "0");
    if (S.p != null) q.set("p", S.p);
    if (!S.chrome) q.set("chrome", "0");
    history.replaceState(null, "", "?" + q + location.hash);
  }

  // ------------------------------------------------------------------ progress (navigation state, not mastery)
  let done = new Set();
  function loadDone() {
    if (S.p == null) {
      try { const s = localStorage.getItem("v2p-done"); if (s) done = new Set(JSON.parse(s)); else S.p = 24; } catch (e) { S.p = 24; }
    }
    if (S.p != null) done = new Set(D.order.slice(0, S.p));
  }
  function persist() { try { localStorage.setItem("v2p-done", JSON.stringify([...done])); } catch (e) { } }
  const isDone = id => done.has(id);
  const isReady = id => !done.has(id) && preds[id].every(isDone);
  const status = id => isDone(id) ? "done" : isReady(id) ? "ready" : "locked";
  // SITE-V2-DRAFT §2.1: an edge shows once its source is done and its target is done or next up.
  const edgeVisible = (a, b) => !S.growth || (isDone(a) && (isDone(b) || isReady(b)));
  function visDeg(id) {
    let n = 0;
    preds[id].forEach(p => { if (edgeVisible(p, id)) n++; });
    succs[id].forEach(s => { if (edgeVisible(id, s)) n++; });
    return n;
  }
  const shape = id => (S.growth ? visDeg(id) : fullDeg(id)) >= 2 ? "node" : "leaf";

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
  const cv = document.createElement("canvas").getContext("2d");
  function tw(t, font) { cv.font = font; return cv.measureText(t).width; }
  function wrap(t, font, max) {
    const words = t.split(" "), lines = [];
    let cur = "";
    words.forEach(w => {
      const nx = cur ? cur + " " + w : w;
      if (tw(nx, font) > max && cur) { lines.push(cur); cur = w; } else cur = nx;
    });
    if (cur) lines.push(cur);
    return lines;
  }
  const narrow = () => innerWidth < 760;

  // d3's curveBasis, for dagre's edge points
  function basis(p) {
    if (p.length < 3) return `M${p[0].x},${p[0].y}L${p[p.length - 1].x},${p[p.length - 1].y}`;
    let d = `M${p[0].x},${p[0].y}`, x0 = p[0].x, y0 = p[0].y, x1 = p[1].x, y1 = p[1].y;
    d += `L${(5 * x0 + x1) / 6},${(5 * y0 + y1) / 6}`;
    for (let i = 2; i < p.length; i++) {
      const x = p[i].x, y = p[i].y;
      d += `C${(2 * x0 + x1) / 3},${(2 * y0 + y1) / 3},${(x0 + 2 * x1) / 3},${(y0 + 2 * y1) / 3},${(x0 + 4 * x1 + x) / 6},${(y0 + 4 * y1 + y) / 6}`;
      x0 = x1; y0 = y1; x1 = x; y1 = y;
    }
    d += `C${(2 * x0 + x1) / 3},${(2 * y0 + y1) / 3},${(x0 + 2 * x1) / 3},${(y0 + 2 * y1) / 3},${x1},${y1}`;
    return d;
  }
  function dag(opts) {
    const g = new dagre.graphlib.Graph({ compound: !!opts.compound, multigraph: false });
    g.setGraph(Object.assign({ rankdir: "TB", nodesep: 22, ranksep: 40, marginx: 16, marginy: 16 }, opts.graph));
    g.setDefaultEdgeLabel(() => ({}));
    return g;
  }
  function fitSvg(svg, gw, gh, host) {
    const avail = Math.max(280, host.clientWidth - (narrow() ? 24 : 48));
    const scale = Math.min(1, avail / gw);
    svg.setAttribute("viewBox", `0 0 ${gw} ${gh}`);
    svg.setAttribute("width", gw * scale);
    svg.setAttribute("height", gh * scale);
    return scale;
  }

  // ------------------------------------------------------------------ tooltip (edge bridges on the map)
  const tip = $("#tip");
  function showTip(evt, html) {
    tip.innerHTML = html; tip.hidden = false;
    const x = Math.min(evt.clientX + 14, innerWidth - tip.offsetWidth - 8);
    const y = Math.min(evt.clientY + 14, innerHeight - tip.offsetHeight - 8);
    tip.style.left = x + "px"; tip.style.top = y + "px";
  }
  const hideTip = () => { tip.hidden = true; };
  function bridgeTip(a, b) {
    const e = EDGE[a + ">" + b];
    return `<div class="tl">${esc(C[a].title)} → ${esc(C[b].title)}</div>${esc(e.bridge)}`;
  }

  // ------------------------------------------------------------------ zoom transition (a layer grows out of what you clicked)
  let origin = null;
  function zoomIn(node) {
    node.classList.remove("zoom-in");
    if (origin) {
      const R = node.getBoundingClientRect();
      const s = Math.max(0.08, Math.min(0.6, origin.width / Math.max(1, R.width)));
      const dx = origin.left + origin.width / 2 - (R.left + R.width / 2);
      const dy = origin.top + origin.height / 2 - (R.top + Math.min(R.height, innerHeight) / 2);
      node.style.setProperty("--from", `translate(${dx}px, ${dy}px) scale(${s})`);
    } else node.style.setProperty("--from", "scale(.97)");
    void node.offsetWidth;
    node.classList.add("zoom-in");
    origin = null;
  }

  // ------------------------------------------------------------------ top bar
  function crumbs(chId, cid) {
    const parts = [`<a href="#/">${esc(D.subject.title)}</a>`];
    if (!chId) parts[0] = `<b>${esc(D.subject.title)}</b><span class="sub">&nbsp;· ${esc(D.subject.line)}</span>`;
    if (chId) {
      const ch = CH[chId];
      parts.push(cid ? `<a href="#/ch/${chId}">${ch.n} ${esc(ch.title)}</a>` : `<b>${ch.n} ${esc(ch.title)}</b>`);
    }
    if (cid) parts.push(`<b>${esc(C[cid].title)}</b>`);
    if (narrow() && parts.length > 2) parts.shift();  // phones: drop the subject, keep chapter › concept
    else if (narrow() && parts.length === 2) parts[0] = `<a href="#/">◂</a>`;
    $("#crumbs").innerHTML = parts.join('<span class="sep">›</span>');
  }

  // ================================================================== L0: the subject (chapters only)
  const chDone = ch => ch.concepts.filter(isDone).length;
  const directEdges = () => D.chapterEdges.filter(e => e.direct);
  const chPreds = id => D.chapterEdges.filter(e => e.to === id).map(e => e.from);
  const chSuccs = id => D.chapterEdges.filter(e => e.from === id).map(e => e.to);

  function head(title, meta) {
    const d = h("div", { class: "head" });
    d.innerHTML = `<h1>${title}</h1><div class="meta">${meta}</div>`;
    return d;
  }
  function l0Meta() {
    const st = D.stats;
    return `${st.chapters} chapters · ${st.concepts} concepts · cut automatically (≤ ${D.cut.cap} concepts each) · ${done.size} done`;
  }

  function renderL0(view) {
    const stage = h("div", { class: "stage" });
    view.appendChild(stage);
    stage.appendChild(head(esc(D.subject.title), l0Meta()));
    if (S.l0 === "lanes") l0Lanes(stage);
    else if (S.l0 === "strata") l0Strata(stage);
    else l0River(stage);
    const key = h("div", { class: "foot-key" });
    key.innerHTML = S.l0 === "strata"
      ? "one row = one chapter · <i>●</i> done · <i>■</i> node (converges or splits) · hover a row to light what it builds on"
      : S.l0 === "lanes"
        ? "each lane is a stage of the subject · <i>●</i> chapter finished · a curve = one chapter feeds another"
        : "top → bottom = teaching flow · a line = one chapter feeds the next (shortcuts hidden; hover shows all)";
    stage.appendChild(key);
    zoomIn(stage);
  }

  function chapterBlock(parent, ch, x, y, w, hgt, lines, cls) {
    const g = el("g", { class: `chb h-${hue(ch.id)} ${cls || ""} ${ch.trunk ? "trunk" : ""}`, tabindex: 0, transform: `translate(${x - w / 2},${y - hgt / 2})`, "data-ch": ch.id }, parent);
    el("rect", { class: "box", width: w, height: hgt, rx: 12 }, g);
    el("text", { class: "n", x: 14, y: 22 }, g, String(ch.n));
    lines.forEach((ln, k) => el("text", { class: "t", x: 36, y: 22 + k * 18 }, g, ln));
    const dn = chDone(ch), tot = ch.concepts.length;
    el("text", { class: "s", x: 36, y: 22 + lines.length * 18 + 2 }, g, `${ch.trunk ? "trunk · " : ""}${tot} concepts${dn ? ` · ${dn} ✓` : ""}`);
    el("rect", { class: "pbar", x: 14, y: hgt - 9, width: w - 28, height: 3, rx: 1.5 }, g);
    if (dn) el("rect", { class: "pfill", x: 14, y: hgt - 9, width: (w - 28) * dn / tot, height: 3, rx: 1.5 }, g);
    const go = () => { origin = g.getBoundingClientRect(); location.hash = `#/ch/${ch.id}`; };
    g.addEventListener("click", go);
    g.addEventListener("keydown", e => { if (e.key === "Enter") go(); });
    return g;
  }

  function l0River(stage) {
    const W = narrow() ? 168 : 214, font = "600 14px Inter";
    const g = dag({ graph: { nodesep: narrow() ? 12 : 30, ranksep: narrow() ? 30 : 40, marginx: 24, marginy: 16 } });
    const lines = {};
    D.chapters.forEach(ch => {
      lines[ch.id] = wrap(ch.title, font, W - 52).slice(0, 3);
      g.setNode(ch.id, { width: W, height: 44 + lines[ch.id].length * 18 });
    });
    directEdges().forEach(e => g.setEdge(e.from, e.to, { weight: CH[e.from].stage === CH[e.to].stage ? 3 : 1 }));
    dagre.layout(g);
    const gw = g.graph().width, gh = g.graph().height;
    const svg = el("svg", { class: "map" });
    stage.appendChild(svg);
    fitSvg(svg, gw, gh, stage);
    const wires = el("g", {}, svg);
    const wireOf = {};
    g.edges().forEach(ed => {
      const p = el("path", { class: "wire", d: basis(g.edge(ed).points) }, wires);
      wireOf[ed.v + ">" + ed.w] = p;
    });
    const blocks = {};
    D.chapters.forEach(ch => {
      const n = g.node(ch.id);
      blocks[ch.id] = chapterBlock(svg, ch, n.x, n.y, n.width, n.height, lines[ch.id]);
    });
    // hover: light this chapter's inputs/outputs (all of them, not just the drawn ones)
    D.chapters.forEach(ch => {
      const b = blocks[ch.id];
      b.addEventListener("mouseenter", () => {
        const rel = new Set([ch.id, ...chPreds(ch.id), ...chSuccs(ch.id)]);
        D.chapters.forEach(o => blocks[o.id].classList.toggle("dim", !rel.has(o.id)));
        Object.entries(wireOf).forEach(([k, p]) => {
          const [a, bb] = k.split(">");
          p.classList.toggle("hi", a === ch.id || bb === ch.id);
          p.style.setProperty("--hc", `var(--${hue(ch.id)})`);
        });
      });
      b.addEventListener("mouseleave", () => {
        D.chapters.forEach(o => blocks[o.id].classList.remove("dim"));
        Object.values(wireOf).forEach(p => p.classList.remove("hi"));
      });
    });
    // stage legend (colour carries the stage; no boxes)
    const lg = h("div", { class: "legend" });
    lg.innerHTML = D.stages.map(s => `<span class="h-${s.hue}"><i></i>${esc(s.title)}</span>`).join("");
    stage.insertBefore(lg, svg);
  }

  function l0Lanes(stage) {
    const host = h("div", { style: "width:100%;max-width:760px" });
    stage.appendChild(host);
    const lanes = D.stages.map(s => s.id), laneX = k => 18 + k * 30;
    const rowH = narrow() ? 58 : 54, top = 24, labelX = laneX(lanes.length - 1) + 30;
    const W = Math.max(320, Math.min(760, stage.clientWidth - 24));
    const Hh = top * 2 + rowH * (D.chapters.length - 1) + 20;
    const svg = el("svg", { class: "map", width: W, height: Hh, viewBox: `0 0 ${W} ${Hh}` });
    host.appendChild(svg);
    const pos = {};
    D.chapters.forEach((ch, k) => pos[ch.id] = { x: laneX(lanes.indexOf(ch.stage)), y: top + k * rowH });
    // lane threads
    D.stages.forEach((s, k) => {
      const ys = D.chapters.filter(c => c.stage === s.id).map(c => pos[c.id].y);
      if (!ys.length) return;
      el("line", { class: `lane h-${s.hue}`, x1: laneX(k), x2: laneX(k), y1: Math.min(...ys), y2: Math.max(...ys) }, svg);
    });
    // transfers between lanes (direct chapter links that change stage)
    directEdges().forEach(e => {
      if (CH[e.from].stage === CH[e.to].stage) return;
      const a = pos[e.from], b = pos[e.to], m = Math.min(rowH * 0.9, (b.y - a.y) / 2);
      el("path", { class: "xfer", d: `M${a.x},${a.y}C${a.x},${a.y + m} ${b.x},${b.y - m} ${b.x},${b.y}` }, svg);
    });
    D.chapters.forEach(ch => {
      const p = pos[ch.id], dn = chDone(ch), tot = ch.concepts.length;
      const g = el("g", { class: `station h-${hue(ch.id)} ${dn === tot ? "full" : ""}`, tabindex: 0 }, svg);
      el("rect", { class: "rowhit", x: labelX - 10, y: p.y - rowH / 2 + 3, width: W - labelX + 6, height: rowH - 6, rx: 10 }, g);
      el("circle", { cx: p.x, cy: p.y, r: 5.5 }, g);
      el("text", { class: "n", x: labelX, y: p.y - 3 }, g, String(ch.n));
      const t = wrap(ch.title, "600 14.5px Inter", W - labelX - 40)[0];
      el("text", { class: "t", x: labelX + 26, y: p.y - 3 }, g, t + (ch.trunk ? "   ·  trunk" : ""));
      el("text", { class: "s", x: labelX + 26, y: p.y + 14 }, g, `${tot} concepts${dn ? ` · ${dn} done` : ""}`);
      const go = () => { origin = g.getBoundingClientRect(); location.hash = `#/ch/${ch.id}`; };
      g.addEventListener("click", go);
      g.addEventListener("keydown", e => { if (e.key === "Enter") go(); });
    });
  }

  function l0Strata(stage) {
    const box = h("div", { class: "strata" });
    stage.appendChild(box);
    const rows = {};
    D.stages.forEach(s => {
      const chs = D.chapters.filter(c => c.stage === s.id);
      if (!chs.length) return;
      box.appendChild(h("div", { class: `stratum-stage h-${s.hue}` }, esc(s.title)));
      chs.forEach(ch => {
        const r = h("button", { class: `row h-${hue(ch.id)}`, type: "button" });
        const dots = ch.concepts.map(i => `<span class="${isDone(i) ? "on" : ""} ${fullDeg(i) >= 2 && ch.concepts.some(j => EDGE[i + ">" + j] || EDGE[j + ">" + i]) ? "node" : ""}"></span>`).join("");
        const dn = chDone(ch);
        r.innerHTML = `<span class="n">${ch.n}</span><span class="t">${esc(ch.title)}${ch.trunk ? " · trunk" : ""}<small>${ch.concepts.length} concepts${dn ? ` · ${dn} done` : ""}</small></span><span class="dots">${dots}</span><span class="why"></span>`;
        r.addEventListener("click", () => { origin = r.getBoundingClientRect(); location.hash = `#/ch/${ch.id}`; });
        r.addEventListener("mouseenter", () => {
          const ps = D.chapterEdges.filter(e => e.to === ch.id);
          const lit = new Set(ps.map(e => e.from));
          D.chapters.forEach(o => {
            rows[o.id].classList.toggle("lit", lit.has(o.id));
            rows[o.id].classList.toggle("dim", o.id !== ch.id && !lit.has(o.id));
            const e = ps.find(x => x.from === o.id);
            rows[o.id].querySelector(".why").textContent = e ? `feeds ${ch.n} ${ch.title} · ${e.n} link${e.n > 1 ? "s" : ""}` : "";
          });
        });
        r.addEventListener("mouseleave", () => D.chapters.forEach(o => rows[o.id].classList.remove("lit", "dim")));
        rows[ch.id] = r;
        box.appendChild(r);
      });
    });
  }

  // ================================================================== L1: one chapter
  let prevVisible = null;
  function renderL1(view, chId) {
    const ch = CH[chId];
    const stage = h("div", { class: `stage h-${hue(chId)}` });
    view.appendChild(stage);
    const dn = chDone(ch);
    const ins = new Set(), outs = new Set();
    ch.concepts.forEach(i => {
      preds[i].forEach(p => { if (chapterOf[p] !== chId) ins.add(chapterOf[p]); });
      succs[i].forEach(s => { if (chapterOf[s] !== chId) outs.add(chapterOf[s]); });
    });
    stage.appendChild(head(`<span class="hue">${ch.n}</span>&nbsp; ${esc(ch.title)}`,
      `${STAGE[ch.stage].title}${ch.trunk ? " · trunk (the subject starts here)" : ""} · ${ch.concepts.length} concepts · ${dn} done · fed by ${ins.size} chapter${ins.size === 1 ? "" : "s"}, feeds ${outs.size}`));
    const host = h("div", { style: "width:100%;display:flex;justify-content:center" });
    stage.appendChild(host);
    drawChapter(host, chId, S.l1);
    const key = h("div", { class: "foot-key" });
    key.innerHTML = `<i>○</i> leaf (one connection) · <i>●</i> node (converges or splits) · bold outline = next up · faint = not reached yet` +
      (S.growth ? " · connections appear as you finish concepts" : "") +
      (S.l1 === "ports" ? " · dashed tags = other chapters" : "") + " · hover a line for its bridge";
    stage.appendChild(key);
    zoomIn(stage);
  }

  function conceptSize(id) {
    const max = narrow() ? 128 : 170, font = (shape(id) === "node" ? "650" : "500") + " 13.5px Inter";
    const lines = wrap(C[id].title, font, max).slice(0, 3);
    const w = Math.max(...lines.map(l => tw(l, font))) * 1.04 + 52;
    return { lines, w, h: lines.length * 17 + 17 };
  }

  function drawChapter(host, chId, variant) {
    const ch = CH[chId], inside = new Set(ch.concepts);
    const g = dag({ compound: variant === "connected", graph: { nodesep: narrow() ? 12 : 22, ranksep: narrow() ? 30 : 38, marginx: 20, marginy: 20 } });
    const size = {};
    if (variant === "connected") g.setNode("cluster", { paddingTop: 34, paddingLeft: 14, paddingRight: 14, paddingBottom: 14 });
    ch.concepts.forEach(i => {
      size[i] = conceptSize(i);
      g.setNode(i, { width: size[i].w, height: size[i].h });
      if (variant === "connected") g.setParent(i, "cluster");
    });
    const inner = D.edges.filter(e => inside.has(e.from) && inside.has(e.to));
    inner.forEach(e => g.setEdge(e.from, e.to));
    const ports = {}, portEdges = [];
    if (variant === "ports") {
      ch.concepts.forEach(i => {
        preds[i].filter(p => !inside.has(p)).forEach(p => {
          const k = "in:" + p;
          if (!ports[k]) ports[k] = { kind: "in", concept: p, ch: chapterOf[p], targets: new Set() };
          ports[k].targets.add(i);
        });
        succs[i].filter(s => !inside.has(s)).forEach(s => {
          const k = "out:" + chapterOf[s];
          if (!ports[k]) ports[k] = { kind: "out", ch: chapterOf[s], concepts: new Set(), targets: new Set() };
          ports[k].concepts.add(s); ports[k].targets.add(i);
        });
      });
    }
    const minis = {};
    if (variant === "connected") {
      ch.concepts.forEach(i => {
        preds[i].filter(p => !inside.has(p)).forEach(p => { minis[chapterOf[p]] = 1; portEdges.push(["ch:" + chapterOf[p], i, p, i]); });
        succs[i].filter(s => !inside.has(s)).forEach(s => { minis[chapterOf[s]] = 1; portEdges.push([i, "ch:" + chapterOf[s], i, s]); });
      });
      Object.keys(minis).forEach(c => {
        const lines = wrap(`${CH[c].title}`, "600 12.5px Inter", 150).slice(0, 2);
        minis[c] = lines;
        g.setNode("ch:" + c, { width: 190, height: 30 + lines.length * 16 });
      });
      const seen = new Set();
      portEdges.forEach(pe => { const k = pe[0] + ">" + pe[1]; if (!seen.has(k)) { seen.add(k); g.setEdge(pe[0], pe[1]); } });
      // keep the river shape among the neighbours
      directEdges().forEach(e => { if (minis[e.from] && minis[e.to]) g.setEdge("ch:" + e.from, "ch:" + e.to); });
    }
    dagre.layout(g);
    const gw = g.graph().width, gh = g.graph().height;
    const svg = el("svg", { class: "map" });
    host.appendChild(svg);
    fitSvg(svg, gw, gh, host.parentNode);

    if (variant === "connected") {
      const n = g.node("cluster");
      el("rect", { class: "cluster", x: n.x - n.width / 2, y: n.y - n.height / 2, width: n.width, height: n.height, rx: 16 }, svg);
      el("text", { class: "cluster-label", x: n.x - n.width / 2 + 16, y: n.y - n.height / 2 + 22 }, svg, `${ch.n} · ${ch.title}`);
    }
    const wires = el("g", {}, svg), nodesG = el("g", {}, svg);
    const nowVisible = new Set(), wireEls = [];
    // inner flow edges
    inner.forEach(e => {
      const vis = edgeVisible(e.from, e.to);
      const pts = g.edge(e.from, e.to).points, d = basis(pts);
      const p = el("path", { class: "wire" + (vis ? "" : " ghost"), d }, wires);
      const k = e.from + ">" + e.to;
      if (vis) {
        nowVisible.add(k);
        if (prevVisible && !prevVisible.has(k)) {
          const len = p.getTotalLength();
          p.style.setProperty("--len", len); p.style.strokeDasharray = len; p.classList.add("grow-in");
        }
      }
      if (vis && status(e.to) === "ready") p.classList.add("hi");
      const hit = el("path", { class: "hit", d }, wires);
      hit.addEventListener("mousemove", ev => { if (vis) showTip(ev, bridgeTip(e.from, e.to)); });
      hit.addEventListener("mouseleave", hideTip);
      wireEls.push({ from: e.from, to: e.to, p, vis });
    });
    // port / neighbour edges
    const seenPE = new Set();
    portEdges.forEach(([a, b, ca, cb]) => {
      const k = a + ">" + b;
      if (seenPE.has(k)) return; seenPE.add(k);
      const ed = g.edge(a, b); if (!ed) return;
      const vis = !S.growth || isDone(ca) || isReady(cb) || isDone(cb);
      const p = el("path", { class: "wire port" + (vis ? "" : " faint"), d: basis(ed.points) }, wires);
      const hit = el("path", { class: "hit", d: basis(ed.points) }, wires);
      hit.addEventListener("mousemove", ev => showTip(ev, bridgeTip(ca, cb)));
      hit.addEventListener("mouseleave", hideTip);
      wireEls.push({ from: a.startsWith("in:") || a.startsWith("ch:") ? null : a, to: b.startsWith("out:") || b.startsWith("ch:") ? null : b, p, vis, port: true, ca, cb });
    });
    if (variant === "connected") {
      g.edges().forEach(ed => {
        if (ed.v.startsWith("ch:") && ed.w.startsWith("ch:")) el("path", { class: "wire faint", d: basis(g.edge(ed).points) }, wires);
      });
    }
    prevVisible = nowVisible;

    // neighbour chapter blocks (connected)
    Object.keys(minis).forEach(c => {
      const n = g.node("ch:" + c), gg = el("g", { class: `chb mini h-${hue(c)}`, transform: `translate(${n.x - n.width / 2},${n.y - n.height / 2})` }, nodesG);
      el("rect", { class: "box", width: n.width, height: n.height, rx: 10 }, gg);
      el("text", { class: "n", x: 12, y: 19 }, gg, String(CH[c].n));
      minis[c].forEach((ln, k) => el("text", { class: "t", x: 34, y: 19 + k * 16, style: "font-size:12.5px" }, gg, ln));
      gg.addEventListener("click", () => { origin = gg.getBoundingClientRect(); location.hash = `#/ch/${c}`; });
    });
    // concepts
    const nodeEl = {};
    ch.concepts.forEach(i => {
      const n = g.node(i), st = status(i), sh = shape(i), c = C[i];
      const gg = el("g", { class: `cn ${sh} ${st} ${c.kind}`, tabindex: 0, transform: `translate(${n.x - n.width / 2},${n.y - n.height / 2})` }, nodesG);
      el("rect", { class: "box", width: n.width, height: n.height, rx: sh === "node" ? 10 : 12 }, gg);
      const cy = n.height / 2;
      if (sh === "node") el("circle", { class: "glyph", cx: 14, cy, r: 4.2 }, gg);
      else el("circle", { class: "glyph", cx: 14, cy, r: 4 }, gg);
      const lines = size[i].lines, y0 = cy - (lines.length - 1) * 8.5 + 4.5;
      lines.forEach((ln, k) => el("text", { class: "lbl", x: 26, y: y0 + k * 17 }, gg, (k === 0 && c.kind === "trap" ? "! " : "") + ln));
      if (st === "done") el("text", { class: "tick", x: n.width - 14, y: cy + 4, "text-anchor": "middle" }, gg, "✓");
      const go = () => { origin = gg.getBoundingClientRect(); location.hash = `#/c/${chId}/${i}`; };
      gg.addEventListener("click", go);
      gg.addEventListener("keydown", e => { if (e.key === "Enter") go(); });
      gg.addEventListener("mouseenter", () => {
        wireEls.forEach(w => { if (w.to === i && w.vis) { w.p.classList.add("hi"); if (w.from && nodeEl[w.from]) nodeEl[w.from].classList.add("pre"); } });
      });
      gg.addEventListener("mouseleave", () => {
        wireEls.forEach(w => { if (!(w.vis && w.to && status(w.to) === "ready" && !w.port)) w.p.classList.remove("hi"); });
        Object.values(nodeEl).forEach(x => x.classList.remove("pre"));
      });
      nodeEl[i] = gg;
    });
    if (variant === "ports") {
      // quiet rails: what feeds this chapter (top) and where it leads (bottom). No lines cross the page;
      // a short stub on a concept marks "fed from / feeds outside", hover a tag to light its concepts.
      const stub = (i, up) => {
        const n = g.node(i), x = n.x, y = up ? n.y - n.height / 2 : n.y + n.height / 2;
        el("line", { class: "wire port", x1: x, x2: x, y1: up ? y - 9 : y, y2: up ? y : y + 9 }, wires);
      };
      const ins = Object.values(ports).filter(p => p.kind === "in"), outs = Object.values(ports).filter(p => p.kind === "out");
      new Set(ins.flatMap(p => [...p.targets])).forEach(i => stub(i, true));
      new Set(outs.flatMap(p => [...p.targets])).forEach(i => stub(i, false));
      const rail = (list, label, top) => {
        if (!list.length) return;
        const r = h("div", { class: "rail-row" });
        r.appendChild(h("span", { class: "rail-lab" }, label));
        list.sort((x, y) => CH[x.ch].n - CH[y.ch].n).forEach(p => {
          const t = h("button", { class: `ptag h-${hue(p.ch)}`, type: "button" },
            `<span class="pnum">${p.kind === "out" ? "→ " : ""}${CH[p.ch].n}</span>${esc(p.kind === "in" ? C[p.concept].title : CH[p.ch].title)}`);
          t.addEventListener("mouseenter", () => { p.targets.forEach(i => nodeEl[i] && nodeEl[i].classList.add("pre")); });
          t.addEventListener("mouseleave", () => Object.values(nodeEl).forEach(x => x.classList.remove("pre")));
          t.addEventListener("mousemove", ev => showTip(ev, p.kind === "in"
            ? `<div class="tl">from ${CH[p.ch].n} · ${esc(CH[p.ch].title)} → ${[...p.targets].map(i => esc(C[i].title)).join(", ")}</div>${esc(EDGE[p.concept + ">" + [...p.targets][0]].bridge)}`
            : `<div class="tl">leads on to ${CH[p.ch].n} · ${esc(CH[p.ch].title)}</div>${[...p.concepts].map(i => esc(C[i].title)).join(" · ")}`));
          t.addEventListener("mouseout", hideTip);
          t.addEventListener("click", () => { origin = t.getBoundingClientRect(); location.hash = p.kind === "in" ? `#/c/${p.ch}/${p.concept}` : `#/ch/${p.ch}`; });
          r.appendChild(t);
        });
        if (top) host.parentNode.insertBefore(r, host); else host.parentNode.insertBefore(r, host.nextSibling);
      };
      rail(ins, "comes from", true);
      rail(outs, "leads to", false);
    }
    if (variant === "connected") {
      requestAnimationFrame(() => {
        const n = g.node("cluster"), sc = parseFloat(svg.getAttribute("width")) / gw;
        const view = $("#view"), top = svg.getBoundingClientRect().top - view.getBoundingClientRect().top + view.scrollTop;
        view.scrollTo({ top: Math.max(0, top + (n.y - n.height / 2) * sc - 80), behavior: "smooth" });
      });
    }
  }

  // ================================================================== L2: focus
  const focus = $("#focus");
  function renderFocus(chId, cid, withWeb) {
    const c = C[cid], st = status(cid), chipEls = {};
    focus.className = `focus h-${hue(chId)}`;
    focus.hidden = false;
    focus.innerHTML = "";
    // strip: where this came from → this → where it leads
    const strip = h("div", { class: "strip" });
    const from = preds[cid], to = succs[cid];
    const shownTo = S.growth ? to.filter(s => isDone(s) || isReady(s)) : to;
    const later = to.length - shownTo.length;
    const chip = (id, dir) => {
      const other = chapterOf[id] !== chId ? `<span class="cx">${CH[chapterOf[id]].n}</span>` : "";
      const b = h("button", { class: `chip ${status(id) === "locked" ? "locked" : ""}`, type: "button" }, other + esc(C[id].title));
      b.addEventListener("click", ev => { ev.stopPropagation(); openPop(b, dir === "in" ? id : cid, dir === "in" ? cid : id, dir); });
      chipEls[id] = b;
      return b;
    };
    if (from.length) {
      const side = h("div", { class: "side" });
      side.appendChild(h("span", { class: "lab" }, "from"));
      const chips = h("div", { class: "chips" }); from.forEach(p => chips.appendChild(chip(p, "in")));
      side.appendChild(chips); strip.appendChild(side);
      strip.appendChild(h("span", { class: "arrow" }, "→"));
    } else strip.appendChild(h("span", { class: "lab" }, "a starting point"));
    strip.appendChild(h("span", { class: "me" }, esc(c.title)));
    if (to.length) {
      strip.appendChild(h("span", { class: "arrow" }, "→"));
      const side = h("div", { class: "side" });
      side.appendChild(h("span", { class: "lab" }, "leads to"));
      const chips = h("div", { class: "chips" }); shownTo.forEach(s => chips.appendChild(chip(s, "out")));
      if (later) chips.appendChild(h("span", { class: "more" }, shownTo.length ? `+${later} later` : `${later} concept${later > 1 ? "s" : ""}, once this is done`));
      side.appendChild(chips); strip.appendChild(side);
    } else strip.appendChild(h("span", { class: "lab" }, "→ an end point: remember it"));
    focus.appendChild(strip);

    // body: one concept, nothing else
    const body = h("div", { class: "fbody" });
    const kind = { idea: "idea", method: "method", trap: "trap", fact: "fact to remember", exam: "exam question", practice: "practice" }[c.kind];
    body.innerHTML = `<div class="kind">${kind} · ${shape(cid)}</div><h1>${esc(c.title)}</h1><p class="gist">${esc(c.gist)}</p>`;
    if (st === "locked") {
      const need = preds[cid].filter(p => !isDone(p));
      body.appendChild(h("div", { class: "needs" }, "Needs first: " + need.map(p => `<a href="#/c/${chapterOf[p]}/${p}">${esc(C[p].title)}</a>`).join(" · ")));
    }
    if (c.body) body.appendChild(h("div", { class: "content" }, c.body));
    else body.appendChild(h("div", { class: "placeholder" }, "Card content arrives with content engine v2 (session 4): real images with markers, the mechanism, right vs wrong, why it matters, and a quick check.<br><br>This prototype is judging <b>structure and focus</b>."));
    const acts = h("div", { class: "actions" });
    const db = h("button", { class: `doneb ${isDone(cid) ? "is" : ""}`, type: "button" }, isDone(cid) ? "✓ Done" : "Mark done");
    db.addEventListener("click", () => { if (isDone(cid)) done.delete(cid); else done.add(cid); S.p = null; persist(); saveQ(); route(); proto(); });
    const wb = h("button", { class: "webb", type: "button" }, "Connect to the web →");
    if (!isDone(cid)) { wb.disabled = true; wb.title = "Finish this concept first. The web opens after."; }
    wb.addEventListener("click", () => { location.hash = `#/c/${chId}/${cid}/web`; });
    acts.appendChild(db); acts.appendChild(wb);
    acts.appendChild(h("span", { class: "note" }, isDone(cid) ? "" : "the web opens once this is done"));
    body.appendChild(acts);
    const k = orderIdx[cid], prev = D.order[k - 1], next = D.order[k + 1];
    const nav = h("div", { class: "fnav" });
    nav.innerHTML = (prev ? `<a href="#/c/${chapterOf[prev]}/${prev}">← ${esc(C[prev].title)}</a>` : "<span></span>") +
      `<span class="pos">${k + 1} of ${D.order.length} in teaching order</span>` +
      (next ? `<a href="#/c/${chapterOf[next]}/${next}" style="text-align:right">${esc(C[next].title)} →</a>` : "<span></span>");
    body.appendChild(nav);
    focus.appendChild(body);
    focus.scrollTop = 0;
    zoomIn(body);
    if (withWeb) renderWeb(chId, cid);
    const auto = Q.get("open");  // screenshot aid: ?open=<concept> opens that chip's bridge
    if (auto && chipEls[auto]) setTimeout(() => chipEls[auto].click(), 450);
  }

  function openPop(chipEl, a, b, dir) {
    focus.querySelectorAll(".pop").forEach(p => p.remove());
    focus.querySelectorAll(".chip.open").forEach(p => p.classList.remove("open"));
    const e = EDGE[a + ">" + b], target = dir === "in" ? a : b;
    const pop = h("div", { class: "pop" });
    let html = `<div class="ph">${dir === "in" ? "how it leads here" : "where this goes next"}</div>`;
    if (dir === "out" && e.predict && !isDone(b)) {
      html += `<div class="pq"><b>Predict first</b>${esc(e.predict)}</div>
               <details><summary style="cursor:pointer;color:var(--accent);font-weight:600">show the bridge</summary><p style="margin:6px 0 0">${esc(e.bridge)}</p></details>`;
    } else html += `<p style="margin:0"><b>${esc(C[a].title)}</b> → <b>${esc(C[b].title)}</b><br>${esc(e.bridge)}</p>`;
    html += `<button class="go" type="button">Open ${esc(C[target].title)} →</button>`;
    pop.innerHTML = html;
    pop.querySelector(".go").addEventListener("click", () => { origin = chipEl.getBoundingClientRect(); location.hash = `#/c/${chapterOf[target]}/${target}`; });
    focus.appendChild(pop);
    const r = chipEl.getBoundingClientRect(), fr = focus.getBoundingClientRect();
    const left = Math.max(12, Math.min(r.left - fr.left, fr.width - pop.offsetWidth - 12));
    pop.style.left = left + "px";
    pop.style.top = (r.bottom - fr.top + focus.scrollTop + 8) + "px";
    chipEl.classList.add("open");
  }
  focus.addEventListener("click", ev => {
    if (!ev.target.closest(".pop") && !ev.target.closest(".chip")) {
      focus.querySelectorAll(".pop").forEach(p => p.remove());
      focus.querySelectorAll(".chip.open").forEach(p => p.classList.remove("open"));
    }
  });

  // ================================================================== L3: the web (after done)
  function renderWeb(chId, cid) {
    document.querySelectorAll(".web,.webscrim").forEach(n => n.remove());
    const scrim = h("div", { class: "webscrim" });
    scrim.addEventListener("click", () => { location.hash = `#/c/${chId}/${cid}`; });
    const p = h("aside", { class: `web h-${hue(chId)}` });
    const c = C[cid];
    let html = `<button class="x" type="button" aria-label="Close">✕</button><div class="kind" style="font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--hc);font-weight:600">the web</div>
      <h2>${esc(c.title)}</h2><div class="sub">How this connects beyond its chapter. It opens after the concept is done: first learn it on its own, then connect it.</div>`;
    if (!isDone(cid)) html += `<div class="needs">Finish this concept first.</div>`;
    const rs = rel[cid] || [];
    if (rs.length) html += `<h3>Related ideas</h3>` + rs.map(r => `<div class="wl"><span class="rail"></span><div><span class="cx">${CH[chapterOf[r.other]].n}</span><a href="#/c/${chapterOf[r.other]}/${r.other}">${esc(C[r.other].title)}</a><p>${esc(r.note)}</p></div></div>`).join("");
    const xin = preds[cid].filter(x => chapterOf[x] !== chId), xout = succs[cid].filter(x => chapterOf[x] !== chId);
    const line = (x, a, b) => `<div class="wl"><span class="rail"></span><div><span class="cx">${CH[chapterOf[x]].n}</span><a href="#/c/${chapterOf[x]}/${x}">${esc(C[x].title)}</a><p>${esc(EDGE[a + ">" + b].bridge)}</p></div></div>`;
    if (xin.length) html += `<h3>Comes from other chapters</h3>` + xin.map(x => line(x, x, cid)).join("");
    if (xout.length) html += `<h3>Used later in</h3>` + xout.map(x => line(x, cid, x)).join("");
    p.innerHTML = html;
    p.querySelector(".x").addEventListener("click", () => { location.hash = `#/c/${chId}/${cid}`; });
    document.body.appendChild(scrim); document.body.appendChild(p);
    p.animate([{ transform: narrow() ? "translateY(40px)" : "translateX(40px)", opacity: 0 }, { transform: "none", opacity: 1 }], { duration: 320, easing: "cubic-bezier(.2,.8,.2,1)" });
  }

  // ================================================================== router
  let cur = { l: -1 };
  function route() {
    hideTip();
    const parts = (location.hash.replace(/^#\/?/, "") || "").split("/").filter(Boolean);
    const view = $("#view");
    document.querySelectorAll(".web,.webscrim").forEach(n => n.remove());
    if (parts[0] === "c" && C[parts[2]]) {
      const chId = CH[parts[1]] ? parts[1] : chapterOf[parts[2]];
      if (cur.l !== 1 || cur.ch !== chId) { view.innerHTML = ""; prevVisible = null; renderL1(view, chId); }
      cur = { l: 2, ch: chId, c: parts[2] };
      crumbs(chId, parts[2]);
      renderFocus(chId, parts[2], parts[3] === "web");
      cur.l = 1; cur.ch = chId; // the map under focus stays as L1
      return;
    }
    focus.hidden = true; focus.innerHTML = "";
    view.innerHTML = "";
    if (parts[0] === "ch" && CH[parts[1]]) {
      if (cur.ch !== parts[1]) prevVisible = null;
      renderL1(view, parts[1]); crumbs(parts[1]); cur = { l: 1, ch: parts[1] };
    } else { renderL0(view); crumbs(); cur = { l: 0 }; }
    view.scrollTop = 0;
  }
  addEventListener("hashchange", route);
  addEventListener("keydown", e => {
    const parts = (location.hash.replace(/^#\/?/, "") || "").split("/").filter(Boolean);
    if (e.key === "Escape") {
      if (parts[0] === "c" && parts[3] === "web") location.hash = `#/c/${parts[1]}/${parts[2]}`;
      else if (parts[0] === "c") location.hash = `#/ch/${parts[1]}`;
      else if (parts[0] === "ch") location.hash = "#/";
    }
    if (parts[0] === "c" && !parts[3] && (e.key === "ArrowRight" || e.key === "ArrowLeft")) {
      const k = orderIdx[parts[2]] + (e.key === "ArrowRight" ? 1 : -1), id = D.order[k];
      if (id) location.hash = `#/c/${chapterOf[id]}/${id}`;
    }
  });
  let rt; addEventListener("resize", () => { clearTimeout(rt); rt = setTimeout(() => { cur = { l: -1 }; route(); }, 150); });

  // ------------------------------------------------------------------ theme
  $("#theme").addEventListener("click", () => {
    const r = document.documentElement, dark = r.dataset.theme ? r.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
    r.dataset.theme = dark ? "light" : "dark";
    try { localStorage.setItem("theme", r.dataset.theme); } catch (e) { }
  });

  // ------------------------------------------------------------------ prototype controls (not part of the design)
  function proto() {
    const box = $("#proto");
    if (!S.chrome) { box.hidden = true; return; }
    const seg = (key, opts) => `<span class="seg">${opts.map(o => `<button type="button" data-k="${key}" data-v="${o}" class="${S[key] === o ? "on" : ""}">${o}</button>`).join("")}</span>`;
    box.className = "proto" + (S.min ? " min" : "");
    box.innerHTML = `<div class="pt">prototype controls <button type="button" data-min>${S.min ? "▴" : "▾"}</button></div>
      <div class="r"><span>L0 map</span>${seg("l0", ["river", "lanes", "strata"])}</div>
      <div class="r"><span>L1 chapter</span>${seg("l1", ["strict", "ports", "connected"])}</div>
      <div class="r"><span>growth</span><span class="seg"><button type="button" data-g="1" class="${S.growth ? "on" : ""}">on</button><button type="button" data-g="0" class="${S.growth ? "" : "on"}">off (full map)</button></span></div>
      <div class="r"><span>progress</span><input type="range" min="0" max="${D.order.length}" value="${done.size}"><b>${done.size}</b></div>`;
    box.querySelectorAll("[data-k]").forEach(b => b.addEventListener("click", () => { S[b.dataset.k] = b.dataset.v; saveQ(); cur = { l: -1 }; route(); proto(); }));
    box.querySelectorAll("[data-g]").forEach(b => b.addEventListener("click", () => { S.growth = b.dataset.g === "1"; saveQ(); cur = { l: -1 }; route(); proto(); }));
    box.querySelector("[data-min]").addEventListener("click", () => { S.min = !S.min; proto(); });
    const rg = box.querySelector("input");
    rg.addEventListener("input", () => { box.querySelector("b").textContent = rg.value; });
    rg.addEventListener("change", () => { S.p = +rg.value; done = new Set(D.order.slice(0, S.p)); persist(); saveQ(); cur = { l: -1 }; route(); proto(); });
  }

  // self-test (?selftest=1): render every layer/variant/concept, report errors in document.title for --dump-dom
  function selftest() {
    const errs = [];
    let n = 0;
    const tryIt = (label, fn) => { try { fn(); n++; } catch (e) { errs.push(label + ": " + e.message); } };
    for (const g of [true, false]) {
      S.growth = g;
      for (const l0 of ["river", "lanes", "strata"]) { S.l0 = l0; tryIt(`L0 ${l0}`, () => { location.hash = "#/"; cur = { l: -1 }; route(); }); }
      for (const l1 of ["strict", "ports", "connected"]) {
        S.l1 = l1;
        D.chapters.forEach(ch => tryIt(`L1 ${l1} ${ch.id}`, () => { history.replaceState(null, "", location.search + `#/ch/${ch.id}`); cur = { l: -1 }; route(); }));
      }
      D.concepts.forEach(c => {
        tryIt(`L2 ${c.id}`, () => { history.replaceState(null, "", location.search + `#/c/${chapterOf[c.id]}/${c.id}`); route(); });
        tryIt(`L3 ${c.id}`, () => { history.replaceState(null, "", location.search + `#/c/${chapterOf[c.id]}/${c.id}/web`); route(); });
      });
    }
    // data checks: every concept in exactly one chapter, order is topological
    const seen = new Set();
    D.order.forEach((id, k) => { preds[id].forEach(p => { if (orderIdx[p] > k) errs.push(`order: ${p} after ${id}`); }); if (seen.has(id)) errs.push("dup " + id); seen.add(id); });
    if (seen.size !== D.concepts.length) errs.push("order misses concepts");
    document.title = `SELFTEST ${errs.length ? "FAIL" : "PASS"} renders=${n} errors=${errs.length} ` + errs.slice(0, 5).join(" | ");
  }

  loadDone();
  const start = () => { if (Q.get("selftest")) { selftest(); return; } route(); proto(); };
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(start); else start();
})();
