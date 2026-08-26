# W4.2 — Route Compatibility & SEO Contract

Fecha: 2026-08-25
Estado: diseño técnico ejecutable sobre W4.1; no activa todavía migración pública.
Baseline productivo: v7.4.0 / `86813813e29dd6b47105ba7fb6259630fcd9cb5b`.
Rama: `design/v8-route-compat-w42` apilada sobre `design/v8-client-architecture-w41`.

## 1. Objetivo

Convertir la matriz W4.1 en un contrato técnico verificable para que v8 pueda cambiar taxonomía y rutas sin perder:

- URLs históricas;
- canonical;
- sitemap;
- breadcrumbs/schema;
- internal linking;
- indexación;
- accesibilidad;
- smoke/E2E;
- rollback a v7.4.

W4.2 no crea todavía páginas v8. Primero define cómo coexistirán legacy y target routes.

---

## 2. Hallazgos del código actual

### 2.1 `scripts/validate_site.py`

El validator general está acoplado a la topología histórica:

- `CATALOG_PAGES` fija 16 rutas bajo `servicios/` y `productos/`;
- `PERSPECTIVE_PAGES` fija 6 perspectivas;
- `SECTOR_PAGES` fija 8 sectores;
- Home debe exponer exactamente 16 `.full-detail-link`;
- Home debe enlazar exactamente 8 sectores;
- exige 16 `data-catalog-id`;
- exige 6 perspectivas y 8 sectores.

Conclusión: no puede simplemente "actualizarse el HTML". v8 requiere un contrato estructural nuevo y version-gating explícito.

### 2.2 `scripts/build_catalog_shells.py`

Hardcodea las 16 fichas y además define semántica histórica:

- `service` → `Service`;
- `product` → `Product`;
- breadcrumbs `Servicios` / `Productos`;
- canonical calculado desde la ruta física histórica.

Conclusión: no debe usarse como renderer v8 de prácticas/soluciones. Debe conservarse para reproducibilidad histórica y quedar no-op/delegado en v8.

### 2.3 `scripts/render_services_v42.mjs`

Encuentra las ocho fichas recorriendo únicamente `servicios/` y buscando `data-catalog-id`.

Conclusión: mover físicamente una práctica antes de introducir renderer v8 rompería el materializador v4.2.

### 2.4 `scripts/apply_experience_solutions_v60.py`

La Experience v6 define `soluciones/` como **seis rutas de necesidad + hub** y exige exactamente seis slugs en Growth/CRO.

Conclusión: v8 redefine semánticamente `/soluciones/` hacia ocho soluciones de alcance definido. La v6 no puede seguir gobernando esa carpeta en v8 sin version-gating.

### 2.5 `scripts/validate_experience_solutions_v60.py`

Exige igualdad exacta entre:

- seis slugs Growth;
- seis slugs CRO;
- seis archivos HTML físicos;
- más `soluciones/index.html`.

Conclusión: debe quedar validator histórico para v6/v7, no relajarse. v8 necesita validator propio.

### 2.6 `scripts/apply_production_v50.py`

`html_targets()` recorre:

- HTML top-level;
- `servicios/`;
- `productos/`;
- `sectores/`;
- `perspectivas/`.

No recorre `soluciones/`, y tampoco conocería futuras carpetas `practicas/` o `servicios-continuos/`.

Además:

- canonical = `BASE_URL + ruta física`;
- `patch_sitemap()` **no genera el sitemap**: solo sustituye la base URL histórica;
- 404/noindex se excluyen de canonical/runtime según reglas históricas.

Conclusión: v8 debe reemplazar el descubrimiento de rutas por un route manifest explícito. No basta con añadir nuevas carpetas.

### 2.7 `scripts/validate_production_v50.py`

Valida:

- que las URLs del sitemap comiencen por `BASE_URL`;
- que `demo.html` no aparezca;
- self-canonical para los HTML que `html_targets()` alcanza.

Pero no prueba que:

- sitemap == conjunto exacto de páginas indexables;
- todas las familias públicas estén incluidas;
- aliases apunten a canonical target;
- nuevas carpetas sean procesadas.

Conclusión: v8 requiere igualdad de conjuntos, no solo validación parcial.

### 2.8 `tests/e2e/public-site.spec.mjs`

El E2E actual hardcodea, entre otros:

- 16 enlaces profundos;
- rutas `/productos/...`;
- rutas `/servicios/...`;
- seis `soluciones/...` de necesidad;
- telemetría asociada a esos slugs.

Conclusión: no silenciar estos tests. Deben preservarse para baseline y crearse expectativas v8 + smoke legacy explícito.

### 2.9 `scripts/canonical_pipeline_v524.py`

