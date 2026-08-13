import { test, expect, expectNoHorizontalOverflow } from './helpers.mjs';

test('portada v5.25 publica autoridad profesional verificable', async ({ page }) => {
  await page.goto('./');
  const proof = page.locator('[data-professional-authority-v525="home"]');
  await expect(proof).toHaveCount(1);
  await expect(proof).toContainText('Universidad EAFIT');
  await expect(proof).toContainText('2018');
  await expect(proof).toContainText('Greenatics S.A.S.');
  await expect(proof).toContainText(/no corresponde a una lista de clientes/i);
  await expect(proof.getByRole('link', { name: /ver trayectoria profesional/i })).toHaveAttribute('href', 'firma.html#trayectoria');
  await expectNoHorizontalOverflow(page);
});

test('firma v5.25 separa trayectoria profesional de experiencia demo', async ({ page }, testInfo) => {
  await page.goto('./firma.html');
  const trajectory = page.locator('[data-professional-authority-v525="firm"]');
  await expect(trajectory).toHaveCount(1);
  for (const text of ['Greenatics S.A.S.', 'Herbalgem S.A.S.', 'Grupo Pineal S.A.S.', 'Incubik', 'Compañía de Empaques']) {
    await expect(trajectory).toContainText(text);
  }
  await expect(trajectory).toContainText(/no constituye una lista de clientes/i);
  if (testInfo.project.name.includes('mobile')) {
    const toggle = page.locator('button[aria-controls="editorial-nav-v47"]');
    await expect(toggle).toBeVisible();
    await expect(toggle).toHaveAccessibleName('Abrir menú');
    await toggle.click();
    await expect(toggle).toHaveAttribute('aria-expanded', 'true');
  }
  await expect(page.getByRole('link', { name: 'Trayectoria', exact: true })).toHaveAttribute('href', '#trayectoria');
  await expect(page.getByRole('link', { name: 'Ver trayectoria profesional', exact: true })).toHaveAttribute('href', '#trayectoria');
  await expect(page.getByRole('link', { name: 'Ver experiencia demostrativa', exact: true })).toHaveCount(0);
  await expectNoHorizontalOverflow(page);
});
