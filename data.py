# -*- coding: utf-8 -*-
"""Content for the BeBest site: contacts, languages, courses, teachers, reviews, FAQ."""

PHONE = "+77479150579"
PHONE_H = "+7 747 915 05 79"
EMAIL = "clients@bebestschool.com"
EMAIL_HR = "recruitment@bebestschool.com"
EMAIL_ADV = "adv@bebestschool.com"
WA = "https://wa.me/34611586216?text=" + "%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5!%20%D0%A5%D0%BE%D1%87%D1%83%20%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C%20%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8E%20%D0%BF%D1%80%D0%BE%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20BeBest%20%D0%B8%20%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D1%8B%D0%B9%20%D0%BF%D1%80%D0%BE%D0%B1%D0%BD%D1%8B%D0%B9%20%D1%83%D1%80%D0%BE%D0%BA."
TG = "https://t.me/BBspecialoffer_bot"
IG = "https://www.instagram.com/be_best_school/"
FB = "https://www.facebook.com/school.Bebest"

# ------------------------------------------------------------------ languages
LANGS = [
    dict(key="english", name="Английский", native="English", code="en", flag="gb", color="#4fd1ff",
         gen="английского", dat="английскому", prep="английском", low="английский",
         hello="Hello!", why="Язык международного бизнеса, IT, науки и путешествий. Английский открывает 80% контента интернета и тысячи вакансий с релокацией.",
         word="English"),
    dict(key="german", name="Немецкий", native="Deutsch", code="de", flag="de", color="#ffd23d",
         gen="немецкого", dat="немецкому", prep="немецком", low="немецкий",
         hello="Hallo!", why="Ключ к бесплатному образованию в Германии и Австрии, работе в медицине, инженерии и IT в сильнейшей экономике Европы.",
         word="Deutsch"),
    dict(key="spanish", name="Испанский", native="Español", code="es", flag="es", color="#ff6b4a",
         gen="испанского", dat="испанскому", prep="испанском", low="испанский",
         hello="¡Hola!", why="На испанском говорят более 500 миллионов человек в 20+ странах. Язык путешествий, музыки, кино и солнечной жизни.",
         word="Español"),
    dict(key="italian", name="Итальянский", native="Italiano", code="it", flag="it", color="#3ddc84",
         gen="итальянского", dat="итальянскому", prep="итальянском", low="итальянский",
         hello="Ciao!", why="Язык искусства, моды, гастрономии и дизайна. Идеален для учёбы в Италии, путешествий и души.",
         word="Italiano"),
    dict(key="french", name="Французский", native="Français", code="fr", flag="fr", color="#8f78ff",
         gen="французского", dat="французскому", prep="французском", low="французский",
         hello="Bonjour!", why="Официальный язык ООН, ЮНЕСКО и Олимпийского движения. Престижные университеты Франции, Бельгии, Швейцарии и Канады.",
         word="Français"),
    dict(key="portuguese", name="Португальский", native="Português", code="pt", flag="pt", color="#ff5fa2",
         gen="португальского", dat="португальскому", prep="португальском", low="португальский",
         hello="Olá!", why="Язык Португалии и Бразилии — более 250 миллионов носителей. Популярен для релокации, ВНЖ и digital-номадов.",
         word="Português"),
    dict(key="polish", name="Польский", native="Polski", code="pl", flag="pl", color="#ff4d6d",
         gen="польского", dat="польскому", prep="польском", low="польский",
         hello="Cześć!", why="Практичный выбор для учёбы и работы в Польше и ЕС. Славянская основа помогает быстро заговорить.",
         word="Polski"),
]
LANG = {l["key"]: l for l in LANGS}

MATH = dict(key="math", name="Математика", native="Math", code="ma", flag="math", color="#d7ff3d",
            gen="математики", dat="математике", prep="математике", low="математика", hello="π", word="Math", why="")

# ------------------------------------------------------------------ courses
# type → content template in pages.py ; tags drive catalog filters
C = []
def course(slug, lang, title, short, ctype, tags, **extra):
    C.append(dict(slug=slug, lang=lang, title=title, short=short, type=ctype, tags=tags, **extra))

