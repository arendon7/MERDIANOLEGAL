# Meridiano Legal — Tarea activa

Actualizado: 2026-08-19.

## Frente vigente

**v7.1.0 — Commercial Clarity / release candidate.**

Rama: `feat/v710-commercial-clarity`

PR: `#170` — draft hasta certificación same-SHA final.

Canal candidate: `github-pages-commercial-clarity-candidate`.

## Baseline certificada

- release pública de partida: **v7.0.0 — Meridiano Legal Intelligence**;
- baseline de apertura: `e5dc22e33c46a1b4fc2ebc9a01ab33444b935eb6`;
- al abrir este candidate, `main == stable` en esa baseline;
- Meridiano Legal permanece como marca madre;
- Meridiano Legal Intelligence permanece como capa transversal;
- se conservan seis rutas públicas y los 8 productos + 8 servicios canónicos;
- `Meridiano Counsel` continúa fuera de la oferta pública.

## Problema que resuelve v7.1

La v7.0 resolvió la arquitectura de Legal Intelligence, pero dejó la Home demasiado condensada para comprensión comercial. El visitante podía reconocer la lógica general, aunque todavía debía navegar demasiado para entender qué puede contratar, qué capacidades concretas existen, qué diferencia hay entre diagnóstico, implementación, operación e ingeniería y qué puede quedar funcionando después.

v7.1 aplica profundidad progresiva:

**situación → forma de intervención → capacidad concreta → resultado → profundidad jurídica de respaldo**.

## Arquitectura comercial v7.1

La Home conserva hero y seis situaciones. Después muestra una única capa Legal Intelligence con cuatro formas de intervención:

1. **Diagnosticar** — Legal AI Diagnostic, auditorías y diagnósticos focales.
2. **Implementar** — productos cerrados, Legal AI Transformation, AI Governance 360, Contract Control y Regulatory Control.
3. **Operar** — Dirección Jurídica Externa, Meridiano Legal Desk y modalidades recurrentes expresamente pactadas.
4. **Construir** — Legal Engineering Studio cuando el problema requiere una solución jurídica-tecnológica específica.

Debajo se hacen visibles cuatro capacidades que pueden quedar operando:

- Contract Control;
- AI Governance 360;
- Regulatory Control;
- Meridiano Legal Desk.

Legal Engineering permanece visible en **Construir** y no se duplica como una quinta capacidad instalada.

## Consolidación de densidad

El nuevo bloque absorbe de la lectura principal dos secciones genéricas de v7.0:

- `v6-outcomes`;
- `v6-home-method`.

El método continúa resumido en el hero y desarrollado en firma/experiencia. El contrato histórico de resultado se preserva mediante el título:

**“El trabajo jurídico debe dejar algo que la organización pueda usar, ejecutar y verificar.”**

La grilla usa cuatro columnas reales y el copy evita anglicismos operativos innecesarios sin alterar los nombres propios de las capacidades.

## Fuentes v7.1

- `knowledge/20_DESIGN/HOME-COMMERCIAL-CLARITY-v71.md`;
- `assets/data/v7/home-commercial-clarity-v71.json`;
- `scripts/apply_legal_intelligence_discovery_v70.py`;
- `scripts/validate_legal_intelligence_discovery_v70.py`;
- `tests/e2e/integral-visual-v526.spec.mjs`.

El materializador/validator prefieren v7.1 cuando existe su contrato y conservan fallback v7.0.

## Capability truth

- Contract Control y Regulatory Control no son SaaS autónomos;
- Legal Desk es capacidad jurídica gestionada dentro de perímetro, canales, control de calidad, capacidad y niveles de servicio pactados cuando correspondan;
- AI Governance 360 no sustituye auditorías técnicas, seguridad o evaluación científica del modelo;
- Legal Engineering solo incluye desarrollo, integraciones, agentes, interfaces o automatización cuando el alcance técnico y jurídico lo establece expresamente;
- no existe promesa de monitoreo automático universal;
- no se publica portal, CLM, CRM, pagos, firma, agenda o upload inexistente;
- no se alteran precios, entregables, responsabilidades o límites de los catálogos canónicos.

## Prototipo certificado antes del candidate

SHA final del prototipo:

`12c8145dc8b6a3901217eb3d5793e210bfe06486`

Ese SHA superó todos los workflows aplicables:

1. Candidate Validation — PASS.
2. Canonical Builder Equivalence — PASS.
3. Browser E2E / axe — PASS.
4. Search Discovery — PASS.
5. Release Governance — PASS.
6. Graphify — PASS.

La primera pasada del Builder volvió a quedar canónica después de materializar Home + hub desde source; el workflow temporal de materialización fue retirado y no forma parte del diff final.

## Release candidate 7.1.0

El candidate cambia únicamente metadata/fase sobre el prototipo certificado:

- `version.json`: `7.1.0` + canal `github-pages-commercial-clarity-candidate`;
- contrato v7.1: `release-candidate`;
- validator v7.1: lifecycle phase-aware `prototype → release-candidate → certified`;
- esta memoria canónica.

El cambio de fase **no modifica HTML, copy, catálogos ni capabilities**.

Después de este commit no se reutiliza la certificación del prototipo. El SHA final candidate debe volver a superar todos los workflows aplicables sobre la misma evidencia.

## Promoción

Solo después de candidate same-SHA verde:

1. verificar head intacto y `main` sin carrera;
2. marcar PR #170 ready;
3. fusionar con `expected_head_sha`;
4. dejar que Builder sincronice la versión pública canónica cuando corresponda;
5. exigir Pages quality y deploy;
6. exigir live smoke;
7. exigir Browser/axe desplegado;
8. exigir Lighthouse;
9. permitir que `stable` se mueva automáticamente.

**No mover `stable` manualmente.**

## Cierre posterior

Una vez la release funcional v7.1 esté en `main == stable`, abrir un cierre documental separado para:

- cambiar `candidate → github-pages-production-commercial-clarity-certified`;
- cambiar contrato v7.1 `release-candidate → certified`;
- publicar `RELEASE-v7.1.md`;
- actualizar README y memoria canónica;
- registrar candidate, merge, builder/Pages y snapshot final;
- volver a pasar la certificación completa del cierre.

## Siguiente ola, fuera de este PR

Después de cerrar v7.1, desarrollar por separado **Buying Clarity** para las fichas profundas y el Centro Demo:

- Legal AI Transformation;
- Contract Control;
- AI Governance 360;
- Regulatory Control;
- demo específico de esas capacidades.

Esa segunda ola debe derivar cantidades, entregables, duración, requisitos y continuidad exclusivamente de los catálogos canónicos. No introduce tarifas hasta que exista truth de pricing aprobado.
