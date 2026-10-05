#!/usr/bin/env python3
"""Genera las páginas estáticas de AdminPlus con cabecera, pie y estilos compartidos."""
import pathlib

OUT = pathlib.Path(__file__).resolve().parent

ICONS = {
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "package": '<path d="m7.5 4.27 9 5.15"/><path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/>',
    "receipt": '<path d="M4 2v20l2-1 2 1 2-1 2 1 2-1 2 1 2-1 2 1V2l-2 1-2-1-2 1-2-1-2 1-2-1-2 1Z"/><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"/><path d="M12 17.5v-11"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    "wallet": '<path d="M19 7V4a1 1 0 0 0-1-1H5a2 2 0 0 0 0 4h15a1 1 0 0 1 1 1v4h-3a2 2 0 0 0 0 4h3a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1"/><path d="M3 5v14a2 2 0 0 0 2 2h15a1 1 0 0 0 1-1v-4"/>',
    "chart": '<path d="M3 3v18h18"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>',
    "scan": '<path d="M3 7V5a2 2 0 0 1 2-2h2"/><path d="M17 3h2a2 2 0 0 1 2 2v2"/><path d="M21 17v2a2 2 0 0 1-2 2h-2"/><path d="M7 21H5a2 2 0 0 1-2-2v-2"/><path d="M7 12h10"/>',
    "archive": '<rect width="20" height="5" x="2" y="3" rx="1"/><path d="M4 8v11a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8"/><path d="M10 12h4"/>',
    "shield": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
    "phone": '<rect width="14" height="20" x="5" y="2" rx="2" ry="2"/><path d="M12 18h.01"/>',
    "wifi-off": '<path d="M12 20h.01"/><path d="M8.5 16.429a5 5 0 0 1 7 0"/><path d="M5 12.859a10 10 0 0 1 5.17-2.69"/><path d="M19 12.859a10 10 0 0 0-2.007-1.523"/><path d="M2 8.82a15 15 0 0 1 4.177-2.643"/><path d="M22 8.82a15 15 0 0 0-11.288-3.764"/><path d="m2 2 20 20"/>',
    "eye-off": '<path d="M9.88 9.88a3 3 0 1 0 4.24 4.24"/><path d="M10.73 5.08A10.43 10.43 0 0 1 12 5c7 0 10 7 10 7a13.16 13.16 0 0 1-1.67 2.68"/><path d="M6.61 6.61A13.526 13.526 0 0 0 2 12s3 7 10 7a9.74 9.74 0 0 0 5.39-1.61"/><line x1="2" x2="22" y1="2" y2="22"/>',
    "share": '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" x2="15.42" y1="13.51" y2="17.49"/><line x1="15.41" x2="8.59" y1="6.51" y2="10.49"/>',
    "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    "map-pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    "trash": '<path d="M3 6h18"/><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"/><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"/><line x1="10" x2="10" y1="11" y2="17"/><line x1="14" x2="14" y1="11" y2="17"/>',
    "image": '<rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/>',
    "file": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/>',
    "arrow-right": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>',
    "cloud": '<path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"/>',
    "alert": '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
    "store": '<path d="m2 7 4.41-4.41A2 2 0 0 1 7.83 2h8.34a2 2 0 0 1 1.42.59L22 7"/><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><path d="M15 22v-4a2 2 0 0 0-2-2h-2a2 2 0 0 0-2 2v4"/><path d="M2 7h20"/><path d="M22 7v3a2 2 0 0 1-2 2a2.7 2.7 0 0 1-1.59-.63.7.7 0 0 0-.82 0A2.7 2.7 0 0 1 16 12a2.7 2.7 0 0 1-1.59-.63.7.7 0 0 0-.82 0A2.7 2.7 0 0 1 12 12a2.7 2.7 0 0 1-1.59-.63.7.7 0 0 0-.82 0A2.7 2.7 0 0 1 8 12a2.7 2.7 0 0 1-1.59-.63.7.7 0 0 0-.82 0A2.7 2.7 0 0 1 4 12a2 2 0 0 1-2-2V7"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "x": '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    "settings": '<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/>',
}


def icon(name, size=20, cls="ico"):
    return (f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
            f'stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true" focusable="false">{ICONS[name]}</svg>')


