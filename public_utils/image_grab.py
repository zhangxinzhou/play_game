import time
import cv2
import numpy as np
from PIL import ImageGrab

t_start = time.time()
while True:
    t_tmp = time.time()
    cost = t_tmp - t_start
    t_start = t_tmp

    img = ImageGrab.grab((0, 0, 500, 300))
    mat = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    cv2.imshow('game', mat)
    cv2.waitKey(1)

    text = "size: [{}], cost: [{}] ms".format(img.size, 1000 * cost)
    print(text)
