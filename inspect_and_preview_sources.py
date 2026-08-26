# -*- coding: utf-8 -*-
from pathlib import Path
from PIL import Image

candidates = [
    Path(r"d:\jinyuliangyuan\素材\模特图\重工提花·香云纱1.jpg"),
    Path(r"d:\jinyuliangyuan\素材\模特图\水墨系列·香云纱1.jpg"),
    Path(r"d:\jinyuliangyuan\素材\模特图\喜上眉梢·香云斜纹套装1.jpg"),
    Path(r"d:\jinyuliangyuan\素材\模特图\庭院风情·香云成衣套装1.jpg"),
    Path(r"d:\jinyuliangyuan\AI视频\素材\Gemini_Generated_Image_bg3iombg3iombg3i.png"),
    Path(r"d:\jinyuliangyuan\AI视频\素材\Gemini_Generated_Image_su173ysu173ysu17.png"),
    Path(r"d:\jinyuliangyuan\AI视频\素材\Gemini_Generated_Image_tdat6mtdat6mtdat.png"),
    Path(r"d:\jinyuliangyuan\香云纱7.1数字人照片\DSC00102.JPG"),
    Path(r"d:\jinyuliangyuan\香云纱7.1数字人照片\DSC00180.JPG")
]

for p in candidates:
    if p.exists():
        im = Image.open(p)
        print(f"{p.name} -> Size: {im.size}, Mode: {im.mode}, Filesize: {p.stat().st_size/1024/1024:.2f} MB")
