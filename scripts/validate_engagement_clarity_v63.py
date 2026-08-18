#!/usr/bin/env python3
"""Valida Engagement Clarity v6.3 contra los 16 catálogos canónicos."""
from __future__ import annotations

from html import escape
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets" / "data" / "v6" / "engagement-clarity-v63.json"
CATALOG_DIRS = (ROOT / "catalog-products-v41", ROOT / "catalog-services-v42")
DETAIL_DIRS = (ROOT / "productos", ROOT / "servicios")
START = "<!-- ENGAGEMENT-CLARITY-V63:START -->"
END = "<!-- ENGAGEMENT-CLARITY-V63:END -->"
CSS_HREF = "../assets/css/v6/engagement-clarity-v63.css"


def e(value: object) -> str:
    return escape(str(value), quote=True)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def body_attr(text: str, name: str) -> str:
    match = re.search(rf'<body\b[^>]*\b{name}="([^"]*)"', text)
    return match.group(1) if match else ""


def load_sources(errors: list[str]) -> dict[str, dict]:
    sources: dict[str, dict] = {}
    for folder in CATALOG_DIRS:
        files = sorted(folder.glob("*.json"))
        if len(files) != 8:
            errors.append(f"{folder.name}: se esperaban 8 fuentes y hay {len(files)}")
        for path in files:
            try:
                payload = load_json(path)
            except Exception as exc:
                errors.append(f"{path.name}: JSON inválido: {exc}")
                continue
            if len(payload) != 1:
                errors.append(f"{path.name}: debe declarar exactamente un catalog_id")
                continue
            catalog_id, source = next(iter(payload.items()))
            sources[catalog_id] = source
            for field in ("requirements", "responsibilities"):
                matrix = source.get(field)
                if not isinstance(matrix, list) or not matrix:
                    errors.append(f"{path.name}: {field} debe ser una matriz no vacía")
                    continue
                for idx, row in enumerate(matrix, 1):
                    if not isinstance(row, list) or len(row) != 2 or not all(isinstance(item, str) and item.strip() for item in row):
                        errors.append(f"{path.name}: {field}[{idx}] debe contener [título, explicación]")
    return sources


def extract_group(block: str, group: str) -> list[tuple[str, str]] | None:
    match = re.search(
        rf'<article class="v63-engagement-panel" data-engagement-group="{group}">(.*?)</article>',
        block,
        flags=re.S,
    )
    if not match:
        return None
    return re.findall(
        r'<div class="v63-engagement-row"><dt>(.*?)</dt><dd>(.*?)</dd></div>',
        match.group(1),
        flags=re.S,
    )


def main() -> int:
    errors: list[str] = []
    if not CONTRACT.exists():
        errors.append("falta assets/data/v6/engagement-clarity-v63.json")
        contract = {}
    else:
        try:
            contract = load_json(CONTRACT)
        except Exception as exc:
            errors.append(f"contrato v6.3 inválido: {exc}")
            contract = {}

    if contract.get("version") != "6.3.0":
        errors.append("el contrato Engagement Clarity debe declarar version 6.3.0")
    scope = contract.get("scope", {})
    if scope.get("detail_pages") != 16 or scope.get("products") != 8 or scope.get("services") != 8:
        errors.append("el contrato debe fijar exactamente 16 fichas = 8 productos + 8 servicios")
    required_fields = contract.get("source_of_truth", {}).get("required_fields")
    if required_fields != ["requirements", "responsibilities"]:
        errors.append("source_of_truth.required_fields debe ser exactamente requirements + responsibilities")

    sources = load_sources(errors)
    if len(sources) != 16:
        errors.append(f"se esperaban 16 fuentes canónicas y hay {len(sources)}")

    pages: dict[str, Path] = {}
    detail_paths = sorted(path for folder in DETAIL_DIRS for path in folder.glob("*.html"))
    if len(detail_paths) != 16:
        errors.append(f"se esperaban 16 fichas HTML y hay {len(detail_paths)}")
    for path in detail_paths:
        text = path.read_text(encoding="utf-8")
        catalog_id = body_attr(text, "data-catalog-id")
        if not catalog_id:
            errors.append(f"{path.relative_to(ROOT)}: falta data-catalog-id")
            continue
        if catalog_id in pages:
            errors.append(f"data-catalog-id duplicado: {catalog_id}")
        pages[catalog_id] = path

    if set(sources) != set(pages):
        errors.append(
            f"source/HTML desalineados: sin HTML={sorted(set(sources)-set(pages))}; "
            f"sin fuente={sorted(set(pages)-set(sources))}"
        )

    for catalog_id in sorted(set(sources) & set(pages)):
        path = pages[catalog_id]
        source = sources[catalog_id]
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()

        if text.count(CSS_HREF) != 1:
            errors.append(f"{rel}: debe cargar exactamente una hoja v6.3")
        if text.count('data-engagement-clarity-v63-nav="true"') != 1:
            errors.append(f"{rel}: debe tener exactamente una ancla Para empezar")
        if text.count('href="#v6-engagement"') != 1:
            errors.append(f"{rel}: la navegación debe apuntar una vez a #v6-engagement")
        if text.count(START) != 1 or text.count(END) != 1:
            errors.append(f"{rel}: marcadores v6.3 deben ser únicos")
            continue

        managed = re.search(re.escape(START) + r'(.*?)' + re.escape(END), text, flags=re.S)
        if not managed:
            errors.append(f"{rel}: no se pudo extraer bloque v6.3")
            continue
        block = managed.group(1)
        if block.count('data-engagement-clarity-v63="true"') != 1:
            errors.append(f"{rel}: debe existir una única sección Engagement Clarity")
        if f'data-engagement-catalog-id="{e(catalog_id)}"' not in block:
            errors.append(f"{rel}: catalog_id visible no coincide con la fuente")
        if 'id="v6-engagement"' not in block:
            errors.append(f"{rel}: falta id #v6-engagement")

        for group, field in (("requirements", "requirements"), ("responsibilities", "responsibilities")):
            actual = extract_group(block, group)
            expected = [(e(label), e(copy)) for label, copy in source[field]]
            if actual is None:
                errors.append(f"{rel}: falta panel {group}")
            elif actual != expected:
                errors.append(f"{rel}: panel {group} diverge del truth canónico")

        boundary_pos = text.find('id="v6-boundary"')
        engagement_pos = text.find('id="v6-engagement"')
        close_pos = text.find('class="v6-section v6-detail-close"')
        if min(boundary_pos, engagement_pos, close_pos) < 0 or not (engagement_pos < boundary_pos < close_pos):
            errors.append(f"{rel}: Engagement Clarity debe quedar antes de límites y del cierre")

    forbidden = ("garantiza", "certifica cumplimiento", "éxito asegurado", "cliente convertido")
    for path in detail_paths:
        text = path.read_text(encoding="utf-8")
        match = re.search(re.escape(START) + r'(.*?)' + re.escape(END), text, flags=re.S)
        if not match:
            continue
        lowered = match.group(1).lower()
        for phrase in forbidden:
            if phrase in lowered:
                errors.append(f"{path.relative_to(ROOT)}: v6.3 no debe introducir claim {phrase!r}")

    if errors:
        print("VALIDACIÓN ENGAGEMENT CLARITY V6.3 FALLIDA", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("VALIDACIÓN ENGAGEMENT CLARITY V6.3 OK: 16/16 fichas reproducen requirements y responsibilities canónicos; navegación, orden e invariantes íntegros.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