BASE_CSS = """
    :root {
      color-scheme: light dark;
      --primary: #1E3A8A;
      --on-primary: #FFFFFF;
      --fg: #0F172A;
      --accent: #A16207;
      --bg: #F8FAFC;
      --card: #FFFFFF;
      --muted: #E8ECF1;
      --muted-fg: #475569;
      --border: #E2E8F0;
      --success: #15803D;
      --destructive: #DC2626;
      --primary-soft: #EEF2FB;
      --accent-soft: #FBF6EA;
      --radius: 12px;
      --measure: 72ch;
      --font: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --primary: #93B4FF;
        --on-primary: #0B1220;
        --fg: #E6ECF5;
        --accent: #E3B341;
        --bg: #0B1220;
        --card: #111A2E;
        --muted: #18233A;
        --muted-fg: #A3B1C6;
        --border: #22304A;
        --success: #4ADE80;
        --destructive: #F87171;
        --primary-soft: #142140;
        --accent-soft: #261F10;
      }
    }
    *, *::before, *::after { box-sizing: border-box; }
    html { -webkit-text-size-adjust: 100%; }
    body {
      margin: 0;
      background: var(--bg);
      color: var(--fg);
      font-family: var(--font);
      font-size: 1rem;
      line-height: 1.65;
      overflow-wrap: break-word;
    }
    img, svg { display: block; max-width: 100%; }
    .ico { flex: none; }
    a { color: var(--primary); text-underline-offset: 3px; text-decoration-thickness: 1px; }
    a:hover { text-decoration-thickness: 2px; }
    :focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; border-radius: 4px; }
    .skip {
      position: absolute; left: 16px; top: -48px; z-index: 10;
      background: var(--primary); color: var(--on-primary);
      padding: 8px 14px; border-radius: 8px; font-weight: 600; text-decoration: none;
    }
    .skip:focus { top: 12px; }
    .wrap { width: 100%; max-width: 1080px; margin: 0 auto; padding: 0 16px; }
    @media (min-width: 768px) { .wrap { padding: 0 24px; } }

    /* Header */
    .site-header { background: var(--card); border-bottom: 1px solid var(--border); }
    .site-header .wrap {
      display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between;
      gap: 8px 24px; padding-top: 12px; padding-bottom: 12px;
    }
    .brand {
      display: inline-flex; align-items: center; gap: 10px;
      color: var(--fg); text-decoration: none; font-weight: 700; font-size: 1.125rem; letter-spacing: -0.01em;
      min-height: 44px;
    }
    .brand-mark {
      display: inline-grid; place-items: center; width: 30px; height: 30px; border-radius: 8px;
      background: var(--primary); color: var(--on-primary);
    }
    .brand small { font-weight: 500; font-size: 0.8125rem; color: var(--muted-fg); }
    .site-nav { margin-left: -7px; }
    .site-nav ul { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 0 2px; }
    @media (min-width: 720px) { .site-nav { margin-left: 0; } }
    .site-nav a {
      display: inline-flex; align-items: center; min-height: 44px; padding: 0 7px;
      color: var(--muted-fg); text-decoration: none; font-weight: 500; font-size: 0.875rem;
      border-radius: 8px; transition: color .15s ease, background-color .15s ease;
    }
    .site-nav a:hover { color: var(--fg); background: var(--muted); }
    @media (min-width: 480px) { .site-nav a { padding: 0 10px; font-size: 0.9375rem; } }
    .site-nav a[aria-current="page"] { color: var(--primary); box-shadow: inset 0 -2px 0 var(--primary); border-radius: 0; }

    /* Typography */
    h1, h2, h3 { line-height: 1.25; letter-spacing: -0.015em; margin: 0; }
    h1 { font-size: clamp(1.75rem, 1.2rem + 2.4vw, 2.5rem); font-weight: 700; }
    h2 { font-size: clamp(1.25rem, 1.1rem + 0.6vw, 1.5rem); font-weight: 600; }
    h3 { font-size: 1.0625rem; font-weight: 600; }
    p { margin: 0 0 14px; }
    ul, ol { margin: 0 0 14px; padding-left: 22px; }
    li { margin: 0 0 6px; }
    strong { font-weight: 600; }
    .eyebrow {
      display: inline-flex; align-items: center; gap: 8px; margin: 0 0 12px;
      font-size: 0.8125rem; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; color: var(--muted-fg);
    }
    .eyebrow::before { content: ""; width: 18px; height: 2px; background: var(--accent); }
    .lead { font-size: 1.125rem; color: var(--muted-fg); max-width: 60ch; }
    .tnum { font-variant-numeric: tabular-nums; }

    /* Legal document layout */
    .doc-head { padding: 40px 0 28px; border-bottom: 1px solid var(--border); background: var(--card); }
    .doc-head h1 { max-width: 24ch; margin-bottom: 12px; }
    .meta { display: grid; gap: 4px 24px; margin: 16px 0 0; padding: 0; font-size: 0.9375rem; color: var(--muted-fg); font-variant-numeric: tabular-nums; }
    .meta div { display: flex; flex-wrap: wrap; gap: 0 6px; }
    .meta dt { font-weight: 600; color: var(--fg); }
    .meta dd { margin: 0; }
    @media (min-width: 640px) { .meta { grid-template-columns: repeat(2, minmax(0, max-content)); } }
    .doc { padding-top: 32px; padding-bottom: 56px; }
    .prose { max-width: var(--measure); }
    .prose > section { padding-top: 32px; margin-top: 32px; border-top: 1px solid var(--border); scroll-margin-top: 16px; }
    .prose > section:first-of-type { border-top: 0; margin-top: 0; }
    .prose h2 { margin-bottom: 14px; display: flex; gap: 12px; align-items: baseline; }
    .prose h2 .num { color: var(--accent); font-variant-numeric: tabular-nums; font-weight: 600; min-width: 1.5em; }
    .prose h3 { margin: 22px 0 8px; }

    .callout {
      display: flex; gap: 14px; align-items: flex-start;
      background: var(--primary-soft); border: 1px solid var(--border); border-left: 3px solid var(--primary);
      border-radius: var(--radius); padding: 18px 18px; margin: 0 0 24px;
    }
    .callout .ico { color: var(--primary); margin-top: 3px; }
    .callout.warn { background: var(--accent-soft); border-left-color: var(--accent); }
    .callout.warn .ico { color: var(--accent); }
    .callout > div > :last-child { margin-bottom: 0; }
    .callout ul { margin-bottom: 0; }

    .toc { background: var(--card); border: 1px solid var(--border); border-radius: var(--radius); padding: 18px 20px; margin: 0 0 8px; }
    .toc h2 { font-size: 1rem; margin: 0 0 10px; }
    .toc ol { margin: 0; padding-left: 0; list-style: none; columns: 1; column-gap: 24px; counter-reset: toc; }
    @media (min-width: 640px) { .toc ol { columns: 2; } }
    .toc li { break-inside: avoid; margin: 0; counter-increment: toc; }
    .toc a { display: flex; gap: 8px; padding: 6px 0; text-decoration: none; color: var(--fg); min-height: 36px; align-items: center; }
    .toc a::before { content: counter(toc) "."; color: var(--muted-fg); font-variant-numeric: tabular-nums; min-width: 1.75em; }
    .toc a:hover { color: var(--primary); text-decoration: underline; }

    .table-wrap { overflow-x: auto; margin: 0 0 16px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); -webkit-overflow-scrolling: touch; }
    table { width: 100%; min-width: 560px; border-collapse: collapse; font-size: 0.9375rem; }
    caption { text-align: left; padding: 12px 14px 0; color: var(--muted-fg); font-size: 0.875rem; }
    th, td { text-align: left; vertical-align: top; padding: 12px 14px; border-bottom: 1px solid var(--border); }
    tbody tr:last-child td { border-bottom: 0; }
    th { font-weight: 600; color: var(--muted-fg); font-size: 0.8125rem; text-transform: uppercase; letter-spacing: 0.04em; background: var(--muted); }
    td:first-child { font-weight: 600; }

    .steps { list-style: none; padding: 0; counter-reset: step; }
    .steps > li { position: relative; padding: 0 0 18px 48px; counter-increment: step; margin: 0; }
    .steps > li::before {
      content: counter(step); position: absolute; left: 0; top: 0;
      width: 32px; height: 32px; border-radius: 50%; display: grid; place-items: center;
      border: 1.5px solid var(--primary); color: var(--primary); font-weight: 600; font-variant-numeric: tabular-nums; font-size: 0.9375rem;
    }
    .steps > li > strong:first-child { display: block; }

    .contact-card { background: var(--card); border: 1px solid var(--border); border-radius: var(--radius); padding: 20px; }
    .contact-card p { display: flex; align-items: center; gap: 10px; margin: 0 0 8px; }
    .contact-card p:last-child { margin-bottom: 0; }
    .contact-card .ico { color: var(--muted-fg); }

    .btn {
      display: inline-flex; align-items: center; justify-content: center; gap: 8px;
      min-height: 48px; padding: 0 20px; border-radius: 10px; font-weight: 600; font-size: 1rem;
      text-decoration: none; border: 1px solid transparent; transition: background-color .15s ease, border-color .15s ease, transform .15s ease;
    }
    .btn-primary { background: var(--primary); color: var(--on-primary); }
    .btn-primary:hover { filter: brightness(1.08); }
    .btn-secondary { background: var(--card); color: var(--fg); border-color: var(--border); }
    .btn-secondary:hover { background: var(--muted); }
    .btn:active { transform: scale(0.98); }

    /* Footer */
    .site-footer { border-top: 1px solid var(--border); background: var(--card); color: var(--muted-fg); font-size: 0.9375rem; }
    .site-footer .wrap { display: flex; flex-wrap: wrap; gap: 8px 24px; justify-content: space-between; align-items: center; padding-top: 24px; padding-bottom: 24px; }
    .site-footer p { margin: 0; }
    .site-footer ul { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 0 16px; }
    .site-footer li { margin: 0; }
    .site-footer a { color: var(--muted-fg); display: inline-flex; min-height: 44px; align-items: center; }
    .site-footer a:hover { color: var(--fg); }

    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after { transition-duration: 0.01ms !important; animation-duration: 0.01ms !important; scroll-behavior: auto !important; }
    }
    @media print {
      .site-header, .site-footer, .skip, .toc { display: none; }
      body { background: #fff; color: #000; }
    }
"""

NAV = [
    ("index.html", "Inicio"),
    ("privacy-policy.html", "Privacidad"),
    ("terminos_y_descripcion.html", "Términos"),
    ("eliminar-datos.html", "Eliminar datos"),
]


CUR = ' aria-current="page"'


def header(active):
    items = "\n".join(
        f'        <li><a href="{href}"{CUR if href == active else ""}>{label}</a></li>'
        for href, label in NAV
    )
    return f"""  <a class="skip" href="#contenido">Saltar al contenido</a>
  <header class="site-header">
    <div class="wrap">
      <a class="brand" href="index.html" aria-label="AdminPlus, inicio">
        <span class="brand-mark" aria-hidden="true">{icon("store", 18)}</span>
        <span>AdminPlus <small>por TotoLab</small></span>
      </a>
      <nav class="site-nav" aria-label="Principal">
        <ul>
{items}
        </ul>
      </nav>
    </div>
  </header>"""


def footer():
    items = "\n".join(f'        <li><a href="{h}">{l}</a></li>' for h, l in NAV[1:])
    return f"""  <footer class="site-footer">
    <div class="wrap">
      <p>© 2026 TotoLab · Managua, Nicaragua. AdminPlus es una marca de TotoLab.</p>
      <ul aria-label="Documentos legales">
{items}
        <li><a href="mailto:totolab2025@gmail.com">Contacto</a></li>
      </ul>
    </div>
  </footer>"""


def page(filename, title, description, og_title, body, extra_css=""):
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#1E3A8A" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#0B1220" media="(prefers-color-scheme: dark)">
  <meta name="color-scheme" content="light dark">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="es_NI">
  <meta property="og:site_name" content="AdminPlus">
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{description}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&amp;display=swap">
  <style>{BASE_CSS}{extra_css}  </style>
