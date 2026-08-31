#!/usr/bin/env python3
"""Generate SUBRATA — DIGITAL UNIVERSE SVG assets. Run from repo root: python tools/generate_assets.py"""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


def load_profile():
    path = ROOT / "config" / "profile.yml"
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    return data

# Theme tokens
BG = "#05070d"
BG2 = "#0a1220"
MID = "#0d1b36"
BLUE = "#3b82f6"
ELEC = "#60a5fa"
VIOLET = "#8b5cf6"
CYAN = "#22d3ee"
MUTED = "#8b9cc8"
TEXT = "#e8eefc"
DIM = "#5b6b8c"
LINE = "#1a2a48"

FONT = "Segoe UI, Helvetica Neue, Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace"


def svg(w, h, body, extra_css=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
<defs>
  <linearGradient id="gSky" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#05070d"/>
    <stop offset="45%" stop-color="#0a1428"/>
    <stop offset="100%" stop-color="#0c1834"/>
  </linearGradient>
  <linearGradient id="gSkyLight" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#e8f0ff"/>
    <stop offset="50%" stop-color="#d5e4fb"/>
    <stop offset="100%" stop-color="#c9d8f5"/>
  </linearGradient>
  <linearGradient id="gNeon" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#22d3ee"/>
    <stop offset="50%" stop-color="#3b82f6"/>
    <stop offset="100%" stop-color="#8b5cf6"/>
  </linearGradient>
  <linearGradient id="gCore" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#67e8f9"/>
    <stop offset="50%" stop-color="#3b82f6"/>
    <stop offset="100%" stop-color="#7c3aed"/>
  </linearGradient>
  <radialGradient id="gGlow" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#22d3ee" stop-opacity="0.55"/>
    <stop offset="40%" stop-color="#3b82f6" stop-opacity="0.18"/>
    <stop offset="100%" stop-color="#05070d" stop-opacity="0"/>
  </radialGradient>
  <filter id="soft" x="-40%" y="-40%" width="180%" height="180%">
    <feGaussianBlur stdDeviation="4" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <pattern id="pGrid" width="32" height="32" patternUnits="userSpaceOnUse">
    <path d="M 32 0 L 0 0 0 32" fill="none" stroke="#22d3ee" stroke-width="0.45"/>
  </pattern>
</defs>
<style>
  .t {{ font-family: {FONT}; }}
  .m {{ font-family: {MONO}; }}
  .pulse {{ animation: pulse 4s ease-in-out infinite; }}
  .spin {{ animation: spin 28s linear infinite; transform-origin: center; }}
  .spinr {{ animation: spinr 42s linear infinite; transform-origin: center; }}
  .tw {{ animation: tw 3.2s ease-in-out infinite; }}
  .scan {{ animation: scan 6s linear infinite; }}
  .blink {{ animation: blink 1.4s steps(2) infinite; }}
  @keyframes pulse {{ 0%,100% {{ opacity:.7 }} 50% {{ opacity:1 }} }}
  @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
  @keyframes spinr {{ to {{ transform: rotate(-360deg); }} }}
  @keyframes tw {{ 0%,100% {{ opacity:.25 }} 50% {{ opacity:1 }} }}
  @keyframes scan {{ 0% {{ transform: translateY(-20px); opacity:0 }} 10% {{ opacity:.35 }} 100% {{ transform: translateY(420px); opacity:0 }} }}
  @keyframes blink {{ 50% {{ opacity:0 }} }}
  {extra_css}
</style>
{body}
</svg>
'''


def stars(n=48, w=1200, h=420, seed=7):
    # deterministic pseudo-random
    out = ['<g id="stars">']
    x, y = seed * 17 + 3, seed * 31 + 11
    for i in range(n):
        x = (x * 1103515245 + 12345) & 0x7FFFFFFF
        y = (y * 1664525 + 1013904223) & 0x7FFFFFFF
        px = (x % (w - 20)) + 10
        py = (y % (h - 16)) + 8
        r = 0.4 + (i % 5) * 0.22
        op = 0.25 + (i % 7) * 0.1
        delay = (i % 11) * 0.28
        c = CYAN if i % 5 == 0 else (ELEC if i % 3 == 0 else "#cfe8ff")
        out.append(
            f'<circle class="tw" cx="{px}" cy="{py}" r="{r:.2f}" fill="{c}" opacity="{op:.2f}" style="animation-delay:{delay}s"/>'
        )
    out.append("</g>")
    return "\n".join(out)


def grid(w, h, step=28, op=0.08):
    return f'<rect width="{w}" height="{h}" fill="url(#pGrid)" opacity="{op}"/>'


def write(rel, content):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("wrote", rel, path.stat().st_size)


def hero(light=False):
    profile = load_profile()
    identity = profile.get("identity", {})
    name = str(identity.get("name", "Subrata Bag")).upper()
    headline = str(identity.get("headline", "Creative Developer")).upper()
    github_username = identity.get("github_username", "subrata-code")

    w, h = 1200, 380
    fill = "url(#gSkyLight)" if light else "url(#gSky)"
    title = "#0b1220" if light else TEXT
    sub = "#334155" if light else MUTED
    accent = "#1d4ed8" if light else CYAN
    hud = "#1e3a5f" if light else "#9ec5ff"
    body = f'''
<rect width="{w}" height="{h}" fill="{fill}"/>
{grid(w, h, 32, 0.06 if light else 0.07)}
{stars(56, w, h, 3 if light else 9)}
<ellipse cx="980" cy="190" rx="220" ry="140" fill="url(#gGlow)" opacity="{0.45 if light else 0.9}"/>
<g transform="translate(980 190)">
  <circle r="34" fill="url(#gCore)" filter="url(#soft)">
    <animate attributeName="opacity" values="0.7;1;0.7" dur="4s" repeatCount="indefinite"/>
  </circle>
  <circle r="18" fill="#eaf6ff" opacity=".85"/>
  <g>
    <ellipse rx="92" ry="28" fill="none" stroke="{accent}" stroke-width="1.2" opacity=".7"/>
    <circle cx="92" cy="0" r="3.2" fill="{accent}"/>
    <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="28s" repeatCount="indefinite"/>
  </g>
  <g>
    <ellipse rx="118" ry="42" fill="none" stroke="{VIOLET}" stroke-width="1" opacity=".45"/>
    <circle cx="-70" cy="18" r="2.2" fill="{VIOLET}"/>
    <animateTransform attributeName="transform" type="rotate" from="28" to="-332" dur="42s" repeatCount="indefinite"/>
  </g>
  <ellipse rx="70" ry="70" fill="none" stroke="{ELEC}" stroke-width="0.6" opacity=".35" stroke-dasharray="4 8">
    <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="60s" repeatCount="indefinite"/>
  </ellipse>
</g>
<g opacity=".55" fill="none" stroke="{hud}" stroke-width="1">
  <rect x="36" y="28" width="86" height="18" rx="2"/>
  <path d="M36 28 L28 28 L28 48"/>
  <rect x="1078" y="28" width="86" height="18" rx="2"/>
  <path d="M1164 28 L1172 28 L1172 48"/>
  <rect x="36" y="334" width="86" height="18" rx="2"/>
  <path d="M36 352 L28 352 L28 332"/>
  <rect x="1078" y="334" width="86" height="18" rx="2"/>
  <path d="M1164 352 L1172 352 L1172 332"/>
</g>
<text class="m" x="48" y="42" fill="{accent}" font-size="10" letter-spacing="2.4">SYS // UNIVERSE.01</text>
<text class="m" x="1040" y="42" fill="{accent}" font-size="10" letter-spacing="1.6" text-anchor="end">LAT 22N · NODE SB</text>
<g transform="translate(72 118)">
  <text class="t" x="0" y="0" fill="{accent}" font-size="13" letter-spacing="6">DIGITAL UNIVERSE</text>
  <text class="t" x="0" y="62" fill="{title}" font-size="52" font-weight="700" letter-spacing="2.5">{name}</text>
  <text class="t" x="0" y="100" fill="{sub}" font-size="20" letter-spacing="4.2" font-weight="600">{headline}</text>
  <rect x="0" y="118" width="220" height="2" fill="url(#gNeon)"/>
  <text class="m" x="0" y="152" fill="{hud}" font-size="14" letter-spacing="1.5">Java  ·  React  ·  Three.js  ·  DevOps</text>
</g>
<g transform="translate(72 300)">
  <rect x="0" y="0" width="320" height="46" rx="8" fill="{('#ffffff' if light else '#061018')}" fill-opacity="{0.7 if light else 0.85}" stroke="{accent}" stroke-opacity=".35"/>
  <text class="m" x="16" y="19" fill="{accent}" font-size="11">~/universe</text>
  <text class="m" x="16" y="36" fill="{title}" font-size="12">$ boot --identity {github_username} <tspan fill="{CYAN}">█<animate attributeName="opacity" values="1;0;1" dur="1.2s" repeatCount="indefinite"/></tspan></text>
</g>
<rect class="scan" x="0" y="0" width="{w}" height="2" fill="{accent}" opacity=".25"/>
'''
    return svg(w, h, body)


def profile_card(light=False):
    profile = load_profile()
    identity = profile.get("identity", {})
    name = str(identity.get("name", "Subrata Bag")).upper()
    headline = str(identity.get("headline", "Creative Developer")).upper()
    education = identity.get("education", "B.Tech Computer Science & Engineering")
    graduation = identity.get("graduation", "2027")
    github_username = identity.get("github_username", "subrata-code")

    w, h = 720, 340
    bg = "#f4f7ff" if light else BG
    title = "#0b1220" if light else TEXT
    sub = "#475569" if light else MUTED
    panel = "#ffffff" if light else "#0b1528"
    stroke = "#93c5fd" if light else LINE
    body = f'''
<rect width="{w}" height="{h}" rx="18" fill="{bg}"/>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="17" fill="{panel}" stroke="url(#gNeon)" stroke-width="1.2"/>
{stars(18, w, h, 21)}
<rect x="0" y="0" width="8" height="{h}" rx="4" fill="url(#gNeon)"/>
<text class="m" x="36" y="36" fill="{CYAN}" font-size="10" letter-spacing="3">ID // CREATIVE.DEV</text>
<text class="t" x="36" y="78" fill="{title}" font-size="28" font-weight="700">{name}</text>
<text class="t" x="36" y="106" fill="{sub}" font-size="14">{education}  ·  {graduation}</text>
<text class="t" x="36" y="132" fill="{ELEC}" font-size="13" letter-spacing="2.2">{headline}</text>
<g transform="translate(36 160)">
  {chip(0, 0, "Three.js / R3F Intern")}
  {chip(214, 0, "Java / DSA")}
  {chip(332, 0, "DevOps")}
  {chip(428, 0, "MERN")}
</g>
<g transform="translate(36 220)">
  <rect width="648" height="86" rx="10" fill="{('#e8eefc' if light else '#07101c')}" stroke="{stroke}"/>
  <text class="m" x="18" y="28" fill="{CYAN}" font-size="11">STATUS</text>
  <text class="t" x="18" y="52" fill="{title}" font-size="14">Building immersive 3D web interfaces while training DSA and DevOps.</text>
  <text class="m" x="18" y="74" fill="{DIM}" font-size="11">CLEARANCE  ·  PUBLIC  ·  NODE {github_username}</text>
</g>
<circle cx="640" cy="64" r="28" fill="none" stroke="url(#gNeon)" stroke-width="2"/>
<circle cx="640" cy="64" r="10" fill="{CYAN}" class="pulse"/>
'''
    return svg(w, h, body)


def chip(x, y, label):
    w = 12 + len(label) * 7.1
    return f'''<g transform="translate({x} {y})">
  <rect width="{w:.0f}" height="28" rx="6" fill="#0d1b36" stroke="#2a4a78"/>
  <circle cx="12" cy="14" r="3" fill="{CYAN}"/>
  <text class="m" x="22" y="18" fill="{TEXT}" font-size="11">{label}</text>
</g>'''


def about():
    w, h = 1100, 260
    body = f'''
<rect width="{w}" height="{h}" rx="16" fill="{BG}"/>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="15" fill="{BG2}" stroke="{LINE}"/>
{grid(w, h, 24, 0.05)}
{stars(22, w, h, 5)}
<!-- workstation -->
<g transform="translate(70 48)">
  <rect x="0" y="20" width="210" height="128" rx="8" fill="#07111e" stroke="{CYAN}" stroke-opacity=".4"/>
  <rect x="10" y="32" width="190" height="92" rx="4" fill="#0a1a30"/>
  <rect x="18" y="42" width="70" height="6" rx="1" fill="{CYAN}" opacity=".7"/>
  <rect x="18" y="56" width="120" height="4" rx="1" fill="{VIOLET}" opacity=".5"/>
  <rect x="18" y="68" width="96" height="4" rx="1" fill="{ELEC}" opacity=".4"/>
  <rect x="18" y="80" width="140" height="4" rx="1" fill="{MUTED}" opacity=".35"/>
  <rect x="18" y="92" width="54" height="4" rx="1" fill="{CYAN}" opacity=".5"/>
  <path d="M40 148 L170 148 L190 172 L20 172 Z" fill="#101a2c" stroke="{LINE}"/>
  <circle cx="248" cy="90" r="46" fill="none" stroke="{VIOLET}" stroke-opacity=".35"/>
  <circle cx="248" cy="90" r="22" fill="url(#gCore)" class="pulse" opacity=".8"/>
</g>
<text class="m" x="380" y="58" fill="{CYAN}" font-size="11" letter-spacing="3">MODULE // ABOUT</text>
<text class="t" x="380" y="92" fill="{TEXT}" font-size="24" font-weight="700">Developer workstation</text>
<text class="t" x="380" y="126" fill="{MUTED}" font-size="15">Immersive web · Java DSA · DevOps &amp; cloud · 3D interfaces</text>
<text class="t" x="380" y="156" fill="{DIM}" font-size="13">A quiet console. A deep black canvas. Systems that feel alive.</text>
<g transform="translate(380 184)">
  <rect width="120" height="28" rx="6" fill="#0d1b36" stroke="{CYAN}" stroke-opacity=".4"/>
  <text class="m" x="60" y="18" text-anchor="middle" fill="{CYAN}" font-size="11">R3F / THREE</text>
  <rect x="132" y="0" width="90" height="28" rx="6" fill="#0d1b36" stroke="{VIOLET}" stroke-opacity=".4"/>
  <text class="m" x="177" y="18" text-anchor="middle" fill="{ELEC}" font-size="11">JAVA</text>
  <rect x="234" y="0" width="110" height="28" rx="6" fill="#0d1b36" stroke="{BLUE}" stroke-opacity=".4"/>
  <text class="m" x="289" y="18" text-anchor="middle" fill="{MUTED}" font-size="11">DEVOPS</text>
</g>
'''
    return svg(w, h, body)


def bar(x, y, w, label, value_note, fill_w):
    return f'''<g transform="translate({x} {y})">
  <text class="m" x="0" y="0" fill="{TEXT}" font-size="12">{label}</text>
  <text class="m" x="210" y="0" text-anchor="end" fill="{DIM}" font-size="10">{value_note}</text>
  <rect x="0" y="8" width="210" height="6" rx="3" fill="#121c30"/>
  <rect x="0" y="8" width="{fill_w}" height="6" rx="3" fill="url(#gNeon)"/>
</g>'''


def mission():
    profile = load_profile()
    mission_cfg = profile.get("mission", {})
    widths = [
        ("DSA", mission_cfg.get("dsa", {}).get("label", "PRIMARY"), mission_cfg.get("dsa", {}).get("bar", 168)),
        ("3D WEB", mission_cfg.get("3d_web", {}).get("label", "ACTIVE"), mission_cfg.get("3d_web", {}).get("bar", 150)),
        ("DEVOPS", mission_cfg.get("devops", {}).get("label", "BUILDING"), mission_cfg.get("devops", {}).get("bar", 110)),
        ("FULL STACK", mission_cfg.get("full_stack", {}).get("label", "ACTIVE"), mission_cfg.get("full_stack", {}).get("bar", 140)),
        ("OPEN SOURCE", mission_cfg.get("open_source", {}).get("label", "SIGNAL"), mission_cfg.get("open_source", {}).get("bar", 96)),
    ]

    # progress is visual/editorial, labeled as FOCUS not %, using bars that are clearly relative focus
    w, h = 1100, 300
    rows = "\n".join(
        [
            f'{bar(40, 130 + i * 48, 210, name, label, value)}'
            for i, (name, label, value) in enumerate(widths[:3])
        ]
        + [
            f'{bar(300, 130 + (i - 3) * 48, 210, name, label, value)}'
            for i, (name, label, value) in enumerate(widths[3:], start=3)
        ]
    )
    body = f'''
<rect width="{w}" height="{h}" rx="16" fill="{BG}"/>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="15" fill="#070e1a" stroke="{LINE}"/>
{stars(16, w, h, 12)}
<text class="m" x="40" y="40" fill="{CYAN}" font-size="11" letter-spacing="3">MISSION CONTROL  ·  FOCUS CHANNELS</text>
<text class="t" x="40" y="72" fill="{TEXT}" font-size="22" font-weight="700">Current mission</text>
<text class="t" x="40" y="98" fill="{DIM}" font-size="12">Bars show relative focus, not measured skill. Edit widths in assets/sections/mission.svg</text>
<!-- EDIT: inner bar width max 210. Labels are focus, not skill %. -->
{rows}
<!-- radar -->
<g transform="translate(860 168)">
  <circle r="92" fill="none" stroke="{LINE}"/>
  <circle r="62" fill="none" stroke="{LINE}"/>
  <circle r="32" fill="none" stroke="{CYAN}" stroke-opacity=".35"/>
  <line x1="-92" y1="0" x2="92" y2="0" stroke="{LINE}"/>
  <line x1="0" y1="-92" x2="0" y2="92" stroke="{LINE}"/>
  <path d="M0 0 L40 -70 A92 92 0 0 1 70 20 Z" fill="{CYAN}" opacity=".12"/>
  <circle r="5" fill="{CYAN}" class="pulse"/>
  <text class="m" x="0" y="118" text-anchor="middle" fill="{MUTED}" font-size="10">SCAN / LIVE</text>
</g>
<rect x="760" y="36" width="300" height="44" rx="8" fill="#0b1528" stroke="{LINE}"/>
<text class="m" x="910" y="55" text-anchor="middle" fill="{CYAN}" font-size="10">INTERN  ·  THREE.JS / R3F</text>
<text class="m" x="910" y="70" text-anchor="middle" fill="{DIM}" font-size="10">GRADUATION WINDOW  ·  2027</text>
'''
    return svg(w, h, body)


def tech():
    w, h = 1100, 88
    body = f'''
<rect width="{w}" height="{h}" rx="12" fill="{BG2}" stroke="{LINE}"/>
{stars(10, w, h, 8)}
<text class="m" x="28" y="36" fill="{CYAN}" font-size="11" letter-spacing="3">TECH UNIVERSE</text>
<text class="t" x="28" y="62" fill="{TEXT}" font-size="18" font-weight="700">Systems in orbit</text>
<text class="m" x="1072" y="50" text-anchor="end" fill="{DIM}" font-size="11">ICONS ONLY</text>
'''
    return svg(w, h, body)


def leetcode():
    w, h = 1100, 88
    body = f'''
<rect width="{w}" height="{h}" rx="12" fill="{BG2}" stroke="{LINE}"/>
{stars(10, w, h, 6)}
<text class="m" x="28" y="36" fill="{CYAN}" font-size="11" letter-spacing="3">LEETCODE INSIGHTS</text>
<text class="t" x="28" y="62" fill="{TEXT}" font-size="18" font-weight="700">Problem telemetry  ·  subrata2005</text>
<text class="m" x="1072" y="50" text-anchor="end" fill="{DIM}" font-size="11">LIVE CARD</text>
'''
    return svg(w, h, body)


def project_card(title, kicker, lines, code):
    w, h = 520, 220
    body = f'''
<rect width="{w}" height="{h}" rx="16" fill="{BG}"/>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="15" fill="#0a1424" stroke="url(#gNeon)" stroke-width="1"/>
<text class="m" x="24" y="32" fill="{CYAN}" font-size="10" letter-spacing="2">{kicker}</text>
<text class="t" x="24" y="64" fill="{TEXT}" font-size="22" font-weight="700">{title}</text>
<text class="t" x="24" y="96" fill="{MUTED}" font-size="13">{lines[0]}</text>
<text class="t" x="24" y="118" fill="{MUTED}" font-size="13">{lines[1]}</text>
<rect x="24" y="148" width="472" height="48" rx="8" fill="#071018" stroke="{LINE}"/>
<text class="m" x="40" y="178" fill="{DIM}" font-size="12">{code}</text>
<circle cx="484" cy="36" r="6" fill="{CYAN}" class="pulse"/>
'''
    return svg(w, h, body)


def terminal():
    w, h = 720, 280
    cmds = [
        ("$", "java solve.java", CYAN),
        ("$", "git commit -m \"orbit\"", ELEC),
        ("$", "docker build -t universe .", VIOLET),
        ("$", "npm run dev", MUTED),
    ]
    rows = []
    for i, (p, c, col) in enumerate(cmds):
        rows.append(f'<text class="m" x="28" y="{88 + i * 36}" fill="{DIM}" font-size="14">{p}</text>')
        rows.append(f'<text class="m" x="48" y="{88 + i * 36}" fill="{col}" font-size="14">{c}</text>')
    body = f'''
<rect width="{w}" height="{h}" rx="14" fill="#03050a"/>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="13" fill="#080d16" stroke="{LINE}"/>
<circle cx="22" cy="22" r="5" fill="#ef4444" opacity=".7"/>
<circle cx="40" cy="22" r="5" fill="#eab308" opacity=".7"/>
<circle cx="58" cy="22" r="5" fill="#22c55e" opacity=".7"/>
<text class="m" x="86" y="26" fill="{DIM}" font-size="11">subrata@universe:~</text>
<line x1="0" y1="40" x2="{w}" y2="40" stroke="{LINE}"/>
{''.join(rows)}
<text class="m" x="28" y="248" fill="{CYAN}" font-size="14">$ <tspan>█<animate attributeName="opacity" values="1;0;1" dur="1.2s" repeatCount="indefinite"/></tspan></text>
'''
    return svg(w, h, body)


def command_center():
    w, h = 1100, 88
    body = f'''
<rect width="{w}" height="{h}" rx="12" fill="{BG2}" stroke="{LINE}"/>
{stars(10, w, h, 4)}
<text class="m" x="28" y="36" fill="{CYAN}" font-size="11" letter-spacing="3">GITHUB COMMAND CENTER</text>
<text class="t" x="28" y="62" fill="{TEXT}" font-size="18" font-weight="700">Telemetry  ·  subrata-code</text>
<text class="m" x="1072" y="50" text-anchor="end" fill="{DIM}" font-size="11">LIVE FEEDS</text>
'''
    return svg(w, h, body)


def achievements():
    w, h = 1100, 200
    # only real, non-invented items + locked slots
    slots = [
        ("ACTIVE ROLE", "Three.js / R3F Intern", CYAN),
        ("PUBLIC NODE", "GitHub  ·  subrata-code", ELEC),
        ("LOCKED", "Awaiting signal", DIM),
        ("LOCKED", "Awaiting signal", DIM),
    ]
    cards = []
    for i, (k, v, c) in enumerate(slots):
        x = 28 + i * 268
        cards.append(f'''<g transform="translate({x} 78)">
  <rect width="252" height="96" rx="10" fill="#0c1628" stroke="{LINE}"/>
  <text class="m" x="16" y="28" fill="{c}" font-size="10" letter-spacing="1.6">{k}</text>
  <text class="t" x="16" y="56" fill="{TEXT}" font-size="14">{v}</text>
</g>''')
    body = f'''
<rect width="{w}" height="{h}" rx="16" fill="{BG}"/>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="15" fill="#070e1a" stroke="{LINE}"/>
<text class="m" x="28" y="36" fill="{CYAN}" font-size="11" letter-spacing="3">ACHIEVEMENT CONSOLE</text>
<text class="t" x="28" y="62" fill="{DIM}" font-size="12">No fabricated awards. Locked slots are ready for real milestones.</text>
{''.join(cards)}
'''
    return svg(w, h, body)


def connect():
    w, h = 1100, 150
    items = ["GitHub", "LinkedIn", "Portfolio", "Instagram", "LeetCode", "GeeksforGeeks"]
    chips = []
    for i, name in enumerate(items):
        x = 28 + (i % 6) * 178
        chips.append(f'''<g transform="translate({x} 78)">
  <rect width="166" height="44" rx="8" fill="#0c1628" stroke="{LINE}"/>
  <text class="m" x="83" y="27" text-anchor="middle" fill="{TEXT}" font-size="12">{name}</text>
</g>''')
    body = f'''
<rect width="{w}" height="{h}" rx="16" fill="{BG}"/>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="15" fill="#070e1a" stroke="{LINE}"/>
<text class="m" x="28" y="40" fill="{CYAN}" font-size="11" letter-spacing="3">UPLINK  ·  CONNECTION PANEL</text>
<text class="t" x="28" y="64" fill="{DIM}" font-size="12">Links live in README. Unknown channels stay unlinked until you add URLs.</text>
{''.join(chips)}
'''
    return svg(w, h, body)


def footer(light=False):
    profile = load_profile()
    identity = profile.get("identity", {})
    name = str(identity.get("name", "Subrata Bag")).upper()
    github_username = identity.get("github_username", "subrata-code")

    w, h = 1100, 160
    fill = "url(#gSkyLight)" if light else "url(#gSky)"
    title = "#0b1220" if light else TEXT
    body = f'''
<rect width="{w}" height="{h}" fill="{fill}"/>
{stars(36, w, h, 19)}
<ellipse cx="550" cy="200" rx="280" ry="70" fill="url(#gGlow)" opacity=".5"/>
<text class="t" x="550" y="78" text-anchor="middle" fill="{title}" font-size="20" font-weight="600">Thanks for exploring my digital universe.</text>
<text class="m" x="550" y="108" text-anchor="middle" fill="{CYAN}" font-size="11" letter-spacing="3">{name}  ·  {github_username}</text>
'''
    return svg(w, h, body)


def divider_galaxy():
    w, h = 1100, 36
    body = f'''
<rect width="{w}" height="{h}" fill="none"/>
{stars(20, w, h, 2)}
<line x1="40" y1="18" x2="1060" y2="18" stroke="url(#gNeon)" stroke-width="1" opacity=".7"/>
<circle cx="550" cy="18" r="4" fill="{CYAN}"/>
'''
    return svg(w, h, body)


def divider_neon():
    w, h = 1100, 28
    body = f'''
<rect width="{w}" height="{h}" fill="none"/>
<rect x="80" y="12" width="940" height="2" rx="1" fill="url(#gNeon)" opacity=".85"/>
'''
    return svg(w, h, body)


def divider_orbit():
    w, h = 1100, 48
    body = f'''
<rect width="{w}" height="{h}" fill="none"/>
<ellipse cx="550" cy="24" rx="120" ry="14" fill="none" stroke="{CYAN}" opacity=".5"/>
<ellipse cx="550" cy="24" rx="70" ry="8" fill="none" stroke="{VIOLET}" opacity=".45"/>
<circle cx="550" cy="24" r="4" fill="{ELEC}"/>
<line x1="40" y1="24" x2="410" y2="24" stroke="{LINE}"/>
<line x1="690" y1="24" x2="1060" y2="24" stroke="{LINE}"/>
'''
    return svg(w, h, body)


def divider_wave():
    w, h = 1100, 40
    body = f'''
<rect width="{w}" height="{h}" fill="none"/>
<path d="M40 22 Q 180 6 320 22 T 600 22 T 880 22 T 1060 22" fill="none" stroke="{CYAN}" stroke-width="1.4" opacity=".7"/>
<path d="M40 28 Q 180 14 320 28 T 600 28 T 880 28 T 1060 28" fill="none" stroke="{VIOLET}" stroke-width="1" opacity=".4"/>
'''
    return svg(w, h, body)


def divider_grid():
    w, h = 1100, 32
    body = f'''
<rect width="{w}" height="{h}" fill="none"/>
{grid(w, h, 16, 0.18)}
<rect x="0" y="14" width="{w}" height="2" fill="url(#gNeon)" opacity=".35"/>
'''
    return svg(w, h, body)


def icon(name, glyph_path):
    # simple 32px HUD icons
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
  <rect width="32" height="32" rx="8" fill="#0c1628" stroke="#1a2a48"/>
  {glyph_path}
</svg>
'''


def project_cards_from_config():
    profile = load_profile()
    projects = profile.get("projects", {})
    return {
        "rivo": {
            "title": projects.get("rivo", {}).get("title", "Rivo"),
            "kicker": "FEATURED  ·  LIVE LOCATION",
            "lines": [
                "Group riding with shared live location",
                "and assistance alerts when a rider needs help.",
            ],
            "repo": projects.get("rivo", {}).get("url", "github.com/subrata-code/Rivo"),
        },
        "portfolio": {
            "title": projects.get("portfolio", {}).get("title", "Personal Portfolio"),
            "kicker": "ORBIT  ·  IDENTITY",
            "lines": [
                "Personal site for experiments, 3D work,",
                "and a public record of the digital universe.",
            ],
            "repo": projects.get("portfolio", {}).get("url", "github.com/subrata-code/subrata-s-portfolio"),
        },
        "devops": {
            "title": projects.get("future_devops", {}).get("title", "Future DevOps Project"),
            "kicker": "QUEUED  ·  PIPELINE",
            "lines": [
                "Reserved slot for a CI/CD, containers,",
                "and cloud automation project.",
            ],
            "repo": projects.get("future_devops", {}).get("url", "EDIT_ME_IN_README"),
        },
        "dsa": {
            "title": projects.get("future_dsa", {}).get("title", "Future Java / DSA Project"),
            "kicker": "QUEUED  ·  ALGORITHMS",
            "lines": [
                "Reserved slot for a Java DSA system,",
                "visualizer, or problem-set archive.",
            ],
            "repo": projects.get("future_dsa", {}).get("url", "EDIT_ME_IN_README"),
        },
    }


def main():
    profile = load_profile()
    projects = project_cards_from_config()
    write("assets/hero/hero.svg", hero(False))
    write("assets/hero/hero-light.svg", hero(True))
    write("assets/cards/profile-card.svg", profile_card(False))
    write("assets/cards/profile-card-light.svg", profile_card(True))
    write("assets/sections/about.svg", about())
    write("assets/sections/mission.svg", mission())
    write("assets/sections/tech-stack.svg", tech())
    write("assets/sections/leetcode.svg", leetcode())
    write("assets/sections/command-center.svg", command_center())
    write("assets/sections/achievements.svg", achievements())
    write("assets/cards/coding-terminal.svg", terminal())
    write("assets/cards/connect.svg", connect())
    write(
        "assets/cards/project-rivo.svg",
        project_card(
            projects["rivo"]["title"],
            projects["rivo"]["kicker"],
            projects["rivo"]["lines"],
            f"repo  ·  {projects['rivo']['repo']}",
        ),
    )
    write(
        "assets/cards/project-portfolio.svg",
        project_card(
            projects["portfolio"]["title"],
            projects["portfolio"]["kicker"],
            projects["portfolio"]["lines"],
            f"repo  ·  {projects['portfolio']['repo']}",
        ),
    )
    write(
        "assets/cards/project-devops.svg",
        project_card(
            projects["devops"]["title"],
            projects["devops"]["kicker"],
            projects["devops"]["lines"],
            f"url  ·  {projects['devops']['repo']}",
        ),
    )
    write(
        "assets/cards/project-dsa.svg",
        project_card(
            projects["dsa"]["title"],
            projects["dsa"]["kicker"],
            projects["dsa"]["lines"],
            f"url  ·  {projects['dsa']['repo']}",
        ),
    )
    write("assets/footer/footer.svg", footer(False))
    write("assets/footer/footer-light.svg", footer(True))
    write("assets/dividers/galaxy.svg", divider_galaxy())
    write("assets/dividers/neon.svg", divider_neon())
    write("assets/dividers/orbit.svg", divider_orbit())
    write("assets/dividers/wave.svg", divider_wave())
    write("assets/dividers/grid.svg", divider_grid())
    write(
        "assets/icons/github.svg",
        icon("gh", f'<path d="M16 8a8 8 0 0 0-2.5 15.6c.4.07.5-.17.5-.38v-1.3c-2.2.48-2.7-1.06-2.7-1.06-.36-.9-.9-1.14-.9-1.14-.74-.5.06-.5.06-.5.82.06 1.25.84 1.25.84.73 1.25 1.9.89 2.36.68.07-.53.28-.89.5-1.1-1.76-.2-3.6-.88-3.6-3.92 0-.87.3-1.58.82-2.14-.08-.2-.36-1.02.08-2.12 0 0 .67-.22 2.2.82A7.6 7.6 0 0 1 16 11.2c.68 0 1.36.1 2 .28 1.52-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.5.56.82 1.27.82 2.14 0 3.05-1.86 3.72-3.62 3.92.28.24.54.72.54 1.46v2.16c0 .21.14.46.54.38A8 8 0 0 0 16 8z" fill="{TEXT}"/>'),
    )


if __name__ == "__main__":
    main()
