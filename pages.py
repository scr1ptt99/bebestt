# -*- coding: utf-8 -*-
"""Page builders. Run build.py to generate the whole site."""
import math, os
from html import escape
from data import *
from layout import *
from content import course_content

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def write(rel, html):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

def page(rel, title, desc, body, active="", scripts=(), cls=""):
    depth = rel.count("/")
    root = "../" * depth
    html = head(root, title, desc, cls) + header(root, active) + body(root) + footer(root, scripts)
    write(rel, html)

AV_COLORS = ["#d7ff3d", "#8f78ff", "#4fd1ff", "#ff6b4a", "#ff5fa2", "#ffd23d", "#3ddc84"]
BLOB = '<svg class="blob" viewBox="0 0 200 200" aria-hidden="true"><path fill="#0d0b1f" d="M44.7,-58.4C57.2,-48.3,66.1,-33.9,70.6,-17.8C75.1,-1.7,75.2,16.1,67.6,29.9C60,43.7,44.6,53.5,28.4,60.8C12.2,68.1,-4.8,72.9,-21.6,69.6C-38.4,66.3,-55,54.9,-64.6,39.3C-74.2,23.7,-76.8,3.9,-72.2,-13.6C-67.6,-31.1,-55.8,-46.3,-41.4,-56.1C-27,-65.9,-10,-70.3,4.7,-75.9C19.4,-81.5,32.2,-68.5,44.7,-58.4Z" transform="translate(100 100)"/></svg>'

def teacher_card(t, i):
    name, langs, bio, vip, native = t
    lang_names = ", ".join(LANG[l]["low"] for l in langs)
    v = '<span class="teacher__vip">PREMIUM</span>' if vip else ""
    n = '<span class="teacher__native">Носитель языка</span>' if native else ""
    return f'''<article class="teacher" data-tags="{' '.join(langs)}" data-tilt="5">
  <div class="teacher__avatar" style="--av:{AV_COLORS[i % len(AV_COLORS)]}">{BLOB}{v}{n}<span class="teacher__initial">{name[0]}</span></div>
  <div class="teacher__body"><span class="teacher__lang">{lang_names}</span><h3 class="teacher__name">{name}</h3><p class="teacher__bio">{bio}</p><button class="teacher__more" type="button">Читать полностью</button></div>
</article>'''

def review_slides():
    out = []
    for i, (name, role, text, date) in enumerate(REVIEWS):
        out.append(f'''<div class="slider__slide"><article class="review">
  <div class="review__stars">★★★★★</div>
  <p class="review__text">{text}</p>
  <div class="review__who"><span class="review__ava" style="background:{AV_COLORS[i % len(AV_COLORS)]}">{name[0]}</span><div><div class="review__name">{name}</div><div class="review__meta">{role} · {date}</div></div></div>
</article></div>''')
    return "".join(out)

def reviews_section(root, title="Отзывы о нас"):
    return f'''<section class="section section--paper" id="reviews"><div class="container">
  <div class="section-head section-head--split">
    <div><span class="eyebrow" data-reveal="up">Отзывы</span><h2 class="h-l" data-split style="margin-top:18px">{title}</h2></div>
    <div class="flex between center wrap gap"><p class="lead" data-reveal="up">Тысячи студентов уже заговорили — вот что они рассказывают.</p>
      <div class="slider__nav" data-reveal="up"><button class="slider__btn" type="button" data-prev aria-label="Назад">{icon('arrow-left')}</button><button class="slider__btn" type="button" data-next aria-label="Вперёд">{icon('arrow')}</button></div></div>
  </div>
</div>
<div class="slider" data-reveal="up" style="padding-left:max(var(--gutter), calc((100vw - var(--maxw)) / 2 + var(--gutter)))">
  <div class="slider__viewport" data-cursor="Тяни"><div class="slider__track">{review_slides()}</div></div>
  <div class="container" style="padding-left:0"><div class="slider__progress"><i></i></div></div>
</div>
</section>'''

PRICES = [
    dict(name="BASE", price="6 472", desc="Экономичный пакет для тех, кто ценит дисциплину и готов заниматься по фиксированному расписанию.",
         items=[("<b>Сертифицированный преподаватель</b> с опытом до 2-х лет", True), ("<b>Персонализированный сертификат</b> о достижении уровня", True),
                ("<b>Progress check</b> — 5 видеопроверок в год с сохранением записей", True), ("Бесплатная консультация по составлению резюме", False),
                ("Персональный видеоотчёт от методиста", False)],
         gift="🎁 До 80 живых разговорных клубов в подарок при оплате в течение 60 минут после демо-урока"),
    dict(name="OPTIMAL", price="7 397", featured=True, desc="Оптимальный выбор для студентов, которым важен гибкий график и дополнительные возможности.",
         items=[("Опытный преподаватель <b>с международными сертификатами (TESOL, TKT)</b>, стаж от 5 лет", True), ("<b>Персонализированный сертификат</b> о достижении уровня", True),
                ("<b>Progress check</b> — 5 видеопроверок в год + персональный видеоотчёт от методиста", True), ("Бесплатная консультация по составлению резюме", True),
                ("Гибкий график занятий", True)],
         gift="🎁 До 80 живых разговорных клубов в подарок при оплате в течение 60 минут после демо-урока"),
    dict(name="PREMIUM", price="10 633", desc="Премиальный пакет с максимальной гибкостью, индивидуальным сопровождением и расширенными привилегиями.",
         items=[("Ведущие преподаватели <b>с 10+ годами опыта</b>, носители языка или специалисты, <b>живущие в стране языка</b>", True), ("<b>Персонализированный сертификат</b> о достижении уровня", True),
                ("<b>Progress check</b> — полный цикл видеопроверок + видеоотчёт с рекомендациями методиста", True), ("Бесплатная консультация по составлению резюме", True),
                ("Индивидуальное сопровождение", True)],
         gift="🎁 До 80 живых разговорных клубов в подарок"),
]

def price_cards(root):
    out = []
    for p in PRICES:
        feat = " price-card--featured" if p.get("featured") else ""
        badge = '<span class="price-card__badge">Хит</span>' if p.get("featured") else ""
        items = "".join(f'<li class="{"" if ok else "is-off"}"><span>{t}</span></li>' for t, ok in p["items"])
        b = trial_btn("Хочу демо-урок", "btn--block" + (" " if p.get("featured") else " btn--violet"), f"Тариф {p['name']}")
        out.append(f'''<article class="price-card{feat}" data-tilt="4">{badge}
  <div class="price-card__name">{p['name']}</div>
  <p class="price-card__desc">{p['desc']}</p>
  <div class="price-card__price">от {p['price']} ₸<small>за урок</small></div>
  <ul class="price-card__list">{items}</ul>
  <div class="price-card__gift">{p['gift']}</div>
  {b}
</article>''')
    return f'<div class="grid grid-3" data-stagger>{"".join(out)}</div>'

def sticker():
    return '''<div class="hero__sticker" aria-hidden="true"><svg viewBox="0 0 200 200"><defs><path id="circ" d="M100,100 m-78,0 a78,78 0 1,1 156,0 a78,78 0 1,1 -156,0"/></defs>
<text font-family="Unbounded, sans-serif" font-size="17" font-weight="700" letter-spacing="3.2" fill="currentColor"><textPath href="#circ">BE BEST ✦ СТАНЬ ЛУЧШЕЙ ВЕРСИЕЙ СЕБЯ ✦ </textPath></text></svg><b>😜</b></div>'''

GREETINGS = ["Hello", "Hallo", "¡Hola!", "Ciao", "Bonjour", "Olá", "Cześć", "Привет", "Сәлем"]

