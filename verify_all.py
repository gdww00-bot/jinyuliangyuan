# -*- coding: utf-8 -*-
import cv2
import numpy as np
from pathlib import Path

def load_img(path):
    return cv2.imdecode(np.fromfile(str(path), dtype=np.uint8), cv2.IMREAD_COLOR)

backup_dir = Path(r"d:\jinyuliangyuan\官网素材\衣服_backup")
files = [
    '微信图片_20260804154245_44_757.jpg',
    '微信图片_20260804154247_45_757.jpg',
    '微信图片_20260804154248_46_757.jpg',
    '微信图片_20260804154249_47_757.jpg',
    '微信图片_20260804154250_49_757.jpg',
    '微信图片_20260804154251_50_757.jpg'
]

for f in files:
    path = backup_dir / f
    img = load_img(path)
    h, w, _ = img.shape
    print(f"{f}: {w}x{h} OK")

print("All 6 files verified successfully in 衣服_backup!")
