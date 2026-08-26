# -*- coding: utf-8 -*-
import os
from pathlib import Path

folder = Path(r"d:\jinyuliangyuan") / "官网素材" / "衣服"
print(f"Folder exists: {folder.exists()}")
if folder.exists():
    for p in sorted(folder.glob("*.jpg")):
        print(p.name)

backup = Path(r"d:\jinyuliangyuan") / "官网素材" / "衣服_backup"
print(f"\nBackup exists: {backup.exists()}")
if backup.exists():
    for p in sorted(backup.glob("*.jpg")):
        print(p.name)
