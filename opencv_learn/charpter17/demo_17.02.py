import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("water_coins.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(gray, cv2.COLOR_BGR2RGB)
ishow = img.copy()
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, fore = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

plt.subplot(131)
plt.imshow(img)
plt.axis("off")

plt.subplot(132)
plt.imshow(dist_transform)
plt.axis("off")

plt.subplot(133)
plt.imshow(fore)
plt.axis("off")

plt.show()