</head>
<body>
{header(filename)}
  <main id="contenido">
{body}
  </main>
{footer()}
</body>
</html>
"""
    (OUT / filename).write_text(html, encoding="utf-8")
    print("wrote", filename, len(html))


I = icon  # alias corto

# ---------------------------------------------------------------- index.html
PLAY_URL = "https://play.google.com/store/apps/details?id=com.totolab.myapplottery"

# Lista completa (se usa en la página de términos)
MODULES = [
    ("users", "Clientes", "Ficha de cada cliente con teléfono, correo, dirección y notas. Historial de compras y saldo pendiente a la vista."),
    ("package", "Inventario", "Productos y categorías con SKU, código de barras, costo, precio y stock. Entradas, salidas, ajustes y alertas de stock bajo."),
    ("receipt", "Facturación y ventas", "Facturas y recibos con descuentos, IVA configurable y pagos en efectivo, tarjeta, transferencia o crédito. Impresión térmica Bluetooth y PDF."),
    ("clock", "Cobros", "Cuentas por cobrar de ventas a crédito, abonos y fechas de vencimiento. Recordatorios que usted envía por WhatsApp u otra app."),
    ("wallet", "Finanzas", "Ingresos, gastos por categoría y caja diaria con apertura y cierre. Utilidad real del negocio, sin hojas de cálculo."),
    ("chart", "Reportes", "Ventas por período, productos más vendidos, márgenes y gastos para decidir qué comprar y qué precio poner."),
    ("scan", "Escáner", "Lea códigos de barras y QR con la cámara para buscar un producto, venderlo o contar inventario más rápido."),
    ("archive", "Respaldo", "Exporte toda la información a un archivo y guárdelo donde prefiera. Impórtelo para recuperar sus datos en otro teléfono."),
]

# Módulos de la landing (seis bloques)
LANDING_MODULES = [
    ("users", "Clientes", "Ficha de cada cliente con teléfono, correo, dirección y notas.",
     ["Historial de compras", "Saldo pendiente al día", "Búsqueda rápida"]),
    ("scan", "Inventario y escáner", "Productos, categorías, SKU y código de barras con costo, precio y stock.",
     ["Entradas, salidas y ajustes", "Alertas de stock bajo", "Escanee con la cámara para buscar, vender o contar"]),
    ("receipt", "Facturación", "Facturas y recibos en segundos, listos para imprimir o compartir.",
     ["Descuentos e IVA configurable", "Efectivo, tarjeta, transferencia o crédito", "Impresora térmica Bluetooth y PDF"]),
    ("clock", "Cobros", "Ventas a crédito bajo control, sin cuaderno de fiados.",
     ["Abonos y fechas de vencimiento", "Lista de quién le debe y cuánto", "Recordatorios por WhatsApp que usted envía"]),
    ("wallet", "Finanzas", "Lo que entra y lo que sale, en el mismo lugar que sus ventas.",
     ["Gastos por categoría", "Apertura y cierre de caja diaria", "Utilidad real del negocio"]),
    ("chart", "Reportes", "Números claros para decidir qué comprar y a qué precio vender.",
     ["Ventas por día, semana o mes", "Productos más vendidos", "Márgenes y gastos"]),
]

landing_modules_html = "\n".join(
    f"""          <li class="module">
            <span class="module-ico">{I(ic, 22)}</span>
            <h3>{name}</h3>
            <p>{text}</p>
            <ul class="checklist">
{chr(10).join(f'              <li>{I("check", 16)}{b}</li>' for b in bullets)}
            </ul>
          </li>""" for ic, name, text, bullets in LANDING_MODULES
)

FAQ = [
    ("¿Necesito internet para usar AdminPlus?",
     "No. Puede vender, cobrar, registrar gastos, imprimir y ver reportes sin conexión. Internet solo se usa para abrir enlaces externos, como esta política, y para compartir documentos si usted lo decide."),
    ("¿Dónde se guardan mis datos?",
     "En una base de datos local dentro de su teléfono. TotoLab no tiene acceso a ellos y no hay copias en servidores. Para protegerlos, exporte respaldos con frecuencia y guárdelos en un lugar seguro."),
    ("¿Tengo que crear una cuenta?",
     "No. AdminPlus no tiene inicio de sesión. Si en el futuro se agrega una cuenta o un respaldo en la nube, será opcional y la política de privacidad se actualizará antes."),
    ("¿Qué impresora puedo usar?",
     "Impresoras térmicas portátiles con Bluetooth, las más comunes en pulperías y tiendas. También puede generar un PDF de la factura y compartirlo sin imprimir."),
    ("¿Las facturas de AdminPlus sirven ante la DGI?",
     "Son documentos de control interno. Si su negocio está obligado a emitir facturas autorizadas por la DGI, debe seguir usando el sistema o talonario autorizado. Consulte a su contador."),
    ("¿Cómo paso mis datos a otro teléfono?",
     "Exporte un respaldo desde AdminPlus, copie el archivo al teléfono nuevo e impórtelo desde la app."),
    ("¿Cómo borro mi información?",
     'Desde la app (registro por registro o con Ajustes &gt; Restablecer datos), borrando los datos de la app en Android o desinstalándola. Vea <a href="eliminar-datos.html">Eliminar datos</a>.'),
]
faq_html = "\n".join(
    f"""          <details class="faq-item">
            <summary>{q}{I("arrow-right", 18, "ico chev")}</summary>
            <p>{a}</p>
          </details>""" for q, a in FAQ
)


def play_btn(cls="btn btn-primary btn-lg"):
    return (f'<a class="{cls}" href="{PLAY_URL}" rel="noopener">'
            f'{I("phone", 20)}<span><small>Disponible en</small> Google Play</span></a>')


INDEX_CSS = """
    .btn-lg { min-height: 56px; padding: 0 22px; }
    .btn-lg span { display: flex; flex-direction: column; line-height: 1.15; text-align: left; }
    .btn-lg small { font-size: 0.75rem; font-weight: 500; opacity: .85; }

    .hero { background: var(--card); border-bottom: 1px solid var(--border); padding: 40px 0 48px; }
    .hero .wrap { display: grid; gap: 40px; align-items: center; }
    @media (min-width: 900px) { .hero .wrap { grid-template-columns: 1.15fr 0.85fr; } .hero { padding: 72px 0; } }
    .hero h1 { max-width: 18ch; margin-bottom: 16px; }
    .hero h1 em { font-style: normal; color: var(--primary); }
    .badge {
      display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; margin-bottom: 18px;
      border: 1px solid var(--border); border-radius: 999px; font-size: 0.8125rem; font-weight: 600; color: var(--muted-fg); background: var(--bg);
    }
    .badge b { color: var(--accent); font-weight: 700; font-variant-numeric: tabular-nums; }
    .actions { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 24px; align-items: center; }
    .facts { list-style: none; padding: 0; margin: 28px 0 0; display: flex; flex-wrap: wrap; gap: 10px 20px; color: var(--muted-fg); font-size: 0.9375rem; }
    .facts li { display: inline-flex; align-items: center; gap: 8px; margin: 0; }
    .facts .ico { color: var(--success); }

    /* Mockups de teléfono en CSS */
    .phone {
      width: min(260px, 72vw); aspect-ratio: 9 / 18.5; margin: 0 auto; border-radius: 32px; padding: 10px;
      background: var(--fg); box-shadow: 0 24px 48px -24px rgba(15, 23, 42, 0.45); position: relative;
    }
    .phone::before { content: ""; position: absolute; top: 16px; left: 50%; width: 52px; height: 6px; margin-left: -26px; border-radius: 3px; background: var(--card); opacity: .35; z-index: 1; }
    .phone-screen {
      height: 100%; border-radius: 24px; background: var(--bg); overflow: hidden;
      display: flex; flex-direction: column; gap: 10px; padding: 30px 14px 16px;
    }
    .ph-bar { height: 10px; border-radius: 5px; background: var(--muted); }
    .ph-title { width: 55%; height: 14px; border-radius: 6px; background: var(--primary); opacity: .9; }
    .ph-kpis { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
    .ph-kpi { border: 1px solid var(--border); background: var(--card); border-radius: 10px; padding: 10px; display: grid; gap: 6px; }
    .ph-kpi i { display: block; height: 8px; border-radius: 4px; background: var(--muted); width: 60%; }
    .ph-kpi b { display: block; height: 14px; border-radius: 4px; background: var(--fg); opacity: .8; width: 80%; }
    .ph-kpi.acc b { background: var(--accent); opacity: 1; }
    .ph-row { display: flex; align-items: center; gap: 10px; border: 1px solid var(--border); background: var(--card); border-radius: 10px; padding: 10px; }
    .ph-row span { width: 26px; height: 26px; border-radius: 8px; background: var(--primary-soft); flex: none; }
    .ph-row i { flex: 1; height: 8px; border-radius: 4px; background: var(--muted); }
    .ph-row b { width: 36px; height: 10px; border-radius: 4px; background: var(--fg); opacity: .7; }
    .ph-cta { margin-top: auto; height: 36px; border-radius: 10px; background: var(--primary); }
    .ph-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
    .ph-tile { aspect-ratio: 1; border: 1px solid var(--border); background: var(--card); border-radius: 10px; padding: 8px; display: flex; flex-direction: column; justify-content: flex-end; gap: 5px; }
    .ph-tile::before { content: ""; flex: 1; border-radius: 6px; background: var(--primary-soft); }
    .ph-tile i { height: 6px; width: 70%; border-radius: 3px; background: var(--muted); }
    .ph-tile b { height: 8px; width: 45%; border-radius: 3px; background: var(--fg); opacity: .7; }
    .ph-tile.low b { background: var(--accent); opacity: 1; }
    .ph-chart { flex: 1; display: flex; align-items: flex-end; gap: 7px; padding: 12px 10px 10px; border: 1px solid var(--border); background: var(--card); border-radius: 10px; max-height: 150px; }
    .ph-chart span { flex: 1; border-radius: 4px 4px 0 0; background: var(--primary); opacity: .85; }
    .ph-chart span.hi { background: var(--accent); opacity: 1; }
    .ph-total { display: flex; justify-content: space-between; align-items: center; border-top: 1px dashed var(--border); padding-top: 10px; }
    .ph-total i { width: 40%; height: 8px; border-radius: 4px; background: var(--muted); }
    .ph-total b { width: 30%; height: 14px; border-radius: 4px; background: var(--fg); opacity: .85; }

    .section { padding: 56px 0; }
    @media (min-width: 900px) { .section { padding: 80px 0; } }
    .section + .section { border-top: 1px solid var(--border); }
    .section.alt { background: var(--card); }
    .section-head { max-width: 62ch; margin-bottom: 28px; }
    .section-head h2 { margin-bottom: 10px; }
    .section-head p { color: var(--muted-fg); margin: 0; }

    /* Problema / solución */
    .ps { display: grid; gap: 16px; }
    @media (min-width: 768px) { .ps { grid-template-columns: 1fr 1fr; } }
    .ps-col { border: 1px solid var(--border); border-radius: var(--radius); padding: 22px 20px; background: var(--card); }
    .section.alt .ps-col { background: var(--bg); }
    .ps-col h3 { display: flex; align-items: center; gap: 10px; margin-bottom: 14px; }
    .ps-col ul { list-style: none; padding: 0; margin: 0; display: grid; gap: 12px; }
    .ps-col li { display: flex; gap: 10px; align-items: flex-start; margin: 0; }
    .ps-col li .ico { margin-top: 3px; }
    .ps-before h3 .ico, .ps-before li .ico { color: var(--muted-fg); }
    .ps-after { border-color: var(--primary); }
    .ps-after h3 .ico, .ps-after li .ico { color: var(--success); }

    /* Módulos */
    .modules { list-style: none; padding: 0; margin: 0; display: grid; gap: 1px; background: var(--border); border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; }
    @media (min-width: 640px) { .modules { grid-template-columns: repeat(2, 1fr); } }
    @media (min-width: 960px) { .modules { grid-template-columns: repeat(3, 1fr); } }
    .module { background: var(--card); padding: 24px 22px; margin: 0; }
    .module-ico { display: inline-grid; place-items: center; width: 40px; height: 40px; border-radius: 10px; background: var(--primary-soft); color: var(--primary); margin-bottom: 14px; }
    .module h3 { margin-bottom: 6px; }
    .module > p { color: var(--muted-fg); font-size: 0.9375rem; margin: 0 0 12px; }
    .checklist { list-style: none; padding: 0; margin: 0; display: grid; gap: 6px; font-size: 0.9375rem; }
    .checklist li { display: flex; gap: 8px; align-items: flex-start; margin: 0; }
    .checklist .ico { color: var(--success); margin-top: 4px; }

    /* Offline / privacidad */
    .offline { display: grid; gap: 28px; align-items: start; }
    @media (min-width: 900px) { .offline { grid-template-columns: 0.9fr 1.1fr; gap: 48px; } }
    .offline-statement { border-left: 3px solid var(--accent); padding-left: 18px; }
    .offline-statement h2 { margin-bottom: 12px; }
    .offline-statement p { color: var(--muted-fg); }
    .privacy-grid { display: grid; gap: 12px; }
    @media (min-width: 600px) { .privacy-grid { grid-template-columns: repeat(2, 1fr); } }
    .p-item { display: flex; gap: 14px; align-items: flex-start; background: var(--card); border: 1px solid var(--border); border-radius: var(--radius); padding: 18px; }
    .section.alt .p-item { background: var(--bg); }
    .p-item .ico { color: var(--primary); margin-top: 2px; }
    .p-item h3 { margin-bottom: 4px; font-size: 1rem; }
    .p-item p { margin: 0; color: var(--muted-fg); font-size: 0.9375rem; }

    /* Pasos */
    .how { list-style: none; padding: 0; margin: 0; display: grid; gap: 16px; counter-reset: how; }
    @media (min-width: 768px) { .how { grid-template-columns: repeat(3, 1fr); } }
    .how li { margin: 0; counter-increment: how; padding: 22px 20px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); }
    .how li::before {
      content: counter(how, decimal-leading-zero); display: block; margin-bottom: 12px;
      font-size: 2rem; font-weight: 700; line-height: 1; color: var(--accent); font-variant-numeric: tabular-nums; letter-spacing: -0.02em;
    }
    .how h3 { margin-bottom: 6px; }
    .how p { margin: 0; color: var(--muted-fg); font-size: 0.9375rem; }

    /* Capturas */
    .shots { display: grid; gap: 32px; grid-template-columns: 1fr; }
    @media (min-width: 720px) { .shots { grid-template-columns: repeat(3, 1fr); gap: 24px; } }
    .shot { margin: 0; display: flex; flex-direction: column; align-items: center; gap: 14px; }
    .shot .phone { width: min(220px, 64vw); }
    .shot figcaption { text-align: center; font-size: 0.9375rem; color: var(--muted-fg); }
    .shot figcaption strong { display: block; color: var(--fg); }
    .shots-note { display: flex; align-items: center; gap: 8px; margin: 24px 0 0; color: var(--muted-fg); font-size: 0.875rem; }

    .audience { list-style: none; padding: 0; margin: 20px 0 0; display: flex; flex-wrap: wrap; gap: 8px; }
    .audience li { margin: 0; padding: 6px 12px; border: 1px solid var(--border); border-radius: 999px; background: var(--card); font-size: 0.9375rem; }

    /* FAQ */
    .faq { max-width: var(--measure); border-top: 1px solid var(--border); }
    .faq-item { border-bottom: 1px solid var(--border); }
    .faq-item summary {
      list-style: none; cursor: pointer; display: flex; justify-content: space-between; align-items: center; gap: 16px;
      min-height: 56px; padding: 14px 0; font-weight: 600; font-size: 1.0625rem;
    }
    .faq-item summary::-webkit-details-marker { display: none; }
    .faq-item summary:hover { color: var(--primary); }
    .faq-item .chev { color: var(--muted-fg); transform: rotate(90deg); transition: transform .15s ease; }
    .faq-item[open] .chev { transform: rotate(-90deg); }
    .faq-item p { margin: 0 0 18px; color: var(--muted-fg); max-width: 64ch; }

    /* CTA final */
    .cta { background: var(--primary); color: var(--on-primary); padding: 56px 0; }
    .cta .wrap { display: grid; gap: 24px; align-items: center; }
    @media (min-width: 768px) { .cta .wrap { grid-template-columns: 1fr auto; } }
    .cta h2 { margin-bottom: 8px; color: var(--on-primary); }
    .cta p { margin: 0; opacity: .9; max-width: 56ch; }
    .cta .btn-primary { background: var(--on-primary); color: var(--primary); }
    .cta .btn-primary:hover { filter: none; opacity: .92; }
    .cta :focus-visible { outline-color: var(--on-primary); }

    .contact-row { display: grid; gap: 16px; }
    @media (min-width: 720px) { .contact-row { grid-template-columns: 1fr 1fr; align-items: center; } }
    .docs-inline { list-style: none; padding: 0; margin: 14px 0 0; display: flex; flex-wrap: wrap; gap: 4px 18px; }
    .docs-inline li { margin: 0; }
    .docs-inline a { display: inline-flex; align-items: center; gap: 6px; min-height: 44px; }