# English
course("anglijskij-dlya-nachinayushchih", "english", "Английский для начинающих", "С нуля до уверенного A2: алфавит, базовая грамматика и первые диалоги.", "beginner", "adults beginner", popular=True)
course("kursy-anglijskogo-dlya-vzroslyh", "english", "Английский для взрослых", "Гибкий график и живое общение для тех, кто совмещает учёбу с работой.", "general", "adults")
course("razgovornyj-anglijskij", "english", "Разговорный английский", "70% урока — говорите вы. Снимаем языковой барьер навсегда.", "speaking", "adults", popular=True)
course("intensivnyj-kurs-anglijskogo", "english", "Интенсивный английский", "Максимум результата в сжатые сроки: уровень за 2–3 месяца.", "intensive", "adults", popular=True)
course("kursy-anglijskogo-s-nositelem-yazyka", "english", "Английский с носителем", "Живое произношение, акценты и культура — от тех, для кого язык родной.", "native", "adults kids", popular=True)
course("angliyskiy-dlya-detey", "english", "Английский для детей", "Игры, песни и мультики — дети учат язык с удовольствием.", "kids", "kids", popular=True)
course("ent-english-for-children", "english", "Подготовка к ЕНТ по английскому", "Системная подготовка к ЕНТ: формат заданий, стратегии и пробные тесты.", "ent", "kids exams")
course("ielts-podgotovka", "english", "Подготовка к IELTS", "Стратегии всех четырёх модулей и пробные тесты для высокого балла.", "exam", "adults exams", exam="ielts", popular=True)
course("toefl-podgotovka", "english", "Подготовка к TOEFL", "TOEFL iBT для поступления в зарубежные университеты.", "exam", "adults exams", exam="toefl")
course("cambridge-exams-course", "english", "Cambridge exams (KET, PET, FCE, CAE)", "Подготовка к кембриджским экзаменам от A2 до C1.", "exam", "adults exams", exam="cambridge")
course("cambridge-exams-for-children", "english", "Cambridge exams для детей", "KET и PET for Schools — первые международные сертификаты ребёнка.", "exam", "kids exams", exam="cambridge_kids")
course("biznes-anglikij", "english", "Бизнес-английский", "Переговоры, презентации, деловая переписка и small talk.", "business", "adults business")
course("korporativnyj-anglijskij", "english", "Корпоративный английский", "Обучение команд: персональные графики, отчёты для HR.", "corporate", "business corporate")
course("anglijskij-dlya-it", "english", "Английский для IT", "Стендапы, код-ревью, документация и собеседования в международные компании.", "it", "adults business", popular=True)
course("english-job-interview", "english", "Подготовка к собеседованию", "Резюме, самопрезентация и ответы на сложные вопросы на английском.", "interview", "adults business")
course("grammar-english", "english", "Грамматический курс", "Вся грамматика простым языком — от Present Simple до инверсии.", "grammar", "adults")
course("kurs-anglijskogo-dlya-podvinutogo-urovnya", "english", "Курс для продвинутых (B2+)", "От «хорошего» к «блестящему»: идиомы, нюансы и свободная речь.", "advanced", "adults")
course("meditsinskiy-angliyskiy", "english", "Английский для медиков", "Медицинская терминология, общение с пациентами и коллегами.", "medical", "adults business")
course("anglikij-dlya-puteshestvij", "english", "Английский для путешествий", "Аэропорт, отель, ресторан и small talk — всё для свободных поездок.", "travel", "adults")
course("anglijskij-dlya-pereezda", "english", "Английский для переезда", "Аренда, банк, врач, работа — язык для новой жизни за границей.", "relocation", "adults")
course("anglikij-dlya-moryakov", "english", "Английский для моряков", "Морская лексика, Marlins и CES — для работы в международных экипажах.", "sailors", "adults business")
course("speaking-club", "english", "Speaking club", "Живые разговорные клубы с носителями и преподавателями каждую неделю.", "club", "clubs adults")

