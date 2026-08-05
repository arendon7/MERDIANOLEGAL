#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const SOURCE_PATH = path.join(ROOT, 'catalog-v32.js');
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

const hero = (entry) => `<div>
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

const body = (entry) => {
  const method = `<ol class="method-list">${entry.method.map(([title, description], index) => `
    <li><b>${String(index + 1).padStart(2, '0')}</b><strong>${escapeHtml(title)}</strong><span>${escapeHtml(description)}</span></li>`).join('')}
  </ol>`;
  const limits = `<div class="container limits-layout">
    <div class="limits-intro"><p class="detail-eyebrow">LÍMITES Y EXCLUSIONES</p><h2 id="limites-title">Claridad sobre lo que esta solución no promete.</h2><p>El rigor también exige separar decisiones propias, especialidades externas y resultados que dependen de autoridades o terceros.</p></div>
    <ul class="limits-list">${entry.limits.map((item) => `<li>${escapeHtml(item)}</li>`).join('')}</ul>
  </div>`;
  const related = `<div class="related-grid">${entry.related.map(([label, title, description, url]) => `
    <article class="related-card"><span>${escapeHtml(label)}</span><strong>${escapeHtml(title)}</strong><p>${escapeHtml(description)}</p><a href="${escapeHtml(url)}">Explorar →</a></article>`).join('')}
  </div>`;
  const whatsappText = encodeURIComponent(`Hola, revisé la ficha de ${entry.title} en Meridiano Legal y quiero presentar una necesidad relacionada.`);
  const contact = `<section class="detail-section detail-contact" id="contacto" aria-labelledby="contacto-title">
    <div class="container detail-contact-grid">
      <div><p class="detail-eyebrow">SIGUIENTE PASO</p><h2 id="contacto-title">Definamos si esta es la solución adecuada para su necesidad.</h2><p>La primera conversación permite comprender la decisión, la urgencia, los actores, la evidencia y el resultado esperado. No envíe todavía información confidencial ni documentos sensibles.</p></div>
      <div class="detail-contact-panel"><strong>${escapeHtml(entry.title)}</strong><span>${escapeHtml(entry.type)} · ${escapeHtml(entry.duration)}</span><div class="detail-cta-row"><a class="btn btn-gold" href="https://wa.me/${WHATSAPP}?text=${whatsappText}" target="_blank" rel="noopener noreferrer">Conversar por WhatsApp →</a><a class="btn btn-outline-light" href="../index.html#contacto">Formulario general</a></div></div>
    </div>
  </section>`;

  return [
    section({ id: 'pregunta', eyebrow: 'PREGUNTA EJECUTIVA', title: 'La decisión que organiza el alcance.', body: `<div class="executive-question"><span>PREGUNTA CENTRAL</span><p>${escapeHtml(entry.question)}</p></div>` }),
    section({ id: 'situaciones', eyebrow: 'CUÁNDO PUEDE SER ÚTIL', title: 'Situaciones que justifican evaluar esta solución.', description: 'La calificación definitiva depende de hechos, documentos, actores, urgencia y especialidades aplicables.', className: 'soft', body: cards(entry.situations, 'situation', 'SITUACIÓN') }),
    section({ id: 'alcance', eyebrow: 'ALCANCE ORIENTATIVO', title: 'Qué frentes puede comprender.', description: 'La propuesta final define expresamente el perímetro, la profundidad, las revisiones y las exclusiones.', body: cards(entry.scope, 'scope', 'FRENTE') }),
    section({ id: 'metodo', eyebrow: 'MÉTODO DE TRABAJO', title: 'Una secuencia que evita documentos prematuros.', description: 'El orden puede adaptarse al asunto, pero siempre debe conservar comprensión, calificación, estructuración, implementación y cierre.', className: 'ivory', body: method }),
    section({ id: 'entregables', eyebrow: 'ENTREGABLES', title: 'Qué puede recibir la empresa.', description: 'Los formatos se ajustan al alcance y deben indicar supuestos, fuentes, responsables, límites y condiciones de actualización.', body: cards(entry.deliverables, 'deliverable', 'SALIDA') }),
    section({ id: 'requisitos', eyebrow: 'INFORMACIÓN Y PARTICIPACIÓN', title: 'Qué se requiere para trabajar con rigor.', description: 'La falta de información o de responsables puede modificar cronograma, profundidad y conclusiones.', className: 'soft', body: cards(entry.requirements, 'requirement', 'REQUISITO') }),
    `<section class="detail-section" aria-labelledby="limites-title">${limits}</section>`,
    section({ id: 'relacionadas', eyebrow: 'SOLUCIONES RELACIONADAS', title: 'Cómo puede conectarse con el resto del portafolio.', className: 'ivory', body: related }),
    contact,
  ].join('\n');
};

const replaceBlock = (html, name, content) => {
  const pattern = new RegExp(`<!-- ${name}:START -->[\\s\\S]*?<!-- ${name}:END -->`);
  if (!pattern.test(html)) throw new Error(`Falta el bloque ${name}.`);
  return html.replace(pattern, `<!-- ${name}:START -->\n${content}\n<!-- ${name}:END -->`);
};

let updated = 0;
for (const [catalogId, entry] of Object.entries(entries)) {
  const match = source.match(new RegExp(`['\"]${catalogId}['\"]`));
  if (!match) throw new Error(`Entrada no localizada: ${catalogId}`);
  const pagePath = [...fs.readdirSync(path.join(ROOT, 'servicios')).map((name) => `servicios/${name}`), ...fs.readdirSync(path.join(ROOT, 'productos')).map((name) => `productos/${name}`)]
    .find((relative) => fs.readFileSync(path.join(ROOT, relative), 'utf8').includes(`data-catalog-id="${catalogId}"`));
  if (!pagePath) throw new Error(`No existe una ficha para ${catalogId}.`);
  const absolute = path.join(ROOT, pagePath);
  let html = fs.readFileSync(absolute, 'utf8');
  html = replaceBlock(html, 'STATIC-CATALOG-HERO', hero(entry));
  html = replaceBlock(html, 'STATIC-CATALOG-BODY', body(entry));
  fs.writeFileSync(absolute, html, 'utf8');
  updated += 1;
}
console.log(`Contenido estático generado en ${updated} fichas.`);
