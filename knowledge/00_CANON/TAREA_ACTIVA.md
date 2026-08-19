# Meridiano Legal — Tarea activa

Actualizado: 2026-08-18.

## Frente vigente

**v7.1 — Commercial Clarity / profundidad progresiva de Home y hub de Soluciones.**

Rama: `feat/v710-commercial-clarity`

PR: `#170` — draft.

## Baseline

- `main`: v7.0.0 certificada;
- baseline de apertura: `e5dc22e33c46a1b4fc2ebc9a01ab33444b935eb6`;
- Meridiano Legal permanece como marca madre;
- Meridiano Legal Intelligence permanece como capa transversal;
- se conservan seis rutas públicas y los 8 productos + 8 servicios canónicos;
- `Meridiano Counsel` continúa fuera de la oferta pública.

## Problema observable

La v7.0 mejoró arquitectura y redujo carga cognitiva, pero dejó la Home demasiado condensada para comprensión comercial. El visitante reconoce una lógica de intervención, pero debe navegar demasiado para entender qué puede contratar, qué capacidades concretas existen y qué puede quedar funcionando después.

## Hipótesis

Aplicar profundidad progresiva: **situación → forma de intervención → capacidad concreta → resultado → profundidad jurídica de respaldo**. Recuperar sustancia sin regresar a acumulación de tarjetas, taxonomías o claims tecnológicos.

## Arquitectura consolidada v7.1

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

Legal Engineering no se repite como quinta capacidad instalada: permanece claramente visible en **Construir**.

## Consolidación de densidad

El prototipo absorbe y retira de la lectura principal dos bloques genéricos de v7.0:

- `v6-outcomes`;
- `v6-home-method`.

El método no desaparece: sigue resumido en el artifact del hero y desarrollado en firma/experiencia. El contrato histórico de resultado se conserva reutilizando como título del bloque concreto de capacidades:

**“El trabajo jurídico debe dejar algo que la organización pueda usar, ejecutar y verificar.”**

Así se preserva continuidad semántica sin reintroducir contenido redundante.

## Fuentes v7.1

- `knowledge/20_DESIGN/HOME-COMMERCIAL-CLARITY-v71.md`;
- `assets/data/v7/home-commercial-clarity-v71.json`.

El materializador y validador de discovery prefieren v7.1 cuando el contrato existe y conservan fallback v7.0.

## Capability truth

- Contract Control y Regulatory Control no son SaaS autónomos;
- Legal Desk es capacidad jurídica gestionada dentro de perímetro, canales, QA, capacidad y SLA pactados cuando correspondan;
- AI Governance 360 no sustituye auditorías técnicas, seguridad o evaluación científica del modelo;
- Legal Engineering solo incluye desarrollo, integraciones, agentes, interfaces o automatización cuando el alcance técnico y jurídico lo establece expresamente;
- no existe promesa de monitoreo automático universal.

## No objetivos

- no crear séptima ruta ni segundo catálogo;
- no modificar todavía los 16 catálogos jurídicos;
- no publicar nuevas tarifas;
- no prometer portal, CLM/SaaS, CRM, pagos, firma, agenda o upload;
- no publicar Meridiano Counsel;
- no inventar clientes, resultados o credenciales;
- no degradar accesibilidad, responsive, performance, SEO o funnel.

## Criterio de aceptación

Sin abrir fichas profundas, el usuario debe poder explicar:

1. dónde encaja su situación;
2. la diferencia entre diagnosticar, implementar, operar y construir;
3. qué son Contract Control, AI Governance 360, Regulatory Control y Legal Desk;
4. que Legal Engineering puede construir tecnología únicamente dentro de alcance pactado;
5. qué capacidades no equivalen a SaaS autónomo o monitoreo universal;
6. qué puede quedar funcionando después;
7. cómo pasar de la necesidad a la oferta formal y al contacto.

## Estado técnico

- materialización source-driven Home + hub: implementada;
- seis rutas y capability truth: preservados;
- Search Discovery y Release Governance: verdes en iteraciones del prototipo;
- se detectó y corrigió una incompatibilidad con el contrato histórico del resultado de Home reutilizando su título en la nueva sección concreta;
- PR permanece draft hasta obtener todos los gates verdes sobre el mismo SHA final.
