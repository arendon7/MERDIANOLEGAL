# Meridiano Legal v5.20.0 — compresión de decisión en portada

Fecha: 2026-08-12.

## Objetivo

Reducir carga cognitiva en la portada sin disminuir profundidad jurídica, cobertura de oferta ni controles de conversión. La auditoría posterior a v5.19 mostró que las 16 fichas profundas ya tenían perímetro, entregables, formatos, responsabilidades, aceptación y límites suficientes; la fricción principal estaba en varios mecanismos consecutivos que pedían al prospecto decidir repetidamente cómo contratar.

## Arquitectura final

La portada queda organizada en dos decisiones consecutivas:

1. **Situación empresarial:** se conservan las seis rutas por necesidad de v5.1.
2. **Modalidad de contratación:** se ofrece una sola superficie con cinco modalidades canónicas: diagnóstico, auditoría, producto cerrado, servicio especialista y capacidad recurrente.

El estándar verificable de propuesta de v5.12 sigue visible. Los límites y alternativas de v5.14 siguen disponibles mediante `<details>` nativo. Las 16 fichas profundas permanecen intactas en alcance y contenido jurídico.

## Redundancia eliminada

Desde v5.20 la salida HTML final deja de materializar:

- el bloque separado de “Forma de contratar” v5.8 en la portada;
- la repetición independiente de recomendación v5.14;
- la sección histórica `#elegir` / “CÓMO ELEGIR”.

La compatibilidad de v5.8, v5.12, v5.14 y v5.15 se conserva mediante selectores semánticos y validadores version-aware. La redundancia no se oculta con CSS: se elimina de la composición final.

## Límites preservados

v5.20 no introduce scoring, inferencia automática de intención, cambio automático de `decision_stage`, PII adicional, almacenamiento persistente, transporte de red, backend, CRM ni automatización de WhatsApp.

Se mantienen:

- 46 páginas HTML;
- 16 fichas profundas;
- 1 formulario físico canónico;
- 37 entradas E2E;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- handoff manual y salvaguardas v5.16–v5.19.

## Implementación y PR

PR funcional **#74**: `feat(v5.20): comprimir decisión comercial en portada`.

Merge funcional inicial: `745723c0de896e9d0a7f613dd1b83e5efcaa4878`.

Cambios fuente principales:

- `version.json` → `5.20.0`;
- `scripts/apply_decision_action_v515.py` → composición final unificada;
- `decision-action-v515.css` → layout de la superficie compacta;
- `scripts/validate_decision_v58.py` → continuidad v5.8 en estado intermedio/final;
- `scripts/validate_proof_v512.py` → continuidad v5.12 en estado intermedio/final.

Release Governance del PR #74 pasó completo antes del merge.

## Incidencias de compatibilidad resueltas

### 1. Idempotencia v4.5

La primera materialización produjo correctamente v5.20, pero la segunda pasada del builder falló porque `scripts/apply_ux_v45.py` todavía exigía la sección histórica `#elegir`.

PR **#75** hizo el generador y validator v4.5 version-aware:

- hasta v5.19 conserva el contrato histórico;
- desde v5.20 no exige ni reintroduce `#elegir`;
- desde v5.20 valida la nueva superficie unificada entre Necesidades y Servicios.

Merge: `5ba9053c0e995c77bff555cbd9c37c2909814d81`.

El gate de idempotencia no se omitió ni relajó; volvió a ejecutarse y pasó.

### 2. Marcador canónico global

Después de resolver idempotencia, `scripts/validate_site.py` todavía exigía literalmente “CÓMO ELEGIR”.

PR **#76** hizo ese contrato version-aware:

- hasta v5.19 exige el marcador histórico;
- desde v5.20 exige `data-home-decision-v520="true"` y el encabezado de la nueva arquitectura;
- desde v5.20 falla si reaparecen “CÓMO ELEGIR” o `id="elegir"`.

Merge y SHA funcional final certificado: `85bdcfc9b52172e085dfa9b1df8e8d081b136233`.

Tampoco se relajó este gate; el mismo pipeline se reejecutó hasta quedar verde.

## Evidencia funcional certificada

Run final de Pages/certificación: **`31651473515`**.

SHA desplegado y promovido: **`85bdcfc9b52172e085dfa9b1df8e8d081b136233`**.

Al cierre funcional:

- `main == stable == 85bdcfc9b52172e085dfa9b1df8e8d081b136233`;
- builder e idempotencia: PASS;
- validadores históricos y contratos v5.8→v5.19: PASS;
- GitHub Pages + smoke público: PASS;
- Browser E2E + axe: 37 observados → **35 PASS / 2 SKIP / 0 FAIL / 0 RETRY**;
- tiempo reporter Browser: **85 s**;
- 7 superficies axe sin violaciones serias/críticas;
- Lighthouse: **6/6 PASS**;
- accesibilidad Lighthouse: **1.00 en las seis superficies**;
- performance: **1.00** en portada, solución IA, producto IA y demo; **0.98** en sector tecnología y perspectiva IA;
- portada: LCP **1421 ms**, CLS **0**, TBT **83 ms**;
- máximo global observado: LCP **1421 ms**, CLS **0.087**, TBT **83 ms**;
- CI hasta `stable`: **191 s**;
- baseline v5.5: **279 s**;
- mejora frente al baseline: **31.5%**;
- cobertura reducida: **no**;
- budgets relajados: **no**;
- release-health: PASS;
- promoción de `stable`: PASS.

## Artefactos finales

Run `31651473515`:

- Lighthouse `9162821238`, `sha256:681cd883c725e44c26b65c2f9b0c6a276c8668096266618dfe36c75567a3b3c0`;
- CI `9162836693`, `sha256:1862dea240db5ea3c491afc0d8505d51d5bed74dff6cf081a255a8ab1f6564af`;
- release-health `9162837264`, `sha256:00c1e747dc887dc37d4daae63fd4fdd5a279d2e813745312802277931b60c323`;
- Pages `9162779134`, `sha256:31cea6e7fd74a2bdb73543660c6a49ec6d9838341f6fb98bfd604f8abc5d852a`.

## Graphify / procedencia

Antes del cierre documental, `knowledge/graphify-live` reportó:

- `version = 5.20.0`;
- `source_commit = 85bdcfc9b52172e085dfa9b1df8e8d081b136233`;
- 588 nodos;
- 948 relaciones;
- 94 notas wiki.

El cierre documental puede mover `main` sin modificar el snapshot funcional `stable`; la frescura final se comprueba contra el run Graphify posterior al merge documental.

## Condición de cierre

v5.20 queda funcionalmente certificada. El cierre formal se completa al integrar esta documentación, verificar Graphify fresco sobre el último `main` documental y dejar explícito que no existe una v5.21 abierta dentro de este ciclo.
