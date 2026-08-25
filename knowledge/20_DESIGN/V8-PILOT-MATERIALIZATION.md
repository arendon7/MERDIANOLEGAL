# W4.4 — v8 Pilot Materialization Candidate

Fecha: 2026-08-25  
Estado: **PASS — candidate efímero certificado por Browser/Axe**.  
Dependencias: W4.1 → W4.2 → W4.3.

## 1. Objetivo

Probar HTML v8 real en navegador antes de añadir una sola ruta target al árbol público del repositorio.

W4.4 transforma el renderer W4.3 en tres archivos físicos **solo dentro del checkout desechable de GitHub Actions**. Al terminar el job, esos archivos desaparecen y la rama continúa con 46 HTML.

## 2. Targets efímeros

- SO07 — `/soluciones/sistema-contractual-empresarial.html` — fuente `catalog-products-v41/p07-contractual.json`.
- PR02 — `/practicas/corporativo-societario-gobierno.html` — fuente `catalog-services-v42/s04-societario.json`.
- RC01 — `/servicios-continuos/direccion-juridica-externa.html` — fuente `catalog-services-v42/s02-direccion.json`.

## 3. Materializador

`scripts/materialize_v8_pilot.py`

Contrato:

- raíz de salida obligatoria;
- materializar sobre working tree exige `--allow-working-tree` explícito;
- solo tres pilotos;
- no sobrescribe targets;
- conserva `noindex,follow`;
- no crea forms;
- emite `.v8-pilot-materialization.json`;
- no pertenece aún al builder canónico.

## 4. Topología temporal

Antes de materializar: **46 HTML**.  
Durante Browser CI: **46 legacy + 3 target = 49 HTML**.  
Después del job: el runner se destruye y la rama vuelve a **46 HTML**.

W4.4 separa correctamente dos preguntas:

1. ¿el nuevo renderer produce páginas reales correctas?
2. ¿debe cambiar la topología pública?

Este frente responde solo la primera.

## 5. Validación materializada

`scripts/validate_v8_pilot_materialized.py` comprueba:

- manifest efímero;
- tres targets exactos;
- 49 HTML temporales;
- canonical candidate target;
- robots `noindex,follow`;
- cuatro CSS v8;
- `data-v8-pilot`;
- `data-source-catalog-id`;
- un único H1;
- ningún form;
- ningún internal link target que vuelva a `/productos/` o `/servicios/`;
- legacy pilots presentes.

## 6. Preservación legacy

El workflow ejecuta `git diff --exit-code` sobre:

- `productos/sistema-contractual-empresarial.html`;
- `servicios/sociedades-gobierno-inversion.html`;
- `servicios/direccion-juridica-externa.html`.

La existencia del target no autoriza todavía a modificar el legacy.

## 7. Browser contract

`tests/e2e/v8-pilot-materialization.spec.mjs` se ejecuta sobre:

- Chromium desktop;
- Chromium mobile;
- WebKit desktop.

Para cada piloto comprueba HTTP 200, `noindex,follow`, familia semántica correcta, source catalog id, H1, cero forms, meta ledger, situaciones de encaje, profundidad material, CTA al contacto canónico, commercial intent, related links target, disclosure por teclado, cero overflow horizontal y axe WCAG 2.1 A/AA sin violaciones `serious` o `critical`.

También verifica HTTP 200 y H1 de los tres legacy pilots.

## 8. Incidencia de accesibilidad y corrección de sistema

El primer Browser gate detectó únicamente `color-contrast` en texto secundario sobre `ivory` y etiquetas textuales de acento. No se rebajó axe.

La corrección fue sistémica:

- `--ml-muted`: `#65717a` → `#52606a`;
- `--ml-gold` permanece como oro de marca para bordes, líneas, puntos y acentos no textuales;
- `--ml-gold-ink: #765b38` gobierna texto pequeño dorado;
- `scripts/validate_v8_contrast_tokens.py` fija un gate determinista de 4.5:1 antes de Browser.

El nuevo muted supera AA sobre blanco, ivory y soft. El oro textual accesible supera AA sobre blanco e ivory.

## 9. Workflow y evidencia definitiva

Workflow: `.github/workflows/v80-pilot-materialization-candidate.yml`.

Secuencia certificada:

1. checkout;
2. Python/Node;
3. compile;
4. W4.2 route contract;
5. W4.3 non-activation gate;
6. contraste determinista de tokens;
7. canonical pipeline manifest;
8. materialización efímera;
9. validator 49-page;
10. legacy diff;
11. E2E syntax;
12. npm locked dependencies;
13. Chromium + WebKit;
14. server local;
15. Playwright desktop/mobile/WebKit + axe.

Evidencia final:

- Run: `32905639585`.
- Job: `97989006324`.
- Conclusión: **success**.
- Browser/Axe: **success**.
- Failure artifacts: skipped en el run final porque no hubo fallo.

## 10. Crítica visual independiente previa a W4.5

La revisión de screenshots reales obtenidos del run anterior —válidos para layout porque su única falla era contraste— confirma:

### Aciertos

- lenguaje visual sobrio y jurídico;
- jerarquía editorial clara;
- límites materiales visibles;
- responsive sin overflow;
- composición distinta de un catálogo genérico de tarjetas;
- profundidad jurídica accesible sin dominar la primera capa.

### Observación de polish

En mobile, el summary nativo `Profundidad jurídica y operativa / Ver alcance completo` adquiere demasiado peso visual respecto del contenido siguiente. Se registra para W4.5+ como polish posterior: compactar jerarquía y spacing sin ocultar profundidad material ni reemplazar el comportamiento nativo accesible de `<details>`.

No se mezcló esta preferencia visual con el cierre de accesibilidad W4.4.

## 11. No objetivos preservados

W4.4 no:

- commitea target HTML;
- añade rutas al sitemap;
- cambia robots productivo;
- cambia canonical legacy;
- cambia Home/navigation;
- modifica Builder/Pages;
- cambia `version.json`;
- publica RC02 Meridiano Contratos;
- despliega;
- mueve `stable`.

## 12. Gate hacia W4.5

W4.4 ya satisface el prerrequisito Browser/Axe.

El siguiente frente autorizado es **W4.5 — v8 Public-Tree Candidate**, que puede persistir exactamente los tres target HTML `noindex` en una rama candidate, mantener los 46 legacy completos y demostrar que la mera presencia física de las nuevas familias no altera indexación, navegación ni producción existente.

El canonical handoff, sitemap target, Home/navigation y activación v8 continúan fuera de este siguiente cambio.
