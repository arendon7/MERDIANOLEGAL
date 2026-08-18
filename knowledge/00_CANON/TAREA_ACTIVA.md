# Meridiano Legal — Tarea activa

Actualizado: 2026-08-18.

## Estado

**Ciclo funcional activo: ninguno.**

Frente vigente: **cierre documental de v6.0.0 — Experience System**.

Rama de cierre: `docs/v600-release-closure`.
SHA funcional certificado: `a7940696cb358fcd4ace50e32f4a1463b76fdaa5`.
Al inicio de este cierre: `main == stable == a7940696cb358fcd4ace50e32f4a1463b76fdaa5`.

No abrir una v6.1/v6.0.1 funcional por inercia. El siguiente ciclo debe partir de un problema observable y un criterio de éxito verificable.

## Qué falta para cerrar v6.0 definitivamente

1. marcar `version.json` como canal certificado;
2. actualizar README y memoria canónica v5.x→v6.0;
3. crear `RELEASE-v6.0.md` con contrato, incidencias y evidencia;
4. someter el commit documental a los gates vigentes;
5. fusionar solo con certificación aplicable verde;
6. dejar que Builder → Pages → smoke → Browser/axe → Lighthouse → snapshot promueva `stable` automáticamente;
7. verificar al final `main == stable` y Graphify alineado al SHA de cierre.

## Resultado funcional ya certificado

- 46/46 superficies públicas migradas a Experience System v6.
- 16/16 fichas profundas preservan truth y profundidad.
- 8 productos + 8 servicios.
- 7 superficies de soluciones.
- 8 sectores.
- 6 perspectivas + hub editorial.
- 1 formulario físico.
- 30 pasos canónicos exactos.
- Idempotencia: PASS.
- Static validations: PASS.
- GitHub Pages sirve v6.0.0.
- Smoke público v5.0→v5.3: PASS.
- Browser E2E + axe sobre la v6 pública: PASS.
- Lighthouse: PASS sin relajar budgets.
- `stable` promovido automáticamente al SHA funcional final.
- Graphify funcional alineado: 1.007 nodos, 1.887 relaciones, 115 notas wiki, 17 specs E2E.

## Invariantes para el cierre

- no tocar contenido público para “hacer coincidir” documentación;
- no modificar catálogos jurídicos ni truth de ofertas;
- no inventar métricas, clientes, precios, testimonios o capacidades;
- no añadir backend/CRM/auth/pagos/firma/upload/agenda ficticios;
- no mover `stable` manualmente;
- no reducir tests, axe, Lighthouse ni budgets;
- mantener un único formulario físico y WhatsApp manual;
- mantener 46 HTML y 30 pasos canónicos;
- `main` y `stable` solo vuelven a coincidir después de la certificación del cierre.

## Próximo ciclo

**No definido todavía.**

Antes de proponerlo:

1. revisar comportamiento real de v6 ya publicada;
2. identificar una fricción observable de usuario, comercial, jurídica, responsive, accesibilidad, performance u operación;
3. formular una hipótesis y criterio de éxito;
4. evitar volver a sedimentar capas versionadas si el problema puede resolverse consolidando el Experience System existente;
5. si el cambio afecta superficies públicas, aplicar el design orchestrator y validar una muestra representativa antes de propagar.

Hasta completar el cierre documental, no iniciar trabajo funcional nuevo.
