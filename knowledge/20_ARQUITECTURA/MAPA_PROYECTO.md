# Meridiano Legal — Mapa de arquitectura y puntos de impacto

Esta nota es un mapa humano. Graphify debe usarse para relaciones estructurales actuales; `main` sigue siendo la autoridad.

## 1. Fuentes de negocio y oferta

### Productos

- Fuente: `catalog-products-v41/`.
- Renderer: `scripts/render_catalog_static.mjs`.
- Salida: `productos/*.html`.
- Contrato: 8 productos profundos, alcance cerrado, entregables, límites, aceptación y suplementos.

### Servicios

- Fuente: `catalog-services-v42/`.
- Renderer: `scripts/render_services_v42.mjs`.
- Salida: `servicios/*.html`.
- Contrato: 8 servicios especializados diferenciados de los productos cerrados.

### Rutas por necesidad

- Fuente estructural: `growth-solutions-v51.json`.
- CRO/intención: `cro-solutions-v52.json`.
- Autoridad/interlinking: `authority-v53.json`.
- Salida: `soluciones/`.
- Regla: no crear doorway pages delgadas; cada ruta debe orientar una decisión y conectar con servicio/producto/evidencia.

## 2. Portada y runtime público

- HTML canónico: `index.html`, materializado por la cadena de aplicadores.
- Runtime base: `site-v3.js`.
- Enriquecimiento comercial: `catalog-home-v32.js`.
- Selector/contexto: `decision-flow.js`, `page-context.js`.
- Telemetría local: `telemetry-v50.js` + `measurement-v53.js`.
- CSS base: `site-v3.css`.
- Capas posteriores relevantes: `visual-v39.css`, `commercial-v43.css`, `ux-v45.css`, `quality-v48.css`, `operations-v49.css`, `growth-v51.css` y otras capas específicas.

Regla: cuando un defecto aparece solo en la portada, verificar primero cascada CSS + runtime progresivo antes de modificar generadores de páginas profundas.

## 3. Editorial y autoridad

- Firma: `firma.html`.
- Biblioteca: `perspectivas.html` + `perspectivas/*.html`.
- Sectores: `sectores/*.html`.
- Centro Demo: `experiencia.html`.
- Portal demo: `demo.html` + runtime asociado.

Fuentes/aplicadores principales:

- `scripts/enrich_editorial_pages.py`;
- `scripts/apply_editorial_ux_v47.py`;
- `scripts/normalize_editorial_v47.py`;
- `scripts/apply_authority_v53.py`.

## 4. Build canónico

La cadena histórica es acumulativa. No eliminar una capa anterior solo porque una versión nueva la complementa.

Orden conceptual vigente:

1. construir shells de productos;
2. renderizar productos;
3. renderizar servicios;
4. enriquecer editorial;
5. aplicar sistema comercial/conversión;
6. aplicar sistema visual;
7. aplicar UX de portada;
8. aplicar UX de fichas profundas;
9. aplicar UX editorial/demo;
10. normalizar compatibilidad histórica;
11. calidad v4.8;
12. operaciones públicas v4.9;
13. sincronizar versión pública;
14. configuración de producción v5.0;
15. growth/soluciones v5.1;
16. CRO/intención v5.2;
17. autoridad/medición v5.3;
18. infraestructura E2E v5.4;
19. performance/accesibilidad v5.5.

Workflow: `.github/workflows/build-canonical.yml`.

## 5. Calidad y certificación

### Estático

- `scripts/validate_site.py`;
- `scripts/validate_static_catalog.py`;
- validadores versionados `validate_*` para cada capa;
- validadores JS/JSON/contexto/visual/editorial.

### Navegador

- `playwright.config.mjs`;
- `tests/e2e/`;
- Chromium desktop;
- Chromium mobile;
- WebKit desktop;
- axe en Chromium sobre superficies representativas.

### Performance/accesibilidad

- `quality-budgets-v55.json`;
- `scripts/run_quality_v55.mjs`;
- Lighthouse sobre seis superficies.

### Publicación

Workflow: `.github/workflows/pages.yml`.

Secuencia de autoridad:

`idempotencia → validadores → deploy Pages → smoke → browser E2E/axe/Lighthouse → stable`.

## 6. Refs y disciplina de release

- `main`: candidato/fuente actual.
- `stable`: última publicación certificada.
- `knowledge/graphify-live`: fotografía estructural regenerable de un `main` concreto.

No mover `stable` si un gate está rojo, aunque Pages haya desplegado correctamente.

## 7. Mapa rápido de impacto

### Cambiar un producto

Revisar: JSON del producto → renderer → salida HTML → catálogo/portada si aplica → validator estático → E2E profundo si afecta interacción.

### Cambiar un servicio

Revisar: JSON del servicio → renderer → salida HTML → rutas relacionadas → validator estático → interlinking.

### Cambiar una solución

Revisar: growth v5.1 + CRO v5.2 + authority v5.3 → generador/aplicador → schema/SEO → links a producto/servicio/perspectiva/sector.

### Cambiar portada

Revisar: `index.html` materializado → `site-v3.css` + capas CSS → `site-v3.js` + `catalog-home-v32.js` + `decision-flow.js` → v4.5/v4.8 validators → Playwright móvil/desktop → axe → Lighthouse.

### Cambiar contacto/medición

Revisar: formulario → operaciones v4.9 → runtime telemetry/measurement → contrato sin PII → E2E de preparación de lead → privacidad.

### Cambiar build o validator

Revisar: workflow canónico → idempotencia → compatibilidad histórica → Pages workflow → riesgo de carrera/concurrencia → reglas de `stable`.

## 8. Principio para Graphify

Graphify debe responder primero: “¿qué módulos y relaciones pueden verse afectados?”. Después el agente confirma en fuente: “¿cuáles de esas relaciones son reales y qué contratos de prueba las protegen?”. Esta separación evita tanto exploración masiva como confianza excesiva en inferencias.