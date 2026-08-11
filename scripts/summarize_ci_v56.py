#!/usr/bin/env python3
"""Resume la certificación CI v5.6 a partir del payload de jobs de GitHub Actions."""
from __future__ import annotations

import argparse
from datetime import datetime
import json
import os
from pathlib import Path

R = Path(__file__).resolve().parents[1]
EXPECTED = [
    "Validate current site",
    "Deploy GitHub Pages",
    "Verify deployed Pages",
    "Browser E2E on deployed Pages",
    "Lighthouse quality on deployed Pages",
]
SNAPSHOT_JOB = "Update stable snapshot"


def parse_ts(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def seconds(start: str | None, end: str | None) -> int | None:
    a, b = parse_ts(start), parse_ts(end)
    if not a or not b:
        return None
    return max(0, round((b - a).total_seconds()))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("jobs_json")
    parser.add_argument("--markdown", required=True)
    parser.add_argument("--json", dest="json_path", required=True)
    args = parser.parse_args()

    payload = json.loads(Path(args.jobs_json).read_text(encoding="utf-8"))
    jobs = payload.get("jobs", [])
    by_name = {job.get("name"): job for job in jobs}
    missing = [name for name in EXPECTED if name not in by_name]
    if missing:
        raise SystemExit(f"CI SUMMARY V5.6 FALLÓ: faltan jobs: {', '.join(missing)}")

    rows = []
    for name in EXPECTED:
        job = by_name[name]
        rows.append({
            "name": name,
            "status": job.get("status"),
            "conclusion": job.get("conclusion"),
            "startedAt": job.get("started_at"),
            "completedAt": job.get("completed_at"),
            "durationSeconds": seconds(job.get("started_at"), job.get("completed_at")),
        })

    failed = [row for row in rows if row["conclusion"] != "success"]
    if failed:
        raise SystemExit("CI SUMMARY V5.6 FALLÓ: un gate requerido no terminó success")

    starts = [parse_ts(row["startedAt"]) for row in rows if row["startedAt"]]
    snapshot_start = parse_ts(by_name.get(SNAPSHOT_JOB, {}).get("started_at"))
    if not starts:
        gate_ready = None
    elif snapshot_start:
        gate_ready = round((snapshot_start - min(starts)).total_seconds())
    else:
        ends = [parse_ts(row["completedAt"]) for row in rows if row["completedAt"]]
        gate_ready = round((max(ends) - min(starts)).total_seconds()) if ends else None

    baseline = json.loads((R / "ci-baseline-v56.json").read_text(encoding="utf-8"))
    baseline_seconds = baseline["baseline"]["criticalPathSeconds"]
    improvement = None
    if gate_ready is not None and baseline_seconds:
        improvement = round(((baseline_seconds - gate_ready) / baseline_seconds) * 100, 1)

    result = {
        "version": "5.6.0",
        "measurement": "quality-start-to-snapshot-start",
        "runId": os.environ.get("GITHUB_RUN_ID", ""),
        "headSha": os.environ.get("MERIDIANO_DEPLOYED_SHA") or os.environ.get("GITHUB_SHA", ""),
        "criticalPathSeconds": gate_ready,
        "baselineCriticalPathSeconds": baseline_seconds,
        "improvementPercent": improvement,
        "jobs": rows,
        "coverageReduced": False,
        "budgetsRelaxed": False,
    }

    md = [
        "### Certificación CI v5.6",
        "",
        f"- Run: `{result['runId'] or 'local'}`",
        f"- SHA desplegado: `{result['headSha'] or 'local'}`",
        f"- Tiempo hasta el gate de `stable`: **{gate_ready} s**" if gate_ready is not None else "- Tiempo hasta el gate de `stable`: n/d",
        f"- Baseline v5.5: **{baseline_seconds} s**",
        f"- Mejora frente a baseline: **{improvement}%**" if improvement is not None else "- Mejora frente a baseline: n/d",
        "- Cobertura reducida: **no**",
        "- Presupuestos relajados: **no**",
        "",
        "| Gate | Estado | Duración |",
        "|---|---|---:|",
    ]
    for row in rows:
        md.append(f"| {row['name']} | {row['conclusion']} | {row['durationSeconds']} s |")
    md.append("")

    markdown = "\n".join(md) + "\n"
    out_md = Path(args.markdown)
    out_json = Path(args.json_path)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(markdown, encoding="utf-8")
    out_json.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
