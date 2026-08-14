# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-14.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Fuente técnica/documental: `main`.
- Snapshot funcional certificado: `stable`.
- Última release certificada: **5.29.0 — funnel observable y confianza contextual**.
- Baseline certificada al abrir el nuevo ciclo: `36e014fd0cc852ce8835b6befdeb673328e838bd`.
- Release candidata: **5.30.0 — profundidad comercial de las 16 ofertas**.
- Canal candidato: `github-pages-production-offer-commercial-depth-candidate`.

## Hallazgo que abre v5.30

La auditoría de `catalog-products-v41/` y `catalog-services-v42/` confirma que las 16 ofertas ya poseen profundidad jurídica, cantidades de referencia, entregables, cronogramas, responsabilidades, criterios de aceptación, límites y extensiones. La brecha no es sustantiva sino de arquitectura de compra: la persona debe integrar manualmente información distribuida para entender cómo se dimensiona la propuesta y cuándo termina el alcance.

## Contrato candidato v5.30

- `offer-commercial-v530.json` complementa, pero no reemplaza, los catálogos fuente.
- Cada oferta declara una unidad/base de contratación, lógica de honorarios, tres variables de dimensionamiento, regla de cambio de alcance y cierre verificable.
- No se permiten importes, monedas, tarifas inventadas, descuentos ni cotización automática.
- La materialización se integra dentro del resumen `buying-clarity-v58` para evitar una nueva sección narrativa y redundancia con v5.22.
- La síntesis enlaza al perímetro y aceptación originales de cada ficha.
- No se añade JavaScript funcional nuevo.
- v5.30 se encadena al final de v5.29 dentro del paso canónico `v5.18+`; el pipeline sigue teniendo 30 pasos.

## Baseline preservada

Hasta certificar v5.30 permanecen obligatorios todos los contratos v5.29:

- 46 HTML;
- 16 fichas profundas;
- un único formulario físico;
- WhatsApp manual;
- portal real deshabilitado;
- funnel v5.29 en memoria, sin PII ni persistencia;
- no inferir conversión comercial desde navegación, contacto o handoff;
- no clientes, testimonios o resultados inventados;
- no ocultar profundidad para aparentar menor densidad;
- idempotencia, validadores, E2E/axe y Lighthouse sin relajación;
- `stable` solo después de todos los gates verdes.

## Evidencia pendiente para cierre

v5.30 no es certificada hasta completar:

1. Release Governance sobre la candidata;
2. builder canónico de 30 pasos;
3. segunda pasada/idempotencia;
4. validaciones estáticas históricas y validator v5.30;
5. GitHub Pages y smoke público;
6. Browser E2E/axe;
7. Lighthouse;
8. promoción automática de `stable`;
9. Graphify regenerado y alineado con el `main` final.

## Estado del ciclo

**v5.30 está en desarrollo como candidata. v5.29 continúa siendo la última release funcional certificada hasta completar el ciclo de gates.**
