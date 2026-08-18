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

test('v6.3 expone Engagement Clarity en las 16 fichas profundas', async ({ page }) => {
  for (const route of DETAIL_ROUTES) {
    await page.goto(`./${route}`);
    await expect(page.locator('[data-engagement-clarity-v63="true"]')).toHaveCount(1);
    await expect(page.locator('[data-engagement-clarity-v63-nav="true"]')).toHaveCount(1);
    await expect(page.locator('[data-engagement-group="requirements"] .v63-engagement-row').first()).toBeVisible();
    await expect(page.locator('[data-engagement-group="responsibilities"] .v63-engagement-row').first()).toBeVisible();
  }
});

for (const route of [
  'productos/diagnostico-juridico-empresarial.html',
  'servicios/direccion-juridica-externa.html',
]) {
  test(`v6.3 navega a condiciones del encargo desde ${route}`, async ({ page }) => {
    await page.goto(`./${route}`);
    const nav = page.locator('[data-engagement-clarity-v63-nav="true"]');
    await expect(nav).toHaveText('Para empezar');
    await nav.click();
    await expect(page).toHaveURL(/#v6-engagement$/);
    await expect(page.locator('#v6-engagement')).toBeVisible();
  });
}
