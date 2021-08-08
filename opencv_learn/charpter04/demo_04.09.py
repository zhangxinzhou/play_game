import cv2
import numpy as np

opencv = cv2.imread(r"..\lena.jpg")
hsv = cv2.cvtColor(opencv, cv2.COLOR_BGR2HSV)
cv2.imshow("opencv", opencv)

# ==================指定蓝色值得范围=======================
minBlue = np.array([110, 50, 50])
maxBlue = np.array([130, 255, 255])
# 确定蓝色区域
mask = cv2.bitwise_and(hsv, minBlue, maxBlue)
# 通过掩码控制的按位与运算,锁定蓝色区域
mask = np.zeros([720, 750, 3], dtype=np.uint8)
blue = cv2.bitwise_and(opencv, opencv, mask=mask)
cv2.imshow("blue", blue)

# ==================指定绿色值得范围=======================
minGreen = np.array([50, 50, 50])
maxGreen = np.array([70, 255, 255])
# 确定绿色区域
mask = cv2.inRange(hsv, minGreen, maxGreen)
mask = np.zeros([720, 750, 3], dtype=np.uint8)
# 通过掩码控制的按位与运算,锁定绿色区域
green = cv2.bitwise_and(opencv, opencv, mask=mask)
cv2.imshow("green", green)

# ==================指定红色值得范围=======================
minRed = np.array([0, 50, 50])
maxRed = np.array([30, 255, 255])
# 确定红色区域
mask = cv2.inRange(hsv, minRed, maxRed)
mask = np.zeros([720, 750, 3], dtype=np.uint8)
# 通过掩码控制的按位与运算,锁定红色区域
red = cv2.bitwise_and(opencv, opencv, mask=mask)
cv2.imshow("red", red)

cv2.waitKey()
cv2.destroyAllWindows()
