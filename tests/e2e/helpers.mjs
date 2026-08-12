import { expect, test as base } from '@playwright/test';

const benignResourceFragments = [
  'favicon.ico',
];

export const test = base.extend({
  runtimeGuard: [async ({ page }, use) => {
    const failures = [];
    await page.addInitScript(() => {
      window.__meridianoHandoffGuardV517 = { references: [] };
      window.__meridianoClipboard = [];
      try {
        Object.defineProperty(navigator, 'clipboard', {
          configurable: true,
          value: {
            writeText: async (value) => {
              window.__meridianoClipboard.push(String(value));
            },
          },
        });
      } catch { /* el test de handoff verificará la rama disponible */ }
      window.addEventListener('meridiano:handoff-draft-v517', (event) => {
        const reference = String(event.detail?.reference || '').trim();
        if (reference) window.__meridianoHandoffGuardV517.references.push(reference);
      });
    });
    page.on('pageerror', (error) => failures.push(`pageerror: ${error.message}`));
    page.on('response', (response) => {
      if (response.status() < 400) return;
      const url = response.url();
      if (benignResourceFragments.some((fragment) => url.includes(fragment))) return;
      failures.push(`http.${response.status()}: ${url}`);
    });
    page.on('console', (message) => {
      if (message.type() !== 'error') return;
      const text = message.text();
      if (text.startsWith('Failed to load resource:')) return;
      if (benignResourceFragments.some((fragment) => text.includes(fragment))) return;
      failures.push(`console.error: ${text}`);
    });
    await use(failures);

    const handoff = await page.evaluate(() => {
      const guard = window.__meridianoHandoffGuardV517;
      if (!guard?.references?.length) return null;
      const form = document.getElementById('contact-form');
      const panel = form?.querySelector('[data-handoff-v517="true"]');
      const values = ['name', 'company', 'email', 'message']
        .map((name) => String(form?.querySelector(`[name="${name}"]`)?.value || '').trim())
        .filter(Boolean);
      return {
        references: [...guard.references],
        panelHidden: panel?.hidden ?? true,
        state: panel?.dataset.handoffState || '',
        referenceText: panel?.querySelector('[data-handoff-reference-v517]')?.textContent?.trim() || '',
        panelText: panel?.textContent || '',
        reopenDisabled: panel?.querySelector('[data-handoff-reopen-v517]')?.disabled ?? true,
        copyDisabled: panel?.querySelector('[data-handoff-copy-v517]')?.disabled ?? true,
        values,
      };
    });

    if (handoff) {
      expect(handoff.references).toHaveLength(1);
      expect(handoff.panelHidden).toBe(false);
      expect(handoff.state).toBe('prepared');
      expect(handoff.referenceText).toBe(handoff.references[0]);
      expect(handoff.reopenDisabled).toBe(false);
      expect(handoff.copyDisabled).toBe(false);
      for (const value of handoff.values) expect(handoff.panelText).not.toContain(value);

      const observability = await page.evaluate(() => window.MeridianoHandoffObservabilityV518);
      expect(observability).toEqual(expect.objectContaining({
        version: '5.18.0',
        privacy: expect.objectContaining({
          piiAllowed: false,
          networkTransportIntroduced: false,
          persistentStorage: false,
          crossSessionIdentifier: false,
          formContentAllowed: false,
        }),
        semanticLimits: expect.objectContaining({
          sentKnown: false,
          deliveredKnown: false,
          readKnown: false,
          acceptedKnown: false,
          engagementStartedKnown: false,
          conversionKnown: false,
        }),
      }));

      await expect.poll(async () => (await telemetrySnapshot(page)).some((event) =>
        event.name === 'handoff_prepared' && event.detail?.stage === 'handoff' && event.detail?.target === 'whatsapp-draft'
      )).toBe(true);

      const panel = page.locator('#contact-form [data-handoff-v517="true"]');
      await panel.locator('[data-handoff-reopen-v517]').click();
      await expect.poll(async () => (await telemetrySnapshot(page)).some((event) =>
        event.name === 'handoff_reopen_requested' && event.detail?.target === 'whatsapp'
      )).toBe(true);

      await panel.locator('[data-handoff-copy-v517]').click();
      await expect.poll(async () => (await telemetrySnapshot(page)).some((event) =>
        event.name === 'handoff_copy_succeeded' && event.detail?.target === 'clipboard'
      )).toBe(true);
      const copied = await page.evaluate(() => window.__meridianoClipboard || []);
      expect(copied).toHaveLength(1);

      await panel.locator('[data-handoff-edit-v517]').click();
      await expect.poll(async () => (await telemetrySnapshot(page)).some((event) =>
        event.name === 'handoff_edit_requested' && event.detail?.target === 'contact-form'
      )).toBe(true);

      const telemetryBeforeChange = JSON.stringify(await telemetrySnapshot(page));
      for (const value of handoff.values) expect(telemetryBeforeChange).not.toContain(value);

      const message = page.locator('#contact-form textarea[name="message"]');
      if (await message.count()) {
        const original = await message.inputValue();
        await message.fill(`${original} Cambio posterior a la preparación.`);
        await expect(panel).toHaveAttribute('data-handoff-state', 'changed');
        await expect(panel.locator('[data-handoff-reopen-v517]')).toBeDisabled();
        await expect(panel.locator('[data-handoff-copy-v517]')).toBeDisabled();
        await expect.poll(async () => (await telemetrySnapshot(page)).some((event) =>
          event.name === 'handoff_draft_stale' && event.detail?.stage === 'handoff' && event.detail?.target === 'draft'
        )).toBe(true);
      }
    }

    expect(failures, failures.join('\n')).toEqual([]);
  }, { auto: true }],
});

export { expect };

export async function expectNoHorizontalOverflow(page, tolerance = 4) {
  const metrics = await page.evaluate(() => ({
    scrollWidth: document.documentElement.scrollWidth,
    clientWidth: document.documentElement.clientWidth,
  }));
  expect(metrics.scrollWidth).toBeLessThanOrEqual(metrics.clientWidth + tolerance);
}

export async function telemetrySnapshot(page) {
  return page.evaluate(() => window.MeridianoTelemetry?.snapshot?.() || []);
}

export async function preventNavigationFor(locator) {
  await locator.evaluate((node) => {
    node.addEventListener('click', (event) => event.preventDefault(), { once: true, capture: true });
  });
}
