#!/usr/bin/env node
import { spawnSync } from 'node:child_process';
import { appendFileSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, '..');
const config = JSON.parse(readFileSync(join(root, 'quality-budgets-v55.json'), 'utf8'));
const ciPolicyFile = join(root, 'ci-baseline-v56.json');
const ciPolicy = JSON.parse(readFileSync(ciPolicyFile, 'utf8')).policy || {};
const configuredBase = process.env.MERIDIANO_BASE_URL || 'https://arendon7.github.io/MERDIANOLEGAL/';
const baseURL = configuredBase.endsWith('/') ? configuredBase : `${configuredBase}/`;
const outputDir = join(root, 'quality-artifacts', 'v5.5');
const lighthouseBin = join(root, 'node_modules', '.bin', process.platform === 'win32' ? 'lighthouse.cmd' : 'lighthouse');
const chromeFlags = '--headless --no-sandbox --disable-dev-shm-usage';
const verificationRuns = Number(ciPolicy.lighthouseVerificationRunsOnFailure || 0);
const maxSamples = Number(ciPolicy.lighthouseMaxSamplesPerSurface || 1);
const aggregation = ciPolicy.lighthouseAggregation || 'single-sample';
const verificationMetrics = new Set(ciPolicy.lighthouseVerificationMetrics || []);
const nonRetryableMetrics = new Set(ciPolicy.lighthouseNonRetryableMetrics || []);

mkdirSync(outputDir, { recursive: true });

function round(value, digits = 2) {
  return Number.isFinite(value) ? Number(value.toFixed(digits)) : null;
}

function metric(lhr, key) {
  return lhr.audits?.[key]?.numericValue;
}

function valuesFromLhr(surface, url, lhr, attempt) {
  return {
    id: surface.id,
    url,
    attempt,
    performanceScore: lhr.categories?.performance?.score ?? null,
    accessibilityScore: lhr.categories?.accessibility?.score ?? null,
    largestContentfulPaintMs: metric(lhr, 'largest-contentful-paint'),
    cumulativeLayoutShift: metric(lhr, 'cumulative-layout-shift'),
    totalBlockingTimeMs: metric(lhr, 'total-blocking-time'),
    totalByteWeight: metric(lhr, 'total-byte-weight'),
  };
}

function printableValues(item) {
  return {
    ...item,
    performanceScore: round(item.performanceScore),
    accessibilityScore: round(item.accessibilityScore),
    largestContentfulPaintMs: round(item.largestContentfulPaintMs, 0),
    cumulativeLayoutShift: round(item.cumulativeLayoutShift, 3),
    totalBlockingTimeMs: round(item.totalBlockingTimeMs, 0),
    totalByteWeight: round(item.totalByteWeight, 0),
  };
}

function layoutDiagnostics(lhr) {
  return Object.entries(lhr.audits || {})
    .filter(([id, audit]) => id.includes('layout') && (audit?.details?.items?.length || audit?.numericValue))
    .map(([id, audit]) => ({
      id,
      title: audit.title,
      score: audit.score,
      numericValue: audit.numericValue ?? null,
      items: (audit.details?.items || []).slice(0, 12),
    }));
}

function compactDetail(value, depth = 0) {
  if (value === null || value === undefined) return value;
  if (typeof value === 'string') return value.replace(/\s+/g, ' ').trim().slice(0, 360);
  if (typeof value === 'number' || typeof value === 'boolean') return value;
  if (depth >= 3) return '[truncated]';
  if (Array.isArray(value)) return value.slice(0, 8).map((item) => compactDetail(item, depth + 1));
  if (typeof value !== 'object') return String(value).slice(0, 160);

  const preferredKeys = [
    'selector', 'snippet', 'nodeLabel', 'explanation', 'label', 'text', 'path',
    'tapTargetScore', 'overlappingTargetScore', 'overlapScoreRatio', 'size',
    'source', 'target', 'subItems', 'node',
  ];
  const result = {};
  for (const key of preferredKeys) {
    if (Object.prototype.hasOwnProperty.call(value, key)) result[key] = compactDetail(value[key], depth + 1);
  }
  if (Object.keys(result).length) return result;
  for (const [key, item] of Object.entries(value).slice(0, 8)) result[key] = compactDetail(item, depth + 1);
  return result;
}

function accessibilityDiagnostics(lhr) {
  const refs = lhr.categories?.accessibility?.auditRefs || [];
  return refs
    .map((ref) => ({ ref, audit: lhr.audits?.[ref.id] }))
    .filter(({ audit }) => Number.isFinite(audit?.score) && audit.score < 1)
    .map(({ ref, audit }) => ({
      id: ref.id,
      title: audit.title || ref.id,
      score: audit.score,
      weight: ref.weight ?? null,
      group: ref.group ?? null,
      displayValue: audit.displayValue || null,
      items: (audit.details?.items || []).slice(0, 8).map((item) => compactDetail(item)),
    }));
}

