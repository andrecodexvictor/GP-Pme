(() => {
  const form = document.getElementById('search-form'); if (!form) return;
  const input = document.getElementById('query'), filter = document.getElementById('kind');
  const status = document.getElementById('search-status'), list = document.getElementById('search-results');
  const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const tokens = value => normalize(value).match(/[a-z0-9]+/g) || [];
  const index = window.GEAR_INDEX || window.GPPME_INDEX;
  if (!index || !Array.isArray(index.docs)) {
    status.textContent = 'O índice local não foi carregado. Reabra a página ou navegue pela documentação.';
    form.querySelector('button').disabled = true; return;
  }
  const text = (tag, value, cls) => { const el = document.createElement(tag); el.textContent = value; if (cls) el.className = cls; return el; };
  function search() {
    const terms = [...new Set(tokens(input.value))]; list.replaceChildren();
    if (!terms.length) { status.textContent = 'Digite uma palavra para começar.'; return; }
    status.textContent = 'Consultando o índice local…';
    const results = index.docs.filter(doc => !filter.value || doc.tipo === filter.value).map(doc => {
      const title = tokens(`${doc.titulo_doc} ${doc.secao}`), body = tokens(doc.texto), kw = tokens((doc.keywords || []).join(' '));
      const score = terms.reduce((sum, term) => sum + (title.includes(term) ? 5 : 0) + (body.includes(term) ? 1 : 0) + (kw.includes(term) ? 2 : 0), 0);
      return { doc, score };
    }).filter(result => result.score > 0).sort((a, b) => b.score - a.score || a.doc.id.localeCompare(b.doc.id)).slice(0, 30);
    results.forEach(({ doc }) => {
      const item = document.createElement('li'), heading = document.createElement('h2'), a = document.createElement('a');
      a.href = doc.href; a.textContent = `${doc.titulo_doc} — ${doc.secao}`; heading.append(a); item.append(heading);
      const clean = doc.texto.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1').replace(/[`*#|]/g, '');
      const normalized = normalize(clean), at = Math.max(0, Math.min(...terms.map(term => normalized.indexOf(term)).filter(i => i >= 0)) - 70);
      const start = Number.isFinite(at) ? at : 0;
      item.append(text('p', (start ? '…' : '') + clean.slice(start, start + 280) + (clean.length > start + 280 ? '…' : '')));
      item.append(text('p', `${doc.breadcrumb} · ${doc.tipo}`, 'origin')); list.append(item);
    });
    status.textContent = results.length ? `${results.length} trechos encontrados${results.length === 30 ? ' (até 30 exibidos)' : ''}. Busca lexical no conteúdo revisado.` : 'Nenhum trecho encontrado. Tente outro termo ou remova o filtro.';
  }
  form.addEventListener('submit', event => { event.preventDefault(); search(); });
  filter.addEventListener('change', search);
  const query = new URLSearchParams(location.search).get('q'); if (query) { input.value = query; search(); }
})();
