import { test, expect, expectNoHorizontalOverflow } from './helpers.mjs';

test('portada muestra prueba profesional concreta sin presentarla como clientes', async ({ page }) => {
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

test('firma distingue trayectoria del director de la experiencia demostrativa', async ({ page }, testInfo) => {
  await page.goto('./firma.html');
  const trajectory = page.locator('[data-professional-authority-v525="firm"]');
  await expect(trajectory).toHaveCount(1);
  await expect(trajectory).toContainText('Greenatics S.A.S.');
  await expect(trajectory).toContainText('Herbalgem S.A.S.');
  await expect(trajectory).toContainText('Grupo Pineal S.A.S.');
  await expect(trajectory).toContainText('Incubik');
  await expect(trajectory).toContainText('Compañía de Empaques');
  await expect(trajectory).toContainText(/no constituye una lista de clientes/i);
  if (testInfo.project.name.includes('mobile')) {
    const toggle = page.locator('.menu-toggle');
    await expect(toggle).toBeVisible();
    await toggle.click();
    await expect(toggle).toHaveAttribute('aria-expanded', 'true');
  }
  await expect(page.getByRole('link', { name: 'Trayectoria', exact: true })).toHaveAttribute('href', '#trayectoria');
  await expect(page.getByRole('link', { name: 'Ver trayectoria profesional', exact: true })).toHaveAttribute('href', '#trayectoria');
  await expect(page.getByRole('link', { name: 'Ver experiencia demostrativa', exact: true })).toHaveCount(0);
  await expectNoHorizontalOverflow(page);
});
