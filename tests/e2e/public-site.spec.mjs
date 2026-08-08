import { test, expect, expectNoHorizontalOverflow, telemetrySnapshot, preventNavigationFor } from './helpers.mjs';

test('portada pública conserva rutas, profundidad y layout', async ({ page }) => {
  await page.goto('./');
  await expect(page).toHaveTitle(/Meridiano Legal/);
  await expect(page.getByRole('heading', { level: 1 })).toContainText('Dirección jurídica');
  await expect(page.locator('.need-card')).toHaveCount(6);
  await expect(page.locator('.full-detail-link')).toHaveCount(16);
  await expect(page.getByRole('link', { name: /Centro demo/i }).first()).toBeVisible();
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

  const faq = page.locator('.cro-faq-v52 details').first();
  await expect(faq).toBeVisible();
  await faq.locator('summary').click();
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
  await page.addInitScript(() => {
    window.__meridianoOpenedUrls = [];
    window.open = (url) => {
      window.__meridianoOpenedUrls.push(String(url));
      return { closed: false };
    };
  });
  await page.goto('./#contacto');
  const form = page.locator('form[data-contact-v49="true"]');
  await expect(form).toBeVisible();
  await form.locator('[name="name"]').fill('Prueba E2E');
  await form.locator('[name="company"]').fill('Empresa de prueba');
  await form.locator('[name="email"]').fill('e2e@example.com');

  const need = form.locator('[name="need"]');
  const needTag = await need.evaluate((node) => node.tagName);
  if (needTag === 'SELECT') {
    const options = await need.locator('option').count();
    await need.selectOption({ index: Math.min(1, Math.max(0, options - 1)) });
  } else {
    await need.fill('Gobernanza de IA');
  }
  await form.locator('[name="message"]').fill('Necesitamos revisar el gobierno de un caso de uso de IA.');

  await page.waitForTimeout(900);
  await form.getByRole('button', { name: /Abrir solicitud en WhatsApp/i }).click();
  const status = form.locator('.form-status');
  await expect(status).toContainText(/ML-\d{8}-[A-Z0-9]{5}/);
  await expect(form).toHaveAttribute('data-last-lead-reference', /ML-\d{8}-[A-Z0-9]{5}/);

  const opened = await page.evaluate(() => window.__meridianoOpenedUrls || []);
  expect(opened).toHaveLength(1);
  expect(opened[0]).toMatch(/^https:\/\/wa\.me\/573008507813\?text=/);
  expect(page.url()).toMatch(/#contacto$/);

  const events = await telemetrySnapshot(page);
  expect(events).toContainEqual(expect.objectContaining({
    name: 'lead_prepared',
    detail: expect.objectContaining({ target: 'whatsapp' }),
  }));
});

test('honeypot bloquea preparación automatizada', async ({ page }) => {
  await page.addInitScript(() => {
    window.__meridianoOpenedUrls = [];
    window.open = (url) => {
      window.__meridianoOpenedUrls.push(String(url));
      return { closed: false };
    };
  });
  await page.goto('./#contacto');
  const form = page.locator('form[data-contact-v49="true"]');
  await form.locator('[name="name"]').fill('Bot de prueba');
  await form.locator('[name="email"]').fill('bot@example.com');
  await form.locator('[name="message"]').fill('Intento automatizado de prueba.');
  await form.locator('[name="website"]').evaluate((node) => { node.value = 'https://spam.invalid'; });

  const need = form.locator('[name="need"]');
  if (await need.evaluate((node) => node.tagName) === 'SELECT') {
    await need.selectOption({ index: 1 });
  } else {
    await need.fill('Otra necesidad');
  }
  await page.waitForTimeout(900);
  await form.getByRole('button', { name: /Abrir solicitud en WhatsApp/i }).click();
  await expect(form.locator('.form-status')).toContainText('No fue posible preparar la solicitud');
  expect(await page.evaluate(() => window.__meridianoOpenedUrls || [])).toHaveLength(0);
});

test('menú móvil abre, cierra con Escape y devuelve el foco', async ({ page }, testInfo) => {
  test.skip(!testInfo.project.name.includes('mobile'), 'Control específico de viewport móvil');
  await page.goto('./');
  const toggle = page.locator('.menu-toggle');
  const nav = page.locator('.main-nav');
  await expect(toggle).toBeVisible();
  await toggle.click();
  await expect(toggle).toHaveAttribute('aria-expanded', 'true');
  await expect(nav).toHaveClass(/open/);
  await expect(page.locator('body')).toHaveClass(/menu-open/);
  await page.keyboard.press('Escape');
  await expect(toggle).toHaveAttribute('aria-expanded', 'false');
  await expect(toggle).toBeFocused();
  await expectNoHorizontalOverflow(page);
});
