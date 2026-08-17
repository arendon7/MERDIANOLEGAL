import { test, expect, expectNoHorizontalOverflow } from './helpers.mjs';

const deepPages = [
  './productos/diagnostico-juridico-empresarial.html',
  './productos/empresa-juridicamente-organizada.html',
  './productos/activos-intangibles-protegidos.html',
  './productos/empresa-lista-para-inversion.html',
  './productos/programa-gobernanza-ia.html',
  './productos/proyecto-regulado-estructurado.html',
  './productos/sistema-contractual-empresarial.html',
  './productos/proteccion-datos-consumidor.html',
  './servicios/diagnostico-juridico-empresarial.html',
  './servicios/direccion-juridica-externa.html',
  './servicios/contratacion-estrategica.html',
  './servicios/sociedades-gobierno-inversion.html',
  './servicios/propiedad-intelectual.html',
  './servicios/tecnologia-inteligencia-artificial.html',
  './servicios/proyectos-regulados.html',
  './servicios/legal-operations.html',
];

const solutionPages = [
  './soluciones/ordenar-riesgo-juridico-empresa.html',
  './soluciones/direccion-juridica-externa-empresa.html',
  './soluciones/gobernar-inteligencia-artificial-empresa.html',
  './soluciones/preparar-empresa-para-inversion.html',
  './soluciones/estructurar-proyecto-regulado.html',
  './soluciones/ordenar-operacion-juridica.html',
];

test('v5.31 reduce las fichas a dos grupos decisionales abiertos sin perder profundidad', async ({ page }) => {
  for (const path of deepPages) {
    await page.goto(path);
    await expect(page.locator('[data-buying-clarity-v58="true"]')).toBeVisible();
    await expect(page.locator('[data-offer-commercial-v530]')).toBeVisible();
    await expect(page.locator('[data-decision-compression-v531="decision-result"]')).toBeVisible();
    const depth = page.locator('details[data-decision-compression-v531="offer-narrative"]');
    await expect(depth).toHaveCount(1);
    await expect(depth).not.toHaveAttribute('open', '');
    await expect(page.locator('#alcance-title')).toHaveCount(1);
    await expect(page.locator('#contacto')).toHaveCount(1);
  }
});

test('v5.31 mantiene la narrativa secundaria accesible por teclado y conserva su contenido', async ({ page }) => {
  await page.goto('./productos/programa-gobernanza-ia.html');
  const depth = page.locator('details[data-decision-compression-v531="offer-narrative"]');
  const summary = depth.locator('summary');
  await summary.focus();
  await expect(summary).toBeFocused();
  await summary.press('Enter');
  await expect(depth).toHaveAttribute('open', '');
  await expect(depth.getByText('CRITERIO DE CONTRATACIÓN')).toBeVisible();
  await expect(depth.getByText('ALTERNATIVA CERCANA')).toBeVisible();
  await expect(depth.getByText('LENTE JURÍDICA')).toBeVisible();
});

test('v5.31 deja abierta la ruta principal y pliega solo soporte secundario en las seis soluciones', async ({ page }) => {
  for (const path of solutionPages) {
    await page.goto(path);
    await expect(page.locator('#ruta')).toBeVisible();
    await expect(page.getByText('ALCANCE Y HONORARIOS')).toBeVisible();
    await expect(page.getByText('RESULTADO ESPERADO')).toBeVisible();
    await expect(page.getByText('LÍMITES')).toBeVisible();
    await expect(page.locator('.growth-cta-v51')).toBeVisible();
    for (const key of ['objections', 'faq', 'related', 'proof']) {
      const details = page.locator(`details[data-decision-compression-v531="solution-${key}"]`);
      await expect(details).toHaveCount(1);
      await expect(details).not.toHaveAttribute('open', '');
    }
  }
});

test('v5.31 conserva foco nativo y contención móvil en ficha y ruta de necesidad', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  for (const path of ['./servicios/direccion-juridica-externa.html', './soluciones/gobernar-inteligencia-artificial-empresa.html']) {
    await page.goto(path);
    const summary = page.locator('details[data-decision-compression-v531] > summary').first();
    await summary.focus();
    await expect(summary).toBeFocused();
    await expectNoHorizontalOverflow(page);
  }
});
