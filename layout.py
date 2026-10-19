# -*- coding: utf-8 -*-
"""Shared layout: icons, flags, head, header, footer, modal, helpers."""
from html import escape
from data import *

# ------------------------------------------------------------------ icons (inline SVG, stroke = currentColor)
_I = {
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "arrow-left": '<path d="M19 12H5M11 6l-6 6 6 6"/>',
    "arrow-up": '<path d="M12 19V5M6 11l6-6 6 6"/>',
    "chev": '<path d="M6 9l6 6 6-6"/>',
    "close": '<path d="M6 6l12 12M18 6L6 18"/>',
    "chat": '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/><path d="M8.5 11h.01M12 11h.01M15.5 11h.01"/>',
    "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>',
    "platform": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
    "cert": '<circle cx="12" cy="9" r="5"/><path d="M8.5 13 7 21l5-3 5 3-1.5-8"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14.5a5 5 0 0 1 5.5 5"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/>',
    "code": '<path d="m8 8-5 4 5 4M16 8l5 4-5 4M14 4l-4 16"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z"/>',
    "book": '<path d="M4 4.5A2.5 2.5 0 0 1 6.5 2H20v17H6.5A2.5 2.5 0 0 0 4 21.5z"/><path d="M4 21.5A2.5 2.5 0 0 1 6.5 19H20v3H6.5"/>',
    "mic": '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v4"/>',
    "trophy": '<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0z"/><path d="M17 5h3v2a3 3 0 0 1-3 3M7 5H4v2a3 3 0 0 0 3 3"/>',
    "spark": '<path d="M12 2v6M12 16v6M2 12h6M16 12h6M5 5l3.5 3.5M15.5 15.5 19 19M5 19l3.5-3.5M15.5 8.5 19 5"/>',
    "rocket": '<path d="M5 15c-1.5 1.3-2 4-2 6 2 0 4.7-.5 6-2M9 12a22 22 0 0 1 11-9 22 22 0 0 1-9 11z"/><path d="M9 12H5l2-4h5M12 15v4l4-2v-5"/><circle cx="15" cy="9" r="1.5"/>',
    "heart": '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1L12 21l7.8-7.6 1-1a5.5 5.5 0 0 0 0-7.8z"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "plane": '<path d="M17.8 19.2 16 11l3.5-3.5c1.5-1.5 2-3.5 1.5-4.5-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"/>',
    "ship": '<path d="M2 20c2 1 4 1 6 0s4-1 6 0 4 1 6 0M4 16l-1-5h18l-1 5M12 4v7M7 11V7h10v4"/>',
    "med": '<path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6z"/>',
    "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "play": '<circle cx="12" cy="12" r="9"/><path d="m10 8 6 4-6 4z"/>',
    "home": '<path d="M3 11 12 3l9 8v10H3z"/><path d="M9 21v-7h6v7"/>',
    "star": '<path d="m12 2 3 6.5 7 .8-5.2 4.8 1.4 7L12 17.6 5.8 21l1.4-7L2 9.3l7-.8z"/>',
    "grad": '<path d="M2 9 12 4l10 5-10 5z"/><path d="M6 11v5c3 2.5 9 2.5 12 0v-5M22 9v6"/>',
    "app": '<rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/>',
    "smile": '<circle cx="12" cy="12" r="9"/><path d="M8 14a5 5 0 0 0 8 0M9 9h.01M15 9h.01"/>',
    "layers": '<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 17 10 5 10-5M2 12l10 5 10-5"/>',
    "wa": '<path d="M20.5 3.5A11.8 11.8 0 0 0 1.9 17.7L.3 23.7l6.2-1.6A11.8 11.8 0 0 0 20.5 3.5zM12 21.6c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.6zm5.4-7.3c-.3-.1-1.8-.9-2-1s-.5-.1-.7.1-.8 1-.9 1.2-.3.2-.6.1a8 8 0 0 1-4-3.5c-.3-.5.3-.5.8-1.6.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.8.4 3.5 3.5 0 0 0-1.1 2.6 6 6 0 0 0 1.3 3.2 13.8 13.8 0 0 0 5.3 4.7c2 .8 2.7.9 3.7.8.6-.1 1.8-.8 2-1.5s.3-1.3.2-1.5-.3-.2-.6-.3z" fill="currentColor" stroke="none"/>',
    "tg": '<path d="M21.5 4.3 2.9 11.5c-1.3.5-1.2 1.2-.2 1.5l4.8 1.5 1.8 5.6c.2.6.4.8.9.8.4 0 .6-.2.9-.5l2.3-2.2 4.8 3.5c.9.5 1.5.2 1.7-.8l3.1-14.7c.3-1.3-.5-1.9-1.5-1.4zM9.6 14.4l-.4 3.9-1.4-4.6 10.4-6.6z" fill="currentColor" stroke="none"/>',
    "ig": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/>',
    "fb": '<path d="M14 8h3V4h-3a4 4 0 0 0-4 4v2H8v4h2v8h4v-8h3l1-4h-4V8a0 0 0 0 1 0 0z"/>',
    "pin": '<path d="M12 22s7-6.3 7-12a7 7 0 0 0-14 0c0 5.7 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
    "copy": '<rect x="8" y="8" width="13" height="13" rx="2"/><path d="M16 8V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h3"/>',
}

