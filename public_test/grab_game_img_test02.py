import time
import cv2
import numpy as np
from PIL import ImageGrab

"""
速度稍慢,即使修改截取面积发现,时间也没多大变化,怀疑是先全屏截图,然后再对这个图片进行裁剪,因此速度无法更上一层楼
"""

w_pos = (10, 10, 500, 350)
g_pos = (w_pos[0] + 8, w_pos[1] + 115, w_pos[2], w_pos[3] - 155)

while True:
    t_total_start = time.time()

    t_grab_start = time.time()
    img = ImageGrab.grab((g_pos[0], g_pos[1], g_pos[2], g_pos[3]))
    t_grab_end = time.time()
    t_grab_cost = (t_grab_end - t_grab_start) * 1000

    mat = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

    t_show_start = time.time()
    cv2.imshow('game', mat)
    cv2.waitKey(1)
    t_show_end = time.time()
    t_show_cost = (t_show_end - t_show_start) * 1000

    t_total_end = time.time()
    t_total_cost = (t_total_end - t_total_start) * 1000
    text = "size: [{}], grab cost: [{:.2f}] ms, show cost: [{:.2f}] ms, total cost: [{:.2f}] ms".format(img.size,
                                                                                                        t_grab_cost,
                                                                                                        t_show_cost,
                                                                                                        t_total_cost)
    print(text)
