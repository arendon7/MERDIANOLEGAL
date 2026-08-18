import { test, expect, expectNoHorizontalOverflow, openDetailLegacy } from './helpers.mjs';

const offers = [
  ['./productos/diagnostico-juridico-empresarial.html', 'product-diagnostic'],
  ['./productos/empresa-juridicamente-organizada.html', 'product-organized'],
  ['./productos/activos-intangibles-protegidos.html', 'product-assets'],
  ['./productos/empresa-lista-para-inversion.html', 'product-investment'],
  ['./productos/programa-gobernanza-ia.html', 'product-ai'],
  ['./productos/proyecto-regulado-estructurado.html', 'product-regulated'],
  ['./productos/sistema-contractual-empresarial.html', 'product-contract-system'],
  ['./productos/proteccion-datos-consumidor.html', 'product-data-consumer'],
  ['./servicios/diagnostico-juridico-empresarial.html', 'service-diagnostic'],
  ['./servicios/direccion-juridica-externa.html', 'service-direction'],
  ['./servicios/contratacion-estrategica.html', 'service-contracts'],
  ['./servicios/sociedades-gobierno-inversion.html', 'service-corporate'],
  ['./servicios/propiedad-intelectual.html', 'service-ip'],
  ['./servicios/tecnologia-inteligencia-artificial.html', 'service-ai'],
  ['./servicios/proyectos-regulados.html', 'service-regulated'],
  ['./servicios/legal-operations.html', 'service-ops'],
];

test('v5.30 cubre exactamente las 16 ofertas con lógica de contratación verificable', async ({ page }) => {
  for (const [path, catalogId] of offers) {
    await page.goto(path);
    const block = page.locator(`[data-offer-commercial-v530="${catalogId}"]`);
    await expect(block).toHaveCount(1);
    await expect(block.getByText('CONTRATACIÓN SIN LETRA PEQUEÑA')).toHaveCount(1);
    await expect(block.getByRole('link', { name: 'Ver perímetro exacto' })).toHaveAttribute('href', '#perimetro-title');
    await expect(block.getByRole('link', { name: 'Ver criterios de cierre' })).toHaveAttribute('href', '#aceptacion-title');
    await expect(block.locator('.buying-contract-driver-v530')).toHaveCount(3);
    await expect(page.locator('#perimetro-title')).toHaveCount(1);
    await expect(page.locator('#aceptacion-title')).toHaveCount(1);
    await expect(page.locator('#contacto')).toHaveCount(1);
  }
});

test('v5.30 explica honorarios sin publicar una cotización inventada', async ({ page }) => {
  await page.goto('./productos/diagnostico-juridico-empresarial.html');
  await openDetailLegacy(page);
  const block = page.locator('[data-offer-commercial-v530="product-diagnostic"]');
  await expect(block).toBeVisible();
  await expect(block).toContainText('UNIDAD DE CONTRATACIÓN');
  await expect(block).toContainText('honorarios');
  await expect(block).toContainText('CIERRE VERIFICABLE');
  await expect(block).toContainText('SI EL ALCANCE CAMBIA');
  const text = await block.innerText();
  expect(text).not.toMatch(/\$|€|£|\bCOP\b|\bUSD\b|\bEUR\b/i);

  const details = block.locator('details.buying-contract-drivers-wrap-v530');
  await details.locator('summary').focus();
  await expect(details.locator('summary')).toBeFocused();
  await details.locator('summary').press('Enter');
  await expect(details).toHaveAttribute('open', '');
  await expect(details.locator('.buying-contract-driver-v530')).toHaveCount(3);
});

test('v5.30 diferencia un servicio recurrente sin fingir tarifa fija', async ({ page }) => {
  await page.goto('./servicios/direccion-juridica-externa.html');
  await openDetailLegacy(page);
  const block = page.locator('[data-offer-commercial-v530="service-direction"]');
  await expect(block).toContainText('Plan recurrente mensual o trimestral');
  await expect(block).toContainText('capacidad recurrente');
  await expect(block).toContainText('SLA');
  const text = await block.innerText();
  expect(text).not.toMatch(/\$|€|£|\bCOP\b|\bUSD\b|\bEUR\b/i);
});

test('v5.30 conserva contención móvil y foco navegable al abrir profundidad', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('./productos/sistema-contractual-empresarial.html');
  await openDetailLegacy(page);
  const block = page.locator('[data-offer-commercial-v530="product-contract-system"]');
  await expect(block).toBeVisible();
  const summary = block.locator('summary');
  await summary.focus();
  await expect(summary).toBeFocused();
  await expectNoHorizontalOverflow(page);
});
