import random
import numpy as np

a = [[1], [2], [3]]
b = [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]
c = [1, 2, 3, 4]

print(np.array(a).shape)
print(np.array(b).shape)
print(np.array(c).shape)

d = (None, 4)
print(d)

a = [1,2,3]
a = np.argmax(a)
print(a)


import uuid

uid = uuid.uuid4()
print(uid)
print(uid.hex)
print(type(uid))