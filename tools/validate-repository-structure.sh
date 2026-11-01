#!/usr/bin/env bash
#
# Минимальный валидатор структуры HTOM-команды («иммунная система» генома).
# Проверяет наличие базовых артефактов «ДНК-шаблона» и ловит самовольный рост
# дерева до того, как он превратится в хаос. Запускать из корня HTOM-команды:
#
#   ./tools/validate-repository-structure.sh
#
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

failures=0
warnings=0

fail() {
  printf 'FAIL: %s\n' "$1" >&2
  failures=$((failures + 1))
}

warn() {
  printf 'WARN: %s\n' "$1" >&2
  warnings=$((warnings + 1))
}

require_dir() {
  [[ -d "$1" ]] || fail "missing directory: $1"
}

require_file() {
  [[ -f "$1" ]] || fail "missing file: $1"
}

# Печатает первый существующий путь из списка кандидатов, иначе возвращает 1.
# Нормируется наличие контракта, а не его физическое размещение: HTOM-команда
# вправе держать управляющие документы в корне или вынести их в governance-каталог
# (как это сделал сам Хаб по ADR-007 / B-056).
resolve_one_of() {
  local candidate
  for candidate in "$@"; do
    if [[ -f "$candidate" ]]; then
      printf '%s\n' "$candidate"
      return 0
    fi
  done
  return 1
}

required_directories=(
  "docs/adr"
  "docs/audit"
  ".github/ISSUE_TEMPLATE"
  ".github/workflows"
  "tools"
)

required_files=(
  "AGENTS.md"
  ".hub-profile.json"
  "README.md"
  "CONTRIBUTING.md"
  "CHANGELOG.md"
  "docs/adr/.gitkeep"
  "docs/audit/.gitkeep"
  ".github/ISSUE_TEMPLATE/task.md"
  ".github/ISSUE_TEMPLATE/task-creative.md"
  ".github/workflows/validate.yml"
  "tools/validate-repository-structure.sh"
)

for dir in "${required_directories[@]}"; do
  require_dir "$dir"
done

for file in "${required_files[@]}"; do
  require_file "$file"
done

# Управляющие контракты HTOM-команды: обязательно наличие, размещение — на выбор
# команды. Порядок кандидатов задаёт приоритет разрешения при нескольких копиях.
# shellcheck disable=SC2034  # путь резолвится для сообщения об ошибке, не используется дальше
governance_contract="$(resolve_one_of \
  "AI_GOVERNANCE.md" \
  "governance/AI_GOVERNANCE.md" \
  "ai-governance/ai-governance.md")" ||
  fail "missing governance contract: ожидался один из AI_GOVERNANCE.md, governance/AI_GOVERNANCE.md, ai-governance/ai-governance.md"

quick_rules="$(resolve_one_of \
  "AI_QUICK_RULES.md" \
  "governance/AI_QUICK_RULES.md" \
  "ai-rules/ai-quick-rules.md")" ||
  fail "missing quick rules: ожидался один из AI_QUICK_RULES.md, governance/AI_QUICK_RULES.md, ai-rules/ai-quick-rules.md"

handover_prompt="$(resolve_one_of \
  "AI_SESSION_HANDOVER_PROMPT.md" \
  "governance/AI_SESSION_HANDOVER_PROMPT.md" \
  "ai-rules/AI_SESSION_HANDOVER_PROMPT.md")" ||
  fail "missing handover prompt: ожидался один из AI_SESSION_HANDOVER_PROMPT.md, governance/AI_SESSION_HANDOVER_PROMPT.md, ai-rules/AI_SESSION_HANDOVER_PROMPT.md"

# Handover Prompt должен оставаться параметризованным ({{REPO_NAME}}), чтобы
# «доверенность» переносилась в любую HTOM-команду без правок (см. AI_SESSION_HANDOVER_PROMPT.md).
if [[ -n "${handover_prompt:-}" ]] && ! grep -Fq '{{REPO_NAME}}' "$handover_prompt"; then
  fail "$handover_prompt must keep the {{REPO_NAME}} placeholder"
fi

