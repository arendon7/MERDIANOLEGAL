# Meridiano Legal v5.25.0 — Autoridad profesional verificable

Fecha de cierre funcional: 2026-08-14.

## Propósito

v5.25 convierte la trayectoria profesional documentada del director en una capa pública, sobria, verificable y técnicamente protegida de autoridad.

La auditoría posterior a v5.24 mostró que la profundidad comercial ya estaba bien desarrollada en las 16 ofertas y protegida por validadores transversales. También mostró que la autoridad v5.3 cubría conocimiento temático, sectores, perspectivas, schema e interlinking. El vacío de mayor impacto estaba en otro punto: la web explicaba método y conocimiento, pero materializaba poca trayectoria profesional concreta.

`experiencia.html` permanece deliberadamente ficticia y `noindex`; sirve para demostrar método y entregables, no para probar trayectoria real. v5.25 separa expresamente esas dos funciones.

## Fuente canónica

`professional-authority-v525.json` es la fuente de verdad de los hechos profesionales publicados por esta release.

Incluye:

- Agustín Rendón Calle como fundador y director;
- Abogado de la Universidad EAFIT, graduado en 2018;
- formación de posgrado en Propiedad Intelectual y Nuevas Tecnologías en UNIR, España, sin presentarla como título completado;
- idiomas: español, inglés C1 e italiano B1;
- cinco entradas cronológicas de trayectoria profesional;
- cuatro grupos de asuntos representativos.

La capa se materializa mediante `scripts/apply_professional_authority_v525.py` y se protege con `scripts/validate_professional_authority_v525.py`.

## Resultado público

### Portada

La sección de firma incorpora una síntesis profesional concreta con formación y trayectoria, más enlace directo a `firma.html#trayectoria`.

La prueba declara expresamente que la trayectoria del director **no corresponde a una lista de clientes de Meridiano Legal**.

### Firma

`firma.html` incorpora `#trayectoria` con:

- formación y ubicación profesional;
- cinco entradas cronológicas de experiencia;
- cuatro grupos de asuntos representativos;
- una frontera explícita que distingue experiencia profesional del director, clientes de la firma y resultados atribuibles a terceros.

### Datos estructurados

Portada y firma conservan un grafo coherente `Organization ↔ Person`:

- la organización enlaza al director mediante `founder`;
- `Person` conserva identidad, rol y ubicación;
- Universidad EAFIT se materializa como `alumniOf`;
- `knowsAbout` deriva de los cuatro grupos representativos definidos en la fuente v5.25.

## Fronteras de verdad preservadas

v5.25 no convierte experiencia profesional en social proof ficticio.

Quedan fuera del contrato:

- listas de clientes no verificadas;
- testimonios inventados;
- logos de terceros usados como supuesta prueba comercial;
- métricas o porcentajes de éxito no sustentados;
- garantías de resultado;
- claims de "mejor firma", "líder del mercado" o equivalentes no demostrados;
- atribución de resultados concretos a organizaciones citadas en la trayectoria.

`experiencia.html` conserva su naturaleza demostrativa, sus disclaimers y `noindex`. El portal real continúa deshabilitado y la demo no se presenta como capacidad productiva.

## Integración canónica

v5.25 se integra dentro del paso existente `Apply handoff observability v5.18+` por medio de `apply_handoff_observability_v518.py`.

El manifiesto protegido por v5.24 continúa teniendo exactamente 30 pasos:

`builder == segunda pasada == manifiesto`

No se abrió un paso paralelo ni se alteró el orden canónico.

## Incidencias resueltas sin debilitar gates

### 1. Stub accidental retirado antes de publicación

Durante la preparación inicial se creó accidentalmente en `main` un stub de `professional-authority-v525.json` que contenía únicamente la versión. Fue revertido inmediatamente antes de cualquier builder público o movimiento de `stable`.

No produjo cambio funcional publicado ni formó parte de una candidata certificada. A partir de allí el ciclo volvió al flujo branch + PR.

### 2. Idempotencia de `firma.html`

La primera candidata materializada falló correctamente la segunda pasada de Pages. El compositor retiraba su bloque consumiendo también indentación de la sección siguiente y luego buscaba un ancla demasiado literal. Además, el enlace de navegación `Trayectoria` requería normalización a una única instancia.

PR #107 corrigió el compositor para:

- retirar solo el bloque propio;
- localizar semánticamente `section#enfoque`;
- normalizar el enlace `Trayectoria`;
- permanecer idempotente sobre HTML ya materializado.

El gate no se relajó; el compositor se corrigió.

### 3. Modelado E2E de navegación accesible

Las siguientes incidencias de Browser correspondieron al nuevo test v5.25, no a una regresión productiva:

- PR #108 hizo exacto el locator `Trayectoria` para distinguirlo de `Ver trayectoria profesional`;
- PR #109 modeló que en móvil la navegación debe abrirse antes de inspeccionar el enlace;
- PR #110 corrigió el selector al control editorial real de `firma.html`;
- PR #111 sustituyó el locator dependiente del nombre mutable por la identidad estable `aria-controls="editorial-nav-v47"`, conservando la comprobación del nombre inicial `Abrir menú` y del estado `aria-expanded=true`.

No se eliminó ninguna aserción funcional y la cobertura aumentó frente a v5.24.

### 4. Hardening de workflows

La auditoría final detectó que Builder y Release Governance todavía no vigilaban de forma explícita los cuatro archivos source/logic de v5.25.

