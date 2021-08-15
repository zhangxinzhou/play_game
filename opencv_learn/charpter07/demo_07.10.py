import cv2
import numpy as np

o = cv2.imread(r"..\lena.jpg")
kernel = np.ones((9, 9), np.float32) / 81
print(kernel)
r = cv2.filter2D(o, -1, kernel)
cv2.imshow("original", o)
cv2.imshow("result", r)
cv2.waitKey()
cv2.destroyAllWindows()