def icon(name, cls=""):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_I[name]}</svg>'

STAR = '<svg class="marquee__star" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 0c.6 6.4 5.6 11.4 12 12-6.4.6-11.4 5.6-12 12-.6-6.4-5.6-11.4-12-12C6.4 11.4 11.4 6.4 12 0z"/></svg>'

# ------------------------------------------------------------------ flags
FLAGS = {
    "gb": '<rect width="60" height="60" fill="#012169"/><path d="M0 0l60 60M60 0L0 60" stroke="#fff" stroke-width="12"/><path d="M0 0l60 60M60 0L0 60" stroke="#C8102E" stroke-width="5"/><path d="M30 0v60M0 30h60" stroke="#fff" stroke-width="18"/><path d="M30 0v60M0 30h60" stroke="#C8102E" stroke-width="10"/>',
    "de": '<rect width="60" height="20" fill="#000"/><rect y="20" width="60" height="20" fill="#DD0000"/><rect y="40" width="60" height="20" fill="#FFCE00"/>',
    "es": '<rect width="60" height="60" fill="#AA151B"/><rect y="15" width="60" height="30" fill="#F1BF00"/>',
    "it": '<rect width="20" height="60" fill="#009246"/><rect x="20" width="20" height="60" fill="#fff"/><rect x="40" width="20" height="60" fill="#CE2B37"/>',
    "fr": '<rect width="20" height="60" fill="#0055A4"/><rect x="20" width="20" height="60" fill="#fff"/><rect x="40" width="20" height="60" fill="#EF4135"/>',
    "pt": '<rect width="24" height="60" fill="#006600"/><rect x="24" width="36" height="60" fill="#FF0000"/><circle cx="24" cy="30" r="10" fill="#FFCC00"/><circle cx="24" cy="30" r="6" fill="#fff" stroke="#FF0000" stroke-width="2"/>',
    "pl": '<rect width="60" height="30" fill="#fff"/><rect y="30" width="60" height="30" fill="#DC143C"/>',
    "math": '<rect width="60" height="60" fill="#d7ff3d"/><text x="30" y="42" font-family="Georgia, serif" font-size="34" font-weight="700" text-anchor="middle" fill="#0d0b1f">π</text>',
}

def flag_svg(code):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 60" preserveAspectRatio="xMidYMid slice">{FLAGS[code]}</svg>'

LOGO_MARK = '''<svg class="logo__mark" viewBox="0 0 42 42" aria-hidden="true"><g class="spin"><circle cx="21" cy="21" r="19.5" fill="none" stroke="#d7ff3d" stroke-width="1.5" stroke-dasharray="2 4.2"/></g><circle cx="21" cy="21" r="14" fill="#d7ff3d"/><path d="M16 13.5h6.2c3 0 4.7 1.4 4.7 3.6 0 1.5-.8 2.6-2.2 3.1 1.8.4 2.9 1.7 2.9 3.5 0 2.6-2 4.3-5.2 4.3H16zm3.4 5.8h2.4c1.3 0 2-.6 2-1.6s-.7-1.6-2-1.6h-2.4zm0 6.1h2.8c1.4 0 2.2-.6 2.2-1.7s-.8-1.8-2.2-1.8h-2.8z" fill="#0d0b1f"/></svg>'''

