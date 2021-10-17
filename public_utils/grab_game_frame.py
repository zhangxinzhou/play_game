import random
import win32gui
import win32con
import time
import sys
import pyautogui
from PyQt5.QtWidgets import QApplication

game_title = r'chrome://dino/ - Google Chrome'
# 获取window句柄
handle = win32gui.FindWindow(None, game_title)
if handle == 0:
    print('can not find game [{}]'.format(game_title))
    print('exit!!!')
    exit()

# 修改游戏窗口尺寸l
win32gui.SetWindowPos(handle, win32con.HWND_TOPMOST, -800, 0, 500, 350, win32con.SWP_SHOWWINDOW)
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
while True:
    t_tmp = time.time()
    cost = t_tmp - t_start
    t_start = t_tmp

    random_action()

    q_pix_map = screen.grabWindow(handle)
    text = "size: [{}], cost: [{}] ms".format(q_pix_map.size(), 1000 * cost)
    print(text)
