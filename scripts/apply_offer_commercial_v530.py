#!/usr/bin/env python3
"""v5.30: hace explícita la lógica de contratación de las 16 ofertas sin duplicar su ficha jurídica."""
from __future__ import annotations

from html import escape
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
VERSION = ROOT / "version.json"
CONTRACT = ROOT / "offer-commercial-v530.json"
DETAILS = sorted((ROOT / "servicios").glob("*.html")) + sorted((ROOT / "productos").glob("*.html"))
STYLE = '<link rel="stylesheet" href="../offer-commercial-v530.css">'
START = "<!-- OFFER-COMMERCIAL-V530:START -->"
END = "<!-- OFFER-COMMERCIAL-V530:END -->"
DECISION_START = "<!-- DECISION-V58-DETAIL:START -->"
DECISION_END = "<!-- DECISION-V58-DETAIL:END -->"
META_RE = re.compile(r'(<div class="buying-clarity-meta-v58"[^>]*>.*?</div>)', re.S)


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def ensure_style(text: str) -> str:
    text = re.sub(r'(?m)^[ \t]*' + re.escape(STYLE) + r'[ \t]*(?:\r?\n)?', "", text)
    if "</head>" not in text:
        raise RuntimeError("Ficha sin </head> para cargar offer-commercial-v530.css")
    return text.replace("</head>", f"  {STYLE}\n</head>", 1)


def remove_block(text: str) -> str:
    pattern = re.compile(r'\s*' + re.escape(START) + r'.*?' + re.escape(END) + r'\s*', re.S)
    return pattern.sub("\n", text, count=1)


def load_catalog_ids() -> set[str]:
    ids: set[str] = set()
    for folder in ("catalog-products-v41", "catalog-services-v42"):
        for path in sorted((ROOT / folder).glob("*.json")):
            payload = json.loads(path.read_text(encoding="utf-8"))
            if len(payload) != 1:
                raise RuntimeError(f"{path.name}: se esperaba exactamente una oferta")
            catalog_id = next(iter(payload))
            if catalog_id in ids:
                raise RuntimeError(f"ID de oferta duplicado: {catalog_id}")
            ids.add(catalog_id)
    if len(ids) != 16:
        raise RuntimeError(f"v5.30 esperaba 16 ofertas fuente y encontró {len(ids)}")
    return ids


def load_contract(catalog_ids: set[str]) -> dict[str, dict]:
    payload = json.loads(CONTRACT.read_text(encoding="utf-8"))
    offers = payload.get("offers") or {}
    if payload.get("version") != "5.30.0" or set(offers) != catalog_ids:
        raise RuntimeError("offer-commercial-v530.json debe declarar v5.30.0 y cubrir exactamente las 16 ofertas")
    return offers


def contract_block(catalog_id: str, data: dict) -> str:
    drivers = "".join(
        f'<article class="buying-contract-driver-v530"><strong>{escape(title)}</strong><p>{escape(copy)}</p></article>'
        for title, copy in data["drivers"]
    )
    return f'''{START}
<div class="buying-contract-v530" data-offer-commercial-v530="{escape(catalog_id)}">
  <div class="buying-contract-head-v530">
    <div><span>CONTRATACIÓN SIN LETRA PEQUEÑA</span><h3>Cómo se dimensiona esta oferta antes de presentar una propuesta.</h3><p>La ficha jurídica conserva el perímetro, los entregables, las responsabilidades, las exclusiones y los criterios de aceptación. Este resumen explica cómo esos elementos se traducen en una unidad de contratación y qué puede cambiar el alcance.</p></div>
  </div>
  <div class="buying-contract-grid-v530">
    <article class="buying-contract-card-v530"><span>01 · UNIDAD DE CONTRATACIÓN</span><strong>{escape(data["engagement_basis"])}</strong><p>{escape(data["fee_logic"])}</p></article>
    <article class="buying-contract-card-v530"><span>02 · CIERRE VERIFICABLE</span><strong>Cómo se entiende ejecutado el alcance.</strong><p>{escape(data["close_rule"])}</p></article>
    <article class="buying-contract-card-v530"><span>03 · SI EL ALCANCE CAMBIA</span><strong>Cómo se amplía sin volver abierta la obligación.</strong><p>{escape(data["change_rule"])}</p></article>
  </div>
  <details class="buying-contract-drivers-wrap-v530">
    <summary>Qué variables pueden modificar alcance y honorarios</summary>
    <div class="buying-contract-drivers-v530">{drivers}</div>
  </details>
  <nav class="buying-contract-nav-v530" aria-label="Profundizar en condiciones de contratación">
    <a href="#perimetro-title">Ver perímetro exacto</a><a href="#aceptacion-title">Ver criterios de cierre</a><a href="#contacto">Presentar necesidad</a>
  </nav>
</div>
{END}'''


def patch_page(path: Path, offers: dict[str, dict]) -> str:
    text = remove_block(path.read_text(encoding="utf-8"))
    text = ensure_style(text)
    match = re.search(r'data-catalog-id="([^"]+)"', text)
    if not match:
        raise RuntimeError(f"{path.relative_to(ROOT)}: falta data-catalog-id")
    catalog_id = match.group(1)
    if catalog_id not in offers:
        raise RuntimeError(f"{path.relative_to(ROOT)}: oferta {catalog_id} ausente del contrato v5.30")

    decision_pattern = re.compile(re.escape(DECISION_START) + r'(.*?)' + re.escape(DECISION_END), re.S)
    decision = decision_pattern.search(text)
    if not decision:
        raise RuntimeError(f"{path.relative_to(ROOT)}: falta bloque v5.8 para integrar v5.30")
    inner = decision.group(1)
    if not META_RE.search(inner):
        raise RuntimeError(f"{path.relative_to(ROOT)}: falta buying-clarity-meta-v58")
    inner = META_RE.sub(lambda m: m.group(1) + "\n" + contract_block(catalog_id, offers[catalog_id]), inner, count=1)
    text = text[:decision.start(1)] + inner + text[decision.end(1):]
    if text.count(START) != 1 or text.count(STYLE) != 1:
        raise RuntimeError(f"{path.relative_to(ROOT)}: v5.30 no quedó materializada exactamente una vez")
    path.write_text(text, encoding="utf-8")
    return catalog_id


def validate() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts/validate_offer_commercial_v530.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise RuntimeError((result.stderr or result.stdout).strip())
    if result.stdout.strip():
        print(result.stdout.strip())


def main() -> int:
    version = json.loads(VERSION.read_text(encoding="utf-8")).get("version", "0.0.0")
    if semver(version) < (5, 30, 0):
        return 0
    catalog_ids = load_catalog_ids()
    offers = load_contract(catalog_ids)
    if len(DETAILS) != 16:
        raise RuntimeError(f"v5.30 esperaba 16 fichas profundas y encontró {len(DETAILS)}")
    seen = {patch_page(path, offers) for path in DETAILS}
    if seen != catalog_ids:
        raise RuntimeError(f"v5.30 no cubrió exactamente el catálogo: faltan={sorted(catalog_ids-seen)}")
    validate()
    print("OFFER COMMERCIAL V5.30 OK: 16 fichas con unidad, honorarios, cambios de alcance y cierre verificable explícitos.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
