#!/usr/bin/env python3
"""Source-driven W5 v8 global shell renderer.

The shell is intentionally candidate-only. It resolves only physical fallback
routes or certified v8 pilots. RC02 is rendered as a non-link capability until
its dedicated materialization/publication gate exists.
"""
from __future__ import annotations

from html import escape
from pathlib import Path
import json
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "assets/data/v8/home-shell-v80.json"


def load_model(root: Path = ROOT) -> dict:
    path = root / MODEL_PATH.relative_to(ROOT)
    return json.loads(path.read_text(encoding="utf-8"))


def prefixed(href: str | None, prefix: str = "") -> str | None:
    if href is None or href.startswith("#") or href.startswith("http://") or href.startswith("https://"):
        return href
    return f"{prefix}{href}"


def resolve_item_href(row: list, prefix: str = "") -> str | None:
    """Resolve the candidate-safe physical href from a 5-field nav item row."""
    _code, _label, _target, fallback, availability = row
    if availability in {"legacy_bridge", "v8_pilot"}:
        if not fallback:
            raise ValueError(f"{_code}: candidate item has no fallback href")
        return prefixed(fallback, prefix)
    if availability == "owner_confirmed_not_materialized":
        if fallback is not None:
            raise ValueError(f"{_code}: non-materialized capability cannot expose href")
        return None
    raise ValueError(f"{_code}: unsupported availability {availability!r}")


def _icon_chevron() -> str:
    return '<svg class="ml-nav-chevron" viewBox="0 0 12 8" aria-hidden="true"><path d="m1 1 5 5 5-5"/></svg>'


def _render_mega_group(title: str, rows: Iterable[list], prefix: str) -> str:
    items: list[str] = []
    for row in rows:
        code, label, _target, _fallback, availability = row
        href = resolve_item_href(row, prefix)
        if href:
            items.append(
                f'<li><a class="ml-mega-item" data-ml-item-id="{escape(code)}" '
                f'href="{escape(href, quote=True)}"><span>{escape(label)}</span>'
                '<span class="ml-mega-arrow" aria-hidden="true">→</span></a></li>'
            )
        else:
            items.append(
                f'<li><span class="ml-mega-item ml-mega-item--static" data-ml-item-id="{escape(code)}" '
                'data-ml-capability-status="owner-confirmed">'
                f'<span>{escape(label)}</span><small>Disponible dentro de la relación con clientes; ruta pública en preparación.</small></span></li>'
            )
    return (
        '<section class="ml-mega-group">'
        f'<p class="ml-mega-label">{escape(title)}</p>'
        f'<ul>{"".join(items)}</ul>'
        '</section>'
    )


