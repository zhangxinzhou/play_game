import sys

# sys.path.append(r'D:\repository\git\game_explorer')

# print(sys.path)
for i in sys.path:
    print(i)
print(type(sys.path))

from src.custom_env.MyEnv2 import MyEnv2

a = MyEnv2()
