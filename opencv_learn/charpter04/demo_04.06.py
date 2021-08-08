import cv2
import numpy as np

# ================测试一下opencv中蓝色的HSV模式值=================
imgBlue = np.zeros([1, 1, 3], dtype=np.uint8)
imgBlue[0, 0, 0] = 255
Blue = imgBlue
BlueHSV = cv2.cvtColor(Blue, cv2.COLOR_BGR2HSV)
print("Blue=\n", Blue)
print("BlueHSV=\n", BlueHSV)

# ================测试一下opencv中绿色的HSV模式值=================
imgGreen = np.zeros([1, 1, 3], dtype=np.uint8)
imgGreen[0, 0, 1] = 255
Green = imgGreen
GreenHSV = cv2.cvtColor(Green, cv2.COLOR_BGR2HSV)
print("Green=\n", Green)
print("GreenHSV=\n", GreenHSV)

# ================测试一下opencv中红色的HSV模式值=================
imgRed = np.zeros([1, 1, 3], dtype=np.uint8)
imgRed[0, 0, 2] = 255
Red = imgRed
RedHSV = cv2.cvtColor(Red, cv2.COLOR_BGR2HSV)
print("Red=\n", Red)
print("RedHSV=\n", RedHSV)

# ================测试一下opencv中黑色的HSV模式值=================
imgBlack = np.ones([1, 1, 3], dtype=np.uint8) * 255
Black = imgBlack
BlackHSV = cv2.cvtColor(Black, cv2.COLOR_BGR2HSV)
print("Black=\n", Black)
print("BlackHSV=\n", BlackHSV)
