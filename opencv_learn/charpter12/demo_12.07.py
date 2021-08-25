import cv2
import numpy as np

# ------------------读取及显示原始图像-------------------
o = cv2.imread("contours0.bmp")
cv2.imshow("original", o)
# ------------------获取轮廓-------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# ------------------计算个轮廓的长度之和，平均长度-------------------
n = len(contours)  # 获取轮廓的个数
cntLen = []  # 获取各轮廓的长度
for i in range(n):
    cntLen.append(cv2.arcLength(contours[i], True))
    print("第" + str(i) + "个轮廓的长度：%d" % cntLen[i])
cntLenSum = np.sum(cntLen)  # 各轮廓的长度之和
cntLenAvr = np.mean(cntLen)  # 各轮廓的平均值
print("轮廓的总长度为：%d" % cntLenSum)
print("轮廓的平均长度为：%d" % cntLenAvr)
# ------------------显示长度超过平均值的轮廓-------------------
contoursImg = []
for i in range(n):
    temp = np.zeros(o.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, (255, 255, 255), 3)
    if cv2.arcLength(contours[i], True) > cntLenAvr:
        cv2.imshow("contours[" + str(i) + "]", contoursImg[i])

print(type(contours[0]))
print(contours[0].shape)
print(contours[0])
cv2.waitKey()
cv2.destroyAllWindows()
