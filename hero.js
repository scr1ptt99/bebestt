/* =========================================================
   BeBest School — hero.js
   Interactive "language constellation": floating greetings in
   7 languages + particles linked by lines, reacting to cursor.
   Click anywhere in the hero → shockwave burst.
   Works on any <canvas data-field>. data-field="lite" = fewer nodes.
   ========================================================= */
(function () {
  "use strict";
  const BB = window.BB || {};
  const canvases = document.querySelectorAll("canvas[data-field]");
  if (!canvases.length) return;

  const WORDS = ["Hello", "Hallo", "Hola", "Ciao", "Bonjour", "Olá", "Cześć", "Thanks", "Danke", "Gracias", "Grazie", "Merci", "Obrigado", "Dziękuję",
    "Be best", "Speak!", "Wow", "Ja", "Sí", "Oui", "Tak", "A1→C2", "IELTS", "DELE", "Goethe", "DELF", "TOEFL"];
  const COLORS = ["#d7ff3d", "#8f78ff", "#4fd1ff", "#ff6b4a", "#f5f1e8", "#ff5fa2"];

  canvases.forEach((canvas) => {
    const ctx = canvas.getContext("2d");
    const lite = canvas.dataset.field === "lite";
    const host = canvas.parentElement;
    let W = 0, H = 0, DPR = Math.min(window.devicePixelRatio || 1, 2);
    let nodes = [];
    let waves = [];
    const mouse = { x: -9999, y: -9999, active: false };
    let visible = true;
    let t = 0;

    function resize() {
      const r = host.getBoundingClientRect();
      W = r.width; H = r.height;
      canvas.width = W * DPR; canvas.height = H * DPR;
      canvas.style.width = W + "px"; canvas.style.height = H + "px";
      ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
      build();
    }

    function build() {
      const area = W * H;
      const dots = Math.round(clampN(area / (lite ? 26000 : 14000), 24, lite ? 60 : 120));
      const words = lite ? 8 : Math.round(clampN(W / 70, 8, 22));
      nodes = [];
      for (let i = 0; i < dots; i++) {
        nodes.push(makeNode(false));
      }
      for (let i = 0; i < words; i++) {
        nodes.push(makeNode(true));
      }
    }
    function clampN(v, a, b) { return Math.max(a, Math.min(b, v)); }
    function makeNode(isWord) {
      const z = Math.random() * 0.8 + 0.2; // depth
      return {
        x: Math.random() * W, y: Math.random() * H,
        bx: 0, by: 0,
        vx: (Math.random() - 0.5) * 0.35 * z, vy: (Math.random() - 0.5) * 0.35 * z,
        z,
        r: isWord ? 0 : 1 + z * 2.2,
        word: isWord ? WORDS[Math.floor(Math.random() * WORDS.length)] : null,
        color: COLORS[Math.floor(Math.random() * COLORS.length)],
        phase: Math.random() * Math.PI * 2,
        size: isWord ? 12 + z * (lite ? 14 : 22) : 0
      };
    }

    host.addEventListener("mousemove", (e) => {
      const r = canvas.getBoundingClientRect();
      mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top; mouse.active = true;
    });
    host.addEventListener("mouseleave", () => { mouse.active = false; mouse.x = mouse.y = -9999; });
    host.addEventListener("click", (e) => {
      if (e.target.closest("a, button")) return;
      const r = canvas.getBoundingClientRect();
      waves.push({ x: e.clientX - r.left, y: e.clientY - r.top, r: 0, a: 1 });
      nodes.forEach((n) => {
        const dx = n.x - (e.clientX - r.left), dy = n.y - (e.clientY - r.top);
        const d = Math.hypot(dx, dy) || 1;
        if (d < 380) { const f = (380 - d) / 380 * 9; n.vx += dx / d * f * n.z; n.vy += dy / d * f * n.z; }
      });
    });

    if ("IntersectionObserver" in window) {
      new IntersectionObserver((en) => { visible = en[0].isIntersecting; }).observe(canvas);
    }

    function step() {
      if (!(BB.reduce && t > 0.02)) requestAnimationFrame(step);
      if (!visible) return;
      t += 0.01;
      ctx.clearRect(0, 0, W, H);

      // update
      for (const n of nodes) {
        if (mouse.active) {
          const dx = n.x - mouse.x, dy = n.y - mouse.y;
          const d2 = dx * dx + dy * dy;
          const R = 170;
          if (d2 < R * R) {
            const d = Math.sqrt(d2) || 1;
            const f = (R - d) / R * 0.9 * n.z;
            n.vx += (dx / d) * f; n.vy += (dy / d) * f;
          }
        }
        n.vx *= 0.96; n.vy *= 0.96;
        // gentle drift so they never stop
        n.vx += Math.cos(t + n.phase) * 0.006 * n.z;
        n.vy += Math.sin(t * 1.3 + n.phase) * 0.006 * n.z;
        n.x += n.vx; n.y += n.vy;
        const pad = 60;
        if (n.x < -pad) n.x = W + pad; if (n.x > W + pad) n.x = -pad;
        if (n.y < -pad) n.y = H + pad; if (n.y > H + pad) n.y = -pad;
      }

      // links
      const dots = nodes.filter((n) => !n.word);
      const LINK = lite ? 110 : 130;
      ctx.lineWidth = 1;
      for (let i = 0; i < dots.length; i++) {
        const a = dots[i];
        for (let j = i + 1; j < dots.length; j++) {
          const b = dots[j];
          const dx = a.x - b.x, dy = a.y - b.y;
          const d2 = dx * dx + dy * dy;
          if (d2 < LINK * LINK) {
            const o = (1 - Math.sqrt(d2) / LINK) * 0.22 * Math.min(a.z, b.z);
            ctx.strokeStyle = `rgba(143,120,255,${o})`;
            ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
          }
        }
        // link to mouse
        if (mouse.active) {
          const dx = a.x - mouse.x, dy = a.y - mouse.y;
          const d = Math.hypot(dx, dy);
          if (d < 220) {
            ctx.strokeStyle = `rgba(215,255,61,${(1 - d / 220) * 0.5})`;
            ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(mouse.x, mouse.y); ctx.stroke();
          }
        }
      }

      // draw dots
      for (const n of dots) {
        ctx.beginPath();
        ctx.fillStyle = n.color;
        ctx.globalAlpha = 0.35 + n.z * 0.6;
        ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
        ctx.fill();
      }
      // draw words
      ctx.textAlign = "center"; ctx.textBaseline = "middle";
      for (const n of nodes) {
        if (!n.word) continue;
        const pulse = 0.5 + Math.sin(t * 2 + n.phase) * 0.15;
        ctx.globalAlpha = (0.08 + n.z * 0.22) * (pulse + 0.5);
        ctx.font = `700 ${n.size}px Unbounded, Arial Black, sans-serif`;
        ctx.fillStyle = n.color;
        ctx.fillText(n.word, n.x, n.y);
      }
      ctx.globalAlpha = 1;

      // shockwaves
      waves = waves.filter((w) => w.a > 0.01);
      for (const w of waves) {
        w.r += 9; w.a *= 0.94;
        ctx.strokeStyle = `rgba(215,255,61,${w.a})`;
        ctx.lineWidth = 2;
        ctx.beginPath(); ctx.arc(w.x, w.y, w.r, 0, Math.PI * 2); ctx.stroke();
      }
    }

    resize();
    let rt;
    window.addEventListener("resize", () => { clearTimeout(rt); rt = setTimeout(resize, 150); });
    requestAnimationFrame(step);
  });
})();
