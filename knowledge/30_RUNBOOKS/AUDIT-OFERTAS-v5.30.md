# Auditoría de las 16 ofertas — v5.30

Fecha: 2026-08-14.
Baseline: `36e014fd0cc852ce8835b6befdeb673328e838bd` (v5.29 certificada).

## Objetivo

Revisar las 8 fichas de producto y 8 fichas de servicio desde la perspectiva conjunta de dirección jurídica, diseño de servicios profesionales y decisión comercial, sin reducir profundidad ni inventar capacidades, clientes, resultados o tarifas.

## Universo auditado

### Productos

1. Auditoría Jurídica Empresarial Integral.
2. Empresa Jurídicamente Organizada.
3. Marca, Software y Activos Intangibles Protegidos.
4. Empresa Lista para Inversión.
5. Programa de Gobernanza Jurídica y Uso Responsable de IA.
6. Proyecto Regulado Jurídicamente Estructurado.
7. Sistema Contractual Empresarial.
8. Programa de Datos, Consumidor y Canales Digitales.

### Servicios

1. Diagnóstico Jurídico Empresarial.
2. Dirección Jurídica Externa.
3. Contratación Estratégica y Gestión Contractual.
4. Sociedades, Gobierno e Inversión.
5. Propiedad Intelectual y Activos Intangibles.
6. Tecnología e Inteligencia Artificial.
7. Estructuración Jurídica de Proyectos Regulados.
8. Legal Operations y Transformación de la Función Jurídica.

## Hallazgo principal

Las fichas no carecen de profundidad. Las fuentes canónicas ya describen, con buen nivel de precisión, pregunta ejecutiva, resultado, situaciones de uso, alcance, perímetro, método, entregables, formatos, cronograma, requisitos, responsabilidades, aceptación, límites, suplementos y soluciones relacionadas.

La fricción está en otro lugar: para entender cómo se compra la oferta, el lector debe reconstruir por sí mismo información distribuida entre varias secciones. En particular, todavía debe inferir:

- cuál es la unidad comercial concreta que se cotiza;
- cómo se dimensionan los honorarios sin confundirlos con una tarifa fija universal;
- qué variables hacen crecer o cambiar el alcance;
- qué ocurre si el asunto supera el perímetro inicial;
- qué criterio objetivo determina que el trabajo quedó cerrado.

## Diferencia entre productos y servicios

Los productos presentan la mejor claridad de perímetro: fijan cantidades máximas, entregables y criterios de aceptación. Su brecha principal consiste en explicar, cerca del resumen ejecutivo, que los honorarios corresponden al paquete estándar y que sociedades, documentos, trámites, remediaciones o unidades adicionales se manejan como suplementos o alcances separados.

Los servicios están jurídicamente bien delimitados, pero por naturaleza admiten más variabilidad. Allí la propuesta comercial debe explicar de forma expresa qué unidad se está comprando —negociación, proyecto, portafolio, capacidad recurrente, casos de uso, flujos, etc.— y cuáles variables cambian la intensidad del trabajo. No corresponde publicar una cifra genérica cuando hechos, actores, rondas, urgencia o especialidades alteran materialmente el esfuerzo.

## Riesgo de redundancia

v5.8 ya presenta un resumen ejecutivo de compra y v5.22 explica decisión, modalidad, capacidad instalada, alternativa y lente jurídica. Añadir otra sección extensa aumentaría densidad y repetiría contenido.

Por ello v5.30 no crea una narrativa independiente. Extiende el bloque `buying-clarity-v58` con una ficha compacta de contratación que cubre únicamente la información todavía no explícita.

## Contrato v5.30

Cada una de las 16 ofertas debe declarar cinco elementos adicionales mediante `offer-commercial-v530.json`:

1. `engagement_basis`: unidad o base de contratación;
2. `fee_logic`: cómo se dimensionan honorarios sin publicar precios inventados;
3. `drivers`: exactamente tres variables que pueden modificar alcance y honorarios;
4. `change_rule`: regla de ampliación o cambio de modalidad;
5. `close_rule`: definición de cierre verificable.

La materialización debe ubicarse dentro del resumen v5.8, inmediatamente después de sus metadatos de contratación, y enlazar a las secciones fuente de perímetro, aceptación y contacto.

## No objetivos

v5.30 no debe:

- publicar tarifas, descuentos, precios mínimos o máximos no aprobados;
- construir un cotizador automático;
- asignar puntajes o estimaciones algorítmicas de honorarios;
- reemplazar el catálogo fuente por un segundo catálogo paralelo;
- añadir CRM, pagos, firma electrónica, agenda, autenticación o carga documental;
- prometer tiempos de terceros, decisiones de autoridades, aceptación de contrapartes o resultados;
- duplicar las secciones de perímetro, entregables, aceptación o límites;
- relajar idempotencia, E2E, axe o Lighthouse.

## Criterio de éxito

Una persona que lea solo el hero, el resumen v5.8 y la extensión v5.30 debe poder responder antes de entrar al detalle largo:

- qué tipo de unidad está contratando;
- por qué los honorarios pueden cambiar;
- cuáles tres variables principales modifican el alcance;
- cómo se trata una ampliación;
- cómo se verifica el cierre;
- dónde consultar el perímetro y los criterios exactos de aceptación.
