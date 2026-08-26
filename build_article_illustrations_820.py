# -*- coding: utf-8 -*-
import os
import shutil
import subprocess
from pathlib import Path
from PIL import Image

brain_dir = Path(r"C:\Users\Administrator\.gemini\antigravity\brain\0169f376-faac-423f-9de2-77dde7e8eb51")
out_dir = Path(r"d:\jinyuliangyuan\公众号推文\封面图\今遇莨缘香云纱公众号推广文 2026-8-20  v1")
out_dir.mkdir(parents=True, exist_ok=True)

# Find Chromium browser
browser_candidates = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]
chrome_path = None
for cand in browser_candidates:
    if os.path.exists(cand):
        chrome_path = cand
        break

if not chrome_path:
    raise RuntimeError("No Chromium browser found!")

print(f"Using browser: {chrome_path}")

# 1. Source AI background images
bg_sources = {
    "xiangyun_boutique_tactile_fabric_4K.jpg": brain_dir / "xiangyun_boutique_tactile_fabric_1787191148345.jpg",
    "xiangyun_blazer_power_female_4K.jpg": brain_dir / "xiangyun_blazer_power_female_1787192048947.jpg",
    "xiangyun_nanyou_luxury_atelier_4K.jpg": brain_dir / "xiangyun_nanyou_luxury_atelier_1787120792179.jpg",
    "xiangyun_tactile_macro_touch_4K.jpg": brain_dir / "xiangyun_tactile_macro_touch_1787191109420.jpg"
}

for dst_name, src_path in bg_sources.items():
    if src_path.exists():
        shutil.copy(src_path, out_dir / dst_name)
        print(f"Copied {src_path.name} -> {dst_name}")

# 2. Template generator for editorial illustrations (2560x1440)
def get_editorial_html(bg_img_name, badge_text, pre_title, main_title, subtitle, tags, signature, img_pos="center center"):
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