def logo(root):
    return f'<a class="logo" href="{root}index.html" aria-label="BeBest School — на главную">{LOGO_MARK}<span>Be<b>Best</b></span></a>'

# ------------------------------------------------------------------ helpers
def btn(text, href=None, cls="", attrs="", icon_name="arrow"):
    inner = f'<span class="btn__text"><span>{text}</span><span>{text}</span></span><span class="btn__icon">{icon(icon_name)}</span>'
    if href:
        return f'<a class="btn {cls}" href="{href}" {attrs}>{inner}</a>'
    return f'<button class="btn {cls}" type="button" {attrs}>{inner}</button>'

def trial_btn(text="Пробный урок бесплатно", cls="", course=""):
    c = f' data-course="{escape(course)}"' if course else ""
    return btn(text, None, cls, f'data-modal-open{c}')

def lang_of(c):
    return MATH if c["lang"] == "math" else LANG[c["lang"]]

def course_href(root, c):
    return f'{root}courses/{c["slug"]}.html'

def test_href(root, lang_key):
    return f'{root}test.html?lang={TEST_LANG[lang_key]}'

def flag(root, code, cls="", alt=""):
    return f'<img class="{cls}" src="{root}assets/img/flags/{code}.svg" alt="{alt}" width="40" height="40" loading="lazy">'

def course_card(root, c, reveal=True):
    L = lang_of(c)
    tagmap = {"kids": "Детям", "exams": "Экзамен", "business": "Карьера", "corporate": "Компаниям", "clubs": "Клуб", "beginner": "С нуля", "adults": "Взрослым"}
    first = c["tags"].split()[-1] if "beginner" in c["tags"] else c["tags"].split()[0]
    for pref in ["exams", "corporate", "clubs", "kids", "beginner", "business", "adults"]:
        if pref in c["tags"].split():
            first = pref; break
    return f'''<a class="course-card" href="{course_href(root, c)}" style="--c:{L['color']}" data-tags="{c['lang']} {c['tags']}" data-cursor="Открыть">
  <div class="course-card__top"><span class="course-card__tag">{tagmap.get(first, "Курс")}</span>{flag(root, L['flag'], 'course-card__flag', L['name'])}</div>
  <h3 class="course-card__title">{c['title']}</h3>
  <p class="course-card__text">{c['short']}</p>
  <div class="course-card__go"><span>{L['name']}</span><span class="course-card__arrow">{icon('arrow')}</span></div>
</a>'''

def marquee_tape(items, cls="", speed="0.7", direction="left"):
    its = "".join(f'<span class="marquee__item">{i}</span>' for i in items)
    return f'<div class="marquee marquee--tape {cls}" data-mspeed="{speed}" data-dir="{direction}" aria-hidden="true"><div class="marquee__track"><div class="marquee__group">{its}</div></div></div>'

def marquee_big(items, speed="0.5", direction="left"):
    its = "".join(f'<span class="marquee__item">{i}{STAR}</span>' for i in items)
    return f'<div class="marquee marquee--big" data-mspeed="{speed}" data-dir="{direction}" aria-hidden="true"><div class="marquee__track"><div class="marquee__group">{its}</div></div></div>'

def faq_block(items, single=True, by_founder=False):
    out = []
    for i, (q, a) in enumerate(items):
        by = '<p class="acc__by">Отвечает: основательница школы Валентина Залевская</p>' if (by_founder and i == 0) else ""
        out.append(f'''<div class="acc"><button class="acc__head" type="button" aria-expanded="false">{q}<span class="acc__icon"></span></button>
<div class="acc__body"><div><p>{a}</p>{by}</div></div></div>''')
    return f'<div class="accordion" {"data-single" if single else ""} data-stagger>{"".join(out)}</div>'

def crumbs(root, items):
    parts = [f'<a href="{root}index.html">Главная</a>']
    for label, href in items:
        parts.append(f'<span><a href="{href}">{label}</a></span>' if href else f'<span>{label}</span>')
    return f'<nav class="crumbs" aria-label="Хлебные крошки" data-reveal="up">{"".join(parts)}</nav>'

