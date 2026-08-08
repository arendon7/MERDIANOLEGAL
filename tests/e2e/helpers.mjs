import { expect, test as base } from '@playwright/test';

const benignResourceFragments = [
  'favicon.ico',
];

export const test = base.extend({
  runtimeGuard: [async ({ page }, use) => {
    const failures = [];
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
