# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente.

## Qué es el proyecto

Sitio público y centro demostrativo de Meridiano Legal. Combina servicios jurídicos especializados, productos de alcance cerrado, planes recurrentes, rutas por necesidad, sectores, perspectivas y una experiencia demo estática.

## Arquitectura comercial vigente

- 8 servicios especializados;
- 8 productos de alcance cerrado;
- 5 planes recurrentes;
- 6 rutas de decisión en `soluciones/` más su hub;
- 8 sectores;
- 6 perspectivas más biblioteca;
- Firma/método y Centro Demo;
- 4 formas de contratación en portada;
- 5 bloques ejecutivos de compra en cada una de las 16 fichas profundas;
- calificación comercial v5.9 en el formulario, con resumen previo a WhatsApp;
- v5.10 transmite intención contextual desde las 16 fichas y muestra la ruta `calificación → alcance/propuesta → aceptación → inicio`.

Principio comercial: el usuario puede empezar por su situación empresarial y no necesita conocer el nombre técnico del servicio correcto.

## Diferenciaciones que no deben perderse

- Diagnóstico jurídico ≠ Auditoría Jurídica Empresarial Integral.
- Dirección Jurídica Externa ≠ disponibilidad jurídica ilimitada.
- Contratación Estratégica ≠ Sistema Contractual Empresarial.
- Sociedades/Gobierno/Inversión ≠ Empresa Lista para Inversión.
- Propiedad Intelectual como servicio ≠ paquete cerrado de activos protegidos.
- Gobernanza jurídica de IA como servicio ≠ programa cerrado de gobernanza.
- Proyecto regulado como servicio ≠ producto estructurado de alcance cerrado.
- Legal Operations ≠ Dirección Jurídica Externa.

## Fuentes principales

- `catalog-products-v41/` — productos.
- `catalog-services-v42/` — servicios.
- `growth-solutions-v51.json` — rutas por necesidad.
- `cro-solutions-v52.json` — CRO, objeciones, FAQ e intención de búsqueda.
- `authority-v53.json` — autoridad, interlinking y semántica editorial.
- `measurement-contract-v53.json` — eventos sin PII.
- `decision-v58.css` + `scripts/apply_decision_v58.py` — claridad de compra.
- `commercial-intake-v59.json`, CSS/JS y applicator/validator — calificación y privacidad.
- `conversion-close-v510.css` + `scripts/apply_conversion_v510.py` + `scripts/validate_conversion_v510.py` — intención, propuesta y cierre.
- `release-governance-v57.json` — policy de Actions, runtimes, dependencias, permisos e invariantes.
- `tests/e2e/` — contrato funcional de navegador.

## Secuencia de release

fuentes → generadores históricos → v5.8 → v5.9 → v5.10 → validadores → idempotencia → Pages → smoke → Browser/axe + Lighthouse → release-health → `stable`.

Los generadores históricos deben preservar atributos de capas posteriores. El builder debe terminar sin drift en la segunda pasada.

## Estado actual resumido

- Versión declarada en cierre: v5.10.0.
- Fundación funcional v5.10 certificada en run `31558953560`, SHA `f8b47f2ec2885cc39ff64a2448792f352619f9c3`.
- Antes del cierre documental: `main == stable` en ese SHA.
- Browser E2E: 35 passed / 2 skipped / 0 failed / 0 retries sobre 37 entradas.
- axe: 7 superficies sin violaciones serias/críticas.
- Lighthouse: 6/6 dentro de budget.
- CI: 173 s hasta `stable`, 38.0% mejor que baseline v5.5 de 279 s.
- v5.10 añade intención contextual, ruta de propuesta/cierre y anatomía de propuesta sin scoring ni promesa de contratación.
- La web sigue sin almacenar el formulario en servidor y sin CRM/backend.
- La telemetría no debe contener nombre, correo, empresa ni texto libre del caso.
- La release 5.9 ya no está pendiente: v5.10 se apoya sobre ella como capa certificada.

## Graphify

Graphify reduce el espacio de búsqueda, no decide la verdad. La rama `knowledge/graphify-live` contiene `BUILD_META.json`, snapshot, reporte y wiki. Confirmar siempre su `source_commit` contra `main` y luego verificar en fuente/tests.

## Regla de continuidad

Antes de explorar masivamente: confirmar refs, leer esta nota + `ESTADO_ACTUAL.md` + `TAREA_ACTIVA.md`, revisar Graphify y abrir únicamente el conjunto mínimo de archivos afectados.
