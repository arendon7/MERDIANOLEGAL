#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const SOURCE_PATH = path.join(ROOT, 'catalog-v32.js');
const VERSION = JSON.parse(fs.readFileSync(path.join(ROOT, 'version.json'), 'utf8'));
const RELEASE_YEAR = String(VERSION.release_date || '').slice(0, 4) || String(new Date().getFullYear());
const START = '  const entries = ';
const END = '\n\n  const create = ';
const WHATSAPP = '573008507813';

const escapeHtml = (value = '') => String(value)
  .replaceAll('&', '&amp;')
  .replaceAll('<', '&lt;')
  .replaceAll('>', '&gt;')
  .replaceAll('"', '&quot;')
  .replaceAll("'", '&#39;');

const source = fs.readFileSync(SOURCE_PATH, 'utf8');
const start = source.indexOf(START);
const end = source.indexOf(END, start + START.length);
if (start < 0 || end < 0) throw new Error('No fue posible localizar el catálogo central.');
const literal = source.slice(start + START.length, end).trim().replace(/;$/, '');
const entries = vm.runInNewContext(`(${literal})`, Object.create(null), { timeout: 1000 });
const PRODUCT_V41_DIR = path.join(ROOT, 'catalog-products-v41');
if (fs.existsSync(PRODUCT_V41_DIR)) {
  for (const name of fs.readdirSync(PRODUCT_V41_DIR).filter((item) => item.endsWith('.json')).sort()) {
    const overrides = JSON.parse(fs.readFileSync(path.join(PRODUCT_V41_DIR, name), 'utf8'));
    for (const [catalogId, override] of Object.entries(overrides)) {
      if (!entries[catalogId]) throw new Error(`Producto v4.1 desconocido: ${catalogId}`);
      entries[catalogId] = { ...entries[catalogId], ...override, productV41: true };
    }
  }
}

const cards = (items, className, prefix) => `<div class="${className}-grid">${items.map(([title, description], index) => `
  <article class="${className}-card">
    <span>${String(index + 1).padStart(2, '0')} · ${prefix}</span>
    <h3>${escapeHtml(title)}</h3>
    <p>${escapeHtml(description)}</p>
  </article>`).join('')}
</div>`;

const section = ({ id, eyebrow, title, description = '', className = '', body }) => `<section class="detail-section${className ? ` ${className}` : ''}" aria-labelledby="${id}-title">
  <div class="container">
    <div class="detail-heading">
      <p class="eyebrow">${escapeHtml(eyebrow)}</p>
      <h2 id="${id}-title">${escapeHtml(title)}</h2>${description ? `
      <p>${escapeHtml(description)}</p>` : ''}
    </div>
    ${body}
  </div>
</section>`;

const heroInner = (entry) => `<div>
  <p class="detail-eyebrow">${escapeHtml(entry.type.toUpperCase())} · ${escapeHtml(entry.code)}</p>
  <h1>${escapeHtml(entry.title)}</h1>
  <p class="summary">${escapeHtml(entry.summary)}</p>
  <div class="detail-cta-row">
    <a class="btn btn-gold" href="#contacto">Presentar esta necesidad →</a>
    <a class="btn btn-outline-light" href="${entry.type === 'Servicio profesional' ? '../index.html#servicios' : '../index.html#productos'}">Volver al portafolio</a>
  </div>
</div>
<div class="detail-meta" aria-label="Resumen de la solución">
${[['Tipo', entry.type], ['Horizonte', entry.duration], ['Modalidad', entry.modality], ['Dirigido a', entry.audience]].map(([label, value]) => `  <article><span>${escapeHtml(label)}</span><strong>${escapeHtml(value)}</strong></article>`).join('\n')}
</div>`;

const methodList = (entry) => `<ol class="method-list">${entry.method.map(([title, description], index) => `
    <li><b>${String(index + 1).padStart(2, '0')}</b><strong>${escapeHtml(title)}</strong><span>${escapeHtml(description)}</span></li>`).join('')}
  </ol>`;

const limitsBlock = (entry) => `<div class="container limits-layout">
    <div class="limits-intro"><p class="detail-eyebrow">LÍMITES Y EXCLUSIONES</p><h2 id="limites-title">Claridad sobre lo que esta solución no promete.</h2><p>El rigor también exige separar decisiones propias, especialidades externas y resultados que dependen de autoridades, contrapartes o terceros.</p></div>
    <ul class="limits-list">${entry.limits.map((item) => `<li>${escapeHtml(item)}</li>`).join('')}</ul>
  </div>`;

