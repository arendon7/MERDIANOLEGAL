# Meridiano Legal · Web canónica v3.5.0

Sitio público, responsive y autocontenido, desarrollado y publicado directamente desde GitHub.

## Flujo de trabajo

- `main`: código vigente y fuente de GitHub Pages.
- `stable`: último commit validado y desplegado correctamente.
- Cada cambio en `main` activa validación, publicación y actualización automática de `stable`.
- Si una validación falla, la web pública conserva el último despliegue aprobado.
- No se crean ramas ordinarias, pull requests temporales ni copias con sufijos de versión.

## Accesos

- Web pública: `https://arendon7.github.io/MERDIANOLEGAL/`
- La firma: `https://arendon7.github.io/MERDIANOLEGAL/firma.html`
- Perspectivas: `https://arendon7.github.io/MERDIANOLEGAL/perspectivas.html`
- Centro de demostración: `https://arendon7.github.io/MERDIANOLEGAL/experiencia.html`
- Portal demostrativo: `https://arendon7.github.io/MERDIANOLEGAL/demo.html`

## Arquitectura consolidada

- Landing comercial con selector guiado de solución.
- Comparación entre orientación, servicio, producto y plan.
- Contacto contextual según la página o recomendación de origen.
- Navegación móvil compacta con accesos a demostración y área de clientes.
- Página institucional con dirección, método, principios y experiencia.
- 8 servicios profesionales y 8 productos de alcance cerrado.
- 8 páginas sectoriales profundas.
- Biblioteca con 6 perspectivas jurídicas y empresariales.
- 5 planes recurrentes y 6 documentos guiados.
- Centro de demostración y portal ficticio por perfiles.
- Páginas legales, página 404, manifiesto, `robots.txt` y sitemap.

## Archivos canónicos

| Componente | Archivos |
|---|---|
| Portada | `index.html`, `site-v3.css`, `clarity-v31.css`, `site-v3.js` |
| Enlaces y catálogo en portada | `catalog-home-v32.js` |
| Selector y contacto contextual | `decision-flow.js`, `decision-flow.css` |
| Servicios y productos | `servicios/`, `productos/`, `catalog-v32.js`, `catalog-v32.css` |
| Firma | `firma.html`, `firma.css` |
| Perspectivas | `perspectivas.html`, `perspectivas.css`, `perspectivas/` |
| Sectores | `sectores.css`, `sectores/` |
| Demostración | `experiencia.html`, `experiencia.css`, `experiencia.js` |
| Portal ficticio | `demo.html`, `styles.css`, `demo.js` |

Los nombres históricos que todavía identifican archivos activos se actualizan directamente. No se crean copias `final`, `nuevo`, `v36` o equivalentes.

## Validación

```bash
python3 scripts/validate_site.py
python3 scripts/validate_decision_flow.py
node --check site-v3.js
node --check catalog-v32.js
node --check catalog-home-v32.js
node --check decision-flow.js
node --check experiencia.js
node --check demo.js
python3 -m json.tool manifest.webmanifest
python3 -m json.tool version.json
```

El workflow `.github/workflows/pages.yml` publica únicamente después de aprobar todas las comprobaciones.

## Credenciales ficticias de la demo

| Perfil | Usuario | Contraseña |
|---|---|---|
| Cliente | `cliente@empresa-demo.com` | `Cliente2026!` |
| Abogada | `abogado@meridianolegal.local` | `Abogado2026!` |
| Socio director | `admin@meridianolegal.local` | `Meridiano2026!` |

## Límites

Esta versión es demostrativa. No almacena archivos, no autentica usuarios reales y no debe utilizarse con datos personales, expedientes, credenciales o información confidencial.
