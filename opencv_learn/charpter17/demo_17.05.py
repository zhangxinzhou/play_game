import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("water_coins.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
ishow = img.copy()
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.zeros((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
sure_bg = cv2.dilate(opening, kernel, iterations=3)
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, fore = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
fore = np.uint8(fore)
ret, markers1 = cv2.connectedComponents(fore)
foreAdy = fore.copy()
unkonw = cv2.subtract(sure_bg, foreAdy)
ret, markers2 = cv2.connectedComponents(foreAdy)
markers2 = markers1 + 1
markers2[unkonw == 255] = 0

plt.subplot(121)
plt.imshow(markers1)
plt.axis("off")

plt.subplot(122)
plt.imshow(markers2)
plt.axis("off")

plt.show()
