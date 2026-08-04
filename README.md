# Meridiano Legal · Web canónica v2.31.0

Base pública, responsive y autocontenida para iterar directamente desde GitHub.

## Accesos

- Web pública: `https://arendon7.github.io/MERDIANOLEGAL/`
- Centro de demostración: `https://arendon7.github.io/MERDIANOLEGAL/experiencia.html`
- Portal demostrativo: `https://arendon7.github.io/MERDIANOLEGAL/demo.html`

La publicación requiere que el repositorio tenga seleccionado **Settings → Pages → Source: GitHub Actions**.

## Alcance consolidado

- Landing comercial completa.
- 8 servicios profesionales.
- 8 productos jurídicos de alcance cerrado.
- 5 planes recurrentes.
- 6 documentos guiados.
- Sectores priorizados y Ruta Meridiano.
- Portal por perfiles con 9 módulos.
- Centro de demostración migrado desde la versión autocontenida.
- Recorridos ejecutivos de 10 y 20 minutos.
- Galería de entregables jurídicos demostrativos.
- Caso integral ficticio.
- Simulador privado de alcance sin transmisión de información.
- Modalidades de trabajo y arquitectura de propuesta.
- Identidad visual propia y recursos SVG/CSS locales.
- Diseño responsive sin dependencias de imágenes externas.
- Páginas legales, página 404, `robots.txt`, manifiesto y `sitemap.xml`.
- Validación automática antes de cada despliegue.

## Credenciales ficticias de la demo

| Perfil | Usuario | Contraseña |
|---|---|---|
| Cliente | `cliente@empresa-demo.com` | `Cliente2026!` |
| Abogada | `abogado@meridianolegal.local` | `Abogado2026!` |
| Socio director | `admin@meridianolegal.local` | `Meridiano2026!` |

## Validación local

```bash
python3 scripts/validate_site.py
node --check app.js
node --check enhancements.js
node --check experiencia.js
node --check demo.js
python3 -m json.tool manifest.webmanifest
python3 -m json.tool version.json
```

El workflow `.github/workflows/pages.yml` ejecuta estas verificaciones y solo despliega cuando pasan.

## Documentación de mantenimiento

- `docs/REGLAS_CANONICAS.md`: identidad, arquitectura y restricciones.
- `docs/GUIA_DE_ITERACION.md`: archivos y flujo para cambios puntuales.
- `docs/ESTADO_GITHUB.md`: separación entre demo pública y backend productivo.
- `CHANGELOG.md`: historial de las iteraciones consolidadas.

## Límites

Esta versión es demostrativa. No almacena archivos, no autentica usuarios reales, no envía información a una base de datos y no debe utilizarse con datos personales, expedientes o información confidencial.
