import numpy as np
import win32gui
import time
import sys
import pyautogui
import cv2
from PyQt5.QtWidgets import QApplication
from public_utils import qpixmap_to_array
from numba import jit

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
@jit()
def action_cv2(image_tmp):
    has_obstacle = np.mean(image_tmp[140:160, 115:155]) > 50
    if has_obstacle:
        return 1
    return 0


@jit()
def game_over(image_tmp):
    return np.mean(image_tmp[100:130, 230:270]) > 80


time.sleep(1)
pyautogui.press('up')
while True:
    t_cycle_start = time.time()

    q_pix_map = screen.grabWindow(0, new_pos[0], new_pos[1], new_pos[2], new_pos[3])

    img = qpixmap_to_array.qpixmap_to_array(q_pix_map)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    action = action_cv2(img)
    if action == 1:
        pyautogui.press('up')

    if True:
        cv2.imshow('img', img)
        cv2.waitKey(1)

    t_cycle_cost = (time.time() - t_cycle_start) * 1000
    if action != 0:
        print("action :[{}], cost : [{:.2f}]".format(action, t_cycle_cost))
    if game_over(img):
        print("game is over!!!")
        exit(0)
