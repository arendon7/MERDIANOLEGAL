# Release v5.4.0 · Browser E2E y QA responsive real

Fecha: 2026-08-08

## Objetivo

La v5.4 incorpora Playwright como barrera de aprobación posterior al despliegue. La finalidad no es añadir contenido ni rediseñar la web, sino comprobar que la versión realmente servida se comporta correctamente en navegador antes de mover `stable`.

## Arquitectura del gate

La secuencia de release queda:

`build canónico → idempotencia → validadores → GitHub Pages → smoke HTTP → Browser E2E → stable`

`stable` depende expresamente del job `browser_e2e`.

Playwright usa tres proyectos:

- Chromium desktop, 1440 × 1000;
- Chromium mobile, emulación Pixel 7;
- WebKit desktop, perfil Safari, 1440 × 1000.

La instalación de Chromium/WebKit tiene un timeout externo de 360 s y el job completo un timeout de 12 minutos. Los traces, screenshots, resultados y reporte HTML solo se conservan cuando existe un fallo.

## Cobertura

La suite cubre:

- portada y seis rutas de necesidad;
- 16 enlaces a fichas profundas;
- navegación real a solución de IA;
- overflow horizontal;
- `ItemList` de solución;
- `solution_view`, `faq_open` y `authority_open`;
- contrato de medición sin PII/red/persistencia;
- perspectiva y sector hacia solución;
- formulario, consentimiento, referencia `ML-*` y handoff WhatsApp interceptado;
- `lead_prepared`;
- honeypot;
- menú móvil + Escape + devolución de foco;
- `pageerror` y `console.error`;
- login ficticio de Meridiano Empresas;
- nueve módulos demo;
- hash profundo hacia Documentos guiados;
- generación de vista previa ficticia;
- “Nueva solicitud” y ticket de sesión.

No se envían mensajes reales de WhatsApp ni se utilizan datos reales de cliente.

## Primera ejecución: el gate bloqueó correctamente la release

La primera candidata v5.4 aprobó:

- construcción canónica;
- idempotencia;
- matriz estática;
- GitHub Pages;
- smoke HTTP.

Sin embargo, Browser E2E produjo:

- 18 pruebas aprobadas;
- 2 omitidas;
- 10 fallidas.

`stable` no avanzó.

### Hallazgo 1 · `solution_view` se perdía

Causa: `measurement-v53.js` se ejecutaba de forma síncrona mientras `telemetry-v50.js` estaba marcado `defer`. Al cargar la página, la medición intentaba usar el bus antes de que este existiera.

Corrección: las 20 páginas instrumentadas cargan `measurement-v53.js` con `defer`, preservando el orden del documento con la telemetría.

### Hallazgo 2 · el formulario no hacía submit en la prueba

No era un defecto de producción. El test olvidaba aceptar el checkbox HTML `required` de privacidad. El navegador bloqueaba correctamente la presentación antes del handler JavaScript.

Corrección: tanto el flujo de contacto como la prueba honeypot aceptan privacidad antes de simular el submit. No se relajó ningún requisito público.

### Hallazgo 3 · “Nueva solicitud” estaba oculta en móvil

Era un defecto responsive real. Una regla previa ocultaba `.portal-header-actions .btn` en viewports menores o iguales a 760 px, sin un control móvil alternativo.

Corrección: v5.4 restaura el CTA en móvil y permite wrap del encabezado para conservar accesibilidad y ancho de viewport.

## Corrección de idempotencia

La primera pasada correctiva dejó una diferencia de whitespace en dos `<link>` del `<head>` de `demo.html`. El gate `git diff --exit-code` volvió a bloquear Pages.

No se excluyó el archivo ni se debilitó el control. `apply_authority_v53.py`, version-aware desde v5.4, normaliza esas líneas y la siguiente reconstrucción produjo diff cero.

## Resultado funcional aprobado

Run de calidad/deploy: `31273600016`.

Job Browser E2E: `93143606671`.

Resultado exacto:

- 30 entradas ejecutadas;
- 28 aprobadas;
- 2 omitidas por diseño;
- 0 fallos;
- 55,8 s de ejecución Playwright.

Las dos omisiones corresponden al test de menú móvil dentro de los perfiles de escritorio. El mismo control sí se ejecuta en Chromium mobile.

Después de Playwright:

- `Update stable snapshot`: success;
- `main` y `stable` quedaron sincronizados en la base funcional v5.4.

## Archivos principales

- `package.json`
- `.gitignore`
- `playwright.config.mjs`
- `tests/e2e/helpers.mjs`
- `tests/e2e/public-site.spec.mjs`
- `tests/e2e/demo.spec.mjs`
- `scripts/validate_browser_v54.py`
- `scripts/apply_authority_v53.py`
- `.github/workflows/build-canonical.yml`
- `.github/workflows/pages.yml`

## Decisiones de arquitectura

- Playwright se instala únicamente en CI; no se versionan binarios.
- La dependencia `@playwright/test` está fijada en 1.55.0.
- El Browser E2E se ejecuta contra la URL de Pages, no contra un servidor local que pueda ocultar problemas de despliegue.
- La suite no contiene credenciales o información real: utiliza los perfiles demo ya publicados.
- Los errores runtime son fallos de release.
- Los artefactos de Playwright solo se retienen cuando el job falla.
- El smoke HTTP se conserva: navegador y HTTP validan capas distintas y se complementan.

## Integraciones que siguen apagadas

La v5.4 no activa:

- dominio personalizado;
- Search Console;
- analítica externa;
- CRM;
- backend de formularios;
- envío transaccional de correo.

La configuración pública y la política de privacidad siguen reflejando ese estado real.

## Base siguiente

Con Browser E2E ya incorporado, el próximo ciclo puede concentrarse en performance y accesibilidad medidos —por ejemplo presupuestos de Core Web Vitals/Lighthouse y auditoría automatizada de accesibilidad— sin añadir nuevas capas visuales por defecto.