import numpy as np

# --------------------生成一个元素都是零值的数组------------------------
a = np.zeros((5, 5), dtype=np.uint8)
# --------------------随机将其中10个位置上的数值设置为1------------------------
# ---times 控制次数
# ---i,j时随机生成的行,列位置
# ---a[i,j]=1,将随机挑选出来的位置上的值设置为1
for times in range(10):
    i = np.random.randint(0, 5)
    j = np.random.randint(0, 5)
    a[i, j] = 1

# 打印数组a,观察数组a内值得情况
print("a=\n", a)
# ----查找数组a内非零值得位置信息------
loc = np.transpose(np.nonzero(a))
# ----输出数组a内非零值的位置信息------
print(np.nonzero(a))
print("a内非零值得位置:\n", loc)
