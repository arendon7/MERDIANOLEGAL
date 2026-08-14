#!/usr/bin/env python3
"""Valida el contrato v5.30 de profundidad comercial de las 16 ofertas."""
from __future__ import annotations

from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
VERSION = ROOT / "version.json"
CONTRACT = ROOT / "offer-commercial-v530.json"
DETAILS = sorted((ROOT / "servicios").glob("*.html")) + sorted((ROOT / "productos").glob("*.html"))
START = "<!-- OFFER-COMMERCIAL-V530:START -->"
END = "<!-- OFFER-COMMERCIAL-V530:END -->"
STYLE = '<link rel="stylesheet" href="../offer-commercial-v530.css">'
REQUIRED = ("engagement_basis", "fee_logic", "drivers", "change_rule", "close_rule")
FORBIDDEN_PRICE = re.compile(r'(?:\$|€|£|\bCOP\b|\bUSD\b|\bEUR\b|\b(?:precio|tarifa)\s*[:=]\s*\d)', re.I)


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def source_ids() -> set[str]:
    ids: set[str] = set()
    for folder in ("catalog-products-v41", "catalog-services-v42"):
        for path in sorted((ROOT / folder).glob("*.json")):
            payload = json.loads(path.read_text(encoding="utf-8"))
            if len(payload) != 1:
                raise AssertionError(f"{path.name}: fuente debe contener una sola oferta")
            catalog_id = next(iter(payload))
            if catalog_id in ids:
                raise AssertionError(f"ID duplicado: {catalog_id}")
            ids.add(catalog_id)
    return ids


def validate_contract() -> set[str]:
    payload = json.loads(CONTRACT.read_text(encoding="utf-8"))
    assert payload.get("version") == "5.30.0", "contrato v5.30 con versión incorrecta"
    principles = payload.get("principles") or {}
    assert principles.get("no_automatic_quote") is True, "v5.30 debe prohibir cotización automática"
    ids = source_ids()
    assert len(ids) == 16, f"se esperaban 16 ofertas fuente y hay {len(ids)}"
    offers = payload.get("offers") or {}
    assert set(offers) == ids, f"contrato desalineado: faltan={sorted(ids-set(offers))}, extra={sorted(set(offers)-ids)}"
    for catalog_id, entry in offers.items():
        missing = [key for key in REQUIRED if not entry.get(key)]
        assert not missing, f"{catalog_id}: faltan campos {missing}"
        drivers = entry["drivers"]
        assert isinstance(drivers, list) and len(drivers) == 3, f"{catalog_id}: deben existir exactamente 3 drivers"
        for driver in drivers:
            assert isinstance(driver, list) and len(driver) == 2 and all(str(x).strip() for x in driver), f"{catalog_id}: driver inválido"
        serialized = json.dumps(entry, ensure_ascii=False)
        assert not FORBIDDEN_PRICE.search(serialized), f"{catalog_id}: v5.30 no puede publicar precio o moneda"
        assert "honorarios" in entry["fee_logic"].lower(), f"{catalog_id}: fee_logic debe explicar honorarios"
    return ids


def validate_pages(ids: set[str]) -> None:
    assert len(DETAILS) == 16, f"se esperaban 16 fichas HTML y hay {len(DETAILS)}"
    seen: set[str] = set()
    for path in DETAILS:
        text = path.read_text(encoding="utf-8")
        match = re.search(r'data-catalog-id="([^"]+)"', text)
        assert match, f"{path.name}: falta data-catalog-id"
        catalog_id = match.group(1)
        seen.add(catalog_id)
        assert catalog_id in ids, f"{path.name}: ID desconocido {catalog_id}"
        assert text.count(START) == 1 and text.count(END) == 1, f"{path.name}: bloque v5.30 no es único"
        assert text.count(STYLE) == 1, f"{path.name}: CSS v5.30 debe cargarse una vez"
        assert text.count(f'data-offer-commercial-v530="{catalog_id}"') == 1, f"{path.name}: binding v5.30 incorrecto"
        decision_start = text.find("<!-- DECISION-V58-DETAIL:START -->")
        decision_end = text.find("<!-- DECISION-V58-DETAIL:END -->")
        block_start = text.find(START)
        meta = text.find('class="buying-clarity-meta-v58"')
        assert -1 not in (decision_start, decision_end, block_start, meta), f"{path.name}: falta arquitectura v5.8/v5.30"
        assert decision_start < meta < block_start < decision_end, f"{path.name}: v5.30 debe extender el resumen v5.8 después de meta"
        assert text.count('href="#perimetro-title"') >= 1, f"{path.name}: falta enlace a perímetro"
        assert text.count('href="#aceptacion-title"') >= 1, f"{path.name}: falta enlace a aceptación"
        assert text.count('href="#contacto"') >= 1, f"{path.name}: falta enlace a contacto"
        assert 'id="perimetro-title"' in text, f"{path.name}: falta destino perímetro"
        assert 'id="aceptacion-title"' in text, f"{path.name}: falta destino aceptación"
        assert 'id="contacto"' in text, f"{path.name}: falta contacto canónico"
        assert text.count('class="buying-contract-driver-v530"') == 3, f"{path.name}: deben materializarse 3 drivers"
        assert "Qué variables pueden modificar alcance y honorarios" in text, f"{path.name}: falta transparencia de dimensionamiento"
        assert not FORBIDDEN_PRICE.search(text[text.find(START):text.find(END)+len(END)]), f"{path.name}: bloque v5.30 contiene precio/moneda"
    assert seen == ids, f"fichas v5.30 desalineadas: faltan={sorted(ids-seen)}"


def main() -> int:
    version = json.loads(VERSION.read_text(encoding="utf-8")).get("version", "0.0.0")
    if semver(version) < (5, 30, 0):
        return 0
    try:
        ids = validate_contract()
        validate_pages(ids)
    except (AssertionError, json.JSONDecodeError) as exc:
        print(f"OFFER COMMERCIAL V5.30 FAIL: {exc}", file=sys.stderr)
        return 1
    print("OFFER COMMERCIAL V5.30 PASS: contrato + 16 fichas + honorarios sin tarifas inventadas + cierre y cambios de alcance verificables.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
