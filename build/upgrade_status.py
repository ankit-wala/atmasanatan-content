#!/usr/bin/env python3
"""Upgrade status: reviewed → ready_to_publish for all entries that now have a real date."""
import os, re

BASE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "kathas", "festivals")

upgraded = 0
skipped = 0

for slug in sorted(os.listdir(BASE)):
    path = os.path.join(BASE, slug, "meta.yaml")
    if not os.path.exists(path):
        continue
    with open(path) as f:
        text = f.read()

    # Only upgrade if date_2026 is now a real date (not TODO-VERIFY)
    if re.search(r'date_2026:\s*TODO-VERIFY', text):
        skipped += 1
        continue
    if "status: reviewed" not in text:
        skipped += 1
        continue

    # Replace any "status: reviewed" line, preserving any trailing comment
    new_text = re.sub(
        r'status:\s*reviewed(\s*(#[^\n]*)?)',
        lambda m: 'status: ready_to_publish' + (m.group(1) if m.group(1) else ''),
        text
    )

    if new_text != text:
        with open(path, "w") as f:
            f.write(new_text)
        upgraded += 1
    else:
        skipped += 1

print(f"Upgraded: {upgraded}")
print(f"Skipped:  {skipped}")