def page_hero(root, title, lead="", crumbs_items=None, extra="", eyebrow="", blobs=True):
    b = ('<div class="page-hero__bg"><canvas class="hero__canvas" data-field="lite"></canvas>'
         '<div class="blob blob--violet" style="width:520px;height:520px;right:-120px;top:-160px"></div>'
         '<div class="blob blob--lime" style="width:360px;height:360px;left:-120px;bottom:-120px;animation-delay:-6s"></div></div>') if blobs else ""
    cr = crumbs(root, crumbs_items) if crumbs_items is not None else ""
    eb = f'<span class="eyebrow" data-reveal="up">{eyebrow}</span>' if eyebrow else ""
    ld = f'<p class="lead" data-reveal="up" style="--d:.25s">{lead}</p>' if lead else ""
    return f'''<section class="page-hero">{b}
  <div class="container page-hero__inner">{cr}{eb}
    <h1 class="h-xl page-hero__title" data-split>{title}</h1>{ld}{extra}
  </div>
</section>'''

def cta_block(root, title="Попробуйте обучение на пробном уроке", text="Запишитесь на бесплатный пробный урок и опробуйте нашу методику на практике — онлайн и в удобное для вас время.", course=""):
    return f'''<section class="section section--tight"><div class="container">
  <div class="cta" data-reveal="scale">
    <span class="cta__shape cta__shape--1"></span><span class="cta__shape cta__shape--2"></span>
    <div class="flex" style="flex-direction:column;gap:22px">
      <span class="eyebrow" style="color:#fff">Первый урок — 0 ₸</span>
      <h2 class="h-l" data-split>{title}</h2>
      <p style="font-size:18px;opacity:.85;max-width:520px">{text}</p>
    </div>
    <div class="flex wrap gap" style="justify-content:flex-start">
      {trial_btn("Записаться бесплатно", "", course)}
      {btn("Написать в WhatsApp", WA, "btn--ink", 'target="_blank" rel="noopener"', "wa")}
    </div>
  </div>
</div></section>'''

# ------------------------------------------------------------------ head
def head(root, title, desc, page_cls=""):
    return f'''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{escape(desc)}">
<meta name="theme-color" content="#0d0b1f">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:image" content="{root}assets/img/og.svg">
<link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Unbounded:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/base.css">
<link rel="stylesheet" href="{root}assets/css/animations.css">
<link rel="stylesheet" href="{root}assets/css/components.css">
<link rel="stylesheet" href="{root}assets/css/pages.css">
</head>
<body class="{page_cls}">
<a class="visually-hidden" href="#main">Перейти к содержимому</a>
<div class="preloader" aria-hidden="true">
  <div class="preloader__inner">
    <div class="preloader__word"><span style="animation-delay:.05s">B</span><span style="animation-delay:.1s">e</span><span style="animation-delay:.15s">B</span><span style="animation-delay:.2s">e</span><span style="animation-delay:.25s">s</span><span style="animation-delay:.3s">t</span></div>
    <div class="preloader__hello"><ul><li>Hello</li><li>Hallo</li><li>Hola</li><li>Ciao</li><li>Bonjour</li><li>Привет 👋</li></ul></div>
    <div class="preloader__bar"><i></i></div>
  </div>
  <div class="preloader__count">000</div>
</div>
<div class="curtain" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div>
<div class="progress" aria-hidden="true"></div>
<div class="grain" aria-hidden="true"></div>
'''

# ------------------------------------------------------------------ header
def mega_menu(root):
    tabs, panels = [], []
    groups = LANGS + [MATH]
    for i, L in enumerate(groups):
        act = " is-active" if i == 0 else ""
        tabs.append(f'<button class="mega__lang{act}" type="button" data-tab="{L["key"]}"><img src="{root}assets/img/flags/{L["flag"]}.svg" alt="">{L["name"]}</button>')
        links = []
        for c in COURSES:
            if c["lang"] == L["key"]:
                links.append(f'<a href="{course_href(root, c)}">{c["title"]}</a>')
        if L["key"] in TEST_LANG:
            links.append(f'<a href="{test_href(root, L["key"])}">Тест на знание {L["gen"]}</a>')
        hub = f'{root}languages/{L["key"]}.html' if L["key"] != "math" else f'{root}courses/kursy-matematiki.html'
        links.append(f'<a class="mega__all" href="{hub}">Всё о курсе: {L["name"].lower()} →</a>')
        panels.append(f'<div class="mega__panel{act}" data-panel="{L["key"]}">{"".join(links)}</div>')
    return f'<div class="mega"><div class="mega__inner"><div class="mega__langs">{"".join(tabs)}</div><div class="mega__panels">{"".join(panels)}</div></div></div>'

