from PIL import Image
import pyautogui
import numpy as np

# =====坐标=====
# 屏幕宽度,高度

win_width, win_height = pyautogui.size()
# 图片宽度,高度
img_width, img_height = (1200, 640)
# 基准xy(偏移量 )
base_xy = ((win_width - img_width) / 2, 103)
# 图片区域
img_region = (base_xy[0], base_xy[1], img_width, img_height)

img = pyautogui.screenshot('screen.png', img_region)

ar = np.matrix([
    [0, 1], [1, 0]
])

print(ar)
print(ar.I)
