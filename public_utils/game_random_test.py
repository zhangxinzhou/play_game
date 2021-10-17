import random
import win32gui
import win32con
import time
import sys
import pyautogui
import cv2
from PyQt5.QtWidgets import QApplication
import qpixmap_to_array

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

# 修改游戏窗口尺寸
win32gui.SetWindowPos(handle, win32con.HWND_TOPMOST, 10, 10, 500, 350, win32con.SWP_SHOWWINDOW)
# 聚焦游戏窗口
win32gui.SetForegroundWindow(handle)

app = QApplication(sys.argv)
screen = app.primaryScreen()


# 随机行动测试
def random_action():
    time.sleep(0.1)
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
    t_tmp = time.time()
    cost = t_tmp - t_start
    t_start = t_tmp

    # random_action()

    q_pix_map = screen.grabWindow(393802)
    q_pix_map.save('buff.jpg')

    mat1 = cv2.imread(img_name)
    mat2 = qpixmap_to_array.qpixmap_to_array(q_pix_map)
    print(mat1.shape)
    cv2.imshow('mat1', mat1)
    cv2.imshow('mat2', mat2)
    cv2.waitKey(1)
    text = "size: [{}], cost: [{}] ms".format(q_pix_map.size(), 1000 * cost)
    print(text)