# =================================================================== HOME
def build_index():
    def body(root):
        rot = "".join(f"<span>{L['word']}</span>" for L in LANGS)
        avatars = "".join(f'<li style="background:{AV_COLORS[i]};animation-delay:{1.2 + i*0.1:.1f}s">{ch}</li>' for i, ch in enumerate("АДВОК"))
        lang_rows = "".join(f'''<a class="lang-row" href="{root}languages/{L['key']}.html" data-reveal="up" style="--d:{i*0.05:.2f}s">{flag(root, L['flag'], '', L['name'])}<div><b>{L['name']}</b><small>{L['native']} · {sum(1 for c in COURSES if c['lang']==L['key'])} программ</small></div><span class="course-card__arrow">{icon('arrow')}</span></a>''' for i, L in enumerate(LANGS))
        # orbit
        outer, inner = LANGS[:4], LANGS[4:]
        def orbit_items(lst, offset):
            s = []
            for i, L in enumerate(lst):
                a = (i / len(lst)) * 2 * math.pi + offset
                x = 50 + 50 * math.cos(a); y = 50 + 50 * math.sin(a)
                s.append(f'<div class="orbit__item" data-a="{a:.4f}" style="left:{x:.2f}%;top:{y:.2f}%"><a href="{root}languages/{L["key"]}.html">{flag(root, L["flag"], "", L["name"])}<span>{L["native"]}</span></a></div>')
            return "".join(s)
        popular = [c for c in COURSES if c.get("popular")][:8]
        pop_cards = "".join(course_card(root, c) for c in popular)
        teachers = "".join(teacher_card(t, i) for i, t in enumerate([TEACHERS[1], TEACHERS[18], TEACHERS[26], TEACHERS[11]]))
        stats = "".join(f'''<div class="stat" data-reveal="up" style="--d:{i*0.1:.1f}s"><div class="stat__num" data-count="{n}" data-suffix="{suf}">0</div><p class="stat__label">{lbl}</p></div>''' for i, (n, lbl, suf) in enumerate(STATS_HOME))
        lang_opts = "".join(f'<option value="{L["name"]}">{L["name"]}</option>' for L in LANGS + [MATH])
        flags_row = "".join(flag(root, L["flag"], "", L["name"]) for L in LANGS)
        return f'''
<section class="hero">
  <canvas class="hero__canvas" data-field></canvas>
  <div class="hero__vignette"></div>
  {sticker()}
  <div class="container hero__inner">
    <span class="eyebrow" data-reveal="up">Онлайн-школа иностранных языков · 10 лет</span>
    <h1 class="h-mega hero__title" data-split>Заговори на&nbsp;языке <span class="hero__rotator">{rot}</span></h1>
    <div class="hero__bottom">
      <div class="flex" style="flex-direction:column;gap:28px">
        <p class="lead" data-reveal="up" style="--d:.5s;max-width:560px">Оптимальное решение для тех, кто решил начать изучать иностранный язык или усовершенствовать свои знания. Живой язык вместо тяжёлой грамматики.</p>
        <div class="hero__actions" data-reveal="up" style="--d:.65s">{trial_btn("Пробный урок бесплатно")}{btn("Узнать свой уровень", root + "test.html", "btn--ghost")}</div>
      </div>
      <div class="flex" style="flex-direction:column;gap:22px;align-items:flex-start;--d:.8s" data-reveal="up">
        <div class="hero__avatars"><ul>{avatars}</ul><p><b>5000+</b><br>выпускников и по 10 новых каждый день</p></div>
        <div class="hero__badges"><span class="pill">⭐ 4.9 рейтинг студентов</span><span class="pill">🌍 7 языков</span><span class="pill">🕐 уроки 24/7</span></div>
      </div>
    </div>
  </div>
  <div class="scroll-cue"><span>Скролл</span><i></i></div>
</section>

{marquee_tape(GREETINGS + ["Be Best", "Speak up"], "", "0.8")}

<section class="section section--paper">
  <div class="container">
    <span class="eyebrow" data-reveal="up">Наш подход</span>
    <p class="statement mt" data-statement>Наша цель — не нагружать студентов тяжёлой грамматикой, делая из них филологов. Мы учим <span class="hl">настоящему, живому языку</span> <span class="inline-chip">{flag_svg('gb')}</span> — тому, который вы услышите в магазине, который позволит общаться, заводить знакомства <span class="inline-chip">{flag_svg('es')}</span> и чётко формулировать свои мысли на иностранном языке.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="container"><div class="grid grid-4">{stats}</div></div>
</section>

<section class="section section--paper">
  <div class="container">
    <div class="section-head section-head--split">
      <div><span class="eyebrow" data-reveal="up">Кратко о школе</span><h2 class="h-l mt-s" data-split>Почему с BeBest получается</h2></div>
      <p class="lead" data-reveal="up">Мы не конвейер. Нам важно, чтобы обучение основывалось на передаче опыта и дружеской коммуникации.</p>
    </div>
    <div class="bento">
      <div class="bento-cell bento-cell--violet b-wide" data-reveal="up" data-tilt="3">
        <span class="bento-cell__label">practice</span>
        <div class="bento-cell__big"><span data-count="70" data-suffix="%">0</span></div>
        <p>70% времени на уроке говорит и практикуется студент — знания сразу применяются в диалогах с преподавателем и группой.</p>
        <div class="bento-meter" style="--w:70%"><i></i></div>
      </div>
      <div class="bento-cell bento-cell--ink" data-reveal="up" style="--d:.1s" data-tilt="4">
        <span class="bento-cell__label" style="color:var(--lime)">languages</span>
        <div class="bento-cell__big">7</div>
        <div class="bento-langs">{flags_row}</div>
      </div>
      <div class="bento-cell b-tall" data-reveal="up" style="--d:.15s">
        <span class="bento-cell__label">easy!</span>
        <h3 class="h-m">Мобильное приложение для учеников</h3>
        <p>Домашние задания, словарь и прогресс — всегда в кармане.</p>
        <div class="phone-mock" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div>
      </div>
      <div class="bento-cell bento-cell--lime" data-reveal="up" style="--d:.2s" data-tilt="4">
        <span class="bento-cell__label">deadline</span>
        <h3 class="h-m">Результат к сроку</h3>
        <p>Программы рассчитаны на достижение результата за определённое количество занятий.</p>
      </div>
      <div class="bento-cell" data-reveal="up" style="--d:.25s" data-tilt="4">
        <span class="bento-cell__label">LMS</span>
        <h3 class="h-m">Своя платформа</h3>
        <p>Learning management system: собственная платформа для онлайн-обучения.</p>
      </div>
      <div class="bento-cell bento-cell--coral" data-reveal="up" style="--d:.1s" data-tilt="4">
        <span class="bento-cell__label">quality</span>
        <h3 class="h-m">Контроль качества</h3>
        <p>Каждые полгода преподаватели проходят квалификацию, методисты следят за качеством.</p>
      </div>
      <div class="bento-cell bento-cell--ink" data-reveal="up" style="--d:.15s" data-tilt="4">
        <span class="bento-cell__label" style="color:var(--lime)">grammar</span>
        <h3 class="h-m">Просто о сложном</h3>
        <p style="opacity:.75">Показываем, как работает язык в жизни, и объясняем грамматику простым языком.</p>
      </div>
      <div class="bento-cell b-half" data-reveal="up">
        <span class="bento-cell__label">friends</span>
        <div class="flex between center gap"><h3 class="h-m">10 лет учим и дружим с нашими студентами</h3><span class="bento-cell__emoji">🤝</span></div>
      </div>
      <div class="bento-cell bento-cell--violet b-half" data-reveal="up" style="--d:.1s">
        <span class="bento-cell__label">mood</span>
        <div class="flex between center gap"><h3 class="h-m">Наш любимый эмоджи в чатах со студентами</h3><span class="bento-cell__emoji" style="animation-delay:-2s">😜</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container orbit-wrap">
    <div>
      <span class="eyebrow" data-reveal="up">7 языков · 50+ программ</span>
      <h2 class="h-l mt-s" data-split>Выберите язык, который изменит вашу жизнь</h2>
      <div class="lang-list mt">{lang_rows}</div>
    </div>
    <div class="orbit" data-reveal="scale">
      <div class="orbit__ring" data-spin="0.16">{orbit_items(outer, -math.pi/2)}</div>
      <div class="orbit__ring orbit__ring--2" data-spin="-0.24">{orbit_items(inner, math.pi/6)}</div>
      <div class="orbit__core"><div><b>7</b><small>языков</small></div></div>
    </div>
  </div>
</section>

<section class="hscroll">
  <div class="hscroll__sticky">
    <div class="container"><span class="eyebrow">Путь студента</span><h2 class="h-l mt-s">Как проходит обучение</h2></div>
    <div class="hscroll__track">
      <article class="step-card"><div class="step-card__icon">{icon('play')}</div><div><h3>Пробный урок</h3><p class="mt-s">Обучение начинается с бесплатного пробного урока — знакомитесь с преподавателем и нашим подходом.</p></div><span class="step-card__n">01</span></article>
      <article class="step-card"><div class="step-card__icon">{icon('users')}</div><div><h3>Удобный формат</h3><p class="mt-s">Индивидуально, в мини-группах (2–4 студента) или в группах до 8 человек — на интерактивной платформе школы.</p></div><span class="step-card__n">02</span></article>
      <article class="step-card"><div class="step-card__icon">{icon('target')}</div><div><h3>Программа под вашу цель</h3><p class="mt-s">Преподаватель составит программу уроков для ваших целей и порекомендует количество уроков для освоения уровня.</p></div><span class="step-card__n">03</span></article>
      <article class="step-card"><div class="step-card__icon">{icon('cert')}</div><div><h3>Сертификат уровня</h3><p class="mt-s">После финального теста в конце каждого уровня вы получаете персонализированный сертификат.</p></div><span class="step-card__n">04</span></article>
      <article class="step-card" style="background:var(--violet);border-color:var(--violet);justify-content:center;align-items:flex-start"><h3>Готовы начать?</h3><p>Первый урок — бесплатно.</p>{trial_btn("Хочу пробный урок")}</article>
    </div>
    <div class="hscroll__bar"><i></i></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head section-head--split">
      <div><span class="eyebrow" data-reveal="up">Популярно сейчас</span><h2 class="h-l mt-s" data-split>Курсы, которые выбирают чаще всего</h2></div>
      <div data-reveal="up">{btn("Все 50+ курсов", root + "courses.html", "btn--ghost")}</div>
    </div>
    <div class="grid grid-4" data-stagger>{pop_cards}</div>
  </div>
</section>

<section class="section section--paper" id="price">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow" data-reveal="up">Стоимость</span>
      <h2 class="h-l" data-split>Выберите свой формат</h2>
      <p class="lead" data-reveal="up">Первый урок — бесплатно. Платите только за результат, который чувствуете.</p>
    </div>
    {price_cards(root)}
    <div class="mt-l" style="text-align:center" data-reveal="up"><a class="link-arrow" href="{root}price.html">Сравнить все тарифы подробно {icon('arrow')}</a></div>
  </div>
</section>

<section class="section section--violet" style="overflow:hidden">
  <div class="blob blob--lime" style="width:500px;height:500px;right:-150px;top:-100px;opacity:.35"></div>
  <div class="container grid grid-2 center" style="position:relative">
    <div>
      <span class="eyebrow" style="color:#fff" data-reveal="up">Для бизнеса</span>
      <h2 class="h-l mt-s" data-split>Корпоративное обучение языкам</h2>
      <p class="lead mt" style="color:rgba(255,255,255,.85)" data-reveal="up">Хотите, чтобы сотрудники свободно заговорили на иностранном языке, вели переговоры или деловую переписку? Мы поможем!</p>
      <div class="mt" data-reveal="up">{btn("Подробнее для компаний", root + "courses/korporativnyj-anglijskij.html", "btn--ink")}</div>
    </div>
    <ul class="grid" data-stagger style="gap:14px">
      <li class="card" style="background:rgba(255,255,255,.1);border-color:rgba(255,255,255,.2)"><b class="h-s">📅 Персональные графики</b><p style="opacity:.8;margin-top:6px">Обучение онлайн в удобное для каждого сотрудника время.</p></li>
      <li class="card" style="background:rgba(255,255,255,.1);border-color:rgba(255,255,255,.2)"><b class="h-s">👥 Индивидуально или в группе</b><p style="opacity:.8;margin-top:6px">С коллегами — дешевле и с командным духом.</p></li>
      <li class="card" style="background:rgba(255,255,255,.1);border-color:rgba(255,255,255,.2)"><b class="h-s">🎯 Пробный урок каждому</b><p style="opacity:.8;margin-top:6px">Подберём преподавателя под каждого сотрудника.</p></li>
      <li class="card" style="background:rgba(255,255,255,.1);border-color:rgba(255,255,255,.2)"><b class="h-s">💸 Гибкие цены</b><p style="opacity:.8;margin-top:6px">Система скидок для корпоративных клиентов.</p></li>
    </ul>
  </div>
</section>

<section class="section section--paper">
  <div class="container founder">
    <div class="founder__portrait" data-reveal="clip" data-tilt="4">
      <span class="ring"></span><span class="ring"></span><span class="initials" data-speed="-0.06">ВЗ</span>
      <span class="tag">15 лет в преподавании</span>
    </div>
    <div class="flex" style="flex-direction:column;gap:26px">
      <span class="eyebrow" data-reveal="up">Основательница школы</span>
      <p class="founder__quote" data-split>Стань собой — самым лучшим собой!</p>
      <div class="founder__text" data-reveal="up">
        <p>Мне всегда очень везло с учителями! Однажды учительница химии дала мне прочитать стихотворение, в котором была эта строка. Мне кажется, именно так и родилось название школы BeBest.</p>
        <p>Я не жду от студентов, что они выучат всё и сразу, но <b>важно сегодня быть чуточку лучше и знать чуточку больше, чем вчера.</b> Мой бизнес — не конвейер. <b>Нам важен каждый клиент и каждая маленькая победа над собой.</b></p>
        <p>Моя семья сегодня насчитывает более 5000 человек — это все студенты BeBest и наш замечательный коллектив. <b>Мы помогаем сделать жизнь лучше, возможности — реальными, хорошее образование — доступным.</b></p>
      </div>
      <div class="founder__sign" data-reveal="up">Валентина Залевская<small>Основательница BeBest, практикующий педагог</small></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head section-head--split">
      <div><span class="eyebrow" data-reveal="up">Команда</span><h2 class="h-l mt-s" data-split>Наши преподаватели</h2></div>
      <div data-reveal="up" class="flex wrap gap center"><p class="lead">Каждые полгода — квалификация. 3 из 10 кандидатов проходят отбор.</p>{btn("Все преподаватели", root + "teachers.html", "btn--ghost")}</div>
    </div>
    <div class="grid grid-4" data-stagger>{teachers}</div>
  </div>
</section>

{reviews_section(root)}

<section class="section--tight">{marquee_big(["English", "Deutsch", "Español", "Italiano", "Français", "Português", "Polski"])}</section>

<section class="section">
  <div class="container grid grid-2" style="gap:clamp(40px,6vw,100px);align-items:start">
    <div style="position:sticky;top:120px" class="flex" >
      <div class="flex" style="flex-direction:column;gap:22px">
        <span class="eyebrow" data-reveal="up">FAQ</span>
        <h2 class="h-l" data-split>Часто задаваемые вопросы</h2>
        <p class="lead" data-reveal="up">Не нашли ответ? Напишите нам — ответим за пару минут.</p>
        <div class="flex wrap gap" data-reveal="up">{btn("Все вопросы", root + "faq.html", "btn--ghost")}{btn("WhatsApp", WA, "", 'target="_blank" rel="noopener"', "wa")}</div>
      </div>
    </div>
    {faq_block(FAQ[:6], by_founder=True)}
  </div>
</section>

<section class="section section--lime" id="trial">
  <div class="container grid grid-2 center" style="gap:clamp(30px,6vw,90px)">
    <div class="flex" style="flex-direction:column;gap:20px">
      <span class="eyebrow" data-reveal="up">Бесплатно · онлайн · в удобное время</span>
      <h2 class="h-xl" data-split>Запишитесь на пробное занятие</h2>
      <p class="lead" style="color:rgba(13,11,31,.7)" data-reveal="up">…и попробуйте обучение на практике!</p>
    </div>
    <form class="form js-lead-form card" style="background:var(--ink);color:var(--paper);border:0" novalidate data-reveal="up">
      <div class="field"><input id="f-name" name="name" type="text" placeholder=" " autocomplete="name"><label for="f-name">Ваше имя</label></div>
      <div class="field"><input id="f-phone" name="phone" type="tel" placeholder=" " autocomplete="tel"><label for="f-phone">Телефон / WhatsApp</label></div>
      <div class="field"><select id="f-lang" name="lang">{lang_opts}</select><label for="f-lang">Язык</label></div>
      <button class="btn btn--block" type="submit"><span class="btn__text"><span>Попробовать бесплатно</span><span>Попробовать бесплатно</span></span><span class="btn__icon">{icon('arrow')}</span></button>
      <p class="form__note">Нажимая «Попробовать бесплатно», вы принимаете <a href="{root}terms.html">условия обслуживания</a>.</p>
    </form>
  </div>
</section>

<section style="padding:60px 0 20px;overflow:hidden">
  {marquee_tape(["Ищем преподавателей!", "Немецкий", "Испанский", "Итальянский", "Французский", "Английский", "Португальский", "Присоединяйся к команде BeBest"], "alt", "0.6", "right")}
  <div class="container" style="text-align:center;margin-top:50px" data-reveal="up">{btn("Вакансии", root + "vacancies.html", "btn--ghost")}</div>
</section>

<section class="section section--tight">
  <div class="container">
    <div class="section-head"><span class="eyebrow" data-reveal="up">Онлайн-школа в Казахстане</span><h2 class="h-m" data-reveal="up">Онлайн-школа английского языка BeBest</h2></div>
    <div class="grid grid-2 muted" data-reveal="up" style="font-size:15px">
      <p>BeBest — онлайн-школа английского в Казахстане. Мы помогаем студентам овладеть языком на уровне, позволяющем свободно и уверенно использовать его в повседневной жизни, образовании и карьере. Индивидуальный подход, компетентные преподаватели, интерактивные уроки и детальная обратная связь делают обучение комфортным и эффективным.</p>
      <p>Гибкий формат позволяет выбрать оптимальное время и темп. На инновационной платформе студенты занимаются с преподавателем в реальном времени, обмениваются материалами и заданиями, а библиотека видеоуроков и тестов помогает закреплять знания и отслеживать прогресс самостоятельно.</p>
    </div>
  </div>
</section>
'''
    page("index.html", "Онлайн-школа иностранных языков BeBest — английский, немецкий, испанский онлайн в Казахстане",
         "Онлайн-школа BeBest: английский, немецкий, испанский, итальянский, французский, португальский и польский языки. Первый урок бесплатно. 5000+ выпускников.",
         body, "", cls="page-home")

