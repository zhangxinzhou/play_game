import win32gui
import time
import sys
from PyQt5.QtWidgets import QApplication

game_title = r'chrome://dino/ - Google Chrome'
hwnd = win32gui.FindWindow(None, game_title)
if hwnd == 0:
    print('can not find game [{}]'.format(game_title))
    print('exit!!!')
    exit()

app = QApplication(sys.argv)
screen = app.primaryScreen()
while True:
    t0 = time.time()
    q_pix_map = screen.grabWindow(hwnd)
    t1 = time.time()
    text = "size: [{}], cost: [{}] ms".format(q_pix_map.size(), 1000 * (t1 - t0))
    print(text)
