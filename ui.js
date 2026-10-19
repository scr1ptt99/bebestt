/* =========================================================
   BeBest School — ui.js
   Accordion, filters, slider, modal + multi-step lead form,
   live clock, copy-to-clipboard, reading progress
   ========================================================= */
(function () {
  "use strict";
  const BB = window.BB || {};
  const WA_NUMBER = "34611586216"; // WhatsApp отдела продаж (как на текущем сайте)

  /* ---------- Accordion ---------- */
  document.querySelectorAll(".acc__head").forEach((head) => {
    head.addEventListener("click", () => {
      const acc = head.closest(".acc");
      const group = acc.closest(".accordion");
      const open = !acc.classList.contains("is-open");
      if (group && group.dataset.single !== undefined) {
        group.querySelectorAll(".acc.is-open").forEach((a) => {
          a.classList.remove("is-open");
          a.querySelector(".acc__head").setAttribute("aria-expanded", "false");
        });
      }
      acc.classList.toggle("is-open", open);
      head.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });

  /* ---------- Filters (teachers, catalog, blog) with FLIP ---------- */
  document.querySelectorAll("[data-filter-group]").forEach((group) => {
    const target = document.querySelector(group.dataset.filterGroup);
    if (!target) return;
    const items = [...target.children];
    const chips = group.querySelectorAll("[data-filter]");
    const counter = document.querySelector(group.dataset.counter || "#none");

    function apply(val) {
      const first = new Map(items.map((it) => [it, it.getBoundingClientRect()]));
      let shown = 0;
      items.forEach((it) => {
        const tags = (it.dataset.tags || "").split(" ");
        const show = val === "all" || tags.includes(val);
        it.classList.toggle("is-hidden", !show);
        if (show) shown++;
      });
      if (counter) counter.textContent = shown;
      if (BB.reduce) return;
      items.forEach((it) => {
        if (it.classList.contains("is-hidden")) return;
        const a = first.get(it);
        const b = it.getBoundingClientRect();
        if (!a || a.width === 0) {
          it.animate([{ opacity: 0, transform: "scale(.9)" }, { opacity: 1, transform: "none" }], { duration: 600, easing: "cubic-bezier(.16,1,.3,1)" });
          return;
        }
        const dx = a.left - b.left, dy = a.top - b.top;
        if (dx || dy) it.animate([{ transform: `translate(${dx}px,${dy}px)` }, { transform: "none" }], { duration: 700, easing: "cubic-bezier(.16,1,.3,1)" });
      });
    }
    chips.forEach((chip) => chip.addEventListener("click", () => {
      chips.forEach((c) => c.classList.toggle("is-active", c === chip));
      apply(chip.dataset.filter);
    }));
    // deep link: ?lang=german
    const q = new URLSearchParams(location.search).get(group.dataset.param || "filter");
    if (q) { const c = group.querySelector(`[data-filter="${q}"]`); if (c) c.click(); }
  });

  /* ---------- Teacher bio expand ---------- */
  document.querySelectorAll(".teacher__more").forEach((btn) => {
    btn.addEventListener("click", () => {
      const card = btn.closest(".teacher");
      const exp = card.classList.toggle("is-expanded");
      btn.textContent = exp ? "Свернуть" : "Читать полностью";
    });
  });

  /* ---------- Draggable slider ---------- */
  document.querySelectorAll(".slider").forEach((slider) => {
    const vp = slider.querySelector(".slider__viewport");
    const track = slider.querySelector(".slider__track");
    const slides = [...track.children];
    const scope = slider.closest("section") || slider;
    const prev = scope.querySelector("[data-prev]");
    const next = scope.querySelector("[data-next]");
    const bar = slider.querySelector(".slider__progress i");
    let x = 0, target = 0, dragging = false, startX = 0, startT = 0, moved = 0;

    const maxX = () => Math.max(0, track.scrollWidth - vp.clientWidth);
    const stepW = () => (slides[0]?.getBoundingClientRect().width || 400) + 24;
    const clampT = () => { target = Math.max(-maxX(), Math.min(0, target)); };

    function render() {
      x += (target - x) * 0.12;
      track.style.transform = `translate3d(${x}px,0,0)`;
      if (bar) bar.style.width = (maxX() ? (-x / maxX()) * 100 : 100) + "%";
      requestAnimationFrame(render);
    }
    render();

    vp.addEventListener("pointerdown", (e) => {
      dragging = true; moved = 0; startX = e.clientX; startT = target;
      vp.classList.add("is-dragging");
      vp.setPointerCapture(e.pointerId);
    });
    vp.addEventListener("pointermove", (e) => {
      if (!dragging) return;
      moved = e.clientX - startX;
      target = startT + moved * 1.2;
    });
    const end = () => {
      if (!dragging) return;
      dragging = false; vp.classList.remove("is-dragging");
      const s = stepW();
      target = Math.round(target / s) * s;
      clampT();
    };
    vp.addEventListener("pointerup", end);
    vp.addEventListener("pointercancel", end);
    vp.addEventListener("click", (e) => { if (Math.abs(moved) > 6) e.preventDefault(); }, true);

    prev && prev.addEventListener("click", () => { target += stepW(); clampT(); });
    next && next.addEventListener("click", () => { target -= stepW(); if (target < -maxX() - 5) target = 0; clampT(); });

    let auto = setInterval(() => { if (!dragging) { target -= stepW(); if (target < -maxX() - 5) target = 0; clampT(); } }, 5000);
    slider.addEventListener("mouseenter", () => clearInterval(auto));
    slider.addEventListener("mouseleave", () => { clearInterval(auto); auto = setInterval(() => { target -= stepW(); if (target < -maxX() - 5) target = 0; clampT(); }, 5000); });
  });

  /* ---------- Modal ---------- */
  const modal = document.querySelector("#lead-modal");
  let lastFocus = null;
  function openModal(course) {
    if (!modal) return;
    lastFocus = document.activeElement;
    modal.classList.add("is-open");
    modal.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    const form = modal.querySelector("form");
    resetSteps(form);
    if (course) {
      const ci = form.querySelector("[name=course]");
      if (ci) ci.value = course;
      const langVal = (course.match(/английск|немецк|испанск|итальянск|французск|португальск|польск|математ/i) || [""])[0].toLowerCase();
      const map = { "английск": "Английский", "немецк": "Немецкий", "испанск": "Испанский", "итальянск": "Итальянский", "французск": "Французский", "португальск": "Португальский", "польск": "Польский", "математ": "Математика" };
      const want = map[langVal];
      if (want) form.querySelectorAll("[name=lang]").forEach((r) => { r.checked = r.value === want; });
    }
    setTimeout(() => modal.querySelector(".modal__close")?.focus(), 400);
  }
  function closeModal() {
    if (!modal) return;
    modal.classList.remove("is-open");
    modal.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    lastFocus && lastFocus.focus && lastFocus.focus();
  }
  BB.openModal = openModal;
  document.addEventListener("click", (e) => {
    const t = e.target.closest("[data-modal-open]");
    if (t) { e.preventDefault(); openModal(t.dataset.course || ""); }
    if (e.target.closest("[data-modal-close]")) closeModal();
  });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape" && modal?.classList.contains("is-open")) closeModal(); });
  if (location.hash === "#trial") setTimeout(() => openModal(""), 1600);

  /* ---------- Multi-step lead form ---------- */
  function resetSteps(form) {
    if (!form) return;
    form.querySelectorAll(".form-step").forEach((s, i) => s.classList.toggle("is-active", i === 0));
    form.querySelectorAll(".steps-dots i").forEach((d, i) => d.classList.toggle("is-done", i === 0));
    const ok = form.querySelector(".form-success");
    if (ok) ok.classList.remove("is-active");
  }
  function validPhone(v) { return v.replace(/\D/g, "").length >= 10; }

  function buildMessage(form) {
    const fd = new FormData(form);
    const lines = ["Здравствуйте! Хочу записаться на бесплатный пробный урок в BeBest."];
    const add = (label, key) => { const v = (fd.get(key) || "").toString().trim(); if (v) lines.push(`${label}: ${v}`); };
    add("Имя", "name"); add("Телефон", "phone"); add("Язык", "lang"); add("Для кого", "who");
    add("Формат", "format"); add("Уровень", "level"); add("Курс", "course"); add("Комментарий", "comment");
    return lines.join("\n");
  }

  document.querySelectorAll(".js-lead-form").forEach((form) => {
    const steps = [...form.querySelectorAll(".form-step")];
    const dots = [...form.querySelectorAll(".steps-dots i")];
    const go = (i) => {
      steps.forEach((s, k) => s.classList.toggle("is-active", k === i));
      dots.forEach((d, k) => d.classList.toggle("is-done", k <= i));
    };
    form.querySelectorAll("[data-next-step]").forEach((b) => b.addEventListener("click", () => {
      const cur = steps.findIndex((s) => s.classList.contains("is-active"));
      go(Math.min(cur + 1, steps.length - 1));
    }));
    form.querySelectorAll("[data-prev-step]").forEach((b) => b.addEventListener("click", () => {
      const cur = steps.findIndex((s) => s.classList.contains("is-active"));
      go(Math.max(cur - 1, 0));
    }));
    // auto-advance after picking a tile on step 1/2
    form.querySelectorAll(".form-step [data-auto] input").forEach((inp) => inp.addEventListener("change", () => {
      const cur = steps.findIndex((s) => s.classList.contains("is-active"));
      setTimeout(() => go(Math.min(cur + 1, steps.length - 1)), 280);
    }));

    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const name = form.querySelector("[name=name]");
      const phone = form.querySelector("[name=phone]");
      let ok = true;
      [name, phone].forEach((f) => f && f.closest(".field").classList.remove("is-error"));
      if (name && name.value.trim().length < 2) { name.closest(".field").classList.add("is-error"); ok = false; }
      if (phone && !validPhone(phone.value)) { phone.closest(".field").classList.add("is-error"); ok = false; }
      if (!ok) { BB.toast && BB.toast("Проверьте имя и телефон"); return; }

      const msg = buildMessage(form);
      const url = `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(msg)}`;
      const success = form.querySelector(".form-success");
      if (success) {
        steps.forEach((s) => s.classList.remove("is-active"));
        success.classList.add("is-active");
        const wa = success.querySelector("[data-wa]");
        if (wa) wa.href = url;
      } else {
        BB.toast && BB.toast("Спасибо! Открываем WhatsApp…");
      }
      confetti(form);
      setTimeout(() => window.open(url, "_blank", "noopener"), success ? 1400 : 600);
      try { localStorage.setItem("bb-lead", JSON.stringify({ name: name?.value, t: Date.now() })); } catch (err) {}
    });
  });

  /* Phone mask (+7 7xx xxx xx xx) */
  document.querySelectorAll("input[type=tel]").forEach((inp) => {
    inp.addEventListener("input", () => {
      let d = inp.value.replace(/\D/g, "");
      if (!d) { inp.value = ""; return; }
      if (d[0] === "8") d = "7" + d.slice(1);
      if (d[0] !== "7") { inp.value = "+" + d.slice(0, 15); return; }
      const p = [d.slice(1, 4), d.slice(4, 7), d.slice(7, 9), d.slice(9, 11)];
      inp.value = "+7" + (p[0] ? " " + p[0] : "") + (p[1] ? " " + p[1] : "") + (p[2] ? " " + p[2] : "") + (p[3] ? " " + p[3] : "");
    });
  });

  /* ---------- Confetti burst (DOM, no libs) ---------- */
  function confetti(anchor) {
    if (BB.reduce) return;
    const r = anchor.getBoundingClientRect();
    const colors = ["#d7ff3d", "#6b4eff", "#ff6b4a", "#4fd1ff", "#ff5fa2", "#f5f1e8"];
    for (let i = 0; i < 90; i++) {
      const p = document.createElement("i");
      const size = 6 + Math.random() * 8;
      p.style.cssText = `position:fixed;z-index:9700;left:${r.left + r.width / 2}px;top:${r.top + r.height / 3}px;width:${size}px;height:${size * (Math.random() > .5 ? 1 : .4)}px;background:${colors[i % colors.length]};border-radius:${Math.random() > .5 ? "50%" : "2px"};pointer-events:none`;
      document.body.appendChild(p);
      const ang = Math.random() * Math.PI * 2;
      const dist = 160 + Math.random() * 380;
      p.animate([
        { transform: "translate(0,0) rotate(0)", opacity: 1 },
        { transform: `translate(${Math.cos(ang) * dist}px, ${Math.sin(ang) * dist - 120}px) rotate(${Math.random() * 720}deg)`, opacity: 1, offset: 0.6 },
        { transform: `translate(${Math.cos(ang) * dist * 1.1}px, ${Math.sin(ang) * dist + 260}px) rotate(${Math.random() * 1080}deg)`, opacity: 0 }
      ], { duration: 1600 + Math.random() * 900, easing: "cubic-bezier(.16,1,.3,1)" }).onfinish = () => p.remove();
    }
  }
  BB.confetti = confetti;

  /* ---------- Live clock (Almaty) + open status ---------- */
  document.querySelectorAll("[data-clock]").forEach((el) => {
    const status = document.querySelector("[data-open-status]");
    const tick = () => {
      const now = new Date();
      const opts = { timeZone: "Asia/Almaty", hour: "2-digit", minute: "2-digit", second: "2-digit", hour12: false };
      let s;
      try { s = now.toLocaleTimeString("ru-RU", opts); } catch (e) { s = now.toLocaleTimeString("ru-RU"); }
      el.textContent = s;
      if (status) {
        const h = parseInt(s.slice(0, 2), 10);
        const open = h >= 10 && h < 19;
        status.classList.toggle("off", !open);
        status.textContent = open ? "Менеджеры сейчас на связи" : "Менеджеры ответят с 10:00 · уроки идут 24/7";
      }
    };
    tick(); setInterval(tick, 1000);
  });

  /* ---------- Copy to clipboard ---------- */
  document.querySelectorAll("[data-copy]").forEach((el) => {
    el.addEventListener("click", (e) => {
      e.preventDefault();
      const v = el.dataset.copy;
      const done = () => BB.toast && BB.toast("Скопировано: " + v);
      if (navigator.clipboard) navigator.clipboard.writeText(v).then(done, () => { location.href = "mailto:" + v; });
      else location.href = "mailto:" + v;
    });
  });

  /* ---------- Reading progress (blog articles) ---------- */
  const rb = document.querySelector(".reading-bar");
  const art = document.querySelector(".article");
  if (rb && art) {
    window.addEventListener("scroll", () => {
      const r = art.getBoundingClientRect();
      const p = Math.min(1, Math.max(0, -r.top / (r.height - window.innerHeight)));
      rb.style.width = p * 100 + "%";
    }, { passive: true });
  }
})();
