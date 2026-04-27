/* ==========================================================
   GONGBANS DB — catalog / filter / search
   Vanilla JS, no framework. Loads gongbans.json, renders grid,
   wires up filter chips and search.
   ========================================================== */

(async function () {
  const grid = document.getElementById('gongban-grid');
  const searchInput = document.getElementById('search-input');
  const entryCount = document.getElementById('entry-count');
  const chips = document.querySelectorAll('.filter-chip');

  let data = null;
  const state = {
    category: 'all',
    files: null,        // null | 'has-files' | 'metadata-only'
    query: ''
  };

  // Load manifest
  try {
    const res = await fetch('data/gongbans.json');
    data = await res.json();
  } catch (e) {
    grid.innerHTML = `<div class="empty-state">⚠ Couldn't load catalog. If running locally, serve via <code>python3 -m http.server</code>.</div>`;
    console.error(e);
    return;
  }

  // Filter logic
  function filter(gongbans) {
    return gongbans.filter(g => {
      if (state.category !== 'all' && g.category !== state.category) return false;
      if (state.files === 'has-files' && !g.files_available) return false;
      if (state.files === 'metadata-only' && g.files_available) return false;
      if (state.query) {
        const q = state.query.toLowerCase();
        const haystack = [
          g.name, g.chip, g.chip_brand, g.chip_role, g.application,
          g.category, g.project_no, (g.tags || []).join(' '),
          g.mcu_chip, g.mcu_brand
        ].filter(Boolean).join(' ').toLowerCase();
        if (!haystack.includes(q)) return false;
      }
      return true;
    });
  }

  // Render a single card
  function renderCard(g) {
    const status = g.files_available
      ? `<span class="card-status has-files">Full Design Pack</span>`
      : `<span class="card-status metadata-only">Catalog Entry</span>`;

    const price = g.chip_price_5k_usd
      ? `<span class="card-price">CHIP <strong>$${g.chip_price_5k_usd.toFixed(2)}</strong> / 5k</span>`
      : `<span class="card-price">—</span>`;

    return `
      <a class="gongban-card" href="db/${g.slug}.html">
        <div class="card-header">
          <span class="card-projno">${g.project_no}</span>
          <span class="card-category">${g.category}</span>
        </div>
        <h2 class="card-title">${g.name}</h2>
        <div class="card-chip">
          <div class="chip-brand">${g.chip_brand}</div>
          <div class="chip-name">${g.chip}</div>
          <div class="chip-role">${g.chip_role || ''}</div>
        </div>
        <p class="card-app">${g.application}</p>
        <div class="card-footer">
          ${price}
          ${status}
        </div>
      </a>
    `;
  }

  function render() {
    const filtered = filter(data.gongbans);
    if (filtered.length === 0) {
      grid.innerHTML = `<div class="empty-state">No gongbans match these filters. Try clearing the search or category.</div>`;
    } else {
      grid.innerHTML = filtered.map(renderCard).join('');
    }
    entryCount.textContent = `${filtered.length} OF ${data.gongbans.length} ENTRIES`;
  }

  // Wire up chips
  chips.forEach(chip => {
    chip.addEventListener('click', () => {
      const filterType = chip.dataset.filter;
      const value = chip.dataset.value;

      if (filterType === 'category') {
        state.category = value;
        document.querySelectorAll('[data-filter="category"]').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
      } else if (filterType === 'files') {
        // toggle
        if (state.files === value) {
          state.files = null;
          chip.classList.remove('active');
        } else {
          state.files = value;
          document.querySelectorAll('[data-filter="files"]').forEach(c => c.classList.remove('active'));
          chip.classList.add('active');
        }
      }
      render();
    });
  });

  // Wire up search (debounced)
  let searchTimer = null;
  searchInput.addEventListener('input', e => {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => {
      state.query = e.target.value.trim();
      render();
    }, 120);
  });

  // Initial render
  render();
})();
