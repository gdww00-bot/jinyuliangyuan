# -*- coding: utf-8 -*-
import os
import subprocess
from pathlib import Path
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_dir = Path(r"d:\jinyuliangyuan\公众号推文\封面图\今遇莨缘香云纱公众号推广文 2026-8-19  v1")
brain_dir = Path(r"C:\Users\Administrator\.gemini\antigravity\brain\0169f376-faac-423f-9de2-77dde7e8eb51")

options = [
    "cover21_option_A_1344x924",
    "cover21_option_B_1344x924",
    "cover21_option_C_1344x924"
]

for name in options:
    html_path = out_dir / f"{name}.html"
    temp_png = out_dir / f"{name}_temp_2x.png"
    final_jpg = out_dir / f"{name}.jpg"
    final_png = out_dir / f"{name}_超清2.6K.png"
    final_2k_jpg = out_dir / f"{name}_超清2.6K.jpg"
    
    file_url = f"file:///{str(html_path).replace(os.sep, '/')}"
    
    # Render with 2x scale factor (2688x1848)
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--force-device-scale-factor=2",
        f"--window-size=1344,924",
        f"--screenshot={str(temp_png)}",
        file_url
    ]
    
    print(f"Rendering {name} with 2x scale factor...")
    res = subprocess.run(cmd, capture_output=True)
    
    if not temp_png.exists():
        print(f"Error: {temp_png} not found")
        continue
        
    img = Image.open(temp_png)
    print(f"Rendered image size: {img.size}") # Should be 2688 x 1848
    
    # Save Lossless PNG
    img.save(final_png, format="PNG")
    
    # Save Ultra HD 2.6K JPG with max quality (quality=98, subsampling=0)
    img.convert("RGB").save(final_2k_jpg, format="JPEG", quality=98, subsampling=0)
    
    # Also overwrite the primary cover21_option_X_1344x924.jpg with the 2x Ultra HD quality (or 100% quality)
    # WeChat official account supports images up to 10MB! A 2688x1848 2-3MB image uploads flawlessly and displays ultra crisp on Retina/mobile screens!
    img.convert("RGB").save(final_jpg, format="JPEG", quality=98, subsampling=0)
    
    # Clean up temp
    if temp_png.exists():
        temp_png.unlink()
        
    # Copy to brain dir
    shutil_jpg = brain_dir / f"{name}.jpg"
    img.convert("RGB").save(shutil_jpg, format="JPEG", quality=98, subsampling=0)
    
    print(f"Saved: {final_jpg} ({final_jpg.stat().st_size / 1024 / 1024:.2f} MB)")
    print(f"Saved: {final_2k_jpg} ({final_2k_jpg.stat().st_size / 1024 / 1024:.2f} MB)")
    print(f"Saved: {final_png} ({final_png.stat().st_size / 1024 / 1024:.2f} MB)")

print("Ultra HD re-rendering complete!")
