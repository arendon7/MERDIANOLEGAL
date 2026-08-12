# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-12.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot certificado: `stable`.
- Release declarada en este cierre: `5.16.0`.
- SHA funcional certificado antes del cierre documental: `2cd5fb0d2b428187c08cf21e562427f9bc44508c`.
- Run funcional final: `31618614227`.
- Estado de refs antes del cierre documental: `main == stable == 2cd5fb0d2b428187c08cf21e562427f9bc44508c`.

Refs, Pages y gates son la autoridad para el estado productivo. El SHA definitivo de 5.16.0 será el que contenga este cierre formal, sincronice la versión visible y vuelva a superar la certificación completa.

## Estado funcional

**v5.16 está funcionalmente certificada y en cierre formal.**

El ciclo reduce fricción móvil y cierra causas reales de accesibilidad sin esconder contenido jurídico material ni alterar el modelo comercial. La mejora se apoyó en diagnóstico Lighthouse de auditorías con score < 1, no en cambios a ciegas.

### Implementación principal

- `scripts/run_quality_v55.mjs`: conserva auditorías Lighthouse de accesibilidad con score < 1 y detalles acotados;
- `scripts/validate_quality_v55.py`: blinda observabilidad, budgets y reglas v5.16;
- `decision-action-v515.css` / `.js`: targets táctiles, progressive disclosure móvil, regiones desplazables accesibles y contraste corregido;
- `proof-v512.css`: hardening final de menú/CTA de fichas profundas;
- `tests/e2e/accessibility.spec.mjs`: portada y ficha profunda en viewport móvil real, sin aumentar las 37 entradas.

### UX móvil

- tres CTA “Explorar la práctica” tienen target mínimo de 44 px;
- calificación, contexto, recomendación y ruta comercial permanecen visibles;
- únicamente el detalle secundario de v5.10/v5.11 se repliega en `<details>` nativos en móvil;
- sin JS, el HTML permanece expandido;
- tres regiones horizontalmente desplazables reciben foco, rol, nombre accesible y foco visible;
- menú profundo, sus cinco enlaces y CTA fijo cumplen targets/contraste móvil.

v5.16 no añade cuestionario, scoring, `localStorage`, `sessionStorage`, backend, XHR/fetch propio ni PII adicional.

## Evidencia funcional final v5.16

Run `31618614227`, SHA `2cd5fb0d2b428187c08cf21e562427f9bc44508c`:

- builder/idempotencia + validadores históricos + hardening v5.16: PASS;
- GitHub Pages + smoke: PASS;
- Browser E2E + axe: 37 observados → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- 7 superficies axe: sin violaciones serias/críticas;
- Lighthouse: 6/6 PASS;
- accesibilidad Lighthouse: 1.00 en las seis superficies;
- `accessibilityAuditGaps`: vacío en las seis superficies;
- portada: performance 1.00, a11y 1.00, LCP 1255 ms, CLS 0, TBT 7 ms, 101,214 B;
- solución IA: 1.00 / 1.00, LCP 902 ms;
- producto IA: 1.00 / 1.00, LCP 905 ms, CLS 0, TBT 0 ms, 37,789 B;
- sector tecnología: 0.98 / 1.00, LCP 905 ms, CLS 0.087;
- perspectiva IA: 1.00 / 1.00, LCP 902 ms;
- demo: 1.00 / 1.00, LCP 905 ms;
- CI hasta `stable`: 187 s;
- baseline v5.5: 279 s;
- mejora frente al baseline: 33.0%;
- cobertura reducida: no;
- budgets relajados: no.

Artefactos de referencia:
- Lighthouse `9150367908`, digest `sha256:73290506d7149c03299ffd43c82a30f13b11ad2af801cc5a19aa411f8c0e002d`;
- CI `9150389424`, digest `sha256:a130b599977430eb908f59a33be8eab127d6f490b9c3acb86d79b70b4ce58b33`.

## Gates que v5.16 aprovechó, no debilitó

1. Lighthouse identificó `target-size` en tres CTA de Perspectivas detrás del 0.97 de portada; se corrigió a 1.00;
2. axe móvil reveló contraste insuficiente en un paso v5.10 y falta de acceso de teclado en tres regiones desplazables Safari; se corrigieron en fuente;
3. el diagnóstico Lighthouse ampliado expuso A11y 0.91 en la ficha Programa de Gobernanza IA por CTA/menú móvil; no se cerró la release hasta llevarla a 1.00;
4. ninguna corrección redujo tests, superficies, budgets o severidad de axe.

## Contratos vigentes

- 46 páginas HTML;
- 16 fichas profundas;
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

El snapshot funcional vigente se construyó exactamente sobre `source_commit = 2cd5fb0d2b428187c08cf21e562427f9bc44508c`, Graphify 0.9.26, 548 nodos, 882 relaciones y 88 notas wiki. Conserva `version = 5.15.0` y el canal anterior únicamente porque `version.json` todavía no se había elevado cuando se generó. El cierre formal 5.16.0 debe reconstruir Graphify desde el commit real correspondiente; no se debe reescribir `source_commit` manualmente.

## Gate de cierre formal

La release 5.16.0 queda definitivamente cerrada cuando el SHA que incluye este versionado vuelva a pasar builder, idempotencia, Pages, smoke, Browser/axe, Lighthouse y release-health, y `main == stable` en ese SHA.

## Próximo ciclo candidato

**v5.17 — continuidad del handoff comercial.** Mejorar la transición entre resumen preparado, WhatsApp manual y expectativa de respuesta, con foco móvil y sin inventar backend, CRM, envío automático o almacenamiento servidor.
