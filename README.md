# Meridiano Legal · Web canónica v5.4.0

Sitio público, responsive, static-first y autocontenido de Meridiano Legal, publicado mediante GitHub Pages. La v5.4 conserva íntegra la arquitectura jurídica, comercial, CRO, SEO, autoridad y privacidad acumulada hasta v5.3 y añade un nuevo estándar de aprobación: **la versión publicada debe funcionar también en navegador real antes de convertirse en `stable`**.

## Estado de la release

La publicación conserva **46 páginas HTML** y la arquitectura pública existente:

- 8 servicios profesionales;
- 8 productos jurídicos de alcance cerrado;
- 5 planes recurrentes;
- 8 lecturas sectoriales;
- 6 perspectivas jurídicas;
- página institucional de Firma;
- Centro Demo;
- Meridiano Empresas con información ficticia y `noindex,nofollow`;
- 1 hub de soluciones y 6 rutas de decisión empresarial.

La URL pública canónica continúa siendo `https://arendon7.github.io/MERDIANOLEGAL/`.

No se ha inventado ni activado un dominio personalizado, CRM, backend propio, Search Console o analítica externa. WhatsApp continúa siendo el canal real de contacto; la telemetría v5.0/v5.3 sigue siendo first-party, local, sin PII y sin transporte de red.

## v5.4 · Browser E2E como barrera real de publicación

Hasta v5.3, una candidata debía aprobar construcción, idempotencia, validadores estáticos, GitHub Pages y smoke HTTP. v5.4 añade un quinto nivel: **Playwright ejecutado contra la URL realmente desplegada**.

La secuencia de aprobación queda así:

1. construcción canónica;
2. segunda pasada con `git diff --exit-code`;
3. validadores v4.4→v5.4, JavaScript y JSON;
4. despliegue en GitHub Pages;
5. smoke HTTP de la URL pública;
6. Browser E2E sobre la URL desplegada;
7. promoción de `stable` únicamente si todo lo anterior es verde.

Una candidata puede, por tanto, existir temporalmente en Pages y seguir sin ser una release aprobada. `stable` representa ahora una versión que fue observada funcionando dentro del navegador, no solo una colección de archivos válidos.

## Navegadores y perfiles

`playwright.config.mjs` define tres proyectos:

- **Chromium desktop**: viewport 1440 × 1000;
- **Chromium mobile**: emulación Pixel 7;
- **WebKit desktop**: perfil Desktop Safari, viewport 1440 × 1000.

En CI se utiliza un solo worker para mantener trazabilidad determinista. Los reintentos solo se habilitan en CI y las evidencias de fallo se conservan mediante trace, screenshot y reporte HTML.

La instalación de Chromium y WebKit está limitada explícitamente a **360 segundos**. Si la infraestructura del runner se atasca, la release falla de forma controlada en lugar de permanecer indefinidamente en ejecución.

## Cobertura del Browser E2E

La suite se divide en web pública y Meridiano Empresas.

### Web pública

Se comprueba en navegador:

- portada, H1, navegación y seis rutas por necesidad;
- presencia de las 16 fichas profundas;
- navegación real desde una necesidad hacia una solución;
- ausencia de overflow horizontal relevante;
- carga de schema `ItemList` en solución;
- evento `solution_view` de v5.3;
- apertura de FAQ y evento `faq_open`;
- contrato de medición con `piiAllowed: false`, `networkTransport: false` y `persistentStorage: false`;
- paso perspectiva → solución y evento `authority_open`;
- paso sector → solución;
- formulario público completo;
- consentimiento de privacidad obligatorio;
- generación de referencia `ML-YYYYMMDD-XXXXX`;
- construcción correcta de URL `wa.me` sin enviar un mensaje real;
- evento local `lead_prepared`;
- honeypot y bloqueo de preparación automatizada;
- menú móvil, `Escape`, devolución de foco y bloqueo de scroll;
- errores JavaScript mediante `pageerror`;
- errores de consola mediante `console.error`.

Durante las pruebas, `window.open` se intercepta. La suite valida el handoff a WhatsApp, pero **no remite solicitudes reales**.

### Meridiano Empresas

La suite utiliza únicamente perfiles y datos ficticios y verifica:

- ingreso con el perfil demo de cliente;
- los 9 módulos del portal;
- navegación profunda mediante `?context=...#documentos`;
- creación de una vista previa documental ficticia;
- apertura de “Nueva solicitud”;
- creación de un ticket ficticio únicamente durante la sesión;
- funcionamiento de estas superficies en desktop, móvil y WebKit.

## Resultado final de Playwright

La ejecución funcional aprobada sobre la URL pública produjo:

- **30 entradas de test ejecutadas**;
- **28 aprobadas**;
- **2 omitidas por diseño**;
- **0 fallos**;
- **55,8 segundos** de ejecución de la suite.

Las dos omisiones corresponden al test específicamente móvil del menú, que no se ejecuta en los dos proyectos de escritorio. Ese mismo escenario sí se ejecuta y aprueba en Chromium mobile.

## Qué encontró el primer Browser E2E

El valor de v5.4 quedó demostrado en su primera ejecución. La candidata había aprobado Pages y smoke HTTP, pero Playwright terminó con **18 aprobadas, 2 omitidas y 10 fallidas**. `stable` no avanzó.

El análisis separó tres categorías:

