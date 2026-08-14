import { test, expect, expectNoHorizontalOverflow } from './helpers.mjs';

test('v5.26 consolida contexto superior en una sola superficie visual', async ({ page }) => {
  await page.goto('./');
  const signal = page.locator('[data-integral-v526="signal"]');
  await expect(signal).toHaveCount(1);
  await expect(page.locator('section.principles')).toHaveCount(0);
  await expect(page.locator('section.audience-strip')).toHaveCount(0);
  await expect(signal).toContainText('Menos capas. Más criterio aplicable.');
  await expect(signal).toContainText('16 fichas con alcance verificable');
  await expect(signal).toContainText('5 modalidades de contratación');
  await expect(signal).toContainText('8 lecturas sectoriales');
  const map = signal.locator('img[src="assets/decision-map-v526.svg"]');
  await expect(map).toBeVisible();
  await expect(map).toHaveJSProperty('complete', true);
  const loaded = await map.evaluate((node) => node.naturalWidth > 0 && node.naturalHeight > 0);
  expect(loaded).toBeTruthy();
  await expectNoHorizontalOverflow(page);
});

test('v5.26 conserva la secuencia necesidad y modalidad después de simplificar', async ({ page }) => {
  await page.goto('./');
  const order = await page.locator('main > section').evaluateAll((sections) => sections.map((node) => ({
    signal: node.matches('[data-integral-v526="signal"]'),
    needs: node.id === 'necesidades',
    decision: node.matches('[data-home-decision-v520="true"]'),
  })));
  const signalIndex = order.findIndex((item) => item.signal);
  const needsIndex = order.findIndex((item) => item.needs);
  const decisionIndex = order.findIndex((item) => item.decision);
  expect(signalIndex).toBeGreaterThan(-1);
  expect(needsIndex).toBeGreaterThan(signalIndex);
  expect(decisionIndex).toBeGreaterThan(needsIndex);
  await expect(page.locator('#necesidades .need-card')).toHaveCount(6);
  await expect(page.locator('[data-home-decision-v520="true"] [data-proof-model-v512]')).toHaveCount(5);
  await expect(page.locator('.visual-home-hero')).toBeVisible();
  await expectNoHorizontalOverflow(page);
});
