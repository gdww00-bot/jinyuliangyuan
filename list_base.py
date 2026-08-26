# -*- coding: utf-8 -*-
from pathlib import Path

base = Path(r"d:\jinyuliangyuan") / "官网素材"
print(f"Base exists: {base.exists()}")
if base.exists():
    for p in base.iterdir():
        print(f"{p.name} (is_dir={p.is_dir()})")
