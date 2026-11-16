#!/usr/bin/env python3
"""GRA-002: do the six Hub course checks that "pass on the spoke copies" guard spoke text?

The Hub replay of RFC #721 (F-3, spoke-guard-replay.log) found six of the 19 course
CI steps passing both on the Hub files and with the moved files replaced by the
spoke copies. A pass says nothing if the check never reads a spoke copy. This
experiment adds the falsifier the replay lacked:

  hub    - Hub tree at PIN_SHA as is (baseline, must pass like Hub CI did);
  spoke  - every file that has a copy here (MAPPING of tools/import_from_hub.py,
           including the ten-company example that the Hub replay skipped because
           it lives in the container exp/day1-osint-709/) replaced by that copy;
  blank  - the same files replaced by empty files.

A step that still passes on `blank` does not read any spoke copy: its pass on
`spoke` is vacuous, it guards a Hub-era variant. A step that fails on `blank`
reads at least one copy. To see in which role, the copies are then emptied one
at a time (the rest stay spoke copies): the failing line names the file the
step was checking. If that file is a Hub-era file whose links point into the
emptied copy, the copy is only a link target; if it is the copy itself, the
step checks text the course still has here.

Only Hub check scripts are executed, in a temporary detached worktree of a local
Hub clone (python3 -I, 120 s timeout, 512 MiB address space); spoke files are
copied as data. Nothing in this repository runs Hub code: the invariants chosen
by GRA-002 are rewritten in tests/test_course_handouts.py.

Usage:
  git clone https://github.com/G-Ivan-A/hybrid-Intelligence-lab /tmp/hub-repo
  python3 -I experiments/gra_002_replay_hub_checks.py /tmp/hub-repo \\
      > experiments/gra-002-replay-hub-checks.log
"""
from __future__ import annotations

import re
import resource
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from import_from_hub import DOMAIN, MAPPING  # noqa: E402  (data only: the path table)

PIN_SHA = "48ebe5230be87ca5bf8a08b385e296a2987e9958"
# The six steps of spoke-guard-replay.log at PIN_SHA with "ok | ok".
BOTH_PASS = (
    "Check presentation UX coverage and preservation",
    "Check Day 4 rationale and method slide structure and gate of #685",
    "Check Day 4 Gamma deck and lecturer script of #687",
    "Check Day 4 correction files and unchanged Variant 1 of #689",
    "Check Day 4 Variant 3 deck and lecturer script of #691",
    "Check cold-start OSINT pipeline of #709",
)
STEP_RE = re.compile(r"\n      - name: ")
SCRIPT_RE = re.compile(r"python3 (?:-I )?(research/reputation-technologies/\S+\.py)([^\n]*)")


def limit() -> None:
    resource.setrlimit(resource.RLIMIT_AS, (512 << 20, 512 << 20))


def steps(tree: Path) -> list[tuple[str, list[str]]]:
    found = []
    workflow = (tree / ".github/workflows/validate.yml").read_text(encoding="utf-8")
    for block in STEP_RE.split(workflow)[1:]:
        name = block.split("\n", 1)[0].strip()
        if name in BOTH_PASS:
            found.append((name, [m[1] + m[2] for m in SCRIPT_RE.finditer(block)]))
    assert [n for n, _ in found] == list(BOTH_PASS), "workflow at PIN_SHA changed"
    return found


def overlay(tree: Path, blank: bool, only: str | None = None) -> int:
    """Replace Hub files by their spoke copies; ``blank`` empties them instead
    (all of them, or only the Hub file ``only`` while the rest stay spoke copies)."""
    subprocess.run(["git", "-C", str(tree), "checkout", "-q", "-f", "HEAD", "--", DOMAIN], check=True)
    count = 0
    for hub_rel, copy in MAPPING.items():
        target = tree / DOMAIN / hub_rel
        if not target.is_file():
            continue
        empty = blank and (only is None or only == hub_rel)
        target.write_text("" if empty else (ROOT / copy).read_text(encoding="utf-8"), encoding="utf-8")
        count += 1
    return count


def run(tree: Path, command: str) -> tuple[int, str]:
    script, *args = command.split()
    proc = subprocess.run([sys.executable, "-I", script, *args], cwd=tree, capture_output=True,
                          text=True, timeout=120, preexec_fn=limit)
    tail = (proc.stdout + proc.stderr).strip().splitlines()
    return proc.returncode, tail[-1][:150] if tail else ""


def condition(tree: Path, commands: list[str]) -> tuple[str, str]:
    results = [run(tree, c) for c in commands]
    failed = [line for rc, line in results if rc]
    return ("FAIL", failed[0]) if failed else ("ok", "")


def main() -> int:
    hub = Path(sys.argv[1]).resolve()
    tmp = Path(tempfile.mkdtemp(prefix="gra-002-"))
    tree = tmp / "hub"
    subprocess.run(["git", "-C", str(hub), "worktree", "add", "-q", "--detach", str(tree), PIN_SHA],
                   check=True)
    try:
        print(f"Hub commit: {PIN_SHA}; course steps checked: {len(BOTH_PASS)}")
        print("step | hub | spoke | blank | verdict | first failing line (spoke, else blank)")
        rows, readers = [], []
        for name, commands in steps(tree):
            subprocess.run(["git", "-C", str(tree), "checkout", "-q", "-f", "HEAD", "--", DOMAIN], check=True)
            hub_rc, _ = condition(tree, commands)
            replaced = overlay(tree, blank=False)
            spoke_rc, spoke_line = condition(tree, commands)
            overlay(tree, blank=True)
            blank_rc, blank_line = condition(tree, commands)
            if blank_rc == "ok":
                verdict = "vacuous: reads no spoke copy"
            elif spoke_rc == "ok":
                verdict = "reads a spoke copy (role: see below)"
            else:
                verdict = "fails on spoke copy"
            rows.append(verdict)
            print(f"{name} | {hub_rc} | {spoke_rc} | {blank_rc} | {verdict} | {spoke_line or blank_line}")
            if blank_rc != "ok":
                readers.append((name, commands))
        print(f"files replaced by spoke copies: {replaced}")
        print("summary: " + ", ".join(f"{v}: {rows.count(v)}" for v in sorted(set(rows))))
        # Which copy does a step read? Empty one copy at a time, keep the rest.
        print()
        print("step | spoke copy whose emptying fails the step | failing line")
        for name, commands in readers:
            for hub_rel, copy in MAPPING.items():
                if not (tree / DOMAIN / hub_rel).is_file():
                    continue
                overlay(tree, blank=True, only=hub_rel)
                rc, line = condition(tree, commands)
                if rc != "ok":
                    print(f"{name} | {copy} | {line}")
    finally:
        subprocess.run(["git", "-C", str(hub), "worktree", "remove", "--force", str(tree)], check=False)
        shutil.rmtree(tmp, ignore_errors=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