# 3. Infographic HTML for 配图 4 (2560x1440)
def get_infographic_html():
    return """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>配图4 - 无法被算法虚拟的三大感官态与大厂护城河 (2560x1440)</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;700;900&family=Cinzel:wght@600;700&display=swap');

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      width: 2560px;
      height: 1440px;
      overflow: hidden;
      font-family: 'Noto Serif SC', 'Source Han Serif SC', serif;
      background-color: #120d0a;
      color: #ffffff;
      position: relative;
    }}

    .background-img {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      object-fit: cover;
      object-position: center center;
      filter: brightness(0.78) contrast(1.2) saturate(1.15);
    }

    .overlay-gradient {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      background: 
        radial-gradient(circle at 50% 45%, rgba(15, 10, 8, 0.88) 0%, rgba(10, 8, 6, 0.96) 88%),
        linear-gradient(to bottom, rgba(12, 9, 7, 0.92) 0%, rgba(12, 9, 7, 0.70) 50%, rgba(10, 8, 6, 0.97) 100%);
    }

    .border-frame {
      position: absolute;
      top: 40px; left: 40px; right: 40px; bottom: 40px;
      border: 2px solid rgba(212, 175, 55, 0.55);
      pointer-events: none;
      box-shadow: inset 0 0 50px rgba(0, 0, 0, 0.6);
    }

    .border-frame::before {
      content: '';
      position: absolute;
      top: 10px; left: 10px; right: 10px; bottom: 10px;
      border: 1px solid rgba(212, 175, 55, 0.25);
    }

    .container {
      position: relative;
      z-index: 10;
      height: 100%;
      padding: 75px 100px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
    }

    .header-badge {
      display: inline-flex;
      align-items: center;
      gap: 16px;
      background: linear-gradient(135deg, rgba(212, 175, 55, 0.28), rgba(139, 90, 43, 0.38));
      border: 1.5px solid rgba(212, 175, 55, 0.85);
      backdrop-filter: blur(12px);
      padding: 14px 42px;
      border-radius: 6px;
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
    }

    .badge-icon {
      width: 14px;
      height: 14px;
      background: #d4af37;
      transform: rotate(45deg);
      box-shadow: 0 0 12px #d4af37;
    }

    .badge-text {
      font-size: 26px;
      font-weight: 700;
      letter-spacing: 3px;
      color: #f5eaaf;
    }

    .title-box {
      text-align: center;
      margin-top: 5px;
    }

    .main-title {
      font-size: 58px;
      line-height: 1.35;
      font-weight: 900;
      color: #ffffff;
      text-shadow: 0 6px 28px rgba(0, 0, 0, 0.95);
      letter-spacing: 2px;
    }

    .highlight-text {
      background: linear-gradient(135deg, #ffffff 0%, #ffe08a 35%, #d4af37 75%, #b5831b 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: inline-block;
    }

    .subtitle {
      font-size: 27px;
      color: #dfdbd3;
      font-weight: 500;
      letter-spacing: 2.5px;
      margin-top: 12px;
      text-shadow: 0 3px 14px rgba(0, 0, 0, 0.9);
    }

    .grid-container {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 30px;
      width: 100%;
      margin: 25px 0;
    }

    .card-item {
      background: rgba(24, 18, 14, 0.75);
      border: 1.5px solid rgba(212, 175, 55, 0.42);
      backdrop-filter: blur(16px);
      padding: 36px 28px;
      border-radius: 10px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      box-shadow: 0 14px 40px rgba(0, 0, 0, 0.6);
    }

    .card-header {
      display: flex;
      align-items: center;
      gap: 14px;
      border-bottom: 1.5px solid rgba(212, 175, 55, 0.3);
      padding-bottom: 14px;
    }

    .card-number {
      font-family: 'Cinzel', serif;
      font-size: 36px;
      font-weight: 700;
      color: #d4af37;
      line-height: 1;
    }

    .card-title {
      font-size: 25px;
      font-weight: 700;
      color: #f5eaaf;
      letter-spacing: 1.5px;
    }

    .card-desc {
      font-size: 19px;
      line-height: 1.68;
      color: #dedad2;
      font-weight: 400;
    }

    .footer {
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1.5px solid rgba(212, 175, 55, 0.4);
      padding-top: 22px;
    }

    .footer-tags {
      display: flex;
      gap: 36px;
      font-size: 21px;
      color: #dfbe76;
      letter-spacing: 2.5px;
      font-weight: 600;
    }

    .footer-tag-item::before {
      content: "✦ ";
      color: #d4af37;
    }

    .brand-signature {
      font-family: 'Cinzel', serif;
      font-size: 21px;
      letter-spacing: 5px;
      color: rgba(212, 175, 55, 0.85);
      font-weight: 700;
    }
  </style>
</head>
<body>

  <img class="background-img" src="xiangyun_boutique_tactile_fabric_4K.jpg" alt="背景">
  <div class="overlay-gradient"></div>
  <div class="border-frame"></div>

  <div class="container">
    
    <div class="header-badge">
      <div class="badge-icon"></div>
      <span class="badge-text">【今遇莨缘】 核心价值解析 · 构筑实体感官壁垒</span>
    </div>

    <div class="title-box">
      <h1 class="main-title">
        无法被算法虚拟的<span class="highlight-text">三大物理感官态与大厂壁垒</span>
      </h1>
      <p class="subtitle">告别像素脱水与算法虚假 · 以真实物质颗粒度与古法天序构筑实体护城河</p>
    </div>

    <div class="grid-container">
      
      <!-- Card 1 -->
      <div class="card-item">
        <div class="card-header">
          <span class="card-number">01</span>
          <h3 class="card-title">指尖触觉沉坠</h3>
        </div>
        <p class="card-desc">
          深山野生薯莨与富铁河泥古法过乌，初触如抚古玉般微凉透气，手指抚过凹凸肌理带来诚实的物理安全感。
        </p>
      </div>

      <!-- Card 2 -->
      <div class="card-item">
        <div class="card-header">
          <span class="card-number">02</span>
          <h3 class="card-title">响云沙沙白噪音</h3>
        </div>
        <p class="card-desc">
          十八晒十八莨淬炼致密骨骼。走动间衣袂摩擦发出低沉克制的“沙沙”声，成为高端女性步步生风的无声BGM。
        </p>
      </div>

      <!-- Card 3 -->
      <div class="card-item">
        <div class="card-header">
          <span class="card-number">03</span>
          <h3 class="card-title">随体温包浆熟化</h3>
        </div>
        <p class="card-desc">
          时间复利活态资产。随穿着者体温与皮肤天然油脂滋润二次熟化，越穿越润越值钱，彻底撕碎快消贬值诅咒。
        </p>
      </div>

      <!-- Card 4 -->
      <div class="card-item">
        <div class="card-header">
          <span class="card-number">04</span>
          <h3 class="card-title">纯B端大厂边界</h3>
        </div>
        <p class="card-desc">
          全渠道坚决谢绝零散客、不开直播破价。千亩晒莨基地大货直供，小单柔性快反，100%利润让渡实体。
        </p>
      </div>

    </div>

    <div class="footer">
      <div class="footer-tags">
        <span class="footer-tag-item">深圳南油名品馆103</span>
        <span class="footer-tag-item">纯手工非遗生态母本</span>
        <span class="footer-tag-item">高客单利润护城河</span>
      </div>
      <div class="brand-signature">JINYU LANGYUAN · SENSORY & BUSINESS BARRIERS</div>
    </div>

  </div>

</body>
</html>"""

