import random
import win32gui
import win32con
import time
import sys
import pyautogui
import cv2
from PyQt5.QtWidgets import QApplication
from public_utils import qpixmap_to_array

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


# 随机行动测试
def random_action():
    action = random.randint(0, 2)
    print(action)
    if action == 1:
        pyautogui.press('up')
    elif action == 2:
        pyautogui.press('down')


# 截图
img_name = 'buff.jpg'
while True:
    t_total_start = time.time()

    t_grab_start = time.time()
    q_pix_map = screen.grabWindow(0, new_pos[0], new_pos[1], new_pos[2], new_pos[3])
    t_grab_end = time.time()
    t_grab_cost = (t_grab_end - t_grab_start) * 1000

    t_load_start = time.time()
    q_pix_map.save('buff.jpg')
    mat1 = cv2.imread(img_name)
    t_load_end = time.time()
    t_load_cost = (t_load_end - t_load_start) * 1000

    t_transform_start = time.time()
    mat2 = qpixmap_to_array.qpixmap_to_array(q_pix_map)
    t_transform_end = time.time()
    t_transform_cost = (t_transform_end - t_transform_start) * 1000

    t_show_start = time.time()
    cv2.imshow('mat1', mat1)
    cv2.imshow('mat2', mat2)
    cv2.waitKey(1)
    t_show_end = time.time()
    t_show_cost = (t_show_end - t_show_start) * 1000

    t_total_end = time.time()
    t_total_cost = (t_total_end - t_total_start) * 1000
    text = "size: [{}], grab cost: [{:.4f}] ms, load cost: [{:.4f}] ms, transform cost: [{:.4f}] ms, show cost:[{:.4f}] ms, total cost:[{:.4f}] ms".format(
        q_pix_map.size(),
        t_grab_cost,
        t_load_cost,
        t_transform_cost,
        t_show_cost,
        t_total_cost)
    print(text)
