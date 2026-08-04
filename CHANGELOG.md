# Historial de versiones

## v2.30.0 — 2026-08-04

### Confianza y cumplimiento

- Se publicaron páginas separadas de privacidad, términos de uso y aviso legal.
- Se aclaró el funcionamiento local del formulario y la apertura de WhatsApp.
- Se documentaron los límites de la demo, el uso de información confidencial y el inicio de la relación profesional.

### Experiencia de usuario

- Se añadió navegación activa según la sección visible.
- Se incorporaron accesos flotantes a WhatsApp y regreso al inicio.
- Se añadieron enlaces legales permanentes en el pie de página.
- Se agregó una nota de confianza junto al formulario de contacto.

### Publicación y SEO

- Se añadió `manifest.webmanifest`.
- Se amplió `sitemap.xml` con las páginas legales.
- Se incorporó una capa separada de mejoras en `enhancements.js` y `enhancements.css`.

### Calidad

- GitHub Actions valida ahora el JavaScript de mejoras, el manifiesto y los metadatos de versión.
- El núcleo v2.29 permanece separado y recuperable.

## v2.29.0 — 2026-08-04

### Estabilidad

- Se incorporó validación automática de HTML, rutas, anclas, imágenes y recursos internos.
- Se agregó validación sintáctica de `app.js` y `demo.js`.
- El despliegue queda condicionado a que todas las comprobaciones pasen.
- Se actualizaron las acciones oficiales utilizadas por GitHub Pages.
- Se creó la rama de restauración `stable-v2.29.0`.

### Publicación

- Se agregó página 404 coherente con la identidad visual.
- Se agregaron `robots.txt` y `sitemap.xml`.
- Se documentó la URL prevista de GitHub Pages.

### Funcionalidad

- El formulario público prepara la solicitud y abre WhatsApp sin requerir backend.
- Se mejoró el cierre y la recuperación de foco de menús y modales.
- Los filtros de productos exponen correctamente su estado accesible.
- Los perfiles de la demo muestran acciones diferenciadas.

### Seguridad de la demo

- Se neutraliza HTML ingresado en solicitudes y documentos guiados.
- Se protege el uso de `sessionStorage` frente a restricciones del navegador.
- Se marca la demo como contenido no indexable.
- Se mantiene la carga de archivos deshabilitada.

### Mantenimiento

- Se fijaron reglas canónicas de marca, arquitectura y contenido.
- Se creó una guía para iteraciones puntuales desde GitHub.
- Se registró la versión en `version.json`.
- Se reorganizó el JavaScript público y demostrativo para facilitar futuras ediciones.

## v2.28.0 — 2026-08-04

- Primera consolidación completa de la landing pública.
- Incorporación del portal demostrativo con tres perfiles y nueve módulos.
- Recursos gráficos SVG autocontenidos.
- Configuración inicial de GitHub Pages.