SCHOOL_LINKS = [
    ("about.html", "О школе BeBest", "История, цифры и подход"),
    ("teachers.html", "Преподаватели", "Профессионалы с многолетним опытом"),
    ("courses.html", "Каталог курсов", "Все 50+ программ в одном месте"),
    ("exercises.html", "Упражнения", "Тренажёр фраз на 5 языках"),
    ("blog.html", "Блог", "Материалы для самостоятельного изучения"),
    ("vacancies.html", "Вакансии", "Присоединяйтесь к команде BeBest"),
    ("contact.html", "Контакты", "Как с нами связаться"),
]

def header(root, active=""):
    def act(k): return " is-active" if active == k else ""
    school = "".join(f'<a href="{root}{h}"><b>{t}</b><span>{s}</span></a>' for h, t, s in SCHOOL_LINKS)
    # mobile sub-lists
    msub = []
    for L in LANGS + [MATH]:
        msub.append(f'<h5>{L["name"]}</h5>')
        for c in COURSES:
            if c["lang"] == L["key"]:
                msub.append(f'<a href="{course_href(root, c)}">{c["title"]}</a>')
    mschool = "".join(f'<a href="{root}{h}">{t}</a>' for h, t, s in SCHOOL_LINKS)
    return f'''<header class="header">
  <div class="container header__inner">
    {logo(root)}
    <nav class="nav" aria-label="Основная навигация">
      <div class="nav__item"><a class="nav__link{act('langs')}" href="{root}courses.html">Языки онлайн {icon('chev')}</a>{mega_menu(root)}</div>
      <div class="nav__item"><a class="nav__link{act('school')}" href="{root}about.html">Про школу {icon('chev')}</a><div class="dropdown">{school}</div></div>
      <div class="nav__item"><a class="nav__link{act('price')}" href="{root}price.html" data-scramble>Цены</a></div>
      <div class="nav__item"><a class="nav__link{act('test')}" href="{root}test.html" data-scramble>Тест уровня</a></div>
      <div class="nav__item"><a class="nav__link{act('faq')}" href="{root}faq.html" data-scramble>FAQ</a></div>
    </nav>
    <div class="header__cta">
      <a class="header__phone" href="tel:{PHONE}">{PHONE_H}<small>только звонки</small></a>
      {trial_btn("Пробный урок", "btn--sm")}
      <button class="burger" type="button" aria-label="Меню" aria-expanded="false"><i></i><i></i></button>
    </div>
  </div>
</header>
<div class="mobile-menu" aria-label="Мобильное меню">
  <ul class="mobile-menu__list">
    <li><button type="button" data-sub-toggle>Языки онлайн <span>+</span></button><div class="mobile-menu__sub">{"".join(msub)}</div></li>
    <li><button type="button" data-sub-toggle>Про школу <span>+</span></button><div class="mobile-menu__sub">{mschool}</div></li>
    <li><a href="{root}price.html">Цены</a></li>
    <li><a href="{root}test.html">Тест уровня</a></li>
    <li><a href="{root}faq.html">FAQ</a></li>
    <li><a href="{root}contact.html">Контакты</a></li>
  </ul>
  <div class="mobile-menu__foot">
    {trial_btn("Пробный урок бесплатно", "btn--block")}
    <a href="tel:{PHONE}" style="font-family:var(--font-display);font-size:22px;font-weight:700">{PHONE_H}</a>
    <a href="mailto:{EMAIL}">{EMAIL}</a>
    {socials()}
  </div>
</div>
<main id="main">
'''

