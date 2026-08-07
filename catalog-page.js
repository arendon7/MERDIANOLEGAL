(() => {
  const menu = document.querySelector('.detail-menu');
  const nav = document.querySelector('.detail-nav');
  const body = document.body;
  const closeMenu = ({ restoreFocus = false } = {}) => {
    if (!menu || !nav) return;
    menu.setAttribute('aria-expanded', 'false');
    menu.setAttribute('aria-label', 'Abrir menú');
    nav.classList.remove('open');
    body.classList.remove('detail-menu-open');
    if (restoreFocus) menu.focus();
  };
  menu?.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open));
    menu.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    nav?.classList.toggle('open', open);
    body.classList.toggle('detail-menu-open', open);
  });
  nav?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => closeMenu()));
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && nav?.classList.contains('open')) closeMenu({ restoreFocus: true });
  });
  document.querySelector('[data-top]')?.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  const year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());

  const id = body.dataset.catalogId || '';
  const productSources = {
    'product-diagnostic': '../catalog-products-v41/p01-auditoria.json',
    'product-organized': '../catalog-products-v41/p02-organizada.json',
    'product-assets': '../catalog-products-v41/p03-intangibles.json',
    'product-investment': '../catalog-products-v41/p04-inversion.json',
    'product-ai': '../catalog-products-v41/p05-ia.json',
    'product-regulated': '../catalog-products-v41/p06-regulado.json',
    'product-contract-system': '../catalog-products-v41/p07-contractual.json',
    'product-data-consumer': '../catalog-products-v41/p08-datos-consumidor.json',
  };
  if (!productSources[id]) return;

  const esc = (value = '') => String(value).replace(/[&<>"']/g, (char) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[char]));
  const cards = (items, className, prefix) => `<div class="${className}-grid">${(items || []).map(([title, description], index) => `<article class="${className}-card"><span>${String(index + 1).padStart(2, '0')} · ${prefix}</span><h3>${esc(title)}</h3><p>${esc(description)}</p></article>`).join('')}</div>`;
  const section = ({ id: sid, eyebrow, title, description = '', className = '', body: content }) => `<section class="detail-section${className ? ` ${className}` : ''}" aria-labelledby="${sid}-title"><div class="container"><div class="detail-heading"><p class="eyebrow">${esc(eyebrow)}</p><h2 id="${sid}-title">${esc(title)}</h2>${description ? `<p>${esc(description)}</p>` : ''}</div>${content}</div></section>`;
  const list = (items, className = 'limits-list') => `<ul class="${className}">${(items || []).map((item) => `<li>${esc(Array.isArray(item) ? `${item[0]} — ${item[1]}` : item)}</li>`).join('')}</ul>`;

  const render = (entry) => {
    document.title = `${entry.title} | Meridiano Legal`;
    body.dataset.pageTitle = entry.title;
    const journey = document.querySelector('.journey-bar strong');
    if (journey) journey.textContent = entry.title;
    const current = document.querySelector('.detail-breadcrumb [aria-current="page"]');
    if (current) current.textContent = entry.title;
    const hero = document.getElementById('detail-hero-content');
    if (hero) hero.innerHTML = `<div><p class="detail-eyebrow">PRODUCTO JURÍDICO · ${esc(entry.code)}</p><h1>${esc(entry.title)}</h1><p class="summary">${esc(entry.summary)}</p><div class="detail-cta-row"><a class="btn btn-gold" href="#contacto">Evaluar esta solución →</a><a class="btn btn-outline-light" href="../index.html#productos">Volver al portafolio</a></div></div><div class="detail-meta" aria-label="Resumen de la solución"><article><span>Tipo</span><strong>${esc(entry.type)}</strong></article><article><span>Horizonte</span><strong>${esc(entry.duration)}</strong></article><article><span>Modalidad</span><strong>${esc(entry.modality)}</strong></article><article><span>Dirigido a</span><strong>${esc(entry.audience)}</strong></article></div>`;

    const method = `<ol class="method-list">${(entry.method || []).map(([title, description], index) => `<li><b>${String(index + 1).padStart(2, '0')}</b><strong>${esc(title)}</strong><span>${esc(description)}</span></li>`).join('')}</ol>`;
    const responsibilities = cards(entry.responsibilities, 'requirement', 'RESPONSABLE');
    const supplements = cards(entry.supplements, 'scope', 'SUPLEMENTO');
    const related = `<div class="related-grid">${(entry.related || []).map(([label, title, description, url]) => `<article class="related-card"><span>${esc(label)}</span><strong>${esc(title)}</strong><p>${esc(description)}</p><a href="${esc(url)}">Explorar →</a></article>`).join('')}</div>`;
    const whatsapp = encodeURIComponent(`Hola, revisé ${entry.title} en Meridiano Legal y quiero evaluar esta solución.`);
    const main = document.getElementById('detail-page');
    if (!main) return;
    main.innerHTML = [
      section({ id: 'pregunta', eyebrow: 'PREGUNTA EJECUTIVA', title: 'La pregunta que debe poder responder la dirección.', body: `<div class="executive-question"><span>PREGUNTA CENTRAL</span><p>${esc(entry.question)}</p></div>` }),
      section({ id: 'resultado', eyebrow: 'RESULTADO EMPRESARIAL', title: 'Qué cambia cuando termina el producto.', className: 'ivory', body: `<div class="result-panel"><p>${esc(entry.result)}</p></div>` }),
      section({ id: 'situaciones', eyebrow: 'CUÁNDO TIENE SENTIDO', title: 'Situaciones que justifican intervenir.', className: 'soft', body: cards(entry.situations, 'situation', 'SITUACIÓN') }),
      section({ id: 'alcance', eyebrow: 'ALCANCE JURÍDICO', title: 'Qué frentes comprende.', body: cards(entry.scope, 'scope', 'FRENTE') }),
      section({ id: 'perimetro', eyebrow: 'PERÍMETRO ESTÁNDAR', title: 'Qué cantidad de trabajo está incluida.', className: 'ivory', body: cards(entry.perimeter, 'deliverable', 'UNIDAD') }),
      section({ id: 'metodo', eyebrow: 'MÉTODO DE TRABAJO', title: 'Cómo se ejecuta.', body: method }),
      section({ id: 'entregables', eyebrow: 'ENTREGABLES EXACTOS', title: 'Qué recibe la empresa.', className: 'soft', body: cards(entry.deliverables, 'deliverable', 'ENTREGABLE') }),
      section({ id: 'formatos', eyebrow: 'FORMATOS Y PLATAFORMA', title: 'Cómo se entrega y administra la evidencia.', body: cards(entry.formats, 'scope', 'FORMATO') }),
      section({ id: 'cronograma', eyebrow: 'CRONOGRAMA', title: `Horizonte estimado: ${entry.duration}.`, className: 'ivory', body: cards(entry.timeline, 'situation', 'ETAPA') }),
      section({ id: 'requisitos', eyebrow: 'INFORMACIÓN Y PARTICIPACIÓN', title: 'Qué necesita aportar la empresa.', body: cards(entry.requirements, 'requirement', 'REQUISITO') }),
      section({ id: 'responsabilidades', eyebrow: 'RESPONSABILIDADES', title: 'Quién debe hacer qué.', className: 'soft', body: responsibilities }),
      section({ id: 'aceptacion', eyebrow: 'CRITERIOS DE ACEPTACIÓN', title: 'Cómo se verifica que el producto está cerrado.', body: cards(entry.acceptance, 'deliverable', 'CRITERIO') }),
      `<section class="detail-section" aria-labelledby="limites-title"><div class="container limits-layout"><div class="limits-intro"><p class="detail-eyebrow">LÍMITES Y EXCLUSIONES</p><h2 id="limites-title">Qué no está incluido en el alcance estándar.</h2><p>Las exclusiones evitan falsas expectativas y permiten cotizar separadamente lo que requiera otra especialidad, volumen o actuación.</p></div>${list(entry.limits)}</div></section>`,
      section({ id: 'relacionadas', eyebrow: 'AMPLIACIONES Y SOLUCIONES RELACIONADAS', title: 'Cómo puede ampliarse sin desdibujar el producto.', className: 'ivory', body: `<div class="detail-subgroup"><h3>Suplementos disponibles</h3>${supplements}</div><div class="detail-subgroup"><h3>Soluciones relacionadas</h3>${related}</div>` }),
      `<section class="detail-section detail-contact" id="contacto" aria-labelledby="contacto-title"><div class="container detail-contact-grid"><div><p class="detail-eyebrow">SIGUIENTE PASO</p><h2 id="contacto-title">Definamos si este producto resuelve la necesidad concreta de su empresa.</h2><p>La primera conversación sirve para confirmar perímetro, urgencia, información disponible y eventuales especialidades adicionales. No envíe todavía documentos confidenciales.</p></div><div class="detail-contact-panel"><strong>${esc(entry.title)}</strong><span>${esc(entry.type)} · ${esc(entry.duration)}</span><div class="detail-cta-row"><a class="btn btn-gold" href="https://wa.me/573008507813?text=${whatsapp}" target="_blank" rel="noopener noreferrer">Conversar por WhatsApp →</a><a class="btn btn-outline-light" href="../index.html#contacto">Formulario general</a></div></div></div></section>`,
    ].join('');
  };

  fetch(productSources[id], { cache: 'no-cache' })
    .then((response) => { if (!response.ok) throw new Error(`HTTP ${response.status}`); return response.json(); })
    .then((data) => render(data[id]))
    .catch(() => { /* El HTML estático anterior permanece utilizable como fallback. */ });
})();
