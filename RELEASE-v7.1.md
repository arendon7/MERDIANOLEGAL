# Meridiano Legal — Release v7.1.0

Fecha funcional: 2026-08-19.

## Resultado

**v7.1.0 — Commercial Clarity** refina la capa pública de **Meridiano Legal Intelligence** para que un visitante pueda entender con menos navegación qué problema puede resolver, cómo puede intervenir Meridiano, qué capacidades concretas existen y qué puede quedar funcionando después.

No crea productos ni servicios nuevos. Los 8 productos y 8 servicios canónicos continúan gobernando alcance jurídico, entregables, tiempos, honorarios, responsabilidades y límites.

## Problema resuelto

v7.0 estableció la arquitectura de Legal Intelligence, pero la Home quedó demasiado condensada para comprensión comercial. v7.1 aplica profundidad progresiva:

**situación → forma de intervención → capacidad concreta → resultado → profundidad jurídica de respaldo**.

La mejora recupera sustancia sin volver a una Home acumulativa ni crear un segundo catálogo.

## Arquitectura publicada

La Home conserva las seis rutas por situación y concentra cuatro formas de intervención:

1. **Diagnosticar** — Legal AI Diagnostic, auditorías y diagnósticos focales.
2. **Implementar** — productos cerrados, Legal AI Transformation, AI Governance 360, Contract Control y Regulatory Control.
3. **Operar** — Dirección Jurídica Externa, Meridiano Legal Desk y modalidades gestionadas expresamente pactadas.
4. **Construir** — Legal Engineering Studio cuando el caso requiere una solución jurídica-tecnológica específica.

Debajo se explican cuatro capacidades que pueden quedar funcionando:

- Contract Control;
- AI Governance 360;
- Regulatory Control;
- Meridiano Legal Desk.

Legal Engineering Studio se mantiene claramente visible en **Construir** sin duplicarlo como una quinta capacidad instalada.

## Densidad y lenguaje

v7.1 absorbe de la lectura principal dos bloques genéricos de v7.0:

- `v6-outcomes`;
- `v6-home-method`.

El método sigue resumido en el hero y desarrollado en firma/experiencia. El contrato histórico de resultado permanece visible mediante el encabezado:

**“El trabajo jurídico debe dejar algo que la organización pueda usar, ejecutar y verificar.”**

La revisión final también redujo anglicismos no esenciales y sustituyó expresiones internas por lenguaje comprensible para gerencia: modalidades gestionadas, mejoras de rápida ejecución, recepción estructurada, flujos de trabajo, criterios de actuación y control de calidad.

## Diseño y accesibilidad

- cuatro formas de intervención ocupan una grilla real de 4 columnas en desktop;
- adaptación 2×2 en tablet;
- apilado móvil preservado;
- contraste de las capacidades sobre superficie clara corregido de forma scoped;
- regresión visual histórica actualizada para validar la arquitectura consolidada sin exigir bloques eliminados deliberadamente.

## Source-driven

Fuentes principales de v7.1:

- `assets/data/v7/home-commercial-clarity-v71.json`;
- `knowledge/20_DESIGN/HOME-COMMERCIAL-CLARITY-v71.md`;
- `scripts/apply_legal_intelligence_discovery_v70.py`;
- `scripts/validate_legal_intelligence_discovery_v70.py`.

Home y hub de Soluciones se materializan desde el contrato. El materializador conserva fallback v7.0 y la segunda pasada es idempotente.

## Capability truth

Se preservan límites fail-closed:

- no séptima ruta ni catálogo paralelo;
- Contract Control y Regulatory Control no son SaaS autónomos;
- Legal Desk es capacidad jurídica gestionada, no una bolsa de horas indefinida ni simple acceso a software;
- AI Governance 360 no sustituye seguridad, controles técnicos o evaluación científica;
- Legal Engineering solo incorpora desarrollo, integraciones, interfaces de IA o automatización cuando se pactan expresamente;
- no existe promesa de monitoreo automático universal;
- Meridiano Counsel continúa fuera de la oferta pública;
- no se publicaron nuevas tarifas ni se alteró el formulario canónico.

## Candidate y merge funcional

Candidate final pre-merge:

`12c8145dc8b6a3901217eb3d5793e210bfe06486`

Ese mismo SHA superó:

1. Candidate Validation.
2. Canonical Builder Equivalence + idempotencia.
3. Browser E2E / axe en Chromium y WebKit.
4. Search Discovery Readiness.
5. Release Governance Health.
6. Graphify.

- PR funcional: **#170**.
- Merge protegido por expected head SHA: `f01c5163e2c70012218c7d369bfb68180db04ed7`.
- Cobertura reducida: no.
- Budgets relajados: no.
- Tests eliminados para aprobar: no.

## Promoción productiva

La evidencia definitiva de publicación funcional no se declara por el merge. `pages.yml` exige quality, deploy, live smoke, Browser/axe y Lighthouse antes de mover automáticamente `stable`.

**Estado al abrir este cierre documental:** promoción productiva del merge funcional todavía pendiente de constatar mediante el movimiento automático de `stable`.

Este apartado debe actualizarse antes del merge del cierre documental con el SHA realmente promovido.

## Cierre documental

La release queda totalmente cerrada cuando este propio cierre:

1. actualice la versión pública a 7.1.0;
2. atraviese nuevamente los gates pre-merge;
3. se fusione con SHA protegido;
4. complete Builder → Pages → live smoke → Browser/axe → Lighthouse → snapshot;
5. termine con `main == stable` en el commit canónico resultante.

Canal propuesto de certificación:

`github-pages-production-commercial-clarity-certified`
