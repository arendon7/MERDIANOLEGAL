# ADR-007 — Arquitectura comercial Legal Intelligence v7

Fecha: 2026-08-18
Estado: propuesto para prototipo; no modifica todavía la release pública certificada.

## Contexto

Meridiano Legal ya dispone de una arquitectura pública sólida: rutas por situación, 8 productos cerrados y 8 servicios profesionales con verdad canónica, profundidad jurídica, requisitos, responsabilidades, límites y validación source-driven. La nueva necesidad de negocio no es añadir más tarjetas ni crear marcas aisladas, sino hacer visible una capacidad emergente: combinar criterio jurídico, Legal Operations, inteligencia artificial, automatización y desarrollo de soluciones para diagnosticar, transformar y operar trabajo jurídico.

El riesgo de añadir `Contract Control`, `Regulatory Control`, `Legal Desk`, `AI Governance`, `Legal Engineering` y `Meridiano Counsel` como productos independientes es duplicar alcance existente, fragmentar navegación y publicar capacidades tecnológicas que todavía no están productivamente habilitadas.

## Decisión

Adoptar **Meridiano Legal Intelligence** como una **arquitectura de soluciones integrada bajo la marca Meridiano Legal**, no como sociedad, marca o catálogo independiente.

### 1. La marca madre no cambia

`Meridiano Legal` conserva la relación comercial, la autoridad jurídica y la navegación principal.

`Meridiano Legal Intelligence` funciona como descriptor de una familia de capacidades de transformación, operación y Legal Engineering.

### 2. Los 16 catálogos actuales permanecen como verdad jurídica/comercial

No se duplican ni sustituyen `catalog-products-v41/*.json` ni `catalog-services-v42/*.json`.

La nueva capa v7 referencia esas fuentes y explica cómo se combinan en recorridos de negocio.

### 3. Escalera comercial autorizada

La experiencia debe poder explicar, cuando aplique:

1. **Diagnosticar** — comprender problema, demanda, riesgo y oportunidad.
2. **Transformar** — rediseñar e implementar procesos, reglas y pilotos.
3. **Operar** — prestar capacidad jurídica gestionada bajo alcance, SLA y gobierno acordados.
4. **Controlar** — estructurar información, obligaciones, riesgos y seguimiento mediante procesos y herramientas habilitadas.
5. **Construir** — desarrollar Legal Engineering específico cuando la necesidad no encaja en una solución estándar.

La tecnología es un habilitador; no se presenta como capability productiva autónoma si no existe evidencia técnica real.

### 4. Arquitectura de soluciones

- **Legal AI Diagnostic** — punto de entrada para analizar operación jurídica, demanda, procesos, conocimiento y oportunidades de IA/automatización.
- **Legal AI Transformation** — intervención de Legal Operations + tecnología para dejar procesos rediseñados y pilotos operables.
- **Meridiano Legal Desk** — servicio jurídico gestionado que combina intake, triage, playbooks, profesionales, QA, seguimiento y métricas dentro del alcance contratado.
- **Contract Control** — evolución operativa del Sistema Contractual Empresarial: contratos, riesgos, obligaciones, fechas, responsables y evidencia. No se declara SaaS autónomo mientras no exista producto habilitado.
- **Regulatory Control** — evolución operativa de Proyectos Regulados: cambios, aplicabilidad, obligaciones, responsables, plazos y evidencia. No se declara monitoreo automático productivo sin implementación real.
- **AI Governance 360** — escalera Readiness → implementación → gobierno recurrente, sustentada en P05 y S06.
- **Legal Engineering Studio** — construcción a medida de workflows, automatizaciones, agentes o herramientas, siempre mediante alcance técnico y jurídico expreso.
- **Meridiano Counsel** — concepto de interfaz inteligente transversal. Se mantiene como capacidad futura/no pública hasta contar con implementación verificable, permisos, fuentes y trazabilidad productiva.

### 5. Capability truth

Mientras la release pública siga declarando portal, auth, CRM, upload, firma, agenda y otras capacidades como no implementadas:

- Legal Desk no promete un portal productivo.
- Contract Control no promete una plataforma SaaS disponible de autoservicio.
- Regulatory Control no promete vigilancia automática si el servicio se ejecuta mediante revisión humana o herramientas internas.
- Meridiano Counsel no se comercializa como producto disponible.
- Dashboards, integraciones, agentes o automatizaciones solo se publican cuando el alcance real o la implementación los soporten.

### 6. Navegación

La entrada principal sigue siendo **situación/decisión del cliente**, conforme al Experience System v6.

La capa Legal Intelligence debe aparecer como una ruta de comprensión transversal y conectar con las ofertas actuales, no reemplazar las seis rutas existentes por una taxonomía tecnológica.

### 7. Estrategia de URLs

Se preservan las URLs actuales de productos, servicios, sectores, perspectivas y soluciones.

Cualquier nueva landing se añade de forma aditiva únicamente después de validar el prototipo y actualizar sitemap, discovery, validators y E2E correspondientes.

### 8. Prototipado antes de propagación

La primera iteración v7 debe limitarse a:

- arquitectura y copy canónico de la familia;
- prototipo de hub/landing;
- prototipo de capa comercial en una ficha contractual y una ficha de Legal Operations/IA;
- revisión desktop, mobile, teclado y reduced motion;
- validación de capability truth;
- crítica independiente antes de propagar.

No se modifica masivamente 46/46 superficies en la primera iteración.

## Fuentes canónicas relacionadas

- `catalog-products-v41/p05-ia.json`
- `catalog-products-v41/p06-regulado.json`
- `catalog-products-v41/p07-contractual.json`
- `catalog-services-v42/s01-diagnostico.json`
- `catalog-services-v42/s02-direccion.json`
- `catalog-services-v42/s03-contratos.json`
- `catalog-services-v42/s06-tecnologia-ia.json`
- `catalog-services-v42/s07-regulados.json`
- `catalog-services-v42/s08-legal-ops.json`
- `growth-solutions-v51.json`
- `experience-content-v60.json`

## Consecuencias positivas

- evita duplicación de productos;
- mantiene una sola marca comercial;
- hace comprensible la progresión diagnóstico → implementación → operación;
- permite vender servicios antes de prometer un SaaS;
- convierte LegalAIZ/Binario u otras capacidades internas en infraestructura, no en claims públicos no certificados;
- conserva la fortaleza jurídica y el Experience System actual.

## Riesgos

- confundir una capacidad de servicio con software disponible;
- crear una segunda taxonomía que compita con las rutas por situación;
- sobrecargar el home;
- introducir copy comercial que accidentalmente cree obligaciones nuevas.

Mitigación: fuente v7 separada, referencias explícitas a catálogos canónicos, validator dedicado, prototipo reducido y capability truth fail-closed.

## Criterio para aceptar este ADR

Se acepta únicamente cuando una iteración v7 materializada demuestre que:

1. la familia Legal Intelligence se entiende sin conocer terminología LegalTech;
2. no duplica las 16 ofertas existentes;
3. no publica capabilities tecnológicas inexistentes;
4. mejora la ruta de decisión en desktop y mobile;
5. conserva accesibilidad, performance, funnel, privacidad y un solo formulario físico;
6. supera los gates existentes más los controles v7 que correspondan.
