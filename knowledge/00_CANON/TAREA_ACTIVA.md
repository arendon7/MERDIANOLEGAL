# Meridiano Legal — Tarea activa

Actualizado: 2026-08-19.

## Frente vigente

**Cierre v7.1.0 — Commercial Clarity / candidate → certified.**

Rama documental: `docs/v710-release-closure`.

La mejora funcional ya fue fusionada mediante PR **#170**. Este frente no debe cambiar productos, servicios, capabilities ni arquitectura pública; únicamente consolida versión, evidencia y memoria de release después de comprobar la promoción productiva automática.

## Release funcional

- baseline de apertura v7.1: `e5dc22e33c46a1b4fc2ebc9a01ab33444b935eb6`;
- candidate funcional certificado pre-merge: `12c8145dc8b6a3901217eb3d5793e210bfe06486`;
- seis gates sobre el mismo SHA: PASS;
- PR funcional: #170;
- merge protegido por expected head SHA: `f01c5163e2c70012218c7d369bfb68180db04ed7`;
- promoción productiva de `stable`: pendiente de constatar antes de cerrar esta rama documental.

## Resultado v7.1

La Home conserva las seis situaciones de entrada y aplica profundidad progresiva:

**situación → forma de intervención → capacidad concreta → resultado → profundidad jurídica de respaldo**.

Cuatro formas de intervención:

1. **Diagnosticar** — Legal AI Diagnostic, auditorías y diagnósticos focales.
2. **Implementar** — productos cerrados, Legal AI Transformation, AI Governance 360, Contract Control y Regulatory Control.
3. **Operar** — Dirección Jurídica Externa, Meridiano Legal Desk y modalidades gestionadas expresamente pactadas.
4. **Construir** — Legal Engineering Studio cuando el caso requiere una solución jurídica-tecnológica específica.

Cuatro capacidades visibles que pueden quedar funcionando:

- Contract Control;
- AI Governance 360;
- Regulatory Control;
- Meridiano Legal Desk.

Legal Engineering permanece visible en **Construir** y no se duplica como quinta capacidad instalada.

## Refinamiento comercial

- los antiguos bloques genéricos `v6-outcomes` y `v6-home-method` fueron absorbidos para evitar acumulación;
- grilla específica: 4 columnas desktop, 2×2 tablet y apilado móvil;
- contraste WCAG corregido en la superficie clara de capacidades;
- menor dependencia de anglicismos operativos;
- hub de Soluciones explica valor y resultado antes de nomenclatura interna;
- Home y hub permanecen source-driven mediante `assets/data/v7/home-commercial-clarity-v71.json`.

## Capability truth preservado

- seis rutas públicas intactas;
- 8 productos + 8 servicios canónicos intactos;
- Contract Control y Regulatory Control no son SaaS autónomos;
- Legal Desk no es una bolsa de horas indefinida ni acceso a software;
- AI Governance 360 no sustituye seguridad, controles técnicos o evaluación científica;
- Legal Engineering incluye desarrollo, integraciones, interfaces de IA o automatización únicamente cuando el alcance lo pacta expresamente;
- no existe promesa de monitoreo automático universal;
- Meridiano Counsel continúa fuera de la oferta pública.

## Evidencia pre-merge

Sobre `12c8145dc8b6a3901217eb3d5793e210bfe06486`:

- Candidate Validation: PASS;
- Canonical Builder Equivalence + idempotencia: PASS;
- Browser E2E / axe en Chromium y WebKit: PASS;
- Search Discovery Readiness: PASS;
- Release Governance Health: PASS;
- Graphify: PASS.

No se redujo cobertura, no se relajaron budgets y no se eliminaron pruebas para aprobar la release.

## Criterio de cierre

Este frente queda cerrado únicamente cuando:

1. la release funcional fusionada complete la cadena productiva oficial y `stable` se promueva automáticamente;
2. la documentación de v7.1.0 atraviese sus gates pre-merge;
3. el cierre documental se fusione con SHA protegido;
4. Builder → Pages → live smoke → Browser/axe → Lighthouse → snapshot vuelvan a pasar;
5. `main == stable` en el commit canónico de cierre;
6. `version.json` y la memoria canónica identifiquen **7.1.0 — Commercial Clarity**.

## No objetivos del cierre

- no alterar HTML funcional salvo sincronización automática de versión/metadata;
- no cambiar los 16 catálogos;
- no introducir nuevas rutas, precios o capabilities;
- no mover `stable` manualmente;
- no certificar producción antes de la evidencia fail-closed del pipeline oficial.
