# Meridiano Legal · Web canónica v5.20.0

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
- **v5.20:** compresión de la decisión comercial en portada.

v5.20 no elimina contratos anteriores: consolida su presentación pública. Las seis rutas por situación empresarial continúan como primer punto de entrada y después aparece una única superficie con cinco modalidades de contratación. Las 16 fichas profundas y el formulario/handoff permanecen íntegros.

## v5.20 · Compresión de decisión

La portada deja de pedir al prospecto que decida varias veces entre producto, servicio, diagnóstico o capacidad recurrente.

La arquitectura final es:

1. **Situación empresarial:** seis rutas por necesidad.
2. **Modalidad:** diagnóstico, auditoría, producto cerrado, servicio especialista o capacidad recurrente.

El estándar verificable de propuesta permanece visible y la comparación de límites/alternativas sigue disponible mediante `<details>`.

La salida final ya no materializa el bloque separado de “Forma de contratar” v5.8 ni la sección histórica `#elegir`. Esta redundancia se elimina del HTML; no se oculta con CSS.

## Evidencia funcional v5.20

PR funcional #74 y hotfixes de compatibilidad #75/#76 → SHA certificado `85bdcfc9b52172e085dfa9b1df8e8d081b136233`.

Run `31651473515`:

- `main == stable == 85bdcfc9b52172e085dfa9b1df8e8d081b136233` al cierre funcional;
- builder + idempotencia + validadores históricos: PASS;
- Pages + smoke: PASS;
- Browser E2E + axe: 37 → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- 7 superficies axe limpias;
- Lighthouse 6/6 PASS;
- accesibilidad Lighthouse 1.00 en las seis superficies;
- performance 0.98–1.00;
- portada: performance 1.00, accesibilidad 1.00, LCP 1421 ms, CLS 0, TBT 83 ms;
- CI hasta `stable`: 191 s, 31.5% mejor que baseline v5.5 de 279 s;
- cobertura reducida: no;
- budgets relajados: no.

## Integraciones externas: estado verdadero

Activas: GitHub Pages, WhatsApp como handoff manual, contexto comercial client-side, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estático/noindex y pipeline de certificación.

No declarar activas sin configuración real: analítica externa, CRM/backend, almacenamiento servidor del formulario, email transaccional, firma electrónica, pagos, agenda o carga documental.

## Documentación

- `RELEASE-v5.20.md`: compresión de decisión, compatibilidad y evidencia final;
- `RELEASE-v5.19.md`: foco comercial adaptativo;
- `RELEASE-v5.18.md`: observabilidad verificable del handoff;
- `knowledge/HOME.md`: entrada a memoria operativa.

## Principios

- No reducir cobertura ni relajar budgets para hacer pasar una candidata.
- No mover `stable` con un gate rojo.
- No inventar integraciones, clientes, testimonios ni resultados.
- No transmitir PII en telemetría.
- No inferir intención comercial que el usuario no haya declarado.
- No convertir acciones locales en afirmaciones sobre envío, lectura, aceptación o conversión.
- Graphify orienta; `main`, Pages, validadores y tests deciden.
