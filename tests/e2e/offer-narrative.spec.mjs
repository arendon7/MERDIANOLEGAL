import { test, expect, expectNoHorizontalOverflow, openHomeLegacy, openDetailLegacy } from './helpers.mjs';

test('v6 Home conserva narrativa v5.22 completa bajo profundidad sin duplicar selector', async ({ page }) => {
  await page.goto('./');
  await expect(page.locator('#v6-home-title')).toContainText('Decisiones empresariales complejas');
  await expect(page.locator('[data-home-narrative-v522="true"]')).toHaveCount(1);
  await expect(page.locator('[data-home-narrative-v522="true"]')).not.toBeVisible();

  await openHomeLegacy(page);
  const legacy = page.locator('#v6-depth');
  await expect(legacy.getByText('CÓMO SE VE EL CRITERIO SENIOR')).toBeVisible();
  await expect(legacy.locator('[data-home-decision-v520="true"]')).toHaveCount(1);
  await expect(legacy.locator('#elegir')).toHaveCount(0);
  await expect(legacy.locator('#servicios h2')).toContainText('criterio adaptable');
  await expect(legacy.locator('#productos h2')).toContainText('perímetro, entregables y cierre definidos');
  await expectNoHorizontalOverflow(page);
});

test('fichas v5.22 explican decisión, modalidad, lente jurídica y alternativa cercana dentro de profundidad v6', async ({ page }) => {
  await page.goto('./productos/programa-gobernanza-ia.html');
  await openDetailLegacy(page);
  const depth = page.locator('details[data-decision-compression-v531="offer-narrative"]');
  const ai = page.locator('[data-offer-narrative-v522="product-ai"]');
  await expect(depth).toHaveCount(1);
  await expect(depth).not.toHaveAttribute('open', '');
  await expect(ai).toHaveCount(1);
  await expect(ai.locator('.offer-positioning-card-v522')).toHaveCount(3);
  await expect(ai).toContainText('CAPACIDAD QUE QUEDA INSTALADA');

  const depthSummary = depth.locator(':scope > summary');
  await depthSummary.focus();
  await expect(depthSummary).toBeFocused();
  await depthSummary.press('Enter');
  await expect(depth).toHaveAttribute('open', '');
  await expect(ai.getByText('CAPACIDAD QUE QUEDA INSTALADA')).toBeVisible();

  await ai.locator('summary').click();
  await expect(ai.locator('.offer-legal-lens-grid-v522 article')).toHaveCount(3);
  await expect(ai.getByText('CONPES 4144 de 2025')).toBeVisible();
  await expect(ai.getByRole('link', { name: /comparar alternativa/i })).toHaveAttribute('href', '../servicios/tecnologia-inteligencia-artificial.html');
  await expect(page.locator('#detail-page')).toContainText('Meridiano Empresas cuando esté habilitado productivamente');
  await expect(page.locator('#detail-page')).not.toContainText('Meridiano Empresas o Microsoft 365');
  await expect(page.locator('#detail-page a[href="../demo.html"]')).toHaveCount(0);
  await expectNoHorizontalOverflow(page);

  await page.goto('./servicios/contratacion-estrategica.html');
  await openDetailLegacy(page);
  const serviceDepth = page.locator('details[data-decision-compression-v531="offer-narrative"]');
  const contracts = page.locator('[data-offer-narrative-v522="service-contracts"]');
  await expect(serviceDepth).toHaveCount(1);
  await expect(serviceDepth).not.toHaveAttribute('open', '');
  await expect(contracts).toHaveCount(1);
  await expect(contracts).toContainText('Sistema Contractual Empresarial');
  const serviceDepthSummary = serviceDepth.locator(':scope > summary');
  await serviceDepthSummary.focus();
  await expect(serviceDepthSummary).toBeFocused();
  await serviceDepthSummary.press('Enter');
  await expect(serviceDepth).toHaveAttribute('open', '');
  await expect(contracts.getByRole('link', { name: /comparar alternativa/i })).toHaveAttribute('href', '../productos/sistema-contractual-empresarial.html');
  await expectNoHorizontalOverflow(page);
});