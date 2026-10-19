/* =========================================================
   BeBest School — core.js
   Preloader, page transitions, header, menus, progress, toast
   ========================================================= */
(function () {
  "use strict";

  const BB = (window.BB = window.BB || {});
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  BB.reduce = reduce;

  const store = {
    get(k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } },
    set(k, v) { try { sessionStorage.setItem(k, v); } catch (e) {} },
    del(k) { try { sessionStorage.removeItem(k); } catch (e) {} }
  };
  BB.store = store;

  /* ---------- Toast ---------- */
  BB.toast = function (msg) {
    let t = document.querySelector(".toast");
    if (!t) { t = document.createElement("div"); t.className = "toast"; document.body.appendChild(t); }
    t.textContent = msg;
    t.classList.add("is-show");
    clearTimeout(t._h);
    t._h = setTimeout(() => t.classList.remove("is-show"), 2600);
  };

  /* ---------- Preloader ---------- */
  const pre = document.querySelector(".preloader");
  const fromTransition = store.get("bb-trans") === "1";
  store.del("bb-trans");

  function ready() {
    document.body.classList.remove("is-loading");
    document.documentElement.classList.add("is-ready");
    window.dispatchEvent(new CustomEvent("bb:ready"));
  }

  if (pre) {
    const seen = store.get("bb-seen") === "1";
    if (seen || reduce || fromTransition) {
      pre.remove();
      ready();
    } else {
      store.set("bb-seen", "1");
      document.body.classList.add("is-loading");
      const bar = pre.querySelector(".preloader__bar i");
      const count = pre.querySelector(".preloader__count");
      let p = 0;
      const tick = () => {
        p += Math.max(1, (100 - p) * 0.06);
        if (p > 99.5) p = 100;
        if (bar) bar.style.width = p + "%";
        if (count) count.textContent = String(Math.round(p)).padStart(3, "0");
        if (p < 100) requestAnimationFrame(tick);
        else setTimeout(() => {
          pre.classList.add("is-done");
          setTimeout(ready, 450);
          setTimeout(() => pre.remove(), 1200);
        }, 350);
      };
      setTimeout(() => requestAnimationFrame(tick), 900);
    }
  } else {
    ready();
  }

  /* ---------- Page transition curtain ---------- */
  const curtain = document.querySelector(".curtain");
  if (curtain && fromTransition && !reduce) {
    const bars = curtain.querySelectorAll("i");
    bars.forEach((b) => { b.style.transition = "none"; });
    curtain.classList.add("is-in");
    void curtain.offsetWidth;
    requestAnimationFrame(() => {
      bars.forEach((b) => { b.style.transition = ""; });
      curtain.classList.add("is-out");
      setTimeout(() => curtain.classList.remove("is-in", "is-out"), 1100);
    });
  }

  function isInternal(a) {
    if (!a || !a.href) return false;
    if (a.target && a.target !== "_self") return false;
    if (a.hasAttribute("download") || a.dataset.noTransition !== undefined) return false;
    const href = a.getAttribute("href") || "";
    if (href.startsWith("#") || href.startsWith("mailto:") || href.startsWith("tel:") || href.startsWith("javascript:")) return false;
    if (a.protocol !== location.protocol || a.host !== location.host) return false;
    // same page anchor
    if (a.pathname === location.pathname && a.hash) return false;
    return true;
  }

  document.addEventListener("click", (e) => {
    if (e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;
    const a = e.target.closest("a");
    if (!isInternal(a) || !curtain || reduce) return;
    e.preventDefault();
    store.set("bb-trans", "1");
    curtain.classList.remove("is-out");
    curtain.classList.add("is-in");
    document.body.classList.remove("menu-open");
    setTimeout(() => { window.location.href = a.href; }, 720);
  });

  window.addEventListener("pageshow", (e) => {
    if (e.persisted && curtain) curtain.classList.remove("is-in", "is-out");
  });

  /* ---------- Header: hide on scroll down, solid after hero ---------- */
  const header = document.querySelector(".header");
  const progress = document.querySelector(".progress");
  const toTop = document.querySelector(".to-top");
  let lastY = window.scrollY;
  let ticking = false;

  function onScroll() {
    const y = window.scrollY;
    if (header) {
      header.classList.toggle("is-scrolled", y > 40);
      const goingDown = y > lastY && y > 300;
      if (!document.body.classList.contains("menu-open")) header.classList.toggle("is-hidden", goingDown);
    }
    if (progress) {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      progress.style.transform = "scaleX(" + (max > 0 ? y / max : 0) + ")";
    }
    if (toTop) toTop.classList.toggle("is-visible", y > 900);
    lastY = y;
    ticking = false;
  }
  window.addEventListener("scroll", () => {
    if (!ticking) { requestAnimationFrame(onScroll); ticking = true; }
  }, { passive: true });
  onScroll();

  if (toTop) toTop.addEventListener("click", () => window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" }));

  /* ---------- Mega menu language tabs ---------- */
  document.querySelectorAll(".mega").forEach((mega) => {
    const tabs = mega.querySelectorAll(".mega__lang");
    const panels = mega.querySelectorAll(".mega__panel");
    tabs.forEach((tab) => {
      const activate = () => {
        tabs.forEach((t) => t.classList.toggle("is-active", t === tab));
        panels.forEach((p) => p.classList.toggle("is-active", p.dataset.panel === tab.dataset.tab));
      };
      tab.addEventListener("mouseenter", activate);
      tab.addEventListener("focus", activate);
      tab.addEventListener("click", activate);
    });
  });

  /* ---------- Mobile menu ---------- */
  const burger = document.querySelector(".burger");
  if (burger) {
    burger.addEventListener("click", () => {
      const open = document.body.classList.toggle("menu-open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      if (header) header.classList.remove("is-hidden");
      document.querySelectorAll(".mobile-menu__list > li > a, .mobile-menu__list > li > button").forEach((el, i) => {
        el.style.transitionDelay = open ? 0.25 + i * 0.06 + "s" : "0s";
      });
    });
  }
  document.querySelectorAll("[data-sub-toggle]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const sub = btn.nextElementSibling;
      const open = sub.classList.toggle("is-open");
      btn.querySelector("span").textContent = open ? "−" : "+";
    });
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && document.body.classList.contains("menu-open")) {
      document.body.classList.remove("menu-open");
    }
  });

  /* ---------- Year ---------- */
  document.querySelectorAll("[data-year]").forEach((el) => { el.textContent = new Date().getFullYear(); });
})();
