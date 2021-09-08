import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"..\lena.jpg", 0)
template = cv2.imread(r"..\lena_eyes.png", 0)
tw, th = template.shape[::-1]
rv = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(rv)
topLeft = maxLoc
bottomRight = (topLeft[0] + tw, topLeft[1] + th)
cv2.rectangle(img, topLeft, bottomRight, 252, 2)

plt.subplot(1, 2, 1)
plt.imshow(rv, cmap='gray')
plt.title('Matching Result')
plt.xticks([])
plt.yticks([])

plt.subplot(1, 2, 2)
plt.imshow(img, cmap='gray')
plt.title('Detected Point')
plt.xticks([])
plt.yticks([])

plt.show()