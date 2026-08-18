import { test, expect } from './helpers.mjs';

test('v6.2 mantiene Search Console fail-closed y coherente con runtime', async ({ page }) => {
  await page.goto('./');

  const state = await page.evaluate(() => {
    const metas = [...document.querySelectorAll('meta[name="google-site-verification"]')]
      .map((node) => node.getAttribute('content') || '');
    return {
      configured: Boolean(window.MERIDIANO_PUBLIC_CONFIG?.searchConsoleConfigured),
      metas,
    };
  });

  if (state.configured) {
    expect(state.metas).toHaveLength(1);
    expect(state.metas[0].trim().length).toBeGreaterThan(0);
  } else {
    expect(state.metas).toEqual([]);
  }
});

test('v6.2 sirve sitemap mínimo con la frontera indexable 43/3', async ({ page }) => {
  await page.goto('./');
  const sitemap = await page.evaluate(async () => {
    const response = await fetch('sitemap.xml', { cache: 'no-store' });
    if (!response.ok) throw new Error(`sitemap HTTP ${response.status}`);
    return response.text();
  });

  expect(sitemap).not.toContain('<lastmod>');
  expect(sitemap).not.toContain('<priority>');
  expect(sitemap).not.toContain('<changefreq>');
  expect((sitemap.match(/<loc>/g) || [])).toHaveLength(43);
  expect(sitemap).not.toContain('/404.html</loc>');
  expect(sitemap).not.toContain('/demo.html</loc>');
  expect(sitemap).not.toContain('/experiencia.html</loc>');
});
