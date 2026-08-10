# Meridiano Legal · Web canónica v5.5.0

Sitio público, responsive, static-first y autocontenido de Meridiano Legal, publicado mediante GitHub Pages. La v5.5 conserva la arquitectura jurídica, comercial, CRO, SEO, autoridad, privacidad y Browser E2E acumulada hasta v5.4 y añade una barrera medible de **performance y accesibilidad sobre la URL realmente desplegada**.

## Estado actual

La publicación conserva **46 páginas HTML** y esta arquitectura pública:

- 8 servicios profesionales;
- 8 productos jurídicos de alcance cerrado;
- 5 planes recurrentes;
- 1 hub de soluciones y 6 rutas de decisión empresarial;
- 8 lecturas sectoriales;
- 6 perspectivas jurídicas;
- página institucional de Firma;
- Centro Demo;
- Meridiano Empresas con datos ficticios y `noindex,nofollow`.

URL pública canónica:

`https://arendon7.github.io/MERDIANOLEGAL/`

La política de release mantiene dos refs:

- `main`: fuente/candidata vigente;
- `stable`: último commit que superó construcción, idempotencia, validadores, Pages, smoke, Browser E2E, axe y Lighthouse.

Una candidata puede estar temporalmente publicada y seguir sin estar aprobada. `stable` solo se mueve al final de la cadena completa.

## v5.5 · Performance + Accessibility QA

La infraestructura de navegador usa Node 22 o superior y dependencias fijadas mediante `package-lock.json` + `npm ci`:

- `@playwright/test` 1.62.0;
- `@axe-core/playwright` 4.12.1;
- `lighthouse` 13.4.1.

La suite Browser E2E cubre Chromium desktop, Chromium mobile y WebKit desktop. axe se ejecuta sobre siete superficies representativas. Lighthouse mide seis superficies públicas con presupuestos versionados en `quality-budgets-v55.json`.

## Resultado certificado de v5.5

El run funcional `31431923694` certificó la candidata `bd310076bbc098771dffd8fde03cabee9e16bc6f` antes del cierre documental.

### Browser E2E + axe

- 37 entradas de prueba;
- 35 aprobadas;
- 2 omitidas por diseño;
- 0 fallos;
- las 7 auditorías axe quedaron sin violaciones serias/críticas.

### Lighthouse

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Portada | 1.00 | 0.97 | 1207 ms | **0** | 0 ms | 73,930 B |
| Solución IA | 1.00 | 1.00 | 904 ms | 0 | 0 ms | 23,509 B |
| Producto IA | 1.00 | 1.00 | 906 ms | 0 | 0 ms | 33,142 B |
| Sector tecnología | 0.98 | 1.00 | 907 ms | 0.087 | 0 ms | 24,557 B |
| Perspectiva IA | 0.98 | 1.00 | 908 ms | 0.087 | 0 ms | 26,153 B |
| Demo | 1.00 | 1.00 | 917 ms | 0 | 0 ms | 21,905 B |

Las seis superficies cumplen sus presupuestos.

## Incidente CLS de portada y aprendizaje

La primera candidata v5.5 tenía un CLS de aproximadamente `0.304`, por encima del presupuesto `<= 0.15`. Lighthouse identificó `section.hero > .container > .hero-art` como zona desplazada.

La causa no era la descarga de la imagen: el HTML ya contenía `src`, dimensiones, prioridad y preload. El problema era de **estado de layout**:

1. el HTML inicial cargaba la imagen sin `visual-home-hero`;
2. `visual-v39.js` añadía la clase después del primer layout;
3. esa clase activa `position:absolute`;
4. la imagen pasaba tardíamente de participar en el grid a quedar fuera de flujo;
5. el navegador recalculaba el hero y acumulaba CLS.

La corrección materializa `visual-home-hero` desde el HTML inicial y elimina la mutación tardía en JavaScript.

Durante la reconstrucción apareció un segundo contrato histórico: `apply_quality_v48.py` volvía a materializar el `<img>` del hero después de la capa visual. `normalize_quality_v48.py` se convirtió en el punto determinista de compatibilidad para conservar la clase después de v4.8.

