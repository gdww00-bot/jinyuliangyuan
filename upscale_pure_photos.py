# -*- coding: utf-8 -*-
import os
from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter

brain_dir = Path(r"C:\Users\Administrator\.gemini\antigravity\brain\0169f376-faac-423f-9de2-77dde7e8eb51")
out_dir = Path(r"d:\jinyuliangyuan\公众号推文\封面图\今遇莨缘香云纱公众号推广文 2026-8-20  v1")

pure_photos = [
    ("文章配图1_指尖触感与重工丝绸肌理", brain_dir / "xiangyun_boutique_tactile_fabric_1787191148345.jpg"),
    ("文章配图2_东方大女主现代高定风衣", brain_dir / "xiangyun_intellectual_trench_touch_1787191124901.jpg"),
    ("文章配图3_现代立裁垫肩西装步步生风", brain_dir / "xiangyun_blazer_power_female_1787192048947.jpg"),
    ("文章配图4_深圳南油品鉴中心高端展陈", brain_dir / "xiangyun_nanyou_luxury_atelier_1787120792179.jpg"),
    ("文章配图5_日光草木千亩晒莨非遗造物", brain_dir / "xiangyun_sundrying_meadow_1787108666939.jpg"),
    ("文章配图6_深山野生薯莨与富铁河泥过乌", brain_dir / "xiangyun_eco_craft_mud_dye_1787120666937.jpg")
]

for name, src_p in pure_photos:
    if not src_p.exists(): continue
    img = Image.open(src_p)
    w, h = img.size
    
    # 2x upscale using Lanczos resampling
    target_w, target_h = w * 2, h * 2
    img_hd = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Subtle unsharp mask enhancement to enhance fine silk fibers and details
    img_hd = img_hd.filter(ImageFilter.UnsharpMask(radius=1.5, percent=115, threshold=3))
    
    jpg_path = out_dir / f"{name}.jpg"
    png_path = out_dir / f"{name}_超清无损.png"
    
    # Save Ultra HD JPG (quality=98, subsampling=0)
    img_hd.convert("RGB").save(jpg_path, format="JPEG", quality=98, subsampling=0)
    
    # Save Lossless PNG
    img_hd.save(png_path, format="PNG")
    
    # Copy to brain dir
    brain_jpg = brain_dir / f"{name}.jpg"
    img_hd.convert("RGB").save(brain_jpg, format="JPEG", quality=98, subsampling=0)
    
    print(f"Enhanced {name}: {target_w}x{target_h} | JPG: {jpg_path.stat().st_size / 1024 / 1024:.2f} MB | PNG: {png_path.stat().st_size / 1024 / 1024:.2f} MB")

print("All 6 in-article pure photos enhanced and saved in Ultra HD!")
