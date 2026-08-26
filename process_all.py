# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np
from pathlib import Path

def load_img(path):
    return cv2.imdecode(np.fromfile(str(path), dtype=np.uint8), cv2.IMREAD_COLOR)

def save_img(path, img):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    ext = path.suffix
    cv2.imencode(ext, img, [cv2.IMWRITE_JPEG_QUALITY, 100])[1].tofile(str(path))

base_dir = Path(r"d:\jinyuliangyuan")
gw_dir = base_dir / "官网素材"
backup_dir = gw_dir / "衣服_backup"

# Locate reference 48 and 51
ref48_path = gw_dir / "微信图片_20260804154249_48_757.jpg"
if not ref48_path.exists():
    ref48_path = backup_dir / "微信图片_20260804154249_48_757.jpg"

ref51_path = gw_dir / "微信图片_20260804154252_51_757.jpg"
if not ref51_path.exists():
    ref51_path = backup_dir / "微信图片_20260804154252_51_757.jpg"

print(f"Ref 48 path: {ref48_path}")
print(f"Ref 51 path: {ref51_path}")

img48 = load_img(ref48_path)
# Extract AN patch from 48 (y: 242..278, x: 1084..1174)
an48 = img48[242:278, 1084:1174].astype(np.float32)
gray48 = cv2.cvtColor(an48.astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32)
bg48 = np.percentile(gray48, 10)
alpha48 = np.clip((gray48 - bg48) / (255.0 - bg48), 0, 1)

img51 = load_img(ref51_path)
# Extract AN patch from 51 (y: 1795..1835, x: 1007..1115)
an51 = img51[1795:1835, 1007:1115].astype(np.float32)
gray51 = cv2.cvtColor(an51.astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32)
bg51 = np.percentile(gray51, 10)
alpha51 = np.clip((gray51 - bg51) / (255.0 - bg51), 0, 1)

# List of 6 target files to process
targets = {
    '微信图片_20260804154245_44_757.jpg': (1785, 1056, alpha51),
    '微信图片_20260804154247_45_757.jpg': (132, 1009, alpha48),
    '微信图片_20260804154248_46_757.jpg': (1878, 1021, alpha51),
    '微信图片_20260804154249_47_757.jpg': (163, 1138, alpha48),
    '微信图片_20260804154250_49_757.jpg': (1878, 1023, alpha51),
    '微信图片_20260804154251_50_757.jpg': (191, 1066, alpha48),
}

dest_folders = [
    backup_dir,
    gw_dir / "衣服",
    gw_dir
]

for filename, (uy, u_right, alpha_an) in targets.items():
    # find source file
    src_file = None
    for folder in dest_folders:
        cand = folder / filename
        if cand.exists():
            src_file = cand
            break
            
    if src_file is None:
        print(f"Error: {filename} not found!")
        continue
        
    img_orig = load_img(src_file)
    h, w, _ = img_orig.shape
    ha, wa = alpha_an.shape
    
    img_mod = img_orig.copy()
    patch = img_mod[uy:uy+ha, u_right:u_right+wa].astype(np.float32)
    for c in range(3):
        patch[:, :, c] = patch[:, :, c] * (1.0 - alpha_an) + 255.0 * alpha_an
    img_mod[uy:uy+ha, u_right:u_right+wa] = np.clip(patch, 0, 255).astype(np.uint8)
    
    # Save to all destination folders so the user sees the updated files regardless of path
    for dest_f in dest_folders:
        dest_p = dest_f / filename
        save_img(dest_p, img_mod)
        print(f"Saved {filename} -> {dest_p}")

print("Processing complete!")
