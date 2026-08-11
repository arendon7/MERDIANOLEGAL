import { appendFileSync } from 'node:fs';

export default class MeridianoCiSummaryReporter {
  constructor() {
    this.latest = new Map();
    this.startedAt = Date.now();
  }

  onTestEnd(test, result) {
    this.latest.set(test.id, {
      status: result.status,
      duration: Number(result.duration || 0),
      retry: Number(result.retry || 0),
    });
  }

  onEnd(fullResult) {
    const counts = { passed: 0, failed: 0, skipped: 0, timedOut: 0, interrupted: 0, other: 0 };
    let durationMs = 0;
    let retried = 0;
    for (const entry of this.latest.values()) {
      durationMs += entry.duration;
      if (entry.retry > 0) retried += 1;
      if (entry.status === 'passed') counts.passed += 1;
      else if (entry.status === 'failed') counts.failed += 1;
      else if (entry.status === 'skipped') counts.skipped += 1;
      else if (entry.status === 'timedOut') counts.timedOut += 1;
      else if (entry.status === 'interrupted') counts.interrupted += 1;
      else counts.other += 1;
    }

    const wallSeconds = Math.max(0, Math.round((Date.now() - this.startedAt) / 1000));
    const lines = [
      '### Browser E2E + axe',
      '',
      '| Métrica | Resultado |',
      '|---|---:|',
      `| Estado global | ${fullResult.status} |`,
      `| Tests observados | ${this.latest.size} |`,
      `| Aprobados | ${counts.passed} |`,
      `| Omitidos | ${counts.skipped} |`,
      `| Fallidos | ${counts.failed + counts.timedOut + counts.interrupted + counts.other} |`,
      `| Tests con reintento | ${retried} |`,
      `| Tiempo de pared reporter | ${wallSeconds} s |`,
      '',
    ];
    const markdown = `${lines.join('\n')}\n`;
    console.log(markdown.trim());

    const summaryPath = process.env.GITHUB_STEP_SUMMARY;
    if (summaryPath) {
      try {
        appendFileSync(summaryPath, markdown, 'utf8');
      } catch (error) {
        console.warn(`No fue posible escribir GITHUB_STEP_SUMMARY: ${error.message}`);
      }
    }
  }
}
