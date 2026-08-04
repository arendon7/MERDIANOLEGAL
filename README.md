# Meridiano Legal · Web canónica v2.29.0

Base pública, responsive y autocontenida para iterar directamente desde GitHub.

## Accesos

- Web pública: `https://arendon7.github.io/MERDIANOLEGAL/`
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
- Identidad visual propia y recursos SVG locales.
- Diseño responsive sin dependencias de imágenes externas.
- Página 404, `robots.txt` y `sitemap.xml`.
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
node --check demo.js
```

El workflow `.github/workflows/pages.yml` ejecuta estas verificaciones y solo despliega cuando pasan.

## Documentación de mantenimiento

- `docs/REGLAS_CANONICAS.md`: identidad, arquitectura y restricciones.
- `docs/GUIA_DE_ITERACION.md`: archivos y flujo para cambios puntuales.
- `docs/ESTADO_GITHUB.md`: separación entre demo pública y backend productivo.

## Límites

Esta versión es demostrativa. No almacena archivos, no autentica usuarios reales, no envía información a una base de datos y no debe utilizarse con datos personales, expedientes o información confidencial.
