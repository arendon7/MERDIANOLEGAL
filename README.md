# Meridiano Legal · Web canónica v3.2.0

Base pública, responsive y autocontenida para iterar directamente desde GitHub con validación automática y puntos de restauración.

## Accesos

- Web pública: `https://arendon7.github.io/MERDIANOLEGAL/`
- Centro de demostración: `https://arendon7.github.io/MERDIANOLEGAL/experiencia.html`
- Portal demostrativo: `https://arendon7.github.io/MERDIANOLEGAL/demo.html`

## Arquitectura consolidada

- Identidad visual angular v3 en marino, marfil, azul y dorado.
- Landing comercial con guía para elegir modalidad y punto de entrada.
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

## Estándar de las fichas v3.2

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

Los archivos se encuentran en:

- `servicios/`
- `productos/`
- `catalog-v32.js`
- `catalog-v32.css`
- `catalog-home-v32.js`

## Credenciales ficticias de la demo

| Perfil | Usuario | Contraseña |
|---|---|---|
| Cliente | `cliente@empresa-demo.com` | `Cliente2026!` |
| Abogada | `abogado@meridianolegal.local` | `Abogado2026!` |
| Socio director | `admin@meridianolegal.local` | `Meridiano2026!` |

## Validación local

```bash
python3 scripts/validate_site.py
node --check site-v3.js
node --check catalog-v32.js
node --check catalog-home-v32.js
node --check app.js
node --check enhancements.js
node --check experiencia.js
node --check demo.js
python3 -m json.tool manifest.webmanifest
python3 -m json.tool version.json
```

El workflow `.github/workflows/pages.yml` valida todas las páginas raíz y de subdirectorios. El despliegue solo se ejecuta cuando pasan los controles.

## Documentación de mantenimiento

- `docs/REGLAS_CANONICAS.md`: identidad, arquitectura y restricciones.
- `docs/GUIA_DE_ITERACION.md`: archivos y flujo para cambios puntuales.
- `docs/ESTADO_GITHUB.md`: separación entre demo pública y backend productivo.
- `docs/ROADMAP_V3.md`: etapas de consolidación previstas.
- `CHANGELOG.md`: historial de versiones.

## Límites

Esta versión es demostrativa. No almacena archivos, no autentica usuarios reales, no envía información a una base de datos y no debe utilizarse con datos personales, expedientes o información confidencial.
