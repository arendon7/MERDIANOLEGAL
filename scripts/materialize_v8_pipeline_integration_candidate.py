#!/usr/bin/env python3
"""Materialize W4.7 integrated Builder/Pages candidates in a disposable repo copy.

The real branch workflows are deliberately never rewritten by this script. It
requires a different --root and applies exact, fail-closed textual transforms to
copies of the production workflows.
"""
from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    raise AssertionError(message)


def digest_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def replace_once(value: str, old: str, new: str, label: str) -> str:
    count = value.count(old)
    if count != 1:
        fail(f"{label}: expected exactly one anchor, found {count}")
    return value.replace(old, new, 1)


def patch_builder(value: str) -> str:
    if "MERIDIANO_V8_PIPELINE_COMPAT" in value or "apply_v8_builder_compat.py" in value:
        fail("builder already contains v8 integration markers")

    value = replace_once(
        value,
        "      - .gitignore\n",
        "      - practicas/**\n"
        "      - servicios-continuos/**\n"
        "      - soluciones/**\n"
        "      - scripts/apply_v8_builder_compat.py\n"
        "      - scripts/run_v8_pages_quality_compat.py\n"
        "      - .gitignore\n",
        "builder trigger paths",
    )

    npm = "          npm install --package-lock-only --ignore-scripts --no-audit --no-fund\n"
    integration = npm + (
        "          if [ -f assets/data/v8/pipeline-compat-v80.json ] && "
        "[ -f soluciones/sistema-contractual-empresarial.html ] && "
        "[ -f practicas/corporativo-societario-gobierno.html ] && "
        "[ -f servicios-continuos/direccion-juridica-externa.html ]; then\n"
        "            echo 'MERIDIANO_V8_PIPELINE_COMPAT=true' >> \"$GITHUB_ENV\"\n"
        "            python3 scripts/apply_v8_builder_compat.py\n"
        "          else\n"
        "            echo 'MERIDIANO_V8_PIPELINE_COMPAT=false' >> \"$GITHUB_ENV\"\n"
        "          fi\n"
    )
    value = replace_once(value, npm, integration, "builder adapter integration")

    value = replace_once(
        value,
        "      - name: Synchronize visible public version\n"
        "        run: python3 scripts/sync_public_version.py\n",
        "      - name: Synchronize visible public version\n"
        "        if: env.MERIDIANO_V8_PIPELINE_COMPAT != 'true'\n"
        "        run: python3 scripts/sync_public_version.py\n",
        "builder public version step",
    )

    value = replace_once(
        value,
        "      - name: Apply handoff observability v5.18 + canonical extensions\n"
        "        run: |\n",
        "      - name: Apply handoff observability v5.18 + canonical extensions\n"
        "        if: env.MERIDIANO_V8_PIPELINE_COMPAT != 'true'\n"
        "        run: |\n",
        "builder canonical extension step",
    )
    return value


def patch_pages(value: str) -> str:
    if "MERIDIANO_V8_PIPELINE_COMPAT" in value or "apply_v8_builder_compat.py" in value:
        fail("Pages already contains v8 integration markers")

    start = (
        "      - name: Check canonical generators are idempotent\n"
        "        run: |\n"
    )
    integrated_start = start + (
        "          if [ -f assets/data/v8/pipeline-compat-v80.json ] && "
        "[ -f soluciones/sistema-contractual-empresarial.html ] && "
        "[ -f practicas/corporativo-societario-gobierno.html ] && "
        "[ -f servicios-continuos/direccion-juridica-externa.html ]; then\n"
        "            echo 'MERIDIANO_V8_PIPELINE_COMPAT=true' >> \"$GITHUB_ENV\"\n"
        "            python3 scripts/apply_v8_builder_compat.py --check\n"
        "          else\n"
        "            echo 'MERIDIANO_V8_PIPELINE_COMPAT=false' >> \"$GITHUB_ENV\"\n"
    )
    value = replace_once(value, start, integrated_start, "Pages adapter integration")

    diff_line = (
        "          git diff --exit-code -- index.html catalog-home-v32.js decision-flow.js "
        "site-v3.js page-context.js sitemap.xml robots.txt runtime-config.js site-status.json "
        "servicios productos firma.html perspectivas perspectivas.html sectores soluciones "
        "experiencia.html demo.html 404.html aviso-legal.html privacidad.html terminos.html "
        "manifest.webmanifest CNAME scripts/build_catalog_shells.py\n"
    )
    value = replace_once(value, diff_line, "          fi\n" + diff_line, "Pages canonical check close")

    growth = (
        "      - name: Validate growth and decision routes v5.1\n"
        "        run: python3 scripts/validate_growth_v51.py\n"
    )
    growth_integrated = (
        "      - name: Validate growth and decision routes v5.1\n"
        "        run: |\n"
        "          if [ \"$MERIDIANO_V8_PIPELINE_COMPAT\" = \"true\" ]; then\n"
        "            python3 scripts/validate_v8_pipeline_compat.py\n"
        "          else\n"
        "            python3 scripts/validate_growth_v51.py\n"
        "          fi\n"
    )
    value = replace_once(value, growth, growth_integrated, "Pages Growth compatibility")
    return value


def main(argv: list[str] | None = None) -> int:
    parser = ArgumentParser()
    parser.add_argument("--root", required=True, help="Disposable repository root to patch")
    args = parser.parse_args(argv)

    target_root = Path(args.root).resolve()
    if target_root == ROOT.resolve():
        fail("W4.7 materializer refuses to patch the active repository checkout")
    builder = target_root / ".github/workflows/build-canonical.yml"
    pages = target_root / ".github/workflows/pages.yml"
    if not builder.exists() or not pages.exists():
        fail("target root does not contain canonical Builder and Pages workflows")

    original_builder = builder.read_text(encoding="utf-8")
    original_pages = pages.read_text(encoding="utf-8")
    integrated_builder = patch_builder(original_builder)
    integrated_pages = patch_pages(original_pages)
    builder.write_text(integrated_builder, encoding="utf-8")
    pages.write_text(integrated_pages, encoding="utf-8")

    manifest = {
        "contract": "v8-pipeline-integration-materialization",
        "status": "candidate",
        "builder_before": digest_text(original_builder),
        "builder_after": digest_text(integrated_builder),
        "pages_before": digest_text(original_pages),
        "pages_after": digest_text(integrated_pages),
        "production_checkout_touched": False,
    }
    (target_root / ".v8-pipeline-integration-candidate.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print("MATERIALIZE V8 PIPELINE INTEGRATION CANDIDATE OK: Builder + Pages patched only in disposable root.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, json.JSONDecodeError) as exc:
        print(f"MATERIALIZE V8 PIPELINE INTEGRATION CANDIDATE FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
