import { test, expect } from './helpers.mjs';

const SURFACES = [
  {
    route: 'index.html',
    selector: '[data-v7-legal-intelligence-discovery="home"]',
    child: '[data-v7-li-discovery]',
    count: 4,
  },
  {
    route: 'soluciones/index.html',
    selector: '[data-v7-legal-intelligence-discovery="hub"]',
    child: '[data-v7-li-area="true"]',
    count: 3,
  },
  {
    route: 'soluciones/ordenar-operacion-juridica.html',
    selector: '[data-v7-legal-intelligence="prototype"]',
    child: '[data-v7-intervention]',
    count: 3,
  },
  {
    route: 'servicios/legal-operations.html',
    selector: '[data-v7-deep-offer="legal-ai-transformation"]',
  },
  {
    route: 'productos/sistema-contractual-empresarial.html',
    selector: '[data-v7-deep-offer="contract-control"]',
  },
  {
    route: 'soluciones/gobernar-inteligencia-artificial-empresa.html',
    selector: '[data-v7-ai-governance-360="route"]',
    child: '[data-v7-ai-governance-stage]',
    count: 3,
  },
  {
    route: 'productos/programa-gobernanza-ia.html',
    selector: '[data-v7-ai-governance-deep="ai-governance-implementation"]',
  },
  {
    route: 'servicios/tecnologia-inteligencia-artificial.html',
    selector: '[data-v7-ai-governance-deep="ai-governance-readiness-managed"]',
  },
  {
    route: 'soluciones/estructurar-proyecto-regulado.html',
    selector: '[data-v7-regulatory-control="route"]',
    child: '[data-v7-regulatory-stage]',
    count: 3,
  },
  {
    route: 'productos/proyecto-regulado-estructurado.html',
    selector: '[data-v7-regulatory-deep="regulatory-control-implementation"]',
  },
  {
    route: 'servicios/proyectos-regulados.html',
    selector: '[data-v7-regulatory-deep="regulatory-control-managed"]',
  },
];

const SIX_CANONICAL_ROUTES = [
  'ordenar-riesgo-juridico-empresa.html',
  'direccion-juridica-externa-empresa.html',
  'gobernar-inteligencia-artificial-empresa.html',
  'preparar-empresa-para-inversion.html',
  'estructurar-proyecto-regulado.html',
  'ordenar-operacion-juridica.html',
];

test('v7 materializa las 11 superficies Legal Intelligence con boundaries visibles', async ({ page }) => {
  for (const surface of SURFACES) {
    await page.goto(`./${surface.route}`);
    const section = page.locator(surface.selector);
    await expect(section).toHaveCount(1);
    await expect(section).toBeVisible();
    await expect(section.locator('[data-v7-capability-boundary="true"]')).toHaveCount(1);
    await expect(section.locator('[data-v7-capability-boundary="true"]')).toBeVisible();
    if (surface.child) {
      await expect(section.locator(surface.child)).toHaveCount(surface.count);
    }
  }
});

test('v7 conserva las seis rutas de decisión y no expone Meridiano Counsel', async ({ page }) => {
  await page.goto('./soluciones/index.html');
  const canonical = page.locator('#v6-solutions-routes');
  await expect(canonical).toBeVisible();
  for (const href of SIX_CANONICAL_ROUTES) {
    await expect(canonical.locator(`a[href="${href}"]`)).toHaveCount(1);
  }
  await expect(page.getByText('Meridiano Counsel', { exact: true })).toHaveCount(0);

  await page.goto('./index.html');
  await expect(page.getByText('Meridiano Counsel', { exact: true })).toHaveCount(0);
});

test('v7 navega desde Home hacia Legal Intelligence con fragmento verificable', async ({ page }) => {
  await page.goto('./index.html');
  const link = page.locator('a[href="soluciones/ordenar-operacion-juridica.html#v7-legal-intelligence"]').first();
  await expect(link).toBeVisible();
  await link.click();
  await expect(page).toHaveURL(/soluciones\/ordenar-operacion-juridica\.html#v7-legal-intelligence$/);
  await expect(page.locator('#v7-legal-intelligence')).toBeVisible();
});

test('v7 navega desde el hub hacia AI Governance 360 y Regulatory Control', async ({ page }) => {
  await page.goto('./soluciones/index.html');
  const ai = page.locator('a[href="gobernar-inteligencia-artificial-empresa.html#v7-ai-governance-360"]');
  await expect(ai).toHaveCount(1);
  await ai.click();
  await expect(page).toHaveURL(/gobernar-inteligencia-artificial-empresa\.html#v7-ai-governance-360$/);
  await expect(page.locator('#v7-ai-governance-360')).toBeVisible();

  await page.goto('./soluciones/index.html');
  const regulatory = page.locator('a[href="estructurar-proyecto-regulado.html#v7-regulatory-control"]');
  await expect(regulatory).toHaveCount(1);
  await regulatory.click();
  await expect(page).toHaveURL(/estructurar-proyecto-regulado\.html#v7-regulatory-control$/);
  await expect(page.locator('#v7-regulatory-control')).toBeVisible();
});
