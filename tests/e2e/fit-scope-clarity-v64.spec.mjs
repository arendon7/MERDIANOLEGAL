import { test, expect } from './helpers.mjs';

const DETAIL_ROUTES = [
  'productos/activos-intangibles-protegidos.html',
  'productos/diagnostico-juridico-empresarial.html',
  'productos/empresa-juridicamente-organizada.html',
  'productos/empresa-lista-para-inversion.html',
  'productos/programa-gobernanza-ia.html',
  'productos/proteccion-datos-consumidor.html',
  'productos/proyecto-regulado-estructurado.html',
  'productos/sistema-contractual-empresarial.html',
  'servicios/contratacion-estrategica.html',
  'servicios/diagnostico-juridico-empresarial.html',
  'servicios/direccion-juridica-externa.html',
  'servicios/legal-operations.html',
  'servicios/propiedad-intelectual.html',
  'servicios/proyectos-regulados.html',
  'servicios/sociedades-gobierno-inversion.html',
  'servicios/tecnologia-inteligencia-artificial.html',
];

test('v6.4 expone encaje y ampliaciones de alcance en las 16 fichas profundas', async ({ page }) => {
  for (const route of DETAIL_ROUTES) {
    await page.goto(`./${route}`);
    const section = page.locator('[data-fit-scope-clarity-v64="true"]');
    await expect(section).toHaveCount(1);
    await expect(section.locator('[data-fit-scope-group="situations"] .v64-fit-scope-row').first()).toBeVisible();
    await expect(section.locator('[data-fit-scope-group="supplements"] .v64-fit-scope-row').first()).toBeVisible();
    await expect(page.locator('.v6-detail-nav a[href="#v6-fit-scope"]')).toHaveCount(0);
  }
});

for (const route of [
  'productos/diagnostico-juridico-empresarial.html',
  'servicios/contratacion-estrategica.html',
]) {
  test(`v6.4 mantiene el bloque entre Resultado y Entregables en ${route}`, async ({ page }) => {
    await page.goto(`./${route}`);
    await expect(page.locator('#v6-fit-scope')).toBeVisible();
    const order = await page.evaluate(() => {
      const result = document.querySelector('#v6-result');
      const fit = document.querySelector('#v6-fit-scope');
      const deliverables = document.querySelector('#v6-deliverables');
      if (!result || !fit || !deliverables) return false;
      return Boolean(result.compareDocumentPosition(fit) & Node.DOCUMENT_POSITION_FOLLOWING)
        && Boolean(fit.compareDocumentPosition(deliverables) & Node.DOCUMENT_POSITION_FOLLOWING);
    });
    expect(order).toBe(true);
  });
}
