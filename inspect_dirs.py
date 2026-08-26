# -*- coding: utf-8 -*-
from pathlib import Path

base = Path(r"d:\jinyuliangyuan") / "官网素材"
for p in base.iterdir():
    print(repr(p.name), p.is_dir())
    if p.is_dir():
        files = list(p.glob("*.jpg")) + list(p.glob("*.png"))
        print(f"  --> {len(files)} image files")
        for f in files[:5]:
            print(f"      {f.name}")
