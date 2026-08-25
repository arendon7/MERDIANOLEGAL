# W4.4 — v8 Pilot Materialization Candidate

Fecha: 2026-08-25
Estado: candidate efímero; no publicación.
Dependencias: W4.1 → W4.2 → W4.3.

## 1. Objetivo

Probar HTML v8 real en navegador antes de añadir una sola ruta target al árbol público del repositorio.

W4.4 transforma el renderer W4.3 en tres archivos físicos **solo dentro del checkout desechable de GitHub Actions**. Al terminar el job, esos archivos desaparecen.

La rama sigue conteniendo 46 HTML públicos.

---

## 2. Targets efímeros

### SO07

`/soluciones/sistema-contractual-empresarial.html`

Fuente:

`catalog-products-v41/p07-contractual.json`

### PR02

`/practicas/corporativo-societario-gobierno.html`

Fuente:

`catalog-services-v42/s04-societario.json`

### RC01

`/servicios-continuos/direccion-juridica-externa.html`

Fuente:

`catalog-services-v42/s02-direccion.json`

---

## 3. Materializador

`scripts/materialize_v8_pilot.py`

Contrato:

- raíz de salida obligatoria;
- materializar sobre working tree exige `--allow-working-tree` explícito;
- solo tres pilotos;
- no sobrescribe targets;
- conserva `noindex,follow`;
- no crea forms;
- emite `.v8-pilot-materialization.json`.

No pertenece aún al builder canónico.

---

## 4. Topología temporal

Antes de materializar:

- 46 HTML.

Durante Browser CI:

- 46 legacy;
- 3 target;
- total = 49 HTML.

Después del job:

- el runner se destruye;
- la rama continúa en 46 HTML.

Esto separa correctamente dos preguntas:

1. ¿el nuevo renderer produce páginas reales correctas?
2. ¿debe cambiar la topología pública?

W4.4 responde solo la primera.

---

## 5. Validator materializado

`scripts/validate_v8_pilot_materialized.py`

Debe comprobar:

- manifest efímero;
- tres targets exactos;
- 49 HTML temporales;
- canonical candidate target;
- robots `noindex,follow`;
- referencia a los cuatro CSS v8;
- `data-v8-pilot`;
- `data-source-catalog-id`;
- un único H1;
- ningún form;
- ningún enlace interno target que vuelva a `/productos/` o `/servicios/`;
- legacy pilots presentes.

---

## 6. Legacy preservation

El workflow ejecuta `git diff --exit-code` sobre:

- `productos/sistema-contractual-empresarial.html`;
- `servicios/sociedades-gobierno-inversion.html`;
- `servicios/direccion-juridica-externa.html`.

La existencia del target no autoriza todavía a modificar el legacy.

---

## 7. Browser contract

`tests/e2e/v8-pilot-materialization.spec.mjs`

Se ejecuta sobre:

- Chromium desktop;
- Chromium mobile;
- WebKit desktop.

Para cada piloto comprueba:

1. HTTP 200;
2. `noindex,follow`;
3. familia visual/semántica correcta;
4. source catalog id correcto;
5. un H1 con título target;
6. cero forms;
7. meta ledger;
8. cuatro situaciones de encaje;
9. profundidad material suficiente;
10. CTA al único contacto canónico;
11. commercial intent preservado;
12. related links ya en rutas target;
13. disclosure operable con teclado;
14. cero overflow horizontal;
15. axe WCAG 2.1 A/AA sin violaciones `serious` o `critical`.

Además verifica HTTP 200 y H1 en los tres legacy pilots.

---

## 8. Ajuste de accesibilidad previo a Browser

La identidad v6 usa oro `#a88454`.

Ese tono se conserva como:

- borde;
- línea;
- punto de timeline;
- acento no textual.

Para texto pequeño se introduce:

`--ml-gold-ink: #765b38`.

Motivo:

- el oro de marca original no alcanza 4.5:1 sobre blanco para texto pequeño;
- el nuevo token conserva la familia cromática y supera el umbral AA sobre blanco e ivory;
- no se altera la identidad principal.

Aplicaciones:

- eyebrow;
- índices numéricos;
- numeración de ledgers;
- marker textual de la familia Solution.

---

## 9. Workflow

`.github/workflows/v80-pilot-materialization-candidate.yml`

Secuencia:

1. checkout;
2. Python/Node;
3. compile;
4. W4.2 route contract;
5. W4.3 non-activation gate;
6. canonical pipeline manifest;
7. materialización efímera;
8. validator 49-page;
9. legacy diff;
10. E2E syntax;
11. npm locked dependencies;
12. Chromium + WebKit;
13. server local;
14. Playwright desktop/mobile/WebKit + axe;
15. failure artifacts.

---

## 10. Estado observado durante construcción

El primer corte W4.4 comprobó exitosamente antes de browser:

- compile PASS;
- W4.2 PASS;
- W4.3 PASS;
- materialización PASS;
- 49-page topology PASS;
- legacy unchanged PASS;
- E2E syntax PASS.

El resultado Browser final debe registrarse únicamente desde GitHub Actions; no se presume.

---

## 11. No objetivos

W4.4 no:

- commitea los target HTML;
- añade rutas al sitemap;
- cambia robots productivo;
- cambia canonical legacy;
- cambia Home/navigation;
- modifica Builder/Pages;
- cambia version.json;
- publica RC02;
- despliega;
- mueve stable.

---

## 12. Gate hacia W4.5

W4.5 solo puede abrirse si W4.4 demuestra Browser PASS.

Entonces W4.5 podrá estudiar:

- comprometer tres target HTML `noindex` en una rama candidate;
- version-gate de validators que hoy asumen 46 HTML;
- extensión v8 del pipeline canónico;
- idempotencia de materialización;
- candidate Pages sin canonical handoff;
- visual review con screenshots.

No se modifica todavía ningún legacy canonical en el mismo cambio que introduce los targets.
