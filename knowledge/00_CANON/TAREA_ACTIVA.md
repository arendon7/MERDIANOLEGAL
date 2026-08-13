# Meridiano Legal — Tarea activa

Actualizado: 2026-08-12.

## Release activa

**v5.21.0 — frontera de capacidades reales y superficies demostrativas.**

La auditoría posterior a v5.20 confirmó que el catálogo, las fichas profundas y la arquitectura inicial de decisión ya tienen suficiente profundidad. El siguiente riesgo de confianza está en la frontera entre lo que la web demuestra y lo que realmente está operativo: `demo.html` es una interfaz ficticia/noindex, pero algunas superficies públicas todavía la presentan como “Área de clientes”.

## Objetivo

Convertir esa frontera en un contrato técnico verificable:

1. `site-config.json` declara explícitamente si existe o no un portal real de clientes;
2. mientras `client_portal.enabled=false`, ninguna superficie indexable puede presentar la demo como área o portal productivo;
3. todo enlace público hacia `demo.html` debe incorporar una etiqueta inequívocamente demostrativa;
4. `runtime-config.js` y `site-status.json` publican el estado real de la capacidad;
5. `demo.html` conserva `noindex,nofollow`, datos ficticios y una marca técnica `demo-only`;
6. si en el futuro se habilita un portal real, la configuración deberá contener una URL HTTPS distinta de `demo.html` y CI exigirá al menos un enlace público real hacia ella.

## Alcance técnico

- `version.json`: `5.21.0`;
- `site-config.json`: nueva capacidad `capabilities.client_portal`;
- `scripts/site_config.py`: validación estricta de estado/URL;
- `scripts/apply_capability_truth_v521.py`: normalización final de enlaces demo + runtime/status;
- `scripts/validate_capability_truth_v521.py`: contrato anti-drift;
- `scripts/apply_handoff_observability_v518.py`: hook final version-aware para materializar v5.21 después de todas las capas históricas;
- `tests/e2e/capability-truth.spec.mjs`: cobertura real desktop/móvil/WebKit.

## Contrato v5.21

- portal real actualmente deshabilitado;
- `demo.html` no puede ser la URL de un portal real;
- “Área de clientes” no puede aparecer como CTA público mientras el portal esté deshabilitado;
- cualquier CTA hacia `demo.html` debe decir `demo` o `demostrativo`;
- demo continúa fuera del sitemap y con `noindex,nofollow`;
- no autenticación real;
- no cuentas reales;
- no backend, CRM, storage persistente, email transaccional, firma, pagos, agenda ni carga documental nuevos;
- no nueva PII ni transporte de red;
- no modificación del catálogo ni de las 16 fichas profundas;
- no reducción de cobertura E2E/axe/Lighthouse;
- no relajación de budgets v5.5.

## Criterio de cierre

1. Release Governance: PASS;
2. builder canónico e idempotencia: PASS;
3. validator v5.21 + validadores históricos: PASS;
4. Pages + smoke público: PASS;
5. Browser E2E + axe: sin regresiones y con nueva cobertura v5.21;
6. Lighthouse: 6/6 dentro de budgets vigentes;
7. release-health: PASS;
8. promoción de `stable` solo después de todos los gates verdes;
9. Graphify fresco y versionado en `5.21.0`;
10. documentación final y cierre de la tarea.

## No objetivos

- no construir todavía un portal productivo;
- no crear usuarios o autenticación reales;
- no convertir datos ficticios de la demo en datos persistentes;
- no ampliar productos/servicios;
- no abrir v5.22 dentro de este ciclo.
