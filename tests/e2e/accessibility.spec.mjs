import AxeBuilder from '@axe-core/playwright';
import { test, expect } from './helpers.mjs';

const wcagTags = ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'];
const blockingImpacts = new Set(['serious', 'critical']);

const publicSurfaces = [
  ['portada', './'],
  ['solución IA', './soluciones/gobernar-inteligencia-artificial-empresa.html'],
  ['ficha profunda', './productos/programa-gobernanza-ia.html'],
  ['sector tecnología', './sectores/tecnologia-software-ia.html'],
  ['perspectiva IA', './perspectivas/gobierno-juridico-inteligencia-artificial.html'],
  ['Centro Demo', './demo.html'],
];

function compactViolations(violations) {
  return violations.map((violation) => ({
    id: violation.id,
    impact: violation.impact,
    description: violation.description,
    help: violation.help,
    targets: violation.nodes.slice(0, 5).map((node) => node.target.join(' ')),
  }));
}

async function audit(page) {
  const result = await new AxeBuilder({ page }).withTags(wcagTags).analyze();
  const blocking = result.violations.filter((violation) => blockingImpacts.has(violation.impact));
  expect(compactViolations(blocking), JSON.stringify(compactViolations(blocking), null, 2)).toEqual([]);
}

for (const [label, path] of publicSurfaces) {
  test(`axe WCAG 2.1 AA sin violaciones serias/críticas · ${label}`, async ({ page }) => {
    if (path === './') await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(path);

    if (path === './') {
      const practiceTargets = page.locator('.perspectives-grid button[data-service]');
      await expect(practiceTargets).toHaveCount(3);
      const targetHeights = await practiceTargets.evaluateAll((nodes) => nodes.map((node) => node.getBoundingClientRect().height));
      expect(Math.min(...targetHeights)).toBeGreaterThanOrEqual(44);

      const disclosures = page.locator('details[data-mobile-disclosure-v516]');
      await expect(disclosures).toHaveCount(2);
      for (let index = 0; index < 2; index += 1) {
        const disclosure = disclosures.nth(index);
        await expect(disclosure).not.toHaveAttribute('open', '');
        const summary = disclosure.locator('summary');
        const box = await summary.boundingBox();
        expect(box?.height || 0).toBeGreaterThanOrEqual(44);
        await summary.click();
        await expect(disclosure).toHaveAttribute('open', '');
      }
      await expect(page.locator('[data-engagement-state-v511]')).toHaveCount(4);
      await expect(page.locator('[data-engagement-automatic-v511="false"]')).toHaveCount(1);
    }

    await audit(page);
  });
}

test('axe valida portal demo autenticado y modal de nueva solicitud', async ({ page }) => {
  await page.goto('./demo.html');
  await page.locator('.credential-card[data-email="cliente@empresa-demo.com"]').click();
  await page.getByRole('button', { name: 'Ingresar' }).click();
  await expect(page.locator('#portal-view')).not.toHaveClass(/hidden/);
  await page.locator('#new-ticket').click();
  await expect(page.locator('#ticket-modal')).toHaveAttribute('open', '');
  await audit(page);
});
