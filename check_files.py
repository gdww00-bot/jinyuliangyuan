import os
import cv2
import numpy as np

def load_img(path):
    return cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR)

folder = r'd:\jinyuliangyuan\官网素材\衣服'

six_files = [
    '微信图片_20260804154245_44_757.jpg',
    '微信图片_20260804154247_45_757.jpg',
    '微信图片_20260804154248_46_757.jpg',
    '微信图片_20260804154249_47_757.jpg',
    '微信图片_20260804154250_49_757.jpg',
    '微信图片_20260804154251_50_757.jpg'
]

for f in six_files:
    path = os.path.join(folder, f)
    if os.path.exists(path):
        img = load_img(path)
        h, w, _ = img.shape
        print(f'{f}: {w}x{h}, exists=True')
    else:
        print(f'{f}: NOT FOUND')
