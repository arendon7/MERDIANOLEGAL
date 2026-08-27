import { test, expect, expectNoHorizontalOverflow } from './helpers.mjs';

// W5.0E is served from a disposable mirror whose root index.html is the exact
// future production Home. Do not test it from a synthetic subdirectory: that
// would change relative URL semantics for runtime-config, assets and links.
const candidate = './';
const persistedCandidate = process.env.MERIDIANO_W5_PERSISTED_CANDIDATE === '1';
const sections = Array.from({ length: 12 }, (_, index) => `H${String(index + 1).padStart(2, '0')}`);

async function openCandidate(page) {
  const external = [];
  page.on('request', (request) => {
    const url = new URL(request.url());
    const host = url.hostname.replace(/\.$/, '');
    if (!['127.0.0.1', 'localhost'].includes(host)) external.push(request.url());
  });
  const response = await page.goto(candidate);
  expect(response?.status()).toBe(200);
  await expect(page.locator('html')).toHaveAttribute('data-v8-home-candidate', 'persisted');
  return external;
}

test('W5.0E future root is indexable, source-driven and SEO-bridged without pilot handoff', async ({ page }) => {
  test.skip(!persistedCandidate, 'W5.0E persisted Home specs run only in their dedicated candidate workflow.');
  const external = await openCandidate(page);
  await expect(page.locator('meta[name="robots"]')).toHaveAttribute('content', 'index,follow,max-image-preview:large');
  await expect(page.locator('link[rel="canonical"]')).toHaveAttribute('href', 'https://arendon7.github.io/MERDIANOLEGAL/');
  await expect(page.locator('h1')).toHaveCount(1);
  await expect(page.locator('#contact-form')).toHaveCount(1);
  const observed = await page.locator('[data-v8-home-section]').evaluateAll((nodes) => nodes.map((node) => node.dataset.v8HomeSection));
  expect(observed).toEqual(sections);

  await expect(page.locator('a[href="productos/sistema-contractual-empresarial.html"]')).not.toHaveCount(0);
  await expect(page.locator('a[href="servicios/sociedades-gobierno-inversion.html"]')).not.toHaveCount(0);
  await expect(page.locator('a[href="servicios/direccion-juridica-externa.html"]')).not.toHaveCount(0);
  await expect(page.locator('a[href="soluciones/sistema-contractual-empresarial.html"]')).toHaveCount(0);
  await expect(page.locator('a[href="practicas/corporativo-societario-gobierno.html"]')).toHaveCount(0);
  await expect(page.locator('a[href="servicios-continuos/direccion-juridica-externa.html"]')).toHaveCount(0);
  await expect(page.locator('a[href*="meridiano-contratos"]')).toHaveCount(0);
  expect(external).toEqual([]);
  await expectNoHorizontalOverflow(page, 1);
});

test('W5.0E contact prepares WhatsApp only after explicit submit and protects stale drafts', async ({ page }) => {
  test.skip(!persistedCandidate, 'W5.0E persisted Home specs run only in their dedicated candidate workflow.');
  await openCandidate(page);
  await page.evaluate(() => {
    window.__meridianoOpened = [];
    window.open = (url) => {
      window.__meridianoOpened.push(String(url));
      return {};
    };
  });

  const form = page.locator('#contact-form');
  await form.locator('[name="name"]').fill('Ana Prueba');
  await form.locator('[name="company"]').fill('Empresa Demo');
  await form.locator('[name="email"]').fill('ana@example.com');
  await form.locator('[name="need"]').selectOption({ label: 'Contratos y negociaciones' });
  await form.locator('[name="decision_stage"]').selectOption({ label: 'Quiero recibir una propuesta' });
  await form.locator('[name="urgency"]').selectOption({ label: 'En 2 a 4 semanas' });
  await form.locator('[name="budget"]').selectOption({ label: 'COP 5 a 15 millones' });
  await form.locator('[name="message"]').fill('Necesitamos ordenar modelos y aprobaciones contractuales.');
  await form.locator('[name="privacy"]').check();

  expect(await page.evaluate(() => window.__meridianoOpened.length)).toBe(0);
  await form.locator('[data-v8-contact-submit]').click();
  const opened = await page.evaluate(() => window.__meridianoOpened.slice());
  expect(opened).toHaveLength(1);
  expect(opened[0]).toMatch(/^https:\/\/wa\.me\/573008507813\?text=/);
  expect(decodeURIComponent(opened[0])).toContain('Contratos y negociaciones');
  await expect(form.locator('[data-v8-handoff]')).toBeVisible();
  await expect(form.locator('[data-v8-contact-status]')).toContainText('Revise el texto');
  await expect(form.locator('[data-v8-handoff-reopen]')).toBeEnabled();

  await form.locator('[name="message"]').fill('Contexto actualizado después de preparar.');
  await expect(form.locator('[data-v8-handoff-reopen]')).toBeDisabled();
  await expect(form.locator('[data-v8-handoff-copy-button]')).toBeDisabled();
  await expect(form.locator('[data-v8-contact-status]')).toContainText('desactualizada');

  const storage = await page.evaluate(() => ({
    local: localStorage.length,
    session: sessionStorage.length,
    cookie: document.cookie,
    contact: window.MeridianoV8Contact,
    measurement: window.MeridianoV8Measurement.snapshot(),
  }));
  expect(storage.local).toBe(0);
  expect(storage.session).toBe(0);
  expect(storage.cookie).toBe('');
  expect(storage.contact.persistentStorage).toBe(false);
  expect(storage.contact.piiInMeasurement).toBe(false);
  expect(storage.measurement).toContain('awareness');
  expect(storage.measurement).toContain('contact');
  expect(storage.measurement).toContain('handoff');
});

test('W5.0E shell remains keyboard-operable and mobile-safe', async ({ page }, testInfo) => {
  test.skip(!persistedCandidate, 'W5.0E persisted Home specs run only in their dedicated candidate workflow.');
  await openCandidate(page);
  const mobile = testInfo.project.name === 'chromium-mobile';
  const menuToggle = page.locator('[data-ml-menu-toggle]');
  const megaToggle = page.locator('[data-ml-mega-toggle]');
  if (mobile) {
    await menuToggle.focus();
    await page.keyboard.press('Enter');
    await expect(menuToggle).toHaveAttribute('aria-expanded', 'true');
  }
  await megaToggle.focus();
  await page.keyboard.press('Enter');
  await expect(page.locator('[data-ml-mega]')).toBeVisible();
  await page.keyboard.press('Escape');
  await expect(page.locator('[data-ml-mega]')).toBeHidden();
  if (mobile) {
    await page.keyboard.press('Escape');
    await expect(menuToggle).toHaveAttribute('aria-expanded', 'false');
  }
  await expectNoHorizontalOverflow(page, 1);
});
