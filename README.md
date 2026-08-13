# Meridiano Legal · Web canónica v5.21.0

Sitio público, responsive, static-first y autocontenido de Meridiano Legal, publicado mediante GitHub Pages.

URL pública: `https://arendon7.github.io/MERDIANOLEGAL/`

## Estado actual

La publicación conserva 46 páginas HTML, 16 fichas profundas y un único formulario físico canónico. `stable` solo se mueve cuando builder, idempotencia, Pages, smoke, Browser E2E, axe, Lighthouse y release-health están verdes.

## Capas vigentes

- **v5.8:** claridad de compra;
- **v5.9:** calificación comercial y privacidad;
- **v5.10:** intención contextual, propuesta y cierre;
- **v5.11:** solicitud, propuesta, aceptación e inicio;
- **v5.12:** modalidades y prueba verificable;
- **v5.13:** continuidad hasta formulario/WhatsApp;
- **v5.14:** recomendación explicable sin scoring;
- **v5.15:** recomendación→acción;
- **v5.16:** UX móvil y accesibilidad;
- **v5.17:** continuidad manual del handoff y stale protection;
- **v5.18:** observabilidad verificable del handoff sin PII;
- **v5.19:** progressive disclosure por intención explícita;
- **v5.20:** compresión de la decisión comercial en portada;
- **v5.21:** frontera verificable entre demo y capacidades reales.

v5.21 no añade un portal productivo: hace técnicamente imposible presentarlo como activo mientras no exista. La demo continúa siendo ficticia, client-side y `noindex`; el estado real del portal se declara en configuración y se comprueba en CI y navegador.

## v5.21 · Veracidad de capacidades

La configuración canónica declara actualmente:

```json
"capabilities": {
  "client_portal": {
    "enabled": false,
    "url": ""
  }
}
```

Consecuencias públicas y técnicas:

- no se presenta “Área de clientes” como capacidad activa;
- los 25 accesos públicos identificados hacia `demo.html` están rotulados como demo/demostrativos;
- `runtime-config.js` y `site-status.json` reflejan que el portal real está deshabilitado;
- `demo.html` conserva `data-capability-v521="demo-only"` y exactamente un `noindex,nofollow`;
- `demo.js` no inyecta un segundo meta robots;
- una futura activación exige URL HTTPS real, distinta de `demo.html`, y un acceso público verificable.

No se añadieron autenticación, cuentas reales, backend, CRM, almacenamiento servidor, PII, email transaccional, firma electrónica, pagos, agenda ni carga documental.

## Evidencia funcional v5.21

PR funcional #79 + hotfixes #80/#81 → SHA certificado `b2a6d4d4d2608362e86b53ea4cc197cd7ce33cc1`.

Run final `31658340092`:

- `main == stable == b2a6d4d4d2608362e86b53ea4cc197cd7ce33cc1` al cierre funcional;
- builder + idempotencia + validadores históricos: PASS;
- Pages + smoke: PASS;
- Browser E2E + axe: 43 observados → 41 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- cobertura Browser ampliada frente a v5.20, no reducida;
- 7 superficies axe conservadas;
- Lighthouse 6/6 PASS;
- accesibilidad Lighthouse 1.00 en las seis superficies;
- performance Lighthouse 0.98–1.00;
- portada: performance 1.00, accesibilidad 1.00, LCP 1410 ms, CLS 0, TBT 91 ms;
- máximo global: LCP 1410 ms, CLS 0.087, TBT 91 ms;
- CI hasta `stable`: 178 s, 36.2% mejor que baseline v5.5 de 279 s;
- cobertura reducida: no;
- budgets relajados: no.

## Integraciones externas: estado verdadero

Activas: GitHub Pages, WhatsApp como handoff manual, contexto comercial client-side, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estático/noindex y pipeline de certificación.

Explícitamente deshabilitada: portal real de clientes.

No declarar activas sin configuración real: autenticación/cuentas reales, analítica externa, CRM/backend, almacenamiento servidor del formulario, email transaccional, firma electrónica, pagos, agenda o carga documental.

## Documentación

- `RELEASE-v5.21.md`: frontera de capacidades, incidencias y evidencia final;
- `RELEASE-v5.20.md`: compresión de decisión;
- `RELEASE-v5.19.md`: foco comercial adaptativo;
- `knowledge/HOME.md`: entrada a memoria operativa.

## Principios

- No reducir cobertura ni relajar budgets para hacer pasar una candidata.
- No mover `stable` con un gate rojo.
- No inventar integraciones, clientes, testimonios ni resultados.
- No transmitir PII en telemetría.
- No inferir intención comercial que el usuario no haya declarado.
- No convertir acciones locales en afirmaciones sobre envío, lectura, aceptación o conversión.
- Una demo no equivale a una capacidad productiva.
- Graphify orienta; `main`, Pages, validadores y tests deciden.
