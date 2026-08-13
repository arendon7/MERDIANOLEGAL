import { test, expect } from './helpers.mjs';

test('v5.23 conserva completo el formulario alrededor de la síntesis', async ({ page }) => {
  await page.goto('./#contacto');
  const form = page.locator('form[data-contact-compression-v523="true"]');
  await expect(form).toHaveCount(1);
  const synthesis = form.locator('[data-contact-synthesis-v523="true"]');
  await expect(synthesis).toHaveCount(1);
  await expect(synthesis).toHaveAttribute('role', 'region');
  expect(await synthesis.evaluate((node) => node.tagName)).toBe('DIV');
  await expect(form.locator('textarea[name="message"]')).toHaveCount(1);
  await expect(form.locator('[name="privacy"]')).toHaveCount(1);
  await expect(form.locator('button[type="submit"]')).toHaveCount(1);
});
