#!/usr/bin/env node
import { spawnSync } from 'node:child_process';
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, '..');
const config = JSON.parse(readFileSync(join(root, 'quality-budgets-v55.json'), 'utf8'));
const configuredBase = process.env.MERIDIANO_BASE_URL || 'https://arendon7.github.io/MERDIANOLEGAL/';
const baseURL = configuredBase.endsWith('/') ? configuredBase : `${configuredBase}/`;
const outputDir = join(root, 'quality-artifacts', 'v5.5');
const lighthouseBin = join(root, 'node_modules', '.bin', process.platform === 'win32' ? 'lighthouse.cmd' : 'lighthouse');
const chromeFlags = '--headless --no-sandbox --disable-dev-shm-usage';

mkdirSync(outputDir, { recursive: true });

function round(value, digits = 2) {
  return Number.isFinite(value) ? Number(value.toFixed(digits)) : null;
}

function metric(lhr, key) {
  return lhr.audits?.[key]?.numericValue;
}

const failures = [];
const summary = [];

for (const surface of config.surfaces) {
  const url = new URL(surface.path, baseURL).href;
  const reportPath = join(outputDir, `${surface.id}.json`);
  const args = [
    url,
    '--quiet',
    '--output=json',
    `--output-path=${reportPath}`,
    '--only-categories=performance,accessibility',
    `--chrome-flags=${chromeFlags}`,
  ];
  const run = spawnSync(lighthouseBin, args, {
    cwd: root,
    env: process.env,
    encoding: 'utf8',
    timeout: 120_000,
  });
  if (run.error || run.status !== 0) {
    const detail = run.error?.message || run.stderr || run.stdout || `exit ${run.status}`;
    failures.push(`${surface.id}: Lighthouse no pudo ejecutarse: ${String(detail).trim()}`);
    continue;
  }

  const lhr = JSON.parse(readFileSync(reportPath, 'utf8'));
  const values = {
    id: surface.id,
    url,
    performanceScore: lhr.categories?.performance?.score ?? null,
    accessibilityScore: lhr.categories?.accessibility?.score ?? null,
    largestContentfulPaintMs: metric(lhr, 'largest-contentful-paint'),
    cumulativeLayoutShift: metric(lhr, 'cumulative-layout-shift'),
    totalBlockingTimeMs: metric(lhr, 'total-blocking-time'),
    totalByteWeight: metric(lhr, 'total-byte-weight'),
  };
  summary.push(values);

  const b = config.budgets;
  const checks = [
    ['performanceScore', values.performanceScore, '>=', b.performanceScoreMin],
    ['accessibilityScore', values.accessibilityScore, '>=', b.accessibilityScoreMin],
    ['largestContentfulPaintMs', values.largestContentfulPaintMs, '<=', b.largestContentfulPaintMsMax],
    ['cumulativeLayoutShift', values.cumulativeLayoutShift, '<=', b.cumulativeLayoutShiftMax],
    ['totalBlockingTimeMs', values.totalBlockingTimeMs, '<=', b.totalBlockingTimeMsMax],
    ['totalByteWeight', values.totalByteWeight, '<=', b.totalByteWeightMax],
  ];
  for (const [name, actual, operator, limit] of checks) {
    const pass = Number.isFinite(actual) && (operator === '>=' ? actual >= limit : actual <= limit);
    if (!pass) failures.push(`${surface.id}: ${name}=${actual} exige ${operator} ${limit}`);
  }
}

const printable = summary.map((item) => ({
  ...item,
  performanceScore: round(item.performanceScore),
  accessibilityScore: round(item.accessibilityScore),
  largestContentfulPaintMs: round(item.largestContentfulPaintMs, 0),
  cumulativeLayoutShift: round(item.cumulativeLayoutShift, 3),
  totalBlockingTimeMs: round(item.totalBlockingTimeMs, 0),
  totalByteWeight: round(item.totalByteWeight, 0),
}));
writeFileSync(join(outputDir, 'summary.json'), `${JSON.stringify({ config, results: printable, failures }, null, 2)}\n`);
console.table(printable);

if (failures.length) {
  console.error('\nQUALITY V5.5 FALLÓ');
  failures.forEach((failure) => console.error(`- ${failure}`));
  process.exit(1);
}

console.log(`QUALITY V5.5 OK: ${summary.length} superficies cumplen Lighthouse y presupuestos.`);
