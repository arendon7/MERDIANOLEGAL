import { test, expect, expectNoHorizontalOverflow, openHomeLegacy } from './helpers.mjs';

test('v6 acerca el contacto después de oferta y contratación sin eliminar profundidad v5.28', async ({ page }) => {
  await page.goto('./');

  const order = await page.locator('main > :is(section,details)').evaluateAll((nodes) => nodes.map((node) => node.id || ''));
  const offer = order.indexOf('v6-offer');
  const contracting = order.indexOf('v6-commercial-depth');
  const contact = order.indexOf('contacto');
  const legacy = order.indexOf('v6-depth');
  expect(offer).toBeGreaterThan(-1);
  expect(contracting).toBeGreaterThan(offer);
  expect(contact).toBeGreaterThan(contracting);
  expect(legacy).toBeGreaterThan(contact);

  const contactSection = page.locator('#contacto[data-conversion-path-v528="true"]');
  await expect(contactSection).toHaveCount(1);
  await expect(contactSection.locator('[data-conversion-readiness-v528="true"]')).toHaveCount(1);
  await expect(contactSection.locator('.contact-readiness-items-v528 > span')).toHaveCount(3);
  await expect(page.locator('.contact-prelude')).toHaveCount(0);
  await expect(page.locator('form#contact-form')).toHaveCount(1);
  await expect(contactSection.locator('[data-contact-synthesis-v523="true"]')).toHaveCount(1);
  await expect(contactSection.locator('details[data-contact-process-v523="true"]')).toHaveCount(1);

  const readiness = contactSection.locator('.contact-readiness-items-v528');
  await expect(readiness).toHaveAttribute('tabindex', '0');
  await expect(readiness).toHaveAttribute('role', 'region');
  await expect(readiness).toHaveAttribute('aria-label', 'Datos mínimos de la solicitud');
  await readiness.focus();
  await expect(readiness).toBeFocused();

  for (const [selector, label] of [
    ['.contact-synthesis-grid-v523', 'Síntesis de la solicitud'],
    ['.contact-brief-grid-v523', 'Modalidad y estándar de trabajo'],
  ]) {
    const deck = contactSection.locator(selector);
    await expect(deck).toHaveAttribute('tabindex', '0');
    await expect(deck).toHaveAttribute('aria-label', label);
    await expect(deck).not.toHaveAttribute('role', 'region');
    expect(await deck.evaluate((node) => node.tagName)).toBe('DL');
    await deck.focus();
    await expect(deck).toBeFocused();
  }

  const historicalDepth = page.locator('[data-conversion-depth-v528="true"]');
  await expect(historicalDepth).toHaveCount(1);
  await expect(historicalDepth).not.toBeVisible();
  await openHomeLegacy(page);
  await expect(historicalDepth).toBeVisible();
  await expect(historicalDepth.locator('a[href="#sectores"]')).toHaveCount(1);
  await expect(historicalDepth.locator('a[href="#perspectivas"]')).toHaveCount(1);
  await expect(historicalDepth.locator('a[href="#firma"]')).toHaveCount(1);
  await expect(historicalDepth.locator('a[href="#preguntas"]')).toHaveCount(1);

  await expectNoHorizontalOverflow(page);
});

test('v5.28 contiene la síntesis comercial dentro del viewport móvil', async ({ page }) => {
  await page.goto('./#contacto');
  const width = await page.evaluate(() => window.innerWidth);

  if (width <= 620) {
    for (const selector of ['.contact-synthesis-grid-v523', '.contact-brief-grid-v523']) {
      const deck = page.locator(selector);
      await expect(deck).toHaveCount(1);
      const metrics = await deck.evaluate((node) => ({
        clientWidth: node.clientWidth,
        scrollWidth: node.scrollWidth,
        children: node.children.length,
      }));
      expect(metrics.children).toBeGreaterThan(1);
      expect(metrics.scrollWidth).toBeGreaterThan(metrics.clientWidth + 20);
      await deck.focus();
      await expect(deck).toBeFocused();
    }
  }

  const process = page.locator('details[data-contact-process-v523="true"]');
  await expect(process).not.toHaveAttribute('open', '');
  await expectNoHorizontalOverflow(page);
});
