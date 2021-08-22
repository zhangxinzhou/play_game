import cv2
import numpy as np

o = cv2.imread(r"..\lena.jpg")
# ====================生成高斯金字塔======================
g0 = o
g1 = cv2.pyrDown(g0)
g2 = cv2.pyrDown(g1)
g3 = cv2.pyrDown(g2)
# ====================生成拉普拉斯金字塔======================
l0 = g0 - cv2.pyrUp(g1)
l1 = g1 - cv2.pyrUp(g2)
l2 = g2 - cv2.pyrUp(g3)
# ====================复原 g0======================
rg0 = l0 + cv2.pyrUp(g1)
print("g0.shape", g0.shape)
print("rg0.shape", rg0.shape)
result = rg0 - g0
# 计算result的绝对值，避免求和时负负为正，3+（-3）=0
result = abs(result)
# 计算result的所有元素的和
print("原始图像g0与恢复图像rg0差值的绝对值和：", np.sum(result))
# ====================复原 g1======================
rg1 = l1 + cv2.pyrUp(g2)
print("g1.shape", g1.shape)
print("rg1.shape", rg1.shape)
result = rg1 - g1
print("原始图像g0与恢复图像rg0差值的绝对值和：", np.sum(result))
# ====================复原 g2======================
rg2 = l2 + cv2.pyrUp(g3)
print("g2.shape", g2.shape)
print("rg2.shape", rg2.shape)
result = rg2 - g2
print("原始图像g0与恢复图像rg0差值的绝对值和：", np.sum(result))
