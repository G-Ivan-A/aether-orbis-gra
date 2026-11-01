#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
agents_file="$ROOT_DIR/AGENTS.md"
profile_file="$ROOT_DIR/.hub-profile.json"

fail() {
  printf 'ERROR: %s\n' "$1" >&2
  exit 1
}

[[ -f "$agents_file" ]] || fail "missing file: AGENTS.md"
[[ -f "$profile_file" ]] || fail "missing file: .hub-profile.json"

profile_error="$(mktemp)"
trap 'rm -f "$profile_error"' EXIT
if ! profile_values="$(python3 - "$profile_file" 2>"$profile_error" <<'PY'
import json
import os
import sys

with open(sys.argv[1], encoding="utf-8") as source:
    profile = json.load(source)
archetype = profile.get("archetype")
if archetype not in {"A", "B", "C", "D"}:
    raise SystemExit("archetype must be one of: A, B, C, D")
allowed = {"local", "gigacode", "serverless"}
environment = profile.get("environment", "local")
if environment not in allowed:
    raise SystemExit("environment must be one of: local, gigacode, serverless")
secondary = profile.get("secondary_environments", [])
if not isinstance(secondary, list) or any(item not in allowed for item in secondary):
    raise SystemExit("secondary_environments contains an unknown value")
declared = profile.get("project_specific_directories", [])
if not isinstance(declared, list):
    raise SystemExit("project_specific_directories must be an array")
for item in declared:
    path = item.get("path") if isinstance(item, dict) else None
    reason = item.get("reason") if isinstance(item, dict) else None
    if not isinstance(path, str) or not path.strip() or os.path.isabs(path) or ".." in path.split("/"):
        raise SystemExit("project_specific_directories path must be a non-empty relative path")
    if not isinstance(reason, str) or not reason.strip():
        raise SystemExit(f"project_specific_directories reason must be non-empty: {path}")
print(archetype)
print(environment)
PY
)"; then
  fail "$(cat "$profile_error")"
fi

archetype="$(printf '%s\n' "$profile_values" | sed -n '1p')"
environment="$(printf '%s\n' "$profile_values" | sed -n '2p')"
grep -Fq -- "- archetype: \`${archetype}\`" "$agents_file" || fail "AGENTS.md archetype must match .hub-profile.json"
grep -Fq -- "- environment: \`${environment}\`" "$agents_file" || fail "AGENTS.md environment must match .hub-profile.json"

for section in scope hard_rules forbidden guidelines hybrid_work project_specific_rules routing artifact_homes issue_levels missing_tags context_scope validation models escalation; do
  grep -Fq "<$section>" "$agents_file" || fail "AGENTS.md missing section: <$section>"
  grep -Fq "</$section>" "$agents_file" || fail "AGENTS.md missing section: </$section>"
done

token_estimate="$(python3 - "$agents_file" <<'PY'
import re
import sys
print(len(re.findall(r"\w+|[^\w\s]", open(sys.argv[1], encoding="utf-8").read(), flags=re.UNICODE)))
PY
)"
((token_estimate <= 8000)) || fail "AGENTS.md exceeds the 8K-token hard limit (estimate: $token_estimate)"
if ((token_estimate > 4000)); then
  printf 'WARNING: AGENTS.md exceeds the 4K-token soft limit (estimate: %d).\n' "$token_estimate" >&2
fi

printf 'AGENTS.md bootstrap validation passed (%s/%s).\n' "$archetype" "$environment"