def socials():
    return f'''<div class="socials">
  <a class="social" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{icon('wa')}</a>
  <a class="social" href="{TG}" target="_blank" rel="noopener" aria-label="Telegram">{icon('tg')}</a>
  <a class="social" href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{icon('ig')}</a>
  <a class="social" href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{icon('fb')}</a>
</div>'''

# ------------------------------------------------------------------ modal
def modal(root):
    langs = LANGS + [MATH]
    tiles = "".join(f'<label class="radio-tile"><input type="radio" name="lang" value="{L["name"]}"{" checked" if i == 0 else ""}><span><img src="{root}assets/img/flags/{L["flag"]}.svg" alt="">{L["name"]}</span></label>' for i, L in enumerate(langs))
    who = "".join(f'<label class="radio-tile"><input type="radio" name="who" value="{w}"{" checked" if i == 0 else ""}><span>{w}</span></label>' for i, w in enumerate(["Для себя", "Для ребёнка", "Для компании"]))
    fmt = "".join(f'<label class="radio-tile"><input type="radio" name="format" value="{w}"{" checked" if i == 0 else ""}><span>{w}</span></label>' for i, w in enumerate(["Индивидуально", "Мини-группа 2–4", "Группа до 8"]))
    lvl = "".join(f'<label class="radio-tile"><input type="radio" name="level" value="{w}"{" checked" if i == 0 else ""}><span>{w}</span></label>' for i, w in enumerate(["С нуля", "Базовый", "Средний", "Продвинутый", "Не знаю"]))
    return f'''<div class="modal" id="lead-modal" aria-hidden="true" role="dialog" aria-modal="true" aria-labelledby="modal-title">
  <div class="modal__backdrop" data-modal-close></div>
  <div class="modal__dialog">
    <button class="modal__close" type="button" data-modal-close aria-label="Закрыть">{icon('close')}</button>
    <aside class="modal__aside">
      <span class="orb"></span>
      <span class="eyebrow" style="color:#fff;position:relative">Бесплатно · 0 ₸</span>
      <h3 id="modal-title">Пробный урок, после которого захочется продолжить</h3>
      <ul><li>Определим ваш уровень</li><li>Познакомитесь с преподавателем</li><li>Составим план под вашу цель</li><li>До 80 разговорных клубов в подарок*</li></ul>
      <small style="position:relative;opacity:.75">* при оплате в течение 60 минут после демо-урока</small>
    </aside>
    <div class="modal__main">
      <form class="form js-lead-form" novalidate>
        <div class="steps-dots"><i class="is-done"></i><i></i><i></i></div>
        <div class="form-step is-active">
          <h4 class="h-s">1. Какой язык хотите учить?</h4>
          <div class="radio-tiles" data-auto>{tiles}</div>
          <button class="link-arrow" type="button" data-next-step>Дальше {icon('arrow')}</button>
        </div>
        <div class="form-step">
          <h4 class="h-s">2. Для кого и в каком формате?</h4>
          <div class="radio-tiles">{who}</div>
          <div class="radio-tiles">{fmt}</div>
          <h4 class="h-s" style="margin-top:6px">Ваш уровень</h4>
          <div class="radio-tiles">{lvl}</div>
          <div class="flex between center"><button class="link-arrow" type="button" data-prev-step>{icon('arrow-left')} Назад</button><button class="link-arrow" type="button" data-next-step>Дальше {icon('arrow')}</button></div>
        </div>
        <div class="form-step">
          <h4 class="h-s">3. Куда прислать приглашение?</h4>
          <div class="field"><input id="m-name" name="name" type="text" placeholder=" " autocomplete="name" required><label for="m-name">Ваше имя</label></div>
          <div class="field"><input id="m-phone" name="phone" type="tel" placeholder=" " autocomplete="tel" required><label for="m-phone">Телефон / WhatsApp</label></div>
          <div class="field"><input id="m-comment" name="comment" type="text" placeholder=" "><label for="m-comment">Цель или удобное время (необязательно)</label></div>
          <input type="hidden" name="course" value="">
          <button class="btn btn--block" type="submit"><span class="btn__text"><span>Записаться бесплатно</span><span>Записаться бесплатно</span></span><span class="btn__icon">{icon('arrow')}</span></button>
          <p class="form__note">Нажимая кнопку, вы принимаете <a href="{root}terms.html">условия обслуживания</a> и <a href="{root}privacy.html">политику конфиденциальности</a>.</p>
          <button class="link-arrow" type="button" data-prev-step>{icon('arrow-left')} Назад</button>
        </div>
        <div class="form-success">
          <svg class="form-success__check" viewBox="0 0 100 100"><circle cx="50" cy="50" r="46" fill="none" stroke="#d7ff3d" stroke-width="5"/><path d="M30 52l13 13 27-29" fill="none" stroke="#d7ff3d" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <h4 class="h-m">Заявка готова! 🎉</h4>
          <p class="muted">Открываем WhatsApp с вашей заявкой — просто нажмите «Отправить», и менеджер подберёт время пробного урока.</p>
          <a class="btn btn--violet" data-wa href="{WA}" target="_blank" rel="noopener"><span class="btn__text"><span>Открыть WhatsApp</span><span>Открыть WhatsApp</span></span><span class="btn__icon">{icon('wa')}</span></a>
        </div>
      </form>
    </div>
  </div>
</div>'''