# =================================================================== LANGUAGE HUB
def build_lang(L):
    def body(root):
        cs = [c for c in COURSES if c["lang"] == L["key"]]
        cards = "".join(course_card(root, c) for c in cs)
        if L["key"] in TEST_LANG:
            cards += f'''<a class="course-card" href="{test_href(root, L['key'])}" style="--c:var(--lime)" data-cursor="Тест"><div class="course-card__top"><span class="course-card__tag">Бесплатно</span><span style="font-size:30px">🧠</span></div><h3 class="course-card__title">Тест на знание {L['gen']}</h3><p class="course-card__text">Определите уровень за 3 минуты — прямо сейчас.</p><div class="course-card__go"><span>Пройти тест</span><span class="course-card__arrow">{icon('arrow')}</span></div></a>'''
        ts = [t for t in TEACHERS if L["key"] in t[1]]
        tcards = "".join(teacher_card(t, i) for i, t in enumerate(ts[:4]))
        teach = f'''<section class="section"><div class="container">
  <div class="section-head section-head--split"><div><span class="eyebrow" data-reveal="up">Преподаватели</span><h2 class="h-l mt-s" data-split>Кто будет вас учить</h2></div>
  <div data-reveal="up">{btn("Все преподаватели", root + "teachers.html?lang=" + L['key'], "btn--ghost")}</div></div>
  <div class="grid grid-4" data-stagger>{tcards}</div></div></section>''' if ts else ""
        hero_extra = f'''<div class="flex wrap gap" data-reveal="up" style="--d:.35s">{trial_btn("Пробный урок бесплатно", "", "Язык: " + L['low'])}{btn("Тест уровня", test_href(root, L['key']), "btn--ghost") if L['key'] in TEST_LANG else ""}</div>
<div class="page-hero__meta" data-reveal="up" style="--d:.45s"><span class="pill">{flag(root, L['flag'])}{L['native']}</span><span class="pill">📚 {len(cs)} программ</span><span class="pill">👩‍🏫 {max(len(ts), 1)}+ преподавателей</span><span class="pill">💬 speaking clubs</span></div>'''
        return f'''{page_hero(root, f"{L['name']} язык онлайн <span class='accent-lime'>{L['hello']}</span>", L['why'], [("Языки", root + "courses.html"), (L['name'], None)], hero_extra)}
<div class="course-band" style="--c:{L['color']}"><div class="course-band__word">{L['word']} · {L['word']} · {L['word']}</div></div>
<section class="section"><div class="container">
  <div class="section-head section-head--split"><div><span class="eyebrow" data-reveal="up">Программы</span><h2 class="h-l mt-s" data-split>Курсы {L['gen']} языка</h2></div><p class="lead" data-reveal="up">Для взрослых, детей и компаний — от первого слова до международного экзамена.</p></div>
  <div class="grid grid-3" data-stagger>{cards}</div>
</div></section>
<section class="section section--paper"><div class="container">
  <div class="section-head section-head--center"><span class="eyebrow" data-reveal="up">Почему BeBest</span><h2 class="h-l" data-split>Учить {L['low']} — это легко</h2></div>
  <div class="grid grid-4" data-stagger>
    <div class="card feature"><span class="feature__num">01</span><div class="feature__icon">{icon('mic')}</div><div><h3 class="feature__title">70% практики</h3><p class="feature__text mt-s">Говорите с первого урока.</p></div></div>
    <div class="card feature"><span class="feature__num">02</span><div class="feature__icon">{icon('platform')}</div><div><h3 class="feature__title">Своя платформа</h3><p class="feature__text mt-s">Интерактивные уроки и приложение.</p></div></div>
    <div class="card feature"><span class="feature__num">03</span><div class="feature__icon">{icon('target')}</div><div><h3 class="feature__title">Под вашу цель</h3><p class="feature__text mt-s">Персональная программа и дедлайн.</p></div></div>
    <div class="card feature"><span class="feature__num">04</span><div class="feature__icon">{icon('cert')}</div><div><h3 class="feature__title">Сертификат</h3><p class="feature__text mt-s">После каждого уровня.</p></div></div>
  </div>
</div></section>
{teach}
{reviews_section(root, "Студенты о BeBest")}
{cta_block(root, f"Заговорите на {L['prep']} уже на первом уроке", course="Язык: " + L['low'])}
'''
    page(f"languages/{L['key']}.html", f"{L['name']} язык онлайн — курсы в школе BeBest",
         f"Курсы {L['gen']} языка онлайн для взрослых, детей и компаний. {L['why']} Первый урок бесплатно.", body, "langs")

