# Guía de iteración desde GitHub

## Archivos principales

| Archivo | Uso |
|---|---|
| `index.html` | Contenido y estructura de la web pública. |
| `styles.css` | Sistema visual y responsive de todas las páginas. |
| `app.js` | Menú, filtros, fichas de productos y contacto. |
| `demo.html` | Estructura del portal demostrativo. |
| `demo.js` | Usuarios ficticios, navegación y datos de la demo. |
| `assets/` | Logo e ilustraciones canónicas. |
| `docs/REGLAS_CANONICAS.md` | Restricciones de marca, contenido y tecnología. |

## Flujo recomendado

1. Definir un cambio pequeño y verificable.
2. Modificar únicamente los archivos necesarios.
3. Ejecutar las validaciones locales.
4. Revisar la landing y la demo en escritorio y móvil.
5. Publicar en `main` cuando las validaciones pasen.

## Validaciones locales

```bash
python3 scripts/validate_site.py
node --check app.js
node --check demo.js
```

## Publicación

Cada cambio en `main` activa el workflow de calidad y despliegue. Si una referencia, ancla, imagen o archivo interno queda roto, la publicación se detiene antes de afectar GitHub Pages.

## Datos demostrativos

Las credenciales visibles son intencionalmente ficticias. Cualquier integración con usuarios reales, archivos, formularios, correo o bases de datos deberá implementarse en un entorno privado diferente de GitHub Pages.
