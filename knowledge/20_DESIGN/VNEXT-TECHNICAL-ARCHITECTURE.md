# Arquitectura técnica vNext — candidato Meridiano Legal v6

Fecha: 2026-08-17
Estado: diseño técnico previo a release. **No abre todavía v6.0.**
Baseline documental/técnico: `main@5fdca20b3837eab9ea2b2341b3d239660f48562f`.
Baseline funcional certificado: v5.31.0.

## 1. Problema técnico a resolver

La arquitectura pública es correcta, está certificada y es idempotente, pero la presentación se obtiene aplicando sucesivamente generaciones históricas de shell, visual, UX, CRO, proof, commercial, offer y compresión. El resultado funciona; el costo es sedimentación de CSS, selectores y bloques que deben conocerse para hacer cualquier cambio transversal.

El objetivo vNext no es añadir una nueva capa final. Es convertir el sistema visual en una **gramática semántica canónica** y hacer que los generadores produzcan esa gramática directamente.

## 2. Invariantes no negociables

vNext debe preservar:

1. sitio público static-first;
2. 46 HTML públicos;
3. 16 fichas profundas;
4. 6 rutas de necesidad + índice;
5. un único formulario físico;
6. WhatsApp manual;
7. ausencia de portal real, autenticación, pagos, firma, upload o CRM ficticios;
8. funnel sin PII ni persistencia;
9. no inferir conversión comercial;
10. profundidad jurídica completa en DOM;
11. divulgación progresiva nativa y accesible para profundidad secundaria;
12. exactamente **30 pasos** del builder;
13. idempotencia;
14. Release Governance, Graphify, Pages, smoke, Playwright, axe y Lighthouse sin relajación;
15. `stable` solo después de certificación completa.

## 3. Qué significa conservar los 30 pasos

El builder actual tiene 30 pasos de job desde `Set up job`/checkout/generación hasta `Commit canonical outputs`. La cifra no debe crecer por incorporar vNext.

Regla de arquitectura:

- **No crear un paso 31.**
- La lógica vNext debe integrarse sustituyendo o absorbiendo lógica en pasos existentes.
- Los materializadores históricos de presentación deben quedar version-gated para no reinsertar markup/CSS legado cuando `version >= 6.0.0`.
- Las fuentes jurídicas/comerciales que sigan siendo autoridad pueden conservarse aunque cambie su materializador.

## 4. Separación de capas propuesta

### 4.1 Truth layer — permanece

Autoridad sobre contenido y contratos:
- catálogos fuente de productos/servicios;
- `offer-narrative-v522.json`;
- `offer-commercial-v530.json`;
- contratos de funnel/handoff/capability truth;
- profesional authority;
- sectores, perspectivas, soluciones y demás fuentes aprobadas.

No deben convertirse en CSS ni en componentes; son datos/verdad.

### 4.2 Experience model — nuevo contrato canónico

Crear una fuente semántica v6 que describa **qué representa cada bloque**, no cómo se ve.

Familias:
- `decision_statement`;
- `situation_index`;
- `outcome_ledger`;
- `deliverable_ledger`;
- `process_timeline`;
- `perimeter_matrix`;
- `responsibility_note`;
- `boundary_band`;
- `evidence_block`;
- `commercial_matrix`;
- `deep_disclosure`;
- `contextual_cta`;
- `contact_handoff`.

La misma familia semántica puede renderizar distinto según `home`, `product`, `service`, `solution`, `sector`, `perspective` o `legal`.

### 4.3 Renderer — salida HTML

Un renderizador v6 debe producir el markup final desde truth + experience model. El objetivo es reducir transformaciones regex acumulativas sobre HTML ya materializado.

Prioridad:
1. render directo desde datos cuando existe fuente estructurada;
2. transformaciones DOM/HTML acotadas cuando la migración todavía lo requiera;
3. regex solo para compatibilidad temporal, con marcadores únicos y validators.

### 4.4 Design system — salida CSS consolidada

Objetivo final: una familia pequeña de hojas con responsabilidades estables, por ejemplo:

- `assets/css/tokens.css`
- `assets/css/base.css`
- `assets/css/layout.css`
- `assets/css/components.css`
- `assets/css/surfaces.css`
- `assets/css/print.css`

Los nombres son propuesta, no contrato definitivo.

No mantener como estrategia permanente una cadena de `visual-v39.css` + `detail-v46.css` + `decision-v58.css` + `proof-v512.css` + `offer-v522.css` + `offer-commercial-v530.css` + `decision-compression-v531.css` sobre cada ficha.

## 5. Tokens

### Preservar inicialmente
- navy `#13263a`;
- navy deep `#091725`;
- blue `#2c5878`;
- ivory `#f5f1e8`;
- gold `#a88454`;
- gold light `#d9bc8b`;
- sans stack actual;
- serif production baseline actual hasta decisión tipográfica expresa.

### Normalizar
- spacing scale;
- content widths;
- typography scale;
- line-height;
- border colors;
- focus ring;
- radius tiers;
- shadow tiers;
- motion duration/easing;
- z-index layers.

No aprobar Source Serif 4 por el hecho de haberse usado como proxy en Figma.

## 6. Componentes semánticos v6

### Shell
`SiteHeader`, `PrimaryNav`, `Breadcrumb`, `PageContext`, `SiteFooter`.

### Editorial
`Eyebrow`, `DecisionStatement`, `EditorialIntro`, `IndexedList`, `SectionRule`.

### Trabajo jurídico
`OutcomeLedger`, `DeliverableLedger`, `ProcessTimeline`, `PerimeterMatrix`, `ResponsibilityNote`, `BoundaryBand`, `EvidenceBlock`.

