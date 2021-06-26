import numpy as np
from PyQt5.QtWidgets import QApplication
import os
import win32gui
import sys
import cv2
import time
import datetime
import threading
from concurrent.futures import ThreadPoolExecutor
from getkeys import key_check
from keys_control import key_to_index

show_img = True

# 如果是1920*1080 你可能需要这个,因为大图截图和保存图需要更多时间
# 线程池
threadPool = ThreadPoolExecutor(max_workers=10, thread_name_prefix="thread_")


# 保存图片,FIXME 希望可以找到异步保存的更好方法
def q_pix_map_save(file_name):
    try:
        t0 = time.time()
        thread_name = threading.current_thread().name
        file_p = '\\'.join(file_name.split('\\')[:-1])
        if not os.path.exists(file_p):
            os.mkdir(file_p)
        q_pix_map.save(file_name)
        t1 = time.time()
        cost = int(1000 * (t1 - t0))
        text = 'thread [{}] save file [{}] success!,cost [{}] ms'.format(thread_name, file_name, cost)
        # print(text)
    except Exception as ex:
        print('\033[0;31;31m{}\033[0m'.format(ex))


# QPixmap => CvMat
# method from google/baidu
def qtpixmap_to_cvmat(qtpixmap):
    qimg = qtpixmap.toImage()
    temp_shape = (qimg.height(), qimg.bytesPerLine() * 8 // qimg.depth())
    temp_shape += (4,)
    ptr = qimg.bits()
    ptr.setsize(qimg.byteCount())
    result = np.array(ptr, dtype=np.uint8).reshape(temp_shape)
    result = result[..., :3]

    return result


def get_keys_index(keys_list):
    if 'W' in keys_list and 'A' in keys_list:
        keys = 'key_wa'
    elif 'W' in keys_list and 'D' in keys_list:
        keys = 'key_wd'
    elif 'S' in keys_list and 'A' in keys_list:
        keys = 'key_sa'
    elif 'S' in keys_list and 'D' in keys_list:
        keys = 'key_sd'
    elif 'W' in keys_list:
        keys = 'key_w'
    elif 'S' in keys_list:
        keys = 'key_s'
    elif 'A' in keys_list:
        keys = 'key_a'
    elif 'D' in keys_list:
        keys = 'key_d'
    else:
        keys = 'key_'

    index = key_to_index(keys)
    return index


game_title = r'Grand Theft Auto V'
game_title = '下议院II'
hwnd = win32gui.FindWindow(None, game_title)
if hwnd == 0:
    print('can not find [{}]'.format(game_title))
    print('exit')
    exit()
app = QApplication(sys.argv)
screen = app.primaryScreen()
file_path = r'E:\gta5\collect_data\{}\{}.jpg'

# N秒准备时间
for i in list(range(3))[::-1]:
    print(i + 1)
    time.sleep(1)

while True:
    t0 = time.time()
    q_pix_map = screen.grabWindow(hwnd)
    keys_list = key_check()
    key_index = get_keys_index(keys_list)
    now = datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    file_name = file_path.format(key_index, now)
    # 将保存图片的方法放到线程池中异步执行,把保存图片的时间节省下来,可以保持帧率
    threadPool.submit(q_pix_map_save, file_name)
    t1 = time.time()
    cost = 1000 * (t1 - t0)
    text = 'hwnd : {} , cost : {:.6f} ms'.format(hwnd, cost)
    print(text)
    if show_img:
        mat = qtpixmap_to_cvmat(q_pix_map)
        # FIXME 图片颜色怪异,但如果不写下面代码,则cv2.putText会报错
        mat = cv2.cvtColor(mat, cv2.COLOR_RGB2BGR)
        cv2.putText(mat, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow('window', mat)
        cv2.waitKey(20)

    # T键退出
    if 'T' in keys_list:
        break
