import cv2
import numpy as np

o = cv2.imread(r"..\lena.jpg")
go = o
g1 = cv2.pyrDown(go)
l0 = o - cv2.pyrUp(g1)
r0 = l0 + cv2.pyrUp(g1)
print("o.shape=", o.shape)
print("ro.shape=", r0.shape)
result = r0 - o
# 计算result的绝对值，避免求和时否否为正
result = abs(result)
# 计算result所有元素的和
print("原始图像o与恢复图像r0之差的绝对值和： ", np.sum(result))
