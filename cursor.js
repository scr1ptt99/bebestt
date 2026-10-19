/* =========================================================
   BeBest School — cursor.js
   Custom cursor, magnetic elements, 3D tilt, card glow
   ========================================================= */
(function () {
  "use strict";
  const BB = window.BB || {};
  const fine = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  if (!fine || BB.reduce) return;

  const lerp = (a, b, n) => a + (b - a) * n;

  /* ---------- Cursor ---------- */
  const cursor = document.createElement("div");
  cursor.className = "cursor";
  cursor.innerHTML = '<span class="cursor__label"></span>';
  const dot = document.createElement("div");
  dot.className = "cursor-dot";
  document.body.append(cursor, dot);
  const label = cursor.querySelector(".cursor__label");

  let mx = window.innerWidth / 2, my = window.innerHeight / 2;
  let cx = mx, cy = my;
  let visible = false;

  window.addEventListener("mousemove", (e) => {
    mx = e.clientX; my = e.clientY;
    dot.style.transform = `translate(${mx}px, ${my}px)`;
    if (!visible) { visible = true; cursor.style.opacity = dot.style.opacity = "1"; }
  }, { passive: true });
  document.addEventListener("mouseleave", () => { visible = false; cursor.style.opacity = dot.style.opacity = "0"; });
  window.addEventListener("mousedown", () => cursor.style.scale = "0.8");
  window.addEventListener("mouseup", () => cursor.style.scale = "1");

  (function loop() {
    cx = lerp(cx, mx, 0.16);
    cy = lerp(cy, my, 0.16);
    cursor.style.transform = `translate(${cx}px, ${cy}px)`;
    requestAnimationFrame(loop);
  })();

  const hoverSel = "a, button, .chip, .acc__head, input, select, textarea, label, [data-cursor]";
  document.addEventListener("mouseover", (e) => {
    const t = e.target.closest(hoverSel);
    if (!t) return;
    const text = t.closest("[data-cursor]")?.dataset.cursor;
    if (text) { label.textContent = text; cursor.classList.add("is-label"); }
    else cursor.classList.add("is-hover");
  });
  document.addEventListener("mouseout", (e) => {
    const t = e.target.closest(hoverSel);
    if (!t) return;
    if (e.relatedTarget && t.contains(e.relatedTarget)) return;
    cursor.classList.remove("is-hover", "is-label");
  });

  /* ---------- Magnetic ---------- */
  document.querySelectorAll("[data-magnetic], .btn, .social, .slider__btn, .burger, .fab").forEach((el) => {
    const strength = parseFloat(el.dataset.magnetic) || 0.35;
    el.addEventListener("mousemove", (e) => {
      const r = el.getBoundingClientRect();
      const x = e.clientX - (r.left + r.width / 2);
      const y = e.clientY - (r.top + r.height / 2);
      el.style.transform = `translate(${x * strength}px, ${y * strength}px)`;
    });
    el.addEventListener("mouseleave", () => { el.style.transform = ""; });
  });

  /* ---------- 3D tilt with shine ---------- */
  document.querySelectorAll("[data-tilt]").forEach((el) => {
    const max = parseFloat(el.dataset.tilt) || 8;
    if (!el.querySelector(".tilt__shine")) {
      const s = document.createElement("span");
      s.className = "tilt__shine";
      el.appendChild(s);
    }
    el.classList.add("tilt");
    el.addEventListener("mousemove", (e) => {
      const r = el.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width;
      const py = (e.clientY - r.top) / r.height;
      el.style.transform = `perspective(900px) rotateY(${(px - 0.5) * max * 2}deg) rotateX(${(0.5 - py) * max * 2}deg) translateZ(0)`;
      el.style.setProperty("--sx", px * 100 + "%");
      el.style.setProperty("--sy", py * 100 + "%");
    });
    el.addEventListener("mouseleave", () => { el.style.transform = ""; });
  });

  /* ---------- Spotlight glow following mouse inside cards ---------- */
  document.querySelectorAll(".card").forEach((card) => {
    if (!card.querySelector(".card__glow")) {
      const g = document.createElement("span");
      g.className = "card__glow";
      card.prepend(g);
    }
    card.addEventListener("mousemove", (e) => {
      const r = card.getBoundingClientRect();
      card.style.setProperty("--mx", e.clientX - r.left + "px");
      card.style.setProperty("--my", e.clientY - r.top + "px");
    });
  });
})();
