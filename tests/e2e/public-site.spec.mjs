import { test, expect, expectNoHorizontalOverflow, telemetrySnapshot, preventNavigationFor } from './helpers.mjs';

test('portada pública conserva rutas, profundidad y layout', async ({ page }) => {
  await page.goto('./');
  await expect(page).toHaveTitle(/Meridiano Legal/);
  await expect(page.getByRole('heading', { level: 1 })).toContainText('Dirección jurídica');
  await expect(page.locator('.need-card')).toHaveCount(6);
  await expect(page.locator('.full-detail-link')).toHaveCount(16);
  await expect(page.getByRole('link', { name: /Centro demo/i }).first()).toBeVisible();
  await expect(page.locator('[data-engagement-router-v58="true"]')).toBeVisible();
  await expect(page.locator('.engagement-router-card-v58')).toHaveCount(4);
  await expectNoHorizontalOverflow(page);

  await page.goto('./productos/programa-gobernanza-ia.html');
  await expect(page.locator('[data-buying-clarity-v58="true"]')).toBeVisible();
  await expect(page.locator('.buying-clarity-card-v58')).toHaveCount(5);
  await expect(page.locator('[data-decision-v58-cta="true"]')).toBeVisible();
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

  await page.goto('./productos/programa-gobernanza-ia.html');
  const proposalCta = page.locator('[data-decision-v58-cta="true"][data-close-intent-v510="proposal"]');
  await expect(proposalCta).toBeVisible();
  await expect(proposalCta).toHaveAttribute('href', /commercial_intent=proposal#contacto$/);
  await proposalCta.click();
  await expect(page).toHaveURL(/commercial_intent=proposal#contacto$/);

  const form = page.locator('form[data-contact-v49="true"]');
  await expect(form).toBeVisible();
  await expect(form).toHaveAttribute('data-commercial-intake-v59', 'true');
  await expect(form).toHaveAttribute('data-commercial-close-v510', 'true');
  await expect(form.locator('[data-qualification-v59="true"]')).toBeVisible();
  await expect(form.locator('[data-close-path-v510="true"]')).toBeVisible();
  await expect(form.locator('[name="need"]')).toHaveValue('Gobernanza de IA');
  await expect(form.locator('[name="decision_stage"]')).toHaveValue('Quiero recibir una propuesta');
  await expect(form).toHaveAttribute('data-close-route-v510', 'proposal');
  await expect(form.locator('[data-close-route-v510]')).toContainText('Ruta de propuesta');
  await expect.poll(async () => (await telemetrySnapshot(page)).some((event) =>
    event.name === 'close_intent_applied' && event.detail?.target === 'contact-form'
  )).toBe(true);

  await form.locator('[name="name"]').fill('Prueba E2E');
  await form.locator('[name="company"]').fill('Empresa de prueba');
  await form.locator('[name="email"]').fill('e2e@example.com');
  await form.locator('[name="urgency"]').selectOption({ label: 'En 2 a 4 semanas' });
  await form.locator('[name="budget"]').selectOption({ label: '$8 a $20 millones COP' });
  await form.locator('[name="message"]').fill('Necesitamos revisar el gobierno de un caso de uso de IA.');
  await form.locator('[name="privacy"]').check();

  await expect(form).toHaveAttribute('data-proposal-readiness', 'proposal_ready');
  await expect(form.locator('[data-qualification-next-step-v59]').first()).toContainText('Propuesta estructurada');
  await expect(form.locator('[data-qualification-context-v59]')).toContainText('Producto jurídico');
  await expectNoHorizontalOverflow(page);

  await page.waitForTimeout(900);
  await form.getByRole('button', { name: /Preparar solicitud de propuesta en WhatsApp/i }).click();
  const status = form.locator('.form-status');
  await expect(status).toContainText(/ML-\d{8}-[A-Z0-9]{5}/);
  await expect(form).toHaveAttribute('data-last-lead-reference', /ML-\d{8}-[A-Z0-9]{5}/);

  const opened = await page.evaluate(() => window.__meridianoOpenedUrls || []);
  expect(opened).toHaveLength(1);
  expect(opened[0]).toMatch(/^https:\/\/wa\.me\/573008507813\?text=/);
  const whatsappText = new URL(opened[0]).searchParams.get('text') || '';
  expect(whatsappText).toContain('Etapa de decisión: Quiero recibir una propuesta');
  expect(whatsappText).toContain('Horizonte comercial: En 2 a 4 semanas');
  expect(whatsappText).toContain('Presupuesto orientativo: $8 a $20 millones COP');
  expect(whatsappText).toContain('Siguiente paso sugerido: Propuesta estructurada');
  expect(page.url()).toMatch(/#contacto$/);

  const events = await telemetrySnapshot(page);
  expect(events).toContainEqual(expect.objectContaining({
    name: 'lead_prepared',
    detail: expect.objectContaining({ target: 'whatsapp' }),
  }));
  expect(events).toContainEqual(expect.objectContaining({
    name: 'close_handoff_prepared',
    detail: expect.objectContaining({ stage: 'proposal', target: 'whatsapp' }),
  }));
  const telemetryText = JSON.stringify(events);
  expect(telemetryText).not.toContain('Prueba E2E');
  expect(telemetryText).not.toContain('Empresa de prueba');
  expect(telemetryText).not.toContain('e2e@example.com');
  expect(telemetryText).not.toContain('Necesitamos revisar el gobierno');
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
  await form.locator('[name="decision_stage"]').selectOption({ label: 'Estoy explorando la necesidad' });
  await form.locator('[name="urgency"]').selectOption({ label: 'Sin fecha definida' });
  await form.locator('[name="privacy"]').check();
  await form.locator('[name="website"]').evaluate((node) => { node.value = 'https://spam.invalid'; });

  const need = form.locator('[name="need"]');
  if (await need.evaluate((node) => node.tagName) === 'SELECT') {
    await need.selectOption({ index: 1 });
  } else {
    await need.fill('Otra necesidad');
  }
  await page.waitForTimeout(900);
  await form.locator('button[type="submit"]').click();
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
