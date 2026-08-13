#!/usr/bin/env python3
"""Carga y valida la configuración pública canónica del sitio."""
from __future__ import annotations

from pathlib import Path
from urllib.parse import urlsplit
import json
import re

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "site-config.json"


def load_site_config() -> dict:
    data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    base_url = str(data.get("base_url", "")).strip()
    parsed = urlsplit(base_url)
    if parsed.scheme != "https" or not parsed.netloc:
        raise ValueError("site-config.json: base_url debe ser una URL HTTPS absoluta")
    if parsed.query or parsed.fragment:
        raise ValueError("site-config.json: base_url no puede incluir query ni fragment")
    if not base_url.endswith("/"):
        raise ValueError("site-config.json: base_url debe terminar en /")
    public_path = parsed.path or "/"
    if not public_path.startswith("/") or not public_path.endswith("/"):
        raise ValueError("site-config.json: la ruta pública derivada debe comenzar y terminar en /")

    custom_domain = str(data.get("custom_domain", "") or "").strip().lower()
    if custom_domain:
        if "/" in custom_domain or ":" in custom_domain:
            raise ValueError("site-config.json: custom_domain debe contener solo el hostname")
        if parsed.hostname != custom_domain:
            raise ValueError("site-config.json: custom_domain debe coincidir con el host de base_url")

    contact = data.get("contact") or {}
    whatsapp = re.sub(r"\D+", "", str(contact.get("whatsapp", "")))
    if not re.fullmatch(r"\d{10,15}", whatsapp):
        raise ValueError("site-config.json: contact.whatsapp debe contener 10 a 15 dígitos")

    analytics = data.get("analytics") or {}
    enabled = bool(analytics.get("enabled", False))
    provider = str(analytics.get("provider", "none") or "none").strip().lower()
    site_id = str(analytics.get("site_id", "") or "").strip()
    if not enabled and provider != "none":
        raise ValueError("site-config.json: analytics.provider debe ser none mientras analytics.enabled=false")
    if enabled and provider == "none":
        raise ValueError("site-config.json: analytics.enabled=true requiere un provider real")
    if enabled and not site_id:
        raise ValueError("site-config.json: analítica habilitada requiere analytics.site_id")

    capabilities = data.get("capabilities") or {}
    client_portal = capabilities.get("client_portal") or {}
    portal_enabled = bool(client_portal.get("enabled", False))
    portal_url = str(client_portal.get("url", "") or "").strip()
    if portal_enabled:
        portal_parsed = urlsplit(portal_url)
        if portal_parsed.scheme != "https" or not portal_parsed.netloc:
            raise ValueError("site-config.json: client_portal.url debe ser HTTPS absoluta cuando el portal está habilitado")
        if portal_parsed.query or portal_parsed.fragment:
            raise ValueError("site-config.json: client_portal.url no puede incluir query ni fragment")
        demo_url = base_url + "demo.html"
        if portal_url.rstrip("/") == demo_url.rstrip("/"):
            raise ValueError("site-config.json: demo.html no puede declararse como portal real de clientes")
    elif portal_url:
        raise ValueError("site-config.json: client_portal.url debe estar vacío mientras client_portal.enabled=false")

    verification = str(data.get("search_console_verification", "") or "").strip()
    if verification and not re.fullmatch(r"[A-Za-z0-9_\-:.]+", verification):
        raise ValueError("site-config.json: search_console_verification contiene caracteres no permitidos")

    normalized = dict(data)
    normalized["base_url"] = base_url
    normalized["host"] = parsed.netloc
    normalized["public_path"] = public_path
    normalized["custom_domain"] = custom_domain
    normalized["contact"] = {"whatsapp": whatsapp}
    normalized["analytics"] = {"enabled": enabled, "provider": provider, "site_id": site_id}
    normalized["capabilities"] = {
        "client_portal": {"enabled": portal_enabled, "url": portal_url}
    }
    normalized["search_console_verification"] = verification
    return normalized


def absolute_url(relative: str = "") -> str:
    config = load_site_config()
    return config["base_url"] + relative.lstrip("/")


if __name__ == "__main__":
    cfg = load_site_config()
    print(json.dumps(cfg, ensure_ascii=False, indent=2))