# =================================================================== COURSE
def build_course(c):
    L = lang_of(c)
    K = course_content(c)
    def body(root):
        facts = [("Формат", "Онлайн"), ("Урок", "50 / 90 мин"), ("Уровни", K["levels"]), ("Старт", "Любой день")]
        facts_html = "".join(f'<div class="course-fact"><small>{a}</small><b>{b}</b></div>' for a, b in facts)
        aud = "".join(f'<div class="card feature"><div class="feature__icon">{icon(i)}</div><div><h3 class="feature__title">{t}</h3><p class="feature__text mt-s">{x}</p></div></div>' for i, t, x in K["audience"])
        prog = "".join(f'<div class="tl-item"><span class="tl-item__dot">{n+1:02d}</span><div><h3>{t}</h3><p>{x}</p></div></div>' for n, (t, x) in enumerate(K["program"]))
        skills = "".join(f'<div class="skill"><div class="skill__top"><span>{s}</span><span>{v}%</span></div><div class="skill__bar"><i style="--w:{v}%"></i></div></div>' for s, v in K["skills"])
        res = "".join(f'<li class="card" style="display:flex;gap:14px;align-items:center"><span class="feature__icon" style="width:44px;height:44px;flex:none">{icon("check")}</span><span style="font-weight:700">{r}</span></li>' for r in K["results"])
        hub = f'{root}languages/{L["key"]}.html' if L["key"] != "math" else f'{root}courses.html'
        related = [x for x in COURSES if x["lang"] == c["lang"] and x["slug"] != c["slug"]][:3]
        if len(related) < 3:
            related += [x for x in COURSES if x.get("popular") and x["slug"] != c["slug"] and x not in related][:3 - len(related)]
        rel_html = "".join(course_card(root, x) for x in related)
        ts = [t for t in TEACHERS if c["lang"] in t[1]][:4]
        tsec = f'''<section class="section"><div class="container">
  <div class="section-head section-head--split"><div><span class="eyebrow" data-reveal="up">Преподаватели</span><h2 class="h-l mt-s" data-split>Ваши будущие преподаватели</h2></div><div data-reveal="up">{btn("Все преподаватели", root + "teachers.html?lang=" + c['lang'], "btn--ghost")}</div></div>
  <div class="grid grid-4" data-stagger>{"".join(teacher_card(t, i) for i, t in enumerate(ts))}</div></div></section>''' if ts else ""
        exam_block = ""
        if "exam" in K:
            ex = K["exam"]
            exam_block = f'''<section class="section section--tight"><div class="container"><div class="cta" style="background:var(--ink-2);border:1px solid var(--line)" data-reveal="up">
  <div><span class="eyebrow">Об экзамене</span><h2 class="h-l mt-s">{ex['name']}</h2><p class="lead mt-s">{ex['full']}</p></div>
  <div class="grid" style="gap:12px"><div class="pill">📏 {ex['scale']}</div><div class="pill">🎯 {ex['use']}</div></div></div></div></section>'''
        test_link = btn("Тест уровня", test_href(root, c["lang"]), "btn--ghost") if c["lang"] in TEST_LANG else btn("Все курсы", root + "courses.html", "btn--ghost")
        title = c["title"]
        return f'''<section class="page-hero course-hero">
  <div class="page-hero__bg"><canvas class="hero__canvas" data-field="lite"></canvas><div class="blob" style="background:{L['color']};width:560px;height:560px;right:-160px;top:-180px;opacity:.35"></div></div>
  <div class="container">
    {crumbs(root, [("Курсы", root + "courses.html"), (L['name'], hub), (title, None)])}
    <div class="course-hero__grid mt">
      <div class="flex" style="flex-direction:column;gap:26px">
        <img class="course-hero__flag" src="{root}assets/img/flags/{L['flag']}.svg" alt="{L['name']}" style="--c:{L['color']}">
        <h1 class="h-xl" data-split>{title}</h1>
        <p class="lead" data-reveal="up" style="--d:.3s">{K['lead']}</p>
        <div class="flex wrap gap" data-reveal="up" style="--d:.45s">{trial_btn("Записаться на пробный урок", "", title)}{test_link}</div>
      </div>
      <div class="course-facts" data-reveal="up" style="--d:.5s">{facts_html}</div>
    </div>
  </div>
  <div class="course-band" style="--c:{L['color']}"><div class="course-band__word">{L['word']} · {escape(title)} · {L['word']}</div></div>
</section>

<section class="section"><div class="container">
  <div class="section-head"><span class="eyebrow" data-reveal="up">Кому подойдёт</span><h2 class="h-l mt-s" data-split>Этот курс для вас, если…</h2></div>
  <div class="grid grid-4" data-stagger>{aud}</div>
</div></section>

{exam_block}

<section class="section section--paper"><div class="container grid grid-2" style="gap:clamp(40px,7vw,120px);align-items:start">
  <div style="position:sticky;top:120px" class="flex"><div class="flex" style="flex-direction:column;gap:22px">
    <span class="eyebrow" data-reveal="up">Программа</span><h2 class="h-l" data-split>Как устроен курс</h2>
    <p class="lead" data-reveal="up">Точную программу и количество уроков преподаватель составит после пробного занятия — под вашу цель и уровень.</p>
    <div data-reveal="up">{trial_btn("Получить программу", "btn--violet", title)}</div></div></div>
  <div class="timeline"><span class="timeline__fill"></span>{prog}</div>
</div></section>

<section class="section"><div class="container grid grid-2" style="gap:clamp(40px,7vw,120px)">
  <div class="flex" style="flex-direction:column;gap:24px"><span class="eyebrow" data-reveal="up">Фокус курса</span><h2 class="h-l" data-split>Что прокачаем</h2><div class="skills">{skills}</div></div>
  <div class="flex" style="flex-direction:column;gap:24px"><span class="eyebrow" data-reveal="up">Результат</span><h2 class="h-l" data-split>После курса вы…</h2><ul class="grid" data-stagger style="gap:12px">{res}</ul></div>
</div></section>

<section class="section section--paper"><div class="container">
  <div class="section-head section-head--center"><span class="eyebrow" data-reveal="up">Стоимость</span><h2 class="h-l" data-split>Тарифы обучения</h2><p class="lead" data-reveal="up">Первый урок — бесплатно для всех тарифов.</p></div>
  {price_cards(root)}
</div></section>

{tsec}

<section class="section"><div class="container grid grid-2" style="gap:clamp(40px,6vw,100px);align-items:start">
  <div class="flex" style="flex-direction:column;gap:20px"><span class="eyebrow" data-reveal="up">Вопросы</span><h2 class="h-l" data-split>Частые вопросы о курсе</h2></div>
  {faq_block(K['faq'])}
</div></section>

<section class="section section--tight"><div class="container">
  <div class="section-head section-head--split"><div><span class="eyebrow" data-reveal="up">Смотрите также</span><h2 class="h-m mt-s" data-reveal="up">Похожие программы</h2></div><div data-reveal="up"><a class="link-arrow" href="{hub}">Все курсы направления {icon('arrow')}</a></div></div>
  <div class="grid grid-3" data-stagger>{rel_html}</div>
</div></section>

{cta_block(root, "Начните с бесплатного пробного урока", course=title)}
'''
    page(f"courses/{c['slug']}.html", f"{c['title']} онлайн — школа BeBest",
         f"{c['title']}: {c['short']} Онлайн-обучение в школе BeBest, первый урок бесплатно.", body, "langs")

