# W4.5 — v8 Public-Tree Candidate

Fecha: 2026-08-25
Estado inicial: bootstrap reproducible.
Dependencia: W4.4 Browser/Axe PASS (`32905639585`).

## Objetivo

Persistir en Git exactamente los tres HTML v8 ya probados de forma efímera, todavía como `noindex,follow`, sin activar su descubrimiento público ni modificar la semántica SEO de las 46 rutas legacy.

## Principio de incorporación

Los HTML no se reconstruyen manualmente. El renderer source-driven continúa siendo autoridad de materialización.

W4.5 usa dos fases:

### Fase A — bootstrap

Si los tres targets aún no existen:

1. CI copia el checkout a un workspace temporal;
2. ejecuta el materializador W4.4;
3. valida 49 HTML en el workspace temporal;
4. ejecuta Browser/Axe;
5. publica como artefacto únicamente los tres target HTML generados.

### Fase B — persisted candidate

Cuando los tres targets ya existen en la rama:

1. CI genera nuevamente los tres targets en un workspace limpio alterno;
2. compara byte-for-byte cada generado contra cada persistido;
3. valida topología 49 en el árbol real;
4. valida `noindex`, canonical candidate y ausencia de forms;
5. comprueba que sitemap/Home/navigation no activaron v8;
6. comprueba legacy preservation;
7. ejecuta Browser/Axe directamente sobre los archivos persistidos.

## Targets

- SO07 `/soluciones/sistema-contractual-empresarial.html`.
- PR02 `/practicas/corporativo-societario-gobierno.html`.
- RC01 `/servicios-continuos/direccion-juridica-externa.html`.

## No activación

La mera presencia física de estas tres páginas no equivale a lanzamiento v8.

Durante W4.5:

- `robots=noindex,follow` en target;
- target fuera de `sitemap.xml`;
- target sin enlace desde Home/navigation principal;
- legacy conserva self-canonical;
- `version.json` continúa v7.4;
- no cambio a Builder/Pages productivo;
- no redirect/alias activo;
- no RC02;
- no movimiento de `stable`.

## Gate de salida

W4.5 termina solo con:

- tres HTML persistidos;
- byte parity renderer/persistido;
- route/truth/contrast gates PASS;
- 49-page candidate contract PASS;
- Browser Chromium desktop/mobile + WebKit PASS;
- axe PASS;
- old routes PASS;
- sitemap y Home sin activación;
- stable intacta.

El siguiente frente W4.6 podrá abordar integración version-gated al pipeline y candidate deployment controlado, pero no canonical handoff automático.
