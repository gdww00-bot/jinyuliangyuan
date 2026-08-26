# -*- coding: utf-8 -*-
from pathlib import Path
from PIL import Image

ai_vid_dir = Path(r"d:\jinyuliangyuan\AI视频\素材")
brain_dir = Path(r"C:\Users\Administrator\.gemini\antigravity\brain\0169f376-faac-423f-9de2-77dde7e8eb51")

for f in ai_vid_dir.glob("*.png"):
    im = Image.open(f)
    print(f"{f.name}: size={im.size}, mode={im.mode}")
    # copy thumbnail or copy to brain
    target = brain_dir / f"inspect_{f.stem}.jpg"
    im.convert("RGB").save(target, "JPEG", quality=85)
