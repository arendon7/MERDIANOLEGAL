# Meridiano Legal — Tarea activa

Actualizado: 2026-08-12.

## Estado

**v5.21.0 — frontera de capacidades reales y superficies demostrativas — funcionalmente certificada; cierre documental en curso.**

No hay desarrollo funcional pendiente dentro de v5.21. El runtime público ya superó builder, idempotencia, validadores, Pages, smoke, Browser E2E, axe, Lighthouse y release-health y fue promovido a `stable`.

## Evidencia funcional

- PR funcional: #79.
- Hotfix UX v4.5: #80.
- Hotfix robots demo: #81.
- SHA funcional final: `b2a6d4d4d2608362e86b53ea4cc197cd7ce33cc1`.
- Run final: `31658340092`.
- Snapshot certificado: `main == stable == b2a6d4d4d2608362e86b53ea4cc197cd7ce33cc1` al cierre funcional.
- Browser E2E + axe: 43 → 41 PASS / 2 SKIP / 0 FAIL / 0 RETRY.
- Lighthouse: 6/6 PASS; accesibilidad 1.00; performance 0.98–1.00.
- Portada: performance 1.00, accesibilidad 1.00, LCP 1410 ms, CLS 0, TBT 91 ms.
- CI hasta `stable`: 178 s, 36.2% mejor que baseline 279 s.
- cobertura reducida: no.
- budgets relajados: no.

## Contrato v5.21

- portal real de clientes explícitamente `disabled`;
- URL del portal vacía mientras esté deshabilitado;
- `demo.html` nunca puede configurarse como portal real;
- 25 accesos públicos hacia la demo deben estar etiquetados como `demo`/`demostrativo`;
- `runtime-config.js` y `site-status.json` reflejan el estado canónico;
- demo con datos ficticios, `demo-only` y exactamente un `noindex,nofollow`;
- `demo.js` sin inyección dinámica de robots meta;
- futura activación del portal exige URL HTTPS real y acceso público verificable;
- sin autenticación, cuentas reales, backend, CRM, PII, persistencia servidor ni transporte nuevo.

## Cierre pendiente

1. integrar `RELEASE-v5.21.md`;
2. alinear README y memoria canónica;
3. confirmar que el diff es exclusivamente documental;
4. fusionar el cierre documental;
5. verificar Graphify posterior y su frescura/versionado `5.21.0`;
6. marcar el ciclo como formalmente cerrado y dejar explícito que no existe v5.22 abierta.

No es necesario modificar de nuevo `stable`: debe conservar el snapshot funcional certificado salvo que exista un cambio funcional/publicable posterior.

## No objetivos

- no nuevas features;
- no construir portal real en este cierre;
- no ampliar catálogo;
- no reescribir fichas profundas;
- no backend/CRM;
- no nueva analítica externa;
- no modificar retrospectivamente el contrato certificado v5.21;
- no abrir v5.22 dentro de este cierre.
