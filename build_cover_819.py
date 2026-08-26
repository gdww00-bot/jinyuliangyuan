# -*- coding: utf-8 -*-
import os
import shutil
import subprocess
from pathlib import Path

brain_dir = Path(r"C:\Users\Administrator\.gemini\antigravity\brain\0169f376-faac-423f-9de2-77dde7e8eb51")
out_dir = Path(r"d:\jinyuliangyuan\公众号推文\封面图\今遇莨缘香云纱公众号推广文 2026-8-19  v1")
out_dir.mkdir(parents=True, exist_ok=True)

# 1. Source images in brain dir
img_a_src = brain_dir / "xiangyun_eco_fashion_model_1787108485699.jpg"
img_b_src = brain_dir / "xiangyun_sundrying_meadow_1787108666939.jpg"
img_c_src = brain_dir / "xiangyun_eco_macro_drape_1787108466918.jpg"

img_a_dst = out_dir / "xiangyun_eco_fashion_model_4K.jpg"
img_b_dst = out_dir / "xiangyun_eco_sundrying_meadow_4K.jpg"
img_c_dst = out_dir / "xiangyun_eco_macro_drape_4K.jpg"

if img_a_src.exists(): shutil.copy(img_a_src, img_a_dst)
if img_b_src.exists(): shutil.copy(img_b_src, img_b_dst)
if img_c_src.exists(): shutil.copy(img_c_src, img_c_dst)

print("Images copied to target directory.")

