# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-10.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot certificado: `stable`.
- Versión declarada: `5.6.0`.
- Evidencia funcional v5.6: run `31458580456`, sobre la candidata `c4f48e43a1681cdbd24db4c6308878efeb801700` antes del cierre documental.

Los SHA de `main` y `stable` deben consultarse dinámicamente. Las notas documentan hitos; los refs actuales y los gates son la autoridad del estado vigente.

## Estado funcional

**v5.6 quedó funcionalmente certificada antes del cierre documental.**

La cadena aprobó:

- idempotencia canónica;
- validadores v4.4→v5.6;
- 46 páginas y recursos;
- catálogo estático de 16 fichas;
- JavaScript y JSON;
- GitHub Pages;
- smoke HTTP público;
- Browser E2E sobre Pages;
- axe;
- seis auditorías Lighthouse;
- resumen CI v5.6;
- promoción de `stable`.

## Arquitectura CI vigente

Después del smoke público se ejecutan dos rails paralelos:

- `browser_e2e` — Chromium desktop/mobile, WebKit y axe;
- `lighthouse_quality` — seis superficies y budgets v5.5.

`stable` depende de ambos.

No se cachean binarios Playwright. Sí se usa caché npm reproducible mediante `package-lock.json`.

Lighthouse usa Chromium fijado por Playwright, no el Chrome mutable del runner.

## Evidencia de navegador

Browser E2E + axe:

- 37 entradas;
- 35 aprobadas;
- 2 omitidas por diseño;
- 0 fallos;
- 0 retries;
- 7 superficies axe sin violaciones serias/críticas.

Lighthouse final:

- portada: performance 1.00, a11y 0.97, LCP 1239 ms, CLS 0, TBT 0, 73,834 B;
- solución IA: performance 1.00, a11y 1.00, LCP 964 ms, CLS 0, TBT 0;
- producto IA: performance 1.00, a11y 1.00, LCP 911 ms, CLS 0, TBT 0;
- sector tecnología: performance 1.00, a11y 1.00, LCP 935 ms, CLS 0, TBT 0;
- perspectiva IA: performance 0.98, a11y 1.00, LCP 904 ms, CLS 0.087, TBT 0;
- demo: performance 1.00, a11y 1.00, LCP 944 ms, CLS 0, TBT 0.

Las seis superficies aprobaron con una sola muestra y sin relajar presupuestos.

## Eficiencia CI

Baseline comparable v5.5:

- 279 s hasta habilitar el snapshot estable.

Run funcional v5.6:

- 160 s;
- mejora 42.7%;
- objetivo interno: 20%;
- cobertura reducida: no;
- budgets relajados: no.

La mejora proviene de paralelizar Browser E2E/axe y Lighthouse, reutilizar caché npm segura, evitar ciclos canónicos redundantes y desacoplar observabilidad de logs extensos.

## Robustez Lighthouse

Un primer experimento v5.6 con el Chrome mutable del runner produjo TBT aislado de 497 ms en portada.

La release final:

- restaura Chromium fijado por Playwright;
- instala solo Chromium en el rail Lighthouse;
- mantiene los budgets v5.5;
- permite verificación únicamente para performance/LCP/CLS/TBT;
- exige dos muestras adicionales y mediana de tres si todos los fallos iniciales son de ese conjunto;
- trata accesibilidad y peso como no reintentables;
- registra todas las muestras.

El run final no necesitó activar esa verificación.

## Estado de integraciones externas

Activas:

- GitHub Pages;
- WhatsApp como handoff real de contacto;
- contexto comercial en sesión/local según contratos vigentes;
- telemetría local en memoria y semántica de eventos sin PII;
- sitemap, robots, canonical y Open Graph;
- demo estático/noindex;
- build canónico, validadores, smoke, Browser E2E, axe, Lighthouse, resumen CI y snapshot `stable`.

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

Los cambios exclusivamente de memoria regeneran Graphify sin desplegar el sitio público.

## Regla de continuidad

Al retomar:

1. confirmar `main` y `stable`;
2. leer `CONTEXTO_RAPIDO.md`, `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md`;
3. verificar `graphify-out/BUILD_META.json.source_commit` contra `main`;
4. usar Graphify para definir el conjunto mínimo de impacto;
5. verificar en fuente y tests antes de modificar;
6. conservar el gate dual Browser + Lighthouse antes de `stable`.
