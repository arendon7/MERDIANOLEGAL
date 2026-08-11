# Meridiano Legal — Tarea activa

Actualizado: 2026-08-10.

## Ciclo cerrado

**v5.6 — Eficiencia de CI y observabilidad de calidad: funcionalmente certificado.**

Evidencia principal:

- run `31458580456`;
- candidata funcional `c4f48e43a1681cdbd24db4c6308878efeb801700` antes del cierre documental;
- idempotencia y validadores v4.4→v5.6: verdes;
- Pages: verde;
- smoke público: verde;
- Browser E2E: 35 passed / 2 skipped / 0 failed / 0 retries;
- axe: 7 superficies sin violaciones serias/críticas;
- Lighthouse: 6/6 superficies dentro de presupuesto;
- mediana-de-tres: no activada en el run final;
- tiempo hasta gate de `stable`: 160 s frente a baseline 279 s;
- mejora: 42.7%;
- cobertura reducida: no;
- budgets relajados: no.

## Aprendizajes consolidados

### Topología del pipeline

Browser E2E/axe y Lighthouse deben compartir deploy+smoke, pero no serializarse entre sí. La topología paralela reduce tiempo sin reducir garantía.

### Dependencias y caché

- usar `npm ci` + `package-lock.json`;
- usar caché npm de `setup-node`;
- no cachear binarios Playwright;
- Lighthouse instala solo Chromium;
- Browser E2E instala Chromium + WebKit con dependencias.

### Browser de laboratorio

Lighthouse debe usar Chromium fijado por Playwright para mantener comparabilidad entre runs. El Chrome mutable del runner produjo una desviación experimental de TBT que desapareció al restaurar el browser pinneado.

### Métricas volátiles

Si un primer fallo se limita exclusivamente a performance/LCP/CLS/TBT:

- dos muestras adicionales;
- tres muestras válidas obligatorias;
- mediana de tres;
- nunca mejor-de-N.

A11y y peso no se reintentan.

### Compatibilidad histórica

Los validators históricos deben hacerse version-aware cuando una release posterior **fortalece** su contrato. No se debe debilitar un gate para compatibilizar sintaxis nueva.

### Memoria y observabilidad

El pipeline deja resúmenes compactos de Playwright, Lighthouse y certificación CI. Graphify/Obsidian deben enlazar estos artefactos y el estado canónico, no sustituir los gates.

## Próximo ciclo propuesto

**v5.7 — Release governance, dependencias y salud operativa del pipeline.**

Objetivo: consolidar mantenimiento preventivo ahora que cobertura, performance y tiempos están bajo control.

Frentes prioritarios:

1. inventario versionado de Actions y dependencias QA;
2. política controlada de actualización de dependencias, evitando upgrades simultáneos innecesarios;
3. detección temprana de Actions/runtimes deprecados;
4. revisión de permisos mínimos de workflows y artefactos;
5. resumen de release reutilizable por Graphify/Obsidian;
6. limpieza de ramas temporales y deuda de CI sin tocar `main/stable` certificados;
7. mantener una ejecución pública completa obligatoria antes de cualquier promoción de `stable`.

## Regla para v5.7

No convertir mantenimiento en una actualización masiva. Cada cambio de runtime, Action o dependencia debe demostrar compatibilidad con el pipeline actual y conservar:

- 37 entradas E2E;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5;
- gate dual Browser + Lighthouse;
- idempotencia;
- `main == stable` al cierre.
