# Meridiano Legal · Web canónica v5.2.0

Sitio público, responsive y autocontenido de Meridiano Legal, publicado mediante GitHub Pages. La v5.2 conserva íntegra la arquitectura jurídica, production-ready y static-first acumulada hasta v5.1 y añade un ciclo específico de **CRO, calificación comercial y SEO de intención** sobre las rutas de `soluciones/`.

## Estado de la release

La publicación mantiene **46 páginas HTML** y la arquitectura canónica existente:

- 8 servicios profesionales;
- 8 productos jurídicos de alcance cerrado;
- 5 planes recurrentes;
- 8 lecturas sectoriales;
- 6 perspectivas jurídicas;
- página institucional de Firma;
- Centro Demo;
- Meridiano Empresas con información ficticia y `noindex,nofollow`;
- 1 hub de soluciones y 6 rutas de decisión empresarial.

La URL pública canónica continúa siendo `https://arendon7.github.io/MERDIANOLEGAL/`. No se ha inventado un dominio, CRM, backend, analítica de terceros ni token de Search Console. WhatsApp continúa siendo el canal real de contacto y `telemetry-v50.js` permanece como instrumentación first-party en memoria, sin transmisión externa.

## v5.2 · Conversión sin simplificar el contenido jurídico

v5.1 permitió que el prospecto empezara por su problema empresarial. v5.2 trabaja el siguiente tramo del funnel: **entender si la ruta realmente encaja, resolver objeciones razonables y llegar al contacto con expectativas más precisas**.

Las seis páginas de solución conservan señales, decisiones, modalidades, entregables, límites y evidencia v5.1. Sobre esa base añaden:

1. **Criterio de encaje**: cuándo conviene explorar la ruta.
2. **No encaje**: cuándo el problema probablemente exige otra intervención o especialidad.
3. **Tres objeciones frecuentes** por necesidad, contestadas con razonamiento jurídico-comercial desarrollado.
4. **Criterio de alcance y honorarios**, enlazando la fuente pública canónica de precios en vez de duplicar valores.
5. **Tres preguntas frecuentes** por landing, para un total de 18 respuestas nuevas.
6. **`FAQPage` JSON-LD** independiente en cada una de las seis rutas.
7. **Dos rutas relacionadas** por página para mejorar continuidad e interlinking.
8. **CTA final específico** de la necesidad, en lugar del cierre genérico de v5.1.
9. Títulos y descripciones SEO orientados a intención de búsqueda empresarial.

El hub `soluciones/` conserva su arquitectura y añade una guía rápida para distinguir entre necesidad de priorizar riesgos, capacidad jurídica recurrente y decisiones de crecimiento/regulación.

## Las seis rutas optimizadas

### 1. Ordenar el riesgo jurídico empresarial

La página distingue entre percepción general de exposición y un asunto puntual. Responde objeciones como “ya tenemos abogado o contador”, explica por qué una auditoría debe tener perímetro cerrado y conecta diagnóstico, auditoría profunda y dirección jurídica externa.

### 2. Dirección jurídica externa

Explica cuándo deja de ser eficiente contratar asunto por asunto, cómo controlar una capacidad mensual y por qué una dirección externa puede complementar —no necesariamente reemplazar— un equipo jurídico interno.

### 3. Gobernanza jurídica de IA

Aclara que el riesgo puede existir antes de un “proyecto formal” de IA, diferencia gobernanza jurídica de ciberseguridad y evita presentar una política como sustituto de evaluaciones técnicas. Conecta casos de uso, datos, propiedad intelectual, contratos, consumidor, laboral, responsabilidad y gobierno corporativo.

### 4. Preparación para inversión y due diligence

Desarrolla el problema de llegar tarde a una revisión, la cadena de titularidad de activos, gobierno, capital y data room. Explica expresamente que la preparación jurídica no sustituye valoración, banca de inversión, contabilidad o tributación.

### 5. Estructuración de proyectos regulados

Diferencia una lista de permisos de una verdadera secuencia de viabilidad. Conecta autoridad, territorio, habilitaciones, contratos, condiciones precedentes, responsables y cronograma técnico/financiero.

### 6. Legal Operations

Plantea la pregunta central “¿falta capacidad o falta sistema?” y evita vender software como respuesta automática. Prioriza demanda, procesos, taxonomías, estados, responsables, documentos, obligaciones e indicadores antes de automatizar.

## SEO de intención y datos estructurados

`cro-solutions-v52.json` concentra la capa editorial/comercial v5.2 y separa esta optimización del catálogo jurídico canónico.

Cada landing recibe:

- `<title>` específico de intención;
- meta description específica;
- Open Graph title/description alineados;
- canonical y `og:url` heredados de la configuración v5.0/v5.1;
- FAQ visible en HTML;
- un segundo bloque JSON-LD `FAQPage` con exactamente tres preguntas y respuestas;
- enlaces a rutas relacionadas;
- continuidad hacia servicios, productos, sectores, perspectivas, Firma y Centro Demo.

La v5.2 no crea nuevas páginas únicamente para capturar keywords. Se optimizan las páginas que ya corresponden a decisiones empresariales reales y que derivan a una oferta jurídica existente.

## Honorarios: una sola fuente pública

La capa CRO no replica valores monetarios dentro de `cro-solutions-v52.json`. Cada landing explica **qué variables determinan el alcance** y remite a las secciones canónicas `#honorarios` o `#planes`.

Esto evita:

- inconsistencias entre páginas;
- precios desactualizados en landings SEO;
- confundir un valor orientativo con una cotización definitiva;
- presentar un plan recurrente como precio automático de cualquier asunto.

