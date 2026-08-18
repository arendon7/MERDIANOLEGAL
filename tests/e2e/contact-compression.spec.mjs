import { test, expect, expectNoHorizontalOverflow } from './helpers.mjs';

test('v5.23 concentra el contacto abierto en una síntesis y un proceso colapsado', async ({ page }) => {
  await page.goto('./#contacto');

  const form = page.locator('form[data-contact-compression-v523="true"]');
  await expect(form).toBeVisible();
  const synthesis = form.locator('[data-contact-synthesis-v523="true"]');
  await expect(synthesis).toHaveCount(1);
  await expect(synthesis).toHaveAttribute('role', 'region');
  expect(await synthesis.evaluate((node) => node.tagName)).toBe('DIV');
  await expect(form.locator('[data-qualification-summary-v59="true"]')).toHaveCount(1);
  await expect(form.locator('[data-commercial-brief-v513="true"]')).toHaveCount(1);
  await expect(form.locator('[data-recommendation-brief-v514="true"]')).toHaveCount(1);

  const process = form.locator('details[data-contact-process-v523="true"]');
  await expect(process).toHaveCount(1);
  await expect(process).not.toHaveAttribute('open', '');
  await expect(process.locator('[data-close-path-v510="true"]')).toHaveCount(1);
  await expect(process.locator('[data-engagement-v511="true"]')).toHaveCount(1);
  await expect(process.locator('[data-engagement-state-v511]')).toHaveCount(4);

  await form.locator('[name="need"]').selectOption({ label: 'Contratos y negociaciones' });
  await form.locator('[name="decision_stage"]').selectOption({ label: 'Estoy explorando la necesidad' });
  await form.locator('[name="urgency"]').selectOption({ label: 'En 1 a 3 meses' });
  await expect(form.locator('[data-qualification-need-v59]')).toContainText('Contratos y negociaciones');
  await expect(form.locator('[data-qualification-next-step-v59]')).toContainText('Orientación inicial');
  await expect(form.locator('[data-route-label-v515]')).toContainText('Orientación inicial');
  await expect(process).not.toHaveAttribute('open', '');
  await expectNoHorizontalOverflow(page);
});

test('v5.23 abre el único proceso cuando la intención explícita v6 es propuesta', async ({ page }) => {
  await page.goto('./productos/programa-gobernanza-ia.html');
  const proposal = page.locator('[data-experience-v60-cta="primary"]');
  await expect(proposal).toBeVisible();
  const href = await proposal.getAttribute('href');
  const source = new URL(href, 'https://meridiano.invalid/');
  expect(source.searchParams.get('commercial_intent')).toBe('proposal');
  expect(source.searchParams.get('modality')).toBe('product');
  expect(source.searchParams.get('proof_standard')).toBe('source');
  expect(source.searchParams.get('experience')).toBe('v6');
  await proposal.click();
  await expect(page).toHaveURL(/#contacto$/);
  const current = new URL(page.url());
  expect(current.searchParams.get('commercial_intent')).toBe('proposal');

  const form = page.locator('form[data-contact-compression-v523="true"]');
  const synthesis = form.locator('[data-contact-synthesis-v523="true"]');
  const process = form.locator('details[data-contact-process-v523="true"]');

  await expect(synthesis).toHaveCount(1);
  await expect(synthesis).toHaveAttribute('role', 'region');
  expect(await synthesis.evaluate((node) => node.tagName)).toBe('DIV');
  await expect(synthesis.locator('[data-brief-modality-v513]')).toContainText('Producto de alcance cerrado');
  await expect(synthesis.locator('[data-recommendation-fit-v514]')).not.toBeEmpty();
  await expect(synthesis.locator('[data-route-label-v515]')).toContainText('Propuesta verificable');
  await expect(process).toHaveAttribute('open', '');
  await expect(process).toHaveAttribute('data-default-state-v523', 'expanded-proposal');
  await expect(process.locator('[data-close-path-v510="true"]')).toBeVisible();
  await expect(process.locator('[data-engagement-v511="true"]')).toBeVisible();
  await expect(process.locator('[data-engagement-state-v511="accepted"]')).toContainText('Propuesta aceptada');
  await expect(process.locator('[data-engagement-state-v511="started"]')).toContainText('Encargo iniciado');
  await expectNoHorizontalOverflow(page);
});
