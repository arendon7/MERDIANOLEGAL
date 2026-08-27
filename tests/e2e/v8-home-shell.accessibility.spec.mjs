import AxeBuilder from '@axe-core/playwright';
import { test, expect } from '@playwright/test';

const wcagTags = ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'];
const blockingImpacts = new Set(['serious', 'critical']);

function compact(violations) {
  return violations.map((violation) => ({
    id: violation.id,
    impact: violation.impact,
    targets: violation.nodes.slice(0, 8).map((node) => node.target.join(' ')),
  }));
}

test('W5 Home preview no presenta violaciones axe serious/critical WCAG 2.1 AA', async ({ page }) => {
  const response = await page.goto('./.w5-preview/index.html');
  expect(response?.status()).toBe(200);
  await expect(page.locator('h1')).toHaveCount(1);

  const result = await new AxeBuilder({ page }).withTags(wcagTags).analyze();
  const blocking = result.violations.filter((violation) => blockingImpacts.has(violation.impact));
  expect(compact(blocking), JSON.stringify(compact(blocking), null, 2)).toEqual([]);
});

test('W5 Home preview conserva landmarks y nombres accesibles de navegación', async ({ page }) => {
  await page.goto('./.w5-preview/index.html');
  await expect(page.locator('header[data-ml-shell]')).toHaveCount(1);
  await expect(page.locator('nav[aria-label="Navegación principal"]')).toHaveCount(1);
  await expect(page.locator('footer')).toHaveCount(1);
  await expect(page.getByRole('button', { name: /qué hacemos/i })).toHaveCount(1);
  await expect(page.getByRole('link', { name: /hablar con meridiano/i }).first()).toBeVisible();
  await expect(page.locator('[data-ml-menu-toggle]')).toHaveAttribute('aria-controls', 'ml-nav-panel');
  await expect(page.locator('[data-ml-mega-toggle]')).toHaveAttribute('aria-controls', 'ml-mega-menu');
});
