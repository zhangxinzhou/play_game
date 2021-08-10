import cv2
import numpy as np

img = cv2.imread(r"..\lena.jpg")
height, width = img.shape[:2]
M = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 0.6)
rotate = cv2.warpAffine(img, M, (width, height))
cv2.imshow("original", img)
cv2.imshow("rotation", rotate)
cv2.waitKey()
cv2.destroyAllWindows()
