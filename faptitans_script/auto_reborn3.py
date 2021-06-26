# encoding=utf-8

import pyautogui
from PIL import Image

# 相关常量
# 屏幕偏移量
window_offset = 1920

# 截取游戏画面图
screen_region = (360, 100, 1200, 640)
x = pyautogui.screenshot('screen.png', screen_region)
print(type(x))
print(x)
print(x.getpixel((100, 200)))


def position_match_color(position, expected_color, tolerance=10):
    img = pyautogui.screenshot(region=screen_region)
    pixel = img.getpixel(position)
    r, g, b = pixel[:3]
    ex_r, ex_g, ex_b = expected_color[:3]
    return (abs(r - ex_r) <= tolerance) and (abs(g - ex_g) <= tolerance) and (abs(b - ex_b) <= tolerance)


position = (100, 200)
expected_color = (129, 171, 182)
a = position_match_color(position, expected_color)
print(a)
