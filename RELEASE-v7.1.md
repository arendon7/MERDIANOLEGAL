# Meridiano Legal — Release v7.1.0

Fecha: 2026-08-19.

## Resultado

**v7.1.0 — Commercial Clarity** mejora la comprensión comercial de la capa pública de **Meridiano Legal Intelligence** sin crear nuevas rutas, productos, servicios ni capacidades ficticias.

La release conserva las seis rutas públicas y los 8 productos + 8 servicios canónicos. Los catálogos continúan gobernando alcance, entregables, tiempos, honorarios, responsabilidades y límites.

## Problema resuelto

v7.0 hizo visible la arquitectura de Legal Intelligence, pero la Home quedó demasiado condensada para que un comprador entendiera, sin navegación adicional, cómo podía intervenir Meridiano y qué podía quedar funcionando después.

v7.1 aplica una secuencia de profundidad progresiva:

**situación → forma de intervención → capacidad concreta → resultado → profundidad jurídica de respaldo**.

## Cuatro formas de intervención

1. **Diagnosticar** — Legal AI Diagnostic, auditorías y diagnósticos focales.
2. **Implementar** — productos cerrados, Legal AI Transformation, AI Governance 360, Contract Control y Regulatory Control.
3. **Operar** — Dirección Jurídica Externa, Meridiano Legal Desk y modalidades gestionadas expresamente pactadas.
4. **Construir** — Legal Engineering Studio cuando el caso exige una solución jurídica-tecnológica específica.

## Capacidades visibles

La Home explica cuatro capacidades que pueden quedar operando dentro de un alcance contratado:

- Contract Control;
- AI Governance 360;
- Regulatory Control;
- Meridiano Legal Desk.

Legal Engineering Studio permanece visible en **Construir** y no se duplica como una quinta capacidad instalada.

## Densidad, lenguaje y diseño

- `v6-outcomes` y `v6-home-method` fueron absorbidos de la lectura principal para evitar acumulación de bloques genéricos.
- Se conserva el mensaje: **“El trabajo jurídico debe dejar algo que la organización pueda usar, ejecutar y verificar.”**
- El lenguaje operativo reduce anglicismos no esenciales sin alterar nombres propios de capacidades.
- La grilla de intervención usa 4 columnas en desktop, 2×2 en tablet y apilado móvil.
- El contraste de las capacidades sobre superficie clara fue corregido de forma scoped.
- La regresión E2E histórica fue actualizada para validar la arquitectura consolidada, no una sección eliminada deliberadamente.

## Source-driven

Fuentes principales:

- `assets/data/v7/home-commercial-clarity-v71.json`;
- `knowledge/20_DESIGN/HOME-COMMERCIAL-CLARITY-v71.md`;
- `scripts/apply_legal_intelligence_discovery_v70.py`;
- `scripts/validate_legal_intelligence_discovery_v70.py`;
- `tests/e2e/integral-visual-v526.spec.mjs`.

Home y hub de Soluciones se materializan desde el contrato. El materializador conserva fallback v7.0 y la segunda pasada es idempotente.

## Capability truth preservado

- Meridiano Legal sigue siendo marca madre y Legal Intelligence una capa transversal.
- No existe una séptima ruta ni un segundo catálogo.
- Contract Control y Regulatory Control no se presentan como SaaS autónomos.
- Meridiano Legal Desk es capacidad jurídica gestionada, no una bolsa de horas indefinida ni simple acceso a software.
- AI Governance 360 no sustituye seguridad, auditorías técnicas o evaluación científica.
- Legal Engineering solo incorpora desarrollo, integraciones, interfaces de IA o automatización cuando se pactan expresamente.
- No existe promesa de monitoreo automático universal.
- Portal, auth, CRM, pagos, firma, agenda y upload continúan fuera de capability productiva.
- `Meridiano Counsel` permanece fuera de la oferta pública.
- No se publicaron nuevas tarifas.

## Evidencia funcional

### Cambio funcional #170

- Baseline: `e5dc22e33c46a1b4fc2ebc9a01ab33444b935eb6`.
- Candidate funcional final: `12c8145dc8b6a3901217eb3d5793e210bfe06486`.
- Gates aplicables sobre el mismo SHA: PASS.
- PR #170 fusionado con `expected_head_sha`.
- Merge funcional: `f01c5163e2c70012218c7d369bfb68180db04ed7`.
- `stable` fue promovido automáticamente a ese merge después de la cadena productiva oficial.

### Release candidate #171

- Candidate formal 7.1.0: `8f0a3c2e016b6bc1aab92922f418965e57cb06c3`.
- 9/9 workflows aplicables: PASS:
  - Candidate Validation;
  - Canonical Builder Equivalence + idempotencia;
  - Fit & Scope Clarity;
  - Engagement Clarity;
  - Search Discovery Readiness;
  - Release Governance;
  - Graphify;
  - Browser E2E / axe;
  - Measurement Readiness / Browser E2E.
- Browser y Measurement tuvieron una cancelación externa inicial; ambos se reejecutaron sobre el mismo SHA sin cambios de código y terminaron en `success`.
- PR #171 fusionado con `expected_head_sha`.
- Merge candidate: `5185e5c1aed4e3ed23074a41318e446fbb3a741d`.
- Builder canónico: `8b13ff120cceddc9c9913892416046efb7368572`.
- Pages completó quality, deploy, live smoke, Browser/axe y Lighthouse.
- `stable` fue promovido automáticamente a `8b13ff120cceddc9c9913892416046efb7368572`.
- Antes de abrir este cierre: `main == stable == 8b13ff120cceddc9c9913892416046efb7368572`.

## Cierre certified

Este cierre cambia únicamente metadata/documentación:

- `version.json`: canal candidate → `github-pages-production-commercial-clarity-certified`;
- contrato v7.1: `release-candidate` → `certified`;
- README;
- esta nota de release;
- `CONTEXTO_RAPIDO.md`;
- `ESTADO_ACTUAL.md`;
- `TAREA_ACTIVA.md`.

No modifica HTML, CSS, catálogos, materializadores, validators funcionales, E2E, workflows ni capabilities.

El cierre solo queda definitivo después de superar nuevamente sus gates, fusionarse con SHA protegido y completar otra vez Builder → Pages → live smoke → Browser/axe → Lighthouse → snapshot con `main == stable` y `stable/version.json` en canal certificado.

## Próxima ola

Después de cerrar v7.1, el siguiente frente recomendado es **Buying Clarity** para fichas profundas y Centro Demo: hacer más explícitos cantidades, entregables, duración, requisitos, continuidad y forma de contratación usando exclusivamente truth canónico. No introducir tarifas hasta contar con pricing truth aprobado.
