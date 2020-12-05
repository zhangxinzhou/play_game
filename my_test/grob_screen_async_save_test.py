from PyQt5.QtWidgets import QApplication
import win32gui
import sys
import cv2
import time
import datetime
import threading
from concurrent.futures import ThreadPoolExecutor

# 如果是1920*1080 你可能需要这个,因为大图截图和保存图需要更多时间
# 线程池
threadPool = ThreadPoolExecutor(max_workers=10, thread_name_prefix="thread_")


# 保存图片,FIXME 希望可以找到异步保存的更好方法
def q_pix_map_save(file_name):
    thread_name = threading.current_thread().name
    t0 = time.time()
    q_pix_map.save(file_name)
    t1 = time.time()
    cost = int(1000 * (t1 - t0))
    # print('save file [{}] success!,cost [{}] ms'.format(file_name, cost))


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
    # 将保存图片的方法放到线程池中异步执行,把保存图片的时间节省下来,可以保持帧率
    threadPool.submit(q_pix_map_save, file_name)
    t1 = time.time()
    cost = 1000 * (t1 - t0)
    text = 'hwnd : {} , cost : {:.6f} ms'.format(hwnd, cost)
    print(text)
