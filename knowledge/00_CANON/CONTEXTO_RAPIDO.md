# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente. `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md` mandan si existe cualquier diferencia.

## Proyecto

Sitio público y centro demostrativo de Meridiano Legal. Arquitectura static-first publicada en GitHub Pages, con 46 páginas HTML, 16 fichas profundas y un único formulario físico canónico.

## Estado funcional

- Última release certificada: **5.27.0 — densidad comercial móvil**.
- `main = stable = 26c90ec3a0e1ea08ae251673cba0a7fc56b4e0b2` al cierre de v5.27.
- Builder v5.27: `31813283560`.
- Certificación pública v5.27: `31813319651`.
- Pages, smoke, Browser E2E/axe, Lighthouse y promoción de `stable`: PASS.
- Portal real de clientes: deshabilitado; `demo.html` continúa siendo demostrativo/noindex.

## Qué aporta v5.27

La portada móvil conserva todas las opciones comerciales y transforma servicios, productos, planes, referencias de honorarios y sectores en decks horizontales contenidos con `scroll-snap`. La release cerró sin overflow global ni pérdida de rutas, y mantiene el diseño de escritorio.

## Ciclo activo

**v5.28.0 — compresión de la ruta de conversión: activa.**

Problema observable: después de `#contratacion`, el recorrido lineal todavía atraviesa sectores, perspectivas, autoridad/firma y FAQ antes de llegar al único formulario; además el contacto repite un preámbulo de tres pasos ya explicado en el bloque de contratación.

Contrato previsto:

1. mover `#contacto` inmediatamente después de `#contratacion`;
2. preservar sectores, perspectivas, firma y FAQ como profundidad opcional posterior;
3. consolidar las tres tarjetas del preámbulo en una sola franja operativa;
4. mantener intactos calificación, síntesis, recomendación, proceso, aceptación y handoff manual a WhatsApp;
5. compactar en móvil las rejillas de síntesis mediante overflow local contenido;
6. conservar los 30 pasos canónicos de v5.24 y ejecutar v5.28 dentro de la extensión final `v5.18+`;
7. no mover `stable` hasta gates verdes.

## Source-of-truth

- `main`: verdad técnica y ejecutable.
- `stable`: último snapshot público certificado.
- `catalog-products-v41/` y `catalog-services-v42/`: fuente jurídica/comercial de las 16 ofertas.
- `offer-narrative-v522.json`: contrato editorial de oferta.
- `professional-authority-v525.json`: hechos profesionales publicables.
- `visual-assets-v526.json`: verdad de activos visuales.
- `conversion-path-v528.css`, `scripts/apply_conversion_path_v528.py` y `scripts/validate_conversion_path_v528.py`: contrato funcional del ciclo activo.

## Invariantes

- no inventar clientes, testimonios, premios, antigüedad o resultados;
- no PII ni nueva persistencia/transporte;
- WhatsApp manual;
- portal real deshabilitado mientras no exista implementación auténtica;
- no CRM/backend, firma, pagos, agenda, autenticación o carga documental ficticios;
- no reducir cobertura ni relajar budgets;
- conservar un solo formulario físico canónico;
- no ocultar contenido material para aparentar menor densidad;
- `stable` solo después de gates verdes.

## Graphify

Graphify es memoria derivada. El snapshot disponible reconoce v5.27 y fue construido desde `75d18b45d7273ae10a3722617bfc3808350a3f0f`, anterior al commit canónico final `26c90ec3…`; por tanto `main` manda hasta la siguiente regeneración.
