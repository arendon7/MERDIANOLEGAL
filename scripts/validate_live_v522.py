#!/usr/bin/env python3
"""v5.22: espera coherencia real del deploy antes de Browser/Lighthouse.

GitHub Pages puede responder 200 mientras algunos objetos de la nueva publicación aún
no convergen en CDN. Este gate no relaja contratos: exige que portada, fichas profundas
y CSS críticos pertenezcan a la misma generación pública antes de habilitar QA browser.
"""
from __future__ import annotations

from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json
import re
import sys
import time

from validate_live_v53 import BASE, main as validate_v53

R = Path(__file__).resolve().parents[1]
VERSION = json.loads((R / "version.json").read_text(encoding="utf-8")).get("version", "0.0.0")
ATTEMPTS = 8
DELAY_SECONDS = 4


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def fresh_get(path: str, attempt: int) -> str:
    separator = "&" if "?" in path else "?"
    query = urlencode({"v522_coherence": f"{VERSION}-{attempt}"})
    url = BASE + path.lstrip("/") + separator + query
    req = Request(
        url,
        headers={
            "User-Agent": "MeridianoDeployCoherence/5.22",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
        },
    )
    with urlopen(req, timeout=12) as response:
        body = response.read().decode("utf-8", errors="replace")
        if response.status != 200:
            raise RuntimeError(f"{url}: HTTP {response.status}")
        return body


def coherence_checks() -> dict[str, tuple[str, ...]]:
    return {
        "": (
            f"Web pública v{VERSION}",
            'data-home-narrative-v522="true"',
            "CÓMO SE VE EL CRITERIO SENIOR",
            'href="offer-v522.css"',
        ),
        "productos/programa-gobernanza-ia.html": (
            'data-offer-narrative-v522="product-ai"',
            "CAPACIDAD QUE QUEDA INSTALADA",
            "CONPES 4144 de 2025",
            'href="../offer-v522.css"',
        ),
        "servicios/contratacion-estrategica.html": (
            'data-offer-narrative-v522="service-contracts"',
            "Sistema Contractual Empresarial",
            "LENTE JURÍDICA",
            'href="../offer-v522.css"',
        ),
        "offer-v522.css": (
            "OFFER-NARRATIVE-V522:START",
            ".offer-positioning-v522",
            ".offer-legal-lens-v522",
        ),
        "catalog-v32.css": (
            ".detail-hero",
            ".detail-section",
            ".related-grid",
        ),
    }


def wait_for_coherent_generation() -> int:
    checks = coherence_checks()
    last_errors: list[str] = []

    for attempt in range(1, ATTEMPTS + 1):
        errors: list[str] = []
        for path, markers in checks.items():
            try:
                body = fresh_get(path, attempt)
                for marker in markers:
                    if marker not in body:
                        errors.append(f"{path or '/'}: falta {marker!r}")
            except (HTTPError, URLError, TimeoutError, RuntimeError) as exc:
                errors.append(f"{path or '/'}: {exc}")

        if not errors:
            print(
                f"DEPLOY COHERENCE V5.22 OK: {BASE} sirve una generación coherente "
                f"de {VERSION} en portada, 2 fichas profundas y 2 CSS críticos."
            )
            return 0

        last_errors = errors
        if attempt < ATTEMPTS:
            time.sleep(DELAY_SECONDS)

    print("DEPLOY COHERENCE V5.22 FALLIDO", file=sys.stderr)
    for error in last_errors:
        print(f"- {error}", file=sys.stderr)
    return 1


def main() -> int:
    if validate_v53() != 0:
        return 1
    if semver(VERSION) < (5, 22, 0):
        return 0
    return wait_for_coherent_generation()


if __name__ == "__main__":
    raise SystemExit(main())
