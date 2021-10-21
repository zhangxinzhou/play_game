import numpy as np
import random
import win32gui
import time
import sys
import pyautogui
import cv2
from PyQt5.QtWidgets import QApplication
from public_utils import qpixmap_to_array
from numba import jit

"""
比较满意的截图方式,速度很快,
只是不太明白,为什么用传入handle截的图全是黑的,这里只能传0
"""

game_title = r'chrome://dino/ - Google Chrome'
# 获取window句柄
handle = win32gui.FindWindow(None, game_title)
if handle == 0:
    print("=" * 100)
    print('can not find game [{}]'.format(game_title))
    print('exit!!!')
    print("=" * 100)
    exit()
else:
    print("=" * 100)
    print("success find game [{}], handle = [{}]".format(game_title, handle))
    print("=" * 100)

x0, y0, x1, y1 = win32gui.GetWindowRect(handle)
width = 500
height = 350
new_pos = (x0 + 8, y0 + 115, width, height - 155)

# 不修改坐标,修改游戏窗口尺寸
win32gui.MoveWindow(handle, x0, y0, width, height, False)
# 聚焦游戏窗口
win32gui.SetForegroundWindow(handle)

app = QApplication(sys.argv)
screen = app.primaryScreen()


# 行动,如果前方有障碍物就跳起来
def action_cv2(image_tmp):
    has_obstacle = np.mean(image_tmp[140:160, 115:155]) > 50
    has_bird = np.mean(image_tmp[80:110, 120:160]) > 50
    if has_obstacle:
        pyautogui.press('up')
    elif has_bird:
        pyautogui.press('down')


@jit()
def game_over(image_tmp):
    return np.mean(image_tmp[100:130, 230:270]) > 80


t_total_start = time.time()
pyautogui.press('up')
while True:
    t_cycle_start = time.time()

    t_grab_start = time.time()
    q_pix_map = screen.grabWindow(0, new_pos[0], new_pos[1], new_pos[2], new_pos[3])
    t_grab_cost = (time.time() - t_grab_start) * 1000

    t_transform_start = time.time()
    img = qpixmap_to_array.qpixmap_to_array(q_pix_map)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    action_cv2(img)
    t_transform_cost = (time.time() - t_transform_start) * 1000

    t_show_start = time.time()
    cv2.imshow('img', img)
    cv2.waitKey(1)
    t_show_cost = (time.time() - t_show_start) * 1000

    t_cycle_cost = (time.time() - t_cycle_start) * 1000
    t_total_cost = (time.time() - t_total_start) * 1000
    text = "size=[{}], grab=[{:.2f}]ms, transform=[{:.2f}]ms, show=[{:.4f}]ms, cycle=[{:.2f}]ms, total cost:[{:.2f}]ms".format(
        q_pix_map.size(),
        t_grab_cost,
        t_transform_cost,
        t_show_cost,
        t_cycle_cost,
        t_total_cost)
    print(text)

    if game_over(img):
        print("game is over!!!")
        # exit(0)
