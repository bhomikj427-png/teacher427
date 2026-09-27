// ece' study — the subject map: one page, every chapter an island, every concept a node.
// Overview → click a chapter (zoom in) → click a concept (zoom in + open its card).
// Routes live in the URL hash so the browser Back button walks back out: '', #/ch/ID, #/c/ID/CID.
(function () {
  var D = JSON.parse(document.getElementById('map-data').textContent);
  var NS = 'http://www.w3.org/2000/svg';
  var vp = document.getElementById('viewport'), svg = document.getElementById('map'), cam = document.getElementById('cam');
  var card = document.getElementById('card'), scrim = document.getElementById('scrim');
  var TOP = 56, HUB = 80, DOT = 23;
  var hue = {}; D.stages.forEach(function (s) { hue[s.id] = s.hue; });
  var KIND = { idea: ['◆', 'idea'], method: ['▶', 'method'], exam: ['★', 'exam question'], trap: ['!', 'trap'], practice: ['✎', 'practice'] };

  // ---------------------------------------------------------------- seen (per-viewer convenience only)
  var SEEN = 'seen:' + D.slug, seen = {};
  try { seen = JSON.parse(localStorage.getItem(SEEN) || '{}') || {}; } catch (e) { seen = {}; }
  function markSeen(k) { seen[k] = 1; try { localStorage.setItem(SEEN, JSON.stringify(seen)); } catch (e) {} }

  // ---------------------------------------------------------------- helpers
  function el(tag, attrs, parent, text) {
    var n = document.createElementNS(NS, tag);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    if (text != null) n.textContent = text;
    if (parent) parent.appendChild(n);
    return n;
  }
  function wrap(s, max) {
    var words = s.split(' '), lines = [''];
    words.forEach(function (w) {
      var cur = lines[lines.length - 1];
      if (cur && (cur + ' ' + w).length > max) lines.push(w); else lines[lines.length - 1] = cur ? cur + ' ' + w : w;
    });
    return lines;
  }
  function byId(id) { for (var i = 0; i < D.chapters.length; i++) if (D.chapters[i].id === id) return D.chapters[i]; }
  function key(ch, c) { return ch.id + '/' + c.id; }

  // ---------------------------------------------------------------- layout
  var W, H, portrait, bounds;
  function layout() {
    W = vp.clientWidth; H = vp.clientHeight; portrait = W < H * 0.9;
    var maxR = 0;
    D.chapters.forEach(function (ch) { ch.R = Math.max(150, ch.concepts.length * 19); maxR = Math.max(maxR, ch.R); });
    var cw = 2 * (maxR + 190), chh = 2 * (maxR + 95);
    var n = D.chapters.length, cols = 1, best = 0;
    for (var tc = 1; tc <= n; tc++) {                // pick the grid that shows the islands biggest
      var tr = Math.ceil(n / tc), sc = Math.min(W / (tc * cw), (H - TOP) / (tr * chh));
      if (sc > best * 1.001) { best = sc; cols = tc; }
    }
    var ordered = D.chapters.slice().sort(function (a, b) { return a.n - b.n; });
    ordered.forEach(function (ch, i) {
      var r = Math.floor(i / cols), c = i % cols;
      if (r % 2 === 1) c = cols - 1 - c;              // snake, so the next chapter is always a neighbour
      ch.x = c * cw + cw / 2; ch.y = r * chh + chh / 2;
      ch.box = [ch.x - ch.R - 200, ch.y - ch.R - 95, 2 * (ch.R + 200), 2 * (ch.R + 95)];
    });
    var rows = Math.ceil(n / cols);
    bounds = [0, 0, cols * cw, rows * chh];
    draw();
  }

  function draw() {
    cam.textContent = '';
    var defs = el('defs', {}, cam);
    var mk = el('marker', { id: 'arr', viewBox: '0 0 10 10', refX: 8, refY: 5, markerWidth: 6, markerHeight: 6, orient: 'auto' }, defs);
    el('path', { d: 'M0,0 L10,5 L0,10 z', 'class': 'edge-head' }, mk);
    var gE = el('g', { 'class': 'edges' }, cam), gI = el('g', { 'class': 'islands' }, cam);
    D.edges.forEach(function (e) {
      var a = D.chapters.filter(function (c) { return c.n === e[0]; })[0], b = D.chapters.filter(function (c) { return c.n === e[1]; })[0];
      var dx = b.x - a.x, dy = b.y - a.y, len = Math.hypot(dx, dy), ux = dx / len, uy = dy / len;
      var sx = a.x + ux * (a.R + DOT + 20), sy = a.y + uy * (a.R + DOT + 20), ex = b.x - ux * (b.R + DOT + 26), ey = b.y - uy * (b.R + DOT + 26);
      var mx = (sx + ex) / 2 - uy * 40, my = (sy + ey) / 2 + ux * 40;
      el('path', { d: 'M' + sx + ',' + sy + ' Q' + mx + ',' + my + ' ' + ex + ',' + ey, 'class': 'edge h-' + hue[b.stage], 'marker-end': 'url(#arr)' }, gE);
    });
    var nextUp = firstUnseen();
    D.chapters.forEach(function (ch) {
      var g = el('g', { 'class': 'island h-' + hue[ch.stage] + (ch.ready ? ' ready' : ' todo'), 'data-ch': ch.id }, gI);
      el('circle', { cx: ch.x, cy: ch.y, r: ch.R + 58, 'class': 'isl-bg' }, g);
      var n = ch.concepts.length;
      ch.concepts.forEach(function (c, k) {
        var a = -Math.PI / 2 + k * 2 * Math.PI / n, ca = Math.cos(a), sa = Math.sin(a);
        var px = ch.x + ch.R * ca, py = ch.y + ch.R * sa;
        c.x = px; c.y = py;
        el('line', { x1: ch.x + (HUB + 4) * ca, y1: ch.y + (HUB + 4) * sa, x2: px - DOT * ca, y2: py - DOT * sa, 'class': 'spoke' }, g);
        var cls = 'cn k-' + c.kind + (c.ready ? ' ready' : ' todo') + (seen[key(ch, c)] ? ' seen' : '') +
          (nextUp && nextUp[1] === c ? ' next-up' : '');
        var cg = el('g', { 'class': cls, 'data-c': c.id, 'data-ch': ch.id, tabindex: c.ready ? 0 : -1 }, g);
        el('title', {}, cg, c.title + (c.gist ? ' — ' + c.gist : '') + (c.ready ? '' : ' (not drawn yet)'));
        el('circle', { cx: px, cy: py, r: DOT + 9, 'class': 'cn-halo' }, cg);
        el('circle', { cx: px, cy: py, r: DOT, 'class': 'cn-dot' }, cg);
        el('text', { x: px, y: py + 6, 'class': 'cn-num', 'text-anchor': 'middle' }, cg, String(k + 1));
        var bx = px + DOT * 0.78, by = py - DOT * 0.78;
        el('circle', { cx: bx, cy: by, r: 10, 'class': 'cn-badge' }, cg);
        el('text', { x: bx, y: by + 4.5, 'class': 'cn-glyph', 'text-anchor': 'middle' }, cg, KIND[c.kind][0]);
        var lr = DOT + 16, lx = px + lr * ca, ly = py + lr * sa;
        var anchor = ca > 0.12 ? 'start' : ca < -0.12 ? 'end' : 'middle';
        var lines = wrap(c.title, 20).slice(0, 3), lh = 19;
        var y0 = anchor === 'middle' ? (sa < 0 ? ly - (lines.length - 1) * lh - 4 : ly + 14) : ly + 6 - (lines.length - 1) * lh / 2;
        var t = el('text', { x: lx, y: y0, 'class': 'cn-lab', 'text-anchor': anchor }, cg);
        lines.forEach(function (ln, i) { el('tspan', { x: lx, dy: i ? lh : 0 }, t, ln); });
      });
      // hub
      var hg = el('g', { 'class': 'hub', 'data-hub': ch.id, tabindex: 0 }, g);
      el('title', {}, hg, 'Chapter ' + ch.n + ': ' + ch.title + (ch.note ? ' — ' + ch.note : ''));
      el('circle', { cx: ch.x, cy: ch.y, r: HUB, 'class': 'hub-c' }, hg);
      el('text', { x: ch.x, y: ch.y - 34, 'class': 'hub-n', 'text-anchor': 'middle' }, hg, 'CHAPTER ' + ch.n);
      var tl = wrap(ch.title, 13).slice(0, 3), ty = ch.y - 4 - (tl.length - 1) * 9;
      var tt = el('text', { x: ch.x, y: ty, 'class': 'hub-t', 'text-anchor': 'middle' }, hg);
      tl.forEach(function (ln, i) { el('tspan', { x: ch.x, dy: i ? 19 : 0 }, tt, ln); });
      var dots = ch.weight ? 'weight ' + '●●●'.slice(0, ch.weight) + '○○○'.slice(0, 3 - ch.weight) : '';
      el('text', { x: ch.x, y: ch.y + 50, 'class': 'hub-w', 'text-anchor': 'middle' }, hg, ch.ready ? dots : 'coming soon');
      // far-zoom label: one big readable name over the island
      var fg = el('g', { 'class': 'far-lab' }, g);
      var fl = wrap(ch.n + '  ' + ch.title, 15).slice(0, 3), fw = Math.max.apply(null, fl.map(function (s) { return s.length; })) * 25 + 90;
      var fh = 70 + (fl.length - 1) * 50;
      el('rect', { x: ch.x - fw / 2, y: ch.y - fh / 2, width: fw, height: fh, rx: 26, 'class': 'far-bg' }, fg);
      var ft = el('text', { x: ch.x, y: ch.y + 16 - (fl.length - 1) * 25, 'class': 'far-t', 'text-anchor': 'middle' }, fg);
      fl.forEach(function (ln, i) { el('tspan', { x: ch.x, dy: i ? 50 : 0 }, ft, ln); });
      el('text', { x: ch.x, y: ch.y + fh / 2 + 44, 'class': 'far-s', 'text-anchor': 'middle' }, fg,
        ch.ready ? ch.concepts.length + ' concepts · ready' : ch.concepts.length + ' concepts · coming soon');
    });
  }

  function firstUnseen() {
    for (var i = 0; i < D.chapters.length; i++) {
      var ch = D.chapters[i];
      for (var j = 0; j < ch.concepts.length; j++) if (ch.concepts[j].ready && !seen[key(ch, ch.concepts[j])]) return [ch, ch.concepts[j]];
    }
  }

  // ---------------------------------------------------------------- camera
  var V = { x: 0, y: 0, s: 1 }, anim = null;
  function apply() {
    cam.setAttribute('transform', 'translate(' + V.x + ',' + V.y + ') scale(' + V.s + ')');
    svg.classList.toggle('far', V.s < 0.62 && !cur.ch);
    svg.classList.toggle('near', V.s >= 1.15);
  }
  function fitView(b, pad, bottom) {
    pad = pad == null ? 28 : pad; bottom = bottom || 0;
    var h = H - TOP - bottom;
    var s = Math.min((W - 2 * pad) / b[2], (h - 2 * pad) / b[3]);
    s = Math.max(0.12, Math.min(s, 2.4));
    return { s: s, x: W / 2 - (b[0] + b[2] / 2) * s, y: TOP + h / 2 - (b[1] + b[3] / 2) * s };
  }
  function centerOn(x, y, s) { return { s: s, x: W / 2 - x * s, y: TOP + (H - TOP) / 2 - y * s }; }
  function go(T, ms, done) {
    if (anim) cancelAnimationFrame(anim.id);
    if (!ms || matchMedia('(prefers-reduced-motion: reduce)').matches) { V = T; apply(); if (done) done(); return; }
    var F = { x: V.x, y: V.y, s: V.s }, t0 = performance.now();
    // zoom in log space so the motion feels even
    var ls0 = Math.log(F.s), ls1 = Math.log(T.s);
    anim = { id: 0 };
    (function step(now) {
      var p = Math.min(1, (now - t0) / ms), e = p < .5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2;
      var s = Math.exp(ls0 + (ls1 - ls0) * e);
      // keep the world point under the viewport centre moving in a straight line
      var cx0 = (W / 2 - F.x) / F.s, cy0 = (TOP + (H - TOP) / 2 - F.y) / F.s;
      var cx1 = (W / 2 - T.x) / T.s, cy1 = (TOP + (H - TOP) / 2 - T.y) / T.s;
      var cx = cx0 + (cx1 - cx0) * e, cy = cy0 + (cy1 - cy0) * e;
      V = { s: s, x: W / 2 - cx * s, y: TOP + (H - TOP) / 2 - cy * s };
      apply();
      if (p < 1) anim.id = requestAnimationFrame(step); else { anim = null; if (done) done(); }
    })(t0);
  }
  function zoomAt(px, py, f) {
    var s = Math.max(0.12, Math.min(4, V.s * f)), k = s / V.s;
    V = { s: s, x: px - (px - V.x) * k, y: py - (py - V.y) * k };
    apply();
  }

  // ---------------------------------------------------------------- routes
  var cur = { ch: null, c: null };
  function route(ms) {
    var h = location.hash.replace(/^#\/?/, '').split('/');
    hideSheet();
    var chEl = document.querySelector('.crumb-ch');
    if (h[0] === 'c' && byId(h[1])) {
      var ch = byId(h[1]), c = ch.concepts.filter(function (x) { return x.id === h[2]; })[0];
      if (!c || !c.ready) { location.hash = '#/ch/' + ch.id; return; }
      crumb(ch);
      var s = Math.max(1.5, Math.min(2.2, W / 700));
      var reopen = !card.hidden;
      cur = { ch: ch, c: c };
      focusIsland(ch);
      if (reopen) { openCard(ch, c, true); go(centerOn(c.x, c.y, s), ms == null ? 600 : ms); }
      else go(centerOn(c.x, c.y, s), ms == null ? 700 : ms, function () { openCard(ch, c, false); });
    } else if (h[0] === 'ch' && byId(h[1])) {
      var ch2 = byId(h[1]);
      closeCard(); crumb(ch2); focusIsland(ch2); cur = { ch: ch2, c: null };
      if (W < 700) {                                   // phone: ring on top, readable list below
        var sh = sheet(ch2);
        go(fitView([ch2.x - ch2.R - 40, ch2.y - ch2.R - 40, 2 * ch2.R + 80, 2 * ch2.R + 80], 10, sh), ms == null ? 750 : ms);
      } else go(fitView(ch2.box, 18), ms == null ? 750 : ms);
    } else {
      closeCard(); crumb(null); focusIsland(null); cur = { ch: null, c: null };
      go(fitView(bounds), ms == null ? 750 : ms);
    }
    if (chEl) chEl.hidden = !cur.ch;
  }
  var sheetEl = document.getElementById('chsheet');
  function sheet(ch) {
    sheetEl.innerHTML = '';
    var hd = document.createElement('div');
    hd.className = 'sh-h h-' + hue[ch.stage];
    hd.textContent = 'Chapter ' + ch.n + ' · ' + ch.concepts.length + ' concepts';
    sheetEl.appendChild(hd);
    ch.concepts.forEach(function (c, i) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'sh-i h-' + hue[ch.stage] + ' k-' + c.kind + (c.ready ? '' : ' todo') + (seen[key(ch, c)] ? ' seen' : '');
      b.innerHTML = '<span class="sh-n"></span><span class="sh-k"></span><span class="sh-t"></span>';
      b.querySelector('.sh-n').textContent = i + 1;
      b.querySelector('.sh-k').textContent = KIND[c.kind][0];
      b.querySelector('.sh-t').textContent = c.title;
      b.onclick = function () {
        if (!c.ready) { toast('“' + c.title + '” is in the text pack; not drawn yet.'); return; }
        location.hash = '#/c/' + ch.id + '/' + c.id;
      };
      sheetEl.appendChild(b);
    });
    sheetEl.hidden = false;
    svg.classList.add('sheet');
    return sheetEl.getBoundingClientRect().height + 12;
  }
  function hideSheet() { sheetEl.hidden = true; svg.classList.remove('sheet'); }
  function crumb(ch) {
    var e = document.querySelector('.crumb-ch');
    if (!ch) { e.hidden = true; return; }
    e.hidden = false;
    e.className = 'crumb-ch h-' + hue[ch.stage];
    e.innerHTML = '';
    var b = document.createElement('button');
    b.type = 'button'; b.textContent = ch.n + ' · ' + ch.title;
    b.onclick = function () { location.hash = '#/ch/' + ch.id; };
    e.appendChild(b);
  }
  function focusIsland(ch) {
    svg.classList.toggle('focused', !!ch);
    svg.querySelectorAll('.island').forEach(function (g) { g.classList.toggle('on', !!ch && g.dataset.ch === ch.id); });
  }

  // ---------------------------------------------------------------- card
  function readyList(ch) { return ch.concepts.filter(function (c) { return c.ready; }); }
  function neighbour(ch, c, dir) {
    var list = readyList(ch), i = list.indexOf(c) + dir;
    if (i >= 0 && i < list.length) return [ch, list[i]];
    var ci = D.chapters.indexOf(ch) + dir;
    for (; ci >= 0 && ci < D.chapters.length; ci += dir) {
      var l2 = readyList(D.chapters[ci]);
      if (l2.length) return [D.chapters[ci], dir > 0 ? l2[0] : l2[l2.length - 1]];
    }
    return null;
  }
  function openCard(ch, c, swap) {
    var tpl = document.getElementById('t-' + ch.id + '--' + c.id);
    card.className = 'card h-' + hue[ch.stage] + ' k-' + c.kind;
    card.querySelector('.card-ch').textContent = 'Chapter ' + ch.n + ' · ' + ch.title;
    card.querySelector('.card-kind').textContent = KIND[c.kind][0] + ' ' + KIND[c.kind][1];
    card.querySelector('#card-title').textContent = c.title;
    card.querySelector('.card-gist').textContent = c.gist || '';
    var body = card.querySelector('.card-b');
    body.innerHTML = '';
    body.appendChild(tpl.content.cloneNode(true));
    body.scrollTop = 0;
    if (window.initSteppers) window.initSteppers(body);
    var pips = card.querySelector('.pips');
    pips.innerHTML = '';
    readyList(ch).forEach(function (x, i) {
      var p = document.createElement('button');
      p.type = 'button';
      p.className = 'pip k-' + x.kind + (x === c ? ' on' : '') + (seen[key(ch, x)] ? ' seen' : '');
      p.title = (i + 1) + '. ' + x.title;
      p.setAttribute('aria-label', p.title);
      p.onclick = function () { location.hash = '#/c/' + ch.id + '/' + x.id; };
      pips.appendChild(p);
    });
    var pv = neighbour(ch, c, -1), nx = neighbour(ch, c, 1);
    setNav(card.querySelector('.prev'), pv, 'Chapter map', '#/ch/' + ch.id);
    setNav(card.querySelector('.next'), nx, 'Back to the map', '#/ch/' + ch.id);
    markSeen(key(ch, c));
    var node = svg.querySelector('.cn[data-ch="' + ch.id + '"][data-c="' + c.id + '"]');
    svg.querySelectorAll('.cn.current').forEach(function (n) { n.classList.remove('current'); });
    if (node) { node.classList.add('seen', 'current'); node.classList.remove('next-up'); }
    if (swap && !card.hidden) {
      card.classList.add('open');
      if (body.animate) body.animate([{ opacity: 0, transform: 'translateY(10px)' }, { opacity: 1, transform: 'none' }], { duration: 260, easing: 'ease-out' });
      return;
    }
    // grow out of the node
    card.hidden = false; scrim.classList.add('on');
    var r = node ? node.getBoundingClientRect() : { left: W / 2, top: H / 2, width: 0, height: 0 };
    var cr = card.getBoundingClientRect();
    var dx = r.left + r.width / 2 - (cr.left + cr.width / 2), dy = r.top + r.height / 2 - (cr.top + cr.height / 2);
    card.style.transition = 'none';
    card.style.transform = 'translate(' + dx + 'px,' + dy + 'px) scale(0.04)';
    card.style.opacity = '0';
    card.getBoundingClientRect();
    card.style.transition = '';
    card.style.transform = '';
    card.style.opacity = '';
    card.classList.add('open');
    setTimeout(function () { var b = card.querySelector('.card-x'); if (b) b.focus({ preventScroll: true }); }, 350);
  }
  function setNav(btn, target, fallback, fallbackHash) {
    btn.querySelector('span').textContent = target ? target[1].title : fallback;
    btn.onclick = function () { location.hash = target ? '#/c/' + target[0].id + '/' + target[1].id : fallbackHash; };
  }
  function closeCard() {
    if (card.hidden) return;
    card.classList.remove('open'); scrim.classList.remove('on');
    svg.querySelectorAll('.cn.current').forEach(function (n) { n.classList.remove('current'); });
    setTimeout(function () { if (!card.classList.contains('open')) card.hidden = true; }, 260);
  }
  card.querySelector('.card-x').onclick = function () { location.hash = cur.ch ? '#/ch/' + cur.ch.id : ''; };
  scrim.onclick = card.querySelector('.card-x').onclick;

  // ---------------------------------------------------------------- input: click, drag, pinch, wheel, keys
  var pts = {}, down = null, moved = false, pinch = null;
  vp.addEventListener('pointerdown', function (e) {
    pts[e.pointerId] = { x: e.clientX, y: e.clientY };
    vp.setPointerCapture(e.pointerId);
    if (Object.keys(pts).length === 1) { down = { x: e.clientX, y: e.clientY, target: e.target }; moved = false; }
    else { var p = Object.values(pts); pinch = { d: Math.hypot(p[0].x - p[1].x, p[0].y - p[1].y) }; moved = true; }
    if (anim) { cancelAnimationFrame(anim.id); anim = null; }
    hideHint();
  });
  vp.addEventListener('pointermove', function (e) {
    if (!pts[e.pointerId]) return;
    var prev = pts[e.pointerId];
    pts[e.pointerId] = { x: e.clientX, y: e.clientY };
    var ids = Object.keys(pts);
    if (ids.length === 2 && pinch) {
      var p = Object.values(pts), d = Math.hypot(p[0].x - p[1].x, p[0].y - p[1].y);
      zoomAt((p[0].x + p[1].x) / 2, (p[0].y + p[1].y) / 2, d / pinch.d);
      pinch.d = d;
      return;
    }
    if (down && (moved || Math.hypot(e.clientX - down.x, e.clientY - down.y) > 5)) {
      moved = true; vp.classList.add('dragging');
      V.x += e.clientX - prev.x; V.y += e.clientY - prev.y; apply();
    }
  });
  function up(e) {
    delete pts[e.pointerId];
    if (Object.keys(pts).length < 2) pinch = null;
    vp.classList.remove('dragging');
    if (down && !moved && Object.keys(pts).length === 0) activate(down.target);
    if (!Object.keys(pts).length) down = null;
  }
  vp.addEventListener('pointerup', up);
  vp.addEventListener('pointercancel', up);
  vp.addEventListener('wheel', function (e) {
    e.preventDefault(); hideHint();
    if (anim) { cancelAnimationFrame(anim.id); anim = null; }
    zoomAt(e.clientX, e.clientY, Math.exp(-e.deltaY * (e.ctrlKey ? 0.01 : 0.0016)));
  }, { passive: false });

  function activate(t) {
    var cn = t.closest && t.closest('.cn'), hub = t.closest && t.closest('.hub'), isl = t.closest && t.closest('.island');
    if (cn) {
      var ch = byId(cn.dataset.ch), c = ch.concepts.filter(function (x) { return x.id === cn.dataset.c; })[0];
      if (!c.ready) { toast('“' + c.title + '” is in the text pack; not drawn yet.'); return; }
      location.hash = '#/c/' + ch.id + '/' + c.id;
    } else if (hub || isl) {
      var id = (hub || isl).dataset.hub || (hub || isl).dataset.ch;
      if (location.hash === '#/ch/' + id) route(); else location.hash = '#/ch/' + id;
    }
  }
  svg.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); activate(e.target); }
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      if (!card.hidden) location.hash = '#/ch/' + cur.ch.id;
      else if (cur.ch) location.hash = '';
    } else if (!card.hidden && !e.target.closest('input,textarea') && (e.key === 'ArrowRight' || e.key === 'ArrowLeft')) {
      (e.key === 'ArrowRight' ? card.querySelector('.next') : card.querySelector('.prev')).click();
    }
  });
  document.querySelectorAll('.zoom button').forEach(function (b) {
    b.onclick = function () {
      if (b.dataset.z === 'fit') { route(); return; }
      var f = b.dataset.z === 'in' ? 1.4 : 1 / 1.4, s = V.s * f;
      var cx = (W / 2 - V.x) / V.s, cy = (TOP + (H - TOP) / 2 - V.y) / V.s;
      go(centerOn(cx, cy, Math.max(0.12, Math.min(4, s))), 300);
    };
  });
  document.querySelector('.crumb').onclick = function () { location.hash = ''; };
  var lg = document.getElementById('legend'), lgb = lg.querySelector('.lg-toggle');
  lgb.onclick = function () { var c = lg.classList.toggle('closed'); lgb.setAttribute('aria-expanded', String(!c)); };
  if (innerWidth < 700) { lg.classList.add('closed'); lgb.setAttribute('aria-expanded', 'false'); }

  var hint = document.getElementById('hint'), hintT = setTimeout(hideHint, 7000);
  if (matchMedia('(pointer: coarse)').matches) hint.textContent = 'Tap a chapter · pinch to zoom · drag to move';
  function hideHint() { hint.classList.add('gone'); clearTimeout(hintT); }
  var toastT;
  function toast(msg) {
    var t = document.getElementById('toast');
    t.textContent = msg; t.classList.add('on');
    clearTimeout(toastT); toastT = setTimeout(function () { t.classList.remove('on'); }, 2600);
  }

  window.addEventListener('hashchange', function () { route(); });
  window.addEventListener('resize', function () {
    var wasP = portrait;
    W = vp.clientWidth; H = vp.clientHeight;
    if ((W < H * 0.9) !== wasP) layout();
    route(0);
  });

  layout();
  V = fitView(bounds); apply();
  route(0);
})();