# =================================================================== CATALOG
def build_catalog():
    def body(root):
        chips = '<button class="chip is-active" type="button" data-filter="all">Все</button>'
        chips += "".join(f'<button class="chip" type="button" data-filter="{L["key"]}">{L["name"]}</button>' for L in LANGS)
        chips2 = "".join(f'<button class="chip" type="button" data-filter="{k}">{v}</button>' for k, v in [("adults", "Взрослым"), ("kids", "Детям"), ("exams", "Экзамены"), ("business", "Карьера"), ("corporate", "Компаниям"), ("clubs", "Разговорные клубы"), ("beginner", "С нуля")])
        cards = "".join(course_card(root, c) for c in COURSES)
        return f'''{page_hero(root, "Каталог онлайн-курсов <span class='grad-text'>BeBest</span>", "50+ программ на 7 языках и математика. Отфильтруйте по языку или цели — и запишитесь на бесплатный пробный урок.", [("Каталог курсов", None)])}
<section class="section" style="padding-top:20px"><div class="container">
  <div class="chips" data-filter-group="#catalog" data-param="lang" data-counter="#cat-count" data-reveal="up">{chips}{chips2}</div>
  <p class="muted mt-s" data-reveal="up">Найдено программ: <b id="cat-count" style="color:var(--lime)">{len(COURSES)}</b></p>
  <div class="grid grid-4 mt" id="catalog">{cards}</div>
</div></section>
{cta_block(root, "Не знаете, что выбрать?", "Пройдите бесплатный пробный урок — преподаватель определит уровень и подберёт программу под вашу цель.")}
'''
    page("courses.html", "Каталог онлайн-курсов иностранных языков — BeBest", "Все курсы английского, немецкого, испанского, итальянского, французского, португальского и польского языков онлайн.", body, "langs")

# =================================================================== ABOUT
def build_about():
    def body(root):
        nums = [("12", "уроков мы проводим каждый час по всему миру", ""), ("10", "лет опыта и экспертизы в обучении языкам", ""), ("98", "студентов успешно сдают экзамен на подтверждение уровня", "%"),
                ("3", "из 10 учителей проходят отбор и стажировку в школу", "/10"), ("150", "собственных материалов, вебинаров и мероприятий", ""), ("5000", "выпускников по всему миру", "+")]
        stats = "".join(f'<div class="stat" data-reveal="up" style="--d:{i*0.08:.2f}s"><div class="stat__num" data-count="{n}" data-suffix="{s}">0</div><p class="stat__label">{l}</p></div>' for i, (n, l, s) in enumerate(nums))
        return f'''{page_hero(root, "Мы верим, что выучить язык может <span class='accent-lime'>каждый</span>", "Дать максимум для эффективного обучения, быть интересными для наших студентов и обеспечить необходимый комфорт — вот цели, которых мы придерживаемся с первого дня.", [("О школе", None)])}
{marquee_tape(["Speaking", "Reading", "Listening", "Writing", "Grammar", "Vocabulary", "Confidence"], "", "0.7")}
<section class="section section--paper"><div class="container">
  <span class="eyebrow" data-reveal="up">Миссия</span>
  <p class="statement mt" data-statement>Знание языков открывает возможности: для учёбы, для работы, для культурной интеграции и социальной мобильности. Мы в BeBest помогаем сделать <span class="hl">жизнь людей лучше</span>, возможности — реальными, хорошее образование — доступным.</p>
</div></section>
<section class="section"><div class="container">
  <div class="section-head"><span class="eyebrow" data-reveal="up">BeBest в цифрах</span><h2 class="h-l mt-s" data-split>Сильные стороны школы</h2></div>
  <div class="grid grid-3">{stats}</div>
</div></section>
<section class="section section--paper"><div class="container">
  <div class="section-head section-head--split"><div><span class="eyebrow" data-reveal="up">Методика</span><h2 class="h-l mt-s" data-split>Обучаем так, чтобы был результат</h2></div><p class="lead" data-reveal="up">Обучение соответствует международным стандартам и позволяет сдать IELTS, FCE / KET / PET, TOEFL и профессиональные тесты.</p></div>
  <div class="grid grid-3" data-stagger>
    <div class="card feature" data-tilt="5"><span class="feature__num">01</span><div class="feature__icon">{icon('platform')}</div><div><h3 class="feature__title">Обучение онлайн</h3><p class="feature__text mt-s">Всё, что нужно для урока, — хороший интернет. Разговаривайте с педагогом, пишите задания прямо на экране, проходите тесты онлайн — без дороги и сборов.</p></div></div>
    <div class="card feature" data-tilt="5"><span class="feature__num">02</span><div class="feature__icon">{icon('smile')}</div><div><h3 class="feature__title">Увлекательные уроки</h3><p class="feature__text mt-s">Обучение у нас — это микс учёбы и интересного времяпрепровождения. Мы делаем сложное простым.</p></div></div>
    <div class="card feature" data-tilt="5"><span class="feature__num">03</span><div class="feature__icon">{icon('rocket')}</div><div><h3 class="feature__title">Быстрое освоение языка</h3><p class="feature__text mt-s">70% урока вы практикуетесь в 4 навыках: speaking, reading, listening и writing — и быстро начинаете говорить.</p></div></div>
  </div>
</div></section>
<section class="section"><div class="container">
  <div class="section-head"><span class="eyebrow" data-reveal="up">Инфраструктура</span><h2 class="h-l mt-s" data-split>Больше, чем уроки</h2></div>
  <div class="grid grid-2" data-stagger>
    <a class="card feature" href="{root}blog.html" data-tilt="4" data-cursor="Блог"><div class="feature__icon">{icon('play')}</div><div><h3 class="feature__title">Вебинары и мероприятия</h3><p class="feature__text mt-s">Регулярно проводим бесплатные мастер-классы и вебинары на разнообразные темы с преподавателями и носителями языка.</p></div><span class="link-arrow">Узнать больше {icon('arrow')}</span></a>
    <a class="card feature" href="{root}courses/speaking-club.html" data-tilt="4" data-cursor="Клубы"><div class="feature__icon">{icon('mic')}</div><div><h3 class="feature__title">Еженедельные спикинг-клабы</h3><p class="feature__text mt-s">Каждую неделю собираем разговорные клубы для разных уровней владения языком.</p></div><span class="link-arrow">Узнать больше {icon('arrow')}</span></a>
  </div>
</div></section>
<section class="section section--paper"><div class="container founder">
  <div class="founder__portrait" data-reveal="clip"><span class="ring"></span><span class="ring"></span><span class="initials">ВЗ</span><span class="tag">Основательница BeBest</span></div>
  <div class="flex" style="flex-direction:column;gap:24px">
    <span class="eyebrow" data-reveal="up">Основатель школы</span>
    <h2 class="h-l" data-split>Валентина Залевская</h2>
    <div class="founder__text" data-reveal="up"><p>Практикующий преподаватель английского языка и русского как иностранного. <b>Трудоголик до мозга костей. Преподаватель по призванию.</b></p><p>Визионер, который понимает, что нужно студентам сегодня при изучении иностранного языка.</p></div>
    <div data-reveal="up">{btn("Контакты для сотрудничества", root + "contact.html", "btn--violet")}</div>
  </div>
</div></section>
{reviews_section(root)}
{cta_block(root)}
'''
    page("about.html", "О школе иностранных языков BeBest", "Познакомьтесь с нашим коллективом и методами обучения иностранным языкам. Лучшие преподаватели и выгодные цены.", body, "school")

# =================================================================== TEACHERS
def build_teachers():
    def body(root):
        used = []
        for t in TEACHERS:
            for l in t[1]:
                if l not in used: used.append(l)
        chips = '<button class="chip is-active" type="button" data-filter="all">Все</button>' + "".join(
            f'<button class="chip" type="button" data-filter="{l}">{LANG[l]["name"]}<sup>{sum(1 for t in TEACHERS if l in t[1])}</sup></button>' for l in [x["key"] for x in LANGS] if l in used)
        cards = "".join(teacher_card(t, i) for i, t in enumerate(TEACHERS))
        return f'''{page_hero(root, "Наши преподаватели и <span class='accent-lime'>академический отдел</span>", "Профессионалы с многолетним опытом и международными сертификатами. Каждые полгода — квалификация, методисты следят за качеством.", [("Преподаватели", None)])}
<section class="section" style="padding-top:20px"><div class="container">
  <div class="chips" data-filter-group="#teachers" data-param="lang" data-counter="#t-count" data-reveal="up">{chips}</div>
  <p class="muted mt-s" data-reveal="up">Показано: <b id="t-count" style="color:var(--lime)">{len(TEACHERS)}</b> преподавателей</p>
  <div class="grid grid-4 mt" id="teachers">{cards}</div>
</div></section>
{marquee_tape(["TESOL", "TKT", "CELTA", "DELE", "DELF", "Goethe", "CILS", "IELTS", "CEFR"], "", "0.7")}
{cta_block(root, "Хотите заниматься с одним из них?", "Запишитесь на пробный урок — подберём преподавателя под ваш характер, цель и график.")}
'''
    page("teachers.html", "Преподаватели школы BeBest", "Преподаватели английского, немецкого, испанского, итальянского, французского и португальского языков онлайн-школы BeBest.", body, "school")