# 2. HTML Templates
def get_html(bg_img_name, option_title, img_pos="72% center"):
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>{option_title} - 1344x924</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;700;900&family=Cinzel:wght@600;700&display=swap');

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      width: 1344px;
      height: 924px;
      overflow: hidden;
      font-family: 'Noto Serif SC', 'Source Han Serif SC', serif;
      background-color: #140e0a;
      color: #ffffff;
      position: relative;
    }}

    .background-img {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: {img_pos};
      filter: brightness(1.02) contrast(1.15) saturate(1.18);
    }}

    /* Cinematic dark-gold gradient on the left for maximum readability */
    .overlay-gradient {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: 
        radial-gradient(circle at 18% 50%, rgba(12, 8, 6, 0.90) 0%, rgba(12, 8, 6, 0.50) 60%, transparent 100%),
        linear-gradient(to right, rgba(10, 7, 5, 0.96) 0%, rgba(10, 7, 5, 0.76) 45%, rgba(10, 7, 5, 0.12) 82%),
        linear-gradient(to top, rgba(8, 6, 4, 0.88) 0%, transparent 32%),
        linear-gradient(to bottom, rgba(8, 6, 4, 0.65) 0%, transparent 25%);
    }}

    /* Elegant double gold border frame */
    .border-frame {{
      position: absolute;
      top: 24px;
      left: 24px;
      right: 24px;
      bottom: 24px;
      border: 1px solid rgba(212, 175, 55, 0.65);
      pointer-events: none;
      box-shadow: inset 0 0 35px rgba(0, 0, 0, 0.4);
    }}

    .border-frame::before {{
      content: '';
      position: absolute;
      top: 6px;
      left: 6px;
      right: 6px;
      bottom: 6px;
      border: 1px solid rgba(212, 175, 55, 0.25);
    }}

    /* Main Container */
    .container {{
      position: relative;
      z-index: 10;
      height: 100%;
      padding: 64px 76px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    /* Header Badge */
    .header-badge {{
      display: inline-flex;
      align-items: center;
      gap: 12px;
      background: linear-gradient(135deg, rgba(212, 175, 55, 0.32), rgba(139, 90, 43, 0.42));
      border: 1px solid rgba(212, 175, 55, 0.85);
      backdrop-filter: blur(8px);
      padding: 10px 26px;
      border-radius: 4px;
      align-self: flex-start;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.35);
    }}

    .badge-icon {{
      width: 10px;
      height: 10px;
      background: #d4af37;
      transform: rotate(45deg);
      box-shadow: 0 0 12px #d4af37;
    }}

    .badge-text {{
      font-size: 18px;
      font-weight: 700;
      letter-spacing: 2px;
      color: #f5eaaf;
    }}

    /* Content Area (Optimized for WeChat 2.35:1 Center Safe Zone) */
    .content-box {{
      max-width: 930px;
      margin-top: 5px;
    }}

    .pre-title {{
      font-size: 32px;
      font-weight: 700;
      color: #f7d274;
      letter-spacing: 4px;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 16px;
      text-shadow: 0 2px 14px rgba(0, 0, 0, 0.95);
    }}

    .pre-title::after {{
      content: '';
      flex: 1;
      max-width: 140px;
      height: 2px;
      background: linear-gradient(to right, #d4af37, transparent);
    }}

    .main-title {{
      font-size: 42px;
      line-height: 1.36;
      font-weight: 900;
      color: #ffffff;
      text-shadow: 0 4px 24px rgba(0, 0, 0, 0.95);
      letter-spacing: 1.5px;
    }}

    .highlight-text {{
      background: linear-gradient(135deg, #ffffff 0%, #ffe08a 35%, #d4af37 75%, #b5831b 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: inline-block;
      filter: drop-shadow(0 2px 8px rgba(0, 0, 0, 0.8));
    }}

    .subtitle-box {{
      margin-top: 22px;
      padding-left: 22px;
      border-left: 4px solid #d4af37;
    }}

    .subtitle {{
      font-size: 23px;
      line-height: 1.48;
      color: #eae7e1;
      font-weight: 500;
      letter-spacing: 1px;
      text-shadow: 0 2px 12px rgba(0, 0, 0, 0.85);
    }}

    /* Footer Area */
    .footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid rgba(212, 175, 55, 0.4);
      padding-top: 22px;
    }}

    .footer-tags {{
      display: flex;
      gap: 28px;
      font-size: 17px;
      color: #dfbe76;
      letter-spacing: 2px;
      font-weight: 600;
    }}

    .footer-tag-item {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .footer-tag-item::before {{
      content: "✦";
      font-size: 14px;
      color: #d4af37;
    }}

    .brand-signature {{
      font-family: 'Cinzel', serif;
      font-size: 16px;
      letter-spacing: 4px;
      color: rgba(212, 175, 55, 0.9);
      text-transform: uppercase;
      font-weight: 700;
    }}
  </style>
</head>
<body>

  <img class="background-img" src="{bg_img_name}" alt="背景图">
  <div class="overlay-gradient"></div>
  <div class="border-frame"></div>

  <div class="container">
    
    <div class="header-badge">
      <div class="badge-icon"></div>
      <span class="badge-text">【今遇莨缘】 深圳南油非遗工坊 · 东方生态奢侈品</span>
    </div>

    <div class="content-box">
      <div class="pre-title">当全球时装遭遇“绿色清算”</div>
      <h1 class="main-title">
        为什么在日光与泥土里浸透的香云纱，<br>
        <span class="highlight-text">能成为穿越周期的生态硬通货？</span>
      </h1>
      <div class="subtitle-box">
        <p class="subtitle">告别化纤微塑料与快消反噬 · 千年古法天序的生态奢侈硬实力</p>
      </div>
    </div>

    <div class="footer">
      <div class="footer-tags">
        <span class="footer-tag-item">纯天然全降解</span>
        <span class="footer-tag-item">越穿越润时间资产</span>
        <span class="footer-tag-item">纯B端护城河</span>
      </div>
      <div class="brand-signature">XIANGYUN SILK ECOLOGICAL LUXURY</div>
    </div>

  </div>

</body>
</html>"""

options = [
    ("xiangyun_eco_fashion_model_4K.jpg", "封面图A - 现代高定版", "cover21_option_A_1344x924", "72% center"),
    ("xiangyun_eco_sundrying_meadow_4K.jpg", "封面图B - 生态晒莨草木古法版", "cover21_option_B_1344x924", "center center"),
    ("xiangyun_eco_macro_drape_4K.jpg", "封面图C - 自然垂褶意境版", "cover21_option_C_1344x924", "65% center")
]

render_script = r"C:\Users\Administrator\.gemini\config\skills\image-designer\scripts\render_banner.js"

for bg_img, title, name, pos in options:
    html_path = out_dir / f"{name}.html"
    jpg_path = out_dir / f"{name}.jpg"
    
    html_content = get_html(bg_img, title, pos)
    html_path.write_text(html_content, encoding='utf-8')
    print(f"Written HTML: {html_path}")
    
    # Run render_banner.js
    cmd = [
        "node",
        render_script,
        f"--html={str(html_path)}",
        f"--out={str(jpg_path)}",
        "--width=1344",
        "--height=924"
    ]
    print(f"Rendering {name}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)
        
    # Copy to brain dir for embedding
    brain_jpg = brain_dir / f"{name}.jpg"
    if jpg_path.exists():
        shutil.copy(jpg_path, brain_jpg)
        print(f"Copied to brain: {brain_jpg}")

print("All covers rendered successfully!")
