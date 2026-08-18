import { test, expect, expectNoHorizontalOverflow, openDetailLegacy, openSolutionLegacy } from './helpers.mjs';

const detailPaths = [
  './productos/activos-intangibles-protegidos.html',
  './productos/diagnostico-juridico-empresarial.html',
  './productos/empresa-juridicamente-organizada.html',
  './productos/empresa-lista-para-inversion.html',
  './productos/programa-gobernanza-ia.html',
  './productos/proteccion-datos-consumidor.html',
  './productos/proyecto-regulado-estructurado.html',
  './productos/sistema-contractual-empresarial.html',
  './servicios/contratacion-estrategica.html',
  './servicios/diagnostico-juridico-empresarial.html',
  './servicios/direccion-juridica-externa.html',
  './servicios/legal-operations.html',
  './servicios/proyectos-regulados.html',
  './servicios/propiedad-intelectual.html',
  './servicios/sociedades-gobierno-inversion.html',
  './servicios/tecnologia-inteligencia-artificial.html',
];

const solutionPaths = [
  './soluciones/direccion-juridica-externa-empresa.html',
  './soluciones/estructurar-proyecto-regulado.html',
  './soluciones/gobernar-inteligencia-artificial-empresa.html',
  './soluciones/ordenar-operacion-juridica.html',
  './soluciones/ordenar-riesgo-juridico-empresa.html',
  './soluciones/preparar-empresa-para-inversion.html',
];

test('v6 mantiene v5.31 completo como profundidad nativa en 16 fichas', async ({ page }) => {
  for (const path of detailPaths) {
    await page.goto(path);
    await expect(page.locator('body')).toHaveAttribute('data-experience-wave', 'deep-offers');
    await expect(page.locator('.v6-detail-hero')).toBeVisible();
    await expect(page.locator('#v6-detail-depth')).not.toHaveAttribute('open', '');

    const buying = page.locator('[data-buying-clarity-v58="true"]');
    const commercial = page.locator('[data-offer-commercial-v530]');
    const pair = page.locator('[data-decision-compression-v531="decision-result"]');
    const narrative = page.locator('details[data-decision-compression-v531="offer-narrative"]');

    await expect(buying).toHaveCount(1);
    await expect(commercial).toHaveCount(1);
    await expect(pair).toHaveCount(1);
    await expect(narrative).toHaveCount(1);
    await expect(buying).not.toBeVisible();
    await expect(pair).not.toBeVisible();

    await openDetailLegacy(page);
    await expect(buying).toBeVisible();
    await expect(commercial).toBeVisible();
    await expect(pair).toBeVisible();
    await expect(narrative).not.toHaveAttribute('open', '');
    await expect(narrative).toContainText('CRITERIO DE CONTRATACIÓN');
    await expect(narrative).toContainText('ALTERNATIVA CERCANA');
    await expect(narrative).toContainText('LENTE JURÍDICA');

    const summary = narrative.locator(':scope > summary');
    await summary.focus();
    await page.keyboard.press('Enter');
    await expect(narrative).toHaveAttribute('open', '');
    await page.keyboard.press('Enter');
    await expect(narrative).not.toHaveAttribute('open', '');
    await expectNoHorizontalOverflow(page);
  }
});

test('v6 mantiene las cuatro profundidades secundarias v5.31 en las 6 soluciones', async ({ page }) => {
  for (const path of solutionPaths) {
    await page.goto(path);
    await expect(page.locator('body')).toHaveAttribute('data-experience-wave', 'solutions');
    await expect(page.locator('#v6-solution-signals')).toBeVisible();
    await expect(page.locator('#v6-solution-result')).toBeVisible();
    await expect(page.locator('#v6-solution-pricing')).toBeVisible();
    await expect(page.locator('#v6-solution-boundary')).toBeVisible();

    const outer = page.locator('#v6-solution-depth');
    await expect(outer).not.toHaveAttribute('open', '');
    await expect(page.locator('#ruta')).not.toBeVisible();
    await openSolutionLegacy(page);

    await expect(page.locator('#ruta')).toBeVisible();
    await expect(page.getByText('ALCANCE Y HONORARIOS', { exact: true })).toBeVisible();
    await expect(page.getByText('RESULTADO ESPERADO', { exact: true })).toBeVisible();
    await expect(page.getByText('LÍMITES', { exact: true }).first()).toBeVisible();
    await expect(page.locator('.growth-cta-v51')).toBeVisible();

    for (const key of ['objections', 'faq', 'related', 'proof']) {
      const disclosure = page.locator(`details[data-decision-compression-v531="solution-${key}"]`);
      await expect(disclosure).toHaveCount(1);
      await expect(disclosure).not.toHaveAttribute('open', '');
      const summary = disclosure.locator(':scope > summary');
      await summary.focus();
      await page.keyboard.press('Enter');
      await expect(disclosure).toHaveAttribute('open', '');
      await page.keyboard.press('Enter');
      await expect(disclosure).not.toHaveAttribute('open', '');
    }
    await expectNoHorizontalOverflow(page);
  }
});
