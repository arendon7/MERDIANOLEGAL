import { readFileSync } from 'node:fs';
import AxeBuilder from '@axe-core/playwright';
import { test, expect } from './helpers.mjs';

const wcagTags = ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'];
const blockingImpacts = new Set(['serious', 'critical']);
const deepMobilePath = './productos/programa-gobernanza-ia.html';
const releaseVersion = JSON.parse(readFileSync(new URL('../../version.json', import.meta.url), 'utf8')).version || '0.0.0';
const releaseParts = String(releaseVersion).split('.').map((part) => Number.parseInt(part, 10) || 0);
const unifiedContactDisclosureV523 = releaseParts[0] > 5 || (releaseParts[0] === 5 && releaseParts[1] >= 23);

const publicSurfaces = [
  ['portada', './'],
  ['solución IA', './soluciones/gobernar-inteligencia-artificial-empresa.html'],
  ['ficha profunda', deepMobilePath],
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
    if (path === './' || path === deepMobilePath) await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(path);

    if (path === './') {
      const practiceTargets = page.locator('.perspectives-grid button[data-service]');
      await expect(practiceTargets).toHaveCount(3);
      const targetHeights = await practiceTargets.evaluateAll((nodes) => nodes.map((node) => node.getBoundingClientRect().height));
      expect(Math.min(...targetHeights)).toBeGreaterThanOrEqual(44);

      const scrollRegions = page.locator('[data-mobile-scrollable-v516="true"]');
      await expect(scrollRegions).toHaveCount(3);
      for (let index = 0; index < 3; index += 1) {
        const region = scrollRegions.nth(index);
        await expect(region).toHaveAttribute('tabindex', '0');
        await expect(region).toHaveAttribute('role', 'region');
        await expect(region).toHaveAttribute('aria-label', /.+/);
      }

      const disclosures = page.locator('details[data-mobile-disclosure-v516]');
      if (unifiedContactDisclosureV523) {
        await expect(disclosures).toHaveCount(1);
        const disclosure = disclosures.first();
        await expect(disclosure).toHaveAttribute('data-contact-process-v523', 'true');
        await expect(disclosure).not.toHaveAttribute('open', '');
        await expect(disclosure.locator('[data-close-path-v510="true"]')).toHaveCount(1);
        await expect(disclosure.locator('[data-engagement-v511="true"]')).toHaveCount(1);
        await expect(disclosure.locator('[data-engagement-state-v511]')).toHaveCount(4);
        await expect(disclosure.locator('[data-engagement-automatic-v511="false"]')).toHaveCount(1);
        const summary = disclosure.locator(':scope > summary');
        const box = await summary.boundingBox();
        expect(box?.height || 0).toBeGreaterThanOrEqual(44);
        await summary.click();
        await expect(disclosure).toHaveAttribute('open', '');
        await expect(disclosure.locator('[data-close-path-v510="true"]')).toBeVisible();
        await expect(disclosure.locator('[data-engagement-v511="true"]')).toBeVisible();
      } else {
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
      }
      await expect(page.locator('[data-engagement-state-v511]')).toHaveCount(4);
      await expect(page.locator('[data-engagement-automatic-v511="false"]')).toHaveCount(1);
    }

    if (path === deepMobilePath) {
      const menu = page.locator('.detail-menu');
      await expect(menu).toBeVisible();
      const menuBox = await menu.boundingBox();
      expect(menuBox?.width || 0).toBeGreaterThanOrEqual(44);
      expect(menuBox?.height || 0).toBeGreaterThanOrEqual(44);

      const mobilePrimary = page.locator('.detail-mobile-cta-v46 > a:first-child');
      await expect(mobilePrimary).toBeVisible();
      const primaryBox = await mobilePrimary.boundingBox();
      expect(primaryBox?.height || 0).toBeGreaterThanOrEqual(44);

      await menu.click();
      const nav = page.locator('#detail-nav');
      await expect(nav).toHaveClass(/open/);
      const navLinks = nav.locator(':scope > a');
      await expect(navLinks).toHaveCount(5);
      const navHeights = await navLinks.evaluateAll((nodes) => nodes.map((node) => node.getBoundingClientRect().height));
      expect(Math.min(...navHeights)).toBeGreaterThanOrEqual(44);
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