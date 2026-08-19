# Meridiano Legal — Tarea activa

Actualizado: 2026-08-19.

## Frente vigente

**v7.3.0 — Legal Intelligence Demo / release candidate.**

Rama: `release/v730-legal-intelligence-demo-candidate`.

La fase funcional quedó certificada y fusionada mediante PR #177.

- Baseline anterior certificado: v7.2.0.
- SHA funcional final: `dc3d4beea5637fc6aa104964d0fd0849b8c904c7`.
- 10/10 workflows aplicables verdes sobre el SHA funcional.
- Merge funcional #177: `4867f3418c45a5a6689cd43b79ff48f191cda3a1`.

## Qué añade v7.3

El Centro Demo conserva sus cinco experiencias históricas y añade una sexta pestaña **Legal Intelligence** con cinco escenarios completamente ficticios:

1. Legal AI Transformation.
2. Contract Control.
3. AI Governance 360.
4. Regulatory Control.
5. Meridiano Legal Desk.

Cada escenario muestra:

**problema → flujo → artefacto demostrativo → resultado → referencia de alcance → frontera → oferta relacionada**.

## Fuente de verdad

Las referencias cuantitativas se derivan verbatim de los catálogos canónicos aplicables. Legal Desk no publica LU, volumen, canales, SLA o capacidad incluida porque esa verdad no está aprobada.

## Candidate formal

Este branch cambia únicamente lifecycle/release metadata respecto de la funcionalidad ya fusionada:

- `version.json`: 7.2.0 → 7.3.0, canal `github-pages-legal-intelligence-demo-candidate`;
- `assets/data/v7/legal-intelligence-demo-v73.json`: `demo-prototype` → `release-candidate`;
- `scripts/validate_legal_intelligence_demo_v73.py`: lifecycle phase-aware `demo-prototype → release-candidate → certified`;
- esta memoria de tarea.

No debe introducir cambios nuevos en `experiencia.html`, CSS funcional, catálogos, E2E o capabilities.

## Capability truth preservado

- DEMO y datos ficticios visibles;
- sin carga de información real;
- sin asesoría jurídica;
- sin portal productivo implícito;
- sin Meridiano Counsel;
- sin monitoreo automático universal;
- sin decisión jurídica autónoma;
- sin precios nuevos;
- Legal Desk no fija capacidad, LU o SLA estándar.

## Gate del candidate

Antes de merge:

1. confirmar boundary mínimo de cuatro archivos;
2. fijar SHA final;
3. superar todos los workflows aplicables sobre ese mismo SHA;
4. fusionar únicamente con `expected_head_sha`;
5. observar Builder canónico;
6. exigir Pages quality/deploy → live smoke → Browser/axe + Lighthouse;
7. permitir únicamente promoción automática de `stable`;
8. terminar con `main == stable` antes del cierre documental.

`stable` no se mueve manualmente.

## Cierre posterior

Después de certificar productivamente el candidate se abrirá un PR separado `candidate → production-certified` con boundary documental mínimo: versión/canal, contrato `certified`, README, RELEASE-v7.3 y memoria canónica.
