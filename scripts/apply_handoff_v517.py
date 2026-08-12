#!/usr/bin/env python3
"""Aplica v5.17: continuidad manual y verificable del handoff a WhatsApp."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SITE_JS = ROOT / "site-v3.js"
START = "<!-- HANDOFF-V517:START -->"
END = "<!-- HANDOFF-V517:END -->"
AUTO_CLIPBOARD = "try { await navigator.clipboard?.writeText(summary); } catch { /* copia opcional */ }"
DRAFT_EVENT = "window.dispatchEvent(new CustomEvent('meridiano:handoff-draft-v517', { detail: { reference, summary, url } }));"


def public_html() -> list[Path]:
    paths = list(ROOT.glob("*.html"))
    for folder in ("servicios", "productos", "soluciones", "sectores", "perspectivas"):
        paths.extend((ROOT / folder).glob("*.html"))
    return sorted(set(paths))


def contact_pages() -> list[Path]:
    result = []
    for path in public_html():
        text = path.read_text(encoding="utf-8")
        if 'id="contact-form"' in text and 'data-contact-v49="true"' in text:
            result.append(path)
    return result


def prefix_for(path: Path) -> str:
    return "" if path.parent == ROOT else "../"


def panel_markup() -> str:
    return f'''{START}
<section class="handoff-continuity-v517 full" data-handoff-v517="true" data-handoff-state="idle" hidden aria-labelledby="handoff-v517-title">
  <div class="handoff-head-v517">
    <span>HANDOFF MANUAL A WHATSAPP</span>
    <h3 id="handoff-v517-title">El mensaje queda preparado; el envío y cualquier paso posterior siguen bajo su control.</h3>
    <p>Esta web no recibe confirmación de entrega, lectura, aceptación ni inicio del encargo. Si cambia el formulario, deberá preparar de nuevo el handoff para mantener coherencia.</p>
  </div>
  <dl class="handoff-facts-v517">
    <div><dt>Referencia</dt><dd><code data-handoff-reference-v517>Se genera al preparar</code></dd></div>
    <div><dt>Qué conservar</dt><dd>La referencia y el mensaje que usted decida enviar en WhatsApp.</dd></div>
    <div><dt>Qué ocurre después</dt><dd>La conversación continúa en WhatsApp. Este formulario público no registra entrega, aceptación contractual ni apertura de expediente.</dd></div>
  </dl>
  <div class="handoff-actions-v517" aria-label="Acciones del handoff preparado">
    <button type="button" data-handoff-reopen-v517>Abrir WhatsApp de nuevo</button>
    <button type="button" data-handoff-copy-v517>Copiar resumen</button>
    <button type="button" data-handoff-edit-v517>Editar solicitud</button>
  </div>
  <p class="handoff-live-v517" data-handoff-live-v517 role="status" aria-live="polite"></p>
</section>
{END}'''


def ensure_head_item(text: str, item: str) -> str:
    text = re.sub(r'(?m)^[ \t]*' + re.escape(item) + r'[ \t]*(?:\r?\n)?', "", text)
    if "</head>" not in text:
        raise RuntimeError("página sin </head>")
    return text.replace("</head>", f"  {item}\n</head>", 1)


def ensure_script(text: str, item: str, anchor: str) -> str:
    text = re.sub(r'(?m)^[ \t]*' + re.escape(item) + r'[ \t]*(?:\r?\n)?', "", text)
    if anchor in text:
        return text.replace(anchor, anchor + "\n  " + item, 1)
    if "</body>" not in text:
        raise RuntimeError("página sin </body>")
    return text.replace("</body>", f"  {item}\n</body>", 1)


def patch_page(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    prefix = prefix_for(path)
    style = f'<link rel="stylesheet" href="{prefix}handoff-continuity-v517.css">'
    script = f'<script src="{prefix}handoff-continuity-v517.js"></script>'
    script_anchor = f'<script src="{prefix}decision-action-v515.js"></script>'

    block = panel_markup()
    marked = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if marked.search(text):
        text = marked.sub(block, text, count=1)
    else:
        status = '<p class="form-status full" role="status" aria-live="polite"></p>'
        if status not in text:
            raise RuntimeError(f"{path.relative_to(ROOT)}: falta status del formulario")
        text = text.replace(status, status + block, 1)

    text = ensure_head_item(text, style)
    text = ensure_script(text, script, script_anchor)
    path.write_text(text, encoding="utf-8")


def patch_site_runtime() -> None:
    text = SITE_JS.read_text(encoding="utf-8")
    if DRAFT_EVENT not in text:
        if AUTO_CLIPBOARD not in text:
            raise RuntimeError("site-v3.js: no se encontró la copia automática histórica")
        text = text.replace(AUTO_CLIPBOARD, DRAFT_EVENT, 1)
    text = text.replace(AUTO_CLIPBOARD, "")
    SITE_JS.write_text(text, encoding="utf-8")


def main() -> int:
    targets = contact_pages()
    if len(targets) < 17:
        raise RuntimeError(f"Se esperaban al menos 17 superficies con contact-form y se encontraron {len(targets)}")
    for path in targets:
        patch_page(path)
    patch_site_runtime()
    print(f"HANDOFF V5.17 OK: continuidad manual aplicada a {len(targets)} formularios públicos; copia automática eliminada.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
