import cv2
import numpy as np

# -----------------------读取原始图像--------------------------
o = cv2.imread("cc.bmp")
cv2.imshow("original", o)

# 读取轮廓
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# 绘制空心轮廓
mask1 = np.zeros(gray.shape, np.uint8)
cv2.drawContours(mask1, [cnt], 0, 255, 2)
pixelpoints1 = cv2.findNonZero(mask1)
print("pixelpoints1.shape=", pixelpoints1)
print("pixelpoints=\n", pixelpoints1)
cv2.imshow("mask1", mask1)

# 绘制实心轮廓
mask2 = np.zeros(gray.shape, np.uint8)
cv2.drawContours(mask2, [cnt], 0, 255, -1)
pixelpoints2 = cv2.findNonZero(mask2)
print("pixelpoints2.shape=", pixelpoints2.shape)
print("pixelpoints2=\n", pixelpoints2)
cv2.imshow("mask2", mask2)

# 释放窗口
cv2.waitKey()
cv2.destroyAllWindows()
