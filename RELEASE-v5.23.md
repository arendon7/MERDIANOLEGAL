# Meridiano Legal v5.23.0 — Compresión del contacto comercial

Fecha de cierre funcional: 2026-08-13.

## Propósito

v5.23 reduce la carga cognitiva del último tramo de conversión de la portada sin eliminar información jurídica material ni ampliar el tratamiento de datos.

La auditoría posterior a v5.22 mostró que el cuello de botella ya no estaba en la profundidad de las 16 ofertas ni en la arquitectura superior de decisión, sino dentro del formulario: calificación, resumen, modalidad, recomendación, ruta a propuesta y estados de aceptación/inicio se presentaban como superficies visuales sucesivas alrededor de los campos que el visitante debía completar.

La release conserva la lógica comercial existente y cambia su arquitectura de presentación.

## Resultado funcional

### Antes

Dentro del único formulario canónico convivían superficies separadas para:

1. calificación comercial v5.9;
2. resumen de calificación v5.9;
3. brief de modalidad y prueba v5.13;
4. recomendación explicable v5.14/v5.15;
5. ruta de solicitud a propuesta v5.10;
6. estados previos al inicio v5.11;
7. handoff manual a WhatsApp v5.17/v5.18.

La información era válida, pero la lectura obligaba al usuario a atravesar varias tarjetas antes de completar contexto, privacidad y CTA.

### Después

v5.23 deja una secuencia visible más corta:

1. datos de contacto y necesidad;
2. momento de decisión, horizonte y presupuesto opcional;
3. **una sola síntesis comercial** que conserva contexto, necesidad, modalidad, estándar verificable, recomendación y siguiente paso;
4. **un solo disclosure de proceso** que contiene la ruta v5.10 y las condiciones/estados v5.11;
5. contexto general, privacidad y CTA a WhatsApp;
6. handoff manual únicamente después de que el usuario decide prepararlo.

La síntesis final es un `div[role="region"]` y no una sección anidada. El disclosure usa `<details>` nativo y mantiene una única jerarquía conceptual en escritorio y móvil.

## Contratos preservados

v5.23 no cambia el modelo comercial subyacente.

Se conservan:

- un único `#contact-form` físico;
- `name`, `company`, `email`, `need`, `decision_stage`, `urgency`, `budget`, `message` y `privacy`;
- calificación v5.9 sin scoring;
- modalidad y estándar v5.13;
- recomendación explicable v5.14;
- recomendación→acción v5.15;
- ruta a propuesta v5.10;
- cuatro estados de engagement v5.11;
- handoff manual v5.17;
- observabilidad local sin PII v5.18;
- intención comercial explícita como única señal adaptativa.

Una intención explícita de propuesta puede abrir el único disclosure de proceso. Orientación y definición de alcance lo mantienen cerrado. La web no infiere intención, no asigna puntajes y no cambia automáticamente el estado comercial.

## No objetivos cumplidos

v5.23 no:

- cambia productos, servicios, planes, precios u honorarios;
- añade campos de PII;
- crea CRM, backend, agenda, firma, pagos o portal real;
- almacena respuestas del formulario;
- automatiza el envío de WhatsApp;
- introduce scoring, IA de recomendación o inferencia de intención;
- reduce cobertura;
- relaja budgets;
- reescribe retrospectivamente v5.22.

## Arquitectura técnica

### Composición final

La capa v5.23 se materializa mediante:

- `scripts/apply_contact_compression_v523.py`;
- `scripts/normalize_contact_compression_v523.py`;
- `scripts/validate_contact_compression_v523.py`;
- `tests/e2e/contact-compression.spec.mjs`;
- `tests/e2e/contact-integrity-v523.spec.mjs`;
- comportamiento adaptativo en `decision-action-v515.js`;
- presentación y corrección AA en `decision-action-v515.css`.

`apply_handoff_observability_v518.py` continúa siendo el compositor final de las capas posteriores y encadena v5.21, v5.22 y v5.23 de forma version-aware.

### Validator v5.23

El contrato anti-drift exige, entre otros puntos:

- un formulario físico;
- una síntesis;
- un disclosure de proceso;
- una sola instancia de cada campo;
- una sola instancia de los contratos v5.9/v5.13/v5.14/v5.10/v5.11;
- cuatro pasos v5.10;
- cuatro estados v5.11;
- controles de no automatización;
- orden semántico de la jerarquía;
- ausencia de storage/red/scoring nuevo;
- cobertura E2E específica.

