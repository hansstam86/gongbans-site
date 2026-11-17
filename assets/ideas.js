/* ==========================================================
   GONGBANS — ideas (ideas.html)
   Vanilla JS. The idea cards are static HTML written by
   build_ideas.py; this script adds category / tag chips, instant
   search and sorting over the cards' data-* attributes. State lives
   in the URL hash (#cat=Smart%20home&tag=lorawan&q=knob&sort=margin)
   so any view can be linked.
   ========================================================== */

(function () {
  var grid = document.getElementById('ideas-grid');
  if (!grid) return;
  var cards = Array.prototype.slice.call(grid.querySelectorAll('a.board.idea'));
  var searchInput = document.getElementById('search-input');
  var entryCount = document.getElementById('entry-count');
  var resetBtn = document.getElementById('filter-reset');
  var emptyState = document.getElementById('empty-state');
  var emptyReset = document.getElementById('empty-reset');
  var sortSelect = document.getElementById('sort-select');
  var catChips = document.querySelectorAll('#chips-cat .filter-chip');
  var tagChips = document.querySelectorAll('#chips-tag .filter-chip');

  var state = { cat: 'all', tag: null, q: '', sort: 'score' };

  (function readHash() {
    var h = new URLSearchParams(location.hash.replace(/^#/, ''));
    if (h.get('cat')) state.cat = h.get('cat');
    if (h.get('tag')) state.tag = h.get('tag');
    if (h.get('q')) state.q = h.get('q');
    if (h.get('sort')) state.sort = h.get('sort');
  })();

  function writeHash() {
    var h = new URLSearchParams();
    if (state.cat !== 'all') h.set('cat', state.cat);
    if (state.tag) h.set('tag', state.tag);
    if (state.q) h.set('q', state.q);
    if (state.sort !== 'score') h.set('sort', state.sort);
    var s = h.toString();
    history.replaceState(null, '', s ? '#' + s : location.pathname);
  }

  var SORTERS = {
    score: function (a, b) { return num(b, 'score') - num(a, 'score') || title(a).localeCompare(title(b)); },
    d: function (a, b) { return num(b, 'd') - num(a, 'd') || num(b, 'score') - num(a, 'score') || title(a).localeCompare(title(b)); },
    b: function (a, b) { return num(b, 'b') - num(a, 'b') || num(b, 'score') - num(a, 'score') || title(a).localeCompare(title(b)); },
    m: function (a, b) { return num(b, 'm') - num(a, 'm') || num(b, 'score') - num(a, 'score') || title(a).localeCompare(title(b)); },
    s: function (a, b) { return num(b, 's') - num(a, 's') || num(b, 'score') - num(a, 'score') || title(a).localeCompare(title(b)); },
    title: function (a, b) { return title(a).localeCompare(title(b)); }
  };
  function num(el, k) { return parseInt(el.getAttribute('data-' + k), 10) || 0; }
  function title(el) { return el.getAttribute('data-title') || ''; }

  function matches(el) {
    if (state.cat !== 'all' && el.getAttribute('data-cat') !== state.cat) return false;
    if (state.tag && (' ' + el.getAttribute('data-tags') + ' ').indexOf(' ' + state.tag + ' ') < 0) return false;
    if (state.q) {
      var hay = el.getAttribute('data-hay') || '';
      var terms = state.q.toLowerCase().split(/\s+/).filter(Boolean);
      for (var i = 0; i < terms.length; i++) if (hay.indexOf(terms[i]) < 0) return false;
    }
    return true;
  }

  function render() {
    var sorter = SORTERS[state.sort] || SORTERS.score;
    var sorted = cards.slice().sort(sorter);
    var shown = 0;
    sorted.forEach(function (el) {
      var ok = matches(el);
      el.hidden = !ok;
      if (ok) shown++;
      grid.appendChild(el);          // re-append in sorted order
    });
    if (emptyState) { grid.appendChild(emptyState); emptyState.hidden = shown > 0; }
    if (entryCount) entryCount.textContent = shown === cards.length ? cards.length + ' ideas' : shown + ' of ' + cards.length + ' ideas';
    catChips.forEach(function (c) { c.classList.toggle('active', c.getAttribute('data-cat') === state.cat); });
    tagChips.forEach(function (c) { c.classList.toggle('active', c.getAttribute('data-tag') === state.tag); });
    var dirty = state.cat !== 'all' || state.tag || state.q;
    if (resetBtn) resetBtn.hidden = !dirty;
    if (sortSelect && sortSelect.value !== state.sort) sortSelect.value = state.sort;
    if (searchInput && searchInput.value !== state.q) searchInput.value = state.q;
    writeHash();
  }

  catChips.forEach(function (c) {
    c.addEventListener('click', function () { state.cat = c.getAttribute('data-cat'); render(); });
  });
  tagChips.forEach(function (c) {
    c.addEventListener('click', function () {
      var t = c.getAttribute('data-tag');
      state.tag = state.tag === t ? null : t;
      render();
    });
  });
  function reset() { state.cat = 'all'; state.tag = null; state.q = ''; render(); }
  if (resetBtn) resetBtn.addEventListener('click', reset);
  if (emptyReset) emptyReset.addEventListener('click', reset);
  if (sortSelect) sortSelect.addEventListener('change', function () { state.sort = sortSelect.value; render(); });
  if (searchInput) {
    var timer = null;
    searchInput.addEventListener('input', function () {
      clearTimeout(timer);
      timer = setTimeout(function () { state.q = searchInput.value.trim(); render(); }, 120);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === '/' && document.activeElement !== searchInput && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)) {
        e.preventDefault(); searchInput.focus();
      }
    });
  }
  window.addEventListener('hashchange', function () {
    var h = new URLSearchParams(location.hash.replace(/^#/, ''));
    state.cat = h.get('cat') || 'all'; state.tag = h.get('tag') || null; state.q = h.get('q') || ''; state.sort = h.get('sort') || 'score';
    render();
  });

  render();
})();
