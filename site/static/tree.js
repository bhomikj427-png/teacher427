// ece' study — the subject tree.
// subject → stage → chapter → group → concept. Chapters start folded; opening one grows its branch.
// Groups marked seq draw a spine (each item builds on the one above); other groups fan out (independent).
// Wide screens: left-to-right tree. Narrow screens: indented outline. Same data, same routes:
// ''  ·  #/ch/ID (chapter open)  ·  #/c/ID/CID (concept card open)
(function () {
  var D = JSON.parse(document.getElementById('tree-data').textContent);
  var NS = 'http://www.w3.org/2000/svg';
  var stage = document.getElementById('stage'), box = document.getElementById('tree'), wires = document.getElementById('wires');
  var card = document.getElementById('card'), scrim = document.getElementById('scrim');
  var MARK = { exam: '★', trap: '!' };

  var SEEN = 'seen:' + D.slug, seen = {};
  try { seen = JSON.parse(localStorage.getItem(SEEN) || '{}') || {}; } catch (e) { seen = {}; }
  function markSeen(k) { seen[k] = 1; try { localStorage.setItem(SEEN, JSON.stringify(seen)); } catch (e) {} }

  // ------------------------------------------------------------ model
  var nodes = [], byKey = {};
  function mk(type, title, parent, x) {
    var n = { type: type, title: title, parent: parent, children: [], depth: parent ? parent.depth + 1 : 0 };
    for (var k in x) n[k] = x[k];
    nodes.push(n);
    if (parent) parent.children.push(n);
    return n;
  }
  var root = mk('root', D.title, null, { hue: '' });
  D.stages.forEach(function (s) {
    var st = mk('stage', s.title, root, { hue: s.hue });
    D.chapters.filter(function (c) { return c.stage === s.id; }).forEach(function (c) {
      var ch = mk('chapter', c.title, st, { hue: s.hue, ch: c, open: false });
      byKey['ch:' + c.id] = ch;
      (function add(items, parent) {
        items.forEach(function (it) {
          if (it.group != null) add(it.items, mk('group', it.group, parent, { hue: s.hue, seq: it.seq, ch: c }));
          else byKey['c:' + c.id + '/' + it.id] = mk('concept', it.title, parent, { hue: s.hue, c: it, ch: c, chn: ch });
        });
      })(c.tree, ch);
    });
  });
  var order = nodes.filter(function (n) { return n.type === 'concept' && n.c.ready; });
  function ckey(n) { return n.ch.id + '/' + n.c.id; }
  function chapterOf(n) { while (n && n.type !== 'chapter') n = n.parent; return n; }
  function prevInSeq(n) {
    if (!n.parent || !n.parent.seq) return null;
    var i = n.parent.children.indexOf(n);
    return i > 0 ? n.parent.children[i - 1] : null;
  }
  function needsOf(n) {
    var out = [], p = prevInSeq(n);
    if (p) out.push(p);
    (n.c.needs || []).forEach(function (id) {
      var m = byKey['c:' + n.ch.id + '/' + id];
      if (m && out.indexOf(m) < 0) out.push(m);
    });
    return out;
  }

  // ------------------------------------------------------------ DOM
  function span(cls, text) { var s = document.createElement('span'); s.className = cls; s.textContent = text; return s; }
  nodes.forEach(function (n) {
    var e;
    if (n.type === 'chapter' || n.type === 'concept') { e = document.createElement('button'); e.type = 'button'; }
    else e = document.createElement('div');
    e.className = 'node t-' + n.type + (n.hue ? ' h-' + n.hue : '');
    if (n.type === 'root') {
      e.appendChild(span('title', n.title));
      e.appendChild(span('sub', D.code + ' · ' + D.exam));
    } else if (n.type === 'chapter') {
      e.appendChild(span('num', String(n.ch.n)));
      e.appendChild(span('title', n.title));
      var wt = span('wt', '');
      wt.title = 'Exam weight';
      for (var i = 1; i <= 3; i++) { var b = document.createElement('i'); if (i <= n.ch.weight) b.className = 'on'; wt.appendChild(b); }
      if (n.ch.weight) e.appendChild(wt);
      e.appendChild(span('meta', n.ch.count + (n.ch.ready ? '' : ' · soon')));
      if (!n.ch.ready) e.classList.add('todo');
      e.setAttribute('aria-expanded', 'false');
    } else if (n.type === 'concept') {
      e.classList.add('k-' + n.c.kind);
      if (MARK[n.c.kind]) e.appendChild(span('mk ' + n.c.kind, MARK[n.c.kind]));
      e.appendChild(span('title', n.title));
      if (!n.c.ready) { e.classList.add('todo'); e.setAttribute('aria-disabled', 'true'); e.title = 'Not drawn yet'; }
      else if (n.c.gist) e.title = n.c.gist;
      if (n.c.ready && seen[ckey(n)]) e.classList.add('seen');
    } else {
      e.appendChild(span('title', n.title));
    }
    n.el = e;
    box.appendChild(e);
    if (n.parent) {
      n.wire = document.createElementNS(NS, 'path');
      n.wire.setAttribute('class', 'wire' + (n.hue ? ' h-' + n.hue : ''));
      wires.appendChild(n.wire);
    }
    if (n.type === 'group' && n.seq) {
      n.spine = document.createElementNS(NS, 'path');
      n.spine.setAttribute('class', 'spine h-' + n.hue);
      wires.appendChild(n.spine);
    }
    if (n.parent && n.parent.seq) {
      n.dot = document.createElementNS(NS, 'circle');
      n.dot.setAttribute('class', 'sdot h-' + n.hue);
      n.dot.setAttribute('r', 3.5);
      wires.appendChild(n.dot);
    }
  });

  // ------------------------------------------------------------ layout
  var outline = false;
  function kids(n) { return n.type === 'chapter' && !n.open ? [] : n.children; }
  function visible(n) { for (var p = n.parent; p; p = p.parent) if (p.type === 'chapter' && !p.open) return false; return true; }
  function lcaDepth(a, b) {
    var pa = []; for (var p = a; p; p = p.parent) pa.push(p);
    for (var q = b; q; q = q.parent) if (pa.indexOf(q) >= 0) return q.depth;
    return 0;
  }

  function layout() {
    outline = stage.clientWidth < 760;
    box.classList.toggle('outline', outline);
    nodes.forEach(function (n) { n.w = n.el.offsetWidth; n.h = n.el.offsetHeight; n.vis = visible(n); });
    var W = 0, H = 0, last = null, y = 0;
    function gap(n) {
      if (!last) return 0;
      var d = lcaDepth(last, n);
      var extra = d === 0 ? 30 : d === 1 ? ((last.type === 'chapter' && n.type === 'chapter') ? 4 : 22) : d === 2 ? 12 : 2;
      return extra;
    }
    if (!outline) {
      var col = [];
      (function walk(n) { col[n.depth] = Math.max(col[n.depth] || 0, n.w); kids(n).forEach(walk); })(root);
      var GX = [0, 46, 44, 60, 40], x = [0];
      for (var d = 1; d < col.length; d++) x[d] = x[d - 1] + col[d - 1] + GX[d];
      (function place(n) {
        n.x = x[n.depth];
        var k = kids(n);
        if (!k.length) {
          y += (last ? last.h / 2 + n.h / 2 + 2 : n.h / 2) + gap(n);
          n.y = y; last = n;
        } else {
          k.forEach(place);
          n.y = (k[0].y + k[k.length - 1].y) / 2;
        }
        W = Math.max(W, n.x + n.w); H = Math.max(H, n.y + n.h / 2);
      })(root);
    } else {
      var IND = { root: 0, stage: 0, chapter: 10, group: 34, concept: 34 };
      (function place(n) {
        n.x = IND[n.type] + (n.type === 'concept' && n.parent.type === 'group' ? 22 : 0);
        y += (last ? last.h / 2 + n.h / 2 + 2 : n.h / 2) + (last ? (n.type === 'stage' ? 22 : n.type === 'chapter' ? 2 : n.type === 'group' ? 8 : 0) : 0);
        n.y = y; last = n;
        W = Math.max(W, n.x + n.w); H = Math.max(H, n.y + n.h / 2);
        kids(n).forEach(place);
      })(root);
    }
    // hidden nodes collapse onto their nearest visible ancestor
    nodes.forEach(function (n) {
      if (n.vis) return;
      var p = n.parent; while (!p.vis) p = p.parent;
      n.x = p.x; n.y = p.y;
    });
    box.style.width = Math.ceil(W + 4) + 'px';
    box.style.height = Math.ceil(H + 4) + 'px';
    wires.setAttribute('width', Math.ceil(W + 4)); wires.setAttribute('height', Math.ceil(H + 4));
    nodes.forEach(function (n) {
      n.el.style.transform = 'translate(' + n.x + 'px,' + (n.y - n.h / 2) + 'px)';
      n.el.classList.toggle('hid', !n.vis);
      n.el.tabIndex = n.vis ? 0 : -1;
    });
    drawWires();
  }

  function setD(path, d) { path.style.d = 'path("' + d + '")'; path.setAttribute('d', d); }
  function drawWires() {
    nodes.forEach(function (n) {
      if (!n.wire) return;
      var p = n.parent, d, seqChild = p.seq, first = seqChild && p.children[0] === n;
      if (!outline) {
        var sx = p.x + p.w + 8, sy = p.y, ex = n.x - (seqChild ? 16 : 8), ey = n.y, mx = (sx + ex) / 2;
        if (seqChild && !first) d = 'M' + ex + ',' + ey + ' L' + ex + ',' + ey;   // drawn by the spine instead
        else d = 'M' + sx + ',' + sy + ' C' + mx + ',' + sy + ' ' + mx + ',' + ey + ' ' + ex + ',' + ey;
        if (seqChild) d += ' M' + ex + ',' + ey + ' L' + (n.x - 6) + ',' + ey;
      } else {
        var vx = p.x + (p.type === 'group' ? 10 : 12), vy = p.y + p.h / 2 - 3, hx = n.x - 6;
        d = 'M' + vx + ',' + vy + ' L' + vx + ',' + n.y + ' L' + hx + ',' + n.y;
      }
      if (!n.vis) { var q = n.parent; while (!q.vis) q = q.parent; var ax = outline ? q.x + 12 : q.x + q.w + 8; d = 'M' + ax + ',' + q.y + ' L' + ax + ',' + q.y; }
      setD(n.wire, d);
      n.wire.classList.toggle('hid', !n.vis);
      if (n.dot) {
        var cx = outline ? p.x + 10 : n.x - 16;
        n.dot.style.cx = cx + 'px'; n.dot.style.cy = n.y + 'px';
        n.dot.setAttribute('cx', cx); n.dot.setAttribute('cy', n.y);
        n.dot.classList.toggle('hid', !n.vis);
      }
    });
    nodes.forEach(function (g) {
      if (!g.spine) return;
      var a = g.children[0], b = g.children[g.children.length - 1];
      var sx = outline ? g.x + 10 : a.x - 16, d = 'M' + sx + ',' + a.y + ' L' + sx + ',' + b.y;
      if (!g.vis || !a.vis) d = 'M' + sx + ',' + a.y + ' L' + sx + ',' + a.y;
      setD(g.spine, d);
      g.spine.classList.toggle('hid', !(g.vis && a.vis));
    });
  }

  // ------------------------------------------------------------ focus + highlight
  function inBranch(n, ch) { for (var p = n; p; p = p.parent) if (p === ch) return true; return false; }
  function onPath(n, target) { for (var p = target; p; p = p.parent) if (p === n) return true; return false; }
  function focus(ch) {
    nodes.forEach(function (n) {
      var keep = !ch || inBranch(n, ch) || onPath(n, ch) || n.type === 'chapter' || n.type === 'stage' || n.type === 'root';
      n.el.classList.toggle('dim', !keep || (ch && n.type === 'chapter' && n !== ch));
      if (n.wire) n.wire.classList.toggle('on', !!ch && (inBranch(n, ch) || onPath(n, ch)));
    });
    nodes.forEach(function (n) { if (n.spine) n.spine.classList.toggle('on', !!ch && inBranch(n, ch)); });
  }
  function highlight(n, on) {
    needsOf(n).forEach(function (m) { m.el.classList.toggle('need', on); });
    for (var p = n; p && p.wire; p = p.parent) p.wire.classList.toggle('hot', on);
  }

  // ------------------------------------------------------------ routes
  var cur = null;
  function route() {
    var h = location.hash.replace(/^#\/?/, '').split('/');
    var ch = null, cn = null;
    if (h[0] === 'ch') ch = byKey['ch:' + h[1]];
    if (h[0] === 'c') { cn = byKey['c:' + h[1] + '/' + h[2]]; ch = byKey['ch:' + h[1]]; if (cn && !cn.c.ready) cn = null; }
    var changed = false;
    nodes.forEach(function (n) {
      if (n.type !== 'chapter') return;
      var open = n === ch;
      if (n.open !== open) { n.open = open; changed = true; n.el.setAttribute('aria-expanded', String(open)); n.el.classList.toggle('open', open); }
    });
    if (changed || !box.style.width) layout();
    focus(ch);
    if (cn) openCard(cn);
    else {
      closeCard();
      if (ch && changed) setTimeout(function () { reveal(ch); }, 80);
    }
    cur = { ch: ch, cn: cn };
  }
  function reveal(ch) {
    var top = ch.y, bot = ch.y;
    (function walk(n) { if (!n.vis) return; top = Math.min(top, n.y - n.h / 2); bot = Math.max(bot, n.y + n.h / 2); n.children.forEach(walk); })(ch);
    var r = box.getBoundingClientRect(), sr = stage.getBoundingClientRect();
    var absTop = r.top - sr.top + stage.scrollTop + top, absBot = r.top - sr.top + stage.scrollTop + bot;
    var view = stage.clientHeight;
    var target = absBot - absTop < view - 80 ? (absTop + absBot) / 2 - view / 2 : absTop - 40;
    stage.scrollTo({ top: Math.max(0, target), behavior: 'smooth' });
  }

  // ------------------------------------------------------------ card
  function openCard(n) {
    var tpl = document.getElementById('t-' + n.ch.id + '--' + n.c.id);
    // "open" = visible now; a card still fading out after a close counts as closed, so it animates back in
    var wasOpen = !card.hidden && card.classList.contains('open');
    // keep `open` when swapping cards in place; dropping it faded the card to opacity 0 (it vanished on next/prev)
    card.className = 'card h-' + n.hue + ' k-' + n.c.kind + (wasOpen ? ' open' : '');
    var cr = card.querySelector('.crumbs');
    cr.innerHTML = '';
    var trail = [];
    for (var p = n.parent; p && p.type !== 'stage'; p = p.parent) trail.unshift(p);
    trail.forEach(function (t, i) {
      if (i) cr.appendChild(span('sep', '/'));
      if (t.type === 'chapter') {
        var b = document.createElement('button');
        b.type = 'button'; b.textContent = t.ch.n + ' ' + t.title;
        b.onclick = function () { location.hash = '#/ch/' + t.ch.id; };
        cr.appendChild(b);
      } else cr.appendChild(span('', t.title));
    });
    card.querySelector('#card-title').textContent = n.title;
    card.querySelector('.gist').textContent = n.c.gist || '';
    var bl = card.querySelector('.builds'), needs = needsOf(n);
    bl.innerHTML = '';
    if (needs.length) {
      bl.appendChild(span('lbl', 'Builds on'));
      needs.forEach(function (m) {
        var b = document.createElement('button');
        b.type = 'button'; b.textContent = m.title;
        b.onclick = function () { location.hash = '#/c/' + m.ch.id + '/' + m.c.id; };
        bl.appendChild(b);
      });
    }
    var body = card.querySelector('.card-b');
    body.innerHTML = '';
    body.appendChild(tpl.content.cloneNode(true));
    body.scrollTop = 0;
    if (window.initSteppers) window.initSteppers(body);
    var i = order.indexOf(n), pv = order[i - 1], nx = order[i + 1];
    var inCh = order.filter(function (m) { return m.ch === n.ch; });
    card.querySelector('.pos').textContent = (inCh.indexOf(n) + 1) + ' of ' + inCh.length;
    nav(card.querySelector('.prev'), pv, '← ', '', 'Back to the tree');
    nav(card.querySelector('.next'), nx, '', ' →', 'Back to the tree');
    markSeen(ckey(n)); n.el.classList.add('seen');
    nodes.forEach(function (m) { m.el.classList.remove('current'); });
    n.el.classList.add('current');
    if (wasOpen) {
      if (body.animate) body.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 180 });
      return;
    }
    card.hidden = false; scrim.classList.add('on');
    var r = n.el.getBoundingClientRect(), c = card.getBoundingClientRect();
    card.style.transformOrigin = (r.left + r.width / 2 - c.left) + 'px ' + (r.top + r.height / 2 - c.top) + 'px';
    card.getBoundingClientRect();
    card.classList.add('open');
  }
  function nav(btn, target, pre, post, fallback) {
    btn.textContent = target ? pre + target.title + post : (pre ? '← ' : '') + fallback + (post ? ' →' : '');
    btn.onclick = function () {
      location.hash = target ? '#/c/' + target.ch.id + '/' + target.c.id : (cur && cur.ch ? '#/ch/' + cur.ch.ch.id : '');
    };
  }
  function closeCard() {
    if (card.hidden) return;
    card.classList.remove('open'); scrim.classList.remove('on');
    nodes.forEach(function (m) { m.el.classList.remove('current'); });
    setTimeout(function () { if (!card.classList.contains('open')) card.hidden = true; }, 220);
  }
  function back() { location.hash = cur && cur.ch ? '#/ch/' + cur.ch.ch.id : ''; }
  card.querySelector('.card-x').onclick = back;
  scrim.onclick = back;

  // ------------------------------------------------------------ input
  nodes.forEach(function (n) {
    if (n.type === 'chapter') n.el.onclick = function () { location.hash = n.open ? '' : '#/ch/' + n.ch.id; };
    if (n.type === 'concept') {
      n.el.onclick = function () { if (n.c.ready) location.hash = '#/c/' + n.ch.id + '/' + n.c.id; };
      n.el.onmouseenter = function () { highlight(n, true); };
      n.el.onmouseleave = function () { highlight(n, false); };
      n.el.onfocus = function () { highlight(n, true); };
      n.el.onblur = function () { highlight(n, false); };
    }
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      if (!card.hidden) back();
      else if (cur && cur.ch) location.hash = '';
    } else if (!card.hidden && (e.key === 'ArrowRight' || e.key === 'ArrowLeft')) {
      card.querySelector(e.key === 'ArrowRight' ? '.next' : '.prev').click();
    }
  });
  window.addEventListener('hashchange', route);
  var lastW = stage.clientWidth;
  window.addEventListener('resize', function () {
    if ((stage.clientWidth < 760) !== (lastW < 760)) { lastW = stage.clientWidth; layout(); focus(cur && cur.ch); }
  });

  // fonts change text widths: lay out once they are ready
  box.classList.add('instant');
  route();
  (document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve()).then(function () {
    layout(); focus(cur && cur.ch);
    requestAnimationFrame(function () { box.classList.remove('instant'); });
  });
})();
