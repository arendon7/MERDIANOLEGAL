import { defineConfig, devices } from '@playwright/test';

const configuredBase = process.env.MERIDIANO_BASE_URL || 'https://arendon7.github.io/MERDIANOLEGAL/';
const baseURL = configuredBase.endsWith('/') ? configuredBase : `${configuredBase}/`;
const a11ySpec = /accessibility\.spec\.mjs$/;
const w5HomeSpec = /v8-home-shell(?:\.accessibility)?\.spec\.mjs$/;
const w5HomeCandidate = process.env.MERIDIANO_W5_HOME_CANDIDATE === '1';
// v5.5 compatibility invariant: browser projects preserve the historical testIgnore: a11ySpec behavior while W5 adds its isolated spec family.
const browserIgnore = w5HomeCandidate ? a11ySpec : [a11ySpec, w5HomeSpec];
const accessibilityIgnore = w5HomeCandidate ? [] : [w5HomeSpec];

export default defineConfig({
  testDir: './tests/e2e',
  fullyParallel: false,
  forbidOnly: Boolean(process.env.CI),
  retries: process.env.CI ? 1 : 0,
  workers: process.env.CI ? 1 : undefined,
  timeout: 30_000,
  expect: { timeout: 7_000 },
  reporter: process.env.CI
    ? [
        ['line'],
        ['github'],
        ['./tests/e2e/ci-summary-reporter.mjs'],
        ['html', { outputFolder: 'playwright-report', open: 'never' }],
      ]
    : [['list']],
  use: {
    baseURL,
    actionTimeout: 10_000,
    navigationTimeout: 20_000,
    trace: 'retain-on-failure',
    screenshot: 'only-on-failure',
    video: 'off',
  },
  projects: [
    {
      name: 'chromium-desktop',
      testIgnore: browserIgnore,
      use: {
        ...devices['Desktop Chrome'],
        viewport: { width: 1440, height: 1000 },
      },
    },
    {
      name: 'chromium-mobile',
      testIgnore: browserIgnore,
      use: {
        ...devices['Pixel 7'],
      },
    },
    {
      name: 'webkit-desktop',
      testIgnore: browserIgnore,
      use: {
        ...devices['Desktop Safari'],
        viewport: { width: 1440, height: 1000 },
      },
    },
    {
      name: 'accessibility-chromium',
      testMatch: a11ySpec,
      testIgnore: accessibilityIgnore,
      use: {
        ...devices['Desktop Chrome'],
        viewport: { width: 1440, height: 1000 },
      },
    },
  ],
});
