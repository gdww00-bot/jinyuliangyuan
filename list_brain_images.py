# -*- coding: utf-8 -*-
from pathlib import Path
from PIL import Image

brain_dir = Path(r"C:\Users\Administrator\.gemini\antigravity\brain\0169f376-faac-423f-9de2-77dde7e8eb51")

images = []
for p in brain_dir.glob("*.jpg"):
    if not "cover" in p.name and not "procedural" in p.name:
        im = Image.open(p)
        images.append((p.name, im.size, p.stat().st_size / 1024 / 1024))

for name, size, mb in sorted(images, key=lambda x: x[2], reverse=True):
    print(f"{name:50s} | Size: {size} | {mb:.2f} MB")
