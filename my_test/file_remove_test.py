import os

op_path = r'E:\BaiduNetdiskDownload\xiaodidi09.7z.002等多个文件\xiaodidi09'
prefix = 'xiaodidi09 - '

for root, dirs, files in os.walk(op_path):
    for file_name in files:
        if not file_name.startswith(prefix):
            old_file_path = os.path.join(root, file_name)
            new_file_path = os.path.join(op_path, prefix + file_name)
            os.rename(old_file_path, new_file_path)
