# Meridiano Legal — Tarea activa

Actualizado: 2026-08-19.

## Baseline certificado

**v7.2.0 — Buying Clarity** está completamente cerrada y certificada.

- `main == stable == f7bbf06588518141490a62db7b9fae8530659991` al abrir este frente.
- `stable/version.json`: `7.2.0`, canal `github-pages-production-buying-clarity-certified`.
- 16/16 fichas profundas conservan su Resumen de contratación source-driven.

## Frente vigente

**v7.3 — Centro Demo / Legal Intelligence Scenarios.**

Rama: `feat/v730-legal-intelligence-demo`.

PR: `#177` — draft hasta cerrar regresión same-SHA.

## Objetivo

Que un comprador pueda ver, con información completamente ficticia, cómo cinco capacidades de Meridiano Legal Intelligence convierten un problema jurídico-operativo en un flujo, un artefacto, un resultado y una siguiente decisión.

Escenarios:

1. Legal AI Transformation.
2. Contract Control.
3. AI Governance 360.
4. Regulatory Control.
5. Meridiano Legal Desk.

## Diseño

El Centro Demo conserva las cinco experiencias históricas y añade una sexta pestaña **Legal Intelligence**.

Cada escenario muestra:

**problema → flujo → artefacto demostrativo → resultado → referencia de alcance → frontera → oferta relacionada**.

El panel se materializa source-driven desde `assets/data/v7/legal-intelligence-demo-v73.json`.

## Fuente de verdad cuantitativa

Las referencias de alcance se leen verbatim de:

- `catalog-services-v42/s08-legal-ops.json` para Legal AI Transformation;
- `catalog-products-v41/p07-contractual.json` para Contract Control;
- `catalog-products-v41/p05-ia.json` para AI Governance 360;
- `catalog-products-v41/p06-regulado.json` para Regulatory Control.

Legal Desk no muestra LU, volumen, canales, SLA o capacidad incluida porque esa verdad no está aprobada. Su card explica expresamente que esos elementos requieren propuesta y alcance específicos.

## Implementación

- contrato: `assets/data/v7/legal-intelligence-demo-v73.json`;
- CSS: `assets/css/v7/legal-intelligence-demo-v73.css`;
- materializador: `scripts/apply_legal_intelligence_demo_v73.py`;
- validator fail-closed: `scripts/validate_legal_intelligence_demo_v73.py`;
- integración: `scripts/normalize_experience_compat_v60.py`;
- HTML materializado: `experiencia.html`;
- E2E: `tests/e2e/legal-intelligence-demo-v73.spec.mjs`;
- gate dedicado: `.github/workflows/v73-legal-intelligence-demo-candidate.yml`.

`experiencia.js` no requiere cambios: el sistema existente de `data-target` / `data-panel` soporta la sexta pestaña.

## Boundary funcional actual

**9 archivos permanentes** respecto del baseline v7.2:

1. `.github/workflows/v73-legal-intelligence-demo-candidate.yml`.
2. `assets/css/v7/legal-intelligence-demo-v73.css`.
3. `assets/data/v7/legal-intelligence-demo-v73.json`.
4. `experiencia.html`.
5. `scripts/apply_legal_intelligence_demo_v73.py`.
6. `scripts/normalize_experience_compat_v60.py`.
7. `scripts/validate_legal_intelligence_demo_v73.py`.
8. `tests/e2e/legal-intelligence-demo-v73.spec.mjs`.
9. `knowledge/00_CANON/TAREA_ACTIVA.md`.

No quedan modificaciones temporales de Graphify ni workflows auxiliares.

## Capability truth

El panel exige de forma visible:

- `DEMO` en cada escenario;
- datos ficticios;
- sin carga de información real;
- sin asesoría jurídica;
- sin funcionalidad productiva implícita.

Además:

- no Meridiano Counsel;
- no portal productivo incluido;
- no monitoreo automático universal;
- no decisión jurídica autónoma;
- no precios nuevos;
- no métricas de Legal Desk no aprobadas;
- no outputs presentados como resultados de clientes reales.

## Correcciones realizadas durante materialización

1. El validator dejó de tratar la frase negativa “no fija … Legal Units, SLA…” como si fuera un claim positivo.
2. El materializador retira también la indentación de sus markers para que `apply → validate → --check` sea idempotente.
3. La capa se reaplica dentro del normalizador canónico después de las reconstrucciones v6.

## Criterio de aceptación funcional

1. La pestaña `Legal Intelligence` aparece una sola vez como sexta experiencia.
2. El panel contiene exactamente cinco escenarios.
3. Cada escenario muestra `DEMO` y una frontera explícita.
4. Las cantidades de los cuatro escenarios con perímetro estándar coinciden verbatim con sus catálogos.
5. Legal Desk no inventa capacidad, volumen, canales o SLA.
6. No existen forms/uploads dentro del nuevo panel.
7. El panel no altera las otras cinco experiencias.
8. El materializador es idempotente dentro de Canonical Builder.
9. Browser E2E/axe y Measurement E2E permanecen verdes.

## Gate de release

- fijar un SHA funcional final;
- superar todos los workflows aplicables same-SHA;
- merge #177 únicamente con `expected_head_sha`;
- después abrir candidate formal `7.3.0` como PR separado;
- Builder → Pages quality/deploy → live smoke → Browser/axe + Lighthouse → `stable` automático;
- cierre documental `candidate → production-certified` separado.

`stable` nunca se mueve manualmente.