# Define illustrations 1, 2, 3
illustrations = [
    {
        "filename": "配图1_算法无法复制的指尖重量与触觉安全感_2.6K",
        "bg_img": "xiangyun_boutique_tactile_fabric_4K.jpg",
        "badge": "【今遇莨缘】 具身认知安全感 · 东方物理图腾",
        "pre_title": "触觉饥渴反扑：算法算不出指尖重量",
        "main_title": "手指划过野生薯莨揉搓的天然凹凸肌理：<span class=\"highlight-text\">初触如玉的微凉，无法被算法克隆</span>",
        "subtitle": "沉淀特定河床铁盐的沉坠分量 · 身体在触碰织物的刹那做出最诚实的价值判断",
        "tags": ["触觉饥渴本能反扑", "具身认知安全感", "初触如玉温润微凉", "零化学添加"],
        "signature": "TACTILE HUNGER & SENSORY SECURITY",
        "pos": "65% center"
    },
    {
        "filename": "配图2_步步生风响云白噪音与现代大女主战袍_2.6K",
        "bg_img": "xiangyun_blazer_power_female_4K.jpg",
        "badge": "【今遇莨缘】 现代立裁骨架 · 对抗快消贬值诅咒",
        "pre_title": "步步带风的身份BGM · 现代智性廓形",
        "main_title": "行走间低沉沙沙的“响云白噪音”：<span class=\"highlight-text\">赋予东方独立大女主雷厉风行的风骨气场</span>",
        "subtitle": "干练垫肩西装与极简风衣立体剪裁 · 随体温油脂二次包浆熟化，越穿越润的时间资产",
        "tags": ["响云沙沙白噪音", "现代垫肩西装/风衣", "随体温包浆熟化", "高知独立战袍"],
        "signature": "HAUTE COUTURE INTELLECTUAL SUIT",
        "pos": "center 28%"
    },
    {
        "filename": "配图3_深圳南油今遇莨缘品鉴中心纯B端大厂_2.6K",
        "bg_img": "xiangyun_nanyou_luxury_atelier_4K.jpg",
        "badge": "【今遇莨缘】 深圳南油品鉴中心 · 纯B端护城河",
        "pre_title": "恪守大厂边界 · 全渠道坚决谢绝零散客",
        "main_title": "千亩生态晒莨基地源头大货直供：<span class=\"highlight-text\">将100%定价自主权与利润护城河让渡实体</span>",
        "subtitle": "原创典籍图腾壁垒 · 小单柔性快反补单 · 随货配套国际水准高清画册与话术库",
        "tags": ["深圳南油103名品馆", "坚决不开直播破价", "小单柔性快反", "全案视觉物料交付"],
        "signature": "EXCLUSIVE B2B ATELIER SHENZHEN",
        "pos": "center center"
    }
]

# Generate HTML files
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

# Generate 配图4 HTML
html4_file = out_dir / "配图4_无法被算法虚拟的三大感官态与大厂护城河_2.6K.html"
html4_file.write_text(get_infographic_html(), encoding='utf-8')
print(f"Generated HTML: {html4_file.name}")

# Render targets
render_targets = [
    out_dir / "配图1_算法无法复制的指尖重量与触觉安全感_2.6K.html",
    out_dir / "配图2_步步生风响云白噪音与现代大女主战袍_2.6K.html",
    out_dir / "配图3_深圳南油今遇莨缘品鉴中心纯B端大厂_2.6K.html",
    out_dir / "配图4_无法被算法虚拟的三大感官态与大厂护城河_2.6K.html"
]

print("Rendering all 4 article illustrations with Chromium headless in Ultra HD (2560x1440)...")

for html_p in render_targets:
    stem = html_p.stem
    temp_png = out_dir / f"{stem}_temp.png"
    final_png = out_dir / f"{stem}.png"
    final_jpg = out_dir / f"{stem}.jpg"
    
    file_url = f"file:///{str(html_p).replace(os.sep, '/')}"
    
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
        # Lossless PNG
        img.save(final_png, format="PNG")
        # 98% Ultra HD JPG
        img.convert("RGB").save(final_jpg, format="JPEG", quality=98, subsampling=0)
        
        temp_png.unlink()
        
        # Copy to brain dir
        brain_jpg = brain_dir / f"{stem}.jpg"
        img.convert("RGB").save(brain_jpg, format="JPEG", quality=98, subsampling=0)
        
        print(f"Rendered: {stem}.jpg ({final_jpg.stat().st_size / 1024 / 1024:.2f} MB, {img.size[0]}x{img.size[1]})")
        print(f"Rendered: {stem}.png ({final_png.stat().st_size / 1024 / 1024:.2f} MB)")

print("All 4 article illustrations completed successfully in the 8-20 folder!")
