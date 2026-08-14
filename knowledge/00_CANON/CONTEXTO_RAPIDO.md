# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente. `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md` mandan si existe cualquier diferencia.

## Proyecto

Sitio público y centro demostrativo de Meridiano Legal. Arquitectura static-first publicada en GitHub Pages, con 46 páginas HTML, 16 fichas profundas y un único formulario físico canónico.

## Estado funcional

- Última release certificada: **5.28.0 — ruta de conversión compacta**.
- SHA funcional/canónico certificado previo al commit documental de cierre: `786bd9d4dc720f027f64067c9dd83d583e7e934c`.
- Builder final v5.28: `31819573869`.
- Certificación pública final v5.28: `31819606409`.
- Release Governance final de la corrección semántica: `31819530202`.
- Browser E2E/axe: 79 observados · 77 PASS · 2 SKIP · 0 FAIL · 0 retries.
- Pages, smoke, Lighthouse, E2E/axe y promoción de `stable`: PASS.
- Portal real de clientes: deshabilitado; `demo.html` continúa siendo demostrativo/noindex.

## Qué aporta v5.28

La portada lleva el único `#contacto` inmediatamente después de `#contratacion`, antes de sectores, perspectivas, firma y FAQ. La profundidad jurídica y editorial permanece disponible después del punto de contacto mediante navegación explícita. El preámbulo repetido de tres tarjetas se consolidó en una franja operativa de tres datos mínimos y las rejillas de síntesis se compactan en móvil mediante scroll local contenido, focable y accesible.

La release preserva un único formulario físico, WhatsApp manual, calificación y límites de capacidad real. Los decks `<dl>` conservan semántica nativa, foco de teclado y etiquetas accesibles.

## Ciclo activo

**No hay un incremento funcional abierto después del cierre de v5.28.** El siguiente ciclo debe abrirse de forma explícita desde esta baseline certificada.

## Source-of-truth

- `main`: verdad técnica y documental.
- `stable`: último snapshot público certificado.
- `catalog-products-v41/` y `catalog-services-v42/`: fuente jurídica/comercial de las 16 ofertas.
- `offer-narrative-v522.json`: contrato editorial de oferta.
- `professional-authority-v525.json`: hechos profesionales publicables.
- `visual-assets-v526.json`: verdad de activos visuales.
- `conversion-path-v528.css`, `scripts/apply_conversion_path_v528.py`, `scripts/validate_conversion_path_v528.py` y `tests/e2e/conversion-path-v528.spec.mjs`: contrato funcional v5.28.

## Invariantes

- no inventar clientes, testimonios, premios, antigüedad o resultados;
- no PII ni nueva persistencia/transporte;
- WhatsApp manual;
- portal real deshabilitado mientras no exista implementación auténtica;
- no CRM/backend, firma, pagos, agenda, autenticación o carga documental ficticios;
- no reducir cobertura ni relajar budgets;
- conservar un solo formulario físico canónico;
- no ocultar contenido material para aparentar menor densidad;
- preservar semántica HTML nativa al añadir foco/accesibilidad;
- `stable` solo después de gates verdes.

## Graphify

Graphify es memoria derivada. El snapshot verde disponible declara v5.28 y fue construido desde `7f9caa0a77923b79da6b1d5e2054680dfce0f63d`, anterior al commit canónico certificado `786bd9d4…`. Hasta la siguiente regeneración, `main` manda.
