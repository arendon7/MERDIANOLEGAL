import { test, expect } from './helpers.mjs';

async function expectNoHorizontalOverflow(page) {
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  expect(overflow).toBeLessThanOrEqual(1);
}

const SCENARIOS = [
  'legal-ai-transformation',
  'contract-control',
  'ai-governance-360',
  'regulatory-control',
  'legal-desk',
];

test('v7.3 expone Legal Intelligence como sexto escenario del Centro Demo', async ({ page }) => {
  await page.goto('./experiencia.html');
  const tab = page.locator('[data-target="intelligence"]');
  await expect(tab).toHaveCount(1);
  await expect(tab).toBeVisible();
  await expect(tab).toContainText('Legal Intelligence');

  await tab.click();
  const panel = page.locator('[data-panel="intelligence"]');
  await expect(panel).toBeVisible();
  await expect(panel).toContainText('LEGAL INTELLIGENCE · DEMO');
  await expect(panel).toContainText('Datos ficticios');
  await expect(panel).toContainText('Sin carga de información real');
  await expect(panel).toContainText('Sin asesoría jurídica');
  await expect(panel.locator('[data-li-demo-scenario]')).toHaveCount(5);
  await expect(panel.locator('.li-demo-badge-v73')).toHaveCount(5);
  await expectNoHorizontalOverflow(page);
});

test('v7.3 muestra los cinco escenarios y sus fronteras sin capabilities ficticias', async ({ page }) => {
  await page.goto('./experiencia.html#intelligence');
  const panel = page.locator('[data-panel="intelligence"]');
  await expect(panel).toBeVisible();

  for (const scenario of SCENARIOS) {
    const card = panel.locator(`[data-li-demo-scenario="${scenario}"]`);
    await expect(card).toHaveCount(1);
    await expect(card).toContainText('DEMO');
    await expect(card).toContainText('Frontera.');
    await expect(card.locator('a')).toHaveCount(1);
  }

  await expect(panel.locator('form')).toHaveCount(0);
  await expect(panel.locator('input[type="file"]')).toHaveCount(0);
  await expect(panel).not.toContainText('Meridiano Counsel');
  await expect(panel).not.toContainText('portal productivo incluido');
  await expect(panel).not.toContainText('decisión jurídica autónoma');
});

test('v7.3 deriva cantidades demostrativas de las ofertas canónicas', async ({ page }) => {
  await page.goto('./experiencia.html#intelligence');

  const operations = page.locator('[data-li-demo-scenario="legal-ai-transformation"]');
  await expect(operations).toContainText('Hasta 10 tipos de servicio');
  await expect(operations).toContainText('Hasta 6 flujos prioritarios');
  await expect(operations).toContainText('Hasta 12 plantillas o artefactos');
  await expect(operations).toContainText('1 tablero de indicadores');
  await expect(operations).toContainText('1 piloto funcional');

  const contracts = page.locator('[data-li-demo-scenario="contract-control"]');
  await expect(contracts).toContainText('Hasta 40 contratos históricos');
  await expect(contracts).toContainText('Hasta 60 relaciones inventariadas');
  await expect(contracts).toContainText('Hasta 6 modelos contractuales');
  await expect(contracts).toContainText('Hasta 20 módulos de cláusulas');
  await expect(contracts).toContainText('Hasta 40 posiciones de playbook');
  await expect(contracts).toContainText('Hasta 100 obligaciones');

  const ai = page.locator('[data-li-demo-scenario="ai-governance-360"]');
  await expect(ai).toContainText('Hasta 25 casos de uso');
  await expect(ai).toContainText('Hasta 30 proveedores o herramientas');

  const regulatory = page.locator('[data-li-demo-scenario="regulatory-control"]');
  await expect(regulatory).toContainText('Hasta 15 permisos');
  await expect(regulatory).toContainText('Hasta 10 autoridades');
  await expect(regulatory).toContainText('Hasta 12 contratos');
  await expect(regulatory).toContainText('1 ruta habilitante');
  await expect(regulatory).toContainText('1 calendario regulatorio');
});

test('v7.3 mantiene Legal Desk como modelo demostrativo sin inventar capacidad', async ({ page }) => {
  await page.goto('./experiencia.html#intelligence');
  const desk = page.locator('[data-li-demo-scenario="legal-desk"]');
  await expect(desk).toContainText('Solicitud');
  await expect(desk).toContainText('Triage');
  await expect(desk).toContainText('Revisión jurídica');
  await expect(desk).toContainText('QA');
  await expect(desk).toContainText('no fija volumen, canales, Legal Units, SLA o capacidad incluida');
  await expect(desk.locator('.li-demo-metric-v73')).toHaveCount(0);
});
