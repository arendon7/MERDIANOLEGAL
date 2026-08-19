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

test('v6.5 expone formatos y ritmo de trabajo en las 16 fichas profundas', async ({ page }) => {
  for (const route of DETAIL_ROUTES) {
    await page.goto(`./${route}`);
    const section = page.locator('[data-delivery-plan-clarity-v65="true"]');
    await expect(section).toHaveCount(1);
    await expect(section.locator('[data-delivery-plan-group="formats"] .v65-delivery-plan-row').first()).toBeVisible();
    await expect(section.locator('[data-delivery-plan-group="timeline"] .v65-delivery-plan-row').first()).toBeVisible();
    await expect(page.locator('.v6-detail-nav a')).toHaveCount(7);
    await expect(page.locator('.v6-detail-nav a[href="#v6-delivery-plan"]')).toHaveCount(0);
  }
});

for (const route of [
  'productos/diagnostico-juridico-empresarial.html',
  'servicios/direccion-juridica-externa.html',
]) {
  test(`v6.5 mantiene Entregables → Entrega y ritmo → Perímetro en ${route}`, async ({ page }) => {
    await page.goto(`./${route}`);
    await expect(page.locator('#v6-delivery-plan')).toBeVisible();
    const order = await page.evaluate(() => {
      const deliverables = document.querySelector('#v6-deliverables');
      const delivery = document.querySelector('#v6-delivery-plan');
      const perimeter = document.querySelector('#v6-perimeter');
      if (!deliverables || !delivery || !perimeter) return false;
      return Boolean(deliverables.compareDocumentPosition(delivery) & Node.DOCUMENT_POSITION_FOLLOWING)
        && Boolean(delivery.compareDocumentPosition(perimeter) & Node.DOCUMENT_POSITION_FOLLOWING);
    });
    expect(order).toBe(true);
  });
}
