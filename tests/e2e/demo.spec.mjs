import { test, expect, expectNoHorizontalOverflow } from './helpers.mjs';

async function enterDemo(page, hash = '') {
  await page.goto(`./demo.html${hash}`);
  const profile = page.locator('.credential-card[data-email="cliente@empresa-demo.com"]');
  await profile.click();
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await expect(page.locator('#portal-view')).not.toHaveClass(/hidden/);
}

test('portal demo autentica perfil ficticio y conserva nueve módulos', async ({ page }) => {
  await enterDemo(page);
  await expect(page.locator('#user-name')).toHaveText('Laura Gómez');
  await expect(page.locator('.portal-nav')).toHaveCount(9);
  await expect(page.locator('#view-title')).toHaveText('Resumen');
  await expectNoHorizontalOverflow(page, 6);
});

test('hash profundo abre Documentos guiados y genera vista previa ficticia', async ({ page }) => {
  await enterDemo(page, '?context=Prueba+E2E#documentos');
  await expect(page.locator('#view-title')).toHaveText('Documentos guiados');
  await page.locator('#doc-counterparty').fill('Contraparte Demo S.A.S.');
  await page.locator('#doc-object').fill('Prestación de servicios de prueba');
  await page.locator('#generate-doc').click();
  await expect(page.locator('#doc-preview')).not.toHaveClass(/hidden/);
  await expect(page.locator('#doc-preview')).toContainText('VISTA PREVIA FICTICIA');
  await expect(page.locator('#doc-preview')).toContainText('Contraparte Demo S.A.S.');
});

test('ticket demostrativo se crea solo en la sesión', async ({ page }) => {
  await enterDemo(page);
  await page.locator('#new-ticket').click();
  const modal = page.locator('#ticket-modal');
  await expect(modal).toHaveAttribute('open', '');
  await modal.locator('[name="subject"]').fill('Solicitud E2E');
  await modal.locator('[name="description"]').fill('Registro ficticio para validar el flujo de navegador.');
  await modal.getByRole('button', { name: 'Crear solicitud' }).click();
  await expect(modal.locator('.form-status')).toContainText('Solicitud ficticia creada');
  await expect(page.locator('#view-title')).toHaveText('Solicitudes', { timeout: 3_000 });
  await expect(page.locator('#ticket-rows')).toContainText('Solicitud E2E');
});
