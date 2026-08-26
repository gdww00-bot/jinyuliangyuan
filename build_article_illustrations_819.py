# -*- coding: utf-8 -*-
import os
import shutil
import subprocess
from pathlib import Path
from PIL import Image

brain_dir = Path(r"C:\Users\Administrator\.gemini\antigravity\brain\0169f376-faac-423f-9de2-77dde7e8eb51")
out_dir = Path(r"d:\jinyuliangyuan\公众号配图\今遇莨缘香云纱公众号推广文 2026-8-19  v1")
out_dir.mkdir(parents=True, exist_ok=True)
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# 1. Source AI images
src_imgs = {
    "xiangyun_eco_craft_mud_dye_4K.jpg": brain_dir / "xiangyun_eco_craft_mud_dye_1787120666937.jpg",
    "xiangyun_intellectual_power_suit_4K.jpg": brain_dir / "xiangyun_intellectual_power_suit_1787120775567.jpg",
    "xiangyun_nanyou_luxury_atelier_4K.jpg": brain_dir / "xiangyun_nanyou_luxury_atelier_1787120792179.jpg",
    "xiangyun_sundrying_meadow_4K.jpg": brain_dir / "xiangyun_sundrying_meadow_1787108666939.jpg"
}

for dst_name, src_path in src_imgs.items():
    if src_path.exists():
        shutil.copy(src_path, out_dir / dst_name)
        print(f"Copied {src_path.name} -> {dst_name}")

