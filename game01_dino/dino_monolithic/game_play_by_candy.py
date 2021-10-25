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
bird_pt1 = (100, 100)
bird_pt2 = (160, 120)
obstacle_pt1 = (100, 120)
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
    obstacle_img = image_tmp[obstacle_pt1[1]:obstacle_pt2[1], obstacle_pt1[0]:obstacle_pt2[0]]
    bird_img = image_tmp[bird_pt1[1]:bird_pt2[1], bird_pt1[0]:bird_pt2[0]]
    obstacle_count = np.count_nonzero(obstacle_img)
    bird_count = np.count_nonzero(bird_img)
    is_obstacle = obstacle_count >= 30
    is_bird = bird_count >= 30 and not is_obstacle

    if is_obstacle:
        return 1
    elif is_bird:
        return 1
    return 0


# 作弊代码
# 无敌
# Runner.instance_.gameOver=function(){}
# 急速
# Runner.instance_.setSpeed(299792458)
# 跳高
# Runner.instance_.tRex.setJumpVelocity(1000000)
def game_over(image_tmp):
    text_tmp = image_tmp[gm_pt1[1]:gm_pt2[1], gm_pt1[0]:gm_pt2[0]]
    text_count = np.count_nonzero(text_tmp)
    return text_count >= 500


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
    cv2.rectangle(candy, bird_pt1, bird_pt2, (255, 255, 255), 1)
    cv2.imshow("candy", candy)
    cv2.imwrite("candy.jpg", candy)
    cv2.waitKey(1)

    t_cycle_cost = (time.time() - t_cycle_start) * 1000
    if action > 0:
        print("action :[{}], cost : [{:.2f}]".format(action, t_cycle_cost))
    if game_over(candy):
        print("game is over!!!")
        exit(0)
