# -*- coding: utf-8 -*-
import os
import shutil
from pathlib import Path
from PIL import Image

brain_dir = Path(r"C:\Users\Administrator\.gemini\antigravity\brain\0169f376-faac-423f-9de2-77dde7e8eb51")
out_dir = Path(r"d:\jinyuliangyuan\公众号推文\封面图\今遇莨缘香云纱公众号推广文 2026-8-20  v1")
out_dir.mkdir(parents=True, exist_ok=True)

# Map of pure photographic illustrations
pure_photos = [
    {
        "src": brain_dir / "xiangyun_boutique_tactile_fabric_1787191148345.jpg",
        "name": "文章配图1_指尖触感与重工丝绸肌理",
        "desc": "对应第一节：触觉饥渴与真实物理分量（双手抚摸重工香云纱细腻龟裂纹特写）"
    },
    {
        "src": brain_dir / "xiangyun_intellectual_trench_touch_1787191124901.jpg",
        "name": "文章配图2_东方大女主现代高定风衣",
        "desc": "对应第二节：现代独立女性战袍（禅意庭院中高知女性手抚香云纱风衣衣襟）"
    },
    {
        "src": brain_dir / "xiangyun_blazer_power_female_1787192048947.jpg",
        "name": "文章配图3_现代立裁垫肩西装步步生风",
        "desc": "对应第二节：响云白噪音与职场气场（独立大女主身着重工立裁西装漫步）"
    },
    {
        "src": brain_dir / "xiangyun_nanyou_luxury_atelier_1787120792179.jpg",
        "name": "文章配图4_深圳南油品鉴中心高端展陈",
        "desc": "对应第三/四节：深圳南油103名品馆展厅（高端成衣展陈、布卷与非遗典籍）"
    },
    {
        "src": brain_dir / "xiangyun_sundrying_meadow_1787108666939.jpg",
        "name": "文章配图5_日光草木千亩晒莨非遗造物",
        "desc": "对应生态母本：晨曦金光草甸上翻晒的香云纱布匹与非遗手作"
    },
    {
        "src": brain_dir / "xiangyun_eco_craft_mud_dye_1787120666937.jpg",
        "name": "文章配图6_深山野生薯莨与富铁河泥过乌",
        "desc": "对应工艺溯源：匠人双手在晨光中进行纯天然薯莨与河泥过乌手作"
    }
]

print("Processing and saving pure in-article photographic illustrations in Ultra HD...")

for item in pure_photos:
    src_p = item["src"]
    if not src_p.exists():
        print(f"Warning: {src_p} does not exist!")
        continue
        
    img = Image.open(src_p)
    
    # Target file paths in the 8-20 cover/illustration directory
    jpg_target = out_dir / f"{item['name']}.jpg"
    png_target = out_dir / f"{item['name']}_无损.png"
    
    # Save JPG with 98% Ultra HD quality and 4:4:4 color subsampling (subsampling=0)
    img.convert("RGB").save(jpg_target, format="JPEG", quality=98, subsampling=0)
    
    # Save Lossless PNG
    img.save(png_target, format="PNG")
    
    # Copy to brain dir for embedding
    brain_jpg = brain_dir / f"{item['name']}.jpg"
    img.convert("RGB").save(brain_jpg, format="JPEG", quality=98, subsampling=0)
    
    print(f"Saved: {jpg_target.name} ({jpg_target.stat().st_size / 1024 / 1024:.2f} MB, {img.size[0]}x{img.size[1]})")
    print(f"Saved: {png_target.name} ({png_target.stat().st_size / 1024 / 1024:.2f} MB)")

print("All pure in-article illustrations processed successfully!")
