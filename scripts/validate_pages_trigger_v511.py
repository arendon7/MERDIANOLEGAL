#!/usr/bin/env python3
"""Validate v5.11 release topology: Pages must run from canonical builder completion."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / ".github" / "workflows" / "pages.yml"
BUILD = ROOT / ".github" / "workflows" / "build-canonical.yml"


def trigger_block(text: str) -> str:
    match = re.search(r"(?ms)^on:\n(.*?)(?=^concurrency:)", text)
    if not match:
        raise RuntimeError("pages.yml: no se pudo localizar el bloque on")
    return match.group(1)


def main() -> int:
    errors: list[str] = []
    pages = PAGES.read_text(encoding="utf-8")
    build = BUILD.read_text(encoding="utf-8")
    triggers = trigger_block(pages)

    if re.search(r"(?m)^\s{2}push:\s*$", triggers):
        errors.append("pages.yml: Site Quality no debe dispararse directamente por push; debe esperar al builder canónico")

    for fragment in (
        "workflow_dispatch:",
        "workflow_run:",
        'workflows: ["Build canonical public site"]',
        "types: [completed]",
    ):
        if fragment not in triggers:
            errors.append(f"pages.yml: falta trigger canónico `{fragment}`")

    if "github.event.workflow_run.conclusion == 'success'" not in pages:
        errors.append("pages.yml: el workflow_run debe exigir builder exitoso")

    if "github.event_name != 'push'" in pages or "github.event.head_commit.message" in pages:
        errors.append("pages.yml: conserva lógica residual del antiguo trigger directo por push")

    if "Build canonical public site" not in build:
        errors.append("build-canonical.yml: nombre canónico del builder ausente")
    if "workflow_dispatch:" not in build or re.search(r"(?m)^\s{2}push:\s*$", trigger_block(build)) is None:
        errors.append("build-canonical.yml: el builder debe conservar push de fuentes + dispatch manual")
    if "git push origin HEAD:main" not in build:
        errors.append("build-canonical.yml: falta publicación de outputs canónicos a main")

    if errors:
        print("PAGES TRIGGER V5.11 FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PAGES TRIGGER V5.11 OK: Pages espera al builder canónico; sin carrera directa por push.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