PR #113 añadió a las superficies existentes:

- `professional-authority-v525.json`;
- `professional-authority-v525.css`;
- `scripts/apply_professional_authority_v525.py`;
- `scripts/validate_professional_authority_v525.py`.

Release Governance añadió además el gate nominal:

`Validate professional authority v5.25`

La corrida de PR `31754374648` lo ejecutó y pasó. No se cambiaron permisos, cron, arquitectura de triggers, budgets ni el manifiesto de 30 pasos.

## Trazabilidad de implementación

- PR #106 — implementación principal de autoridad profesional;
- PR #107 — idempotencia del compositor;
- PR #108 — selector accesible exacto;
- PR #109 — navegación móvil en E2E;
- PR #110 — control editorial accesible correcto;
- PR #111 — locator móvil estable y spec final;
- PR #113 — hardening de Builder y Release Governance;
- issue #112 — apoyo operativo para abrir el PR de hardening cuando el wrapper de integración bloqueó la creación directa.

Builder autoritativo posterior al hardening: run `31772373318`.

Certificación pública final: run `31772394136`.

SHA funcional final certificado:

`b5a23e0ac1b675cade3ad69d197bbf86d5b998d8`

Al cierre funcional:

`main == stable == b5a23e0ac1b675cade3ad69d197bbf86d5b998d8`.

Después del cierre documental, `main` puede avanzar solo por documentación/memoria; `stable` debe conservar este SHA funcional.

## Evidencia final

### Builder, idempotencia y despliegue

- builder canónico de 30 pasos: PASS;
- segunda pasada/idempotencia: PASS;
- validadores estáticos e históricos: PASS;
- Pages: PASS;
- smoke público: PASS;
- Browser E2E/axe: PASS;
- Lighthouse: PASS;
- release-health: PASS;
- promoción de `stable`: PASS.

### Browser E2E + axe

Job `94680987092`:

- 64 pruebas observadas;
- 62 PASS;
- 2 SKIP;
- 0 FAIL;
- 0 RETRY;
- reporter wall time: 107 s;
- Playwright: 1.8 min;
- Chromium desktop;
- Chromium mobile;
- WebKit desktop;
- 7 superficies axe WCAG 2.1 AA sin violaciones serias/críticas.

Las dos pruebas v5.25 pasan en los tres perfiles funcionales. La cobertura creció desde 58 pruebas observadas en v5.24 a 64 en v5.25.

### Lighthouse

Job `94680987079`: 6/6 superficies PASS.

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Home | 1.00 | 1.00 | 1387 ms | 0 | 72 ms | 108,689 B |
| Solution IA | 1.00 | 1.00 | 903 ms | 0 | 0 ms | 23,358 B |
| Product IA | 1.00 | 1.00 | 903 ms | 0 | 0 ms | 37,295 B |
| Sector tecnología | 0.98 | 1.00 | 933 ms | 0.087 | 0 ms | 24,421 B |
| Perspective IA | 1.00 | 1.00 | 905 ms | 0 | 0 ms | 25,931 B |
| Demo | 1.00 | 1.00 | 902 ms | 0 | 0 ms | 21,946 B |

Budgets vigentes sin relajación: performance >= 0.70, accesibilidad >= 0.90, LCP <= 4000 ms, CLS <= 0.15, TBT <= 350 ms y transferencia <= 1.5 MB.

### CI y release health

Job `94681425380`:

- tiempo hasta gate de `stable`: 240 s;
- baseline v5.5: 279 s;
- mejora frente al baseline: 14.0%;
- cobertura reducida: no;
- budgets relajados: no.

Duraciones observadas:

- Validate current site: 23 s;
- Deploy GitHub Pages: 14 s;
- Verify deployed Pages: 13 s;
- Browser E2E: 174 s;
- Lighthouse: 93 s.

Release Governance mantuvo:

- 5 workflows;
- 22 usos de Actions;
- SHA pinning;
- permisos explícitos;
- dependencias y gates protegidos.

La promoción final registró:

`a9025ed..b5a23e0  HEAD -> stable`

## Artefactos finales

Run `31772394136`:

- GitHub Pages — ID `9208605008` — `sha256:87338ea8ce544ea9249104943667efa02933cac1dbceb3654cbd0aabc4b0ecce`;
- Lighthouse — ID `9208641741` — `sha256:77891063d71cafaa2642b10021496906a04a6b7644a540bd53a7633d03755fc1`;
- CI certification — ID `9208666168` — `sha256:9b1cf3b13e559cf1615afd44b9c9b9899383f54db1c9be8ca7b88ddc8d1f3310`;
- Release Governance health — ID `9208666425` — `sha256:e457163ab77d0bf427b5ad306e66a1cd13aacd62edd909228a1213d6ad58f3d5`.

## Capacidades no añadidas

v5.25 no añade backend, CRM, cuentas, autenticación productiva, portal real, almacenamiento servidor, email transaccional, firma electrónica, pagos, agenda, carga documental, PII, scoring, analítica externa ni transporte nuevo.

WhatsApp continúa como handoff manual. La telemetría continúa first-party/local y sin PII. El portal real sigue deshabilitado.

## Estado de cierre

v5.25 queda funcionalmente certificada en `stable = b5a23e0ac1b675cade3ad69d197bbf86d5b998d8`.

No se abre v5.26 por inercia. Cualquier ciclo posterior debe comenzar con una auditoría nueva y un problema observable.