#!/usr/bin/env bash
# Evidence for issue #3 (Hub RFC #721, S-1): every Hub link pinned to PIN_SHA answers 200.
# Collects unique blob/tree URLs on PIN_SHA from tracked and new files (anchors dropped:
# GitHub answers per file, an anchor is resolved by the browser), probes each with HEAD.
# Usage: experiments/probe_pin_sha_links.sh [PIN_SHA] > experiments/probe-pin-sha-links.log
set -euo pipefail
pin="${1:-48ebe5230be87ca5bf8a08b385e296a2987e9958}"
root="$(git rev-parse --show-toplevel)"
cd "$root"
mapfile -t urls < <(git ls-files -z -c -o --exclude-standard \
  | xargs -0 grep -ohE "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/(blob|tree)/${pin}/[^)#> \"\`]+" \
  | sort -u)
fail=0
for url in "${urls[@]}"; do
  code="$(curl -s -o /dev/null -I -L --retry 2 --max-time 30 -w '%{http_code}' "$url")"
  echo "$code $url"
  [[ "$code" == 200 ]] || fail=$((fail + 1))
done
echo "summary: ${#urls[@]} unique PIN_SHA URLs, $fail not 200"
[[ $fail -eq 0 ]]