def render_header(model: dict | None = None, *, prefix: str = "", contact_href: str = "#contacto") -> str:
    model = model or load_model()
    nav = model["navigation"]
    primary = nav["primary"]
    actions = {row[0]: row for row in nav["actions"]}
    groups = nav["mega_groups"]

    primary_links: list[str] = []
    for key, label, kind, href in primary:
        if key == "what":
            primary_links.append(
                '<span class="ml-nav-what">'
                '<a class="ml-nav-link ml-nav-fallback" href="#soluciones">Qué hacemos</a>'
                f'<button class="ml-nav-link ml-nav-trigger" type="button" data-ml-mega-toggle '
                f'aria-expanded="false" aria-controls="ml-mega-menu">{escape(label)}{_icon_chevron()}</button>'
                '</span>'
            )
            continue
        if not href:
            raise ValueError(f"primary navigation item {key} has no href")
        target = contact_href if key == "contact" else prefixed(href, prefix)
        primary_links.append(
            f'<a class="ml-nav-link" data-ml-nav-id="{escape(key)}" href="{escape(target or "", quote=True)}">{escape(label)}</a>'
        )

    talk = actions["talk"]
    talk_href = contact_href if talk[3] == "#contacto" else prefixed(talk[3], prefix)
    diagnostic = actions["diagnostic"]
    diagnostic_href = prefixed(diagnostic[3], prefix)

    mega = (
        '<div class="ml-mega" id="ml-mega-menu" data-ml-mega hidden>'
        '<div class="ml-container ml-mega-grid">'
        f'{_render_mega_group("Prácticas", groups["practices"], prefix)}'
        f'{_render_mega_group("Soluciones", groups["solutions"], prefix)}'
        f'{_render_mega_group("Relación continua", groups["recurring"], prefix)}'
        '</div></div>'
    )

    return (
        '<header class="ml-site-header" data-ml-shell>'
        '<div class="ml-container ml-header-inner">'
        f'<a class="ml-brand" href="{escape(prefixed("index.html", prefix) or "index.html", quote=True)}" aria-label="Meridiano Legal, inicio">'
        f'<img src="{escape(prefixed("assets/brand/meridiano-logo-horizontal-dark.svg", prefix) or "", quote=True)}" '
        'alt="Meridiano Legal"></a>'
        '<button class="ml-menu-toggle" type="button" data-ml-menu-toggle aria-expanded="false" aria-controls="ml-nav-panel">'
        '<span aria-hidden="true"></span><span aria-hidden="true"></span><span aria-hidden="true"></span>'
        '<span class="ml-visually-hidden">Abrir navegación</span></button>'
        '<div class="ml-nav-panel" id="ml-nav-panel" data-ml-nav-panel>'
        f'<nav class="ml-primary-nav" aria-label="Navegación principal">{"".join(primary_links)}</nav>'
        '<div class="ml-nav-actions">'
        f'<a class="ml-btn ml-btn--secondary ml-nav-diagnostic" data-ml-event="diagnosis_start" href="{escape(diagnostic_href or "", quote=True)}">{escape(diagnostic[1])}</a>'
        f'<a class="ml-btn ml-nav-talk" data-ml-event="cta_click" href="{escape(talk_href or "", quote=True)}">{escape(talk[1])}</a>'
        '</div>'
        f'{mega}'
        '</div>'
        '</div>'
        '</header>'
    )


def _footer_links(rows: Iterable[list], prefix: str) -> str:
    output: list[str] = []
    for row in rows:
        code, label, *_ = row
        href = resolve_item_href(row, prefix)
        if href:
            output.append(
                f'<li><a data-ml-footer-id="{escape(code)}" href="{escape(href, quote=True)}">{escape(label)}</a></li>'
            )
        else:
            output.append(
                f'<li><span class="ml-footer-static" data-ml-footer-id="{escape(code)}">{escape(label)}</span></li>'
            )
    return "".join(output)


def render_footer(model: dict | None = None, *, prefix: str = "", contact_href: str = "#contacto") -> str:
    model = model or load_model()
    groups = model["navigation"]["mega_groups"]
    return (
        '<footer class="ml-site-footer">'
        '<div class="ml-container ml-footer-grid">'
        '<div class="ml-footer-brand">'
        f'<img src="{escape(prefixed("assets/brand/meridiano-logo-horizontal-dark.svg", prefix) or "", quote=True)}" alt="Meridiano Legal">'
        '<p>Derecho empresarial, comprensión del negocio y tecnología aplicada para decisiones que necesitan avanzar.</p>'
        f'<a class="ml-footer-contact" href="{escape(contact_href, quote=True)}">Hablar con Meridiano →</a>'
        '</div>'
        '<nav class="ml-footer-nav" aria-label="Navegación secundaria">'
        '<section><p class="ml-footer-label">Prácticas</p><ul>'
        f'{_footer_links(groups["practices"], prefix)}</ul></section>'
        '<section><p class="ml-footer-label">Soluciones</p><ul>'
        f'{_footer_links(groups["solutions"], prefix)}</ul></section>'
        '<section><p class="ml-footer-label">Relación continua</p><ul>'
        f'{_footer_links(groups["recurring"], prefix)}</ul></section>'
        '</nav>'
        '</div>'
        '<div class="ml-container ml-footer-legal">'
        '<span>© Meridiano Legal</span>'
        '<span class="ml-footer-legal-links">'
        f'<a href="{escape(prefixed("privacidad.html", prefix) or "", quote=True)}">Privacidad</a>'
        f'<a href="{escape(prefixed("terminos.html", prefix) or "", quote=True)}">Términos</a>'
        f'<a href="{escape(prefixed("aviso-legal.html", prefix) or "", quote=True)}">Aviso legal</a>'
        '</span></div>'
        '</footer>'
    )


if __name__ == "__main__":
    model = load_model()
    print(render_header(model))
    print(render_footer(model))
