/* =========================================================
   BeBest School — test.js
   Interactive level test for 5 languages (?lang=en|de|es|it|fr)
   ========================================================= */
(function () {
  "use strict";
  const root = document.querySelector("[data-test]");
  if (!root) return;
  const BB = window.BB || {};

  const BANK = {
    en: { name: "английского", page: "languages/english.html", q: [
      ["She ___ a teacher.", ["am", "is", "are", "be"], 1],
      ["I ___ to the cinema yesterday.", ["go", "went", "gone", "going"], 1],
      ["There isn't ___ milk in the fridge.", ["some", "any", "many", "a"], 1],
      ["He has lived here ___ 2015.", ["for", "since", "from", "during"], 1],
      ["If it rains tomorrow, we ___ at home.", ["stay", "will stay", "would stay", "stayed"], 1],
      ["This is the ___ film I've ever seen.", ["good", "better", "best", "most good"], 2],
      ["By the time we arrived, the film ___.", ["started", "has started", "had started", "was start"], 2],
      ["I'm looking forward to ___ you.", ["see", "seeing", "saw", "be seen"], 1],
      ["The report ___ by the manager tomorrow.", ["will review", "will be reviewed", "is reviewing", "reviewed"], 1],
      ["She suggested that he ___ a doctor.", ["sees", "see", "saw", "seeing"], 1],
      ["Hardly ___ the house when it started to rain.", ["I had left", "had I left", "I left", "did I leave"], 1],
      ["“To take something with a pinch of salt” means…", ["to believe it completely", "to be sceptical about it", "to add flavour", "to forget it"], 1]
    ]},
    de: { name: "немецкого", page: "languages/german.html", q: [
      ["Ich ___ aus Kasachstan.", ["bin", "bist", "ist", "sind"], 0],
      ["Das ist ___ Auto.", ["der", "die", "das", "dem"], 2],
      ["Ich habe ___ Bruder.", ["ein", "einen", "einem", "eines"], 1],
      ["Gestern ___ ich ins Kino gegangen.", ["habe", "bin", "war", "hatte"], 1],
      ["Wir fahren morgen ___ Berlin.", ["nach", "zu", "in", "bei"], 0],
      ["Ich weiß nicht, ob er heute ___.", ["kommt", "kommen", "zu kommen", "gekommen"], 0],
      ["Wenn ich Zeit ___, würde ich mehr reisen.", ["habe", "hätte", "hatte", "haben"], 1],
      ["Das Haus, ___ wir gekauft haben, ist alt.", ["der", "die", "das", "dem"], 2]
    ]},
    es: { name: "испанского", page: "languages/spanish.html", q: [
      ["Yo ___ estudiante.", ["soy", "estoy", "es", "eres"], 0],
      ["Mi casa ___ cerca del centro.", ["es", "está", "hay", "tiene"], 1],
      ["___ muchos turistas en Madrid.", ["Están", "Son", "Hay", "Tienen"], 2],
      ["Ayer ___ al cine con mis amigos.", ["voy", "fui", "iba", "iré"], 1],
      ["Me ___ mucho el café.", ["gusto", "gusta", "gustan", "gustas"], 1],
      ["Cuando era niño, ___ en un pueblo.", ["vivo", "viví", "vivía", "viviré"], 2],
      ["Espero que ___ buen tiempo mañana.", ["hace", "haga", "hará", "hacía"], 1],
      ["Si tuviera dinero, ___ una casa.", ["compro", "compraré", "compraría", "compré"], 2]
    ]},
    it: { name: "итальянского", page: "languages/italian.html", q: [
      ["Io ___ di Almaty.", ["sono", "sei", "è", "siamo"], 0],
      ["Noi ___ una macchina nuova.", ["abbiamo", "avete", "hanno", "ho"], 0],
      ["___ amici sono simpatici.", ["Il", "Gli", "Le", "Lo"], 1],
      ["Ieri (io, Maria) ___ andata al mare.", ["ho", "sono", "è", "era"], 1],
      ["Domani vado ___ Roma.", ["in", "a", "da", "per"], 1],
      ["Quando ero piccola, ___ sempre in giardino.", ["gioco", "giocavo", "ho giocato", "giocherò"], 1],
      ["Penso che lui ___ ragione.", ["ha", "abbia", "avrà", "aveva"], 1],
      ["Se avessi tempo, ___ di più.", ["leggo", "leggerò", "leggerei", "ho letto"], 2]
    ]},
    fr: { name: "французского", page: "languages/french.html", q: [
      ["Je ___ étudiant.", ["suis", "es", "est", "sont"], 0],
      ["Nous ___ deux enfants.", ["avons", "avez", "ont", "ai"], 0],
      ["Il habite ___ France.", ["à", "en", "au", "dans"], 1],
      ["Hier, je ___ allé au cinéma.", ["ai", "suis", "étais", "vais"], 1],
      ["Le matin, je bois ___ café.", ["le", "du", "de la", "des"], 1],
      ["Quand j'étais petit, je ___ au foot.", ["joue", "jouais", "ai joué", "jouerai"], 1],
      ["Il faut que tu ___ tes devoirs.", ["fais", "fasses", "feras", "faisais"], 1],
      ["Si j'avais le temps, j'___ le piano.", ["apprends", "apprendrai", "apprendrais", "ai appris"], 2]
    ]}
  };

  const LEVELS = [
    { max: 0.25, code: "A1", title: "Beginner", text: "Вы делаете первые шаги — отличный момент начать системно. Курс для начинающих даст прочный фундамент за 2–3 месяца." },
    { max: 0.45, code: "A2", title: "Elementary", text: "База есть! Теперь важно расширить словарь и начать уверенно говорить в бытовых ситуациях." },
    { max: 0.65, code: "B1", title: "Intermediate", text: "Вы уже объясняетесь на языке. Разговорная практика и speaking clubs помогут убрать барьер окончательно." },
    { max: 0.85, code: "B2", title: "Upper-Intermediate", text: "Сильный уровень! Самое время готовиться к международному экзамену или прокачать язык для карьеры." },
    { max: 1.01, code: "C1", title: "Advanced", text: "Впечатляюще! Вам подойдут курсы для продвинутых, бизнес-язык и подготовка к экзаменам уровня C1–C2." }
  ];

  const prefix = root.dataset.root || "";
  const params = new URLSearchParams(location.search);
  let lang = BANK[params.get("lang")] ? params.get("lang") : (root.dataset.lang || "en");
  let idx = 0, score = 0, locked = false;

  const qEl = root.querySelector(".test__q");
  const optsEl = root.querySelector(".test__options");
  const bar = root.querySelector(".test__progress i");
  const cnt = root.querySelector(".test__count");
  const play = root.querySelector(".test__play");
  const result = root.querySelector(".test__result");

  function setLangChips() {
    document.querySelectorAll("[data-test-lang]").forEach((c) => c.classList.toggle("is-active", c.dataset.testLang === lang));
    const nm = document.querySelector("[data-test-name]");
    if (nm) nm.textContent = BANK[lang].name;
  }

  function render() {
    const set = BANK[lang].q;
    const [text, opts] = set[idx];
    locked = false;
    cnt.textContent = `${idx + 1} / ${set.length}`;
    bar.style.width = (idx / set.length) * 100 + "%";
    qEl.innerHTML = text.replace("___", "<u>&nbsp;</u>");
    qEl.style.animation = "none"; void qEl.offsetWidth; qEl.style.animation = "";
    optsEl.innerHTML = opts.map((o, i) => `<button class="test__opt" type="button" data-i="${i}"><kbd>${i + 1}</kbd>${o}</button>`).join("");
  }

  function answer(i) {
    if (locked) return;
    locked = true;
    const set = BANK[lang].q;
    const right = set[idx][2];
    const btns = optsEl.querySelectorAll(".test__opt");
    btns[right].classList.add("is-right");
    if (i === right) score++;
    else btns[i].classList.add("is-wrong");
    const u = qEl.querySelector("u");
    if (u) u.textContent = set[idx][1][right];
    setTimeout(() => {
      idx++;
      if (idx < set.length) render();
      else finish();
    }, 900);
  }

  function finish() {
    const set = BANK[lang].q;
    bar.style.width = "100%";
    const ratio = score / set.length;
    const lvl = LEVELS.find((l) => ratio < l.max) || LEVELS[LEVELS.length - 1];
    play.hidden = true;
    result.hidden = false;
    result.innerHTML = `
      <span class="eyebrow">Ваш результат · ${score} из ${set.length}</span>
      <div class="test__level">${lvl.code}</div>
      <h3 class="h-m">${lvl.title}</h3>
      <p class="lead" style="max-width:560px">${lvl.text}</p>
      <div class="flex wrap gap" style="justify-content:center">
        <button class="btn btn--violet" data-modal-open data-course="Пробный урок: уровень ${lvl.code}, язык — ${BANK[lang].name}">
          <span class="btn__text"><span>Закрепить на пробном уроке</span><span>Закрепить на пробном уроке</span></span>
        </button>
        <a class="btn btn--ghost" href="${prefix}${BANK[lang].page}"><span class="btn__text"><span>Подобрать курс</span><span>Подобрать курс</span></span></a>
        <button class="btn btn--ghost" type="button" data-test-restart><span class="btn__text"><span>Пройти ещё раз</span><span>Пройти ещё раз</span></span></button>
      </div>`;
    BB.confetti && BB.confetti(result);
  }

  function restart() {
    idx = 0; score = 0;
    play.hidden = false; result.hidden = true;
    setLangChips();
    render();
  }

  optsEl.addEventListener("click", (e) => {
    const b = e.target.closest(".test__opt");
    if (b) answer(parseInt(b.dataset.i, 10));
  });
  document.addEventListener("keydown", (e) => {
    if (play.hidden) return;
    const n = parseInt(e.key, 10);
    if (n >= 1 && n <= 4) answer(n - 1);
  });
  document.addEventListener("click", (e) => {
    if (e.target.closest("[data-test-restart]")) restart();
    const c = e.target.closest("[data-test-lang]");
    if (c) {
      lang = c.dataset.testLang;
      try { const url = new URL(location.href); url.searchParams.set("lang", lang); history.replaceState(null, "", url); } catch (err) {}
      restart();
    }
  });

  restart();
})();
