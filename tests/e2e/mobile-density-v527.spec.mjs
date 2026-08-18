import { test, expect, expectNoHorizontalOverflow, openDisclosure, openHomeLegacy } from './helpers.mjs';

test('v6 compacta la primera lectura móvil y conserva decks v5.27 bajo profundidad', async ({ page }) => {
  await page.goto('./');
  const width = await page.evaluate(() => window.innerWidth);

  await expect(page.locator('#v6-situations .v6-index-row')).toHaveCount(6);
  await expect(page.locator('#v6-offer .v6-family')).toHaveCount(3);
  await expectNoHorizontalOverflow(page);

  if (width <= 620) {
    const firstLayerHeight = await page.evaluate(() => document.documentElement.scrollHeight);
    expect(firstLayerHeight).toBeLessThan(22000);
  }

  await openDisclosure(page.locator('#v6-commercial-depth'));
  await openHomeLegacy(page);

  const decks = [
    { selector: '#servicios .service-grid', count: 8, maxHeight: 1200 },
    { selector: '#productos .product-grid', count: 8, maxHeight: 1200 },
    { selector: '#planes .commercial-plans', count: 5, maxHeight: 1900 },
    { selector: '#honorarios .pricing-grid-v43', count: 4, maxHeight: 2400 },
    { selector: '#sectores .sectors-grid', count: 8, maxHeight: 1100 },
  ];

  for (const deck of decks) {
    const node = page.locator(deck.selector);
    await expect(node).toHaveCount(1);
    expect(await node.evaluate((el) => el.children.length)).toBe(deck.count);

    if (width <= 620) {
      const metrics = await node.evaluate((el) => ({
        clientWidth: el.clientWidth,
        scrollWidth: el.scrollWidth,
        height: el.getBoundingClientRect().height,
        firstWidth: el.firstElementChild?.getBoundingClientRect().width || 0,
      }));
      expect(metrics.scrollWidth).toBeGreaterThan(metrics.clientWidth + 40);
      expect(metrics.firstWidth).toBeGreaterThan(280);
      expect(metrics.height).toBeLessThan(deck.maxHeight);
    }
  }

  await expectNoHorizontalOverflow(page);
});
