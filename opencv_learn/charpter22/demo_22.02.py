import cv2
import numpy as np
import matplotlib.pyplot as plt

# 随机生成两组数值
# xiaomi组,长和宽都在[0,20]内
xiaomi = np.random.randint(0, 20, (30, 2))
# dami组,长和宽的大小都在[40,60]
dami = np.random.randint(40, 60, (30, 2))
# 组合数据
MI = np.vstack((xiaomi, dami))
print(MI)
print(np.hstack((xiaomi, dami)))
# 装换为float32类型
MI = np.float32(MI)
# 调用kmeans模块
# 设置参数criteria值
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# 调用kmeans函数
ret, label, center = cv2.kmeans(MI, 2, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
# 打印返回值
# print(ret)
# print(label)
# print(center)
# 根据kmeans的处理结果,将数据分类,分为XM和DM两大类
XM = MI[label.ravel() == 0]
DM = MI[label.ravel() == 1]
print("=" * 50)
print(label)
print("=" * 50)
print(label.ravel())
# 绘制分类结果数据及中心点
plt.scatter(XM[:, 0], XM[:, 1], c='g', marker='s')
plt.scatter(DM[:, 0], DM[:, 1], c='g', marker='s')
plt.scatter(center[0, 0], center[0, 1], s=200, c='b', marker='o')
plt.scatter(center[1, 0], center[1, 1], s=200, c='b', marker='s')
plt.xlabel('Height')
plt.ylabel('Width')
plt.show()