Finalmente, el validator v4.8 todavía exigía un orden literal de atributos (`<img src=...`). Se hizo semánticamente robusto: sigue exigiendo la imagen canónica, dimensiones, preload y prioridad, pero permite atributos adicionales de capas posteriores. El validator v5.5 exige además que `visual-home-hero` esté presente desde HTML y prohíbe que JavaScript vuelva a añadirla tarde.

**Resultado:** CLS de portada pasó de ~0.304 a **0**, performance de ~0.85 a **1.00**, manteniendo LCP ~1.2 s y TBT 0.

## Cadena de aprobación

`Site Quality and Deploy` exige:

1. reconstrucción canónica e idempotencia;
2. validadores históricos y actuales v4.4→v5.5;
3. JavaScript y JSON válidos;
4. despliegue en GitHub Pages;
5. smoke HTTP sobre la URL pública;
6. Browser E2E sobre Pages;
7. axe sobre superficies representativas;
8. Lighthouse sobre seis superficies y presupuestos versionados;
9. promoción de `stable`.

No se modifica un presupuesto para hacer pasar una candidata: se corrige la causa del incumplimiento.

## Memoria de ingeniería · Graphify + Obsidian

Meridiano incorpora una capa persistente de continuidad para evitar reconstruir el proyecto desde conversaciones largas.

- `AGENTS.md`: protocolo de entrada para agentes.
- `knowledge/00_CANON/`: contexto rápido, estado y tarea activa.
- `knowledge/10_DECISIONES/`: ADR y decisiones persistentes.
- `knowledge/20_ARQUITECTURA/`: mapa humano de fuentes, generadores y gates.
- `knowledge/30_RUNBOOKS/`: flujo de trabajo.
- `knowledge/HOME.md`: MOC para Obsidian.
- `knowledge/99_HANDOFF/`: protocolo para retomar en un chat nuevo.
- rama `knowledge/graphify-live`: grafo, reporte, wiki, `BUILD_META.json` y `PROJECT_SNAPSHOT.md` regenerables.

Graphify se ejecuta `--code-only`, sin backend LLM. Se usa para reducir el conjunto de impacto; toda relación inferida debe confirmarse contra `main`.

Los cambios exclusivamente de memoria regeneran Graphify, pero no disparan Pages + Playwright + axe + Lighthouse. Esto permite mantener contexto al día sin pagar el costo del pipeline público cuando la aplicación no cambió.

## Desarrollo local / QA

Instalar dependencias bloqueadas:

```bash
npm ci --ignore-scripts --no-audit --no-fund
```

Ejecutar Browser E2E:

```bash
npm run test:e2e
```

Ejecutar presupuestos Lighthouse contra la URL configurada:

```bash
npm run audit:quality
```

Regenerar Graphify local:

```bash
./scripts/refresh_graphify_knowledge.sh
```

Abrir la raíz del repositorio como vault de Obsidian y comenzar por `knowledge/HOME.md`.

## Integraciones externas: estado verdadero

Activas:

- GitHub Pages;
- WhatsApp como canal real de contacto;
- contexto comercial de navegación;
- telemetría first-party/local sin PII;
- sitemap, robots, canonical y Open Graph;
- demo estático/noindex;
- pipeline canónico, smoke, Browser E2E, axe, Lighthouse y `stable`.

Preparadas pero **no activas** sin configuración real:

- dominio personalizado/CNAME;
- Search Console;
- proveedor externo de analítica;
- CRM/backend de leads;
- almacenamiento servidor del formulario;
- email transaccional.

## Documentación

- `RELEASE-v5.5.md`: cierre técnico detallado de esta release.
- `RELEASE-v5.4.md`: incorporación de Browser E2E.
- `CHANGELOG.md`: historial acumulado de las capas anteriores.
- `knowledge/HOME.md`: entrada a la memoria operativa.

## Principios vigentes

- No inventar clientes, testimonios, casos de éxito ni resultados.
- No duplicar precios fuera de fuentes canónicas.
- No afirmar que existe un backend o integración que no esté activa.
- No enviar PII a telemetría.
- No mover `stable` con un gate rojo.
- No debilitar un validator para ocultar un defecto.
- Usar Graphify para navegar; usar `main` y pruebas para decidir.
