# Meridiano Legal — Tarea activa

Actualizado: 2026-08-12.

## Release en cierre formal

**v5.16.0 — UX móvil y accesibilidad verificable.**

La funcionalidad está certificada. Evidencia de referencia antes de este cierre documental:

- SHA funcional: `2cd5fb0d2b428187c08cf21e562427f9bc44508c`;
- run funcional: `31618614227`;
- `main == stable` en ese SHA;
- builder/idempotencia + validadores: PASS;
- Pages + smoke: PASS;
- Browser E2E + axe: 37 → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- 7 superficies axe limpias;
- Lighthouse: 6/6 PASS, accesibilidad 1.00 en las seis superficies y `accessibilityAuditGaps` vacío;
- CI hasta `stable`: 187 s;
- baseline v5.5: 279 s;
- mejora: 33.0%;
- cobertura reducida: no;
- budgets relajados: no.

Graphify funcional apunta exactamente a `source_commit = 2cd5fb0d2b428187c08cf21e562427f9bc44508c`, con Graphify 0.9.26, 548 nodos, 882 relaciones y 88 notas. Su versión declarativa aún era 5.15.0 porque el snapshot precede al cambio de `version.json` de este cierre.

## Qué cerró funcionalmente v5.16

1. observabilidad Lighthouse persistente para auditorías de accesibilidad con score < 1;
2. targets >=44 px en tres CTA de Perspectivas;
3. progressive disclosure móvil nativo para detalle secundario v5.10/v5.11, sin eliminar contenido;
4. calificación, contexto, recomendación y ruta visibles de forma permanente;
5. acceso de teclado + nombre accesible para tres regiones móviles desplazables;
6. contraste móvil corregido en el paso comercial expuesto por axe;
7. menú profundo, cinco enlaces y CTA móvil de fichas con targets/contraste corregidos;
8. axe móvil de portada y ficha profunda dentro de las mismas 37 entradas protegidas;
9. seis superficies Lighthouse en A11y 1.00.

## Condición de cierre definitivo de v5.16.0

El SHA que contenga este cierre/versionado debe atravesar nuevamente:

1. builder canónico y sincronización visible a 5.16.0;
2. idempotencia + validadores históricos;
3. Pages + smoke;
4. Browser E2E/axe;
5. Lighthouse y revisión del artifact de accesibilidad;
6. release-health y trigger guard;
7. promoción de `stable`;
8. verificación `main == stable`;
9. procedencia Graphify sin falsificar `source_commit`.

**v5.17 no inicia hasta que esos nueve puntos estén verdes sobre el SHA final versionado.**

## Próximo ciclo después del cierre

**v5.17 — continuidad del handoff comercial.**

### Objetivo candidato

Reducir la fricción entre resumen comercial preparado, salida manual a WhatsApp y expectativa de respuesta, especialmente en móvil, sin convertir el sitio estático en un CRM ni inventar automatizaciones externas.

### Prioridades candidatas

1. medir qué información debe quedar visible justo antes de abrir WhatsApp y qué parte puede compactarse;
2. clarificar qué conservar/copiado y qué ocurre después del handoff;
3. revisar retorno a la web, foco y legibilidad del resumen preparado en móvil;
4. mantener el envío como acción manual del usuario;
5. reutilizar contexto ya existente sin PII adicional ni persistencia nueva;
6. ampliar assertions dentro de las 37 entradas antes de añadir tests independientes.

### No objetivos

- no backend/CRM;
- no envío automático de WhatsApp;
- no email transaccional;
- no firma, pagos, agenda o expediente;
- no `localStorage`/`sessionStorage` adicional para la decisión;
- no PII adicional en telemetría;
- no scoring opaco;
- no relajar budgets/axe/E2E.

## Contratos a preservar

- static-first;
- 46 páginas HTML;
- 16 fichas profundas;
- 37 entradas E2E salvo necesidad independiente demostrada;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5;
- fuente jurídica única;
- WhatsApp manual;
- telemetría sin PII;
- builder idempotente;
- `stable` solo después de todos los gates verdes.