# Управляющие контракты не должны существовать в двух местах одновременно:
# два дома означают два SSOT и расхождение при первой же правке.
for pair in \
  "AI_GOVERNANCE.md:governance/AI_GOVERNANCE.md:ai-governance/ai-governance.md" \
  "AI_QUICK_RULES.md:governance/AI_QUICK_RULES.md:ai-rules/ai-quick-rules.md" \
  "AI_SESSION_HANDOVER_PROMPT.md:governance/AI_SESSION_HANDOVER_PROMPT.md:ai-rules/AI_SESSION_HANDOVER_PROMPT.md"; do
  IFS=':' read -r -a candidates <<<"$pair"
  found=()
  for candidate in "${candidates[@]}"; do
    if [[ -f "$candidate" ]]; then
      found+=("$candidate")
    fi
  done
  if [[ "${#found[@]}" -gt 1 ]]; then
    fail "duplicate governance contract: ${found[*]} — оставьте ровно одно размещение"
  fi
done

# --- Классификация каталогов верхнего уровня (RFC v0.2, issue #535) ----------
#
# Каталог HTOM-команды принадлежит ровно одному из четырёх классов:
#
#   1. канонический      — из структуры генома (список canonical_directories);
#   2. специфичный       — бизнес-логика и доменные данные проекта; легитимен
#                          только если явно задекларирован в .hub-profile.json
#                          (поле project_specific_directories);
#   3. переходный        — не канонический и не задекларированный: остаток
#                          реструктуризации (limbo state), это ошибка;
#   4. архивный          — .archive/, легитимен при наличии README.md с причиной.
#
# Правило существует, чтобы реструктуризация не теряла ценные каталоги проекта
# (класс 2 сохраняется по декларации) и одновременно не накапливала «мусорные»
# переходные каталоги (класс 3 виден машине, а не только человеку на ревью).

PROFILE_FILE=".hub-profile.json"

# The bootstrap contract is shared with the Hub and copied into generated
# repositories by Smart Sync. Read the profile before classifying directories.
bootstrap_validator="tools/validate-agents-bootstrap.sh"
if [[ -x "$bootstrap_validator" ]]; then
  "$bootstrap_validator" "$ROOT_DIR" || failures=$((failures + 1))
fi

canonical_directories=(
  ".git"
  ".github"
  "docs"
  "tools"
  "governance"
  "ai-governance"
  "ai-rules"
)

# Читает из .hub-profile.json декларации специфичных каталогов и льготный срок.
# Формат вывода: строки "declared<TAB>path", "invalid<TAB>path", "grandfather<TAB>date".
read_profile() {
  local py=""
  if command -v python3 >/dev/null 2>&1; then
    py="python3"
  elif command -v python >/dev/null 2>&1; then
    py="python"
  else
    return 2
  fi
  "$py" - "$PROFILE_FILE" <<'PYEOF'
import json, sys
try:
    with open(sys.argv[1], encoding="utf-8") as fh:
        profile = json.load(fh)
except Exception as exc:  # noqa: BLE001 - сообщение уходит в валидатор как FAIL
    print("error\t%s" % exc)
    sys.exit(0)
archetype = profile.get("archetype")
if archetype not in {"A", "B", "C", "D"}:
    print("error\tarchetype must be one of A, B, C, D")
environment = profile.get("environment", "local")
if environment not in {"local", "gigacode", "serverless"}:
    print("error\tenvironment must be one of local, gigacode, serverless")
else:
    print("environment\t%s" % environment)
secondary = profile.get("secondary_environments", []) or []
if not isinstance(secondary, list) or any(value not in {"local", "gigacode", "serverless"} for value in secondary):
    print("error\tsecondary_environments contains an unknown value")
until = profile.get("structure_grandfather_until")
if until:
    print("grandfather\t%s" % until)
for entry in profile.get("project_specific_directories", []) or []:
    if isinstance(entry, str):
        # Строка без причины — декларация без обоснования: не принимается.
        print("invalid\t%s" % entry)
        continue
    path = (entry.get("path") or "").strip().strip("/")
    reason = (entry.get("reason") or "").strip()
    if not path or not reason:
        print("invalid\t%s" % (path or "<empty>"))
        continue
    print("declared\t%s" % path)
PYEOF
}

declared_directories=()
grandfather_until=""
profile_environment="local"
profile_readable=1

