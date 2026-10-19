# -*- coding: utf-8 -*-
"""Generate the full BeBest static site.  Usage:  python3 _build/build.py"""
import os
from layout import FLAGS, flag_svg, LOGO_MARK
from data import LANGS, COURSES
import pages as P

def assets():
    fdir = os.path.join(P.OUT, "assets", "img", "flags")
    os.makedirs(fdir, exist_ok=True)
    for code in FLAGS:
        with open(os.path.join(fdir, f"{code}.svg"), "w", encoding="utf-8") as f:
            f.write(flag_svg(code))
    img = os.path.join(P.OUT, "assets", "img")
    fav = LOGO_MARK.replace('class="logo__mark" ', 'xmlns="http://www.w3.org/2000/svg" ').replace('<g class="spin">', '<g>')
    with open(os.path.join(img, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(fav)
    og = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630"><rect width="1200" height="630" fill="#0d0b1f"/>'
          '<circle cx="1050" cy="80" r="260" fill="#6b4eff" opacity=".55"/><circle cx="120" cy="600" r="200" fill="#d7ff3d" opacity=".25"/>'
          '<text x="80" y="300" font-family="Arial Black, sans-serif" font-size="120" font-weight="900" fill="#f5f1e8">Be<tspan fill="#d7ff3d">Best</tspan></text>'
          '<text x="84" y="390" font-family="Arial, sans-serif" font-size="40" fill="#f5f1e8" opacity=".8">Онлайн-школа иностранных языков</text>'
          '<text x="84" y="460" font-family="Arial, sans-serif" font-size="32" fill="#d7ff3d">Первый урок — бесплатно</text></svg>')
    with open(os.path.join(img, "og.svg"), "w", encoding="utf-8") as f:
        f.write(og)

def main():
    assets()
    P.build_index()
    P.build_catalog()
    for L in LANGS:
        P.build_lang(L)
    for c in COURSES:
        P.build_course(c)
    P.build_about()
    P.build_teachers()
    P.build_price()
    P.build_faq()
    P.build_contact()
    P.build_blog()
    P.build_vacancies()
    P.build_legal()
    P.build_test()
    P.build_exercises()
    P.build_404()
    n = sum(len([f for f in fs if f.endswith(".html")]) for d, _, fs in os.walk(P.OUT) if "_build" not in d)
    print("HTML pages:", n)

if __name__ == "__main__":
    main()
