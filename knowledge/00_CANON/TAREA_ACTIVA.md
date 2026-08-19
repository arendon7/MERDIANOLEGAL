# Meridiano Legal — Tarea activa

Actualizado: 2026-08-19.

## Frente vigente

**v7.1.0 — Commercial Clarity / cierre certified.**

Rama: `docs/v710-certified-closure`.

Objetivo: cerrar documentalmente la release ya publicada como candidate, sin modificar HTML, CSS, catálogos, materializadores, validators funcionales, E2E, workflows ni capabilities.

Canal objetivo: `github-pages-production-commercial-clarity-certified`.

## Estado previo al cierre

- Release certificada de partida: **v7.0.0 — Meridiano Legal Intelligence**.
- Baseline de apertura funcional v7.1: `e5dc22e33c46a1b4fc2ebc9a01ab33444b935eb6`.
- Candidate funcional final: `12c8145dc8b6a3901217eb3d5793e210bfe06486`.
- PR funcional #170: fusionado con expected head SHA.
- Merge funcional: `f01c5163e2c70012218c7d369bfb68180db04ed7`.
- Candidate formal 7.1.0: `8f0a3c2e016b6bc1aab92922f418965e57cb06c3`.
- Candidate #171: 9/9 workflows aplicables PASS.
- Merge candidate: `5185e5c1aed4e3ed23074a41318e446fbb3a741d`.
- Builder/snapshot productivo: `8b13ff120cceddc9c9913892416046efb7368572`.
- Antes de abrir este cierre: `main == stable == 8b13ff120cceddc9c9913892416046efb7368572`.
- `stable` fue promovido automáticamente después de quality, deploy, live smoke, Browser/axe y Lighthouse; no se movió manualmente.

## Resultado que se certifica

v7.1 aplica profundidad progresiva en Home + hub:

**situación → forma de intervención → capacidad concreta → resultado → profundidad jurídica de respaldo**.

Cuatro formas de intervención:

1. **Diagnosticar** — Legal AI Diagnostic, auditorías y diagnósticos focales.
2. **Implementar** — productos cerrados, Legal AI Transformation, AI Governance 360, Contract Control y Regulatory Control.
3. **Operar** — Dirección Jurídica Externa, Meridiano Legal Desk y modalidades gestionadas expresamente pactadas.
4. **Construir** — Legal Engineering Studio cuando el problema requiere una solución jurídica-tecnológica específica.

Capacidades visibles:

- Contract Control;
- AI Governance 360;
- Regulatory Control;
- Meridiano Legal Desk.

Legal Engineering permanece visible en **Construir** y no se duplica como quinta capacidad instalada.

## Capability truth preservado

- Meridiano Legal permanece como marca madre;
- Legal Intelligence continúa como capa transversal, no catálogo paralelo;
- se conservan seis rutas públicas y 8 productos + 8 servicios canónicos;
- Contract Control y Regulatory Control no son SaaS autónomos;
- Legal Desk no es una bolsa de horas indefinida ni simple acceso a software;
- AI Governance 360 no sustituye seguridad, auditorías técnicas o evaluación científica;
- Legal Engineering solo incorpora desarrollo, integraciones, interfaces de IA o automatización cuando se pactan expresamente;
- no existe monitoreo automático universal implícito;
- portal, auth, CRM, pagos, firma, agenda y upload continúan fuera de capability productiva;
- Meridiano Counsel continúa fuera de la oferta pública;
- no se introducen tarifas nuevas.

## Boundary exacto del cierre

El cierre debe contener únicamente siete fuentes:

1. `version.json` — candidate → canal certified.
2. `assets/data/v7/home-commercial-clarity-v71.json` — `release-candidate` → `certified`.
3. `README.md`.
4. `RELEASE-v7.1.md`.
5. `knowledge/00_CANON/CONTEXTO_RAPIDO.md`.
6. `knowledge/00_CANON/ESTADO_ACTUAL.md`.
7. `knowledge/00_CANON/TAREA_ACTIVA.md`.

No modificar funcionalidad pública en este PR.

## Gate del cierre

Antes del merge:

1. comprobar boundary exacto de siete archivos;
2. fijar un SHA final;
3. exigir todos los workflows aplicables verdes sobre ese mismo SHA;
4. no reutilizar como sustituto la certificación del candidate #171;
5. marcar ready únicamente después de same-SHA verde;
6. fusionar con `expected_head_sha`.

Después del merge:

1. Builder canónico debe sincronizar versión/metadata sin drift funcional;
2. Pages quality debe pasar;
3. deploy debe pasar;
4. live smoke debe pasar;
5. Browser E2E/axe desplegado debe pasar;
6. Lighthouse debe pasar;
7. snapshot debe mover `stable` automáticamente;
8. comprobar `main == stable`;
9. comprobar `stable/version.json` = `7.1.0` + `github-pages-production-commercial-clarity-certified`.

**No mover `stable` manualmente.**

## Criterio de cierre definitivo

Cuando los nueve puntos post-merge se cumplan, **v7.1.0 — Commercial Clarity** queda completamente cerrada y certificada.

## Siguiente ola, fuera de este cierre

Abrir un frente independiente de **Buying Clarity** para fichas profundas y Centro Demo.

Objetivo: hacer más explícitos cantidades, entregables, duración, requisitos, continuidad y forma de contratación usando exclusivamente los catálogos canónicos. No introducir tarifas hasta contar con pricing truth aprobado.