const relatedGrid = (entry) => `<div class="related-grid">${entry.related.map(([label, title, description, url]) => `
    <article class="related-card"><span>${escapeHtml(label)}</span><strong>${escapeHtml(title)}</strong><p>${escapeHtml(description)}</p><a href="${escapeHtml(url)}">Explorar →</a></article>`).join('')}
  </div>`;

const contactBlock = (entry) => {
  const whatsappText = encodeURIComponent(`Hola, revisé la ficha de ${entry.title} en Meridiano Legal y quiero presentar una necesidad relacionada.`);
  return `<section class="detail-section detail-contact" id="contacto" aria-labelledby="contacto-title">
    <div class="container detail-contact-grid">
      <div><p class="detail-eyebrow">SIGUIENTE PASO</p><h2 id="contacto-title">Definamos si esta es la solución adecuada para su necesidad.</h2><p>La primera conversación permite comprender la decisión, la urgencia, los actores, la evidencia y el resultado esperado. No envíe todavía información confidencial ni documentos sensibles.</p></div>
      <div class="detail-contact-panel"><strong>${escapeHtml(entry.title)}</strong><span>${escapeHtml(entry.type)} · ${escapeHtml(entry.duration)}</span><div class="detail-cta-row"><a class="btn btn-gold" href="https://wa.me/${WHATSAPP}?text=${whatsappText}" target="_blank" rel="noopener noreferrer">Conversar por WhatsApp →</a><a class="btn btn-outline-light" href="../index.html#contacto">Formulario general</a></div></div>
    </div>
  </section>`;
};

const bodyInnerService = (entry) => [
  section({ id: 'pregunta', eyebrow: 'PREGUNTA EJECUTIVA', title: 'La decisión que organiza el alcance.', body: `<div class="executive-question"><span>PREGUNTA CENTRAL</span><p>${escapeHtml(entry.question)}</p></div>` }),
  section({ id: 'situaciones', eyebrow: 'CUÁNDO PUEDE SER ÚTIL', title: 'Situaciones que justifican evaluar esta solución.', description: 'La calificación definitiva depende de hechos, documentos, actores, urgencia y especialidades aplicables.', className: 'soft', body: cards(entry.situations, 'situation', 'SITUACIÓN') }),
  section({ id: 'alcance', eyebrow: 'ALCANCE ORIENTATIVO', title: 'Qué frentes puede comprender.', description: 'La propuesta final define expresamente el perímetro, la profundidad, las revisiones y las exclusiones.', body: cards(entry.scope, 'scope', 'FRENTE') }),
  section({ id: 'metodo', eyebrow: 'MÉTODO DE TRABAJO', title: 'Una secuencia que evita documentos prematuros.', description: 'El orden puede adaptarse al asunto, pero siempre debe conservar comprensión, calificación, estructuración, implementación y cierre.', className: 'ivory', body: methodList(entry) }),
  section({ id: 'entregables', eyebrow: 'ENTREGABLES', title: 'Qué puede recibir la empresa.', description: 'Los formatos se ajustan al alcance y deben indicar supuestos, fuentes, responsables, límites y condiciones de actualización.', body: cards(entry.deliverables, 'deliverable', 'SALIDA') }),
  section({ id: 'requisitos', eyebrow: 'INFORMACIÓN Y PARTICIPACIÓN', title: 'Qué se requiere para trabajar con rigor.', description: 'La falta de información o de responsables puede modificar cronograma, profundidad y conclusiones.', className: 'soft', body: cards(entry.requirements, 'requirement', 'REQUISITO') }),
  `<section class="detail-section" aria-labelledby="limites-title">${limitsBlock(entry)}</section>`,
  section({ id: 'relacionadas', eyebrow: 'SOLUCIONES RELACIONADAS', title: 'Cómo puede conectarse con el resto del portafolio.', className: 'ivory', body: relatedGrid(entry) }),
  contactBlock(entry),
].join('\n');

