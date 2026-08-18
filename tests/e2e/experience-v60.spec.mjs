import { test, expect, expectNoHorizontalOverflow, openHomeLegacy, openDetailLegacy, openSolutionLegacy } from './helpers.mjs';

function commercialSignature(href) {
  const url = new URL(href, 'https://meridiano.invalid/');
  return {
    intent: url.searchParams.get('commercial_intent'),
    modality: url.searchParams.get('modality'),
    proof: url.searchParams.get('proof_standard'),
    experience: url.searchParams.get('experience'),
    hash: url.hash,
  };
}

test('v6 Home empieza por la decisión y conserva una sola conversión física', async ({ page }) => {
  await page.goto('./');
  await expect(page.locator('body')).toHaveAttribute('data-experience-system', 'v6');
  await expect(page.locator('main[data-experience-v60="home"]')).toHaveCount(1);
  await expect(page.locator('#v6-home-title')).toContainText('Decisiones empresariales complejas');
  await expect(page.locator('#v6-situations .v6-index-row')).toHaveCount(6);
  await expect(page.locator('#contacto form#contact-form')).toHaveCount(1);
  await expect(page.locator('#contacto form#contact-form')).toBeVisible();

  const commercial = page.locator('#v6-commercial-depth');
  const legacy = page.locator('#v6-depth.v6-legacy-home');
  await expect(commercial).not.toHaveAttribute('open', '');
  await expect(legacy).not.toHaveAttribute('open', '');
  await expect(page.locator('.need-card')).toHaveCount(6);
  await expect(page.locator('.need-card').first()).not.toBeVisible();

  await openHomeLegacy(page);
  await expect(page.locator('.need-card').first()).toBeVisible();
  await expect(page.locator('[data-integral-v526="signal"]')).toBeVisible();
  await expectNoHorizontalOverflow(page);
});

test('v6 preserva continuidad comercial en producto y servicio visibles', async ({ page }) => {
  const cases = [
    ['./productos/programa-gobernanza-ia.html', { intent: 'proposal', modality: 'product' }],
    ['./servicios/tecnologia-inteligencia-artificial.html', { intent: 'scope', modality: 'specialist' }],
  ];

  for (const [path, expected] of cases) {
    await page.goto(path);
    await expect(page.locator('body')).toHaveAttribute('data-experience-wave', 'deep-offers');
    const primary = page.locator('a[data-experience-v60-cta="primary"]');
    await expect(primary).toBeVisible();
    const href = await primary.getAttribute('href');
    expect(href).toBeTruthy();
    expect(commercialSignature(href)).toEqual({
      intent: expected.intent,
      modality: expected.modality,
      proof: 'source',
      experience: 'v6',
      hash: '#contacto',
    });

    for (const role of ['header', 'journey', 'close']) {
      await expect(page.locator(`a[data-experience-v60-cta="${role}"]`)).toHaveAttribute('href', href);
    }

    const depth = page.locator('#v6-detail-depth.v6-detail-depth');
    await expect(depth).not.toHaveAttribute('open', '');
    await expect(page.locator('[data-decision-v58-cta="true"]')).not.toBeVisible();
    await openDetailLegacy(page);
    await expect(page.locator('[data-decision-v58-cta="true"]')).toBeVisible();
    await expect(page.locator('[data-buying-clarity-v58="true"]')).toBeVisible();
    await expect(page.locator('[data-offer-commercial-v530]')).toBeVisible();
    await expectNoHorizontalOverflow(page);
  }
});

test('v6 solución mantiene la decisión abierta y el soporte v5.31 bajo profundidad', async ({ page }) => {
  await page.goto('./soluciones/gobernar-inteligencia-artificial-empresa.html');
  await expect(page.locator('body')).toHaveAttribute('data-experience-wave', 'solutions');
  await expect(page.locator('#v6-solution-title')).toContainText('Gobernanza jurídica de inteligencia artificial');
  await expect(page.locator('#v6-solution-signals .v6-signal-row')).toHaveCount(4);
  await expect(page.locator('#v6-solution-routes .v6-route-option')).toHaveCount(3);
  await expect(page.locator('#v6-solution-result')).toBeVisible();
  await expect(page.locator('#v6-solution-pricing')).toBeVisible();
  await expect(page.locator('#v6-solution-boundary')).toBeVisible();

  const depth = page.locator('#v6-solution-depth.v6-solution-depth');
  await expect(depth).not.toHaveAttribute('open', '');
  await expect(page.locator('#ruta')).not.toBeVisible();
  await openSolutionLegacy(page);
  await expect(page.locator('#ruta')).toBeVisible();
  for (const key of ['objections', 'faq', 'related', 'proof']) {
    const historical = page.locator(`details[data-decision-compression-v531="solution-${key}"]`);
    await expect(historical).toHaveCount(1);
    await expect(historical).not.toHaveAttribute('open', '');
  }
  await expectNoHorizontalOverflow(page);
});

test('v6 sector y perspectiva usan jerarquías diferentes sin perder autoridad', async ({ page }) => {
  await page.goto('./sectores/tecnologia-software-ia.html');
  await expect(page.locator('body')).toHaveAttribute('data-experience-wave', 'sectors');
  await expect(page.locator('.v6-sector-decision-row')).toHaveCount(6);
  await expect(page.locator('a[data-authority-solution]')).toHaveCount(2);
  await expectNoHorizontalOverflow(page);

  await page.goto('./perspectivas/gobierno-juridico-inteligencia-artificial.html');
  await expect(page.locator('body')).toHaveAttribute('data-experience-wave', 'perspectives');
  const body = page.locator('article.article-body');
  await expect(body).toBeVisible();
  const insideDetails = await body.evaluate((node) => Boolean(node.closest('details')));
  expect(insideDetails).toBe(false);
  await expect(page.locator('.v6-reading-toc a')).toHaveCount(7);
  await expect(page.locator('a[data-authority-solution]')).toHaveCount(1);
  await expectNoHorizontalOverflow(page);
});

test('v6 hace explícita la frontera demostrativa sin crear capacidades reales', async ({ page }) => {
  await page.goto('./experiencia.html');
  await expect(page.locator('body')).toHaveAttribute('data-experience-surface', 'experience');
  await expect(page.locator('.v6-demo-boundary')).toBeVisible();
  await expect(page.locator('.v6-demo-boundary')).toContainText('no habilita un portal productivo');
  await expect(page.locator('#scope-simulator')).toHaveCount(1);

  await page.goto('./demo.html');
  await expect(page.locator('body')).toHaveAttribute('data-experience-surface', 'demo');
  await expect(page.locator('body')).toHaveAttribute('data-capability-v521', 'demo-only');
  await expect(page.locator('meta[name="robots"]')).toHaveAttribute('content', 'noindex,nofollow');
  await expect(page.locator('.v6-demo-boundary')).toContainText('sin usuarios, archivos ni operaciones reales');
  await expect(page.locator('#login-form')).toBeVisible();
  await expect(page.locator('#portal-view')).toHaveClass(/hidden/);
});

test('v6 mantiene contención móvil en las superficies representativas', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  for (const path of [
    './',
    './productos/programa-gobernanza-ia.html',
    './soluciones/gobernar-inteligencia-artificial-empresa.html',
    './sectores/tecnologia-software-ia.html',
    './perspectivas/gobierno-juridico-inteligencia-artificial.html',
  ]) {
    await page.goto(path);
    await expectNoHorizontalOverflow(page);
  }
});
