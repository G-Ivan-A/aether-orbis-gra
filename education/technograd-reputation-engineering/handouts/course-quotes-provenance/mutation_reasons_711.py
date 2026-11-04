#!/usr/bin/env python3
"""Print the first error each self-test mutation of check-quotes-711.py raises, to see that it is rejected for the intended reason."""
import importlib.util
from pathlib import Path

PATH = Path(__file__).resolve().parent / "check-quotes-711.py"
spec = importlib.util.spec_from_file_location("check", PATH)
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)
text = check.TARGET.read_text(encoding="utf-8") if check.TARGET.is_file() else ""
excerpt_text = check.EXCERPTS.read_text(encoding="utf-8")
for name, fn in check.MUTATIONS.items():
    errors = check.validate(*fn(text, excerpt_text))
    print(f"{name} -> {errors[0][:150] if errors else 'NOT REJECTED'}")
