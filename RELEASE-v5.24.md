# Meridiano Legal v5.24.0 — Orquestación canónica verificable

Fecha de cierre funcional: 2026-08-13.

## Propósito

v5.24 reduce riesgo técnico de mantenimiento en la composición pública de Meridiano Legal sin abrir una nueva capa visual, comercial o de producto.

La auditoría posterior a v5.23 mostró que el problema de mayor impacto ya no estaba en la profundidad de las 16 ofertas, en la arquitectura superior de decisión ni en el contacto comercial. El riesgo más objetivo era la duplicación del orden de composición canónica entre:

1. el builder público;
2. la segunda pasada de Pages usada para comprobar idempotencia;
3. el encadenamiento de extensiones posteriores dentro de la capa v5.18+.

Esa duplicación había expuesto incompatibilidades reales durante releases anteriores. v5.24 convierte el orden esperado en un contrato explícito y verificable: si builder y segunda pasada dejan de ejecutar los mismos pasos, en el mismo orden, el pipeline falla antes de promover `stable`.

## Resultado funcional

v5.24 incorpora `scripts/canonical_pipeline_v524.py` como manifiesto declarativo del orden canónico.

El manifiesto define exactamente 30 pasos únicos:

1. generación de shells de catálogo;
2. prerender estático de productos;
3. prerender estático de servicios;
4. enriquecimiento editorial;
5. capa comercial v4.4;
6. sistema visual canónico;
7. UX de portada v4.5;
8. UX profunda v4.6;
9. UX editorial v4.7;
10. normalización editorial v4.7;
11. compatibilidad de crecimiento v5.1;
12. calidad v4.8;
13. normalización de calidad v4.8;
14. operación pública v4.9;
15. sincronización de versión pública;
16. configuración de producción v5.0;
17. crecimiento v5.1;
18. finalización de crecimiento v5.1;
19. CRO/SEO v5.2;
20. autoridad/descubrimiento v5.3;
21. arquitectura de decisión v5.8;
22. intake comercial v5.9;
23. conversión a cierre v5.10;
24. readiness de engagement v5.11;
25. prueba verificable v5.12;
26. continuidad del brief v5.13;
27. recomendación explicable v5.14;
28. decisión a acción v5.15+;
29. handoff manual v5.17;
30. observabilidad y extensiones canónicas v5.18+.

El contrato compara esa secuencia con las dos rutas reales existentes en `.github/workflows/build-canonical.yml` y `.github/workflows/pages.yml`. No basta con que existan los scripts: deben coincidir los 30 comandos y su orden.

`apply_handoff_observability_v518.py`, que ya atraviesan builder, segunda pasada y Release Governance, activa esta validación desde v5.24. Así el guard forma parte de las rutas de certificación existentes sin modificar permisos, triggers ni estructura de GitHub Actions.

## Contratos preservados

v5.24 conserva íntegramente los contratos funcionales previos:

- sitio static-first;
- 46 HTML;
- 16 fichas profundas;
- un formulario físico canónico;
- arquitectura comercial v5.20;
- frontera demo/capacidad v5.21;
- narrativa diferenciada v5.22;
- compresión del contacto v5.23;
- WhatsApp como handoff manual;
- telemetría first-party/local sin PII;
- portal real deshabilitado;
- analítica externa apagada;
- validators históricos;
- Browser E2E/axe;
- budgets Lighthouse v5.5;
- promoción de `stable` solo detrás de gates verdes.

Los scripts históricos no se fusionaron ni eliminaron. La release tampoco convierte el manifiesto en un mecanismo para saltarse los workflows: builder y Pages permanecen explícitos y verificables.

## No objetivos cumplidos

v5.24 no:

- rediseña la web;
- cambia copy, planes, precios, productos, servicios o firma;
- altera el formulario comercial;
- añade PII;
- crea backend, CRM, cuentas, portal real, storage, email, firma, pagos, agenda o carga documental;
- introduce scoring o inferencia de intención;
- modifica permisos o triggers de GitHub Actions;
- elimina masivamente scripts históricos;
- reduce cobertura;
- relaja budgets;
- reescribe retrospectivamente v5.23.

