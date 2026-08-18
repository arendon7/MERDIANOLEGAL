#!/usr/bin/env python3
"""Valida Wave 3 v6: seis rutas de necesidad + hub, con truth Growth/CRO y legado v5.31."""
from __future__ import annotations

from html import unescape
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
GROWTH = ROOT / "growth-solutions-v51.json"
CRO = ROOT / "cro-solutions-v52.json"
SOLUTIONS = ROOT / "soluciones"

START = "<!-- EXPERIENCE-V60-SOLUTION:START -->"
END = "<!-- EXPERIENCE-V60-SOLUTION:END -->"
HUB_START = "<!-- EXPERIENCE-V60-SOLUTION-HUB:START -->"
HUB_END = "<!-- EXPERIENCE-V60-SOLUTION-HUB:END -->"
LEGACY_START = "<!-- EXPERIENCE-V60-SOLUTION-LEGACY:START -->"
LEGACY_END = "<!-- EXPERIENCE-V60-SOLUTION-LEGACY:END -->"
STYLE_PATHS = [
    "../assets/css/v6/tokens.css",
    "../assets/css/v6/base.css",
    "../assets/css/v6/components.css",
    "../assets/css/v6/surfaces.css",
    "../assets/css/v6/solutions.css",
]


def fail(message: str) -> None:
    raise AssertionError(message)


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(text(path))


def assert_contains(value: str, needles: list[str], label: str) -> None:
    missing = [item for item in needles if item not in value]
    if missing:
        fail(f"{label}: faltan {missing[:8]}" + (f" (+{len(missing)-8})" if len(missing) > 8 else ""))


def assert_once(value: str, needle: str, label: str) -> None:
    count = value.count(needle)
    if count != 1:
        fail(f"{label}: esperaba una ocurrencia de {needle!r} y encontró {count}")


def legacy(value: str, label: str) -> str:
    match = re.search(re.escape(LEGACY_START) + r"(.*?)" + re.escape(LEGACY_END), value, flags=re.S)
    if not match:
        fail(f"{label}: falta profundidad legacy")
    return match.group(1)


def first_layer(value: str, start_marker: str, label: str) -> str:
    start = value.find(start_marker)
    end = value.find(LEGACY_START, start + len(start_marker)) if start >= 0 else -1
    if start < 0 or end < 0:
        fail(f"{label}: no se pudo aislar la primera capa")
    return unescape(value[start:end])


def validate_route(slug: str, growth: dict, cro: dict) -> None:
    path = SOLUTIONS / f"{slug}.html"
    if not path.exists():
        fail(f"falta {path.name}")
    value = text(path)
    assert_contains(value, [
        'data-experience-system="v6"', 'data-experience-wave="solutions"',
        f'data-experience-surface="solution:{slug}"', f'data-experience-v60="solution:{slug}"',
    ], slug)
    for href in STYLE_PATHS:
        assert_once(value, f'href="{href}"', f"{slug}: estilos")
    assert_once(value, START, f"{slug}: marker")
    assert_once(value, END, f"{slug}: marker")
    if re.search(r"<form\b", value):
        fail(f"{slug}: una ruta de necesidad no debe crear formulario")

    first = first_layer(value, START, slug)
    primary = [growth["title"], growth["description"], growth["intent"], growth["limits"], cro["decision_label"], cro["decision_copy"], cro["pricing"]["title"], cro["pricing"]["copy"], cro["cta_title"], cro["cta_copy"]]
    primary.extend(growth["signals"])
    primary.extend(growth["questions"])
    primary.extend(growth["deliverables"])
    primary.extend(cro["fit"])
    primary.extend(cro["not_fit"])
    for route in growth["routes"]:
        primary.extend([route["name"], route["summary"], route["href"]])
    primary.extend([growth["perspective"]["name"], growth["perspective"]["href"], growth["sector"]["name"], growth["sector"]["href"]])
    assert_contains(first, primary, f"{slug}: primera capa Growth/CRO")

    old = legacy(value, slug)
    for key in ("objections", "faq", "related", "proof"):
        assert_once(old, f'data-decision-compression-v531="solution-{key}"', f"{slug}: legacy {key}")
    assert_contains(old, [
        "CRO-V52-OBJECTIONS:START", "CRO-V52-FAQ:START", "CRO-V52-RELATED:START",
        "growth-proof-page-v51", "CRO-V52-PRICING:START", "RESULTADO ESPERADO", "LÍMITES",
    ], f"{slug}: legacy v5.31")
    for opening in re.findall(r'<details[^>]*data-decision-compression-v531="solution-[^"]+"[^>]*>', old):
        if re.search(r'\b(open|hidden)\b', opening):
            fail(f"{slug}: disclosure histórico debe iniciar cerrado y sin hidden")


def validate_hub(growth_solutions: list[dict], hub: dict) -> None:
    path = SOLUTIONS / "index.html"
    value = text(path)
    assert_contains(value, [
        'data-experience-system="v6"', 'data-experience-wave="solutions"',
        'data-experience-surface="solutions-hub"', 'data-experience-v60="solutions-hub"',
        hub["headline"], hub["intro"],
    ], "hub")
    for href in STYLE_PATHS:
        assert_once(value, f'href="{href}"', "hub: estilos")
    assert_once(value, HUB_START, "hub marker")
    assert_once(value, HUB_END, "hub marker")
    first = first_layer(value, HUB_START, "hub")
    for guide in hub["guides"]:
        assert_contains(first, [guide["title"], guide["copy"], guide["href"]], "hub guide")
    for item in growth_solutions:
        assert_contains(first, [item["short"], item["intent"], f'{item["slug"]}.html'], "hub route")
    old = legacy(value, "hub")
    assert_contains(old, ["CRO-V52-HUB-GUIDE:START", "growth-route-grid-v51", "growth-cta-v51"], "hub legacy")
    if re.search(r"<form\b", value):
        fail("hub no debe crear formulario")


def main() -> int:
    growth_payload = load(GROWTH)
    cro_payload = load(CRO)
    growth_solutions = growth_payload.get("solutions", [])
    cro_solutions = cro_payload.get("solutions", [])
    if len(growth_solutions) != 6 or len(cro_solutions) != 6:
        fail("se requieren 6 soluciones Growth y 6 CRO")
    growth_map = {item["slug"]: item for item in growth_solutions}
    cro_map = {item["slug"]: item for item in cro_solutions}
    if set(growth_map) != set(cro_map):
        fail("slugs Growth/CRO desalineados")
    html_routes = sorted(path.stem for path in SOLUTIONS.glob("*.html") if path.name != "index.html")
    if sorted(growth_map) != html_routes:
        fail(f"rutas HTML y fuentes no coinciden: fuente={sorted(growth_map)} html={html_routes}")
    for slug in sorted(growth_map):
        validate_route(slug, growth_map[slug], cro_map[slug])
    validate_hub(growth_solutions, cro_payload["hub"])
    print("VALIDATE EXPERIENCE V6 WAVE 3 OK: 6 rutas + hub con truth Growth/CRO visible y cuatro disclosures v5.31 preservados.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, json.JSONDecodeError) as exc:
        print(f"VALIDATE EXPERIENCE V6 WAVE 3 FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
