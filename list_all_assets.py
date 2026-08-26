# -*- coding: utf-8 -*-
from pathlib import Path

for sub in [Path(r"d:\jinyuliangyuan\素材"), Path(r"d:\jinyuliangyuan\素材\模特图"), Path(r"d:\jinyuliangyuan\官网素材")]:
    if sub.exists():
        print(f"=== {sub} ===")
        for f in sub.iterdir():
            if f.is_file() and f.suffix.lower() in ['.jpg', '.png']:
                print(f"  {f.name} ({f.stat().st_size/1024/1024:.2f} MB)")
