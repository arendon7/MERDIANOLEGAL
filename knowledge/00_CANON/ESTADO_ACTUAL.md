# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-12.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot público certificado: `stable`.
- Release vigente: `5.21.0`.
- PR funcional: `#79`.
- Merge funcional: `9af1674d9caf6353e233c3b1574cb279f0ee116c`.
- Hotfix compatibilidad UX v4.5: PR `#80`, merge `2bed487ee39a6529b50828af360c153deff286e8`.
- Hotfix robots demo: PR `#81`, merge `5e09f9b2b541437a89397194e0c7a892da72e91c`.
- SHA funcional final generado y certificado: `b2a6d4d4d2608362e86b53ea4cc197cd7ce33cc1`.
- Run final de certificación pública: `31658340092`.
- Snapshot público certificado al cierre funcional: `stable = b2a6d4d4d2608362e86b53ea4cc197cd7ce33cc1`.

Refs, Pages, validators y tests son la autoridad para el estado productivo. `stable` conserva el snapshot funcional certificado; `main` puede avanzar posteriormente con documentación/memoria sin que ello implique una nueva release funcional.

## Estado funcional

**v5.21.0 está implementada, desplegada y funcionalmente certificada. El trabajo restante del ciclo es exclusivamente documental y de frescura de Graphify.**

### Frontera de capacidades v5.21

El portal real de clientes está explícitamente deshabilitado en `site-config.json` mediante `capabilities.client_portal.enabled=false`.

Mientras ese estado permanezca así:

- ninguna superficie indexable puede presentar `demo.html` como “Área de clientes” productiva;
- todos los enlaces públicos hacia `demo.html` deben decir `demo` o `demostrativo`;
- runtime y `site-status.json` deben reflejar la capacidad deshabilitada;
- `demo.html` conserva datos ficticios, marca `demo-only` y exactamente un `noindex,nofollow`;
- `demo.js` no puede inyectar dinámicamente otro meta robots.

Si algún día se habilita el portal, CI exige una URL HTTPS real distinta de `demo.html` y al menos un enlace público real hacia esa URL.

No hay autenticación real, cuentas reales, backend, CRM, storage persistente servidor, email transaccional, firma, pagos, agenda ni carga documental.

## Evidencia funcional final v5.21

Run `31658340092`, SHA certificado `b2a6d4d4d2608362e86b53ea4cc197cd7ce33cc1`:

- builder canónico: PASS;
- segunda pasada/idempotencia: PASS;
- validadores históricos v4.4→v5.18: PASS;
- contrato v5.21 final: PASS;
- GitHub Pages + smoke: PASS;
- Browser E2E + axe: 43 observados → 41 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- reporter Browser: 77 s;
- cobertura ampliada frente a v5.20: 37 → 43 observados;
- 7 superficies axe conservadas;
- Lighthouse: 6/6 PASS;
- accesibilidad Lighthouse: 1.00 en las seis superficies;
- performance Lighthouse: 0.98–1.00;
- portada: performance 1.00, accesibilidad 1.00, LCP 1410 ms, CLS 0, TBT 91 ms;
- máximo global: LCP 1410 ms, CLS 0.087, TBT 91 ms;
- CI hasta `stable`: 178 s;
- baseline v5.5: 279 s;
- mejora: 36.2%;
- cobertura reducida: no;
- budgets relajados: no;
- release-health: PASS;
- promoción de `stable`: PASS.

Artefactos finales del run `31658340092`:

- Lighthouse `9165276023`, `sha256:798847e408280e0730accc2d9a2f7e84ad5f2399aed8c3d9dedad4a77184e6ff`;
- CI `9165288913`, `sha256:df0b5776c71cea97f1d8b51956c1e4750c03626e60f5fb9cfe2988a82d5e5091`;
- release-health `9165289152`, `sha256:0820431f230a5520912a0320ddc0749987743f0a234bd3bba36de38cc0ec28e7`;
- Pages `9165233265`, `sha256:d437eaef17490b4f13396bc7e3c33887bbf095ae94f4f0f70495b8e1ba2ff263`.

## Incidencias resueltas durante v5.21

### Compositor histórico v5.8

Release Governance detectó que `apply_decision_v58.py` intentaba reinsertar la portada v5.8 sobre la superficie unificada v5.20. El compositor quedó version-aware: conserva las 16 fichas y no recrea la capa visual legada cuando la superficie unificada ya existe.

### Compositor histórico v5.12

La siguiente pasada encontró la misma clase de acoplamiento en `apply_proof_v512.py`. Se corrigió sin eliminar el contrato de prueba verificable de las fichas profundas.

### Validator UX v4.5

La primera certificación Pages pasó idempotencia, pero `validate_ux_v45.py` todavía exigía literalmente “Área de clientes”. PR #80 mantiene ese requisito hasta v5.20 y desde v5.21 exige `Demo de cliente`, además de fallar si reaparece la etiqueta productiva anterior.

### Robots duplicado en navegador

La nueva cobertura Browser descubrió que `demo.js` creaba un segundo `meta[name=robots]` aunque el HTML ya incluía uno correcto. El test no se debilitó. PR #81 retiró la inyección JS, normalizó exactamente un meta estático y añadió guards de HTML, runtime y CI para impedir regresión.

## Contratos vigentes

- static-first;
- 46 páginas HTML;
- 16 fichas profundas;
- 1 formulario físico canónico;
- 43 entradas E2E observadas en la certificación final;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- telemetría sin PII;
- analítica externa apagada (`provider:none`);
- WhatsApp manual;
- portal real de clientes explícitamente deshabilitado;
- sin CRM/backend, almacenamiento servidor, autenticación real, firma, pagos, agenda o portal documental ficticios;
- `stable` solo después de gates verdes para cambios funcionales/publicables.

## Graphify / procedencia

Graphify ya reconoce `version = 5.21.0`. El snapshot previo al cierre documental procesó el merge funcional/hotfix y todavía no el commit generado por builder `b2a6d4d4...`.

La frescura final no se presume: después de fusionar el cierre documental debe verificarse `knowledge/graphify-live/graphify-out/BUILD_META.json` y comprobar que `source_commit` corresponda al `main` realmente procesado por el último run exitoso. No fijar como regla permanente un SHA derivado que quede obsoleto por la propia regeneración.

## Estado del ciclo

v5.21 está funcionalmente certificada. El cierre formal exige integrar `RELEASE-v5.21.md`, README y memoria canónica, confirmar diff exclusivamente documental y verificar Graphify fresco. **No se abre v5.22 dentro de este ciclo.**