# =================================================================== PRICE
def build_price():
    def body(root):
        rows = [("Опыт преподавателя", "до 2 лет", "5+ лет, TESOL / TKT", "10+ лет, носители / живут в стране языка"),
                ("Стоимость урока", "от 6 472 ₸", "от 7 397 ₸", "от 10 633 ₸"),
                ("Расписание", "Фиксированное", "Гибкое", "Максимально гибкое"),
                ("Персонализированный сертификат", "✓", "✓", "✓"),
                ("Progress check (5 видеопроверок в год)", "✓", "✓", "✓"),
                ("Видеоотчёт от методиста", "—", "✓", "✓"),
                ("Консультация по резюме", "—", "✓", "✓"),
                ("Индивидуальное сопровождение", "—", "—", "✓"),
                ("Разговорные клубы в подарок", "до 80*", "до 80*", "до 80")]
        trs = "".join(f'<div class="requisites" style="display:grid;grid-template-columns:1.4fr repeat(3,1fr);gap:16px;padding:18px 0;border-bottom:1px solid var(--line-ink)" data-reveal="up"><span style="font-weight:700;color:var(--ink)">{a}</span><span>{b}</span><span>{c}</span><span>{d}</span></div>' for a, b, c, d in rows)
        return f'''{page_hero(root, "Стоимость обучения. <span class='accent-lime'>Первый урок — бесплатно</span>", "Три тарифа под разные цели и бюджет. Платите за уроки, а не за абонемент в никуда.", [("Стоимость", None)])}
<section class="section section--paper"><div class="container">{price_cards(root)}</div></section>
<section class="section section--paper" style="padding-top:0"><div class="container">
  <div class="section-head"><span class="eyebrow" data-reveal="up">Подробно</span><h2 class="h-l mt-s" data-split>Сравнение тарифов</h2></div>
  <div style="overflow-x:auto"><div style="min-width:720px">
    <div style="display:grid;grid-template-columns:1.4fr repeat(3,1fr);gap:16px;padding:18px 0;border-bottom:2px solid var(--ink);font-family:var(--font-display);font-weight:700"><span></span><span>BASE</span><span style="color:var(--violet)">OPTIMAL</span><span>PREMIUM</span></div>
    {trs}
  </div></div>
  <p class="muted mt-s" style="font-size:13px">* при оплате в течение 60 минут после демо-урока. Точную стоимость пакета менеджер рассчитает после пробного урока.</p>
</div></section>
<section class="section"><div class="container grid grid-2" style="gap:clamp(40px,6vw,100px);align-items:start">
  <div class="flex" style="flex-direction:column;gap:20px"><span class="eyebrow" data-reveal="up">Вопросы об оплате</span><h2 class="h-l" data-split>Важно знать</h2></div>
  {faq_block([FAQ[1], FAQ[2], FAQ[0], FAQ[4], FAQ[8]])}
</div></section>
{cta_block(root, "Попробуйте бесплатно, а потом решайте")}
'''
    page("price.html", "Стоимость обучения — цены на онлайн-курсы BeBest", "Цены на онлайн-курсы иностранных языков в школе BeBest: тарифы BASE, OPTIMAL и PREMIUM. Первый урок бесплатно.", body, "price")

# =================================================================== FAQ
def build_faq():
    def body(root):
        return f'''{page_hero(root, "Частые вопросы", "Мы собрали ответы на самые популярные вопросы наших учеников.", [("FAQ", None)])}
<section class="section" style="padding-top:20px"><div class="container grid grid-2" style="gap:clamp(40px,6vw,100px);align-items:start">
  <div style="position:sticky;top:120px" class="flex"><div class="card" data-reveal="up" style="display:grid;gap:18px">
    <span style="font-size:56px" class="bento-cell__emoji">🤔</span>
    <h2 class="h-m">Не нашли ответ на свой вопрос?</h2><p class="muted">Оставьте заявку, и мы свяжемся с вами в ближайшее время.</p>
    {trial_btn("Задать вопрос")}{btn("Написать в WhatsApp", WA, "btn--ghost", 'target="_blank" rel="noopener"', "wa")}
  </div></div>
  {faq_block(FAQ, single=False, by_founder=True)}
</div></section>
'''
    page("faq.html", "Ответы на популярные вопросы | Школа BeBest", "Ответы на популярные вопросы об обучении в онлайн-школе иностранных языков BeBest.", body, "faq")

# =================================================================== CONTACT
def build_contact():
    def body(root):
        return f'''{page_hero(root, "Контакты <span class='accent-lime'>BeBest School</span>", "Работаем ежедневно с 10:00 до 19:00. Уроки проводим круглосуточно. Свяжитесь с нами любым удобным способом!", [("Контакты", None)])}
<section class="section" style="padding-top:20px"><div class="container">
  <div class="contact-grid" data-stagger>
    <div class="card contact-tile" data-tilt="4"><span class="feature__icon">{icon('clock')}</span><div><small class="muted">Сейчас в Алматы</small><div class="clock" data-clock>--:--:--</div></div><span class="status-dot" data-open-status>…</span></div>
    <a class="card contact-tile" href="tel:{PHONE}" data-tilt="4" data-cursor="Звонок"><span class="feature__icon">{icon('phone')}</span><div><small class="muted">Отдел продаж · только звонки</small><b>{PHONE_H}</b></div><span class="link-arrow">Позвонить {icon('arrow')}</span></a>
    <a class="card contact-tile" href="mailto:{EMAIL}" data-copy="{EMAIL}" data-tilt="4" data-cursor="Копировать"><span class="feature__icon">{icon('mail')}</span><div><small class="muted">Email отдела продаж</small><b>{EMAIL}</b></div><span class="link-arrow">Скопировать {icon('copy')}</span></a>
    <a class="card contact-tile" href="{WA}" target="_blank" rel="noopener" data-tilt="4" style="background:#25d366;color:#0d0b1f;border-color:#25d366"><span class="feature__icon" style="background:#0d0b1f;color:#25d366">{icon('wa')}</span><div><small>Самый быстрый способ</small><b>WhatsApp</b></div><span class="link-arrow">Написать {icon('arrow')}</span></a>
    <a class="card contact-tile" href="{TG}" target="_blank" rel="noopener" data-tilt="4" style="background:#2aabee;color:#fff;border-color:#2aabee"><span class="feature__icon" style="background:#fff;color:#2aabee">{icon('tg')}</span><div><small>Спецпредложения</small><b>Telegram-бот</b></div><span class="link-arrow">Открыть {icon('arrow')}</span></a>
    <a class="card contact-tile" href="{IG}" target="_blank" rel="noopener" data-tilt="4" style="background:linear-gradient(135deg,#f58529,#dd2a7b,#8134af);color:#fff;border:0"><span class="feature__icon" style="background:#fff;color:#dd2a7b">{icon('ig')}</span><div><small>Полезный контент</small><b>@be_best_school</b></div><span class="link-arrow">Подписаться {icon('arrow')}</span></a>
  </div>
</div></section>
<section class="section section--paper"><div class="container grid grid-3" style="align-items:start">
  <div class="card" data-reveal="up" style="display:grid;gap:14px"><span class="feature__icon">{icon('users')}</span><h3 class="h-s">Вакансии</h3><p class="muted">По всем вопросам трудоустройства обращайтесь в HR-отдел.</p><a class="link-arrow" href="mailto:{EMAIL_HR}">{EMAIL_HR} {icon('arrow')}</a></div>
  <div class="card" data-reveal="up" style="--d:.1s;display:grid;gap:14px"><span class="feature__icon">{icon('briefcase')}</span><h3 class="h-s">Партнёрам</h3><p class="muted">Для предложений о сотрудничестве и деловых обращений.</p><a class="link-arrow" href="mailto:{EMAIL_ADV}">{EMAIL_ADV} {icon('arrow')}</a></div>
  <div class="card" data-reveal="up" style="--d:.2s;display:grid;gap:10px"><span class="feature__icon">{icon('pin')}</span><h3 class="h-s">Реквизиты</h3>
    <div class="requisites"><div><span>Получатель</span><b>ИП BeBest</b></div><div><span>Адрес</span><b>Алматы, пр. Назарбаева 247, оф. 6</b></div><div><span>БИН (ИИН)</span><b>861114050167</b></div><div><span>Банк</span><b>АО «Kaspi Bank»</b></div><div><span>КБе / БИК</span><b>19 / CASPKZKA</b></div><div><span>Счёт</span><b style="word-break:break-all">KZ09722S000043226663</b></div></div></div>
</div></section>
{cta_block(root)}
'''
    page("contact.html", "Контакты онлайн-школы BeBest в Казахстане", "Контактная информация онлайн-школы BeBest: телефон, email, WhatsApp, Telegram и реквизиты.", body, "school")