# German
course("german-real-talk", "german", "Разговорный немецкий", "Немецкий для жизни, работы и путешествий — говорим с первого урока.", "speaking", "adults", popular=True)
course("german-beginners-course", "german", "Немецкий с нуля", "Артикли, порядок слов и первые диалоги без страха.", "beginner", "adults beginner")
course("german-real-talk-for-children", "german", "Немецкий для детей", "Интерактивные уроки с играми для школьников 7–15 лет.", "kids", "kids")
course("german-beginners-course-children", "german", "Немецкий с нуля для детей", "Мягкий старт: алфавит, счёт, цвета и первые фразы.", "kids", "kids beginner")
course("ent-german-for-children", "german", "Подготовка к ЕНТ по немецкому", "Формат ЕНТ, грамматика и лексика, пробные тестирования.", "ent", "kids exams")
course("goethe-course", "german", "Подготовка к Goethe-Zertifikat", "Сертификат Goethe-Institut A1–C1: все модули и пробные экзамены.", "exam", "adults exams", exam="goethe")
course("daf-course", "german", "Подготовка к TestDaF", "Экзамен для поступления в университеты Германии.", "exam", "adults exams", exam="testdaf")
course("business-german-course", "german", "Бизнес-немецкий", "Деловая коммуникация, переписка и переговоры на немецком.", "business", "adults business")
course("german-course-for-medical", "german", "Немецкий для медиков", "Fachsprache, Patientengespräch и подготовка к работе врачом в Германии.", "medical", "adults business")
course("kurs-korporativnogo-nemetskogo-yazyka", "german", "Корпоративный немецкий", "Обучение сотрудников в удобном для компании формате.", "corporate", "business corporate")
course("grupovue-kursu-nemezkogo-yazika", "german", "Групповые курсы немецкого", "Учитесь в мини-группе — дешевле и веселее.", "group", "adults")
course("german-speaking-club", "german", "Разговорный клуб: немецкий", "Sprechen statt Pauken — регулярная практика речи.", "club", "clubs adults")

# Spanish
course("spanish-course", "spanish", "Разговорный испанский", "Живой испанский для общения и путешествий.", "speaking", "adults", popular=True)
course("spanish-beginner", "spanish", "Испанский для начинающих", "Произношение, ser/estar и первые диалоги — с нуля до A2.", "beginner", "adults beginner")
course("spanish-for-children", "spanish", "Испанский для детей", "Яркие уроки с играми и песнями на испанском.", "kids", "kids")
course("kurs-podgotovki-k-ehkzamenu-dele", "spanish", "Подготовка к экзамену DELE", "Официальный диплом Instituto Cervantes от A1 до C2.", "exam", "adults exams", exam="dele")
course("kurs-korporativnogo-ispanskogo-yazyka", "spanish", "Корпоративный испанский", "Испанский для команд и выхода на рынки Латинской Америки.", "corporate", "business corporate")
course("grupovue-kursu-ispanskogo-yazika", "spanish", "Групповые курсы испанского", "Мини-группы по уровню и интересам.", "group", "adults")
course("speaking-club-spanish", "spanish", "Разговорный клуб: испанский", "¡Hablemos! Практика с носителями каждую неделю.", "club", "clubs adults")

# Italian
course("italiano-course", "italian", "Разговорный итальянский", "Итальянский для путешествий, учёбы и удовольствия.", "speaking", "adults", popular=True)
course("italiano-beginner", "italian", "Итальянский для начинающих", "Мелодичный старт: произношение, базовые времена, первые фразы.", "beginner", "adults beginner")
course("italiano-for-children", "italian", "Итальянский для детей", "Весёлые уроки для детей и подростков.", "kids", "kids")
course("kurs-korporativnogo-italianskogo-yazyka", "italian", "Корпоративный итальянский", "Для компаний, работающих с Италией: мода, дизайн, производство.", "corporate", "business corporate")
course("grupovue-kursu-italyanskogo-yazika", "italian", "Групповые курсы итальянского", "Учитесь вместе — мини-группы до 8 человек.", "group", "adults")
course("speaking-club-italian", "italian", "Разговорный клуб: итальянский", "Parliamo! Живое общение на интересные темы.", "club", "clubs adults")

