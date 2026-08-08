#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const VERSION = JSON.parse(fs.readFileSync(path.join(ROOT, 'version.json'), 'utf8'));
const RELEASE_YEAR = String(VERSION.release_date || '').slice(0, 4) || String(new Date().getFullYear());
const SERVICE_V42_DIR = path.join(ROOT, 'catalog-services-v42');
const WHATSAPP = '573008507813';

if (!fs.existsSync(SERVICE_V42_DIR)) throw new Error('Falta catalog-services-v42/.');
const entries = {};
for (const name of fs.readdirSync(SERVICE_V42_DIR).filter((item) => item.endsWith('.json')).sort()) {
  const overrides = JSON.parse(fs.readFileSync(path.join(SERVICE_V42_DIR, name), 'utf8'));
  for (const [catalogId, entry] of Object.entries(overrides)) {
    if (entries[catalogId]) throw new Error(`Servicio v4.2 duplicado: ${catalogId}`);
    entries[catalogId] = entry;
  }
}

const escapeHtml = (value = '') => String(value)
  .replaceAll('&', '&amp;')
  .replaceAll('<', '&lt;')
  .replaceAll('>', '&gt;')
  .replaceAll('"', '&quot;')
  .replaceAll("'", '&#39;');

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
    <a class="btn btn-outline-light" href="../index.html#servicios">Volver al portafolio</a>
  </div>