# =================================================================== BLOG
POSTS = [
    dict(slug="kak-preodolet-yazykovoy-barer", title="Как преодолеть языковой барьер: 7 рабочих способов", tag="Мотивация", color="#d7ff3d", glyph="Aa", min=6,
         intro="Вы понимаете речь, знаете правила, но в момент разговора — пустота. Знакомо? Языковой барьер — это не про знания, а про привычку говорить. И её можно натренировать.",
         sections=[("Почему мы молчим", ["Страх ошибки, перфекционизм и отсутствие практики — три главные причины. В школе нас оценивали за ошибки, и мозг до сих пор считает их опасными."]),
                   ("Что реально работает", ["Говорите каждый день хотя бы 5 минут — с преподавателем, в разговорном клубе или сами с собой.", "Учите не слова, а фразы целиком: «I was wondering if…» полезнее, чем «wonder».", "Записывайте себя на диктофон и переслушивайте — вы удивитесь, насколько лучше звучите, чем думаете.", "Разрешите себе ошибаться: носители тоже говорят неидеально.", "Думайте на языке в бытовых ситуациях: комментируйте про себя, что делаете.", "Найдите тему, о которой вам интересно говорить, — и говорите о ней.", "Выберите формат, где 70% времени говорите вы."])],
         quote="Ошибка — это не провал, а доказательство того, что вы говорите."),
    dict(slug="skolko-vremeni-uchit-yazyk", title="Сколько времени нужно, чтобы выучить язык?", tag="Методика", color="#8f78ff", glyph="⏱", min=5,
         intro="Самый частый вопрос на пробном уроке. Честный ответ: зависит от цели, исходного уровня и регулярности. Но ориентиры есть.",
         sections=[("Уровни CEFR простыми словами", ["A1–A2 — базовое общение: представиться, заказать еду, спросить дорогу.", "B1 — уверенный повседневный уровень: путешествия, работа на простых задачах.", "B2 — свободное общение, учёба и работа на языке.", "C1–C2 — профессиональный и академический уровень."]),
                   ("От чего зависит скорость", ["Регулярность важнее интенсивности: 3 урока в неделю лучше, чем 1 марафон раз в месяц.", "Практика речи: чем больше вы говорите, тем быстрее растёт уровень.", "Цель и дедлайн: конкретная цель дисциплинирует лучше любой мотивации."])],
         quote="Важно сегодня быть чуточку лучше и знать чуточку больше, чем вчера."),
    dict(slug="ielts-ili-toefl", title="IELTS или TOEFL: какой экзамен выбрать?", tag="Экзамены", color="#4fd1ff", glyph="✍", min=7,
         intro="Оба экзамена подтверждают уровень английского, но устроены по-разному. Разбираемся, какой подойдёт именно вам.",
         sections=[("IELTS", ["Принимается в Великобритании, Австралии, Канаде, Европе.", "Speaking — живое интервью с экзаменатором.", "Шкала от 0 до 9 баллов."]),
                   ("TOEFL iBT", ["Особенно популярен в университетах США.", "Speaking — ответы записываются на компьютер.", "Шкала от 0 до 120 баллов."]),
                   ("Как выбрать", ["Проверьте требования университета или работодателя — это главный критерий.", "Если вам комфортнее общаться с человеком — выбирайте IELTS.", "Если привыкли к академическим текстам и компьютерному формату — TOEFL."])],
         quote="Лучший экзамен — тот, который требует ваш университет."),
    dict(slug="nemetskiy-dlya-pereezda", title="Немецкий для переезда: с чего начать", tag="Релокация", color="#ffd23d", glyph="Ä", min=6,
         intro="Германия, Австрия, Швейцария — популярные направления для учёбы и работы. И почти везде нужен немецкий хотя бы на уровне A1–B1.",
         sections=[("Какой уровень нужен", ["A1 — для визы по воссоединению семьи.", "B1 — для многих рабочих виз и интеграции.", "B2–C1 — для учёбы в университете и работы врачом."]),
                   ("План на первые 3 месяца", ["Месяц 1: произношение, артикли, базовые фразы и порядок слов.", "Месяц 2: прошедшее время, бытовые темы — жильё, транспорт, магазины.", "Месяц 3: первые диалоги, разговорный клуб и подготовка к Goethe A1/A2."])],
         quote="Немецкая грамматика пугает только до тех пор, пока её не объяснят простым языком."),
]

def build_blog():
    def card(root, p, i):
        return f'''<a class="post-card" href="{root}blog/{p['slug']}.html" data-cursor="Читать" data-tags="{p['tag']}">
  <div class="post-card__img" style="--c:{p['color']}"><span>{p['glyph']}</span></div>
  <div class="post-card__meta"><span>{p['tag']}</span><span>· {p['min']} мин чтения</span></div>
  <h3 class="post-card__title">{p['title']}</h3>
</a>'''
    def body(root):
        cards = "".join(card(root, p, i) for i, p in enumerate(POSTS))
        return f'''{page_hero(root, "Блог <span class='accent-lime'>BeBest</span>", "Самые интересные материалы для самостоятельного изучения языков: советы, методика, экзамены и мотивация.", [("Блог", None)])}
<section class="section" style="padding-top:20px"><div class="container">
  <div class="grid grid-2" data-stagger style="gap:50px 28px">{cards}</div>
</div></section>
{cta_block(root, "Читать полезно. Говорить — ещё полезнее", "Применяйте знания на практике с преподавателем: первый урок бесплатно.")}
'''
    page("blog.html", "Блог школы BeBest — материалы для изучения языков", "Полезные статьи для самостоятельного изучения иностранных языков от преподавателей BeBest.", body, "school")

    for idx, p in enumerate(POSTS):
        def pbody(root, p=p, idx=idx):
            secs = []
            for h, items in p["sections"]:
                if len(items) == 1:
                    secs.append(f'<h2 data-reveal="up">{h}</h2><p data-reveal="up">{items[0]}</p>')
                else:
                    secs.append(f'<h2 data-reveal="up">{h}</h2><ul data-stagger>{"".join(f"<li>{x}</li>" for x in items)}</ul>')
            secs.insert(1, f'<blockquote data-reveal="scale">{p["quote"]}</blockquote>')
            others = "".join(card(root, q, i) for i, q in enumerate(POSTS) if q["slug"] != p["slug"])[:]
            return f'''<div class="reading-bar"></div>
{page_hero(root, p['title'], p['intro'], [("Блог", root + "blog.html"), (p['tag'], None)], f'<div class="page-hero__meta" data-reveal="up"><span class="pill">🏷 {p["tag"]}</span><span class="pill">⏱ {p["min"]} мин чтения</span><span class="pill">✍ Редакция BeBest</span></div>')}
<section class="section section--paper"><div class="container"><article class="article">{"".join(secs)}
<div class="card" style="margin-top:50px;display:grid;gap:16px;background:var(--ink);color:var(--paper)" data-reveal="up"><h3 class="h-m">Хотите применить это на практике?</h3><p class="muted">Запишитесь на бесплатный пробный урок — преподаватель составит план под вашу цель.</p>{trial_btn("Пробный урок бесплатно")}</div>
</article></div></section>
<section class="section"><div class="container"><div class="section-head"><h2 class="h-m" data-reveal="up">Читайте также</h2></div><div class="grid grid-3" data-stagger>{others}</div></div></section>
'''
        page(f"blog/{p['slug']}.html", p["title"] + " — блог BeBest", p["intro"], pbody, "school")

# =================================================================== VACANCIES
def build_vacancies():
    def body(root):
        langs = ["английского", "немецкого", "испанского", "итальянского", "французского", "португальского"]
        vac = "".join(f'''<a class="lang-row" href="mailto:{EMAIL_HR}?subject=Вакансия: преподаватель {l} языка" data-reveal="up" style="--d:{i*0.05:.2f}s"><span class="feature__icon" style="width:54px;height:54px">{icon('grad')}</span><div><b>Преподаватель {l} языка</b><small>Онлайн · гибкий график · удалённо</small></div><span class="course-card__arrow">{icon('arrow')}</span></a>''' for i, l in enumerate(langs))
        return f'''{page_hero(root, "Присоединяйся к команде <span class='accent-lime'>BeBest!</span>", "Ищем преподавателей, которые любят свой язык и людей. Работайте онлайн из любой точки мира с дружной командой.", [("Вакансии", None)])}
{marquee_tape(["Ищем преподавателей!", "Удалённо", "Гибкий график", "Дружная команда", "Рост и обучение"], "", "0.8")}
<section class="section"><div class="container grid grid-2" style="gap:clamp(40px,6vw,100px);align-items:start">
  <div class="flex" style="flex-direction:column;gap:22px"><span class="eyebrow" data-reveal="up">Открытые позиции</span><h2 class="h-l" data-split>Кого мы ищем</h2><p class="lead" data-reveal="up">Отправьте резюме в HR-отдел — нажмите на вакансию, и письмо создастся автоматически.</p>{btn(EMAIL_HR, "mailto:" + EMAIL_HR, "btn--ghost", "", "mail")}</div>
  <div class="lang-list">{vac}</div>
</div></section>
<section class="section section--paper"><div class="container">
  <div class="section-head section-head--center"><span class="eyebrow" data-reveal="up">Почему BeBest</span><h2 class="h-l" data-split>Что мы предлагаем</h2></div>
  <div class="grid grid-4" data-stagger>
    <div class="card feature"><div class="feature__icon">{icon('globe')}</div><div><h3 class="feature__title">Удалённо</h3><p class="feature__text mt-s">Работайте из любой страны — нужен только интернет.</p></div></div>
    <div class="card feature"><div class="feature__icon">{icon('calendar')}</div><div><h3 class="feature__title">Свой график</h3><p class="feature__text mt-s">Уроки идут круглосуточно — выбирайте удобные слоты.</p></div></div>
    <div class="card feature"><div class="feature__icon">{icon('platform')}</div><div><h3 class="feature__title">Готовая платформа</h3><p class="feature__text mt-s">Собственная LMS и материалы — фокус на уроке.</p></div></div>
    <div class="card feature"><div class="feature__icon">{icon('rocket')}</div><div><h3 class="feature__title">Рост</h3><p class="feature__text mt-s">Квалификация каждые полгода и поддержка методистов.</p></div></div>
  </div>
</div></section>
'''
    page("vacancies.html", "Вакансии — работа преподавателем в BeBest", "Ищем преподавателей немецкого, испанского, итальянского, французского, английского и португальского языков.", body, "school")

