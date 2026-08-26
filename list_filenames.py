import os

folder = r'd:\jinyuliangyuan\官网素材\衣服'
print('--- Files in 官网素材/衣服 ---')
for f in sorted(os.listdir(folder)):
    print(repr(f))

backup_folder = r'd:\jinyuliangyuan\官网素材\衣服_backup'
print('\n--- Files in 官网素材/衣服_backup ---')
for f in sorted(os.listdir(backup_folder)):
    print(repr(f))
