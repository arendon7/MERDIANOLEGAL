# W4.5 — v8 Public-Tree Candidate

Fecha: 2026-08-25  
Estado: **PASS — persisted public-tree candidate certificado**.  
Dependencia: W4.4 Browser/Axe PASS (`32905639585`).

## 1. Objetivo

Persistir en Git exactamente los tres HTML v8 ya probados de forma efímera, todavía como `noindex,follow`, sin activar su descubrimiento público ni modificar la semántica SEO de las 46 rutas legacy.

## 2. Targets persistidos

- SO07 `/soluciones/sistema-contractual-empresarial.html`.
- PR02 `/practicas/corporativo-societario-gobierno.html`.
- RC01 `/servicios-continuos/direccion-juridica-externa.html`.

El árbol W4.5 queda en **49 HTML = 46 legacy + 3 target**.

## 3. Incorporación reproducible

Los HTML no fueron reconstruidos manualmente. El renderer source-driven permaneció como autoridad.

### Bootstrap

El primer gate W4.5:

1. partió de 0/3 targets persistidos;
2. generó los tres targets en un workspace limpio;
3. validó topología temporal 49;
4. ejecutó Chromium desktop/mobile, WebKit y axe;
5. publicó los bytes generados como artefacto.

Run bootstrap: `32906187034` — **success**.

### Persistencia inicial

El workflow incorporó únicamente los tres paths allowlisted después del Browser/Axe PASS.

GitHub no ejecuta automáticamente un segundo workflow normal sobre el commit generado por `github-actions[bot]`; el run correspondiente quedó `action_required` sin jobs. Este estado se trató como ausencia de certificación, no como PASS.

## 4. Hallazgo de integridad de enlaces

Antes de declarar W4.5 cerrado se auditó la salida persistida y se detectó que ciertos relacionados habían sido traducidos al destino arquitectónico v8 aunque esas páginas aún no existían físicamente. Ejemplos de targets futuros:

- `/practicas/contratacion-negocios.html`;
- `/practicas/legal-operations-transformacion-juridica.html`;
- `/soluciones/empresa-juridicamente-organizada.html`;
- `/soluciones/empresa-lista-para-inversion.html`.

Aunque los pilotos estaban `noindex`, aceptar esos enlaces habría producido 404 al navegar desde una URL candidate conocida.

No se modificó el Route Contract: el destino arquitectónico continúa siendo v8.

Se añadió una política de rollout distinta:

**`target-if-materialized-else-legacy`**

- si el target v8 ya existe en la wave, el relacionado apunta al target;
- si todavía no existe, conserva la URL legacy física y válida;
- cuando el target entra en una wave posterior, el fallback desaparece al regenerar.

Esto separa correctamente **destino arquitectónico** de **disponibilidad física actual**.

## 5. Gates añadidos por el hallazgo

### `validate_v8_pilot_materialized.py`

Ahora exige que todo enlace local visible de los tres targets resuelva a un recurso físico existente.

### `validate_v8_public_tree.py`

En modo final persisted exige:

- 49 HTML exactos;
- target noindex;
- canonical candidate;
- legacy íntegro y self-canonical;
- cero activación en Home/sitemap/version;
- cero forms nuevos;
- todos los links locales resolviendo físicamente.

Incluye `--preflight` únicamente para permitir un refresh seguro de targets stale antes de reemplazarlos. El preflight nunca sustituye el gate final.

### Browser E2E

`tests/e2e/v8-pilot-materialization.spec.mjs` ahora sigue cada relacionado y exige HTTP 200 además de responsive, keyboard y axe.

## 6. Refresh seguro

El workflow W4.5 distingue tres estados:

1. `bootstrap`: 0/3 targets.
2. `refresh`: 3/3 existen, pero divergen de la salida generada actual.
3. `match`: 3/3 existen y coinciden byte-for-byte.

Un estado `refresh`:

- no se acepta como cierre;
- genera un candidate limpio;
- valida links y Browser/Axe sobre el generado;
- reemplaza atómicamente solo los tres targets después del PASS;
- exige un run posterior en estado `match`.

Run refresh con política de links corregida: `32906903486` — **success**.

## 7. Evidencia final persisted

Para evitar que el commit de bot fuese tratado como certificación, se generó un commit no funcional posterior que no cambió los tres target HTML y disparó el mismo gate sobre un actor normal.

Run final: `32907133921`  
Job: `97993558730`  
Conclusión: **success**.

Resultado del run final:

- physical mode persisted: PASS;
- source truth: PASS;
- no-activation preflight: PASS;
- protected public surfaces unchanged: PASS;
- clean generated candidate: PASS;
- generated/persisted byte parity: **MATCH**;
- full persisted public-tree validator: PASS;
- artifact refresh: skipped correctamente;
- write/refresh step: skipped correctamente;
- Chromium desktop: PASS;
- Chromium mobile: PASS;
- WebKit desktop: PASS;
- related-link HTTP integrity: PASS;
- axe WCAG 2.1 A/AA serious/critical: PASS.

## 8. No activación preservada

W4.5 termina con:

- targets `noindex,follow`;
- targets fuera de `sitemap.xml`;
- Home/navigation sin links v8 target;
- 46 legacy físicamente presentes;
- legacy indexables conservando self-canonical;
- `version.json` todavía v7.4.0;
- Builder/Pages productivo sin integración v8;
- `robots.txt` sin cambio;
- un único formulario físico canónico;
- analytics sin activación;
- RC02 Meridiano Contratos `publishable=false`;
- `stable` intacta.

## 9. Crítica visual abierta

Sigue registrada como polish no bloqueante:

- en mobile, el summary `Profundidad jurídica y operativa / Ver alcance completo` tiene demasiado peso visual.

Debe tratarse en una wave posterior sin esconder profundidad material ni romper `<details>` nativo.

## 10. Gate hacia W4.6

W4.5 está certificado como **Public-Tree Candidate**, pero **no puede fusionarse aisladamente a `main`**.

La razón es estructural: el pipeline v6 actual continúa suponiendo exactamente seis HTML dentro de `/soluciones/`. Por tanto, la mera presencia del séptimo target v8 haría fallar `validate_experience_solutions_v60.py` en Builder/Pages.

El siguiente frente obligatorio es **W4.6 — Pipeline Compatibility Candidate**:

- introducir una fase/topología explícita v8;
- mantener el contrato v6 intacto para baselines v6/v7;
- integrar v8 como extensión version-gated, no como paso histórico 31;
- mantener Builder == Pages == canonical manifest;
- incluir `/practicas/` y `/servicios-continuos/` en las superficies canónicas aplicables;
- demostrar idempotencia sin activar canonical handoff, sitemap ni navegación v8.
