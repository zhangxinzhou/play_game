import numpy as np

am = np.array(
    [
        [3, 6, 8, 77, 66],
        [1, 2, 88, 3, 98],
        [11, 2, 67, 5, 2]
    ]
)

b = np.where(am > 5)
print(type(b))
print(b)

print("==========")
for i in zip(b):
    print(i)

print("==========")
print(*b)
print("==========")
for i in zip(*b):
    print(i)
