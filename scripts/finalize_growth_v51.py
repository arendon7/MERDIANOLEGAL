#!/usr/bin/env python3
"""Aplica canonical/runtime v5.0 a las páginas nuevas de soluciones v5.1."""
from pathlib import Path

from apply_production_v50 import BASE_URL, patch_html

R = Path(__file__).resolve().parents[1]


def main() -> int:
    pages = sorted((R / "soluciones").glob("*.html"))
    if len(pages) != 7:
        raise SystemExit(f"v5.1 esperaba 7 páginas en soluciones/ y encontró {len(pages)}")
    for page in pages:
        patch_html(page)
    hub = R / "soluciones" / "index.html"
    text = hub.read_text(encoding="utf-8")
    text = text.replace(BASE_URL + "soluciones/index.html", BASE_URL + "soluciones/")
    hub.write_text(text, encoding="utf-8")
    print("Runtime/canonical v5.0 aplicado a hub y 6 rutas v5.1; canonical del hub normalizado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
