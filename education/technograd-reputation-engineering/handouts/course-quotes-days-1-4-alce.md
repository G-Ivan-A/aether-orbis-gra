---
status: draft
version: 1.0
updated: 2026-11-01
temperature: 0.2
scope: reputation-engineering-course-quotes-days-1-4
source: "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-11-01-course-quotes-days-1-4-alce.md"
---

# Цитаты курса «Репутационный инжиниринг»: Дни 1–4 с разметкой ALCE

> **Перенесено из Хаба.** Файл собран в Хабе построителем из каталога
> [course-quotes-provenance/](course-quotes-provenance/README.md) (провенанс, здесь не
> исполняется). При переносе якоря строк `#Lnnn` пересчитаны по копиям материалов
> в этом репозитории; ссылки на файлы, которые остались в Хабе (каталог источников
> #650 и другие), закреплены на коммите Хаба из поля `source`.

Единый список всех дословных цитат из исследований курса в `research/reputation-technologies` (issue #711). Его можно использовать на лекциях и раздавать слушателям. Цитаты сгруппированы по дням курса. У каждой цитаты есть:

- **цитата** — дословно, на языке источника, и перевод (если источник не на русском);
- **интерпретация** — как её читать в контексте репутационных технологий;
- **авторы** — ФИО полностью, насколько их удалось установить;
- **дата** события или публикации;
- **источник** — полное название без сокращений;
- **ссылка** на источник;
- место в источнике, статус проверки и строка репозитория, откуда цитата взята.

Файл собран скриптом [`build_quotes_711.py`](course-quotes-provenance/build_quotes_711.py); не редактируйте его вручную. Проверка — [`check-quotes-711.py`](course-quotes-provenance/check-quotes-711.py): каждая цитата дословно совпадает с указанной строкой репозитория, каждая ссылка [n] ведёт в список источников.

## Как устроена разметка ALCE

Разметка следует стандарту ALCE (Tianyu Gao, Howard Yen, Jiatong Yu, Danqi Chen. Enabling Large Language Models to Generate Text with Citations, 2023; в каталоге курса — источник Н4, см. День 2):

1. Каждое утверждение несёт маркер `[n]`. Маркер стоит после цитаты и после интерпретации.
2. Маркер `[n]` ведёт к записи `n` в разделе «Список источников (ALCE)» в конце файла. Там — авторы, дата, полное название, ссылка и статус проверки.
3. Опорный фрагмент (passage) для каждого утверждения — сама цитата. Интерпретация опирается только на неё и на источник `[n]`; если вывод выходит за пределы источника, это сказано прямо.
4. Номера `[n]` присвоены по порядку первого появления источника в файле.

Статусы проверки (как в каталоге [#650](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md)):

- `VERIFIED-FULLTEXT` — цитата сверена с полным текстом источника;
- `VERIFIED-ABSTRACT` — сверена с официальной аннотацией;
- `VERIFIED-SECONDARY` — сверена по вторичному источнику, который назван в поле «Источник»;
- `VERIFIED (колода v5, решение 7)` — эпиграф Дня 4, сверенный с источником из подписи слайда; исходный текст для #711 сверен ещё раз и сохранён в [`source-excerpts-711.txt`](course-quotes-provenance/source-excerpts-711.txt).

Источники со статусом `UNVERIFIED` цитат не дают и в список не входят.

Переводы: «перевод из каталога #650» и «перевод курса» — уже принятые в репозитории; «перевод наш (#711)» — сделан для этого списка, потому что в репозитории перевода не было.

## Как пользоваться

- Для слайда или раздаточного материала берите цитату вместе с маркером `[n]` и записью `n` из списка источников.
- Интерпретация — это подсказка лектору, а не слова автора. Не выдавайте её за цитату.
- Цитаты со статусом `VERIFIED-SECONDARY` приводите с пометкой «цитируется по…».
- Цитаты, помеченные «слова автора статьи» или «слова обзора», не приписывайте классику, о котором идёт речь.

## Содержание

- [День 1. Гравитационная модель репутации, сети, доверие и репутационный капитал](#день-1-гравитационная-модель-репутации-сети-доверие-и-репутационный-капитал) — 75 цитат
- [День 2. Достоверность данных, разведывательный анализ и работа с ИИ](#день-2-достоверность-данных-разведывательный-анализ-и-работа-с-ии) — 85 цитат
- [День 3. Стейкхолдеры, точки влияния и каналы коммуникации](#день-3-стейкхолдеры-точки-влияния-и-каналы-коммуникации) — 43 цитат
- [День 4. Имидж-технологии: внешность, одежда, первое впечатление](#день-4-имидж-технологии-внешность-одежда-первое-впечатление) — 70 цитат

Всего цитат: 273; источников: 107.

## День 1. Гравитационная модель репутации, сети, доверие и репутационный капитал

### 1.1. Jan Tinbergen — Г1 [1]

> "The factor of distance may also stand for an index of information about export markets. It will be clear that distance – in contrast to the other two factors – has a negative influence on trade flows." [1]

- **Перевод:** «Фактор расстояния может также служить показателем информированности об экспортных рынках. Ясно, что расстояние, в отличие от двух других факторов, оказывает отрицательное влияние на торговые потоки». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 547](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L547))
- **Интерпретация для репутационных технологий:** Тинберген прямо допускает, что расстояние в гравитационной модели может означать информированность о рынке, а не только километры. Для GRA это прецедент информационной оси дистанции: связь слабеет там, где о партнёре мало знают. Формулу GRA из Тинбергена не выводим — это прецедент и одна из сред исследования, а не её первоисточник. [1]
- **Авторы:** Jan Tinbergen
- **Дата:** 1962
- **Источник:** Shaping the World Economy: Suggestions for an International Economic Policy. New York: The Twentieth Century Fund, 1962. Appendix VI «An Analysis of World Trade Flows», pages 262–293
- **Ссылка:** https://repub.eur.nl/pub/16826
- **Место в источнике:** страница 263
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 546](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L546)

### 1.2. Jan Tinbergen — Г1 [1]

> "The exponents a1, a2, and a3 indicate that there is not necessarily direct proportionality between the explanatory variables (Yi, Yj, and Dij) and the variable to be explained (Eij)." [1]

- **Перевод:** «Показатели степени a1, a2 и a3 указывают на то, что между объясняющими переменными (Yi, Yj и Dij) и объясняемой переменной (Eij) не обязательно существует прямая пропорциональность». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 549](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L549))
- **Интерпретация для репутационных технологий:** Степени в гравитационном уравнении оцениваются по данным, прямая пропорциональность не обязательна. Лектору это аргумент против буквального чтения формулы GRA: квадрат расстояния у Тинбергена не заложен, поэтому формулу показываем как эвристику, а массу и дистанцию в курсе описываем словами, а не числами. [1]
- **Авторы:** Jan Tinbergen
- **Дата:** 1962
- **Источник:** Shaping the World Economy: Suggestions for an International Economic Policy. New York: The Twentieth Century Fund, 1962. Appendix VI «An Analysis of World Trade Flows», pages 262–293
- **Ссылка:** https://repub.eur.nl/pub/16826
- **Место в источнике:** страница 264
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 548](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L548)

### 1.3. Thomas Chaney — Г3 [2]

> "Despite this dispersion, the distance coefficient ζ has been remarkably stable, hovering around 1 over more than a century of data." [2]

- **Перевод:** «Несмотря на этот разброс, коэффициент расстояния ζ оставался удивительно стабильным, колеблясь около 1 на данных за более чем столетие». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 569](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L569))
- **Интерпретация для репутационных технологий:** Главное ограничение для формулы GRA: эмпирически торговля убывает примерно как 1/расстояние, а не 1/расстояние². Квадрат расстояния в GRA — условная иллюстрация по аналогии с Ньютоном, а не эмпирическая степень; физическая аналогия становится полезной лишь после калибровки на данных. [2]
- **Авторы:** Thomas Chaney
- **Дата:** август 2013
- **Источник:** The Gravity Equation in International Trade: An Explanation. National Bureau of Economic Research Working Paper Number 19285. Cambridge, Massachusetts: National Bureau of Economic Research, 2013
- **Ссылка:** https://www.nber.org/papers/w19285.pdf
- **Место в источнике:** страница 2 препринта
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 568](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L568)

### 1.4. Каукин Андрей Сергеевич и соавторы — Г4 [3]

> «Гравитационные модели торговли изначально были разработаны как удобный эконометрический инструмент анализа торговых потоков между странами, который получил достаточно широкое распространение в силу «хороших» (согласующихся с интуитивными) эмпирических результатов.» [3]

- **Интерпретация для репутационных технологий:** Рецензируемый российский источник легитимирует «гравитационную» логику в русскоязычном курсе: модель прижилась потому, что давала понятные, согласующиеся с интуицией результаты. Для лектора это повод использовать гравитационный язык как рабочую эвристику для разговора о связях, но не как закон. [3]
- **Авторы:** Каукин Андрей Сергеевич; Идрисов Георгий (отчество: полное имя в открытых источниках не установлено)
- **Дата:** 2013
- **Источник:** Гравитационная модель внешней торговли России: случай большой по площади страны с протяженной границей // Экономическая политика. 2013. Номер 4. Страницы 133–154
- **Ссылка:** https://www.iep.ru/files/text/policy/2013-4/kaukin.pdf
- **Место в источнике:** страница 134
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 579](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L579)

### 1.5. Каукин Андрей Сергеевич и соавторы — Г4 [3]

> «Необходимо отметить, что автор сразу записал эконометрическую спецификацию модели, не выводя ее из строгих теоретических предпосылок.» [3]

- **Интерпретация для репутационных технологий:** Каукин и Идрисов честно фиксируют, что исходная спецификация была записана без вывода из строгих теоретических предпосылок. Отсюда методическая позиция курса: GRA подаётся как эвристика и набор вопросов к связям, а не как закон, из которого можно вычислить силу репутационного влияния. [3]
- **Авторы:** Каукин Андрей Сергеевич; Идрисов Георгий (отчество: полное имя в открытых источниках не установлено)
- **Дата:** 2013
- **Источник:** Гравитационная модель внешней торговли России: случай большой по площади страны с протяженной границей // Экономическая политика. 2013. Номер 4. Страницы 133–154
- **Ссылка:** https://www.iep.ru/files/text/policy/2013-4/kaukin.pdf
- **Место в источнике:** страница 135
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 580](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L580)

### 1.6. Kurt Lewin — Г5 [4]

> "For the social scientist this means that he should give up thinking about such items as group structure, group tension, or social forces as nothing more than a popular metaphor or analogy which should be eliminated from science as much as possible." [4]

- **Перевод:** «Для социального исследователя это означает, что он должен перестать считать такие вещи, как групповая структура, групповое напряжение или социальные силы, всего лишь популярной метафорой или аналогией, которую следует по возможности изгнать из науки». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 596](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L596))
- **Интерпретация для репутационных технологий:** Левин защищает социальные силы и групповое напряжение от обвинения в «просто метафоре». Это сильная опора для языка «сил» в GRA: говорить о притяжении и отталкивании между стейкхолдерами допустимо как об аналитическом инструменте — но именно как о методе, а не о физике общества. [4]
- **Авторы:** Kurt Lewin
- **Дата:** 1947
- **Источник:** Frontiers in Group Dynamics: Concept, Method and Reality in Social Science; Social Equilibria and Social Change // Human Relations. 1947. Volume 1, Number 1. Pages 5–41
- **Ссылка:** https://doi.org/10.1177/001872674700100103
- **Место в источнике:** страница 10
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 595](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L595)

### 1.7. Kurt Lewin — Г5 [4]

> "On the whole, then, we can say that a quasi-stationary social state corresponds to equally strong opposing forces but that no general statement concerning their absolute strength is possible." [4]

- **Перевод:** «В целом, таким образом, можно сказать, что квазистационарное социальное состояние соответствует равным по силе противоположным силам, но никакого общего утверждения об их абсолютной величине сделать нельзя». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 598](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L598))
- **Интерпретация для репутационных технологий:** Вторая половина мысли Левина задаёт границу модели: устойчивое состояние держится на уравновешенных противоположных силах, но их абсолютную величину определить нельзя. Поэтому любые численные значения силы в GRA условны; практик разбирает баланс давлений вокруг репутации, а не измеряет их в единицах. [4]
- **Авторы:** Kurt Lewin
- **Дата:** 1947
- **Источник:** Frontiers in Group Dynamics: Concept, Method and Reality in Social Science; Social Equilibria and Social Change // Human Relations. 1947. Volume 1, Number 1. Pages 5–41
- **Ссылка:** https://doi.org/10.1177/001872674700100103
- **Место в источнике:** страница 16, раздел "(b) Force Fields"
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 597](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L597)

### 1.8. Kurt Lewin — Г6 [5]

> "Field theory is probably best characterized as a method: namely, a method of analyzing causal relations and of building scientific constructs." [5]

- **Перевод:** «Теорию поля, вероятно, лучше всего характеризовать как метод, а именно метод анализа причинных связей и построения научных конструктов». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 610](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L610))
- **Интерпретация для репутационных технологий:** Левин называет теорию поля методом анализа причинных связей, а не вычислительной формулой. Именно в таком методическом статусе GRA уместна в корпоративном курсе: модель делает разбор воспроизводимым, задавая каждой связи одни и те же вопросы, а не выдавая расчёт. [5]
- **Авторы:** Kurt Lewin; редактор Dorwin Cartwright
- **Дата:** 1951
- **Источник:** Field Theory in Social Science: Selected Theoretical Papers / edited by Dorwin Cartwright. New York: Harper & Brothers, 1951
- **Ссылка:** https://archive.org/stream/dli.ernet.503983/503983-Field%20Theory%20In%20Social%20Science_djvu.txt
- **Место в источнике:** страница 45
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 609](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L609)

### 1.9. Kurt Lewin — Г6 [5]

> "A totality of coexisting facts which are conceived of as mutually interdependent is called a field (31)." [5]

- **Перевод:** «Совокупность сосуществующих фактов, понимаемых как взаимозависимые, называется полем (31)». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 612](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L612))
- **Интерпретация для репутационных технологий:** Определение поля как совокупности взаимозависимых фактов обосновывает сетевой взгляд курса: репутацию нельзя разобрать по одному стейкхолдеру, потому что отношения влияют друг на друга. Для GRA это довод смотреть на карту связей целиком, а не на отдельный образ компании. [5]
- **Авторы:** Kurt Lewin; редактор Dorwin Cartwright
- **Дата:** 1951
- **Источник:** Field Theory in Social Science: Selected Theoretical Papers / edited by Dorwin Cartwright. New York: Harper & Brothers, 1951
- **Ссылка:** https://archive.org/stream/dli.ernet.503983/503983-Field%20Theory%20In%20Social%20Science_djvu.txt
- **Место в источнике:** страница 240
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 611](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L611)

### 1.10. Курт Левин — Г7 [6]

> «всякое поведение или всякое изменение в психологическом поле зависит только от психологического поля в тот момент времени» [6]

- **Интерпретация для репутационных технологий:** Мысль о том, что поведение зависит от поля в данный момент, даёт аналог зависимости Полярности GRA от времени t: знак связи фиксируется на дату и может смениться. Ограничения два: Левин говорит о психологическом поле индивида, а не о сети организаций, и цитата приводится по статье Лукова, а не по самому переводу. [6]
- **Авторы:** Курт Левин (Kurt Lewin); цитаты приведены по статье: Луков Валерий Андреевич; переводчики русского издания: полное имя в открытых источниках не установлено
- **Дата:** русское издание 2000; статья Лукова 2017
- **Источник:** Теория поля в социальных науках. Санкт-Петербург: Сенсор, 2000 (у Лукова: Санкт-Петербург: Речь), цитируется по: Полевой и сферный подходы в гуманитарных науках // Горизонты гуманитарного знания. 2017. Номер 6
- **Ссылка:** https://doi.org/10.17805/ggz.2017.6.1
- **Место в источнике:** Левин 2000: 66; приведена у Лукова на странице 6
- **Статус проверки:** VERIFIED-SECONDARY
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 624](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L624)

### 1.11. Курт Левин — Г7 [6]

> «ценности определяют то, какие типы деятельности имеют положительную, а какие отрицательную валентность для индивида в данной ситуации. Другими словами, ценности не являются силовыми полями, но “наводят” на силовые поля» [6]

- **Интерпретация для репутационных технологий:** Русскоязычные термины «положительная и отрицательная валентность» — прямой аналог Полярности в GRA: ценности задают, что для участника притягательно, а что отталкивает. Цитата вторичная, по статье Лукова, и относится к психологическому полю индивида; перенос на сеть организаций — интерпретация курса. [6]
- **Авторы:** Курт Левин (Kurt Lewin); цитаты приведены по статье: Луков Валерий Андреевич; переводчики русского издания: полное имя в открытых источниках не установлено
- **Дата:** русское издание 2000; статья Лукова 2017
- **Источник:** Теория поля в социальных науках. Санкт-Петербург: Сенсор, 2000 (у Лукова: Санкт-Петербург: Речь), цитируется по: Полевой и сферный подходы в гуманитарных науках // Горизонты гуманитарного знания. 2017. Номер 6
- **Ссылка:** https://doi.org/10.17805/ggz.2017.6.1
- **Место в источнике:** Левин 2000: 63; приведена у Лукова на странице 7
- **Статус проверки:** VERIFIED-SECONDARY
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 625](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L625)

### 1.12. Fritz Heider — Г8 [7]

> "we shall understand by attitude the positive or negative relationship of a person p to another person o or to an impersonal entity x which may be a situation, an event, an idea, or a thing, etc." [7]

- **Перевод:** «под установкой мы будем понимать положительное или отрицательное отношение лица p к другому лицу o или к безличной сущности x, которой может быть ситуация, событие, идея, вещь и т. п.» (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 642](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L642))
- **Интерпретация для репутационных технологий:** Хайдер описывает отношение человека к другому лицу или объекту как положительное или отрицательное — это прямой первоисточник Полярности (+/−) в GRA. Ограничение: отношения у него бинарны, нулевое значение и степень отношения не вводятся, а «?» как отдельная отметка — уже правило GRA. [7]
- **Авторы:** Fritz Heider
- **Дата:** 1946
- **Источник:** Attitudes and Cognitive Organization // The Journal of Psychology. 1946. Volume 21. Pages 107–112
- **Ссылка:** https://psychclassics.yorku.ca/Heider/attitudes.htm
- **Место в источнике:** страница 107
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 641](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L641)

### 1.13. Fritz Heider — Г8 [7]

> "If no balanced state exists, then forces towards this state will arise." [7]

- **Перевод:** «Если сбалансированного состояния нет, то возникают силы, направленные к этому состоянию». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 644](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L644))
- **Интерпретация для репутационных технологий:** Идея о том, что дисбаланс порождает силы, направленные к равновесию, помогает читать динамику репутационных конфликтов: несогласованная конфигурация отношений неустойчива и будет меняться. Практику это повод искать на карте напряжённые треугольники, помня, что у Хайдера отношения бинарны и без степени. [7]
- **Авторы:** Fritz Heider
- **Дата:** 1946
- **Источник:** Attitudes and Cognitive Organization // The Journal of Psychology. 1946. Volume 21. Pages 107–112
- **Ссылка:** https://psychclassics.yorku.ca/Heider/attitudes.htm
- **Место в источнике:** страницы 107–108
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 643](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L643)

### 1.14. Fritz Heider — Г8 [7]

> "(b) In the case of three entities, a balanced state exists if all three possible relations are positive in all respects." [7]

- **Перевод:** «(b) В случае трёх сущностей сбалансированное состояние существует, если все три возможных отношения положительны во всех отношениях». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 646](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L646))
- **Интерпретация для репутационных технологий:** Простейший случай баланса — все три отношения положительны; на карте стейкхолдеров это устойчивый треугольник союзников. Из теории баланса GRA берёт именно знак связи; силы, массы и степени отношения у Хайдера нет. [7]
- **Авторы:** Fritz Heider
- **Дата:** 1946
- **Источник:** Attitudes and Cognitive Organization // The Journal of Psychology. 1946. Volume 21. Pages 107–112
- **Ссылка:** https://psychclassics.yorku.ca/Heider/attitudes.htm
- **Место в источнике:** страница 110
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 645](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L645)

### 1.15. Fritz Heider — Г8 [7]

> "This holds generally: the triad of relations is in balance. if two relations are negative and one positive." [7]

- **Перевод:** «Это верно в общем виде: триада отношений находится в балансе, если два отношения отрицательны, а одно положительно». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 649](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L649))
- **Интерпретация для репутационных технологий:** Правило «два минуса и один плюс — тоже баланс» формализует обиходное «враг моего врага». Для GRA вывод практический: отрицательные связи — не шум, они участвуют в устойчивых конфигурациях, поэтому на карте их отмечают знаком, а не опускают. [7]
- **Авторы:** Fritz Heider
- **Дата:** 1946
- **Источник:** Attitudes and Cognitive Organization // The Journal of Psychology. 1946. Volume 21. Pages 107–112
- **Ссылка:** https://psychclassics.yorku.ca/Heider/attitudes.htm
- **Место в источнике:** страница 110
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 647](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L647)

### 1.16. Dorwin Cartwright и соавторы — Г9 [8]

> "A signed graph, or briefly an s-graph, is obtained from a graph when one regards some of the lines as positive and the remaining lines as negative." [8]

- **Перевод:** «Знаковый граф, или кратко s-граф, получается из графа, если рассматривать одни его линии как положительные, а остальные как отрицательные». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 659](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L659))
- **Интерпретация для репутационных технологий:** Знаковый граф — главная формальная опора GRA как графа отношений со знаком, где возможны отношение и его противоположность, например симпатия и антипатия. Ограничение: знаки у Картрайта и Харари дискретны, а масс узлов и расстояний в их модели нет — это добавляет GRA. [8]
- **Авторы:** Dorwin Cartwright; Frank Harary
- **Дата:** 1956
- **Источник:** Structural Balance: A Generalization of Heider's Theory // Psychological Review. 1956. Volume 63, Number 5. Pages 277–293
- **Ссылка:** https://snap.stanford.edu/class/cs224w-readings/cartwright56balance.pdf
- **Место в источнике:** страница 282
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 658](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L658)

### 1.17. Dorwin Cartwright и соавторы — Г9 [8]

> "Thus we define an s-graph (containing any number of points) as balanced if all of its cycles are positive." [8]

- **Перевод:** «Таким образом, мы определяем s-граф (с любым числом точек) как сбалансированный, если все его циклы положительны». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 661](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L661))
- **Интерпретация для репутационных технологий:** Обобщение баланса на сеть любого размера даёт проверяемый критерий: граф сбалансирован, если все его циклы положительны. Практик может искать на карте связей отрицательные циклы как точки напряжения; масса и дистанция в этот критерий не входят. [8]
- **Авторы:** Dorwin Cartwright; Frank Harary
- **Дата:** 1956
- **Источник:** Structural Balance: A Generalization of Heider's Theory // Psychological Review. 1956. Volume 63, Number 5. Pages 277–293
- **Ссылка:** https://snap.stanford.edu/class/cs224w-readings/cartwright56balance.pdf
- **Место в источнике:** страница 284
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 660](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L660)

### 1.18. Mark S. Granovetter — Г10 [9]

> "the strength of a tie is a (probably linear) combination of the amount of time, the emotional intensity, the intimacy (mutual confiding), and the reciprocal services which characterize the tie." [9]

- **Перевод:** «сила связи есть (вероятно, линейная) комбинация количества времени, эмоциональной интенсивности, близости (взаимного доверительного общения) и взаимных услуг, характеризующих связь». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 679](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L679))
- **Интерпретация для репутационных технологий:** Грановеттер даёт операционализацию дистанции через время, эмоциональную интенсивность, доверительность и взаимные услуги. В GRA это одна из осей многомерной дистанции, по которой близость связи можно описать словами; линейность комбинации сам автор оговаривает лишь как вероятную. [9]
- **Авторы:** Mark S. Granovetter
- **Дата:** май 1973
- **Источник:** The Strength of Weak Ties // American Journal of Sociology. 1973. Volume 78, Number 6. Pages 1360–1380
- **Ссылка:** https://www.jstor.org/stable/2776392
- **Место в источнике:** страница 1361
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 678](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L678)

### 1.19. Mark S. Granovetter — Г10 [9]

> "Ties discussed in this paper are assumed to be positive and symmetric; a comprehensive theory might require discussion of negative and/or asymmetric ties…" [9]

- **Перевод:** «Обсуждаемые в статье связи предполагаются положительными и симметричными; всеобъемлющая теория, возможно, потребовала бы рассмотрения отрицательных и/или асимметричных связей…» (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 681](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L681))
- **Интерпретация для репутационных технологий:** Важная оговорка самого Грановеттера: он рассматривает только положительные и симметричные связи. Поэтому Полярность GRA и направленность связи он не обосновывает — для знака курс опирается на Хайдера и на Картрайта с Харари. [9]
- **Авторы:** Mark S. Granovetter
- **Дата:** май 1973
- **Источник:** The Strength of Weak Ties // American Journal of Sociology. 1973. Volume 78, Number 6. Pages 1360–1380
- **Ссылка:** https://www.jstor.org/stable/2776392
- **Место в источнике:** страница 1361, сноска 2
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 680](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L680)

### 1.20. Mark S. Granovetter — Г10 [9]

> "What is important, rather, is that all bridges are weak ties." [9]

- **Перевод:** «Важно, скорее, то, что все мосты являются слабыми связями». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 683](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L683))
- **Интерпретация для репутационных технологий:** Тезис о мостах как слабых связях предупреждает: большая дистанция не означает меньшей ценности связи, через дальние знакомства открываются новые круги. Для репутационной практики это довод не отбрасывать слабые связи; поправки о нелинейности и об отраслях курс берёт из работы Rajkumar и соавторов [9]
- **Авторы:** Mark S. Granovetter
- **Дата:** май 1973
- **Источник:** The Strength of Weak Ties // American Journal of Sociology. 1973. Volume 78, Number 6. Pages 1360–1380
- **Ссылка:** https://www.jstor.org/stable/2776392
- **Место в источнике:** страница 1364
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 682](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L682)

### 1.21. Roger C. Mayer и соавторы — Г11 [10]

> "The definition of trust proposed in this research is the willingness of a party to be vulnerable to the actions of another party based on the expectation that the other will perform a particular action important to the trustor, irrespective of the ability to monitor or control that other party." [10]

- **Перевод:** «Предлагаемое в данном исследовании определение доверия — это готовность стороны быть уязвимой перед действиями другой стороны на основе ожидания, что та совершит определённое действие, важное для доверяющего, независимо от возможности контролировать или отслеживать эту другую сторону». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 702](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L702))
- **Интерпретация для репутационных технологий:** Классическое определение доверия как готовности быть уязвимым без возможности контроля — опора оси доверия в многомерной дистанции GRA (до правки #659 дистанция понималась как обратное доверию). Практику оно напоминает: доверие — это принятие риска, а не просто симпатия. [10]
- **Авторы:** Roger C. Mayer; James H. Davis; F. David Schoorman
- **Дата:** 1995
- **Источник:** An Integrative Model of Organizational Trust // Academy of Management Review. 1995. Volume 20, Number 3. Pages 709–734
- **Ссылка:** https://www.jstor.org/stable/258792
- **Место в источнике:** страница 712
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 701](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L701)

### 1.22. Roger C. Mayer и соавторы — Г11 [10]

> "three characteristics of a trustee appear often in the literature: ability, benevolence, and integrity." [10]

- **Перевод:** «в литературе часто фигурируют три характеристики того, кому доверяют: способности, благожелательность и добросовестность». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 704](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L704))
- **Интерпретация для репутационных технологий:** Способности, благожелательность и добросовестность дают практику готовый чек-лист для разбора связи. Они же показывают ограничение: доверие многомерно, и сведение его к одному скаляру расстояния — упрощение, которое в курсе нужно оговаривать. [10]
- **Авторы:** Roger C. Mayer; James H. Davis; F. David Schoorman
- **Дата:** 1995
- **Источник:** An Integrative Model of Organizational Trust // Academy of Management Review. 1995. Volume 20, Number 3. Pages 709–734
- **Ссылка:** https://www.jstor.org/stable/258792
- **Место в источнике:** страница 717
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 703](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L703)

### 1.23. Charles J. Fombrun — Г12 [11]

> "the set of values and principles employees and managers associate with the company" [11]

- **Перевод:** «совокупность ценностей и принципов, которые сотрудники и менеджеры связывают с компанией». (Перевод наш, [2026-09-30-course-sources-and-presentations-650.md, строка 721](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L721))
- **Интерпретация для репутационных технологий:** Здесь Фомбрун определяет корпоративную идентичность — ценности и принципы, связываемые с компанией изнутри, — а не саму репутацию. Цитата приведена по статье Barnett и соавторов; книгу о репутационном капитале как «Массе» узла в курсе лучше цитировать через проверенные вторичные источники или сверить по печатному экземпляру. [11]
- **Авторы:** Charles J. Fombrun; цитата приведена по статье Michael L. Barnett, John M. Jermier, Barbara A. Lafferty
- **Дата:** 1996 (книга); 2006 (вторичный источник)
- **Источник:** Reputation: Realizing Value from the Corporate Image. Boston, Massachusetts: Harvard Business School Press, 1996, цитируется по: Corporate Reputation: The Definitional Landscape // Corporate Reputation Review. 2006. Volume 9, Number 1. Page 29
- **Ссылка:** https://www.mv.helsinki.fi/home/aula/Top20/corp-reputation-definitional-landscape.pdf
- **Место в источнике:** Barnett и соавторы, 2006, страница 29 (Fombrun 1996, страница 36)
- **Статус проверки:** VERIFIED-SECONDARY
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 720](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L720)

### 1.24. Michael L. Barnett и соавторы — Г13 [12]

> "Corporate Reputation: Observers' collective judgments of a corporation based on assessments of the financial, social, and environmental impacts attributed to the corporation over time." [12]

- **Перевод:** «Корпоративная репутация — коллективные суждения наблюдателей о корпорации, основанные на оценках финансовых, социальных и экологических последствий, приписываемых корпорации, на протяжении времени». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 730](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L730))
- **Интерпретация для репутационных технологий:** Определение разводит репутацию как коллективное суждение наблюдателей и репутационный капитал как актив, причём суждение складывается из финансовых, социальных и экологических последствий во времени. Ограничение для GRA: это оценка многими наблюдателями, а не парная сила между двумя узлами. [12]
- **Авторы:** Michael L. Barnett; John M. Jermier; Barbara A. Lafferty
- **Дата:** 2006
- **Источник:** Corporate Reputation: The Definitional Landscape // Corporate Reputation Review. 2006. Volume 9, Number 1. Pages 26–38
- **Ссылка:** https://www.mv.helsinki.fi/home/aula/Top20/corp-reputation-definitional-landscape.pdf
- **Место в источнике:** страница 34
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 729](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L729)

### 1.25. Michael L. Barnett и соавторы — Г13 [12]

> "As judgments of the firm accumulate over time, reputation capital ebbs and flows." [12]

- **Перевод:** «По мере того как суждения о фирме накапливаются во времени, репутационный капитал то убывает, то прибывает». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 732](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L732))
- **Интерпретация для репутационных технологий:** Формула «ebbs and flows» обосновывает в GRA «Массу» как репутационный капитал, меняющийся во времени: он накапливается и тратится через суждения. На эту опору вместе с данными Edelman курс ставит метафору «доверие — новая валюта», которая остаётся гипотезой. [12]
- **Авторы:** Michael L. Barnett; John M. Jermier; Barbara A. Lafferty
- **Дата:** 2006
- **Источник:** Corporate Reputation: The Definitional Landscape // Corporate Reputation Review. 2006. Volume 9, Number 1. Pages 26–38
- **Ссылка:** https://www.mv.helsinki.fi/home/aula/Top20/corp-reputation-definitional-landscape.pdf
- **Место в источнике:** страница 34
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 731](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L731)

### 1.26. Когденко Вера Геннадьевна — Г14 [13]

> «Социально-репутационный капитал – это репутация компании в глазах стейкхолдеров. Это социальные связи, являющиеся ресурсом для получения выгод, которые способствуют созданию стоимости. Ключевой элемент социально-репутационного капитала – это доверие, то есть оправданные ожидания стейкхолдеров…» [13]

- **Интерпретация для репутационных технологий:** Когденко соединяет в одном определении репутацию, социальные связи и доверие как ключевой элемент — то есть «Массу» и «Дистанцию» GRA. Это близкая русскоязычная опора тезиса «репутационный капитал — это связи»; ограничение — работа об анализе отчётности, количественной формулы сил в ней нет. [13]
- **Авторы:** Когденко Вера Геннадьевна
- **Дата:** 2016
- **Источник:** Анализ интегрированной отчетности: социально-репутационный капитал // Экономический анализ: теория и практика. 2016. Номер 6 (453). Страницы 100–114
- **Ссылка:** https://cyberleninka.ru/article/n/analiz-integrirovannoy-otchetnosti-sotsialno-reputatsionnyy-kapital
- **Место в источнике:** страница 101
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 745](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L745)

### 1.27. Когденко Вера Геннадьевна — Г14 [13]

> «отношения (связи) между основными заинтересованными сторонами, а также доверие и готовность сотрудничать…» [13]

- **Интерпретация для репутационных технологий:** Перечень элементов — отношения между заинтересованными сторонами, доверие, готовность сотрудничать — по сути описывает те связи, которые GRA предлагает картировать. Для разговора с финансистами это мост от отчётности к связям, но сетевой модели и расчёта сил здесь нет. [13]
- **Авторы:** Когденко Вера Геннадьевна
- **Дата:** 2016
- **Источник:** Анализ интегрированной отчетности: социально-репутационный капитал // Экономический анализ: теория и практика. 2016. Номер 6 (453). Страницы 100–114
- **Ссылка:** https://cyberleninka.ru/article/n/analiz-integrirovannoy-otchetnosti-sotsialno-reputatsionnyy-kapital
- **Место в источнике:** страница 101, пункт перечня по стандарту IIRC
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 746](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L746)

### 1.28. Шагеева Гульнара Рафаиловна — Г15 [14]

> «репутация — фундаментальный инструмент социального порядка, основанный на распределенном, спонтанном социальном контроле. Это мнение об объекте, обычно являющееся результатом социальной оценки по набору критериев, таких как поведение или производительность.» [14]

- **Интерпретация для репутационных технологий:** Шагеева описывает репутацию как инструмент распределённого социального контроля и как оценку по набору критериев. В репозитории источник поддерживает перенос «Массы» между узлом-человеком и компанией; ограничение — цитируемое определение задаёт оценку, а не силу взаимодействия. [14]
- **Авторы:** Шагеева Гульнара Рафаиловна
- **Дата:** 2024
- **Источник:** Репутационный капитал личности в деловой среде и его влияние на репутацию компании // Вестник Московского университета. Серия 6. Экономика. 2024. Том 59, номер 4. Страницы 293–312
- **Ссылка:** https://doi.org/10.55959/MSU0130-0105-6-59-4-13
- **Место в источнике:** страница 296
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 758](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L758)

### 1.29. Claudio Castellano и соавторы — Г16 [15]

> "Therefore any modeling of social agents inevitably involves a huge and unwarranted simplification of the real problem." [15]

- **Перевод:** «Поэтому любое моделирование социальных агентов неизбежно предполагает огромное и неоправданное упрощение реальной проблемы». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 774](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L774))
- **Интерпретация для репутационных технологий:** Обзор по статистической физике социальной динамики сам признаёт: моделирование социальных агентов — огромное упрощение. Это обязательная оговорка курса: физические аналогии допустимы как язык и метафора сети, но буквальная «физика репутации» ими не подкреплена. [15]
- **Авторы:** Claudio Castellano; Santo Fortunato; Vittorio Loreto
- **Дата:** 2009
- **Источник:** Statistical Physics of Social Dynamics // Reviews of Modern Physics. 2009. Volume 81, Number 2. Pages 591–646
- **Ссылка:** https://doi.org/10.1103/RevModPhys.81.591
- **Место в источнике:** arXiv, раздел I "Introduction", страница 2
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 773](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L773)

### 1.30. Claudio Castellano и соавторы — Г16 [15]

> "The critique that models used by physicists to describe social systems are too simplified to describe any real situation is most of the times very well grounded." [15]

- **Перевод:** «Критика того, что модели, используемые физиками для описания социальных систем, слишком упрощены, чтобы описать какую-либо реальную ситуацию, в большинстве случаев вполне обоснована». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 776](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L776))
- **Интерпретация для репутационных технологий:** Признание физиков, что критика их социальных моделей в большинстве случаев обоснована, — сильный аргумент лектора против завышенных ожиданий от GRA. Поэтому модель подаётся как набор вопросов-ограничителей для разбора связей, а не как расчёт силы. [15]
- **Авторы:** Claudio Castellano; Santo Fortunato; Vittorio Loreto
- **Дата:** 2009
- **Источник:** Statistical Physics of Social Dynamics // Reviews of Modern Physics. 2009. Volume 81, Number 2. Pages 591–646
- **Ссылка:** https://doi.org/10.1103/RevModPhys.81.591
- **Место в источнике:** arXiv, страница 2
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 775](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L775)

### 1.31. Claudio Castellano и соавторы — Г16 [15]

> "People have used the social network metaphor for over a century to represent complex sets of relationships between members of social systems at all scales, from interpersonal to international." [15]

- **Перевод:** «Метафору социальной сети используют уже более века для представления сложных совокупностей отношений между членами социальных систем на всех масштабах, от межличностного до международного». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 778](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L778))
- **Интерпретация для репутационных технологий:** Метафора социальной сети используется больше века и на всех масштабах — от межличностного до международного. Это легитимирует сетевой язык курса: картировать связи компаний так же правомерно, как связи людей; граница прежняя — сеть как язык и метафора, а не физический закон. [15]
- **Авторы:** Claudio Castellano; Santo Fortunato; Vittorio Loreto
- **Дата:** 2009
- **Источник:** Statistical Physics of Social Dynamics // Reviews of Modern Physics. 2009. Volume 81, Number 2. Pages 591–646
- **Ссылка:** https://doi.org/10.1103/RevModPhys.81.591
- **Место в источнике:** arXiv, страница 6
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 777](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L777)

### 1.32. Somin Wadhwa и соавторы — Н5 [16]

> "Few-shot prompting with GPT-3 achieves near SOTA performance, i.e., roughly equivalent to existing fully supervised models". [16]

- **Перевод:** «Few-shot промптинг GPT-3 дает результат, близкий к лучшему известному, то есть примерно равный полностью обученным моделям». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1467](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1467))
- **Интерпретация для репутационных технологий:** Извлечение сущностей и связей из текстов промптом реалистично: few-shot подход в эксперименте сопоставим с полностью обученными моделями. На это опирается машинная сборка карты связей в курсе; ограничение — это бенчмарки 2023 года (GPT-3, Flan-T5), а не русские новостные тексты. [16]
- **Авторы:** Somin Wadhwa; Silvio Amir; Byron C. Wallace
- **Дата:** 2023 (версия arXiv v2 — 16 июля 2024)
- **Источник:** Revisiting Relation Extraction in the Era of Large Language Models // Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL 2023). arXiv:2305.05003
- **Ссылка:** https://arxiv.org/pdf/2305.05003
- **Место в источнике:** Abstract, страница 1
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1466](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1466)

### 1.33. Somin Wadhwa и соавторы — Н5 [16]

> "We address issues inherent to evaluating generative approaches to RE by doing human evaluations, in lieu of relying on exact matching." [16]

- **Перевод:** «Проблемы оценки генеративного извлечения отношений мы решаем оценкой людьми вместо точного совпадения». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1469](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1469))
- **Интерпретация для репутационных технологий:** Даже исследователи извлечения отношений не полагаются на автоматическое сравнение и проверяют результат людьми. Для репутационного аналитика вывод прямой: карту связей, собранную ИИ, проверяет человек, и это нужно заложить в упражнение заранее. [16]
- **Авторы:** Somin Wadhwa; Silvio Amir; Byron C. Wallace
- **Дата:** 2023 (версия arXiv v2 — 16 июля 2024)
- **Источник:** Revisiting Relation Extraction in the Era of Large Language Models // Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL 2023). arXiv:2305.05003
- **Ссылка:** https://arxiv.org/pdf/2305.05003
- **Место в источнике:** Abstract, страница 1
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1468](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1468)

### 1.34. Somin Wadhwa и соавторы — Н5 [16]

> "we observe a non-trivial number of invalid or empty output instances (∼10.6% of all generated sequences). These results highlight a remaining limitation of in-context learning with large language models: for datasets with long texts or a large number of targets, it is not possible to fit detailed instructions in the prompt." [16]

- **Перевод:** «мы наблюдаем заметную долю некорректных или пустых выводов (~10,6% всех сгенерированных последовательностей). Это показывает сохраняющееся ограничение: для длинных текстов или большого числа целевых отношений подробные инструкции не помещаются в промпт». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1471](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1471))
- **Интерпретация для репутационных технологий:** Около 10,6% некорректных или пустых ответов — реалистичная норма брака при машинном извлечении связей. Курс берёт это как предупреждение: граф сущностей из текстов — рабочая технология, но с ошибками, а на длинных текстах и при многих целях подробные инструкции в промпт не помещаются. [16]
- **Авторы:** Somin Wadhwa; Silvio Amir; Byron C. Wallace
- **Дата:** 2023 (версия arXiv v2 — 16 июля 2024)
- **Источник:** Revisiting Relation Extraction in the Era of Large Language Models // Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL 2023). arXiv:2305.05003
- **Ссылка:** https://arxiv.org/pdf/2305.05003
- **Место в источнике:** раздел 3.3, страница 4
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1470](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1470)

### 1.35. Edelman — М1 [17]

> "Sixty-one percent globally have a moderate or high sense of grievance…" [17]

- **Перевод:** «В мире 61 % людей испытывают умеренное или сильное чувство обиды…» (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Данные Edelman 2025 показывают дефицит доверия: большинство опрошенных несут умеренное или сильное чувство несправедливости, а люди с сильным таким чувством не доверяют ни одному из четырёх институтов. В курсе это мотив слайда 6 и одна из опор метафоры «доверие — новая валюта»; цифра взята по пересказу IPAA Queensland, сайт Edelman был недоступен. [17]
- **Авторы:** Edelman (организация-автор исследования); изложение: Institute of Public Administration Australia, Queensland
- **Дата:** январь 2025
- **Источник:** 2025 Edelman Trust Barometer: Trust and the Crisis of Grievance — изложение Institute of Public Administration Australia, Queensland
- **Ссылка:** https://qld.ipaa.org.au/2025/02/2025-edelman-trust-barometer-trust-and-the-crisis-of-grievance
- **Место в источнике:** изложение отчёта, абзац о чувстве обиды
- **Статус проверки:** VERIFIED-SECONDARY
- **Где в репозитории:** [day-01/rationale-and-method.md, строка 458](../day-01/rationale-and-method.md#L458)

### 1.36. Edelman — М2 [18]

> "Seven out of 10 say they are either unwilling or hesitant to trust someone with different values" [18]

- **Перевод:** «семь из десяти не готовы или не решаются доверять человеку с другими ценностями» (Перевод наш, [day-01/rationale-and-method.md, строка 77](../day-01/rationale-and-method.md#L77))
- **Интерпретация для репутационных технологий:** Edelman 2026 фиксирует замыкание доверия в своих кругах: большинство не готово доверять людям с другими ценностями. Вывод курса — доверие не исчезло, а распределено по узким кругам, и выигрывает тот, кто знает, через какие связи туда попасть. Цитата по пересказу O'Dwyer's. [18]
- **Авторы:** Edelman (организация-автор исследования); цитата о посреднике доверия — Richard Edelman, генеральный директор Edelman; изложение: O'Dwyer's
- **Дата:** январь 2026 (статья O'Dwyer's — 20 января 2026)
- **Источник:** 2026 Edelman Trust Barometer — изложение в статье «National Insularity Threatens Global Economy», O'Dwyer's
- **Ссылка:** https://www.odwyerpr.com/story/public/24179/2026-01-20/national-insularity-threatens-global-economy.html
- **Место в источнике:** изложение отчёта
- **Статус проверки:** VERIFIED-SECONDARY
- **Где в репозитории:** [day-01/rationale-and-method.md, строка 459](../day-01/rationale-and-method.md#L459)

### 1.37. Edelman — М2 [18]

> "leading trust broker" [18]

- **Перевод:** «ведущий посредник доверия» (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Работодатель как ведущий «посредник доверия» — пример узла, через который доверие попадает в узкий круг. В Дне 1 это часть аргумента о сжатии доверия до «своих» (слайд 6); формулировка принадлежит Ричарду Эдельману и известна по пересказу O'Dwyer's. [18]
- **Авторы:** Edelman (организация-автор исследования); цитата о посреднике доверия — Richard Edelman, генеральный директор Edelman; изложение: O'Dwyer's
- **Дата:** январь 2026 (статья O'Dwyer's — 20 января 2026)
- **Источник:** 2026 Edelman Trust Barometer — изложение в статье «National Insularity Threatens Global Economy», O'Dwyer's
- **Ссылка:** https://www.odwyerpr.com/story/public/24179/2026-01-20/national-insularity-threatens-global-economy.html
- **Место в источнике:** слова Ричарда Эдельмана о работодателе (My Employer)
- **Статус проверки:** VERIFIED-SECONDARY
- **Где в репозитории:** [day-01/rationale-and-method.md, строка 459](../day-01/rationale-and-method.md#L459)

### 1.38. Klaudia Jaźwińska и соавторы — М3 [19]

> "Collectively, they provided incorrect answers to more than 60 percent of queries" [19]

- **Перевод:** «В совокупности они дали неверные ответы более чем на 60 процентов запросов» (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Tow Center показал, что восемь ИИ-поисковиков в совокупности ошибались более чем в 60% запросов. Для репутации это значит: образ компании всё чаще собирает машинный посредник, и если компания не понимает своих связей, образ соберут неточно. Цифры остаются в обосновании, на экран слайда не выносятся. [19]
- **Авторы:** Klaudia Jaźwińska; Aisvarya Chandrasekar
- **Дата:** 6 марта 2025
- **Источник:** AI Search Has a Citation Problem // Columbia Journalism Review, Tow Center for Digital Journalism
- **Ссылка:** https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php
- **Место в источнике:** основные выводы исследования
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [day-01/rationale-and-method.md, строка 460](../day-01/rationale-and-method.md#L460)

### 1.39. Klaudia Jaźwińska и соавторы — М3 [19]

> "with alarming confidence, rarely using qualifying phrases" [19]

- **Перевод:** «с пугающей уверенностью, редко прибегая к оговоркам» (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Опасна не только ошибка, но и уверенный тон без оговорок. Отсюда правило курса: черновик ИИ — полезная заготовка, которую проверяют по guardrails GRA, а связь без основания получает «?», а не статус факта. [19]
- **Авторы:** Klaudia Jaźwińska; Aisvarya Chandrasekar
- **Дата:** 6 марта 2025
- **Источник:** AI Search Has a Citation Problem // Columbia Journalism Review, Tow Center for Digital Journalism
- **Ссылка:** https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php
- **Место в источнике:** основные выводы исследования
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [day-01/rationale-and-method.md, строка 460](../day-01/rationale-and-method.md#L460)

### 1.40. Darren Edge и соавторы — М4 [20]

> "first, to derive an entity knowledge graph from the source documents, then to pregenerate community summaries…" [20]

- **Перевод:** «сначала построить из исходных документов граф знаний о сущностях, затем заранее сгенерировать сводки по сообществам…» (перевод наш (#711))
- **Интерпретация для репутационных технологий:** GraphRAG строит из документов граф знаний о сущностях, а затем сводки по сообществам — машина уже умеет собирать карту связей из текстов. Для курса это довод, что разведка связей подешевела и стала доступна МСП, а не только компаниям с аналитическим отделом. [20]
- **Авторы:** Darren Edge; Ha Trinh; Newman Cheng; Joshua Bradley; Alex Chao; Apurva Mody; Steven Truitt; Dasha Metropolitansky; Robert Osazuwa Ness; Jonathan Larson
- **Дата:** апрель 2024 (версия 2 — 19 февраля 2025)
- **Источник:** From Local to Global: A Graph RAG Approach to Query-Focused Summarization. arXiv:2404.16130
- **Ссылка:** https://arxiv.org/abs/2404.16130
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED-FULLTEXT (аннотация)
- **Где в репозитории:** [day-01/rationale-and-method.md, строка 461](../day-01/rationale-and-method.md#L461)

### 1.41. Darren Edge и соавторы — М4 [20]

> "substantial improvements over a conventional RAG baseline for both the comprehensiveness and diversity" [20]

- **Перевод:** «существенные улучшения по сравнению с обычной базовой RAG-системой и по полноте, и по разнообразию» (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Прирост полноты и разнообразия ответов против обычного RAG подтверждает практическую ценность графового представления знаний. Статус в курсе — перенос практики: граф сущностей из текстов работает, но с ошибками, поэтому его вывод требует проверки человеком. [20]
- **Авторы:** Darren Edge; Ha Trinh; Newman Cheng; Joshua Bradley; Alex Chao; Apurva Mody; Steven Truitt; Dasha Metropolitansky; Robert Osazuwa Ness; Jonathan Larson
- **Дата:** апрель 2024 (версия 2 — 19 февраля 2025)
- **Источник:** From Local to Global: A Graph RAG Approach to Query-Focused Summarization. arXiv:2404.16130
- **Ссылка:** https://arxiv.org/abs/2404.16130
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED-FULLTEXT (аннотация)
- **Где в репозитории:** [day-01/rationale-and-method.md, строка 461](../day-01/rationale-and-method.md#L461)

### 1.42. Chris McKay — М5 [21]

> "takes between 5 to 30 minutes… browsing through hundreds of online sources" [21]

- **Перевод:** «занимает от 5 до 30 минут… просматривая сотни онлайн-источников» (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Исследовательский агент за минуты просматривает сотни источников, поэтому подготовка к первому разговору с картой окружения партнёра стала доступна МСП за вечер. Цитата взята по пересказу Maginative, страница OpenAI была недоступна. [21]
- **Авторы:** Chris McKay
- **Дата:** 2 февраля 2025
- **Источник:** OpenAI Unveils Deep Research, an AI Agent That Conducts Multi-Step Research Tasks // Maginative
- **Ссылка:** https://www.maginative.com/article/openai-unveils-deep-research-an-ai-agent-that-conducts-multi-step-research-tasks/
- **Место в источнике:** описание работы агента
- **Статус проверки:** VERIFIED-SECONDARY
- **Где в репозитории:** [day-01/rationale-and-method.md, строка 462](../day-01/rationale-and-method.md#L462)

### 1.43. Chris McKay — М5 [21]

> "can still produce hallucinations and struggles with distinguishing authoritative information from less reliable sources" [21]

- **Перевод:** «всё ещё может выдавать галлюцинации и с трудом отличает авторитетную информацию от менее надёжных источников» (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Галлюцинации и неумение отличить авторитетный источник от ненадёжного — причина, по которой GRA в курсе подаётся как guardrails для ИИ. Без модели, которая задаёт вопросы и ставит «?», вечер с агентом превращается в сбор уверенных выдумок; источник вторичный — Maginative. [21]
- **Авторы:** Chris McKay
- **Дата:** 2 февраля 2025
- **Источник:** OpenAI Unveils Deep Research, an AI Agent That Conducts Multi-Step Research Tasks // Maginative
- **Ссылка:** https://www.maginative.com/article/openai-unveils-deep-research-an-ai-agent-that-conducts-multi-step-research-tasks/
- **Место в источнике:** ограничения агента
- **Статус проверки:** VERIFIED-SECONDARY
- **Где в репозитории:** [day-01/rationale-and-method.md, строка 462](../day-01/rationale-and-method.md#L462)

### 1.44. Karthik Rajkumar и соавторы — М6 [22]

> "inverted U-shaped relationship between tie strength and job transmission…" [22]

- **Перевод:** «перевёрнутая U-образная зависимость между силой связи и передачей информации о вакансиях…» (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Перевёрнутая U-образная зависимость уточняет Грановеттера: слабые связи помогают, но слишком слабая связь уже не работает. Для GRA это довод не постулировать «слабые связи всегда лучше», а спрашивать о дистанции конкретной связи; цитата взята из аннотации работы. [22]
- **Авторы:** Karthik Rajkumar; Guillaume Saint-Jacques; Iavor Bojinov; Erik Brynjolfsson; Sinan Aral
- **Дата:** 16 сентября 2022
- **Источник:** A Causal Test of the Strength of Weak Ties // Science. 2022. Volume 377, Number 6612
- **Ссылка:** https://doi.org/10.1126/science.abl4476
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED-FULLTEXT (аннотация)
- **Где в репозитории:** [day-01/rationale-and-method.md, строка 463](../day-01/rationale-and-method.md#L463)

### 1.45. Karthik Rajkumar и соавторы — М6 [22]

> "weak ties increased job mobility in more digital industries, strong ties increased job mobility in less digital industries" [22]

- **Перевод:** «слабые связи повышали трудовую мобильность в более цифровых отраслях, сильные — в менее цифровых» (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Для аудитории курса — нефтегаз, ОПК, банки, МСП у госзаказа и в рознице — это важная поправка: в менее цифровых отраслях сильные связи могут решать больше. На кейсе 1 розничная сеть как раз такая отрасль: давний поставщик может весить для категорийного менеджера больше десятка знакомств по выставке. [22]
- **Авторы:** Karthik Rajkumar; Guillaume Saint-Jacques; Iavor Bojinov; Erik Brynjolfsson; Sinan Aral
- **Дата:** 16 сентября 2022
- **Источник:** A Causal Test of the Strength of Weak Ties // Science. 2022. Volume 377, Number 6612
- **Ссылка:** https://doi.org/10.1126/science.abl4476
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED-FULLTEXT (аннотация)
- **Где в репозитории:** [day-01/rationale-and-method.md, строка 463](../day-01/rationale-and-method.md#L463)

### 1.46. Heinrich Peters и соавторы — М7 [23]

> "average correlation of r = .29 (range = [.22, .33]) between LLM-inferred and self-reported trait scores" [23]

- **Перевод:** «средняя корреляция r = 0,29 (диапазон [0,22; 0,33]) между оценками черт, выведенными LLM, и самоотчётом» (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Корреляция около 0,29 между выводами модели о чертах личности и самоотчётом показывает, насколько ненадёжно ИИ «читает» человека по текстам. Поэтому в курсе портрет ЛПР — гипотеза низкой уверенности (guardrail 6): подсказка для темы и тона первого письма, а не основание для решения. [23]
- **Авторы:** Heinrich Peters; Sandra C. Matz
- **Дата:** 31 мая 2024
- **Источник:** Large Language Models Can Infer Psychological Dispositions of Social Media Users // PNAS Nexus (Proceedings of the National Academy of Sciences Nexus). 2024. Препринт arXiv:2309.08631
- **Ссылка:** https://arxiv.org/abs/2309.08631
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED-FULLTEXT (аннотация arXiv)
- **Где в репозитории:** [day-01/rationale-and-method.md, строка 464](../day-01/rationale-and-method.md#L464)

### 1.47. Heinrich Peters и соавторы — М7 [23]

> "raises ethical concerns regarding user privacy and self-determination" [23]

- **Перевод:** «вызывает этические вопросы о приватности и самоопределении пользователей» (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Этические вопросы о приватности и самоопределении задают границу сбора данных о людях. Репутационный инженер изучает профессиональную роль ЛПР, но не его частную жизнь — семью, здоровье, перемещения вне профессиональных событий, что в курсе связано и со ст. 152.2 ГК РФ. [23]
- **Авторы:** Heinrich Peters; Sandra C. Matz
- **Дата:** 31 мая 2024
- **Источник:** Large Language Models Can Infer Psychological Dispositions of Social Media Users // PNAS Nexus (Proceedings of the National Academy of Sciences Nexus). 2024. Препринт arXiv:2309.08631
- **Ссылка:** https://arxiv.org/abs/2309.08631
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED-FULLTEXT (аннотация arXiv)
- **Где в репозитории:** [day-01/rationale-and-method.md, строка 464](../day-01/rationale-and-method.md#L464)

### 1.48. Filippo Simini и соавторы — R:Simini [24]

> "Despite its widespread use, it relies on adjustable parameters that vary from region to region" [24]

- **Перевод:** «Несмотря на широкое применение, она опирается на настраиваемые параметры, которые меняются от региона к региону» (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Simini и соавторы указывают слабость гравитационной модели мобильности: её параметры приходится подгонять под каждый регион. Для программы GRA это предупреждение, что гравитационная форма не универсальна и без калибровки на данных её коэффициенты ничего не гарантируют. [24]
- **Авторы:** Filippo Simini; Marta C. González; Amos Maritan; Albert-László Barabási
- **Дата:** 2012
- **Источник:** A Universal Model for Mobility and Migration Patterns // Nature. 2012. Volume 484. Pages 96–100. arXiv:1111.0586
- **Ссылка:** https://arxiv.org/abs/1111.0586
- **Место в источнике:** Abstract (о гравитационной модели)
- **Статус проверки:** VERIFIED-FULLTEXT (аннотация arXiv)
- **Где в репозитории:** [methodology/research-program/50-open-research.md, строка 117](../../../methodology/research-program/50-open-research.md#L117)

### 1.49. Filippo Simini и соавторы — R:Simini [24]

> "Given its parameter-free nature, the model can be applied in areas where we lack previous mobility measurements" [24]

- **Перевод:** «Поскольку модель не требует параметров, её можно применять там, где прежних измерений мобильности нет» (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Модель радиации без подгоночных параметров иллюстрирует второй исход переноса физических аналогий: гравитацию можно заменить конкурирующей структурой, которая объясняет данные лучше. В исследовательской программе GRA на этом стоит гипотеза о конкурентных возможностях — взаимодействие зависит и от числа альтернатив между узлами; её статус — непроверенная гипотеза. [24]
- **Авторы:** Filippo Simini; Marta C. González; Amos Maritan; Albert-László Barabási
- **Дата:** 2012
- **Источник:** A Universal Model for Mobility and Migration Patterns // Nature. 2012. Volume 484. Pages 96–100. arXiv:1111.0586
- **Ссылка:** https://arxiv.org/abs/1111.0586
- **Место в источнике:** Abstract (о модели излучения)
- **Статус проверки:** VERIFIED-FULLTEXT (аннотация arXiv)
- **Где в репозитории:** [methodology/research-program/50-open-research.md, строка 117](../../../methodology/research-program/50-open-research.md#L117)

### 1.50. Dedre Gentner — R:Gentner [25]

> "Argues that the core of analogy is the mapping of relationships" [25]

- **Перевод:** «Утверждает, что ядро аналогии — перенос отношений» (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Ключевая идея для принципа структурного соответствия GRA: в аналогии переносятся отношения между объектами, а не их свойства. Из гравитации берутся не «масса как вещество» и не «расстояние в метрах», а отношения вроде «взаимодействие убывает с разделённостью»; формулировка — слова обзора CogSci Summaries, а не самой Гентнер. [25]
- **Авторы:** Dedre Gentner; обзор — CogSci Summaries (сайт Jim Davies)
- **Дата:** 1983
- **Источник:** Structure-Mapping: A Theoretical Framework for Analogy // Cognitive Science. 1983. Volume 7, Number 2. Pages 155–170, цитируется по обзору CogSci Summaries
- **Ссылка:** https://www.jimdavies.org/summaries/gentner1983.html
- **Место в источнике:** обзор CogSci Summaries
- **Статус проверки:** VERIFIED-SECONDARY (слова обзора, а не Гентнер)
- **Где в репозитории:** [methodology/research-program/50-open-research.md, строка 118](../../../methodology/research-program/50-open-research.md#L118)

### 1.51. Dedre Gentner — R:Gentner [25]

> "the key to analogy is not just relationships but systems of interconnected relationships" [25]

- **Перевод:** «ключ к аналогии — не просто отношения, а системы взаимосвязанных отношений» (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Перенос систем взаимосвязанных отношений, а не отдельных связей, объясняет устройство GRA: из гравитации берётся связанная структура — рост взаимодействия с характеристиками обоих узлов, убывание с разделённостью, направление, — и каждое отношение проверяется как отдельная гипотеза. Цитата — пересказ обзора, первоисточник не извлечён. [25]
- **Авторы:** Dedre Gentner; обзор — CogSci Summaries (сайт Jim Davies)
- **Дата:** 1983
- **Источник:** Structure-Mapping: A Theoretical Framework for Analogy // Cognitive Science. 1983. Volume 7, Number 2. Pages 155–170, цитируется по обзору CogSci Summaries
- **Ссылка:** https://www.jimdavies.org/summaries/gentner1983.html
- **Место в источнике:** обзор CogSci Summaries
- **Статус проверки:** VERIFIED-SECONDARY (слова обзора, а не Гентнер)
- **Где в репозитории:** [methodology/research-program/50-open-research.md, строка 118](../../../methodology/research-program/50-open-research.md#L118)

### 1.52. Catherine H. Crouch и соавторы — П1 [26]

> "A class taught with PI is divided into a series of short presentations, each focused on a central point and followed by a related conceptual question, called a ConcepTest ... Students are given one or two minutes to formulate individual answers and report their answers to the instructor." [26]

- **Перевод:** «Занятие по PI делится на серию коротких изложений, каждое с одной центральной мыслью, за которым следует концептуальный вопрос (ConcepTest)... Студентам дают одну-две минуты на индивидуальный ответ, который они сообщают преподавателю». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1585](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1585))
- **Интерпретация для репутационных технологий:** Каркас Peer Instruction — короткое изложение одной мысли, концептуальный вопрос и минута-две на индивидуальный ответ — основа ритма Дня 1 для молчаливой вечерней аудитории. В курсе это голосования в чате с закрытым выбором «А или Б»; ограничение — данные получены на студентах-физиках Гарварда. [26]
- **Авторы:** Catherine H. Crouch; Eric Mazur
- **Дата:** сентябрь 2001
- **Источник:** Peer Instruction: Ten Years of Experience and Results // American Journal of Physics. 2001. Volume 69, Number 9. Pages 970–977
- **Ссылка:** https://doi.org/10.1119/1.1374249
- **Место в источнике:** страница 970
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1584](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1584)

### 1.53. Catherine H. Crouch и соавторы — П1 [26]

> "the more structured questioning process of PI involves every student in the class." [26]

- **Перевод:** «более структурированный процесс вопросов в PI вовлекает каждого студента». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1587](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1587))
- **Интерпретация для репутационных технологий:** Структурированный вопрос вовлекает каждого, а не только самых смелых. Для взрослой онлайн-аудитории с выключенными камерами это довод заменить открытый вопрос закрытым выбором в чате: ответ одной буквой занимает секунды и ощущается анонимным. [26]
- **Авторы:** Catherine H. Crouch; Eric Mazur
- **Дата:** сентябрь 2001
- **Источник:** Peer Instruction: Ten Years of Experience and Results // American Journal of Physics. 2001. Volume 69, Number 9. Pages 970–977
- **Ссылка:** https://doi.org/10.1119/1.1374249
- **Место в источнике:** страница 970
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1586](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1586)

### 1.54. Catherine H. Crouch и соавторы — П1 [26]

> "after discussion, the number of students who give the correct answer to a ConcepTest increases substantially, as long as the initial percentage of correct answers to a ConcepTest is between 35% and 70%." [26]

- **Перевод:** «после обсуждения число правильных ответов существенно растет, если исходная доля правильных ответов была от 35% до 70%». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1589](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1589))
- **Интерпретация для репутационных технологий:** Правило 35–70% помогает калибровать сложность кейс-вопросов: слишком лёгкий или слишком трудный вопрос не даёт эффекта обсуждения. В Дне 1 из него выведено правило лектора: если больше 70% выберут вариант Б, в финале спрашивать не «что», а «почему». [26]
- **Авторы:** Catherine H. Crouch; Eric Mazur
- **Дата:** сентябрь 2001
- **Источник:** Peer Instruction: Ten Years of Experience and Results // American Journal of Physics. 2001. Volume 69, Number 9. Pages 970–977
- **Ссылка:** https://doi.org/10.1119/1.1374249
- **Место в источнике:** страница 972
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1588](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1588)

### 1.55. Catherine H. Crouch и соавторы — П1 [26]

> "incorrect answer choices should be plausible, and, when possible, based on typical student misunderstandings." [26]

- **Перевод:** «неправильные варианты ответа должны быть правдоподобными и по возможности основанными на типичных заблуждениях». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1591](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1591))
- **Интерпретация для репутационных технологий:** Правдоподобные неверные варианты, построенные на типичных заблуждениях, превращают голосование в диагностику аудитории. Для курса это подсказка строить варианты ответа на привычных представлениях слушателей — например, на «оптике образа», которую День 1 предлагает сменить взглядом на связи. [26]
- **Авторы:** Catherine H. Crouch; Eric Mazur
- **Дата:** сентябрь 2001
- **Источник:** Peer Instruction: Ten Years of Experience and Results // American Journal of Physics. 2001. Volume 69, Number 9. Pages 970–977
- **Ссылка:** https://doi.org/10.1119/1.1374249
- **Место в источнике:** страница 974
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1590](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1590)

### 1.56. Catherine H. Crouch и соавторы — П1 [26]

> "We typically devote one-third to one-half of class time to ConcepTests and spend the remainder lecturing." [26]

- **Перевод:** «Обычно мы отводим на ConcepTest от трети до половины времени занятия, остальное — лекция». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1593](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1593))
- **Интерпретация для репутационных технологий:** Мазур отдаёт вопросам от трети до половины занятия, и День 1 сознательно идёт ниже — около 21% времени на интерактив, потому что фаундер выбрал простую подачу, а глубина уходит в ссылки. Цитата задаёт ориентир, от которого курс отступает осознанно. [26]
- **Авторы:** Catherine H. Crouch; Eric Mazur
- **Дата:** сентябрь 2001
- **Источник:** Peer Instruction: Ten Years of Experience and Results // American Journal of Physics. 2001. Volume 69, Number 9. Pages 970–977
- **Ссылка:** https://doi.org/10.1119/1.1374249
- **Место в источнике:** страница 975 (раздел F "Time management")
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1592](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1592)

### 1.57. Catherine H. Crouch и соавторы — П1 [26]

> "find the main advantages of the network are anonymity of student responses and data collection; our experience indicates that the success of Peer Instruction does not depend on a particular feedback method." [26]

- **Перевод:** «главные преимущества электронной системы — анонимность ответов и сбор данных; по нашему опыту, успех Peer Instruction не зависит от конкретного способа обратной связи». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1595](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1595))
- **Интерпретация для репутационных технологий:** Анонимность ответов названа главным преимуществом электронной системы, а успех метода не зависит от конкретного канала связи. Это обосновывает чат вместо голоса: онлайн достаточно ответа буквой, специальные пульты не нужны. Данные получены на студентах вуза, а не на корпоративной аудитории. [26]
- **Авторы:** Catherine H. Crouch; Eric Mazur
- **Дата:** сентябрь 2001
- **Источник:** Peer Instruction: Ten Years of Experience and Results // American Journal of Physics. 2001. Volume 69, Number 9. Pages 970–977
- **Ссылка:** https://doi.org/10.1119/1.1374249
- **Место в источнике:** страница 976, примечание 9
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1594](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1594)

### 1.58. Scott Freeman и соавторы — П2 [27]

> "average examination scores improved by about 6% in active learning sections, and that students in classes with traditional lecturing were 1.5 times more likely to fail than were students in classes with active learning." [27]

- **Перевод:** «средние экзаменационные баллы в группах с активным обучением выросли примерно на 6%, а студенты на традиционных лекциях в 1,5 раза чаще не сдавали курс». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1605](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1605))
- **Интерпретация для репутационных технологий:** Метаанализ даёт измеримый эффект активного обучения: выше баллы и реже неудачи, чем на традиционной лекции. В курсе это доказательная база формата «лекция плюс совместный разбор кейса»; ограничение — студенты бакалавриата STEM в США, а не взрослые специалисты. [27]
- **Авторы:** Scott Freeman; Sarah L. Eddy; Miles McDonough; Michelle K. Smith; Nnadozie Okoroafor; Hannah Jordt; Mary Pat Wenderoth
- **Дата:** 2014
- **Источник:** Active Learning Increases Student Performance in Science, Engineering, and Mathematics // Proceedings of the National Academy of Sciences of the United States of America. 2014. Volume 111, Number 23. Pages 8410–8415
- **Ссылка:** https://doi.org/10.1073/pnas.1319030111
- **Место в источнике:** Abstract, страница 8410
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1604](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1604)

### 1.59. Scott Freeman и соавторы — П2 [27]

> "Active learning engages students in the process of learning through activities and/or discussion in class, as opposed to passively listening to an expert. It emphasizes higher-order thinking and often involves group work." [27]

- **Перевод:** «Активное обучение вовлекает учащихся в процесс учения через деятельность и/или обсуждение на занятии, в противоположность пассивному слушанию эксперта. Оно делает упор на мышление высокого порядка и часто включает групповую работу». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1607](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1607))
- **Интерпретация для репутационных технологий:** Определение активного обучения через деятельность и обсуждение вместо пассивного слушания задаёт критерий для каждого отрезка Дня 1: он заканчивается действием слушателя — выбором, пробой промпта или вопросом к своей карте связей. [27]
- **Авторы:** Scott Freeman; Sarah L. Eddy; Miles McDonough; Michelle K. Smith; Nnadozie Okoroafor; Hannah Jordt; Mary Pat Wenderoth
- **Дата:** 2014
- **Источник:** Active Learning Increases Student Performance in Science, Engineering, and Mathematics // Proceedings of the National Academy of Sciences of the United States of America. 2014. Volume 111, Number 23. Pages 8410–8415
- **Ссылка:** https://doi.org/10.1073/pnas.1319030111
- **Место в источнике:** Раздел "Materials and Methods" (в HTML PMC нет номеров страниц)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1606](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1606)

### 1.60. Scott Freeman и соавторы — П2 [27]

> "the time devoted to active learning was highly variable in the studies analyzed here, ranging from just 10–15% of class time being devoted to clicker questions to lecture-free “studio” environments, we were not able to evaluate the relationship between the intensity (or type) of active learning and student performance". [27]

- **Перевод:** «доля времени на активное обучение сильно различалась — от 10–15% времени на вопросы с пультами до занятий вообще без лекций; связь интенсивности (или типа) активного обучения с результатами мы оценить не смогли». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1609](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1609))
- **Интерпретация для репутационных технологий:** Честная оговорка метаанализа: оптимальная доля интерактива им не определена. Поэтому лектор не может ссылаться на Freeman и соавторов ради конкретного процента — доля интерактива в Дне 1 остаётся проектным решением, а не выводом из данных. [27]
- **Авторы:** Scott Freeman; Sarah L. Eddy; Miles McDonough; Michelle K. Smith; Nnadozie Okoroafor; Hannah Jordt; Mary Pat Wenderoth
- **Дата:** 2014
- **Источник:** Active Learning Increases Student Performance in Science, Engineering, and Mathematics // Proceedings of the National Academy of Sciences of the United States of America. 2014. Volume 111, Number 23. Pages 8410–8415
- **Ссылка:** https://doi.org/10.1073/pnas.1319030111
- **Место в источнике:** Раздел "Discussion"
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1608](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1608)

### 1.61. Neil A. Bradbury — П3 [28]

> "the available primary data do not support the concept of a 10- to 15-min attention limit. Interestingly, the most consistent finding from a literature review is that the greatest variability in student attention arises from differences between teachers and not from the teaching format itself." [28]

- **Перевод:** «имеющиеся первичные данные не подтверждают идею предела внимания в 10–15 минут. Самый устойчивый вывод обзора: больше всего внимание студентов зависит от преподавателя, а не от формата занятия». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1619](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1619))
- **Интерпретация для репутационных технологий:** Bradbury опровергает популярный «лимит внимания в 10–15 минут» и показывает, что внимание сильнее зависит от преподавателя, чем от формата. В курсе ритм задаётся смыслом, а не таймером: смена активности полезна, но не из-за мифического лимита. [28]
- **Авторы:** Neil A. Bradbury
- **Дата:** декабрь 2016
- **Источник:** Attention Span During Lectures: 8 Seconds, 10 Minutes, or More? // Advances in Physiology Education. 2016. Volume 40, Number 4. Pages 509–513
- **Ссылка:** https://doi.org/10.1152/advan.00109.2016
- **Место в источнике:** Abstract, страница 509
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1618](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1618)

### 1.62. Neil A. Bradbury — П3 [28]

> "there is no reason why students attending a lecture cannot be part of the lecture. This is probably best exemplified by the use of “clickers” that allow the students to answer questions posed by the teacher." [28]

- **Перевод:** «нет причин, по которым слушатели лекции не могут стать ее частью; лучший пример — "кликеры", позволяющие отвечать на вопросы преподавателя». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1621](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1621))
- **Интерпретация для репутационных технологий:** Слушатели могут стать частью лекции через кликеры — в онлайн-курсе их роль играют голосования в чате. Это подкрепляет решение Дня 1 встроить в лекцию короткие закрытые вопросы, а не отказываться от лекционного формата. [28]
- **Авторы:** Neil A. Bradbury
- **Дата:** декабрь 2016
- **Источник:** Attention Span During Lectures: 8 Seconds, 10 Minutes, or More? // Advances in Physiology Education. 2016. Volume 40, Number 4. Pages 509–513
- **Ссылка:** https://doi.org/10.1152/advan.00109.2016
- **Место в источнике:** страница 512
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1620](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1620)

### 1.63. Neil A. Bradbury — П3 [28]

> "Attention by students can also be seriously hampered by teachers merely reading long tracts of projected text." [28]

- **Перевод:** «Внимание студентов может серьезно страдать, когда преподаватель просто зачитывает длинные фрагменты текста со слайдов». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1623](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1623))
- **Интерпретация для репутационных технологий:** Чтение длинного текста со слайда вредит вниманию. Отсюда правило презентаций курса: слайд несёт один тезис и одну картинку, а текст не дублирует речь лектора; вывод согласуется с эффектом избыточности у Mayer и Moreno. [28]
- **Авторы:** Neil A. Bradbury
- **Дата:** декабрь 2016
- **Источник:** Attention Span During Lectures: 8 Seconds, 10 Minutes, or More? // Advances in Physiology Education. 2016. Volume 40, Number 4. Pages 509–513
- **Ссылка:** https://doi.org/10.1152/advan.00109.2016
- **Место в источнике:** страница 512
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1622](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1622)

### 1.64. Neil A. Bradbury — П3 [28]

> "Clearly, the notion that lectures should be dismissed because students have only a 10- to 15-min attention span is erroneous and has little if any data to support it." [28]

- **Перевод:** «Очевидно, мнение, что от лекций надо отказаться, потому что внимание студентов длится лишь 10–15 минут, ошибочно и почти не имеет подтверждения в данных». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1625](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1625))
- **Интерпретация для репутационных технологий:** Тезис о коротком внимании как причине отказаться от лекций почти не подтверждён данными. Лектор может сохранить лекционное ядро 90-минутного занятия, встраивая интерактив по смыслу, а не дробя материал по таймеру. [28]
- **Авторы:** Neil A. Bradbury
- **Дата:** декабрь 2016
- **Источник:** Attention Span During Lectures: 8 Seconds, 10 Minutes, or More? // Advances in Physiology Education. 2016. Volume 40, Number 4. Pages 509–513
- **Ссылка:** https://doi.org/10.1152/advan.00109.2016
- **Место в источнике:** страница 512
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1624](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1624)

### 1.65. Richard E. Mayer и соавторы — П4 [29]

> "coherence effect: Students understand a multimedia explanation better when interesting but extraneous material is excluded rather than included." [29]

- **Перевод:** «эффект связности: учащиеся лучше понимают мультимедийное объяснение, когда интересный, но посторонний материал исключен, а не включен». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1635](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1635))
- **Интерпретация для репутационных технологий:** Эффект связности — правило убирать со слайдов интересное, но постороннее: декоративные картинки и побочные подробности. С ним согласуется решение Дня 1 держать цифры Tow Center в обосновании, а не на экране; данные получены в лабораторных опытах со студентами и короткими анимациями. [29]
- **Авторы:** Richard E. Mayer; Roxana Moreno
- **Дата:** 2003
- **Источник:** Nine Ways to Reduce Cognitive Load in Multimedia Learning // Educational Psychologist. 2003. Volume 38, Number 1. Pages 43–52
- **Ссылка:** https://doi.org/10.1207/S15326985EP3801_6
- **Место в источнике:** страница 48
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1634](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1634)

### 1.66. Richard E. Mayer и соавторы — П4 [29]

> "cognitive load can be reduced by providing cues to the learner about how to select and organize the material—a technique called signaling". [29]

- **Перевод:** «когнитивную нагрузку можно снизить, давая учащемуся подсказки, как отбирать и упорядочивать материал, — прием "сигнализации"». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1637](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1637))
- **Интерпретация для репутационных технологий:** Сигнализация — подсказки, что выделить и как упорядочить материал, — снижает когнитивную нагрузку; на слайдах о GRA это выделенный тезис и явная связь с кейсом. Сами авторы признают, что по сигнализации у них лишь одно предварительное исследование. [29]
- **Авторы:** Richard E. Mayer; Roxana Moreno
- **Дата:** 2003
- **Источник:** Nine Ways to Reduce Cognitive Load in Multimedia Learning // Educational Psychologist. 2003. Volume 38, Number 1. Pages 43–52
- **Ссылка:** https://doi.org/10.1207/S15326985EP3801_6
- **Место в источнике:** страница 48 (Solution: Signaling)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1636](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1636)

### 1.67. Richard E. Mayer и соавторы — П4 [29]

> "redundancy effect: Students understand a multimedia presentation better when words are presented as narration rather than as narration and on-screen text." [29]

- **Перевод:** «эффект избыточности: учащиеся лучше понимают презентацию, когда слова звучат как устный рассказ, а не как рассказ плюс тот же текст на экране». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1639](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1639))
- **Интерпретация для репутационных технологий:** Эффект избыточности прямо обосновывает запрет читать текст со слайда: слова лучше воспринимаются голосом, чем голосом и тем же текстом на экране. В презентациях Дня 1 текст не повторяет речь; вывод согласуется с наблюдением Bradbury. [29]
- **Авторы:** Richard E. Mayer; Roxana Moreno
- **Дата:** 2003
- **Источник:** Nine Ways to Reduce Cognitive Load in Multimedia Learning // Educational Psychologist. 2003. Volume 38, Number 1. Pages 43–52
- **Ссылка:** https://doi.org/10.1207/S15326985EP3801_6
- **Место в источнике:** страница 49
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1638](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1638)

### 1.68. Richard E. Mayer и соавторы — П4 [29]

> "In segmenting, the presentation is broken down into bite-size segments." [29]

- **Перевод:** «При сегментации изложение разбивается на небольшие порции». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1641](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1641))
- **Интерпретация для репутационных технологий:** Сегментация — изложение небольшими порциями — ложится на устройство Дня 1, где слайд со связью несёт утверждение, опору, применение к кейсу и переход. Опора скромная: по сегментации у авторов одно предварительное исследование. [29]
- **Авторы:** Richard E. Mayer; Roxana Moreno
- **Дата:** 2003
- **Источник:** Nine Ways to Reduce Cognitive Load in Multimedia Learning // Educational Psychologist. 2003. Volume 38, Number 1. Pages 43–52
- **Ссылка:** https://doi.org/10.1207/S15326985EP3801_6
- **Место в источнике:** страница 47 (Solution: Segmenting)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1640](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1640)

### 1.69. Richard E. Mayer и соавторы — П4 [29]

> "In some cases when we report only a single preliminary study (i.e., segmenting, signaling, and aligning) more empirical research is needed." [29]

- **Перевод:** «В случаях, когда у нас лишь одно предварительное исследование (сегментация, сигнализация, выравнивание), нужны дополнительные эмпирические данные». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1643](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1643))
- **Интерпретация для репутационных технологий:** Mayer и Moreno сами предупреждают, что для сегментации, сигнализации и выравнивания нужны дополнительные данные. Лектору это напоминание подавать эти приёмы как разумные правила оформления слайдов, а не как доказанные законы восприятия. [29]
- **Авторы:** Richard E. Mayer; Roxana Moreno
- **Дата:** 2003
- **Источник:** Nine Ways to Reduce Cognitive Load in Multimedia Learning // Educational Psychologist. 2003. Volume 38, Number 1. Pages 43–52
- **Ссылка:** https://doi.org/10.1207/S15326985EP3801_6
- **Место в источнике:** страница 51 (ограничение)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1642](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1642)

### 1.70. Лукашевич Денис Анатольевич — П7 [30]

> «Исследование Ноэль-Нойман показало, что каждый человек формирует свое представление об общественном мнении, но сам ограничивает себя в высказываниях, опасаясь вступать в конфликт с доминирующим в обществе мнением, поскольку это может вызвать неодобрение его окружения и, как следствие, изоляцию.» [30]

- **Интерпретация для репутационных технологий:** Объяснение молчания аудитории: люди молчат не от незнания, а из страха разойтись с мнением большинства — в зале это часто начальник или самый уверенный коллега. Отсюда анонимный закрытый выбор до обсуждения; это пересказ Лукашевича, а не цитата Ноэль-Нойман, и перенос на учебную группу — аналогия курса. [30]
- **Авторы:** Лукашевич Денис Анатольевич
- **Дата:** 2013
- **Источник:** Применимость теории «спирали молчания» к сети Интернет и новым медиа // Вестник Новосибирского государственного университета. Серия: История, филология. 2013. Том 12, выпуск 6: Журналистика. Страницы 61–66
- **Ссылка:** https://cyberleninka.ru/article/n/primenimost-teorii-spirali-molchaniya-k-seti-internet-i-novym-media
- **Место в источнике:** страницы 61–62
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1661](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1661)

### 1.71. Ван Цзэкай и соавторы — П8 [31]

> «индивиды, опасаясь социальной изоляции, склоняются к присоединению к доминирующим мнениям. Если человек осознает, что его точка зрения является меньшинственной и непопулярной, он с большей вероятностью будет сохранять молчание в публичных местах». [31]

- **Интерпретация для репутационных технологий:** Свежий русский пересказ спирали молчания: осознавая свою позицию как непопулярную, человек склонен молчать публично. Для курса это довод снижать цену высказывания и брать кейсы, близкие к работе участников, — по упомянутой в статье критике, при личной заинтересованности страх изоляции слабее. Слова принадлежат авторам статьи, а не Ноэль-Нойман. [31]
- **Авторы:** Ван Цзэкай (Zekai Wang); Курышева Юлия Владимировна; Никонов Сергей Борисович
- **Дата:** декабрь 2025
- **Источник:** Концепция «спирали молчания» в контексте политической коммуникации // Litera. 2025. Номер 12. Страницы 240–254
- **Ссылка:** https://doi.org/10.25136/2409-8698.2025.12.77540
- **Место в источнике:** страница 243
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1669](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1669)

### 1.72. Ибрагимов Гасангусейн Ибрагимович — П9 [32]

> «Имитационная образовательная модель направлена на развитие у обучающихся практических умений по использованию сформированного посредством семиотической модели знания. Для этого предполагается моделирование в образовательном процессе ситуаций профессиональной деятельности посредством включения в учебный процесс решения ситуационных задач и проблем, метода проектов, анализа реальных ситуаций (кейс-стади), мозгового штурма и др.» [32]

- **Интерпретация для репутационных технологий:** Имитационная модель в изложении Ибрагимова даёт российскую рамку для формата «лекция, затем совместный разбор кейса»: знание из лекции отрабатывается на ситуациях профессиональной деятельности. Это слова Ибрагимова о Вербицком, а не цитата Вербицкого; первоисточник 1991 года не проверен. [32]
- **Авторы:** Ибрагимов Гасангусейн Ибрагимович (о дидактическом наследии Вербицкого Андрея Александровича)
- **Дата:** 2021
- **Источник:** Дидактическое наследие А. А. Вербицкого и современность: к 80-летию со дня рождения // Казанский педагогический журнал. 2021. Номер 4. Страницы 7–12
- **Ссылка:** https://doi.org/10.51379/KPJ.2021.148.4.001
- **Место в источнике:** страница 9
- **Статус проверки:** VERIFIED-FULLTEXT (слова Ибрагимова, а не Вербицкого)
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1678](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1678)

### 1.73. Ибрагимов Гасангусейн Ибрагимович — П9 [32]

> «ведущей роли совместной деятельности, межличностного взаимодействия и диалогического общения субъектов образовательного процесса – обучающих и обучающихся». [32]

- **Интерпретация для репутационных технологий:** Принцип ведущей роли совместной деятельности и диалога оправдывает в курсе работу участников со своими картами связей и ответы в чате, а не только монолог лектора. Формулировка принадлежит Ибрагимову, излагающему принципы контекстного обучения Вербицкого. [32]
- **Авторы:** Ибрагимов Гасангусейн Ибрагимович (о дидактическом наследии Вербицкого Андрея Александровича)
- **Дата:** 2021
- **Источник:** Дидактическое наследие А. А. Вербицкого и современность: к 80-летию со дня рождения // Казанский педагогический журнал. 2021. Номер 4. Страницы 7–12
- **Ссылка:** https://doi.org/10.51379/KPJ.2021.148.4.001
- **Место в источнике:** Среди принципов контекстного обучения
- **Статус проверки:** VERIFIED-FULLTEXT (слова Ибрагимова, а не Вербицкого)
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1679](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1679)
- **Примечание:** Слова Г. И. Ибрагимова о принципах контекстного обучения А. А. Вербицкого.

### 1.74. Лазарева Анна Сергеевна — П10 [33]

> «корпоративное обучение предполагает проведение работы с профессионально успешными людьми, которые отличаются ответственностью и устоявшимися ценностями, мировоззрением (Алямкина, Рибокене, Флеров, 2020)». [33]

- **Интерпретация для репутационных технологий:** Корпоративная аудитория — профессионально успешные люди с устоявшимися ценностями и мировоззрением. Лектору по репутационным технологиям это напоминание опираться на опыт PR- и GR-специалистов, а не учить их с нуля; источник — статья об обучении иностранным языкам, без экспериментальных данных. [33]
- **Авторы:** Лазарева Анна Сергеевна
- **Дата:** май 2025
- **Источник:** Особенности применения технологии активного обучения в иноязычной подготовке взрослых в корпоративной среде // Педагогика. Вопросы теории и практики. 2025. Том 10, выпуск 5. Страницы 640–648
- **Ссылка:** https://doi.org/10.30853/ped20250077
- **Место в источнике:** страница 641
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1688](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1688)

### 1.75. Лазарева Анна Сергеевна — П10 [33]

> «(4) учет психологических барьеров (тревожность, недостаток уверенности, ограниченность свободного времени и др.) и использование специальных методов для их преодоления (основу составляют активные методы – ролевые игры, симуляции, проектная деятельность)». [33]

- **Интерпретация для репутационных технологий:** Тревожность, неуверенность и нехватка свободного времени названы барьерами, которые снимаются активными методами. Для вечерней онлайн-аудитории курса это объяснение молчания и обоснование коротких действий вместо открытой дискуссии; ограничение — теоретико-методическая работа, перенос на корпоративный класс — вывод курса. [33]
- **Авторы:** Лазарева Анна Сергеевна
- **Дата:** май 2025
- **Источник:** Особенности применения технологии активного обучения в иноязычной подготовке взрослых в корпоративной среде // Педагогика. Вопросы теории и практики. 2025. Том 10, выпуск 5. Страницы 640–648
- **Ссылка:** https://doi.org/10.30853/ped20250077
- **Место в источнике:** страница 645
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1689](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1689)

## День 2. Достоверность данных, разведывательный анализ и работа с ИИ

### 2.1. Luc Moreau и соавторы — Д1 [34]

> "Provenance is information about entities, activities, and people involved in producing a piece of data or thing, which can be used to form assessments about its quality, reliability or trustworthiness." [34]

- **Перевод:** «Происхождение (provenance) — это информация о сущностях, действиях и людях, участвовавших в создании фрагмента данных или объекта. Её можно использовать для оценки его качества, надёжности или заслуживающей доверия природы». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 849](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L849))
- **Интерпретация для репутационных технологий:** Определение W3C связывает происхождение данных с оценкой их качества и надёжности — на нём курс строит провенанс: кто, когда и каким действием создал утверждение. В репутационном отчёте это значит, что каждая цифра и каждое утверждение должны идти вместе с источником; ограничение — PROV лишь модель описания происхождения, статусов достоверности в ней нет. [34]
- **Авторы:** Luc Moreau; Paolo Missier (редакторы рекомендации)
- **Дата:** 30 апреля 2013
- **Источник:** PROV-DM: The PROV Data Model / edited by Luc Moreau, Paolo Missier. World Wide Web Consortium Recommendation, 30 April 2013
- **Ссылка:** https://www.w3.org/TR/2013/REC-prov-dm-20130430/
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 848](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L848)

### 2.2. Luc Moreau и соавторы — Д1 [34]

> "For many purposes, a key consideration for deciding whether something is reliable and/or trustworthy is knowing who or what was reponsible for its production." [34]

- **Перевод:** «Во многих случаях ключевое соображение при решении, надёжно ли что-либо и можно ли ему доверять, — знание того, кто или что отвечало за его создание». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 853](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L853))
- **Интерпретация для репутационных технологий:** Доверие к сведению начинается с вопроса, кто или что отвечало за его создание, — отсюда поле «Источник» в реестре утверждений Дня 2. Практику полезно помнить: двадцать перепостов не добавляют автора, поэтому без восстановленного ответственного звена утверждение остаётся PARTIAL; сами статусы — конструкция курса, в PROV их нет. [34]
- **Авторы:** Luc Moreau; Paolo Missier (редакторы рекомендации)
- **Дата:** 30 апреля 2013
- **Источник:** PROV-DM: The PROV Data Model / edited by Luc Moreau, Paolo Missier. World Wide Web Consortium Recommendation, 30 April 2013
- **Ссылка:** https://www.w3.org/TR/2013/REC-prov-dm-20130430/
- **Место в источнике:** §2.1.3
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 851](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L851)

### 2.3. Luc Moreau и соавторы — Д1 [34]

> "A primary source for a topic refers to something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight." [34]

- **Перевод:** «Первичный источник по теме — это то, что создано агентом, имеющим непосредственный опыт и знание предмета, во время изучения темы, без преимуществ ретроспективного взгляда». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 855](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L855))
- **Интерпретация для репутационных технологий:** Определение первичного источника курс переносит в колонку «Первичный или пересказ»: первичен тот, у кого был непосредственный опыт и кто писал без ретроспективы. Пресс-релиз сети о себе — первичный, пересказ в СМИ или чате — уже нет, и цепочку происхождения нужно восстанавливать назад до звена с автором и датой. [34]
- **Авторы:** Luc Moreau; Paolo Missier (редакторы рекомендации)
- **Дата:** 30 апреля 2013
- **Источник:** PROV-DM: The PROV Data Model / edited by Luc Moreau, Paolo Missier. World Wide Web Consortium Recommendation, 30 April 2013
- **Ссылка:** https://www.w3.org/TR/2013/REC-prov-dm-20130430/
- **Место в источнике:** §5.2.4
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 854](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L854)

### 2.4. Office of the Director of National Intelligence — Д2 [35]

> "Analysis should be informed by all relevant information available. Analytic elements should identify and address critical information gaps" [35]

- **Перевод:** «Анализ должен опираться на всю доступную релевантную информацию. Аналитические подразделения должны выявлять критические информационные пробелы и работать с ними». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 871](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L871))
- **Интерпретация для репутационных технологий:** Стандарт ICD 203 требует не только собрать доступное, но и явно назвать критические пробелы. Для репутационного аналитика это опора статуса PARTIAL: пробел показывается в отчёте, а не замалчивается. Ограничение — документ регулирует разведаналитику США и служит курсу аналогией, ярлыков PARTIAL/CONFLICT в нём нет. [35]
- **Авторы:** Office of the Director of National Intelligence (Управление директора национальной разведки США); подписал James R. Clapper
- **Дата:** вступила в силу 2 января 2015
- **Источник:** Intelligence Community Directive 203: Analytic Standards
- **Ссылка:** https://www.dni.gov/files/documents/ICD/ICD-203.pdf
- **Место в источнике:** страница 4, D.6.d
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 870](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L870)

### 2.5. Office of the Director of National Intelligence — Д2 [35]

> "Analytic products should identify underlying sources and methodologies upon which judgments are based" [35]

- **Перевод:** «В аналитических продуктах следует указывать источники и методологии, на которых основаны суждения». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 873](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L873))
- **Интерпретация для репутационных технологий:** Требование указывать источники и методологию, на которых держится суждение, — самое сильное нормативное обоснование правила «утверждение → источник → дата → статус». Репутационный отчёт без перечня источников и способа их отбора по этому стандарту неполон; при этом ICD 203 — аналогия из разведаналитики, а не корпоративная норма. [35]
- **Авторы:** Office of the Director of National Intelligence (Управление директора национальной разведки США); подписал James R. Clapper
- **Дата:** вступила в силу 2 января 2015
- **Источник:** Intelligence Community Directive 203: Analytic Standards
- **Ссылка:** https://www.dni.gov/files/documents/ICD/ICD-203.pdf
- **Место в источнике:** страница 4, D.6.e(1)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 872](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L872)

### 2.6. Office of the Director of National Intelligence — Д2 [35]

> "Analytic products should indicate and explain the basis for the uncertainties associated with major analytic judgments, specifically the likelihood of occurrence of an event or development, and the analyst's confidence in the basis for this judgment." [35]

- **Перевод:** «Аналитические продукты должны указывать и объяснять основания неопределённости основных аналитических суждений: вероятность события или развития ситуации и уверенность аналитика в основаниях этого суждения». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 876](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L876))
- **Интерпретация для репутационных технологий:** Неопределённость главных выводов нужно не прятать, а объяснять: насколько вероятно событие и насколько уверен аналитик в основаниях. Курс использует это как довод за явные статусы данных вместо гладкой итоговой оценки; сам ICD 203 выражает неопределённость вероятностями и уровнем уверенности, а не метками курса. [35]
- **Авторы:** Office of the Director of National Intelligence (Управление директора национальной разведки США); подписал James R. Clapper
- **Дата:** вступила в силу 2 января 2015
- **Источник:** Intelligence Community Directive 203: Analytic Standards
- **Ссылка:** https://www.dni.gov/files/documents/ICD/ICD-203.pdf
- **Место в источнике:** страница 5, D.6.e(2)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 875](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L875)

### 2.7. Office of the Director of National Intelligence — Д2 [35]

> "Analytic products should clearly distinguish statements that convey underlying intelligence information used in analysis from statements that convey assumptions or judgments." [35]

- **Перевод:** «Аналитические продукты должны чётко отличать утверждения, передающие исходную информацию, от утверждений, выражающих допущения или суждения». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 879](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L879))
- **Интерпретация для репутационных технологий:** На этом требовании стоит второй принцип записи провенанса: сведение и суждение — разные строки реестра. «Пресс-релиз опубликован» — исходная информация, «матрица открыта» — уже интерпретация; смешивая их, репутационный отчёт выдаёт догадку за факт. [35]
- **Авторы:** Office of the Director of National Intelligence (Управление директора национальной разведки США); подписал James R. Clapper
- **Дата:** вступила в силу 2 января 2015
- **Источник:** Intelligence Community Directive 203: Analytic Standards
- **Ссылка:** https://www.dni.gov/files/documents/ICD/ICD-203.pdf
- **Место в источнике:** страница 5, D.6.e(3)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 878](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L878)

### 2.8. Office of the Director of National Intelligence — Д2 [35]

> "Products should be internally consistent and acknowledge significant supporting and contrary information affecting judgments." [35]

- **Перевод:** «Продукты должны быть внутренне непротиворечивы и признавать существенную подтверждающую и противоречащую информацию, влияющую на суждения». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 881](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L881))
- **Интерпретация для репутационных технологий:** Признавать и подтверждающую, и противоречащую информацию — основа тезиса «среднее стирает расхождение». Если пресс-релиз и пост в чате говорят разное, честная запись — CONFLICT с причиной, а не усреднённая оценка «частично открыто»; прямого запрета усреднять метрики в стандарте нет, это вывод курса. [35]
- **Авторы:** Office of the Director of National Intelligence (Управление директора национальной разведки США); подписал James R. Clapper
- **Дата:** вступила в силу 2 января 2015
- **Источник:** Intelligence Community Directive 203: Analytic Standards
- **Ссылка:** https://www.dni.gov/files/documents/ICD/ICD-203.pdf
- **Место в источнике:** страница 6, D.6.e(6)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 880](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L880)

### 2.9. Office of the Director of National Intelligence — Д2 [35]

> "Significant differences in analytic judgment, such as between two IC analytic elements, should be fully considered and brought to the attention of customers." [35]

- **Перевод:** «Существенные расхождения в аналитических суждениях, например между двумя подразделениями разведсообщества, должны быть полностью рассмотрены и доведены до сведения заказчиков». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 883](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L883))
- **Интерпретация для репутационных технологий:** Расхождения между аналитиками или источниками доводятся до заказчика, а не сглаживаются, — так курс обосновывает метку CONFLICT в отчёте для руководителя. Практический вывод: заказчик репутационного анализа должен видеть, где источники спорят; стандарт при этом относится к разведсообществу США и используется как аналогия. [35]
- **Авторы:** Office of the Director of National Intelligence (Управление директора национальной разведки США); подписал James R. Clapper
- **Дата:** вступила в силу 2 января 2015
- **Источник:** Intelligence Community Directive 203: Analytic Standards
- **Ссылка:** https://www.dni.gov/files/documents/ICD/ICD-203.pdf
- **Место в источнике:** страница 6, D.6.e(7)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 882](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L882)

### 2.10. Richards J. Heuer, Jr. — Д3 [36]

> "Once an experienced analyst has the minimum information necessary to make an informed judgment, obtaining additional information generally does not improve the accuracy of his or her estimates. Additional information does, however, lead the analyst to become more confident in the judgment, to the point of overconfidence." [36]

- **Перевод:** «Когда у опытного аналитика есть минимум информации для обоснованного суждения, дополнительная информация, как правило, не повышает точность его оценок. Однако она повышает его уверенность в суждении — вплоть до чрезмерной самоуверенности». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 898](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L898))
- **Интерпретация для репутационных технологий:** Эмпирический аргумент для правила «источник важнее объёма»: сверх минимума информации растёт уверенность аналитика, но не точность. На Дне 2 это гипотеза Г2-1 — 72% позитива или тысячи просмотров делают нас увереннее, а по происхождению могут оказаться одним источником; книга о разведаналитике, перенос на мониторинг — аналогия. [36]
- **Авторы:** Richards J. Heuer, Jr.
- **Дата:** 1999
- **Источник:** Psychology of Intelligence Analysis. Washington, District of Columbia: Center for the Study of Intelligence, Central Intelligence Agency, 1999
- **Ссылка:** https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf
- **Место в источнике:** страница 52 (PDF 80), глава 5
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 897](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L897)

### 2.11. Richards J. Heuer, Jr. — Д3 [36]

> "Analysis of competing hypotheses (ACH) requires an analyst to explicitly identify all the reasonable alternatives and have them compete against each other for the analyst's favor, rather than evaluating their plausibility one at a time." [36]

- **Перевод:** «Анализ конкурирующих гипотез (ACH) требует явно определить все разумные альтернативы и заставить их состязаться друг с другом, а не оценивать правдоподобие каждой по отдельности». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 900](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L900))
- **Интерпретация для репутационных технологий:** Метод конкурирующих гипотез требует явно выписать все разумные объяснения и сравнивать их между собой, а не проверять каждое по отдельности. Для репутационного анализа это способ не влюбиться в первую версию «почему так пишут о компании»; курс опирается на ACH и в шаге «гипотезы» между качественными и количественными данными. [36]
- **Авторы:** Richards J. Heuer, Jr.
- **Дата:** 1999
- **Источник:** Psychology of Intelligence Analysis. Washington, District of Columbia: Center for the Study of Intelligence, Central Intelligence Agency, 1999
- **Ссылка:** https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf
- **Место в источнике:** страница 95 (PDF 123), глава 8
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 899](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L899)

### 2.12. Richards J. Heuer, Jr. — Д3 [36]

> "Note the absence of evidence as well as its presence." [36]

- **Перевод:** «Отмечайте не только наличие свидетельств, но и их отсутствие». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 902](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L902))
- **Интерпретация для репутационных технологий:** Короткое правило Хойера курс превращает в продолжение принципа Дня 1 «„?“ — не 0»: отсутствие данных записывается как наблюдение. Пустой веб-архив фиксируется как «снимков нет», а не как вывод о компании, и такая строка получает PARTIAL. [36]
- **Авторы:** Richards J. Heuer, Jr.
- **Дата:** 1999
- **Источник:** Psychology of Intelligence Analysis. Washington, District of Columbia: Center for the Study of Intelligence, Central Intelligence Agency, 1999
- **Ссылка:** https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf
- **Место в источнике:** страница 99 (PDF 127)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 901](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L901)

### 2.13. Richards J. Heuer, Jr. — Д3 [36]

> "If an item of evidence seems consistent with all the hypotheses, it may have no diagnostic value." [36]

- **Перевод:** «Если свидетельство согласуется со всеми гипотезами, оно может не иметь диагностической ценности». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 904](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L904))
- **Интерпретация для репутационных технологий:** Свидетельство, совместимое со всеми гипотезами, ничего не различает — так курс операционально определяет шум. Рост упоминаний или общий позитив часто подходят к любому объяснению репутационной ситуации, поэтому в отчёте их нельзя выдавать за подтверждение конкретной версии. [36]
- **Авторы:** Richards J. Heuer, Jr.
- **Дата:** 1999
- **Источник:** Psychology of Intelligence Analysis. Washington, District of Columbia: Center for the Study of Intelligence, Central Intelligence Agency, 1999
- **Ссылка:** https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf
- **Место в источнике:** страница 102 (PDF 130)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 903](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L903)

### 2.14. Richards J. Heuer, Jr. — Д3 [36]

> "The most probable hypothesis is usually the one with the least evidence against it, not the one with the most evidence for it." [36]

- **Перевод:** «Наиболее вероятна обычно та гипотеза, против которой меньше всего свидетельств, а не та, в пользу которой их больше всего». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 906](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L906))
- **Интерпретация для репутационных технологий:** Вероятнее та гипотеза, против которой меньше свидетельств, а не та, за которую их больше, — опора для понятия «сигнал» и для метки CONFLICT. Аналитику репутации стоит искать опровергающие данные, а не копить подтверждающие; ограничение — источник описывает разведаналитику, а не медиамониторинг. [36]
- **Авторы:** Richards J. Heuer, Jr.
- **Дата:** 1999
- **Источник:** Psychology of Intelligence Analysis. Washington, District of Columbia: Center for the Study of Intelligence, Central Intelligence Agency, 1999
- **Ссылка:** https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf
- **Место в источнике:** страница 108 (PDF 136)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 905](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L905)

### 2.15. Richards J. Heuer, Jr. — Д3 [36]

> "analysts should identify explicitly those relevant variables on which information is lacking, consider alternative hypotheses concerning the status of these variables, and then modify their judgment and especially confidence in their judgment accordingly." [36]

- **Перевод:** «Аналитикам следует явно выделять значимые переменные, по которым не хватает информации, рассматривать альтернативные гипотезы об их состоянии и соответственно корректировать суждение и особенно уверенность в нём». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 908](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L908))
- **Интерпретация для репутационных технологий:** Хойер требует явно назвать переменные, по которым нет информации, и соответственно снизить уверенность в выводе. Курс берёт это как обоснование статуса PARTIAL с причиной: в отчёте видно, чего не хватает и какой источник снял бы статус. [36]
- **Авторы:** Richards J. Heuer, Jr.
- **Дата:** 1999
- **Источник:** Psychology of Intelligence Analysis. Washington, District of Columbia: Center for the Study of Intelligence, Central Intelligence Agency, 1999
- **Ссылка:** https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf
- **Место в источнике:** страница 120 (PDF 148)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 907](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L907)

### 2.16. Richards J. Heuer, Jr. — Д3 [36]

> "If analysts have information about which they are 70- or 80-percent certain but treat this information as though it were 100-percent certain, judgments based on that information will be overconfident." [36]

- **Перевод:** «Если аналитик уверен в информации на 70–80%, но обращается с ней как со стопроцентно достоверной, основанные на ней суждения будут излишне самоуверенными». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 910](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L910))
- **Интерпретация для репутационных технологий:** Сведения, известные на 70–80%, нельзя использовать как стопроцентные — иначе вывод становится излишне самоуверенным. Для реестра это аргумент не повышать статус до VERIFIED по умолчанию и сохранять степень уверенности рядом с каждым утверждением, а не терять её при сведении в итог. [36]
- **Авторы:** Richards J. Heuer, Jr.
- **Дата:** 1999
- **Источник:** Psychology of Intelligence Analysis. Washington, District of Columbia: Center for the Study of Intelligence, Central Intelligence Agency, 1999
- **Ссылка:** https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf
- **Место в источнике:** страница 122 (PDF 150)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 909](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L909)

### 2.17. Richards J. Heuer, Jr. — Д3 [36]

> "Proceed by trying to disprove the hypotheses rather than prove them." [36]

- **Перевод:** «Двигайтесь, пытаясь опровергнуть гипотезы, а не доказать их». (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Шаг ACH «опровергать, а не доказывать» курс переводит в требование к гипотезам: у каждой формулировки «если…, то…» должно быть опровергающее условие. Практик спрашивает не «что подтверждает версию», а «что бы её опровергло» — и ищет именно это. [36]
- **Авторы:** Richards J. Heuer, Jr.
- **Дата:** 1999
- **Источник:** Psychology of Intelligence Analysis. Washington, District of Columbia: Center for the Study of Intelligence, Central Intelligence Agency, 1999
- **Ссылка:** https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf
- **Место в источнике:** страница 97 (PDF 125), шаг 5 ACH
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 911](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L911)

### 2.18. Richards J. Heuer, Jr. — Д3 [36]

> "Experiments suggest that 'out of sight, out of mind' is a better description of the impact of gaps in the evidence." [36]

- **Перевод:** «Эксперименты показывают, что влияние пробелов в данных лучше описывает формула „с глаз долой — из сердца вон“». (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Пробелы в данных выпадают из рассуждения: чего нет на экране, того как будто нет. Курс использует цитату в тезисе «отсутствие данных не равно нулю» — дашборд показывает найденное, а ненайденное нужно явно вписать в отчёт как пробел. [36]
- **Авторы:** Richards J. Heuer, Jr.
- **Дата:** 1999
- **Источник:** Psychology of Intelligence Analysis. Washington, District of Columbia: Center for the Study of Intelligence, Central Intelligence Agency, 1999
- **Ссылка:** https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf
- **Место в источнике:** страница 119 (PDF 147)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 912](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L912)

### 2.19. Sherman Kent — Д4 [37]

> "It should set forth the community's findings in such a way as to make clear to the reader what is certain knowledge and what is reasoned judgment, and within this large realm of judgment what varying degrees of certitude lie behind each key statement." [37]

- **Перевод:** «Оценка должна излагать выводы так, чтобы читателю было ясно, что является достоверным знанием, а что — обоснованным суждением, и какая степень уверенности стоит за каждым ключевым утверждением в обширной области суждений». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 929](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L929))
- **Интерпретация для репутационных технологий:** Кент требует, чтобы читатель видел, что является достоверным знанием, а что — обоснованным суждением и с какой уверенностью. Курс берёт это как довод за явный статус каждого утверждения в репутационном отчёте; ограничение — Кент предлагает шкалу вероятностей, а не статусы «недостаточно данных» и «противоречие». [37]
- **Авторы:** Sherman Kent
- **Дата:** 1964
- **Источник:** Words of Estimative Probability // Studies in Intelligence. 1964. Volume 8, Number 4 (переиздание Center for the Study of Intelligence, Central Intelligence Agency)
- **Ссылка:** https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf
- **Место в источнике:** PDF страница 3
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 928](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L928)

### 2.20. Sherman Kent — Д4 [37]

> "...the odds were around 65 to 35 in favor of an attack. He was somewhat jolted by this; he and his colleagues had read 'serious possibility' to mean odds very considerably lower." [37]

- **Перевод:** «…шансы нападения были примерно 65 к 35. Его это несколько ошеломило: он и его коллеги понимали "серьёзную возможность" как значительно меньшие шансы». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 931](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L931))
- **Интерпретация для репутационных технологий:** Эпизод с «серьёзной возможностью», которую автор понимал как 65 к 35, а коллеги — как гораздо меньшие шансы, показывает: словесные оценки без согласованной шкалы читаются по-разному. Отсюда фиксированный словарь статусов VERIFIED / PARTIAL / CONFLICT вместо размытых «скорее», «вероятно» в отчёте. [37]
- **Авторы:** Sherman Kent
- **Дата:** 1964
- **Источник:** Words of Estimative Probability // Studies in Intelligence. 1964. Volume 8, Number 4 (переиздание Center for the Study of Intelligence, Central Intelligence Agency)
- **Ссылка:** https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf
- **Место в источнике:** PDF страница 4
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 930](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L930)

### 2.21. Sherman Kent — Д4 [37]

> "Simple prudence requires the qualifier in any type-three statement to show a decent reticence before the unknowable." [37]

- **Перевод:** «Простое благоразумие требует, чтобы оговорка в любом утверждении третьего типа выражала должную сдержанность перед непознаваемым». (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Оценки о непознаваемом требуют осторожной оговорки — Кент называет это простой предусмотрительностью. Для репутационного аналитика это напоминание: прогноз о намерениях партнёра или реакции аудитории формулируется с явной степенью уверенности, а не как факт; статусов курса у Кента нет. [37]
- **Авторы:** Sherman Kent
- **Дата:** 1964
- **Источник:** Words of Estimative Probability // Studies in Intelligence. 1964. Volume 8, Number 4 (переиздание Center for the Study of Intelligence, Central Intelligence Agency)
- **Ссылка:** https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf
- **Место в источнике:** PDF страница 2
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 932](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L932)

### 2.22. Headquarters, Department of the Army — Д5 [38]

> "In every instance the rating is based on previous reporting from that source. If there has been no previous reporting, the source must be rated as 'F'." [38]

- **Перевод:** «Во всех случаях оценка основана на прежних сообщениях этого источника. Если прежних сообщений не было, источник получает оценку "F"». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 948](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L948))
- **Интерпретация для репутационных технологий:** Надёжность источника в уставе FM 2-22.3 оценивается по истории его прежних сообщений, а без истории ставится «F». Курс берёт отсюда шкалу A–F для поля «Надёжность источника»: новый канал не плох и не хорош, мы просто его ещё не знаем. Ограничение — это военный полевой устав, первоисточники НАТО не проверены. [38]
- **Авторы:** Headquarters, Department of the Army (Штаб Министерства армии США) — коллективный автор
- **Дата:** 6 сентября 2006
- **Источник:** Field Manual 2-22.3 (Field Manual 34-52): Human Intelligence Collector Operations. Washington, District of Columbia: Headquarters, Department of the Army, 2006. Appendix B «Source and Information Reliability Matrix»
- **Ссылка:** https://irp.fas.org/doddir/army/fm2-22-3.pdf
- **Место в источнике:** страница B-1
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 947](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L947)

### 2.23. Headquarters, Department of the Army — Д5 [38]

> "An 'F' rating does not necessarily mean that the source cannot be trusted, but that there is no reporting history and therefore no basis for making a determination." [38]

- **Перевод:** «Оценка "F" не обязательно означает, что источнику нельзя доверять; она означает, что истории сообщений нет и, следовательно, нет оснований для вывода». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 950](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L950))
- **Интерпретация для репутационных технологий:** Оценка «F» не означает недоверия — только отсутствие оснований для вывода. Курс прямо опирается на это в определении PARTIAL: статус говорит о состоянии наших знаний, а не о том, что источник или партнёр плох; это важно объяснять заказчику отчёта. [38]
- **Авторы:** Headquarters, Department of the Army (Штаб Министерства армии США) — коллективный автор
- **Дата:** 6 сентября 2006
- **Источник:** Field Manual 2-22.3 (Field Manual 34-52): Human Intelligence Collector Operations. Washington, District of Columbia: Headquarters, Department of the Army, 2006. Appendix B «Source and Information Reliability Matrix»
- **Ссылка:** https://irp.fas.org/doddir/army/fm2-22-3.pdf
- **Место в источнике:** страница B-1, Note
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 949](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L949)

### 2.24. Headquarters, Department of the Army — Д5 [38]

> "The highest degree of confidence in reported information is given to that which has been confirmed by outside sources, '1'." [38]

- **Перевод:** «Наивысшая степень доверия присваивается информации, подтверждённой внешними источниками, — "1"». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 952](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L952))
- **Интерпретация для репутационных технологий:** Высшая степень достоверности — у сведения, подтверждённого внешними источниками. Это ближайший аналог статуса VERIFIED в курсе: есть первичный источник или два независимых; перепосты одного текста внешним подтверждением не считаются. Надёжность источника и достоверность сведения при этом оцениваются по разным шкалам. [38]
- **Авторы:** Headquarters, Department of the Army (Штаб Министерства армии США) — коллективный автор
- **Дата:** 6 сентября 2006
- **Источник:** Field Manual 2-22.3 (Field Manual 34-52): Human Intelligence Collector Operations. Washington, District of Columbia: Headquarters, Department of the Army, 2006. Appendix B «Source and Information Reliability Matrix»
- **Ссылка:** https://irp.fas.org/doddir/army/fm2-22-3.pdf
- **Место в источнике:** страница B-2
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 951](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L951)

### 2.25. Headquarters, Department of the Army — Д5 [38]

> "A rating of '6' does not necessarily mean false information, but is generally used to indicate that no determination can be made since the information is completely new." [38]

- **Перевод:** «Оценка "6" не обязательно означает ложную информацию; обычно она указывает, что вывод сделать нельзя, так как информация совершенно новая». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 954](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L954))
- **Интерпретация для репутационных технологий:** Оценка «6» обозначает совершенно новую информацию, о которой нельзя судить, а не ложь. Вместе с «F» это ближайший аналог PARTIAL: новое сведение в мониторинге честно помечается как непроверенное, а не отбрасывается и не принимается на веру; наш CONFLICT шире оценки «5» этого же устава. [38]
- **Авторы:** Headquarters, Department of the Army (Штаб Министерства армии США) — коллективный автор
- **Дата:** 6 сентября 2006
- **Источник:** Field Manual 2-22.3 (Field Manual 34-52): Human Intelligence Collector Operations. Washington, District of Columbia: Headquarters, Department of the Army, 2006. Appendix B «Source and Information Reliability Matrix»
- **Ссылка:** https://irp.fas.org/doddir/army/fm2-22-3.pdf
- **Место в источнике:** страница B-2, Note
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 953](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L953)

### 2.26. Richard Y. Wang и соавторы — Д6 [39]

> "we define 'data quality' as data that are fit for use by data consumers." [39]

- **Перевод:** «мы определяем "качество данных" как пригодность данных для использования их потребителями». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 977](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L977))
- **Интерпретация для репутационных технологий:** Качество данных определяется пригодностью для конкретного потребителя. Курс выводит отсюда свою интерпретацию: статус относителен шагу — одни и те же данные могут быть VERIFIED для первого письма и PARTIAL для годового договора. Ограничение — модель создана для информационных систем, а не для медиамониторинга. [39]
- **Авторы:** Richard Y. Wang; Diane M. Strong
- **Дата:** 1996
- **Источник:** Beyond Accuracy: What Data Quality Means to Data Consumers // Journal of Management Information Systems. 1996. Volume 12, Number 4. Pages 5–33
- **Ссылка:** https://www.jstor.org/stable/40398176
- **Место в источнике:** страница 6
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 976](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L976)

### 2.27. Richard Y. Wang и соавторы — Д6 [39]

> "data consumers also view believability and reputation as an integral part of intrinsic DQ; accuracy and objectivity alone are not sufficient for data to be considered of high quality." [39]

- **Перевод:** «потребители данных считают правдоподобие и репутацию неотъемлемой частью внутреннего качества данных; одних точности и объективности недостаточно, чтобы данные считались качественными». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 979](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L979))
- **Интерпретация для репутационных технологий:** Потребители данных считают правдоподобие и репутацию частью внутреннего качества: точности и объективности мало. Для репутационного инжиниринга это эмпирический довод, что доверие к данным зависит и от их источника, а курс использует его для разделения оценки источника и оценки содержания. [39]
- **Авторы:** Richard Y. Wang; Diane M. Strong
- **Дата:** 1996
- **Источник:** Beyond Accuracy: What Data Quality Means to Data Consumers // Journal of Management Information Systems. 1996. Volume 12, Number 4. Pages 5–33
- **Ссылка:** https://www.jstor.org/stable/40398176
- **Место в источнике:** страница 20
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 978](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L978)

### 2.28. Richard Y. Wang и соавторы — Д6 [39]

> "TRACEABILITY: The extent to which data are well documented, verifiable, and easily attributed to a source." [39]

- **Перевод:** «ПРОСЛЕЖИВАЕМОСТЬ: степень, в которой данные хорошо задокументированы, проверяемы и легко соотносятся с источником». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 981](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L981))
- **Интерпретация для репутационных технологий:** Прослеживаемость — данные задокументированы, проверяемы и легко соотносятся с источником — курс приравнивает к провенансу. Практический вывод: в репутационном отчёте у каждой цифры должна быть ссылка, которую можно открыть и проверить; модель Wang и Strong при этом описывает качество данных в ИС. [39]
- **Авторы:** Richard Y. Wang; Diane M. Strong
- **Дата:** 1996
- **Источник:** Beyond Accuracy: What Data Quality Means to Data Consumers // Journal of Management Information Systems. 1996. Volume 12, Number 4. Pages 5–33
- **Ссылка:** https://www.jstor.org/stable/40398176
- **Место в источнике:** страница 32 (Appendix)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 980](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L980)

### 2.29. Richard Y. Wang и соавторы — Д6 [39]

> "REPUTATION: The extent to which data are trusted or highly regarded in terms of their source or content." [39]

- **Перевод:** «РЕПУТАЦИЯ: степень доверия к данным или их высокой оценки с точки зрения источника или содержания». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 983](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L983))
- **Интерпретация для репутационных технологий:** Репутация данных определяется доверием к их источнику или содержанию. Курс использует это определение вместе с правдоподобием, чтобы показать: репутация источника и вера в содержание — разные измерения, которые в реестре оцениваются отдельно. [39]
- **Авторы:** Richard Y. Wang; Diane M. Strong
- **Дата:** 1996
- **Источник:** Beyond Accuracy: What Data Quality Means to Data Consumers // Journal of Management Information Systems. 1996. Volume 12, Number 4. Pages 5–33
- **Ссылка:** https://www.jstor.org/stable/40398176
- **Место в источнике:** страница 32 (Appendix)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 982](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L982)

### 2.30. Richard Y. Wang и соавторы — Д6 [39]

> "BELIEVABILITY The extent to which data are accepted or regarded as true, real, and credible." [39]

- **Перевод:** «ПРАВДОПОДОБИЕ: степень, в которой данные принимаются или считаются истинными, реальными и заслуживающими доверия». (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Правдоподобие — насколько данные принимаются как истинные — в модели Wang и Strong отделено от репутации источника. Отсюда правило курса: надёжный источник может передать непроверенное сведение, а малоизвестный — точное, поэтому две шкалы не сливаются в одну оценку. [39]
- **Авторы:** Richard Y. Wang; Diane M. Strong
- **Дата:** 1996
- **Источник:** Beyond Accuracy: What Data Quality Means to Data Consumers // Journal of Management Information Systems. 1996. Volume 12, Number 4. Pages 5–33
- **Ссылка:** https://www.jstor.org/stable/40398176
- **Место в источнике:** страница 31 (Appendix)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 984](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L984)

### 2.31. International Association for the Measurement and Evaluation of Communication — Д7 [40]

> "Numbers alone will not explain why something worked, resonated, or failed. Qualitative analysis provides the critical context behind the numbers" [40]

- **Перевод:** «Одни цифры не объяснят, почему что-то сработало, нашло отклик или провалилось. Качественный анализ даёт критически важный контекст для цифр». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1000](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1000))
- **Интерпретация для репутационных технологий:** Отраслевой стандарт PR-измерений AMEC прямо говорит, что цифры не объясняют, почему что-то сработало или провалилось. Курс использует это для правила «сначала понять „почему“, потом считать „сколько“»; ограничение — Barcelona Principles задают принципы, а не порядок «качественное → количественное». [40]
- **Авторы:** International Association for the Measurement and Evaluation of Communication (Международная ассоциация измерения и оценки коммуникаций) — коллективный автор
- **Дата:** июнь 2025
- **Источник:** Barcelona Principles 4.0 (электронная книга)
- **Ссылка:** https://amecorg.com/wp-content/uploads/2025/06/Barcelona-Principles-V4.0-eBook-Finalv-compressed.pdf
- **Место в источнике:** страница 17
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 999](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L999)

### 2.32. International Association for the Measurement and Evaluation of Communication — Д7 [40]

> "Be wary of relying exclusively on automated dashboards or numerical led reports, as they alone cannot explain the 'why' behind the metrics." [40]

- **Перевод:** «Остерегайтесь полагаться исключительно на автоматические дашборды или отчёты, построенные на цифрах: сами по себе они не объясняют "почему" за метриками». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1002](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1002))
- **Интерпретация для репутационных технологий:** Предостережение против опоры только на автоматические дашборды — основа тезиса Дня 2 «дашборд не объясняет „почему“». Репутационный отчёт, состоящий из графиков упоминаний и тональности, должен дополняться качественным разбором причин; иначе руководитель получает цифры без смысла. [40]
- **Авторы:** International Association for the Measurement and Evaluation of Communication (Международная ассоциация измерения и оценки коммуникаций) — коллективный автор
- **Дата:** июнь 2025
- **Источник:** Barcelona Principles 4.0 (электронная книга)
- **Ссылка:** https://amecorg.com/wp-content/uploads/2025/06/Barcelona-Principles-V4.0-eBook-Finalv-compressed.pdf
- **Место в источнике:** страница 18
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1001](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1001)

### 2.33. International Association for the Measurement and Evaluation of Communication — Д7 [40]

> "Don't make substitution error - e.g. media clip volumes and tonality of coverage do not equate to the effect on the stakeholder audience." [40]

- **Перевод:** «Не совершайте ошибку подмены: например, объём публикаций и тональность освещения не равны воздействию на аудиторию стейкхолдеров». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1004](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1004))
- **Интерпретация для репутационных технологий:** «Ошибка подмены»: объём публикаций и тональность не равны воздействию на стейкхолдеров. Курс считает это ближайшей отраслевой формулировкой к своей «ошибке преждевременной оцифровки» и к различению сигнала и шума; сам термин про оцифровку — наш, у AMEC его нет. [40]
- **Авторы:** International Association for the Measurement and Evaluation of Communication (Международная ассоциация измерения и оценки коммуникаций) — коллективный автор
- **Дата:** июнь 2025
- **Источник:** Barcelona Principles 4.0 (электронная книга)
- **Ссылка:** https://amecorg.com/wp-content/uploads/2025/06/Barcelona-Principles-V4.0-eBook-Finalv-compressed.pdf
- **Место в источнике:** страница 24
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1003](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1003)

### 2.34. International Association for the Measurement and Evaluation of Communication — Д7 [40]

> "Research methodologies should have a clear policy on how to identify, classify and handle the trust levels in different information sources and channels - for example 'bot' social media accounts verses professional and high-credential journalists and news outlets." [40]

- **Перевод:** «В исследовательских методологиях должна быть чёткая политика выявления, классификации и учёта уровней доверия к разным источникам и каналам — например, "бот"-аккаунты в соцсетях против профессиональных журналистов с высокой репутацией и СМИ». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1007](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1007))
- **Интерпретация для репутационных технологий:** AMEC требует, чтобы методология заранее определяла уровни доверия к разным источникам и каналам — от бот-аккаунтов до профессиональных СМИ. Для курса это отраслевая опора отдельной оценки надёжности источника: в мониторинге упоминание бота и публикация редакции не должны весить одинаково. [40]
- **Авторы:** International Association for the Measurement and Evaluation of Communication (Международная ассоциация измерения и оценки коммуникаций) — коллективный автор
- **Дата:** июнь 2025
- **Источник:** Barcelona Principles 4.0 (электронная книга)
- **Ссылка:** https://amecorg.com/wp-content/uploads/2025/06/Barcelona-Principles-V4.0-eBook-Finalv-compressed.pdf
- **Место в источнике:** страница 27
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1005](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1005)

### 2.35. International Association for the Measurement and Evaluation of Communication — Д7 [40]

> "Research, measurement and evaluation should be clear on the data sources used, and when subsets of data have been used, how the sampling has been applied." [40]

- **Перевод:** «Исследование, измерение и оценка должны ясно указывать использованные источники данных, а если использовались подвыборки — как была устроена выборка». (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Измерение должно ясно называть источники данных и способ выборки, если использовано подмножество. В репутационном отчёте это значит: указывать, какие площадки и период охвачены и как отбирались упоминания, иначе выводы нельзя проверить — прямое продолжение правила провенанса. [40]
- **Авторы:** International Association for the Measurement and Evaluation of Communication (Международная ассоциация измерения и оценки коммуникаций) — коллективный автор
- **Дата:** июнь 2025
- **Источник:** Barcelona Principles 4.0 (электронная книга)
- **Ссылка:** https://amecorg.com/wp-content/uploads/2025/06/Barcelona-Principles-V4.0-eBook-Finalv-compressed.pdf
- **Место в источнике:** страница 27
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1008](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1008)

### 2.36. International Association for the Measurement and Evaluation of Communication — Д7 [40]

> "Don't focus only on convenient or positive data." [40]

- **Перевод:** «Не сосредотачивайтесь только на удобных или позитивных данных». (перевод наш (#711))
- **Интерпретация для репутационных технологий:** Короткое правило AMEC против отбора удобных и позитивных данных. Для репутационного аналитика это запрет показывать заказчику только выгодную часть картины: противоречащие сведения попадают в отчёт, а при расхождении источников ставится CONFLICT. [40]
- **Авторы:** International Association for the Measurement and Evaluation of Communication (Международная ассоциация измерения и оценки коммуникаций) — коллективный автор
- **Дата:** июнь 2025
- **Источник:** Barcelona Principles 4.0 (электронная книга)
- **Ссылка:** https://amecorg.com/wp-content/uploads/2025/06/Barcelona-Principles-V4.0-eBook-Finalv-compressed.pdf
- **Место в источнике:** страница 24
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1009](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1009)

### 2.37. International Association for the Measurement and Evaluation of Communication — Д7 [40]

> "Be transparent about the limitations of your methods and clearly communicate where additional qualitative context is required for meaningful interpretation." [40]

- **Перевод:** «Будьте прозрачны в отношении ограничений ваших методов и ясно сообщайте, где для осмысленной интерпретации нужен дополнительный качественный контекст». (перевод наш (#711))
- **Интерпретация для репутационных технологий:** AMEC требует открыто говорить об ограничениях методов и о том, где без качественного контекста цифры не интерпретируются. Курс воплощает это в причинах статуса PARTIAL и в разделе ограничений отчёта; при этом Barcelona Principles — принципы, а не готовый метод. [40]
- **Авторы:** International Association for the Measurement and Evaluation of Communication (Международная ассоциация измерения и оценки коммуникаций) — коллективный автор
- **Дата:** июнь 2025
- **Источник:** Barcelona Principles 4.0 (электронная книга)
- **Ссылка:** https://amecorg.com/wp-content/uploads/2025/06/Barcelona-Principles-V4.0-eBook-Finalv-compressed.pdf
- **Место в источнике:** страница 18
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1010](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1010)

### 2.38. Michael D. Fetters и соавторы — Д8 [41]

> "In an exploratory sequential design, the researcher first collects and analyzes qualitative data, and these findings inform subsequent quantitative data collection (Onwuegbuzie, Bustamante, and Nelson 2010)." [41]

- **Перевод:** «В разведочном последовательном дизайне исследователь сначала собирает и анализирует качественные данные, и полученные результаты определяют последующий сбор количественных данных». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1027](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1027))
- **Интерпретация для репутационных технологий:** Разведочный последовательный дизайн — сначала качественные данные, затем определяемый ими количественный сбор — прямая опора порядка Дня 2 «качественное → гипотезы → количественное». Репутационному аналитику это говорит: сначала разговоры и отзывы, потом метрики; термин «ошибка преждевременной оцифровки» в статье отсутствует, он наш. [41]
- **Авторы:** Michael D. Fetters; Leslie A. Curry; John W. Creswell
- **Дата:** 2013
- **Источник:** Achieving Integration in Mixed Methods Designs — Principles and Practices // Health Services Research. 2013. Volume 48, Number 6, Part 2. Pages 2134–2156
- **Ссылка:** https://doi.org/10.1111/1475-6773.12117
- **Место в источнике:** раздел "Integration at the Study Design Level" (HTML; PDF с пагинацией был недоступен)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1026](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1026)

### 2.39. Большаков Никита Викторович — Д9 [42]

> «Наиболее полное определение стратегии смешивания методов дает Дж. Кресвелл: «В стратегиях смешивания методов исследователь собирает и анализирует как качественные, так и количественные данные, основываясь на исследовательском вопросе; смешивает (интегрирует или соединяет) их параллельно или последовательно, придавая при этом большую значимость одному из них или же обоим…» [Creswell, 2011: 271]». [42]

- **Интерпретация для репутационных технологий:** Большаков приводит определение Кресвелла: качественные и количественные данные смешиваются параллельно или последовательно, исходя из исследовательского вопроса. Курс использует это как русскоязычный обзор смешанных стратегий; определение Кресвелла проверено только через Большакова (VERIFIED-SECONDARY), а порядок «сначала качественное» автор не предписывает — для него нужна связка с работой Fetters и соавторов [42]
- **Авторы:** Большаков Никита Викторович
- **Дата:** 2017
- **Источник:** Сочетать, комбинировать, смешивать: качественные и количественные методы в современной исследовательской практике // Мониторинг общественного мнения: экономические и социальные перемены. 2017. Номер 3 (139). Страницы 21–29
- **Ссылка:** https://doi.org/10.14515/monitoring.2017.3.03
- **Место в источнике:** страница 26 (номер страницы в колонтитуле PDF-страницы 6)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1040](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1040)

### 2.40. Соколова Дарья Валерьевна — Д10 [43]

> «Верификация информации включает как традиционные инструменты (звонок спикеру, поиск первоисточника, поиск альтернативного источника и т. д.), так и возникшие относительно недавно благодаря возможностям Интернета». [43]

- **Интерпретация для репутационных технологий:** Соколова перечисляет традиционные инструменты верификации — звонок спикеру, поиск первоисточника и альтернативного источника — рядом с цифровыми. Курс опирается на это как на базовую процедуру провенанса: дойти до первоисточника, прежде чем ставить VERIFIED; исследование описывает журналистскую практику, а не мониторинг репутации. [43]
- **Авторы:** Соколова Дарья Валерьевна
- **Дата:** 2018
- **Источник:** Фактчекинг и верификация информации в российских СМИ: результаты опроса // Вестник Московского университета. Серия 10. Журналистика. 2018. Номер 4. Страницы 3–25
- **Ссылка:** https://cyberleninka.ru/article/n/faktcheking-i-verifikatsiya-informatsii-v-rossiyskih-smi-rezultaty-oprosa
- **Место в источнике:** страница 5
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1056](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1056)

### 2.41. Соколова Дарья Валерьевна — Д10 [43]

> «В цифровой среде возникает необходимость проверять как источник информации, так и сам контент, подлинность его содержания, особенно если речь идет о пользовательском контенте.» [43]

- **Интерпретация для репутационных технологий:** В цифровой среде нужно проверять отдельно источник и само содержание, особенно пользовательский контент. Это русскоязычная опора для раздельных шкал надёжности источника и достоверности сведения; курс применяет её к кейсу с сокращённым видео без даты, где «он сам сказал» ещё не доказательство. [43]
- **Авторы:** Соколова Дарья Валерьевна
- **Дата:** 2018
- **Источник:** Фактчекинг и верификация информации в российских СМИ: результаты опроса // Вестник Московского университета. Серия 10. Журналистика. 2018. Номер 4. Страницы 3–25
- **Ссылка:** https://cyberleninka.ru/article/n/faktcheking-i-verifikatsiya-informatsii-v-rossiyskih-smi-rezultaty-oprosa
- **Место в источнике:** страница 5
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1057](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1057)

### 2.42. Соколова Дарья Валерьевна — Д10 [43]

> «…происходит подмена достоверности срочностью (Балмаева, Лукина (ред.), 2016: 252)». [43]

- **Интерпретация для репутационных технологий:** Подмена достоверности срочностью иллюстрирует риск, когда скорость мониторинга давит на проверку. Важно: это формулировка Соколовой со ссылкой на Балмаеву и Лукину, а не вывод её опроса; для практика смысл в том, что быстрый ответ на репутационный инцидент не отменяет статуса непроверенного сведения. [43]
- **Авторы:** Соколова Дарья Валерьевна
- **Дата:** 2018
- **Источник:** Фактчекинг и верификация информации в российских СМИ: результаты опроса // Вестник Московского университета. Серия 10. Журналистика. 2018. Номер 4. Страницы 3–25
- **Ссылка:** https://cyberleninka.ru/article/n/faktcheking-i-verifikatsiya-informatsii-v-rossiyskih-smi-rezultaty-oprosa
- **Место в источнике:** страница 16
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1058](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1058)

### 2.43. Поздняков Владимир Александрович — Д11 [44]

> «Достоверность разведывательной информации – свойство синтетическое… Она (достоверность) определяется по следующим параметрам: наличие подтверждения из других источников; стыкование с другой информацией; знание источника и его мотивов; авторитет или длительная положительная история работы с источником; свойства канала передачи информации. Как видно, важнейшее место здесь занимает знание об источнике информации.» [44]

- **Интерпретация для репутационных технологий:** Поздняков перечисляет параметры достоверности — подтверждение другими источниками, согласованность, знание источника и его мотивов, историю работы с ним — и выделяет знание об источнике. Курс берёт это как русскую опору разделения шкал источника и сведения, хотя сам автор сводит их в одно «синтетическое» свойство. [44]
- **Авторы:** Поздняков Владимир Александрович
- **Дата:** 2010
- **Источник:** Свойства и методы обработки информации в конкурентной разведке // Известия Южного федерального университета. Технические науки. 2010. Номер 11 (112). Страницы 238–245
- **Ссылка:** https://cyberleninka.ru/article/n/svoystva-i-metody-obrabotki-informatsii-v-konkurentnoy-razvedke
- **Место в источнике:** страница 241 (номер в колонтитуле PDF-страницы 4)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1073](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1073)

### 2.44. Федеральное агентство по техническому регулированию и метрологии — Д12 [45]

> «[2] определяет достоверность как степень, в которой данные обладают атрибутами, которым пользователи склонны доверять в конкретном контексте использования.» [45]

- **Интерпретация для репутационных технологий:** ГОСТ Р 71484.2-2024 вслед за ИСО/МЭК 25012 определяет достоверность через атрибуты, которым пользователи склонны доверять в конкретном контексте. Курс использует стандарт как действующую российскую норму качества данных; ограничения — он о данных для ИИ и машинного обучения, а термин «достоверность» в нём переводит разные английские понятия. [45]
- **Авторы:** Федеральное агентство по техническому регулированию и метрологии (Росстандарт) — национальный стандарт, персональных авторов нет
- **Дата:** утверждён 28 октября 2024, введён 1 января 2025
- **Источник:** ГОСТ Р 71484.2-2024 (ИСО/МЭК 5259-2:2024). Национальный стандарт Российской Федерации. Искусственный интеллект. Качество данных для аналитики и машинного обучения. Часть 2. Показатели качества данных. Москва: Федеральное государственное бюджетное учреждение «Институт стандартизации», 2024
- **Ссылка:** https://meganorm.ru/mega_doc/norm_update_01032025/gost-r_gosudarstvennyj-standart/0/gost_r_71484_2-2024_iso_mek_5259-2_2024_natsionalnyy.html
- **Место в источнике:** Пункт 6.2.4.1
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1087](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1087)

### 2.45. Федеральное агентство по техническому регулированию и метрологии — Д12 [45]

> «Доверие к подготовке набора данных может быть повышено путем указания происхождения данных в соответствии со структурой жизненного цикла данных (см. ГОСТ Р 70889-2023, пункт 6.6).» [45]

- **Интерпретация для репутационных технологий:** Стандарт прямо пишет, что доверие к набору данных повышается указанием их происхождения. Это российская нормативная опора правила курса: репутационный отчёт показывает, откуда взята каждая строка; область применения ГОСТ — данные для ИИ/ML, поэтому для мониторинга это аналогия. [45]
- **Авторы:** Федеральное агентство по техническому регулированию и метрологии (Росстандарт) — национальный стандарт, персональных авторов нет
- **Дата:** утверждён 28 октября 2024, введён 1 января 2025
- **Источник:** ГОСТ Р 71484.2-2024 (ИСО/МЭК 5259-2:2024). Национальный стандарт Российской Федерации. Искусственный интеллект. Качество данных для аналитики и машинного обучения. Часть 2. Показатели качества данных. Москва: Федеральное государственное бюджетное учреждение «Институт стандартизации», 2024
- **Ссылка:** https://meganorm.ru/mega_doc/norm_update_01032025/gost-r_gosudarstvennyj-standart/0/gost_r_71484_2-2024_iso_mek_5259-2_2024_natsionalnyy.html
- **Место в источнике:** Пункт 6.2.4.1, пример 4
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1088](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1088)

### 2.46. Федеральное агентство по техническому регулированию и метрологии — Д12 [45]

> «Прослеживаемость показывает, в какой степени данные обладают атрибутами, позволяющими отслеживать доступ и любые внесенные в них изменения в конкретном контексте использования.» [45]

- **Интерпретация для репутационных технологий:** Прослеживаемость по ГОСТ — возможность отследить доступ к данным и внесённые изменения. Для реестра утверждений это довод фиксировать дату и состояние источника, например дату снимка веб-архива, чтобы позднее было видно, какая версия страницы легла в основу вывода. [45]
- **Авторы:** Федеральное агентство по техническому регулированию и метрологии (Росстандарт) — национальный стандарт, персональных авторов нет
- **Дата:** утверждён 28 октября 2024, введён 1 января 2025
- **Источник:** ГОСТ Р 71484.2-2024 (ИСО/МЭК 5259-2:2024). Национальный стандарт Российской Федерации. Искусственный интеллект. Качество данных для аналитики и машинного обучения. Часть 2. Показатели качества данных. Москва: Федеральное государственное бюджетное учреждение «Институт стандартизации», 2024
- **Ссылка:** https://meganorm.ru/mega_doc/norm_update_01032025/gost-r_gosudarstvennyj-standart/0/gost_r_71484_2-2024_iso_mek_5259-2_2024_natsionalnyy.html
- **Место в источнике:** Пункт 6.3.5.1
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1089](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1089)

### 2.47. Аргамакова Александра Александровна — Д13 [46]

> «Таким образом, качественный анализ информации на основе цифровых инструментов приобретает свойства количественного: возрастает точность и структурированность данных, качественные данные снабжаются числовыми индексами и показателями, визуализируются на графиках, обрабатываются программными алгоритмами, искусственным интеллектом и т.д.» [46]

- **Интерпретация для репутационных технологий:** Аргамакова нейтрально описывает, как цифровые инструменты придают качественному анализу свойства количественного — индексы, графики, обработку ИИ. Курс читает это как подтверждение, что соблазн оцифровать рано реален; ошибкой это называет курс, а не автор, и термин «преждевременная оцифровка» остаётся нашим. [46]
- **Авторы:** Аргамакова Александра Александровна
- **Дата:** 2023
- **Источник:** Смешанная методология социальных наук // Эпистемология и философия науки. 2023. Том 60, номер 4. Страницы 212–224
- **Ссылка:** https://doi.org/10.5840/eps202360467
- **Место в источнике:** страница 214 (номер в колонтитуле PDF-страницы 3)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1106](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1106)

### 2.48. Jason Wei и соавторы — Н1 [47]

> "generating a chain of thought—a series of intermediate reasoning steps—significantly improves the ability of large language models to perform complex reasoning." [47]

- **Перевод:** «генерация цепочки рассуждений — серии промежуточных шагов — существенно улучшает способность больших языковых моделей к сложным рассуждениям». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1407](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1407))
- **Интерпретация для репутационных технологий:** Цепочка рассуждений улучшает способность моделей к сложным задачам — на этом стоит приём «покажи шаги» при ранжировании и извлечении связей. Смысл для практика: шаги нужны, чтобы их проверить, а не чтобы поверить; истинности вывода приём не гарантирует. [47]
- **Авторы:** Jason Wei; Xuezhi Wang; Dale Schuurmans; Maarten Bosma; Brian Ichter; Fei Xia; Ed Chi; Quoc Le; Denny Zhou
- **Дата:** 2022 (версия arXiv v6 — 10 января 2023)
- **Источник:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models // Advances in Neural Information Processing Systems 35 (36th Conference on Neural Information Processing Systems, NeurIPS 2022). arXiv:2201.11903
- **Ссылка:** https://arxiv.org/pdf/2201.11903
- **Место в источнике:** Abstract, страница 1
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1406](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1406)

### 2.49. Jason Wei и соавторы — Н1 [47]

> "a chain of thought provides an interpretable window into the behavior of the model, suggesting how it might have arrived at a particular answer and providing opportunities to debug where the reasoning path went wrong". [47]

- **Перевод:** «цепочка рассуждений дает интерпретируемое окно в поведение модели: видно, как она могла прийти к ответу, и можно найти место, где рассуждение пошло не так». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1409](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1409))
- **Интерпретация для репутационных технологий:** Цепочка рассуждений даёт окно в поведение модели и позволяет найти место, где рассуждение пошло не так. В репутационной аналитике это аргумент просить ИИ выписывать промежуточные шаги, чтобы человек мог проверить, на каком звене появился неподтверждённый вывод. [47]
- **Авторы:** Jason Wei; Xuezhi Wang; Dale Schuurmans; Maarten Bosma; Brian Ichter; Fei Xia; Ed Chi; Quoc Le; Denny Zhou
- **Дата:** 2022 (версия arXiv v6 — 10 января 2023)
- **Источник:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models // Advances in Neural Information Processing Systems 35 (36th Conference on Neural Information Processing Systems, NeurIPS 2022). arXiv:2201.11903
- **Ссылка:** https://arxiv.org/pdf/2201.11903
- **Место в источнике:** раздел 2, страница 2
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1408](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1408)

### 2.50. Jason Wei и соавторы — Н1 [47]

> "there is no guarantee of correct reasoning paths, which can lead to both correct and incorrect answers; improving factual generations of language models is an open direction for future work". [47]

- **Перевод:** «нет гарантии правильного хода рассуждений, что может вести как к верным, так и к неверным ответам; повышение фактической точности генерации — открытая задача». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1411](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1411))
- **Интерпретация для репутационных технологий:** Сами авторы признают: правильный ход рассуждений не гарантирован, а фактическая точность генерации остаётся открытой задачей. Каталог курса использует это против тезиса «правильный промпт устраняет ошибки» — промпт помогает, но проверку источников не заменяет. [47]
- **Авторы:** Jason Wei; Xuezhi Wang; Dale Schuurmans; Maarten Bosma; Brian Ichter; Fei Xia; Ed Chi; Quoc Le; Denny Zhou
- **Дата:** 2022 (версия arXiv v6 — 10 января 2023)
- **Источник:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models // Advances in Neural Information Processing Systems 35 (36th Conference on Neural Information Processing Systems, NeurIPS 2022). arXiv:2201.11903
- **Ссылка:** https://arxiv.org/pdf/2201.11903
- **Место в источнике:** раздел 6 "Discussion", страница 9
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1410](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1410)

### 2.51. Jason Wei и соавторы — Н1 [47]

> "Overall, there are no guarantees that the reasoning processes generated by large language models are coherent or factually correct". [47]

- **Перевод:** «В целом нет гарантий, что порождаемые LLM рассуждения связны или фактически верны». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1413](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1413))
- **Интерпретация для репутационных технологий:** Признание авторов, что рассуждения LLM не гарантированно связны и фактически верны, работает как прямое ограничение приёма chain-of-thought. Для лектора это готовый довод: красиво расписанные шаги модели — ещё не проверенный вывод о репутации. [47]
- **Авторы:** Jason Wei; Xuezhi Wang; Dale Schuurmans; Maarten Bosma; Brian Ichter; Fei Xia; Ed Chi; Quoc Le; Denny Zhou
- **Дата:** 2022 (версия arXiv v6 — 10 января 2023)
- **Источник:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models // Advances in Neural Information Processing Systems 35 (36th Conference on Neural Information Processing Systems, NeurIPS 2022). arXiv:2201.11903
- **Ссылка:** https://arxiv.org/pdf/2201.11903
- **Место в источнике:** Appendix D.2, страница 28
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1412](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1412)

### 2.52. Jules White и соавторы — Н2 [48]

> "A current weakness of LLMs (including ChatGPT) is they often rapidly (and even enthusiastically!) generate convincing text that is factually incorrect." [48]

- **Перевод:** «Текущая слабость LLM (включая ChatGPT) в том, что они часто быстро (и даже с энтузиазмом!) порождают убедительный, но фактически неверный текст». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1423](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1423))
- **Интерпретация для репутационных технологий:** White и соавторы фиксируют слабость LLM быстро и уверенно порождать убедительный, но неверный текст. В Дне 2 источник прямо не цитируется и рекомендован для самостоятельной работы; он объясняет, зачем в работе с ИИ нужен этап человеческой проверки; ограничение — это каталог паттернов без количественной оценки эффективности. [48]
- **Авторы:** Jules White; Quchen Fu; Sam Hays; Michael Sandborn; Carlos Olea; Henry Gilbert; Ashraf Elnashar; Jesse Spencer-Smith; Douglas C. Schmidt
- **Дата:** 21 февраля 2023
- **Источник:** A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT. arXiv:2302.11382
- **Ссылка:** https://arxiv.org/pdf/2302.11382
- **Место в источнике:** раздел III.I "The Fact Check List Pattern", страница 11
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1422](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1422)
- **Примечание:** В материалах Дня 2 прямо не цитируется; источник из каталога курса для самостоятельной работы.

### 2.53. Jules White и соавторы — Н2 [48]

> "From now on, when you generate an answer, create a set of facts that the answer depends on that should be fact-checked and list this set of facts at the end of your output." [48]

- **Перевод:** «Отныне, формируя ответ, составляй перечень фактов, от которых зависит ответ и которые нужно проверить, и приводи этот перечень в конце». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1425](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1425))
- **Интерпретация для репутационных технологий:** Готовая формулировка паттерна Fact Check List: модель сама выписывает факты, от которых зависит ответ и которые нужно проверить. Каталог курса предлагает её как этап human-in-the-loop для реестра утверждений; в материалах Дня 2 прямо не используется, и эффективность паттерна авторы количественно не оценивали. [48]
- **Авторы:** Jules White; Quchen Fu; Sam Hays; Michael Sandborn; Carlos Olea; Henry Gilbert; Ashraf Elnashar; Jesse Spencer-Smith; Douglas C. Schmidt
- **Дата:** 21 февраля 2023
- **Источник:** A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT. arXiv:2302.11382
- **Ссылка:** https://arxiv.org/pdf/2302.11382
- **Место в источнике:** раздел III.I "The Fact Check List Pattern", страница 11; пример промпта
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1424](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1424)
- **Примечание:** В материалах Дня 2 прямо не цитируется; источник из каталога курса для самостоятельной работы.

### 2.54. Jules White и соавторы — Н2 [48]

> "Errors are potential in all LLM outputs" и "Although the fact check list may also have errors, users often have sufficient knowledge and context to determine its completeness and accuracy relative to the output." [48]

- **Перевод:** «Ошибки возможны в любом выводе LLM»; «Хотя и список фактов для проверки может содержать ошибки, у пользователей часто достаточно знаний и контекста, чтобы оценить его полноту и точность». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1427](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1427))
- **Интерпретация для репутационных технологий:** Авторы паттерна честно оговаривают, что ошибки возможны в любом выводе LLM и в самом списке фактов, но пользователь часто может оценить его полноту по контексту. Для практика это значит: список «на проверку» — подсказка, а не проверка; источник для самостоятельной работы, в Дне 2 не цитируется. [48]
- **Авторы:** Jules White; Quchen Fu; Sam Hays; Michael Sandborn; Carlos Olea; Henry Gilbert; Ashraf Elnashar; Jesse Spencer-Smith; Douglas C. Schmidt
- **Дата:** 21 февраля 2023
- **Источник:** A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT. arXiv:2302.11382
- **Ссылка:** https://arxiv.org/pdf/2302.11382
- **Место в источнике:** раздел III.I "The Fact Check List Pattern", страница 11; Consequences, страница 11
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1426](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1426)
- **Примечание:** В материалах Дня 2 прямо не цитируется; источник из каталога курса для самостоятельной работы.

### 2.55. Jules White и соавторы — Н2 [48]

> "Within scope X, if there are alternative ways to accomplish the same thing, list the best alternate approaches" / "(Optional) compare/contrast the pros and cons of each approach"; p. 10: "The optional statement “compare/contrast the pros and cons of each approach” adds decision making criteria to the analysis." [48]

- **Перевод:** «В рамках X, если есть альтернативные способы достичь того же, перечисли лучшие» / «(Опционально) сравни плюсы и минусы каждого»; «Опциональная инструкция "сравни плюсы и минусы" добавляет в анализ критерии принятия решения». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1429](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1429))
- **Интерпретация для репутационных технологий:** Паттерн «альтернативные подходы» с опциональным сравнением плюсов и минусов добавляет в анализ явные критерии решения. Каталог курса связывает его с ранжированием вариантов и сообщений по заданным критериям; в Дне 2 не цитируется, а эффективность паттерна не измерена. [48]
- **Авторы:** Jules White; Quchen Fu; Sam Hays; Michael Sandborn; Carlos Olea; Henry Gilbert; Ashraf Elnashar; Jesse Spencer-Smith; Douglas C. Schmidt
- **Дата:** 21 февраля 2023
- **Источник:** A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT. arXiv:2302.11382
- **Ссылка:** https://arxiv.org/pdf/2302.11382
- **Место в источнике:** раздел III.G "Alternative Approaches Pattern", страницы 9–10
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1428](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1428)
- **Примечание:** В материалах Дня 2 прямо не цитируется; источник из каталога курса для самостоятельной работы.

### 2.56. Ziwei Ji и соавторы — Н3 [49]

> Галлюцинация — это "the generated content that is nonsensical or unfaithful to the provided source content". [49]

- **Перевод:** «сгенерированное содержание, бессмысленное или не соответствующее предоставленному источнику». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1439](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1439))
- **Интерпретация для репутационных технологий:** Обзор Ji и соавторов определяет галлюцинацию как содержание, бессмысленное или не соответствующее предоставленному источнику. Курс берёт это научное определение как основу «охоты на галлюцинации»: ошибка ИИ измеряется расхождением с источником, а не тем, насколько убедительно звучит ответ. [49]
- **Авторы:** Ziwei Ji; Nayeon Lee; Rita Frieske; Tiezheng Yu; Dan Su; Yan Xu; Etsuko Ishii; Ye Jin Bang; Andrea Madotto; Pascale Fung
- **Дата:** 2023
- **Источник:** Survey of Hallucination in Natural Language Generation // ACM Computing Surveys (Association for Computing Machinery). 2023. Volume 55, Number 12
- **Ссылка:** https://doi.org/10.1145/3571730
- **Место в источнике:** раздел 2 "Definitions", страница 4 PDF arXiv
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1438](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1438)

### 2.57. Ziwei Ji и соавторы — Н3 [49]

> "(1) Intrinsic Hallucinations: The generated output that contradicts the source content." / "(2) Extrinsic Hallucinations: The generated output that cannot be verified from the source content (i.e., output that can neither be supported nor contradicted by the source)." [49]

- **Перевод:** «(1) Внутренние галлюцинации: вывод, противоречащий источнику» / «(2) Внешние галлюцинации: вывод, который нельзя проверить по источнику (источник его ни подтверждает, ни опровергает)». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1441](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1441))
- **Интерпретация для репутационных технологий:** Разделение на внутренние галлюцинации (противоречат источнику) и внешние (источником не подтверждаются и не опровергаются) курс сопоставляет со своими метками: первое ближе к CONFLICT, второе — к PARTIAL или «нет данных». Это разные типы ошибок, и искать их в черновом реестре ИИ нужно по-разному. [49]
- **Авторы:** Ziwei Ji; Nayeon Lee; Rita Frieske; Tiezheng Yu; Dan Su; Yan Xu; Etsuko Ishii; Ye Jin Bang; Andrea Madotto; Pascale Fung
- **Дата:** 2023
- **Источник:** Survey of Hallucination in Natural Language Generation // ACM Computing Surveys (Association for Computing Machinery). 2023. Volume 55, Number 12
- **Ссылка:** https://doi.org/10.1145/3571730
- **Место в источнике:** раздел 2 "Definitions", страница 4 PDF arXiv
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1440](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1440)

### 2.58. Ziwei Ji и соавторы — Н3 [49]

> "Hallucinated text gives the impression of being fluent and natural despite being unfaithful and nonsensical." [49]

- **Перевод:** «Галлюцинированный текст производит впечатление гладкого и естественного, хотя он недостоверен и бессмыслен». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1443](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1443))
- **Интерпретация для репутационных технологий:** Галлюцинированный текст выглядит гладким и естественным — поэтому гладкость ответа ИИ ничего не говорит о его истинности. Для лектора это объяснение, почему каждое утверждение модели проходит провенанс, а стиль ответа не повышает его статус. [49]
- **Авторы:** Ziwei Ji; Nayeon Lee; Rita Frieske; Tiezheng Yu; Dan Su; Yan Xu; Etsuko Ishii; Ye Jin Bang; Andrea Madotto; Pascale Fung
- **Дата:** 2023
- **Источник:** Survey of Hallucination in Natural Language Generation // ACM Computing Surveys (Association for Computing Machinery). 2023. Volume 55, Number 12
- **Ссылка:** https://doi.org/10.1145/3571730
- **Место в источнике:** раздел 2 "Definitions", страница 4 PDF arXiv
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1442](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1442)

### 2.59. Tianyu Gao и соавторы — Н4 [50]

> "our aim is to allow LLMs to generate text with citations, improving their factual correctness and verifiability". [50]

- **Перевод:** «наша цель — дать LLM генерировать текст со ссылками, повышая его фактическую точность и проверяемость». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1453](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1453))
- **Интерпретация для репутационных технологий:** Цель ALCE — научить модели писать текст со ссылками ради точности и проверяемости. Курс использует эту работу как обоснование требования «для каждого утверждения укажи источник» в промпте для реестра; проверяемость появляется, только если ссылку затем открывает человек. [50]
- **Авторы:** Tianyu Gao; Howard Yen; Jiatong Yu; Danqi Chen
- **Дата:** 2023
- **Источник:** Enabling Large Language Models to Generate Text with Citations // Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing. arXiv:2305.14627
- **Ссылка:** https://arxiv.org/pdf/2305.14627
- **Место в источнике:** Abstract, страница 1
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1452](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1452)

### 2.60. Tianyu Gao и соавторы — Н4 [50]

> "current systems have considerable room for improvement—For example, on the ELI5 dataset, even the best models lack complete citation support 50% of the time." [50]

- **Перевод:** «текущим системам есть куда расти: например, на наборе ELI5 даже у лучших моделей в 50% случаев нет полной поддержки утверждений ссылками». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1455](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1455))
- **Интерпретация для репутационных технологий:** Даже лучшие модели на ELI5 в половине случаев не дают полной поддержки утверждений ссылками — эта цифра лежит в основе гипотезы Г2-2 Дня 2. Практический вывод: требовать ссылки в промпте нужно, но проверять их всё равно вручную. [50]
- **Авторы:** Tianyu Gao; Howard Yen; Jiatong Yu; Danqi Chen
- **Дата:** 2023
- **Источник:** Enabling Large Language Models to Generate Text with Citations // Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing. arXiv:2305.14627
- **Ссылка:** https://arxiv.org/pdf/2305.14627
- **Место в источнике:** Abstract, страница 1
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1454](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1454)

### 2.61. Tianyu Gao и соавторы — Н4 [50]

> "Write an accurate, engaging, and concise answer for the given question using only the provided search results (some of which might be irrelevant) and cite them properly. Use an unbiased and journalistic tone. Always cite for any factual claim." [50]

- **Перевод:** «Напиши точный, увлекательный и краткий ответ, используя только предоставленные результаты поиска (часть может быть нерелевантна), и корректно ссылайся на них. Используй беспристрастный журналистский тон. Всегда давай ссылку для любого фактического утверждения». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1457](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1457))
- **Интерпретация для репутационных технологий:** Инструкция из ALCE — отвечать только по предоставленным результатам и ссылаться для любого фактического утверждения — готовый образец формулировки для промпта репутационного аналитика. Ограничение задаёт та же статья: с таким промптом полная поддержка ссылками всё равно не гарантирована. [50]
- **Авторы:** Tianyu Gao; Howard Yen; Jiatong Yu; Danqi Chen
- **Дата:** 2023
- **Источник:** Enabling Large Language Models to Generate Text with Citations // Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing. arXiv:2305.14627
- **Ссылка:** https://arxiv.org/pdf/2305.14627
- **Место в источнике:** Appendix, Table 23 (инструкция промпта), страница 21
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1456](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1456)

### 2.62. National Institute of Standards and Technology — Н6 [51]

> "“Confabulation” refers to a phenomenon in which GAI systems generate and confidently present erroneous or false content in response to prompts." [51]

- **Перевод:** «"Конфабуляция" — явление, при котором системы генеративного ИИ в ответ на промпты порождают и уверенно подают ошибочное или ложное содержание». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1481](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1481))
- **Интерпретация для репутационных технологий:** NIST определяет конфабуляцию как уверенную подачу ошибочного или ложного содержания. Каталог курса называет этот документ главным авторитетным аргументом против обещаний, что ИИ можно заставить не ошибаться; в отчёте уверенный тон модели не заменяет источника. [51]
- **Авторы:** National Institute of Standards and Technology (Национальный институт стандартов и технологий США) — коллективный автор
- **Дата:** июль 2024
- **Источник:** Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)
- **Ссылка:** https://doi.org/10.6028/NIST.AI.600-1
- **Место в источнике:** раздел 2.2 "Confabulation", страница 6 (страница 10 PDF)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1480](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1480)

### 2.63. National Institute of Standards and Technology — Н6 [51]

> "Confabulations are a natural result of the way generative models are designed". [51]

- **Перевод:** «Конфабуляции — естественное следствие того, как устроены генеративные модели». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1483](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1483))
- **Интерпретация для репутационных технологий:** Конфабуляции — естественное следствие устройства генеративных моделей, поэтому промптом их нельзя исключить полностью. На Дне 2 это опора тезиса «ИИ ускоряет сбор и ускоряет ошибку»: ИИ полезен на этапе сбора и черновой сортировки, а каждое его утверждение проходит провенанс. [51]
- **Авторы:** National Institute of Standards and Technology (Национальный институт стандартов и технологий США) — коллективный автор
- **Дата:** июль 2024
- **Источник:** Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)
- **Ссылка:** https://doi.org/10.6028/NIST.AI.600-1
- **Место в источнике:** раздел 2.2 "Confabulation", страница 6 (страница 10 PDF)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1482](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1482)

### 2.64. National Institute of Standards and Technology — Н6 [51]

> "GAI outputs may also include confabulated logic or citations that purport to justify or explain the system’s answer, which may further mislead humans into inappropriately trusting the system’s output." [51]

- **Перевод:** «Вывод может содержать вымышленную логику или ссылки, будто бы обосновывающие ответ, что еще сильнее подталкивает людей к неоправданному доверию». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1485](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1485))
- **Интерпретация для репутационных технологий:** Модель может выдумать и логику, и ссылки, которые будто бы обосновывают ответ, — это ещё сильнее подталкивает к доверию. Курс делает отсюда важный вывод для реестра: метка «источник указан» не значит «источник проверен», ссылку человек открывает сам. [51]
- **Авторы:** National Institute of Standards and Technology (Национальный институт стандартов и технологий США) — коллективный автор
- **Дата:** июль 2024
- **Источник:** Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)
- **Ссылка:** https://doi.org/10.6028/NIST.AI.600-1
- **Место в источнике:** раздел 2.2 "Confabulation", страница 6 (страница 10 PDF)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1484](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1484)

### 2.65. National Institute of Standards and Technology — Н6 [51]

> "This phenomenon is an example of automation bias, or excessive deference to automated systems. Automation bias can exacerbate other risks of GAI, such as risks of confabulation or risks of bias or homogenization." [51]

- **Перевод:** «Это пример automation bias — чрезмерного доверия автоматизированным системам. Он может усиливать другие риски генеративного ИИ, в том числе конфабуляции, предвзятость и гомогенизацию». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1487](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1487))
- **Интерпретация для репутационных технологий:** Automation bias — чрезмерное доверие автоматизированным системам — усиливает риск конфабуляций. Каталог курса использует это для обоснования human-in-the-loop: решение по репутационному анализу принимает человек, который проверил основания, а не тот, кто согласился с выводом машины. [51]
- **Авторы:** National Institute of Standards and Technology (Национальный институт стандартов и технологий США) — коллективный автор
- **Дата:** июль 2024
- **Источник:** Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)
- **Ссылка:** https://doi.org/10.6028/NIST.AI.600-1
- **Место в источнике:** раздел 2.7 "Human-AI Configuration", страница 9 (страница 13 PDF)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1486](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1486)

### 2.66. Anthropic — Н7 [52]

> "Allow Claude to say "I don't know": Explicitly give Claude permission to admit uncertainty. This simple technique can drastically reduce false information." [52]

- **Перевод:** «Разрешите Claude сказать "не знаю": явно позвольте ему признавать неуверенность. Этот простой прием может резко сократить ложную информацию». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1497](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1497))
- **Интерпретация для репутационных технологий:** Документация Anthropic советует явно разрешить модели сказать «не знаю». В промпте Дня 2 это превращено в запрет заполнять пустое поле догадкой — модель пишет «в источниках нет»; ограничение — это рекомендации вендора, а не рецензируемое исследование. [52]
- **Авторы:** Anthropic — документация компании, персональные авторы не указаны
- **Дата:** страница документации, дата обращения 30 сентября 2026
- **Источник:** Reduce Hallucinations // Claude Documentation: Test and Evaluate — Strengthen Guardrails
- **Ссылка:** https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- **Место в источнике:** Раздел "Basic hallucination minimization strategies"
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1496](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1496)

### 2.67. Anthropic — Н7 [52]

> "If you're unsure about any aspect or if the report lacks necessary information, say "I don't have enough information to confidently assess this."" [52]

- **Перевод:** «Если не уверен в каком-либо аспекте или в отчете не хватает данных, скажи: "У меня недостаточно информации для уверенной оценки"». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1499](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1499))
- **Интерпретация для репутационных технологий:** Пример фразы, которой модель должна отвечать при нехватке данных, практически совпадает с приёмами курса для реестра: недостающее помечается, а не достраивается. Для репутационного аналитика это готовый шаблон, который делает пробел видимым и переводимым в PARTIAL; источник — документация вендора. [52]
- **Авторы:** Anthropic — документация компании, персональные авторы не указаны
- **Дата:** страница документации, дата обращения 30 сентября 2026
- **Источник:** Reduce Hallucinations // Claude Documentation: Test and Evaluate — Strengthen Guardrails
- **Ссылка:** https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- **Место в источнике:** Раздел "Basic hallucination minimization strategies"; пример промпта
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1498](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1498)

### 2.68. Anthropic — Н7 [52]

> "Verify with citations: Make Claude's response auditable by having it cite quotes and sources for each of its claims." и "If it can't find a quote, it must retract the claim." [52]

- **Перевод:** «Проверка через цитирование: сделайте ответ проверяемым, требуя цитаты и источники для каждого утверждения»; «Если цитату найти не удается, утверждение нужно отозвать». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1501](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1501))
- **Интерпретация для репутационных технологий:** Требование подкреплять каждое утверждение цитатой и отзывать его, если цитаты нет, делает ответ модели проверяемым. Курс использует этот приём в Промпте-разведчике; но, как предупреждает NIST, ссылки тоже могут быть вымышлены, поэтому человек открывает каждую сам. [52]
- **Авторы:** Anthropic — документация компании, персональные авторы не указаны
- **Дата:** страница документации, дата обращения 30 сентября 2026
- **Источник:** Reduce Hallucinations // Claude Documentation: Test and Evaluate — Strengthen Guardrails
- **Ссылка:** https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- **Место в источнике:** Раздел "Basic hallucination minimization strategies"
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1500](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1500)

### 2.69. Anthropic — Н7 [52]

> "Best-of-N verification: Run Claude through the same prompt multiple times and compare the outputs. Inconsistencies across outputs could indicate hallucinations." и "External knowledge restriction: Explicitly instruct Claude to only use information from provided documents and not its general knowledge." [52]

- **Перевод:** «Проверка best-of-N: прогоните один промпт несколько раз и сравните ответы; расхождения могут указывать на галлюцинации»; «Ограничение внешних знаний: явно укажите использовать только предоставленные документы, а не общие знания». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1503](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1503))
- **Интерпретация для репутационных технологий:** Два приёма: прогонять один промпт несколько раз и сравнивать ответы, а также ограничивать модель только предоставленными документами. Для практика расхождения между прогонами — сигнал возможной галлюцинации, а ограничение внешних знаний не даёт модели подмешивать непроверенное в реестр. [52]
- **Авторы:** Anthropic — документация компании, персональные авторы не указаны
- **Дата:** страница документации, дата обращения 30 сентября 2026
- **Источник:** Reduce Hallucinations // Claude Documentation: Test and Evaluate — Strengthen Guardrails
- **Ссылка:** https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- **Место в источнике:** Раздел "Advanced techniques"
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1502](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1502)

### 2.70. Anthropic — Н7 [52]

> "Remember, while these techniques significantly reduce hallucinations, they don't eliminate them entirely. Always validate critical information, especially for high-stakes decisions." [52]

- **Перевод:** «Помните: эти приемы существенно снижают галлюцинации, но не устраняют их полностью. Всегда проверяйте критически важную информацию, особенно для решений с высокой ценой ошибки». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1505](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1505))
- **Интерпретация для репутационных технологий:** Заключительная оговорка вендора — приёмы существенно снижают галлюцинации, но не устраняют их — даёт курсу готовую формулировку для исправления тезиса «правильный промпт избавляет от ошибок». Критически важные сведения, особенно для решений с высокой ценой ошибки, всё равно проверяет человек. [52]
- **Авторы:** Anthropic — документация компании, персональные авторы не указаны
- **Дата:** страница документации, дата обращения 30 сентября 2026
- **Источник:** Reduce Hallucinations // Claude Documentation: Test and Evaluate — Strengthen Guardrails
- **Ссылка:** https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- **Место в источнике:** Заключительное примечание
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1504](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1504)

### 2.71. OpenAI — Н8 [53]

> "Because the content generated from a model is non-deterministic, prompting to get your desired output is a mix of art and science." [53]

- **Перевод:** «Поскольку вывод модели недетерминирован, получение нужного результата промптингом — смесь искусства и науки». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1515](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1515))
- **Интерпретация для репутационных технологий:** Недетерминированность вывода модели OpenAI называет причиной того, что промптинг — смесь искусства и науки. Каталог курса выводит отсюда приём прогонять промпт несколько раз и сравнивать ответы; в Дне 2 источник прямо не цитируется, это документация вендора. [53]
- **Авторы:** OpenAI — документация компании, персональные авторы не указаны
- **Дата:** страница документации, дата обращения 30 сентября 2026
- **Источник:** Prompt Engineering // OpenAI Application Programming Interface Documentation: Guides
- **Ссылка:** https://developers.openai.com/api/docs/guides/prompt-engineering
- **Место в источнике:** Раздел "Prompt engineering"
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1514](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1514)
- **Примечание:** В материалах Дня 2 прямо не цитируется; источник из каталога курса для самостоятельной работы.

### 2.72. OpenAI — Н8 [53]

> "Building tests and evaluation suites that measure prompt behavior so you can monitor performance as you iterate, or when you change and upgrade model versions". [53]

- **Перевод:** «Создавайте тесты и наборы оценок поведения промпта, чтобы отслеживать качество при доработке или смене версии модели». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1517](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1517))
- **Интерпретация для репутационных технологий:** Совет строить тесты и наборы оценок поведения промпта курс связывает с повторяемостью аналитики: один и тот же промпт для мониторинга должен давать сопоставимый результат при доработке и смене модели. Источник рекомендован для самостоятельной работы и в Дне 2 не цитируется. [53]
- **Авторы:** OpenAI — документация компании, персональные авторы не указаны
- **Дата:** страница документации, дата обращения 30 сентября 2026
- **Источник:** Prompt Engineering // OpenAI Application Programming Interface Documentation: Guides
- **Ссылка:** https://developers.openai.com/api/docs/guides/prompt-engineering
- **Место в источнике:** Раздел "Prompt engineering"; (рекомендация)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1516](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1516)
- **Примечание:** В материалах Дня 2 прямо не цитируется; источник из каталога курса для самостоятельной работы.

### 2.73. OpenAI — Н8 [53]

> "When providing examples, try to show a diverse range of possible inputs with the desired outputs." [53]

- **Перевод:** «Давая примеры, старайтесь показать разнообразные входные данные с желаемыми выходами». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1519](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1519))
- **Интерпретация для репутационных технологий:** Разнообразные примеры входов и желаемых выходов в few-shot помогают модели понять задачу шире одного шаблона. Для репутационного реестра это значит показывать в промпте и подтверждённые, и спорные, и пустые случаи; источник — вендорская документация из каталога, в Дне 2 не цитируется. [53]
- **Авторы:** OpenAI — документация компании, персональные авторы не указаны
- **Дата:** страница документации, дата обращения 30 сентября 2026
- **Источник:** Prompt Engineering // OpenAI Application Programming Interface Documentation: Guides
- **Ссылка:** https://developers.openai.com/api/docs/guides/prompt-engineering
- **Место в источнике:** Раздел "Few-shot learning"
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1518](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1518)
- **Примечание:** В материалах Дня 2 прямо не цитируется; источник из каталога курса для самостоятельной работы.

### 2.74. OpenAI — Н8 [53]

> "To constrain the model's response to a specific set of resources that you have determined will be most beneficial." [53]

- **Перевод:** «Чтобы ограничить ответ модели конкретным набором ресурсов, которые вы сочли наиболее полезными». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1521](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1521))
- **Интерпретация для репутационных технологий:** Ограничение ответа заданным набором ресурсов — вендорская формулировка приёма «работай только с предоставленными источниками». Каталог курса отмечает, что прямого указания на «не знаю» или метки конфликтов в этом тексте нет, поэтому такие приёмы лучше подкреплять документацией Anthropic; в Дне 2 источник не цитируется. [53]
- **Авторы:** OpenAI — документация компании, персональные авторы не указаны
- **Дата:** страница документации, дата обращения 30 сентября 2026
- **Источник:** Prompt Engineering // OpenAI Application Programming Interface Documentation: Guides
- **Ссылка:** https://developers.openai.com/api/docs/guides/prompt-engineering
- **Место в источнике:** Раздел "Include relevant context information"
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1520](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1520)
- **Примечание:** В материалах Дня 2 прямо не цитируется; источник из каталога курса для самостоятельной работы.

### 2.75. Публичное акционерное общество «Сбербанк» — Н9 [54]

> «Современные языковые модели (LLM) способны создавать ответы, которые выглядят логично и убедительно, но иногда они могут быть вымышленными. Чтобы повысить точность и фактическую достоверность ответов, а так же уменьшить вероятность появления несогласованных или выдуманных данных, можно улучшить промпты.» [54]

- **Интерпретация для репутационных технологий:** Документация GigaChat признаёт, что убедительный ответ модели может быть вымышленным, а улучшенный промпт лишь уменьшает вероятность выдуманных данных. Это русскоязычная опора тезиса Дня 2: правильный запрос снижает частоту галлюцинаций, но не отменяет их; источник — документация вендора. [54]
- **Авторы:** Публичное акционерное общество «Сбербанк» — документация компании, персональные авторы не указаны
- **Дата:** страница документации, дата обращения 30 сентября 2026
- **Источник:** Основы промпт-инжиниринга // Документация GigaChat API, раздел Prompts Hub
- **Ссылка:** https://developers.sber.ru/docs/ru/gigachat/prompts-hub/prompt-engineering
- **Место в источнике:** раздел «Проблема достоверности ответов модели»
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1530](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1530)

### 2.76. Публичное акционерное общество «Сбербанк» — Н9 [54]

> «Ограничьте свободу интерпретации. Если модель имеет слишком большую свободу в интерпретации входных данных, это может привести к генерации выдуманных или несогласованных ответов.» [54]

- **Интерпретация для репутационных технологий:** Совет ограничить свободу интерпретации совпадает с запретами Промпта-разведчика: не достраивать выводы там, где фактов нет, и не делать заключений о мотивах. Чем точнее задача и формат вывода, тем меньше места для выдуманных связей; это рекомендация вендора. [54]
- **Авторы:** Публичное акционерное общество «Сбербанк» — документация компании, персональные авторы не указаны
- **Дата:** страница документации, дата обращения 30 сентября 2026
- **Источник:** Основы промпт-инжиниринга // Документация GigaChat API, раздел Prompts Hub
- **Ссылка:** https://developers.sber.ru/docs/ru/gigachat/prompts-hub/prompt-engineering
- **Место в источнике:** раздел «Проблема достоверности ответов модели»
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1531](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1531)

### 2.77. Публичное акционерное общество «Сбербанк» — Н9 [54]

> «Добавьте проверку фактов. Внедрение механизмов проверки фактов может помочь снизить вероятность генерации ложной информации.» [54]

- **Интерпретация для репутационных технологий:** Сбер предлагает встроить проверку фактов, чтобы снизить вероятность ложной информации, — формулировка «снизить», а не «исключить» важна для курса. В репутационной работе проверка фактов — обязательный этап после ответа модели, а не его замена. [54]
- **Авторы:** Публичное акционерное общество «Сбербанк» — документация компании, персональные авторы не указаны
- **Дата:** страница документации, дата обращения 30 сентября 2026
- **Источник:** Основы промпт-инжиниринга // Документация GigaChat API, раздел Prompts Hub
- **Ссылка:** https://developers.sber.ru/docs/ru/gigachat/prompts-hub/prompt-engineering
- **Место в источнике:** раздел «Проблема достоверности ответов модели»
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1532](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1532)

### 2.78. Публичное акционерное общество «Сбербанк» — Н9 [54]

> «если используются цитаты, то в скобках надо указать ссылки на источник, автора и название источника». [54]

- **Интерпретация для репутационных технологий:** Пример системного промпта требует при цитировании указывать источник, автора и название — это русский образец требования «укажи источник» для реестра утверждений. Чтобы запись стала провенансом, к ней нужно добавить дату из источника и проверку ссылки человеком. [54]
- **Авторы:** Публичное акционерное общество «Сбербанк» — документация компании, персональные авторы не указаны
- **Дата:** страница документации, дата обращения 30 сентября 2026
- **Источник:** Основы промпт-инжиниринга // Документация GigaChat API, раздел Prompts Hub
- **Ссылка:** https://developers.sber.ru/docs/ru/gigachat/prompts-hub/prompt-engineering
- **Место в источнике:** Пример системного промпта (раздел о структуре промпта: роль, входные данные, задача, индикатор вывода)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1533](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1533)

### 2.79. Альянс в сфере искусственного интеллекта — Н10 [55]

> «Акторы ИИ не должны допускать передачи полномочий ответственного нравственного выбора СИИ, делегировать ответственность за последствия принятия решений СИИ – за все последствия работы СИИ всегда должен отвечать человек». [55]

- **Интерпретация для репутационных технологий:** Кодекс этики ИИ закрепляет, что за последствия работы ИИ всегда отвечает человек. Каталог курса использует это как российскую опору human-in-the-loop: за репутационное решение, принятое по анализу ИИ, отвечает специалист; в Дне 2 прямо не цитируется, а сам кодекс — добровольный документ, а не закон. [55]
- **Авторы:** Альянс в сфере искусственного интеллекта — коллективный документ, персональные авторы не указаны
- **Дата:** дата принятия в извлечённом тексте не найдена; файл размещён 23 мая 2025
- **Источник:** Кодекс этики в сфере искусственного интеллекта
- **Ссылка:** https://ethics.a-ai.ru/
- **Место в источнике:** Раздел 1, пункт 3 «Ответственность за последствия применения СИИ всегда несет человек», пункт 3.2 «Ответственность», страницы 10–11 (страница 6 PDF)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1542](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1542)
- **Примечание:** В материалах Дня 2 прямо не цитируется; источник из каталога курса для самостоятельной работы.

### 2.80. Альянс в сфере искусственного интеллекта — Н10 [55]

> «Акторам ИИ рекомендуется предоставлять пользователям СИИ достоверную информацию о СИИ, допустимых областях и наиболее эффективных методах применения СИИ, вреде, пользе и существующих ограничениях в их применении.» [55]

- **Интерпретация для репутационных технологий:** Рекомендация сообщать пользователям достоверную информацию об ограничениях ИИ обосновывает честный рассказ слушателям о том, чего промпт не гарантирует. Источник взят из каталога для самостоятельной работы, в Дне 2 не цитируется; кодекс носит добровольный характер. [55]
- **Авторы:** Альянс в сфере искусственного интеллекта — коллективный документ, персональные авторы не указаны
- **Дата:** дата принятия в извлечённом тексте не найдена; файл размещён 23 мая 2025
- **Источник:** Кодекс этики в сфере искусственного интеллекта
- **Ссылка:** https://ethics.a-ai.ru/
- **Место в источнике:** Пункт 6.1 «Достоверность информации о СИИ», страницы 12–13 (страница 7 PDF)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1543](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1543)
- **Примечание:** В материалах Дня 2 прямо не цитируется; источник из каталога курса для самостоятельной работы.

### 2.81. Кирпичёв Александр Евгеньевич — Н11 [56]

> «основной очевидной проблемой использования генеративного ИИ в правосудии все же является риск так называемых галлюцинаций: подобные часто показывают способность производить неправильные, но правдоподобные результаты (Longo, 2023:194), однако выявить галлюцинацию можно, четко понимая ожидаемый результат и порядок работы над ним». [56]

- **Интерпретация для репутационных технологий:** Кирпичёв описывает галлюцинации как неправильные, но правдоподобные результаты и отмечает, что выявить их можно, ясно понимая ожидаемый результат. Каталог курса выводит отсюда правило заранее задавать критерии и шаблон вывода; область статьи — правосудие, в Дне 2 источник не цитируется. [56]
- **Авторы:** Кирпичёв Александр Евгеньевич
- **Дата:** 2024
- **Источник:** Промпты (запросы) для генеративного искусственного интеллекта в юридическом дискурсе // Вестник Российского университета дружбы народов. Серия: Юридические науки. 2024. Том 28, номер 4. Страницы 906–918
- **Ссылка:** https://doi.org/10.22363/2313-2337-2024-28-4-906-918
- **Место в источнике:** страница 913
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1552](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1552)
- **Примечание:** В материалах Дня 2 прямо не цитируется; источник из каталога курса для самостоятельной работы.

### 2.82. Кирпичёв Александр Евгеньевич — Н11 [56]

> «Основной очевидной проблемой использования генеративного ИИ в правосудии является риск «галлюцинаций» – неправильных, но правдоподобных результатов. Для минимизации этого риска необходима стандартизация промптов». [56]

- **Интерпретация для репутационных технологий:** Вывод статьи — для минимизации риска галлюцинаций нужна стандартизация промптов — поддерживает идею единого промпта для реестра утверждений. Формулировка «минимизация», а не устранение, согласуется с позицией курса; предметная область — правосудие, источник рекомендован для самостоятельной работы. [56]
- **Авторы:** Кирпичёв Александр Евгеньевич
- **Дата:** 2024
- **Источник:** Промпты (запросы) для генеративного искусственного интеллекта в юридическом дискурсе // Вестник Российского университета дружбы народов. Серия: Юридические науки. 2024. Том 28, номер 4. Страницы 906–918
- **Ссылка:** https://doi.org/10.22363/2313-2337-2024-28-4-906-918
- **Место в источнике:** страница 915 (Заключение)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1553](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1553)
- **Примечание:** В материалах Дня 2 прямо не цитируется; источник из каталога курса для самостоятельной работы.

### 2.83. Давлатова Мадина Асатуллоевна и соавторы — Н12 [57]

> «информация в сгенерированных ответах может быть ошибочной – содержать вымышленные факты и источники, неверные данные [10]. Такого рода некорректные ответы принято называть «галлюцинациями», и их сложно распознать начинающим пользователям, которые не обладают глубокими экспертными знаниями или не используют критическое мышление при анализе ответов ГенИИ.» [57]

- **Интерпретация для репутационных технологий:** Давлатова и Сперанская подчёркивают, что вымышленные факты и источники трудно распознать начинающим пользователям без экспертизы и критического мышления. Курс отсюда делает этап проверки обязательным: слушатель сверяет ответ ИИ с источниками, а не оценивает его на правдоподобие. [57]
- **Авторы:** Давлатова Мадина Асатуллоевна; Сперанская Марина Викторовна
- **Дата:** 2026
- **Источник:** Промпт-инжиниринг как ключевая компетенция в образовании: сущность, особенности и подходы к оцениванию // Высшее образование в России. 2026. Том 35, номер 2. Страницы 53–73
- **Ссылка:** https://doi.org/10.31992/0869-3617-2026-35-2-53-73
- **Место в источнике:** страница 62
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1562](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1562)

### 2.84. Давлатова Мадина Асатуллоевна и соавторы — Н12 [57]

> «Критическое мышление – это медиатор между первым и третьим принципами, предполагающий оценку, проверку и анализ результатов, выдаваемых ГенИИ и наличие умений корректировать промпты.» [57]

- **Интерпретация для репутационных технологий:** Критическое мышление авторы определяют как оценку, проверку и анализ ответов ГенИИ вместе с умением корректировать промпты. Для курса это описание роли человека в работе с ИИ: проверить ссылку, дату и статус, а при ошибке — переписать запрос. [57]
- **Авторы:** Давлатова Мадина Асатуллоевна; Сперанская Марина Викторовна
- **Дата:** 2026
- **Источник:** Промпт-инжиниринг как ключевая компетенция в образовании: сущность, особенности и подходы к оцениванию // Высшее образование в России. 2026. Том 35, номер 2. Страницы 53–73
- **Ссылка:** https://doi.org/10.31992/0869-3617-2026-35-2-53-73
- **Место в источнике:** страница 62
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1563](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1563)

### 2.85. Давлатова Мадина Асатуллоевна и соавторы — Н12 [57]

> «в литературе преобладают описания техник (Chain-of-Thought, few-shot, self-consistency и др.) над эмпирическими исследованиями.» [57]

- **Интерпретация для репутационных технологий:** Авторы честно отмечают, что в литературе описания техник промптинга преобладают над эмпирическими исследованиями. Каталог курса считает это полезным ограничением для лектора: приёмы вроде chain-of-thought и few-shot подаются как рабочие практики, а не как доказанные гарантии. [57]
- **Авторы:** Давлатова Мадина Асатуллоевна; Сперанская Марина Викторовна
- **Дата:** 2026
- **Источник:** Промпт-инжиниринг как ключевая компетенция в образовании: сущность, особенности и подходы к оцениванию // Высшее образование в России. 2026. Том 35, номер 2. Страницы 53–73
- **Ссылка:** https://doi.org/10.31992/0869-3617-2026-35-2-53-73
- **Место в источнике:** страница 69 (ограничения)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1564](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1564)

## День 3. Стейкхолдеры, точки влияния и каналы коммуникации

### 3.1. Ronald K. Mitchell и соавторы — С1 [58]

> "managers simply cannot attend to all actual or potential claims, and that propose a variety of priorities for managerial attention" [58]

- **Перевод:** «менеджеры просто не могут уделять внимание всем фактическим или потенциальным притязаниям; [подходы] предлагают различные приоритеты управленческого внимания». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1169](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1169))
- **Интерпретация для репутационных технологий:** Исходная посылка всего Дня 3: внимание и ресурсы ограничены, поэтому карта стейкхолдеров нужна не для того, чтобы работать со всеми, а чтобы обоснованно выбрать немногих. Курс опирается на эту фразу, когда требует из примерно 10 узлов отобрать 2–3 точки влияния и явно назвать остальных «не сейчас». [58]
- **Авторы:** Ronald K. Mitchell; Bradley R. Agle; Donna J. Wood
- **Дата:** октябрь 1997
- **Источник:** Toward a Theory of Stakeholder Identification and Salience: Defining the Principle of Who and What Really Counts // Academy of Management Review. 1997. Volume 22, Number 4. Pages 853–886
- **Ссылка:** https://www.jstor.org/stable/259247
- **Место в источнике:** страница 854
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1168](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1168)

### 3.2. Ronald K. Mitchell и соавторы — С1 [58]

> "stakeholder salience-the degree to which managers give priority to competing stakeholder claims" [58]

- **Перевод:** «значимость стейкхолдеров — степень, в которой менеджеры отдают приоритет конкурирующим притязаниям стейкхолдеров». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1171](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1171))
- **Интерпретация для репутационных технологий:** Значимость здесь — не свойство стейкхолдера самого по себе, а степень приоритета, который менеджер отдаёт его притязанию среди конкурирующих. Для репутационного практика это рабочее определение «точки влияния»: значим тот, чьё требование мы обязаны поставить выше других в рамках конкретной задачи. [58]
- **Авторы:** Ronald K. Mitchell; Bradley R. Agle; Donna J. Wood
- **Дата:** октябрь 1997
- **Источник:** Toward a Theory of Stakeholder Identification and Salience: Defining the Principle of Who and What Really Counts // Academy of Management Review. 1997. Volume 22, Number 4. Pages 853–886
- **Ссылка:** https://www.jstor.org/stable/259247
- **Место в источнике:** страница 854
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1170](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1170)

### 3.3. Ronald K. Mitchell и соавторы — С1 [58]

> "(1) the stakeholder's power to influence the firm, (2) the legitimacy of the stakeholder's relationship with the firm, and (3) the urgency of the stakeholder's claim on the firm" [58]

- **Перевод:** «(1) власть стейкхолдера влиять на фирму, (2) легитимность отношений стейкхолдера с фирмой и (3) срочность притязания стейкхолдера к фирме». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1173](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1173))
- **Интерпретация для репутационных технологий:** Три атрибута — власть, легитимность, срочность — исходная логика критериев курса: власть примерно соответствует «власти над бизнес-процессами, финансами, репутацией», срочность — коммуникационной активности и остроте требования. По каталогу, критериев «доступность», «качество данных» и «возможный вред» у Митчелла нет: это надстройка курса, и её нужно так и подавать. [58]
- **Авторы:** Ronald K. Mitchell; Bradley R. Agle; Donna J. Wood
- **Дата:** октябрь 1997
- **Источник:** Toward a Theory of Stakeholder Identification and Salience: Defining the Principle of Who and What Really Counts // Academy of Management Review. 1997. Volume 22, Number 4. Pages 853–886
- **Ссылка:** https://www.jstor.org/stable/259247
- **Место в источнике:** страница 854
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1172](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1172)

### 3.4. Ronald K. Mitchell и соавторы — С1 [58]

> "each attribute is a variable, not a steady state" [58]

- **Перевод:** «каждый атрибут — переменная, а не устойчивое состояние». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1175](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1175))
- **Интерпретация для репутационных технологий:** Атрибуты стейкхолдера меняются со временем, поэтому карта точек влияния — снимок, а не справочник. Отсюда практическое правило курса: регулярно пересматривать карту и фиксировать условие, при котором узел из «не сейчас» вернётся в план. [58]
- **Авторы:** Ronald K. Mitchell; Bradley R. Agle; Donna J. Wood
- **Дата:** октябрь 1997
- **Источник:** Toward a Theory of Stakeholder Identification and Salience: Defining the Principle of Who and What Really Counts // Academy of Management Review. 1997. Volume 22, Number 4. Pages 853–886
- **Ссылка:** https://www.jstor.org/stable/259247
- **Место в источнике:** страница 868
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1174](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1174)

### 3.5. Ronald K. Mitchell и соавторы — С1 [58]

> "power by itself does not guarantee high salience in a stakeholder-manager relationship. Power gains authority through legitimacy, and it gains exercise through urgency." [58]

- **Перевод:** «власть сама по себе не гарантирует высокой значимости в отношениях стейкхолдера и менеджера. Власть обретает полномочность через легитимность, а реализацию — через срочность». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1177](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1177))
- **Интерпретация для репутационных технологий:** Ключевой аргумент против выбора по одной лишь власти: крупный игрок без легитимного отношения к задаче и без срочного притязания не становится приоритетом. Курс использует эту мысль, чтобы объяснить, почему одного критерия «власти» недостаточно и узел оценивают по нескольким осям сразу. [58]
- **Авторы:** Ronald K. Mitchell; Bradley R. Agle; Donna J. Wood
- **Дата:** октябрь 1997
- **Источник:** Toward a Theory of Stakeholder Identification and Salience: Defining the Principle of Who and What Really Counts // Academy of Management Review. 1997. Volume 22, Number 4. Pages 853–886
- **Ссылка:** https://www.jstor.org/stable/259247
- **Место в источнике:** страница 869
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1176](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1176)

### 3.6. Ronald K. Mitchell и соавторы — С1 [58]

> "Proposition 1: Stakeholder salience will be positively related to the cumulative number of stakeholder attributes-power, legitimacy, and urgency-perceived by managers to be present." [58]

- **Перевод:** «Положение 1: значимость стейкхолдера положительно связана с совокупным числом атрибутов стейкхолдера — власти, легитимности и срочности, — которые менеджеры считают присутствующими». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1179](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1179))
- **Интерпретация для репутационных технологий:** Чем больше атрибутов (власть, легитимность, срочность) менеджер видит у стейкхолдера, тем выше его значимость. Это теоретическое основание для отбора 2–3 точек из примерно 10: приоритет получают узлы, у которых совпадает несколько критериев. Важно слово «perceived» — речь о восприятии менеджеров, а не об объективной мере. [58]
- **Авторы:** Ronald K. Mitchell; Bradley R. Agle; Donna J. Wood
- **Дата:** октябрь 1997
- **Источник:** Toward a Theory of Stakeholder Identification and Salience: Defining the Principle of Who and What Really Counts // Academy of Management Review. 1997. Volume 22, Number 4. Pages 853–886
- **Ссылка:** https://www.jstor.org/stable/259247
- **Место в источнике:** страница 873
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1178](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1178)

### 3.7. Ronald K. Mitchell и соавторы — С1 [58]

> "those who can command the attention of the news media (symbolic)" [58]

- **Перевод:** «те, кто способен привлечь внимание новостных СМИ (символическая [власть])». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1181](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1181))
- **Интерпретация для репутационных технологий:** Способность привлечь внимание новостных СМИ Митчелл и соавторы относят к символической власти — для репутационной работы это прямое указание, что медийный доступ является ресурсом влияния. Курс противопоставляет эту цитату выводу С7 о том, что СМИ «не требуют управления». [58]
- **Авторы:** Ronald K. Mitchell; Bradley R. Agle; Donna J. Wood
- **Дата:** октябрь 1997
- **Источник:** Toward a Theory of Stakeholder Identification and Salience: Defining the Principle of Who and What Really Counts // Academy of Management Review. 1997. Volume 22, Number 4. Pages 853–886
- **Ссылка:** https://www.jstor.org/stable/259247
- **Место в источнике:** страница 875
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1180](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1180)

### 3.8. R. Edward Freeman — С2 [59]

> "any group or individual who can affect or is affected by the achievement of the organization's objectives" [59]

- **Перевод:** «любая группа или индивид, который может влиять на достижение целей организации или на которого оно влияет». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1192](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1192))
- **Интерпретация для репутационных технологий:** Двустороннее определение Фримена: стейкхолдер — и тот, кто может влиять, и тот, на кого влияют. Курс примерно соотносит эти половины с парой «точка влияния / аудитория», но у самого Фримена такого деления на два класса нет. Цитата вторичная — по Mitchell и соавторам, 1997, книга не просмотрена. [59]
- **Авторы:** R. Edward Freeman; цитата приведена по статье Ronald K. Mitchell, Bradley R. Agle, Donna J. Wood
- **Дата:** 1984 (книга); 1997 (вторичный источник)
- **Источник:** Strategic Management: A Stakeholder Approach. Boston: Pitman, 1984, цитируется по: Toward a Theory of Stakeholder Identification and Salience // Academy of Management Review. 1997. Page 854
- **Ссылка:** https://www.jstor.org/stable/259247
- **Место в источнике:** Freeman 1984, страница 46, цитируется по Mitchell и соавторы, 1997, страница 854
- **Статус проверки:** VERIFIED-SECONDARY
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1191](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1191)

### 3.9. Richard L. Daft и соавторы — С3 [60]

> "Information richness is defined as the ability of information to change understanding within a time interval." [60]

- **Перевод:** «Насыщенность информации определяется как способность информации изменить понимание в пределах некоторого промежутка времени». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1205](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1205))
- **Интерпретация для репутационных технологий:** Насыщенность канала измеряется не охватом, а способностью изменить понимание за ограниченное время. Для стратегии коммуникации это критерий выбора вида контакта: чем сложнее и спорнее тема для точки влияния, тем насыщеннее должен быть канал. Ограничение: теория описывает внутриорганизационную коммуникацию 1980-х годов. [60]
- **Авторы:** Richard L. Daft; Robert H. Lengel
- **Дата:** май 1986
- **Источник:** Organizational Information Requirements, Media Richness and Structural Design // Management Science. 1986. Volume 32, Number 5. Pages 554–571
- **Ссылка:** https://doi.org/10.1287/mnsc.32.5.554
- **Место в источнике:** страница 560
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1204](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1204)

### 3.10. Richard L. Daft и соавторы — С3 [60]

> "In order of decreasing richness, the media classifications are (1) face-to-face, (2) telephone, (3) personal documents such as letters or memos, (4) impersonal written documents, and (5) numeric documents." [60]

- **Перевод:** «В порядке убывания насыщенности каналы классифицируются так: (1) личная встреча, (2) телефон, (3) персональные документы — письма или служебные записки, (4) обезличенные письменные документы и (5) числовые документы». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1207](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1207))
- **Интерпретация для репутационных технологий:** Иерархия каналов от личной встречи до числовых документов даёт лектору основу для выбора «встреча / письмо / публичное заявление». Публичное заявление и цифровые каналы в этой шкале отсутствуют, поэтому их размещение в ней и перенос на внешних стейкхолдеров — экстраполяция курса, а не вывод авторов. [60]
- **Авторы:** Richard L. Daft; Robert H. Lengel
- **Дата:** май 1986
- **Источник:** Organizational Information Requirements, Media Richness and Structural Design // Management Science. 1986. Volume 32, Number 5. Pages 554–571
- **Ссылка:** https://doi.org/10.1287/mnsc.32.5.554
- **Место в источнике:** страница 560
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1206](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1206)

### 3.11. Richard L. Daft и соавторы — С3 [60]

> "Face-to-face is the richest medium because it provides immediate feedback so that interpretation can be checked." [60]

- **Перевод:** «Личная встреча — самый насыщенный канал, поскольку даёт немедленную обратную связь, позволяющую проверить интерпретацию». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1209](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1209))
- **Интерпретация для репутационных технологий:** Личная встреча ценна обратной связью: можно сразу проверить, как поняли сообщение. Отсюда вывод курса: со сложной, неоднозначной темой к ключевой точке влияния выходят на встречу, а не рассылкой. Перенос с менеджеров внутри организации на внешних стейкхолдеров — экстраполяция курса. [60]
- **Авторы:** Richard L. Daft; Robert H. Lengel
- **Дата:** май 1986
- **Источник:** Organizational Information Requirements, Media Richness and Structural Design // Management Science. 1986. Volume 32, Number 5. Pages 554–571
- **Ссылка:** https://doi.org/10.1287/mnsc.32.5.554
- **Место в источнике:** страница 560
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1208](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1208)

### 3.12. Richard L. Daft и соавторы — С3 [60]

> "media of low richness are effective for processing well understood messages and standard data." [60]

- **Перевод:** «каналы низкой насыщенности эффективны для передачи хорошо понятных сообщений и стандартных данных». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1211](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1211))
- **Интерпретация для репутационных технологий:** Обратная сторона правила насыщенности: стандартную, хорошо понятную информацию достаточно передать письмом или публикацией, и тратить на неё встречу незачем. Помогает распределять ограниченный ресурс контактов между точками влияния и аудиторией; цифровые каналы в исходной теории не рассматривались. [60]
- **Авторы:** Richard L. Daft; Robert H. Lengel
- **Дата:** май 1986
- **Источник:** Organizational Information Requirements, Media Richness and Structural Design // Management Science. 1986. Volume 32, Number 5. Pages 554–571
- **Ссылка:** https://doi.org/10.1287/mnsc.32.5.554
- **Место в источнике:** страница 560
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1210](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1210)

### 3.13. Richard L. Daft и соавторы — С3 [60]

> "face-to-face media were preferred for messages containing equivocality, while written media were used for unequivocal messages." [60]

- **Перевод:** «для сообщений, содержащих неоднозначность, предпочитались личные встречи, а письменные каналы использовались для однозначных сообщений». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1213](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1213))
- **Интерпретация для репутационных технологий:** Эмпирическое наблюдение: для неоднозначных сообщений менеджеры выбирали личную встречу, для однозначных — письменные каналы. В курсе это аргумент подбирать канал под степень неоднозначности темы, а не по привычке. Наблюдение сделано на внутриорганизационной коммуникации, а не на публичных и цифровых каналах. [60]
- **Авторы:** Richard L. Daft; Robert H. Lengel
- **Дата:** май 1986
- **Источник:** Organizational Information Requirements, Media Richness and Structural Design // Management Science. 1986. Volume 32, Number 5. Pages 554–571
- **Ссылка:** https://doi.org/10.1287/mnsc.32.5.554
- **Место в источнике:** страница 555
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1212](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1212)

### 3.14. A. W. van den Ban — С4 [61]

> "Farmers usually hear for the first time of the existence of a new method through the mass media, but the decision to adopt an innovation is mainly influenced by personal contacts." [61]

- **Перевод:** «Фермеры обычно впервые узнают о новом методе из СМИ, но на решение внедрить нововведение в основном влияют личные контакты». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1224](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1224))
- **Интерпретация для репутационных технологий:** Узнают из СМИ, а решают под влиянием личных контактов — эмпирическая основа различия «узнать» (массовый канал, аудитория) и «принять решение» (личный канал, точка влияния). Вывод курса: к точке влияния лучше выходить через личный контакт. Ограничение: данные — сельскохозяйственные инновации в Нидерландах 1960-х, и сам ван ден Бан считает двухступенчатую схему упрощённой. [61]
- **Авторы:** A. W. van den Ban (полное имя в источнике не раскрыто, только инициалы)
- **Дата:** 1964
- **Источник:** A Revision of the Two-Step Flow of Communications Hypothesis // Gazette (International Journal for Mass Communication Studies). 1964. Volume 10, Number 3. Pages 237–249 (страница по перепечатке в хрестоматии)
- **Ссылка:** https://edepot.wur.nl/21986
- **Место в источнике:** перепечатка, страница 263
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1223](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1223)

### 3.15. Paul F. Lazarsfeld и соавторы — С4a [62]

> "Ideas often flow from radio and print to the opinion leaders and from them to the less active sections of the population." [62]

- **Перевод:** «Идеи часто движутся от радио и печати к лидерам мнений, а от них — к менее активным слоям населения». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1235](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1235))
- **Интерпретация для репутационных технологий:** Классическая формулировка двухступенчатого потока: идеи идут от медиа к лидерам мнений, а от них — к менее активным слоям. Каталог называет её прямым прообразом пары «точка влияния / аудитория». Оговорки: речь об электоральной коммуникации, а не о регуляторах, и цитата вторичная — по van den Ban. [62]
- **Авторы:** Paul F. Lazarsfeld; Bernard Berelson; Hazel Gaudet; цитата приведена по A. W. van den Ban
- **Дата:** 1948 (2-е издание; 1-е издание 1944)
- **Источник:** The People's Choice: How the Voter Makes Up His Mind in a Presidential Campaign. 2nd edition. New York: Columbia University Press, 1948, page 151, цитируется по: A Revision of the Two-Step Flow of Communications Hypothesis, 1964
- **Ссылка:** https://edepot.wur.nl/21986
- **Место в источнике:** по van den Ban, перепечатка страница 264
- **Статус проверки:** VERIFIED-SECONDARY
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1234](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1234)

### 3.16. Elihu Katz — С4b [63]

> "despite their greater exposure to the (mass) media, most opinion leaders are primarily affected not by the communication media but by still other people." [63]

- **Перевод:** «несмотря на бо́льшую подверженность воздействию (массовых) СМИ, большинство лидеров мнений испытывают влияние прежде всего не со стороны СМИ, а со стороны других людей». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1246](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1246))
- **Интерпретация для репутационных технологий:** Даже лидеры мнений, больше других читающие СМИ, испытывают влияние прежде всего от других людей. Практический вывод курса: и на саму точку влияния эффективнее действовать через людей, а не через массовые публикации, — довод за канал «через кого». Страница не установлена, цитировать как «Katz 1957, цитируется по: van den Ban 1964». [63]
- **Авторы:** Elihu Katz; цитата приведена по A. W. van den Ban
- **Дата:** 1957
- **Источник:** The Two-Step Flow of Communication: An Up-To-Date Report on an Hypothesis // Public Opinion Quarterly. 1957. Volume 21, Number 1. Pages 61–78, цитируется по: A Revision of the Two-Step Flow of Communications Hypothesis, 1964 (точная страница не установлена)
- **Ссылка:** https://edepot.wur.nl/21986
- **Место в источнике:** страница в оригинале не указана
- **Статус проверки:** VERIFIED-SECONDARY
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1245](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1245)

### 3.17. Marianne Eisenmann и соавторы — С5 [64]

> "Once organizations have identified their stakeholders, there is a struggle for attention: whom to pay attention to, whom to prioritize for more attention, and whom to ignore." [64]

- **Перевод:** «Когда организация определила своих стейкхолдеров, начинается борьба за внимание: кому уделять внимание, кого выделить для повышенного внимания, а кого игнорировать». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1258](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1258))
- **Интерпретация для репутационных технологий:** После составления списка стейкхолдеров начинается борьба за внимание: кому уделять внимание, кого выделить, кого игнорировать. Курс использует эту фразу из IPR-руководства, чтобы обосновать выбор немногих точек влияния и честное решение «не сейчас» для остальных. Это практическое руководство, а не рецензируемая статья. [64]
- **Авторы:** Marianne Eisenmann; John Gilfeather; в руководство входит отредактированная статья Brad L. Rawlins (2006)
- **Дата:** май 2023
- **Источник:** Identifying and Prioritizing Stakeholders for Public Relations — A Guide for Students and Practitioners. Gainesville, Florida: Institute for Public Relations, 2023
- **Ссылка:** https://instituteforpr.org/wp-content/uploads/Stakeholder-Identification-and-Prioritization-FINAL-May-2023.pdf
- **Место в источнике:** страница 4
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1257](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1257)

### 3.18. Marianne Eisenmann и соавторы — С5 [64]

> "Therefore, publics organize from the ranks of stakeholders when they recognize an issue and take action." [64]

- **Перевод:** «Таким образом, общественности формируются из числа стейкхолдеров, когда те осознают проблему и начинают действовать». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1260](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1260))
- **Интерпретация для репутационных технологий:** Общественности возникают из числа стейкхолдеров тогда, когда те осознают проблему и начинают действовать. Для практика это значит, что активность узла возникает по конкретному поводу, поэтому коммуникационную активность оценивают по текущему поводу, а не раз и навсегда. [64]
- **Авторы:** Marianne Eisenmann; John Gilfeather; в руководство входит отредактированная статья Brad L. Rawlins (2006)
- **Дата:** май 2023
- **Источник:** Identifying and Prioritizing Stakeholders for Public Relations — A Guide for Students and Practitioners. Gainesville, Florida: Institute for Public Relations, 2023
- **Ссылка:** https://instituteforpr.org/wp-content/uploads/Stakeholder-Identification-and-Prioritization-FINAL-May-2023.pdf
- **Место в источнике:** страница 5
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1259](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1259)

### 3.19. Marianne Eisenmann и соавторы — С5 [64]

> "Enabling stakeholders have some control and authority over the organization, such as stockholders, board of directors, elected officials, or legislators and regulators." [64]

- **Перевод:** «Наделяющие полномочиями [enabling] стейкхолдеры обладают определённым контролем и властью над организацией: акционеры, совет директоров, выборные должностные лица, законодатели и регуляторы». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1262](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1262))
- **Интерпретация для репутационных технологий:** Стейкхолдеры с контролем и полномочиями над организацией — акционеры, совет директоров, законодатели и регуляторы — в каталоге служат примером, где регулятор назван «enabling stakeholder». При этом обоснование Дня 3 уточняет: регулятор и закон в рамках задачи чаще рамка, чем точка, на которую воздействуют. [64]
- **Авторы:** Marianne Eisenmann; John Gilfeather; в руководство входит отредактированная статья Brad L. Rawlins (2006)
- **Дата:** май 2023
- **Источник:** Identifying and Prioritizing Stakeholders for Public Relations — A Guide for Students and Practitioners. Gainesville, Florida: Institute for Public Relations, 2023
- **Ссылка:** https://instituteforpr.org/wp-content/uploads/Stakeholder-Identification-and-Prioritization-FINAL-May-2023.pdf
- **Место в источнике:** страница 5
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1261](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1261)

### 3.20. Marianne Eisenmann и соавторы — С5 [64]

> "those who face the problem but do not recognize it as a problem are latent publics; those who recognize the problem are aware publics; and those who do something about the problem are active publics." [64]

- **Перевод:** «те, кто сталкивается с проблемой, но не осознаёт её как проблему, — латентные общественности; те, кто осознаёт проблему, — осведомлённые; те, кто что-то предпринимает, — активные общественности». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1264](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1264))
- **Интерпретация для репутационных технологий:** Шкала латентных, осведомлённых и активных общественностей задаёт различение, которое курс переводит в пару «аудитория / точка влияния»: приоритет растёт с осознанием проблемы и действием. Термин «publics» в грюниговском смысле не равен «аудитории» курса — соответствие приблизительное. [64]
- **Авторы:** Marianne Eisenmann; John Gilfeather; в руководство входит отредактированная статья Brad L. Rawlins (2006)
- **Дата:** май 2023
- **Источник:** Identifying and Prioritizing Stakeholders for Public Relations — A Guide for Students and Practitioners. Gainesville, Florida: Institute for Public Relations, 2023
- **Ссылка:** https://instituteforpr.org/wp-content/uploads/Stakeholder-Identification-and-Prioritization-FINAL-May-2023.pdf
- **Место в источнике:** страница 10
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1263](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1263)

### 3.21. Marianne Eisenmann и соавторы — С5 [64]

> "Stakeholders who are also active publics are the top priority." [64]

- **Перевод:** «Высший приоритет — стейкхолдеры, которые одновременно являются активными общественностями». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1266](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1266))
- **Интерпретация для репутационных технологий:** Прямое правило приоритизации: первыми идут стейкхолдеры, которые уже действуют по поводу проблемы. В курсе оно поддерживает выбор 2–3 точек влияния из длинного списка, где решающим оказывается не размер узла, а его активность по текущему поводу. [64]
- **Авторы:** Marianne Eisenmann; John Gilfeather; в руководство входит отредактированная статья Brad L. Rawlins (2006)
- **Дата:** май 2023
- **Источник:** Identifying and Prioritizing Stakeholders for Public Relations — A Guide for Students and Practitioners. Gainesville, Florida: Institute for Public Relations, 2023
- **Ссылка:** https://instituteforpr.org/wp-content/uploads/Stakeholder-Identification-and-Prioritization-FINAL-May-2023.pdf
- **Место в источнике:** страница 12
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1265](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1265)

### 3.22. Marianne Eisenmann и соавторы — С5 [64]

> "Key publics are those whose participation and cooperation are required to accomplish organizational goals." [64]

- **Перевод:** «Ключевые общественности — те, чьё участие и сотрудничество необходимы для достижения целей организации». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1268](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1268))
- **Интерпретация для репутационных технологий:** Ключевые общественности определяются через задачу: без их участия и сотрудничества цель организации недостижима. Это близко к логике курса, где стейкхолдер — связь с задачей, а не пункт в списке «клиенты, партнёры, регуляторы»; узел становится ключевым, если он стоит на пути к результату. [64]
- **Авторы:** Marianne Eisenmann; John Gilfeather; в руководство входит отредактированная статья Brad L. Rawlins (2006)
- **Дата:** май 2023
- **Источник:** Identifying and Prioritizing Stakeholders for Public Relations — A Guide for Students and Practitioners. Gainesville, Florida: Institute for Public Relations, 2023
- **Ссылка:** https://instituteforpr.org/wp-content/uploads/Stakeholder-Identification-and-Prioritization-FINAL-May-2023.pdf
- **Место в источнике:** страница 14
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1267](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1267)

### 3.23. Marianne Eisenmann и соавторы — С5 [64]

> "Effective strategies appeal to the self-interests of the priority publics and reach them through the most appropriate channels" [64]

- **Перевод:** «Эффективные стратегии апеллируют к собственным интересам приоритетных общественностей и достигают их через наиболее подходящие каналы». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1270](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1270))
- **Интерпретация для репутационных технологий:** Мост от приоритизации к стратегии: обращение строят на собственном интересе приоритетной общественности и доводят через подходящий для неё канал. Для слушателей это порядок работы Дня 3 — сначала выбрать точку, затем подобрать её интерес и канал, а не наоборот. [64]
- **Авторы:** Marianne Eisenmann; John Gilfeather; в руководство входит отредактированная статья Brad L. Rawlins (2006)
- **Дата:** май 2023
- **Источник:** Identifying and Prioritizing Stakeholders for Public Relations — A Guide for Students and Practitioners. Gainesville, Florida: Institute for Public Relations, 2023
- **Ссылка:** https://instituteforpr.org/wp-content/uploads/Stakeholder-Identification-and-Prioritization-FINAL-May-2023.pdf
- **Место в источнике:** страница 14
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1269](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1269)

### 3.24. Marianne Eisenmann и соавторы — С5 [64]

> "The intervening publics pass information on to the priority publics and act as opinion leaders." [64]

- **Перевод:** «Промежуточные общественности передают информацию приоритетным общественностям и выступают лидерами мнений». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1272](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1272))
- **Интерпретация для репутационных технологий:** Промежуточные общественности передают информацию приоритетным и выступают лидерами мнений — то есть являются посредниками. Курс использует это для раздела «через кого»: до точки влияния часто дешевле и надёжнее дойти через доверенного посредника, чем напрямую. [64]
- **Авторы:** Marianne Eisenmann; John Gilfeather; в руководство входит отредактированная статья Brad L. Rawlins (2006)
- **Дата:** май 2023
- **Источник:** Identifying and Prioritizing Stakeholders for Public Relations — A Guide for Students and Practitioners. Gainesville, Florida: Institute for Public Relations, 2023
- **Ссылка:** https://instituteforpr.org/wp-content/uploads/Stakeholder-Identification-and-Prioritization-FINAL-May-2023.pdf
- **Место в источнике:** страница 14
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1271](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1271)

### 3.25. Marianne Eisenmann и соавторы — С5 [64]

> "Influentials are independent opinion leaders who often lend third-party credibility to public relations efforts." [64]

- **Перевод:** «Влиятельные лица [influentials] — независимые лидеры мнений, которые часто придают PR-усилиям доверие “третьей стороны”». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1274](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1274))
- **Интерпретация для репутационных технологий:** Ценность influentials — в независимости: они добавляют PR-усилиям доверие третьей стороны. Для практика вывод в том, что сила лидера мнений — в его независимом голосе, а не в охвате; это одна из пограничных категорий между точкой влияния и каналом. [64]
- **Авторы:** Marianne Eisenmann; John Gilfeather; в руководство входит отредактированная статья Brad L. Rawlins (2006)
- **Дата:** май 2023
- **Источник:** Identifying and Prioritizing Stakeholders for Public Relations — A Guide for Students and Practitioners. Gainesville, Florida: Institute for Public Relations, 2023
- **Ссылка:** https://instituteforpr.org/wp-content/uploads/Stakeholder-Identification-and-Prioritization-FINAL-May-2023.pdf
- **Место в источнике:** страница 15
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1273](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1273)

### 3.26. Marianne Eisenmann и соавторы — С5 [64]

> "No organization has unlimited resources for stakeholder engagement which is why the prioritization exercise is so important." [64]

- **Перевод:** «Ни у одной организации нет неограниченных ресурсов для взаимодействия со стейкхолдерами, поэтому упражнение по приоритизации так важно». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1276](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1276))
- **Интерпретация для репутационных технологий:** Ресурсы на взаимодействие со стейкхолдерами всегда ограничены, поэтому приоритизация обязательна, а не желательна. Вместе с тезисом Митчелла о невозможности уделять внимание всем эта фраза обосновывает выбор 2–3 точек и явный список отложенных узлов. [64]
- **Авторы:** Marianne Eisenmann; John Gilfeather; в руководство входит отредактированная статья Brad L. Rawlins (2006)
- **Дата:** май 2023
- **Источник:** Identifying and Prioritizing Stakeholders for Public Relations — A Guide for Students and Practitioners. Gainesville, Florida: Institute for Public Relations, 2023
- **Ссылка:** https://instituteforpr.org/wp-content/uploads/Stakeholder-Identification-and-Prioritization-FINAL-May-2023.pdf
- **Место в источнике:** страница 31
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1275](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1275)

### 3.27. James E. Grunig и соавторы — С5a [65]

> "publics arise on their own and choose the organization for attention." [65]

- **Перевод:** «общественности возникают сами по себе и сами выбирают организацию объектом своего внимания». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1287](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1287))
- **Интерпретация для репутационных технологий:** Общественности возникают сами и сами выбирают организацию объектом внимания, поэтому точку влияния нельзя просто «назначить» из списка аудиторий. Активность возникает по поводу конкретной проблемы и оценивается по текущему поводу. Цитата получена из вторичного источника, текст главы Грюнига и Реппера не просмотрен. [65]
- **Авторы:** James E. Grunig; Fred C. Repper; цитата приведена по руководству Marianne Eisenmann, John Gilfeather
- **Дата:** 1992
- **Источник:** Strategic Management, Publics, and Issues // Excellence in Public Relations and Communication Management / edited by James E. Grunig. Hillsdale, New Jersey: Lawrence Erlbaum Associates, 1992, page 128, цитируется по: Identifying and Prioritizing Stakeholders for Public Relations — A Guide for Students and Practitioners. Gainesville, Florida: Institute for Public Relations, 2023, page 5
- **Ссылка:** https://instituteforpr.org/wp-content/uploads/Stakeholder-Identification-and-Prioritization-FINAL-May-2023.pdf
- **Место в источнике:** по С5, страница 5
- **Статус проверки:** VERIFIED-SECONDARY
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1286](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1286)

### 3.28. Завгородняя Марина Юрьевна — С6 [66]

> «Теория двухступенчатого потока сформулировала центральную роль межличностных посредников (лидеров мнений), которые интерпретируют и фильтруют медиасообщения, превращая влияние СМИ в процесс, встроенный в сеть доверительных связей» [66]

- **Интерпретация для репутационных технологий:** Современный русскоязычный пересказ двухступенчатого потока: лидеры мнений интерпретируют и фильтруют медиасообщения, встраивая их в сеть доверительных связей. Удобен для слайда; речь в статье идёт о цифровых лидерах мнений, а не о регуляторах, и сама статья обзорная. [66]
- **Авторы:** Завгородняя Марина Юрьевна
- **Дата:** 2026
- **Источник:** Место Пола Лазарсфельда в науке: современное применение концепций // Власть. 2026. Том 34, номер 1. Страницы 195–199
- **Ссылка:** https://www.jour.fnisc.ru/index.php/vlast/article/view/11077
- **Место в источнике:** страница 195
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1298](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1298)

### 3.29. Завгородняя Марина Юрьевна — С6 [66]

> «Первым этапом становится картирование сетевой структуры и выявление аккаунтов с наибольшей «проводимостью» информации». В фокус попадают аккаунты с высокой коммуникативной активностью и устойчивой репутацией внутри конкретного сообщества» [66]

- **Интерпретация для репутационных технологий:** Процедура «сначала карта, потом выбор»: картировать сеть и искать узлы с наибольшей «проводимостью», высокой активностью и устойчивой репутацией в сообществе. Поддерживает критерий курса «коммуникационная активность»; при этом статья короткая, обзорная и касается цифровых лидеров мнений. [66]
- **Авторы:** Завгородняя Марина Юрьевна
- **Дата:** 2026
- **Источник:** Место Пола Лазарсфельда в науке: современное применение концепций // Власть. 2026. Том 34, номер 1. Страницы 195–199
- **Ссылка:** https://www.jour.fnisc.ru/index.php/vlast/article/view/11077
- **Место в источнике:** страница 197
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1299](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1299)

### 3.30. Джонек-Ковальска И. и соавторы — С7 [67]

> «А.Менделоу [15] предложила использовать для систематизации заинтересованных сторон матрицу (в дальнейшем «матрица Менделоу»), напоминающую матрицу SWОT-анализа, где стейкхолдеры распределяются по уровню полномочий и заинтересованности в реализации проекта.» [67]

- **Интерпретация для репутационных технологий:** Русскоязычная ссылка на матрицу Менделоу: стейкхолдеров раскладывают по полномочиям и заинтересованности. Годится как привычный инструмент для первичной сортировки карты. Оригинал Менделоу в курсе не просмотрен и известен только по этому пересказу; сама статья — отраслевой кейс горных проектов. [67]
- **Авторы:** Джонек-Ковальска И. (Izabela Jonek-Kowalska — вероятно, но связь с этой статьёй не подтверждена; полное имя в открытых источниках не установлено); Пономаренко Татьяна Владимировна; Маринина Оксана Анатольевна
- **Дата:** август 2018
- **Источник:** Проблемы взаимодействия со стейкхолдерами при реализации долгосрочных горных проектов // Записки Горного института. 2018. Том 232. Страницы 428–437
- **Ссылка:** https://doi.org/10.31897/PMI.2018.4.428
- **Место в источнике:** страница 432
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1310](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1310)

### 3.31. Джонек-Ковальска И. и соавторы — С7 [67]

> «В матрицах анализа стейкхолдеров под властью понимается уровень полномочий, под интересом – уровень заинтересованности в результатах проекта, под влиянием – уровень участия в проекте, под воздействием – способность вносить изменения в проект.» [67]

- **Интерпретация для репутационных технологий:** Даёт русские термины для критериев: власть, интерес, влияние, воздействие — с различием между участием в проекте и способностью его изменить. Лектору полезно для точного словаря при оценке узлов; определения взяты из отраслевого кейса горных проектов. [67]
- **Авторы:** Джонек-Ковальска И. (Izabela Jonek-Kowalska — вероятно, но связь с этой статьёй не подтверждена; полное имя в открытых источниках не установлено); Пономаренко Татьяна Владимировна; Маринина Оксана Анатольевна
- **Дата:** август 2018
- **Источник:** Проблемы взаимодействия со стейкхолдерами при реализации долгосрочных горных проектов // Записки Горного института. 2018. Том 232. Страницы 428–437
- **Ссылка:** https://doi.org/10.31897/PMI.2018.4.428
- **Место в источнике:** страница 432
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1311](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1311)

### 3.32. Джонек-Ковальска И. и соавторы — С7 [67]

> «Самой влиятельной группой являются «категорические» стейкхолдеры, обладающие одновременно тремя атрибутами. Данную группу заинтересованных сторон следует отнести к ключевым стейкхолдерам – выстраивание политик взаимоотношения с ними требует самого тщательного подхода» [67]

- **Интерпретация для репутационных технологий:** Русское изложение модели Митчелла: «категорические» стейкхолдеры с тремя атрибутами — самая влиятельная группа, отношения с которой требуют самого тщательного подхода. В курсе это примерный аналог выбранных 2–3 точек влияния; источник отраслевой, о горных проектах. [67]
- **Авторы:** Джонек-Ковальска И. (Izabela Jonek-Kowalska — вероятно, но связь с этой статьёй не подтверждена; полное имя в открытых источниках не установлено); Пономаренко Татьяна Владимировна; Маринина Оксана Анатольевна
- **Дата:** август 2018
- **Источник:** Проблемы взаимодействия со стейкхолдерами при реализации долгосрочных горных проектов // Записки Горного института. 2018. Том 232. Страницы 428–437
- **Ссылка:** https://doi.org/10.31897/PMI.2018.4.428
- **Место в источнике:** страница 432
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1312](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1312)

### 3.33. Джонек-Ковальска И. и соавторы — С7 [67]

> «Конкуренты, средства массовой информации (СМИ) и учащиеся профильных учебных заведений являются латентными стейкхолдерами и не требуют управления.» [67]

- **Интерпретация для репутационных технологий:** Цитату курс приводит как материал для дискуссии, а не как норму: вывод, что СМИ латентны и «не требуют управления», противоречит репутационной логике, ведь Митчелл и соавторы относят доступ к СМИ к символической власти. Хороший пример того, как отраслевой контекст искажает перенос модели. [67]
- **Авторы:** Джонек-Ковальска И. (Izabela Jonek-Kowalska — вероятно, но связь с этой статьёй не подтверждена; полное имя в открытых источниках не установлено); Пономаренко Татьяна Владимировна; Маринина Оксана Анатольевна
- **Дата:** август 2018
- **Источник:** Проблемы взаимодействия со стейкхолдерами при реализации долгосрочных горных проектов // Записки Горного института. 2018. Том 232. Страницы 428–437
- **Ссылка:** https://doi.org/10.31897/PMI.2018.4.428
- **Место в источнике:** страница 433
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1313](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1313)

### 3.34. Плахин Андрей Евгеньевич — С8 [68]

> «Для оценки применяется шестибалльная шкала, где 1 – наименьшее влияние, 6 – наибольшее влияние.» [68]

- **Интерпретация для репутационных технологий:** Пример экспертной балльной оценки влияния по шестибалльной шкале — прямой аналог упражнения курса «оценить около 10 узлов по критериям и выбрать 2–3». Ограничение: методика учитывает только ресурсное и нормативное влияние, без коммуникационной активности, доступности и качества данных. [68]
- **Авторы:** Плахин Андрей Евгеньевич
- **Дата:** 2018
- **Источник:** Картирование стейкхолдеров промышленных парковых структур Уральского региона // Управленец. 2018. Том 9, номер 4. Страницы 84–92
- **Ссылка:** https://doi.org/10.29141/2218-5003-2018-9-4-9
- **Место в источнике:** страница 86
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1324](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1324)

### 3.35. Плахин Андрей Евгеньевич — С8 [68]

> «Необходимо учитывать, что доминирующие стейкхолдеры осознают возможность влияния на деятельность парковой структуры и будут иметь склонность в распределительном процессе присваивать сформированные эффекты» [68]

- **Интерпретация для репутационных технологий:** Доминирующие стейкхолдеры понимают свою силу и склонны присваивать созданные эффекты — предупреждение, что сильный партнёр забирает выгоду, и это нужно учитывать при выборе точки влияния. В кейсе статьи доминирующими оказались органы власти; методика охватывает лишь две оси влияния. [68]
- **Авторы:** Плахин Андрей Евгеньевич
- **Дата:** 2018
- **Источник:** Картирование стейкхолдеров промышленных парковых структур Уральского региона // Управленец. 2018. Том 9, номер 4. Страницы 84–92
- **Ссылка:** https://doi.org/10.29141/2218-5003-2018-9-4-9
- **Место в источнике:** страница 86
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1325](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1325)

### 3.36. Моисеенкова Ю. А. — С9 [69]

> «любая группа или индивид, который может сам оказывать влияние или на которого окажет влияние достижение целей организации» [69]

- **Интерпретация для репутационных технологий:** Русская передача определения Фримена, пригодная для слайда «откуда термин»: стейкхолдер и влияет, и испытывает влияние. Это пересказ в обзорной статье, а не текст самого Фримена; о приоритизации в источнике почти ничего нет. [69]
- **Авторы:** Моисеенкова Ю. А. (полное имя в открытых источниках не установлено)
- **Дата:** 2025
- **Источник:** Стандартизация как инструмент развития партнерства бизнеса с заинтересованными сторонами // Информационно-экономические аспекты стандартизации и технического регулирования. 2025. Номер 6 (87)
- **Ссылка:** https://iea.gostinfo.ru/article/view/85
- **Место в источнике:** страница 2 PDF (русская передача определения Фримена, ссылка [8] = Freeman 2010)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1336](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1336)

### 3.37. Моисеенкова Ю. А. — С9 [69]

> «лицо или организация, которые могут воздействовать на осуществление деятельности или принятие решения, быть подверженными их воздействию или воспринимать себя в качестве последних» [69]

- **Интерпретация для репутационных технологий:** Формулировка со ссылкой на ГОСТ Р ИСО 9000–2015 добавляет важную деталь: стейкхолдером становится и тот, кто лишь воспринимает себя затронутым. Для репутационного практика это напоминание, что самоощущение узла тоже входит в карту. Текст стандарта в курсе не проверен — только по этой цитате. [69]
- **Авторы:** Моисеенкова Ю. А. (полное имя в открытых источниках не установлено)
- **Дата:** 2025
- **Источник:** Стандартизация как инструмент развития партнерства бизнеса с заинтересованными сторонами // Информационно-экономические аспекты стандартизации и технического регулирования. 2025. Номер 6 (87)
- **Ссылка:** https://iea.gostinfo.ru/article/view/85
- **Место в источнике:** страница 2 PDF (определение со ссылкой [4] = ГОСТ Р ИСО 9000–2015)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1337](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1337)

### 3.38. Моисеенкова Ю. А. — С9 [69]

> «В данном контексте необходимо уделить внимание стандарту АА1000SES – это стандарт взаимодействия с заинтересованными сторонами. Он обязывает организацию быть актуальной, заслуживающей доверия и открытой, а также ответственной и отзывчивой.» [69]

- **Интерпретация для репутационных технологий:** Нормативный контекст взаимодействия со стейкхолдерами: AA1000SES требует актуальности, доверия, открытости, ответственности и отзывчивости. Можно показать как рамку качества коммуникационной стратегии, но формулировки стандарта даны в пересказе автора статьи, а не по тексту AA1000SES. [69]
- **Авторы:** Моисеенкова Ю. А. (полное имя в открытых источниках не установлено)
- **Дата:** 2025
- **Источник:** Стандартизация как инструмент развития партнерства бизнеса с заинтересованными сторонами // Информационно-экономические аспекты стандартизации и технического регулирования. 2025. Номер 6 (87)
- **Ссылка:** https://iea.gostinfo.ru/article/view/85
- **Место в источнике:** страница 4 PDF
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1338](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1338)

### 3.39. Linton C. Freeman — Д3-Т3 [70]

> "the visibility or the potential for activity in communication" [70]

- **Перевод:** «видимость или потенциал активности в коммуникации» (перевод курса, [day-03/rationale-and-method.md, строка 930](../day-03/rationale-and-method.md#L930))
- **Интерпретация для репутационных технологий:** Степенная центральность — число связей узла — отражает лишь видимость и потенциал активности в коммуникации. Курс использует это, чтобы развести «громкий» узел и точку влияния: много связей ещё не значит способности повлиять на решение по нашей задаче. [70]
- **Авторы:** Linton C. Freeman
- **Дата:** 1978/1979
- **Источник:** Centrality in Social Networks: Conceptual Clarification // Social Networks. 1978–1979. Volume 1. Pages 215–239
- **Ссылка:** https://www.bebr.ufl.edu/sites/default/files/Centrality%20in%20Social%20Networks.pdf
- **Место в источнике:** страница 219
- **Статус проверки:** VERIFIED-FULLTEXT
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `Т3-1`
- **Где в репозитории:** [day-03/rationale-and-method.md, строка 930](../day-03/rationale-and-method.md#L930)

### 3.40. Linton C. Freeman — Д3-Т3 [70]

> "a point that falls on the communication paths between other points exhibits a potential for control of their communication" [70]

- **Перевод:** «потенциал контроля над их коммуникацией» (перевод курса, [day-03/rationale-and-method.md, строка 930](../day-03/rationale-and-method.md#L930))
- **Интерпретация для репутационных технологий:** Узел на путях между другими имеет потенциал контроля над их коммуникацией — это посредническая центральность. Для Дня 3 это аргумент искать точки влияния не среди самых заметных, а среди тех, кто стоит между нами и узлом решения. [70]
- **Авторы:** Linton C. Freeman
- **Дата:** 1978/1979
- **Источник:** Centrality in Social Networks: Conceptual Clarification // Social Networks. 1978–1979. Volume 1. Pages 215–239
- **Ссылка:** https://www.bebr.ufl.edu/sites/default/files/Centrality%20in%20Social%20Networks.pdf
- **Место в источнике:** страница 221
- **Статус проверки:** VERIFIED-FULLTEXT
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `Т3-2`
- **Где в репозитории:** [day-03/rationale-and-method.md, строка 930](../day-03/rationale-and-method.md#L930)

### 3.41. Ronald S. Burt — Д3-Т4 [71]

> "Brokerage across structural holes is the source of value added, but closure can be critical to realizing the value buried in structural holes." [71]

- **Перевод:** «Посредничество через структурные дыры — источник добавленной ценности, но замкнутость может быть критична для реализации этой ценности» (перевод курса, [day-03/rationale-and-method.md, строка 931](../day-03/rationale-and-method.md#L931))
- **Интерпретация для репутационных технологий:** Посредничество через структурные дыры создаёт ценность, но реализовать её помогает замкнутость сети — доверие внутри группы. Курс строит на этом тезис «посредник ценнее громкого узла»: сигнал через доверенного посредника идёт по потоку, холодный контакт — против. [71]
- **Авторы:** Ronald S. Burt
- **Дата:** 2000 (препринт главы; книга 2001)
- **Источник:** Structural Holes versus Network Closure as Social Capital // Social Capital: Theory and Research / edited by Nan Lin, Karen S. Cook, Ronald S. Burt. New York: Aldine de Gruyter, 2001 (препринт 2000)
- **Ссылка:** https://snap.stanford.edu/class/cs224w-readings/burt00capital.pdf
- **Место в источнике:** страница 1
- **Статус проверки:** VERIFIED-FULLTEXT
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `Т4`
- **Где в репозитории:** [day-03/rationale-and-method.md, строка 931](../day-03/rationale-and-method.md#L931)

### 3.42. Meeyoung Cha и соавторы — Д3-Т5 [72]

> "popular users who have high indegree are not necessarily influential in terms of spawning retweets or mentions" [72]

- **Перевод:** «Популярные пользователи с большим числом подписчиков не обязательно влиятельны с точки зрения ретвитов и упоминаний» (перевод курса, [day-03/rationale-and-method.md, строка 932](../day-03/rationale-and-method.md#L932))
- **Интерпретация для репутационных технологий:** Эмпирика из Twitter: множество подписчиков не гарантирует ретвитов и упоминаний. Курс превращает это в правило «охват — не значимость» и в противоядие от типичной ошибки — выбора точки влияния по числу подписчиков или просмотров. Влияние здесь измерено именно ретвитами и упоминаниями, а не решениями. [72]
- **Авторы:** Meeyoung Cha; Hamed Haddadi; Fabrício Benevenuto; Krishna P. Gummadi
- **Дата:** 2010
- **Источник:** Measuring User Influence in Twitter: The Million Follower Fallacy // Proceedings of the Fourth International AAAI Conference on Weblogs and Social Media (Association for the Advancement of Artificial Intelligence). 2010
- **Ссылка:** https://snap.stanford.edu/class/cs224w-readings/cha10influence.pdf
- **Место в источнике:** Abstract, страница 1 PDF
- **Статус проверки:** VERIFIED-FULLTEXT
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `Т5-1`
- **Где в репозитории:** [day-03/rationale-and-method.md, строка 932](../day-03/rationale-and-method.md#L932)

### 3.43. Meeyoung Cha и соавторы — Д3-Т5 [72]

> "the most connected users are not necessarily the most influential" [72]

- **Перевод:** «самые связанные пользователи не обязательно самые влиятельные» (перевод курса, [day-03/rationale-and-method.md, строка 932](../day-03/rationale-and-method.md#L932))
- **Интерпретация для репутационных технологий:** Самые связанные пользователи не обязательно самые влиятельные — короткая формула для слайда «Больше подписчиков — не больше влияния». В курсе она напоминает, что активный узел может быть лишь ретранслятором, а общее правило «громкий узел почти никогда не точка» остаётся гипотезой на учебных кейсах. [72]
- **Авторы:** Meeyoung Cha; Hamed Haddadi; Fabrício Benevenuto; Krishna P. Gummadi
- **Дата:** 2010
- **Источник:** Measuring User Influence in Twitter: The Million Follower Fallacy // Proceedings of the Fourth International AAAI Conference on Weblogs and Social Media (Association for the Advancement of Artificial Intelligence). 2010
- **Ссылка:** https://snap.stanford.edu/class/cs224w-readings/cha10influence.pdf
- **Место в источнике:** страница 4 PDF
- **Статус проверки:** VERIFIED-FULLTEXT
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `Т5-2`
- **Где в репозитории:** [day-03/rationale-and-method.md, строка 932](../day-03/rationale-and-method.md#L932)

## День 4. Имидж-технологии: внешность, одежда, первое впечатление

### 4.1. Johannes Itten — О1 [73]

> «Las agrupaciones de colores que cada uno ha realizado responden a una impresión subjetiva : son colores subjetivos». [73]

- **Перевод:** «Цветовые сочетания, которые составил каждый, отвечают субъективному впечатлению: это субъективные цвета». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1774](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1774))
- **Интерпретация для репутационных технологий:** Иттен называет «субъективными» те сочетания, которые человек собирает сам по своему впечатлению. Для имиджмейкера это напоминание: личная палитра клиента отражает предпочтение, а не объективно «идущие» цвета, поэтому её используют как точку входа в разговор о цвете, а не как вердикт. [73]
- **Авторы:** Johannes Itten
- **Дата:** испанское сокращённое издание, год в скане не найден; немецкий оригинал 1961
- **Источник:** Arte del color: aproximación subjetiva y descripción objetiva del arte. Edición abreviada. París: Editorial Bouret (сокращённое испанское издание книги Kunst der Farbe, 1961)
- **Ссылка:** https://archive.org/details/LaHistoriaInterminable
- **Место в источнике:** страница 23
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1773](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1773)

### 4.2. Johannes Itten — О1 [73]

> «El tipo físico de cabello rubio claro, de ojos azules y piel rosácea prefiere, como regla general, colores muy puros». [73]

- **Перевод:** «Физический тип со светло-русыми волосами, голубыми глазами и розоватой кожей, как правило, предпочитает очень чистые цвета». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1776](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1776))
- **Интерпретация для репутационных технологий:** Здесь виден концептуальный исток сезонного цветотипирования: внешность связывается с предпочитаемыми «созвучиями». Важно оговорка «как правило» — это тенденция, а не закон; курс подаёт сезонные системы как практическую эвристику без сильного эмпирического подтверждения. [73]
- **Авторы:** Johannes Itten
- **Дата:** испанское сокращённое издание, год в скане не найден; немецкий оригинал 1961
- **Источник:** Arte del color: aproximación subjetiva y descripción objetiva del arte. Edición abreviada. París: Editorial Bouret (сокращённое испанское издание книги Kunst der Farbe, 1961)
- **Ссылка:** https://archive.org/details/LaHistoriaInterminable
- **Место в источнике:** страница 25
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1775](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1775)

### 4.3. Johannes Itten — О1 [73]

> «Naturalmente, para emitir un juicio no basta el color del cabello, de los ojos y de la piel.» [73]

- **Перевод:** «Разумеется, для суждения недостаточно цвета волос, глаз и кожи». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1778](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1778))
- **Интерпретация для репутационных технологий:** Сам Иттен ограничивает собственную схему: цвета волос, глаз и кожи недостаточно для суждения. Лектор может опереться на эту фразу против механического «определения цветотипа по трём признакам»: палитру всё равно проверяют глазом, контекстом и задачей образа. [73]
- **Авторы:** Johannes Itten
- **Дата:** испанское сокращённое издание, год в скане не найден; немецкий оригинал 1961
- **Источник:** Arte del color: aproximación subjetiva y descripción objetiva del arte. Edición abreviada. París: Editorial Bouret (сокращённое испанское издание книги Kunst der Farbe, 1961)
- **Ссылка:** https://archive.org/details/LaHistoriaInterminable
- **Место в источнике:** страница 25
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1777](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1777)

### 4.4. Johannes Itten — О1 [73]

> «He preguntado muchas veces el criterio objetivo sobre las cuatro concordancias de colores que caracterizan las cuatro estaciones del año y me ha parecido curioso que nadie se confunde en la atribución.» [73]

- **Перевод:** «Я много раз спрашивал об объективном критерии для четырёх цветовых созвучий, характеризующих четыре времени года, и мне показалось любопытным, что никто не ошибается в их отнесении». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1780](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1780))
- **Интерпретация для репутационных технологий:** Фраза показывает, откуда берётся убедительность «сезонной» метафоры: люди легко соглашаются, какое созвучие похоже на весну или осень. Но согласие в ассоциациях не доказывает валидность типологии внешности — каталог курса подчёркивает, что рецензируемых подтверждений сезонного цветотипирования не найдено. [73]
- **Авторы:** Johannes Itten
- **Дата:** испанское сокращённое издание, год в скане не найден; немецкий оригинал 1961
- **Источник:** Arte del color: aproximación subjetiva y descripción objetiva del arte. Edición abreviada. París: Editorial Bouret (сокращённое испанское издание книги Kunst der Farbe, 1961)
- **Ссылка:** https://archive.org/details/LaHistoriaInterminable
- **Место в источнике:** страница 26
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1779](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1779)

### 4.5. Johannes Itten — О1 [73]

> «Es preciso evitar de decir al principio del ejercicio que, según las concordancias subjetivas, se puede deducir el carácter, la manera de pensar y los sentimientos del autor.» [73]

- **Перевод:** «Следует избегать того, чтобы в начале упражнения говорить, будто по субъективным созвучиям можно вывести характер, образ мыслей и чувства автора». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1782](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1782))
- **Интерпретация для репутационных технологий:** Ключевое предостережение для курса: даже автор теории просит не выводить по цветовым созвучиям характер и образ мыслей. Отсюда правило Дня 4 — цвет не сообщает характер ни владельца, ни собеседника, и цветовые тесты нельзя превращать в диагностику личности. [73]
- **Авторы:** Johannes Itten
- **Дата:** испанское сокращённое издание, год в скане не найден; немецкий оригинал 1961
- **Источник:** Arte del color: aproximación subjetiva y descripción objetiva del arte. Edición abreviada. París: Editorial Bouret (сокращённое испанское издание книги Kunst der Farbe, 1961)
- **Ссылка:** https://archive.org/details/LaHistoriaInterminable
- **Место в источнике:** страница 24
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1781](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1781)

### 4.6. Поступаева Надежда Васильевна — О3 [74]

> «Существует два основных критерия определения цветотипа внешности: -контрастность кожи, глаз, волос. -температура кожи, глаз, волос.» [74]

- **Интерпретация для репутационных технологий:** Статья показывает, как практики сводят цветотип к двум осям — контрасту и температуре, что перекликается с контрастами Иттена «светлое–тёмное» и «холодное–тёплое». Для консультанта это удобный рабочий чек-лист, но курс использует его как пример практики, а не как доказательство. [74]
- **Авторы:** Поступаева Надежда Васильевна
- **Дата:** 2021
- **Источник:** Сложности определения цветотипа внешности // Инновационная наука. 2021. Номер 3. Страницы 157–160
- **Ссылка:** https://cyberleninka.ru/article/n/slozhnosti-opredeleniya-tsvetotipa-vneshnosti
- **Место в источнике:** страница 158
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1821](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1821)

### 4.7. Поступаева Надежда Васильевна — О3 [74]

> «По процентному соотношению , составленному мной с учетом практического опыта работы , он занимает около 75- 80 % всех типов внешности в России.» [74]

- **Интерпретация для репутационных технологий:** Процент взят автором из собственного практического опыта, а не из исследования. На лекции эту фразу полезно показывать как образец слабой доказательной базы цветотипирования: такие цифры нельзя переносить в материалы курса как статистику о внешности россиян. [74]
- **Авторы:** Поступаева Надежда Васильевна
- **Дата:** 2021
- **Источник:** Сложности определения цветотипа внешности // Инновационная наука. 2021. Номер 3. Страницы 157–160
- **Ссылка:** https://cyberleninka.ru/article/n/slozhnosti-opredeleniya-tsvetotipa-vneshnosti
- **Место в источнике:** страница 159
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1822](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1822)

### 4.8. Поступаева Надежда Васильевна — О3 [74]

> «Необходимо посмотреть на цвет вен на запястье: синие вены показатель холодного цветотипа , зеленые - теплого.» [74]

- **Интерпретация для репутационных технологий:** «Тест вен» — типичное бытовое правило из практики стилистов, которое исследованиями не подтверждено. Каталог предлагает использовать его как иллюстрацию того, как живут непроверенные приёмы, и учить слушателей отличать удобную примету от метода с опорой. [74]
- **Авторы:** Поступаева Надежда Васильевна
- **Дата:** 2021
- **Источник:** Сложности определения цветотипа внешности // Инновационная наука. 2021. Номер 3. Страницы 157–160
- **Ссылка:** https://cyberleninka.ru/article/n/slozhnosti-opredeleniya-tsvetotipa-vneshnosti
- **Место в источнике:** страница 160
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1823](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1823)

### 4.9. Heinrich Wölfflin — О4 [75]

> "In the former case the stress is laid on the limits of things; in the other the work tends to look limitless. Seeing by volumes and outlines isolates objects: for the painterly eye, they merge." [75]

- **Перевод:** «В первом случае акцент делается на границах вещей, во втором произведение кажется безграничным. Видение объёмами и контурами обособляет предметы; для живописного глаза они сливаются». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1845](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1845))
- **Интерпретация для репутационных технологий:** Вёльфлин противопоставляет видение через границы и видение, где предметы сливаются. Курс берёт эту пару как язык описания внешности: контур и черты против объёмов и фактуры. Перенос на человека — аналогия курса: у Вёльфлина речь об искусстве XVI и XVII веков. [75]
- **Авторы:** Heinrich Wölfflin; переводчик M. D. Hottinger
- **Дата:** английское издание [1950]; немецкий оригинал 1915
- **Источник:** Principles of Art History: The Problem of the Development of Style in Later Art / translated by M. D. Hottinger from the 7th German edition. New York: Dover Publications, [1950] (оригинал: Kunstgeschichtliche Grundbegriffe, 1915)
- **Ссылка:** https://archive.org/details/princarth00wlff
- **Место в источнике:** страница 14
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1844](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1844)

### 4.10. Heinrich Wölfflin — О4 [75]

> "linear style sees in lines, painterly in masses." [75]

- **Перевод:** «линейный стиль видит линиями, живописный — массами». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1847](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1847))
- **Интерпретация для репутационных технологий:** Краткая формула «линии против масс» удобна как словарь: одним словом назвать замысел — графичный силуэт или мягкую массу — стилисту, художнику или нейросети. Доказательной силы у неё нет, это уровень опоры «аналогия». [75]
- **Авторы:** Heinrich Wölfflin; переводчик M. D. Hottinger
- **Дата:** английское издание [1950]; немецкий оригинал 1915
- **Источник:** Principles of Art History: The Problem of the Development of Style in Later Art / translated by M. D. Hottinger from the 7th German edition. New York: Dover Publications, [1950] (оригинал: Kunstgeschichtliche Grundbegriffe, 1915)
- **Ссылка:** https://archive.org/details/princarth00wlff
- **Место в источнике:** страница 18
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1846](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1846)

### 4.11. Heinrich Wölfflin — О4 [75]

> "The painterly mode is the later, and cannot be conceived without the earlier, but it is not absolutely superior." [75]

- **Перевод:** «Живописный способ — более поздний и немыслим без предшествующего, но он не является безусловно высшим». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1849](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1849))
- **Интерпретация для репутационных технологий:** Цитата защищает от оценочности: живописное не «лучше» и не «хуже» линейного. Для имидж-практики это значит, что чёткий графичный образ и мягкий объёмный образ — не ступени иерархии, а два режима, выбор между которыми задаёт задача и аудитория. [75]
- **Авторы:** Heinrich Wölfflin; переводчик M. D. Hottinger
- **Дата:** английское издание [1950]; немецкий оригинал 1915
- **Источник:** Principles of Art History: The Problem of the Development of Style in Later Art / translated by M. D. Hottinger from the 7th German edition. New York: Dover Publications, [1950] (оригинал: Kunstgeschichtliche Grundbegriffe, 1915)
- **Ссылка:** https://archive.org/details/princarth00wlff
- **Место в источнике:** страница 18
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1848](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1848)

### 4.12. Heinrich Wölfflin — О4 [75]

> "Linear style is the style of distinctness plastically felt." [75]

- **Перевод:** «Линейный стиль — это стиль пластически ощущаемой отчётливости». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1851](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1851))
- **Интерпретация для репутационных технологий:** Эпиграф слайда «Форма через призму векторов» даёт имя чёткой, графичной форме, с которой работает гармоничный вектор. Сценарий лектора прямо оговаривает: Вёльфлин здесь словарь для описания замысла, он ничего не доказывает, а перенос его понятий на фигуру — аналогия курса. [75]
- **Авторы:** Heinrich Wölfflin; переводчик M. D. Hottinger
- **Дата:** английское издание [1950]; немецкий оригинал 1915
- **Источник:** Principles of Art History: The Problem of the Development of Style in Later Art / translated by M. D. Hottinger from the 7th German edition. New York: Dover Publications, [1950] (оригинал: Kunstgeschichtliche Grundbegriffe, 1915)
- **Ссылка:** https://archive.org/details/princarth00wlff
- **Место в источнике:** страница 21
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1850](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1850); эпиграф слайда 12: [day-04/presentation.md, строка 348](../day-04/presentation.md#L348), в колоде: «Линейный стиль — это стиль пластически ощущаемой отчётливости».

### 4.13. Шинкарёва Майя Изяславовна — О5 [76]

> «Ученый обозначил пять основных дихотомий: линейное – живописное, плоскостное – глубинное, замкнутая форма – открытая форма, тектоническое – атектоническое, безусловная ясность – неполная ясность». [76]

- **Интерпретация для репутационных технологий:** Источник нужен прежде всего ради русской терминологии пяти пар Вёльфлина для слайдов и раздаточных материалов. Это вторичная статья из музыковедения, поэтому толкование пар через неё применяют осторожно и сверяют с самим Вёльфлиным. [76]
- **Авторы:** Шинкарёва Майя Изяславовна
- **Дата:** 2008
- **Источник:** Понятие «живописное» Г. Вёльфлина применительно к искусству полифонии XVII века // Вестник Московского государственного университета культуры и искусств. 2008. Номер 6. Страницы 256–258
- **Ссылка:** https://cyberleninka.ru/article/n/ponyatie-zhivopisnoe-g-vyolflina-primenitelno-k-iskusstvu-polifonii-xvii-veka
- **Место в источнике:** страница 257
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1868](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1868)

### 4.14. Шинкарёва Майя Изяславовна — О5 [76]

> «„Живописное“ эквивалентно необычности, бесформенности, изменчивости.» [76]

- **Интерпретация для репутационных технологий:** Формулировка принадлежит автору статьи, а не Вёльфлину, и цитировать её от имени Вёльфлина нельзя. Кроме того, у самого Вёльфлина живописное не ниже линейного, поэтому связку «живописное — бесформенное» не стоит превращать в оценку мягкого образа. [76]
- **Авторы:** Шинкарёва Майя Изяславовна
- **Дата:** 2008
- **Источник:** Понятие «живописное» Г. Вёльфлина применительно к искусству полифонии XVII века // Вестник Московского государственного университета культуры и искусств. 2008. Номер 6. Страницы 256–258
- **Ссылка:** https://cyberleninka.ru/article/n/ponyatie-zhivopisnoe-g-vyolflina-primenitelno-k-iskusstvu-polifonii-xvii-veka
- **Место в источнике:** страница 256
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1869](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1869)
- **Примечание:** В оригинале слово «живописное» взято в «ёлочки»; это собственная формулировка автора статьи, а не Вёльфлина.

### 4.15. Серова О. — О6 [77]

> «В период 1926–1929 гг. Софья Николаевна работала в лаборатории зрительных восприятий маскировочного отдела Военно-инженерного научно-испытательного полигона РККА» [77]

- **Интерпретация для репутационных технологий:** Биографическая деталь важна для курса: подход «коррекция пропорций через зрительные иллюзии» вырос из лабораторной психологии восприятия и маскировки, а не из физиогномики. Это сведения из статьи Серовой; текст самой книги 1934 года в проекте не проверен. [77]
- **Авторы:** Серова О. (автор статьи; полное имя в цитируемом тексте не раскрыто) — о Беляевой-Экземплярской Софье Николаевне
- **Дата:** 2012
- **Источник:** Софья Николаевна Беляева-Экземплярская — выпускница Московских высших женских курсов // Развитие личности. 2012. Номер 2
- **Ссылка:** https://cyberleninka.ru/article/n/sofya-nikolaevna-belyaeva-ekzemplyarskaya-vypusknitsa-mvzhk
- **Место в источнике:** страница 42
- **Статус проверки:** VERIFIED-FULLTEXT (статья о книге; текст самой книги 1934 года не проверен)
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1888](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1888)

### 4.16. Серова О. — О6 [77]

> «Итогом напряженной работы этих лет стали монография «Моделирование одежды по законам зрительного восприятия» [11]» [77]

- **Интерпретация для репутационных технологий:** Фраза связывает монографию о моделировании одежды с лабораторной работой автора и объясняет, откуда в курсе тема зрительных иллюзий. Текст самой книги в проекте не проверен, поэтому её конкретные правила курс сверяет с современными данными о полосах и членениях. [77]
- **Авторы:** Серова О. (автор статьи; полное имя в цитируемом тексте не раскрыто) — о Беляевой-Экземплярской Софье Николаевне
- **Дата:** 2012
- **Источник:** Софья Николаевна Беляева-Экземплярская — выпускница Московских высших женских курсов // Развитие личности. 2012. Номер 2
- **Ссылка:** https://cyberleninka.ru/article/n/sofya-nikolaevna-belyaeva-ekzemplyarskaya-vypusknitsa-mvzhk
- **Место в источнике:** страница 42
- **Статус проверки:** VERIFIED-FULLTEXT (статья о книге; текст самой книги 1934 года не проверен)
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1889](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1889)

### 4.17. Серова О. — О6 [77]

> «Была переиздана только одна работа С. Н. Беляевой-Экземплярской – «Моделирование одежды по законам зрительного восприятия». Переиздание осуществлено московским издательством «Академия моды» в 1996 г.» [77]

- **Интерпретация для репутационных технологий:** Сноска фиксирует историю переизданий: книга вернулась в профессиональный оборот через издательство «Академия моды». Лектору это аргумент, что метод живёт в обучении модельеров, но не доказательство его правил — их проверяют экспериментами. [77]
- **Авторы:** Серова О. (автор статьи; полное имя в цитируемом тексте не раскрыто) — о Беляевой-Экземплярской Софье Николаевне
- **Дата:** 2012
- **Источник:** Софья Николаевна Беляева-Экземплярская — выпускница Московских высших женских курсов // Развитие личности. 2012. Номер 2
- **Ссылка:** https://cyberleninka.ru/article/n/sofya-nikolaevna-belyaeva-ekzemplyarskaya-vypusknitsa-mvzhk
- **Место в источнике:** страница 41, сноска
- **Статус проверки:** VERIFIED-FULLTEXT (статья о книге; текст самой книги 1934 года не проверен)
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1890](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1890)

### 4.18. Шипков Олег — О7 [78]

> «Общепринятый стереотип состоит в том, что вертикальные членения поверхности объекта зрительно увеличивают высоту, уменьшая ширину, и наоборот» [78]

- **Интерпретация для репутационных технологий:** Шипков сначала формулирует общепринятый стереотип «вертикаль удлиняет и сужает», чтобы затем его проверить. Для практика это пример бытового правила, которое курс не принимает на веру, а ставит под проверку. [78]
- **Авторы:** Шипков Олег (отчество: полное имя в открытых источниках не установлено)
- **Дата:** декабрь 2017
- **Источник:** Зрительный эффект членения поверхности // Геометрия и графика. 2017. Том 5, номер 4. Страницы 68–72
- **Ссылка:** https://zh-szf.ru/en/nauka/article/19053/jats
- **Место в источнике:** аннотация
- **Статус проверки:** VERIFIED-FULLTEXT (аннотация)
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1906](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1906)

### 4.19. Шипков Олег — О7 [78]

> «В работе показана ошибочность распространенного в искусстве, архитектуре и дизайне стереотипа. Членения поверхности зрительно увеличивают поперечный, а не продольный по отношению к членениям габарит объекта.» [78]

- **Интерпретация для репутационных технологий:** Аннотация прямо опровергает правило «вертикаль стройнит»: членения увеличивают поперечный к ним размер. Источник полезен как контрпример, но журнал отраслевой, а выборка и методика в аннотации не описаны, поэтому вывод подаётся как сигнал перепроверять приём на конкретной фигуре. [78]
- **Авторы:** Шипков Олег (отчество: полное имя в открытых источниках не установлено)
- **Дата:** декабрь 2017
- **Источник:** Зрительный эффект членения поверхности // Геометрия и графика. 2017. Том 5, номер 4. Страницы 68–72
- **Ссылка:** https://zh-szf.ru/en/nauka/article/19053/jats
- **Место в источнике:** аннотация
- **Статус проверки:** VERIFIED-FULLTEXT (аннотация)
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1907](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1907)

### 4.20. Antonis Koutsoumpis и соавторы — О8 [79]

> "Results showed that horizontal stripes and lower luminance have—independently—a small-to-moderate thinning effect on the perceived size of the body" [79]

- **Перевод:** «Результаты показали, что горизонтальные полосы и более низкая светлота — независимо друг от друга — дают слабый или умеренный „стройнящий“ эффект на воспринимаемый размер тела». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1922](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1922))
- **Интерпретация для репутационных технологий:** Эксперимент показывает: иллюзии формы реальны, но их сила лишь слабая или умеренная, а «стройнят» как раз горизонтальная полоса и тёмная одежда. Курс использует это только для зрительной коррекции пропорций, без каких-либо выводов о личности. [79]
- **Авторы:** Antonis Koutsoumpis; Elias Economou; Erik van der Burg
- **Дата:** август 2021
- **Источник:** Helmholtz Versus Haute Couture: How Horizontal Stripes and Dark Clothes Make You Look Thinner // Perception. 2021. Volume 50, Number 9
- **Ссылка:** https://doi.org/10.1177/03010066211038158
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1921](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1921)

### 4.21. Antonis Koutsoumpis и соавторы — О8 [79]

> "These findings do not agree with the common belief that clothes with horizontal stripes make someone appear wider" [79]

- **Перевод:** «Эти данные расходятся с распространённым убеждением, что одежда в горизонтальную полоску делает человека шире». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1924](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1924))
- **Интерпретация для репутационных технологий:** Данные расходятся с бытовой уверенностью, что горизонтальная полоса полнит. Урок для имиджмейкера: правило из учебника или журнала — гипотеза, которую проверяют на реальной фигуре и на носителе, где человека увидят. [79]
- **Авторы:** Antonis Koutsoumpis; Elias Economou; Erik van der Burg
- **Дата:** август 2021
- **Источник:** Helmholtz Versus Haute Couture: How Horizontal Stripes and Dark Clothes Make You Look Thinner // Perception. 2021. Volume 50, Number 9
- **Ссылка:** https://doi.org/10.1177/03010066211038158
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1923](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1923)

### 4.22. Tanya L. Chartrand и соавторы — О9 [80]

> "The chameleon effect refers to nonconscious mimicry of the postures, mannerisms, facial expressions, and other behaviors of one's interaction partners, such that one's behavior passively and unintentionally changes to match that of others in one's current social environment." [80]

- **Перевод:** «Эффект хамелеона — это неосознанное подражание позам, манерам, мимике и другому поведению партнёров по взаимодействию, при котором поведение человека пассивно и непреднамеренно меняется, совпадая с поведением окружающих». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1945](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1945))
- **Интерпретация для репутационных технологий:** Эффект хамелеона обосновывает стратегию подстройки под собеседника. Однако явление описано как неосознанное: намеренное копирование поз и манер на деловой встрече — экстраполяция, и замеченное подражание может сработать иначе. [80]
- **Авторы:** Tanya L. Chartrand; John A. Bargh
- **Дата:** 1999
- **Источник:** The Chameleon Effect: The Perception–Behavior Link and Social Interaction // Journal of Personality and Social Psychology. 1999. Volume 76, Number 6. Pages 893–910
- **Ссылка:** https://doi.org/10.1037/0022-3514.76.6.893
- **Место в источнике:** Abstract, страница 893
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1944](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1944)

### 4.23. Tanya L. Chartrand и соавторы — О9 [80]

> "Experiment 2 had confederates mimic the posture and movements of participants and showed that mimicry facilitates the smoothness of interactions and increases liking between interaction partners." [80]

- **Перевод:** «В эксперименте 2 подставные участники копировали позы и движения испытуемых, и это показало, что подражание делает взаимодействие более гладким и повышает взаимную симпатию». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1947](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1947))
- **Интерпретация для репутационных технологий:** Эксперимент связывает подражание с более гладким взаимодействием и ростом симпатии — опора для гармоничного вектора образа. Оговорка каталога остаётся в силе: эффект изучен как непреднамеренный, и сознательная «зеркальность» не гарантирует того же результата. [80]
- **Авторы:** Tanya L. Chartrand; John A. Bargh
- **Дата:** 1999
- **Источник:** The Chameleon Effect: The Perception–Behavior Link and Social Interaction // Journal of Personality and Social Psychology. 1999. Volume 76, Number 6. Pages 893–910
- **Ссылка:** https://doi.org/10.1037/0022-3514.76.6.893
- **Место в источнике:** Abstract, страница 893
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1946](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1946)

### 4.24. Jordan Soliz и соавторы — О10 [81]

> "Communication Accommodation Theory (CAT) has served as a cross-disciplinary framework for understanding the adjustments individuals make to create, maintain, or decrease social distance in interactions." [81]

- **Перевод:** «Теория коммуникативной аккомодации служит междисциплинарной рамкой для понимания того, как люди подстраиваются, чтобы создать, сохранить или сократить социальную дистанцию во взаимодействии». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1964](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1964))
- **Интерпретация для репутационных технологий:** Теория аккомодации даёт рамку: подстраиваясь или сохраняя дистанцию, человек управляет социальной дистанцией. Для имиджа это выбор между сближением с аудиторией и подчёркнутым отличием; но теория выросла из исследований речи и акцента, и перенос на одежду — аналогия. [81]
- **Авторы:** Jordan Soliz; Howard Giles
- **Дата:** 2014
- **Источник:** Relational and Identity Processes in Communication: A Contextual and Meta-Analytical Review of Communication Accommodation Theory // Annals of the International Communication Association (Communication Yearbook 38). 2014. Volume 38, Number 1. Pages 107–144
- **Ссылка:** https://doi.org/10.1080/23808985.2014.11679160
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED-ABSTRACT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1963](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1963)

### 4.25. Jordan Soliz и соавторы — О10 [81]

> "we summarize a meta-analysis of a subset of these articles (k = 76, N = 18,382)" [81]

- **Перевод:** «мы обобщаем метаанализ подмножества этих статей (k = 76, N = 18 382)». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1966](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1966))
- **Интерпретация для репутационных технологий:** Указание на метаанализ показывает, что у теории коммуникативной аккомодации есть количественная база, и лектор может ссылаться на неё как на проверенную рамку. При этом метаанализ касается коммуникации, а не одежды, а термины convergence/divergence в проверенной аннотации не встречаются. [81]
- **Авторы:** Jordan Soliz; Howard Giles
- **Дата:** 2014
- **Источник:** Relational and Identity Processes in Communication: A Contextual and Meta-Analytical Review of Communication Accommodation Theory // Annals of the International Communication Association (Communication Yearbook 38). 2014. Volume 38, Number 1. Pages 107–144
- **Ссылка:** https://doi.org/10.1080/23808985.2014.11679160
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED-ABSTRACT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1965](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1965)

### 4.26. Judee K. Burgoon — О11 [82]

> "Results generally support the model: violations by rewarding communicators produced more positive outcomes than violations by punishing communicators" [82]

- **Перевод:** «Результаты в целом подтверждают модель: нарушения со стороны „вознаграждающих“ коммуникаторов давали более позитивные исходы, чем нарушения со стороны „наказывающих“». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 1983](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1983))
- **Интерпретация для репутационных технологий:** Исходная модель Бургун — ключ к тезису курса: провокация срабатывает, если у нарушителя есть статус или ценность в глазах собеседника. Ограничение: исследование касалось личного пространства, а не одежды, поэтому перенос на образ — вывод курса. [82]
- **Авторы:** Judee K. Burgoon
- **Дата:** 1978
- **Источник:** A Communication Model of Personal Space Violations: Explication and an Initial Test // Human Communication Research. 1978. Volume 4, Number 2. Pages 129–142
- **Ссылка:** https://doi.org/10.1111/j.1468-2958.1978.tb00603.x
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED-SECONDARY (аннотация через OpenAlex)
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1982](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1982)

### 4.27. Judee K. Burgoon и соавторы — О12 [83]

> "Nonverbal expectancy violations theory holds that positive violations produce more favorable communication outcomes than conformity to expectations, while negative violations produce less favorable ones, and that reward characteristics of the communicator mediate the interpretation and evaluation of violations." [83]

- **Перевод:** «Теория невербальных нарушений ожиданий утверждает, что позитивные нарушения дают более благоприятные результаты коммуникации, чем соответствие ожиданиям, а негативные — менее благоприятные, и что „вознаграждающие“ характеристики коммуникатора опосредуют интерпретацию и оценку нарушений». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 2000](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2000))
- **Интерпретация для репутационных технологий:** Это главная формула дня: нарушение ожиданий — не нейтральный ход, его исход зависит от валентности и от «вознаграждающих» качеств нарушителя. Практик оценивает заранее, прочтут ли его отступление в образе как позитивное и есть ли у него для этого кредит. [83]
- **Авторы:** Judee K. Burgoon; Jerold L. Hale
- **Дата:** 1988
- **Источник:** Nonverbal Expectancy Violations: Model Elaboration and Application to Immediacy Behaviors // Communication Monographs. 1988. Volume 55, Number 1. Pages 58–79
- **Ссылка:** https://doi.org/10.1080/03637758809376158
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED-SECONDARY (аннотация через OpenAlex)
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 1999](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L1999)

### 4.28. Judee K. Burgoon и соавторы — О12 [83]

> "Nonimmedicacy violations produced lower credibility ratings than high immediacy or conformity to expectations for both friends and strangers." [83]

- **Перевод:** «Нарушения в сторону отстранённости снижали оценки доверия по сравнению с высокой вовлечённостью или соответствием ожиданиям — и у друзей, и у незнакомцев». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 2003](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2003))
- **Интерпретация для репутационных технологий:** Предупреждение для любой стратегии провокации: отступление в сторону холодности и отстранённости снижает доверие даже у друзей. Нонконформизм в образе не должен читаться как пренебрежение собеседником. [83]
- **Авторы:** Judee K. Burgoon; Jerold L. Hale
- **Дата:** 1988
- **Источник:** Nonverbal Expectancy Violations: Model Elaboration and Application to Immediacy Behaviors // Communication Monographs. 1988. Volume 55, Number 1. Pages 58–79
- **Ссылка:** https://doi.org/10.1080/03637758809376158
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED-SECONDARY (аннотация через OpenAlex)
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2001](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2001)

### 4.29. Judee K. Burgoon — О13 [84]

> "Human interactions are strongly governed by expectations which, if violated, are arousing and trigger an appraisal process that may be moderated by the rewardingness of the violator." [84]

- **Перевод:** «Человеческие взаимодействия во многом управляются ожиданиями; их нарушение возбуждает и запускает процесс оценки, который может смягчаться „вознаграждающей ценностью“ нарушителя». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 2017](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2017))
- **Интерпретация для репутационных технологий:** Энциклопедическая формулировка объясняет механизм: заметное отступление от ожидаемого возбуждает внимание и запускает оценку, а «вознаграждающая ценность» нарушителя может её смягчить. Для образа это значит, что одно и то же отступление по-разному прочтут у человека с разным весом в глазах аудитории. [84]
- **Авторы:** Judee K. Burgoon
- **Дата:** 18 июня 2015
- **Источник:** Expectancy Violations Theory // The International Encyclopedia of Interpersonal Communication. Hoboken, New Jersey: Wiley, 2015. Pages 1–9
- **Ссылка:** https://doi.org/10.1002/9781118540190.wbeic102
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED-ABSTRACT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2016](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2016)

### 4.30. Judee K. Burgoon — О13 [84]

> "Some contrary findings have led to revision of the theory." [84]

- **Перевод:** «Ряд противоречащих данных привёл к пересмотру теории». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 2019](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2019))
- **Интерпретация для репутационных технологий:** На слайде сборки «встреча с лечащим врачом» эпиграф напоминает: теория нарушения ожиданий пересматривалась и не даёт гарантированного рецепта провокации. Там, где ошибка прочтения дорога, курс выбирает строгую гармонию с профессиональной нормой. [84]
- **Авторы:** Judee K. Burgoon
- **Дата:** 18 июня 2015
- **Источник:** Expectancy Violations Theory // The International Encyclopedia of Interpersonal Communication. Hoboken, New Jersey: Wiley, 2015. Pages 1–9
- **Ссылка:** https://doi.org/10.1002/9781118540190.wbeic102
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED-ABSTRACT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2018](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2018); эпиграф слайда 27: [day-04/presentation.md, строка 641](../day-04/presentation.md#L641), в колоде: «Ряд противоречащих данных привёл к пересмотру теории».

### 4.31. Edwin P. Hollander — О14 [85]

> "Beginning with the consideration that social behavior depends upon attributes of the individual, conditions of the situation, and inputs to a dynamic system arising from their interaction, a theoretical conception relating conformity and status is presented." [85]

- **Перевод:** «Исходя из того, что социальное поведение зависит от свойств индивида, условий ситуации и вкладов в динамическую систему, возникающих из их взаимодействия, предлагается теоретическая концепция, связывающая конформность и статус». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 2040](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2040))
- **Интерпретация для репутационных технологий:** Холландер даёт рамку «право на провокацию зарабатывается соответствием и компетентностью»: поведение зависит от человека, ситуации и их взаимодействия. Ключевая формулировка о «кредите идиосинкразии» в проекте не проверена, поэтому тезис излагают своими словами со ссылкой, без кавычек. [85]
- **Авторы:** Edwin P. Hollander
- **Дата:** 1958
- **Источник:** Conformity, Status, and Idiosyncrasy Credit // Psychological Review. 1958. Volume 65, Number 2. Pages 117–127
- **Ссылка:** https://doi.org/10.1037/h0042501
- **Место в источнике:** Abstract (в OpenAlex он усечён)
- **Статус проверки:** VERIFIED-SECONDARY (аннотация через OpenAlex)
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2039](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2039)

### 4.32. Marilynn B. Brewer — О15 [86]

> "A model of optimal distinctiveness is proposed in which social identity is viewed as a reconciliation of opposing needs for assimilation and differentiation from others." [86]

- **Перевод:** «Предлагается модель оптимальной отличительности, в которой социальная идентичность рассматривается как примирение противоположных потребностей — в уподоблении другим и в отличии от них». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 2059](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2059))
- **Интерпретация для репутационных технологий:** На слайде о цвете через призму векторов Брюэр объясняет, почему нужны оба режима: аудитории важны и принадлежность, и отличие, а вектор — гипотеза о том, какая потребность сейчас сильнее. Модель описывает групповую идентичность, а не впечатление о конкретном руководителе. [86]
- **Авторы:** Marilynn B. Brewer
- **Дата:** 1991
- **Источник:** The Social Self: On Being the Same and Different at the Same Time // Personality and Social Psychology Bulletin. 1991. Volume 17, Number 5. Pages 475–482
- **Ссылка:** https://doi.org/10.1177/0146167291175001
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED-ABSTRACT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2058](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2058); эпиграф слайда 7: [day-04/presentation.md, строка 252](../day-04/presentation.md#L252), в колоде: «…примирение противоположных потребностей в уподоблении другим и отличии от них».

### 4.33. Marilynn B. Brewer — О15 [86]

> "Social identity and group loyalty are hypothesized to be strongest for those self-categorizations that simultaneously provide for a sense of belonging and a sense of distinctiveness." [86]

- **Перевод:** «Предполагается, что социальная идентичность и групповая лояльность сильнее всего для тех самокатегоризаций, которые одновременно дают чувство принадлежности и чувство отличительности». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 2061](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2061))
- **Интерпретация для репутационных технологий:** Эпиграф легенды карты обосновывает стратегию «свой, но заметный» между полной подстройкой и провокацией: образ сильнее, когда даёт и принадлежность, и отличительность. Выбор режима остаётся гипотезой о реакции аудитории, а не правилом. [86]
- **Авторы:** Marilynn B. Brewer
- **Дата:** 1991
- **Источник:** The Social Self: On Being the Same and Different at the Same Time // Personality and Social Psychology Bulletin. 1991. Volume 17, Number 5. Pages 475–482
- **Ссылка:** https://doi.org/10.1177/0146167291175001
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED-ABSTRACT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2060](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2060); эпиграф слайда 3: [day-04/presentation.md, строка 173](../day-04/presentation.md#L173), в колоде: «…одновременно дают чувство принадлежности и чувство отличительности».

### 4.34. Janine Willis и соавторы — О16 [87]

> "Judgments made after a 100-ms exposure correlated highly with judgments made in the absence of time constraints, suggesting that this exposure time was sufficient for participants to form an impression." [87]

- **Перевод:** «Суждения после 100-мс предъявления сильно коррелировали с суждениями без ограничения времени, что говорит о достаточности этого времени для формирования впечатления». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 2082](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2082))
- **Интерпретация для репутационных технологий:** На слайде о типологии Кибби эпиграф задаёт рамку: суждение о лице складывается почти мгновенно, и Кибби предлагает одеваться так, чтобы оно совпадало с одеждой. Ограничения: исследование касается лиц, а не одежды, быстрота не означает точности, а сама типология Кибби эмпирически не проверена. [87]
- **Авторы:** Janine Willis; Alexander Todorov
- **Дата:** 2006
- **Источник:** First Impressions: Making Up Your Mind After a 100-Ms Exposure to a Face // Psychological Science. 2006. Volume 17, Number 7. Pages 592–598
- **Ссылка:** https://doi.org/10.1111/j.1467-9280.2006.01750.x
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED-ABSTRACT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2081](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2081); эпиграф слайда 17: [day-04/presentation.md, строка 447](../day-04/presentation.md#L447), в колоде: «Суждения после показа в 100 мс высоко коррелировали с суждениями без ограничения времени».

### 4.35. Janine Willis и соавторы — О16 [87]

> "this result suggests that additional time may simply boost confidence in judgments." [87]

- **Перевод:** «этот результат говорит о том, что дополнительное время, возможно, просто повышает уверенность в суждениях». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 2084](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2084))
- **Интерпретация для репутационных технологий:** В сценарии с партнёром венчурного фонда цитата напоминает: долгий разговор скорее укрепляет уверенность в первом суждении, чем меняет его, поэтому первое впечатление нельзя отменить, им можно только управлять. Речь о согласованности впечатлений, а не об их правоте. [87]
- **Авторы:** Janine Willis; Alexander Todorov
- **Дата:** 2006
- **Источник:** First Impressions: Making Up Your Mind After a 100-Ms Exposure to a Face // Psychological Science. 2006. Volume 17, Number 7. Pages 592–598
- **Ссылка:** https://doi.org/10.1111/j.1467-9280.2006.01750.x
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED-ABSTRACT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2083](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2083); эпиграф слайда 26: [day-04/presentation.md, строка 621](../day-04/presentation.md#L621), в колоде: «…дополнительное время может лишь повышать уверенность в суждениях».

### 4.36. Neil Howlett и соавторы — О17 [88]

> "Clothing communicates information about the wearer and first impressions can be heavily influenced by the messages conveyed by attire." [88]

- **Перевод:** «Одежда сообщает информацию о своём владельце, и на первое впечатление могут сильно влиять сообщения, которые передаёт костюм». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 2100](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2100))
- **Интерпретация для репутационных технологий:** Исследование даёт прямое эмпирическое подтверждение, что одежда передаёт сведения о владельце и влияет на первое впечатление. Ограничения каталога: британская выборка, модель без лица и только мужские костюмы. [88]
- **Авторы:** Neil Howlett; Karen Pine; Ismail Orakçıoğlu; Ben Fletcher
- **Дата:** 2013
- **Источник:** The Influence of Clothing on First Impressions: Rapid and Positive Responses to Minor Changes in Male Attire // Journal of Fashion Marketing and Management. 2013. Volume 17, Number 1. Pages 38–48
- **Ссылка:** https://doi.org/10.1108/13612021311305128
- **Место в источнике:** структурированная аннотация (Purpose / Findings)
- **Статус проверки:** VERIFIED-ABSTRACT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2099](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2099)

### 4.37. Neil Howlett и соавторы — О17 [88]

> "The man was rated more positively on all attributes apart from trustworthiness when pictured in the bespoke suit." [88]

- **Перевод:** «Мужчину в костюме, сшитом на заказ, оценивали выше по всем характеристикам, кроме надёжности». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 2102](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2102))
- **Интерпретация для репутационных технологий:** На слайде сборки с закупщиком эпиграф предупреждает: костюм на заказ поднимает оценки, но не доверие. Поэтому цель «надёжный производитель» строится на предсказуемости и поведении в переговорах, а деталь гардероба лишь открывает дверь. [88]
- **Авторы:** Neil Howlett; Karen Pine; Ismail Orakçıoğlu; Ben Fletcher
- **Дата:** 2013
- **Источник:** The Influence of Clothing on First Impressions: Rapid and Positive Responses to Minor Changes in Male Attire // Journal of Fashion Marketing and Management. 2013. Volume 17, Number 1. Pages 38–48
- **Ссылка:** https://doi.org/10.1108/13612021311305128
- **Место в источнике:** структурированная аннотация (Purpose / Findings)
- **Статус проверки:** VERIFIED-ABSTRACT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2101](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2101); эпиграф слайда 25: [day-04/presentation.md, строка 601](../day-04/presentation.md#L601), в колоде: «Мужчину оценили выше по всем качествам, кроме надёжности, когда он был в костюме на заказ».

### 4.38. Hajo Adam и соавторы — О18a [89]

> "We introduce the term “enclothed cognition” to describe the systematic influence that clothes have on the wearer's psychological processes." [89]

- **Перевод:** «Мы вводим термин „облачённое познание“ для систематического влияния одежды на психологические процессы того, кто её носит». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 2121](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2121))
- **Интерпретация для репутационных технологий:** Понятие «облачённого познания» объясняет обратную связь «одежда — самоощущение руководителя»: образ влияет не только на зрителя, но и на того, кто его носит. Каталог предписывает подавать это как вероятный, но умеренный и спорный эффект. [89]
- **Авторы:** Hajo Adam; Adam D. Galinsky
- **Дата:** 2012
- **Источник:** Enclothed Cognition // Journal of Experimental Social Psychology. 2012. Volume 48, Number 4. Pages 918–925
- **Ссылка:** https://doi.org/10.1016/j.jesp.2012.02.008
- **Место в источнике:** Abstract (работа 2012 года)
- **Статус проверки:** VERIFIED-ABSTRACT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2120](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2120)

### 4.39. Hajo Adam и соавторы — О18a [89]

> "it depends on both the symbolic meaning and the physical experience of wearing the clothes." [89]

- **Перевод:** «оно зависит и от символического значения, и от физического опыта ношения одежды». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 2123](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2123))
- **Интерпретация для репутационных технологий:** Оговорка авторов важна для практики: эффект связывают и с символическим значением вещи, и с физическим опытом её ношения, а не с самим фактом покупки. Сам эффект при этом остаётся спорным из-за проблем с воспроизводимостью. [89]
- **Авторы:** Hajo Adam; Adam D. Galinsky
- **Дата:** 2012
- **Источник:** Enclothed Cognition // Journal of Experimental Social Psychology. 2012. Volume 48, Number 4. Pages 918–925
- **Ссылка:** https://doi.org/10.1016/j.jesp.2012.02.008
- **Место в источнике:** Abstract (работа 2012 года)
- **Статус проверки:** VERIFIED-ABSTRACT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2122](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2122)

### 4.40. C. Blaine Horton и соавторы — О18b [90]

> "However, a recent high-powered replication failed to replicate one of the original effects." [90]

- **Перевод:** «Однако недавняя репликация с высокой статистической мощностью не воспроизвела один из исходных эффектов». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 2125](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2125))
- **Интерпретация для репутационных технологий:** Признание, что крупная репликация не воспроизвела один из исходных эффектов, — хороший учебный пример для курса: громкая концепция об одежде может не выдержать проверки. Исходный результат 2012 года нельзя подавать как установленный факт. [90]
- **Авторы:** C. Blaine Horton; Hajo Adam; Adam D. Galinsky
- **Дата:** онлайн 17 июля 2023
- **Источник:** Evaluating the Evidence for Enclothed Cognition: Z-Curve and Meta-Analyses // Personality and Social Psychology Bulletin. Volume 51, Number 2. Pages 203–221
- **Ссылка:** https://doi.org/10.1177/01461672231182478
- **Место в источнике:** Abstract (работа 2023 года)
- **Статус проверки:** VERIFIED-ABSTRACT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2124](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2124)

### 4.41. C. Blaine Horton и соавторы — О18b [90]

> "our results raise concerns about the replicability of early enclothed cognition studies but affirm the evidential value for effects published after 2015." [90]

- **Перевод:** «наши результаты ставят под вопрос воспроизводимость ранних исследований облачённого познания, но подтверждают доказательную ценность эффектов, опубликованных после 2015 года». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 2127](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2127))
- **Интерпретация для репутационных технологий:** На слайде «Технология — метод с опорой» эпиграф показывает, что значит уровень опоры: ранние работы под сомнением, поздние подтверждены. Учтите, что метаанализ написан самими авторами концепции, поэтому эффект подают как спорный и умеренный. [90]
- **Авторы:** C. Blaine Horton; Hajo Adam; Adam D. Galinsky
- **Дата:** онлайн 17 июля 2023
- **Источник:** Evaluating the Evidence for Enclothed Cognition: Z-Curve and Meta-Analyses // Personality and Social Psychology Bulletin. Volume 51, Number 2. Pages 203–221
- **Ссылка:** https://doi.org/10.1177/01461672231182478
- **Место в источнике:** Abstract (работа 2023 года)
- **Статус проверки:** VERIFIED-ABSTRACT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2126](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2126); эпиграф слайда 2: [day-04/presentation.md, строка 153](../day-04/presentation.md#L153), в колоде: «…наши результаты ставят под сомнение воспроизводимость ранних исследований „одетого познания“, но подтверждают доказательность эффектов, опубликованных после 2015 года».

### 4.42. Albert Mehrabian — О19 [91]

> "Total Liking = 7% Verbal Liking + 38% Vocal Liking + 55% Facial Liking" [91]

- **Перевод:** «Общая симпатия = 7% вербальной + 38% голосовой + 55% лицевой симпатии». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 2145](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2145))
- **Интерпретация для репутационных технологий:** Формулу 7-38-55 курс приводит только как источник-предостережение. Она описывает общую симпатию при рассогласовании словесного, голосового и лицевого каналов, поэтому лозунг «внешность — это 55% впечатления» ею не подтверждается и в материалах курса не используется. [91]
- **Авторы:** Albert Mehrabian
- **Дата:** страница автора, © 1995–2016; книга Silent Messages — 1971, 2-е издание 1981
- **Источник:** Silent Messages — страница автора с описанием книги на сайте kaaj.com
- **Ссылка:** https://www.kaaj.com/psych/smorder.html
- **Место в источнике:** раздел "Inconsistent communications"
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2144](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2144)

### 4.43. Albert Mehrabian — О19 [91]

> "Unless a communicator is talking about their feelings or attitudes, these equations are not applicable." [91]

- **Перевод:** «Если коммуникатор не говорит о своих чувствах или отношениях, эти уравнения неприменимы». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 2147](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2147))
- **Интерпретация для репутационных технологий:** Сам Меграбян ограничивает свои уравнения сообщениями о чувствах и отношениях. Для лектора это готовый аргумент против популярного мифа: к деловому образу в целом правило 7-38-55 неприменимо. [91]
- **Авторы:** Albert Mehrabian
- **Дата:** страница автора, © 1995–2016; книга Silent Messages — 1971, 2-е издание 1981
- **Источник:** Silent Messages — страница автора с описанием книги на сайте kaaj.com
- **Ссылка:** https://www.kaaj.com/psych/smorder.html
- **Место в источнике:** раздел "Inconsistent communications"
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2146](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2146)

### 4.44. Erving Goffman — О20 [92]

> "It will be convenient to label as “front” that part of the individual’s performance which regularly functions in a general and fixed fashion to define the situation for those who observe the performance." [92]

- **Перевод:** «Удобно называть „фасадом“ ту часть представления индивида, которая регулярно и неизменным образом служит определению ситуации для тех, кто за представлением наблюдает». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 2167](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2167))
- **Интерпретация для репутационных технологий:** Понятие «фасада» — центральная рамка Дня 4: образ как устойчивая часть представления, которая определяет ситуацию для наблюдателей. Гофман при этом описывает социологию взаимодействия, а не технологию имиджа; его подход описательный, а не предписывающий. [92]
- **Авторы:** Erving Goffman
- **Дата:** 1959
- **Источник:** The Presentation of Self in Everyday Life. Garden City, New York: Doubleday Anchor Books, 1959
- **Ссылка:** https://archive.org/details/the-presentation-of-self-in-everyday-life-the-presentation-erving-goffman-1959-a
- **Место в источнике:** страница 22
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2166](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2166)

### 4.45. Erving Goffman — О20 [92]

> "It is sometimes convenient to divide the stimuli which make up personal front into “appearance” and “manner,” according to the function performed by the information that these stimuli convey." [92]

- **Перевод:** «Иногда удобно делить стимулы, составляющие личный фасад, на „внешность“ и „манеру“ — по функции информации, которую эти стимулы передают». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 2169](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2169))
- **Интерпретация для репутационных технологий:** Деление личного фасада на внешность и манеру даёт практику два слоя для аудита образа: что видно и как человек себя ведёт. Это описательная схема Гофмана, которую курс использует как каркас, а не как рецепт. [92]
- **Авторы:** Erving Goffman
- **Дата:** 1959
- **Источник:** The Presentation of Self in Everyday Life. Garden City, New York: Doubleday Anchor Books, 1959
- **Ссылка:** https://archive.org/details/the-presentation-of-self-in-everyday-life-the-presentation-erving-goffman-1959-a
- **Место в источнике:** страница 24
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2168](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2168)

### 4.46. Erving Goffman — О20 [92]

> "We often expect, of course, a confirming consistency between appearance and manner" [92]

- **Перевод:** «Мы, конечно, часто ожидаем подтверждающей согласованности между внешностью и манерой». (перевод из каталога #650, [2026-09-30-course-sources-and-presentations-650.md, строка 2171](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2171))
- **Интерпретация для репутационных технологий:** Эпиграф вводного слайда объясняет, почему образ шире цвета, формы, стиля и аксессуаров: речь, походка и мимика либо подтверждают внешность, либо спорят с ней, а аудитория ждёт их согласия. Гофман описывает это ожидание, а не предписывает поведение. [92]
- **Авторы:** Erving Goffman
- **Дата:** 1959
- **Источник:** The Presentation of Self in Everyday Life. Garden City, New York: Doubleday Anchor Books, 1959
- **Ссылка:** https://archive.org/details/the-presentation-of-self-in-everyday-life-the-presentation-erving-goffman-1959-a
- **Место в источнике:** страница 24
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2170](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2170); эпиграф слайда 1: [day-04/presentation.md, строка 133](../day-04/presentation.md#L133), в колоде: «Мы, конечно, часто ожидаем подтверждающей согласованности между внешностью и манерой».

### 4.47. Ирвинг Гофман — О21 [93]

> «В качестве элементов личного переднего плана можно назвать: отличительные знаки официального положения или ранга, умение одеваться, пол, возраст и расовые характеристики, габариты и внешность, осанку, характерные речевые обороты; выражения лица; жесты и т. п.» [93]

- **Интерпретация для репутационных технологий:** Русский перечень элементов «личного переднего плана» служит готовым чек-листом образа — от знаков ранга и осанки до речевых оборотов, мимики и жестов. Цитируя, нужно оговорить, что «умение одеваться» — вольная передача английского clothing. [93]
- **Авторы:** Ирвинг Гофман (Erving Goffman); переводчик Ковалев Александр Дмитриевич; научный редактор Ковалёва М. С. (полное имя в открытых источниках не установлено)
- **Дата:** 2000 (русское издание)
- **Источник:** Представление себя другим в повседневной жизни / перевод с английского и вступительная статья Александра Дмитриевича Ковалёва; научный редактор М. С. Ковалёва. Москва: КАНОН-пресс-Ц; Кучково поле, 2000
- **Ссылка:** https://archive.org/details/2000_20250325
- **Место в источнике:** страница 56
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2185](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2185)

### 4.48. Ирвинг Гофман — О21 [93]

> «Иногда удобно делить знаковые сигналы, составляющие личный передний план, на внешний вид и манеры согласно функции, исполняемой информацией, которую они передают.» [93]

- **Интерпретация для репутационных технологий:** Фраза даёт каноническую русскую терминологию: «личный передний план», «внешний вид» и «манеры». Её удобно брать в русскоязычные материалы курса вместо самодельных переводов английского front, а само деление служит основой для аудита образа в два слоя. [93]
- **Авторы:** Ирвинг Гофман (Erving Goffman); переводчик Ковалев Александр Дмитриевич; научный редактор Ковалёва М. С. (полное имя в открытых источниках не установлено)
- **Дата:** 2000 (русское издание)
- **Источник:** Представление себя другим в повседневной жизни / перевод с английского и вступительная статья Александра Дмитриевича Ковалёва; научный редактор М. С. Ковалёва. Москва: КАНОН-пресс-Ц; Кучково поле, 2000
- **Ссылка:** https://archive.org/details/2000_20250325
- **Место в источнике:** страница 56
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2186](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2186)

### 4.49. Ирвинг Гофман — О21 [93]

> «Конечно, чаще всего мы ждем подтверждающей правильность восприятия сигналов согласованности между внешностью и манерами.» [93]

- **Интерпретация для репутационных технологий:** Русская версия тезиса о согласованности внешности и манер. Для имидж-практики вывод прямой: если стиль одежды и поведение расходятся, зритель читает это как сбой, поэтому манеру и речь проектируют вместе с внешностью. [93]
- **Авторы:** Ирвинг Гофман (Erving Goffman); переводчик Ковалев Александр Дмитриевич; научный редактор Ковалёва М. С. (полное имя в открытых источниках не установлено)
- **Дата:** 2000 (русское издание)
- **Источник:** Представление себя другим в повседневной жизни / перевод с английского и вступительная статья Александра Дмитриевича Ковалёва; научный редактор М. С. Ковалёва. Москва: КАНОН-пресс-Ц; Кучково поле, 2000
- **Ссылка:** https://archive.org/details/2000_20250325
- **Место в источнике:** страница 57
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2187](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2187)

### 4.50. Шкурко Ольга Васильевна — О22 [94]

> «Субъектную окраску придают трактовке имиджа Г.Г. Почепцов, понимающий имидж как «обращенное во вне «Я» человека, его публичное «Я» [9]» [94]

- **Интерпретация для репутационных технологий:** Определение Почепцова — имидж как публичное «Я» — подчёркивает, что образ обращён к другим. Курс имеет доступ к нему только через статью Шкурко, без страниц первоисточника, поэтому цитировать его следует с пометкой «цитируется по: Шкурко, 2012». [94]
- **Авторы:** Шкурко Ольга Васильевна
- **Дата:** 2012
- **Источник:** Востребованность имиджелогического знания у будущих менеджеров // Сибирский торгово-экономический журнал. 2012. Номер 15
- **Ссылка:** https://cyberleninka.ru/article/n/vostrebovannost-imidzhelogicheskogo-znaniya-u-buduschih-menedzherov
- **Место в источнике:** страницы журнала в PDF не напечатаны; страница 1 PDF (из 4)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2207](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2207)

### 4.51. Шкурко Ольга Васильевна — О22 [94]

> «В.М. Шепель, не сводя имидж к внешности, выводит это понятие из визуального образа, напоминая о том, что «имидж в переводе с английского – образ. Это визуальная привлекательность личности». Однако ученый категорически не согласен с тем, что главным компонентом формирования имиджа является внешний атрибут личности [14].» [94]

- **Интерпретация для репутационных технологий:** Каталог ценит эту цитату как предостережение: Шепель выводит имидж из визуального образа, но не считает внешность главным компонентом. Это поддерживает тезис Дня 4, что образ шире внешности; цитировать только через статью Шкурко. [94]
- **Авторы:** Шкурко Ольга Васильевна
- **Дата:** 2012
- **Источник:** Востребованность имиджелогического знания у будущих менеджеров // Сибирский торгово-экономический журнал. 2012. Номер 15
- **Ссылка:** https://cyberleninka.ru/article/n/vostrebovannost-imidzhelogicheskogo-znaniya-u-buduschih-menedzherov
- **Место в источнике:** страницы журнала в PDF не напечатаны; страница 1 PDF (из 4)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2209](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2209)

### 4.52. Шкурко Ольга Васильевна — О22 [94]

> «В России, по словам А.Ю. Панасюка, исследователи находятся «пока лишь у истоков этой науки, науки имиджелогии» [6].» [94]

- **Интерпретация для репутационных технологий:** Слова Панасюка о том, что имиджелогия в России только у истоков, помогают лектору честно обозначить молодость дисциплины. Формулировка известна из вторых рук, через статью Шкурко в журнале среднего уровня, без страниц первоисточника. [94]
- **Авторы:** Шкурко Ольга Васильевна
- **Дата:** 2012
- **Источник:** Востребованность имиджелогического знания у будущих менеджеров // Сибирский торгово-экономический журнал. 2012. Номер 15
- **Ссылка:** https://cyberleninka.ru/article/n/vostrebovannost-imidzhelogicheskogo-znaniya-u-buduschih-menedzherov
- **Место в источнике:** страницы журнала в PDF не напечатаны; страница 2 PDF (из 4)
- **Статус проверки:** VERIFIED-FULLTEXT
- **Где в репозитории:** [2026-09-30-course-sources-and-presentations-650.md, строка 2211](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md#L2211)

### 4.53. Johannes Itten — E-itten [95]

> "Every woman should know what colors are becoming to her; these will always be her subjective colors and their complements." [95]

- **Перевод:** «Каждая женщина должна знать, какие цвета ей к лицу: это всегда её субъективные цвета и их дополнительные». (перевод курса, [day-04/presentation.md, строка 195](../day-04/presentation.md#L195))
- **Интерпретация для репутационных технологий:** Эпиграф слайда об Иттене связывает цвет с личностью носителя: свои субъективные цвета плюс дополнительные к ним. Курс читает это осторожно — Иттен строит сочетания, но не назначает человеку палитру, а из главы о субъективных тембрах позже выросли сезонные цветотипы, хотя он писал о предпочтениях. [95]
- **Авторы:** Johannes Itten
- **Дата:** английское издание 1973 (немецкий оригинал 1961)
- **Источник:** The Art of Color: The Subjective Experience and Objective Rationale of Color. Revised edition. New York: Van Nostrand Reinhold, 1973. Глава «Subjective Timbre», страницы 24–32
- **Ссылка:** https://archive.org/details/artofcolorsubjec00itte
- **Место в источнике:** страница 32, глава «Subjective Timbre» (открытый скан издания 1973 года)
- **Статус проверки:** VERIFIED (колода v5, решение 7)
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `E4`
- **Где в репозитории:** эпиграф слайда 4, [day-04/presentation.md, строка 195](../day-04/presentation.md#L195)

### 4.54. «Кодекс стиля» (Бератор-паблишинг) — E-kodeks [96]

> «Правильно подобранный цвет должен быть фоном для вашей внешности, а не наоборот». [96]

- **Интерпретация для репутационных технологий:** Эпиграф слайда о колоритах Ватерман и Цингель задаёт принцип: цвет служит фоном лицу, а не перетягивает внимание. Колорит определяют по коже, волосам, бровям и глазам, а не по любимым цветам; опора — справочник «Кодекс стиля», и сочетание проверяют глазом и опытом. [96]
- **Авторы:** Авторы справочника в материалах курса намеренно не называются (RFC v5, строка 36); издатель — «Бератор-паблишинг»
- **Дата:** 2007
- **Источник:** Кодекс стиля. Справочник делового дресс-кода. Москва: Бератор-паблишинг, 2007. 88 страниц (технологии НИА «Гид по стилю»)
- **Ссылка:** https://github.com/user-attachments/files/33784962/kodeks_stilya.pdf
- **Место в источнике:** страница 23 PDF-файла (в колоде: страницы 22–23)
- **Статус проверки:** VERIFIED (колода v5, решение 7: сверено по PDF)
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `E5`
- **Где в репозитории:** эпиграф слайда 5, [day-04/presentation.md, строка 214](../day-04/presentation.md#L214)

### 4.55. «Кодекс стиля» (Бератор-паблишинг) — E-kodeks [96]

> «Тип фигуры, конечно, не объясняет множества индивидуальных особенностей тела, но прекрасно ориентирует в выборе основных элементов кроя, а также в подборе идеальных материалов». [96]

- **Интерпретация для репутационных технологий:** Справочник сам оговаривает границу метода: тип фигуры не объясняет всех особенностей тела, но ориентирует в крое и материалах. Сценарий лектора называет это рабочей схемой для стилиста, а не диагнозом для клиента. [96]
- **Авторы:** Авторы справочника в материалах курса намеренно не называются (RFC v5, строка 36); издатель — «Бератор-паблишинг»
- **Дата:** 2007
- **Источник:** Кодекс стиля. Справочник делового дресс-кода. Москва: Бератор-паблишинг, 2007. 88 страниц (технологии НИА «Гид по стилю»)
- **Ссылка:** https://github.com/user-attachments/files/33784962/kodeks_stilya.pdf
- **Место в источнике:** страница 33 PDF-файла (в колоде: страницы 33–46)
- **Статус проверки:** VERIFIED (колода v5, решение 7: сверено по PDF)
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `E10`
- **Где в репозитории:** эпиграф слайда 10, [day-04/presentation.md, строка 310](../day-04/presentation.md#L310)

### 4.56. «Кодекс стиля» (Бератор-паблишинг) — E-kodeks [96]

> «Как правило, деловая мода базируется на классическом стиле». [96]

- **Интерпретация для репутационных технологий:** Справочник задаёт норму делового кода: классика как база, а собственный стиль входит элементами. Для практика это точка отсчёта — норму сначала знают и соблюдают, и лишь затем осознанно от неё отступают. [96]
- **Авторы:** Авторы справочника в материалах курса намеренно не называются (RFC v5, строка 36); издатель — «Бератор-паблишинг»
- **Дата:** 2007
- **Источник:** Кодекс стиля. Справочник делового дресс-кода. Москва: Бератор-паблишинг, 2007. 88 страниц (технологии НИА «Гид по стилю»)
- **Ссылка:** https://github.com/user-attachments/files/33784962/kodeks_stilya.pdf
- **Место в источнике:** страница 50 (в колоде: страницы 50–62)
- **Статус проверки:** VERIFIED (колода v5, решение 7: сверено по PDF)
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `E14`
- **Где в репозитории:** эпиграф слайда 14, [day-04/presentation.md, строка 387](../day-04/presentation.md#L387)

### 4.57. «Кодекс стиля» (Бератор-паблишинг) — E-kodeks [96]

> «…для каждого из этих стилей характерен свой соответствующий типаж внешности». [96]

- **Интерпретация для репутационных технологий:** Фраза справочника связывает каждое стилевое направление со своим типажом внешности, то есть стиль подбирают под человека, а не наоборот. На слайде шести направлений искусствоведческие параллели помечены как аналогия курса, а опора самого деления — справочник. [96]
- **Авторы:** Авторы справочника в материалах курса намеренно не называются (RFC v5, строка 36); издатель — «Бератор-паблишинг»
- **Дата:** 2007
- **Источник:** Кодекс стиля. Справочник делового дресс-кода. Москва: Бератор-паблишинг, 2007. 88 страниц (технологии НИА «Гид по стилю»)
- **Ссылка:** https://github.com/user-attachments/files/33784962/kodeks_stilya.pdf
- **Место в источнике:** страница 52 PDF-файла (в колоде: страницы 50–61)
- **Статус проверки:** VERIFIED (колода v5, решение 7: сверено по PDF)
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `E16`
- **Где в репозитории:** эпиграф слайда 16, [day-04/presentation.md, строка 425](../day-04/presentation.md#L425)

### 4.58. «Кодекс стиля» (Бератор-паблишинг) — E-kodeks [96]

> «…когда мы смотрим на человека, мы видим его одновременно всего и сразу — от макушки до пяток и оцениваем его в комплексе». [96]

- **Интерпретация для репутационных технологий:** Справочник обосновывает подбор аксессуаров целостностью восприятия: человека видят сразу целиком, поэтому деталь должна повторять линии лица и соответствовать уровню должности. Отсюда отказ от подбора «в тон» одежде; опора — справочник, без экспериментальной проверки. [96]
- **Авторы:** Авторы справочника в материалах курса намеренно не называются (RFC v5, строка 36); издатель — «Бератор-паблишинг»
- **Дата:** 2007
- **Источник:** Кодекс стиля. Справочник делового дресс-кода. Москва: Бератор-паблишинг, 2007. 88 страниц (технологии НИА «Гид по стилю»)
- **Ссылка:** https://github.com/user-attachments/files/33784962/kodeks_stilya.pdf
- **Место в источнике:** страница 47 PDF-файла (в колоде: страницы 16–18, 47–49)
- **Статус проверки:** VERIFIED (колода v5, решение 7: сверено по PDF)
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `E20`
- **Где в репозитории:** эпиграф слайда 20, [day-04/presentation.md, строка 505](../day-04/presentation.md#L505)

### 4.59. Shigenobu Kobayashi — E-kobayashi [97]

> "On this scale every color has three attributes: warm or cool, soft or hard, and clear or grayish" [97]

- **Перевод:** «На этой шкале у каждого цвета три свойства: тёплый или холодный, мягкий или жёсткий, чистый или сероватый». (перевод курса, [day-04/presentation.md, строка 233](../day-04/presentation.md#L233))
- **Интерпретация для репутационных технологий:** Кобаяси переворачивает вопрос с «что мне идёт» на «какое впечатление нужно»: сначала выбирают слово-образ, затем область цветов по трём свойствам. Для имиджмейкера это инструмент постановки цели образа; ограничение — шкала собрана на японской выборке. [97]
- **Авторы:** Shigenobu Kobayashi
- **Дата:** июнь 1981
- **Источник:** The Aim and Method of the Color Image Scale // Color Research & Application. 1981. Volume 6, Number 2. Pages 93–107
- **Ссылка:** https://doi.org/10.1002/col.5080060210
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED (колода v5, решение 7)
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `E6`
- **Где в репозитории:** эпиграф слайда 6, [day-04/presentation.md, строка 233](../day-04/presentation.md#L233)

### 4.60. Gabrielle K. Lehmann и соавторы — E-lehmann [98]

> "For men rating women, we found a small, statistically significant effect" [98]

- **Перевод:** «Для мужчин, оценивающих женщин, мы нашли небольшой, статистически значимый эффект». (перевод курса, [day-04/presentation.md, строка 271](../day-04/presentation.md#L271))
- **Интерпретация для репутационных технологий:** Эпиграф слайда с аналитическими маркерами цвета показывает реальный масштаб знаменитого «эффекта красного»: небольшой и только в одной конфигурации оценки. Отсюда уточнённый тезис курса — цвет не сообщает характер, а слабо и в зависимости от контекста сдвигает первое впечатление. [98]
- **Авторы:** Gabrielle K. Lehmann; Andrew J. Elliot; Robert J. Calin-Jageman
- **Дата:** 1 октября 2018
- **Источник:** Meta-Analysis of the Effect of Red on Perceived Attractiveness // Evolutionary Psychology. 2018. Volume 16, Number 4
- **Ссылка:** https://doi.org/10.1177/1474704918802412
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED (колода v5, решение 7)
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `E8`
- **Где в репозитории:** эпиграф слайда 8, [day-04/presentation.md, строка 271](../day-04/presentation.md#L271)

### 4.61. Беляева-Экземплярская С. Н., аннотация URSS — E-belyaeva [99]

> «Исследование дает соответствующий научный материал, относящийся к так называемым зрительным иллюзиям и их воздействию на психологию восприятия». [99]

- **Интерпретация для репутационных технологий:** Это текст аннотации издательства, а не слова самой Беляевой-Экземплярской. Эпиграф вводит идею слайда: глаз оценивает фигуру через иллюзии, которыми управляет модельер; отдельные правила книги проверены экспериментально с разными результатами. [99]
- **Авторы:** Аннотация издательства URSS к книге Беляевой-Экземплярской Софьи Николаевны
- **Дата:** книга 1934; стереотипное издание URSS 2025
- **Источник:** Моделирование одежды по законам зрительного восприятия. Издание стереотипное. Москва: URSS, 2025. 120 страниц. ISBN 978-5-9710-8597-3 — аннотация издательства
- **Ссылка:** https://urss.ru/cgi-bin/db.pl?lang=Ru&blang=ru&page=Book&id=325972
- **Место в источнике:** аннотация издательства
- **Статус проверки:** VERIFIED (колода v5, решение 7: аннотация издательства)
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `E9`
- **Где в репозитории:** эпиграф слайда 9, [day-04/presentation.md, строка 291](../day-04/presentation.md#L291)

### 4.62. Susan L. Sokolowski и соавторы — E-sokolowski [100]

> "By understanding shape, manufacturers can have a better idea of how to design, fit and grade products for this market throughout a size range" [100]

- **Перевод:** «Понимая форму, изготовители могут лучше проектировать, подгонять и градуировать изделия для этого рынка по всему размерному ряду». (перевод курса, [day-04/presentation.md, строка 329](../day-04/presentation.md#L329))
- **Интерпретация для репутационных технологий:** Эпиграф подчёркивает, что FFIT решает другую задачу — точную посадку изделий по всему размерному ряду, а не управление впечатлением. Для имиджмейкера это отраслевой конкурент типологий фигуры: метод на 3D-сканах полезен для посадки, но не говорит, какой образ построить. [100]
- **Авторы:** Susan L. Sokolowski; Chrissy Bettencourt
- **Дата:** 17 ноября 2020
- **Источник:** Modification of the Female Figure Identification Technique (FFIT) Form for Apparel // Proceedings of 3DBODY.TECH 2020 — 11th International Conference and Exhibition on 3D Body Scanning and Processing Technologies
- **Ссылка:** https://doi.org/10.15221/20.22
- **Место в источнике:** Abstract, страница 1
- **Статус проверки:** VERIFIED (колода v5, решение 7)
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `E11`
- **Где в репозитории:** эпиграф слайда 11, [day-04/presentation.md, строка 329](../day-04/presentation.md#L329)

### 4.63. Peter Thompson и соавторы — E-thompson [101]

> "find no support for the notion that horizontal lines would be 'fattening' on clothes" [101]

- **Перевод:** «…не находим подтверждения тому, что горизонтальные линии на одежде „полнят“». (перевод курса, [day-04/presentation.md, строка 367](../day-04/presentation.md#L367))
- **Интерпретация для репутационных технологий:** Эксперимент не подтвердил, что горизонтальные линии на одежде «полнят». На слайде аналитических маркеров формы вывод такой: иллюзии реальны, но слабы, а привычные правила иногда работают наоборот, поэтому решение проверяют на носителе, а не перед зеркалом. [101]
- **Авторы:** Peter Thompson; Kyriaki Mikellidou
- **Дата:** 2011
- **Источник:** Applying the Helmholtz Illusion to Fashion: Horizontal Stripes Won't Make You Look Fatter // i-Perception. 2011. Volume 2, Number 1. Pages 69–76
- **Ссылка:** https://doi.org/10.1068/i0405
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED (колода v5, решение 7)
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `E13`
- **Где в репозитории:** эпиграф слайда 13, [day-04/presentation.md, строка 367](../day-04/presentation.md#L367)

### 4.64. Трубецкова И. А., Найденская Н. Г., аннотация «Эксмо» — E-eksmo [102]

> «…формулу для расчета вашего персонального коэффициента консервативности — в зависимости от вашей сферы деятельности, занимаемой должности и уровня встречи или мероприятия». [102]

- **Интерпретация для репутационных технологий:** Эпиграф — текст аннотации издательства «Эксмо», а не авторов книги Трубецковой и Найденской. Он вводит метод, где строгость образа вычисляют по сфере деятельности, должности и уровню встречи; формула отвечает только на вопрос о строгости и не заменяет вкус. [102]
- **Авторы:** Аннотация издательства «Эксмо» к книге Трубецковой Инессы Александровны и Найденской Наталии Георгиевны
- **Дата:** 30 ноября 2016 (дата выхода по странице издательства)
- **Источник:** Золотые правила стиля. Дресс-код успешной женщины. Москва: Эксмо, 2016. 256 страниц. ISBN 978-5-699-92975-7 — аннотация издательства
- **Ссылка:** https://eksmo.ru/book/zolotye-pravila-stilya-dress-kod-uspeshnoy-zhenshchiny-ITD816396/
- **Место в источнике:** аннотация издательства (список преимуществ книги)
- **Статус проверки:** VERIFIED (колода v5, решение 7: аннотация издательства)
- **Где в репозитории:** эпиграф слайда 15, [day-04/presentation.md, строка 406](../day-04/presentation.md#L406)
- **Примечание:** В колоде слово «формула» согласовано с контекстом («…формулу…») и короткое тире заменено длинным; на странице издательства: «формула для расчета вашего персонального коэффициента консервативности – в зависимости от вашей сферы деятельности, занимаемой должности и уровня встречи или мероприятия.».

### 4.65. Silvia Bellezza и соавторы — E-bellezza [103]

> "people confer higher status and competence to nonconforming rather than conforming individuals" [103]

- **Перевод:** «Люди приписывают более высокий статус и компетентность нонконформистам, а не конформистам». (перевод курса, [day-04/presentation.md, строка 466](../day-04/presentation.md#L466))
- **Интерпретация для репутационных технологий:** Эффект «красных кроссовок» — опора контрастного вектора: осознанный нонконформизм может повышать приписываемый статус и компетентность. Слайд сразу ограничивает вывод: так бывает, только если аудитория знает норму и видит намерение. [103]
- **Авторы:** Silvia Bellezza; Francesca Gino; Anat Keinan
- **Дата:** июнь 2014 (онлайн 18 декабря 2013)
- **Источник:** The Red Sneakers Effect: Inferring Status and Competence from Signals of Nonconformity // Journal of Consumer Research. 2014. Volume 41, Number 1. Pages 35–54
- **Ссылка:** https://doi.org/10.1086/674870
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED (колода v5, решение 7)
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `E18`
- **Где в репозитории:** эпиграф слайда 18, [day-04/presentation.md, строка 466](../day-04/presentation.md#L466)

### 4.66. Silvia Bellezza и соавторы — E-bellezza [103]

> "the positive inferences disappear when the observer is unfamiliar with the environment, when the nonconforming behavior is depicted as unintentional" [103]

- **Перевод:** «Положительные выводы исчезают, когда наблюдатель не знаком со средой, когда нонконформное поведение показано как ненамеренное…». (перевод курса, [day-04/presentation.md, строка 562](../day-04/presentation.md#L562))
- **Интерпретация для репутационных технологий:** Граница эффекта «красных кроссовок»: выигрыш исчезает, если зритель не знает среды или видит в отступлении случайность. На слайде об аксессуарах вывод такой: одна деталь может нести всё отступление образа, но оно должно читаться как замысел. [103]
- **Авторы:** Silvia Bellezza; Francesca Gino; Anat Keinan
- **Дата:** июнь 2014 (онлайн 18 декабря 2013)
- **Источник:** The Red Sneakers Effect: Inferring Status and Competence from Signals of Nonconformity // Journal of Consumer Research. 2014. Volume 41, Number 1. Pages 35–54
- **Ссылка:** https://doi.org/10.1086/674870
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED (колода v5, решение 7)
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `E23`
- **Где в репозитории:** эпиграф слайда 23, [day-04/presentation.md, строка 562](../day-04/presentation.md#L562)

### 4.67. Georg Simmel — E-simmel [104]

> "Fashion is a form of imitation and so of social equalization, but, paradoxically, in changing incessantly, it differentiates one time from another and one social stratum from another." [104]

- **Перевод:** «Мода — это форма подражания и, значит, социального уравнивания, но, парадоксальным образом, непрерывно меняясь, она отличает одно время от другого и один социальный слой от другого». (перевод курса, [day-04/presentation.md, строка 485](../day-04/presentation.md#L485))
- **Интерпретация для репутационных технологий:** Фраза — первое предложение аннотации редакции к публикации 1957 года, а не собственный текст Зиммеля, и это стоит оговаривать. Эпиграф вводит двойственность моды: образ одновременно показывает принадлежность к кругу и отличие, а мода сезона входит в него подчинённой линией. [104]
- **Авторы:** Georg Simmel
- **Дата:** 1957 (английская публикация; немецкий оригинал 1904–1905)
- **Источник:** Fashion // American Journal of Sociology. 1957. Volume 62, Number 6. Pages 541–558
- **Ссылка:** https://doi.org/10.1086/222102
- **Место в источнике:** страница 541, аннотация (ABSTRACT) публикации 1957 года — текст редакции, а не самого Зиммеля
- **Статус проверки:** VERIFIED (колода v5, решение 7)
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `E19`
- **Где в репозитории:** эпиграф слайда 19, [day-04/presentation.md, строка 485](../day-04/presentation.md#L485)

### 4.68. Marjorie M. Baker — E-baker [105]

> "A well-planned outfit calls attention first to one area, while other areas support the central theme." [105]

- **Перевод:** «Хорошо продуманный комплект сначала привлекает внимание к одной зоне, а остальные поддерживают главную тему». (перевод курса, [day-04/presentation.md, строка 524](../day-04/presentation.md#L524))
- **Интерпретация для репутационных технологий:** Пособие сводит работу с аксессуарами к одному заранее выбранному центру внимания, которому подчинены остальные зоны. Практический вывод для образа — один акцент на спокойной базе; источник при этом рассчитан на непрофессионалов и опирается на принципы баланса, ритма и пропорции, а не на эксперимент. [105]
- **Авторы:** Marjorie M. Baker
- **Дата:** 2020 (пересмотренное издание, «Reviewed 11-2020»; год первого выпуска в PDF не указан)
- **Источник:** Accessories: The Finishing Touch. Publication FCS2-347. Lexington: University of Kentucky Cooperative Extension Service, 2020 (первоначально подготовлено Linda M. Heaton)
- **Ссылка:** https://publications.mgcafe.uky.edu/sites/publications.ca.uky.edu/files/FCS2347.pdf
- **Место в источнике:** страница 4, абзац о выделении (Emphasis)
- **Статус проверки:** VERIFIED (колода v5, решение 7)
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `E21`
- **Где в репозитории:** эпиграф слайда 21, [day-04/presentation.md, строка 524](../day-04/presentation.md#L524)

### 4.69. Young Jee Han и соавторы — E-han [106]

> "Wealthy consumers low in need for status want to associate with their own kind and pay a premium for quiet goods only they can recognize." [106]

- **Перевод:** «Состоятельные покупатели с низкой потребностью в статусе хотят объединяться со своими и платят премию за тихие вещи, которые узнают только они». (перевод курса, [day-04/presentation.md, строка 543](../day-04/presentation.md#L543))
- **Интерпретация для репутационных технологий:** Исследование объясняет логику «тихой роскоши»: часть состоятельных людей платит за вещи, которые узнают только свои. Для имиджа громкость знака статуса выбирают по аудитории: для своего круга — тихий сигнал, для широкой публики — заметный. [106]
- **Авторы:** Young Jee Han; Joseph C. Nunes; Xavier Drèze
- **Дата:** июль 2010
- **Источник:** Signaling Status with Luxury Goods: The Role of Brand Prominence // Journal of Marketing. 2010. Volume 74, Number 4. Pages 15–30
- **Ссылка:** https://doi.org/10.1509/jmkg.74.4.015
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED (колода v5, решение 7)
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `E22`
- **Где в репозитории:** эпиграф слайда 22, [day-04/presentation.md, строка 543](../day-04/presentation.md#L543)

### 4.70. Helmut Leder и соавторы — E-leder [107]

> "they can lower how attractive, but increase how intelligent and trustworthy people wearing them appear. These effects depend on the kind of glasses worn." [107]

- **Перевод:** «…они могут снижать привлекательность, но повышать воспринимаемый интеллект и надёжность их владельцев. Эти эффекты зависят от вида очков». (перевод курса, [day-04/presentation.md, строка 581](../day-04/presentation.md#L581))
- **Интерпретация для репутационных технологий:** Очки — пример детали с измеримым эффектом: они могут снижать привлекательность, но повышать воспринимаемые интеллект и надёжность, причём результат зависит от вида оправы. Вывод слайда: деталь сдвигает впечатление, но доверия не гарантирует. [107]
- **Авторы:** Helmut Leder; Michael Forster; Gernot Gerger
- **Дата:** декабрь 2011
- **Источник:** The Glasses Stereotype Revisited: Effects of Eyeglasses on Perception, Recognition, and Impression of Faces // Swiss Journal of Psychology. 2011. Volume 70, Number 4. Pages 211–222
- **Ссылка:** https://doi.org/10.1024/1421-0185/a000059
- **Место в источнике:** Abstract
- **Статус проверки:** VERIFIED (колода v5, решение 7)
- **Сверка с источником:** текст источника сохранён в [source-excerpts-711.txt](course-quotes-provenance/source-excerpts-711.txt) под ключом `E24`
- **Где в репозитории:** эпиграф слайда 24, [day-04/presentation.md, строка 581](../day-04/presentation.md#L581)

## Границы списка

**Что входит.** Дословная цитата с указанием автора и источника, проверенная по источнику, из этих мест репозитория:

- каталог источников курса [#650](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-09-30-course-sources-and-presentations-650.md) — все цитаты серий Г, Д, С, Н, П, О;
- таблица источников М1–М7 в [обосновании Дня 1](../day-01/rationale-and-method.md);
- записи R:Simini и R:Gentner в [программе исследований GRA](../../../methodology/research-program/50-open-research.md);
- таблица источников Д3-Т3…Д3-Т5 в [обосновании Дня 3](../day-03/rationale-and-method.md);
- эпиграфы всех слайдов [презентации Дня 4, версия 5](../day-04/presentation.md).

**Что не входит и почему.**

- Эпиграфы и тезисы презентаций Дней 1–3 — это формулировки самого курса, а не цитаты источников.
- Высказывания основателей кейсов и формулировки лектора — не опубликованные источники.
- Пересказы (например, Д3-Т1 и Д3-Т2 в обосновании Дня 3) — не дословные цитаты.
- Короткие цитатные фрагменты в тексте модуля `image-technologies` — те же источники уже есть в списке через каталог #650 или эпиграфы Дня 4.
- Источники со статусом `UNVERIFIED` в каталоге #650 (Г2, Д14, Н13, П5, П6, П11, О2) и определение репутации у Fombrun (1996, страница 72): каталог прямо говорит, что их не цитируют.

## Пробелы и решения

- **ФИО не установлены полностью.** Отчество Г. И. Идрисова (Г4) и О. И. Шипкова (О7); полные имена И. Джонек-Ковальской (С7), Ю. А. Моисеенковой (С9), М. С. Ковалёвой (О21), О. Серовой (О6) и A. W. van den Ban (С4). В открытых источниках, доступных при подготовке, их нет; в полях «Авторы» это сказано прямо.
- **Переводчики** русского издания К. Левина (Г7) не установлены.
- **Выходные данные Г7.** Каталог указывает издательство «Сенсор», а у В. А. Лукова — «Речь»; противоречие записано, не разрешено.
- **Дата принятия Кодекса этики в сфере ИИ (Н10)** в извлечённом тексте не найдена; адрес PDF в каталоге повреждён, поэтому дана ссылка на сайт кодекса.
- **«Кодекс стиля».** По решению [RFC v5](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/48ebe5230be87ca5bf8a08b385e296a2987e9958/research/reputation-technologies/2026-11-03-rfc-presentation-update-v5.md) (строка 36) имена авторов справочника в материалах курса не воспроизводятся; список следует этому решению. Расшифровка аббревиатуры «НИА» в репозитории не найдена, поэтому она дана как в колоде.
- **Номера страниц «Кодекса стиля».** В записях указан номер страницы PDF-файла, где найдена цитата, и диапазон из подписи слайда.
- **Эпиграфы Дня 4 — переводы курса.** Колода часто переводит часть длинной фразы. В поле «Цитата» стоит точный отрезок оригинала, которому соответствует перевод; полные фразы — в [`source-excerpts-711.txt`](course-quotes-provenance/source-excerpts-711.txt).
- **И. Иттен (слайд 4).** Экземпляр archive.org из подписи слайда выдаётся только по записи; текст сверен по другому открытому скану того же издания 1973 года (`johannes-ittens-the-art-of-color`).
- **Г. Зиммель (слайд 19).** Фраза эпиграфа — первое предложение аннотации редакции к публикации 1957 года, а не текст самого Зиммеля.
- **M. M. Baker (слайд 21).** Пособие датировано «Reviewed 11-2020»; год первого выпуска в PDF не указан.

## Список источников (ALCE)

[1] Jan Tinbergen. Shaping the World Economy: Suggestions for an International Economic Policy. New York: The Twentieth Century Fund, 1962. Appendix VI «An Analysis of World Trade Flows», pages 262–293. Дата: 1962. https://repub.eur.nl/pub/16826 — VERIFIED-FULLTEXT. Ключ в материалах курса: Г1.

[2] Thomas Chaney. The Gravity Equation in International Trade: An Explanation. National Bureau of Economic Research Working Paper Number 19285. Cambridge, Massachusetts: National Bureau of Economic Research, 2013. Дата: август 2013. https://www.nber.org/papers/w19285.pdf — VERIFIED-FULLTEXT. Ключ в материалах курса: Г3.

[3] Каукин Андрей Сергеевич; Идрисов Георгий (отчество: полное имя в открытых источниках не установлено). Гравитационная модель внешней торговли России: случай большой по площади страны с протяженной границей // Экономическая политика. 2013. Номер 4. Страницы 133–154. Дата: 2013. https://www.iep.ru/files/text/policy/2013-4/kaukin.pdf — VERIFIED-FULLTEXT. Ключ в материалах курса: Г4.

[4] Kurt Lewin. Frontiers in Group Dynamics: Concept, Method and Reality in Social Science; Social Equilibria and Social Change // Human Relations. 1947. Volume 1, Number 1. Pages 5–41. Дата: 1947. https://doi.org/10.1177/001872674700100103 — VERIFIED-FULLTEXT. Ключ в материалах курса: Г5.

[5] Kurt Lewin; редактор Dorwin Cartwright. Field Theory in Social Science: Selected Theoretical Papers / edited by Dorwin Cartwright. New York: Harper & Brothers, 1951. Дата: 1951. https://archive.org/stream/dli.ernet.503983/503983-Field%20Theory%20In%20Social%20Science_djvu.txt — VERIFIED-FULLTEXT. Ключ в материалах курса: Г6.

[6] Курт Левин (Kurt Lewin); цитаты приведены по статье: Луков Валерий Андреевич; переводчики русского издания: полное имя в открытых источниках не установлено. Теория поля в социальных науках. Санкт-Петербург: Сенсор, 2000 (у Лукова: Санкт-Петербург: Речь), цитируется по: Полевой и сферный подходы в гуманитарных науках // Горизонты гуманитарного знания. 2017. Номер 6. Дата: русское издание 2000; статья Лукова 2017. https://doi.org/10.17805/ggz.2017.6.1 — VERIFIED-SECONDARY. Ключ в материалах курса: Г7.

[7] Fritz Heider. Attitudes and Cognitive Organization // The Journal of Psychology. 1946. Volume 21. Pages 107–112. Дата: 1946. https://psychclassics.yorku.ca/Heider/attitudes.htm — VERIFIED-FULLTEXT. Ключ в материалах курса: Г8.

[8] Dorwin Cartwright; Frank Harary. Structural Balance: A Generalization of Heider's Theory // Psychological Review. 1956. Volume 63, Number 5. Pages 277–293. Дата: 1956. https://snap.stanford.edu/class/cs224w-readings/cartwright56balance.pdf — VERIFIED-FULLTEXT. Ключ в материалах курса: Г9.

[9] Mark S. Granovetter. The Strength of Weak Ties // American Journal of Sociology. 1973. Volume 78, Number 6. Pages 1360–1380. Дата: май 1973. https://www.jstor.org/stable/2776392 — VERIFIED-FULLTEXT. Ключ в материалах курса: Г10.

[10] Roger C. Mayer; James H. Davis; F. David Schoorman. An Integrative Model of Organizational Trust // Academy of Management Review. 1995. Volume 20, Number 3. Pages 709–734. Дата: 1995. https://www.jstor.org/stable/258792 — VERIFIED-FULLTEXT. Ключ в материалах курса: Г11.

[11] Charles J. Fombrun; цитата приведена по статье Michael L. Barnett, John M. Jermier, Barbara A. Lafferty. Reputation: Realizing Value from the Corporate Image. Boston, Massachusetts: Harvard Business School Press, 1996, цитируется по: Corporate Reputation: The Definitional Landscape // Corporate Reputation Review. 2006. Volume 9, Number 1. Page 29. Дата: 1996 (книга); 2006 (вторичный источник). https://www.mv.helsinki.fi/home/aula/Top20/corp-reputation-definitional-landscape.pdf — VERIFIED-SECONDARY. Ключ в материалах курса: Г12.

[12] Michael L. Barnett; John M. Jermier; Barbara A. Lafferty. Corporate Reputation: The Definitional Landscape // Corporate Reputation Review. 2006. Volume 9, Number 1. Pages 26–38. Дата: 2006. https://www.mv.helsinki.fi/home/aula/Top20/corp-reputation-definitional-landscape.pdf — VERIFIED-FULLTEXT. Ключ в материалах курса: Г13.

[13] Когденко Вера Геннадьевна. Анализ интегрированной отчетности: социально-репутационный капитал // Экономический анализ: теория и практика. 2016. Номер 6 (453). Страницы 100–114. Дата: 2016. https://cyberleninka.ru/article/n/analiz-integrirovannoy-otchetnosti-sotsialno-reputatsionnyy-kapital — VERIFIED-FULLTEXT. Ключ в материалах курса: Г14.

[14] Шагеева Гульнара Рафаиловна. Репутационный капитал личности в деловой среде и его влияние на репутацию компании // Вестник Московского университета. Серия 6. Экономика. 2024. Том 59, номер 4. Страницы 293–312. Дата: 2024. https://doi.org/10.55959/MSU0130-0105-6-59-4-13 — VERIFIED-FULLTEXT. Ключ в материалах курса: Г15.

[15] Claudio Castellano; Santo Fortunato; Vittorio Loreto. Statistical Physics of Social Dynamics // Reviews of Modern Physics. 2009. Volume 81, Number 2. Pages 591–646. Дата: 2009. https://doi.org/10.1103/RevModPhys.81.591 — VERIFIED-FULLTEXT. Ключ в материалах курса: Г16.

[16] Somin Wadhwa; Silvio Amir; Byron C. Wallace. Revisiting Relation Extraction in the Era of Large Language Models // Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL 2023). arXiv:2305.05003. Дата: 2023 (версия arXiv v2 — 16 июля 2024). https://arxiv.org/pdf/2305.05003 — VERIFIED-FULLTEXT. Ключ в материалах курса: Н5.

[17] Edelman (организация-автор исследования); изложение: Institute of Public Administration Australia, Queensland. 2025 Edelman Trust Barometer: Trust and the Crisis of Grievance — изложение Institute of Public Administration Australia, Queensland. Дата: январь 2025. https://qld.ipaa.org.au/2025/02/2025-edelman-trust-barometer-trust-and-the-crisis-of-grievance — VERIFIED-SECONDARY. Ключ в материалах курса: М1.

[18] Edelman (организация-автор исследования); цитата о посреднике доверия — Richard Edelman, генеральный директор Edelman; изложение: O'Dwyer's. 2026 Edelman Trust Barometer — изложение в статье «National Insularity Threatens Global Economy», O'Dwyer's. Дата: январь 2026 (статья O'Dwyer's — 20 января 2026). https://www.odwyerpr.com/story/public/24179/2026-01-20/national-insularity-threatens-global-economy.html — VERIFIED-SECONDARY. Ключ в материалах курса: М2.

[19] Klaudia Jaźwińska; Aisvarya Chandrasekar. AI Search Has a Citation Problem // Columbia Journalism Review, Tow Center for Digital Journalism. Дата: 6 марта 2025. https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php — VERIFIED-FULLTEXT. Ключ в материалах курса: М3.

[20] Darren Edge; Ha Trinh; Newman Cheng; Joshua Bradley; Alex Chao; Apurva Mody; Steven Truitt; Dasha Metropolitansky; Robert Osazuwa Ness; Jonathan Larson. From Local to Global: A Graph RAG Approach to Query-Focused Summarization. arXiv:2404.16130. Дата: апрель 2024 (версия 2 — 19 февраля 2025). https://arxiv.org/abs/2404.16130 — VERIFIED-FULLTEXT (аннотация). Ключ в материалах курса: М4.

[21] Chris McKay. OpenAI Unveils Deep Research, an AI Agent That Conducts Multi-Step Research Tasks // Maginative. Дата: 2 февраля 2025. https://www.maginative.com/article/openai-unveils-deep-research-an-ai-agent-that-conducts-multi-step-research-tasks/ — VERIFIED-SECONDARY. Ключ в материалах курса: М5.

[22] Karthik Rajkumar; Guillaume Saint-Jacques; Iavor Bojinov; Erik Brynjolfsson; Sinan Aral. A Causal Test of the Strength of Weak Ties // Science. 2022. Volume 377, Number 6612. Дата: 16 сентября 2022. https://doi.org/10.1126/science.abl4476 — VERIFIED-FULLTEXT (аннотация). Ключ в материалах курса: М6.

[23] Heinrich Peters; Sandra C. Matz. Large Language Models Can Infer Psychological Dispositions of Social Media Users // PNAS Nexus (Proceedings of the National Academy of Sciences Nexus). 2024. Препринт arXiv:2309.08631. Дата: 31 мая 2024. https://arxiv.org/abs/2309.08631 — VERIFIED-FULLTEXT (аннотация arXiv). Ключ в материалах курса: М7.

[24] Filippo Simini; Marta C. González; Amos Maritan; Albert-László Barabási. A Universal Model for Mobility and Migration Patterns // Nature. 2012. Volume 484. Pages 96–100. arXiv:1111.0586. Дата: 2012. https://arxiv.org/abs/1111.0586 — VERIFIED-FULLTEXT (аннотация arXiv). Ключ в материалах курса: R:Simini.

[25] Dedre Gentner; обзор — CogSci Summaries (сайт Jim Davies). Structure-Mapping: A Theoretical Framework for Analogy // Cognitive Science. 1983. Volume 7, Number 2. Pages 155–170, цитируется по обзору CogSci Summaries. Дата: 1983. https://www.jimdavies.org/summaries/gentner1983.html — VERIFIED-SECONDARY (слова обзора, а не Гентнер). Ключ в материалах курса: R:Gentner.

[26] Catherine H. Crouch; Eric Mazur. Peer Instruction: Ten Years of Experience and Results // American Journal of Physics. 2001. Volume 69, Number 9. Pages 970–977. Дата: сентябрь 2001. https://doi.org/10.1119/1.1374249 — VERIFIED-FULLTEXT. Ключ в материалах курса: П1.

[27] Scott Freeman; Sarah L. Eddy; Miles McDonough; Michelle K. Smith; Nnadozie Okoroafor; Hannah Jordt; Mary Pat Wenderoth. Active Learning Increases Student Performance in Science, Engineering, and Mathematics // Proceedings of the National Academy of Sciences of the United States of America. 2014. Volume 111, Number 23. Pages 8410–8415. Дата: 2014. https://doi.org/10.1073/pnas.1319030111 — VERIFIED-FULLTEXT. Ключ в материалах курса: П2.

[28] Neil A. Bradbury. Attention Span During Lectures: 8 Seconds, 10 Minutes, or More? // Advances in Physiology Education. 2016. Volume 40, Number 4. Pages 509–513. Дата: декабрь 2016. https://doi.org/10.1152/advan.00109.2016 — VERIFIED-FULLTEXT. Ключ в материалах курса: П3.

[29] Richard E. Mayer; Roxana Moreno. Nine Ways to Reduce Cognitive Load in Multimedia Learning // Educational Psychologist. 2003. Volume 38, Number 1. Pages 43–52. Дата: 2003. https://doi.org/10.1207/S15326985EP3801_6 — VERIFIED-FULLTEXT. Ключ в материалах курса: П4.

[30] Лукашевич Денис Анатольевич. Применимость теории «спирали молчания» к сети Интернет и новым медиа // Вестник Новосибирского государственного университета. Серия: История, филология. 2013. Том 12, выпуск 6: Журналистика. Страницы 61–66. Дата: 2013. https://cyberleninka.ru/article/n/primenimost-teorii-spirali-molchaniya-k-seti-internet-i-novym-media — VERIFIED-FULLTEXT. Ключ в материалах курса: П7.

[31] Ван Цзэкай (Zekai Wang); Курышева Юлия Владимировна; Никонов Сергей Борисович. Концепция «спирали молчания» в контексте политической коммуникации // Litera. 2025. Номер 12. Страницы 240–254. Дата: декабрь 2025. https://doi.org/10.25136/2409-8698.2025.12.77540 — VERIFIED-FULLTEXT. Ключ в материалах курса: П8.

[32] Ибрагимов Гасангусейн Ибрагимович (о дидактическом наследии Вербицкого Андрея Александровича). Дидактическое наследие А. А. Вербицкого и современность: к 80-летию со дня рождения // Казанский педагогический журнал. 2021. Номер 4. Страницы 7–12. Дата: 2021. https://doi.org/10.51379/KPJ.2021.148.4.001 — VERIFIED-FULLTEXT (слова Ибрагимова, а не Вербицкого). Ключ в материалах курса: П9.

[33] Лазарева Анна Сергеевна. Особенности применения технологии активного обучения в иноязычной подготовке взрослых в корпоративной среде // Педагогика. Вопросы теории и практики. 2025. Том 10, выпуск 5. Страницы 640–648. Дата: май 2025. https://doi.org/10.30853/ped20250077 — VERIFIED-FULLTEXT. Ключ в материалах курса: П10.

[34] Luc Moreau; Paolo Missier (редакторы рекомендации). PROV-DM: The PROV Data Model / edited by Luc Moreau, Paolo Missier. World Wide Web Consortium Recommendation, 30 April 2013. Дата: 30 апреля 2013. https://www.w3.org/TR/2013/REC-prov-dm-20130430/ — VERIFIED-FULLTEXT. Ключ в материалах курса: Д1.

[35] Office of the Director of National Intelligence (Управление директора национальной разведки США); подписал James R. Clapper. Intelligence Community Directive 203: Analytic Standards. Дата: вступила в силу 2 января 2015. https://www.dni.gov/files/documents/ICD/ICD-203.pdf — VERIFIED-FULLTEXT. Ключ в материалах курса: Д2.

[36] Richards J. Heuer, Jr. Psychology of Intelligence Analysis. Washington, District of Columbia: Center for the Study of Intelligence, Central Intelligence Agency, 1999. Дата: 1999. https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf — VERIFIED-FULLTEXT. Ключ в материалах курса: Д3.

[37] Sherman Kent. Words of Estimative Probability // Studies in Intelligence. 1964. Volume 8, Number 4 (переиздание Center for the Study of Intelligence, Central Intelligence Agency). Дата: 1964. https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf — VERIFIED-FULLTEXT. Ключ в материалах курса: Д4.

[38] Headquarters, Department of the Army (Штаб Министерства армии США) — коллективный автор. Field Manual 2-22.3 (Field Manual 34-52): Human Intelligence Collector Operations. Washington, District of Columbia: Headquarters, Department of the Army, 2006. Appendix B «Source and Information Reliability Matrix». Дата: 6 сентября 2006. https://irp.fas.org/doddir/army/fm2-22-3.pdf — VERIFIED-FULLTEXT. Ключ в материалах курса: Д5.

[39] Richard Y. Wang; Diane M. Strong. Beyond Accuracy: What Data Quality Means to Data Consumers // Journal of Management Information Systems. 1996. Volume 12, Number 4. Pages 5–33. Дата: 1996. https://www.jstor.org/stable/40398176 — VERIFIED-FULLTEXT. Ключ в материалах курса: Д6.

[40] International Association for the Measurement and Evaluation of Communication (Международная ассоциация измерения и оценки коммуникаций) — коллективный автор. Barcelona Principles 4.0 (электронная книга). Дата: июнь 2025. https://amecorg.com/wp-content/uploads/2025/06/Barcelona-Principles-V4.0-eBook-Finalv-compressed.pdf — VERIFIED-FULLTEXT. Ключ в материалах курса: Д7.

[41] Michael D. Fetters; Leslie A. Curry; John W. Creswell. Achieving Integration in Mixed Methods Designs — Principles and Practices // Health Services Research. 2013. Volume 48, Number 6, Part 2. Pages 2134–2156. Дата: 2013. https://doi.org/10.1111/1475-6773.12117 — VERIFIED-FULLTEXT. Ключ в материалах курса: Д8.

[42] Большаков Никита Викторович. Сочетать, комбинировать, смешивать: качественные и количественные методы в современной исследовательской практике // Мониторинг общественного мнения: экономические и социальные перемены. 2017. Номер 3 (139). Страницы 21–29. Дата: 2017. https://doi.org/10.14515/monitoring.2017.3.03 — VERIFIED-FULLTEXT. Ключ в материалах курса: Д9.

[43] Соколова Дарья Валерьевна. Фактчекинг и верификация информации в российских СМИ: результаты опроса // Вестник Московского университета. Серия 10. Журналистика. 2018. Номер 4. Страницы 3–25. Дата: 2018. https://cyberleninka.ru/article/n/faktcheking-i-verifikatsiya-informatsii-v-rossiyskih-smi-rezultaty-oprosa — VERIFIED-FULLTEXT. Ключ в материалах курса: Д10.

[44] Поздняков Владимир Александрович. Свойства и методы обработки информации в конкурентной разведке // Известия Южного федерального университета. Технические науки. 2010. Номер 11 (112). Страницы 238–245. Дата: 2010. https://cyberleninka.ru/article/n/svoystva-i-metody-obrabotki-informatsii-v-konkurentnoy-razvedke — VERIFIED-FULLTEXT. Ключ в материалах курса: Д11.

[45] Федеральное агентство по техническому регулированию и метрологии (Росстандарт) — национальный стандарт, персональных авторов нет. ГОСТ Р 71484.2-2024 (ИСО/МЭК 5259-2:2024). Национальный стандарт Российской Федерации. Искусственный интеллект. Качество данных для аналитики и машинного обучения. Часть 2. Показатели качества данных. Москва: Федеральное государственное бюджетное учреждение «Институт стандартизации», 2024. Дата: утверждён 28 октября 2024, введён 1 января 2025. https://meganorm.ru/mega_doc/norm_update_01032025/gost-r_gosudarstvennyj-standart/0/gost_r_71484_2-2024_iso_mek_5259-2_2024_natsionalnyy.html — VERIFIED-FULLTEXT. Ключ в материалах курса: Д12.

[46] Аргамакова Александра Александровна. Смешанная методология социальных наук // Эпистемология и философия науки. 2023. Том 60, номер 4. Страницы 212–224. Дата: 2023. https://doi.org/10.5840/eps202360467 — VERIFIED-FULLTEXT. Ключ в материалах курса: Д13.

[47] Jason Wei; Xuezhi Wang; Dale Schuurmans; Maarten Bosma; Brian Ichter; Fei Xia; Ed Chi; Quoc Le; Denny Zhou. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models // Advances in Neural Information Processing Systems 35 (36th Conference on Neural Information Processing Systems, NeurIPS 2022). arXiv:2201.11903. Дата: 2022 (версия arXiv v6 — 10 января 2023). https://arxiv.org/pdf/2201.11903 — VERIFIED-FULLTEXT. Ключ в материалах курса: Н1.

[48] Jules White; Quchen Fu; Sam Hays; Michael Sandborn; Carlos Olea; Henry Gilbert; Ashraf Elnashar; Jesse Spencer-Smith; Douglas C. Schmidt. A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT. arXiv:2302.11382. Дата: 21 февраля 2023. https://arxiv.org/pdf/2302.11382 — VERIFIED-FULLTEXT. Ключ в материалах курса: Н2.

[49] Ziwei Ji; Nayeon Lee; Rita Frieske; Tiezheng Yu; Dan Su; Yan Xu; Etsuko Ishii; Ye Jin Bang; Andrea Madotto; Pascale Fung. Survey of Hallucination in Natural Language Generation // ACM Computing Surveys (Association for Computing Machinery). 2023. Volume 55, Number 12. Дата: 2023. https://doi.org/10.1145/3571730 — VERIFIED-FULLTEXT. Ключ в материалах курса: Н3.

[50] Tianyu Gao; Howard Yen; Jiatong Yu; Danqi Chen. Enabling Large Language Models to Generate Text with Citations // Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing. arXiv:2305.14627. Дата: 2023. https://arxiv.org/pdf/2305.14627 — VERIFIED-FULLTEXT. Ключ в материалах курса: Н4.

[51] National Institute of Standards and Technology (Национальный институт стандартов и технологий США) — коллективный автор. Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1). Дата: июль 2024. https://doi.org/10.6028/NIST.AI.600-1 — VERIFIED-FULLTEXT. Ключ в материалах курса: Н6.

[52] Anthropic — документация компании, персональные авторы не указаны. Reduce Hallucinations // Claude Documentation: Test and Evaluate — Strengthen Guardrails. Дата: страница документации, дата обращения 30 сентября 2026. https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations — VERIFIED-FULLTEXT. Ключ в материалах курса: Н7.

[53] OpenAI — документация компании, персональные авторы не указаны. Prompt Engineering // OpenAI Application Programming Interface Documentation: Guides. Дата: страница документации, дата обращения 30 сентября 2026. https://developers.openai.com/api/docs/guides/prompt-engineering — VERIFIED-FULLTEXT. Ключ в материалах курса: Н8.

[54] Публичное акционерное общество «Сбербанк» — документация компании, персональные авторы не указаны. Основы промпт-инжиниринга // Документация GigaChat API, раздел Prompts Hub. Дата: страница документации, дата обращения 30 сентября 2026. https://developers.sber.ru/docs/ru/gigachat/prompts-hub/prompt-engineering — VERIFIED-FULLTEXT. Ключ в материалах курса: Н9.

[55] Альянс в сфере искусственного интеллекта — коллективный документ, персональные авторы не указаны. Кодекс этики в сфере искусственного интеллекта. Дата: дата принятия в извлечённом тексте не найдена; файл размещён 23 мая 2025. https://ethics.a-ai.ru/ — VERIFIED-FULLTEXT. Ключ в материалах курса: Н10.

[56] Кирпичёв Александр Евгеньевич. Промпты (запросы) для генеративного искусственного интеллекта в юридическом дискурсе // Вестник Российского университета дружбы народов. Серия: Юридические науки. 2024. Том 28, номер 4. Страницы 906–918. Дата: 2024. https://doi.org/10.22363/2313-2337-2024-28-4-906-918 — VERIFIED-FULLTEXT. Ключ в материалах курса: Н11.

[57] Давлатова Мадина Асатуллоевна; Сперанская Марина Викторовна. Промпт-инжиниринг как ключевая компетенция в образовании: сущность, особенности и подходы к оцениванию // Высшее образование в России. 2026. Том 35, номер 2. Страницы 53–73. Дата: 2026. https://doi.org/10.31992/0869-3617-2026-35-2-53-73 — VERIFIED-FULLTEXT. Ключ в материалах курса: Н12.

[58] Ronald K. Mitchell; Bradley R. Agle; Donna J. Wood. Toward a Theory of Stakeholder Identification and Salience: Defining the Principle of Who and What Really Counts // Academy of Management Review. 1997. Volume 22, Number 4. Pages 853–886. Дата: октябрь 1997. https://www.jstor.org/stable/259247 — VERIFIED-FULLTEXT. Ключ в материалах курса: С1.

[59] R. Edward Freeman; цитата приведена по статье Ronald K. Mitchell, Bradley R. Agle, Donna J. Wood. Strategic Management: A Stakeholder Approach. Boston: Pitman, 1984, цитируется по: Toward a Theory of Stakeholder Identification and Salience // Academy of Management Review. 1997. Page 854. Дата: 1984 (книга); 1997 (вторичный источник). https://www.jstor.org/stable/259247 — VERIFIED-SECONDARY. Ключ в материалах курса: С2.

[60] Richard L. Daft; Robert H. Lengel. Organizational Information Requirements, Media Richness and Structural Design // Management Science. 1986. Volume 32, Number 5. Pages 554–571. Дата: май 1986. https://doi.org/10.1287/mnsc.32.5.554 — VERIFIED-FULLTEXT. Ключ в материалах курса: С3.

[61] A. W. van den Ban (полное имя в источнике не раскрыто, только инициалы). A Revision of the Two-Step Flow of Communications Hypothesis // Gazette (International Journal for Mass Communication Studies). 1964. Volume 10, Number 3. Pages 237–249 (страница по перепечатке в хрестоматии). Дата: 1964. https://edepot.wur.nl/21986 — VERIFIED-FULLTEXT. Ключ в материалах курса: С4.

[62] Paul F. Lazarsfeld; Bernard Berelson; Hazel Gaudet; цитата приведена по A. W. van den Ban. The People's Choice: How the Voter Makes Up His Mind in a Presidential Campaign. 2nd edition. New York: Columbia University Press, 1948, page 151, цитируется по: A Revision of the Two-Step Flow of Communications Hypothesis, 1964. Дата: 1948 (2-е издание; 1-е издание 1944). https://edepot.wur.nl/21986 — VERIFIED-SECONDARY. Ключ в материалах курса: С4a.

[63] Elihu Katz; цитата приведена по A. W. van den Ban. The Two-Step Flow of Communication: An Up-To-Date Report on an Hypothesis // Public Opinion Quarterly. 1957. Volume 21, Number 1. Pages 61–78, цитируется по: A Revision of the Two-Step Flow of Communications Hypothesis, 1964 (точная страница не установлена). Дата: 1957. https://edepot.wur.nl/21986 — VERIFIED-SECONDARY. Ключ в материалах курса: С4b.

[64] Marianne Eisenmann; John Gilfeather; в руководство входит отредактированная статья Brad L. Rawlins (2006). Identifying and Prioritizing Stakeholders for Public Relations — A Guide for Students and Practitioners. Gainesville, Florida: Institute for Public Relations, 2023. Дата: май 2023. https://instituteforpr.org/wp-content/uploads/Stakeholder-Identification-and-Prioritization-FINAL-May-2023.pdf — VERIFIED-FULLTEXT. Ключ в материалах курса: С5.

[65] James E. Grunig; Fred C. Repper; цитата приведена по руководству Marianne Eisenmann, John Gilfeather. Strategic Management, Publics, and Issues // Excellence in Public Relations and Communication Management / edited by James E. Grunig. Hillsdale, New Jersey: Lawrence Erlbaum Associates, 1992, page 128, цитируется по: Identifying and Prioritizing Stakeholders for Public Relations — A Guide for Students and Practitioners. Gainesville, Florida: Institute for Public Relations, 2023, page 5. Дата: 1992. https://instituteforpr.org/wp-content/uploads/Stakeholder-Identification-and-Prioritization-FINAL-May-2023.pdf — VERIFIED-SECONDARY. Ключ в материалах курса: С5a.

[66] Завгородняя Марина Юрьевна. Место Пола Лазарсфельда в науке: современное применение концепций // Власть. 2026. Том 34, номер 1. Страницы 195–199. Дата: 2026. https://www.jour.fnisc.ru/index.php/vlast/article/view/11077 — VERIFIED-FULLTEXT. Ключ в материалах курса: С6.

[67] Джонек-Ковальска И. (Izabela Jonek-Kowalska — вероятно, но связь с этой статьёй не подтверждена; полное имя в открытых источниках не установлено); Пономаренко Татьяна Владимировна; Маринина Оксана Анатольевна. Проблемы взаимодействия со стейкхолдерами при реализации долгосрочных горных проектов // Записки Горного института. 2018. Том 232. Страницы 428–437. Дата: август 2018. https://doi.org/10.31897/PMI.2018.4.428 — VERIFIED-FULLTEXT. Ключ в материалах курса: С7.

[68] Плахин Андрей Евгеньевич. Картирование стейкхолдеров промышленных парковых структур Уральского региона // Управленец. 2018. Том 9, номер 4. Страницы 84–92. Дата: 2018. https://doi.org/10.29141/2218-5003-2018-9-4-9 — VERIFIED-FULLTEXT. Ключ в материалах курса: С8.

[69] Моисеенкова Ю. А. (полное имя в открытых источниках не установлено). Стандартизация как инструмент развития партнерства бизнеса с заинтересованными сторонами // Информационно-экономические аспекты стандартизации и технического регулирования. 2025. Номер 6 (87). Дата: 2025. https://iea.gostinfo.ru/article/view/85 — VERIFIED-FULLTEXT. Ключ в материалах курса: С9.

[70] Linton C. Freeman. Centrality in Social Networks: Conceptual Clarification // Social Networks. 1978–1979. Volume 1. Pages 215–239. Дата: 1978/1979. https://www.bebr.ufl.edu/sites/default/files/Centrality%20in%20Social%20Networks.pdf — VERIFIED-FULLTEXT. Ключ в материалах курса: Д3-Т3.

[71] Ronald S. Burt. Structural Holes versus Network Closure as Social Capital // Social Capital: Theory and Research / edited by Nan Lin, Karen S. Cook, Ronald S. Burt. New York: Aldine de Gruyter, 2001 (препринт 2000). Дата: 2000 (препринт главы; книга 2001). https://snap.stanford.edu/class/cs224w-readings/burt00capital.pdf — VERIFIED-FULLTEXT. Ключ в материалах курса: Д3-Т4.

[72] Meeyoung Cha; Hamed Haddadi; Fabrício Benevenuto; Krishna P. Gummadi. Measuring User Influence in Twitter: The Million Follower Fallacy // Proceedings of the Fourth International AAAI Conference on Weblogs and Social Media (Association for the Advancement of Artificial Intelligence). 2010. Дата: 2010. https://snap.stanford.edu/class/cs224w-readings/cha10influence.pdf — VERIFIED-FULLTEXT. Ключ в материалах курса: Д3-Т5.

[73] Johannes Itten. Arte del color: aproximación subjetiva y descripción objetiva del arte. Edición abreviada. París: Editorial Bouret (сокращённое испанское издание книги Kunst der Farbe, 1961). Дата: испанское сокращённое издание, год в скане не найден; немецкий оригинал 1961. https://archive.org/details/LaHistoriaInterminable — VERIFIED-FULLTEXT. Ключ в материалах курса: О1.

[74] Поступаева Надежда Васильевна. Сложности определения цветотипа внешности // Инновационная наука. 2021. Номер 3. Страницы 157–160. Дата: 2021. https://cyberleninka.ru/article/n/slozhnosti-opredeleniya-tsvetotipa-vneshnosti — VERIFIED-FULLTEXT. Ключ в материалах курса: О3.

[75] Heinrich Wölfflin; переводчик M. D. Hottinger. Principles of Art History: The Problem of the Development of Style in Later Art / translated by M. D. Hottinger from the 7th German edition. New York: Dover Publications, [1950] (оригинал: Kunstgeschichtliche Grundbegriffe, 1915). Дата: английское издание [1950]; немецкий оригинал 1915. https://archive.org/details/princarth00wlff — VERIFIED-FULLTEXT. Ключ в материалах курса: О4.

[76] Шинкарёва Майя Изяславовна. Понятие «живописное» Г. Вёльфлина применительно к искусству полифонии XVII века // Вестник Московского государственного университета культуры и искусств. 2008. Номер 6. Страницы 256–258. Дата: 2008. https://cyberleninka.ru/article/n/ponyatie-zhivopisnoe-g-vyolflina-primenitelno-k-iskusstvu-polifonii-xvii-veka — VERIFIED-FULLTEXT. Ключ в материалах курса: О5.

[77] Серова О. (автор статьи; полное имя в цитируемом тексте не раскрыто) — о Беляевой-Экземплярской Софье Николаевне. Софья Николаевна Беляева-Экземплярская — выпускница Московских высших женских курсов // Развитие личности. 2012. Номер 2. Дата: 2012. https://cyberleninka.ru/article/n/sofya-nikolaevna-belyaeva-ekzemplyarskaya-vypusknitsa-mvzhk — VERIFIED-FULLTEXT (статья о книге; текст самой книги 1934 года не проверен). Ключ в материалах курса: О6.

[78] Шипков Олег (отчество: полное имя в открытых источниках не установлено). Зрительный эффект членения поверхности // Геометрия и графика. 2017. Том 5, номер 4. Страницы 68–72. Дата: декабрь 2017. https://zh-szf.ru/en/nauka/article/19053/jats — VERIFIED-FULLTEXT (аннотация). Ключ в материалах курса: О7.

[79] Antonis Koutsoumpis; Elias Economou; Erik van der Burg. Helmholtz Versus Haute Couture: How Horizontal Stripes and Dark Clothes Make You Look Thinner // Perception. 2021. Volume 50, Number 9. Дата: август 2021. https://doi.org/10.1177/03010066211038158 — VERIFIED-FULLTEXT. Ключ в материалах курса: О8.

[80] Tanya L. Chartrand; John A. Bargh. The Chameleon Effect: The Perception–Behavior Link and Social Interaction // Journal of Personality and Social Psychology. 1999. Volume 76, Number 6. Pages 893–910. Дата: 1999. https://doi.org/10.1037/0022-3514.76.6.893 — VERIFIED-FULLTEXT. Ключ в материалах курса: О9.

[81] Jordan Soliz; Howard Giles. Relational and Identity Processes in Communication: A Contextual and Meta-Analytical Review of Communication Accommodation Theory // Annals of the International Communication Association (Communication Yearbook 38). 2014. Volume 38, Number 1. Pages 107–144. Дата: 2014. https://doi.org/10.1080/23808985.2014.11679160 — VERIFIED-ABSTRACT. Ключ в материалах курса: О10.

[82] Judee K. Burgoon. A Communication Model of Personal Space Violations: Explication and an Initial Test // Human Communication Research. 1978. Volume 4, Number 2. Pages 129–142. Дата: 1978. https://doi.org/10.1111/j.1468-2958.1978.tb00603.x — VERIFIED-SECONDARY (аннотация через OpenAlex). Ключ в материалах курса: О11.

[83] Judee K. Burgoon; Jerold L. Hale. Nonverbal Expectancy Violations: Model Elaboration and Application to Immediacy Behaviors // Communication Monographs. 1988. Volume 55, Number 1. Pages 58–79. Дата: 1988. https://doi.org/10.1080/03637758809376158 — VERIFIED-SECONDARY (аннотация через OpenAlex). Ключ в материалах курса: О12.

[84] Judee K. Burgoon. Expectancy Violations Theory // The International Encyclopedia of Interpersonal Communication. Hoboken, New Jersey: Wiley, 2015. Pages 1–9. Дата: 18 июня 2015. https://doi.org/10.1002/9781118540190.wbeic102 — VERIFIED-ABSTRACT. Ключ в материалах курса: О13.

[85] Edwin P. Hollander. Conformity, Status, and Idiosyncrasy Credit // Psychological Review. 1958. Volume 65, Number 2. Pages 117–127. Дата: 1958. https://doi.org/10.1037/h0042501 — VERIFIED-SECONDARY (аннотация через OpenAlex). Ключ в материалах курса: О14.

[86] Marilynn B. Brewer. The Social Self: On Being the Same and Different at the Same Time // Personality and Social Psychology Bulletin. 1991. Volume 17, Number 5. Pages 475–482. Дата: 1991. https://doi.org/10.1177/0146167291175001 — VERIFIED-ABSTRACT. Ключ в материалах курса: О15.

[87] Janine Willis; Alexander Todorov. First Impressions: Making Up Your Mind After a 100-Ms Exposure to a Face // Psychological Science. 2006. Volume 17, Number 7. Pages 592–598. Дата: 2006. https://doi.org/10.1111/j.1467-9280.2006.01750.x — VERIFIED-ABSTRACT. Ключ в материалах курса: О16.

[88] Neil Howlett; Karen Pine; Ismail Orakçıoğlu; Ben Fletcher. The Influence of Clothing on First Impressions: Rapid and Positive Responses to Minor Changes in Male Attire // Journal of Fashion Marketing and Management. 2013. Volume 17, Number 1. Pages 38–48. Дата: 2013. https://doi.org/10.1108/13612021311305128 — VERIFIED-ABSTRACT. Ключ в материалах курса: О17.

[89] Hajo Adam; Adam D. Galinsky. Enclothed Cognition // Journal of Experimental Social Psychology. 2012. Volume 48, Number 4. Pages 918–925. Дата: 2012. https://doi.org/10.1016/j.jesp.2012.02.008 — VERIFIED-ABSTRACT. Ключ в материалах курса: О18a.

[90] C. Blaine Horton; Hajo Adam; Adam D. Galinsky. Evaluating the Evidence for Enclothed Cognition: Z-Curve and Meta-Analyses // Personality and Social Psychology Bulletin. Volume 51, Number 2. Pages 203–221. Дата: онлайн 17 июля 2023. https://doi.org/10.1177/01461672231182478 — VERIFIED-ABSTRACT. Ключ в материалах курса: О18b.

[91] Albert Mehrabian. Silent Messages — страница автора с описанием книги на сайте kaaj.com. Дата: страница автора, © 1995–2016; книга Silent Messages — 1971, 2-е издание 1981. https://www.kaaj.com/psych/smorder.html — VERIFIED-FULLTEXT. Ключ в материалах курса: О19.

[92] Erving Goffman. The Presentation of Self in Everyday Life. Garden City, New York: Doubleday Anchor Books, 1959. Дата: 1959. https://archive.org/details/the-presentation-of-self-in-everyday-life-the-presentation-erving-goffman-1959-a — VERIFIED-FULLTEXT. Ключ в материалах курса: О20.

[93] Ирвинг Гофман (Erving Goffman); переводчик Ковалев Александр Дмитриевич; научный редактор Ковалёва М. С. (полное имя в открытых источниках не установлено). Представление себя другим в повседневной жизни / перевод с английского и вступительная статья Александра Дмитриевича Ковалёва; научный редактор М. С. Ковалёва. Москва: КАНОН-пресс-Ц; Кучково поле, 2000. Дата: 2000 (русское издание). https://archive.org/details/2000_20250325 — VERIFIED-FULLTEXT. Ключ в материалах курса: О21.

[94] Шкурко Ольга Васильевна. Востребованность имиджелогического знания у будущих менеджеров // Сибирский торгово-экономический журнал. 2012. Номер 15. Дата: 2012. https://cyberleninka.ru/article/n/vostrebovannost-imidzhelogicheskogo-znaniya-u-buduschih-menedzherov — VERIFIED-FULLTEXT. Ключ в материалах курса: О22.

[95] Johannes Itten. The Art of Color: The Subjective Experience and Objective Rationale of Color. Revised edition. New York: Van Nostrand Reinhold, 1973. Глава «Subjective Timbre», страницы 24–32. Дата: английское издание 1973 (немецкий оригинал 1961). https://archive.org/details/artofcolorsubjec00itte — VERIFIED (колода v5, решение 7). Ключ в материалах курса: E-itten.

[96] Авторы справочника в материалах курса намеренно не называются (RFC v5, строка 36); издатель — «Бератор-паблишинг». Кодекс стиля. Справочник делового дресс-кода. Москва: Бератор-паблишинг, 2007. 88 страниц (технологии НИА «Гид по стилю»). Дата: 2007. https://github.com/user-attachments/files/33784962/kodeks_stilya.pdf — VERIFIED (колода v5, решение 7: сверено по PDF). Ключ в материалах курса: E-kodeks.

[97] Shigenobu Kobayashi. The Aim and Method of the Color Image Scale // Color Research & Application. 1981. Volume 6, Number 2. Pages 93–107. Дата: июнь 1981. https://doi.org/10.1002/col.5080060210 — VERIFIED (колода v5, решение 7). Ключ в материалах курса: E-kobayashi.

[98] Gabrielle K. Lehmann; Andrew J. Elliot; Robert J. Calin-Jageman. Meta-Analysis of the Effect of Red on Perceived Attractiveness // Evolutionary Psychology. 2018. Volume 16, Number 4. Дата: 1 октября 2018. https://doi.org/10.1177/1474704918802412 — VERIFIED (колода v5, решение 7). Ключ в материалах курса: E-lehmann.

[99] Аннотация издательства URSS к книге Беляевой-Экземплярской Софьи Николаевны. Моделирование одежды по законам зрительного восприятия. Издание стереотипное. Москва: URSS, 2025. 120 страниц. ISBN 978-5-9710-8597-3 — аннотация издательства. Дата: книга 1934; стереотипное издание URSS 2025. https://urss.ru/cgi-bin/db.pl?lang=Ru&blang=ru&page=Book&id=325972 — VERIFIED (колода v5, решение 7: аннотация издательства). Ключ в материалах курса: E-belyaeva.

[100] Susan L. Sokolowski; Chrissy Bettencourt. Modification of the Female Figure Identification Technique (FFIT) Form for Apparel // Proceedings of 3DBODY.TECH 2020 — 11th International Conference and Exhibition on 3D Body Scanning and Processing Technologies. Дата: 17 ноября 2020. https://doi.org/10.15221/20.22 — VERIFIED (колода v5, решение 7). Ключ в материалах курса: E-sokolowski.

[101] Peter Thompson; Kyriaki Mikellidou. Applying the Helmholtz Illusion to Fashion: Horizontal Stripes Won't Make You Look Fatter // i-Perception. 2011. Volume 2, Number 1. Pages 69–76. Дата: 2011. https://doi.org/10.1068/i0405 — VERIFIED (колода v5, решение 7). Ключ в материалах курса: E-thompson.

[102] Аннотация издательства «Эксмо» к книге Трубецковой Инессы Александровны и Найденской Наталии Георгиевны. Золотые правила стиля. Дресс-код успешной женщины. Москва: Эксмо, 2016. 256 страниц. ISBN 978-5-699-92975-7 — аннотация издательства. Дата: 30 ноября 2016 (дата выхода по странице издательства). https://eksmo.ru/book/zolotye-pravila-stilya-dress-kod-uspeshnoy-zhenshchiny-ITD816396/ — VERIFIED (колода v5, решение 7: аннотация издательства). Ключ в материалах курса: E-eksmo.

[103] Silvia Bellezza; Francesca Gino; Anat Keinan. The Red Sneakers Effect: Inferring Status and Competence from Signals of Nonconformity // Journal of Consumer Research. 2014. Volume 41, Number 1. Pages 35–54. Дата: июнь 2014 (онлайн 18 декабря 2013). https://doi.org/10.1086/674870 — VERIFIED (колода v5, решение 7). Ключ в материалах курса: E-bellezza.

[104] Georg Simmel. Fashion // American Journal of Sociology. 1957. Volume 62, Number 6. Pages 541–558. Дата: 1957 (английская публикация; немецкий оригинал 1904–1905). https://doi.org/10.1086/222102 — VERIFIED (колода v5, решение 7). Ключ в материалах курса: E-simmel.

[105] Marjorie M. Baker. Accessories: The Finishing Touch. Publication FCS2-347. Lexington: University of Kentucky Cooperative Extension Service, 2020 (первоначально подготовлено Linda M. Heaton). Дата: 2020 (пересмотренное издание, «Reviewed 11-2020»; год первого выпуска в PDF не указан). https://publications.mgcafe.uky.edu/sites/publications.ca.uky.edu/files/FCS2347.pdf — VERIFIED (колода v5, решение 7). Ключ в материалах курса: E-baker.

[106] Young Jee Han; Joseph C. Nunes; Xavier Drèze. Signaling Status with Luxury Goods: The Role of Brand Prominence // Journal of Marketing. 2010. Volume 74, Number 4. Pages 15–30. Дата: июль 2010. https://doi.org/10.1509/jmkg.74.4.015 — VERIFIED (колода v5, решение 7). Ключ в материалах курса: E-han.

[107] Helmut Leder; Michael Forster; Gernot Gerger. The Glasses Stereotype Revisited: Effects of Eyeglasses on Perception, Recognition, and Impression of Faces // Swiss Journal of Psychology. 2011. Volume 70, Number 4. Pages 211–222. Дата: декабрь 2011. https://doi.org/10.1024/1421-0185/a000059 — VERIFIED (колода v5, решение 7). Ключ в материалах курса: E-leder.
