// ece' study — shared: theme toggle + figure steppers (works for figures added later, e.g. in cards).
(function () {
  var root = document.documentElement;

  document.querySelectorAll('.theme').forEach(function (b) {
    b.addEventListener('click', function () {
      var dark = root.dataset.theme
        ? root.dataset.theme === 'dark'
        : matchMedia('(prefers-color-scheme: dark)').matches;
      root.dataset.theme = dark ? 'light' : 'dark';
      try { localStorage.setItem('theme', root.dataset.theme); } catch (e) {}
    });
  });

  function show(fig, n) {
    var max = +fig.dataset.steps;
    n = Math.max(0, Math.min(max, n));
    fig.dataset.step = n;
    fig.querySelectorAll('[data-step]').forEach(function (g) {
      if (g !== fig) g.classList.toggle('off', +g.dataset.step > n);
    });
    var label = fig.querySelector('.step-n');
    if (label) label.textContent = 'step ' + n + ' / ' + max;
  }

  // one delegated handler for every stepper, present or future
  document.addEventListener('click', function (e) {
    var btn = e.target.closest && e.target.closest('.stepper button');
    if (!btn) return;
    var fig = btn.closest('figure[data-steps]'), n = +fig.dataset.step;
    var act = btn.dataset.act;
    show(fig, act === 'next' ? n + 1 : act === 'prev' ? n - 1 : +fig.dataset.steps);
  });

  window.initSteppers = function (scope) {
    (scope || document).querySelectorAll('figure[data-steps]').forEach(function (f) { show(f, 0); });
  };
  window.initSteppers();
})();
