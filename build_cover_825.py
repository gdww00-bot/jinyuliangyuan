# -*- coding: utf-8 -*-
import os
import shutil
import subprocess
import numpy as np
from pathlib import Path
from PIL import Image, ImageFilter, ImageDraw

brain_dir = Path(r"C:\Users\Administrator\.gemini\antigravity\brain\0169f376-faac-423f-9de2-77dde7e8eb51")
out_dir = Path(r"d:\jinyuliangyuan\公众号推文\封面图\今遇莨缘香云纱公众号推广文 2026-8-25  v1")
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

# Function to generate unique procedural silk backgrounds
def make_silk_texture(width=2688, height=1848, style="obsidian", seed=101):
    np.random.seed(seed)
    y = np.linspace(0, 1, height)[:, None]
    x = np.linspace(0, 1, width)[None, :]
    
    if style == "obsidian":
        # Deep Obsidian & Bronze Sheen
        light_map = 0.65 * np.exp(-((x - 0.78)**2 + (y - 0.38)**2) / 0.38) + 0.35 * (1 - y * 0.4)
        base_r = 12 + (52 - 12) * light_map + 28 * np.exp(-((x - 0.72)**2 + (y - 0.42)**2) / 0.12)
        base_g = 9 + (32 - 9) * light_map + 18 * np.exp(-((x - 0.72)**2 + (y - 0.42)**2) / 0.12)
        base_b = 7 + (22 - 7) * light_map + 10 * np.exp(-((x - 0.72)**2 + (y - 0.42)**2) / 0.12)
        gold_color = (212, 175, 55)
    elif style == "umber":
        # Cinnabar Umber & Mineral Tannin
        light_map = 0.6 * np.exp(-((x - 0.8)**2 + (y - 0.3)**2) / 0.42) + 0.4 * (1 - y * 0.5)
        base_r = 22 + (70 - 22) * light_map + 35 * np.exp(-((x - 0.75)**2 + (y - 0.35)**2) / 0.15)
        base_g = 12 + (36 - 12) * light_map + 18 * np.exp(-((x - 0.75)**2 + (y - 0.35)**2) / 0.15)
        base_b = 8 + (24 - 8) * light_map + 10 * np.exp(-((x - 0.75)**2 + (y - 0.35)**2) / 0.15)
        gold_color = (225, 185, 80)
    else: # "charcoal"
        # Charcoal Ink & Golden Morning Ray
        light_map = 0.7 * np.exp(-((x - 0.85)**2 + (y - 0.25)**2) / 0.5) + 0.3 * (1 - y * 0.3)
        base_r = 10 + (42 - 10) * light_map + 24 * np.exp(-((x - 0.8)**2 + (y - 0.3)**2) / 0.14)
        base_g = 10 + (35 - 10) * light_map + 20 * np.exp(-((x - 0.8)**2 + (y - 0.3)**2) / 0.14)
        base_b = 10 + (28 - 10) * light_map + 14 * np.exp(-((x - 0.8)**2 + (y - 0.3)**2) / 0.14)
        gold_color = (235, 195, 95)
        
    weave_h = np.sin(np.arange(height)[:, None] * 2.0) * 2.2
    weave_v = np.sin(np.arange(width)[None, :] * 2.0) * 2.2
    weave = weave_h + weave_v
    noise = np.random.normal(0, 3.5, (height, width))
    
    r = np.clip(base_r + weave + noise * 0.5, 0, 255).astype(np.uint8)
    g = np.clip(base_g + weave + noise * 0.4, 0, 255).astype(np.uint8)
    b = np.clip(base_b + weave + noise * 0.3, 0, 255).astype(np.uint8)
    
    img = Image.fromarray(np.stack([r, g, b], axis=-1), mode='RGB')
    img = img.filter(ImageFilter.GaussianBlur(radius=0.5))
    
    # Overlay craquelure and gold flecks
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    num_points = 450
    pts_x = np.random.uniform(width * 0.35, width * 1.05, num_points)
    pts_y = np.random.uniform(0, height, num_points)
    
    for i in range(num_points):
        x1, y1 = pts_x[i], pts_y[i]
        dists = (pts_x - x1)**2 + (pts_y - y1)**2
        nearest = np.argsort(dists)[1:4]
        for n_idx in nearest:
            if dists[n_idx] < 230**2:
                x2, y2 = pts_x[n_idx], pts_y[n_idx]
                mx, my = (x1 + x2)/2 + np.random.uniform(-18, 18), (y1 + y2)/2 + np.random.uniform(-18, 18)
                alpha = int(np.random.uniform(20, 60) * (0.2 + 0.8 * (x1 / width)))
                draw.line([(x1, y1), (mx, my), (x2, y2)], fill=(gold_color[0], gold_color[1], gold_color[2], alpha), width=np.random.choice([1, 2]))
                
    for _ in range(700):
        gx = np.random.uniform(width * 0.3, width)
        gy = np.random.uniform(0, height)
        alpha = int(np.random.uniform(30, 110) * (0.3 + 0.7 * (gx / width)))
        draw.ellipse([gx, gy, gx + np.random.uniform(1.2, 4.0), gy + np.random.uniform(1.2, 4.0)], 
                     fill=(gold_color[0], gold_color[1], gold_color[2], alpha))
                     
    overlay = overlay.filter(ImageFilter.GaussianBlur(radius=0.7))
    img.paste(Image.alpha_composite(Image.new("RGBA", (width, height), (0,0,0,255)), overlay).convert("RGB"), (0,0), overlay)
    return img

