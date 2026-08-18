import { test, expect } from './helpers.mjs';

test('v6.1 carga el adapter antes de telemetría y permanece sin transporte externo', async ({ page }) => {
  const externalAnalyticsRequests = [];
  page.on('request', (request) => {
    const url = request.url();
    if (/https:\/\/(?:[^/]+\.)?(?:plausible\.io|umami\.)/i.test(url)) externalAnalyticsRequests.push(url);
  });

  await page.goto('./');
  await expect.poll(() => page.evaluate(() => Boolean(window.MeridianoAnalyticsAdapter))).toBe(true);

  const state = await page.evaluate(() => {
    const scripts = [...document.scripts].map((script) => script.getAttribute('src') || '');
    return {
      api: window.MeridianoAnalyticsAdapter.snapshot(),
      adapterIndex: scripts.findIndex((src) => src.endsWith('assets/js/v6/analytics-adapter-v61.js')),
      telemetryIndex: scripts.findIndex((src) => src.endsWith('telemetry-v50.js')),
      providerScripts: document.querySelectorAll('script[data-meridiano-analytics-provider]').length,
    };
  });

  expect(state.api.version).toBe('6.1.0');
  expect(state.api.enabled).toBe(false);
  expect(state.api.provider).toBe('none');
  expect(state.api.providerReady).toBe(false);
  expect(state.api.queuedEventNames).toEqual([]);
  expect(state.api.emittedEventNames).toEqual([]);
  expect(state.api.observedStageNames).toEqual([]);
  expect(Object.values(state.api.privacy).every((value) => value === false)).toBe(true);
  expect(state.adapterIndex).toBeGreaterThanOrEqual(0);
  expect(state.telemetryIndex).toBeGreaterThan(state.adapterIndex);
  expect(state.providerScripts).toBe(0);

  await page.locator('#v6-situations').scrollIntoViewIfNeeded();
  await expect.poll(() => page.evaluate(() => window.MeridianoFunnelV529.snapshot().milestones.some((item) => item.stage === 'need'))).toBe(true);
  const afterCheckpoint = await page.evaluate(() => window.MeridianoAnalyticsAdapter.snapshot());
  expect(afterCheckpoint.queuedEventNames).toEqual([]);
  expect(afterCheckpoint.emittedEventNames).toEqual([]);
  expect(afterCheckpoint.observedStageNames).toEqual([]);
  expect(externalAnalyticsRequests).toEqual([]);
});

test('v6.1 acepta solo stage saneado, ignora event/target y no consume telemetría raw', async ({ page }) => {
  await page.goto('./');
  await expect.poll(() => page.evaluate(() => Boolean(window.MeridianoAnalyticsAdapter))).toBe(true);

  const result = await page.evaluate(() => {
    const adapter = window.MeridianoAnalyticsAdapter;
    const sentinel = 'PII-V61-NO-SALIR-9382';
    const cases = [
      adapter.preview({ stage: 'need', event: sentinel, target: sentinel, email: sentinel, message: sentinel, reference: sentinel }),
      adapter.preview({ stage: 'handoff', event: sentinel, target: sentinel, need: sentinel, reference: sentinel }),
      adapter.preview({ stage: 'contact', event: sentinel, target: sentinel, company: sentinel }),
      adapter.preview({ stage: 'evidence', event: sentinel, target: sentinel, message: sentinel }),
      adapter.preview({ stage: 'awareness', event: sentinel, target: sentinel }),
      adapter.preview({ stage: sentinel, event: 'contact', target: 'whatsapp' }),
    ];
    const rawTrackResult = adapter.track('lead_prepared', {
      name: 'lead_prepared',
      detail: { need: sentinel, email: sentinel, message: sentinel, reference: sentinel },
    });
    return { cases, rawTrackResult, serialized: JSON.stringify(cases), sentinel };
  });

  expect(result.cases).toEqual([
    { name: 'meridiano_funnel_need' },
    { name: 'meridiano_funnel_handoff' },
    { name: 'meridiano_funnel_contact' },
    { name: 'meridiano_funnel_evidence' },
    null,
    null,
  ]);
  expect(result.rawTrackResult).toBe(false);
  expect(result.serialized).not.toContain(result.sentinel);
  expect(result.serialized).not.toMatch(/"(?:email|message|reference|company|need|target|stage|event)"\s*:/i);
});
