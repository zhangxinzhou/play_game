import os
import shutil

path = r'E:\BaiduNetdiskDownload\党史'

for root, dirs, files in os.walk(path):
    print(f"root={root},dirs={dirs},files={files}")
    for file in files:
        src = os.path.join(root, file)
        dst = os.path.join(path, file)
        print(f"********************** file={src}")
        if not os.path.exists(dst):
            print(f"start move {dst}")
            shutil.move(src, path)
