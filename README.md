# Meridiano Legal · Web canónica v7.3.0

Sitio público static-first de Meridiano Legal: `https://arendon7.github.io/MERDIANOLEGAL/`.

## Estado certificado

**v7.3.0 — Legal Intelligence Demo** sobre la arquitectura de Meridiano Legal Intelligence.

La release convierte el Centro Demo en una demostración comercial concreta, verificable y capability-safe de cinco escenarios jurídico-operativos, sin presentar capacidades futuras como software productivo ni modificar la verdad jurídica de los catálogos.

### Evidencia de release

- Baseline certificado anterior v7.2.0: `f7bbf06588518141490a62db7b9fae8530659991`.
- SHA funcional v7.3: `dc3d4beea5637fc6aa104964d0fd0849b8c904c7` — 10/10 gates verdes.
- Merge funcional #177: `4867f3418c45a5a6689cd43b79ff48f191cda3a1`.
- Candidate formal 7.3.0: `e8656a0ea69aa8cf8140a6d41e74130e3cec9f60` — 10/10 gates verdes.
- Merge candidate #178: `6c194effd5421326f05296c1e99c54f852f04398`.
- Builder/snapshot productivo candidate: `2999d28dc6e4ae497ecbfbb9469f55364f34d899`.
- Pages quality → deploy → live smoke → Browser/axe + Lighthouse → snapshot: PASS.
- `stable` fue promovido automáticamente a `2999d28dc6e4ae497ecbfbb9469f55364f34d899`; no se movió manualmente.
- Canal de cierre: `github-pages-production-legal-intelligence-demo-certified`.

## Qué añade Legal Intelligence Demo

El Centro Demo conserva sus cinco experiencias históricas y añade una sexta pestaña **Legal Intelligence** con cinco escenarios completamente ficticios:

1. Legal AI Transformation.
2. Contract Control.
3. AI Governance 360.
4. Regulatory Control.
5. Meridiano Legal Desk.

Cada escenario presenta una secuencia comercial consistente:

**problema → flujo → artefacto demostrativo → resultado → referencia de alcance → frontera → oferta relacionada**.

Las referencias cuantitativas se recuperan de los catálogos canónicos aplicables. Legal Desk no muestra LU, volumen, canales, SLA ni capacidad incluida porque esos elementos requieren una propuesta específica.

## Capability truth

- cada escenario está marcado como DEMO;
- todos los nombres, situaciones y resultados son ficticios;
- no se cargan documentos o información real;
- la demostración no constituye asesoría jurídica;
- Contract Control y Regulatory Control no se presentan como SaaS autónomos;
- AI Governance 360 no sustituye auditoría técnica, seguridad o evaluación científica;
- Legal Desk es capacidad jurídica gestionada bajo perímetro y condiciones pactadas;
- Meridiano Counsel permanece fuera de la oferta pública;
- portal real, auth, CRM, pagos, firma, agenda y upload siguen fuera de capability productiva;
- no existe monitoreo automático universal ni decisión jurídica autónoma;
- no se publicaron precios nuevos.

## Arquitectura preservada

Meridiano Legal permanece como marca madre y **Meridiano Legal Intelligence** como capa transversal:

- Legal AI Diagnostic;
- Legal AI Transformation;
- Meridiano Legal Desk;
- Contract Control;
- Regulatory Control;
- AI Governance 360;
- Legal Engineering Studio.

v7.3 preserva además:

- v7.2 Buying Clarity;
- v7.1 Commercial Clarity;
- v7.0 Legal Intelligence;
- v6.4 Fit & Scope Clarity;
- v6.3 Engagement Clarity;
- v6.2 Search Discovery;
- v6.1 Measurement privacy-first;
- v6.0 Experience System.

## Release engineering v7.3

- `assets/data/v7/legal-intelligence-demo-v73.json`: contrato source-driven y phase-aware.
- `assets/css/v7/legal-intelligence-demo-v73.css`: estilos aislados del panel.
- `scripts/apply_legal_intelligence_demo_v73.py`: materialización determinista y lifecycle-aware.
- `scripts/validate_legal_intelligence_demo_v73.py`: source truth, capability boundaries y lifecycle fail-closed.
- `scripts/normalize_experience_compat_v60.py`: recomposición canónica después de reconstrucciones v6.
- `tests/e2e/legal-intelligence-demo-v73.spec.mjs`: regresión del panel y sus cinco escenarios.
- `.github/workflows/v73-legal-intelligence-demo-candidate.yml`: gate dedicado.

Durante la release se corrigieron sin relajar gates: un falso positivo de capacidad de Legal Desk, la idempotencia de markers administrados y la transición de lifecycle del materializador prototype → candidate → certified.

## Source of truth

- `main`: verdad técnica/documental vigente.
- `stable`: snapshot certificado.
- `catalog-products-v41/` y `catalog-services-v42/`: verdad jurídica/comercial.
- `assets/data/v7/`: contratos de las capas v7.
- `knowledge/00_CANON/`: memoria operativa actual.

## Siguiente frente

Con v7.3 cerrada, el siguiente trabajo debe partir de evidencia comercial real: usar el recorrido y las fichas comprables para validar interés, consultas y rutas de contratación antes de introducir nuevas capabilities o ampliar la plataforma.

Ver `RELEASE-v7.3.md` para evidencia, límites y arquitectura de la release.