### 1. Evento inicial de medición perdido — defecto real

`measurement-v53.js` se cargaba de forma síncrona después de scripts `defer` de runtime/telemetría. En navegador, `measurement-v53.js` intentaba emitir `solution_view` antes de que `MeridianoTelemetry` existiera, por lo que la primera vista se perdía.

La corrección v5.4 normaliza las 20 páginas instrumentadas —6 soluciones, 6 perspectivas y 8 sectores— para cargar:

```html
<script defer src="../measurement-v53.js"></script>
```

El orden efectivo queda alineado con `telemetry-v50.js` y el evento inicial es observable en navegador.

### 2. Formulario sin submit — defecto de la prueba, no de producción

La primera prueba completaba nombre, correo, necesidad y mensaje, pero omitía marcar el checkbox obligatorio de privacidad. El propio navegador bloqueaba correctamente el `submit` por validación HTML nativa antes de llegar a JavaScript.

No se relajó el formulario. Se corrigió la prueba para comportarse como un usuario válido y aceptar expresamente privacidad antes del envío simulado.

El mismo ajuste se aplicó al caso honeypot para comprobar el control anti-bot después de cumplir los requisitos legítimos del formulario.

### 3. “Nueva solicitud” oculta en móvil — defecto responsive real

El portal contenía una regla previa:

```css
.portal-header-actions .btn { display: none; }
```

en viewport móvil. El botón existía en DOM, pero no era accionable y no había una alternativa equivalente visible.

v5.4 incorpora una normalización responsive administrada que mantiene accesible el CTA “Nueva solicitud” en móvil, con tamaño y wrapping adecuados.

## Idempotencia de las correcciones

La primera corrección funcional reveló además una diferencia puramente determinista en `demo.html`: una segunda reconstrucción cambiaba la indentación de dos enlaces CSS del `<head>`.

La calidad bloqueó Pages antes del deploy. No se excluyó `demo.html` del diff.

El aplicador final normaliza explícitamente esas líneas y la siguiente construcción produjo **diff cero**. La corrección browser y la salida HTML son ahora reproducibles en pasadas sucesivas.

## Archivos v5.4

- `package.json`: dependencia de QA de navegador, fijada en `@playwright/test` 1.55.0.
- `.gitignore`: excluye `node_modules`, reportes y resultados Playwright.
- `playwright.config.mjs`: tres proyectos, timeouts, retries y artefactos de fallo.
- `tests/e2e/helpers.mjs`: guardas de errores runtime y overflow.
- `tests/e2e/public-site.spec.mjs`: recorridos de web pública, conversión, medición y móvil.
- `tests/e2e/demo.spec.mjs`: login, módulos, documentos y solicitudes ficticias del portal.
- `scripts/validate_browser_v54.py`: gate estático de la infraestructura Browser E2E y de las correcciones v5.4.
- `scripts/apply_authority_v53.py`: desde v5.4 conserva v5.3 y añade las dos normalizaciones browser detectadas por la suite.
- `.github/workflows/pages.yml`: incorpora `Browser E2E on deployed Pages` antes de `stable`.
- `.github/workflows/build-canonical.yml`: vigila las nuevas fuentes de QA.
- `RELEASE-v5.4.md`: nota técnica detallada de esta release.

## Construcción y aprobación canónica

La construcción continúa culminando en:

```bash
python3 scripts/apply_cro_v52.py
python3 scripts/apply_authority_v53.py
```

El aplicador de autoridad es version-aware: desde v5.4 conserva la salida v5.3 y normaliza el orden de medición y la accesibilidad del CTA demo móvil.

`Site Quality and Deploy` exige después:

- diff cero;
- integridad de 46 páginas y recursos;
- catálogo estático de 16 fichas;
- conversión v4.4;
- UX v4.5, v4.6 y v4.7;
- calidad static-first v4.8;
- operación pública v4.9;
- producción v5.0;
- rutas v5.1;
- CRO/SEO v5.2;
- autoridad y medición v5.3;
- infraestructura/correcciones browser v5.4;
- selector, contexto, editorial, visual, JavaScript y JSON;
- deploy Pages;
- smoke HTTP;
- Browser E2E;
- `stable`.

## Principios que se mantienen

- No inventar clientes, testimonios, casos de éxito ni resultados.
- No duplicar precios fuera de las fuentes públicas canónicas.
- No afirmar que existe un backend que la web no tiene.
- No enviar datos personales a la telemetría.
- No activar analítica externa, Search Console, CRM o dominio personalizado sin configuración real.
- No debilitar un gate para hacer pasar una release.
- Mantener `main` como fuente vigente y `stable` como último commit que superó **archivo + HTTP + navegador**.

## Próximo ciclo lógico

Después de v5.4, la prioridad ya no debería ser añadir capas por inercia. Los siguientes ciclos de mayor valor son:

1. **performance y accesibilidad medidos en navegador**, incluyendo presupuestos objetivos y auditorías reproducibles;
2. optimización del costo/tiempo del Browser E2E sin perder cobertura;
3. dominio propio y Search Console únicamente cuando existan datos reales;
4. conexión de un proveedor de analítica únicamente si se decide hacerlo y respetando el contrato de eventos sin PII;
5. mejoras comerciales posteriores basadas en evidencia de uso real, no en supuestos de conversión.

El historial acumulado de releases anteriores se conserva en `CHANGELOG.md`.