import cv2
import numpy as np

img1 = cv2.imread(r"closing.png")
img2 = cv2.imread(r"closing2.png")
k = np.ones((20, 20), np.uint8)
r1 = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, k)
r2 = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, k)
cv2.imshow("img1", img1)
cv2.imshow("result1", r1)
cv2.imshow("img2", img2)
cv2.imshow("result2", r2)
cv2.waitKey()
cv2.destroyAllWindows()