# French
course("french-language-course", "french", "Французский для взрослых", "Разговорный французский для жизни, учёбы и карьеры.", "speaking", "adults", popular=True)
course("french-beginner", "french", "Французский с нуля", "Произношение, артикли и базовая грамматика — без стресса.", "beginner", "adults beginner")
course("french-for-children", "french", "Французский для детей", "Игровые уроки французского для школьников.", "kids", "kids")
course("kurs-podgotovki-k-ehkzamenu-dalf-i-delf", "french", "Подготовка к DELF / DALF", "Официальные дипломы Министерства образования Франции.", "exam", "adults exams", exam="delf")
course("kurs-korporativnogo-frantsuzkogo-yazyka", "french", "Корпоративный французский", "Французский для команд и деловых коммуникаций.", "corporate", "business corporate")
course("grupovue-kursu-franzyskogo-yazika", "french", "Групповые курсы французского", "Мини-группы по уровням — с первого урока на французском.", "group", "adults")
course("speaking-club-french", "french", "Разговорный клуб: французский", "Parlons ! Практика речи и культура Франции.", "club", "clubs adults")

# Portuguese / Polish / Math
course("kurs-portugalskogo-yazyka", "portuguese", "Курс португальского языка", "Европейский и бразильский португальский с нуля и для продолжающих.", "speaking", "adults", popular=True)
course("grupovue-kursu-portugalskogo-yazika", "portuguese", "Групповые курсы португальского", "Мини-группы для релокации и путешествий.", "group", "adults")
course("speaking-club-portuguese", "portuguese", "Разговорный клуб: португальский", "Vamos conversar! Практика каждую неделю.", "club", "clubs adults")
course("kurs-polskogo-yazyka", "polish", "Курс польского языка", "Польский для учёбы, работы и Карты поляка.", "speaking", "adults", popular=True)
course("speaking-club-polish", "polish", "Разговорный клуб: польский", "Rozmawiajmy! Живая речь без страха ошибок.", "club", "clubs adults")
course("kursy-matematiki", "math", "Математика онлайн", "Школьная математика: понимание, а не зубрёжка.", "math", "kids")

COURSES = C
COURSE = {c["slug"]: c for c in C}

TEST_LANG = {"english": "en", "german": "de", "spanish": "es", "italian": "it", "french": "fr"}

EXAMS = {
    "ielts": dict(name="IELTS", full="International English Language Testing System",
        parts=[("Listening", "4 части, около 30 минут"), ("Reading", "3 текста, 60 минут"), ("Writing", "2 задания, 60 минут"), ("Speaking", "интервью с экзаменатором, 11–14 минут")],
        scale="Шкала 0–9 баллов", use="Учёба, работа и иммиграция: Великобритания, Канада, Австралия, Европа."),
    "toefl": dict(name="TOEFL iBT", full="Test of English as a Foreign Language",
        parts=[("Reading", "академические тексты"), ("Listening", "лекции и диалоги"), ("Speaking", "устные ответы на задания"), ("Writing", "интегрированное и академическое эссе")],
        scale="Шкала 0–120 баллов", use="Поступление в университеты США, Канады и многих стран мира."),
    "cambridge": dict(name="Cambridge English", full="KET · PET · FCE · CAE",
        parts=[("KET — A2 Key", "базовое общение"), ("PET — B1 Preliminary", "уверенный повседневный уровень"), ("FCE — B2 First", "учёба и работа на английском"), ("CAE — C1 Advanced", "академический и профессиональный уровень")],
        scale="Сертификат без срока действия", use="Пожизненный сертификат, признаваемый университетами и работодателями."),
    "cambridge_kids": dict(name="Cambridge for Schools", full="KET и PET for Schools",
        parts=[("Reading & Writing", "понимание текстов и письмо"), ("Listening", "аудирование"), ("Speaking", "устная часть в паре"), ("Пробные экзамены", "в реальном формате")],
        scale="Сертификат без срока действия", use="Первый международный сертификат ребёнка и мотивация учиться дальше."),
    "dele": dict(name="DELE", full="Diplomas de Español como Lengua Extranjera · Instituto Cervantes",
        parts=[("Comprensión de lectura", "чтение"), ("Comprensión auditiva", "аудирование"), ("Expresión escrita", "письмо"), ("Expresión oral", "устная часть")],
        scale="Уровни A1–C2, бессрочный диплом", use="Учёба, работа, гражданство Испании (A2 и выше)."),
    "delf": dict(name="DELF / DALF", full="Diplômes du Ministère de l'Éducation nationale",
        parts=[("Compréhension orale", "аудирование"), ("Compréhension écrite", "чтение"), ("Production écrite", "письмо"), ("Production orale", "устная часть")],
        scale="DELF A1–B2, DALF C1–C2, бессрочно", use="Поступление во французские вузы, работа, иммиграция во Францию и Канаду."),
    "goethe": dict(name="Goethe-Zertifikat", full="Сертификат Goethe-Institut",
        parts=[("Lesen", "чтение"), ("Hören", "аудирование"), ("Schreiben", "письмо"), ("Sprechen", "устная часть")],
        scale="Уровни A1–C2", use="Визы, воссоединение семьи (A1), работа и учёба в Германии."),
    "testdaf": dict(name="TestDaF", full="Test Deutsch als Fremdsprache",
        parts=[("Leseverstehen", "чтение"), ("Hörverstehen", "аудирование"), ("Schriftlicher Ausdruck", "письмо"), ("Mündlicher Ausdruck", "устная часть")],
        scale="Уровни TDN 3–5 (≈ B2–C1)", use="Поступление в университеты Германии."),
}

