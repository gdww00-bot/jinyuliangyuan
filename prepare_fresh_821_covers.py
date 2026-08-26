# -*- coding: utf-8 -*-
import os
import shutil
import subprocess
from pathlib import Path
from PIL import Image

brain_dir = Path(r"C:\Users\Administrator\.gemini\antigravity\brain\0169f376-faac-423f-9de2-77dde7e8eb51")
out_dir = Path(r"d:\jinyuliangyuan\公众号推文\封面图\今遇莨缘香云纱公众号推广文 2026-8-21  v1")
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

# 1. Select 3 brand-new, never-before-used source images
src_a = Path(r"d:\jinyuliangyuan\AI视频\素材\Gemini_Generated_Image_bg3iombg3iombg3i.png")
src_b = Path(r"d:\jinyuliangyuan\AI视频\素材\中景.png")
src_c = Path(r"d:\jinyuliangyuan\AI视频\素材\远景.png")

dst_a = out_dir / "fresh_821_bg_option_A_4K.jpg"
dst_b = out_dir / "fresh_821_bg_option_B_4K.jpg"
dst_c = out_dir / "fresh_821_bg_option_C_4K.jpg"

Image.open(src_a).convert("RGB").save(dst_a, "JPEG", quality=98)
Image.open(src_b).convert("RGB").save(dst_b, "JPEG", quality=98)
Image.open(src_c).convert("RGB").save(dst_c, "JPEG", quality=98)

print("3 Brand-New Background Images saved to 8-21 folder.")

# 2. HTML Template generator
def get_cover_html(bg_img_name, option_title, img_pos="70% center"):
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
        radial-gradient(circle at 18% 50%, rgba(12, 8, 6, 0.92) 0%, rgba(12, 8, 6, 0.52) 60%, transparent 100%),
        linear-gradient(to right, rgba(10, 7, 5, 0.96) 0%, rgba(10, 7, 5, 0.78) 46%, rgba(10, 7, 5, 0.12) 82%),
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
      max-width: 950px;
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
      font-size: 41px;
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
      <span class="badge-text">【今遇莨缘】 深圳南油非遗工坊 · 东方品质正规军</span>
    </div>

    <div class="content-box">
      <div class="pre-title">市场监管重锤严打“假非遗”</div>
      <h1 class="main-title">
        直播间假真丝全面封禁：<br>
        <span class="highlight-text">谁在收割这一轮“正规军红利”？</span>
      </h1>
      <div class="subtitle-box">
        <p class="subtitle">告别虚假营销与低质劣质 · 经得起显微镜质检的源头手作硬实力</p>
      </div>
    </div>

    <div class="footer">
      <div class="footer-tags">
        <span class="footer-tag-item">严打假非遗真洗牌</span>
        <span class="footer-tag-item">100%特级桑蚕丝</span>
        <span class="footer-tag-item">纯B端源头大厂</span>
      </div>
      <div class="brand-signature">GENUINE HERITAGE · XIANGYUN SILK</div>
    </div>

  </div>

</body>
</html>"""

options = [
    ("fresh_821_bg_option_A_4K.jpg", "封面图A - 现代高定智性风 (全新图)", "cover23_option_A_1344x924", "72% center"),
    ("fresh_821_bg_option_B_4K.jpg", "封面图B - 早秋重工非遗风 (全新图)", "cover23_option_B_1344x924", "65% center"),
    ("fresh_821_bg_option_C_4K.jpg", "封面图C - 日光生态晒莨意境 (全新图)", "cover23_option_C_1344x924", "center center")
]

for bg_img, title, name, pos in options:
    html_path = out_dir / f"{name}.html"
    temp_png = out_dir / f"{name}_temp.png"
    jpg_path = out_dir / f"{name}.jpg"
    png_path = out_dir / f"{name}_超清2.6K.png"
    
    html_content = get_cover_html(bg_img, title, pos)
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

print("All fresh 8-21 covers rendered successfully in Ultra HD!")