function checksFor(values) {
  const b = config.budgets;
  return [
    ['performanceScore', values.performanceScore, '>=', b.performanceScoreMin],
    ['accessibilityScore', values.accessibilityScore, '>=', b.accessibilityScoreMin],
    ['largestContentfulPaintMs', values.largestContentfulPaintMs, '<=', b.largestContentfulPaintMsMax],
    ['cumulativeLayoutShift', values.cumulativeLayoutShift, '<=', b.cumulativeLayoutShiftMax],
    ['totalBlockingTimeMs', values.totalBlockingTimeMs, '<=', b.totalBlockingTimeMsMax],
    ['totalByteWeight', values.totalByteWeight, '<=', b.totalByteWeightMax],
  ].map(([name, actual, operator, limit]) => ({
    name,
    actual,
    operator,
    limit,
    pass: Number.isFinite(actual) && (operator === '>=' ? actual >= limit : actual <= limit),
  }));
}

function failedChecks(values) {
  return checksFor(values).filter((check) => !check.pass);
}

function median(values) {
  const numeric = values.filter(Number.isFinite).sort((a, b) => a - b);
  if (!numeric.length) return null;
  const middle = Math.floor(numeric.length / 2);
  return numeric.length % 2 ? numeric[middle] : (numeric[middle - 1] + numeric[middle]) / 2;
}

function aggregateMedian(surface, url, samples) {
  return {
    id: surface.id,
    url,
    attempt: null,
    performanceScore: median(samples.map((sample) => sample.values.performanceScore)),
    accessibilityScore: median(samples.map((sample) => sample.values.accessibilityScore)),
    largestContentfulPaintMs: median(samples.map((sample) => sample.values.largestContentfulPaintMs)),
    cumulativeLayoutShift: median(samples.map((sample) => sample.values.cumulativeLayoutShift)),
    totalBlockingTimeMs: median(samples.map((sample) => sample.values.totalBlockingTimeMs)),
    totalByteWeight: median(samples.map((sample) => sample.values.totalByteWeight)),
  };
}

function runAudit(surface, url, attempt) {
  const reportName = attempt === 1 ? `${surface.id}.json` : `${surface.id}-verification-${attempt}.json`;
  const reportPath = join(outputDir, reportName);
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
    return { error: String(detail).trim(), attempt, reportPath };
  }

  const lhr = JSON.parse(readFileSync(reportPath, 'utf8'));
  return {
    attempt,
    reportPath,
    lhr,
    values: valuesFromLhr(surface, url, lhr, attempt),
  };
}

const failures = [];
const summary = [];
const diagnostics = {};
const accessibilityAuditGaps = {};
const sampleLedger = {};

for (const surface of config.surfaces) {
  const url = new URL(surface.path, baseURL).href;
  const samples = [];
  const first = runAudit(surface, url, 1);
  if (first.error) {
    failures.push(`${surface.id}: Lighthouse no pudo ejecutarse: ${first.error}`);
    sampleLedger[surface.id] = [{ attempt: 1, error: first.error }];
    continue;
  }
  samples.push(first);
  accessibilityAuditGaps[surface.id] = accessibilityDiagnostics(first.lhr);

  const initialFailures = failedChecks(first.values);
  const hasNonRetryableFailure = initialFailures.some((check) => nonRetryableMetrics.has(check.name));
  const allFailuresAreVerifiable = initialFailures.length > 0 && initialFailures.every((check) => verificationMetrics.has(check.name));
  const canVerify = verificationRuns === 2 && maxSamples === 3 && aggregation === 'median-of-three';
  const verificationTriggered = canVerify && !hasNonRetryableFailure && allFailuresAreVerifiable;

  if (verificationTriggered) {
    const failedNames = initialFailures.map((check) => check.name).join(', ');
    console.log(`LIGHTHOUSE V5.6: ${surface.id} activa verificación mediana-de-tres por ${failedNames}.`);
    for (let extra = 0; extra < verificationRuns; extra += 1) {
      const attempt = samples.length + 1;
      const rerun = runAudit(surface, url, attempt);
      if (rerun.error) {
        failures.push(`${surface.id}: verificación Lighthouse ${attempt}/${maxSamples} no pudo ejecutarse: ${rerun.error}`);
        samples.push(rerun);
        break;
      }
      samples.push(rerun);
    }
  }

  const successfulSamples = samples.filter((sample) => sample.values);
  const useMedian = verificationTriggered && successfulSamples.length === maxSamples;
  const finalValues = useMedian ? aggregateMedian(surface, url, successfulSamples) : first.values;
  const finalFailures = failedChecks(finalValues);

  sampleLedger[surface.id] = samples.map((sample) => sample.values
    ? printableValues(sample.values)
    : { attempt: sample.attempt, error: sample.error });

  summary.push({
    ...finalValues,
    verificationTriggered,
    sampleCount: successfulSamples.length,
    aggregation: useMedian ? 'median-of-three' : 'single-sample',
  });

  if (verificationTriggered && successfulSamples.length !== maxSamples) {
    failures.push(`${surface.id}: la verificación exigía ${maxSamples} muestras válidas y obtuvo ${successfulSamples.length}`);
  }

  for (const check of finalFailures) {
    failures.push(`${surface.id}: ${check.name}=${check.actual} exige ${check.operator} ${check.limit}`);
    if (check.name === 'cumulativeLayoutShift') {
      diagnostics[surface.id] = successfulSamples.map((sample) => ({
        attempt: sample.attempt,
        detail: layoutDiagnostics(sample.lhr),
      }));
    }
  }
}

