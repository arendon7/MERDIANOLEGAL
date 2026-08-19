import { test, expect } from './helpers.mjs';

const SUBJECTS = [
  'legal-ai-transformation',
  'contract-control',
  'ai-governance-360',
  'regulatory-control',
  'legal-desk',
];

async function snapshot(page) {
  return page.evaluate(() => window.MeridianoCommercialEvidenceV74?.snapshot?.() || null);
}

test('v7.4 propaga source allowlisted desde el Centro Demo sin transporte externo', async ({ page }) => {
  const external = [];
  page.on('request', (request) => {
    if (/plausible\.io|google-analytics|googletagmanager|analytics/i.test(request.url())) external.push(request.url());
  });
  await page.goto('./experiencia.html#intelligence');
  for (const subject of SUBJECTS) {
    const link = page.locator(`[data-li-demo-scenario="${subject}"] a`).first();
    await expect(link).toHaveAttribute('href', new RegExp(`source=li-${subject}`));
  }
  const contractLink = page.locator('[data-li-demo-scenario="contract-control"] a').first();
  await contractLink.evaluate((node) => node.addEventListener('click', (event) => event.preventDefault(), { once: true }));
  await contractLink.click();
  const state = await snapshot(page);
  expect(state.status).toBe('readiness-disabled');
  expect(state.events).toContainEqual(expect.objectContaining({ subject: 'contract-control', interaction: 'demo_offer_open' }));
  expect(state.privacy.networkTransport).toBe(false);
  expect(state.privacy.persistentStorage).toBe(false);
  expect(external).toEqual([]);
});

test('v7.4 atribuye oferta y contacto sin exportar texto libre', async ({ page }) => {
  await page.goto('./productos/sistema-contractual-empresarial.html');
  let state = await snapshot(page);
  expect(state.currentSubject).toBe('contract-control');
  expect(state.events).toContainEqual(expect.objectContaining({ subject: 'contract-control', interaction: 'offer_view' }));

  const contact = page.locator('a[href*="#contacto"]:visible').first();
  await expect(contact).toHaveAttribute('href', /source=li-contract-control/);
  await contact.evaluate((node) => node.addEventListener('click', (event) => event.preventDefault(), { once: true }));
  await contact.click();
  state = await snapshot(page);
  expect(state.events).toContainEqual(expect.objectContaining({ subject: 'contract-control', interaction: 'contact_intent' }));
  for (const event of state.events) {
    expect(Object.keys(event).sort()).toEqual(['interaction', 'sequence', 'subject']);
  }
});

test('v7.4 conserva atribución allowlisted hasta handoff preparado sin afirmar envío', async ({ page }) => {
  await page.goto('./index.html?source=li-ai-governance-360#contacto');
  let state = await snapshot(page);
  expect(state.currentSubject).toBe('ai-governance-360');
  expect(state.events).toHaveLength(0);

  await page.evaluate(() => {
    window.dispatchEvent(new CustomEvent('meridiano:lead-prepared', {
      detail: { reference: 'ML-TEST', need: 'contenido que v7.4 no debe consumir' },
    }));
  });
  state = await snapshot(page);
  expect(state.events).toContainEqual(expect.objectContaining({ subject: 'ai-governance-360', interaction: 'handoff_prepared' }));
  expect(state.semanticLimits.handoffPreparedMeansMessageSent).toBe(false);
  expect(state.semanticLimits.handoffPreparedMeansDelivered).toBe(false);
  expect(state.semanticLimits.handoffPreparedMeansClientConversion).toBe(false);
  expect(JSON.stringify(state.events)).not.toContain('ML-TEST');
  expect(JSON.stringify(state.events)).not.toContain('contenido que');
});

test('v7.4 ignora source libre o manipulado', async ({ page }) => {
  await page.goto('./index.html?source=cliente-acme-confidencial#contacto');
  let state = await snapshot(page);
  expect(state.currentSubject).toBe('');
  await page.evaluate(() => window.dispatchEvent(new CustomEvent('meridiano:lead-prepared', { detail: { reference: 'X' } })));
  state = await snapshot(page);
  expect(state.events).toHaveLength(0);
  const exposedSubjects = await page.evaluate(() => window.MeridianoCommercialEvidenceV74?.subjects || []);
  expect(exposedSubjects).toEqual(SUBJECTS);
});
