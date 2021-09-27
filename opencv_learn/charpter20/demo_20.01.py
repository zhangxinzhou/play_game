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
##### 计算当前待识别图像的特征值
o = cv2.imread('image\\test\\5.bmp', 0)  # 读取待识别图像
## 读取图像值
of = np.zeros((round(row / 5), round(col / 5)))  # 存储待识别图像的特征值
for nr in range(0, row):
    for nc in range(0, col):
        if o[nr, nc] == 255:
            of[int(nr / 5), int(nc / 5)] += 1
### 开始计算,识别数字,计算最邻近的若干个数字是多少,判断结果
d = np.zeros(100)
for i in range(0, 100):
    d[i] = np.sum((of - f[i, :, :]) * (of - f[i, :, :]))
print(d)
d = d.tolist()
temp = []
Inf = max(d)
print(Inf)
k = 7
for i in range(k):
    temp.append(d.index(min(d)))
    d[d.index(min(d))] = Inf
print(temp)  # 看看都被识别为那些特征值
temp = [i / 10 for i in temp]
# 也可以返回去处理为array,使用函数处理
temp = np.array(temp)
temp = np.trunc(temp / 10)
print(temp)
# 数组r用来存储结果,r[0]表示k近邻中"0"的个数,r[n]表示k近邻中"n"的个数
r = np.zeros(10)
for i in temp:
    r[int(i)] += 1
print(r)
print('当前的数字可能为:' + str(np.argmax(r)))
