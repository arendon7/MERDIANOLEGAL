#!/usr/bin/env python3
"""Valida contratos estructurales y truth-parity de Experience System v6 Wave 1."""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
DETAILS = {
    "product-diagnostic": ROOT / "productos/diagnostico-juridico-empresarial.html",
    "service-ai": ROOT / "servicios/tecnologia-inteligencia-artificial.html",
}
STYLE_HOME = [
    "assets/css/v6/tokens.css",
    "assets/css/v6/base.css",
    "assets/css/v6/components.css",
    "assets/css/v6/surfaces.css",
]
STYLE_DETAIL = [f"../{href}" for href in STYLE_HOME]
LEGACY_START = "<!-- EXPERIENCE-V60-LEGACY:START -->"
LEGACY_END = "<!-- EXPERIENCE-V60-LEGACY:END -->"


def fail(message: str) -> None:
    raise AssertionError(message)


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def count_public_html() -> int:
    root_files = list(ROOT.glob("*.html"))
    nested = []
    for folder in ("productos", "servicios", "soluciones", "sectores", "perspectivas"):
        nested.extend((ROOT / folder).glob("*.html"))
    return len(root_files) + len(nested)


def assert_once(value: str, needle: str, label: str) -> None:
    count = value.count(needle)
    if count != 1:
        fail(f"{label}: esperaba 1 ocurrencia de {needle!r}; encontró {count}")


def assert_contains(value: str, needles: list[str], label: str) -> None:
    missing = [needle for needle in needles if needle not in value]
    if missing:
        fail(f"{label}: faltan {missing}")


def legacy_block(value: str, label: str) -> str:
    match = re.search(re.escape(LEGACY_START) + r"(.*?)" + re.escape(LEGACY_END), value, flags=re.S)
    if not match:
        fail(f"{label}: falta bloque legacy preservado")
    return match.group(1)


def validate_contracts() -> None:
    contract = json.loads(text(ROOT / "experience-system-v60.json"))
    content = json.loads(text(ROOT / "experience-content-v60.json"))
    if contract.get("version") != "6.0.0" or content.get("version") != "6.0.0":
        fail("contratos Experience v6 deben declarar 6.0.0")
    baseline = contract.get("baseline", {})
    if baseline.get("html_total") != 46 or baseline.get("builder_steps") != 30:
        fail("baseline v6 debe preservar 46 HTML y 30 pasos")
    invariants = contract.get("invariants", {})
    required_true = [
        "static_first",
        "single_physical_form",
        "manual_whatsapp_handoff",
        "no_pii_persistence",
        "no_business_conversion_inference",
        "no_fake_backend_capability",
        "full_legal_depth_preserved",
        "stable_only_after_all_gates",
    ]
    for key in required_true:
        if invariants.get(key) is not True:
            fail(f"invariante v6 no está fijada: {key}")


def validate_builder() -> None:
    workflow = text(ROOT / ".github/workflows/build-canonical.yml")
    names = re.findall(r"(?m)^      - name:", workflow)
    if len(names) != 30:
        fail(f"builder v6 debe conservar 30 pasos nombrados; encontró {len(names)}")
    assert_contains(
        workflow,
        [
            "scripts/apply_experience_v60.py",
            "scripts/validate_experience_v60.py",
            "experience-system-v60.json",
            "experience-content-v60.json",
            "assets/css/v6/**",
        ],
        "builder",
    )