La cadena histórica conserva exactamente 30 pasos y sobre baseline v6 omite materializadores v4/v5, ejecutando una extensión v6 común a Builder y Pages.

Conclusión: v8 no necesita "paso 31". Debe introducir una extensión v8/version gate equivalente que sustituya composición v6 donde corresponda y mantenga Builder == Pages == manifiesto.

---

## 3. Decisión técnica principal: Route Manifest

Se crea:

`assets/data/v8/route-contract-v80.json`

Como fuente estructurada de:

- 46 rutas legacy;
- destino v8;
- acción KEEP/RENAME/MOVE/MERGE;
- familia destino;
- indexación legacy;
- pertenencia al sitemap baseline;
- prioridad;
- target catalog de 6 prácticas, 8 soluciones y 2 recurrentes.

En estado `planning` este archivo **no gobierna producción**. Primero debe superar su validator y revisión W4.2.

Una vez activado v8 será la autoridad de:

- canonical target;
- sitemap target;
- aliases;
- smoke matrix;
- route inventory.

---

## 4. Política de compatibilidad en GitHub Pages

### Restricción

No asumir redirects HTTP de servidor configurables.

El sitio estático debe poder resolver URLs antiguas mediante archivos físicos o una estrategia explícitamente probada.

### Estrategia propuesta por fases

#### Fase A — dual-route pilot

Para las tres superficies piloto:

- crear target v8;
- conservar legacy HTML completo;
- internal links nuevos apuntan al target;
- legacy sigue resolviendo;
- no se elimina ni reescribe aún de forma agresiva;
- comparar canonical/indexación antes de handoff.

Objetivo: validar IA y navegación sin arriesgar enlaces históricos.

#### Fase B — canonical handoff

Después de Browser/SEO checks:

- target v8 = canonical principal;
- legacy se convierte en alias estático explícito;
- alias incluye título claro, canonical target y enlace accesible;
- cualquier `meta refresh`/`location.replace` solo se incorpora si una prueba específica demuestra que no degrada accesibilidad, navegación hacia atrás, analytics semántica ni crawling.

No depender de JavaScript como único mecanismo de recuperación.

#### Fase C — legacy permanence

Mientras GitHub Pages siga siendo hosting y no exista redirect HTTP fiable:

- conservar alias físico para URLs externas históricas;
- excluir aliases del sitemap target;
- mantener smoke permanente de aliases;
- no borrar por limpieza estética.

---

## 5. Política canonical

### Canonical target

Cada página v8 primaria debe ser self-canonical.

### Legacy KEEP

Permanece self-canonical.

### Legacy MOVE/MERGE tras handoff

Debe declarar canonical hacia `target_route`.

### Demo / 404

- `demo.html`: noindex y claramente demostrativa;
- `404.html`: noindex;
- ninguna se incorpora al sitemap.

### Meridiano Contratos

`RC02` permanece `publishable=false`; por tanto:

- no HTML público;
- no sitemap;
- no canonical;
- no enlace de navegación;
- no Schema de oferta;

hasta capability contract aprobado.

---

## 6. Política sitemap v8

El sitemap deja de ser archivo mantenido manualmente.

Debe generarse desde el route contract activo.

Reglas:

1. incluir únicamente rutas primarias indexables;
2. excluir demo/404;
3. excluir aliases legacy después del canonical handoff;
4. excluir targets `publishable=false`;
5. usar `site-config.json.base_url`;
6. orden determinista;
7. segunda pasada idempotente;
8. validator: `set(sitemap URLs) == set(indexable canonical routes)`.

Este gate es más fuerte que v5.0.

---

## 7. Breadcrumb y Schema

El renderer v8 no puede heredar automáticamente `Product`/`Service` y `Productos`/`Servicios` de `build_catalog_shells.py`.

### Práctica

Schema candidato: `Service` o `LegalService` contextual, sin inventar oferta cerrada.
Breadcrumb:

`Inicio → Prácticas → [Práctica]`.

### Solución

Schema debe revisarse por semántica. No utilizar `Product` únicamente porque históricamente estaba en `/productos/`.
Breadcrumb:

`Inicio → Soluciones → [Solución]`.

### Recurrente

Breadcrumb:

`Inicio → Servicios continuos → [Servicio]`.

Schema final debe reflejar verdad comercial real y no plataforma ficticia.

### Perspectivas

Conservar Article/CollectionPage vigente salvo auditoría específica.

---

## 8. Internal linking

Después del piloto:

- Home apunta solo a target routes v8;
- prácticas enlazan soluciones relacionadas;
- soluciones enlazan práctica soporte + recurrente cuando corresponda;
- sectores enlazan prácticas/soluciones;
- perspectivas enlazan targets v8;
- aliases no deben ser destinos de internal linking nuevo.

Validator propuesto:

`new_internal_links_to_legacy_aliases == 0`.

