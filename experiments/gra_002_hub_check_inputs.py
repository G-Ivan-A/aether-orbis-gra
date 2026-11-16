#!/usr/bin/env python3
"""GRA-002: which current course files does each Hub course check name?

Static scan, nothing is executed: for each of the 19 course steps of the Hub
workflow at PIN_SHA, read its check scripts with ``git show`` and list the Hub
files of the import MAPPING (tools/import_from_hub.py) whose names occur in the
script as quoted strings. A step that names no mapped file checks only Hub-era
files; a step that names a mapped file may guard a file the course has here.
The result column of the Hub replay (spoke-guard-replay.log, Hub RFC #721 F-3)
is printed next to it.

Usage:
  git clone https://github.com/G-Ivan-A/hybrid-Intelligence-lab /tmp/hub-repo
  python3 -I experiments/gra_002_hub_check_inputs.py /tmp/hub-repo \\
      > experiments/gra-002-hub-check-inputs.log
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from import_from_hub import DOMAIN, MAPPING  # noqa: E402  (data only: the path table)

PIN_SHA = "48ebe5230be87ca5bf8a08b385e296a2987e9958"
REPLAY = "research/hub/exp/gra-extraction-cleanup-721/spoke-guard-replay.log"
STEP_RE = re.compile(r"\n      - name: ")
SCRIPT_RE = re.compile(r"python3 (?:-I )?(research/reputation-technologies/\S+\.py)")
QUOTED = re.compile(r"[\"']([\w./-]+\.(?:md|json|txt))[\"']")


def show(hub: Path, path: str) -> str:
    return subprocess.run(["git", "-C", str(hub), "show", f"{PIN_SHA}:{path}"],
                          capture_output=True, text=True, check=True).stdout


def main() -> int:
    hub = Path(sys.argv[1]).resolve()
    replay = {}
    for line in show(hub, REPLAY).splitlines():
        parts = line.split(" | ")
        if len(parts) == 4 and parts[1] in ("ok", "FAIL"):
            replay[parts[0]] = parts[2]
    by_name = {Path(key).name: (key, copy) for key, copy in MAPPING.items()}
    print(f"Hub commit: {PIN_SHA}")
    print("step | Hub replay on spoke | current course files named by the script (spoke copy)")
    total = 0
    for block in STEP_RE.split(show(hub, ".github/workflows/validate.yml"))[1:]:
        name = block.split("\n", 1)[0].strip()
        scripts = SCRIPT_RE.findall(block)
        if not scripts:
            continue
        total += 1
        named = set()
        for script in scripts:
            for quoted in QUOTED.findall(show(hub, script)):
                base = Path(quoted).name
                if base in by_name and (quoted == base or quoted.endswith(by_name[base][0])):
                    named.add(by_name[base][1].replace("education/technograd-reputation-engineering/", ""))
        status = replay.get(name[:72], "?")
        print(f"{name} | {status} | {', '.join(sorted(named)) or '-'}")
    print(f"course steps: {total}; DOMAIN: {DOMAIN}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
