import { test, expect, expectNoHorizontalOverflow } from './helpers.mjs';

test('portada v5.22 diferencia necesidad, modalidad, servicios y productos sin duplicar selector', async ({ page }) => {
  await page.goto('./');

  await expect(page.locator('[data-home-narrative-v522="true"]')).toHaveCount(1);
  await expect(page.getByRole('heading', { level: 1 })).toContainText('decisiones que deben avanzar');
  await expect(page.getByText('CÓMO SE VE EL CRITERIO SENIOR')).toBeVisible();
  await expect(page.locator('[data-home-decision-v520="true"]')).toHaveCount(1);
  await expect(page.locator('#elegir')).toHaveCount(0);
  await expect(page.locator('#servicios h2')).toContainText('criterio adaptable');
  await expect(page.locator('#productos h2')).toContainText('perímetro, entregables y cierre definidos');
  await expectNoHorizontalOverflow(page);
});

test('fichas v5.22 explican decisión, modalidad, lente jurídica y alternativa cercana', async ({ page }) => {
  await page.goto('./productos/programa-gobernanza-ia.html');
  const ai = page.locator('[data-offer-narrative-v522="product-ai"]');
  await expect(ai).toHaveCount(1);
  await expect(ai.locator('.offer-positioning-card-v522')).toHaveCount(3);
  await expect(ai.getByText('CAPACIDAD QUE QUEDA INSTALADA')).toBeVisible();
  await ai.locator('summary').click();
  await expect(ai.locator('.offer-legal-lens-grid-v522 article')).toHaveCount(3);
  await expect(ai.getByText('CONPES 4144 de 2025')).toBeVisible();
  await expect(ai.getByRole('link', { name: /comparar alternativa/i })).toHaveAttribute('href', '../servicios/tecnologia-inteligencia-artificial.html');
  await expect(page.locator('#detail-page')).not.toContainText('Meridiano Empresas');
  await expectNoHorizontalOverflow(page);

  await page.goto('./servicios/contratacion-estrategica.html');
  const contracts = page.locator('[data-offer-narrative-v522="service-contracts"]');
  await expect(contracts).toHaveCount(1);
  await expect(contracts).toContainText('Sistema Contractual Empresarial');
  await expect(contracts.getByRole('link', { name: /comparar alternativa/i })).toHaveAttribute('href', '../productos/sistema-contractual-empresarial.html');
  await expectNoHorizontalOverflow(page);
});