const bodyInnerProduct = (entry) => {
  const supplementAndRelated = `<div class="detail-subgroup"><h3>Unidades adicionales disponibles</h3>${cards(entry.supplements || [], 'scope', 'SUPLEMENTO')}</div>
  <div class="detail-subgroup"><h3>Soluciones relacionadas</h3>${relatedGrid(entry)}</div>`;
  return [
    section({ id: 'pregunta', eyebrow: 'PREGUNTA EJECUTIVA', title: 'La decisión que organiza el producto.', body: `<div class="executive-question"><span>PREGUNTA CENTRAL</span><p>${escapeHtml(entry.question)}</p></div>` }),
    section({ id: 'resultado', eyebrow: 'RESULTADO EMPRESARIAL', title: 'Qué cambia al terminar el trabajo.', className: 'ivory', body: `<div class="result-panel"><p>${escapeHtml(entry.result)}</p></div>` }),
    section({ id: 'situaciones', eyebrow: 'CUÁNDO PUEDE SER ÚTIL', title: 'Situaciones en las que este producto suele resolver una necesidad concreta.', description: 'La calificación definitiva depende de hechos, documentos, actores y especialidades aplicables.', className: 'soft', body: cards(entry.situations, 'situation', 'SITUACIÓN') }),
    section({ id: 'alcance', eyebrow: 'ARQUITECTURA JURÍDICA', title: 'Frentes que comprende el producto.', description: 'La contratación debe identificar expresamente qué está incluido y qué requeriría una ampliación.', body: cards(entry.scope, 'scope', 'FRENTE') }),
    section({ id: 'perimetro', eyebrow: 'PERÍMETRO ESTÁNDAR INCLUIDO', title: 'Cantidades y unidades para saber exactamente qué se está contratando.', description: 'Los volúmenes son máximos del paquete estándar y permiten comparar el alcance antes de iniciar.', className: 'ivory', body: cards(entry.perimeter, 'scope', 'INCLUIDO') }),
    section({ id: 'metodo', eyebrow: 'MÉTODO DE TRABAJO', title: 'Una secuencia de trabajo con hitos verificables.', description: 'El método se adapta al asunto sin perder trazabilidad entre información, análisis, documento, decisión e implementación.', body: methodList(entry) }),
    section({ id: 'entregables', eyebrow: 'ENTREGABLES EXACTOS', title: 'Qué recibe la empresa al cierre.', description: 'Cada salida indica cantidad, formato o función para evitar expectativas abiertas o documentos genéricos.', className: 'soft', body: cards(entry.deliverables, 'deliverable', 'ENTREGABLE') }),
    section({ id: 'formatos', eyebrow: 'FORMATOS, PLATAFORMA Y TRAZABILIDAD', title: 'Dónde se entrega y cómo queda administrable.', description: 'La plataforma definitiva depende de la habilitación productiva y del entorno tecnológico del cliente.', body: cards(entry.formats, 'scope', 'FORMATO') }),
    section({ id: 'cronograma', eyebrow: 'CRONOGRAMA ORIENTATIVO', title: `Cómo se distribuyen las ${escapeHtml(entry.duration)}.`, description: 'Los plazos presuponen entrega oportuna de información y decisiones del cliente.', className: 'ivory', body: cards(entry.timeline, 'scope', 'HITO') }),
    section({ id: 'requisitos', eyebrow: 'INFORMACIÓN Y PARTICIPACIÓN', title: 'Qué debe estar disponible para trabajar con rigor.', description: 'Los vacíos de información se documentan y pueden afectar alcance, plazo o conclusión.', body: cards(entry.requirements, 'requirement', 'REQUISITO') }),
    section({ id: 'responsabilidades', eyebrow: 'RESPONSABILIDADES', title: 'Quién hace qué durante el producto.', description: 'La delimitación evita trasladar al asesor decisiones de negocio, tareas técnicas o actuaciones de terceros.', className: 'soft', body: cards(entry.responsibilities, 'scope', 'RESPONSABLE') }),
    section({ id: 'aceptacion', eyebrow: 'CRITERIOS DE ACEPTACIÓN', title: 'Cuándo se entiende cerrado el producto.', description: 'El cierre se verifica contra entregables y criterios objetivos, no contra resultados que dependan de terceros.', body: cards(entry.acceptance, 'scope', 'CRITERIO') }),
    `<section class="detail-section" aria-labelledby="limites-title">${limitsBlock(entry)}</section>`,
    section({ id: 'relacionadas', eyebrow: 'SUPLEMENTOS Y CONTINUIDAD', title: 'Qué puede ampliarse y cómo continúa la relación.', description: 'Los suplementos permiten aumentar el perímetro sin desdibujar el producto base.', className: 'ivory', body: supplementAndRelated }),
    contactBlock(entry),
  ].join('\n');
};

const bodyInner = (entry) => entry.productV41 ? bodyInnerProduct(entry) : bodyInnerService(entry);