# ------------------------------------------------------------------ teachers
# (name, [langs], bio, vip, native)
TEACHERS = [
    ("Людмила", ["english"], "Опыт более 10 лет. Общеразговорный курс, корпоративные занятия, IT, business, морской английский (Marlins, CES), подготовка к IELTS, FCE/KET/PET и государственным экзаменам. Мастер-классы по коммуникативной методике English File. Любознательная, позитивная, терпеливая.", True, False),
    ("Валерия", ["english"], "Опыт более 7 лет. Киевский национальный лингвистический университет. Общеразговорный курс, корпоративные занятия, IT, business. Требовательная, когда нужно строгая и очень терпеливая.", False, False),
    ("Лолита", ["english"], "Высшее образование, опыт в частной школе и репетиторстве. Общеразговорный и деловой курс. Строит уроки в Miro на основе аутентичных материалов. Ответственная, креативная, коммуникабельная.", False, False),
    ("Наталья", ["english"], "Северо-Восточный федеральный университет. Общеразговорный курс, корпоративные занятия, бизнес-английский и подготовка к экзаменам. Энтузиастичная, позитивная и пунктуальная.", False, False),
    ("Ауржан", ["english"], "Быстро анализирует информацию и чётко доносит суть. Внимательна к потребностям учеников, легко адаптируется под разные цели и стили обучения.", True, False),
    ("Tayyeb", ["english"], "Носитель языка, English Teaching Certificate. Разговорный, деловой, медицинский и IT-курсы, подготовка к экзаменам. Спокоен даже если нужно объяснить одно и то же десять раз — важно, чтобы ученик понял.", False, True),
    ("Рауль", ["english"], "Сертификат CEFR. Общеразговорный и бизнес-курс. Терпеливый и позитивный — поднимет настроение даже в самый хмурый день.", False, False),
    ("Joan", ["english"], "Носитель языка. TEFL, IELTS Certification (British Council), M.Ed (University of Lagos). Более 30 индивидуальных курсов, игровые методики, Canva, Quizlet, Twinkl.", False, True),
    ("Гаухар", ["german"], "Fachhochschule Bochum, сертификат DSH. Общеразговорный курс немецкого.", False, False),
    ("Екатерина", ["german"], "Коммуникабельная и ответственная. Легко находит подход к ученикам и создаёт комфортную атмосферу на занятиях.", False, False),
    ("Павел", ["german"], "Опыт в языковом центре Deutsch KZ. Специализация — подготовка к экзаменам Goethe-Institut от A1 до C1.", False, False),
    ("Лариса", ["german"], "Опыт 12 лет. Общеразговорный курс, business, подготовка к Goethe-Zertifikat, DaF и государственным экзаменам. Дисциплина, креативность и дружелюбие.", False, False),
    ("Марина", ["german"], "Минский государственный лингвистический университет, семинары с немецкими преподавателями. Курсы для взрослых и детей. Приоритет — дисциплина.", True, False),
    ("Наталья", ["german", "french"], "Учит практическому применению языка в жизни, а не отдельной лексике и грамматике. Готовит к экзаменам для поступления в вуз.", True, False),
    ("Елена", ["german"], "Чувство юмора — её главный инструмент. Уроки на юморе — залог прочного усвоения материала.", True, False),
    ("Марта", ["german"], "Сертификаты Lakeview Learning Center, Chicago ESL Advanced. Общеразговорный, бизнес-курс, экзамены. Чёткость, искренность и стабильная поддержка.", False, False),
    ("Анна", ["german"], "Два диплома Deutsches Sprachdiplom. Отлично находит общий язык с детьми, создаёт тёплую атмосферу и вдохновляет учиться.", False, False),
    ("Лариса", ["spanish"], "Индивидуальный подход и чувство юмора. Тёплые приятельские отношения с учениками помогают раскрыть их потенциал.", False, False),
    ("Хоусе", ["spanish"], "Носитель языка, опыт более 3 лет. Строит программу вокруг целей студента для самого быстрого результата. Акцент на грамматике и речи.", False, True),
    ("Patricio", ["spanish"], "Носитель языка, Universidad del Bío Bío (Chile). Через месяц с ним любой начнёт читать, говорить и понимать основы испанского.", False, True),
    ("Марина", ["spanish"], "Сертификаты DELE и SIELE. Подготовка к DELE и SIELE. Её фишка — оптимизм, много похвалы и улыбок.", False, False),
    ("Надежда", ["spanish"], "Курсы для взрослых и детей. Постоянно развивается как преподаватель и умеет принимать ошибки — свои и студента.", True, False),
    ("Анна", ["spanish"], "Разговорный, деловой, IT и медицинский испанский, подготовка к экзаменам. Всегда работает на результат.", False, False),
    ("Вера", ["italian"], "Сертификаты CILS B2, C1, C2. Общий разговорный и грамматический курс. Ищет новые способы вовлечь студента.", False, False),
    ("Алеся", ["italian"], "Certificazione C2, Università per stranieri di Siena. Деликатная, терпеливая и ответственная за результат.", False, False),
    ("Елена", ["italian"], "Подготовка к CILS. Немного разбирается в психологии — это помогает понять, на чём делать акценты с каждым учеником.", True, False),
    ("Анаит", ["french"], "МГУ, опыт более 4 лет. Подготовка к DELF, французский для дипломатов. Помогает каждому найти «своё» в языке.", False, False),
    ("Akhat", ["french"], "Alliance Française (Astana, Toulouse), DELF B2. Деловой и юридический французский. Тактичный, находчивый, с отличным чувством юмора.", False, False),
    ("Алла", ["french"], "Всегда максимально вовлечена в урок. Честная, терпеливая и верит в студента независимо от его результатов.", True, False),
    ("Jackson", ["portuguese"], "Носитель языка. Курсы для взрослых, детей и подростков, бизнес-курс. Спокойный, внимательно слушает и создаёт поддерживающую атмосферу.", False, True),
    ("Серафима", ["portuguese"], "TESOL, диплом переводчика, 2 сертификата по португальскому. Разговорный, медицинский курс, экзамены.", False, False),
    ("Ирина", ["portuguese"], "Сертификат Português língua não materna B2. Дисциплинированная, строго контролирует успеваемость, но с тёплой атмосферой.", False, False),
]

