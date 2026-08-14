# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-14.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Fuente técnica/documental: `main`.
- Snapshot funcional certificado: `stable`.
- Release funcional certificada: **5.30.0 — profundidad comercial de las 16 ofertas**.
- SHA funcional certificado: `ee88b8ced3347255cf85ee62e3bf4022b7c34a42`.
- Canal: `github-pages-production-offer-commercial-depth-certified`.
- No existe un ciclo funcional posterior activo.
- El SHA documental definitivo no se fija dentro de esta nota: verificar los refs vigentes `main` y `stable`, que deben coincidir una vez concluida la certificación del cierre.

## Resultado v5.30

La auditoría de las 16 ofertas confirmó que la profundidad jurídica ya era suficiente; la fricción estaba en reconstruir la lógica de compra entre varias secciones. v5.30 complementa el resumen `buying-clarity-v58` sin reescribir los catálogos ni crear otra sección narrativa.

Cada oferta muestra ahora:

- unidad/base de contratación;
- lógica de dimensionamiento de honorarios sin importes o monedas;
- tres drivers de alcance;
- regla de ampliación/cambio de modalidad;
- cierre verificable;
- enlaces al perímetro, aceptación y contacto canónicos.

`catalog-products-v41/` y `catalog-services-v42/` continúan siendo la fuente jurídica de perímetro, entregables, responsabilidades, criterios de aceptación, límites, suplementos y cantidades.

## Evidencia funcional

- PR funcional: `#134`.
- Release Governance: `31834565612` — PASS.
- Builder canónico: `31834618506` — PASS, 30 pasos.
- SHA canónico funcional: `ee88b8ced3347255cf85ee62e3bf4022b7c34a42`.
- Site Quality and Deploy #377: `31834646140` — PASS.
- Idempotencia / segunda pasada: PASS.
- Validaciones estáticas: 37/37 — PASS.
- GitHub Pages: PASS.
- Smoke público: PASS.
- Browser E2E/axe: **100 observados · 98 PASS · 2 SKIP · 0 FAIL · 0 reintentos**.
- Lighthouse: PASS con budgets existentes.
- Promoción de `stable`: PASS.
- Budgets relajados: no.
- Cobertura reducida: no.

## Invariantes preservadas

- 46 HTML;
- 16 fichas profundas;
- un único formulario físico;
- WhatsApp manual;
- portal real deshabilitado;
- funnel v5.29 en memoria, sin PII ni persistencia;
- no inferir conversión comercial desde navegación, contacto o handoff;
- no clientes, testimonios o resultados inventados;
- no importes, monedas o tarifas inventadas;
- no cotizador ni scoring automático de honorarios;
- no ocultar profundidad para aparentar menor densidad;
- exactamente 30 pasos canónicos;
- idempotencia, E2E/axe y Lighthouse sin relajación;
- `stable` únicamente después de gates verdes.

## Estado del ciclo

**v5.30 está implementada y certificada funcionalmente. El cierre documental se considera definitivo cuando el commit que contiene esta memoria haya atravesado los mismos gates y `main = stable`; no abrir una nueva release funcional hasta definir problema, baseline, contrato y verificación.**
