import cv2
import numpy as np

a = cv2.imread(r"..\cat.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("original", a)
face = np.random.randint(0, 256, size=(180, 100, 3))
a[220:400, 250:350] = face
cv2.imshow("result", a)
cv2.waitKey()