La política pública se mantiene: honorarios orientativos, sujetos a alcance final e IVA; tasas y gastos de terceros no están incluidos salvo estipulación expresa.

## Sin prueba social inventada

La v5.2 conserva el principio de v5.1: no se publican testimonios, casos de éxito, tasas de éxito, logos de clientes ni resultados no sustentados.

La credibilidad pública se apoya en elementos inspeccionables:

- 16 fichas jurídicas profundas;
- 8 lecturas sectoriales;
- 6 perspectivas desarrolladas;
- Centro Demo;
- delimitación de alcance, responsabilidades y límites;
- respuestas sustantivas a objeciones y FAQ.

`scripts/validate_cro_v52.py` bloquea expresamente contenido de prueba social no sustentada y evita introducir precios monetarios duplicados en la fuente CRO.

## Archivos v5.2

- `cro-solutions-v52.json`: contenido CRO/SEO estructurado de las seis rutas y guía del hub.
- `cro-v52.css`: estilos limitados a encaje, objeciones, honorarios, FAQ, rutas relacionadas y guía del hub.
- `scripts/apply_cro_v52.py`: aplica la capa después del generador/finalizador v5.1.
- `scripts/validate_cro_v52.py`: valida estructura, SEO, FAQ schema, honorarios, interlinking y ausencia de prueba social inventada.
- `scripts/validate_live_v52.py`: ejecuta primero todo el smoke v5.1 y después comprueba la capa v5.2 sobre la URL realmente servida.

## Construcción canónica

El orden vigente es:

```bash
python3 scripts/build_catalog_shells.py
node scripts/render_catalog_static.mjs
node scripts/render_services_v42.mjs
python3 scripts/enrich_editorial_pages.py
python3 scripts/apply_commercial_v43.py
python3 scripts/apply_visual_assets.py
python3 scripts/apply_ux_v45.py
python3 scripts/apply_detail_ux_v46.py
python3 scripts/apply_editorial_ux_v47.py
python3 scripts/normalize_editorial_v47.py
python3 scripts/normalize_growth_compat_v51.py
python3 scripts/apply_quality_v48.py
python3 scripts/normalize_quality_v48.py
python3 scripts/apply_operations_v49.py
python3 scripts/sync_public_version.py
python3 scripts/apply_production_v50.py
python3 scripts/apply_growth_v51.py
python3 scripts/finalize_growth_v51.py
python3 scripts/apply_cro_v52.py
```

`Site Quality and Deploy` repite la cadena y exige **diff cero** antes de validar:

- integridad de 46 páginas y recursos;
- catálogo estático de 16 fichas;
- conversión v4.4;
- UX v4.5, v4.6 y v4.7;
- calidad static-first v4.8;
- operación pública v4.9;
- producción v5.0;
- rutas de decisión v5.1;
- CRO y SEO de intención v5.2;
- selector guiado;
- contexto y datos estructurados;
- Firma, Perspectivas y Sectores;
- sistema visual;
- JavaScript;
- JSON.

Después de desplegar, `scripts/validate_live_v52.py` conserva todo el smoke v5.1 y comprueba hub, títulos SEO, calificación, objeciones, honorarios, FAQ schema y CTA específicos en las seis landings. `stable` solo se mueve después de ese control HTTP.

## Compatibilidad histórica

La v5.2 no reescribe ni debilita los contratos de releases anteriores. El único ajuste necesario fue hacer `scripts/validate_growth_v51.py` consciente de la nueva versión:

- hasta v5.1 exige el CTA genérico original;
- desde v5.2 exige que el bloque `SIGUIENTE PASO` siga existiendo;
- el validador v5.2 exige, adicionalmente, el CTA específico de cada ruta.

Así se preserva la garantía v5.1 sin impedir que una release posterior mejore el texto comercial.

## Incidencias detectadas durante el cierre v5.2

Las barreras automáticas volvieron a cumplir su función:

1. una operación de actualización movió `version.json` antes que el paquete completo; el constructor generó una salida intermedia etiquetada v5.2 sobre la arquitectura anterior;
2. el paquete completo se reconstruyó sobre el HEAD canónico nuevo y se integró mediante fast-forward sin forzar `main`;
3. la primera matriz completa aprobó idempotencia y v4.8–v5.0, pero v5.1 bloqueó el CTA específico porque esperaba literalmente el cierre genérico anterior;
4. el validador v5.1 se hizo version-aware y el job fallido se reejecutó sin relajar el control;
5. la segunda ejecución aprobó toda la matriz, GitHub Pages, smoke v5.2 y promoción de `stable`.

## Flujo operativo

- `main`: código vigente y fuente de publicación.
- `stable`: último commit que pasó construcción, idempotencia, validadores, Pages y smoke live.
- Los cambios funcionales activan el constructor canónico.
- Pages despliega únicamente una salida validada.
- El smoke post-deploy verifica la URL servida.
- `stable` avanza únicamente después del smoke.

## Próximo ciclo lógico

La arquitectura ya no necesita nuevas capas por inercia. El siguiente ciclo debería basarse en **evidencia de comportamiento** cuando exista una fuente real de medición: qué rutas reciben visitas, dónde se abandona, qué CTA se usa y qué necesidades llegan efectivamente a conversación.

Sin datos reales, las siguientes mejoras útiles son de precisión editorial y autoridad: profundizar contenidos específicos con respaldo normativo cuando aporte valor, preparar el dominio propio y Search Console cuando existan datos reales, y revisar performance/UX con pruebas de navegador sin sobrecargar la interfaz.
