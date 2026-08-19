# Meridiano Legal — Contexto rápido

Actualizado: 2026-08-19.

Use esta nota para orientarse antes de abrir fuentes. `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md` mandan ante cualquier diferencia.

## Proyecto

Sitio público y centro demostrativo de Meridiano Legal, static-first sobre GitHub Pages.

Arquitectura pública preservada:

- 46 superficies HTML;
- 16 fichas profundas: 8 productos + 8 servicios;
- seis rutas públicas de solución;
- un único formulario físico canónico;
- Meridiano Legal como marca madre;
- Meridiano Legal Intelligence como capa transversal, no catálogo paralelo.

## Release vigente

**v7.2.0 — Buying Clarity**.

- Functional SHA: `5e9b04487b92b0e47327d1f61880d2a4ac48c629` — gates funcionales PASS.
- Merge funcional #174: `0b8211ce9aeecda737bec0a11af50496cc6aeccf`.
- Candidate formal SHA: `f11329f40cfcd7d097ff16019dcb462dd97acc70` — 10/10 gates PASS.
- Merge candidate #175: `a5d14d34cd73aa2772a66adfd6d5ea0f07c34a2e`.
- Builder/snapshot candidate: `356f755db67a678142769b3a80ee69837679648d`.
- Pages quality → deploy → live smoke → Browser/axe + Lighthouse: PASS.
- `stable` fue promovido automáticamente a `356f755db67a678142769b3a80ee69837679648d`.
- Canal de cierre: `github-pages-production-buying-clarity-certified`.

## Qué añade v7.2

Cada una de las 16 fichas incorpora un **Resumen de contratación** source-driven inmediatamente después del hero. Hace visible modalidad, duración, destinatario, principales cantidades del perímetro, entregables, requisitos, criterios de cierre y rutas de ampliación/continuidad.

Fuente exclusiva:

- `catalog-products-v41/*.json`;
- `catalog-services-v42/*.json`.

No añade precios, entregables o capacidades nuevas.

## Capas preservadas

- v7.1 Commercial Clarity: Home/hub con profundidad progresiva y cuatro formas de intervención.
- v7.0 Legal Intelligence: Diagnostic, Transformation, Legal Desk, Contract Control, Regulatory Control, AI Governance 360 y Legal Engineering Studio.
- v6.4 Fit & Scope Clarity.
- v6.3 Engagement Clarity.
- v6.2 Search Discovery.
- v6.1 Measurement privacy-first.
- v6.0 Experience System.

## Capability truth

- Contract Control y Regulatory Control: capacidades de implementación/operación, no SaaS autónomos.
- Legal Desk: managed legal service sujeto a perímetro, capacidad, canales y SLA pactados.
- AI Governance 360: no reemplaza seguridad, auditoría técnica o evaluación científica.
- Legal Engineering: tecnología solo cuando se pacta expresamente.
- Meridiano Counsel: futuro/no oferta pública.
- Portal/auth/CRM/pagos/firma/agenda/upload: no productivos.
- No monitoreo automático universal.
- No tarifas nuevas sin pricing truth aprobado.

## Source of truth

- `main`: verdad técnica/documental vigente.
- `stable`: snapshot certificado.
- catálogos v4.1/v4.2: verdad jurídica/comercial.
- `assets/data/v7/`: contratos de las capas v7.
- `knowledge/00_CANON/`: memoria operativa.

## Frente siguiente

Una vez certificado este cierre documental, abrir **Centro Demo — Legal Intelligence Scenarios** como ola independiente. Debe mostrar con datos ficticios Legal AI Transformation, Contract Control, AI Governance 360, Regulatory Control y Meridiano Legal Desk; todo marcado DEMO y sin presentar Meridiano Empresas como portal productivo.

## Invariantes

No inventar clientes, testimonios, resultados, precios, capacidades tecnológicas o certificaciones; no reducir E2E/axe ni relajar Lighthouse; conservar seis rutas, un formulario canónico y `stable` únicamente después de gates productivos verdes.
