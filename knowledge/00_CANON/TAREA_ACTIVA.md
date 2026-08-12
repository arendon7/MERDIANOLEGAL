# Meridiano Legal — Tarea activa

Actualizado: 2026-08-12.

## Release en cierre formal

**v5.17.0 — continuidad manual y verificable del handoff a WhatsApp.**

La funcionalidad está certificada. Evidencia de referencia antes de este cierre documental:

- SHA funcional: `56f99a5398b1e0505da5acd601bac3aec8588c1d`;
- run funcional: `31628244159`;
- `main == stable` en ese SHA;
- builder/idempotencia + validadores históricos + v5.17: PASS;
- Pages + smoke: PASS;
- Browser E2E + axe: 37 → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- reporter Browser: 71 s;
- 7 superficies axe limpias;
- Lighthouse: 6/6 PASS, accesibilidad 1.00 en las seis superficies y `accessibilityAuditGaps` vacío;
- CI hasta `stable`: 181 s;
- baseline v5.5: 279 s;
- mejora: 35.1%;
- cobertura reducida: no;
- budgets relajados: no.

## Qué cerró funcionalmente v5.17

1. un único formulario físico canónico en `index.html`;
2. 16 fichas profundas con rutas contextuales a ese formulario, sin duplicarlo;
3. panel post-preparación con referencia, reabrir WhatsApp, copiar resumen y editar solicitud;
4. eliminación de la copia automática silenciosa al portapapeles;
5. borrador v5.17 únicamente efímero en memoria de la página;
6. protección stale: si cambia el formulario, copiar/reabrir quedan bloqueados hasta preparar de nuevo;
7. no repetición de nombre, empresa, email ni mensaje completo dentro del panel DOM;
8. declaración expresa de que la web no conoce entrega, lectura, aceptación, apertura de expediente ni inicio;
9. applicator semántico capaz de eliminar paneles residuales, marcadores huérfanos y restaurar condicionadamente el cierre canónico del formulario;
10. Pages termina idempotencia en v5.17 y ejecuta su validator explícito;
11. Governance normaliza outputs materializados v5.17 antes de ejecutar intacta la cadena histórica v5.8→v5.15.

## Gates que deben recordarse

- candidato `bed3baf0…`, Pages `31622876902`: idempotencia roja;
- candidato `b9387731…`, Pages `31623621877`: ID duplicado + panel residual + cierre de formulario perdido;
- PR #65: reparación estructural y preflight Governance;
- candidato final `56f99a53…`: todos los gates verdes y promoción a `stable`.

Estos fallos son evidencia útil. No deben eliminarse de la memoria de release ni convertirse en excepciones futuras.

## Condición de cierre definitivo de v5.17.0

El SHA que contenga este cierre/versionado debe atravesar nuevamente:

1. builder canónico y sincronización visible a 5.17.0;
2. idempotencia + todos los validators históricos + v5.17;
3. Pages + smoke;
4. Browser E2E/axe;
5. Lighthouse y revisión del artifact de accesibilidad;
6. release-health y trigger guard;
7. promoción de `stable`;
8. verificación `main == stable`;
9. inspección/alineación Graphify sin falsificar `source_commit`;
10. si existe un commit generado exclusivo de versión/output, documentar equivalencia mediante comparación real.

**v5.18 no inicia hasta que esos diez puntos estén verdes sobre el SHA final versionado.**

## Próximo ciclo después del cierre

**v5.18 — no iniciado.**

El alcance deberá definirse con evidencia posterior al cierre. Una dirección candidata es auditar continuidad y medición comercial después del handoff manual, pero sin asumir que exista CRM, backend, automatización de WhatsApp, email, agenda o almacenamiento servidor.

## No objetivos heredados

- no backend/CRM;
- no envío automático de WhatsApp;
- no email transaccional;
- no firma, pagos, agenda o expediente;
- no persistencia nueva del borrador comercial;
- no PII adicional en telemetría;
- no scoring opaco;
- no relajar budgets/axe/E2E.

## Contratos a preservar

- static-first;
- 46 páginas HTML;
- 16 fichas profundas;
- 1 formulario físico canónico;
- 37 entradas E2E salvo necesidad independiente demostrada;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5;
- fuente jurídica única;
- WhatsApp manual;
- telemetría sin PII;
- builder idempotente;
- `stable` solo después de todos los gates verdes.
