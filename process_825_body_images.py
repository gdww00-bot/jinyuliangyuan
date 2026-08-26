# -*- coding: utf-8 -*-
import os
import shutil
from pathlib import Path
from PIL import Image, ImageFilter

brain_dir = Path(r"C:\Users\Administrator\.gemini\antigravity\brain\0169f376-faac-423f-9de2-77dde7e8eb51")
out_dir = Path(r"d:\jinyuliangyuan\公众号推文\封面图\今遇莨缘香云纱公众号推广文 2026-8-25  v1")
out_dir.mkdir(parents=True, exist_ok=True)

photos = [
    {
        "src": brain_dir / "brand_new_skyline_power_woman_1787193355401.jpg",
        "name": "正文配图1_东方高知大女主天际线职场战袍",
        "desc": "对应第一节：智性大女主的无声权力法则（双排扣立体剪裁香云纱西装与天际线落地窗）"
    },
    {
        "src": brain_dir / "brand_new_acoustic_motion_staircase_1787193422598.jpg",
        "name": "正文配图2_艺术沙龙步步生风沙沙响云白噪音",
        "desc": "对应第二节：步步带风的听觉名片与专属BGM（现代艺术馆旋转阶梯漫步，重工风衣声学流动）"
    }
]

print("Processing 2 pure, text-free in-article photos in 2.7K Ultra HD...")

for item in photos:
    src_p = item["src"]
    if not src_p.exists():
        print(f"Error: {src_p} not found!")
        continue
        
    img = Image.open(src_p)
    w, h = img.size
    
    # 2x Super-resolution scaling using Lanczos (2752x1536)
    target_w, target_h = w * 2, h * 2
    img_hd = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Subtle sharpness enhancement for micro silk fiber & craquelure detail
    img_hd = img_hd.filter(ImageFilter.UnsharpMask(radius=1.4, percent=110, threshold=2))
    
    name = item["name"]
    jpg_path = out_dir / f"{name}.jpg"
    png_path = out_dir / f"{name}_超清无损.png"
    
    # Save Ultra HD JPG (quality=98, subsampling=0)
    img_hd.convert("RGB").save(jpg_path, format="JPEG", quality=98, subsampling=0)
    
    # Save Lossless PNG
    img_hd.save(png_path, format="PNG")
    
    # Copy to brain dir
    brain_jpg = brain_dir / f"{name}.jpg"
    img_hd.convert("RGB").save(brain_jpg, format="JPEG", quality=98, subsampling=0)
    
    print(f"Saved: {jpg_path.name} ({jpg_path.stat().st_size / 1024 / 1024:.2f} MB, {target_w}x{target_h})")
    print(f"Saved: {png_path.name} ({png_path.stat().st_size / 1024 / 1024:.2f} MB)")

print("All 2 pure text-free in-article photos processed successfully!")
