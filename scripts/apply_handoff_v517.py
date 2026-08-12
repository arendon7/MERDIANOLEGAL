#!/usr/bin/env python3
"""Aplica v5.17: continuidad manual y verificable del handoff a WhatsApp."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
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
        raise RuntimeError("portada sin </head>")
    return text.replace("</head>", f"  {item}\n</head>", 1)


def ensure_script(text: str, item: str, anchor: str) -> str:
    text = re.sub(r'(?m)^[ \t]*' + re.escape(item) + r'[ \t]*(?:\r?\n)?', "", text)
    if anchor in text:
        return text.replace(anchor, anchor + "\n  " + item, 1)
    if "</body>" not in text:
        raise RuntimeError("portada sin </body>")
    return text.replace("</body>", f"  {item}\n</body>", 1)


def patch_home() -> None:
    text = HOME.read_text(encoding="utf-8")
    block = panel_markup()
    marked = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if marked.search(text):
        text = marked.sub(block, text, count=1)
    else:
        status = '<p class="form-status full" role="status" aria-live="polite"></p>'
        if status not in text:
            raise RuntimeError("index.html: falta status del formulario")
        text = text.replace(status, status + block, 1)

    text = ensure_head_item(text, '<link rel="stylesheet" href="handoff-continuity-v517.css">')
    text = ensure_script(
        text,
        '<script src="handoff-continuity-v517.js"></script>',
        '<script src="decision-action-v515.js"></script>',
    )
    HOME.write_text(text, encoding="utf-8")


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
    if targets != [HOME]:
        names = ", ".join(str(path.relative_to(ROOT)) for path in targets) or "ninguno"
        raise RuntimeError(f"v5.17 espera un único formulario canónico en index.html; detectados: {names}")
    patch_home()
    patch_site_runtime()
    print("HANDOFF V5.17 OK: continuidad manual aplicada al formulario canónico; 16 fichas profundas conservan sus rutas hacia index.html#contacto.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