## Incidencias resueltas sin debilitar gates

### 1. Compatibilidad histórica v4.9 y v5.10

Al reconstruir el sitio completo, algunos scripts históricos localizaban controles mediante cadenas HTML demasiado literales. La nueva serialización mantenía los mismos campos y límites, pero el orden/forma de atributos podía variar.

La corrección fue version-aware: desde v5.23 se reconoce el control semánticamente dentro del formulario canónico; para versiones anteriores se conserva el comportamiento histórico. Los límites de longitud no cambiaron.

### 2. Truncado del formulario por una sección anidada

La primera síntesis v5.23 se implementó como `<section>`. En la segunda pasada, el helper histórico v4.5 extraía `#contacto` hasta el primer `</section>` y confundía el cierre de la síntesis con el cierre de la sección de contacto. El estado transitorio perdía `message`, privacidad, CTA y cierre del formulario.

La solución corrigió la causa, no el síntoma:

- la síntesis final pasó a `div[role="region"]`;
- v4.5 normaliza, solo desde v5.23, cualquier wrapper materializado antiguo antes de extraer la sección;
- un E2E anti-regresión exige que la síntesis sea `DIV` y que `message`, privacidad y submit permanezcan dentro del formulario.

### 3. Contrato móvil de dos disclosures

La prueba histórica de accesibilidad esperaba dos disclosures separados porque esa era la arquitectura v5.16/v5.19. v5.23 los consolida deliberadamente en uno.

El test se hizo version-aware sin reducir cobertura:

- hasta v5.22 sigue exigiendo exactamente dos;
- desde v5.23 exige exactamente uno;
- además verifica que ese único disclosure contenga v5.10 y v5.11 completos, cuatro estados, controles de no automatización, target mínimo de 44 px, estado colapsado y apertura accesible.

### 4. Contraste WCAG AA real

La primera corrida Browser con el contrato correcto detectó un fallo real de `color-contrast` en cuatro textos de la síntesis oscura. No se excluyeron nodos de axe.

Se corrigieron los colores en `decision-action-v515.css` con márgenes amplios sobre `#102233`:

- `#f5f1e8` ≈ 14.35:1;
- `#e0c58f` ≈ 9.67:1;
- `#d9d2c4` ≈ 10.75:1.

La recertificación posterior dejó axe completamente verde.

### 5. Governance directo de v5.23

Durante los hotfixes se evidenció que los scripts v5.23 se ejecutaban indirectamente por la cadena v5.18, pero no estaban todos listados de forma explícita en los `paths` del builder y Release Governance.

PR #99 cerró esa brecha:

- los tres scripts v5.23 disparan directamente builder/governance;
- Release Governance tiene un paso nominal `Validate contact compression v5.23`;
- el paso valida el estado final ya compuesto y no recompone v5.23 una segunda vez dentro del mismo job.

## Trazabilidad de implementación

- PR #92 — implementación principal de compresión del contacto;
- PR #93 — compatibilidad de segunda pasada en capas históricas;
- PR #95 — corrección raíz del wrapper semántico y E2E de integridad;
- PR #97 — compatibilidad v4.5 sobre HTML materializado previo;
- PR #98 — contrato de accesibilidad version-aware para disclosure único;
- PR #99 — contraste WCAG AA y hardening directo de Governance;
- SHA funcional final certificado: `8d749ab286e8ecbec4d4bd7a083b03dc2b47e5ca`;
- run público final: `31730632791`.

Al cierre funcional:

`main == stable == 8d749ab286e8ecbec4d4bd7a083b03dc2b47e5ca`.

## Evidencia final

### Builder, validación y despliegue

- builder canónico: PASS;
- segunda pasada/idempotencia: PASS;
- validadores históricos: PASS;
- validator v5.23: PASS;
- Pages: PASS;
- smoke público: PASS;
- Browser E2E/axe: PASS;
- Lighthouse: PASS;
- release-health: PASS;
- promoción de `stable`: PASS.

### Browser E2E + axe

Run `31730632791`:

- 58 pruebas observadas;
- 56 PASS;
- 2 SKIP;
- 0 FAIL;
- 0 RETRY;
- reporter wall time: 87 s;
- Chromium desktop;
- Chromium mobile;
- WebKit desktop;
- 7 superficies axe WCAG 2.1 AA sin violaciones serias/críticas.

Las pruebas específicas v5.23 verifican contacto abierto, intención explícita de propuesta e integridad física del formulario. La suite aumentó respecto del piso certificado v5.22 y no redujo cobertura.

### Lighthouse

6/6 superficies PASS, sin relajación de budgets:

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Home | 1.00 | 1.00 | 1304 ms | 0 | 11 ms | 107,322 B |
| Solution IA | 1.00 | 1.00 | 985 ms | 0 | 0 ms | 23,266 B |
| Product IA | 1.00 | 1.00 | 979 ms | 0 | 0 ms | 37,242 B |
| Sector tecnología | 0.98 | 1.00 | 907 ms | 0.087 | 0 ms | 24,322 B |
| Perspective IA | 0.98 | 1.00 | 981 ms | 0.087 | 0 ms | 26,072 B |
| Demo | 1.00 | 1.00 | 904 ms | 0 | 0 ms | 21,988 B |

Budgets vigentes: performance ≥ 0.70, accesibilidad ≥ 0.90, LCP ≤ 4000 ms, CLS ≤ 0.15, TBT ≤ 350 ms y transferencia ≤ 1.5 MB.

### CI

- tiempo hasta gate de `stable`: 264 s;
- baseline v5.5: 279 s;
- mejora frente al baseline: 5.4%;
- cobertura reducida: no;
- budgets relajados: no.

La mayor parte del tiempo Browser corresponde a instalación de dependencias/navegadores; el reporter de la suite fue 87 s.

### Artefactos del run `31730632791`

- Pages: `9193089702`, `sha256:31619db18b44ba746eaca07d9d0dd6b73f5ebd87a7893e6c8df27952a0195533`;
- Lighthouse: `9193157108`, `sha256:d98a955fdadd8d2ad03f5a0a110e77e5cd5cbb75e5275540dbf6d5d28a674390`;
- CI: `9193218997`, `sha256:b98fbbf2b69fb3425526b30a48ddd3db5784f738e08e641d4489e524fbd235d8`;
- release-health: `9193219605`, `sha256:7c7c29957dcb6626cb6ffd1b0350cc687e8e519031d9c81471638a9db5f138cc`.

## Graphify al cierre funcional

Antes del cierre documental, `knowledge/graphify-live/graphify-out/BUILD_META.json` registra:

- `source_commit`: `8d749ab286e8ecbec4d4bd7a083b03dc2b47e5ca`;
- versión: `5.23.0`;
- Graphify: `0.9.26`;
- 675 nodos;
- 1.126 relaciones;
- 96 wiki notes;
- 46 HTML;
- 8 productos fuente;
- 8 servicios fuente;
- 75 scripts Python;
- 25 fuentes JavaScript;
- 9 specs E2E.

El valor `channel` del `version.json` certificado conserva la etiqueta técnica `github-pages-public-contact-compression-candidate`. No se modifica durante el cierre documental porque `version.json` es una entrada funcional vigilada por builder/Pages; el estado de cierre se determina por la promoción de `stable`, la certificación y esta memoria canónica.

## Capacidades externas

Activas y verificables:

- GitHub Pages;
- WhatsApp como handoff manual;
- contexto comercial client-side;
- telemetría first-party/local sin PII;
- sitemap, robots, canonical y Open Graph;
- demo estática/noindex;
- pipeline CI de certificación.

No declarar activas sin implementación/configuración real:

- autenticación o cuentas reales;
- CRM/backend;
- almacenamiento servidor del formulario;
- email transaccional;
- firma electrónica;
- pagos;
- agenda;
- carga documental;
- analítica externa.

## Cierre

v5.23 deja el último tramo comercial con menos superficies visibles y el mismo contenido jurídico verificable. La simplificación se expresa en HTML semántico y progressive disclosure accesible, no en ocultamiento por CSS ni pérdida de controles.

La release funcional queda cerrada en `8d749ab286e8ecbec4d4bd7a083b03dc2b47e5ca`. Cualquier release posterior debe empezar con una auditoría nueva y un contrato independiente; no existe una v5.24 abierta por continuidad automática.