# =================================================================== LEGAL
LEGAL = {
    "terms": ("Публичное соглашение (оферта)", "Условия оказания образовательных услуг онлайн-школой BeBest.",
              [("Общие положения", "Настоящий документ является публичной офертой ИП BeBest об оказании услуг по обучению иностранным языкам в онлайн-формате. Оплата услуг означает полное и безоговорочное принятие условий оферты."),
               ("Предмет соглашения", "Школа оказывает услуги по проведению онлайн-занятий в индивидуальном или групповом формате согласно выбранному тарифу. Первый пробный урок предоставляется бесплатно."),
               ("Порядок оказания услуг", "Занятия проводятся на онлайн-платформе школы по согласованному расписанию. Индивидуальное занятие длится 50 минут, групповое — 90 минут."),
               ("Стоимость и оплата", "Стоимость определяется действующими тарифами, опубликованными на странице «Стоимость». Оплата производится по реквизитам, указанным на странице «Контакты»."),
               ("Перенос и отмена занятий", "Условия переноса, отмены и возврата средств определяются действующей редакцией оферты. Уточняйте актуальные условия у менеджера."),
               ("Реквизиты", "ИП BeBest, Казахстан, Алматы, пр. Назарбаева 247, офис 6. БИН (ИИН) 861114050167. АО «Kaspi Bank», БИК CASPKZKA, счёт KZ09722S000043226663.")]),
    "privacy": ("Политика конфиденциальности", "Как BeBest обрабатывает и защищает персональные данные.",
                [("Какие данные мы собираем", "Имя, номер телефона, адрес электронной почты и сведения о выбранном курсе, которые вы указываете в форме заявки."),
                 ("Зачем мы их используем", "Чтобы связаться с вами, организовать пробный урок, подобрать преподавателя и оказывать образовательные услуги."),
                 ("Передача третьим лицам", "Мы не продаём и не передаём персональные данные третьим лицам, кроме случаев, предусмотренных законодательством."),
                 ("Ваши права", f"Вы можете запросить изменение или удаление своих данных, написав на {EMAIL}.")]),
    "cookies": ("Cookies Policy", "Политика использования файлов cookie на сайте BeBest.",
                [("Что такое cookies", "Небольшие файлы, которые сайт сохраняет в браузере для корректной работы и аналитики."),
                 ("Как мы их используем", "Для запоминания настроек, анализа посещаемости и улучшения сайта."),
                 ("Управление cookies", "Вы можете отключить cookies в настройках браузера — сайт продолжит работать, но некоторые функции могут быть ограничены.")]),
    "legal": ("Legal notice", "Правовая информация о владельце сайта.",
              [("Владелец сайта", "ИП BeBest, Республика Казахстан, г. Алматы, пр. Назарбаева 247, офис 6. БИН (ИИН) 861114050167."),
               ("Контакты", f"Телефон: {PHONE_H}. Email: {EMAIL}."),
               ("Интеллектуальная собственность", "Материалы сайта принадлежат BeBest и не могут использоваться без письменного разрешения.")]),
}

def build_legal():
    for slug, (title, desc, secs) in LEGAL.items():
        def body(root, title=title, secs=secs):
            s = "".join(f'<h2 data-reveal="up">{i+1}. {h}</h2><p data-reveal="up">{t}</p>' for i, (h, t) in enumerate(secs))
            return f'''{page_hero(root, title, "", [(title, None)], blobs=False)}
<section class="section section--paper"><div class="container"><div class="legal">
<p class="pill" style="margin-bottom:20px">ℹ️ Сокращённая редакция. Полный юридический текст переносится из действующей версии документа.</p>{s}</div></div></section>'''
        page(f"{slug}.html", f"{title} — BeBest", desc, body)

# =================================================================== TEST
def build_test():
    def body(root):
        chips = "".join(f'<button class="chip" type="button" data-test-lang="{code}">{LANG[k]["name"]}</button>' for k, code in TEST_LANG.items())
        return f'''{page_hero(root, "Тест на знание <span class='accent-lime' data-test-name>английского</span>", "Ответьте на несколько вопросов и узнайте свой уровень по шкале CEFR — от A1 до C1. Можно отвечать клавишами 1–4.", [("Тест уровня", None)])}
<section class="section section--paper"><div class="container">
  <div class="test-langs chips">{chips}</div>
  <div class="test" data-test data-root="{root}">
    <div class="test__play">
      <div class="test__head"><div class="test__progress"><i></i></div><span class="test__count">1 / 12</span></div>
      <div class="test__q"></div>
      <div class="test__options"></div>
    </div>
    <div class="test__result" hidden></div>
  </div>
</div></section>
{cta_block(root, "Результат — это только начало", "На бесплатном пробном уроке преподаватель уточнит уровень и составит план обучения.")}
'''
    page("test.html", "Тест на знание языка онлайн — BeBest", "Бесплатный онлайн-тест на знание английского, немецкого, испанского, итальянского и французского языков.", body, "test", scripts=("test.js",))

# =================================================================== EXERCISES (flip cards)
def build_exercises():
    PH = [("Как дела?", "How are you?", "gb"), ("Приятно познакомиться", "Freut mich!", "de"), ("Сколько стоит?", "¿Cuánto cuesta?", "es"),
          ("Счёт, пожалуйста", "Il conto, per favore", "it"), ("Я не понимаю", "Je ne comprends pas", "fr"), ("Доброе утро", "Bom dia", "pt"),
          ("Спасибо большое", "Dziękuję bardzo", "pl"), ("Где метро?", "Where is the subway?", "gb"), ("Я учу немецкий", "Ich lerne Deutsch", "de"),
          ("Мне нравится", "Me gusta", "es"), ("Увидимся завтра", "A domani!", "it"), ("С удовольствием", "Avec plaisir", "fr")]
    def body(root):
        cards = "".join(f'''<button class="flip" type="button" data-cursor="Переверни" aria-label="Перевернуть карточку">
  <span class="flip__inner"><span class="flip__face"><img src="{root}assets/img/flags/{f}.svg" alt=""><b>{ru}</b><small>Нажмите, чтобы перевернуть</small></span>
  <span class="flip__face flip__back"><img src="{root}assets/img/flags/{f}.svg" alt=""><b>{tr}</b><small>{ru}</small></span></span></button>''' for ru, tr, f in PH)
        return f'''<style>
.flip{{perspective:1000px;aspect-ratio:1/1.1;width:100%;text-align:left}}
.flip__inner{{position:relative;display:block;width:100%;height:100%;transform-style:preserve-3d;transition:transform .9s var(--ease-out)}}
.flip.is-flipped .flip__inner{{transform:rotateY(180deg)}}
.flip__face{{position:absolute;inset:0;backface-visibility:hidden;-webkit-backface-visibility:hidden;border-radius:var(--radius);padding:26px;display:flex;flex-direction:column;justify-content:space-between;background:var(--white);color:var(--ink);border:1px solid var(--line-ink)}}
.flip__face img{{width:44px;height:44px;border-radius:50%}}
.flip__face b{{font-family:var(--font-display);font-size:clamp(20px,2vw,28px);letter-spacing:-.02em;line-height:1.1}}
.flip__face small{{color:var(--muted-ink);font-size:13px}}
.flip__back{{transform:rotateY(180deg);background:var(--violet);color:#fff;border-color:var(--violet)}}
.flip__back small{{color:rgba(255,255,255,.75)}}
.flip:hover .flip__face:not(.flip__back){{border-color:var(--violet)}}
</style>
{page_hero(root, "Упражнения: <span class='accent-lime'>тренажёр фраз</span>", "Переворачивайте карточки и запоминайте полезные фразы на 7 языках. Пять минут в день — и словарный запас растёт сам.", [("Упражнения", None)])}
<section class="section section--paper"><div class="container">
  <div class="flex between center wrap gap" style="margin-bottom:30px"><h2 class="h-m" data-reveal="up">Карточки дня</h2><button class="btn btn--violet" type="button" id="flip-all"><span class="btn__text"><span>Перевернуть все</span><span>Перевернуть все</span></span><span class="btn__icon">{icon('spark')}</span></button></div>
  <div class="grid grid-4" data-stagger>{cards}</div>
</div></section>
{cta_block(root, "Хотите больше практики?", "Разговорные клубы и уроки с преподавателем — лучший тренажёр. Первый урок бесплатно.")}
<script>
document.querySelectorAll('.flip').forEach(function(f){{f.addEventListener('click',function(){{f.classList.toggle('is-flipped')}})}});
document.getElementById('flip-all').addEventListener('click',function(){{var c=document.querySelectorAll('.flip');var any=[].some.call(c,function(x){{return !x.classList.contains('is-flipped')}});c.forEach(function(x,i){{setTimeout(function(){{x.classList.toggle('is-flipped',any)}},i*60)}})}});
</script>
'''
    page("exercises.html", "Упражнения — тренажёр фраз на иностранных языках | BeBest", "Интерактивные карточки с полезными фразами на английском, немецком, испанском, итальянском, французском, португальском и польском.", body, "school")

# =================================================================== 404
def build_404():
    def body(root):
        return f'''<section class="notfound"><div class="flex" style="flex-direction:column;gap:26px;align-items:center">
  <div class="notfound__num"><span>4</span><span>0</span><span>4</span></div>
  <h1 class="h-m">Oops! Page not found · Seite nicht gefunden · Página no encontrada</h1>
  <p class="lead">Такой страницы нет, но есть много интересного на главной.</p>
  <div class="flex wrap gap" style="justify-content:center">{btn("На главную", root + "index.html")}{btn("Каталог курсов", root + "courses.html", "btn--ghost")}</div>
</div></section>'''
    page("404.html", "Страница не найдена — BeBest", "Страница не найдена.", body)
