# Meridiano Legal v5.17.0 — continuidad manual y verificable del handoff

Fecha: 2026-08-12.

## Objetivo

Reducir la fricción entre una solicitud comercial ya preparada y la conversación manual en WhatsApp, preservando el control del usuario y la arquitectura estática del sitio. v5.17 no convierte la web en CRM, no declara enviado un mensaje que la web no puede verificar y no persiste el contenido de la solicitud.

## Implementación

### 1. Un formulario canónico y 16 rutas contextuales

La arquitectura real conserva un único formulario físico en `index.html`. Las 8 fichas de productos y 8 fichas de servicios no duplican ese formulario: trasladan modalidad, estándar de prueba e intención comercial mediante rutas contextuales hacia `index.html#contacto`.

### 2. Panel posterior a la preparación del handoff

Después de preparar la solicitud, el usuario conserva una superficie operativa con:

- referencia de la solicitud preparada;
- acción explícita **Abrir WhatsApp de nuevo**;
- acción explícita **Copiar resumen**;
- acción **Editar solicitud**;
- explicación de qué ocurre después y de qué no puede conocer la web estática.

La solicitud solo se considera enviada cuando el usuario confirma manualmente el envío en WhatsApp.

### 3. Copia explícita y borrador efímero

Se eliminó la copia automática silenciosa al portapapeles. El resumen sigue prellenado en la URL de WhatsApp, pero copiarlo es una decisión explícita del usuario.

El borrador de continuidad existe únicamente en memoria de la página. v5.17 no introduce `localStorage`, `sessionStorage`, backend, fetch/XHR, `sendBeacon` ni almacenamiento servidor.

### 4. Protección contra borrador desactualizado

Si el usuario modifica el formulario después de preparar el handoff, el panel cambia a estado desactualizado y deshabilita **Copiar resumen** y **Abrir WhatsApp de nuevo** hasta volver a preparar la solicitud. Esto evita reutilizar un mensaje que ya no coincide con los datos visibles.

### 5. Privacidad y límites verificables

El panel no replica en el DOM el nombre, empresa, email ni texto completo de contexto. La telemetría continúa sin PII.

La interfaz declara expresamente que la web no recibe confirmación de:

- entrega del mensaje;
- lectura;
- aceptación de propuesta o contrato;
- apertura de expediente;
- inicio del encargo.

## Hardening de composición y governance

v5.17 fortaleció además la relación fuente → builder → Pages:

- `scripts/apply_handoff_v517.py` recompone la capa como última etapa canónica;
- Pages vuelve a aplicar v5.17 antes del gate de idempotencia;
- `scripts/validate_handoff_v517.py` se ejecuta en quality y en release-health;
- el runtime v5.17 pasa `node --check`;
- Release Governance normaliza outputs v5.17 materializados antes de ejecutar intacta la secuencia histórica v5.8→v5.15;
- el applicator elimina paneles residuales por identidad semántica, limpia marcadores huérfanos y exige una única instancia/ID;
- si un output roto perdió el cierre histórico del formulario, lo restaura únicamente bajo una condición verificable y vuelve a exigir que el formulario cierre antes de `</main>`.

## Gates que detectaron defectos reales

La release no se hizo pasar mediante excepciones ni relajación de QA.

### Candidato 1

SHA `bed3baf0fbec58b85f74bbb97509d15b717f387f`  
Pages run `31622876902`.

Falló correctamente en idempotencia: la reconstrucción de Pages terminaba en v5.15 y una capa previa restauraba la copia automática histórica y desplazaba el tail de contacto. Se corrigió haciendo que Pages termine la composición en v5.17 y validando ese wiring.

### Candidato 2

SHA `b938773173985ab687e5cfdc6d3376f94e9d80c9`  
Pages run `31623621877`.

La idempotencia ya pasó, pero `validate_site.py` detectó el ID duplicado `handoff-v517-title`. La inspección reveló además una segunda sección residual y la pérdida del cierre canónico `</form></div></div></section>`. El applicator se endureció para limpiar por `data-handoff-v517`, restaurar el cierre solo cuando falta y abortar si no quedan exactamente un panel, un título y marcadores balanceados.

