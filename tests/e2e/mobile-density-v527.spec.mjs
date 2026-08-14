import { test, expect, expectNoHorizontalOverflow } from './helpers.mjs';

test('v5.27 compacta comparación comercial en móvil sin perder opciones', async ({ page }) => {
  await page.goto('./');

  const decks = [
    { selector: '#servicios .service-grid', count: 8, maxHeight: 1200 },
    { selector: '#productos .product-grid', count: 8, maxHeight: 1200 },
    { selector: '#planes .commercial-plans', count: 5, maxHeight: 1900 },
    { selector: '#honorarios .pricing-grid-v43', count: 4, maxHeight: 2400 },
    { selector: '#sectores .sectors-grid', count: 8, maxHeight: 1100 },
  ];
  const width = await page.evaluate(() => window.innerWidth);

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

  if (width <= 620) {
    const pageHeight = await page.evaluate(() => document.documentElement.scrollHeight);
    expect(pageHeight).toBeLessThan(35000);
  }

  await expectNoHorizontalOverflow(page);
});
