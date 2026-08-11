# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-11.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot certificado: `stable`.
- Versión declarada en cierre: `5.8.0`.
- Evidencia funcional v5.8: run `31541197197`, SHA `681c252f09a50447af0557a2039b34b8a79faed9`, antes del cierre documental.

Los SHA de `main` y `stable` deben consultarse dinámicamente. Las notas documentan hitos; los refs actuales, Pages y los gates son la autoridad del estado vigente.

## Estado funcional

**La implementación funcional v5.8 quedó certificada. El cierre documental declara 5.8.0 y debe volver a atravesar la certificación pública antes de considerarse definitivo.**

La cadena vigente exige:

- idempotencia canónica;
- validadores históricos v4.4→v5.7;
- contrato fuente/runtime v5.8;
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

## Arquitectura de decisión v5.8

La portada incorpora cuatro formas de contratación:

1. entender primero el problema;
2. contratar un resultado cerrado;
3. obtener dirección jurídica recurrente;
4. abordar una decisión o proyecto especializado.

Las 16 fichas profundas incorporan cinco bloques ejecutivos derivados de sus fuentes:

- `ENCAJA SI` ← `situations`;
- `QUÉ COMPRA` ← `perimeter`;
- `QUÉ RECIBE` ← `deliverables`;
- `QUÉ APORTA` ← `requirements`;
- `QUÉ NO ASUMIR` ← `limits`.

También se derivan duración, modalidad y audiencia. No existe una segunda fuente paralela de marketing para esos datos.

`scripts/validate_decision_v58.py` protege la correspondencia fuente→resumen y exige que la capa se ubique antes de `#detail-page`, fuera del contenedor que `catalog-page.js` puede reemplazar. El resumen debe persistir con JavaScript y seguir disponible sin JavaScript.

## Incidencias de construcción v5.8

Los gates bloquearon dos incompatibilidades antes de promover `stable`:

- idempotencia detectó que un parser histórico v4.5 dependía de cuatro espacios exactos antes de `<section>`; se volvió tolerante a indentación;
- Browser detectó que la primera ubicación del bloque v5.8 era eliminada por el render runtime de productos; se movió fuera de `#detail-page` y se añadió un contrato explícito de persistencia.

En ambos casos `stable` permaneció inmóvil y no se redujo cobertura ni se suavizaron pruebas.

## Evidencia funcional v5.8

Run `31541197197`, SHA `681c252f09a50447af0557a2039b34b8a79faed9`:

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

- portada: performance 1.00, a11y 0.97, LCP 1425 ms, CLS 0, TBT 0 ms, 76,009 B;
- solución IA: performance 1.00, a11y 1.00, LCP 978 ms, CLS 0, TBT 0 ms, 23,234 B;
- producto IA: performance 1.00, a11y 1.00, LCP 909 ms, CLS 0, TBT 0 ms, 35,406 B;
- sector tecnología: performance 1.00, a11y 1.00, LCP 938 ms, CLS 0, TBT 0 ms, 24,260 B;
- perspectiva IA: performance 1.00, a11y 1.00, LCP 1003 ms, CLS 0, TBT 0 ms, 25,728 B;
- demo: performance 1.00, a11y 1.00, LCP 970 ms, CLS 0, TBT 0 ms, 22,045 B.

Las seis superficies aprobaron con una sola muestra y sin relajar presupuestos.

### Eficiencia CI

- baseline v5.5: 279 s;
- run funcional v5.8: 232 s hasta gate de `stable`;
- mejora frente a baseline: 16.8%;
- cobertura reducida: no;
- presupuestos relajados: no.

## Release governance v5.7 preservada

`release-governance-v57.json` continúa protegiendo:

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
6. conservar los contratos v5.8, release-health y el gate dual Browser + Lighthouse antes de `stable`.