"""

PHONE_SALES = """<div class="phone" aria-hidden="true"><div class="phone-screen">
              <div class="ph-title"></div>
              <div class="ph-row"><span></span><i></i><b></b></div>
              <div class="ph-row"><span></span><i></i><b></b></div>
              <div class="ph-row"><span></span><i></i><b></b></div>
              <div class="ph-total"><i></i><b></b></div>
              <div class="ph-cta"></div>
            </div></div>"""
PHONE_INV = """<div class="phone" aria-hidden="true"><div class="phone-screen">
              <div class="ph-title"></div>
              <div class="ph-bar"></div>
              <div class="ph-grid">
                <div class="ph-tile"><i></i><b></b></div>
                <div class="ph-tile low"><i></i><b></b></div>
                <div class="ph-tile"><i></i><b></b></div>
                <div class="ph-tile"><i></i><b></b></div>
              </div>
            </div></div>"""
PHONE_REP = """<div class="phone" aria-hidden="true"><div class="phone-screen">
              <div class="ph-title"></div>
              <div class="ph-kpis">
                <div class="ph-kpi"><i></i><b></b></div>
                <div class="ph-kpi acc"><i></i><b></b></div>
              </div>
              <div class="ph-chart"><span style="height:40%"></span><span style="height:65%"></span><span style="height:50%"></span><span class="hi" style="height:90%"></span><span style="height:70%"></span><span style="height:55%"></span></div>
              <div class="ph-row"><span></span><i></i><b></b></div>
            </div></div>"""

INDEX_BODY = f"""    <section class="hero" aria-labelledby="hero-title">
      <div class="wrap">
        <div>
          <p class="badge">Versión <b>2.0</b> · Android</p>
          <h1 id="hero-title">Su negocio en orden, <em>desde el teléfono</em>.</h1>
          <p class="lead">Clientes, inventario, ventas, cobros y finanzas en una sola app para pulperías, tiendas, ferreterías, cafeterías y emprendimientos de Nicaragua y Centroamérica. Funciona sin internet y sus datos se quedan en su teléfono.</p>
          <div class="actions">
            {play_btn()}
            <a class="btn btn-secondary" href="#modulos">Ver qué incluye {I("arrow-right", 18)}</a>
          </div>
          <ul class="facts" aria-label="Características clave">
            <li>{I("check", 18)} Sin cuentas</li>
            <li>{I("check", 18)} Sin publicidad</li>
            <li>{I("check", 18)} Funciona sin conexión</li>
          </ul>
        </div>
        <div role="img" aria-label="Ilustración de la pantalla de inicio de AdminPlus con resumen de ventas">
          {PHONE_REP}
        </div>
      </div>
    </section>

    <section class="section" id="problema" aria-labelledby="problema-title">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">El problema</p>
          <h2 id="problema-title">El cuaderno ya no alcanza</h2>
          <p>En un negocio pequeño, la misma persona vende, cobra, compra y lleva las cuentas. Cuando todo está en papel o en la memoria, el dinero se escapa sin que se note.</p>
        </div>
        <div class="ps">
          <div class="ps-col ps-before">
            <h3>{I("alert", 20)} Sin AdminPlus</h3>
            <ul>
              <li>{I("x", 18)}<span>Fiados anotados en un cuaderno que nadie revisa a tiempo.</span></li>
              <li>{I("x", 18)}<span>Se acaba un producto y uno se entera cuando el cliente lo pide.</span></li>
              <li>{I("x", 18)}<span>Al final del día no cuadra la caja y no se sabe por qué.</span></li>
              <li>{I("x", 18)}<span>Se vende mucho, pero no se sabe cuánto se gana de verdad.</span></li>
            </ul>
          </div>
          <div class="ps-col ps-after">
            <h3>{I("check", 20)} Con AdminPlus</h3>
            <ul>
              <li>{I("check", 18)}<span>Cada crédito con su saldo, abonos y fecha de vencimiento.</span></li>
              <li>{I("check", 18)}<span>Alertas de stock bajo antes de quedarse sin producto.</span></li>
              <li>{I("check", 18)}<span>Apertura y cierre de caja con el detalle de cada venta y gasto.</span></li>
              <li>{I("check", 18)}<span>Reportes de márgenes y utilidad con un toque.</span></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="section alt" id="modulos" aria-labelledby="modulos-title">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">Módulos</p>
          <h2 id="modulos-title">Todo lo que el mostrador necesita</h2>
          <p>Los módulos trabajan juntos: una venta descuenta el stock, suma a la caja del día y, si es a crédito, crea la cuenta por cobrar del cliente.</p>
        </div>
        <ul class="modules">
{landing_modules_html}
        </ul>
      </div>
    </section>

    <section class="section" id="privacidad" aria-labelledby="privacidad-title">
      <div class="wrap offline">
        <div class="offline-statement">
          <p class="eyebrow">Sin internet, sin nube</p>
          <h2 id="privacidad-title">Funciona sin internet. Sus datos se quedan en su teléfono.</h2>
          <p>AdminPlus guarda la información en una base de datos local del dispositivo. TotoLab no la ve, no la copia y no la vende. Usted decide cuándo algo sale del teléfono.</p>
          <p><a href="privacy-policy.html">Leer la política de privacidad</a></p>
        </div>
        <div class="privacy-grid">
          <div class="p-item">{I("wifi-off", 22)}<div><h3>Venda sin señal</h3><p>Vender, cobrar, imprimir y ver reportes no requiere conexión.</p></div></div>
          <div class="p-item">{I("eye-off", 22)}<div><h3>Sin rastreo ni anuncios</h3><p>Sin cuentas, publicidad, analíticas ni SDK de terceros que recolecten datos.</p></div></div>
          <div class="p-item">{I("share", 22)}<div><h3>Usted decide qué sale</h3><p>Solo cuando comparte una factura, envía un recordatorio o exporta un respaldo.</p></div></div>
          <div class="p-item">{I("archive", 22)}<div><h3>Respaldo en sus manos</h3><p>Exporte un archivo con toda la información e impórtelo en otro teléfono.</p></div></div>
        </div>
      </div>
    </section>

    <section class="section alt" id="como-funciona" aria-labelledby="como-title">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">Cómo funciona</p>
          <h2 id="como-title">Listo para vender en tres pasos</h2>
        </div>
        <ol class="how">
          <li><h3>Instale y configure su negocio</h3><p>Descargue AdminPlus, escriba el nombre y los datos de su negocio y defina el IVA. Sin registros ni contraseñas.</p></li>
          <li><h3>Cargue sus productos</h3><p>Agréguelos a mano o escaneando el código de barras, con costo, precio y existencias iniciales.</p></li>
          <li><h3>Venda y cobre</h3><p>Facture en el mostrador, imprima o comparta el recibo y revise al cierre cuánto vendió y cuánto le deben.</p></li>
        </ol>
      </div>
    </section>

    <section class="section" id="capturas" aria-labelledby="capturas-title">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">La app</p>
          <h2 id="capturas-title">Así se ve AdminPlus</h2>
          <p>Hecha para usarse con una mano, detrás del mostrador.</p>
        </div>
        <div class="shots">
          <figure class="shot">
            {PHONE_SALES}
            <figcaption><strong>Ventas</strong>Factura con total y cobro</figcaption>
          </figure>
          <figure class="shot">
            {PHONE_INV}
            <figcaption><strong>Inventario</strong>Productos y alertas de stock bajo</figcaption>
          </figure>
          <figure class="shot">
            {PHONE_REP}
            <figcaption><strong>Reportes</strong>Ventas y utilidad del período</figcaption>
          </figure>
        </div>
        <p class="shots-note">{I("image", 16)} Ilustraciones de referencia. Pronto publicaremos capturas reales de la versión 2.0.</p>
        <ul class="audience" aria-label="Tipos de negocio">
          <li>Pulperías</li>
          <li>Tiendas y misceláneas</li>
          <li>Ferreterías</li>
          <li>Cafeterías y comiderías</li>
          <li>Distribuidores pequeños</li>
          <li>Emprendedores</li>
        </ul>
      </div>
    </section>

    <section class="section alt" id="preguntas" aria-labelledby="faq-title">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">Preguntas frecuentes</p>
          <h2 id="faq-title">Lo que más nos preguntan</h2>
        </div>
        <div class="faq">
{faq_html}
        </div>
      </div>
    </section>

    <section class="cta" aria-labelledby="cta-title">
      <div class="wrap">
        <div>
          <h2 id="cta-title">Ponga su negocio en orden hoy</h2>
          <p>Descargue AdminPlus en su teléfono Android y empiece a vender en minutos.</p>
        </div>
        {play_btn()}
      </div>
    </section>

    <section class="section" id="contacto" aria-labelledby="contacto-title">
      <div class="wrap contact-row">
        <div class="section-head" style="margin:0">
          <p class="eyebrow">Contacto</p>
          <h2 id="contacto-title">¿Preguntas o sugerencias?</h2>
          <p>Escríbanos. AdminPlus es desarrollada por TotoLab en Managua, Nicaragua.</p>
          <ul class="docs-inline" aria-label="Documentos">
            <li><a href="privacy-policy.html">{I("shield", 16)} Política de privacidad</a></li>
            <li><a href="terminos_y_descripcion.html">{I("file", 16)} Términos y condiciones</a></li>
            <li><a href="eliminar-datos.html">{I("trash", 16)} Eliminar datos</a></li>
          </ul>
        </div>
        <div class="contact-card">
          <p>{I("mail", 18)} <a href="mailto:totolab2025@gmail.com">totolab2025@gmail.com</a></p>
          <p>{I("map-pin", 18)} Managua, Nicaragua</p>
        </div>
      </div>
    </section>"""

page("index.html",
     "AdminPlus – Gestión para pequeños negocios",
     "AdminPlus organiza clientes, inventario, facturación, cobros y finanzas de pequeños negocios en Android. Funciona sin internet y guarda los datos solo en el teléfono.",
     "AdminPlus – Gestión para pequeños negocios",
     INDEX_BODY, INDEX_CSS)

# ---------------------------------------------------------------- 404.html
NF_CSS = """
    .nf { padding: 72px 0 96px; }
    .nf-code { font-size: clamp(4rem, 3rem + 6vw, 7rem); font-weight: 700; line-height: 1; color: var(--accent); font-variant-numeric: tabular-nums; letter-spacing: -0.04em; margin: 0 0 16px; }
    .nf h1 { margin-bottom: 12px; }
    .nf .actions { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 24px; }
