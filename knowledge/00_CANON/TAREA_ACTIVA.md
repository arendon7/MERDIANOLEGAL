# Meridiano Legal — Tarea activa

Actualizado: 2026-08-19.

## Frente vigente

**v7.1.0 — Commercial Clarity / release candidate.**

Rama: `feat/v710-commercial-clarity`

PR candidate: **#171** — draft hasta certificación same-SHA final.

PR funcional #170: **fusionado** en `main` mediante `f01c5163e2c70012218c7d369bfb68180db04ed7`.

Canal candidate: `github-pages-commercial-clarity-candidate`.

## Baseline

- release certificada de partida: **v7.0.0 — Meridiano Legal Intelligence**;
- baseline de apertura funcional: `e5dc22e33c46a1b4fc2ebc9a01ab33444b935eb6`;
- candidate funcional pre-merge: `12c8145dc8b6a3901217eb3d5793e210bfe06486`;
- merge funcional #170: `f01c5163e2c70012218c7d369bfb68180db04ed7`;
- Meridiano Legal permanece como marca madre;
- Meridiano Legal Intelligence permanece como capa transversal;
- se conservan seis rutas públicas y los 8 productos + 8 servicios canónicos;
- `Meridiano Counsel` continúa fuera de la oferta pública.

## Problema que resuelve v7.1

v7.0 resolvió la arquitectura de Legal Intelligence, pero la Home quedó demasiado condensada para comprensión comercial. v7.1 aplica profundidad progresiva:

**situación → forma de intervención → capacidad concreta → resultado → profundidad jurídica de respaldo**.

## Arquitectura comercial v7.1

La Home conserva hero y seis situaciones. Después muestra una única capa Legal Intelligence con cuatro formas de intervención:

1. **Diagnosticar** — Legal AI Diagnostic, auditorías y diagnósticos focales.
2. **Implementar** — productos cerrados, Legal AI Transformation, AI Governance 360, Contract Control y Regulatory Control.
3. **Operar** — Dirección Jurídica Externa, Meridiano Legal Desk y modalidades gestionadas expresamente pactadas.
4. **Construir** — Legal Engineering Studio cuando el problema requiere una solución jurídica-tecnológica específica.

Debajo se hacen visibles cuatro capacidades que pueden quedar operando:

- Contract Control;
- AI Governance 360;
- Regulatory Control;
- Meridiano Legal Desk.

Legal Engineering permanece visible en **Construir** y no se duplica como quinta capacidad instalada.

## Consolidación de densidad y lenguaje

- `v6-outcomes` y `v6-home-method` fueron absorbidos de la lectura principal para evitar redundancia;
- el método continúa resumido en el hero y desarrollado en firma/experiencia;
- se preserva el contrato semántico: **“El trabajo jurídico debe dejar algo que la organización pueda usar, ejecutar y verificar.”**;
- grilla: 4 columnas desktop, 2×2 tablet y apilado móvil;
- contraste WCAG scoped para las capacidades sobre superficie clara;
- menor dependencia de anglicismos operativos sin alterar nombres propios de capacidades.

## Fuentes v7.1

- `knowledge/20_DESIGN/HOME-COMMERCIAL-CLARITY-v71.md`;
- `assets/data/v7/home-commercial-clarity-v71.json`;
- `scripts/apply_legal_intelligence_discovery_v70.py`;
- `scripts/validate_legal_intelligence_discovery_v70.py`;
- `tests/e2e/integral-visual-v526.spec.mjs`.

## Capability truth

- Contract Control y Regulatory Control no son SaaS autónomos;
- Legal Desk es capacidad jurídica gestionada dentro de perímetro, canales, control de calidad, capacidad y niveles de servicio pactados cuando correspondan;
- AI Governance 360 no sustituye auditorías técnicas, seguridad o evaluación científica del modelo;
- Legal Engineering solo incluye desarrollo, integraciones, agentes, interfaces o automatización cuando el alcance técnico y jurídico lo establece expresamente;
- no existe promesa de monitoreo automático universal;
- no se publica portal, CLM, CRM, pagos, firma, agenda o upload inexistente;
- no se alteran precios, entregables, responsabilidades o límites de los catálogos canónicos.

## Evidencia funcional previa

SHA funcional final antes de abrir candidate:

`12c8145dc8b6a3901217eb3d5793e210bfe06486`

Ese SHA pasó:

1. Candidate Validation.
2. Canonical Builder Equivalence + idempotencia.
3. Browser E2E / axe.
4. Search Discovery.
5. Release Governance.
6. Graphify.

PR #170 fue fusionado con expected head SHA y no se reescribió `main`.

## Release candidate 7.1.0

PR #171 cambia únicamente lifecycle/metadata sobre el prototipo funcional ya fusionado:

- `version.json`: `7.1.0` + canal `github-pages-commercial-clarity-candidate`;
- contrato v7.1: `release-candidate`;
- validator: lifecycle phase-aware `prototype → release-candidate → certified`;
- esta memoria canónica.

**No modifica HTML, copy, CSS funcional, catálogos ni capabilities.**

El SHA final de #171 debe obtener nuevamente todos los workflows aplicables verdes; no se reutiliza la certificación de #170.

## Promoción candidate

Solo después de same-SHA verde en #171:

1. verificar head intacto y ausencia de carrera con `main`;
2. marcar **PR #171** ready;
3. fusionar #171 con `expected_head_sha`;
4. dejar que Builder sincronice versión/metadata pública;
5. exigir Pages quality + deploy;
6. exigir live smoke;
7. exigir Browser/axe desplegado;
8. exigir Lighthouse;
9. permitir que `stable` se mueva automáticamente.

**No mover `stable` manualmente.**

## Cierre certified posterior

Cuando el candidate 7.1 esté publicado y `main == stable`, abrir un cierre documental separado para:

- cambiar canal `candidate → github-pages-production-commercial-clarity-certified`;
- cambiar contrato `release-candidate → certified`;
- publicar `RELEASE-v7.1.md`;
- actualizar README, `ESTADO_ACTUAL`, `CONTEXTO_RAPIDO` y `TAREA_ACTIVA`;
- registrar candidate, merge, Builder/Pages y snapshot final;
- volver a pasar la certificación completa del cierre.

## Siguiente ola, fuera de este PR

Después de cerrar v7.1, desarrollar por separado **Buying Clarity** para fichas profundas y Centro Demo, derivando cantidades, entregables, duración, requisitos y continuidad exclusivamente de los catálogos canónicos. No introducir tarifas hasta que exista truth de pricing aprobado.
