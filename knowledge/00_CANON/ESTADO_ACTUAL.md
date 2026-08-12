# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-11.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot certificado: `stable`.
- Versión declarada en cierre: `5.10.0`.
- Evidencia funcional v5.10 previa al cierre documental: run `31558953560`, SHA `f8b47f2ec2885cc39ff64a2448792f352619f9c3`.

Los SHA actuales de `main` y `stable` deben consultarse dinámicamente. Las notas documentan hitos; los refs, Pages y gates son la autoridad.

## Estado funcional

**La implementación funcional v5.10 está certificada. El commit documental que declara 5.10.0 debe volver a atravesar la certificación pública completa antes de considerarse release definitiva.**

La cadena vigente exige:

- construcción e idempotencia canónica;
- validadores históricos v4.4→v5.7;
- contrato de decisión v5.8;
- contrato de calificación comercial/privacidad v5.9;
- contrato de conversión/propuesta/cierre v5.10;
- 46 páginas y recursos;
- catálogo de 16 fichas;
- JavaScript y JSON;
- GitHub Pages + smoke público;
- Browser E2E, axe y seis Lighthouse;
- resumen CI y release-health;
- promoción de `stable` únicamente con ambos rails pesados verdes.

## v5.10 — Conversión, propuesta y cierre

Las 16 fichas profundas transmiten una intención comercial contextual al formulario. Los productos orientan a propuesta y los servicios a definición de alcance, sin impedir que el usuario cambie la selección.

La interfaz presenta cuatro etapas: `Calificación`, `Alcance y propuesta`, `Aceptación` e `Inicio`. También explica la anatomía de la propuesta: objetivo, perímetro, entregables, cronograma y supuestos/exclusiones.

Preparar la solicitud o abrir WhatsApp no constituye asesoría, cotización definitiva, aceptación del encargo, reserva de disponibilidad, contratación ni promesa de resultado.

La web sigue siendo estática: no guarda el formulario en servidor. No existe CRM/backend activo. La telemetría permanece libre de nombre, correo, empresa y texto libre del caso.

## Compatibilidad y accesibilidad corregidas en v5.10

Los gates bloquearon dos problemas antes de `stable`:

- v5.9 esperaba una firma del formulario incompatible con atributos de v5.10; su applicator quedó preparado para preservar atributos de capas posteriores;
- axe detectó contraste insuficiente en `.close-legal-v510`; el color se corrigió y la suite pública posterior pasó sin violaciones serias/críticas.

El builder posterior terminó con `Canonical public files are current.`. No se redujo cobertura ni se relajaron criterios.

## Evidencia funcional v5.10 previa al cierre documental

Run `31558953560`, SHA `f8b47f2ec2885cc39ff64a2448792f352619f9c3`:

### Browser E2E + axe

- 37 entradas;
- 35 aprobadas;
- 2 omitidas por diseño;
- 0 fallos;
- 0 retries;
- Chromium desktop/mobile;
- WebKit desktop;
- 7 superficies axe sin violaciones serias/críticas.

La cobertura valida el flujo de contacto v5.9/v5.10, el handoff a WhatsApp y la ausencia de PII en telemetría.

### Lighthouse

- portada: performance 1.00, a11y 0.97, LCP 1250 ms, CLS 0, TBT 0 ms, 84,524 B;
- solución IA: 1.00 / 1.00, LCP 955 ms, CLS 0, TBT 0 ms, 23,213 B;
- producto IA: 1.00 / 1.00, LCP 905 ms, CLS 0, TBT 0 ms, 35,506 B;
- sector tecnología: 0.98 / 1.00, LCP 945 ms, CLS 0.087, TBT 0 ms, 24,226 B;
- perspectiva IA: 0.98 / 1.00, LCP 904 ms, CLS 0.087, TBT 0 ms, 25,867 B;
- demo: 1.00 / 1.00, LCP 903 ms, CLS 0, TBT 0 ms, 22,040 B.

Las seis superficies aprobaron sin relajar presupuestos.

### Eficiencia CI

- baseline v5.5: 279 s;
- run funcional v5.10: 173 s hasta `stable`;
- mejora: 38.0%;
- cobertura reducida: no;
- presupuestos relajados: no.

## Contratos preservados

- 37 entradas E2E;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5;
- workers Playwright CI = 1;
- gate dual Browser + Lighthouse;
- idempotencia;
- Actions inventariadas y fijadas a SHA;
- permisos controlados;
- upgrades major no automáticos;
- fuente jurídica única para alcance/entregables;
- capa v5.8 persistente con y sin JavaScript;
- v5.9 posterior a v5.8 y privacy-safe;
- v5.10 posterior a v5.9 y compatible con reconstrucción canónica.

## Integraciones externas

Activas: GitHub Pages, WhatsApp como handoff, contexto comercial local/de sesión, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estático/noindex y pipeline de certificación.

No declarar activas sin evidencia real: dominio personalizado/CNAME, Search Console, analítica externa, CRM/backend, almacenamiento servidor del formulario, email transaccional, firma electrónica, pagos, agenda o carga documental.

## Memoria de ingeniería

Graphify + Obsidian siguen operativos. Al retomar: confirmar `main`/`stable`, leer `CONTEXTO_RAPIDO.md`, `ESTADO_ACTUAL.md`, `TAREA_ACTIVA.md`, comparar `BUILD_META.source_commit` con `main`, usar Graphify para acotar y confirmar luego en fuente/tests.