"""
NF_BODY = f"""    <section class="nf">
      <div class="wrap">
        <p class="nf-code" aria-hidden="true">404</p>
        <h1>Página no encontrada</h1>
        <p class="lead">La dirección que buscó no existe o cambió de lugar. Estas son las páginas disponibles:</p>
        <div class="actions">
          <a class="btn btn-primary" href="index.html">Ir al inicio {I("arrow-right", 18)}</a>
          <a class="btn btn-secondary" href="privacy-policy.html">Política de privacidad</a>
          <a class="btn btn-secondary" href="terminos_y_descripcion.html">Términos y condiciones</a>
          <a class="btn btn-secondary" href="eliminar-datos.html">Eliminar datos</a>
        </div>
      </div>
    </section>"""
page("404.html", "Página no encontrada – AdminPlus",
     "La página que busca no existe en el sitio de AdminPlus.",
     "Página no encontrada – AdminPlus", NF_BODY, NF_CSS)


# ------------------------------------------------------ privacy-policy.html
PRIV_SECTIONS = [
    ("responsable", "Responsable"),
    ("alcance", "Alcance"),
    ("informacion", "Información que se guarda en el dispositivo"),
    ("no-recopila", "Información que no se recopila"),
    ("permisos", "Permisos del dispositivo"),
    ("compartir", "Cuándo sale la información del dispositivo"),
    ("terceros", "Datos de terceros"),
    ("conservacion", "Conservación y eliminación"),
    ("seguridad", "Seguridad"),
    ("menores", "Menores de edad"),
    ("futuro", "Funciones futuras opcionales"),
    ("cambios", "Cambios en esta política"),
    ("contacto", "Contacto"),
]


def toc(sections):
    items = "\n".join(f'            <li><a href="#{sid}">{t}</a></li>' for sid, t in sections)
    return f"""        <nav class="toc" aria-labelledby="toc-title">
          <h2 id="toc-title">Contenido</h2>
          <ol>
{items}
          </ol>
        </nav>"""


def h2(sections, sid):
    idx = [s for s, _ in sections].index(sid) + 1
    title = dict(sections)[sid]
    return f'<h2><span class="num">{idx}.</span> {title}</h2>'


P = lambda sid: h2(PRIV_SECTIONS, sid)

PERMS = [
    ("Cámara", "Escanear códigos de barras y QR para buscar, vender y contar productos. Tomar, si usted lo desea, una foto de un producto.",
     "Las imágenes del escáner se procesan en el momento y no se guardan ni se envían. Las fotos de productos se guardan solo en el almacenamiento privado de la app."),
    ("Bluetooth (buscar y conectar dispositivos)", "Encontrar y conectarse a la impresora térmica para imprimir facturas y recibos.",
     "No se usa para rastrear ni identificar otros dispositivos."),
    ("Ubicación (solo Android 11 o anterior)", "Android exige este permiso en esas versiones para poder buscar dispositivos Bluetooth cercanos.",
     "AdminPlus no lee, no guarda y no envía la ubicación del dispositivo. En Android 12 o posterior no se solicita."),
    ("Acceso a internet", "Abrir enlaces externos, como esta política o el correo de soporte.",
     "La app no envía la información de su negocio a través de internet."),
    ("Vibración", "Dar respuesta táctil al pulsar botones o al leer un código.", "No accede a ningún dato."),
]
perm_rows = "\n".join(
    f"""              <tr>
                <td>{p}</td>
                <td>{u}</td>
                <td>{n}</td>
              </tr>""" for p, u, n in PERMS)

PRIV_BODY = f"""    <div class="doc-head">
      <div class="wrap">
        <p class="eyebrow">Documento legal</p>
        <h1>Política de Privacidad de AdminPlus</h1>
        <dl class="meta">
          <div><dt>Entrada en vigor:</dt><dd>4 de octubre de 2026</dd></div>
          <div><dt>Versión de la app:</dt><dd>2.0</dd></div>
          <div><dt>Paquete:</dt><dd>com.totolab.myapplottery</dd></div>
          <div><dt>Desarrollador:</dt><dd>TotoLab, Managua, Nicaragua</dd></div>
        </dl>
      </div>
    </div>
    <div class="wrap doc">
      <article class="prose">
        <p>Esta política explica qué información maneja la aplicación AdminPlus, cómo se usa y qué control tiene quien la usa. Aplica a la aplicación para Android distribuida en Google Play.</p>

        <div class="callout" role="note">
          {I("shield", 22)}
          <div>
            <p><strong>En resumen</strong></p>
            <ul>
              <li>AdminPlus <strong>no recopila ni envía datos</strong> a TotoLab ni a ningún servidor.</li>
              <li>Toda la información del negocio se guarda <strong>únicamente en el dispositivo</strong> y la app funciona sin conexión.</li>
              <li>No hay cuentas de usuario, publicidad, analíticas, rastreo ni componentes de terceros que recolecten datos.</li>
              <li>La información solo sale del dispositivo cuando el usuario decide compartir una factura o recibo, enviar un recordatorio de cobro o exportar un respaldo.</li>
              <li>El usuario puede borrar sus datos en cualquier momento desde la app o desde Android.</li>
            </ul>
          </div>
        </div>