def validate_home() -> None:
    value = text(HOME)
    assert_contains(
        value,
        [
            'data-experience-system="v6"',
            'data-experience-v60="home"',
            "Decisiones empresariales complejas, convertidas en estructura jurídica ejecutable.",
            "No necesita saber el nombre del servicio. Empiece por la decisión que debe resolver.",
            "El trabajo jurídico debe dejar algo que la organización pueda usar, ejecutar y verificar.",
            "Cuéntenos qué decisión necesita resolver.",
            "soluciones/ordenar-riesgo-juridico-empresa.html",
            "soluciones/direccion-juridica-externa-empresa.html",
            "soluciones/gobernar-inteligencia-artificial-empresa.html",
            "soluciones/preparar-empresa-para-inversion.html",
            "soluciones/estructurar-proyecto-regulado.html",
            "soluciones/ordenar-operacion-juridica.html",
        ],
        "Home v6",
    )
    for href in STYLE_HOME:
        assert_once(value, f'href="{href}"', "Home v6 styles")
    if len(re.findall(r"<form\b", value)) != 1:
        fail("Home v6 debe contener exactamente un formulario físico")
    if value.count('id="contacto"') != 1:
        fail("Home v6 debe exponer un único id=contacto")
    if value.count('id="contacto-v531-legacy"') != 1:
        fail("Home v6 debe renombrar el contacto legacy una sola vez")

    # v5.11 y v5.17 viven dentro del mismo formulario físico. Al mover ese formulario
    # al cierre v6, sus contratos deben permanecer una única vez en la página, no en
    # el bloque legacy del que deliberadamente se extrajo el formulario.
    for marker in (
        "<!-- ENGAGEMENT-V511:START -->",
        "<!-- ENGAGEMENT-V511:END -->",
        "<!-- HANDOFF-V517:START -->",
        "<!-- HANDOFF-V517:END -->",
        'data-engagement-v511="true"',
        'data-handoff-v517="true"',
    ):
        assert_once(value, marker, "Home v6 form contracts")

    legacy = legacy_block(value, "Home v6")
    assert_contains(
        legacy,
        [
            "PROFESSIONAL-AUTHORITY-V525-HOME:START",
            "EXPERIENCIA SECTORIAL",
            "PERSPECTIVAS",
            "PREGUNTAS FRECUENTES",
        ],
        "Home legacy",
    )
    if re.search(r"<form\b", legacy):
        fail("Home legacy no puede conservar una segunda copia del formulario")
    if "ENGAGEMENT-V511:START" in legacy or "HANDOFF-V517:START" in legacy:
        fail("los contratos v5.11/v5.17 deben viajar con el formulario canónico, no duplicarse en legacy")


def validate_detail(catalog_id: str, path: Path) -> None:
    value = text(path)
    assert_contains(value, ['data-experience-system="v6"', f'data-experience-v60="{catalog_id}"'], catalog_id)
    for href in STYLE_DETAIL:
        assert_once(value, f'href="{href}"', f"{catalog_id} styles")
    if re.search(r"<form\b", value):
        fail(f"{catalog_id}: una ficha profunda no debe crear formulario físico")
    legacy = legacy_block(value, catalog_id)
    assert_contains(
        legacy,
        [
            "DECISION-V58-DETAIL:START",
            "DECISION-COMPRESSION-V531:PAIR-START",
            "OFFER-NARRATIVE-V522:START",
            "PROOF-V512-DETAIL:START",
            'id="limites-title"',
        ],
        f"{catalog_id} legacy",
    )

    if catalog_id == "product-diagnostic":
        assert_contains(
            value,
            [
                "Sepa qué riesgo jurídico existe, qué evidencia falta y qué debe corregirse primero.",
                "1 informe jurídico ejecutivo",
                "1 matriz maestra de riesgos",
                "1 plan jurídico de 90 días",
                "1 sociedad colombiana",
                "Hasta 8",
                "Hasta 60",
                "Hasta 80",
                "Hasta 5",
                "No es auditoría de aseguramiento absoluto ni certificación de cumplimiento.",
                "Definir",
                "Inventariar",
                "Contrastar",
                "Calificar",
                "Cerrar",
            ],
            catalog_id,
        )
    else:
        assert_contains(
            value,
            [
                "Adopte inteligencia artificial con casos, datos, proveedores y responsabilidades gobernables.",
                "¿La organización sabe dónde usa inteligencia artificial, qué datos intervienen, quién responde, cómo supervisa resultados y qué debe hacer ante un incidente?",
                "1 inventario de IA",
                "1 matriz de clasificación",
                "1 marco de gobernanza",
                "Hasta 20",
                "Hasta 8",
                "Hasta 3",
                "2 sesiones",
                "No constituye auditoría técnica, certificación algorítmica, pentesting ni evaluación científica del modelo.",
                "Descubrir",
                "Clasificar",
                "Diseñar",
                "Implementar",
                "Revisar",
            ],
            catalog_id,
        )


def main() -> int:
    if count_public_html() != 46:
        fail(f"se esperaban 46 HTML públicos; se encontraron {count_public_html()}")
    validate_contracts()
    validate_builder()
    validate_home()
    for catalog_id, path in DETAILS.items():
        validate_detail(catalog_id, path)
    print("VALIDATE EXPERIENCE V6 OK: 46 HTML, 30 pasos, 1 formulario, Home + Auditoría + IA con truth/depth preservados.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"VALIDATE EXPERIENCE V6 FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
