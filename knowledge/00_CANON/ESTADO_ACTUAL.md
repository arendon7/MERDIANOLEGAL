# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-11.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot certificado: `stable`.
- Versión declarada: `5.7.0`.
- Evidencia funcional de la fundación v5.7: run `31534382576`, SHA `945abb9c4e35c87d4f9a9ecd5ff161707b7d716e`, antes del cierre documental.

Los SHA de `main` y `stable` deben consultarse dinámicamente. Las notas documentan hitos; los refs actuales, Pages y los gates son la autoridad del estado vigente.

## Estado funcional

**La fundación funcional v5.7 quedó certificada y el cierre documental declara 5.7.0.**

El commit documental solo queda cerrado definitivamente cuando vuelve a atravesar la misma certificación pública y `main == stable`.

La cadena v5.7 exige:

- idempotencia canónica;
- validadores v4.4→v5.7;
- 46 páginas y recursos;
- catálogo estático de 16 fichas;
- JavaScript y JSON;
- GitHub Pages;
- smoke HTTP público;
- Browser E2E sobre Pages;
- axe;
- seis auditorías Lighthouse;
- resumen CI;
- release-health v5.7;
- promoción de `stable` únicamente después de Browser + Lighthouse.

## Release governance v5.7

`release-governance-v57.json` protege:

- inventario de Actions oficiales;
- SHA exacto y major validado de cada Action;
- runtimes Node, Python, uv y Graphify;
- dependencias QA exactas;
- workflows obligatorios;
- contratos de permisos;
- 37 entradas E2E;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5;
- gate dual Browser + Lighthouse.

El validator v5.7 bloquea Actions no inventariadas, referencias móviles, SHA fuera de policy, `pull_request_target`, `permissions: write-all`, pérdida de concurrency/timeout y cambios incompatibles en los contratos protegidos.

## Dependencias y supply chain

Dependabot revisa semanalmente npm y GitHub Actions:

- máximo dos PR abiertos por ecosistema;
- minor/patch automáticos;
- upgrades major bloqueados para revisión explícita.

Las dependencias QA continúan fijadas:

- `@playwright/test` 1.62.0;
- `@axe-core/playwright` 4.12.1;
- `lighthouse` 13.4.1;
- Node >=22.

Los checkouts read-only desactivan credenciales persistentes. Solo los jobs que deben escribir conservan autorización de push.

## Arquitectura CI vigente

Después del smoke público se ejecutan dos rails paralelos:

- `browser_e2e` — Chromium desktop/mobile, WebKit y axe;
- `lighthouse_quality` — seis superficies y budgets v5.5.

`stable` depende de ambos y el snapshot genera además `release-governance-health-v57`.

No se cachean binarios Playwright. Sí se usa caché npm reproducible mediante `package-lock.json`.

Lighthouse usa Chromium fijado por Playwright, no el Chrome mutable del runner.

## Evidencia v5.7 de navegador

Browser E2E + axe, tentativa limpia certificada:

- 37 entradas;
- 35 aprobadas;
- 2 omitidas por diseño;
- 0 fallos;
- 0 retries;
- 7 superficies axe sin violaciones serias/críticas.

La primera tentativa Browser del run `31534382576` agotó 360 s durante la instalación Chromium+WebKit por lentitud transitoria del mirror Ubuntu, antes de ejecutar tests. `stable` no se movió. La repetición limpia instaló correctamente y aprobó la suite completa; no se redujo cobertura ni se alteró el timeout.

Lighthouse de la fundación v5.7:

- portada: performance 1.00, a11y 0.97, LCP 1484 ms, CLS 0, TBT 62 ms, 73,826 B;
- solución IA: performance 1.00, a11y 1.00, LCP 904 ms, CLS 0, TBT 0;
- producto IA: performance 1.00, a11y 1.00, LCP 1005 ms, CLS 0, TBT 0;
- sector tecnología: performance 0.98, a11y 1.00, LCP 996 ms, CLS 0.087, TBT 0;
- perspectiva IA: performance 0.98, a11y 1.00, LCP 916 ms, CLS 0.087, TBT 0;
- demo: performance 1.00, a11y 1.00, LCP 986 ms, CLS 0, TBT 0.

Las seis superficies aprobaron con una sola muestra y sin relajar presupuestos.

## Eficiencia CI

Se conserva como referencia limpia:

- baseline v5.5: 279 s;
- run funcional limpio v5.6: 160 s;
- mejora v5.6: 42.7%.

El total de 634 s informado por el run de fundación v5.7 no se adopta como benchmark porque incorpora la tentativa Browser fallida por infraestructura y su reejecución. No representa una nueva topología ni una reducción de eficiencia comparable.

## Robustez Lighthouse

Se mantiene el contrato v5.6:

- Chromium fijado por Playwright;
- budgets v5.5 intactos;
- verificación únicamente para performance/LCP/CLS/TBT;
- dos muestras adicionales si todos los fallos iniciales pertenecen a ese conjunto;
- tres muestras válidas obligatorias;
- mediana de tres, nunca mejor-de-N;
- accesibilidad y peso no reintentables.

## Estado de integraciones externas

Activas:

- GitHub Pages;
- WhatsApp como handoff real de contacto;
- contexto comercial en sesión/local según contratos vigentes;
- telemetría local en memoria y semántica de eventos sin PII;
- sitemap, robots, canonical y Open Graph;
- demo estático/noindex;
- build canónico, validadores, smoke, Browser E2E, axe, Lighthouse, release-health y snapshot `stable`.

No deben declararse activas sin evidencia/configuración real:

- dominio personalizado/CNAME;
- Search Console;
- proveedor externo de analítica;
- CRM/backend de leads;
- almacenamiento servidor del formulario;
- email transaccional.

## Memoria de ingeniería

Graphify + Obsidian continúa operativo:

- `AGENTS.md` define protocolo de entrada;
- `knowledge/HOME.md` es el MOC de Obsidian;
- `knowledge/00_CANON/` conserva contexto, estado y tarea;
- `knowledge/10_DECISIONES/` conserva ADR;
- `knowledge/20_ARQUITECTURA/` conserva mapa humano;
- `knowledge/30_RUNBOOKS/` conserva el flujo;
- `knowledge/99_HANDOFF/` conserva reanudación entre chats;
- `knowledge/graphify-live` contiene memoria estructural regenerable.

## Regla de continuidad

Al retomar:

1. confirmar `main` y `stable`;
2. leer `CONTEXTO_RAPIDO.md`, `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md`;
3. verificar `graphify-out/BUILD_META.json.source_commit` contra `main`;
4. usar Graphify para definir el conjunto mínimo de impacto;
5. verificar en fuente y tests antes de modificar;
6. conservar release-health y el gate dual Browser + Lighthouse antes de `stable`.
