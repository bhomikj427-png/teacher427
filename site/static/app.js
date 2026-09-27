// ece' study — theme toggle, figure steppers, table-of-contents highlight.
(function () {
  var root = document.documentElement;

  // theme: explicit choice wins, else follow the OS
  document.querySelectorAll('.theme').forEach(function (b) {
    b.addEventListener('click', function () {
      var dark = root.dataset.theme
        ? root.dataset.theme === 'dark'
        : matchMedia('(prefers-color-scheme: dark)').matches;
      root.dataset.theme = dark ? 'light' : 'dark';
      try { localStorage.setItem('theme', root.dataset.theme); } catch (e) {}
    });
  });

  // steppers: groups tagged data-step appear one at a time
  document.querySelectorAll('figure[data-steps]').forEach(function (fig) {
    var max = +fig.dataset.steps, label = fig.querySelector('.step-n');
    function show(n) {
      n = Math.max(0, Math.min(max, n));
      fig.dataset.step = n;
      fig.querySelectorAll('[data-step]').forEach(function (g) {
        if (g === fig) return;
        g.classList.toggle('off', +g.dataset.step > n);
      });
      label.textContent = 'step ' + n + ' / ' + max;
    }
    fig.querySelector('.stepper').addEventListener('click', function (e) {
      var act = e.target.dataset && e.target.dataset.act, n = +fig.dataset.step;
      if (act === 'next') show(n + 1);
      else if (act === 'prev') show(n - 1);
      else if (act === 'all') show(max);
    });
    show(0);
  });

  // TOC: mark the section currently on screen
  var links = document.querySelectorAll('.toc a');
  if (links.length && 'IntersectionObserver' in window) {
    var byId = {};
    links.forEach(function (a) { byId[a.getAttribute('href').slice(1)] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting && byId[en.target.id]) {
          links.forEach(function (a) { a.classList.remove('on'); });
          byId[en.target.id].classList.add('on');
        }
      });
    }, { rootMargin: '-80px 0px -70% 0px' });
    document.querySelectorAll('main h2[id]').forEach(function (h) { io.observe(h); });
  }
})();