# ------------------------------------------------------------------ reviews
REVIEWS = [
    ("Валентина Роднина", "врач", "Совмещаю медицинскую практику с преподаванием иностранцам. Времени на репетиторов не было — нашла BeBest. Улучшила уровень, освоила медицинскую терминологию. Посоветовала курсы племяннику — они и для детей тоже.", "17.01.2021"),
    ("Виктория Калинина", "ветеринар", "Пришлось с дочерью уехать за границу и столкнуться с языковым барьером. Интенсив для начинающих дал превосходные базовые навыки — общение с иностранцами даётся всё легче.", "23.09.2021"),
    ("Ольга Петрова", "предприниматель", "Сына пригласили в футбольную школу в Эстонии. С BeBest он уже свободно общается на английском. Методика нравится и мне, и ребёнку — я и сама подучила грамматику.", "22.09.2022"),
    ("Дания Искандерова", "пенсионерка", "Друзья подарили путешествие по Европе, а языковой барьер не давал покоя. Теперь чувствую себя увереннее, и грамматика с их методикой совсем не сложная.", "02.01.2021"),
    ("Катерина Гусак", "администратор отеля", "Работаю на ресепшене. В сравнении с прошлым опытом эффективность выше: вспомнила то, что учила, и усовершенствовала базовые навыки.", "29.12.2021"),
    ("Айсуле Куняшова", "продавец", "Дочь в 10 классе, готовится к поступлению. После курса она свободнее общается с родственниками из Америки — они сами отметили прогресс.", "19.12.2021"),
    ("Амир Серикбеков", "курсант морской академии", "Освоил не только базу, но и профессиональную морскую лексику и грамматические структуры. Индивидуальный онлайн-формат — очень удобно.", "20.07.2022"),
    ("Денис Довлатов", "менеджер", "Карьерный рост требовал английский «на вчера». Благодаря коммуникативной методике и интенсивности быстро преодолеваю языковой барьер.", "27.09.2021"),
    ("Наталья Кутуз", "домохозяйка", "Для меня BeBest — спасение. Прохожу интенсив с нуля: уже понимаю переписку с иностранцами и могу ответить. Эффективность налицо.", "31.03.2021"),
]

