from PyQt5.QtWidgets import QApplication
import win32gui
import sys
import cv2
import time
import datetime

# 如果图片不大,那么截图和保存图片消耗不了多少时间,就可以直接用这个方法
game_title = r'Grand Theft Auto V'
hwnd = win32gui.FindWindow(None, game_title)
if hwnd == 0:
    print('can not find [{}]'.format(game_title))
    print('exit')
    # exit()
app = QApplication(sys.argv)
screen = app.primaryScreen()
file_path = r'E:\gta5\collect_data\{}.jpg'
while True:
    t0 = time.time()
    q_pix_map = screen.grabWindow(hwnd)
    now = datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    file_name = file_path.format(now)
    q_pix_map.save(file_name)
    t1 = time.time()
    cost = 1000 * (t1 - t0)
    text = 'hwnd : {} , cost : {:.6f} ms'.format(hwnd, cost)
    print(text)
    mat = cv2.imread(file_name)
    cv2.putText(mat, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow('window', mat)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
