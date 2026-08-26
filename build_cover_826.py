# -*- coding: utf-8 -*-
import os
import shutil
import subprocess
from pathlib import Path
from PIL import Image

brain_dir = Path(r"C:\Users\Administrator\.gemini\antigravity\brain\0169f376-faac-423f-9de2-77dde7e8eb51")
out_dir = Path(r"d:\jinyuliangyuan\公众号推文\封面图\今遇莨缘香云纱公众号推广文 2026-8-26  v1")
out_dir.mkdir(parents=True, exist_ok=True)

# Locate Edge / Chrome
browser_candidates = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]
chrome_path = None
for cand in browser_candidates:
    if os.path.exists(cand):
        chrome_path = cand
        break

if not chrome_path:
    raise RuntimeError("No Chromium browser found!")

print(f"Using browser: {chrome_path}")

# Source high-res background photography images
src_a = brain_dir / "brand_new_tactile_vip_touch_1787193346525.jpg"
src_b = brain_dir / "brand_new_skyline_power_woman_1787193355401.jpg"
src_c = brain_dir / "brand_new_acoustic_motion_staircase_1787193422598.jpg"

dst_a = out_dir / "bg_option_A_boutique_vip_fitting.jpg"
dst_b = out_dir / "bg_option_B_skyline_power_woman.jpg"
dst_c = out_dir / "bg_option_C_acoustic_staircase.jpg"

if src_a.exists(): shutil.copy(src_a, dst_a)
if src_b.exists(): shutil.copy(src_b, dst_b)
if src_c.exists(): shutil.copy(src_c, dst_c)

print("Background images copied to 8-26 folder.")

