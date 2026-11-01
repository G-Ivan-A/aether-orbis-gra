---
status: draft
version: 0.5
updated: 2026-11-01
temperature: 0.1
---

# AI Governance - aether-orbis-gra

Операционный контракт для AI-assisted work в HTOM-команде `aether-orbis-gra`
(HTOM = Hybrid Team Operating Model: гибридная работа человека и ИИ-агентов).

Этот файл - **ядро генома** HTOM-команды: обязателен в корне (жёсткое
ограничение). Он определяет, кто принимает решения, что делает ИИ и где проходят
границы. HTOM-команда наследует правила Хаба и при конфликте ссылается на
источник истины: [https://github.com/G-Ivan-A/hybrid-Intelligence-lab](https://github.com/G-Ivan-A/hybrid-Intelligence-lab) (Хаб `hybrid-Intelligence-lab`,
документ `AI_GOVERNANCE.md`). Команда не дублирует знания Хаба, а ссылается на
них.

Хаб является источником рекомендаций, reusable governance-практик, стандартов и
шаблонов. Он не является механическим блокером локальной работы: команда может
адаптировать рекомендацию под свой риск и контекст, если решение явно
зафиксировано в PR, ADR или audit.

## Роли

| Роль | Ответственность |
| --- | --- |
| Пользователь | Vision, priorities, publication boundaries и финальные решения по проекту. |
| Human reviewer | Проверяет структуру, источники, риски и полезность до merge или публикации. |
| Contributor | Создаёт issues, artifacts и pull requests внутри модели проекта. |
| AI agent | Готовит черновики, проверки и summaries внутри scope issue и правил этого контракта. |

## Правила

1. Работа начинается с issue или явного maintainer request.
2. AI agents читают issue, последние comments, relevant files и текущий PR
   context до изменения файлов.
3. AI agents могут предлагать структуру, но humans принимают финальные решения
   по vision, publication, license и sensitive context.
4. Claims, влияющие на решения, связываются с sources, experiments, issues, PRs
   или ADR в `docs/adr/`.
5. Secrets, private client data, credentials и несанитизированные
   production-промпты не коммитятся.
6. Малые reviewable pull requests предпочтительнее широких undocumented rewrites.
7. Структура HTOM-команды не растёт "на вырост": новый каталог создаётся только
   при доказанной операционной боли (Anti-Inflation principle Хаба).
8. Markdown-артефакты используют минимальный frontmatter Хаба:
   `status`, `version`, `updated`, `temperature`.

## Границы действий

Три корзины разрешений прозой (без YAML-манифеста и машинерии - это `ОТЛОЖИТЬ`
до первого инцидента):

- **Можно без спроса** - готовить черновики artifacts, summaries и проверки в
  рамках открытого issue; читать issue, comments и relevant files; предлагать
  структуру в pull request.
- **Можно с апрувом** - публиковать изменения через merge или публикацию,
  менять навигацию и ссылки на Хаб, создавать новый каталог при доказанной
  операционной боли (всё - после human review).
- **Нельзя никогда** - коммитить secrets, private client data, credentials или
  несанитизированные production-промпты; принимать за человека финальные решения
  по vision, license и publication.

## Operating Modes

Канонический словарь Хаба и принципы автономии задаёт
[`ADR-010`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/adr/2026-08-adr-010-agent-autonomy-principles.md).
Локальные `Research` ниже — task profile, а не режим Хаба; миграцию словаря
нужно оформить отдельным human-reviewed решением команды.

| Mode | Когда использовать |
| --- | --- |
| Structured | По умолчанию для структуры проекта, governance и tooling. |
| Creative | Для задач с заданной целью и свободой выбора структуры, prompt/process/context решений или governance-синтеза. |
| Research | Для source-backed analysis (фундаментальные знания - вкладом в `research/` Хаба, а не в команду). |

## Обоснованный обход в Creative Mode

Structured mode работает fail-closed: если действие не описано правилами или
контекст противоречив, агент останавливается и зовёт человека.

Creative mode допускает обоснованный обход рекомендации Хаба, когда это нужно
для цели задачи и не нарушает hard bans. Обход должен быть минимальным и
записанным: какое правило обойдено, почему, какой артефакт изменён, чем
проверено решение. Если обход меняет архитектуру или governance-практику
команды, фиксируйте ADR в `docs/adr/`.

## Специфика работы с AI-агентами

- Каждый запуск агента - новая сессия; нужный контекст должен быть в issue,
  PR, handover prompt или summary.
- Comments и CI после остановки сессии не отслеживаются автоматически.
- Comment + manual restart = итерация; merge = принято; close = отклонено или
  отменено.
- Агент не заполняет пустые поля задачи выдуманными значениями.

## Эскалация

Перед продолжением нужно запросить human guidance, если:

- требования противоречат друг другу или правилу Хаба;
- изменение публикует sensitive или private information;
- от HTOM-команды требуют создать `research/` или иной "выключенный ген" по умолчанию
  (см. `AI_QUICK_RULES.md`): назови правило и его источник, предложи легитимную
  альтернативу, а осознанное отклонение зафиксируй как ADR в `docs/adr/`;
- Creative override затрагивает hard bans, publication, license, security или
  права на пользовательский контент;
- AI agent не может проверить важное claim или migration decision.

## Definition of Done

Для AI-assisted изменений в HTOM-команде:

- активные файлы находятся в ожидаемых каталогах;
- навигация и ссылки на Хаб обновлены;
- значимое изменение отражено в `CHANGELOG.md` (`## Unreleased`);
- Creative override, если был, записан в PR, ADR или audit;
- `./tools/validate-repository-structure.sh` проходит (exit code 0);
- PR description объясняет implementation, validation и remaining risks.