El único cambio visible esperado frente a v5.23 es la metadata/versionado correspondiente a v5.24.0.

## Arquitectura técnica

### Manifiesto verificable

`scripts/canonical_pipeline_v524.py`:

- exige `version >= 5.24.0`;
- declara 30 claves únicas;
- comprueba que cada target exista;
- normaliza comandos Python y Node;
- extrae la secuencia efectiva del builder;
- extrae la secuencia efectiva de la segunda pasada de Pages;
- exige `builder == Pages == manifiesto`;
- falla determinísticamente ante cualquier divergencia;
- ofrece modos `validate`, `list` y `apply` para inspección y ejecución controlada.

### Punto de integración

`apply_handoff_observability_v518.py` invoca el guard desde v5.24 antes de continuar la composición de extensiones posteriores. Esto permite que el contrato se ejecute en las rutas que ya estaban protegidas por el proyecto, sin duplicar otro pipeline paralelo.

### Canal público certificado

El `channel` funcional certificado de v5.24 es:

`github-pages-production-canonical-orchestration-candidate`

`sync_public_version.py` interpreta `production` como superficie pública y materializa correctamente `Web pública v5.24.0` en la portada. Esta metadata no debe modificarse durante el cierre documental porque `version.json` es entrada funcional vigilada por builder/Pages.

## Incidencias resueltas sin debilitar gates

### 1. Parser inicial de comandos YAML

El primer guard de v5.24 detectó una divergencia durante Release Governance. La causa no era drift real: el extractor inicial solo recogía comandos incluidos dentro de bloques YAML `run: |` y omitía comandos escritos como `run: python3 ...` en una sola línea.

Como resultado, veía únicamente seis de los treinta pasos del builder.

La corrección amplió el parser para reconocer y normalizar ambas formas, inline y multiline, sin cambiar ningún workflow ni rebajar el contrato. La siguiente corrida de Governance atravesó todas las capas históricas y confirmó los 30 pasos reales.

### 2. Metadata de canal sin condición pública

Tras el primer merge funcional, el builder produjo un candidato correcto y la segunda pasada/idempotencia pasó. Sin embargo, `validate_production_v50.py` bloqueó Pages porque `index.html` declaraba `Web demostrativa v5.24.0` en lugar de `Web pública v5.24.0`.

El validator funcionó correctamente. La causa fue que el channel inicial de v5.24 (`github-pages-canonical-orchestration-candidate`) no contenía `public` ni `production`, que son las condiciones explícitas usadas por `sync_public_version.py` para identificar una superficie pública.

PR #103 corrigió únicamente esa metadata a `github-pages-production-canonical-orchestration-candidate`. Governance volvió a pasar completa y la certificación pública se reinició desde cero. No se modificó el validator histórico para hacer pasar la candidata.

## Trazabilidad de implementación

- PR #102 — manifiesto de 30 pasos y guard de orden canónico;
- PR #103 — corrección de metadata del canal público;
- builder final: run `31739786763`;
- run público final: `31739813251`;
- SHA funcional final certificado: `73ba88fda16545cc3a257594b2a91d67a9c848b6`.

Al cierre funcional:

`main == stable == 73ba88fda16545cc3a257594b2a91d67a9c848b6`.

Después del cierre documental, `main` puede avanzar exclusivamente por documentación/memoria; `stable` debe conservar este SHA funcional.

## Evidencia final

### Builder, idempotencia y despliegue

Run final `31739813251`:

- builder canónico previo: PASS;
- manifiesto v5.24: PASS;
- builder == segunda pasada == manifiesto: PASS;
- segunda pasada/idempotencia: PASS;
- validadores históricos: PASS;
- Pages: PASS;
- smoke público: PASS;
- Browser E2E/axe: PASS;
- Lighthouse: PASS;
- release-health: PASS;
- promoción de `stable`: PASS.

El guard dejó evidencia explícita:

`CANONICAL PIPELINE V5.24 CONTRACT OK: builder y segunda pasada conservan el mismo orden.`

### Browser E2E + axe

Job `94580399251`:

- 58 pruebas observadas;
- 56 PASS;
- 2 SKIP;
- 0 FAIL;
- 0 RETRY;
- reporter wall time: 96 s;
- Chromium desktop;
- Chromium mobile;
- WebKit desktop;
- 7 superficies axe WCAG 2.1 AA sin violaciones serias/críticas.

La cobertura no disminuyó frente al piso certificado de v5.23.

### Lighthouse

Job `94580399229`: 6/6 superficies PASS, todas con performance 1.00 y accesibilidad 1.00.

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Home | 1.00 | 1.00 | 1421 ms | 0 | 42 ms | 107,413 B |
| Solution IA | 1.00 | 1.00 | 907 ms | 0 | 0 ms | 23,574 B |
| Product IA | 1.00 | 1.00 | 913 ms | 0 | 0 ms | 37,238 B |
| Sector tecnología | 1.00 | 1.00 | 1004 ms | 0 | 0 ms | 24,259 B |
| Perspective IA | 1.00 | 1.00 | 985 ms | 0 | 0 ms | 26,159 B |
| Demo | 1.00 | 1.00 | 905 ms | 0 | 0 ms | 21,981 B |

Budgets vigentes sin relajación: performance >= 0.70, accesibilidad >= 0.90, LCP <= 4000 ms, CLS <= 0.15, TBT <= 350 ms y transferencia <= 1.5 MB.

### CI

- tiempo hasta gate de `stable`: 196 s;
- baseline v5.5: 279 s;
- mejora frente al baseline: 29.7%;
- cobertura reducida: no;
- budgets relajados: no.

Duraciones principales:

- Validate current site: 13 s;
- Deploy Pages: 14 s;
- Verify Pages: 10 s;
- Browser E2E: 146 s;
- Lighthouse: 104 s.

### Artefactos del run `31739813251`

- Pages: `9196603570` — `sha256:5b5afff20a4fa0d0b87c9cf322c78ce949dd0735c6e817e17268703e2e2b8b6a`;
- Lighthouse: `9196671033` — `sha256:72bb492b9e5b2508005aa372fb28481bc57520d14b6b663513542f1387d31b21`;
- CI: `9196701543` — `sha256:329a461fc4ac92fcbb9e08399b84920a2ed1597a92e609354e86dfabd0dfae05`;
- release-health: `9196701995` — `sha256:9b8cf6410f03ed715d1854977c59956137d12b8d37c1e9f7ccaa6f7e5eb7be83`.

## Graphify al cierre funcional

Antes del cierre documental, Graphify 0.9.26 ya reconoce v5.24 y registra:

- 685 nodos;
- 1.147 relaciones;
- 96 wiki notes;
- 46 HTML;
- 8 productos fuente;
- 8 servicios fuente;
- 76 scripts Python;
- 25 fuentes JavaScript;
- 9 specs E2E.

Su `source_commit` previo al cierre documental corresponde al merge funcional anterior al commit automático del builder. El cierre formal exige una nueva corrida sobre el `main` documental definitivo para que `BUILD_META.source_commit` coincida exactamente con ese `main`.

## Capacidades externas

Activas y verificables:

- GitHub Pages;
- WhatsApp como handoff manual;
- contexto comercial client-side;
- telemetría first-party/local sin PII;
- sitemap, robots, canonical y Open Graph;
- demo estática/noindex;
- pipeline CI de certificación;
- guard verificable de orden canónico v5.24.

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

v5.24 convierte el orden de composición en un contrato auditable sin añadir otra capa pública ni borrar historia útil. El valor de la release está en impedir que dos rutas aparentemente equivalentes diverjan de forma silenciosa.

La release funcional queda certificada en `73ba88fda16545cc3a257594b2a91d67a9c848b6`. Cualquier ciclo posterior debe empezar con una auditoría independiente; no se abre una v5.25 por continuidad automática.
