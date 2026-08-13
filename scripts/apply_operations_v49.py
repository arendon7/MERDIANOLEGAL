#!/usr/bin/env python3
"""v4.9: prepara la web pública para operación comercial real sin backend ficticio."""
from pathlib import Path
import json
import re

R = Path(__file__).resolve().parents[1]
I = R / "index.html"
S = R / "site-v3.js"
V = json.loads((R / "version.json").read_text(encoding="utf-8"))
VER = V["version"]
CONTACT_A = "<!-- OPERATIONS-V49-CONTACT:START -->"
CONTACT_B = "<!-- OPERATIONS-V49-CONTACT:END -->"


def semver(value):
    return tuple(int(x) for x in value.split(".")[:3])


def ensure_maxlength_v523(text, field, limit):
    """Desde v5.23 conserva el campo por name y normaliza maxlength sin depender del orden de atributos."""
    tag_name = "textarea" if field == "message" else "input"
    pattern = re.compile(rf'<{tag_name}\b(?P<attrs>[^>]*\bname="{re.escape(field)}"[^>]*)>', re.I)
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"No se encontró una única instancia del campo {field}")
    match = matches[0]
    attrs = match.group("attrs")
    attrs = re.sub(r'\s+maxlength="\d+"', "", attrs)
    attrs = attrs.rstrip() + f' maxlength="{limit}"'
    replacement = f'<{tag_name}{attrs}>'
    return text[:match.start()] + replacement + text[match.end():]


def patch_index():
    t = I.read_text(encoding="utf-8")
    tag = '<link rel="stylesheet" href="operations-v49.css">'
    t = t.replace("  " + tag + "\n", "").replace(tag + "\n", "").replace("  " + tag, "").replace(tag, "")
    anchor = '<link rel="stylesheet" href="quality-v48.css">'
    if anchor not in t:
        raise RuntimeError("No se encontró quality-v48.css")
    t = t.replace(anchor, anchor + '\n  ' + tag, 1)

    t = re.sub(re.escape(CONTACT_A) + r"[\s\S]*?" + re.escape(CONTACT_B), "", t, count=1)

    # v4.9 es una capa histórica: debe reconocer el formulario aunque capas
    # posteriores añadan data-* propios. Solo normaliza su atributo y preserva
    # cualquier extensión que no le pertenezca para que el generador posterior
    # pueda reconstruirla de forma determinista.
    form_match = re.search(r'<form class="contact-form" id="contact-form"(?P<attrs>[^>]*)>', t)
    if not form_match:
        raise RuntimeError("No se encontró el formulario de contacto")
    attrs = form_match.group("attrs")
    attrs = re.sub(r'\s+data-contact-v49="true"', '', attrs)
    marker49 = '<form class="contact-form" id="contact-form" data-contact-v49="true"' + attrs + '>'
    block = CONTACT_A + '<label class="contact-hp-v49" aria-hidden="true">Sitio web<input type="text" name="website" tabindex="-1" autocomplete="off"></label>' + CONTACT_B
    t = t[:form_match.start()] + marker49 + block + t[form_match.end():]

    if semver(VER) >= (5, 23, 0):
        # v5.23 compacta el contacto y varias capas históricas vuelven a serializar
        # temporalmente los campos en segunda pasada. Se identifica cada control por
        # su name —el contrato estable— y no por una cadena HTML completa.
        for field, limit in (("name", 120), ("company", 160), ("email", 180), ("message", 2000)):
            t = ensure_maxlength_v523(t, field, limit)
    else:
        replacements = {
            '<input type="text" name="name" autocomplete="name" required>': '<input type="text" name="name" autocomplete="name" maxlength="120" required>',
            '<input type="text" name="company" autocomplete="organization">': '<input type="text" name="company" autocomplete="organization" maxlength="160">',
            '<input type="email" name="email" autocomplete="email" required>': '<input type="email" name="email" autocomplete="email" maxlength="180" required>',
            '<textarea name="message" rows="6" required placeholder="Describa la decisión, el plazo y el resultado esperado. No incluya datos sensibles ni documentos confidenciales."></textarea>': '<textarea name="message" rows="6" maxlength="2000" required placeholder="Describa la decisión, el plazo y el resultado esperado. No incluya datos sensibles ni documentos confidenciales."></textarea>',
        }
        for old, new in replacements.items():
            if new not in t:
                if old not in t:
                    raise RuntimeError("No se encontró un campo esperado del formulario")
                t = t.replace(old, new, 1)

    t = re.sub(
        r'<div class="trust-note full"><span>✓</span><p><strong>.*?</strong>.*?</p></div>',
        '<div class="trust-note full"><span>✓</span><p><strong>Canal directo, sin carga de archivos.</strong> Al continuar se abre WhatsApp con una referencia única. La solicitud se completa únicamente cuando usted envía el mensaje allí; esta web estática no guarda el formulario.</p></div>',
        t,
        count=1,
    )
    t = t.replace('<button class="btn btn-navy full" type="submit">Preparar solicitud por WhatsApp</button>', '<button class="btn btn-navy full" type="submit">Abrir solicitud en WhatsApp</button>', 1)
    t = re.sub(r'<p class="form-status full"(?: role="status")? aria-live="polite"></p>', '<p class="form-status full" role="status" aria-live="polite"></p>', t, count=1)
    t = re.sub(r'<div class="contact-v49-direct">[\s\S]*?</div>', '', t, count=1)
    status = '<p class="form-status full" role="status" aria-live="polite"></p>'
    direct = '<div class="contact-v49-direct"><span>¿Prefiere empezar sin formulario?</span><a href="https://wa.me/573008507813" target="_blank" rel="noopener noreferrer">Abrir WhatsApp directamente</a></div>'
    if status not in t:
        raise RuntimeError("No se encontró el estado del formulario")
    t = t.replace(status, status + direct, 1)
    I.write_text(t, encoding="utf-8")


