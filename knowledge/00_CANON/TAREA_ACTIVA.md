# Meridiano Legal — Tarea activa

Actualizado: 2026-08-12.

## Estado

**No hay una release funcional activa. v5.21.0 está formalmente cerrada y certificada.**

El snapshot público funcional permanece en `stable = b2a6d4d4d2608362e86b53ea4cc197cd7ce33cc1`. Los cambios posteriores de `main` son exclusivamente documentación/memoria y no implican una nueva release pública.

## Última release cerrada: v5.21

Objetivo cumplido: convertir la frontera entre demo y capacidad real en un contrato verificable.

- portal real de clientes: `disabled`;
- `demo.html` nunca puede configurarse como portal real;
- 25 accesos públicos hacia la demo quedan explícitamente rotulados como `demo`/`demostrativo`;
- runtime/status reflejan la capacidad real;
- demo conserva datos ficticios, `demo-only` y exactamente un `noindex,nofollow`;
- `demo.js` no inyecta robots meta dinámicamente;
- una futura activación exige URL HTTPS real y acceso público verificable.

## Evidencia de cierre

- PR funcional: #79.
- Hotfixes: #80 y #81.
- SHA funcional certificado: `b2a6d4d4d2608362e86b53ea4cc197cd7ce33cc1`.
- Run público final: `31658340092`.
- Browser E2E + axe: 43 → 41 PASS / 2 SKIP / 0 FAIL / 0 RETRY.
- Lighthouse: 6/6 PASS; accesibilidad 1.00; performance 0.98–1.00.
- Portada: performance 1.00, accesibilidad 1.00, LCP 1410 ms, CLS 0, TBT 91 ms.
- CI hasta `stable`: 178 s; 36.2% mejor que baseline 279 s.
- cobertura reducida: no.
- budgets relajados: no.
- PR de cierre documental principal: #82.
- Graphify posterior al cierre documental principal: PASS, versión `5.21.0`.

## Regla para el próximo ciclo

No abrir una v5.22 por continuidad numérica o acumulación de features. Antes de cualquier nuevo desarrollo debe existir una auditoría breve del estado actual y un frente con:

1. problema observable;
2. impacto esperado;
3. alcance técnico/comercial concreto;
4. no-objetivos;
5. pruebas y criterios de cierre;
6. preservación de los contratos certificados v5.8→v5.21.

## Invariantes que no deben degradarse

- 46 páginas HTML y 16 fichas profundas;
- un único formulario físico canónico;
- static-first;
- no inventar integraciones o capacidades productivas;
- no PII en telemetría;
- WhatsApp manual mientras no exista integración real;
- portal real deshabilitado mientras no exista implementación auténtica;
- no reducir cobertura ni relajar budgets;
- `stable` solo después de gates verdes para cambios funcionales/publicables;
- Graphify es memoria derivada; su frescura se verifica contra el último run exitoso y no mediante un SHA humano fijado permanentemente.

**No existe una v5.22 activa.**
