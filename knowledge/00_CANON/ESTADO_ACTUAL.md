# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-13.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot público certificado: `stable`.
- Release pública certificada y cerrada: `5.22.0`.
- SHA funcional de las mejoras v5.22: `5c3f3194b45afb9ac21a8def27afdc3d2157b3e2`.
- Run de certificación funcional: `31671834728`.
- Snapshot público final `ready`: `stable = dcb5bc9643eff595c0f8614c7cf6acbadc3bb719`.
- Run final de recertificación `ready`: `31673266141`.
- Canal: `github-pages-public-offer-narrative-ready`.
- No existe una release funcional posterior activa.

El SHA `5c3f3194…` identifica el cierre funcional de las mejoras de producto/contenido. El SHA `dcb5bc96…` incorpora además el cierre documental y metadata `ready` y volvió a superar toda la certificación pública. Después de este punto, commits exclusivamente documentales pueden hacer avanzar `main` sin mover `stable`, siempre que no modifiquen runtime o salida pública.

## Estado funcional

**v5.22.0 está implementada, desplegada, certificada y formalmente cerrada.**

La release reconcilia la mejor narrativa histórica con el catálogo profundo v4.1/v4.2 y la arquitectura comercial v5.20–v5.21, sin crear ofertas nuevas.

### Arquitectura editorial v5.22

Cada una de las 16 fichas profundas conserva su perímetro, cantidades, entregables, responsabilidades, aceptación y límites, y añade una única capa source-driven que explica:

1. decisión empresarial;
2. por qué esa modalidad;
3. alternativa cercana;
4. lente jurídica;
5. capacidad instalada.

Cinco pares quedan explícitamente diferenciados:

- Diagnóstico Jurídico Empresarial ↔ Auditoría Jurídica Empresarial Integral;
- Contratación Estratégica ↔ Sistema Contractual Empresarial;
- Propiedad Intelectual ↔ Activos Intangibles Protegidos;
- Tecnología e IA ↔ Programa de Gobernanza Jurídica de IA;
- Proyectos Regulados a medida ↔ Proyecto Regulado de alcance cerrado.

La portada conserva una sola superficie de modalidad v5.20 y refuerza la tesis de que el criterio jurídico debe convertirse en decisiones, instrumentos, responsables y acciones verificables.

### Criterio jurídico y seniority

La autoridad profesional se demuestra mediante preguntas de control, régimen, fuentes, supuestos, materialidad, responsables, método, perímetro, exclusiones, entregables, aceptación y cierre. No se publican claims no verificables sobre clientes, premios, antigüedad, liderazgo o resultados garantizados.

En IA, el CONPES 4144 de 2025 se trata como política pública nacional y se distingue de derecho vinculante y proyectos legislativos. Las obligaciones vigentes se analizan por materia y sector.

### Capability truth source-driven

La frontera v5.21 continúa vigente:

- portal real de clientes deshabilitado;
- `demo.html` ficticio/noindex;
- WhatsApp manual;
- sin autenticación real, CRM/backend, storage servidor, firma, pagos, agenda o carga documental.

v5.22 endurece además el source-of-truth del catálogo: `Meridiano Empresas` solo puede aparecer condicionado a una habilitación productiva real o como demostración explícita. El compositor no muta silenciosamente el contrato fuente después del render.

### Static-first real en navegador

El runtime preserva el HTML prerenderizado de las fichas cuando `#detail-page` declara `data-static-catalog="true"`. `catalog-page.js` ya no reemplaza la salida canónica con el template dinámico legado; el renderer dinámico queda como fallback para superficies no canónicas.

## Evidencia funcional v5.22

Run `31671834728`, SHA funcional `5c3f3194b45afb9ac21a8def27afdc3d2157b3e2`:

- builder + idempotencia: PASS;
- validadores históricos + v5.22: PASS;
- Pages + smoke: PASS;
- Browser E2E + axe: 49 observados → 47 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- 7 superficies axe WCAG 2.1 AA sin violaciones serias/críticas;
- Lighthouse: 6/6 PASS;
- accesibilidad Lighthouse: 1.00 en las seis superficies;
- performance Lighthouse: 0.96–1.00;
- portada: performance 1.00, accesibilidad 1.00, LCP 1367 ms, CLS 0, TBT 55 ms;
- Product IA: performance 0.96, accesibilidad 1.00, LCP 1245 ms, CLS 0, TBT 210 ms;
- CI hasta `stable`: 206 s;
- mejora frente a baseline 279 s: 26.2%;
- cobertura reducida: no;
- budgets relajados: no.

Artefactos funcionales:

- Lighthouse `9170023458`, `sha256:1184af3788a4cf82a017c59e301bdc30f72bfa0291efd27fb6fd17387168457c`;
- CI `9170051799`, `sha256:d4bcc4135c9e3f5047f00d6e29e398fb30434a62711bfe779cc7cda65ae76365`;
- release-health `9170052414`, `sha256:c947f7b9c4b98b03bc63059d317c6c35f9da8b3dfa43fe0a28156ebab3d42dce`;
- Pages `9169986924`, `sha256:247be73a2e8077eef40f4080f900bab98b0ba528f28a8473221d85a6c7eef3c8`.

## Recertificación pública de cierre `ready`

Run `31673266141`, SHA público final `dcb5bc9643eff595c0f8614c7cf6acbadc3bb719`:

- Validate current site: PASS;
- builder/segunda pasada e idempotencia: PASS;
- Pages: PASS;
- smoke público: PASS;
- Browser E2E/axe: PASS;
- Lighthouse: PASS;
- release-health: PASS;
- `stable` promovida: PASS;
- tiempo hasta gate `stable`: 204 s;
- mejora frente al baseline: 26.9%;
- cobertura reducida: no;
- budgets relajados: no.

Artefactos de recertificación:

- Lighthouse `9170555585`, `sha256:caa45c6b95f374fcbafd1ccdc2f4d900047747e045575bbcdc23394ca788c72b`;
- CI `9170580133`, `sha256:d4a2f062fb94acd5534774bce0b9c0f92b5bc77e249535934a21f141331a6bdf`;
- release-health `9170580558`, `sha256:6ede271d091608c1094b091593f51c27c76885d12a029fddd09c781729921e3a`;
- Pages `9170509163`, `sha256:80f860e54f8c55715ca18e9dcf8d633ca3bf5324d25a661a8c4169eb97f548bf`.

## Trazabilidad v5.22

- PR #84: arquitectura editorial de oferta;
- PR #85: compatibilidad del validator growth;
- PR #86: capability truth desde catálogo fuente;
- PR #87: smoke público version-aware;
- PR #88: preservación del prerender static-first en runtime;
- PR #89: contraste AA de ficha profunda;
- PR #90: cierre formal, release note, README y canal `ready`.

La documentación extensa vive en `RELEASE-v5.22.md`.

## Invariantes vigentes

- static-first;
- 46 páginas HTML;
- 16 fichas profundas;
- 1 formulario físico canónico;
- 49 pruebas E2E observadas como piso certificado v5.22;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- telemetría sin PII;
- analítica externa apagada (`provider:none`);
- WhatsApp manual;
- portal real de clientes explícitamente deshabilitado;
- sin CRM/backend, almacenamiento servidor, autenticación real, firma, pagos, agenda o portal documental ficticios;
- sin claims de clientes, premios, experiencia o resultados no verificables;
- contenido contractual corregido en fuente, no mediante mutación oculta post-render;
- `stable` solo después de gates verdes para cambios funcionales/publicables.

## Graphify / procedencia

La rama `knowledge/graphify-live` es memoria derivada. La comprobación correcta de frescura es leer `graphify-out/BUILD_META.json` y verificar que `source_commit` coincida con el `main` documental realmente procesado por el último run exitoso.

## Estado del ciclo

**v5.22 está cerrada. No existe una v5.23 activa.**

Un ciclo posterior debe empezar con una auditoría independiente, definir problema observable, objetivo, contrato, no-objetivos y criterios de cierre antes de crear una nueva versión funcional.
