import { test, expect, expectNoHorizontalOverflow } from './helpers.mjs';

test('v5.28 acerca el contacto al cierre comercial sin eliminar profundidad', async ({ page }) => {
  await page.goto('./');

  const order = await page.locator('main > section').evaluateAll((sections) => sections.map((node) => node.id || node.getAttribute('data-integral-v526') || ''));
  const contracting = order.indexOf('contratacion');
  const contact = order.indexOf('contacto');
  const sectors = order.indexOf('sectores');
  const perspectives = order.indexOf('perspectivas');
  const firm = order.indexOf('firma');
  const faq = order.indexOf('preguntas');

  expect(contracting).toBeGreaterThan(-1);
  expect(contact).toBe(contracting + 1);
  expect(sectors).toBeGreaterThan(contact);
  expect(perspectives).toBeGreaterThan(sectors);
  expect(firm).toBeGreaterThan(perspectives);
  expect(faq).toBeGreaterThan(firm);

  const contactSection = page.locator('#contacto[data-conversion-path-v528="true"]');
  await expect(contactSection).toHaveCount(1);
  await expect(contactSection.locator('[data-conversion-readiness-v528="true"]')).toHaveCount(1);
  await expect(contactSection.locator('.contact-readiness-items-v528 > span')).toHaveCount(3);
  await expect(page.locator('.contact-prelude')).toHaveCount(0);
  await expect(page.locator('form#contact-form')).toHaveCount(1);
  await expect(contactSection.locator('[data-contact-synthesis-v523="true"]')).toHaveCount(1);
  await expect(contactSection.locator('details[data-contact-process-v523="true"]')).toHaveCount(1);

  for (const [selector, label] of [
    ['.contact-readiness-items-v528', 'Datos mínimos de la solicitud'],
    ['.contact-synthesis-grid-v523', 'Síntesis de la solicitud'],
    ['.contact-brief-grid-v523', 'Modalidad y estándar de trabajo'],
  ]) {
    const region = contactSection.locator(selector);
    await expect(region).toHaveAttribute('tabindex', '0');
    await expect(region).toHaveAttribute('role', 'region');
    await expect(region).toHaveAttribute('aria-label', label);
    await region.focus();
    await expect(region).toBeFocused();
  }

  const depth = page.locator('[data-conversion-depth-v528="true"]');
  await expect(depth).toHaveCount(1);
  await expect(depth.locator('a[href="#sectores"]')).toHaveCount(1);
  await expect(depth.locator('a[href="#perspectivas"]')).toHaveCount(1);
  await expect(depth.locator('a[href="#firma"]')).toHaveCount(1);
  await expect(depth.locator('a[href="#preguntas"]')).toHaveCount(1);

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