{toc(PRIV_SECTIONS)}

        <section id="responsable">
          {P("responsable")}
          <p>El responsable de la aplicación es <strong>TotoLab</strong>, con sede en Managua, Nicaragua. Los datos de contacto figuran en la <a href="#contacto">sección 13</a>.</p>
        </section>

        <section id="alcance">
          {P("alcance")}
          <p>AdminPlus es una herramienta de gestión para pequeños negocios: clientes, inventario, facturación y ventas, cobros, finanzas, reportes, escáner de códigos y respaldo. Esta política cubre la versión 2.0 y posteriores mientras no sea reemplazada por una versión más reciente publicada en esta misma dirección.</p>
        </section>

        <section id="informacion">
          {P("informacion")}
          <p>Para funcionar, AdminPlus guarda en una base de datos local (SQLite) dentro del almacenamiento privado del dispositivo la información que el usuario registra:</p>
          <ul>
            <li><strong>Datos del negocio:</strong> nombre, teléfono, dirección, tasa de impuesto y demás datos que el usuario configure para sus facturas y recibos.</li>
            <li><strong>Clientes:</strong> nombre, teléfono, correo electrónico, dirección y notas de las personas que el usuario decide registrar, junto con su historial de compras y saldo pendiente. Todos los campos son opcionales salvo el nombre.</li>
            <li><strong>Inventario:</strong> productos, categorías, SKU, códigos de barras, costos, precios, existencias y movimientos de entrada, salida y ajuste. Si el usuario lo desea, una foto de cada producto.</li>
            <li><strong>Ventas y facturación:</strong> facturas, recibos, productos vendidos, descuentos, impuestos, importes, fechas y método de pago (efectivo, tarjeta, transferencia o crédito). AdminPlus solo registra el método de pago: no procesa pagos ni guarda números de tarjeta.</li>
            <li><strong>Cobros:</strong> cuentas por cobrar, abonos y fechas de vencimiento.</li>
            <li><strong>Finanzas:</strong> ingresos, gastos y sus categorías, y registros de apertura y cierre de caja.</li>
            <li><strong>Preferencias:</strong> el tema visual elegido y la impresora Bluetooth seleccionada.</li>
          </ul>
          <p>TotoLab <strong>no tiene acceso</strong> a esta información: no se transmite, no se sincroniza y no se almacena en servidores externos.</p>
        </section>

        <section id="no-recopila">
          {P("no-recopila")}
          <p>AdminPlus no recopila, ni para TotoLab ni para terceros:</p>
          <ul>
            <li>Datos de cuenta, contraseñas o identificadores de usuario (la app no tiene inicio de sesión).</li>
            <li>Ubicación del dispositivo.</li>
            <li>Contactos, mensajes, historial de llamadas ni archivos personales.</li>
            <li>Identificadores de publicidad, estadísticas de uso, informes de fallos ni datos de rastreo.</li>
          </ul>
          <p>La app no incluye publicidad ni kits de desarrollo (SDK) de terceros que recolecten datos.</p>
        </section>

        <section id="permisos">
          {P("permisos")}
          <p>AdminPlus solicita los siguientes permisos, cada uno para una función concreta. Los permisos de cámara y Bluetooth se piden solo cuando el usuario usa la función que los necesita, y pueden revocarse en cualquier momento desde los ajustes de Android.</p>
          <div class="table-wrap" tabindex="0" role="region" aria-label="Tabla de permisos">
            <table>
              <thead>
                <tr><th scope="col">Permiso</th><th scope="col">Para qué se usa</th><th scope="col">Qué no hace</th></tr>
              </thead>
              <tbody>
{perm_rows}
              </tbody>
            </table>
          </div>
          <p>A partir de la versión 2.0, AdminPlus <strong>ya no solicita</strong> el permiso de almacenamiento externo ni el permiso para mostrarse sobre otras aplicaciones.</p>
        </section>

        <section id="compartir">
          {P("compartir")}
          <p>TotoLab <strong>no vende, no alquila y no comparte</strong> información con terceros. La información solo sale del dispositivo cuando el usuario lo decide, en estos casos:</p>
          <ul>
            <li><strong>Compartir una factura o recibo:</strong> la app genera un PDF o una imagen y abre el menú de compartir de Android.</li>
            <li><strong>Enviar un recordatorio de cobro:</strong> la app prepara el mensaje y lo abre en WhatsApp o en otra aplicación elegida por el usuario, quien revisa y envía el mensaje manualmente. AdminPlus no envía mensajes de forma automática.</li>
            <li><strong>Exportar un respaldo:</strong> la app crea un archivo con la información del negocio y el usuario elige dónde guardarlo (por ejemplo, en el almacenamiento del teléfono o en un servicio de su preferencia).</li>
            <li><strong>Imprimir:</strong> los datos de la factura o recibo se envían por Bluetooth a la impresora térmica que el usuario conectó.</li>
          </ul>
          <p>En todos los casos, el usuario decide con qué aplicación, servicio o persona comparte la información. A partir de ese momento, queda sujeta a las políticas de esa aplicación o servicio. Se recomienda guardar los archivos de respaldo en un lugar seguro, ya que contienen toda la información del negocio, incluidos los datos de clientes.</p>
        </section>

        <section id="terceros">
          {P("terceros")}
          <p>Al registrar datos de clientes, el usuario de AdminPlus actúa como responsable de esa información. Le corresponde informar a sus clientes, contar con su consentimiento cuando la ley lo exija y usar sus datos conforme a la legislación aplicable, incluida la Ley n.º 787 de Protección de Datos Personales de Nicaragua.</p>
        </section>

        <section id="conservacion">
          {P("conservacion")}
          <p>La información permanece en el dispositivo hasta que el usuario la elimina. Puede borrarse de estas formas:</p>
          <ul>
            <li>Eliminando registros individuales (clientes, productos, ventas, gastos u otros) desde la propia aplicación.</li>
            <li>Usando <em>Ajustes &gt; Restablecer datos</em> dentro de AdminPlus, lo que borra toda la información registrada.</li>
            <li>Borrando los datos de la aplicación desde los ajustes de Android.</li>
            <li>Desinstalando la aplicación, lo que elimina toda la información guardada en ella.</li>
          </ul>
          <p>Los archivos de respaldo exportados y los documentos compartidos quedan fuera de la app y deben eliminarse por separado. Como TotoLab no conserva copias en servidores, una vez eliminada la información no puede recuperarse, salvo que el usuario tenga su propio respaldo. Las instrucciones paso a paso están en <a href="eliminar-datos.html">Eliminar sus datos</a>.</p>
        </section>

        <section id="seguridad">
          {P("seguridad")}
          <p>La información se guarda en el almacenamiento privado de la aplicación, al que Android impide el acceso de otras aplicaciones. Se recomienda proteger el dispositivo con bloqueo de pantalla, ya que cualquier persona con acceso al teléfono desbloqueado puede ver la información registrada, y mantener los archivos de respaldo en un lugar de confianza.</p>
        </section>

        <section id="menores">
          {P("menores")}
          <p>AdminPlus es una herramienta dirigida a personas adultas que administran negocios. No está dirigida a menores de 18 años y no recopila intencionalmente información de menores.</p>
        </section>

        <section id="futuro">
          {P("futuro")}
          <div class="callout" role="note">
            {I("cloud", 22)}
            <div>
              <p>En versiones futuras, TotoLab podría agregar un <strong>inicio de sesión opcional</strong> y un <strong>respaldo en la nube</strong>. Hoy esas funciones no existen.</p>
              <p>Si se incorporan, serán opcionales, la app seguirá funcionando sin ellas y esta política se actualizará <strong>antes</strong> de activarlas, explicando qué datos se envían, dónde se guardan y cómo eliminarlos.</p>
            </div>
          </div>
        </section>

        <section id="cambios">
          {P("cambios")}
          <p>Si la aplicación cambia la forma en que maneja la información, esta política se actualizará en esta misma dirección y se modificará la fecha de entrada en vigor indicada al inicio. Los cambios importantes también se indicarán en la descripción de la actualización en Google Play.</p>
        </section>

        <section id="contacto">
          {P("contacto")}
          <p>Para consultas sobre esta política o sobre la privacidad en AdminPlus:</p>
          <div class="contact-card">
            <p><strong>TotoLab</strong></p>
            <p>{I("mail", 18)} <a href="mailto:totolab2025@gmail.com">totolab2025@gmail.com</a></p>
            <p>{I("map-pin", 18)} Managua, Nicaragua</p>
          </div>
        </section>
      </article>
    </div>"""

page("privacy-policy.html",
     "Política de Privacidad – AdminPlus",
     "Política de privacidad de AdminPlus, la app de gestión para pequeños negocios de TotoLab. Los datos se guardan solo en el dispositivo.",
     "Política de Privacidad de AdminPlus",
     PRIV_BODY)

# --------------------------------------------- terminos_y_descripcion.html
TERMS_SECTIONS = [
    ("aceptacion", "Aceptación"),
    ("uso", "Uso de la aplicación"),
    ("requisitos", "Requisitos"),
    ("datos", "Datos del usuario y respaldos"),
    ("fiscal", "Facturas y obligaciones fiscales"),
    ("clientes", "Datos de clientes"),
    ("terceros", "Servicios y dispositivos de terceros"),
    ("propiedad", "Propiedad intelectual"),
    ("garantia", "Sin garantía"),
    ("responsabilidad", "Limitación de responsabilidad"),
    ("cambios", "Cambios en la app y en estos términos"),
    ("ley", "Ley aplicable"),
    ("contacto", "Contacto"),
]
T = lambda sid: h2(TERMS_SECTIONS, sid)

desc_modules = "\n".join(
    f"""            <li class="dm">{I(ic, 20)}<div><strong>{name}.</strong> {text}</div></li>""" for ic, name, text in MODULES)

TERMS_CSS = """
    .dm-list { list-style: none; padding: 0; margin: 0 0 16px; display: grid; gap: 12px; }
    .dm { display: flex; gap: 12px; align-items: flex-start; margin: 0; padding: 14px 16px; background: var(--card); border: 1px solid var(--border); border-radius: var(--radius); }
    .dm .ico { color: var(--primary); margin-top: 3px; }
    .part { font-size: 0.8125rem; font-weight: 600; letter-spacing: .06em; text-transform: uppercase; color: var(--muted-fg); margin: 48px 0 8px; padding-top: 24px; border-top: 2px solid var(--fg); }
    .part:first-child { margin-top: 0; }
    .part-title { margin-bottom: 16px; }