const ensureBlocks = (html) => {
  if (!html.includes('STATIC-CATALOG-HERO:START')) {
    html = html.replace('<div class="container detail-hero-grid" id="detail-hero-content"></div>', '<!-- STATIC-CATALOG-HERO:START -->\n<div class="container detail-hero-grid" id="detail-hero-content" data-static-catalog="true"></div>\n<!-- STATIC-CATALOG-HERO:END -->');
  }
  if (!html.includes('STATIC-CATALOG-BODY:START')) {
    html = html.replace('<main id="contenido"><div id="detail-page"></div></main>', '<!-- STATIC-CATALOG-BODY:START -->\n<main id="contenido"><div id="detail-page" data-static-catalog="true"></div></main>\n<!-- STATIC-CATALOG-BODY:END -->');
  }
  return html;
};

const replaceBlock = (html, name, content) => {
  const pattern = new RegExp(`<!-- ${name}:START -->[\\s\\S]*?<!-- ${name}:END -->`);
  if (!pattern.test(html)) throw new Error(`Falta el bloque ${name}.`);
  return html.replace(pattern, `<!-- ${name}:START -->\n${content}\n<!-- ${name}:END -->`);
};

const enhanceHeadAndScripts = (html, entry) => {
  if (!html.includes('property="og:site_name"')) html = html.replace('<meta property="og:type" content="website">', '<meta property="og:type" content="website">\n  <meta property="og:site_name" content="Meridiano Legal">');
  if (!html.includes('name="twitter:title"')) html = html.replace('<meta name="twitter:card" content="summary_large_image">', `<meta name="twitter:card" content="summary_large_image">\n  <meta name="twitter:title" content="${escapeHtml(entry.title)} | Meridiano Legal">\n  <meta name="twitter:description" content="${escapeHtml(entry.summary)}">\n  <meta name="twitter:image" content="../assets/hero-meridiano-v3.svg">`);
  html = html
    .replace(/<title>[\s\S]*?<\/title>/, `<title>${escapeHtml(entry.title)} | Meridiano Legal</title>`)
    .replace(/(<meta name="description" content=")[^"]*(">)/, `$1${escapeHtml(entry.summary)}$2`)
    .replace(/(<meta property="og:title" content=")[^"]*(">)/, `$1${escapeHtml(entry.title)} | Meridiano Legal$2`)
    .replace(/(<meta property="og:description" content=")[^"]*(">)/, `$1${escapeHtml(entry.summary)}$2`)
    .replace(/(<meta name="twitter:title" content=")[^"]*(">)/, `$1${escapeHtml(entry.title)} | Meridiano Legal$2`)
    .replace(/(<meta name="twitter:description" content=")[^"]*(">)/, `$1${escapeHtml(entry.summary)}$2`)
    .replace('<span id="year"></span>', `<span id="year">${RELEASE_YEAR}</span>`)
    .replace(/Ficha v\d+(?:\.\d+){1,2}/, `Ficha v${VERSION.version}`)
    .replace('<script src="../catalog-v32.js"></script>', '<script defer src="../catalog-page.js"></script>')
    .replace('<script src="../page-context.js"></script>', '<script defer src="../page-context.js"></script>');
  return html;
};

const catalogFiles = [
  ...fs.readdirSync(path.join(ROOT, 'servicios')).filter((name) => name.endsWith('.html')).map((name) => `servicios/${name}`),
  ...fs.readdirSync(path.join(ROOT, 'productos')).filter((name) => name.endsWith('.html')).map((name) => `productos/${name}`),
];

let updated = 0;
for (const [catalogId, entry] of Object.entries(entries)) {
  if (!entry.productV41) continue;
  const pagePath = catalogFiles.find((relative) => fs.readFileSync(path.join(ROOT, relative), 'utf8').includes(`data-catalog-id="${catalogId}"`));
  if (!pagePath) throw new Error(`No existe una ficha para ${catalogId}.`);
  const absolute = path.join(ROOT, pagePath);
  let html = ensureBlocks(fs.readFileSync(absolute, 'utf8'));
  html = replaceBlock(html, 'STATIC-CATALOG-HERO', `<div class="container detail-hero-grid" id="detail-hero-content" data-static-catalog="true">\n${heroInner(entry)}\n</div>`);
  html = replaceBlock(html, 'STATIC-CATALOG-BODY', `<main id="contenido"><div id="detail-page" data-static-catalog="true">\n${bodyInner(entry)}\n</div></main>`);
  html = enhanceHeadAndScripts(html, entry);
  fs.writeFileSync(absolute, html, 'utf8');
  updated += 1;
}
console.log(`Contenido estático v4.1 generado en ${updated} fichas de producto; servicios preservados.`);
