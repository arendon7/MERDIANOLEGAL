#!/usr/bin/env python3
"""Validate v5.11 release topology: Pages must run from canonical builder completion."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / ".github" / "workflows" / "pages.yml"
BUILD = ROOT / ".github" / "workflows" / "build-canonical.yml"
IGNORED_BUILD_MESSAGE = "build: sincroniza sitio público canónico"


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
    build_triggers = trigger_block(build)

    if re.search(r"(?m)^\s{2}push:\s*$", triggers):
        errors.append("pages.yml: Site Quality no debe dispararse directamente por push; debe esperar al builder canónico")

    for fragment in (
        "workflow_dispatch:",
        "workflow_run:",
        'workflows: [\"Build canonical public site\"]',
        "types: [completed]",
    ):
        if fragment not in triggers:
            errors.append(f"pages.yml: falta trigger canónico `{fragment}`")

    if "github.event.workflow_run.conclusion == 'success'" not in pages:
        errors.append("pages.yml: el workflow_run debe exigir builder exitoso")

    if "github.event_name != 'push'" in pages or "github.event.head_commit.message" in pages:
        errors.append("pages.yml: conserva lógica residual del antiguo trigger directo por push")

    if f"!startsWith(github.event.workflow_run.head_commit.message, '{IGNORED_BUILD_MESSAGE}')" not in pages:
        errors.append("pages.yml: quality debe ignorar el workflow_run generado por el commit canónico build:")

    concurrency_match = re.search(r'(?m)^\s*group:\s*"([^"]+)"\s*$', pages)
    if not concurrency_match:
        errors.append("pages.yml: concurrency.group dinámico debe permanecer entre comillas dobles para ser YAML inequívoco")
        concurrency_value = ""
    else:
        concurrency_value = concurrency_match.group(1)
    for fragment in (
        "meridiano-pages-${{",
        "github.event_name == 'workflow_run'",
        f"startsWith(github.event.workflow_run.head_commit.message, '{IGNORED_BUILD_MESSAGE}')",
        "'ignored-build-output'",
        "'main'",
    ):
        if fragment not in concurrency_value:
            errors.append(f"pages.yml: concurrencia debe aislar workflow_run build:; falta {fragment!r}")
    if re.search(r"(?m)^\s*group:\s*meridiano-pages-main\s*$", pages):
        errors.append("pages.yml: un grupo fijo meridiano-pages-main permite que un run ignorado cancele una release válida")
    if "cancel-in-progress: true" not in pages:
        errors.append("pages.yml: releases válidas deben conservar cancel-in-progress para evitar despliegues obsoletos")

    if "Build canonical public site" not in build:
        errors.append("build-canonical.yml: nombre canónico del builder ausente")
    if "workflow_dispatch:" not in build or re.search(r"(?m)^\s{2}push:\s*$", build_triggers) is None:
        errors.append("build-canonical.yml: el builder debe conservar push de fuentes + dispatch manual")
    if "scripts/validate_*.py" not in build_triggers:
        errors.append("build-canonical.yml: el builder debe vigilar todos los validators Python que pueden bloquear Pages")
    if "scripts/apply_search_discovery_v62.py" not in build_triggers:
        errors.append("build-canonical.yml: cambios del materializador Search Discovery v6.2 deben disparar el builder")
    if "git push origin HEAD:main" not in build:
        errors.append("build-canonical.yml: falta publicación de outputs canónicos a main")

    if errors:
        print("PAGES TRIGGER V5.11 FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "PAGES TRIGGER V5.11 OK: Pages espera al builder canónico, aísla los workflow_run build: "
        "y el builder vigila validators + Search Discovery v6.2 antes de publicar."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
