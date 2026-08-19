# Meridiano Legal — Tarea activa

Actualizado: 2026-08-18.

## Baseline pública preservada

- Release certificada de partida: **v6.4.0 — Fit & Scope Clarity / encaje y cambio de alcance**.
- `main` y `stable` estaban alineados en `704d61b9f56e58b4ac135fd66aeee89033e22f24` al abrir este ciclo.
- La funcionalidad v6.4 permanece vigente: 16/16 fichas con `situations` y `supplements` materializados desde truth canónico.
- 46 HTML, 16 fichas profundas, un único formulario físico y 30 pasos históricos permanecen como baseline.
- Search Console continúa sin configurar y analytics externa continúa deshabilitada.
- Portal, auth, CRM, pagos, firma, agenda y upload continúan fuera de capability productiva.

## Ciclo funcional activo

**v7.0.0 — Meridiano Legal Intelligence / release candidate.**

Rama:

`feat/v700-legal-intelligence-release`

PR:

`#167`

Canal candidate:

`github-pages-legal-intelligence-candidate`

Motivo de negocio:

Hacer visible y comprensible una capacidad que ya estaba distribuida entre Diagnóstico, Dirección Jurídica Externa, Contratación, Tecnología/IA, Proyectos Regulados y Legal Operations: diagnosticar, transformar, controlar y operar trabajo jurídico combinando criterio legal, procesos, IA, automatización y Legal Engineering.

El objetivo no es crear un catálogo paralelo. Es organizar una capa transversal que conecte problemas empresariales con las 16 ofertas canónicas existentes.

## Reconciliación con v6.4

El prototipo original #163 nació sobre v6.3 y dejó de ser un vehículo seguro de release cuando `main` avanzó a v6.4.

Por eso v7 fue reconciliado de nuevo desde `main` v6.4:

- rama nueva creada desde la baseline certificada;
- solo se portó source v7: contratos, materializadores, validators, documentación técnica, normalizador y E2E;
- v7 se rematerializó sobre el HTML v6.4 existente;
- el boundary permitió cambios únicamente en las 11 superficies previstas;
- Fit & Scope v6.4 se validó después de aplicar v7;
- Graphify temporal fue restaurado y no forma parte del diff final.

SHA limpio de reconciliación antes de abrir el candidate:

`67b097c4e6cb1adf9d252aafb7e6a524b7e0636e`

Ese SHA superó 9/9 workflows aplicables:

1. Candidate Validation.
2. Canonical Builder Equivalence.
3. Fit & Scope v6.4.
4. Engagement Clarity v6.3.
5. Search Discovery v6.2.
6. Release Governance.
7. Graphify.
8. Browser E2E / axe.
9. Measurement / Browser E2E.

## Arquitectura v7

Meridiano Legal permanece como marca madre. **Meridiano Legal Intelligence** es una capa transversal, no una unidad comercial paralela.

Arquitectura:

1. Legal AI Diagnostic.
2. Legal AI Transformation.
3. Meridiano Legal Desk.
4. Contract Control.
5. Regulatory Control.
6. AI Governance 360.
7. Legal Engineering Studio.
8. Meridiano Counsel como concepto futuro/no producto público.

La entrada pública continúa siendo la situación o decisión del cliente y las seis rutas v6.

## Superficies v7

Se materializan 11 superficies existentes, sin nuevas URLs:

- `index.html`;
- `soluciones/index.html`;
- `soluciones/ordenar-operacion-juridica.html`;
- `servicios/legal-operations.html`;
- `productos/sistema-contractual-empresarial.html`;
- `soluciones/gobernar-inteligencia-artificial-empresa.html`;
- `productos/programa-gobernanza-ia.html`;
- `servicios/tecnologia-inteligencia-artificial.html`;
- `soluciones/estructurar-proyecto-regulado.html`;
- `productos/proyecto-regulado-estructurado.html`;
- `servicios/proyectos-regulados.html`.

## Reglas de capability

- no publicar portal, auth, upload, CRM, firma, pagos o SaaS inexistente;
- Contract Control y Regulatory Control siguen siendo patrones de implementación/operación, no productos SaaS autónomos;
- Meridiano Counsel sigue fuera de la oferta pública;
- automatizaciones, agentes, integraciones y herramientas solo forman parte de un encargo si se incluyen expresamente en su alcance;
- no prometer monitoreo regulatorio universal, certificaciones técnicas ni decisiones favorables de autoridades;
- no alterar precios, tiempos, responsabilidades o entregables de los 8 productos y 8 servicios canónicos mediante la capa v7.

## Release candidate

`version.json` declara ahora **7.0.0** en canal candidate.

El contrato arquitectónico v7 es phase-aware y permite `prototype → release-candidate → certified` sin modificar los límites de capability.

Antes de merge, el **SHA final del candidate** debe volver a superar los 9 workflows aplicables. No se reutiliza la certificación del SHA de reconciliación después de cambiar metadata.

## Promoción a producción

Solo después de candidate same-SHA verde:

1. fusionar PR #167 a `main`;
2. dejar que Builder materialice el sitio canónico;
3. exigir Pages quality;
4. desplegar GitHub Pages;
5. exigir live smoke;
6. exigir Browser/axe sobre producción;
7. exigir Lighthouse;
8. permitir que el workflow promueva `stable` automáticamente.

**No mover `stable` manualmente.**

## Cierre posterior

Una vez `main` y `stable` estén certificados en v7, abrir un cierre documental separado para:

- cambiar canal `candidate → github-pages-production-legal-intelligence-certified`;
- actualizar README y memoria canónica;
- publicar `RELEASE-v7.0.md`;
- registrar candidate, merge, builder, Pages y stable SHA;
- volver a pasar la cadena completa de certificación del cierre documental.

El PR #163 debe cerrarse sin merge una vez #167 haya sido promovido correctamente, dejando constancia de que fue sustituido por la reconciliación sobre v6.4.