# ------------------------------------------------------------------ FAQ
FAQ = [
    ("Сколько длится занятие?", "Групповое занятие длится 90 минут, индивидуальное — 50 минут. Расписание подбирается под вас: уроки проводим круглосуточно."),
    ("Сколько стоит обучение?", "Стоимость зависит от тарифа: BASE — от 6 472 ₸ за урок, OPTIMAL — от 7 397 ₸, PREMIUM — от 10 633 ₸. Первый урок — бесплатный."),
    ("Чем отличаются тарифные планы?", "Опытом преподавателя и сервисом. BASE — сертифицированный преподаватель с опытом до 2 лет и фиксированное расписание. OPTIMAL — преподаватель с международными сертификатами (TESOL, TKT) и стажем от 5 лет, гибкий график. PREMIUM — ведущие преподаватели с опытом 10+ лет, носители языка или специалисты, живущие в стране языка, и индивидуальное сопровождение."),
    ("Какие языки преподаются в школе?", "Английский, немецкий, испанский, итальянский, французский, португальский и польский. Также есть курс математики для школьников."),
    ("Сколько человек обучается в группе?", "Мы проводим индивидуальные занятия, мини-группы на 2–4 студента и группы до 8 человек."),
    ("Что такое разговорные клубы (speaking clubs)?", "Еженедельные живые встречи для практики речи с преподавателями и носителями языка. Клубы проходят для разных уровней — это лучший способ снять языковой барьер."),
    ("Где проходит обучение?", "Онлайн, на собственной интерактивной платформе школы (LMS). Всё, что нужно, — хороший интернет. Для студентов есть мобильное приложение."),
    ("Сколько времени длится курс?", "Наши программы рассчитаны на достижение результата за определённое количество занятий. После пробного урока преподаватель составит программу под ваши цели и порекомендует количество уроков для освоения уровня."),
    ("Нужно ли покупать дополнительные материалы?", "Нет. Все учебные материалы, видеоуроки и тесты доступны на платформе школы."),
    ("Выдаёт ли школа сертификат?", "Да. После финального теста в конце каждого уровня вы получаете персонализированный сертификат о достижении уровня."),
]

STATS_HOME = [
    ("10", "лет учим и дружим с нашими студентами", ""),
    ("5000", "выпускников и по 10 новых каждый день", "+"),
    ("33", "курса преподаём одновременно", ""),
    ("70", "времени урока говорит и практикуется студент", "%"),
]
