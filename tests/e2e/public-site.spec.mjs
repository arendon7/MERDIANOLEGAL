import { test, expect, expectNoHorizontalOverflow, preventNavigationFor, telemetrySnapshot } from './helpers.mjs';

test('portada pública conserva rutas, profundidad y layout', async ({ page }) => {
  await page.goto('./');
  await expect(page.locator('header.site-header')).toBeVisible();
  await expect(page.locator('main')).toBeVisible();
  await expect(page.locator('#necesidades')).toBeVisible();
  await expect(page.locator('#servicios')).toBeVisible();
  await expect(page.locator('#productos')).toBeVisible();
  await expect(page.locator('#honorarios')).toBeVisible();
  await expect(page.locator('#contacto')).toBeVisible();
  await expectNoHorizontalOverflow(page);
});

test('ruta de necesidad abre una solución indexable', async ({ page }) => {
  await page.goto('./');
  const route = page.locator('.need-card').filter({ hasText: 'Gobernar el uso de IA' });
  await expect(route).toBeVisible();
  await route.click();
  await expect(page).toHaveURL(/soluciones\/gobernar-inteligencia-artificial-empresa\.html$/);
  await expect(page.getByRole('heading', { level: 1 })).toContainText('Gobernanza jurídica de inteligencia artificial');
  await expect(page.locator('script[data-authority-v53="item-list"]')).toHaveCount(1);
  await expectNoHorizontalOverflow(page);
});

test('solución registra vista y apertura de FAQ sin PII', async ({ page }) => {
  await page.goto('./soluciones/gobernar-inteligencia-artificial-empresa.html');
  await expect.poll(async () => (await telemetrySnapshot(page)).some((event) =>
    event.name === 'solution_view' && event.detail?.target === 'solution:gobernar-inteligencia-artificial-empresa'
  )).toBe(true);

  const faqDepth = page.locator('details[data-decision-compression-v531="solution-faq"]');
  await expect(faqDepth).toHaveCount(1);
  await expect(faqDepth).not.toHaveAttribute('open', '');
  const faqDepthSummary = faqDepth.locator(':scope > summary');
  await expect(faqDepthSummary).toHaveCount(1);
  await faqDepthSummary.click();
  await expect(faqDepth).toHaveAttribute('open', '');

  const faq = page.locator('.cro-faq-v52 details').first();
  await expect(faq).toBeVisible();
  await faq.locator(':scope > summary').click();
  await expect(faq).toHaveAttribute('open', '');
  await expect.poll(async () => (await telemetrySnapshot(page)).some((event) =>
    event.name === 'faq_open' && event.detail?.target === 'faq:1'
  )).toBe(true);

  const contract = await page.evaluate(() => window.MeridianoMeasurementV53);
  expect(contract).toEqual(expect.objectContaining({
    version: '5.3.0',
    piiAllowed: false,
    networkTransport: false,
    persistentStorage: false,
  }));
});

test('perspectiva y sector conectan autoridad con solución', async ({ page }) => {
  await page.goto('./perspectivas/gobierno-juridico-inteligencia-artificial.html');
  const perspectiveRoute = page.locator('a[data-authority-solution]').first();
  await expect(perspectiveRoute).toHaveAttribute('href', /soluciones\/gobernar-inteligencia-artificial-empresa\.html/);
  await preventNavigationFor(perspectiveRoute);
  await perspectiveRoute.click();
  await expect.poll(async () => (await telemetrySnapshot(page)).some((event) =>
    event.name === 'authority_open' && event.detail?.target === 'solution:gobernar-inteligencia-artificial-empresa'
  )).toBe(true);

  await page.goto('./sectores/tecnologia-software-ia.html');
  await expect(page.locator('a[data-authority-solution]')).toHaveCount(2);
  await expect(page.locator('a[data-authority-solution="gobernar-inteligencia-artificial-empresa"]')).toBeVisible();
  await expectNoHorizontalOverflow(page);
});

test('formulario prepara WhatsApp sin enviar ni salir de la web', async ({ page }) => {
  await page.goto('./');
  await page.locator('#contacto').scrollIntoViewIfNeeded();

  const form = page.locator('#contact-form');
  await form.locator('[name="nombre"]').fill('QA Meridiano');
  await form.locator('[name="empresa"]').fill('Empresa QA');
  await form.locator('[name="email"]').fill('qa@example.com');
  await form.locator('[name="telefono"]').fill('3001234567');
  await form.locator('[name="mensaje"]').fill('Necesito revisar una situación jurídica empresarial.');

  await form.getByRole('button', { name: /preparar whatsapp/i }).click();
  const handoff = page.locator('[data-handoff-v517="true"]');
  await expect(handoff).toBeVisible();
  await expect(page).toHaveURL(/MERDIANOLEGAL\/?(?:#.*)?$/);
});

test('honeypot bloquea preparación automatizada', async ({ page }) => {
  await page.goto('./');
  const form = page.locator('#contact-form');
  await form.locator('[name="nombre"]').fill('Bot QA');
  await form.locator('[name="empresa"]').fill('Bot Corp');
  await form.locator('[name="email"]').fill('bot@example.com');
  await form.locator('[name="telefono"]').fill('3001234567');
  await form.locator('[name="mensaje"]').fill('Automatización de prueba.');
  const honey = form.locator('[name="website"]');
  await honey.fill('https://spam.invalid');
  await form.getByRole('button', { name: /preparar whatsapp/i }).click();
  await expect(page.locator('[data-handoff-v517="true"]')).toHaveCount(0);
});

test('menú móvil abre, cierra con Escape y devuelve el foco', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('./');
  const toggle = page.locator('[data-nav-toggle]');
  await toggle.click();
  await expect(toggle).toHaveAttribute('aria-expanded', 'true');
  await page.keyboard.press('Escape');
  await expect(toggle).toHaveAttribute('aria-expanded', 'false');
  await expect(toggle).toBeFocused();
});