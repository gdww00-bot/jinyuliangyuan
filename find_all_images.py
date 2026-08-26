# -*- coding: utf-8 -*-
from pathlib import Path

base_dir = Path(r"d:\jinyuliangyuan")
brain_base = Path(r"C:\Users\Administrator\.gemini\antigravity\brain")

images = []
for p in base_dir.rglob("*"):
    if p.is_file() and p.suffix.lower() in ['.jpg', '.jpeg', '.png']:
        if p.stat().st_size > 300 * 1024:
            images.append((p.stat().st_size, str(p)))

for p in brain_base.rglob("*"):
    if p.is_file() and p.suffix.lower() in ['.jpg', '.jpeg', '.png']:
        if p.stat().st_size > 500 * 1024 and not "temp" in p.name.lower():
            images.append((p.stat().st_size, str(p)))

images.sort(reverse=True)
for sz, path in images[:60]:
    print(f"{sz/1024/1024:.2f} MB -> {path}")
