# Meridiano Legal v5.21.0 — Veracidad de capacidades

Fecha de cierre funcional: 2026-08-12.

## Propósito

v5.21 convierte en contrato técnico una frontera que antes dependía demasiado del copy: distinguir con precisión una superficie demostrativa de una capacidad productiva real.

La web conserva `demo.html` como interfaz ficticia, local y `noindex`, pero deja de presentarla como si fuera un área autenticada de clientes. La existencia futura de un portal real pasa a depender de configuración canónica y validación automática, no de una etiqueta comercial aislada.

## Resultado funcional

La release establece que:

- `site-config.json` declara `capabilities.client_portal.enabled=false`;
- mientras el portal real esté deshabilitado, ninguna superficie indexable puede usar “Área de clientes” como promesa de capacidad;
- todo enlace público hacia `demo.html` debe contener `demo` o `demostrativo`;
- `runtime-config.js` y `site-status.json` publican el estado real de la capacidad;
- `demo.html` mantiene datos ficticios, `data-capability-v521="demo-only"` y exactamente un `meta robots` con `noindex,nofollow`;
- `demo.js` ya no inyecta dinámicamente un segundo `meta robots`;
- si en el futuro se habilita un portal real, la configuración deberá aportar una URL HTTPS distinta de `demo.html` y la validación exigirá al menos un acceso público real a esa URL.

El cierre mantiene el modelo static-first y no crea autenticación, cuentas, backend, CRM, almacenamiento servidor, firma electrónica, pagos, agenda, carga documental ni analítica externa.

## Superficie pública normalizada

Durante Release Governance, v5.21 identificó y gobernó 25 accesos públicos hacia la demo distribuidos en 17 superficies. La normalización final evita que el enlace de demostración se confunda con una capacidad productiva.

Ejemplos de la regla:

- `Área de clientes` → `Demo de cliente`;
- `Abrir Meridiano Empresas` → `Abrir portal demo`;
- `Documentos guiados` → `Documentos guiados · demo`;
- otras etiquetas hacia `demo.html` deben contener explícitamente `demo` o `demostrativo`.

## Arquitectura técnica

### Configuración

`site-config.json` incorpora:

```json
"capabilities": {
  "client_portal": {
    "enabled": false,
    "url": ""
  }
}
```

`scripts/site_config.py` impide estados incoherentes:

- portal habilitado sin URL HTTPS;
- URL con query o fragment;
- uso de `demo.html` como URL del portal real;
- URL residual cuando el portal está deshabilitado.

### Materialización final

`scripts/apply_capability_truth_v521.py` se encadena después de v5.18 y actúa como normalizador final de capacidad. Esto permite que las capas históricas sigan reconstruyendo sus estados intermedios y garantiza que la salida pública termine siempre con la frontera v5.21.

La materialización:

1. normaliza enlaces públicos a la demo;
2. fija `data-capability-v521="demo-only"`;
3. normaliza exactamente un `noindex,nofollow` estático en `demo.html`;
4. elimina la inyección heredada `robotsMeta` de `demo.js`;
5. sincroniza `runtime-config.js` y `site-status.json`;
6. ejecuta el validator v5.21 sobre la salida materializada.

### Validator

`scripts/validate_capability_truth_v521.py` falla si:

- la versión es inferior a 5.21.0;
- runtime/status divergen de `site-config.json`;
- la demo pierde su marca ficticia o `noindex`;
- hay cero o más de un `meta[name=robots]` en la demo;
- `demo.js` vuelve a inyectar robots dinámicamente;
- una superficie indexable presenta “Área de clientes” mientras el portal real está apagado;
- un enlace hacia `demo.html` carece de etiqueta demostrativa;
- se habilita un portal sin URL HTTPS real y sin acceso público verificable.

### Browser E2E

`tests/e2e/capability-truth.spec.mjs` protege la frontera en navegador real:

- portada sin “Área de clientes” productiva;
- enlaces a demo explícitamente demostrativos;
- runtime `clientPortal.enabled=false`;
- demo marcada `demo-only`;
- badge `DEMO FICTICIA`;
- heading `Portal demostrativo`;
- un único `noindex,nofollow`;
- aviso de que la información no se envía a servidor.

La suite corre en Chromium desktop, Chromium mobile y WebKit desktop.

## Compatibilidad histórica resuelta

### v5.8

El primer Release Governance bloqueó la candidata porque `apply_decision_v58.py` intentaba reinsertar la portada histórica aunque ya existía la superficie unificada v5.20. Se corrigió el compositor para preservar las 16 fichas y no recrear la capa visual legada cuando la salida unificada ya existe.

### v5.12

La siguiente pasada avanzó hasta v5.12 y encontró el mismo patrón en `apply_proof_v512.py`. Se hizo version-aware para conservar la prueba unificada v5.20 sin perder el contrato de las fichas profundas.

### Validator UX v4.5

