import { test, expect, expectNoHorizontalOverflow, openHomeLegacy } from './helpers.mjs';

test('portada v6 distingue demo de portal productivo', async ({ page }) => {
  await page.goto('./');

  await expect(page.getByRole('link', { name: /Ver experiencia demo/i })).toBeVisible();
  await expect(page.getByRole('link', { name: 'Área de clientes' })).toHaveCount(0);
  await expect(page.getByRole('link', { name: 'Demo de cliente' })).toHaveCount(0);
  await expect(page.getByRole('link', { name: 'Centro demo' }).first()).toBeVisible();

  await openHomeLegacy(page);
  const labels = await page.locator('a[href^="demo.html"]').allTextContents();
  expect(labels.length).toBeGreaterThan(0);
  for (const label of labels) {
    expect(label).toMatch(/demo|demostrativ/i);
  }

  await expect.poll(async () => page.evaluate(() => window.MERIDIANO_PUBLIC_CONFIG?.capabilities?.clientPortal)).toEqual({
    enabled: false,
    url: '',
  });
  await expectNoHorizontalOverflow(page);
});

test('portal ficticio conserva frontera demostrativa explícita', async ({ page }) => {
  await page.goto('./demo.html');
  await expect(page.locator('body')).toHaveAttribute('data-capability-v521', 'demo-only');
  await expect(page.locator('body')).toHaveAttribute('data-experience-surface', 'demo');
  await expect(page.locator('.v6-demo-boundary')).toBeVisible();
  await expect(page.locator('.demo-badge').first()).toContainText('DEMO FICTICIA');
  await expect(page.getByRole('heading', { level: 1, name: 'Portal demostrativo' })).toBeVisible();
  await expect(page.locator('meta[name="robots"]')).toHaveAttribute('content', 'noindex,nofollow');
  await expect(page.getByText(/no se envía a ningún servidor/i)).toBeVisible();
  await expectNoHorizontalOverflow(page, 6);
});
