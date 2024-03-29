import cv2
import numpy as np

img = np.random.randint(0, 256, size=[3, 4, 3], dtype=np.uint8)
rst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("img=\n", img)
print("rst=\n", rst)
print(img[1, 0, 0], img[1, 0, 1], img[1, 0, 2])
print("像素点(1,0)直接计算得到的值=", img[1, 0, 0] * 0.114 + img[1, 0, 1] * 0.587 + img[1, 0, 2] * 0.299)
print("像素点(1,0)使用公式cv2.cvtColor()转换值=", rst[1, 0])