La primera certificación Pages pasó idempotencia pero fue bloqueada porque `validate_ux_v45.py` exigía literalmente “Área de clientes”. PR #80 mantuvo el requisito histórico hasta v5.20 y, desde v5.21, exige `Demo de cliente` y falla si reaparece la etiqueta productiva anterior.

### Robots duplicado en demo

La nueva cobertura E2E encontró una deuda real que los validators estáticos no veían: `demo.html` ya tenía un `noindex,nofollow` correcto, pero `demo.js` creaba un segundo meta robots al cargar la página. No se debilitó el test. PR #81 eliminó la inyección desde el compositor, normalizó un único meta estático y añadió un guard anti-regresión.

## Trazabilidad de implementación

- PR funcional: `#79`;
- merge funcional: `9af1674d9caf6353e233c3b1574cb279f0ee116c`;
- hotfix UX v4.5: PR `#80`, merge `2bed487ee39a6529b50828af360c153deff286e8`;
- hotfix robots demo: PR `#81`, merge `5e09f9b2b541437a89397194e0c7a892da72e91c`;
- SHA materializado por builder y certificado: `b2a6d4d4d2608362e86b53ea4cc197cd7ce33cc1`;
- run final de certificación pública: `31658340092`.

## Evidencia final

### Builder, validación y despliegue

- builder canónico: PASS;
- segunda pasada/idempotencia: PASS;
- validadores históricos v4.4→v5.18: PASS;
- contrato v5.21 ejecutado como extensión final del compositor: PASS;
- GitHub Pages: PASS;
- smoke público: PASS;
- release-health: PASS;
- promoción de `stable`: PASS.

Al cierre funcional:

`main == stable == b2a6d4d4d2608362e86b53ea4cc197cd7ce33cc1`.

### Browser E2E + axe

- 43 pruebas observadas;
- 41 PASS;
- 2 SKIP;
- 0 FAIL;
- 0 RETRY;
- reporter: 77 s;
- cobertura v5.21 ejecutada en Chromium desktop, Chromium mobile y WebKit desktop;
- 7 superficies axe conservadas sin reducción de cobertura.

La release aumenta la suite respecto de v5.20: de 37 a 43 pruebas observadas.

### Lighthouse

6/6 superficies PASS, sin relajación de budgets:

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT |
|---|---:|---:|---:|---:|---:|
| Home | 1.00 | 1.00 | 1410 ms | 0 | 91 ms |
| Solution IA | 1.00 | 1.00 | 905 ms | 0 | 0 ms |
| Product IA | 1.00 | 1.00 | 909 ms | 0 | 0 ms |
| Sector tecnología | 0.98 | 1.00 | 935 ms | 0.087 | 0 ms |
| Perspective IA | 1.00 | 1.00 | 906 ms | 0 | 0 ms |
| Demo | 1.00 | 1.00 | 903 ms | 0 | 0 ms |

Máximos observados: LCP 1410 ms, CLS 0.087, TBT 91 ms.

### CI

- tiempo hasta gate de `stable`: 178 s;
- baseline v5.5: 279 s;
- mejora frente al baseline: 36.2%;
- cobertura reducida: no;
- budgets relajados: no.

### Artefactos del run `31658340092`

- Lighthouse: `9165276023`, `sha256:798847e408280e0730accc2d9a2f7e84ad5f2399aed8c3d9dedad4a77184e6ff`;
- CI: `9165288913`, `sha256:df0b5776c71cea97f1d8b51956c1e4750c03626e60f5fb9cfe2988a82d5e5091`;
- release-health: `9165289152`, `sha256:0820431f230a5520912a0320ddc0749987743f0a234bd3bba36de38cc0ec28e7`;
- Pages: `9165233265`, `sha256:d437eaef17490b4f13396bc7e3c33887bbf095ae94f4f0f70495b8e1ba2ff263`.

## Estado de capacidades externas

Activas y verificables:

- GitHub Pages;
- WhatsApp como handoff manual;
- contexto comercial client-side;
- telemetría local/first-party sin PII;
- sitemap, robots, canonical y Open Graph;
- demo ficticia/noindex;
- pipeline CI de certificación.

Deshabilitada explícitamente:

- portal real de clientes (`client_portal.enabled=false`).

No declarar activas sin implementación/configuración real:

- autenticación o cuentas reales;
- CRM/backend;
- persistencia servidor del formulario;
- email transaccional;
- firma electrónica;
- pagos;
- agenda;
- carga documental;
- analítica externa.

## No objetivos cumplidos

v5.21 no construye un portal real ni amplía el catálogo. No modifica las 16 fichas profundas, no añade PII, no introduce storage o red adicional y no automatiza el handoff de WhatsApp.

## Cierre

El resultado de v5.21 no es “tener portal”: es que la web ya no puede afirmar o sugerir esa capacidad mientras no exista. La frontera demo/producto queda explícita en configuración, HTML, runtime, CI y navegador.
