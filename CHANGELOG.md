# Historial de versiones

## v3.4.0 — 2026-08-05

### Arquitectura sectorial

- Se publicaron ocho páginas profundas para tecnología y software, servicios públicos y economía circular, agroindustria y sostenibilidad, salud y negocios regulados, comercio y distribución, startups e inversión, proyectos públicos y transformación de operaciones jurídicas.
- Cada página incorpora decisiones frecuentes, mapa jurídico-operativo, riesgos tempranos, soluciones relacionadas y lecturas recomendadas.
- Se unificó en la portada el frente de servicios públicos, aseo y economía circular.
- La octava entrada sectorial se destinó a transformación de operaciones jurídicas y Legal Operations.

### Navegación y posicionamiento

- Las tarjetas sectoriales de la portada enlazan sus páginas completas.
- El sitemap incorpora las ocho rutas sectoriales.
- Los contenidos conectan sectores, servicios, productos y perspectivas en recorridos coherentes.

### Calidad

- El validador exige exactamente ocho páginas sectoriales.
- Se comprueban sus bloques principales, recursos, anclas y enlaces desde la portada.
- El despliegue continúa actualizando `stable` únicamente después de una publicación exitosa.

## v3.3.1 — 2026-08-05

### Biblioteca de perspectivas

- Se creó una biblioteca pública de contenido jurídico y empresarial.
- Se publicaron seis perspectivas profundas sobre gobierno jurídico de IA, contratos administrables, cadena de titularidad de activos intangibles, socios e inversión, secuencia de viabilidad en proyectos regulados y Legal Operations.
- Cada artículo incorpora pregunta ejecutiva, marco de análisis, señales de alerta, preguntas de control, componentes de implementación, límites y enlaces a servicios o productos relacionados.
- La portada incorpora acceso a la biblioteca y a tres perspectivas destacadas.
- El sitemap incluye la biblioteca y las seis rutas editoriales.

### Calidad

- El validador exige la presencia de las seis perspectivas y sus bloques editoriales principales.
- Se controla que la portada conserve los enlaces a la biblioteca y a las lecturas destacadas.
- `stable` continúa actualizándose únicamente después de un despliegue exitoso.

## v3.3.0 — 2026-08-04

### Autoridad institucional

- Se creó una página profunda de la firma con dirección, enfoque profesional, método, principios de actuación, experiencia sectorial y modelo de colaboración.
- La portada incorpora acceso directo a la página institucional sin perder su resumen ejecutivo.
- El sitemap incorpora la nueva ruta pública.

### Flujo directo de implementación

- `main` pasa a ser la línea única de trabajo y publicación.
- Se eliminó el proceso ordinario de ramas temporales y pull requests de QA.
- La rama única `stable` conserva automáticamente el último commit desplegado con éxito.
- Si una validación falla, GitHub Pages mantiene la última versión aprobada.

### Depuración

- Se eliminaron `app.js`, `enhancements.js` y `autocontenida.css`, que ya no eran consumidos por ninguna página activa.
- Se eliminaron dos SVG duplicados sustituidos por los activos canónicos v3.
- Se simplificaron workflow, documentación y validaciones para trabajar sobre el código vigente.

## v3.2.0 — 2026-08-04

### Fichas profundas

- Se crearon páginas individuales para los 8 servicios profesionales.
- Se crearon páginas individuales para los 8 productos de alcance cerrado.
- Cada ficha incorpora pregunta ejecutiva, situaciones de uso, alcance, método, entregables, requisitos, exclusiones y soluciones relacionadas.
- Se mantuvo una arquitectura común para facilitar futuras correcciones sin perder consistencia.

### Navegación y descubrimiento

- Las tarjetas de la portada conservan la ficha ejecutiva y agregan acceso a la página completa.
- Los modales distinguen correctamente entre servicio profesional y producto jurídico.
- El sitemap incorpora las 16 nuevas rutas públicas.

### Calidad

- El validador revisa páginas HTML en subdirectorios.
- Se verifica la presencia y unicidad de 16 identificadores de catálogo.
- GitHub Actions valida `catalog-v32.js` y `catalog-home-v32.js`.
- Se controla que la portada siga cargando la navegación hacia las fichas profundas.

## v3.1.0 — 2026-08-04

### Claridad y conversión

- Se explicó para quién es Meridiano y cuándo puede agregar mayor valor.
- Se diferenció orientación focal, servicio profesional, producto cerrado y plan recurrente.
- Se incorporó una sección de entregables concretos.
- Se agregaron criterios de encaje, preguntas frecuentes y un proceso de contacto en tres etapas.
- Se documentó el roadmap de consolidación v3.

## v3.0.0 — 2026-08-04

### Reconstrucción canónica

- Se sustituyó la reconstrucción beta por la identidad visual angular v3.
- Se incorporaron logotipo principal y claro, hero gráfico y Ruta Meridiano.
- Se restauró la arquitectura de 8 servicios, 8 productos, 5 planes, 6 documentos y 8 sectores.
- Se añadieron controles antirregresión y la rama estable `stable-v3.0.0`.

## v2.31.0 — 2026-08-04

### Migración desde la versión autocontenida

- Se incorporó un Centro de demostración integrado con recorrido ejecutivo de 10 o 20 minutos.
- Se agregó una galería visual de entregables jurídicos demostrativos.
- Se incorporó un caso integral completamente ficticio desde comprensión hasta seguimiento.
- Se agregó un simulador privado de alcance que funciona en el navegador y no transmite información.
- Se creó una vista contextual de Meridiano Empresas y sus módulos.
- La landing incorpora modalidades de trabajo y una entrada visible a la experiencia demostrativa.

### Identidad y experiencia

- Se reforzó la jerarquía editorial mediante la combinación serif/sans, paleta marino, marfil, azul y dorado.
- Se incorporaron composiciones de matriz, ruta, contrato, política y tablero sin depender de imágenes externas.
- Se mantuvo la arquitectura canónica de 8 servicios, 8 productos, 5 planes y 6 documentos guiados.
- La experiencia conserva navegación responsive y tratamiento diferenciado para escritorio y móvil.

### Calidad

- El validador exige ahora todos los recursos del centro de demostración.
- GitHub Actions valida `experiencia.js` además de los archivos públicos y de la demo privada.
- Se incorporó `experiencia.html` al sitemap público.

## v2.30.0 — 2026-08-04

### Confianza y conversión

- Se agregaron política de privacidad, términos de uso y aviso legal navegables.
- Se incorporaron accesos flotantes a WhatsApp y regreso al inicio.
- Se agregó una nota de confianza al formulario de contacto.
- Se incorporó navegación activa por sección.

### Publicación

- Se agregó manifiesto web instalable y metadatos sociales básicos.
- Se amplió el sitemap con páginas institucionales.
- Se reforzó la validación de JSON, enlaces y recursos.

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