</div>
<div class="detail-meta" aria-label="Resumen del servicio">
${[['Tipo', entry.type], ['Horizonte', entry.duration], ['Modalidad', entry.modality], ['Dirigido a', entry.audience]].map(([label, value]) => `  <article><span>${escapeHtml(label)}</span><strong>${escapeHtml(value)}</strong></article>`).join('\n')}
</div>`;

const methodList = (entry) => `<ol class="method-list">${entry.method.map(([title, description], index) => `
    <li><b>${String(index + 1).padStart(2, '0')}</b><strong>${escapeHtml(title)}</strong><span>${escapeHtml(description)}</span></li>`).join('')}
  </ol>`;

const limitsBlock = (entry) => `<div class="container limits-layout">
    <div class="limits-intro"><p class="detail-eyebrow">LÍMITES Y EXCLUSIONES</p><h2 id="limites-title">Claridad sobre lo que el servicio no incluye ni puede garantizar.</h2><p>La propuesta separa la intervención jurídica de decisiones empresariales, especialidades externas y resultados que dependen de autoridades, contrapartes o terceros.</p></div>
    <ul class="limits-list">${entry.limits.map((item) => `<li>${escapeHtml(item)}</li>`).join('')}</ul>
  </div>`;

const relatedGrid = (entry) => `<div class="related-grid">${entry.related.map(([label, title, description, url]) => `
    <article class="related-card"><span>${escapeHtml(label)}</span><strong>${escapeHtml(title)}</strong><p>${escapeHtml(description)}</p><a href="${escapeHtml(url)}">Explorar →</a></article>`).join('')}
  </div>`;

const contactBlock = (entry) => {
  const whatsappText = encodeURIComponent(`Hola, revisé el servicio ${entry.title} en Meridiano Legal y quiero presentar una necesidad relacionada.`);
  return `<section class="detail-section detail-contact" id="contacto" aria-labelledby="contacto-title">
    <div class="container detail-contact-grid">
      <div><p class="detail-eyebrow">SIGUIENTE PASO</p><h2 id="contacto-title">Convirtamos la necesidad en un alcance verificable.</h2><p>La primera conversación permite comprender decisión, urgencia, actores, volumen y resultado esperado. A partir de allí se define perímetro, entregables, responsables, tiempos, honorarios y exclusiones. No envíe todavía información confidencial ni documentos sensibles.</p></div>
      <div class="detail-contact-panel"><strong>${escapeHtml(entry.title)}</strong><span>${escapeHtml(entry.type)} · ${escapeHtml(entry.duration)}</span><div class="detail-cta-row"><a class="btn btn-gold" href="https://wa.me/${WHATSAPP}?text=${whatsappText}" target="_blank" rel="noopener noreferrer">Conversar por WhatsApp →</a><a class="btn btn-outline-light" href="../index.html#contacto">Formulario general</a></div></div>
    </div>
  </section>`;
};

const bodyInner = (entry) => {
  const supplementAndRelated = `<div class="detail-subgroup"><h3>Unidades y extensiones disponibles</h3>${cards(entry.supplements || [], 'scope', 'EXTENSIÓN')}</div>
  <div class="detail-subgroup"><h3>Soluciones relacionadas</h3>${relatedGrid(entry)}</div>`;
  return [
    section({ id: 'pregunta', eyebrow: 'PREGUNTA EJECUTIVA', title: 'La decisión que organiza el servicio.', body: `<div class="executive-question"><span>PREGUNTA CENTRAL</span><p>${escapeHtml(entry.question)}</p></div>` }),
    section({ id: 'resultado', eyebrow: 'RESULTADO EMPRESARIAL', title: 'Qué cambia cuando el servicio termina o entra en operación.', className: 'ivory', body: `<div class="result-panel"><p>${escapeHtml(entry.result)}</p></div>` }),
    section({ id: 'situaciones', eyebrow: 'CUÁNDO PUEDE SER ÚTIL', title: 'Situaciones en las que esta intervención suele resolver una necesidad real.', description: 'La calificación definitiva depende de hechos, documentos, actores, materialidad, urgencia y especialidades aplicables.', className: 'soft', body: cards(entry.situations, 'situation', 'SITUACIÓN') }),
    section({ id: 'alcance', eyebrow: 'ARQUITECTURA DEL SERVICIO', title: 'Frentes jurídicos que puede comprender la intervención.', description: 'La propuesta definitiva identifica expresamente los frentes incluidos, su profundidad y cualquier materia que requiera un alcance adicional.', body: cards(entry.scope, 'scope', 'FRENTE') }),
    section({ id: 'perimetro', eyebrow: 'PERÍMETRO DE REFERENCIA', title: 'Volumen, unidades y límites para saber qué se está contratando.', description: 'Estas unidades sirven como referencia comercial; la propuesta concreta confirma cantidades, rondas, usuarios, entidades y documentos aplicables.', className: 'ivory', body: cards(entry.perimeter, 'scope', 'REFERENCIA') }),
    section({ id: 'metodo', eyebrow: 'MÉTODO DE TRABAJO', title: 'Una secuencia con hitos, decisiones y trazabilidad.', description: 'El método se adapta al asunto sin perder conexión entre información, análisis, documento, decisión e implementación.', body: methodList(entry) }),
    section({ id: 'entregables', eyebrow: 'ENTREGABLES', title: 'Qué recibe la empresa y para qué sirve cada salida.', description: 'La propuesta confirma qué entregables se incluyen y evita sustituir profundidad jurídica por documentos genéricos.', className: 'soft', body: cards(entry.deliverables, 'deliverable', 'ENTREGABLE') }),
    section({ id: 'formatos', eyebrow: 'FORMATOS, PLATAFORMA Y TRAZABILIDAD', title: 'Dónde se entrega y cómo queda administrable.', description: 'Los formatos se ajustan a la naturaleza del asunto y al entorno tecnológico habilitado por el cliente.', body: cards(entry.formats, 'scope', 'FORMATO') }),
    section({ id: 'cronograma', eyebrow: 'CADENCIA Y CRONOGRAMA', title: `Cómo puede organizarse un horizonte de ${escapeHtml(entry.duration)}.`, description: 'Los plazos dependen de disponibilidad de información, decisiones internas, terceros y complejidad efectiva.', className: 'ivory', body: cards(entry.timeline, 'scope', 'HITO') }),
    section({ id: 'requisitos', eyebrow: 'INFORMACIÓN Y PARTICIPACIÓN', title: 'Qué debe aportar la empresa para que el análisis sea serio y útil.', description: 'Los vacíos de información se documentan y pueden modificar profundidad, plazo o conclusión.', body: cards(entry.requirements, 'requirement', 'REQUISITO') }),
    section({ id: 'responsabilidades', eyebrow: 'RESPONSABILIDADES', title: 'Quién hace qué durante la intervención.', description: 'La delimitación evita trasladar al asesor decisiones de negocio, tareas técnicas o actuaciones que pertenecen a terceros.', className: 'soft', body: cards(entry.responsibilities, 'scope', 'RESPONSABLE') }),
    section({ id: 'aceptacion', eyebrow: 'CRITERIOS DE ACEPTACIÓN', title: 'Cómo se verifica que el alcance acordado fue ejecutado.', description: 'El cierre se contrasta con entregables y criterios objetivos, no con resultados que dependan de autoridades, contrapartes o mercado.', body: cards(entry.acceptance, 'scope', 'CRITERIO') }),
    `<section class="detail-section" aria-labelledby="limites-title">${limitsBlock(entry)}</section>`,
    section({ id: 'relacionadas', eyebrow: 'EXTENSIONES Y CONTINUIDAD', title: 'Qué puede ampliarse y cómo puede continuar el acompañamiento.', description: 'Las extensiones permiten aumentar el perímetro sin convertir el alcance inicial en una obligación abierta.', className: 'ivory', body: supplementAndRelated }),
    contactBlock(entry),
  ].join('\n');
};

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

const serviceFiles = fs.readdirSync(path.join(ROOT, 'servicios')).filter((name) => name.endsWith('.html')).map((name) => `servicios/${name}`);
let updated = 0;
for (const [catalogId, entry] of Object.entries(entries)) {
  if (!entry.serviceV42) throw new Error(`Servicio v4.2 sin bandera serviceV42: ${catalogId}`);
  const pagePath = serviceFiles.find((relative) => fs.readFileSync(path.join(ROOT, relative), 'utf8').includes(`data-catalog-id="${catalogId}"`));
  if (!pagePath) throw new Error(`No existe una ficha de servicio para ${catalogId}.`);
  const absolute = path.join(ROOT, pagePath);
  let html = ensureBlocks(fs.readFileSync(absolute, 'utf8'));
  html = replaceBlock(html, 'STATIC-CATALOG-HERO', `<div class="container detail-hero-grid" id="detail-hero-content" data-static-catalog="true">\n${heroInner(entry)}\n</div>`);
  html = replaceBlock(html, 'STATIC-CATALOG-BODY', `<main id="contenido"><div id="detail-page" data-static-catalog="true">\n${bodyInner(entry)}\n</div></main>`);
  html = enhanceHeadAndScripts(html, entry);
  fs.writeFileSync(absolute, html, 'utf8');
  updated += 1;
}
if (updated !== 8) throw new Error(`Se esperaban 8 servicios v4.2 y se generaron ${updated}.`);
console.log(`Contenido estático v4.2 generado en ${updated} fichas de servicio.`);
