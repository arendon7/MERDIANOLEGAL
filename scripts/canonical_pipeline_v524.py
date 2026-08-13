#!/usr/bin/env python3
"""v5.24: única fuente de verdad para el orden de composición canónica pública."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
VERSION_FILE = ROOT / "version.json"


@dataclass(frozen=True)
class Step:
    key: str
    title: str
    command: tuple[str, ...]


def py(script: str) -> tuple[str, ...]:
    return (sys.executable, str(ROOT / "scripts" / script))


def node(script: str) -> tuple[str, ...]:
    return ("node", str(ROOT / "scripts" / script))


CANONICAL_STEPS: tuple[Step, ...] = (
    Step("catalog-shells", "Generate catalog shells", py("build_catalog_shells.py")),
    Step("products-static", "Pre-render product catalog", node("render_catalog_static.mjs")),
    Step("services-static", "Pre-render service catalog v4.2", node("render_services_v42.mjs")),
    Step("editorial-enrich", "Enrich editorial pages", py("enrich_editorial_pages.py")),
    Step("commercial-v44", "Apply commercial and conversion system v4.4", py("apply_commercial_v43.py")),
    Step("visual-canonical", "Apply canonical visual system", py("apply_visual_assets.py")),
    Step("ux-v45", "Apply homepage UX/UI v4.5", py("apply_ux_v45.py")),
    Step("detail-v46", "Apply deep-page UX/UI v4.6", py("apply_detail_ux_v46.py")),
    Step("editorial-v47", "Apply editorial and demo UX/UI v4.7", py("apply_editorial_ux_v47.py")),
    Step("editorial-normalize-v47", "Normalize editorial UX/UI v4.7", py("normalize_editorial_v47.py")),
    Step("growth-compat-v51", "Normalize growth compatibility v5.1", py("normalize_growth_compat_v51.py")),
    Step("quality-v48", "Apply final quality polish v4.8", py("apply_quality_v48.py")),
    Step("quality-normalize-v48", "Normalize final quality v4.8", py("normalize_quality_v48.py")),
    Step("operations-v49", "Apply public operations v4.9", py("apply_operations_v49.py")),
    Step("public-version", "Synchronize visible public version", py("sync_public_version.py")),
    Step("production-v50", "Apply production configuration v5.0", py("apply_production_v50.py")),
    Step("growth-v51", "Apply growth and decision-entry system v5.1", py("apply_growth_v51.py")),
    Step("growth-finalize-v51", "Finalize growth and decision-entry system v5.1", py("finalize_growth_v51.py")),
    Step("cro-v52", "Apply CRO and search-intent system v5.2", py("apply_cro_v52.py")),
    Step("authority-v53", "Apply authority, discovery and measurement system v5.3", py("apply_authority_v53.py")),
    Step("decision-v58", "Apply buying decision architecture v5.8", py("apply_decision_v58.py")),
    Step("intake-v59", "Apply commercial intake and proposal handoff v5.9", py("apply_commercial_v59.py")),
    Step("close-v510", "Apply conversion-to-close architecture v5.10", py("apply_conversion_v510.py")),
    Step("engagement-v511", "Apply engagement readiness v5.11", py("apply_engagement_v511.py")),
    Step("proof-v512", "Apply verifiable proof and modality guidance v5.12", py("apply_proof_v512.py")),
    Step("brief-v513", "Apply commercial brief continuity v5.13", py("apply_commercial_brief_v513.py")),
    Step("recommendation-v514", "Apply explainable modality recommendation v5.14", py("apply_recommendation_v514.py")),
    Step("decision-action-v515", "Apply decision-to-action efficiency v5.15", py("apply_decision_action_v515.py")),
    Step("handoff-v517", "Apply manual handoff continuity v5.17", py("apply_handoff_v517.py")),
    Step("handoff-observability-v518-plus", "Apply handoff observability and canonical extensions v5.18+", py("apply_handoff_observability_v518.py")),
)


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def validate_manifest() -> None:
    version = json.loads(VERSION_FILE.read_text(encoding="utf-8")).get("version", "0.0.0")
    if semver(version) < (5, 24, 0):
        raise SystemExit("CANONICAL PIPELINE V5.24 FAIL: version.json debe declarar v5.24+")
    keys = [step.key for step in CANONICAL_STEPS]
    if len(keys) != len(set(keys)):
        raise SystemExit("CANONICAL PIPELINE V5.24 FAIL: existen claves de paso duplicadas")
    if len(CANONICAL_STEPS) != 30:
        raise SystemExit(f"CANONICAL PIPELINE V5.24 FAIL: se esperaban 30 pasos y hay {len(CANONICAL_STEPS)}")
    if CANONICAL_STEPS[-1].key != "handoff-observability-v518-plus":
        raise SystemExit("CANONICAL PIPELINE V5.24 FAIL: la extensión canónica final debe permanecer en v5.18+")
    for step in CANONICAL_STEPS:
        target = step.command[-1]
        if target.endswith((".py", ".mjs")) and not Path(target).exists():
            raise SystemExit(f"CANONICAL PIPELINE V5.24 FAIL: falta {target}")


def run_pipeline() -> int:
    validate_manifest()
    print(f"CANONICAL PIPELINE V5.24: {len(CANONICAL_STEPS)} pasos, una única secuencia declarada.")
    for index, step in enumerate(CANONICAL_STEPS, start=1):
        print(f"[{index:02d}/{len(CANONICAL_STEPS)}] {step.key} · {step.title}", flush=True)
        completed = subprocess.run(step.command, cwd=ROOT)
        if completed.returncode:
            raise SystemExit(
                f"CANONICAL PIPELINE V5.24 FAIL: paso {index} ({step.key}) terminó con {completed.returncode}"
            )
    print("CANONICAL PIPELINE V5.24 OK: composición completa ejecutada sin rutas alternativas.")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    mode = args[0] if args else "apply"
    if mode == "apply":
        return run_pipeline()
    if mode == "validate":
        validate_manifest()
        print("CANONICAL PIPELINE V5.24 MANIFEST OK")
        return 0
    if mode == "list":
        for index, step in enumerate(CANONICAL_STEPS, start=1):
            print(f"{index:02d}\t{step.key}\t{step.title}\t{' '.join(step.command)}")
        return 0
    raise SystemExit(f"uso: {Path(sys.argv[0]).name} [apply|validate|list]")


if __name__ == "__main__":
    raise SystemExit(main())
