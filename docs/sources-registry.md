---
status: draft
version: 0.2
updated: 2026-11-09
temperature: 0.1
type: registry
---

# Реестр источников

> Внешние источники, на которые опирается документация L1–L4. Источники
> исследовательской модели и курса (коды вида `[650:Г1]`, `[R:Lakatos]`)
> перечислены в
> [50-open-research.md §6](../methodology/research-program/50-open-research.md#6-источники).
> Правило: утверждение о внешней практике без источника записывается как пробел.

## Проектные источники

| Код | Источник | Роль |
| --- | --- | --- |
| P-HUB | Хаб hybrid-Intelligence-lab, каталог `research/reputation-technologies`, снимок [32b5fa5](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/32b5fa524e542af23c1a8e67c919bd66d5f4e399/research/reputation-technologies) | Исходные материалы переноса; практики оформления |
| P-ISSUE | [Issue #1 этого репозитория](https://github.com/G-Ivan-A/aether-orbis-gra/issues/1) и приложенная переписка автора | Постановка; высказывания автора об истории |
| P-TG | [Страница курса на сайте Технограда](https://technograd.moscow/event_page_new?669#programm_event) | Опубликованная программа курса |
| P-AO | [Aether Orbis](https://github.com/G-Ivan-A/aether-orbis) | Родственный проект экосистемы |

## Стандарты и индустриальные практики

| Код | Источник | Где используется |
| --- | --- | --- |
| S-ISO-G2 | ISO/IEC Guide 2:2004. Standardization and related activities — General vocabulary | Что такое стандарт ([ADR-002](adr/2026-11-adr-002-methodology-form-and-l1-l4-structure.md)) |
| S-ISO-20671 | ISO 20671-1:2021. Brand evaluation — Part 1: Principles and fundamentals | Критерии качества метода |
| S-ISO-10668 | ISO 10668:2010. Brand valuation — Requirements for monetary brand valuation | Позиционирование |
| S-ISO-42010 | ISO/IEC/IEEE 42010:2022. Software, systems and enterprise — Architecture description | Структура раннего черновика стандарта (история) |
| S-AMEC-IEF | AMEC (2016). Integrated Evaluation Framework. <https://amecorg.com/amecframework/> | Позиционирование |
| S-BP | AMEC (2020). Barcelona Principles 3.0. <https://amecorg.com/resources/barcelona-principles-3-0/>; Barcelona Principles 4.0 (2025). Семь принципов версии 3.0: (1) цели — предпосылка планирования и оценки; (2) измерять результаты коммуникаций (outputs), изменения (outcomes) и возможное влияние (impact); (3) изменения и влияние определяются для стейкхолдеров, общества и организации; (4) качественный и количественный анализ; (5) AVE — не ценность коммуникаций; (6) все значимые онлайн- и офлайн-каналы; (7) целостность и прозрачность | Критерии качества метода |
| S-REPTRAK | Fombrun, C. J., Ponzi, L. J., & Newburry, W. (2015). Stakeholder tracking and analysis: The RepTrak® system for measuring corporate reputation. *Corporate Reputation Review*, 18(1), 3–24 | Позиционирование; кандидат в компонент M4 |
| S-PROV | W3C (2013). PROV-O: The PROV Ontology. W3C Recommendation | Provenance |
| S-AJP | NATO. AJP-2.1, Allied Joint Doctrine for Intelligence Procedures — оценка надёжности источника (A–F) и достоверности сведения (1–6), известная как «адмиралтейская» шкала | Шкалы слоя данных |
| S-CODES | Кодексы профессиональной этики: AMEC; IPRA Code of Conduct; CIPR Code of Conduct | Этика ([L3](methodology.md#этика-и-защита-данных)) |
| S-GDPR | Регламент (ЕС) 2016/679 (GDPR), ст. 6, 14, 35, 89 | Защита данных в партнёрских исследованиях |
| S-152FZ | Федеральный закон от 27.07.2006 № 152-ФЗ «О персональных данных», ст. 10.1 | Защита данных: персональные данные, разрешённые субъектом для распространения |

## Методология исследований

| Код | Источник |
| --- | --- |
| M-MS | March, S. T., & Smith, G. F. (1995). Design and natural science research on information technology. *Decision Support Systems*, 15(4), 251–266 |
| M-HEV | Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly*, 28(1), 75–105 |
| M-PEF | Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems*, 24(3), 45–77 |
| M-LAK | Lakatos, I. (1978). *The Methodology of Scientific Research Programmes*. Cambridge University Press |
| M-KRI | Krippendorff, K. (2018). *Content Analysis: An Introduction to Its Methodology* (4th ed.). SAGE — надёжность разметки (K2) |
| M-ROB | Robins, G., Pattison, P., Kalish, Y., & Lusher, D. (2007). An introduction to exponential random graph (p*) models for social networks. *Social Networks*, 29(2), 173–191 — ERGM |
| M-SNI | Snijders, T. A. B., van de Bunt, G. G., & Steglich, C. E. G. (2010). Introduction to stochastic actor-based models for network dynamics. *Social Networks*, 32(1), 44–60 — SAOM |

## Научные линии конструктов

| Код | Источник | Понятие GRA |
| --- | --- | --- |
| N-FRE | Freeman, L. C. (1978). Centrality in social networks: Conceptual clarification. *Social Networks*, 1(3), 215–239 | Масса (M3) |
| N-WF | Wasserman, S., & Faust, K. (1994). *Social Network Analysis: Methods and Applications*. Cambridge University Press | Масса, связи |
| N-BP | Brin, S., & Page, L. (1998). The anatomy of a large-scale hypertextual Web search engine. *Computer Networks and ISDN Systems*, 30(1–7), 107–117 | Масса (M3) |
| N-BURT | Burt, R. S. (1992). *Structural Holes: The Social Structure of Competition*. Harvard University Press | Масса (посредничество) |
| N-FOM | Fombrun, C. J. (1996). *Reputation: Realizing Value from the Corporate Image*. Harvard Business School Press | Масса (M4) |
| N-BOS | Boschma, R. (2005). Proximity and innovation: A critical assessment. *Regional Studies*, 39(1), 61–74 | Дистанция |
| N-HEI | Heider, F. (1946). Attitudes and cognitive organization. *The Journal of Psychology*, 21(1), 107–112 | Полярность |
| N-CH | Cartwright, D., & Harary, F. (1956). Structural balance: A generalization of Heider's theory. *Psychological Review*, 63(5), 277–293 | Полярность |
| N-LES | Leskovec, J., Huttenlocher, D., & Kleinberg, J. (2010). Signed networks in social media. *Proceedings of CHI 2010*, 1361–1370 | Полярность |
| N-MCP | McPherson, M., Smith-Lovin, L., & Cook, J. M. (2001). Birds of a feather: Homophily in social networks. *Annual Review of Sociology*, 27, 415–444 | Магнетизм |
| N-STE | Stewart, J. Q. (1948). Demographic gravitation: Evidence and applications. *Sociometry*, 11(1/2), 31–58 | Гравитация |
| N-TIN | Tinbergen, J. (1962). *Shaping the World Economy*. Twentieth Century Fund | Гравитация |
| N-BA | Barabási, A.-L., & Albert, R. (1999). Emergence of scaling in random networks. *Science*, 286(5439), 509–512 | Гравитация, инерция массивных узлов (R7) |
| N-MER | Merton, R. K. (1968). The Matthew effect in science. *Science*, 159(3810), 56–63 | Накопленное преимущество (R7) |
| N-SIM | Simini, F., González, M. C., Maritan, A., & Barabási, A.-L. (2012). A universal model for mobility and migration patterns. *Nature*, 484, 96–100 | Гипотеза H5 |
| N-KL | Katz, E., & Lazarsfeld, P. F. (1955). *Personal Influence*. Free Press | Информационные поля |
| N-ROG | Rogers, E. M. (2003). *Diffusion of Innovations* (5th ed.). Free Press | Информационные поля |
| N-FRE84 | Freeman, R. E. (1984). *Strategic Management: A Stakeholder Approach*. Pitman | Узлы, контуры |
| N-MAW | Mitchell, R. K., Agle, B. R., & Wood, D. J. (1997). Toward a theory of stakeholder identification and salience. *Academy of Management Review*, 22(4), 853–886 | Узлы |
| N-MEN | Mendelow, A. L. (1981). Environmental scanning: The impact of the stakeholder concept. *ICIS 1981 Proceedings* | Узлы (power–interest) |
| N-MDS | Mayer, R. C., Davis, J. H., & Schoorman, F. D. (1995). An integrative model of organizational trust. *Academy of Management Review*, 20(3), 709–734 | Дистанция (D3) |
| N-HG | Hon, L. C., & Grunig, J. E. (1999). *Guidelines for Measuring Relationships in Public Relations*. Institute for Public Relations | Отношения организации и стейкхолдеров; базовая линия |
| N-LB | Ledingham, J. A., & Bruning, S. D. (1998). Relationship management in public relations: Dimensions of an organization-public relationship. *Public Relations Review*, 24(1), 55–65 | Отношения организации и стейкхолдеров |
| N-YT | Yang, A., & Taylor, M. (2015). Looking over, looking out, and moving forward: Positioning public relations in theorizing organizational network ecologies. *Communication Theory*, 25(1), 91–115 | Сетевой подход к связям с общественностью |
| N-JOS | Jøsang, A., Ismail, R., & Boyd, C. (2007). A survey of trust and reputation systems for online service provision. *Decision Support Systems*, 43(2), 618–644 | Вычисление доверия |
| N-EIG | Kamvar, S. D., Schlosser, M. T., & Garcia-Molina, H. (2003). The EigenTrust algorithm for reputation management in P2P networks. *Proceedings of WWW 2003*, 640–651 | Вычисление доверия |

## Прикладные исследования

Прикладные источники Академии ПСБ по issue #7 (N01–N20) ведутся в
[реестре evidence](../experiments/issue-7/evidence.json) и
[записке с локаторами](analysis/2026-11-09-issue-7-academy-decision-makers.md).
Это открытые свидетельства об организации и профессиональных функциях,
не научные основания или валидация GRA; ограничения каждого источника
размечены отдельно.

## Пробелы

- Barcelona Principles 4.0: в реестре указан год; постоянная ссылка на текст
  не зафиксирована.
- Сетевые исследования в связях с общественностью (в том числе работы
  Sommerfeldt и коллег) ещё не разобраны; обзор литературы — шаг A2b
  [дорожной карты](roadmap.md).
- Проприетарные детали методик RepTrak и коммерческих платформ мониторинга не
  анализировались.
