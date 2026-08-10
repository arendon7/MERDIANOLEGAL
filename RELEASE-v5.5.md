# Meridiano Legal — Release v5.5.0

Fecha de cierre funcional: 2026-08-10.
Canal: `github-pages-public-performance-accessibility-ready`.

## Objetivo

v5.5 convierte performance y accesibilidad en contratos reproducibles de publicación. La release no añade una nueva capa comercial o visual por inercia: mide el sitio existente en navegador real, fija presupuestos objetivos y evita que `stable` avance si la experiencia pública no cumple.

## Infraestructura de QA

- Node.js >= 22.
- dependencias fijadas con `package-lock.json` y `npm ci`;
- `@playwright/test` 1.62.0;
- `@axe-core/playwright` 4.12.1;
- `lighthouse` 13.4.1;
- Chromium desktop;
- Chromium mobile;
- WebKit desktop;
- axe sobre siete superficies representativas;
- Lighthouse sobre seis superficies con `quality-budgets-v55.json`.

## Evidencia funcional

Run de certificación: `31431923694`.
Candidata funcional certificada antes del cierre documental: `bd310076bbc098771dffd8fde03cabee9e16bc6f`.
URL ensayada: `https://arendon7.github.io/MERDIANOLEGAL/`.

Todos los jobs terminaron en `success`:

- Validate current site;
- Deploy GitHub Pages;
- Verify deployed Pages;
- Browser E2E on deployed Pages;
- Update stable snapshot.

La fase estática aprobó idempotencia, catálogo, conversión, UX v4.5-v4.7, calidad v4.8, operación v4.9, producción v5.0, growth v5.1, CRO/search v5.2, autoridad/medición v5.3, browser v5.4, calidad v5.5, selector, contexto, editorial, sistema visual, JavaScript y JSON.

## Browser E2E + axe

La suite final ejecutó 37 entradas:

- 35 `passed`;
- 2 `skipped` por diseño;
- 0 fallos.

Las siete superficies axe quedaron sin violaciones serias/críticas.

## Lighthouse final

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Portada | 1.00 | 0.97 | 1207 ms | **0** | 0 ms | 73,930 B |
| Solución IA | 1.00 | 1.00 | 904 ms | 0 | 0 ms | 23,509 B |
| Producto IA | 1.00 | 1.00 | 906 ms | 0 | 0 ms | 33,142 B |
| Sector tecnología | 0.98 | 1.00 | 907 ms | 0.087 | 0 ms | 24,557 B |
| Perspectiva IA | 0.98 | 1.00 | 908 ms | 0.087 | 0 ms | 26,153 B |
| Demo | 1.00 | 1.00 | 917 ms | 0 | 0 ms | 21,905 B |

Resultado del runner:

`QUALITY V5.5 OK: 6 superficies cumplen Lighthouse y presupuestos.`

## Incidente: CLS de portada

### Síntoma inicial

La portada presentaba aproximadamente:

- performance score: 0.85;
- accessibility score: 0.97;
- LCP: ~1206 ms;
- TBT: 0 ms;
- transferencia: ~73.9 KB;
- CLS: `0.303806...`;
- presupuesto CLS: `<= 0.15`.

Lighthouse señaló como elemento desplazado la zona `main#contenido > section.hero > div.container > div.hero-art`.

### Causa raíz

El `<img>` del hero ya tenía dimensiones, prioridad y preload. El defecto era de transición de layout:

1. en el HTML inicial la imagen no tenía `visual-home-hero`;
2. `visual-v39.js` añadía esa clase después del primer layout;
3. la clase activa `position:absolute`;
4. la imagen dejaba tardíamente de participar en el grid;
5. el navegador recalculaba la geometría del hero.

### Corrección

PR #12:

- `scripts/apply_visual_assets.py` materializa `visual-home-hero` desde HTML;
- `visual-v39.js` deja de añadir la clase tardíamente;
- `scripts/validate_visual_assets.py` exige el estado inicial y prohíbe la regresión;
- `.obsidian/` queda ignorado por Git.

PR #13:

- se identificó que `apply_quality_v48.py` reconstruía posteriormente el `<img>`;
- `normalize_quality_v48.py` conserva determinísticamente la clase después de la capa v4.8.

PR #14:

- el validator v4.8 exigía un orden literal de atributos;
- se cambió a una validación semántica del elemento `<img>` y su `src`;
- no se eliminó ninguna exigencia sobre imagen, dimensiones, preload o prioridad;
- v5.5 conserva el contrato adicional de layout estable desde HTML.

### Resultado

- CLS de portada: ~0.304 → **0**.
- performance: ~0.85 → **1.00**.
- LCP: ~1206 → 1207 ms, esencialmente estable.
- TBT: 0 → 0 ms.
- presupuesto CLS: no fue modificado.

## Memoria de ingeniería incorporada durante el ciclo

En paralelo se adoptó el patrón Graphify + Obsidian validado previamente en otro proyecto, adaptándolo a Meridiano:

- PR #10: memoria humana + Graphify estructural + `AGENTS.md` + handoff;
- PR #11: cambios exclusivamente de memoria dejan de disparar el despliegue público;
- Graphify corre `--code-only`, sin backend LLM;
- la rama regenerable `knowledge/graphify-live` publica `BUILD_META.json`, snapshot, reporte y wiki;
- Obsidian abre la raíz del repositorio y usa `knowledge/HOME.md` como MOC;
- las relaciones `INFERRED` nunca sustituyen la verificación de fuente.

El corpus piloto optimizado produjo 341 nodos, 520 relaciones, 56 comunidades y 67 notas wiki.

## Política de cierre

La release solo se considera cerrada cuando el commit documental final vuelve a atravesar el pipeline público y `main` y `stable` coinciden. Los SHA escritos en esta nota documentan evidencia histórica; para el estado vigente siempre deben consultarse los refs actuales.

## Integraciones externas

Se mantienen activas únicamente las integraciones verificadas: GitHub Pages, WhatsApp, contexto comercial local/session, telemetría local sin PII, SEO técnico y pipeline de publicación.

Continúan preparadas pero no activas: dominio personalizado, Search Console, analítica externa, CRM/backend, almacenamiento servidor del formulario y email transaccional.