const printable = summary.map((item) => printableValues(item));
const summaryPayload = {
  config,
  verificationPolicy: {
    browser: ciPolicy.lighthouseBrowser,
    runsOnFailure: verificationRuns,
    maxSamplesPerSurface: maxSamples,
    aggregation,
    verificationMetrics: [...verificationMetrics],
    nonRetryableMetrics: [...nonRetryableMetrics],
    budgetsRelaxed: false,
  },
  results: printable,
  samples: sampleLedger,
  failures,
  diagnostics,
  accessibilityAuditGaps,
};
writeFileSync(join(outputDir, 'summary.json'), `${JSON.stringify(summaryPayload, null, 2)}\n`);
console.table(printable.map(({ attempt, ...item }) => item));

const verifiedSurfaces = printable.filter((item) => item.verificationTriggered).map((item) => item.id);
const gapEntries = Object.entries(accessibilityAuditGaps).filter(([, audits]) => audits.length);
const accessibilityMarkdown = gapEntries.length
  ? [
      '',
      '#### Diagnóstico de accesibilidad Lighthouse',
      '',
      'Auditorías con score < 1 (diagnóstico; no cambia presupuestos ni política de retry):',
      ...gapEntries.flatMap(([surface, audits]) => [
        `- **${surface}**: ${audits.map((audit) => `${audit.id}=${round(audit.score)}`).join(', ')}`,
        ...audits.slice(0, 6).map((audit) => {
          const selector = audit.items?.map((item) => item?.node?.selector || item?.selector).find(Boolean);
          return `  - ${audit.title}${selector ? ` · \`${String(selector).slice(0, 140)}\`` : ''}`;
        }),
      ]),
    ]
  : [
      '',
      '#### Diagnóstico de accesibilidad Lighthouse',
      '',
      'Todas las auditorías puntuables de accesibilidad obtuvieron score 1.',
    ];

const markdown = [
  '### Lighthouse · performance + accesibilidad',
  '',
  `Estado: **${failures.length ? 'FALLÓ' : 'OK'}** · ${printable.length}/${config.surfaces.length} superficies medidas.`,
  `Browser de laboratorio: **${ciPolicy.lighthouseBrowser || 'no declarado'}**.`,
  `Verificación de outlier: **${aggregation}**, hasta ${maxSamples} muestras solo si el primer fallo pertenece exclusivamente a métricas volátiles autorizadas.`,
  `Superficies verificadas: **${verifiedSurfaces.length ? verifiedSurfaces.join(', ') : 'ninguna'}**.`,
  '',
  '| Superficie | Perf. | A11y | LCP ms | CLS | TBT ms | Bytes | Muestras | Agregación |',
  '|---|---:|---:|---:|---:|---:|---:|---:|---|',
  ...printable.map((item) => `| ${item.id} | ${item.performanceScore} | ${item.accessibilityScore} | ${item.largestContentfulPaintMs} | ${item.cumulativeLayoutShift} | ${item.totalBlockingTimeMs} | ${item.totalByteWeight} | ${item.sampleCount} | ${item.aggregation} |`),
  '',
  `Presupuestos: performance >= ${config.budgets.performanceScoreMin}; a11y >= ${config.budgets.accessibilityScoreMin}; LCP <= ${config.budgets.largestContentfulPaintMsMax} ms; CLS <= ${config.budgets.cumulativeLayoutShiftMax}; TBT <= ${config.budgets.totalBlockingTimeMsMax} ms; transferencia <= ${config.budgets.totalByteWeightMax} B.`,
  '**Los presupuestos no se modifican ni se relajan durante la verificación.**',
  ...accessibilityMarkdown,
  '',
  ...(failures.length ? ['Fallos:', ...failures.map((failure) => `- ${failure}`), ''] : []),
].join('\n');
writeFileSync(join(outputDir, 'summary.md'), `${markdown}\n`);

if (process.env.GITHUB_STEP_SUMMARY) {
  try {
    appendFileSync(process.env.GITHUB_STEP_SUMMARY, `${markdown}\n`, 'utf8');
  } catch (error) {
    console.warn(`No fue posible escribir GITHUB_STEP_SUMMARY: ${error.message}`);
  }
}

if (failures.length) {
  console.error('\nQUALITY V5.5/V5.6 FALLÓ');
  failures.forEach((failure) => console.error(`- ${failure}`));
  for (const [surface, detail] of Object.entries(diagnostics)) {
    console.error(`\nCLS DIAGNÓSTICO · ${surface}`);
    console.error(JSON.stringify(detail, null, 2));
  }
  process.exit(1);
}

console.log(`QUALITY V5.5/V5.6 OK: ${summary.length} superficies cumplen Lighthouse y presupuestos sin relajación.`);
