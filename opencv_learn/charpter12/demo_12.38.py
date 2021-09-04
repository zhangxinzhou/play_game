import cv2
import numpy as np

o = cv2.imread(r"ct.jpg")
cv2.imshow("original", o)
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for index, i in enumerate(contours):
    cnt = i
    tmp = np.count_nonzero(cnt)
    if tmp <= 1000:
        continue
    # 使用掩码获取感兴趣区域的最大值
    # minMaxLoc对立对象为灰度图像,如果要处理彩色图像,需要提取各个通道图像分别计算
    mask = np.zeros(gray.shape, np.uint8)
    mask = cv2.drawContours(mask, [cnt], -1, 255, -1)
    print("gray=\n", gray)
    print("mask=\n", mask)
    meanVal = cv2.mean(o, mask=mask)
    print("meanVal=", meanVal)
    meanValWithoutMask = cv2.mean(o)
    print("meanValWithoutMask=", meanValWithoutMask)
    # 使用掩膜获取感兴趣区域并显示
    masko = np.zeros(o.shape, np.uint8)
    masko = cv2.drawContours(masko, [cnt], -1, (255, 255, 255), -1)
    loc = cv2.bitwise_and(o, masko)
    cv2.imshow("masko" + str(index), masko)
    # 显示灰度结果
    loc = cv2.bitwise_and(gray, mask)
    cv2.imshow("mask" + str(index), loc)
# 释放窗口
cv2.waitKey()
cv2.destroyAllWindows()
