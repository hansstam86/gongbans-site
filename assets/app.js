/* ==========================================================
   GONGBANS — catalogue (boards.html)
   Vanilla JS. Loads data/catalog.json (slim grid data written by
   build_catalog.py), builds the filter chips from the data (category,
   issuer, files, openness), instant search, renders cards 60 at a time
   with "Show more" + auto-load on scroll. Filters live in the URL hash
   (#cat=IoT&issuer=Espressif&files=schematic&open=open_download&q=esp32)
   so any view can be linked.
   ========================================================== */

(async function () {
  const grid = document.getElementById('gongban-grid');
  const searchInput = document.getElementById('search-input');
  const entryCount = document.getElementById('entry-count');
  const showMoreBtn = document.getElementById('show-more');
  const sentinel = document.getElementById('grid-sentinel');
  const resetBtn = document.getElementById('filter-reset');
  const groups = {
    cat: document.getElementById('chips-cat'),
    issuer: document.getElementById('chips-issuer'),
    files: document.getElementById('chips-files'),
    open: document.getElementById('chips-open')
  };

  const PAGE = 60;
  const TOP_ISSUERS = 11;
  let data = null;
  let filtered = [];
  let shown = 0;

  const state = { cat: 'all', issuer: 'all', files: null, open: null, q: '' };

  (function readHash() {
    const h = new URLSearchParams(location.hash.replace(/^#/, ''));
    if (h.get('cat')) state.cat = h.get('cat');
    if (h.get('issuer')) state.issuer = h.get('issuer');
    if (h.get('files')) state.files = h.get('files');
    if (h.get('status')) state.files = h.get('status');          // old deep links
    if (h.get('open')) state.open = h.get('open');
    if (h.get('q')) state.q = h.get('q');
  })();

  function writeHash() {
    const h = new URLSearchParams();
    if (state.cat !== 'all') h.set('cat', state.cat);
    if (state.issuer !== 'all') h.set('issuer', state.issuer);
    if (state.files) h.set('files', state.files);
    if (state.open) h.set('open', state.open);
    if (state.q) h.set('q', state.q);
    const s = h.toString();
    history.replaceState(null, '', s ? '#' + s : location.pathname);
  }

  try {
    const res = await fetch('data/catalog.json');
    data = await res.json();
  } catch (e) {
    grid.innerHTML = '<div class="empty-state">⚠ Couldn\'t load the catalogue. If running locally, serve the folder via <code>python3 -m http.server</code>.</div>';
    console.error(e);
    return;
  }

  const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const fmt = n => n.toLocaleString('en-US');

  const all = data.gongbans;
  all.forEach(g => {
    g._hay = [g.name, g.chip, g.chip_brand, g.issuer, g.application, g.category, g.project_no, g.hint, (g.tags || []).join(' ')]
      .filter(Boolean).join(' ').toLowerCase();
  });

  // ---- chip definitions (from data) ----
  const count = (fn) => all.reduce((m, g) => { const k = fn(g); if (k) m[k] = (m[k] || 0) + 1; return m; }, {});
  const catCounts = count(g => g.category);
  const issuerCounts = count(g => g.issuer);
  const topIssuers = Object.entries(issuerCounts).sort((a, b) => b[1] - a[1]).slice(0, TOP_ISSUERS).map(([k]) => k);
  const otherIssuerCount = all.filter(g => !topIssuers.includes(g.issuer)).length;
  const FILES = [
    ['full-pack', 'Full pack on this site', g => g.status === 'full-pack'],
    ['schematic', 'Schematic', g => g.kinds.includes('schematic')],
    ['pcb', 'PCB layout', g => g.kinds.includes('pcb')],
    ['gerber-bom', 'Gerber / BOM', g => g.kinds.includes('gerber') || g.kinds.includes('bom')],
    ['spec', 'Spec / manual', g => g.kinds.includes('spec')],
    ['links', 'Direct file links', g => g.links > 0],
    ['metadata-only', 'Catalogue entry only', g => g.status === 'metadata-only']
  ];
  const OPEN = [
    ['open_download', 'Open download'], ['registration', 'Registration'], ['with_purchase', 'With purchase'],
    ['contact_atu', 'Via distributor'], ['community', 'Community'], ['hosted', 'Hosted here']
  ].filter(([k]) => all.some(g => g.openness === k));
  const openCounts = count(g => g.openness);

  function chip(type, value, label, n, active) {
    return `<button class="filter-chip${active ? ' active' : ''}" data-type="${esc(type)}" data-value="${esc(value)}" aria-pressed="${active ? 'true' : 'false'}">${esc(label)}${n != null ? `<small>${fmt(n)}</small>` : ''}</button>`;
  }
  function buildChips() {
    groups.cat.innerHTML = chip('cat', 'all', 'All', all.length, state.cat === 'all') +
      (data.categories || Object.keys(catCounts)).filter(c => catCounts[c]).map(c => chip('cat', c, c, catCounts[c], state.cat === c)).join('');
    groups.issuer.innerHTML = chip('issuer', 'all', 'All', null, state.issuer === 'all') +
      topIssuers.map(i => chip('issuer', i, i, issuerCounts[i], state.issuer === i)).join('') +
      (otherIssuerCount ? chip('issuer', 'other', 'Other', otherIssuerCount, state.issuer === 'other') : '');
    groups.files.innerHTML = FILES.map(([k, label, fn]) => chip('files', k, label, all.filter(fn).length, state.files === k)).join('');
    groups.open.innerHTML = OPEN.map(([k, label]) => chip('open', k, label, openCounts[k], state.open === k)).join('');
  }

  // ---- filter ----
  const fileFn = Object.fromEntries(FILES.map(([k, , fn]) => [k, fn]));
  function filter() {
    const q = state.q.toLowerCase();
    const ff = state.files ? fileFn[state.files] : null;
    return all.filter(g => {
      if (state.cat !== 'all' && g.category !== state.cat) return false;
      if (state.issuer !== 'all') {
        if (state.issuer === 'other' ? topIssuers.includes(g.issuer) : g.issuer !== state.issuer) return false;
      }
      if (ff && !ff(g)) return false;
      if (state.open && g.openness !== state.open) return false;
      if (q && !g._hay.includes(q)) return false;
      return true;
    });
  }

  // ---- cards ----
  const STATUS_LABEL = { 'full-pack': 'Full design pack', 'source-files': 'Design files at source', 'metadata-only': 'Catalogue entry' };
  const KIND_SHORT = { schematic: 'SCH', pcb: 'PCB', gerber: 'GBR', bom: 'BOM', spec: 'SPEC', firmware: 'FW', bsp: 'BSP', enclosure: '3D', mech: 'MECH', photos: 'IMG', block_diagram: 'BLK', pcb_lib: 'LIB', sch_lib: 'LIB', artwork: 'ART', presentation: 'PPT', datasheets: 'DS' };

  function renderCard(g) {
    const id = g.project_no || g.issuer || '';
    const tag = [g.category, g.chip || g.hint].filter(Boolean).join(' · ');
    const desc = g.application || (g.chip ? `${g.chip_brand || ''} ${g.chip}`.trim() : '') || (g.kinds.length ? 'Files published: ' + g.kinds.map(k => KIND_SHORT[k] || k).join(', ') : '');
    const kinds = g.kinds.length ? g.kinds.map(k => KIND_SHORT[k] || k.toUpperCase()).filter((v, i, a) => a.indexOf(v) === i).join(' ') : '';
    const right = g.price != null
      ? `CHIP <strong>$${g.price.toFixed(2)}</strong> / 5k`
      : [kinds, g.openness_label, g.year].filter(Boolean).join(' · ');
    return `
      <a class="board ${esc(g.status)}" href="db/${esc(g.slug)}.html">
        <div class="board-id">${esc(id)}</div>
        <h3 class="board-name">${esc(g.name)}</h3>
        <div class="board-tag">${esc(tag)}</div>
        <p class="board-desc clamp">${esc(desc)}</p>
        <div class="board-foot">
          <span class="status ${esc(g.status)}">${STATUS_LABEL[g.status] || ''}</span>
          <span class="meta">${right}</span>
        </div>
      </a>`;
  }

  function appendPage() {
    const slice = filtered.slice(shown, shown + PAGE);
    grid.insertAdjacentHTML('beforeend', slice.map(renderCard).join(''));
    shown += slice.length;
    updateCount();
  }

  function updateCount() {
    const total = all.length;
    entryCount.textContent = filtered.length === total
      ? `${fmt(Math.min(shown, total))} OF ${fmt(total)} BOARDS`
      : `${fmt(Math.min(shown, filtered.length))} OF ${fmt(filtered.length)} MATCHES · ${fmt(total)} BOARDS`;
    const more = filtered.length - shown;
    showMoreBtn.hidden = more <= 0;
    showMoreBtn.textContent = more > 0 ? `Show ${fmt(Math.min(more, PAGE))} more · ${fmt(more)} left` : '';
    const dirty = state.cat !== 'all' || state.issuer !== 'all' || state.files || state.open || state.q;
    resetBtn.hidden = !dirty;
  }

  function render() {
    filtered = filter();
    shown = 0;
    grid.innerHTML = '';
    writeHash();
    if (filtered.length === 0) {
      grid.innerHTML = '<div class="empty-state">No boards match these filters. Try clearing the search or a chip.</div>';
      updateCount();
      return;
    }
    appendPage();
  }

  showMoreBtn.addEventListener('click', appendPage);
  if ('IntersectionObserver' in window && sentinel) {
    new IntersectionObserver(entries => {
      if (entries.some(e => e.isIntersecting) && shown < filtered.length) appendPage();
    }, { rootMargin: '600px 0px' }).observe(sentinel);
  }

  // ---- chip clicks (delegated) ----
  Object.values(groups).forEach(el => el.addEventListener('click', e => {
    const b = e.target.closest('.filter-chip');
    if (!b) return;
    const t = b.dataset.type, v = b.dataset.value;
    if (t === 'cat') state.cat = v;
    else if (t === 'issuer') state.issuer = v;
    else if (t === 'files') state.files = state.files === v ? null : v;
    else if (t === 'open') state.open = state.open === v ? null : v;
    buildChips();
    render();
  }));

  resetBtn.addEventListener('click', () => {
    Object.assign(state, { cat: 'all', issuer: 'all', files: null, open: null, q: '' });
    searchInput.value = '';
    buildChips();
    render();
  });

  let timer = null;
  searchInput.addEventListener('input', e => {
    clearTimeout(timer);
    timer = setTimeout(() => { state.q = e.target.value.trim(); render(); }, 120);
  });
  document.addEventListener('keydown', e => {
    if (e.key === '/' && document.activeElement !== searchInput && !/INPUT|TEXTAREA/.test(document.activeElement.tagName)) { e.preventDefault(); searchInput.focus(); }
  });
  window.addEventListener('hashchange', () => {
    const h = new URLSearchParams(location.hash.replace(/^#/, ''));
    Object.assign(state, { cat: h.get('cat') || 'all', issuer: h.get('issuer') || 'all', files: h.get('files') || null, open: h.get('open') || null, q: h.get('q') || '' });
    searchInput.value = state.q;
    buildChips();
    render();
  });

  searchInput.value = state.q;
  buildChips();
  render();
})();
