# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-11.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot certificado: `stable`.
- Versión declarada en este cierre: `5.11.0`.
- Evidencia funcional v5.11 previa al cierre documental: run `31560805174`, SHA `cf4341eb9ec051a3e583b4675263b228ee5f0839`.

Los SHA actuales de `main` y `stable` deben consultarse dinámicamente. Las notas documentan hitos; refs, Pages y gates son la autoridad.

## Estado funcional

**La implementación funcional v5.11 está certificada. El commit documental que declara 5.11.0 debe volver a atravesar la certificación pública completa antes de considerar cerrada la release definitiva.**

La cadena vigente exige:

- builder canónico;
- idempotencia y validadores históricos;
- contratos v5.8, v5.9, v5.10 y v5.11;
- GitHub Pages + smoke público;
- Browser E2E/axe y seis Lighthouse;
- resumen CI + release-health;
- promoción de `stable` únicamente con ambos rails pesados verdes.

## v5.11 — Release serializada

Pages ya no compite con el builder mediante `push` directo. `Site Quality and Deploy` se activa por finalización exitosa de `Build canonical public site` o por `workflow_dispatch` manual.

`scripts/validate_pages_trigger_v511.py` protege esta topología. `scripts/validate_ci_v56.py` fue actualizado para exigirla sin perder los contratos históricos de cobertura, budgets, paralelismo y promoción dual.

Evidencia real de topología: builder `31560235195` → único Pages `31560254312` por `workflow_run`; no apareció el run espurio por push observado en v5.10.

## v5.11 — Preparación del encargo

La web distingue:

1. `Solicitud preparada`;
2. `Propuesta emitida`;
3. `Propuesta aceptada`;
4. `Encargo iniciado`.

Antes del inicio se explican verificaciones de partes/conflictos cuando correspondan, alcance/exclusiones, condiciones económicas, fecha o condición de inicio, interlocutores y canal apropiado para información confidencial.

El formulario público no acepta contratos, no cobra pagos, no reserva agenda, no crea expedientes, no habilita carga documental y no inicia el encargo automáticamente. La aceptación y el inicio se rigen por la propuesta y sus condiciones aplicables.

## Evidencia funcional v5.11

Run `31560805174`, SHA `cf4341eb9ec051a3e583b4675263b228ee5f0839`:

### Browser E2E + axe

- 37 entradas;
- 35 aprobadas;
- 2 omitidas por diseño;
- 0 fallos;
- 0 retries;
- Chromium desktop/mobile;
- WebKit desktop;
- 7 superficies axe sin violaciones serias/críticas.

### Lighthouse

- portada: performance 1.00, a11y 0.97, LCP 1247 ms, CLS 0, TBT 74 ms, 86,682 B;
- solución IA: 1.00 / 1.00, LCP 904 ms, CLS 0, TBT 0 ms, 23,310 B;
- producto IA: 1.00 / 1.00, LCP 907 ms, CLS 0, TBT 0 ms, 35,468 B;
- sector tecnología: 0.98 / 1.00, LCP 922 ms, CLS 0.087, TBT 0 ms, 24,507 B;
- perspectiva IA: 0.98 / 1.00, LCP 902 ms, CLS 0.087, TBT 0 ms, 25,914 B;
- demo: 1.00 / 1.00, LCP 906 ms, CLS 0, TBT 0 ms, 22,058 B.

### Eficiencia CI

- baseline v5.5: 279 s;
- run funcional v5.11: 193 s hasta `stable`;
- mejora: 30.8%;
- cobertura reducida: no;
- presupuestos relajados: no.

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
- secuencia v5.8 → v5.9 → v5.10 → v5.11;
- telemetría sin PII;
- sin CRM/backend ni almacenamiento servidor del formulario;
- sin firma, pagos, agenda o portal documental ficticios.

## Integraciones externas

Activas: GitHub Pages, WhatsApp como handoff, contexto comercial local/de sesión, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estático/noindex y pipeline de certificación.

No declarar activas sin evidencia real: dominio personalizado/CNAME, Search Console, analítica externa, CRM/backend, almacenamiento servidor del formulario, email transaccional, firma electrónica, pagos, agenda o carga documental.

## Memoria de ingeniería

Graphify + Obsidian siguen operativos. Al retomar: confirmar `main`/`stable`, leer `CONTEXTO_RAPIDO.md`, `ESTADO_ACTUAL.md`, `TAREA_ACTIVA.md`, comparar `BUILD_META.source_commit` con `main`, usar Graphify para acotar y confirmar luego en fuente/tests.