if [[ -f "$PROFILE_FILE" ]]; then
  profile_output="$(read_profile)" || profile_readable=0
  if [[ "$profile_readable" -eq 1 ]]; then
    while IFS=$'\t' read -r kind value; do
      [[ -n "$kind" ]] || continue
      case "$kind" in
        declared) declared_directories+=("$value") ;;
        grandfather) grandfather_until="$value" ;;
        environment) profile_environment="$value" ;;
        invalid)
          fail "$PROFILE_FILE: декларация каталога '$value' неполна — нужны непустые поля path и reason"
          ;;
        error)
          fail "$PROFILE_FILE не разбирается как JSON: $value"
          ;;
      esac
    done <<<"$profile_output"
  else
    warn "python не найден: декларации $PROFILE_FILE не проверены, классификация каталогов пропущена."
  fi
fi

# Environment deltas are additive. Local has no extra surface; provider
# adapters remain pointers and are never treated as copies of Hub rules.
case "$profile_environment" in
  local) ;;
  gigacode) canonical_directories+=(".gigacode") ;;
  serverless) canonical_directories+=(".serverless") ;;
esac

in_list() {
  local needle="$1"
  shift
  local item
  for item in "$@"; do
    [[ "$item" == "$needle" ]] && return 0
  done
  return 1
}

# Льготный период (grandfathering): существующие специфичные каталоги не ломают
# CI сразу, но обязаны быть задекларированы до указанной даты — один цикл
# синхронизации. После даты недекларированный каталог становится FAIL.
grandfather_active=0
if [[ -n "$grandfather_until" ]]; then
  today="$(date -u +%F)"
  if [[ "$today" < "$grandfather_until" || "$today" == "$grandfather_until" ]]; then
    grandfather_active=1
  fi
fi

if [[ "$profile_readable" -eq 1 ]]; then
  while IFS= read -r dir; do
    name="${dir#./}"
    [[ -n "$name" && "$name" != "." ]] || continue
    in_list "$name" "${canonical_directories[@]}" && continue
    [[ "$name" == ".archive" ]] && continue
    if in_list "$name" ${declared_directories[@]+"${declared_directories[@]}"}; then
      continue
    fi
    message="недекларированный каталог: $name/ — он не входит в каноническую структуру генома. Либо задекларируйте его как специфичный для проекта в $PROFILE_FILE (project_specific_directories: path + reason), либо перенесите содержимое в канонический дом, либо перенесите каталог в .archive/ с README.md. Переходные каталоги (limbo state) не сохраняются."
    if [[ "$grandfather_active" -eq 1 ]]; then
      warn "$message (льготный период до $grandfather_until)"
    else
      fail "$message"
    fi
  done < <(find . -maxdepth 1 -type d ! -name '.')

  # Декларация, потерявшая свой каталог, — мёртвая запись конфигурации.
  for declared in ${declared_directories[@]+"${declared_directories[@]}"}; do
    if [[ ! -d "$declared" ]]; then
      warn "$PROFILE_FILE декларирует каталог '$declared', которого нет в репозитории — удалите запись."
    fi
  done
fi

# Архив легитимен, но обязан объяснять себя: README.md с причиной архивации.
if [[ -d ".archive" ]] && [[ ! -f ".archive/README.md" ]]; then
  fail ".archive/ существует без README.md: архив обязан объяснять, что и почему в нём лежит."
fi

# Negative check: research/ по умолчанию не создаётся в HTOM-команде.
# Фундаментальные знания живут в research/ Хаба. Если папка появилась — это
# должно быть осознанным решением, зафиксированным как ADR (см. AI_QUICK_RULES.md).
if [[ -d "research" ]]; then
  warn "research/ найдена в HTOM-команде: по умолчанию её быть не должно. Зафиксируйте отклонение как ADR в docs/adr/ или вынесите знания в research/ Хаба."
fi

# Незаменённые плейсхолдеры шаблона: подсказка запустить init (если он ещё есть).
# Паттерн — регулярка, а не точный токен, чтобы init.sh не переписал эту проверку.
if grep -RIlq '{{[a-z_][a-z_]*}}' . --include='*.md' 2>/dev/null; then
  warn "найдены незаменённые плейсхолдеры шаблона ({{...}}): запустите ./init.sh для инициализации HTOM-команды."
fi

if [[ "$warnings" -gt 0 ]]; then
  printf '\n%d warning(s) — не блокируют, но требуют внимания.\n' "$warnings" >&2
fi

if [[ "$failures" -gt 0 ]]; then
  printf '\nHTOM-team structure validation failed with %d issue(s).\n' "$failures" >&2
  exit 1
fi

printf 'HTOM-team structure validation passed.\n'
