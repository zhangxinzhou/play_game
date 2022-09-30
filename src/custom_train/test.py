# from src.custom_env.MyEnv1 import MyEnv1
#
# env = MyEnv1()
# env.reset()
import sys

l = sys.path
for i in l:
    print(i)

import src.custom_env.MyEnv1 as xxx
