# ADR-009 — W5 Home shell y boundary de Meridiano Contratos

Fecha: 2026-08-25
Estado: accepted para W5 candidate; no activa todavía producción.
Base certificada: `619d11ce829ce251f02314a96201f5d0e7eb120e`.

## Contexto

ADR-008 y el canon W4.1 marcaron RC02 — Meridiano Contratos — como capability pendiente porque el repositorio no contenía evidencia suficiente para inferir una plataforma, autenticación, almacenamiento, SLA o un CLM autónomo.

Posteriormente, el owner confirmó una capacidad comercial central que debe formar parte de Meridiano: los clientes de la firma pueden acceder a una plataforma privada para volver a generar contratos previamente configurados para su empresa; Meridiano mantiene jurídicamente los modelos maestros y los actualiza conforme a cambios legales y necesidades acordadas.

W5 necesita incorporar esa capacidad sin convertir la confirmación de negocio en claims técnicos que todavía no han sido verificados dentro de este repositorio.

## Decisión

RC02 pasa en W5 de `hipótesis comercial` a **capability owner-confirmed, candidate-only**.

Se autorizan, para el Home candidate, únicamente estos claims:

1. el cliente dispone de acceso para generar nuevos contratos sobre modelos previamente configurados para su organización;
2. los modelos pueden parametrizarse para usos recurrentes con clientes, trabajadores, proveedores u otros destinatarios definidos en el alcance;
3. Meridiano mantiene y versiona jurídicamente los modelos maestros durante la relación contratada;
4. las actualizaciones del modelo aplican a futuras generaciones y no reescriben automáticamente contratos ya celebrados;
5. cambios materiales, excepciones y negociaciones fuera del modelo se escalan a revisión jurídica humana.

## Claims todavía no autorizados

Hasta verificación técnica separada, la web no debe afirmar detalles sobre:

- método de autenticación;
- ubicación o arquitectura de almacenamiento;
- cifrado o certificaciones de seguridad;
- disponibilidad o uptime;
- integraciones con terceros;
- firma electrónica;
- pagos;
- CRM;
- automatización jurídica autónoma;
- modificación automática de contratos ejecutados.

## Relación con Sistema Contractual Empresarial

SO07 y RC02 no son duplicados.

- **SO07 — Sistema Contractual Empresarial** instala la arquitectura: inventario, taxonomía, modelos, cláusulas, playbook, aprobaciones, obligaciones, procedimiento y gobierno contractual según el alcance contratado.
- **RC02 — Meridiano Contratos** es continuidad: permite reutilizar modelos configurados, generar nuevos documentos, mantener los masters y escalar excepciones.

La secuencia `Contratación y Negocios → Sistema Contractual Empresarial → Meridiano Contratos` es una ruta comercial posible, no obligatoria.

## Boundary de publicación W5

W5.0 puede mostrar Meridiano Contratos como bloque central del Home candidate. No puede todavía:

- crear una ruta RC02 indexable;
- añadir RC02 al sitemap;
- exponer una URL de portal no verificada;
- describir infraestructura técnica no comprobada;
- activar canonical/SEO de RC02.

La ruta objetivo permanece `/servicios-continuos/meridiano-contratos.html`, pero su materialización y publicación requieren un gate específico posterior.

## Efecto sobre documentos anteriores

ADR-008, V8-OFFER-CANON y la matriz W4.1 conservan valor histórico como decisiones del momento en que la capability no estaba confirmada. Esta ADR no reescribe esa historia: registra explícitamente el cambio de estado para W5.

## Criterio de aceptación

- Home model identifica RC02 como `owner_confirmed` y `candidate_only`.
- Renderer falla si intenta convertir RC02 en link público no materializado.
- Copy incluye el límite sobre contratos ya celebrados y revisión humana de excepciones.
- No se publican claims técnicos no verificados.
- Producción permanece intacta hasta el gate coordinado de W5.