"""

TERMS_BODY = f"""    <div class="doc-head">
      <div class="wrap">
        <p class="eyebrow">Producto y condiciones</p>
        <h1>AdminPlus: descripción y Términos y Condiciones</h1>
        <dl class="meta">
          <div><dt>Última actualización:</dt><dd>4 de octubre de 2026</dd></div>
          <div><dt>Versión de la app:</dt><dd>2.0</dd></div>
          <div><dt>Desarrollador:</dt><dd>TotoLab, Managua, Nicaragua</dd></div>
        </dl>
      </div>
    </div>
    <div class="wrap doc">
      <article class="prose">
        <p class="part" id="descripcion">Parte 1</p>
        <h2 class="part-title">Descripción del producto</h2>
        <p>AdminPlus es una aplicación para Android que ayuda a administrar pequeños negocios: <strong>pulperías, tiendas, ferreterías, cafeterías, distribuidores y emprendedores</strong> de Nicaragua y Centroamérica. Reúne en un solo lugar los clientes, el inventario, las ventas, los cobros y las finanzas del negocio, y funciona sin conexión a internet.</p>
        <ul class="dm-list">
{desc_modules}
        </ul>
        <div class="callout" role="note">
          {I("info", 22)}
          <div>
            <p><strong>Importante.</strong> AdminPlus es una herramienta de <strong>gestión administrativa</strong> que guarda la información solo en el dispositivo. No procesa pagos en línea, no cobra a sus clientes en su nombre y no envía información a TotoLab. Los detalles están en la <a href="privacy-policy.html">Política de Privacidad</a>.</p>
          </div>
        </div>

        <p class="part" id="terminos">Parte 2</p>
        <h2 class="part-title">Términos y Condiciones</h2>
        <p>Estos términos regulan el uso de AdminPlus. Léalos con atención.</p>

