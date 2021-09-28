import cv2
import numpy as np
import matplotlib.pyplot as plt

# 第一步 准备数据
# 表现为A级的员工的笔试,面试成绩
a = np.random.randint(95, 100, (20, 2)).astype(np.float32)
# 表现为B级的员工的表示,面试成绩
b = np.random.randint(90, 95, (20, 2)).astype(np.float32)
# 合并数据
data = np.vstack((a, b))
data = np.array(data, dtype='float32')
# 第二步 建立分组标签, 代表A级,1代表B级
# aLabel 对应着A标签,为类型0-等级A
aLabel = np.zeros((20, 1))
# bLabel 对应着B标签,为类型1-等级B
bLabel = np.ones((20, 1))
# 合并标签
label = np.vstack((aLabel, bLabel))
label = np.array(label, dtype='int32')

print("=" * 20, "data", "=" * 20)
print(data.shape)
print(data)
print("=" * 20, "label", "=" * 20)
print(label.shape)
print(label)
# 第三步, 训练
# 用ml机器学习模块 SVM_create() 创建svm
svm = cv2.ml.SVM_create()
# 属性设置,直接采用默认值即可
# svm.setType(cv2.ml.SVM_C_SVC)  # svm type
# svm.setKernel(cv2.ml.SVM_LINEAR) # line
# svm.setC(0.01)
# 训练

result = svm.train(data, cv2.ml.ROW_SAMPLE, label)
# 第四步,预测
# 生成两个随机的笔试成绩和面试成绩数据对
test = np.vstack(([98, 90], [90, 99]))
test = np.array(test, dtype='float32')
# 预测
(p1, p2) = svm.predict(test)
# 第五步 观察结果
# 可视化
plt.scatter(a[:, 0], a[:, 1], 80, 'g', 'o')
plt.scatter(b[:, 0], b[:, 1], 80, 'b', 's')
plt.scatter(test[:, 0], test[:, 1], 80, 'r', '*')
plt.show()
# 打印原始测试数据test,预测结果
print("=" * 20, "predict", "=" * 20)
print(test)
print(p2)
