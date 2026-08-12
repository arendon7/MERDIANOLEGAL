# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-12.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot certificado: `stable`.
- Versión declarada en este cierre: `5.12.0`.
- Evidencia funcional v5.12 previa al cierre documental: run `31562692907`, SHA `f8c4d1abc38929040f1ce67b04a2c2c4193c3690`.

Los SHA actuales de `main` y `stable` deben consultarse dinámicamente. Las notas documentan hitos; refs, Pages y gates son la autoridad.

## Estado funcional

**La implementación funcional v5.12 está certificada. El commit documental que declara 5.12.0 debe volver a atravesar la certificación pública completa antes de considerar cerrada la release definitiva.**

## v5.12 — Modalidad y prueba verificable

La portada ofrece cinco criterios de modalidad: diagnóstico, auditoría, producto cerrado, servicio especializado y acompañamiento recurrente.

Las 16 fichas profundas incorporan una prueba de trabajo derivada de la fuente jurídica, con método, entregables, formatos y criterios de aceptación/cierre. No se declaran clientes, testimonios, casos de éxito, métricas ni resultados no demostrables.

Implementación: `proof-v512.css`, `scripts/apply_proof_v512.py`, `scripts/validate_proof_v512.py`.

## Accesibilidad

El primer candidato v5.12 fue bloqueado por axe por contraste insuficiente en el título del panel oscuro de portada. PR #45 corrigió el color y añadió un guardrail estático. El candidato corregido `f8c4d1abc38929040f1ce67b04a2c2c4193c3690` pasó posteriormente axe y todos los demás gates.

## Evidencia funcional v5.12

Run `31562692907`:

- Browser E2E: 37 entradas, 35 aprobadas, 2 omitidas, 0 fallos, 0 retries;
- axe: 7 superficies sin violaciones serias/críticas;
- Lighthouse: 6/6 dentro de presupuesto;
- portada: performance 1.00, a11y 0.97, LCP 1263 ms, CLS 0, TBT 2 ms, 88,599 B;
- solución IA: 1.00 / 1.00, LCP 908 ms, 23,343 B;
- producto IA: 1.00 / 1.00, LCP 908 ms, 37,309 B;
- sector tecnología: 0.98 / 1.00, LCP 960 ms, CLS 0.087, 24,400 B;
- perspectiva IA: 0.98 / 1.00, LCP 906 ms, CLS 0.087, 26,003 B;
- demo: 1.00 / 1.00, LCP 978 ms, 22,076 B;
- CI hasta `stable`: 187 s;
- mejora frente a baseline v5.5 de 279 s: 33.0%;
- cobertura reducida: no;
- budgets relajados: no;
- Release Governance: PASS;
- Pages trigger builder→workflow_run→Pages: PASS.

## Contratos preservados

- 46 páginas HTML;
- 16 fichas profundas;
- 37 entradas E2E;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5;
- workers Playwright CI = 1;
- gate dual Browser + Lighthouse;
- idempotencia;
- Actions fijadas a SHA y permisos controlados;
- fuente jurídica única para alcance/entregables;
- secuencia v5.8 → v5.9 → v5.10 → v5.11 → v5.12;
- telemetría sin PII;
- sin CRM/backend ni almacenamiento servidor del formulario;
- sin firma, pagos, agenda o portal documental ficticios.

## Integraciones externas

Activas: GitHub Pages, WhatsApp como handoff manual, contexto comercial local/de sesión, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estático/noindex y pipeline de certificación.

No declarar activas sin evidencia real: dominio personalizado/CNAME, Search Console, analítica externa, CRM/backend, almacenamiento servidor del formulario, email transaccional, firma electrónica, pagos, agenda o carga documental.

## Memoria de ingeniería

Graphify + Obsidian siguen operativos. Antes del cierre documental Graphify estaba alineado con `f8c4d1ab…` (463 nodos / 725 edges / 79 notas). Al retomar: confirmar `main`/`stable`, leer las tres notas canónicas y comparar `BUILD_META.source_commit` con `main`.