{toc(TERMS_SECTIONS)}

        <section id="aceptacion">
          {T("aceptacion")}
          <p>Al descargar, instalar o usar AdminPlus, el usuario acepta estos Términos y Condiciones y la <a href="privacy-policy.html">Política de Privacidad</a>. Si no está de acuerdo, debe dejar de usar la aplicación y desinstalarla.</p>
        </section>

        <section id="uso">
          {T("uso")}
          <p>AdminPlus se ofrece como herramienta de apoyo para registrar y organizar la información de un negocio. El usuario se compromete a:</p>
          <ul>
            <li>Usar la aplicación para fines lícitos y conforme a la legislación aplicable.</li>
            <li>No usarla para registrar actividades ilegales ni para engañar a terceros con documentos falsos.</li>
            <li>No intentar descompilar, modificar, redistribuir ni vender la aplicación, salvo lo que permita la ley.</li>
          </ul>
        </section>

        <section id="requisitos">
          {T("requisitos")}
          <p>AdminPlus está dirigida a personas mayores de 18 años que administran un negocio o actúan en su nombre. Requiere un dispositivo Android compatible. Algunas funciones necesitan hardware adicional, como una impresora térmica Bluetooth o una cámara.</p>
        </section>

        <section id="datos">
          {T("datos")}
          <p>La información que el usuario registra se guarda únicamente en su dispositivo. Por eso:</p>
          <ul>
            <li>El usuario es el único responsable de la exactitud de los datos que ingresa y de su conservación.</li>
            <li>Si el dispositivo se pierde, se daña, se restablece o se desinstala la app, la información puede perderse definitivamente. TotoLab no puede recuperarla porque no guarda copias.</li>
            <li>Se recomienda exportar respaldos con frecuencia y guardarlos en un lugar seguro.</li>
          </ul>
        </section>

        <section id="fiscal">
          {T("fiscal")}
          <div class="callout warn" role="note">
            {I("alert", 22)}
            <div>
              <p>Las facturas y recibos que genera AdminPlus son <strong>documentos de control interno</strong>. La aplicación <strong>no reemplaza</strong> los sistemas de facturación, las facturas autorizadas ni los registros contables que la Dirección General de Ingresos (DGI) u otra autoridad tributaria exija a su negocio.</p>
            </div>
          </div>
          <p>El usuario es responsable de cumplir sus obligaciones fiscales y contables, de configurar correctamente impuestos como el IVA y de verificar que los montos, descuentos e impuestos calculados sean correctos antes de entregar un documento a un cliente. Ante cualquier duda, debe consultar a un contador o a la autoridad tributaria correspondiente.</p>
        </section>

        <section id="clientes">
          {T("clientes")}
          <p>Al registrar datos de sus clientes, el usuario actúa como responsable de esa información. Le corresponde contar con su consentimiento cuando la ley lo exija, usar los datos solo para fines legítimos de su negocio y enviar recordatorios de cobro de forma respetuosa y conforme a la ley.</p>
        </section>

        <section id="terceros">
          {T("terceros")}
          <p>AdminPlus puede interactuar con aplicaciones y dispositivos de terceros elegidos por el usuario, como WhatsApp, el menú de compartir de Android, servicios de almacenamiento o impresoras térmicas. TotoLab no controla esos productos y no responde por su funcionamiento, disponibilidad ni por el tratamiento que hagan de la información compartida a través de ellos.</p>
        </section>

        <section id="propiedad">
          {T("propiedad")}
          <p>AdminPlus, su código, diseño, nombre y logotipos son propiedad de TotoLab y están protegidos por las leyes de propiedad intelectual. TotoLab otorga al usuario un derecho personal, no exclusivo e intransferible de usar la aplicación de acuerdo con estos términos. La información que el usuario registra en la app le pertenece al usuario.</p>
        </section>

        <section id="garantia">
          {T("garantia")}
          <p>AdminPlus se ofrece <strong>"tal cual" y "según disponibilidad"</strong>, sin garantías de ningún tipo, expresas o implícitas, incluidas las de funcionamiento ininterrumpido, ausencia de errores o adecuación a un propósito particular. TotoLab trabaja para que la aplicación sea confiable, pero no garantiza que los cálculos, reportes o documentos estén libres de errores en todas las circunstancias.</p>
        </section>

        <section id="responsabilidad">
          {T("responsabilidad")}
          <p>En la medida en que lo permita la ley, TotoLab no será responsable por daños directos, indirectos, incidentales o consecuentes derivados del uso o de la imposibilidad de usar AdminPlus, incluidos la pérdida de datos, de ventas o de ganancias, errores en precios, inventario, impuestos o cobros, sanciones fiscales, ni decisiones comerciales tomadas con base en la información de la aplicación. El usuario es responsable de revisar la información antes de usarla.</p>
        </section>

        <section id="cambios">
          {T("cambios")}
          <p>TotoLab puede actualizar, modificar o retirar funciones de AdminPlus. En el futuro podría ofrecer funciones opcionales, como inicio de sesión o respaldo en la nube; si eso ocurre, la Política de Privacidad se actualizará antes de activarlas.</p>
          <p>Estos términos pueden cambiar. La versión vigente estará siempre publicada en esta dirección con su fecha de actualización. El uso continuado de la aplicación después de un cambio implica la aceptación de los nuevos términos.</p>
        </section>

        <section id="ley">
          {T("ley")}
          <p>Estos términos se rigen por las leyes de la República de Nicaragua. Cualquier controversia se someterá a los tribunales competentes de Managua, Nicaragua, sin perjuicio de los derechos que la ley de protección al consumidor del país de residencia del usuario le reconozca.</p>
        </section>

        <section id="contacto">
          {T("contacto")}
          <p>Para consultas sobre estos términos:</p>
          <div class="contact-card">
            <p><strong>TotoLab</strong></p>
            <p>{I("mail", 18)} <a href="mailto:totolab2025@gmail.com">totolab2025@gmail.com</a></p>
            <p>{I("map-pin", 18)} Managua, Nicaragua</p>
          </div>
        </section>
      </article>
    </div>"""

page("terminos_y_descripcion.html",
     "Descripción y Términos y Condiciones – AdminPlus",
     "Descripción de AdminPlus 2.0, app de gestión para pequeños negocios, y sus Términos y Condiciones de uso.",
     "AdminPlus: descripción y Términos y Condiciones",
     TERMS_BODY, TERMS_CSS)

# ---------------------------------------------------- eliminar-datos.html
DEL_BODY = f"""    <div class="doc-head">
      <div class="wrap">
        <p class="eyebrow">Sus datos</p>
        <h1>Cómo eliminar sus datos de AdminPlus</h1>
        <dl class="meta">
          <div><dt>Última actualización:</dt><dd>4 de octubre de 2026</dd></div>
          <div><dt>Aplicación:</dt><dd>AdminPlus (com.totolab.myapplottery)</dd></div>
          <div><dt>Desarrollador:</dt><dd>TotoLab</dd></div>
        </dl>
      </div>
    </div>
    <div class="wrap doc">
      <article class="prose">
        <div class="callout" role="note">
          {I("phone", 22)}
          <div>
            <p><strong>AdminPlus no tiene cuentas ni servidores.</strong> Toda la información se guarda solo en su dispositivo, por lo que usted mismo puede borrarla en cualquier momento, sin enviar una solicitud a TotoLab. TotoLab no guarda copias de sus datos.</p>
          </div>
        </div>

        <section id="registros">
          <h2><span class="num">1.</span> Borrar registros individuales</h2>
          <p>Para eliminar solo algunos datos, ábralos dentro de AdminPlus y use la opción <em>Eliminar</em>. Aplica a clientes, productos, categorías, ventas, cobros, gastos y demás registros. La eliminación es inmediata y permanente.</p>
        </section>

        <section id="restablecer">
          <h2><span class="num">2.</span> Borrar toda la información desde la app</h2>
          <ol class="steps">
            <li><strong>Abra AdminPlus.</strong> Vaya a <em>Ajustes</em>.</li>
            <li><strong>Toque <em>Restablecer datos</em>.</strong> La app le pedirá confirmar la acción.</li>
            <li><strong>Confirme.</strong> Se borran clientes, inventario, fotos de productos, ventas, cobros, finanzas y configuración del negocio.</li>
          </ol>
        </section>

        <section id="android">
          <h2><span class="num">3.</span> Borrar los datos desde Android</h2>
          <ol class="steps">
            <li><strong>Abra los Ajustes del teléfono.</strong> Entre a <em>Aplicaciones</em> y busque <em>AdminPlus</em>.</li>
            <li><strong>Toque <em>Almacenamiento</em></strong> (el nombre puede variar según el fabricante).</li>
            <li><strong>Toque <em>Borrar datos</em></strong> y confirme. La app quedará como recién instalada.</li>
          </ol>
          <p>También puede <strong>desinstalar AdminPlus</strong>: Android elimina toda la información guardada por la app.</p>
        </section>

        <section id="fuera">
          <h2><span class="num">4.</span> Información que quedó fuera de la app</h2>
          <p>Los siguientes elementos no se borran con los pasos anteriores porque usted los guardó o compartió fuera de AdminPlus:</p>
          <ul>
            <li><strong>Archivos de respaldo exportados:</strong> elimínelos de la carpeta o servicio donde los guardó.</li>
            <li><strong>Facturas, recibos o recordatorios compartidos:</strong> quedan en las aplicaciones o conversaciones a las que los envió (por ejemplo, WhatsApp) y deben borrarse allí.</li>
          </ul>
        </section>

        <section id="importante">
          <h2><span class="num">5.</span> Antes de borrar</h2>
          <div class="callout warn" role="note">
            {I("alert", 22)}
            <div>
              <p>La eliminación no se puede deshacer. Si cree que podría necesitar la información después, exporte un respaldo desde AdminPlus antes de borrarla.</p>
            </div>
          </div>
          <p>Si en el futuro AdminPlus ofrece un inicio de sesión o respaldo en la nube opcionales, esta página incluirá también cómo eliminar la cuenta y los datos guardados en la nube.</p>
        </section>

        <section id="ayuda">
          <h2><span class="num">6.</span> ¿Necesita ayuda?</h2>
          <p>Escríbanos y le explicaremos los pasos para su dispositivo.</p>
          <div class="contact-card">
            <p><strong>TotoLab</strong></p>
            <p>{I("mail", 18)} <a href="mailto:totolab2025@gmail.com?subject=AdminPlus%20-%20Eliminar%20datos">totolab2025@gmail.com</a></p>
            <p>{I("map-pin", 18)} Managua, Nicaragua</p>
          </div>
          <p style="margin-top:16px">Más información en la <a href="privacy-policy.html">Política de Privacidad</a>.</p>
        </section>
      </article>
    </div>"""

page("eliminar-datos.html",
     "Eliminar datos – AdminPlus",
     "Instrucciones para eliminar los datos de AdminPlus. La app no tiene cuentas ni servidores: la información se borra directamente en el dispositivo.",
     "Cómo eliminar sus datos de AdminPlus",
     DEL_BODY)
