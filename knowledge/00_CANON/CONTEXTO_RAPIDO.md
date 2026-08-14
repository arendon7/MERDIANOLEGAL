# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente. `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md` mandan si existe cualquier diferencia.

## Proyecto

Sitio público y centro demostrativo de Meridiano Legal. Arquitectura static-first publicada en GitHub Pages, con 46 páginas HTML, 16 fichas profundas y un único formulario físico canónico.

## Estado funcional

- Última release: **5.29.0 — funnel observable y confianza contextual**.
- Estado: **implementada, publicada, certificada y cerrada**.
- Canal: `github-pages-production-funnel-trust-certified`.
- Certificación documental completada: Site Quality and Deploy #375, run `31824770838`, PASS.
- Builder del cierre: `31824748343`, 30 pasos canónicos PASS.
- Graphify del cierre: `31824748359`, PASS.
- La referencia SHA exacta se obtiene de `refs/heads/main` y `refs/heads/stable`; al cierre ambos refs deben estar alineados.
- Portal real de clientes: deshabilitado; `demo.html` continúa siendo demostrativo/noindex.

## Qué aporta v5.29

La web unifica señales ya existentes en un funnel semántico verificable de siete etapas: `awareness → need → offer → evidence → decision → contact → handoff`. La cola v5.29 vive solo en memoria, está limitada a 48 eventos, no lee valores del formulario y no introduce persistencia, identificadores entre sesiones, fingerprinting ni transporte de red propio.

La portada observa checkpoints de exposición y las 16 fichas profundas se reconocen por su `data-catalog-id`. `contact` y `handoff` describen únicamente hechos observables por el navegador: no prueban envío, entrega, lectura, aceptación de propuesta, inicio de encargo ni conversión a cliente.

Entre `#contratacion` y `#contacto` existe un `<aside>` compacto de confianza derivado exclusivamente de `professional-authority-v525.json`. No crea una nueva sección narrativa, por lo que `#contacto` sigue siendo la siguiente `<section>` después de `#contratacion`, preservando v5.28.

## Ciclo activo

**No hay un incremento funcional abierto.** El siguiente ciclo debe abrirse explícitamente desde la baseline v5.29 certificada y partir de un problema observable nuevo.

## Source-of-truth

- `main`: verdad técnica y documental.
- `stable`: último snapshot funcional certificado.
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

Graphify es memoria derivada y no sustituye a `main`. El cierre v5.29 fue regenerado con versión `5.29.0`, canal `github-pages-production-funnel-trust-certified` y `source_commit` alineado con el commit de cierre que lo produjo. Para retomar el proyecto, comprobar siempre que `graphify-out/BUILD_META.json.source_commit` corresponda al `main` actual.