# HTML Template Generator for 8-26
def get_cover_html(bg_img_name, option_title, img_pos="72% center", img_brightness="1.06"):
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>{option_title} - 1344x924</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;700;900&family=Cinzel:wght@600;700;800&display=swap');

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
      background-color: #0c0806;
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
      filter: brightness({img_brightness}) contrast(1.12) saturate(1.15);
    }}

    /* Cinematic dark-gold gradient: dark on left for text legibility, CLEAR AND BRIGHT on right for model */
    .overlay-gradient {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: 
        radial-gradient(circle at 18% 50%, rgba(10, 7, 5, 0.95) 0%, rgba(10, 7, 5, 0.58) 55%, transparent 100%),
        linear-gradient(to right, rgba(8, 5, 4, 0.98) 0%, rgba(8, 5, 4, 0.88) 38%, rgba(8, 5, 4, 0.35) 65%, rgba(8, 5, 4, 0.02) 88%),
        linear-gradient(to top, rgba(6, 4, 3, 0.88) 0%, transparent 26%),
        linear-gradient(to bottom, rgba(6, 4, 3, 0.72) 0%, transparent 22%);
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

    /* Corner ornamental flourishes */
    .corner-tl, .corner-tr, .corner-bl, .corner-br {{
      position: absolute;
      width: 16px;
      height: 16px;
      border: 2px solid #d4af37;
      pointer-events: none;
    }}
    .corner-tl {{ top: 20px; left: 20px; border-right: none; border-bottom: none; }}
    .corner-tr {{ top: 20px; right: 20px; border-left: none; border-bottom: none; }}
    .corner-bl {{ bottom: 20px; left: 20px; border-right: none; border-top: none; }}
    .corner-br {{ bottom: 20px; right: 20px; border-left: none; border-top: none; }}

    /* Main Container */
    .container {{
      position: relative;
      z-index: 10;
      height: 100%;
      padding: 60px 76px;
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
      backdrop-filter: blur(10px);
      padding: 10px 24px;
      border-radius: 4px;
      align-self: flex-start;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
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
      color: #f7ebc2;
    }}

    /* Content Area (Optimized for WeChat 2.35:1 Safe Zone) */
    .content-box {{
      max-width: 960px;
      margin-top: 4px;
    }}

    .pre-title {{
      font-size: 28px;
      font-weight: 700;
      color: #f7d274;
      letter-spacing: 4px;
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 16px;
      text-shadow: 0 2px 14px rgba(0, 0, 0, 0.95);
    }}

    .pre-title::after {{
      content: '';
      flex: 1;
      max-width: 150px;
      height: 2px;
      background: linear-gradient(to right, #d4af37, transparent);
    }}

    .main-title {{
      font-size: 38px;
      line-height: 1.36;
      font-weight: 900;
      color: #ffffff;
      text-shadow: 0 4px 26px rgba(0, 0, 0, 0.98);
      letter-spacing: 1px;
    }}

    .highlight-text {{
      background: linear-gradient(135deg, #ffffff 0%, #ffe08a 35%, #d4af37 75%, #b5831b 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: inline-block;
      filter: drop-shadow(0 2px 10px rgba(0, 0, 0, 0.85));
    }}

    .subtitle-box {{
      margin-top: 20px;
      padding-left: 20px;
      border-left: 4px solid #d4af37;
    }}

    .subtitle {{
      font-size: 21px;
      line-height: 1.48;
      color: #eae5dc;
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
      padding-top: 18px;
    }}

    .footer-tags {{
      display: flex;
      gap: 26px;
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
  <div class="corner-tl"></div>
  <div class="corner-tr"></div>
  <div class="corner-bl"></div>
  <div class="corner-br"></div>

  <div class="container">
    
    <div class="header-badge">
      <div class="badge-icon"></div>
      <span class="badge-text">【今遇莨缘】 深圳南油非遗工坊 · 超级私域高客单</span>
    </div>

    <div class="content-box">
      <div class="pre-title">2026 实体零售洗牌新分化</div>
      <h1 class="main-title">
        大众连锁集体闭店，买手店逆势爆单：<br>
        <span class="highlight-text">谁在靠“超级私域+非遗孤品”赚翻了？</span>
      </h1>
      <div class="subtitle-box">
        <p class="subtitle">放弃平庸规模与低价内卷 · 靠100个高净值私域客户实现单店高盈利</p>
      </div>
    </div>

    <div class="footer">
      <div class="footer-tags">
        <span class="footer-tag-item">单店盈利新模型</span>
        <span class="footer-tag-item">无法比价非遗孤品</span>
        <span class="footer-tag-item">纯B端源头大厂</span>
      </div>
      <div class="brand-signature">SUPER PRIVATE DOMAIN · XIANGYUN SILK</div>
    </div>

  </div>

</body>
</html>"""

options = [
    ("bg_option_A_boutique_vip_fitting.jpg", "封面图A - 高端买手店私域VIP沙龙试穿版", "cover25_option_A_1344x924", "70% center", "1.08"),
    ("bg_option_B_skyline_power_woman.jpg", "封面图B - 独立大女主天际线战袍版", "cover25_option_B_1344x924", "78% center", "1.08"),
    ("bg_option_C_acoustic_staircase.jpg", "封面图C - 艺术沙龙步步生风白噪音版", "cover25_option_C_1344x924", "72% center", "1.10")
]

for bg_img, title, name, pos, bright in options:
    html_path = out_dir / f"{name}.html"
    temp_png = out_dir / f"{name}_temp.png"
    jpg_path = out_dir / f"{name}.jpg"
    png_path = out_dir / f"{name}_超清2.6K.png"
    
    html_content = get_cover_html(bg_img, title, pos, bright)
    html_path.write_text(html_content, encoding='utf-8')
    print(f"Written HTML: {html_path.name}")
    
    file_url = f"file:///{str(html_path).replace(os.sep, '/')}"
    
    # Render with 2x Device Scale Factor (2688 x 1848)
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--force-device-scale-factor=2",
        "--window-size=1344,924",
        f"--screenshot={str(temp_png)}",
        file_url
    ]
    
    subprocess.run(cmd, capture_output=True)
    
    if temp_png.exists():
        img = Image.open(temp_png)
        # Lossless PNG
        img.save(png_path, format="PNG")
        # 98% Ultra HD JPG
        img.convert("RGB").save(jpg_path, format="JPEG", quality=98, subsampling=0)
        
        temp_png.unlink()
        
        # Copy to brain dir for embedding
        brain_jpg = brain_dir / f"{name}.jpg"
        img.convert("RGB").save(brain_jpg, format="JPEG", quality=98, subsampling=0)
        
        print(f"Rendered {name}: JPG={jpg_path.stat().st_size / 1024 / 1024:.2f} MB, PNG={png_path.stat().st_size / 1024 / 1024:.2f} MB ({img.size[0]}x{img.size[1]})")

print("All 8-26 covers rendered successfully in Ultra HD!")
