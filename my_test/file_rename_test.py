import os

folder_path = r'F:\cosplay\RiaKurumi'
l = os.listdir(folder_path)
for i in l:
    old_name = i
    if not (old_name.startswith("RiaKurumi") or old_name.startswith("ria")):
        arr = old_name.split("-")
        new_name = arr[1] + "-" + arr[0] + "-" + arr[2]
        old_file_path = os.path.join(folder_path, old_name)
        new_file_path = os.path.join(folder_path, new_name)
        print("=" * 100)
        print(old_name)
        print(new_name)
        # os.rename(old_file_path, new_file_path)
