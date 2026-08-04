# Flujo directo de iteración en GitHub

## Regla operativa

`main` es simultáneamente la línea de trabajo y la fuente de publicación. Las mejoras se aplican directamente sobre los archivos vigentes, sin crear una rama o un archivo nuevo por cada versión.

GitHub Actions ejecuta tres etapas:

1. valida estructura, enlaces, recursos, JavaScript y metadatos;
2. publica GitHub Pages únicamente cuando todo pasa;
3. mueve la rama única `stable` al commit efectivamente desplegado.

Si una validación falla, el commit permanece en `main` para corregirse, pero la web pública conserva la última versión aprobada.

## Reglas de mantenimiento

- Modificar el archivo canónico existente; no crear copias con sufijos como `final`, `nuevo`, `v2` o fechas.
- Crear archivos adicionales solo cuando exista una función o página nueva y permanente.
- Eliminar recursos sustituidos después de comprobar que ninguna página los referencia.
- Mantener una sola implementación por componente.
- Hacer commits pequeños, coherentes y funcionales.
- Actualizar `version.json` y `CHANGELOG.md` únicamente cuando exista una mejora visible o funcional.
- No crear ramas temporales, pull requests de QA ni ramas estables versionadas para el flujo ordinario.
- Usar `stable` como único punto de recuperación del último despliegue aprobado.

## Archivos canónicos

| Archivo o carpeta | Uso |
|---|---|
| `index.html` | Portada y arquitectura comercial pública. |
| `site-v3.css` | Sistema visual principal. |
| `clarity-v31.css` | Capa vigente de claridad y conversión; se actualiza en sitio, no se duplica. |
| `site-v3.js` | Interacciones de la portada. |
| `catalog-home-v32.js` | Enlaces entre portada y fichas profundas. |
| `servicios/` | Ocho fichas profesionales. |
| `productos/` | Ocho fichas de alcance cerrado. |
| `catalog-v32.css` | Sistema visual de las fichas. |
| `catalog-v32.js` | Catálogo y renderizado de fichas. |
| `experiencia.html` y `experiencia.js` | Centro de demostración. |
| `demo.html` y `demo.js` | Meridiano Empresas demostrativo. |
| `scripts/validate_site.py` | Control de integridad antes de publicar. |
| `assets/` | Identidad e ilustraciones activas. |

Los nombres históricos que aún sean activos se actualizan directamente. No se crearán archivos `v33`, `v34` o equivalentes para nuevas mejoras.

## Secuencia de trabajo

1. Auditar el componente que se modificará.
2. Aplicar el cambio directamente en `main`.
3. Esperar el resultado de **Site Quality and Deploy**.
4. Corregir inmediatamente si la validación falla.
5. Verificar la versión publicada.
6. Continuar con el siguiente bloque pequeño.

## Validación local equivalente

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

## Límites

GitHub Pages continúa siendo una demostración estática. No debe recibir expedientes, datos personales, documentos confidenciales ni credenciales reales. La infraestructura productiva requerirá backend, autenticación, almacenamiento y controles de seguridad independientes.
