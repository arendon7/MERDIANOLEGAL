# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente. `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md` mandan si existe cualquier diferencia.

## Proyecto

Sitio público y centro demostrativo de Meridiano Legal. Arquitectura static-first publicada en GitHub Pages, con 46 páginas HTML, 16 fichas profundas y un único formulario físico canónico.

## Capas vigentes

v5.8 claridad de compra → v5.9 calificación → v5.10 propuesta/cierre → v5.11 engagement readiness → v5.12 prueba verificable → v5.13 continuidad comercial → v5.14 recomendación explicable → v5.15 recomendación→acción → hardening v5.16 → v5.17 continuidad manual del handoff → v5.18 observabilidad verificable → v5.19 disclosure adaptativo → v5.20 compresión de decisión → v5.21 frontera demo/capacidad real → **v5.22 arquitectura editorial de oferta y narrativa jurídica senior**.

## Último estado público certificado

- Release cerrada: `5.22.0`.
- SHA funcional de las mejoras: `5c3f3194b45afb9ac21a8def27afdc3d2157b3e2`.
- Run funcional: `31671834728`.
- Snapshot público final `ready`: `dcb5bc9643eff595c0f8614c7cf6acbadc3bb719`.
- Run de recertificación final: `31673266141`.
- Canal: `github-pages-public-offer-narrative-ready`.
- Browser E2E + axe: 49 observados → 47 PASS / 2 SKIP / 0 FAIL / 0 RETRY en la certificación funcional; el run `ready` volvió a pasar Browser E2E/axe.
- Lighthouse: 6/6 PASS; accesibilidad 1.00 en las seis superficies en la certificación funcional; el run `ready` volvió a pasar budgets.
- Portal real de clientes: deshabilitado; `demo.html` es exclusivamente demostrativo/noindex.
- No existe una release funcional posterior activa.

## Qué aporta v5.22

La release reconcilia las mejores versiones históricas de narrativa y profundidad jurídica con el catálogo v4.1/v4.2 y la arquitectura comercial v5.20–v5.21.

No crea ofertas nuevas. Mantiene las 16 fichas y añade una capa editorial compacta por `catalog-id` con:

1. decisión empresarial;
2. por qué esa modalidad;
3. alternativa cercana;
4. lente jurídica de análisis;
5. capacidad que queda instalada.

Pares explícitamente diferenciados: diagnóstico/auditoría, contratación puntual/sistema contractual, PI, IA y proyectos regulados.

La narrativa no vende horas aisladas como unidad principal. El comprador debe poder entender resultado, perímetro, método, entregables, responsabilidades, límites y cierre. El seniority se demuestra en el criterio y la estructura del trabajo, no mediante claims no verificables.

## Source-of-truth y capability truth

- `catalog-products-v41/` y `catalog-services-v42/` siguen siendo fuente jurídica/comercial.
- `offer-narrative-v522.json` añade el contrato editorial, no sustituye el catálogo.
- `scripts/apply_offer_narrative_v522.py` preserva el contenido fuente y falla ante copy ambiguo.
- `Meridiano Empresas` solo puede aparecer condicionado a habilitación productiva real o como demostración explícita.
- `catalog-page.js` preserva el prerender canónico cuando la ficha declara `data-static-catalog="true"`; no rehidrata destructivamente `#detail-page`.

## Fuentes principales v5.22

- `RELEASE-v5.22.md` — release note y evidencia completa;
- `offer-narrative-v522.json` — contrato editorial de 16 ofertas;
- `offer-v522.css` — presentación trust-first;
- `scripts/apply_offer_narrative_v522.py` — materialización final;
- `scripts/validate_offer_narrative_v522.py` — contrato anti-drift;
- `catalog-products-v41/` y `catalog-services-v42/` — perímetro jurídico/comercial fuente;
- `recommendation-v514.json` — límites y alternativas de modalidad;
- `tests/e2e/` — Browser + axe;
- `quality-budgets-v55.json` + `scripts/run_quality_v55.mjs` — Lighthouse/budgets;
- workflows builder, Pages y Release Governance.

## Evidencia clave

Certificación funcional:

- 49 E2E observados; 47 PASS / 2 SKIP.
- 7 superficies axe WCAG 2.1 AA sin violaciones serias/críticas.
- Lighthouse 6/6 PASS.
- Home: performance 1.00, a11y 1.00, LCP 1367 ms, CLS 0, TBT 55 ms.
- Product IA: performance 0.96, a11y 1.00, LCP 1245 ms, CLS 0, TBT 210 ms.
- CI hasta stable: 206 s; 26.2% mejor que baseline v5.5.

Recertificación `ready`:

- todos los gates PASS;
- CI hasta stable: 204 s;
- mejora: 26.9%;
- cobertura reducida: no;
- budgets relajados: no.

## Invariantes

- no inventar clientes, testimonios, premios, antigüedad o resultados;
- no PII ni nueva persistencia/transporte;
- WhatsApp manual;
- portal real deshabilitado mientras no exista implementación auténtica;
- no CRM/backend, firma, pagos, agenda, autenticación o carga documental ficticios;
- no reducir cobertura ni relajar budgets;
- conservar una sola superficie de modalidad v5.20;
- no mutar contenido contractual de forma oculta después del render;
- `stable` solo después de gates verdes.

## Estado del ciclo

**v5.22 cerrada; no hay release funcional activa. No abrir v5.23 por inercia.**

El siguiente ciclo debe empezar por auditoría y evidencia, no por numeración de versión.

## Graphify

Graphify es memoria derivada. El cierre documental final debe dejar `graphify-out/BUILD_META.json` apuntando al `main` documental procesado por el último run exitoso; `stable` puede permanecer en el snapshot público `ready` si los commits posteriores son solo documentación.