### Comercial
`CommercialMatrix`, `ScopeDriversDisclosure`, `ContextualCTA`.

### Profundidad
`DeepDisclosure` con `<details>/<summary>` nativo.

### Contacto
`ContactIntro`, `CanonicalContactForm`, `WhatsAppHandoff`.

Una función semántica no debe reutilizar un componente visual solo porque ambos “caben en una card”.

## 7. Estrategia de compatibilidad con materializadores históricos

### Fase de transición

Cada script histórico que modifica presentación debe incorporar una de estas políticas para `version >= 6.0.0`:

A. **no-op explícito** cuando su resultado ya lo produce v6;
B. conservar solo la parte de truth/metadata que siga siendo necesaria;
C. delegar en un renderer v6 compartido.

No borrar de inmediato scripts históricos: sirven para reproducir/releases antiguas y documentan decisiones previas.

### Posición del renderer v6

No añadir un paso nuevo. Reutilizar un paso existente de presentación como punto de entrada v6 —candidato: `Apply canonical visual system`— y hacer que los pasos visuales posteriores sean no-op/delegación bajo semver v6, mientras sus validadores comprueban la nueva verdad equivalente.

Alternativa válida: usar uno de los pasos tardíos existentes como `finalize` v6, siempre que no permita que capas antiguas reescriban después el markup final.

La selección definitiva debe probarse con dos pasadas idempotentes antes de abrir release.

## 8. Generación de las 16 fichas

El generador base ya declara las 16 páginas y distingue 8 servicios/8 productos. v6 debe conservar esa autoridad de catálogo, pero la plantilla debe evolucionar a shell semántico común.

Producto y servicio **no deben ser el mismo layout con distinto título**:

- Producto cerrado prioriza `resultado → entregables → perímetro → proceso → cierre`.
- Servicio adaptable prioriza `decisión/pregunta → resultado → capas/intervención → perímetro → gobierno/cierre`.

Ambos comparten accesibilidad, tokens y componentes primitivos.

## 9. Home

La Home v6 se materializa desde el modelo client-first:

1. hero/decision statement;
2. seis situaciones;
3. cuatro resultados;
4. método;
5. evidencia/autoridad;
6. familias de oferta;
7. sectores/perspectivas/firma como profundidad;
8. contacto.

Servicios, productos, planes y modalidades siguen siendo accesibles/SEO, pero no gobiernan la primera lectura.

## 10. Solutions, sectors y perspectives

### Solutions
Mantener 6 rutas + índice. Adoptar gramática `situación → señales → decisión → resultado → modalidad → límites → CTA → profundidad`.

### Sectors
No convertirlos en catálogos comerciales. Usar lectura sectorial: contexto → decisiones recurrentes → riesgos/actores → oferta relacionada → perspectiva.

### Perspectives
Tratar como biblioteca editorial con metadata, lectura y relacionados; no reutilizar cards comerciales como identidad principal.

## 11. Contacto

La implementación v6 debe preservar físicamente **un solo formulario**.

Puede cambiar:
- orden visual;
- copy;
- agrupación;
- disclosure de proceso/condiciones;
- CTA contextual que precarga parámetros permitidos.

No puede añadir:
- segundo formulario;
- upload;
- persistencia;
- envío automático que finja delivery/aceptación;
- campos que conviertan el funnel en CRM oculto.

## 12. Navegación

Objetivo provisional de primer nivel:
- Cómo podemos ayudar / Necesidades (resolver redundancia de naming);
- Soluciones u Oferta, según test de arquitectura;
- Sectores;
- Perspectivas;
- Firma;
- CTA: Presentar necesidad.

`Centro demo` deja de competir como CTA de header; se reencuadra como evidencia/metodología secundaria: `Cómo trabajamos` o equivalente.

## 13. Motion

Solo después de HTML/CSS semánticos estables.

Aplicar lente Emil Design Engineering a:
- hover/focus;
- disclosure;
- TOC/current section;
- feedback de CTA;
- cambios de estado del handoff;
- progresión visual del método si aporta causalidad.

Contrato:
- transform/opacity preferentemente;
- 120–220 ms para microfeedback;
- reduced motion obligatorio;
- sin scroll-jacking/parallax pesado/texto por letra.

## 14. Plan de validación

### Structural
- 46 HTML;
- 16 fichas;
- 6 rutas + índice;
- 1 formulario;
- no markup duplicado;
- no CSS histórico cargado accidentalmente en superficies migradas;
- idempotencia dos pasadas.

### Content truth
- cantidades, horizontes, límites, entregables y cierres iguales a fuente;
- no pérdida de profundidad;
- no claims nuevos no soportados.

### Browser
- desktop Chromium/WebKit;
- mobile Chromium/WebKit según matriz vigente;
- keyboard/focus;
- details/summary;
- CTA/context handoff;
- navegación;
- no overflow.

### Accessibility
- axe serious/critical 0 en superficies cubiertas;
- headings/landmarks coherentes;
- labels y errores de formulario;
- contraste;
- reduced motion.

### Performance
- no empeorar budgets Lighthouse existentes;
- medir reducción de requests/CSS bytes y style recalculation cuando sea posible;
- no introducir fuentes externas sin presupuesto aprobado.

## 15. Acceptance bar técnico antes de abrir v6.0

Debe existir y ser revisable:

1. inventario de hojas/scripts de presentación actuales;
2. matriz de migración de 46 superficies;
3. mapping truth → experience component;
4. estrategia concreta de integración en los 30 pasos;
5. baseline browser/Lighthouse actual;
6. prototipo Home + producto + servicio + mobile aprobado;
7. non-goals de release;
8. rollback claro a `stable`.

Cumplidos esos puntos, puede abrirse formalmente el ciclo v6.0 con baseline y contrato verificable.