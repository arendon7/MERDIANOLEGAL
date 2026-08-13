# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente. `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md` mandan si existe cualquier diferencia.

## Proyecto

Sitio público y centro demostrativo de Meridiano Legal. Arquitectura static-first publicada en GitHub Pages, con 46 páginas HTML, 16 fichas profundas y un único formulario físico canónico.

## Capas vigentes

v5.8 claridad de compra → v5.9 calificación → v5.10 propuesta/cierre → v5.11 engagement readiness → v5.12 prueba verificable → v5.13 continuidad comercial → v5.14 recomendación explicable → v5.15 recomendación→acción → hardening v5.16 → v5.17 continuidad manual del handoff → v5.18 observabilidad verificable → v5.19 disclosure adaptativo → v5.20 compresión de decisión → v5.21 frontera demo/capacidad real → **v5.22 arquitectura editorial de oferta, actualmente candidata**.

## Último snapshot público certificado

- Release pública cerrada: `5.21.0`.
- SHA funcional certificado: `b2a6d4d4d2608362e86b53ea4cc197cd7ce33cc1`.
- Run público final: `31658340092`.
- `stable` permanece en ese SHA hasta que una candidata posterior supere todos los gates.
- Browser E2E + axe v5.21: 43 observados → 41 PASS / 2 SKIP / 0 FAIL / 0 RETRY.
- Lighthouse v5.21: 6/6 PASS; accesibilidad 1.00 en las seis superficies.
- Portal real de clientes: deshabilitado; `demo.html` es exclusivamente demostrativo/noindex.

## Release activa v5.22

Objetivo: reconciliar las mejores versiones históricas de narrativa y profundidad jurídica con el catálogo v4.1/v4.2 y la arquitectura comercial v5.20–v5.21.

La release no crea ofertas nuevas. Mantiene las 16 fichas y añade una capa editorial compacta por `catalog-id` con:

1. decisión empresarial;
2. por qué esa modalidad;
3. alternativa cercana;
4. lente jurídica de análisis;
5. capacidad que queda instalada.

Pares prioritarios: diagnóstico/auditoría, contratación puntual/sistema contractual, PI, IA y proyectos regulados.

La narrativa no vende horas aisladas como unidad principal. El comprador debe poder entender resultado, perímetro, método, entregables, responsabilidades, límites y cierre. El seniority se demuestra en el criterio y la estructura del trabajo, no mediante claims no verificables.

## Fuentes principales v5.22

- `offer-narrative-v522.json` — contrato editorial de 16 ofertas;
- `offer-v522.css` — presentación trust-first;
- `scripts/apply_offer_narrative_v522.py` — materialización final y reconciliación de portada;
- `scripts/validate_offer_narrative_v522.py` — contrato anti-drift;
- `catalog-products-v41/` y `catalog-services-v42/` — perímetro jurídico/comercial fuente;
- `recommendation-v514.json` — límites y alternativas de modalidad;
- `tests/e2e/` — Browser + axe;
- `quality-budgets-v55.json` + `scripts/run_quality_v55.mjs` — Lighthouse/budgets;
- workflows builder, Pages y Release Governance.

## Invariantes

- no inventar clientes, testimonios, premios, antigüedad o resultados;
- no PII ni nueva persistencia/transporte;
- WhatsApp manual;
- portal real deshabilitado mientras no exista implementación auténtica;
- no CRM/backend, firma, pagos, agenda, autenticación o carga documental ficticios;
- no reducir cobertura ni relajar budgets;
- conservar una sola superficie de modalidad v5.20;
- `stable` solo después de gates verdes.

## Secuencia de release

fuentes → builder canónico → capas históricas → capability truth v5.21 → narrativa v5.22 → idempotencia/validators → Pages → smoke → Browser/axe + Lighthouse → release-health → `stable`.

## Graphify

Graphify es memoria derivada. Verifique `graphify-out/BUILD_META.json` contra el `main` realmente procesado por el último run exitoso; no use un SHA histórico como sustituto de la comprobación de frescura.