# ------------------------------------------------------------------ footer
def footer(root, scripts=()):
    lang_links = "".join(f'<a href="{root}languages/{L["key"]}.html">{L["name"]}</a>' for L in LANGS) + f'<a href="{root}courses/kursy-matematiki.html">Математика</a>'
    school = "".join(f'<a href="{root}{h}">{t}</a>' for h, t, s in SCHOOL_LINKS[:6]) + f'<a href="{root}price.html">Цены</a><a href="{root}faq.html">FAQ</a>'
    extra = "".join(f'<script src="{root}assets/js/{s}"></script>' for s in scripts)
    return f'''</main>
<footer class="footer">
  <div class="container">
    <div class="footer__top">
      <div class="flex" style="flex-direction:column;gap:22px" data-reveal="up">
        {logo(root)}
        <p class="muted" style="max-width:340px">Онлайн-школа английского, немецкого, испанского, итальянского, французского, португальского и польского языков для взрослых, детей и компаний.</p>
        {socials()}
      </div>
      <div data-reveal="up" style="--d:.1s"><h4 class="footer__title">Языки</h4><div class="footer__links">{lang_links}</div></div>
      <div data-reveal="up" style="--d:.2s"><h4 class="footer__title">Школа</h4><div class="footer__links">{school}</div></div>
      <div data-reveal="up" style="--d:.3s"><h4 class="footer__title">Отдел продаж</h4>
        <div class="footer__links">
          <a href="tel:{PHONE}">{PHONE_H}</a><span class="muted" style="font-size:13px;margin-top:-8px">только звонки</span>
          <a href="mailto:{EMAIL}">{EMAIL}</a>
          <a href="{WA}" target="_blank" rel="noopener">WhatsApp</a>
          <a href="{TG}" target="_blank" rel="noopener">Telegram-бот</a>
          <span class="muted" style="font-size:13px">Ежедневно 10:00–19:00<br>Уроки — круглосуточно</span>
        </div>
      </div>
    </div>
    <div class="footer__big" aria-hidden="true">BE BEST</div>
    <div class="footer__bottom">
      <span>© <span data-year>2026</span> BeBest School. Стань лучшей версией себя.</span>
      <div class="flex wrap gap"><a href="{root}terms.html">Публичная оферта</a><a href="{root}privacy.html">Privacy Policy</a><a href="{root}cookies.html">Cookies Policy</a><a href="{root}legal.html">Legal notice</a></div>
    </div>
  </div>
</footer>
<a class="fab" href="{WA}" target="_blank" rel="noopener" aria-label="Написать в WhatsApp" data-cursor="Чат">{icon('wa')}</a>
<button class="to-top" type="button" aria-label="Наверх">{icon('arrow-up')}</button>
{modal(root)}
<script src="{root}assets/js/core.js"></script>
<script src="{root}assets/js/motion.js"></script>
<script src="{root}assets/js/hero.js"></script>
<script src="{root}assets/js/ui.js"></script>
<script src="{root}assets/js/cursor.js"></script>
{extra}
</body>
</html>
'''
