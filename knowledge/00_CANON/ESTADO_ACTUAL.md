# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-12.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot público certificado: `stable`.
- Release pública certificada: `5.21.0`.
- Snapshot funcional certificado: `stable = b2a6d4d4d2608362e86b53ea4cc197cd7ce33cc1`.
- Run público final v5.21: `31658340092`.
- Release candidata en desarrollo: `5.22.0` — arquitectura editorial de oferta y narrativa jurídica senior.
- Rama candidata: `feature/v522-offer-narrative`.
- PR funcional candidato: `#84`.

Refs, Pages, validators y tests son la autoridad para el estado productivo. La apertura de v5.22 no modifica el snapshot público certificado: `stable` permanece en v5.21 hasta que builder, idempotencia, Pages, smoke, Browser E2E/axe, Lighthouse y release-health estén verdes.

## Estado funcional

**v5.21.0 está implementada, desplegada, certificada y formalmente cerrada. v5.22.0 está activa únicamente como candidata y todavía no está promovida a `stable`.**

### Frontera de capacidades v5.21

El portal real de clientes está explícitamente deshabilitado en `site-config.json` mediante `capabilities.client_portal.enabled=false`.

Mientras ese estado permanezca así:

- ninguna superficie indexable puede presentar `demo.html` como “Área de clientes” productiva;
- todos los enlaces públicos hacia `demo.html` deben decir `demo` o `demostrativo`;
- runtime y `site-status.json` deben reflejar la capacidad deshabilitada;
- `demo.html` conserva datos ficticios, marca `demo-only` y exactamente un `noindex,nofollow`;
- `demo.js` no puede inyectar dinámicamente otro meta robots.

No hay autenticación real, cuentas reales, backend, CRM, storage persistente servidor, email transaccional, firma, pagos, agenda ni carga documental.

## Evidencia funcional final v5.21

Run `31658340092`, SHA certificado `b2a6d4d4d2608362e86b53ea4cc197cd7ce33cc1`:

- builder canónico e idempotencia: PASS;
- validadores históricos y capability truth: PASS;
- GitHub Pages + smoke: PASS;
- Browser E2E + axe: 43 observados → 41 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- 7 superficies axe conservadas;
- Lighthouse: 6/6 PASS;
- accesibilidad Lighthouse: 1.00 en las seis superficies;
- performance Lighthouse: 0.98–1.00;
- portada: performance 1.00, accesibilidad 1.00, LCP 1410 ms, CLS 0, TBT 91 ms;
- CI hasta `stable`: 178 s;
- baseline v5.5: 279 s;
- mejora: 36.2%;
- cobertura reducida: no;
- budgets relajados: no;
- release-health: PASS.

Artefactos finales del run `31658340092`:

- Lighthouse `9165276023`, `sha256:798847e408280e0730accc2d9a2f7e84ad5f2399aed8c3d9dedad4a77184e6ff`;
- CI `9165288913`, `sha256:df0b5776c71cea97f1d8b51956c1e4750c03626e60f5fb9cfe2988a82d5e5091`;
- release-health `9165289152`, `sha256:0820431f230a5520912a0320ddc0749987743f0a234bd3bba36de38cc0ec28e7`;
- Pages `9165233265`, `sha256:d437eaef17490b4f13396bc7e3c33887bbf095ae94f4f0f70495b8e1ba2ff263`.

## Release activa v5.22

### Problema observable

Las 16 fichas profundas ya conservan buen perímetro, cantidades, entregables, responsabilidades, criterios de aceptación y límites. La debilidad auditada está en la lectura comercial/editorial: productos y servicios se perciben demasiado parecidos, varias ofertas cercanas se solapan y parte de la mejor narrativa jurídica de versiones anteriores quedó diluida al superponer capas posteriores.

### Objetivo

Reconciliar las mejores decisiones históricas de contenido con el catálogo v4.1/v4.2 y la arquitectura de compra v5.20–v5.21, sin crear ofertas nuevas ni inflar la página con otro selector.

Cada una de las 16 fichas conserva su profundidad y añade una sola capa editorial source-driven por `catalog-id` que responde:

1. qué decisión empresarial debe poder tomar la dirección;
2. por qué conviene esa modalidad;
3. cuál es la alternativa cercana y cuándo elegirla;
4. qué lente jurídica gobierna el análisis;
5. qué capacidad queda instalada o administrable al cierre.

Pares prioritarios de diferenciación:

- Diagnóstico Jurídico Empresarial ↔ Auditoría Jurídica Empresarial Integral;
- Contratación Estratégica ↔ Sistema Contractual Empresarial;
- Propiedad Intelectual ↔ Activos Intangibles Protegidos;
- Tecnología e IA ↔ Programa de Gobernanza Jurídica de IA;
- Estructuración de Proyectos Regulados ↔ Proyecto Regulado Jurídicamente Estructurado.

La portada conserva la secuencia v5.20 y una sola superficie de modalidad. La nueva tesis enfatiza decisión, resultado, perímetro, método, evidencia, implementación y capacidad instalada. El seniority se demuestra mediante criterio jurídico, preguntas de control, fuentes, responsables y cierre; no mediante clientes, premios, antigüedad o resultados no verificables.

### Estado técnico de la candidata

- `offer-narrative-v522.json`: contrato editorial de las 16 ofertas;
- `offer-v522.css`: presentación trust-first, baja variación y sin motion decorativo;
- `scripts/apply_offer_narrative_v522.py`: normalizador final source-driven;
- `scripts/validate_offer_narrative_v522.py`: contrato anti-drift;
- `tests/e2e/offer-narrative.spec.mjs`: cobertura de portada y fichas;
- builder, Pages y Release Governance vigilan explícitamente las nuevas fuentes;
- `CONTEXTO_RAPIDO.md` fue actualizado desde su estado obsoleto v5.18.

Release Governance del PR #84 ya confirmó en una segunda pasada que la cadena histórica v5.8→v5.21 y el contrato v5.22 pueden coexistir. Esta evidencia es de candidata y no equivale todavía a certificación pública.

## Invariantes vigentes

- static-first;
- 46 páginas HTML;
- 16 fichas profundas;
- 1 formulario físico canónico;
- 43 pruebas E2E observadas en v5.21 como piso de cobertura;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- telemetría sin PII;
- analítica externa apagada (`provider:none`);
- WhatsApp manual;
- portal real de clientes explícitamente deshabilitado;
- sin CRM/backend, almacenamiento servidor, autenticación real, firma, pagos, agenda o portal documental ficticios;
- sin claims de clientes, premios, experiencia o resultados no verificables;
- `stable` solo después de gates verdes para cambios funcionales/publicables.

## Graphify / procedencia

La rama `knowledge/graphify-live` es memoria derivada. La comprobación correcta de frescura es leer `graphify-out/BUILD_META.json` y verificar que `source_commit` coincida con el `main` realmente procesado por el último run exitoso; no fijar un SHA derivado como regla permanente.

## Estado del ciclo

v5.22 está abierta con objetivo, contrato, no-objetivos y criterios de cierre definidos. No debe promoverse ni declararse cerrada hasta superar builder canónico, segunda pasada, validadores históricos + v5.22, Pages, smoke, Browser E2E/axe, Lighthouse, release-health, actualización controlada de `stable` y cierre documental. **No existe una v5.23 activa.**
