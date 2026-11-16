/* ==========================================================
   GONGBANS — catalogue (boards.html)
   Vanilla JS. Loads data/catalog.json (slim grid data written by
   build_catalog.py), builds the filter chips from the data (category,
   issuer, files, openness), instant search, renders cards 60 at a time
   with "Show more" + auto-load on scroll. Filters live in the URL hash
   (#cat=IoT&issuer=Espressif&files=schematic&open=open_download&q=esp32&beginner=1)
   so any view can be linked; `?beginner=1` as a query string works too
   (start.html links to it). Chip/badge wording is plain language for
   first-time founders; the data keys are unchanged.
   ========================================================== */

(async function () {
  const grid = document.getElementById('gongban-grid');
  const searchInput = document.getElementById('search-input');
  const entryCount = document.getElementById('entry-count');
  const showMoreBtn = document.getElementById('show-more');
  const sentinel = document.getElementById('grid-sentinel');
  const resetBtn = document.getElementById('filter-reset');
  const quickNote = document.getElementById('quick-note');
  const groups = {
    quick: document.getElementById('chips-quick'),
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

  const state = { cat: 'all', issuer: 'all', files: null, open: null, q: '', beginner: false };

  const flag = (p, k) => p.has(k) && p.get(k) !== '0' && p.get(k) !== 'false';
  (function readHash() {
    const h = new URLSearchParams(location.hash.replace(/^#/, ''));
    const qs = new URLSearchParams(location.search);
    if (h.get('cat')) state.cat = h.get('cat');
    if (h.get('issuer')) state.issuer = h.get('issuer');
    if (h.get('files')) state.files = h.get('files');
    if (h.get('status')) state.files = h.get('status');          // old deep links
    if (h.get('open')) state.open = h.get('open');
    if (h.get('q')) state.q = h.get('q');
    if (flag(h, 'beginner') || flag(qs, 'beginner')) state.beginner = true;
  })();

  function writeHash() {
    const h = new URLSearchParams();
    if (state.cat !== 'all') h.set('cat', state.cat);
    if (state.issuer !== 'all') h.set('issuer', state.issuer);
    if (state.files) h.set('files', state.files);
    if (state.open) h.set('open', state.open);
    if (state.q) h.set('q', state.q);
    if (state.beginner) h.set('beginner', '1');
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
  const FREE = g => g.openness === 'open_download' || g.openness === 'hosted';
  // Beginner-friendly = free to download AND at least one real design file (schematic, PCB layout or Gerber).
  // Community boards pass too: they still need a licence check (the note under the chip says so).
  const BEGINNER = g => FREE(g) && ['schematic', 'pcb', 'gerber'].some(k => g.kinds.includes(k));
  const nBeginner = all.filter(BEGINNER).length;
  const FILES = [
    ['full-pack', 'Full design pack on this site', g => g.status === 'full-pack'],
    ['schematic', 'Schematic (circuit drawing)', g => g.kinds.includes('schematic')],
    ['pcb', 'PCB layout (board drawing)', g => g.kinds.includes('pcb')],
    ['gerber-bom', 'Gerber (factory files) / BOM (parts list)', g => g.kinds.includes('gerber') || g.kinds.includes('bom')],
    ['spec', 'Spec sheet / manual', g => g.kinds.includes('spec')],
    ['links', 'Direct links to the files', g => g.links > 0],
    ['metadata-only', 'Specs only, no files', g => g.status === 'metadata-only']
  ];
  // same wording as OPENNESS_PLAIN in build_detail_pages.py
  const OPEN_LABEL = {
    open_download: 'Free download', registration: 'Free account needed', with_purchase: 'Comes with purchase',
    contact_atu: 'Ask the distributor', community: 'Community project', hosted: 'Download here (full pack)',
    contact_issuer: 'Datasheet public, files via maker'
  };
  const OPEN = ['open_download', 'hosted', 'registration', 'with_purchase', 'contact_atu', 'contact_issuer', 'community']
    .filter(k => all.some(g => g.openness === k)).map(k => [k, OPEN_LABEL[k]]);
  const openCounts = count(g => g.openness);

  function chip(type, value, label, n, active, cls) {
    return `<button class="filter-chip${cls ? ' ' + cls : ''}${active ? ' active' : ''}" data-type="${esc(type)}" data-value="${esc(value)}" aria-pressed="${active ? 'true' : 'false'}">${esc(label)}${n != null ? `<small>${fmt(n)}</small>` : ''}</button>`;
  }
  function buildChips() {
    if (groups.quick) groups.quick.innerHTML = chip('quick', 'beginner', 'Beginner-friendly (free files)', nBeginner, state.beginner, 'quick');
    if (quickNote) quickNote.hidden = !state.beginner;
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
      if (state.beginner && !BEGINNER(g)) return false;
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
  const STATUS_LABEL = { 'full-pack': 'Full design pack', 'source-files': 'Files at the maker’s site', 'metadata-only': 'Specs only' };
  const KIND_LABEL = {
    schematic: 'Schematic', pcb: 'PCB layout', gerber: 'Gerber', bom: 'BOM', spec: 'Spec sheet', firmware: 'Firmware', bsp: 'BSP',
    enclosure: '3D enclosure', mech: 'Mechanical', photos: 'Photos', block_diagram: 'Block diagram', pcb_lib: 'Libraries', sch_lib: 'Libraries',
    artwork: 'Artwork', presentation: 'Slides', datasheets: 'Datasheets'
  };
  const kindList = g => g.kinds.map(k => KIND_LABEL[k] || k).filter((v, i, a) => a.indexOf(v) === i);

  function renderCard(g) {
    const id = g.project_no || g.issuer || '';
    const tag = [g.category, g.chip || g.hint].filter(Boolean).join(' · ');
    const kl = kindList(g);
    const desc = g.application || (g.chip ? `${g.chip_brand || ''} ${g.chip}`.trim() : '') || (kl.length ? 'Files published: ' + kl.join(', ') : '');
    const kinds = kl.length ? (kl.length > 3 ? kl.slice(0, 3).join(' · ') + ` +${kl.length - 3}` : kl.join(' · ')) : '';
    const right = g.price != null
      ? `CHIP <strong>$${g.price.toFixed(2)}</strong> / 5k`
      : [kinds, OPEN_LABEL[g.openness] || g.openness_label, g.year].filter(Boolean).join(' · ');
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
    const dirty = state.cat !== 'all' || state.issuer !== 'all' || state.files || state.open || state.q || state.beginner;
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
  Object.values(groups).filter(Boolean).forEach(el => el.addEventListener('click', e => {
    const b = e.target.closest('.filter-chip');
    if (!b) return;
    const t = b.dataset.type, v = b.dataset.value;
    if (t === 'cat') state.cat = v;
    else if (t === 'issuer') state.issuer = v;
    else if (t === 'files') state.files = state.files === v ? null : v;
    else if (t === 'open') state.open = state.open === v ? null : v;
    else if (t === 'quick') state.beginner = !state.beginner;
    buildChips();
    render();
  }));

  resetBtn.addEventListener('click', () => {
    Object.assign(state, { cat: 'all', issuer: 'all', files: null, open: null, q: '', beginner: false });
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
    Object.assign(state, { cat: h.get('cat') || 'all', issuer: h.get('issuer') || 'all', files: h.get('files') || null, open: h.get('open') || null, q: h.get('q') || '', beginner: flag(h, 'beginner') });
    searchInput.value = state.q;
    buildChips();
    render();
  });

  searchInput.value = state.q;
  buildChips();
  render();
})();
