# -*- coding: utf-8 -*-
import os
from pathlib import Path
from PIL import Image, ImageFilter

brain_dir = Path(r"C:\Users\Administrator\.gemini\antigravity\brain\0169f376-faac-423f-9de2-77dde7e8eb51")
out_dir = Path(r"d:\jinyuliangyuan\公众号推文\封面图\今遇莨缘香云纱公众号推广文 2026-8-20  v1")
out_dir.mkdir(parents=True, exist_ok=True)

# 5 Brand New, Unique, Non-repeating Photographic Illustrations for 8-20
brand_new_items = [
    {
        "src": brain_dir / "brand_new_tactile_vip_touch_1787193346525.jpg",
        "name": "正文配图1_买手店私域VIP触感试穿体验",
        "section": "第一节：触觉饥渴的本能反扑（买手店VIP客户指尖抚摸衣襟肌理）"
    },
    {
        "src": brain_dir / "brand_new_skyline_power_woman_1787193355401.jpg",
        "name": "正文配图2_东方高知大女主天际线职场战袍",
        "section": "第二节：现代大女主战袍（高知女性身着重工立裁双排扣西装俯瞰天际线）"
    },
    {
        "src": brain_dir / "brand_new_yam_tannin_silk_macro_1787193371180.jpg",
        "name": "正文配图3_深山野生薯莨单宁与重工丝绸微距",
        "section": "第一节：天然矿物与草木微凉（双手展开重工丝绸，切片野生薯莨单宁纹与瓷碗）"
    },
    {
        "src": brain_dir / "brand_new_acoustic_motion_staircase_1787193422598.jpg",
        "name": "正文配图4_艺术沙龙步步生风沙沙响云白噪音",
        "section": "第二节：步步带风的响云白噪音（现代艺术馆旋转楼梯漫步，重工裙摆声学流动）"
    },
    {
        "src": brain_dir / "brand_new_nanyou_vip_consultation_1787193433615.jpg",
        "name": "正文配图5_深圳南油今遇莨缘VIP品鉴台与选品画册",
        "section": "第三/四节：深圳南油品鉴中心与大厂实体坚守（黑石品鉴桌、精装非遗画册、功夫茶与布卷）"
    }
]

print("Processing 5 brand-new in-article photos in 2.7K Ultra HD...")

for item in brand_new_items:
    src_p = item["src"]
    if not src_p.exists():
        print(f"Error: {src_p} not found!")
        continue
        
    img = Image.open(src_p)
    w, h = img.size
    
    # 2x super-resolution scaling using Lanczos (2752x1536)
    target_w, target_h = w * 2, h * 2
    img_hd = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Subtle sharpness enhancement for micro tactile craquelure texture
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

print("All 5 brand-new in-article illustrations processed successfully!")