def patch_site_js():
    t = S.read_text(encoding="utf-8")
    pattern = r"\n  const form = document\.getElementById\('contact-form'\);[\s\S]*?\n  const year = document\.getElementById\('year'\);"
    replacement = r'''
  const form = document.getElementById('contact-form');
  const contactStartedAt = Date.now();
  const cleanContactValue = (value, max = 2000) => String(value || '').trim().replace(/\s+/g, ' ').slice(0, max);
  form?.addEventListener('submit', async (event) => {
    event.preventDefault();
    const status = form.querySelector('.form-status');
    const setStatus = (message, state = '') => {
      if (!status) return;
      status.textContent = message;
      if (state) status.dataset.state = state;
      else delete status.dataset.state;
    };
    if (!form.reportValidity()) {
      setStatus('Revise los campos obligatorios antes de continuar.', 'error');
      return;
    }
    const data = new FormData(form);
    if (cleanContactValue(data.get('website'), 120)) {
      setStatus('No fue posible preparar la solicitud. Inténtelo nuevamente.', 'error');
      return;
    }
    if (Date.now() - contactStartedAt < 800) {
      setStatus('Revise la información antes de continuar.', 'error');
      return;
    }
    const now = new Date();
    const reference = `ML-${now.toISOString().slice(0, 10).replace(/-/g, '')}-${Math.random().toString(36).slice(2, 7).toUpperCase()}`;
    const current = new URL(window.location.href);
    const context = cleanContactValue(form.dataset.commercialContext || current.searchParams.get('context') || '', 220);
    const source = `${current.pathname}${current.search}`;
    const lines = [
      'Hola, quiero presentar una necesidad a Meridiano Legal.',
      '',
      `Referencia web: ${reference}`,
      `Nombre: ${cleanContactValue(data.get('name'), 120)}`,
      `Empresa: ${cleanContactValue(data.get('company'), 160) || 'No indicada'}`,
      `Correo: ${cleanContactValue(data.get('email'), 180)}`,
      `Necesidad: ${cleanContactValue(data.get('need'), 160)}`,
    ];
    if (context) lines.push(`Contexto comercial: ${context}`);
    lines.push(`Origen: ${source}`, '', 'Contexto general:', cleanContactValue(data.get('message'), 2000), '', 'Confirmo que no estoy enviando información confidencial.');
    const summary = lines.join('\n');
    const url = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(summary)}`;
    setStatus('Abriendo WhatsApp. La solicitud solo queda enviada cuando confirme el envío allí.');
    try { await navigator.clipboard?.writeText(summary); } catch { /* copia opcional */ }
    window.dispatchEvent(new CustomEvent('meridiano:lead-prepared', { detail: { reference, need: cleanContactValue(data.get('need'), 160), context } }));
    const opened = window.open(url, '_blank', 'noopener,noreferrer');
    if (!opened) {
      window.location.assign(url);
      return;
    }
    form.dataset.lastLeadReference = reference;
    setStatus(`WhatsApp se abrió con la referencia ${reference}. Revise el mensaje y pulse Enviar para completar la solicitud.`, 'ready');
  });

  const year = document.getElementById('year');'''
    replacement_text = "\n" + replacement.strip("\n")
    updated, count = re.subn(pattern, lambda _match: replacement_text, t, count=1)
    if count != 1:
        raise RuntimeError("No se pudo sustituir el flujo de contacto")
    S.write_text(updated, encoding="utf-8")


def main():
    if semver(VER) < (4, 9, 0):
        raise SystemExit("v4.9 requiere version.json >= 4.9.0")
    patch_index()
    patch_site_js()
    print(f"Operación pública v{VER} aplicada: contacto, anti-bot, trazabilidad y fallback.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
