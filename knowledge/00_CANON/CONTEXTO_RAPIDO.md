# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente. `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md` mandan si existe cualquier diferencia.

## Proyecto

Sitio público y centro demostrativo de Meridiano Legal. Arquitectura static-first publicada en GitHub Pages, con 46 páginas HTML, 16 fichas profundas y un único formulario físico canónico.

## Estado funcional

- Última release certificada: **5.29.0 — funnel observable y confianza contextual**.
- Baseline certificada al abrir v5.30: `36e014fd0cc852ce8835b6befdeb673328e838bd`.
- Nueva candidata: **5.30.0 — profundidad comercial de las 16 ofertas**.
- Canal candidato: `github-pages-production-offer-commercial-depth-candidate`.
- `stable` no debe avanzar hasta que la candidata supere todos los gates públicos.
- Portal real de clientes: deshabilitado; `demo.html` continúa siendo demostrativo/noindex.

## Problema v5.30

Las 16 ofertas ya tienen fuentes jurídicamente profundas y cuantificadas. El problema observable es de síntesis de compra: la unidad de contratación, la lógica de honorarios, las variables que amplían el alcance y el criterio de cierre todavía deben inferirse a partir de secciones separadas.

v5.30 no reescribe los catálogos ni añade otra sección extensa. Complementa el resumen ejecutivo v5.8 con una ficha compacta que explica, por oferta, unidad de contratación, dimensionamiento de honorarios sin tarifas inventadas, tres drivers de alcance, regla de ampliación y cierre verificable.

## Source-of-truth

- `main`: verdad técnica y documental cuando la candidata sea integrada.
- `stable`: último snapshot funcional certificado; permanece en v5.29 mientras v5.30 esté candidata.
- `catalog-products-v41/` y `catalog-services-v42/`: fuente jurídica/comercial principal de las 16 ofertas.
- `offer-narrative-v522.json`: contrato editorial de decisión y modalidad.
- `offer-commercial-v530.json`: contrato complementario de lógica de contratación; nunca sustituye el perímetro o aceptación de los catálogos.
- `professional-authority-v525.json`: hechos profesionales publicables.
- `visual-assets-v526.json`: verdad de activos visuales.
- `funnel-contract-v529.json`: límites semánticos y de privacidad del funnel.

## Invariantes

- no inventar clientes, testimonios, premios, antigüedad o resultados;
- no publicar importes, monedas, descuentos o tarifas no aprobadas en v5.30;
- no cotizador automático ni scoring de honorarios;
- no PII ni lectura del contenido del formulario;
- WhatsApp manual;
- portal real deshabilitado mientras no exista implementación auténtica;
- no CRM/backend, firma, pagos, agenda, autenticación o carga documental ficticios;
- no reducir cobertura ni relajar budgets;
- conservar un solo formulario físico canónico;
- no ocultar contenido material para aparentar menor densidad;
- no equiparar exposición/contacto/handoff con conversión comercial;
- conservar exactamente 30 pasos canónicos;
- `stable` solo después de gates verdes.

## Graphify

Graphify es memoria derivada y no sustituye a `main`. La baseline v5.29 está alineada con `36e014fd0cc852ce8835b6befdeb673328e838bd`. Una vez integrada v5.30, el snapshot derivado solo será autoridad auxiliar cuando `BUILD_META.json.source_commit` coincida con el `main` vigente.
