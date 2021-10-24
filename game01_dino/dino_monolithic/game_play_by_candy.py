import numpy as np
import win32gui
import time
import sys
import pyautogui
import cv2
from PyQt5.QtWidgets import QApplication
from public_utils import qpixmap_to_array

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
obstacle_pt1 = (100, 100)
obstacle_pt2 = (150, 150)
gm_pt1 = (135, 55)
gm_pt2 = (365, 75)

# 不修改坐标,修改游戏窗口尺寸
win32gui.MoveWindow(handle, x0, y0, width, height, False)
# 聚焦游戏窗口
win32gui.SetForegroundWindow(handle)

app = QApplication(sys.argv)
screen = app.primaryScreen()


# 行动,如果前方有障碍物就跳起来
def action_cv2(image_tmp):
    tmp = image_tmp[obstacle_pt1[1]:obstacle_pt2[1], obstacle_pt1[0]:obstacle_pt2[0]]
    xy_loc = np.where(tmp == 255)
    x_loc = xy_loc[0]
    y_loc = xy_loc[1]
    if len(x_loc) == 0:
        return 0
    x_median = np.median(x_loc)
    y_median = np.median(y_loc)
    xy_median = np.median(xy_loc)

    median_limit = np.abs(0.5 * (obstacle_pt2[1] - obstacle_pt1[1])) - 10
    print(x_median, y_median, xy_median, median_limit)

    if xy_median >= median_limit:
        return 1
    elif xy_median < median_limit:
        return 2
    return 0


# 作弊代码
# 无敌
# Runner.instance_.gameOver=function(){}
# 急速
# Runner.instance_.setSpeed(299792458)
# 跳高
# Runner.instance_.tRex.setJumpVelocity(1000000)
def game_over(image_tmp):
    tmp = image_tmp[gm_pt1[1]:gm_pt2[1], gm_pt1[0]:gm_pt2[0]]
    tmp = np.where(tmp >= 255)
    count = len(tmp[0])
    return count >= 500


time.sleep(1)
pyautogui.press('up')
while True:
    t_cycle_start = time.time()

    q_pix_map = screen.grabWindow(0, new_pos[0], new_pos[1], new_pos[2], new_pos[3])

    img = qpixmap_to_array.qpixmap_to_array(q_pix_map)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    candy = cv2.Canny(gray, 100, 200)
    action = action_cv2(candy)
    if action == 1:
        pyautogui.press('up')
    elif action == 2:
        pyautogui.press('down')

    # cv2.imshow('img', img)
    cv2.rectangle(candy, gm_pt1, gm_pt2, (255, 255, 255), 1)
    cv2.rectangle(candy, obstacle_pt1, obstacle_pt2, (255, 255, 255), 1)
    cv2.imshow("candy", candy)
    cv2.imwrite("candy.jpg", candy)
    cv2.waitKey(1)

    t_cycle_cost = (time.time() - t_cycle_start) * 1000
    if action > 0:
        print("action :[{}], cost : [{:.2f}]".format(action, t_cycle_cost))
    if game_over(candy):
        print("game is over!!!")
        exit(0)
