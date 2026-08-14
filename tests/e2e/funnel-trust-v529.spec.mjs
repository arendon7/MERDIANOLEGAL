import { test, expect, expectNoHorizontalOverflow } from './helpers.mjs';

test('v5.29 coloca confianza verificable sin romper la secuencia v5.28', async ({ page }) => {
  await page.goto('./');

  const trust = page.locator('aside[data-funnel-trust-v529="true"]');
  await expect(trust).toHaveCount(1);
  await expect(page.locator('#contratacion + aside[data-funnel-trust-v529="true"]')).toHaveCount(1);
  await expect(page.locator('aside[data-funnel-trust-v529="true"] + #contacto')).toHaveCount(1);
  await expect(trust.getByText('Abogado · Universidad EAFIT')).toHaveCount(1);
  await expect(trust.getByText('Director Jurídico y Administrativo')).toHaveCount(1);
  await expect(trust.getByRole('link', { name: /Ver trayectoria completa/ })).toHaveAttribute('href', 'firma.html#trayectoria');

  const evidence = trust.locator('.decision-trust-evidence-v529');
  await expect(evidence).toHaveAttribute('tabindex', '0');
  await expect(evidence).toHaveAttribute('role', 'region');
  await evidence.focus();
  await expect(evidence).toBeFocused();

  const sectionOrder = await page.locator('main > section').evaluateAll((sections) => sections.map((node) => node.id || ''));
  expect(sectionOrder.indexOf('contacto')).toBe(sectionOrder.indexOf('contratacion') + 1);
  await expectNoHorizontalOverflow(page);
});

test('v5.29 observa el funnel en memoria sin capturar contenido del formulario', async ({ page }) => {
  await page.goto('./');
  await expect.poll(() => page.evaluate(() => Boolean(window.MeridianoFunnelV529))).toBe(true);

  const api = await page.evaluate(() => ({
    version: window.MeridianoFunnelV529.version,
    privacy: window.MeridianoFunnelV529.privacy,
    limits: window.MeridianoFunnelV529.semanticLimits,
  }));
  expect(api.version).toBe('5.29.0');
  expect(api.privacy.piiAllowed).toBe(false);
  expect(api.privacy.formContentAllowed).toBe(false);
  expect(api.privacy.persistentStorage).toBe(false);
  expect(api.privacy.crossSessionIdentifier).toBe(false);
  expect(api.privacy.networkTransportIntroduced).toBe(false);
  expect(Object.values(api.limits).every((value) => value === false)).toBe(true);

  for (const selector of ['#necesidades', '#servicios', '#contratacion', '#contacto']) {
    await page.locator(selector).scrollIntoViewIfNeeded();
    await page.waitForTimeout(120);
  }

  const sentinel = 'PII-V529-NO-CAPTURAR-7421';
  const message = page.locator('#contact-form textarea[name="message"]');
  if (await message.count()) await message.fill(sentinel);
  await page.locator('#contacto').scrollIntoViewIfNeeded();
  await page.waitForTimeout(120);

  const snapshot = await page.evaluate(() => window.MeridianoFunnelV529.snapshot());
  const stages = snapshot.milestones.map((item) => item.stage);
  expect(stages).toContain('awareness');
  expect(stages).toContain('need');
  expect(stages).toContain('offer');
  expect(stages).toContain('decision');
  expect(stages).toContain('contact');
  expect(snapshot.furthestStage).toBe('contact');
  expect(snapshot.events.length).toBeLessThanOrEqual(48);
  expect(JSON.stringify(snapshot)).not.toContain(sentinel);
  expect(JSON.stringify(snapshot)).not.toMatch(/name=|email=|phone=|message=/i);
});

test('v5.29 reconoce una ficha profunda como oferta sin afirmar conversión', async ({ page }) => {
  await page.goto('./servicios/diagnostico-juridico-empresarial.html');
  await expect.poll(() => page.evaluate(() => Boolean(window.MeridianoFunnelV529))).toBe(true);
  await expect.poll(() => page.evaluate(() => window.MeridianoFunnelV529.snapshot().milestones.some((item) => item.stage === 'offer'))).toBe(true);

  const snapshot = await page.evaluate(() => window.MeridianoFunnelV529.snapshot());
  const offer = snapshot.milestones.find((item) => item.stage === 'offer');
  expect(offer.event).toBe('funnel_checkpoint');
  expect(offer.target).toBe('offer:service-diagnostic');
  expect(snapshot.milestones.some((item) => item.stage === 'handoff')).toBe(false);
});
