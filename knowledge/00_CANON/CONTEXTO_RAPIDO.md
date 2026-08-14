# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente. `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md` mandan si existe cualquier diferencia.

## Proyecto

Sitio público y centro demostrativo de Meridiano Legal. Arquitectura static-first publicada en GitHub Pages, con 46 páginas HTML, 16 fichas profundas y un único formulario físico canónico.

## Estado funcional

- Última release certificada: **5.29.0 — funnel observable y confianza contextual**.
- SHA funcional certificado previo al cierre documental: `8a8d3bfe473dd5b0ca931c05fbb73b60afaa1f70`.
- Builder funcional final v5.29: `31823965908`.
- Certificación pública funcional final v5.29: `31823985048`.
- Release Governance final relevante: `31823922160`.
- Browser E2E/axe: 88 observados · 86 PASS · 2 SKIP · 0 FAIL · 0 retries.
- Pages, smoke, Lighthouse, E2E/axe y promoción de `stable`: PASS.
- Portal real de clientes: deshabilitado; `demo.html` continúa siendo demostrativo/noindex.

## Qué aporta v5.29

La web unifica señales ya existentes en un funnel semántico verificable de siete etapas: `awareness → need → offer → evidence → decision → contact → handoff`. La cola v5.29 vive solo en memoria, está limitada a 48 eventos, no lee valores del formulario y no introduce persistencia, identificadores entre sesiones, fingerprinting ni transporte de red propio.

La portada observa checkpoints de exposición y las 16 fichas profundas se reconocen por su `data-catalog-id`. `contact` y `handoff` describen únicamente hechos que el navegador puede observar: no prueban envío, entrega, lectura, aceptación de propuesta, inicio de encargo ni conversión a cliente.

Entre `#contratacion` y `#contacto` existe un `<aside>` compacto de confianza derivado exclusivamente de `professional-authority-v525.json`. No crea una nueva sección narrativa, por lo que `#contacto` sigue siendo la siguiente `<section>` después de `#contratacion`, preservando v5.28.

## Ciclo activo

**No hay un incremento funcional abierto después del cierre de v5.29.** El siguiente ciclo debe abrirse explícitamente desde esta baseline certificada.

## Source-of-truth

- `main`: verdad técnica y documental.
- `stable`: último snapshot público certificado.
- `catalog-products-v41/` y `catalog-services-v42/`: fuente jurídica/comercial de las 16 ofertas.
- `offer-narrative-v522.json`: contrato editorial de oferta.
- `professional-authority-v525.json`: hechos profesionales publicables y fuente del trust contextual v5.29.
- `visual-assets-v526.json`: verdad de activos visuales.
- `conversion-path-v528.css` + compositor/validator/E2E v5.28: contrato de ruta de conversión.
- `funnel-contract-v529.json`, `funnel-observability-v529.js`, `funnel-trust-v529.css`, compositor/validator/E2E v5.29: contrato de funnel y confianza contextual.

## Invariantes

- no inventar clientes, testimonios, premios, antigüedad o resultados;
- no PII ni lectura del contenido del formulario;
- no persistencia, identificadores cross-session, fingerprinting ni transporte propio en v5.29;
- WhatsApp manual;
- portal real deshabilitado mientras no exista implementación auténtica;
- no CRM/backend, firma, pagos, agenda, autenticación o carga documental ficticios;
- no reducir cobertura ni relajar budgets;
- conservar un solo formulario físico canónico;
- no ocultar contenido material para aparentar menor densidad;
- no equiparar exposición/contacto/handoff con conversión comercial;
- `stable` solo después de gates verdes.

## Graphify

Graphify es memoria derivada. El snapshot funcional v5.29 ya fue regenerado contra `8a8d3bfe473dd5b0ca931c05fbb73b60afaa1f70`. El cierre documental cambiará el canal a `certified` y debe generar un snapshot final cuyo `source_commit` coincida exactamente con el `main` de cierre.