print("Generating 3 unique 2.6K procedural silk textures...")
tex_a = make_silk_texture(2688, 1848, "obsidian", seed=2026)
tex_b = make_silk_texture(2688, 1848, "umber", seed=8888)
tex_c = make_silk_texture(2688, 1848, "charcoal", seed=9999)

bg_a_path = out_dir / "procedural_silk_bg_A.jpg"
bg_b_path = out_dir / "procedural_silk_bg_B.jpg"
bg_c_path = out_dir / "procedural_silk_bg_C.jpg"

tex_a.save(bg_a_path, quality=98)
tex_b.save(bg_b_path, quality=98)
tex_c.save(bg_c_path, quality=98)
print("Background textures generated and saved.")

# HTML Template Generator for 8-25
def get_cover_html(bg_img_name, option_title, theme_accent="#d4af37"):
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
      background-color: #0f0a07;
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
      filter: brightness(1.03) contrast(1.18) saturate(1.15);
    }}

    /* Cinematic dark-gold gradient on left */
    .overlay-gradient {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: 
        radial-gradient(circle at 18% 50%, rgba(10, 7, 5, 0.95) 0%, rgba(10, 7, 5, 0.65) 58%, transparent 100%),
        linear-gradient(to right, rgba(8, 5, 4, 0.98) 0%, rgba(8, 5, 4, 0.85) 44%, rgba(8, 5, 4, 0.22) 80%),
        linear-gradient(to top, rgba(6, 4, 3, 0.9) 0%, transparent 30%),
        linear-gradient(to bottom, rgba(6, 4, 3, 0.7) 0%, transparent 25%);
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
      box-shadow: inset 0 0 40px rgba(0, 0, 0, 0.5);
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
      padding: 62px 76px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    /* Header Badge */
    .header-badge {{
      display: inline-flex;
      align-items: center;
      gap: 12px;
      background: linear-gradient(135deg, rgba(212, 175, 55, 0.28), rgba(139, 90, 43, 0.38));
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

    /* Content Area (Safe Zone for WeChat 2.35:1) */
    .content-box {{
      max-width: 960px;
      margin-top: 6px;
    }}

    .pre-title {{
      font-size: 30px;
      font-weight: 700;
      color: #f7d274;
      letter-spacing: 4px;
      margin-bottom: 15px;
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
      font-size: 40px;
      line-height: 1.38;
      font-weight: 900;
      color: #ffffff;
      text-shadow: 0 4px 26px rgba(0, 0, 0, 0.98);
      letter-spacing: 1.5px;
    }}

    .highlight-text {{
      background: linear-gradient(135deg, #ffffff 0%, #ffe08a 35%, #d4af37 75%, #b5831b 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: inline-block;
      filter: drop-shadow(0 2px 10px rgba(0, 0, 0, 0.85));
    }}

    .subtitle-box {{
      margin-top: 22px;
      padding-left: 22px;
      border-left: 4px solid #d4af37;
    }}

    .subtitle {{
      font-size: 22px;
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
      padding-top: 20px;
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
      <span class="badge-text">【今遇莨缘】 深圳南油非遗工坊 · 东方无声权威</span>
    </div>

    <div class="content-box">
      <div class="pre-title">2026 早秋高知名流的穿衣哲学</div>
      <h1 class="main-title">
        不显山露水的压迫感：<br>
        <span class="highlight-text">为什么都在穿“无声权威”的重工香云纱？</span>
      </h1>
      <div class="subtitle-box">
        <p class="subtitle">撕碎浮夸Logo与软塌茶服 · 历经天地日光淬炼的东方终极战袍</p>
      </div>
    </div>

    <div class="footer">
      <div class="footer-tags">
        <span class="footer-tag-item">智性大女主战袍</span>
        <span class="footer-tag-item">黑曜石内敛暗光</span>
        <span class="footer-tag-item">纯B端源头大厂</span>
      </div>
      <div class="brand-signature">SILENT AUTHORITY · XIANGYUN SILK</div>
    </div>

  </div>

</body>
</html>"""

options = [
    ("procedural_silk_bg_A.jpg", "封面图A - 黑曜金箔无声权威版", "cover24_option_A_1344x924", "#d4af37"),
    ("procedural_silk_bg_B.jpg", "封面图B - 古铜朱赭矿物单宁版", "cover24_option_B_1344x924", "#e1b950"),
    ("procedural_silk_bg_C.jpg", "封面图C - 深邃松烟晨曦金光版", "cover24_option_C_1344x924", "#ebc35f")
]

for bg_img, title, name, accent in options:
    html_path = out_dir / f"{name}.html"
    temp_png = out_dir / f"{name}_temp.png"
    jpg_path = out_dir / f"{name}.jpg"
    png_path = out_dir / f"{name}_超清2.6K.png"
    
    html_content = get_cover_html(bg_img, title, accent)
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

print("All 8-25 covers rendered successfully in Ultra HD!")
