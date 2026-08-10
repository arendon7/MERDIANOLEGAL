# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-10.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot certificado: `stable`.
- Versión declarada: `5.5.0`.
- Evidencia funcional de cierre: run `31431923694`, sobre la candidata `bd310076bbc098771dffd8fde03cabee9e16bc6f` antes del cierre documental.

Los SHA de `main` y `stable` deben consultarse dinámicamente. Las notas documentan hitos; los refs actuales son la autoridad del estado vigente.

## Estado funcional

**v5.5 quedó funcionalmente certificada.**

La cadena completa aprobó:

- idempotencia canónica;
- validadores v4.4→v5.5;
- 46 páginas y recursos;
- catálogo estático de 16 fichas;
- JavaScript y JSON;
- GitHub Pages;
- smoke HTTP público;
- Playwright sobre Pages;
- axe;
- seis auditorías Lighthouse;
- promoción de `stable`.

## Evidencia de navegador

Browser E2E + axe:

- 37 entradas;
- 35 aprobadas;
- 2 omitidas por diseño;
- 0 fallos;
- 7 superficies axe sin violaciones serias/críticas.

Lighthouse final:

- portada: performance 1.00, accesibilidad 0.97, LCP 1207 ms, CLS 0, TBT 0, ~73.9 KB;
- solución IA: performance 1.00, accesibilidad 1.00, CLS 0;
- producto IA: performance 1.00, accesibilidad 1.00, CLS 0;
- sector tecnología: performance 0.98, accesibilidad 1.00, CLS 0.087;
- perspectiva IA: performance 0.98, accesibilidad 1.00, CLS 0.087;
- demo: performance 1.00, accesibilidad 1.00, CLS 0.

Las seis superficies cumplen los presupuestos versionados.

## Incidente CLS y resolución

El único bloqueo pendiente era CLS de portada ~0.304 frente a presupuesto <=0.15.

Causa confirmada:

- la imagen del hero nacía en flujo;
- `visual-v39.js` añadía después `visual-home-hero`;
- esa clase activa `position:absolute`;
- el cambio tardío obligaba a recalcular el grid/hero.

Corrección:

- el HTML inicial materializa `visual-home-hero`;
- JS ya no añade esa clase;
- `normalize_quality_v48.py` preserva el contrato después de la reconstrucción histórica v4.8;
- el validator v4.8 valida semánticamente la imagen sin depender del orden de atributos;
- el validator visual exige la clase inicial y prohíbe la mutación tardía.

Resultado: CLS ~0.304 → 0 y performance ~0.85 → 1.00, sin modificar el presupuesto.

## Estado de integraciones externas

Activas:

- GitHub Pages;
- WhatsApp como handoff real de contacto;
- contexto comercial en sesión/local según contratos vigentes;
- telemetría local en memoria y semántica de eventos sin PII;
- sitemap, robots, canonical y Open Graph;
- demo estático/noindex;
- build canónico, validadores, smoke, Browser E2E, axe, Lighthouse y snapshot `stable`.

No deben declararse activas sin evidencia/configuración real:

- dominio personalizado/CNAME;
- Search Console;
- proveedor externo de analítica;
- CRM/backend de leads;
- almacenamiento servidor del formulario;
- email transaccional.

## Memoria de ingeniería

Graphify + Obsidian está operativo:

- `AGENTS.md` define protocolo de entrada;
- `knowledge/HOME.md` es el MOC de Obsidian;
- `knowledge/00_CANON/` conserva contexto, estado y tarea;
- `knowledge/10_DECISIONES/` conserva ADR;
- `knowledge/20_ARQUITECTURA/` conserva mapa humano;
- `knowledge/30_RUNBOOKS/` conserva el flujo;
- `knowledge/99_HANDOFF/` conserva reanudación entre chats;
- `knowledge/graphify-live` contiene memoria estructural regenerable.

Corpus Graphify de referencia: 341 nodos, 520 relaciones, 56 comunidades y 67 notas wiki, ejecutado `--code-only` sin backend LLM.

Los cambios exclusivamente de memoria regeneran Graphify sin desplegar el sitio público.

## Regla de continuidad

Al retomar:

1. confirmar `main` y `stable`;
2. leer `CONTEXTO_RAPIDO.md`, `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md`;
3. verificar `graphify-out/BUILD_META.json.source_commit` contra `main`;
4. usar Graphify para definir el conjunto mínimo de impacto;
5. verificar en fuente y tests antes de modificar.
