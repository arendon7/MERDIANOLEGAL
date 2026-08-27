import AxeBuilder from '@axe-core/playwright';
import { test, expect, expectNoHorizontalOverflow } from './helpers.mjs';

// The disposable server root contains the exact future production index.html.
const candidate = './';

test('W5.0E future root has no serious/critical axe violations', async ({ page }) => {
  const response = await page.goto(candidate);
  expect(response?.status()).toBe(200);
  const results = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']).analyze();
  const blocking = results.violations.filter((item) => ['serious', 'critical'].includes(item.impact));
  expect(blocking, JSON.stringify(blocking, null, 2)).toEqual([]);
  await expectNoHorizontalOverflow(page, 1);
});
