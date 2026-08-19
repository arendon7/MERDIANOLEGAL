# v7.4 — Commercial Evidence Readiness

## Problema observable

v7.0–v7.3 hicieron más clara, comprable y demostrable la capa Meridiano Legal Intelligence, pero la medición privacy-first vigente solo distingue etapas generales del funnel. No permite saber, ni siquiera como readiness, qué capacidad de Legal Intelligence originó una intención de contacto.

## Hipótesis

Una atribución comercial cerrada y sin identidad puede preservar la privacidad y, al mismo tiempo, preparar evidencia útil para priorizar producto y ventas. La señal debe viajar como un token allowlisted (`source=li-*`) y los eventos deben existir únicamente en memoria mientras no haya una decisión separada de activar un proveedor externo.

## Superficies

1. `index.html` — único formulario físico y handoff.
2. `experiencia.html` — cinco escenarios Legal Intelligence.
3. `servicios/legal-operations.html` — Legal AI Transformation.
4. `productos/sistema-contractual-empresarial.html` — Contract Control.
5. `productos/programa-gobernanza-ia.html` — AI Governance 360.
6. `productos/proyecto-regulado-estructurado.html` — Regulatory Control.
7. `soluciones/ordenar-operacion-juridica.html` — destino de Meridiano Legal Desk.

## Sujetos allowlisted

- `legal-ai-transformation`
- `contract-control`
- `ai-governance-360`
- `regulatory-control`
- `legal-desk`

Los tokens públicos usan prefijo `li-`. Cualquier valor diferente se ignora.

## Interacciones

- `offer_view`: superficie de oferta cargada con sujeto válido.
- `demo_offer_open`: apertura explícita de la oferta relacionada desde un escenario del Centro Demo.
- `contact_intent`: CTA hacia el contacto desde una superficie atribuida.
- `handoff_prepared`: resumen de WhatsApp preparado en Home con `source` válido.

Ninguna interacción equivale por sí sola a usuario único, mensaje enviado, entrega, lectura, aceptación, contratación o cliente.

## Privacidad y no objetivos

v7.4 permanece `readiness-disabled`:

- sin proveedor externo;
- sin tráfico de analítica;
- sin cookies;
- sin local/session storage;
- sin identificadores cross-session;
- sin fingerprinting;
- sin PII;
- sin contenido del formulario;
- sin texto libre en eventos;
- sin URLs completas en el payload de eventos;
- sin activar pageviews automáticos;
- sin cambiar el único formulario físico;
- sin inferir conversiones que el sitio estático no conoce.

El `source` sí permanece visible en la URL y, por el contrato histórico de `site-v3.js`, forma parte del campo `Origen` del resumen que el usuario revisa antes de enviar por WhatsApp.

## Decisión de diseño

No se añade UI visible nueva. La mejora es de continuidad comercial y observabilidad preparada. Los enlaces del Centro Demo reciben el token correspondiente y las superficies de oferta lo propagan hasta `#contacto`. Home conserva el token hasta el handoff.

No se modifica la navegación, el formulario, los campos, los anchors ni el contenido jurídico.

## Criterios de aceptación

1. Siete superficies cargan el runtime v7.4 exactamente una vez.
2. Solo cinco sujetos y cuatro interacciones pueden existir.
3. Source libre/manipulado se ignora.
4. Eventos locales contienen únicamente `sequence`, `subject`, `interaction`.
5. No se crea transporte externo, almacenamiento o identificador.
6. Plausible/analytics siguen deshabilitados en producción.
7. Un enlace del demo propaga el source al destino.
8. Una oferta atribuida propaga el source a su CTA de contacto.
9. Home atribuye `handoff_prepared` solo cuando el source es válido.
10. Browser E2E, axe, Measurement v6.1 y contratos históricos permanecen verdes.

## Activación futura

Una eventual activación externa es otra decisión/release. Debe definir proveedor, identificador real del sitio, política de privacidad, semántica agregada y límites de retención. v7.4 no autoriza esa activación.
