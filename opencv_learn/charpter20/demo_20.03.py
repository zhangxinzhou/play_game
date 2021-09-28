import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取样本(特征)图像的值
s = 'image'
num = 100  # 样本总数
row = 240  # 特征图像的行数
col = 240  # 特征图像的列数
a = np.zeros((num, row, col))  # 存储所有样本的数值
print(a.shape)
n = 0  # 存储当前图像的编号
for i in range(0, 10):
    for j in range(1, 11):
        a[n, :, :] = cv2.imread(s + str(i) + '\\' + str(i) + '-' + str(j) + '.bmp', 0)
        n = n + 1
# 提取样本图像的特征
feature = np.zeros((num, round(row / 5), round(col / 5)))  # 用来存储所有样本的特征值
print(feature.shape)  # 看看特征值的形状是什么
print(row)  # 看看row的值,有多少个特征值

for ni in range(0, num):
    for nr in range(0, row):
        for nc in range(0, col):
            if a[ni, nr, nc] == 255:
                feature[ni, int(nr / 5), int(nc / 5)] += 1
f = feature  # 简化变量名称
# 将feature处理为单行形式
train = feature[:, :].reshape(-1, round(row / 5) * round(col / 5)).astype(np.float32)
# print(train.shape)
# 贴标签,要注意,是range(0,100)而非range(0,101)
trainLabels = [int(i / 10) for i in range(0, 101)]
trainLabels = np.asarray(trainLabels)
# print(*trainLabels) # 打印测试看看标签值
## 读取图像值
o = cv2.imread('image\\test\\5.bmp', 0)  # 读取待识别图像
of = np.zeros((round(row / 5), round(col / 5)))  # 用来存储待识别图像的特征值
for nr in range(0, row):
    for nc in range(0, col):
        if o[nr, nc] == 255:
            of[int(nr / 5), int(nc / 5)] += 1

test = of.reshape(-1, round(row / 5) * round(col / 5)).astype(np.float32)
# 调用函数识别图像
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, trainLabels)
ret, result, neighbours, dist = knn.findNearest(test, k=5)
print("当前随机数可以判断为类型:", result)
print("距离当前点最近的五个邻居是:", neighbours)
print("五个最近邻居的距离是:", dist)
