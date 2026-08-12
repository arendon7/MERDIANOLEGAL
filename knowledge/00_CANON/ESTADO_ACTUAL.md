# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-12.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot certificado: `stable`.
- Release declarada en este cierre: `5.17.0`.
- SHA funcional certificado antes del cierre documental: `56f99a5398b1e0505da5acd601bac3aec8588c1d`.
- Run funcional final: `31628244159`.
- Estado de refs antes del cierre documental: `main == stable == 56f99a5398b1e0505da5acd601bac3aec8588c1d`.

Refs, Pages y gates son la autoridad para el estado productivo. El SHA definitivo de 5.17.0 será el que contenga este cierre formal, sincronice la versión visible y vuelva a superar la certificación completa.

## Estado funcional

**v5.17 está funcionalmente certificada y en cierre formal.**

El ciclo mejora la continuidad entre la preparación de la solicitud y el handoff manual a WhatsApp, sin introducir backend, CRM, persistencia del formulario ni automatización ficticia del envío.

### Arquitectura comercial v5.17

- existe un único formulario físico canónico en `index.html`;
- las 8 fichas de productos y 8 fichas de servicios no duplican el formulario;
- esas 16 fichas preservan modalidad, estándar verificable e intención mediante rutas contextuales hacia `index.html#contacto`;
- después de preparar una solicitud aparece un panel con referencia y acciones manuales para reabrir WhatsApp, copiar el resumen o editar;
- la copia automática silenciosa al portapapeles fue eliminada;
- el borrador vive únicamente en memoria de la página;
- si el usuario cambia el formulario, el borrador queda `changed/stale` y copiar/reabrir se deshabilitan hasta volver a prepararlo;
- el panel no replica nombre, empresa, email ni mensaje completo en el DOM;
- la web declara expresamente que no conoce entrega, lectura, aceptación, apertura de expediente ni inicio del encargo.

### Hardening de composición

- `scripts/apply_handoff_v517.py` es la última capa canónica del builder;
- limpia paneles residuales por identidad `data-handoff-v517`, no solo por comentarios;
- elimina marcadores START/END huérfanos;
- repara el cierre histórico `</form></div></div></section>` únicamente cuando el único formulario perdió su cierre antes de `</main>`;
- aborta si no queda exactamente un panel, un `handoff-v517-title` y marcadores balanceados;
- Pages termina su prueba de idempotencia reaplicando v5.17;
- Pages ejecuta el validator v5.17 y valida sintaxis de su runtime;
- Release Governance normaliza outputs materializados v5.17 antes de correr la secuencia histórica v5.8→v5.15, sin modificar ni debilitar esos validators.

## Gates que detectaron problemas reales

### Candidato `bed3baf0…`

Pages run `31622876902` falló en idempotencia. La segunda composición todavía terminaba en v5.15, permitiendo que una capa previa restaurara la copia automática y desplazara el tail de contacto. Se corrigió el wiring de Pages y se blindó desde el validator v5.17.

### Candidato `b9387731…`

Pages run `31623621877` pasó idempotencia, pero `validate_site.py` detectó `handoff-v517-title` duplicado. La inspección encontró un segundo panel residual y la pérdida del cierre del formulario. Se corrigió en el applicator, no en el gate.

### PR #65

El PR reparador añadió limpieza semántica, restauración condicionada del cierre, preflight de Governance y contratos estructurales. El run Governance demostró que, tras normalizar el output, v5.8→v5.15 vuelven a pasar intactos, incluido v5.10, y que el validator final v5.17 también pasa.

Ningún problema se resolvió reduciendo cobertura, severity, budgets o conteo de tests.

## Evidencia funcional final v5.17

Run `31628244159`, SHA `56f99a5398b1e0505da5acd601bac3aec8588c1d`:

- builder/idempotencia + validadores históricos + v5.17: PASS;
- GitHub Pages + smoke: PASS;
- Browser E2E + axe: 37 observados → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- tiempo de pared reporter: 71 s;
- 7 superficies axe: sin violaciones serias/críticas;
- Lighthouse: 6/6 PASS;
- accesibilidad Lighthouse: 1.00 en las seis superficies;
- `accessibilityAuditGaps`: vacío en las seis superficies;
- portada: performance 1.00, a11y 1.00, LCP 1276 ms, CLS 0, TBT 1 ms, 104,394 B;
- solución IA: 1.00 / 1.00, LCP 904 ms;
- producto IA: 1.00 / 1.00, LCP 919 ms, CLS 0, TBT 0 ms;
- sector tecnología: 0.98 / 1.00, LCP 947 ms, CLS 0.087;
- perspectiva IA: 0.98 / 1.00, LCP 906 ms, CLS 0.087;
- demo: 1.00 / 1.00, LCP 948 ms;
- CI hasta `stable`: 181 s;
- baseline v5.5: 279 s;
- mejora frente al baseline: 35.1%;
- cobertura reducida: no;
- budgets relajados: no.

Artefactos de referencia:
- Lighthouse `9154061576`, digest `sha256:7e128bbc31eaa9512ea1cfc5e37ee056bf4de182d423eaa9b9ea3dfe90e402d2`;
- CI `9154078333`, digest `sha256:779c4ff6c048a8a905a3f770c826143ecac167bc2834b0d7349a18cf67cdee6d`.

## Contratos vigentes

- 46 páginas HTML;
- 16 fichas profundas;
- 1 formulario físico canónico;
- 37 entradas E2E;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- workers Playwright CI = 1;
- fuente jurídica única para alcance/entregables;
- telemetría sin PII;
- WhatsApp manual;
- scoring opaco desactivado;
- sin CRM/backend ni almacenamiento servidor del formulario;
- sin firma, pagos, agenda o portal documental ficticios.

## Graphify / procedencia

Graphify debe conservar el `source_commit` que realmente haya extraído. El cierre formal 5.17.0 debe producir/alinear un snapshot desde el commit real correspondiente. Si posteriormente el builder genera un commit exclusivo de sincronización visible, la relación entre ambos debe documentarse mediante comparación de commits; no se debe reescribir `source_commit` manualmente.

## Gate de cierre formal

La release 5.17.0 queda definitivamente cerrada cuando el SHA que incluye este versionado vuelva a pasar builder, idempotencia, Pages, smoke, Browser/axe, Lighthouse y release-health, `main == stable` en ese SHA, y la procedencia Graphify quede alineada sin falsificación.

## Próximo ciclo candidato

**v5.18 no está iniciado.** El alcance se define únicamente después del cierre formal. Puede evaluarse continuidad/medición comercial posterior al handoff si existe evidencia suficiente, siempre sin convertir la web en CRM/backend ni añadir automatismos ficticios.