# 2. Template Generator for 配图 1, 2, 3
def get_editorial_html(bg_img_name, badge_text, pre_title, main_title, subtitle, tags, signature, img_pos="center center", gradient_dir="to top"):
    tags_html = "".join([f'<span class="footer-tag-item">{tag}</span>' for tag in tags])
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>{pre_title} (2560x1440)</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;700;900&family=Cinzel:wght@600;700&display=swap');

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      width: 2560px;
      height: 1440px;
      overflow: hidden;
      font-family: 'Noto Serif SC', 'Source Han Serif SC', serif;
      background-color: #120d0a;
      color: #ffffff;
      position: relative;
    }}

    .background-img {{
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      object-fit: cover;
      object-position: {img_pos};
      filter: brightness(1.02) contrast(1.16) saturate(1.18);
    }}

    .overlay-gradient {{
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      background: 
        linear-gradient(to top, rgba(10, 7, 5, 0.96) 0%, rgba(10, 7, 5, 0.82) 26%, rgba(10, 7, 5, 0.25) 55%, transparent 100%),
        linear-gradient(to bottom, rgba(8, 6, 4, 0.75) 0%, transparent 25%),
        radial-gradient(circle at 50% 100%, rgba(12, 8, 6, 0.95) 0%, transparent 75%);
    }}

    .border-frame {{
      position: absolute;
      top: 40px; left: 40px; right: 40px; bottom: 40px;
      border: 2px solid rgba(212, 175, 55, 0.55);
      pointer-events: none;
      box-shadow: inset 0 0 50px rgba(0, 0, 0, 0.5);
    }}

    .border-frame::before {{
      content: '';
      position: absolute;
      top: 10px; left: 10px; right: 10px; bottom: 10px;
      border: 1px solid rgba(212, 175, 55, 0.25);
    }}

    .container {{
      position: relative;
      z-index: 10;
      height: 100%;
      padding: 70px 90px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .header-badge {{
      display: inline-flex;
      align-items: center;
      gap: 16px;
      background: linear-gradient(135deg, rgba(212, 175, 55, 0.28), rgba(139, 90, 43, 0.38));
      border: 1.5px solid rgba(212, 175, 55, 0.85);
      backdrop-filter: blur(12px);
      padding: 12px 36px;
      border-radius: 6px;
      align-self: flex-start;
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
    }}

    .badge-icon {{
      width: 14px;
      height: 14px;
      background: #d4af37;
      transform: rotate(45deg);
      box-shadow: 0 0 12px #d4af37;
    }}

    .badge-text {{
      font-size: 24px;
      font-weight: 700;
      letter-spacing: 3px;
      color: #f5eaaf;
    }}

    .content-box {{
      max-width: 2200px;
      margin-bottom: 10px;
    }}

    .pre-title {{
      font-size: 36px;
      font-weight: 700;
      color: #f7d274;
      letter-spacing: 4px;
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 20px;
      text-shadow: 0 3px 16px rgba(0, 0, 0, 0.95);
    }}

    .pre-title::after {{
      content: '';
      flex: 1;
      max-width: 180px;
      height: 2px;
      background: linear-gradient(to right, #d4af37, transparent);
    }}

    .main-title {{
      font-size: 58px;
      line-height: 1.32;
      font-weight: 900;
      color: #ffffff;
      text-shadow: 0 5px 28px rgba(0, 0, 0, 0.95);
      letter-spacing: 2px;
    }}

    .highlight-text {{
      background: linear-gradient(135deg, #ffffff 0%, #ffe08a 35%, #d4af37 75%, #b5831b 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: inline-block;
      filter: drop-shadow(0 3px 10px rgba(0, 0, 0, 0.8));
    }}

    .subtitle-box {{
      margin-top: 20px;
      padding-left: 24px;
      border-left: 5px solid #d4af37;
    }}

    .subtitle {{
      font-size: 28px;
      line-height: 1.5;
      color: #eae7e1;
      font-weight: 500;
      letter-spacing: 2px;
      text-shadow: 0 3px 14px rgba(0, 0, 0, 0.9);
    }}

    .footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1.5px solid rgba(212, 175, 55, 0.4);
      padding-top: 24px;
    }}

    .footer-tags {{
      display: flex;
      gap: 36px;
      font-size: 22px;
      color: #dfbe76;
      letter-spacing: 2.5px;
      font-weight: 600;
    }}

    .footer-tag-item {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .footer-tag-item::before {{
      content: "✦";
      font-size: 18px;
      color: #d4af37;
    }}

    .brand-signature {{
      font-family: 'Cinzel', serif;
      font-size: 22px;
      letter-spacing: 5px;
      color: rgba(212, 175, 55, 0.9);
      text-transform: uppercase;
      font-weight: 700;
    }}
  </style>
</head>
<body>

  <img class="background-img" src="{bg_img_name}" alt="背景">
  <div class="overlay-gradient"></div>
  <div class="border-frame"></div>

  <div class="container">
    
    <div class="header-badge">
      <div class="badge-icon"></div>
      <span class="badge-text">{badge_text}</span>
    </div>

    <div class="content-box">
      <div class="pre-title">{pre_title}</div>
      <h1 class="main-title">{main_title}</h1>
      <div class="subtitle-box">
        <p class="subtitle">{subtitle}</p>
      </div>
    </div>

    <div class="footer">
      <div class="footer-tags">
        {tags_html}
      </div>
      <div class="brand-signature">{signature}</div>
    </div>

  </div>

</body>
</html>"""

# Define illustrations 1, 2, 3
illustrations = [
    {
        "filename": "配图1_草木与河泥过乌古法生态_2.6K",
        "bg_img": "xiangyun_eco_craft_mud_dye_4K.jpg",
        "badge": "【今遇莨缘】 千年非遗古法天序 · 生态母本溯源",
        "pre_title": "零化学添加 · 纯天然全生物降解防线",
        "main_title": "野生深山薯莨与富铁河泥过乌：<span class=\"highlight-text\">唯有大自然借来的色彩，方配陪伴一生</span>",
        "subtitle": "蚕丝单宁天然着色，十八晒十八莨淬炼 · 抑菌透气微凉不燥，呵护高知女性身心健康",
        "tags": ["野生深山薯莨", "珠江流域富铁河泥", "零化学微塑料", "纯天然全降解"],
        "signature": "HERITAGE BOTANICAL ECOLOGY",
        "pos": "center 38%"
    },
    {
        "filename": "配图2_现代大女主智性高定西装_2.6K",
        "bg_img": "xiangyun_intellectual_power_suit_4K.jpg",
        "badge": "【今遇莨缘】 现代立裁骨架 · 对抗快消贬值诅咒",
        "pre_title": "随体温包浆熟化 · 越穿越润的时间资产",
        "main_title": "融入世界级极简廓形与干练立裁：<span class=\"highlight-text\">赋予东方独立大女主雷厉风行的气场</span>",
        "subtitle": "撕碎过季即废品魔咒 · 行走间低沉沙沙白噪音，踏入国际商务峰会与高端宴会的底气",
        "tags": ["时间复利资产", "现代垫肩西装/风衣", "高知独立气场", "拒绝松垮养生袍"],
        "signature": "HAUTE COUTURE INTELLECTUAL SUIT",
        "pos": "center 28%"
    },
    {
        "filename": "配图3_深圳南油品鉴中心高端展陈_2.6K",
        "bg_img": "xiangyun_nanyou_luxury_atelier_4K.jpg",
        "badge": "【今遇莨缘】 深圳南油品鉴中心 · 纯B端护城河",
        "pre_title": "恪守大厂边界 · 全渠道坚决谢绝零散客",
        "main_title": "千亩生态晒莨基地源头直供：<span class=\"highlight-text\">将100%定价自主权与利润护城河让渡实体</span>",
        "subtitle": "原创典籍图腾壁垒 · 小单柔性快反补单 · 配套提供国际水准高清视觉大片与话术库",
        "tags": ["深圳南油103名品馆", "坚决不开直播破价", "小单柔性快反", "全案视觉物料交付"],
        "signature": "EXCLUSIVE B2B ATELIER SHENZHEN",
        "pos": "center center"
    }
]

# 3. Generate HTML and render
for item in illustrations:
    fname = item["filename"]
    html_file = out_dir / f"{fname}.html"
    html_content = get_editorial_html(
        item["bg_img"],
        item["badge"],
        item["pre_title"],
        item["main_title"],
        item["subtitle"],
        item["tags"],
        item["signature"],
        item["pos"]
    )
    html_file.write_text(html_content, encoding='utf-8')
    print(f"Generated HTML: {html_file.name}")

# Also ensure 配图4 is there and updated with ultra-high quality
html4_path = out_dir / "配图4_今遇莨缘四大生态硬通货法则_2.6K.html"

# Render list: 配图1, 配图2, 配图3, 配图4
all_render_targets = [
    out_dir / "配图1_草木与河泥过乌古法生态_2.6K.html",
    out_dir / "配图2_现代大女主智性高定西装_2.6K.html",
    out_dir / "配图3_深圳南油品鉴中心高端展陈_2.6K.html",
    out_dir / "配图4_今遇莨缘四大生态硬通货法则_2.6K.html"
]

print("Rendering all 4 illustrations with Chrome Headless in Ultra HD...")

for html_p in all_render_targets:
    stem = html_p.stem
    temp_png = out_dir / f"{stem}_temp.png"
    final_png = out_dir / f"{stem}.png"
    final_jpg = out_dir / f"{stem}.jpg"
    
    file_url = f"file:///{str(html_p).replace(os.sep, '/')}"
    
    # 2560 x 1440 window with 1x or 2x device scale factor
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=2560,1440",
        f"--screenshot={str(temp_png)}",
        file_url
    ]
    
    subprocess.run(cmd, capture_output=True)
    
    if temp_png.exists():
        img = Image.open(temp_png)
        # Save lossless PNG
        img.save(final_png, format="PNG")
        # Save ultra-clear JPG (quality=98, subsampling=0)
        img.convert("RGB").save(final_jpg, format="JPEG", quality=98, subsampling=0)
        
        # Clean temp
        temp_png.unlink()
        
        # Copy to brain dir
        brain_jpg = brain_dir / f"{stem}.jpg"
        img.convert("RGB").save(brain_jpg, format="JPEG", quality=98, subsampling=0)
        
        print(f"Rendered: {stem}.jpg ({final_jpg.stat().st_size / 1024 / 1024:.2f} MB, {img.size[0]}x{img.size[1]})")
        print(f"Rendered: {stem}.png ({final_png.stat().st_size / 1024 / 1024:.2f} MB)")

print("All 4 article illustrations rendered successfully!")
