# -*- coding: utf-8 -*-
from pathlib import Path
from PIL import Image, ImageStat

ai_vid_dir = Path(r"d:\jinyuliangyuan\AI视频\素材")
brain_dir = Path(r"C:\Users\Administrator\.gemini\antigravity\brain\0169f376-faac-423f-9de2-77dde7e8eb51")

files = [
    ai_vid_dir / "Gemini_Generated_Image_bg3iombg3iombg3i.png",
    ai_vid_dir / "Gemini_Generated_Image_su173ysu173ysu17.png",
    ai_vid_dir / "Gemini_Generated_Image_tdat6mtdat6mtdat.png",
    ai_vid_dir / "特写.png",
    ai_vid_dir / "中景.png",
    ai_vid_dir / "远景.png",
    Path(r"d:\jinyuliangyuan\香云纱7.1数字人照片\DSC00102.JPG"),
    Path(r"d:\jinyuliangyuan\香云纱7.1数字人照片\DSC00180.JPG")
]

for f in files:
    if f.exists():
        im = Image.open(f)
        stat = ImageStat.Stat(im)
        print(f"File: {f.name} | Size: {im.size} | Mean RGB: {stat.mean[:3]}")
        # Save a copy in brain
        copy_dst = brain_dir / f"check_{f.stem}.jpg"
        im.convert("RGB").save(copy_dst, "JPEG", quality=90)
