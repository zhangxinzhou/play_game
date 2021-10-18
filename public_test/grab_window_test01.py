import random
import win32gui
import win32con
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

w_pos = (10, 10, 500, 350)
g_pos = (w_pos[0] + 8, w_pos[1] + 115, w_pos[2], w_pos[3]-155)

# 修改游戏窗口尺寸
win32gui.SetWindowPos(handle, win32con.HWND_TOPMOST, w_pos[0], w_pos[1], w_pos[2], w_pos[3], win32con.SWP_SHOWWINDOW)
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
t_start = time.time()
img_name = 'buff.jpg'
while True:
    t_total_start = time.time()

    t_grab_start = time.time()
    q_pix_map = screen.grabWindow(0, g_pos[0], g_pos[1], g_pos[2], g_pos[3])
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

    cv2.imshow('mat1', mat1)
    cv2.imshow('mat2', mat2)
    cv2.waitKey(1)

    t_total_end = time.time()
    t_total_cost = (t_total_end - t_total_start) * 1000
    text = "size: [{}], grab cost: [{:.4f}] ms, load cost: [{:.4f}] ms, transform cost: [{:.4f}] ms, total cost:[{:.4f}] ms".format(
        q_pix_map.size(),
        t_grab_cost,
        t_load_cost,
        t_transform_cost,
        t_total_cost)
    print(text)
