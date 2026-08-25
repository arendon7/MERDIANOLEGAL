import AxeBuilder from '@axe-core/playwright';
import { test, expect } from '@playwright/test';

const wcagTags = ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'];
const blockingImpacts = new Set(['serious', 'critical']);

const pilots = [
  {
    id: 'SO07',
    path: './soluciones/sistema-contractual-empresarial.html',
    family: 'solution',
    title: 'Sistema Contractual Empresarial',
    source: 'product-contract-system',
  },
  {
    id: 'PR02',
    path: './practicas/corporativo-societario-gobierno.html',
    family: 'practice',
    title: 'Corporativo, Societario y Gobierno',
    source: 'service-corporate',
  },
  {
    id: 'RC01',
    path: './servicios-continuos/direccion-juridica-externa.html',
    family: 'recurring',
    title: 'Dirección Jurídica Externa',
    source: 'service-direction',
  },
];

function compact(violations) {
  return violations.map((violation) => ({
    id: violation.id,
    impact: violation.impact,
    targets: violation.nodes.slice(0, 6).map((node) => node.target.join(' ')),
  }));
}

async function audit(page) {
  const result = await new AxeBuilder({ page }).withTags(wcagTags).analyze();
  const blocking = result.violations.filter((violation) => blockingImpacts.has(violation.impact));
  expect(compact(blocking), JSON.stringify(compact(blocking), null, 2)).toEqual([]);
}

for (const pilot of pilots) {
  test(`${pilot.id} materializa semántica v8, truth surface y boundary de candidate`, async ({ page }) => {
    const response = await page.goto(pilot.path);
    expect(response?.status()).toBe(200);

    await expect(page.locator('meta[name="robots"]')).toHaveAttribute('content', 'noindex,follow');
    await expect(page.locator('body')).toHaveClass(new RegExp(`ml-surface--${pilot.family}`));
    await expect(page.locator('body')).toHaveAttribute('data-v8-pilot', pilot.id);
    await expect(page.locator('body')).toHaveAttribute('data-source-catalog-id', pilot.source);
    await expect(page.locator('h1')).toHaveCount(1);
    await expect(page.locator('h1')).toHaveText(pilot.title);
    await expect(page.locator('form')).toHaveCount(0);

    await expect(page.locator('.ml-meta-ledger > div')).toHaveCount(3);
    await expect(page.locator('#ml-fit .ml-index-row')).toHaveCount(4);
    expect(await page.locator('.ml-ledger-item').count()).toBeGreaterThan(10);

    const primary = page.locator('.ml-hero .ml-btn').first();
    await expect(primary).toHaveAttribute('href', /\.\.\/index\.html\?.+#contacto$/);
    await expect(primary).toHaveAttribute('href', /commercial_intent=/);
    await expect(primary).toHaveAttribute('href', /proof_standard=source/);

    const legacyRelated = page.locator('#ml-related a[href*="../productos/"], #ml-related a[href*="../servicios/"]');
    await expect(legacyRelated).toHaveCount(0);

    const disclosure = page.locator('.ml-disclosure');
    await expect(disclosure).toHaveCount(1);
    await expect(disclosure).not.toHaveAttribute('open', '');
    const summary = disclosure.locator('summary');
    await summary.focus();
    await page.keyboard.press('Enter');
    await expect(disclosure).toHaveAttribute('open', '');
    await expect(disclosure.locator('#ml-related')).toBeVisible();

    const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    expect(overflow).toBeLessThanOrEqual(1);

    await audit(page);
  });
}

test('pilotos v8 mantienen los tres legacy certificados disponibles en paralelo', async ({ page }) => {
  const legacy = [
    './productos/sistema-contractual-empresarial.html',
    './servicios/sociedades-gobierno-inversion.html',
    './servicios/direccion-juridica-externa.html',
  ];
  for (const path of legacy) {
    const response = await page.goto(path);
    expect(response?.status(), path).toBe(200);
    await expect(page.locator('h1')).toHaveCount(1);
  }
});