Excepciones: documentación o pruebas de compatibilidad, nunca navegación productiva.

---

## 9. Nuevo contrato de validación

### Ya añadido

`scripts/validate_route_contract_v80.py`

En estado planning comprueba:

- 46/46 legacy routes;
- árbol físico == contract;
- 43/43 URLs del sitemap baseline;
- self-canonical baseline para indexables;
- demo/404 noindex;
- 6 prácticas target;
- 8 soluciones target;
- 2 recurrentes target;
- RC02 `publishable=false`;
- no asumir redirects de servidor;
- prohibición de retirar legacy antes de certificación.

### Antes de activación v8 debe ampliarse con

- target pages físicas esperadas por wave;
- alias canonical target;
- sitemap target;
- zero orphan target routes;
- zero new internal links to aliases;
- schema/breadcrumb target;
- status lifecycle `planning → pilot → candidate → certified`.

---

## 10. Validators/materializadores afectados

### P0 — deben version-gatearse antes del primer move

- `scripts/validate_site.py`;
- `scripts/build_catalog_shells.py`;
- `scripts/render_services_v42.mjs`;
- `scripts/apply_experience_solutions_v60.py`;
- `scripts/validate_experience_solutions_v60.py`;
- `scripts/apply_production_v50.py`;
- `scripts/validate_production_v50.py`;
- `tests/e2e/public-site.spec.mjs`;
- `scripts/canonical_pipeline_v524.py`;
- `.github/workflows/build-canonical.yml`;
- `.github/workflows/pages.yml`.

### P1 — auditar por hardcoded paths/slugs

- `catalog-home-v32.js`;
- `page-context.js`;
- `growth-solutions-v51.json`;
- `cro-solutions-v52.json`;
- `authority-v53.json`;
- materializadores v5.1/v5.2/v5.3;
- validadores Search Discovery, Engagement, Fit & Scope, Buying Clarity y Legal Intelligence que apunten a rutas históricas.

No se cambia ninguno hasta que el piloto identifique el mínimo conjunto real.

---

## 11. Nuevos invariantes v8

Sustituir gradualmente invariantes históricos de forma verificable:

### Arquitectura

- legacy mapping: 46/46;
- prácticas primarias: 6/6;
- soluciones primarias: 8/8;
- recurrente publicable inicial: 1/1;
- RC02 bloqueado hasta capability truth;
- perspectivas: 6/6;
- formulario físico: 1/1.

### SEO

- canonical primario: 1 por página indexable;
- sitemap == canonical indexable set;
- aliases fuera de sitemap tras handoff;
- legacy smoke: 100%;
- broken internal links: 0;
- orphan canonical routes: 0.

### Capability

- portal ficticio: 0;
- auth/pago/firma/upload/CRM ficticios: 0;
- demo confundible con portal: 0;
- nuevos precios no soportados: 0.

### UX/accessibility

- keyboard PASS;
- axe serious/critical 0;
- no horizontal overflow;
- mobile route recovery PASS;
- reduced motion donde aplique.

---

## 12. Piloto técnico W4.3 recomendado

No mover ocho + seis páginas de una vez.

Probar exactamente:

1. **SO07 Sistema Contractual Empresarial**
   - legacy `/productos/sistema-contractual-empresarial.html`;
   - target `/soluciones/sistema-contractual-empresarial.html`.

2. **PR02 Corporativo, Societario y Gobierno**
   - legacy `/servicios/sociedades-gobierno-inversion.html`;
   - target `/practicas/corporativo-societario-gobierno.html`.

3. **RC01 Dirección Jurídica Externa**
   - legacy `/servicios/direccion-juridica-externa.html`;
   - target `/servicios-continuos/direccion-juridica-externa.html`.

Estas tres superficies prueban las tres familias sin introducir RC02.

---

## 13. Rollback

Hasta certificación v8:

- `stable` permanece v7.4;
- legacy pages no se eliminan;
- target routes nacen solo en rama/candidate;
- si falla SEO/Browser/axe/canonical, descartar rama target restaura topología certificada;
- no mover `stable` manualmente.

---

## 14. Definition of Done W4.2

W4.2 puede cerrarse cuando:

- route contract estructurado existe;
- 46/46 legacy routes verificables;
- 43/43 sitemap baseline verificable;
- estrategia de alias compatible definida sin asumir server redirects;
- canonical policy definida;
- sitemap target generator contract definido;
- breadcrumb/schema policy definida;
- materializadores/validators afectados inventariados;
- nuevos invariantes v8 definidos;
- piloto de tres superficies seleccionado;
- RC02 continúa bloqueado;
- `stable` intacta.

El siguiente frente es **W4.3 — v8 renderer/design-system pilot infrastructure**, todavía sin propagación masiva.
