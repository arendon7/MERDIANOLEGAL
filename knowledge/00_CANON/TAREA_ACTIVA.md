# Meridiano Legal — Tarea activa

Actualizado: 2026-08-19.

## Frente vigente

**v7.3.0 — Legal Intelligence Demo / production-certified closure.**

Rama: `docs/v730-certified-closure`.

La funcionalidad y el candidate ya fueron certificados productivamente.

- Baseline anterior certificado: v7.2.0.
- SHA funcional final v7.3: `dc3d4beea5637fc6aa104964d0fd0849b8c904c7`.
- 10/10 workflows aplicables verdes sobre el SHA funcional.
- Merge funcional #177: `4867f3418c45a5a6689cd43b79ff48f191cda3a1`.
- SHA candidate final: `e8656a0ea69aa8cf8140a6d41e74130e3cec9f60`.
- 10/10 workflows aplicables verdes sobre el SHA candidate.
- Merge candidate #178: `6c194effd5421326f05296c1e99c54f852f04398`.
- Builder/snapshot productivo candidate: `2999d28dc6e4ae497ecbfbb9469f55364f34d899`.
- Pages quality/deploy/live smoke + Browser/axe + Lighthouse: PASS.
- `stable` fue promovido automáticamente a `2999d28dc6e4ae497ecbfbb9469f55364f34d899`.

## Qué añade v7.3

El Centro Demo conserva sus cinco experiencias históricas y añade una sexta pestaña **Legal Intelligence** con cinco escenarios completamente ficticios:

1. Legal AI Transformation.
2. Contract Control.
3. AI Governance 360.
4. Regulatory Control.
5. Meridiano Legal Desk.

Cada escenario muestra:

**problema → flujo → artefacto demostrativo → resultado → referencia de alcance → frontera → oferta relacionada**.

Las referencias cuantitativas provienen verbatim de los catálogos canónicos aplicables. Legal Desk no publica LU, volumen, canales, SLA o capacidad estándar.

## Correcciones cerradas

Durante desarrollo/candidate se corrigieron sin relajar ningún gate:

1. falso positivo del validator sobre la negación de Legal Units/SLA de Legal Desk;
2. idempotencia de markers administrados;
3. recomposición canónica v7.3 después de las capas v6;
4. incompatibilidad de lifecycle del materializador al pasar de prototype a candidate.

Validator y materializador comparten ahora una máquina de estados cerrada:

- `demo-prototype` → prefijo `7.3.0-prototype`;
- `release-candidate` → versión exacta `7.3.0`;
- `certified` → versión exacta `7.3.0`;
- baseline exacta `7.2.0`.

## Capability truth preservado

- DEMO y datos ficticios visibles;
- sin carga de información real;
- sin asesoría jurídica;
- sin portal productivo implícito;
- sin Meridiano Counsel;
- sin monitoreo automático universal;
- sin decisión jurídica autónoma;
- sin precios nuevos;
- Legal Desk no fija capacidad, LU o SLA estándar;
- Contract Control y Regulatory Control no son SaaS autónomos.

## Boundary del cierre

El cierre `production-certified` modifica exactamente siete archivos:

1. `version.json`: canal candidate → `github-pages-production-legal-intelligence-demo-certified`.
2. `assets/data/v7/legal-intelligence-demo-v73.json`: `release-candidate` → `certified`.
3. `README.md`.
4. `RELEASE-v7.3.md`.
5. `knowledge/00_CANON/CONTEXTO_RAPIDO.md`.
6. `knowledge/00_CANON/ESTADO_ACTUAL.md`.
7. esta memoria.

No modifica HTML, CSS, catálogos, materializadores, validators funcionales, E2E, workflows ni capabilities.

## Gate del cierre

Antes de declarar v7.3 definitivamente cerrada:

1. confirmar boundary exacto de siete archivos;
2. fijar SHA final del PR;
3. superar todos los workflows aplicables sobre ese mismo SHA;
4. fusionar únicamente con `expected_head_sha`;
5. observar Builder canónico;
6. exigir Pages quality/deploy → live smoke → Browser/axe + Lighthouse;
7. permitir únicamente promoción automática de `stable`;
8. terminar con `main == stable`;
9. confirmar `stable/version.json` = v7.3.0 + canal `github-pages-production-legal-intelligence-demo-certified`.

`stable` no se mueve manualmente.

## Después de v7.3

El siguiente frente debe priorizarse con evidencia comercial real producida por la navegación, fichas comprables y Centro Demo. No se abrirán nuevas capabilities tecnológicas solo por completar catálogo: la siguiente ola debe responder a señales de demanda, conversión o aprendizaje verificable.
