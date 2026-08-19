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

async function expectNoHorizontalOverflow(page) {
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  expect(overflow).toBeLessThanOrEqual(1);
}

test('v7.2 expone un resumen de contratación en las 16 fichas', async ({ page }) => {
  for (const route of DETAIL_ROUTES) {
    await page.goto(`./${route}`);
    const summary = page.locator('[data-buying-clarity-v72="true"]');
    await expect(summary).toHaveCount(1);
    await expect(summary).toBeVisible();
    await expect(summary.locator('.v72-buying-meta > div')).toHaveCount(3);
    await expect(summary.locator('.v72-buying-panel')).toHaveCount(2);
    await expect(summary.locator('.v72-buying-secondary > article')).toHaveCount(3);
    await expect(summary).toContainText('Estas ampliaciones no hacen parte del alcance base');
    await expectNoHorizontalOverflow(page);
  }
});

test('v7.2 hace comprable la Auditoría Jurídica desde la primera lectura', async ({ page }) => {
  await page.goto('./productos/diagnostico-juridico-empresarial.html');
  const summary = page.locator('#v72-buying-summary');
  await expect(summary).toContainText('Auditoría jurídica de alcance cerrado');
  await expect(summary).toContainText('5 a 6 semanas');
  await expect(summary).toContainText('1 sociedad colombiana');
  await expect(summary).toContainText('Hasta 60 documentos');
  await expect(summary).toContainText('1 informe jurídico ejecutivo');
  await expect(summary).toContainText('1 matriz maestra de riesgos');
  await expect(summary).toContainText('Patrocinador con autoridad');
  await expect(summary).toContainText('Completitud del expediente');
  await expect(summary).toContainText('Sociedad adicional');
});

test('v7.2 diferencia una capacidad recurrente de un producto cerrado', async ({ page }) => {
  await page.goto('./servicios/direccion-juridica-externa.html');
  const summary = page.locator('#v72-buying-summary');
  await expect(summary).toContainText('Plan recurrente de dirección jurídica');
  await expect(summary).toContainText('Mensual o trimestral');
  await expect(summary).toContainText('Hasta 5 usuarios solicitantes');
  await expect(summary).toContainText('Bolsa mensual definida');
  await expect(summary).toContainText('1 tablero jurídico ejecutivo');
  await expect(summary).toContainText('Responsable de relación');
  await expect(summary).toContainText('Canal operativo');
  await expect(summary).toContainText('Bolsa adicional');
});
