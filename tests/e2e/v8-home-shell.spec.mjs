import { test, expect, expectNoHorizontalOverflow } from './helpers.mjs';

const preview = './.w5-preview/index.html';
const expectedSections = Array.from({ length: 12 }, (_, index) => `H${String(index + 1).padStart(2, '0')}`);

async function openPreview(page) {
  const response = await page.goto(preview);
  expect(response?.status()).toBe(200);
  await expect(page.locator('html')).toHaveAttribute('data-v8-home-preview', 'true');
}

test('W5 Home preview materializa H01-H12 sin activar producción ni duplicar contacto', async ({ page }) => {
  await openPreview(page);

  await expect(page.locator('meta[name="robots"]')).toHaveAttribute('content', 'noindex,nofollow');
  await expect(page.locator('link[rel="canonical"]')).toHaveCount(0);
  await expect(page.locator('h1')).toHaveCount(1);
  await expect(page.locator('h1')).toHaveText('Derecho empresarial para decisiones que necesitan avanzar.');
  await expect(page.locator('form')).toHaveCount(0);

  const sections = await page.locator('[data-v8-home-section]').evaluateAll((nodes) =>
    nodes.map((node) => node.getAttribute('data-v8-home-section'))
  );
  expect(sections).toEqual(expectedSections);

  await expect(page.locator('[data-v8-home-section="H04"]')).toContainText('Meridiano Contratos');
  await expect(page.locator('[data-v8-home-section="H04"]')).toContainText('futuras generaciones');
  await expect(page.locator('[data-v8-home-section="H04"]')).toContainText('revisión jurídica humana');
  await expect(page.locator('a[href*="meridiano-contratos"]')).toHaveCount(0);

  const direction = page.locator('[data-v8-home-section="H08"]');
  for (const label of ['Cobertura', 'Complejidad', 'Prioridad', 'SLA / nivel de servicio', 'Gobierno y reporting']) {
    await expect(direction).toContainText(label);
  }
  const directionText = (await direction.innerText()).toLowerCase();
  expect(directionText).not.toContain('10 horas al mes');
  expect(directionText).not.toContain('20 horas al mes');
  expect(directionText).not.toContain('40 horas al mes');
  expect(directionText).not.toContain('bolsa mensual de horas');

  await expectNoHorizontalOverflow(page, 1);
});

test('W5 shell opera por teclado y mantiene RC02 como capability no enlazada', async ({ page }, testInfo) => {
  await openPreview(page);
  const mobile = testInfo.project.name === 'chromium-mobile';
  const menuToggle = page.locator('[data-ml-menu-toggle]');
  const navPanel = page.locator('[data-ml-nav-panel]');
  const megaToggle = page.locator('[data-ml-mega-toggle]');
  const mega = page.locator('[data-ml-mega]');

  if (mobile) {
    await expect(menuToggle).toBeVisible();
    await menuToggle.focus();
    await page.keyboard.press('Enter');
    await expect(menuToggle).toHaveAttribute('aria-expanded', 'true');
    await expect(navPanel).toBeVisible();
    await expect(page.locator('body')).toHaveClass(/ml-nav-open/);
  } else {
    await expect(menuToggle).toBeHidden();
    await expect(navPanel).toBeVisible();
  }

  await megaToggle.focus();
  await page.keyboard.press('Enter');
  await expect(megaToggle).toHaveAttribute('aria-expanded', 'true');
  await expect(mega).toBeVisible();

  const rc02 = mega.locator('[data-ml-item-id="RC02"]');
  await expect(rc02).toHaveCount(1);
  await expect(rc02).toHaveAttribute('data-ml-capability-status', 'owner-confirmed');
  expect(await rc02.evaluate((node) => node.tagName)).toBe('SPAN');
  await expect(rc02.locator('a')).toHaveCount(0);

  await page.keyboard.press('Escape');
  await expect(mega).toBeHidden();
  await expect(megaToggle).toHaveAttribute('aria-expanded', 'false');
  await expect(megaToggle).toBeFocused();

  if (mobile) {
    await page.keyboard.press('Escape');
    await expect(navPanel).toBeHidden();
    await expect(menuToggle).toHaveAttribute('aria-expanded', 'false');
    await expect(page.locator('body')).not.toHaveClass(/ml-nav-open/);
    await expect(menuToggle).toBeFocused();
  }
});

test('W5 mobile mantiene targets táctiles y navegación sin overflow', async ({ page }, testInfo) => {
  test.skip(testInfo.project.name !== 'chromium-mobile', 'Contrato específico de mobile');
  await openPreview(page);

  const menuToggle = page.locator('[data-ml-menu-toggle]');
  await menuToggle.click();
  const targets = page.locator('[data-ml-nav-panel] a[href], [data-ml-nav-panel] button:not([hidden])');
  const count = await targets.count();
  expect(count).toBeGreaterThan(8);
  for (let index = 0; index < count; index += 1) {
    const target = targets.nth(index);
    if (!(await target.isVisible())) continue;
    const box = await target.boundingBox();
    expect(box, `target ${index} without box`).toBeTruthy();
    expect(box.height, `target ${index} height`).toBeGreaterThanOrEqual(44);
  }
  await expectNoHorizontalOverflow(page, 1);
});

test('W5 CTA conserva un único formulario físico en el Home canónico', async ({ page }) => {
  await openPreview(page);
  const cta = page.locator('[data-v8-home-section="H01"] a[href$="index.html#contacto"]').first();
  await expect(cta).toHaveCount(1);
  const href = await cta.getAttribute('href');
  expect(href).toBe('../index.html#contacto');

  const response = await page.goto('../index.html#contacto');
  expect(response?.status()).toBe(200);
  await expect(page.locator('#contacto')).toHaveCount(1);
  await expect(page.locator('#contact-form')).toHaveCount(1);
});

test('W5 preview respeta reduced motion sin romper navegación', async ({ page }) => {
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await openPreview(page);
  const megaToggle = page.locator('[data-ml-mega-toggle]');
  if (await page.locator('[data-ml-menu-toggle]').isVisible()) {
    await page.locator('[data-ml-menu-toggle]').click();
  }
  await megaToggle.click();
  await expect(page.locator('[data-ml-mega]')).toBeVisible();
  await page.keyboard.press('Escape');
  await expect(page.locator('[data-ml-mega]')).toBeHidden();
  await expectNoHorizontalOverflow(page, 1);
});
