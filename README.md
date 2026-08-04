# Meridiano Legal · Web canónica v3.3.0

Sitio público, responsive y autocontenido, desarrollado y publicado directamente desde GitHub.

## Flujo actual

- `main`: código vigente y fuente de GitHub Pages.
- `stable`: último commit que pasó validación y fue desplegado correctamente.
- No se crean ramas de iteración, pull requests temporales ni copias versionadas para el trabajo ordinario.
- Cada cambio directo en `main` activa validación, publicación y actualización automática de `stable`.
- Si una validación falla, la web pública conserva el último despliegue aprobado.

## Accesos

- Web pública: `https://arendon7.github.io/MERDIANOLEGAL/`
- La firma: `https://arendon7.github.io/MERDIANOLEGAL/firma.html`
- Centro de demostración: `https://arendon7.github.io/MERDIANOLEGAL/experiencia.html`
- Portal demostrativo: `https://arendon7.github.io/MERDIANOLEGAL/demo.html`

## Arquitectura consolidada

- Identidad visual angular v3 en marino, marfil, azul y dorado.
- Landing comercial con guía para elegir modalidad y punto de entrada.
- Página institucional con dirección, método, principios, experiencia y colaboración profesional.
- 8 servicios profesionales con página profunda individual.
- 8 productos jurídicos de alcance cerrado con página profunda individual.
- 5 planes recurrentes.
- 6 documentos guiados.
- 8 sectores priorizados.
- Ruta Meridiano y explicación de entregables.
- Preguntas frecuentes, criterios de encaje y contacto por WhatsApp.
- Portal por perfiles con 9 módulos.
- Centro de demostración con recorrido, entregables, caso integral y simulador.
- Páginas legales, página 404, `robots.txt`, manifiesto y sitemap ampliado.

## Archivos canónicos

- `index.html`, `site-v3.css`, `clarity-v31.css` y `site-v3.js`: portada pública.
- `firma.html` y `firma.css`: página institucional.
- `servicios/` y `productos/`: 16 fichas profundas.
- `catalog-v32.js`, `catalog-v32.css` y `catalog-home-v32.js`: catálogo y conexiones de navegación.
- `experiencia.html`, `experiencia.css` y `experiencia.js`: centro de demostración.
- `demo.html`, `styles.css` y `demo.js`: portal demostrativo.

Los nombres históricos que todavía corresponden a archivos activos se actualizan directamente. No se crearán copias `v33`, `v34`, `final`, `nuevo` o equivalentes.

## Estándar de las fichas

Cada servicio y producto incorpora:

- pregunta ejecutiva;
- situaciones en las que puede ser útil;
- alcance orientativo;
- método de trabajo;
- entregables;
- información y participación requerida;
- límites y exclusiones;
- soluciones relacionadas;
- siguiente paso y canal de contacto.

## Credenciales ficticias de la demo

| Perfil | Usuario | Contraseña |
|---|---|---|
| Cliente | `cliente@empresa-demo.com` | `Cliente2026!` |
| Abogada | `abogado@meridianolegal.local` | `Abogado2026!` |
| Socio director | `admin@meridianolegal.local` | `Meridiano2026!` |

## Validación

```bash
python3 scripts/validate_site.py
node --check site-v3.js
node --check catalog-v32.js
node --check catalog-home-v32.js
node --check experiencia.js
node --check demo.js
python3 -m json.tool manifest.webmanifest
python3 -m json.tool version.json
```

El workflow `.github/workflows/pages.yml` valida todas las páginas y recursos. Solo después publica el contenido y mueve `stable` al commit desplegado.

## Documentación

- `docs/REGLAS_CANONICAS.md`: identidad, arquitectura y restricciones.
- `docs/GUIA_DE_ITERACION.md`: flujo directo de trabajo sobre `main`.
- `docs/ESTADO_GITHUB.md`: separación entre demo pública y backend productivo.
- `docs/ROADMAP_V3.md`: etapas de consolidación.
- `CHANGELOG.md`: historial funcional.

## Límites

Esta versión es demostrativa. No almacena archivos, no autentica usuarios reales, no envía información a una base de datos y no debe utilizarse con datos personales, expedientes o información confidencial.
