# Meridiano Legal — Tarea activa

Actualizado: 2026-08-12.

## Estado

**No hay una release funcional activa. v5.20.0 está formalmente cerrada y no existe una v5.21 abierta.**

El snapshot público certificado permanece en `stable = 85bdcfc9b52172e085dfa9b1df8e8d081b136233`. Los commits documentales posteriores en `main` no modifican el runtime público certificado.

## Última release cerrada

**v5.20.0 — compresión de decisión en portada.**

- PR funcional: #74.
- Hotfixes de compatibilidad: #75 y #76.
- SHA funcional certificado: `85bdcfc9b52172e085dfa9b1df8e8d081b136233`.
- Run final: `31651473515`.
- PR de cierre documental: #77.
- Merge documental principal: `62f2f9b5069682ed1fbd8b72865bec267f6c6ac3`.
- Graphify posterior al cierre principal: PASS, versión `5.20.0`, 588 nodos, 948 relaciones y 94 notas wiki.

## Resultado

La portada conserva seis rutas por situación empresarial y una sola superficie con cinco modalidades de contratación. Ya no materializa el bloque separado v5.8 ni la sección histórica `#elegir`. Las 16 fichas profundas, el formulario y el handoff permanecen íntegros.

Certificación final:

- Browser E2E + axe: 37 → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- Lighthouse: 6/6 PASS;
- accesibilidad: 1.00 en las seis superficies;
- performance: 0.98–1.00;
- portada: performance 1.00, accesibilidad 1.00, LCP 1421 ms, CLS 0, TBT 83 ms;
- CI hasta `stable`: 191 s, 31.5% mejor que baseline;
- cobertura reducida: no;
- budgets relajados: no.

## Siguiente ciclo

Cualquier trabajo posterior debe comenzar con una auditoría del estado vigente y abrir explícitamente una nueva tarea/release antes de modificar comportamiento público. No reutilizar v5.20 para incorporar nuevas features ni cambios funcionales.
