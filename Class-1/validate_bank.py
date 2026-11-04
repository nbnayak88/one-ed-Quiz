#!/usr/bin/env python3
"""Validate Class 1 10,000-question bank structure. Run: python Class-1/validate_bank.py"""
from pathlib import Path
from collections import Counter
import json
import re

ROOT = Path(__file__).resolve().parent
manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
errors = []
seen = []
checked = 0
for lab in manifest["labs"]:
    for volume in lab["volumes"]:
        path = volume.get("path")
        if not path:
            continue
        src = ROOT.parent / path
        if not src.exists():
            errors.append(f"Missing published volume: {path}")
            continue
        text = src.read_text(encoding="utf-8")
        matches = list(re.finditer(r"(?m)^###\s*Q\s*([\d,]+)(?=\s|\.|$)", text))
        ids = [int(m.group(1).replace(",", "")) for m in matches]
        a, b = volume["range"]
        if ids != list(range(a, b + 1)):
            errors.append(f"ID sequence wrong in {path}: found {len(ids)} expected 250")
        for i, match in enumerate(matches):
            end = matches[i + 1].start() if i+1 < len(matches) else len(text)
            piece = text[match.end():end]
            q = ids[i]
            if not re.search(r"(?m)^\*\*Answer:", piece):
                errors.append(f"No answer: Q{q} in {path}")
            if not re.search(r"(?m)^(?:💡\s*)?\*\*Explanation:", piece):
                errors.append(f"No explanation: Q{q} in {path}")
            heading = text[match.start():text.find("\n", match.start()) if "\n" in text[match.start():] else len(text)]
            if q % 25 == 0 and "SUPER OLYMPIAD" not in heading.upper():
                errors.append(f"Super Olympiad challenge label missing: Q{q} in {path}")
        seen.extend(ids)
        checked += 1
dupes = [n for n,c in Counter(seen).items() if c > 1]
if dupes:
    errors.append(f"Duplicate IDs: {dupes[:20]}")
expected = manifest["published_questions"]
if len(seen) != expected:
    errors.append(f"Published question count: {len(seen)}; expected {expected}")
print(f"Validated {checked} published volumes, {len(seen)} question IDs; planned bank total {manifest['planned_questions']}")
if errors:
    print("STRUCTURAL CHECK FAILED")
    for error in errors: print("-", error)
    raise SystemExit(1)
print("STRUCTURAL CHECK PASSED; independent factual/editorial audit still required.")
