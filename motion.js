/* =========================================================
   BeBest School — motion.js
   Scroll reveals, split text, counters, marquees, parallax,
   horizontal scroll, word-by-word statements, scramble…
   ========================================================= */
(function () {
  "use strict";
  const BB = window.BB || {};
  const reduce = !!BB.reduce;
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));

  /* ---------- Split text into words (keeps inner HTML like <span class>) ---------- */
  function splitWords(el) {
    if (el.dataset.splitDone) return;
    el.dataset.splitDone = "1";
    let i = 0;
    const walk = (node) => {
      [...node.childNodes].forEach((child) => {
        if (child.nodeType === 3) {
          const parts = child.textContent.split(/(\s+)/);
          const frag = document.createDocumentFragment();
          parts.forEach((p) => {
            if (!p) return;
            if (/^\s+$/.test(p)) { frag.appendChild(document.createTextNode(" ")); return; }
            const w = document.createElement("span");
            w.className = "w";
            const wi = document.createElement("span");
            wi.className = "wi";
            wi.style.setProperty("--i", i++);
            wi.textContent = p;
            w.appendChild(wi);
            frag.appendChild(w);
          });
          child.replaceWith(frag);
        } else if (child.nodeType === 1 && !child.classList.contains("hero__rotator") && child.tagName !== "BR") {
          walk(child);
        } else if (child.nodeType === 1 && child.classList.contains("hero__rotator")) {
          const w = document.createElement("span");
          w.className = "w";
          const wi = document.createElement("span");
          wi.className = "wi";
          wi.style.setProperty("--i", i++);
          child.replaceWith(w);
          wi.appendChild(child);
          w.appendChild(wi);
        }
      });
    };
    walk(el);
  }
  document.querySelectorAll("[data-split]").forEach(splitWords);

  /* ---------- Statement: word-by-word highlight on scroll ---------- */
  const statements = [...document.querySelectorAll("[data-statement]")];
  statements.forEach((el) => {
    const walk = (node) => {
      [...node.childNodes].forEach((child) => {
        if (child.nodeType === 3) {
          const frag = document.createDocumentFragment();
          child.textContent.split(/(\s+)/).forEach((p) => {
            if (!p) return;
            if (/^\s+$/.test(p)) { frag.appendChild(document.createTextNode(" ")); return; }
            const s = document.createElement("span");
            s.dataset.word = "";
            s.textContent = p;
            frag.appendChild(s);
          });
          child.replaceWith(frag);
        } else if (child.nodeType === 1 && !child.classList.contains("inline-chip")) walk(child);
        else if (child.nodeType === 1) child.dataset.word = "";
      });
    };
    walk(el);
    el._words = [...el.querySelectorAll("[data-word]")];
  });

  /* ---------- Reveal on intersection ---------- */
  function initReveal() {
    const targets = document.querySelectorAll("[data-reveal], [data-split], [data-stagger], .draw-line, [data-count], .skills, .bento-meter, .tl-item");
    if (reduce || !("IntersectionObserver" in window)) {
      targets.forEach((t) => { t.classList.add("is-in"); if (t.dataset.count) runCount(t, true); });
      return;
    }
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (!en.isIntersecting) return;
        const t = en.target;
        t.classList.add("is-in");
        if (t.dataset.count !== undefined) runCount(t);
        io.unobserve(t);
      });
    }, { threshold: 0.15, rootMargin: "0px 0px -6% 0px" });
    targets.forEach((t) => io.observe(t));
  }

  /* ---------- Counters ---------- */
  function runCount(el, instant) {
    const end = parseFloat(el.dataset.count);
    const dec = (el.dataset.count.split(".")[1] || "").length;
    const suffix = el.dataset.suffix || "";
    const prefix = el.dataset.prefix || "";
    const fmt = (v) => prefix + v.toLocaleString("ru-RU", { minimumFractionDigits: dec, maximumFractionDigits: dec }) + suffix;
    if (instant) { el.textContent = fmt(end); return; }
    const dur = parseFloat(el.dataset.duration) || 2200;
    const t0 = performance.now();
    const step = (now) => {
      const p = clamp((now - t0) / dur, 0, 1);
      const e = 1 - Math.pow(1 - p, 4);
      el.textContent = fmt(end * e);
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }

  /* ---------- Hero word rotator ---------- */
  function initRotators() {
    document.querySelectorAll(".hero__rotator").forEach((rot) => {
      const items = [...rot.children];
      if (items.length < 2) return;
      let idx = 0;
      items[0].classList.add("is-current");
      // size the grid to the widest word to avoid layout jumps
      setInterval(() => {
        const cur = items[idx];
        idx = (idx + 1) % items.length;
        const next = items[idx];
        cur.classList.remove("is-current");
        cur.classList.add("is-leaving");
        next.classList.remove("is-leaving");
        void next.offsetWidth;
        next.classList.add("is-current");
        setTimeout(() => cur.classList.remove("is-leaving"), 1000);
      }, 2200);
    });
  }

  /* ---------- Marquees with scroll-velocity boost ---------- */
  const marquees = [];
  document.querySelectorAll(".marquee").forEach((m) => {
    const track = m.querySelector(".marquee__track");
    const group = m.querySelector(".marquee__group");
    if (!track || !group) return;
    // clone enough groups to fill
    for (let i = 0; i < 3; i++) track.appendChild(group.cloneNode(true));
    marquees.push({ el: m, track, group, x: 0, dir: m.dataset.dir === "right" ? 1 : -1, speed: parseFloat(m.dataset.mspeed) || 0.6 });
  });

  let velocity = 0, lastScroll = window.scrollY;
  window.addEventListener("scroll", () => {
    const y = window.scrollY;
    velocity = clamp(y - lastScroll, -60, 60);
    lastScroll = y;
  }, { passive: true });

  /* ---------- Parallax targets ---------- */
  const parallax = [...document.querySelectorAll("[data-speed]")];
  const bands = [...document.querySelectorAll(".course-band__word")];
  const footerBig = document.querySelector(".footer__big");

  /* ---------- Horizontal scroll section ---------- */
  const hscrolls = [...document.querySelectorAll(".hscroll")].map((sec) => {
    const track = sec.querySelector(".hscroll__track");
    const bar = sec.querySelector(".hscroll__bar i");
    const o = { sec, track, bar, dist: 0 };
    const size = () => {
      if (window.innerWidth <= 860) { sec.style.height = ""; o.dist = 0; track.style.transform = ""; return; }
      o.dist = Math.max(0, track.scrollWidth - window.innerWidth);
      sec.style.height = window.innerHeight + o.dist + "px";
    };
    size();
    window.addEventListener("resize", size);
    window.addEventListener("load", size);
    return o;
  });

  /* ---------- Orbiting language flags (labels stay upright) ---------- */
  const orbits = [...document.querySelectorAll(".orbit__ring[data-spin]")].map((ring) => ({
    ring, spin: parseFloat(ring.dataset.spin), items: [...ring.querySelectorAll(".orbit__item")].map((el) => ({ el, a: parseFloat(el.dataset.a) }))
  }));
  let orbitT = 0, orbitPaused = false;
  document.querySelectorAll(".orbit").forEach((o) => {
    o.addEventListener("mouseenter", () => (orbitPaused = true));
    o.addEventListener("mouseleave", () => (orbitPaused = false));
  });

  /* ---------- Timeline fill ---------- */
  const timelines = [...document.querySelectorAll(".timeline")];

  /* ---------- Main loop ---------- */
  let skew = 0;
  function frame() {
    velocity *= 0.9;
    const vh = window.innerHeight;

    marquees.forEach((m) => {
      const boost = 1 + Math.abs(velocity) * 0.12;
      const scrollDir = velocity < -1 ? -1 : 1; // scrolling up reverses the tape
      m.x += m.speed * boost * m.dir * scrollDir;
      const w = m.group.offsetWidth;
      if (w) {
        if (m.x <= -w) m.x += w;
        if (m.x > 0) m.x -= w;
      }
      m.track.style.transform = `translate3d(${m.x}px,0,0)`;
    });

    skew += (velocity * 0.15 - skew) * 0.15;
    document.querySelectorAll("[data-skew]").forEach((el) => { el.style.transform = `skewY(${clamp(skew, -6, 6)}deg)`; });

    parallax.forEach((el) => {
      const r = el.getBoundingClientRect();
      if (r.bottom < -200 || r.top > vh + 200) return;
      const speed = parseFloat(el.dataset.speed);
      const center = r.top + r.height / 2 - vh / 2;
      el.style.translate = `0 ${(-center * speed).toFixed(1)}px`;
    });

    bands.forEach((el) => {
      const r = el.parentElement.getBoundingClientRect();
      if (r.bottom < 0 || r.top > vh) return;
      const p = (vh - r.top) / (vh + r.height);
      el.style.transform = `translate(${(-p * 40 + 5).toFixed(2)}%, -50%)`;
    });

    hscrolls.forEach((o) => {
      if (!o.dist) return;
      const r = o.sec.getBoundingClientRect();
      const p = clamp(-r.top / o.dist, 0, 1);
      o.track.style.transform = `translate3d(${-p * o.dist}px,0,0)`;
      if (o.bar) o.bar.style.transform = `scaleX(${p})`;
    });

    statements.forEach((el) => {
      const r = el.getBoundingClientRect();
      if (r.bottom < 0 || r.top > vh) return;
      const p = clamp((vh * 0.85 - r.top) / (r.height + vh * 0.35), 0, 1);
      const n = Math.floor(p * el._words.length * 1.05);
      el._words.forEach((w, i) => w.classList.toggle("on", i < n));
    });

    if (!orbitPaused) orbitT += 1 / 60;
    orbits.forEach((o) => {
      o.items.forEach((it) => {
        const a = it.a + orbitT * o.spin;
        it.el.style.left = 50 + 50 * Math.cos(a) + "%";
        it.el.style.top = 50 + 50 * Math.sin(a) + "%";
      });
    });

    timelines.forEach((tl) => {
      const fill = tl.querySelector(".timeline__fill");
      if (!fill) return;
      const r = tl.getBoundingClientRect();
      const p = clamp((vh * 0.6 - r.top) / r.height, 0, 1);
      fill.style.height = p * (r.height - 20) + "px";
    });

    requestAnimationFrame(frame);
  }

  /* ---------- Text scramble on hover ---------- */
  const glyphs = "ABCDEFGHÄÖÜÉÈÑÇßŁŻЖЯ#%&*@0123456789";
  document.querySelectorAll("[data-scramble]").forEach((el) => {
    const original = el.textContent;
    let raf = null;
    el.addEventListener("mouseenter", () => {
      if (reduce) return;
      let frameN = 0;
      cancelAnimationFrame(raf);
      const run = () => {
        const reveal = frameN / 2;
        el.textContent = original.split("").map((ch, i) => {
          if (ch === " ") return " ";
          return i < reveal ? original[i] : glyphs[Math.floor(Math.random() * glyphs.length)];
        }).join("");
        frameN++;
        if (reveal < original.length) raf = requestAnimationFrame(run);
        else el.textContent = original;
      };
      run();
    });
  });

  /* ---------- Footer giant word: letters jump on hover ---------- */
  if (footerBig && !footerBig.dataset.done) {
    footerBig.dataset.done = "1";
    const txt = footerBig.textContent.trim();
    footerBig.innerHTML = txt.split("").map((c) => `<span>${c === " " ? "&nbsp;" : c}</span>`).join("");
    footerBig.querySelectorAll("span").forEach((s) => {
      s.addEventListener("mouseenter", () => {
        s.style.transform = "translateY(-18%) rotate(-8deg)";
        setTimeout(() => (s.style.transform = ""), 600);
      });
    });
  }

  /* ---------- Boot ---------- */
  const start = () => {
    initReveal();
    initRotators();
    if (!reduce) requestAnimationFrame(frame);
    else marquees.forEach((m) => (m.track.style.transform = "none"));
  };
  if (document.documentElement.classList.contains("is-ready")) start();
  else window.addEventListener("bb:ready", start, { once: true });
})();
