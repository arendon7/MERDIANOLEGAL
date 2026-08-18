import { test, expect, expectNoHorizontalOverflow, openHomeLegacy } from './helpers.mjs';

test('v6 muestra una primera capa coherente y conserva la señal visual v5.26 en profundidad', async ({ page }) => {
  await page.goto('./');
  await expect(page.locator('.v6-hero')).toBeVisible();
  await expect(page.locator('#v6-situations')).toBeVisible();
  await expect(page.locator('.v6-home-method')).toBeVisible();
  await expect(page.locator('.v6-evidence')).toBeVisible();

  const signal = page.locator('[data-integral-v526="signal"]');
  await expect(signal).toHaveCount(1);
  await expect(signal).not.toBeVisible();
  await openHomeLegacy(page);
  await expect(page.locator('section.principles')).toHaveCount(0);
  await expect(page.locator('section.audience-strip')).toHaveCount(0);
  await expect(signal).toBeVisible();
  await expect(signal).toContainText('Menos capas. Más criterio aplicable.');
  await expect(signal).toContainText('16 fichas con alcance verificable');
  await expect(signal).toContainText('5 modalidades de contratación');
  await expect(signal).toContainText('8 lecturas sectoriales');
  const map = signal.locator('img[src="assets/decision-map-v526.svg"]');
  await expect(map).toBeVisible();
  await expect(map).toHaveJSProperty('complete', true);
  expect(await map.evaluate((node) => node.naturalWidth > 0 && node.naturalHeight > 0)).toBeTruthy();
  await expectNoHorizontalOverflow(page);
});

test('v6 ordena decisión antes de oferta y conserva secuencia v5.26 al abrir profundidad', async ({ page }) => {
  await page.goto('./');
  const v6Order = await page.locator('main > :is(section,details)').evaluateAll((nodes) => nodes.map((node) => ({
    situations: node.id === 'v6-situations',
    offer: node.id === 'v6-offer',
    contact: node.id === 'contacto',
    legacy: node.id === 'v6-depth',
  })));
  const situationsIndex = v6Order.findIndex((item) => item.situations);
  const offerIndex = v6Order.findIndex((item) => item.offer);
  const contactIndex = v6Order.findIndex((item) => item.contact);
  const legacyIndex = v6Order.findIndex((item) => item.legacy);
  expect(situationsIndex).toBeGreaterThan(-1);
  expect(offerIndex).toBeGreaterThan(situationsIndex);
  expect(contactIndex).toBeGreaterThan(offerIndex);
  expect(legacyIndex).toBeGreaterThan(contactIndex);

  await openHomeLegacy(page);
  const depth = page.locator('#v6-depth');
  await expect(depth.locator('#necesidades .need-card')).toHaveCount(6);
  await expect(depth.locator('[data-home-decision-v520="true"] [data-proof-model-v512]')).toHaveCount(5);
  await expect(depth.locator('.visual-home-hero')).toBeVisible();
  await expectNoHorizontalOverflow(page);
});
