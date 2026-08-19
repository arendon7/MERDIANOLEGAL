# Release v7.3.0 — Legal Intelligence Demo

Fecha: 2026-08-19.

## Objetivo

Convertir el Centro Demo de Meridiano Legal en una demostración comercial concreta de la arquitectura **Meridiano Legal Intelligence**, de forma que un comprador pueda comprender cómo un problema jurídico-operativo se transforma en flujo, artefacto, resultado y siguiente decisión sin confundir la demostración con un portal productivo, asesoría real o software autónomo.

## Cambio funcional

El Centro Demo conserva sus cinco experiencias históricas y añade una sexta pestaña **Legal Intelligence** con cinco escenarios completamente ficticios:

1. Legal AI Transformation.
2. Contract Control.
3. AI Governance 360.
4. Regulatory Control.
5. Meridiano Legal Desk.

Cada escenario expone:

**problema → flujo → artefacto demostrativo → resultado → referencia de alcance → frontera → oferta relacionada**.

Las referencias cuantitativas de los cuatro escenarios con perímetro estándar se derivan verbatim de sus catálogos canónicos. Meridiano Legal Desk no fija LU, volumen, canales, SLA o capacidad incluida porque esa verdad solo puede existir en una propuesta específica.

## Evidencia funcional

- Baseline certificado v7.2.0: `f7bbf06588518141490a62db7b9fae8530659991`.
- SHA funcional final: `dc3d4beea5637fc6aa104964d0fd0849b8c904c7`.
- Gates funcionales same-SHA: 10/10 PASS.
- PR funcional #177 fusionado con `expected_head_sha`.
- Merge funcional: `4867f3418c45a5a6689cd43b79ff48f191cda3a1`.

## Candidate formal

- SHA candidate final: `e8656a0ea69aa8cf8140a6d41e74130e3cec9f60`.
- Gates aplicables same-SHA: 10/10 PASS.
- PR #178 fusionado con `expected_head_sha`.
- Merge candidate: `6c194effd5421326f05296c1e99c54f852f04398`.
- Builder canónico: `2999d28dc6e4ae497ecbfbb9469f55364f34d899`.
- Pages quality/deploy/live smoke: PASS.
- Browser E2E/axe desplegado: PASS.
- Lighthouse: PASS.
- `stable` promovido automáticamente a `2999d28dc6e4ae497ecbfbb9469f55364f34d899`.
- `stable/version.json`: `7.3.0`, canal `github-pages-legal-intelligence-demo-candidate` antes de este cierre.

## Implementación source-driven

La capa v7.3 está compuesta por:

- `assets/data/v7/legal-intelligence-demo-v73.json`;
- `assets/css/v7/legal-intelligence-demo-v73.css`;
- `scripts/apply_legal_intelligence_demo_v73.py`;
- `scripts/validate_legal_intelligence_demo_v73.py`;
- integración en `scripts/normalize_experience_compat_v60.py`;
- `tests/e2e/legal-intelligence-demo-v73.spec.mjs`;
- `.github/workflows/v73-legal-intelligence-demo-candidate.yml`;
- `experiencia.html` como superficie materializada.

`experiencia.js` no necesitó modificación: la arquitectura existente de `data-target` / `data-panel` soporta la sexta pestaña.

## Correcciones realizadas sin relajar gates

1. **Legal Desk capability boundary.** El primer validator trataba la frase negativa “no fija … Legal Units, SLA…” como si fuera un claim positivo. Se endureció para permitir la negación contractual y bloquear únicamente cantidades o promesas positivas no aprobadas.
2. **Idempotencia de markers.** El materializador incorporó la indentación de sus markers al bloque gestionado para evitar acumulación de espacios en segundas pasadas.
3. **Recomposición canónica.** v7.3 se reaplica desde `normalize_experience_compat_v60.py` después de las reconstrucciones v6.
4. **Lifecycle phase-aware.** Al abrir el candidate se detectó que el validator admitía `release-candidate`, pero el materializador aún exigía `7.3.0-prototype`. Se alinearon ambos con una máquina de estados fail-closed: `demo-prototype → release-candidate → certified`, manteniendo versión y baseline exactas.

## Capability truth

- cada card muestra `DEMO`;
- escenarios, datos y resultados son ficticios;
- no hay carga de expedientes o información real;
- no se presenta output como asesoría jurídica;
- Contract Control no es un CLM/SaaS autónomo;
- Regulatory Control no garantiza permisos ni cobertura automática universal;
- AI Governance 360 no sustituye auditoría técnica, pentesting, seguridad o evaluación científica;
- Legal Desk no implica bolsa ilimitada, LU, SLA, volumen o canales estándar;
- Meridiano Counsel permanece fuera de la oferta pública;
- portal/auth/CRM/pagos/firma/agenda/upload continúan fuera de capability productiva;
- no existe decisión jurídica autónoma;
- no se publicaron tarifas nuevas.

## Capas preservadas

v7.3 preserva íntegramente:

- v7.2 Buying Clarity;
- v7.1 Commercial Clarity;
- v7.0 Legal Intelligence;
- v6.4 Fit & Scope Clarity;
- v6.3 Engagement Clarity;
- v6.2 Search Discovery;
- v6.1 Measurement privacy-first;
- v6.0 Experience System.

## Cierre certified

El cierre documental cambia únicamente metadata y memoria:

- `version.json` → `github-pages-production-legal-intelligence-demo-certified`;
- `assets/data/v7/legal-intelligence-demo-v73.json` → `status: certified`;
- README y memoria canónica actualizados;
- este documento de release.

No modifica HTML, CSS, catálogos, materializadores, validators funcionales, E2E, workflows ni capabilities.

La release queda definitivamente cerrada cuando este propio cierre supere nuevamente todos los gates, se fusione con SHA protegido y la cadena productiva termine otra vez con `main == stable` y `stable/version.json` en canal production-certified.

## Siguiente frente

La siguiente ola no debe ampliar capacidades por intuición. Debe utilizar las 16 fichas comprables y el Centro Demo ya certificado para obtener evidencia comercial real sobre qué ofertas generan mayor interés, qué recorridos convierten y qué implementación tecnológica merece priorizarse.