### Gate de PR reparador

PR #65 demostró que, una vez normalizado el output roto, los validators históricos v5.8→v5.15 vuelven a pasar sin ser modificados, incluido v5.10. El validator final v5.17 también quedó verde antes del merge.

## Evidencia funcional certificada

Run: `31628244159`  
SHA funcional: `56f99a5398b1e0505da5acd601bac3aec8588c1d`

- `main == stable == 56f99a5398b1e0505da5acd601bac3aec8588c1d` al cierre funcional;
- builder + idempotencia + validadores históricos + v5.17: PASS;
- Pages + smoke: PASS;
- Browser E2E + axe: 37 observados → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- tiempo de pared Browser reporter: 71 s;
- axe WCAG 2.1 AA sin violaciones serias/críticas en las 7 superficies protegidas;
- Lighthouse: 6/6 PASS;
- accesibilidad Lighthouse: 1.00 en las seis superficies;
- `accessibilityAuditGaps`: vacío en las seis superficies;
- CI hasta `stable`: 181 s;
- baseline v5.5: 279 s;
- mejora frente al baseline: 35.1%;
- cobertura reducida: no;
- budgets relajados: no.

### Lighthouse funcional

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT |
|---|---:|---:|---:|---:|---:|
| Portada | 1.00 | 1.00 | 1276 ms | 0 | 1 ms |
| Solución IA | 1.00 | 1.00 | 904 ms | 0 | 0 ms |
| Producto IA | 1.00 | 1.00 | 919 ms | 0 | 0 ms |
| Sector tecnología | 0.98 | 1.00 | 947 ms | 0.087 | 0 ms |
| Perspectiva IA | 0.98 | 1.00 | 906 ms | 0.087 | 0 ms |
| Demo | 1.00 | 1.00 | 948 ms | 0 | 0 ms |

Artefactos:

- Lighthouse `9154061576` — `sha256:7e128bbc31eaa9512ea1cfc5e37ee056bf4de182d423eaa9b9ea3dfe90e402d2`;
- CI `9154078333` — `sha256:779c4ff6c048a8a905a3f770c826143ecac167bc2834b0d7349a18cf67cdee6d`.

## Límites preservados

v5.17 no añade:

- CRM o backend;
- almacenamiento servidor del formulario;
- envío automático de WhatsApp;
- email transaccional;
- firma electrónica;
- pagos;
- agenda;
- expediente o portal documental real;
- `localStorage` o `sessionStorage` para el borrador v5.17;
- transporte fetch/XHR propio;
- scoring opaco;
- PII adicional en telemetría;
- testimonios, clientes o resultados fabricados.

## Contratos preservados

- 46 páginas HTML;
- 16 fichas profundas;
- 1 formulario físico canónico;
- 37 entradas E2E;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- workers Playwright CI = 1;
- fuente jurídica única;
- WhatsApp como handoff manual;
- `stable` solo después de todos los gates verdes.

## Graphify / procedencia

Graphify debe conservar el `source_commit` que realmente haya extraído. Este cierre documental no autoriza reescribir ese campo para hacerlo coincidir artificialmente con un commit generado por el builder.

Después del merge formal, si el builder crea un commit exclusivo de sincronización visible de versión, la equivalencia deberá demostrarse mediante comparación de commits y documentarse en la rama de conocimiento, manteniendo intacta la procedencia real de Graphify.

## Condición de cierre definitivo

Este documento declara `5.17.0`, pero la release solo queda definitivamente cerrada cuando el SHA versionado resultante vuelva a superar:

1. builder y sincronización visible;
2. idempotencia y todos los validators, incluido v5.17;
3. Pages + smoke;
4. Browser E2E + axe;
5. Lighthouse y revisión del artifact;
6. release-health;
7. promoción de `stable`;
8. verificación `main == stable`;
9. alineación de procedencia Graphify sin falsificar `source_commit`.

v5.18 no inicia antes de ese cierre.
