# Meridiano Legal — Tarea activa

Actualizado: 2026-08-18.

## Estado base certificado

- Release certificada de partida: **v6.0.0 — Experience System**.
- `main == stable == 65b45f43dad812474c065a1810ceb56bd602d835` al abrir este ciclo.
- Canal base: `github-pages-production-experience-system-certified`.
- GitHub Pages sirve v6.0.0 hasta que el ciclo v6.1 complete promoción automática.
- Browser E2E/axe público v6.0: 122 PASS, 2 skipped, 0 failed.
- Lighthouse público v6.0: 6/6 superficies PASS; performance y accesibilidad 1.00 en la muestra; LCP 906–1.626 ms; CLS 0; TBT 0.
- No existe evidencia que justifique un ciclo de performance, accesibilidad o reparación funcional inmediata.

## Ciclo funcional activo

**v6.1.0 — Measurement Readiness / observabilidad privacy-first.**

Rama: `feat/v61-measurement-readiness`.
PR: `#154` (Draft hasta certificación same-SHA).
Release candidate: `version.json = 6.1.0`, fecha `2026-08-18`, canal `github-pages-measurement-readiness-candidate`.

### Problema observable

La web modela correctamente el funnel y sus etapas, pero la evidencia solo vive en memoria del navegador:

- `analytics.enabled=false`;
- `provider=none`;
- sin transporte de red;
- sin persistencia;
- sin identificador cross-session;
- Search Console aún no está configurado.

Por tanto podemos certificar que el recorrido funciona, pero no responder con datos agregados reales preguntas como dónde abandonan visitantes, qué rutas llegan con mayor frecuencia a contacto o cuántas sesiones alcanzan handoff.

### Hipótesis

Si Meridiano incorpora una capa de medición gobernada que transforme únicamente las etapas ya saneadas del funnel en eventos externos allowlisted —sin propiedades custom, PII del formulario, referencias, cookies propias, persistencia o fingerprinting— podremos habilitar medición agregada cuando exista un proveedor real y una política actualizada, sin reescribir el funnel ni degradar privacidad.

### Alcance de readiness

1. contrato `assets/data/v6/measurement-readiness-v61.json`;
2. adapter `assets/js/v6/analytics-adapter-v61.js` compatible con el hook histórico `MeridianoAnalyticsAdapter`;
3. fuente externa única: evento saneado `meridiano:funnel-v529`, aceptando exclusivamente `detail.stage`;
4. raw `adapter.track(name,event)` conservado por compatibilidad pero deliberadamente `no-op`;
5. seis eventos externos de etapa: need, offer, evidence, decision, contact y handoff;
6. payload **custom aportado por Meridiano** limitado al nombre del evento; cero propiedades custom;
7. deduplicación: primer evento por etapa durante la vida de la página;
8. Plausible como primer adapter preparado, pero deshabilitado y sin site token real;
9. pageviews automáticos de Plausible explícitamente deshabilitados (`autoCapturePageviews:false`);
10. cualquier metadata estándar que el proveedor procese al transmitir un custom event queda sujeta a revisión y actualización previa de la política antes de activar;
11. Umami evaluado como alternativa, no declarado como soporte runtime en esta fase;
12. Cloudflare Web Analytics evaluado para RUM/pageviews, pero no elegido para el funnel porque no aporta custom events en el estado revisado;
13. integración dentro del normalizador Experience v6 existente, sin crear un paso 31;
14. validator estático fail-closed;
15. E2E que demuestre cero red externa con producción apagada y descarte de payload contaminado;
16. topología exacta: **43 superficies instrumentadas + 3 deliberadamente sin telemetría (`404.html`, `demo.html`, `experiencia.html`)**;
17. gate dedicado `.github/workflows/v61-measurement-readiness.yml` que ejecuta contrato, Governance y suite Browser completa;
18. Builder y Canonical Equivalence cubren los assets v6.1 mediante su filtro existente `assets/**`;
19. `sync_public_version.py` sincroniza rótulo público, dos JS demostrativos, `runtime-config.js` y `site-status.json` desde `version.json + site-config.json` y expone `--check` fail-closed;
20. Candidate, Browser, Measurement y Canonical Equivalence reproducen esa sincronización antes de validar una baseline v6;
21. Canonical Equivalence distingue estrictamente wiring v6.1 (43 HTML), bump de release (4 superficies no-HTML adicionales, con `index.html` solapado) y baseline ya materializada.

## Criterios de éxito

- `analytics.enabled` continúa `false` en producción;
- no aparece ningún request a proveedor externo en E2E disabled;
- adapter carga antes de `telemetry-v50.js` en exactamente 43 superficies;
- `404.html`, `demo.html` y `experiencia.html` permanecen sin adapter porque no tenían telemetría previa;
- PII, nombre, empresa, correo, mensaje, referencia, presupuesto y urgencia no forman parte del payload custom de Meridiano;
- `event` y `target` del funnel saneado no se exportan como propiedades;
- eventos/etapas desconocidos se descartan;
- solo seis etapas allowlisted pueden convertirse en eventos externos;
- no se introducen pageviews automáticos, `fetch`, `XMLHttpRequest`, `sendBeacon`, storage, cookies o fingerprinting propios;
- `version.json`, rótulo público, `runtime-config.js` y `site-status.json` quedan sincronizados en el mismo release;
- 46 HTML, 16 fichas, 1 formulario y 30 pasos canónicos permanecen intactos;
- Browser/axe, Lighthouse, Governance y equivalencia continúan sin relajación;
- cambios futuros en los assets de measurement vuelven a disparar Builder/Equivalence y el gate dedicado v6.1;
- `stable` solo se mueve por la cadena post-deploy después de Browser + Lighthouse verdes.

## Fuera de alcance de esta fase

- activar Plausible u otro tercero;
- crear una cuenta/proyecto de analytics sin decisión explícita;
- incluir un `pa-...` ficticio;
- cambiar la política de privacidad como si ya existiera tratamiento por un tercero;
- asumir que el request estándar del proveedor contiene únicamente el nombre del evento;
- enviar propiedades custom, contenido de formulario o identificadores propios;
- inferir mensaje enviado, propuesta aceptada, encargo iniciado o cliente convertido;
- cambiar copy, layout, productos, servicios, precios o funnel público por intuición antes de tener datos.

## Condición para futura activación

Una activación real requerirá, como mínimo:

1. proveedor seleccionado;
2. identificador/snippet auténtico del sitio;
3. revisión técnica de la metadata estándar que el proveedor transmite/procesa;
4. revisión y actualización previa de la política pública y configuración;
5. validación del tráfico saliente exacto con pageviews automáticos deshabilitados;
6. confirmación de que Meridiano sigue aportando únicamente nombres de evento sin propiedades custom o aprobación expresa de cualquier ampliación;
7. gates verdes y promoción automática de `stable`.

Hasta entonces, v6.1 es **readiness**, no analítica activa.
